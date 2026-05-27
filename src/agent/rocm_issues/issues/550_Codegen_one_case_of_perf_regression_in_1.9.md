# Codegen: one case of perf regression in 1.9 

> **Issue #550**
> **状态**: closed
> **创建时间**: 2018-09-19T02:36:49Z
> **更新时间**: 2020-12-16T12:22:38Z
> **关闭时间**: 2020-12-16T12:22:38Z
> **作者**: preda
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/550

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

In GpuOwl https://github.com/preda/gpuowl I see a perf regression after moving to 1.9 from 1.8.2. I think the bulk of it comes from the miscompilation of one kernel "mulFused" that I paste below for comparison.
[mulFused-1.8.2.txt](https://github.com/RadeonOpenCompute/ROCm/files/2395206/mulFused-1.8.2.txt)
[mulFused-1.9.txt](https://github.com/RadeonOpenCompute/ROCm/files/2395207/mulFused-1.9.txt)

In 1.8.2:
		workitem_private_segment_byte_size = 0
		workgroup_group_segment_byte_size = 4096
		gds_segment_byte_size = 0
		kernarg_segment_byte_size = 56
		workgroup_fbarrier_count = 0
		wavefront_sgpr_count = 28
		workitem_vgpr_count = 216

In 1.9:
		workitem_private_segment_byte_size = 380
		workgroup_group_segment_byte_size = 4096
		gds_segment_byte_size = 0
		kernarg_segment_byte_size = 72
		workgroup_fbarrier_count = 0
		wavefront_sgpr_count = 27
		workitem_vgpr_count = 256

As you see, there is an issue with the VGPRs allocation. 1.9 causes spilling, while 1.8.2 did not.

On a related note, how may I install ROCm 1.8.2 or 1.8.3, not that it's not the most recent version anymore?
thanks!

(for repro in GpuOwl, please do: echo "88593847" > worktodo.txt )

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-09-19T15:30:33Z)

All of our previous ROCm releases are archived at http://repo.radeon.com/rocm/archive/

---

### 评论 #2 — b-sumner (2018-09-19T16:37:43Z)

Thanks for letting us know.  We'll look into this.

---

### 评论 #3 — ROCmSupport (2020-12-16T12:22:38Z)

This is 2 years old issue and the environment is very old.
Recommend to try with the latest ROCm release and file a ticket if any.

---
