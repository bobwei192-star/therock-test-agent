# Heavy usage of flat instead of ds atomic operations 

> **Issue #1181**
> **状态**: closed
> **创建时间**: 2020-07-23T07:49:07Z
> **更新时间**: 2021-04-08T11:43:30Z
> **关闭时间**: 2021-04-08T11:43:29Z
> **作者**: Lolliedieb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1181

## 描述

Hello

I observed that the lightning compiler - at least those that is included with rga prefers to use flat atomic operations in local memory instead of ds_atomics This applies as well to my Radeon VII as to RX 580 target.

I wondered why this happens and if it would not be more beneficiary to default to ds operations when available, because the flat operations

- need 8 byte instead of 4 byte (ds ops) addressing in shared memory (when in 64 bit addressing mode)
- require a "s_waitcnt    vmcnt(0) & lgkmcnt(0)" wait instead of "lgkmcnt" (ds ops) only, which causes a performance regression when the shared atomics are interleaved with global read or write operations
- On Ellesmere target only: the additional address offset causes an extra "s_load_dword" operation followed by a "lgkmcnt" wait when ever occurring - I do not know why this sreg is not loaded in the beginning of the kernel and then kept for every use - it seems this happens on Vega target correctly and saves a lot of s_load operations in a tight loop I have in my code.

- (Not a down, but strange: for pure read and write operation the ds_ operations are used... so we have indeed to different ways of addressing same space mixed in the kernel)

So I would appreciate usage of ds_ instead of flat_ operations and I do not see why this is not default. In case there is good reason to have flat_ as default maybe there is a switch that can toggle the behavior? If yes any comment about it would be heavily appreciated. 



---

## 评论 (9 条)

### 评论 #1 — b-sumner (2020-07-23T14:49:19Z)

@Lolliedieb I assume you are using the hip language.  In this language, and unlike OpenCL C, there is no concept of address spaces, and a pointer can point to anything.  In OpenCL terminology, every pointer is a generic pointer.  So with hip, we have to rely on the compiler being able to "figure out" that a generic pointer is actually pointing to a `__shared__` / `__local` variable, and this is not always possible.  That being said, it is possible that the compiler can do a better job of this than it does now.  It would be helpful if you can provide a minimal standalone example (i.e. definitely not a pointer to a repo with hundreds of thousands of lines of code and tons of external dependencies) where you're certain the compiler should be able to do better.

---

### 评论 #2 — Lolliedieb (2020-07-23T15:17:27Z)

No, I am speaking about rocm-cl / the OpenCl compiler integrated in rga 2.3.1.

Since my source code is of OpenCL 1.2 standard kind of the oposite is the case: every memory has a clearly defined address space (const, private, private scratch, local (lds) or global), so it should be easy to guess the ideal operation type. 

---

### 评论 #3 — b-sumner (2020-07-23T15:25:36Z)

Thanks for the clarification.  Would you be able to provide or point to a (ideally small or minimal) OpenCL C source that exhibits the problem?

---

### 评论 #4 — Lolliedieb (2020-08-10T09:33:24Z)

Sorry for the delay - summer holidays ;)

Yes of course. Consider the following OpenCL source

> __attribute__((reqd_work_group_size(1024, 1, 1))) 
> __kernel void sort (	__global uint4 * input,
> 			__global uint4 * output,
> 			__global uint * counter,
> 			uint grpDist,
> 			uint bucketSize) {
> 
> 	uint lId = get_local_id(0);
> 	uint grp = get_group_id(0);
> 	
> 	__local uint histo[256];
> 	
> 	if (lId < 256) histo[lId] = 0;
> 	
> 	barrier(CLK_LOCAL_MEM_FENCE);		
> 	
> 	uint4 load0, load1, load2, load3;
> 	
> 	load0 = input[grp * bucketSize + lId];
> 	load1 = input[grp * bucketSize + lId + 1024];
> 	load2 = input[grp * bucketSize + lId + 2048];
> 	load3 = input[grp * bucketSize + lId + 3072];			
> 	
> 	atomic_inc(&histo[load0.s0 & 0xFF]);
> 	atomic_inc(&histo[load1.s0 & 0xFF]);
> 	atomic_inc(&histo[load2.s0 & 0xFF]);
> 	atomic_inc(&histo[load3.s0 & 0xFF]);
> 	
> 	barrier(CLK_LOCAL_MEM_FENCE);	
> 	
> 	if (lId < 256) {
> 		histo[lId] = atomic_add(&counter[lId], histo[lId]);
> 	}
> 	
> 	barrier(CLK_LOCAL_MEM_FENCE);	
> 	
> 	uint pos;
> 	
> 	pos = atomic_inc(&histo[load0.s0 & 0xFF]);
> 	pos += bucketSize * (load0.s0 & 0xFF);
> 	output[pos] = load0;
> 	
> 	pos = atomic_inc(&histo[load1.s0 & 0xFF]);
> 	pos += bucketSize * (load1.s0 & 0xFF);
> 	output[pos] = load1;
> 	
> 	pos = atomic_inc(&histo[load2.s0 & 0xFF]);
> 	pos += bucketSize * (load2.s0 & 0xFF);
> 	output[pos] = load2;
> 	
> 	pos = atomic_inc(&histo[load3.s0 & 0xFF]);
> 	pos += bucketSize * (load3.s0 & 0xFF);
> 	output[pos] = load3;	
>  }

The kernel is rather simple. Each thread loads 4 uint4 and then tries to sort it according to the lowest 2 byte of the first uint int each uint4 package (Kind of a bucket sort). To save global atomic operations the work group first collects the number of outputs to each buffer before writing something.

Now compiled with rga for Ellesmere target (and well quite similar for Vega or VII), when writing it looks like

> flat_store_dwordx4    v[19:20], v[13:16]
> flat_atomic_add       v0, v[17:18], v2 glc
> s_waitcnt             vmcnt(0) lgkmcnt(0)
> v_add_u32_e32         v0, vcc, v0, v23
> v_lshlrev_b64         v[13:14], 4, v[0:1]
> v_add_u32_e32         v13, vcc, s14, v13
> v_addc_u32_e32        v14, vcc, v30, v14, vcc
> flat_store_dwordx4    v[13:14], v[7:10]
> flat_atomic_add       v0, v[11:12], v2 glc
> s_waitcnt             vmcnt(0) lgkmcnt(0)
> v_add_u32_e32         v0, vcc, v0, v24
> v_lshlrev_b64         v[0:1], 4, v[0:1]
> v_add_u32_e32         v0, vcc, s14, v0
> v_addc_u32_e32        v1, vcc, v21, v1, vcc
> flat_store_dwordx4    v[0:1], v[3:6]


Here you see that after fetching an address to write element B to, the compiler inserts "s_waitcnt             vmcnt(0) lgkmcnt(0)" which it needs to do, because the local atomic was translated to a flat atomic add instead of a local one. This vmcnt(0) wait but also waits for the (likely uncoalesced) write of element A before increasing the latency before the writing of B can be issued significantly. 

Compiling the same code with the amdgpu-pro building compiler (thats else often much worse then rocm, but this times does better) produces code 

> flat_store_dwordx4 v[9:10], v[1:4]
> ds_add_rtn_u32  v0, v21, v23
> v_bfe_u32       v1, v13, 0, 8
> v_mul_lo_u32    v1, v1, s7
> s_waitcnt       lgkmcnt(0)
> v_add_u32       v0, vcc, v1, v0
> v_mov_b32       v1, 0
> v_lshlrev_b64   v[0:1], 4, v[0:1]
> v_add_u32       v0, vcc, s0, v0
> v_addc_u32      v1, vcc, v19, v1, vcc
> flat_store_dwordx4 v[0:1], v[13:16]
> ds_add_rtn_u32  v0, v22, v23
> v_bfe_u32       v1, v5, 0, 8
> v_mul_lo_u32    v1, v1, s7
> s_waitcnt       lgkmcnt(0)
> v_add_u32       v0, vcc, v1, v0
> v_mov_b32       v1, 0
> v_lshlrev_b64   v[0:1], 4, v[0:1]
> v_add_u32       v0, vcc, s0, v0
> v_addc_u32      v1, vcc, v19, v1, vcc
> flat_store_dwordx4 v[0:1], v[5:8]

This performs significantly better in this case and even requires less vector registers for addressing. 

Note that I am aware the kernel is a bit artificial - but there are other examples like reading elements from global buffer and then inserting them into a local hash table (that needs atomic_cmpxchg in a tight loop). Here the reading operation and the insertion can barely be interleaved when the local atomic (but translated to flat atomic) requires a  vmcnt(0) wait instruction.

---

### 评论 #5 — ROCmSupport (2020-12-17T03:44:02Z)

Thanks @Lolliedieb for reaching out.
I will get back to you with an update on this asap.
Thank you.

---

### 评论 #6 — ROCmSupport (2020-12-17T03:47:06Z)

Hi @Lolliedieb 
I have assigned this issue to developer and got an update that this issue got fixed in the latest internal builds.
So it will be part of first release of 2021.
Request you to wait till that time for the fix.
Thank you.

---

### 评论 #7 — ROCmSupport (2021-01-05T04:03:55Z)

Hi @Lolliedieb 
Fix is ready and its part of our internal builds.
We will make sure the fix will be part of next possible release.
Thank you.


---

### 评论 #8 — ROCmSupport (2021-01-29T12:18:05Z)

Hi @Lolliedieb 

Verified with our internal builds and issue is fixed and the changes will be part of next ROCm release.
Please stay tuned for the next ROCm release.
Thank you.

---

### 评论 #9 — ROCmSupport (2021-04-08T11:43:29Z)

Verified and fixed with 4.1.
Thank you.

---
