# Compiler Optimizing Memory Access in Bad Ways, Triggered by Seemingly Unrelated Change

- **Issue #:** 657
- **State:** closed
- **Created:** 2019-01-02T18:18:41Z
- **Updated:** 2023-12-20T18:14:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/657

This is an issue with a number of facets that I am going to try and lay out.
I want to optimize a piece of code and run into a number of problems with compiler optimization behaviour that I struggle to rein in.

This is my initial state: https://github.com/949f45ac/xmrig-HIP/blob/f5a71d80ef7f48761a9f1b496bafc19f9a42747d/src/nvidia/phase2.cu#L592
There is `fast_div_v2` taking three arguments. `RCP` is a `__shared__` lookup table that gets initialized at the start of the kernel, here: https://github.com/949f45ac/xmrig-HIP/blob/f5a71d80ef7f48761a9f1b496bafc19f9a42747d/src/nvidia/phase2.cu#L486
Now I replace `fast_div_v2` with a version that works without a lookup table and is slightly faster. All good, I get improved performance. Call now simply looks like this:
`fast_div_v2(reinterpret_cast<ulonglong2*>(&c)->y, din);`

But when I remove `RCP` (already unused inside the loop!) from the kernel completely, that is, remove the initialization at the top, I suffer a ~30% loss in performance.
Very weird!
I looked at the genereted ISA and the problem basically comes down to the following. If we take a look at this whole chunk of code:
```C++
		// long_state is 2 MB of memory paced throughout 512 MB
		// j1 is random adress inside
		ulonglong2 y2 = long_state[j1];
		uint64_t t1_64 = c.x | (((uint64_t) c.y) << 32);

		// Reads memory adjacent to y2, ie. long_state[j1^1], [j1^2], [j1^3]
		LOAD_CHUNK(chunk1, j1, 1);
		LOAD_CHUNK(chunk2, j1, 2);
		LOAD_CHUNK(chunk3, j1, 3);

		PRIO(3) // This does s_setprio 0x3.

		const uint din = ( (c.x) + (sqrt_result << 1)) | 0x80000001UL;
		uint64_t n_division_result = fast_div_v2(reinterpret_cast<ulonglong2*>(&c)->y, din);
		uint32_t n_sqrt_result = fast_sqrt_v2(t1_64 + n_division_result);

		y2.x ^= division_result ^ (((uint64_t) sqrt_result) << 32);

		division_result = n_division_result;
		sqrt_result = n_sqrt_result;


		uint64_t hi = UMUL64HI(t1_64, y2.x);
		uint64_t lo = t1_64 * y2.x;


		ulonglong2 result_mul = make_ulonglong2(hi, lo);

		chunk1 = v_xor(chunk1, result_mul);
		result_mul = v_xor(result_mul, chunk2);

		// Write back to long_state[j1^1]
		STORE_CHUNK(j1, v_add(chunk3, d_old), 1);

```
Loads are going to be very slow, since they are from a random adress.
Hence to reach maximum performance:
- Loads should be scheduled ASAP.
- Blocking on loads via `s_waitcnt` should be delayed as much as possible by the compiler ->
- Everything up to the value of `n_sqrt_result` does not depend on the loads, so all of that should be executed before the first `s_waitcnt`

And so when removing the initialisation of `RCP` we can see that all of this goes wrong:
```asm
        global_load_dwordx4 v[28:31], v[54:55], off
        v_rcp_f32_e32 v38, v37
        ;;#ASMSTART
        V_CVT_F32_UBYTE0 v36, v3
        ;;#ASMEND
        global_load_dwordx4 v[32:35], v[52:53], off
        v_sub_u32_e32 v42, 0, v3
        v_fma_f32 v37, v37, v38, -1.0
        v_add_u32_e32 v39, s7, v38
        v_fma_f32 v36, v36, v38, v37
        v_mul_f32_e32 v36, v36, v39
        v_rndne_f32_e32 v36, v36
        v_cvt_i32_f32_e32 v36, v36
        v_lshlrev_b32_e32 v43, 9, v38
        v_mov_b32_e32 v46, v4
        v_mov_b32_e32 v48, v4
        v_sub_u32_e32 v36, v43, v36
        v_mul_hi_u32 v38, v26, v36
        v_mov_b32_e32 v49, v4
        v_cmp_eq_u32_e32 vcc, 0, v2
        s_and_b64 vcc, exec, vcc
        s_waitcnt vmcnt(1)
        v_add_co_u32_e64 v11, s[0:1], v30, v11
        v_addc_co_u32_e64 v12, s[0:1], v31, v12, s[0:1]
        v_add_co_u32_e64 v9, s[0:1], v28, v9
        v_addc_co_u32_e64 v10, s[0:1], v29, v10, s[0:1]
        v_mad_u64_u32 v[36:37], s[0:1], v27, v36, v[26:27]
        global_load_dwordx4 v[28:31], v[40:41], off
	;; And so on
```
Instead of doing all loads at once, they are far spread out, and the sqrt calculation is pushed a long way down.

Compare with the ISA generated for the least invasive replacement of `fast_div_v2`, where `RCP` is initialized, even passed to the `fast_div_v2` call still, but unused inside.

```asm
        global_load_dwordx4 v[28:31], v[48:49], off
        global_load_dwordx4 v[32:35], v[22:23], off
        global_load_dwordx4 v[36:39], v[61:62], off
        global_load_dwordx4 v[40:43], v[59:60], off
        v_rcp_f32_e32 v46, v45
        ;;#ASMSTART
        V_CVT_F32_UBYTE0 v44, v11
        ;;#ASMEND
        v_sub_u32_e32 v50, 0, v11
        ;;#ASMSTART
        s_setprio 0x3
        ;;#ASMEND
        v_fma_f32 v45, v45, v46, -1.0
        v_add_u32_e32 v47, s7, v46
        v_fma_f32 v44, v44, v46, v45
        v_mul_f32_e32 v44, v44, v47
        v_rndne_f32_e32 v44, v44
        v_cvt_i32_f32_e32 v44, v44
        v_lshlrev_b32_e32 v52, 9, v46
        v_sub_u32_e32 v44, v52, v44
        v_mul_hi_u32 v46, v26, v44
        v_mad_u64_u32 v[44:45], s[0:1], v27, v44, v[26:27]
        v_add_co_u32_e64 v44, s[0:1], v44, v46
        v_addc_co_u32_e64 v45, s[0:1], v45, v13, s[0:1]
        v_mul_lo_i32 v46, v45, v11
        v_mul_hi_u32 v47, v45, v11
        v_cmp_lt_u64_e64 s[0:1], v[44:45], v[26:27]
        v_cndmask_b32_e64 v44, 0, v11, s[0:1]
        v_sub_co_u32_e64 v46, s[0:1], v26, v46
        v_subb_co_u32_e64 v47, s[0:1], v27, v47, s[0:1]
        v_sub_u32_e32 v47, v47, v44
        v_ashrrev_i32_e32 v44, 31, v47
        v_cmp_ge_i64_e64 s[0:1], v[46:47], v[11:12]
        v_and_b32_e32 v11, v44, v11
        v_addc_co_u32_e64 v57, s[2:3], v44, v45, s[0:1]
        v_add_u32_e32 v11, v11, v46
        v_cndmask_b32_e64 v44, 0, v50, s[0:1]
        v_add_u32_e32 v50, v11, v44
        v_add_co_u32_e64 v11, s[0:1], v57, v24
        v_addc_co_u32_e64 v46, s[0:1], v50, v25, s[0:1]
        v_lshrrev_b32_e32 v44, 9, v46
        v_or_b32_e32 v44, s8, v44
        ;;#ASMSTART
        V_RSQ_F32 v45, v44
        
        ;;#ASMEND                                                                                                                                                                                                                            
        ;;#ASMSTART                                                                                                                                                                                                                          
        V_SQRT_F32 v44, v44
        ;;#ASMEND
        v_add_u32_e32 v52, s10, v44
        v_add_u32_e32 v47, s9, v45
        v_mul_hi_u32 v45, v52, v52
        v_mul_lo_i32 v44, v52, v52
        v_lshlrev_b32_e32 v52, 10, v52
        v_lshlrev_b64 v[44:45], 18, v[44:45]
        v_sub_co_u32_e64 v44, s[0:1], v11, v44
        v_subb_co_u32_e64 v44, s[0:1], v46, v45, s[0:1]
        v_cvt_f32_i32_e32 v44, v44
        v_mul_f32_e32 v44, v47, v44
        v_rndne_f32_e32 v44, v44
        v_cvt_i32_f32_e32 v44, v44
        v_add_u32_e32 v52, v52, v44
        v_sub_co_u32_e64 v44, s[0:1], 0, v11
        v_lshrrev_b32_e32 v11, 1, v52
        v_and_b32_e32 v47, 1, v52
        v_subb_co_u32_e64 v45, s[0:1], v52, v46, s[0:1]
        v_add_u32_e32 v46, v11, v47
        v_mad_u64_u32 v[44:45], s[0:1], v46, v11, v[44:45]
        v_add_co_u32_e64 v46, s[0:1], v44, v47
        v_addc_co_u32_e64 v47, s[0:1], v45, v13, s[0:1]
        v_add_co_u32_e64 v11, s[0:1], v44, v11
        v_addc_co_u32_e64 v11, s[0:1], v45, v51, s[0:1]
        v_cmp_lt_i64_e64 s[0:1], 0, v[46:47]
        s_waitcnt vmcnt(2)
```
Splendid! All loads are done at once and quite early, and awaited only when sqrt calculations have been executed to the last bit.
Yet even with this case there are some problems, mostly that loads aren’t scheduled completely ASAP yet (some instructions are needlessly placed before), and the whole thing crumbles if `#pragma unroll 4` is used over `#pragma unroll 2`.
Additionally, of course, I would like to have some control over this and not have it magically work because there is some unused `__shared__` memory declared somewhere else in the kernel.


So I have been trying to somehow force the compiler into doing what I want.
I am using this macro:
`#define FENCE32(x) asm volatile("v_mov_b32 %0, %1" : "=v" (x) : "v" (x) : "memory");`
The idea is that at least memory operations cannot be reordered with respect to the state of the input variable x at the given point.

So for example I can do 

```C++
		// ==== LOAD 2 : chunks ====
		LOAD_CHUNK(chunk3, j1, 3);
		ulonglong2 y2 = long_state[j1];
		LOAD_CHUNK(chunk1, j1, 1);
		LOAD_CHUNK(chunk2, j1, 2);

		PRIO(3)
		FENCE32(c.x);
		uint64_t t1_64 = c.x | (((uint64_t) c.y) << 32);
```
And the compiler starts doing the loads ASAP and not spread out, since I have just disallowed it from using `c.x` (which is needed by some parts of the following code) before it’s scheduled all the loads.

In the same vain I am trying to do
```C++
uint32_t n_sqrt_result = fast_sqrt_v2(t1_64 + n_division_result);

FENCE32(n_sqrt_result);

STORE_CHUNK(j1, v_add(chunk3, d_old), 1);
```
but here my method starts failing already, since the compiler will INSIST on calculating `v_add(chunk3, d_old)` (and hence waiting for the `chunk3` load to complete) before calculating some parts of `fast_sqrt_v2`, even though the store instruction must wait for the sqrt calculation to be complete.

Finally I have been able to achieve the desired result (more or less) by implementing `v_add` in volatile asm – so that it cannot be reordered with respect to `FENCE32(n_sqrt_result)`:

```C++
		uint32_t n_sqrt_result = fast_sqrt_v2(t1_64 + n_division_result);
		FENCE32(n_sqrt_result);

		uint4 dl = make_uint4(d_old.x, d_old.x >> 32, d_old.y, d_old.y >> 32);
		asm volatile(
			"v_add_co_u32_e32  %0, vcc, %8, %4 \n\t"
			"v_addc_co_u32_e32 %1, vcc, %9, %5, vcc \n\t"
			"v_add_co_u32_e32  %2, vcc, %10, %6 \n\t"
			"v_addc_co_u32_e32 %3, vcc, %11, %7, vcc \n\t"
			: "=v" (dl.x), "=v" (dl.y), "=v" (dl.z), "=v" (dl.w)
			: "v" ((uint32_t)chunk3.x), "v" ((uint32_t)(chunk3.x >> 32)), "v" ((uint32_t)chunk3.y), "v" ((uint32_t)(chunk3.y>>32)),
			  "v" (dl.x), "v" (dl.y), "v" (dl.z), "v" (dl.w) : "vcc", "memory");

		reinterpret_cast<uint4*>(long_state)[j1^1] = dl;

		y2.x ^= division_result ^ (((uint64_t) sqrt_result) << 32);
```
It is the fastest version, but still there are problems:
- NOT PORTABLE. ISA for addition changed between gfx803 and gfx900, so I cannot build a **single binary** that works on both. Cf. this issue: https://github.com/ROCm-Developer-Tools/HIP/issues/754
- Actually it is only fastest when using `#pragma unroll 4` which finally stops creating incorrect code. Lower unrolls are slower than the silly version with the unused `RCP` array.


I have created a branch documenting the variants I’ve discussed, and a few inbetween, here: https://github.com/949f45ac/xmrig-HIP/commits/bug_doc0
In the `configs/` folder there are two example configs the program can be tested with. They will mine on the Monero testnet. For every commit I have put a comment inside these configs that tells how it performed for me.

I understand this is a complex issue, but maybe someone’d interested in looking into it, since it’s quite baffling.

Cheers!

ps. Since creating the examples branch I have noticed that `fast_div_v2` contains some aliasing code that may be UB and tried to fix it – it didn’t really help the problem at hand, though.