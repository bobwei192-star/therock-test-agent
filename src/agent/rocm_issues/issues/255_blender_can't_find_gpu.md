# blender can't find gpu

> **Issue #255**
> **状态**: closed
> **创建时间**: 2017-11-17T06:29:44Z
> **更新时间**: 2018-06-03T16:24:06Z
> **关闭时间**: 2018-06-03T15:10:18Z
> **作者**: extraymond
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/255

## 描述

Greetings. 

I'm running ubuntu 16.04 with rocm enabled with a rx 480.
Clinfo showed that I'm having opencl running correctly. But blender somehow can't find my gpu's while luxmark can.

Here's the clinfo output if anyone is interested.

---

```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (2508.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx803
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  1.1 (HSA,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Max compute units                               36
  Max clock frequency                             1342MHz
  Device Partition                                (core)
    Max number of sub-devices                     36
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size multiple              64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              8589934592 (8GiB)
  Error Correction support                        No
  Max memory allocation                           7301444403 (6.8GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26591
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max constant buffer size                        7301444403 (6.8GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.8
  ICD loader Profile                              OpenCL 1.2
	NOTE:	your OpenCL library declares to support OpenCL 1.2,
		but it seems to support up to OpenCL 2.1 too.

```


---

## 评论 (8 条)

### 评论 #1 — extraymond (2018-03-13T00:09:00Z)

Blender can find my gpu now!
Although opencl is still not working in blender, this can be closed.

---

### 评论 #2 — extraymond (2018-06-03T15:23:49Z)

Greetings, may I understand why this issue is closed? I'm still having the issue.
It may be better to leave the status or operation for this issue. So people can learn something from this instead of spamming the same error.

Thx.

---

### 评论 #3 — gstoner (2018-06-03T15:45:31Z)

This is duplicate we have other Blender open issue. Note we have Blender talking to GPU, some scene have slow compile times since they implementing  functions support 

---

### 评论 #4 — gstoner (2018-06-03T15:46:01Z)

It OpenCL loaded you have path issue for Blender. 

---

### 评论 #5 — extraymond (2018-06-03T15:49:49Z)

Thx for the update!

It would be nice to mark duplicate before closing this. This would allow information to be shareable between duplicated issues. I reckon marking duplicates would make managing project as big as ROCM a lot easier. And people can volunteer to help you sort things out even if they are not that familiar with technical issues.

---

### 评论 #6 — gstoner (2018-06-03T15:51:37Z)

Your having issue of Gromacs finding the GPU we have user who have Gromacs using the GPU already.  This is more of application install issue, not ROCm issue that your reporting. 

---

### 评论 #7 — gstoner (2018-06-03T16:14:41Z)

@extraymond  Before you reported this did you test to see if other opencl application could compile and run. 

---

### 评论 #8 — extraymond (2018-06-03T16:24:06Z)

When the time I first reported this issue, opencl was already working in my setup.
After some point between ROCM 1.7-1.8, blender start to be able to find my gpu.

As of not working, I mean the part that blender can't use opencl. I agree that should be taken in another issue #316 (Thx for mentioning it)

---
