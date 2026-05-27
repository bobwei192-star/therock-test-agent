# ROCM conflicts with openmpi

> **Issue #1017**
> **状态**: closed
> **创建时间**: 2020-02-21T12:14:27Z
> **更新时间**: 2021-04-19T12:53:36Z
> **关闭时间**: 2021-04-19T12:53:36Z
> **作者**: PhilipDeegan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1017

## 描述

I'm not trying to use either of my GPUs, is there a simple way to prevent them being picked up via mpirun?

```
mpirun -np 2 echo "foo"
Memory access fault by GPU node-2 (Agent handle: 0x557153bfcf50) on address (nil). Reason: Unknown.
Aborted
```



---

## 评论 (2 条)

### 评论 #1 — PhilipDeegan (2020-02-23T16:07:03Z)

I had compiled OpenMPI 4.0.(2?) locally when this began.
It didn't happen with OpenMPI 3.x from apt (buster-backports) or MPICH (latest from source) 

Removing rocm* from via apt allowed mpirun to complete, not exactly ideal!

---

### 评论 #2 — ROCmSupport (2021-04-19T12:53:36Z)

Thanks @PhilipDeegan 
This issue is fixed and not observed with the latest ROCm 4.1.
Hence recommend you to try with the same.
Feel free to open a new issue, for any, for quick resolution.
Thank you.

---
