# GCN ISA: document impact of FP IEEE_mode on VOP3 output modifiers

> **Issue #968**
> **状态**: closed
> **创建时间**: 2019-12-15T07:45:54Z
> **更新时间**: 2023-12-18T15:56:53Z
> **关闭时间**: 2023-12-18T15:56:53Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/968

## 描述

It seems that "output modifiers" on VOP3 instructions (e.g. mul:2 on v_mul_f64) are ignored when IEEE_mode is set. Please add this information in the GCN ISA document. This is important because by default OpenCL code is generated with IEEE_mode set, and inline __asm() is supported, which can be used to take advantage of output modifiers.

Context: see #964

---

## 评论 (11 条)

### 评论 #1 — b-sumner (2019-12-15T17:23:01Z)

We're looking into this.  It was probably an oversight.

Note that the use of inline asm for ordinary floating point operations is not likely to improve performance  The compiler doesn't know what goes on in inline asm and will disable various other optimizations around them.

---

### 评论 #2 — gwoltman (2019-12-18T23:27:35Z)

Inline assembly can be necessary to workaround compiler generating poor code.  See https://github.com/RadeonOpenCompute/ROCm/issues/803 (never addressed).  Using inline assembly here turns 18 add_f64 ops into 16 add_f64 ops and a several percent performance boost.   The use of output modifiers led to a 0.75% performance boost (not much but I'm running out of ideas!)

---

### 评论 #3 — b-sumner (2019-12-18T23:49:19Z)

Would it be possible to provide a simple test case for this 18 vs. 16 operations issue?  It's pretty surprising to me that we would get something wrong with a straight series of adds, unless you're exploiting some algebraic property that in general we can't for floating point.

---

### 评论 #4 — gwoltman (2019-12-19T01:57:29Z)

Sure, nothing but 16 simple adds and subtracts (with lots of register renaming thrown in).  This series of operations are the butterfly operations at the heart of any radix-4 fast Fourier transform).  Try this:

`KERNEL(256) testKernel(global double2 *io) {
	double2 u0, u1, u2, u3;
	u0 = io[0];
	u1 = io[1];
	u2 = io[2];
	u3 = io[3];

#define A2(a, b) { double2 t = a; a = t + b; b = t - b; }
#define X3(a, b) { double2 t = a; a = t + b; t.x = b.x - t.x; b.x = t.y - b.y; b.y = t.x; }

	A2(u0, u2);
	X3(u1, u3);
	A2(u0, u1);
	A2(u2, u3);

	io[0] = u0;
	io[1] = u1;
	io[2] = u2;
	io[3] = u3;
}
`

---

### 评论 #5 — b-sumner (2019-12-20T15:14:15Z)

Umm... I'm not sure what compiler you're using or which device, but when I compile your code for gfx900, and extract the f64 operations I get 16:

        v_add_f64 v[8:9], s[0:1], v[0:1]
        v_add_f64 v[12:13], s[0:1], -v[0:1]
        v_add_f64 v[10:11], s[2:3], v[2:3]
        v_add_f64 v[14:15], s[6:7], v[6:7]
        v_add_f64 v[16:17], s[2:3], -v[2:3]
        v_add_f64 v[20:21], s[6:7], -v[6:7]
        v_add_f64 v[4:5], s[4:5], v[4:5]
        v_add_f64 v[18:19], s[12:13], -v[0:1]
        v_add_f64 v[2:3], v[10:11], v[14:15]
        v_add_f64 v[6:7], v[10:11], -v[14:15]
        v_add_f64 v[0:1], v[8:9], v[4:5]
        v_add_f64 v[4:5], v[8:9], -v[4:5]
        v_add_f64 v[8:9], v[12:13], v[20:21]
        v_add_f64 v[10:11], v[16:17], v[18:19]
        v_add_f64 v[14:15], v[16:17], -v[18:19]
        v_add_f64 v[12:13], v[12:13], -v[20:21]



---

### 评论 #6 — gwoltman (2019-12-20T15:29:57Z)

Device is Radeon VII.   Compiler is ROCm 2.10.  The output I get is:

	.protected	testKernel      ; -- Begin function testKernel
	.globl	testKernel
	.p2align	8
	.type	testKernel,@function
testKernel:                             ; @testKernel
; %bb.0:
	s_load_dwordx2 s[16:17], s[4:5], 0x0
	s_mov_b32 s18, s7
	s_mov_b32 s32, s18
	s_waitcnt lgkmcnt(0)
	s_load_dwordx4 s[0:3], s[16:17], 0x0
	s_load_dwordx4 s[4:7], s[16:17], 0x10
	s_load_dwordx4 s[8:11], s[16:17], 0x20
	s_load_dwordx4 s[12:15], s[16:17], 0x30
	s_waitcnt lgkmcnt(0)
	v_mov_b32_e32 v0, s0
	v_mov_b32_e32 v4, s4
	v_mov_b32_e32 v5, s5
	v_mov_b32_e32 v1, s1
	v_add_f64 v[8:9], s[8:9], v[0:1]
	v_add_f64 v[14:15], s[12:13], v[4:5]
	v_mov_b32_e32 v2, s2
	v_mov_b32_e32 v0, s8
	v_mov_b32_e32 v3, s3
	v_mov_b32_e32 v1, s9
	v_mov_b32_e32 v13, s7
	v_add_f64 v[6:7], s[10:11], v[2:3]
	v_mov_b32_e32 v2, s10
	v_add_f64 v[16:17], s[0:1], -v[0:1]
	v_add_f64 v[20:21], s[12:13], -v[4:5]
	v_add_f64 v[0:1], v[14:15], v[8:9]
	v_add_f64 v[4:5], v[8:9], -v[14:15]
	v_mov_b32_e32 v8, s14
	v_mov_b32_e32 v15, s13
	v_mov_b32_e32 v9, s15
	v_mov_b32_e32 v14, s12
	v_mov_b32_e32 v12, s6
	v_mov_b32_e32 v3, s11
	v_add_f64 v[8:9], s[6:7], -v[8:9]
	v_add_f64 v[10:11], s[14:15], v[12:13]
	v_add_f64 v[12:13], s[14:15], -v[12:13]
	v_add_f64 v[18:19], s[2:3], -v[2:3]
	v_add_f64 v[14:15], s[4:5], -v[14:15]
	v_add_f64 v[8:9], v[8:9], v[16:17]
	v_add_f64 v[2:3], v[10:11], v[6:7]
	v_add_f64 v[6:7], v[6:7], -v[10:11]
	v_add_f64 v[12:13], v[16:17], v[12:13]
	v_add_f64 v[10:11], v[20:21], v[18:19]
	v_add_f64 v[14:15], v[18:19], v[14:15]
	v_mov_b32_e32 v16, s16
	v_mov_b32_e32 v17, s17
	global_store_dwordx4 v[16:17], v[0:3], off
	global_store_dwordx4 v[16:17], v[4:7], off offset:16
	global_store_dwordx4 v[16:17], v[8:11], off offset:32
	global_store_dwordx4 v[16:17], v[12:15], off offset:48
	s_endpgm




---

### 评论 #7 — b-sumner (2019-12-20T16:18:52Z)

I don't know what a "Radeon VII" is.  What is the device name from clinfo, or what the the asm say the device is?

---

### 评论 #8 — b-sumner (2019-12-20T16:26:15Z)

Hmm, I compiled for gfx906 and added -cl-fast-relaxed math and am seeing 18 ops now.  @gwoltman, we'll look into this further.

---

### 评论 #9 — preda (2019-12-20T21:03:47Z)

> I don't know what a "Radeon VII" is. What is the device name from clinfo, or what the the asm say the device is?

@b-sumner RadeonVII https://www.amd.com/en/products/graphics/amd-radeon-vii is a major AMD GPU; Vega20, gfx906+sram-ecc


---

### 评论 #10 — nartmada (2023-12-13T23:02:30Z)

Hi @preda, is this still an issue ?  If not, please close the ticket.  

---

### 评论 #11 — nartmada (2023-12-18T15:56:53Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
