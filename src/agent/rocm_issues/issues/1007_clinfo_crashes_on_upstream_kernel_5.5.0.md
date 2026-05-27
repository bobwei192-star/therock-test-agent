# clinfo crashes on upstream kernel 5.5.0

> **Issue #1007**
> **状态**: closed
> **创建时间**: 2020-01-27T13:11:10Z
> **更新时间**: 2021-04-19T12:57:46Z
> **关闭时间**: 2021-04-19T12:57:46Z
> **作者**: jcdutton
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1007

## 描述

clinfo hangs when run on kernel 5.5.0
clinfo works fine on kernel 5.4.15

dmesg output below




---

## 评论 (6 条)

### 评论 #1 — jcdutton (2020-01-27T13:13:50Z)

[clinfo-bad1.log](https://github.com/RadeonOpenCompute/ROCm/files/4117258/clinfo-bad1.log)


---

### 评论 #2 — jcdutton (2020-01-27T13:17:54Z)

GPU is a AMD Vega 56

---

### 评论 #3 — JMadgwick (2020-02-05T20:48:59Z)

The homepage doesn't mention support for those kernels. Maybe try following the instructions for using upstream kernels?

---

### 评论 #4 — pramenku (2020-02-29T10:05:34Z)

ROCm currently doesn't support kernel 5.5.0 

---

### 评论 #5 — seesturm (2020-02-29T10:56:24Z)

Only the kernel modules shipped with ROCm (rocm-dkms) fail with kernel 5.5. For me, ROCm 3.0 itself is working fine with the kernel modules directly provided by kernel 5.5 (5.5.7) for both OpenCL and HIP.

Maybe this information is useful for someone wanting to use ROCm with kernel 5.5.

---

### 评论 #6 — ROCmSupport (2021-04-19T12:57:46Z)

Thanks for reaching out.
This issue is fixed and not observed with the latest ROCm 4.1.
Hence recommend you to try with the same.
Feel free to open a new issue, for any, for quick resolution.
Thank you.

---
