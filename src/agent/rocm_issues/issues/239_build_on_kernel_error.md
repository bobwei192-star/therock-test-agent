# build on kernel error

> **Issue #239**
> **状态**: closed
> **创建时间**: 2017-10-27T01:18:17Z
> **更新时间**: 2017-10-27T13:15:17Z
> **关闭时间**: 2017-10-27T13:15:17Z
> **作者**: reger-men
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/239

## 描述

What doest that mean:

```
ERROR (dkms apport): binary package for amdtPwrProf: 6.01 not found
Error! Bad return status for module build on kernel: 4.11.0-kfd-compute-rocm-rel-1.6-180 (x86_64)
```
Is the Kernel build successful?


---

## 评论 (3 条)

### 评论 #1 — gstoner (2017-10-27T01:21:55Z)

Are you mixing AMD GPUpro with ROCm components that is only reason you see issue 

---

### 评论 #2 — reger-men (2017-10-27T01:23:55Z)

I uninstalled it with `amdgpu-pro-uninstall`.

When I run test `/HelloWorld`, I get:
```
Failed to find any OpenCL platforms.
Failed to create OpenCL context.
```

---

### 评论 #3 — reger-men (2017-10-27T13:15:13Z)

I reinstall ubuntu 16.04 and then I install ROCm. Now it work.

---
