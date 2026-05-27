# redundant s_waitcnt lgkmcnt(0) with barrier

> **Issue #1056**
> **状态**: closed
> **创建时间**: 2020-03-23T10:15:05Z
> **更新时间**: 2024-08-18T16:41:44Z
> **关闭时间**: 2024-07-24T14:17:27Z
> **作者**: preda
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1056

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

ROCm 3.1, Radeon VII,
looking at the generated code I often see this block:
```
s_waitcnt lgkmcnt(0)
s_barrier
s_waitcnt lgkmcnt(0)
```
It seems that the second s_waitcnt is not needed, right?

---

## 评论 (11 条)

### 评论 #1 — preda (2020-03-23T10:31:38Z)

The above happens when using
barrier(CLK_LOCAL_MEM_FENCE);

If instead barrier(0) is used, the generated ISA is as expected:
```
s_waitcnt lgkmcnt(0)
s_barrier
```

So, IMO, something is wrong with barrier(CLK_LOCAL_MEM_FENCE) as an extra s_waitcnt lgkmcnt(0) is generated in that situation.

---

### 评论 #2 — ROCmSupport (2021-04-05T10:18:45Z)

Thanks @preda 
Can you please share me the exact steps for better understanding and reproducing the problem.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-04-08T09:23:23Z)

Request you to try with the latest ROCm 4.1 or 4.1.1 and hope issue is fixed now as its more like an old issue.
Feel free to open a new issue, if any, for quick resolution.

---

### 评论 #4 — hsadasiv (2024-04-12T17:31:21Z)

Seems to happen with rocm6.1

---

### 评论 #5 — nartmada (2024-04-21T16:07:07Z)

@hsadasiv, I will reach out to the internal team for investigation.  Thanks.

---

### 评论 #6 — ppanchad-amd (2024-07-17T20:34:30Z)

Internal ticket has been created to investigate this issue. Thanks!

---

### 评论 #7 — jamesxu2 (2024-07-19T20:06:48Z)

Hi @hsadasiv or @preda , could you provide a reproducer for this issue? I don't see this showing up when inserting barrier(*) instructions and extracting temps with ```hipcc --save-temps -g```. 

I think I agree with you @preda that the second s_waitcnt is redundant on a theoretical basis - The question is if there be other wavefronts or threads manipulating (workgroup-)local memory between the time of the first s_waitcnt lgkmcnt(0) and the s_barrier?

I don't think so, since those threads will be executing the same kernel, and have passed the first s_waitcnt and then stopped at the barrier before they can perform any other operations touching memory. The first s_waitcnt combined with the barrier would seem to _implicitly_ guarantee the consistency of local memory (but not global memory), so I'm not sure why a second s_waitcnt is generated after the barrier and can investigate further if this issue can be reproduced.

One answer might be from [this documentation](https://android.googlesource.com/toolchain/llvm/+/refs/heads/master/docs/AMDGPUUsage.rst) on line 2973, stating:
```
 Since
the LLVM ``memfence`` instruction does not allow an address space to be
specified the OpenCL fence has to convervatively assume both local and
global address space was specified. However, optimizations can often be
done to eliminate the additional ``s_waitcnt`` instructions when there are
no intervening memory instructions which access the corresponding address
space. 
```

If this is a compiler limitation as this documentation says - that the scope of the OpenCL memory fence cannot be disambiguated - then it would make sense that in the case of CLK_LOCAL_MEM_FENCE and CLK_GLOBAL_MEM_FENCE would produce similar assembly with an extra s_waitcnt, while barrier(0), requesting no memory fences/no memory consistency, does not.
 

---

### 评论 #8 — preda (2024-07-23T15:02:39Z)

@jamesxu2  I'm unable to dump OpenCL ISA the way I used to due to #2940  (as soon as -save-temps works again I'll confirm the behavior of the most recent ROCm release).



---

### 评论 #9 — preda (2024-07-23T15:07:30Z)

@jamesxu2 you mentioned
> The first s_waitcnt combined with the barrier would seem to implicitly guarantee the consistency of local memory (but not global memory)

But s_waitcnt lgkmcnt(0) is concerned with LDS, GDS and "konstant" mem-counts, not "global memory" which would be vmcnt.
On OpenCL, GDS is not accessible to the source program (can't be used at all, for all practical purposes there's no GDS), so that leaves LDS and konstant.


---

### 评论 #10 — jamesxu2 (2024-07-24T14:17:27Z)

Hi @preda, after some discussion with our LLVM internal team, this issue is already known and a fix is in the works, though it has not yet been merged into any ROCm release.

Here's some more information about this issue:

Per LLVM docs: 
> Languages such as OpenCL C provide fence operations such as atomic_work_item_fence that can take an explicit address space to fence.

> By default, LLVM has no means to carry that information in the IR, so the information is lost during lowering to LLVM IR. This means that targets such as AMDGPU have to conservatively emit instructions to fence all address spaces in all cases, which can have a noticeable performance impact in high-performance applications.

https://llvm.org/docs/MemoryModelRelaxationAnnotations.html#implementation-example-adding-address-space-information-to-fences

So, I believe what's happening is that GDS is being unnecessarily protected using this ISA, provided by internal team 
```
    s_waitcnt vmcnt(0) lgkmcnt(0)
        s_waitcnt_vscnt null, 0x0
        s_barrier
        s_waitcnt vmcnt(0) lgkmcnt(0)
        s_waitcnt_vscnt null, 0x0
```

as part of a conservative default to fence all memory spaces (even GDS, though it's not technically accessible). Like you've said, this is unnecessary. A fix is in progress for this. 

---

### 评论 #11 — preda (2024-08-18T16:41:44Z)

With ROCm 6.2.0, with this version of the compiler:
```
"AMD clang version 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.2.0 24292 26466ce804ac523b398608f17388eb6d605a3f09)"
```
for a groupsize=64 on gfx906 (thus no wave barrier is necessary as the group has a single wave)

such code is generated:

```
	ds_write2_b64 v136, v[25:26], v[27:28] offset1:4
	ds_write2_b64 v136, v[51:52], v[53:54] offset0:8 offset1:12
	s_waitcnt lgkmcnt(0)
	; wave barrier
	s_waitcnt lgkmcnt(0)
	ds_read2st64_b64 v[25:28], v135 offset1:1
	ds_read2st64_b64 v[29:32], v135 offset0:2 offset1:3
	s_waitcnt lgkmcnt(0)
	; wave barrier
	s_waitcnt lgkmcnt(0)
	ds_write2_b64 v136, v[33:34], v[37:38] offset1:4
	ds_write2_b64 v136, v[39:40], v[35:36] offset0:8 offset1:12
	s_waitcnt lgkmcnt(0)
	; wave barrier
	s_waitcnt lgkmcnt(0)
```

Which IMO can't be defended. I don't know whether the fix you mentioned should be in the LLVM 18 above, but for all I can see the issue is not fixed (maybe it should be re-opened as it's still active?)


---
