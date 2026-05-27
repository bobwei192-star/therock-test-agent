# Linking error and unsupported APIs in rocblas

> **Issue #217**
> **状态**: closed
> **创建时间**: 2017-09-29T11:18:00Z
> **更新时间**: 2017-10-06T09:44:21Z
> **关闭时间**: 2017-09-29T12:05:17Z
> **作者**: sriharikarnam
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/217

## 描述

**Background:** 
Porting Mxnet Deep Learning framework to ROCm Platform and migrating from hcblas to rocblas

**Issue:** 
Link error /home/user/workspace/rocblas_integration_latst/mxnet/mshadow/mshadow/./././dot_engine-inl.h:456: undefined reference to `rocblas_hgemm'

/home/user/workspace/rocblas_integration_latst/mxnet/mshadow/mshadow/./././dot_engine-inl.h:456: undefined reference to `rocblas_hgemm'
collect2: error: ld returned 1 exit status
Makefile:302: recipe for target 'bin/im2rec' failed
make: *** [bin/im2rec] Error 1

rocblas_hgemm() function declaration is present at rocblas/include/rocblas-functions.h. But while linking we facing above error. Encountering above error while compiling on nvcc platform.

**Unsupported APIs :**
Unable to find relevant implementation of below APIs:

- hipblasSgemmBatched()
- hipblasDgemmBatched()
- cublasSgemmEx()

Please provide inputs for the above queries.

---

## 评论 (3 条)

### 评论 #1 — gstoner (2017-09-29T12:05:17Z)

We need to put issue in the right forum,  rocBLAS and HCC compiler 

---

### 评论 #2 — kknox (2017-10-04T04:22:48Z)

I've not seen a follow-up issue on this in hipblas/rocblas, but you can find those repositories here:
https://github.com/ROCmSoftwarePlatform/hipBLAS
https://github.com/ROCmSoftwarePlatform/rocBLAS

Quickly:
1.  We had API's defined that returned a NOT_IMPLEMENTED error code.  After discussion, this is confusing and we commented those API's out in our develop branch.
2.  rocBLAS implements a strided, batched GEMM API, for performance reasons.  Thus far, we see no reason to implement a non strided batched routine.  If you disagree, you can add [input here](https://github.com/ROCmSoftwarePlatform/hipBLAS/pull/21)



---

### 评论 #3 — sriharikarnam (2017-10-06T09:44:21Z)

Thanks for your inputs. For any followup questions/clarifications we will raise ticket in rocBLAS forum.

---
