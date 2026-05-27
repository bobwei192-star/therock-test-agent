# optimization: inefficient 32x32->64 wide mul?

> **Issue #480**
> **状态**: closed
> **创建时间**: 2018-07-30T12:10:34Z
> **更新时间**: 2023-12-12T21:48:52Z
> **关闭时间**: 2023-12-12T21:48:51Z
> **作者**: preda
> **标签**: Under Investigation, Compiler Performance Issue
> **URL**: https://github.com/ROCm/ROCm/issues/480

## 标签

- **Under Investigation** (颜色: #0052cc)
- **Compiler Performance Issue** (颜色: #8ff442)

## 描述

uint a, b;
ulong x = a * (ulong) b;

When doing the wide integer multiplication 32x32 -> 64, such code is generated:

```
	v_mul_lo_u32 v0, v4, v3                                    // 000000003D58: D2850000 00020704
	v_mul_hi_u32 v1, v4, v3                                    // 000000003D60: D2860001 00020704
```

It seems to me it would be more efficient to generate a single v_mad_u64_u32 instead, e.g.
```
v_mad_u64_u32 v[0:1], vcc, v4, v3, 0
```

---

## 评论 (12 条)

### 评论 #1 — b-sumner (2018-07-30T16:47:58Z)

Thanks, we'll look into this.

---

### 评论 #2 — preda (2018-08-03T07:43:03Z)

About the balance between two MULs (lo/hi) vs. a single MAD_u64 -- it seems to me that the MAD_u64 has the potential to be up to twice as fast, with the drawback of requiring aligned destination registers, and clobbering a pair of SGPRs.

If that's the case and indeed the MAD_u64 is a better option, then the compiler may also consider applying the same optimization to integer division (32 bit and 64 bit), which right now also generates pairs of MUL LO/HI that can be merged.


---

### 评论 #3 — ex-rzr (2018-09-17T08:23:32Z)

We use this instruction (inline asm) in rocRAND for Philox engine: https://github.com/ROCmSoftwarePlatform/rocRAND/blob/master/library/include/rocrand_common.h#L44

We'd like to remove the asm instruction once this optimization is supported by the compiler.

---

### 评论 #4 — TCS-SK (2019-05-29T09:38:48Z)

Hi Preda ,

Here is the software, GPU and Environment details

    clang version 3.8.0-2
    Environment: Ubuntu 16.x and x86_64-pc-linux-gnu
    Target GPU: --amdgpu-target=gfx803

Kernel :

__global__ void comp(unsigned int * a, unsigned int *b, unsigned long int * c){

        *c = (*a) * ( unsigned long int) (*b);
}

Here is the log file tested values for widemul

---------------- Output for widemul-------------------
 Input 99999     99999
  output 9999800001
 ---------------- Output for widemul-------------------
 Input 66666     66666
  output 4444355556
 ---------------- Output for widemul-------------------
 Input 88888     88888
  output 7901076544
 ---------------- Output for widemul-------------------
 Input 22222     22222
  output 493817284
 ---------------- Output for widemul-------------------
 Input 12121     12121
  output 146918641
 ---------------- Output for widemul-------------------
 Input 50000     50000
  output 2500000000
 ---------------- Output for widemul-------------------
 Input 500000     500000
  output 250000000000

Question 1: Is the issue still exists ?

Question 2: Can you provide the clang version , Environment and target hardware details (GPU)?

Thank you.

---

### 评论 #5 — preda (2019-05-29T21:18:14Z)

@TCS-SK, did you try to reproduce the issue? this way you could establish yourself if it's still present or not.

I tested now with ROCm 2.2 and RadeonVII, and yes it's still present:
```
KERNEL(256) testKernel(P(long) io) {
  uint me = get_local_id(0);
  io[me] = io[me + 256] * (long) io[me +512];
}
```
Compiles to:
```
	s_load_dwordx2 s[0:1], s[4:5], 0x0                         // 00000001BF00: C0060002 00000000
	v_lshlrev_b32_e32 v0, 3, v0                                // 00000001BF08: 24000083
	s_movk_i32 s2, 0x1000                                      // 00000001BF0C: B0021000
	s_waitcnt lgkmcnt(0)                                       // 00000001BF10: BF8CC07F
	v_mov_b32_e32 v1, s1                                       // 00000001BF14: 7E020201
	v_add_co_u32_e32 v0, vcc, s0, v0                           // 00000001BF18: 32000000
	v_addc_co_u32_e32 v1, vcc, 0, v1, vcc                      // 00000001BF1C: 38020280
	v_add_co_u32_e32 v2, vcc, s2, v0                           // 00000001BF20: 32040002
	v_addc_co_u32_e32 v3, vcc, 0, v1, vcc                      // 00000001BF24: 38060280
	global_load_dwordx2 v[4:5], v[0:1], off offset:2048        // 00000001BF28: DC548800 047F0000
	global_load_dwordx2 v[2:3], v[2:3], off                    // 00000001BF30: DC548000 027F0002
	s_waitcnt vmcnt(0)                                         // 00000001BF38: BF8C0F70
	v_mul_lo_u32 v3, v3, v4                                    // 00000001BF3C: D2850003 00020903
	v_mul_lo_u32 v5, v2, v5                                    // 00000001BF44: D2850005 00020B02
	v_mul_hi_u32 v6, v2, v4                                    // 00000001BF4C: D2860006 00020902
	v_mul_lo_u32 v2, v2, v4                                    // 00000001BF54: D2850002 00020902
	v_add3_u32 v3, v6, v5, v3                                  // 00000001BF5C: D1FF0003 040E0B06
	global_store_dwordx2 v[0:1], v[2:3], off                   // 00000001BF64: DC748000 007F0200
	s_endpgm                                                   // 00000001BF6C: BF810000
```


---

### 评论 #6 — TCS-SK (2019-05-30T10:25:15Z)

Hi  Perda ,

I Tested the code with rocm version 2.4.25 and AMD gpu gfx803 . I was getting proper result
I Couldnot find rocm support for RadeonVII  ?
Below is the refernce
https://github.com/RadeonOpenCompute/ROCm#supported-gpus(refernce)

I have a doubt 1- Is Rocm 2.2 or 2.4.25 supports on RadeonVII GPU ?                     
                        2- Can you verify is the problem with Rocm version or/and GPU ?

Thank you

---

### 评论 #7 — preda (2019-05-30T11:46:01Z)

RadeonVII is the successor of Vega64; of course it's supported by ROCm.

ROCm 2.3 has a serious performance regresion vs. 2.2 which is tracked by AMD. And afterwards ROCm 2.4 was released with this performance regression still present, which is not nice. Because I'm using AMD GPUs for performance, I can't use ROCm 2.3 or 2.4.

Anyway, for this bug's verification sake, I did a checkout and build of rocm-opencl, which should be fresher than what's in 2.4, and verified yes this issue is still present. At this point, could you please post the kernel that you used to verify the bug's absence, and the ISA you observed? Thank you.


---

### 评论 #8 — TCS-SK (2019-05-31T10:58:15Z)

Hi Perda,

We have only -amdgpu-target=gfx803 gpu. 

Here is the kernel
// OpenCL kernel
const char *kernelSource =                                                            "\n" \
"#pragma OPENCL EXTENSION cl_khr_fp64 : enable                   \n" \
"__kernel void WideMul( __global unsigned int *a,                          \n" \
"                       __global unsigned int *b,                                         \n" \
"                       __global unsigned long int *c,                                 \n" \
"                       const unsigned int n)                                              \n" \
"{                                                                                                     \n" \
"    //Get our global thread ID                                                          \n" \
"    int id = get_local_id(0);                                                              \n" \
"    //Make sure we do not go out of bounds                                   \n" \
" *c = ( (*a)* (unsigned long int) (*b));                                             \n" \
"}                                                                                                    \n" \
                                                                                                      "\n" ;
Here is the assembly code.
// Disassembly:
	s_load_dwordx4 s[0:3], s[4:5], 0x0                      // 000000001100: C00A0002 00000000
	s_load_dwordx4 s[4:7], s[4:5], 0x10                    // 000000001108: C00A0102 00000010
	s_waitcnt lgkmcnt(0)                                            // 000000001110: BF8C007F
	s_load_dword s0, s[0:1], 0x0                               // 000000001114: C0020000 00000000
	s_load_dword s1, s[2:3], 0x0                               // 00000000111C: C0020041 00000000
	v_mov_b32_e32 v0, s4                                       // 000000001124: 7E000204
	v_mov_b32_e32 v1, s5                                       // 000000001128: 7E020205
	s_waitcnt lgkmcnt(0)                                           // 00000000112C: BF8C007F
	v_mov_b32_e32 v2, s0                                       // 000000001130: 7E040200
	v_mul_hi_u32 v3, s1, v2                                     // 000000001134: D2860003 00020401
	s_mul_i32 s1, s1, s0                                           // 00000000113C: 92010001
	v_mov_b32_e32 v2, s1                                       // 000000001140: 7E040201
	flat_store_dwordx2 v[0:1], v[2:3]                         // 000000001144: DC740000 00000200
	s_endpgm                                                           // 00000000114C: BF810000

Thank you.





---

### 评论 #9 — preda (2019-06-01T00:50:59Z)

@TCS-SK , looking at your ISA, I see that there is no 64-bit mul instruction (e.g. v_mad_u64_u32). So your ISA shows that the bug is still present, not that it's fixed.

It would also be good to index ("id") into the buffers in your code to get a more realistic example.


---

### 评论 #10 — ROCmSupport (2021-01-07T07:23:05Z)

Hi @preda
Thanks for reaching out.
Can you please verify with the latest ROCm 4.0 and update the status asap.
Thank you.

---

### 评论 #11 — tasso (2023-12-08T17:10:36Z)

Is this still an issue with the latest ROCm?  If not, can we please close it?

---

### 评论 #12 — tasso (2023-12-12T21:48:51Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---
