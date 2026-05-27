# Cooperative Group is causing error on MI-250

> **Issue #1729**
> **状态**: closed
> **创建时间**: 2022-04-22T14:36:06Z
> **更新时间**: 2024-01-19T17:49:11Z
> **关闭时间**: 2024-01-19T17:49:11Z
> **作者**: JieyangChen7
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1729

## 描述

We are working on porting the ZFP lossy compressor onto AMD GPUs using HIP. Part of the implementation relies on the Cooperative Group (CG). The CG kernels run correctly without error on MI-100 GPU, but it is reporting `HSA_STATUS_ERROR_MEMORY_FAULT: Agent attempted to access an inaccessible address.` error on MI-250 GPU. This was tested with both ROCM 4.5.0 and 5.1.0.

Here is how to reproduce the issue:
First, build ZFP with HIP
```
mkdir -p zfp
zfp_src=./zfp/src
zfp_build=./zfp/build
git clone -b feature/hip-support https://github.com/JieyangChen7/zfp.git ${zfp_src}
cmake -S ${zfp_src} -B ${zfp_build} \
-DZFP_WITH_HIP=ON \
-DZFP_WITH_OPENMP=OFF \
-DCMAKE_HIP_ARCHITECTURES="gfx90a" \
-DCMAKE_C_COMPILER=amdclang \
-DCMAKE_CXX_COMPILER=amdclang++ \
-DZFP_HIP_STREAM_MEMSET=ON \
-DZFP_HIP_HOST_REGISTER=OFF
cmake --build ${zfp_build} -j
```

Then run
```
./zfp/build-crusher/bin/testexec
```

On MI-100, all tests can pass without error. On MI-250, we get the following error message:

```
Queue at 0x7f4e03654000 inactivated due to async error:
	HSA_STATUS_ERROR_MEMORY_FAULT: Agent attempted to access an inaccessible address.
Aborted
```

---

## 评论 (2 条)

### 评论 #1 — ffleader1 (2022-05-31T17:26:26Z)

I just came across this issue with my VEGA 56
Is it because the GPU memory is a bit low?
has there been a fix for this?
Thank you

---

### 评论 #2 — nartmada (2024-01-18T03:38:48Z)

Hi @JieyangChen7, please close the ticket if the issue has been fixed.  Thanks.

---
