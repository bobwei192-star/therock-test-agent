# Help needed: GCN asm question

- **Issue #:** 1487
- **State:** closed
- **Created:** 2021-05-31T12:20:57Z
- **Updated:** 2021-06-02T20:06:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/1487

Hi, I see a strange situation where this bit of code works correctly
```
	#SUB
	v_sub_co_u32_e32  v6, vcc, v0, v2
	v_subb_co_u32_e32 v7, vcc, v1, v3, vcc
	s_mov_b64_e32 s[0:1], vcc
	v_addc_co_u32 v6, vcc, 0, v6, vcc
	s_orn2_b64_e32 vcc, vcc, s[0:1]
	v_addc_co_u32_e32 v7, vcc, -1, v7, vcc
```
But the below fails non-deterministically (i.e. after a while, and not always at the same spot)
```
	#SUB BAD
	v_sub_co_u32_e32  v6, vcc, v0, v2
	v_subb_co_u32_e32 v7, vcc, v1, v3, vcc
	v_addc_co_u32 v6, s[0:1], 0, v6, vcc
	s_orn2_b64_e32 vcc, s[0:1], vcc
	v_addc_co_u32_e32 v7, vcc, -1, v7, vcc
```
In my oppinion the two pieces should be equivalent. I'm running this on RadeonVII. I checked multiple times the ISA docs about "manually inserted wait states", and it does not appear I have any missing wait-states.

These were both generated using this function:
```
typedef uint u32;
typedef ulong u64;
u32  U32(u32 x)   { return x; }
#define OVL __attribute__((overloadable))
u64 OVL U64(u64 x)   { return x; }
u64 OVL U64(u32 a, u32 b) { return as_ulong((uint2)(a, b)); }

u64 sub(u64 a, u64 b) {
  u32 c, d;
  u64 stmp;
#if USE_BAD
  __asm("#SUB BAD\n\t"
        "v_sub_co_u32_e32  %[c], vcc, %[aLo], %[bLo]\n\t"
	"v_subb_co_u32_e32 %[d], vcc, %[aHi], %[bHi], vcc\n\t"
        "v_addc_co_u32 %[c], %[stmp], 0, %[c], vcc\n\t"
        "s_orn2_b64_e32 vcc, %[stmp], vcc\n\t"
        "v_addc_co_u32_e32 %[d], vcc, -1, %[d], vcc"        
        : [c] "=&v"(c), [d] "=v"(d), [stmp] "=&s"(stmp)
        : [aLo] "v"(U32(a)), [aHi] "v"(U32(a>>32)), [bLo] "v"(U32(b)), [bHi] "v"(U32(b>>32))
        : "vcc");
#else
  __asm("#SUB\n\t"
        "v_sub_co_u32_e32  %[c], vcc, %[aLo], %[bLo]\n\t"
	"v_subb_co_u32_e32 %[d], vcc, %[aHi], %[bHi], vcc\n\t"
        "s_mov_b64_e32 %[stmp], vcc\n\t"
        "v_addc_co_u32 %[c], vcc, 0, %[c], vcc\n\t"
        "s_orn2_b64_e32 vcc, vcc, %[stmp]\n\t"
        "v_addc_co_u32_e32 %[d], vcc, -1, %[d], vcc"        
        : [c] "=&v"(c), [d] "=v"(d), [stmp] "=&s"(stmp)
        : [aLo] "v"(U32(a)), [aHi] "v"(U32(a>>32)), [bLo] "v"(U32(b)), [bHi] "v"(U32(b>>32))
        : "vcc");
#endif

  return U64(c, d);
}
```
I'm using ROCm 3.3.0, targeting Radeon VII. Should I suspect a bug in the compiler? A bug in the HW (such as a needed wait-state that's not in the docs)? or am I doing something wrong? thanks!
