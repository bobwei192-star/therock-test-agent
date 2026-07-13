# Honor __HIP_PLATFORM_AMD__ in all ROCM components

- **Issue #:** 1566
- **State:** closed
- **Created:** 2021-08-26T01:10:04Z
- **Updated:** 2021-11-16T20:11:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/1566

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