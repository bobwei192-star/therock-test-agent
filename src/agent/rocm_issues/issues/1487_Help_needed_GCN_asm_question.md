# Help needed: GCN asm question

> **Issue #1487**
> **状态**: closed
> **创建时间**: 2021-05-31T12:20:57Z
> **更新时间**: 2021-06-02T20:06:42Z
> **关闭时间**: 2021-06-02T12:52:41Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1487

## 描述

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


---

## 评论 (18 条)

### 评论 #1 — preda (2021-05-31T12:36:24Z)

(the source in its entirety is here:
https://github.com/preda/gpuowl/blob/d8c6b122122dbab7527d6a23f7ef915642519fd2/gpuowl.cl#L146
)

---

### 评论 #2 — b-sumner (2021-05-31T15:16:28Z)

Would you describe what "fails" means?  The while application, or are you testing just that function and getting incorrect results?

---

### 评论 #3 — seesturm (2021-05-31T15:49:09Z)

I guess the problem is with
`v_addc_co_u32 v6, s[0:1], 0, v6, vcc`
which accesses two scalar operands (s[0:1] and VCC) with a vector instruction. According to "6.2.1. Instruction Inputs"

> At most one SGPR can be read per instruction, ...

"3.9. Vector Compares: VCC and VCCZ" states

> VCC physically resides in the SGPR register file, so when an instruction
sources VCC, that counts against the limit on the total number of SGPRs that
can be sourced for a given instruction. VCC physically resides in the highest
two user SGPRs.

---

### 评论 #4 — preda (2021-05-31T18:01:28Z)

> Would you describe what "fails" means? The while application, or are you testing just that function and getting incorrect results?

@b-sumner I am testing the whole application that uses this function. The function does not fail every time, but only from time to time. When using the "good" version everything works reliably correctly, when swapping with the "bad" version it fails after a [long] while.


---

### 评论 #5 — seesturm (2021-05-31T18:02:05Z)

I was wrong. s[0:1] is a destination so it should not count as "read register".

---

### 评论 #6 — preda (2021-05-31T18:07:38Z)

> I was wrong. s[0:1] is a destination so it should not count as "read register".

Yes. Also, I'd expect the assembler to detect the not-allowed situations (like reading too many SGPRs) and report an error instead of accepting it to fail at runtime.


---

### 评论 #7 — arsenm (2021-06-01T16:25:58Z)

The best advice for inline asm I can give is to never use it. It really does more harm than good and I 1000% advise against ever using it. It's only for the most desperate situations. Why are you trying to use it for this? This looks like a basic sub with overflow.

I do see you are missing an implicit exec read on your constraints which may or may not be relevant

---

### 评论 #8 — preda (2021-06-01T17:04:34Z)

> The best advice for inline asm I can give is to never use it. It really does more harm than good and I 1000% advise against ever using it. It's only for the most desperate situations. Why are you trying to use it for this? This looks like a basic sub with overflow.
> 
> I do see you are missing an implicit exec read on your constraints which may or may not be relevant

@arsenm could you please explain me a bit more about the missing exec read constraint? (what is it, why do I need it?)

That code is not a "basic sub with overflow". Instead, it implements this C function:
```
u64 sub(u64 a, u64 b) {
  return (a >= b) ? a - b : (a - b - 0xffffffff);
}
```
which LLVM compiles to:
```
	v_sub_co_u32_e32 v6, vcc, v0, v2
	v_subb_co_u32_e32 v7, vcc, v1, v3, vcc
	v_add_co_u32_e32 v8, vcc, 1, v6
	v_addc_co_u32_e32 v9, vcc, -1, v7, vcc
	v_cmp_lt_u64_e32 vcc, v[0:1], v[2:3]
	v_cndmask_b32_e32 v1, v7, v9, vcc
	v_cndmask_b32_e32 v0, v6, v8, vcc
```

please compare with the functionally-equivalent:
```
	v_sub_co_u32_e32  v6, vcc, v0, v2
	v_subb_co_u32_e32 v7, vcc, v1, v3, vcc
	s_mov_b64_e32 s[0:1], vcc
	v_addc_co_u32_e32 v6, vcc, 0, v6, vcc
	s_orn2_b64_e32 vcc, vcc, s[0:1]
	v_addc_co_u32_e32 v7, vcc, -1, v7, vcc
```

and at this point it becomes visible how this is a sub-optimal ("wasteful") compilation: not only in the number of vectorial instructions (7 vs. 4), but also most importantly in the VGPR allocation -- the compiler unfortunately does a terrible job.

See also #1002 , #989 , #967 , #488 , #477 for other examples of missed optimizations that require asm() to work-around. Some of these are extremely basic (such as recognizing the carry-out idiom for 64-bit operations), have been reported 3 years ago, and are still not fixed in LLVM. 

So IMO inline assembly is a stop-gap solution until the optimizer is fixed.


---

### 评论 #9 — arsenm (2021-06-01T17:25:13Z)

Nearly all VALU instructions have an implicit exec register read. It's a special register, but still a register that needs a read constraint (e.g. after the second : you need "exec"). If you only had SALU instructions in your asm, it wouldn't be necessary.

I suspect you could also work around the optimizer by using the add/sub with overflow builtins which would be preferable to the asm

---

### 评论 #10 — preda (2021-06-01T17:27:47Z)

I would very much prefer to not have to use inline assembly, ever. Simply enjoy the compiler instead of suspecting it, fighting it, coercing it in order to get not-terrible code. But optimizing GCN is not an easy task, and the compiler is not there yet.


---

### 评论 #11 — preda (2021-06-01T17:34:28Z)

> Nearly all VALU instructions have an implicit exec register read. It's a special register, but still a register that needs a read constraint (e.g. after the second : you need "exec"). If you only had SALU instructions in your asm, it wouldn't be necessary.

Ok, thanks, I'll try that.

> I suspect you could also work around the optimizer by using the add/sub with overflow builtins which would be preferable to the asm

Thanks I was not aware of those builtins. Found them here https://clang.llvm.org/docs/LanguageExtensions.html#checked-arithmetic-builtins and I'll look into using them.
 

---

### 评论 #12 — b-sumner (2021-06-01T17:54:44Z)

@preda you have probably seen that there is a hazard when VALU writes SGPR and VMEM reads that SGPR.  That hazard is hanging off the end of the inline asm and compiler doesn't know about it and may be scheduling a VMEM too early.

---

### 评论 #13 — preda (2021-06-01T18:18:49Z)

> @preda you have probably seen that there is a hazard when VALU writes SGPR and VMEM reads that SGPR. That hazard is hanging off the end of the inline asm and compiler doesn't know about it and may be scheduling a VMEM too early.

@b-sumner but there's no SGPR output from that assembly block. "stmp" is named in the output list only to be used as a temporary SGPR, it's value is not used after the block (you see, it's not used in the return value of the sum() function). Do you think the hazard you mention still applies?

---

### 评论 #14 — b-sumner (2021-06-01T19:33:18Z)

@preda, yes sorry I'm trying to do too many things at once. 

---

### 评论 #15 — preda (2021-06-01T19:50:16Z)

> Nearly all VALU instructions have an implicit exec register read. It's a special register, but still a register that needs a read constraint (e.g. after the second : you need "exec"). If you only had SALU instructions in your asm, it wouldn't be necessary.

@arsenm thanks for pointing out the read-exec dependency!
so is this the correct way to write it:
```
int dummy;
int x = 1;
int y;
__asm("v_add_u32 %0, %1, %1" : "=v"(y) : "v"(x), "{exec}"(dummy));
```
i.e. I have to use a dummy variable explicitly mapped to the exec register (the compiler won't accept just "exec" or "{exec}"). It seems the size mismatch (exec being 64-bit, dummy in the example 32-bit) doesn't matter either.


---

### 评论 #16 — b-sumner (2021-06-01T22:56:39Z)

@preda, a unhandled hazard still seems like a possibility.  Can you test that bad sub function by itself and see if it ever produces an incorrect result, randomly or not?

---

### 评论 #17 — preda (2021-06-02T12:07:30Z)

I found a bug in my code: s_orn2_b64 sets SCC, so I need to add "scc" to the clobbered list. I'm validating now.

Everything seems fine for now. Thank you @arsenm @b-sumner for the help! and sorry for the false alarm.


---

### 评论 #18 — preda (2021-06-02T20:06:42Z)

> I suspect you could also work around the optimizer by using the add/sub with overflow builtins which would be preferable to the asm

@arsenm looking at the LLVM [carry builtins](https://clang.llvm.org/docs/LanguageExtensions.html#multiprecision-arithmetic-builtins), I don't see any good match to represent the GCN v_mad_u64_u32, i.e. a multiplication with 32-bit multiplicands but a 64-bit carry-in. (plus a 1-bit carry-out).


---
