# Hawaii (r9 295x2) does not load OpenCL with rocm 2.0

> **Issue #663**
> **状态**: closed
> **创建时间**: 2019-01-05T18:35:10Z
> **更新时间**: 2019-01-07T23:05:23Z
> **关闭时间**: 2019-01-07T23:05:23Z
> **作者**: nioroso-x3
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/663

## 描述


I have a Intel Haswell PC with two R9 295X2, rocm opencl is not working, clinfo just shows no platforms available.
But rocminfo works, and loading the amdgpu 18.10 opencl implementation through LD_LIBRARY_PATH also works.

I'm using the latest rocm and rocm-dkms in the apt repo with ubuntu 16.04 and kernel 4.15, and also copied the hawaii firmware files to the amdgpu folder.


---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-01-07T23:05:23Z)

I believe this problem has already been reported in #640. Hawaii firmware is not correctly loaded by default, and I am not yet convinced that it successfully works for OpenCL our other high-level programming environments even after that problem is fixed. I would prefer to keep the "Hawaii is broken on ROCm 2.x" issues in a single location, however, so I'm going to close this one. Please keep an eye on #640.

---
