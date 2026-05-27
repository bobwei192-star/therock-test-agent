# Honor __HIP_PLATFORM_AMD__ in all ROCM components

> **Issue #1566**
> **状态**: closed
> **创建时间**: 2021-08-26T01:10:04Z
> **更新时间**: 2021-11-16T20:11:06Z
> **关闭时间**: 2021-11-16T20:11:06Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1566

## 描述

Hit the issue of `hipsparse.h` not picking up `__HIP_PLATFORM_AMD__`
```
/opt/rocm-4.3.0/include$ grep -R _PLATFORM_HCC__ |grep  -v __HIP_PLATFORM_AMD__
hipsparse.h:#if defined(__HIP_PLATFORM_HCC__)
rocrand/rocrand_common.h:#if __HIP_DEVICE_COMPILE__ && (defined(__HIP_PLATFORM_HCC__) || (defined(__HIP_PLATFORM_NVCC__) && (__CUDA_ARCH__ >= 530)))
rocrand/rocrand_common.h:  #if defined(__HIP_PLATFORM_HCC__) && defined(__HIP_DEVICE_COMPILE__) \
rocrand/rocrand_philox4x32_10.h:        #if defined(__HIP_PLATFORM_HCC__)
hip/hip_common.h:#ifndef __HIP_PLATFORM_HCC__
hip/hip_common.h:#define __HIP_PLATFORM_HCC__
hip/hip_runtime.h:#ifdef __HIP_PLATFORM_HCC__
hip/hip_runtime.h:#ifdef __HIP_PLATFORM_HCC__
hiprand/hiprand_kernel.h:#ifdef __HIP_PLATFORM_HCC__
hiprand/hiprand.h:#if defined(__HIP_PLATFORM_HCC__)
hiprand/hiprand_mtgp32_host.h:#if defined(__HIP_PLATFORM_HCC__) || HIPRAND_DOXYGEN
hiprand/hiprand_mtgp32_host.h:#endif // __HIP_PLATFORM_HCC__
```
Please check all the components

---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2021-09-13T06:52:41Z)

Thanks @ye-luo for reaching out.
I will check this for you and get back with an update.
Thank you.

---

### 评论 #2 — doctorcolinsmith (2021-09-14T15:18:32Z)

Thanks for the report @ye-luo.  Can you please add which GPU and OS you are using?

---

### 评论 #3 — ye-luo (2021-09-14T15:35:22Z)

Ubuntu 20.4. Radeon VII. Why GPU matters, I don't need a GPU to compile code.

---

### 评论 #4 — ROCmSupport (2021-11-16T09:26:13Z)

Hi @ye-luo 
Good news. This issue is tracked and fixed as part of 4.5, can you please verify and update asap.
Thank you.

---

### 评论 #5 — ye-luo (2021-11-16T20:11:06Z)

4.5 is good

---
