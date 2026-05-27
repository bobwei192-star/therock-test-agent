# OpenCL runtime returns improper values for max work items per dimension

> **Issue #58**
> **状态**: closed
> **创建时间**: 2016-12-18T21:05:13Z
> **更新时间**: 2017-07-02T17:16:07Z
> **关闭时间**: 2017-07-02T17:16:07Z
> **作者**: ekondis
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/58

## 描述

I'm experimenting with the ROCm v1.4 OpenCL preview runtime on a R9-Nano GPU.

clinfo returns for the GPU:
```
...
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
...
```

I think it would be proper for "Max work items[x]"(CL_DEVICE_MAX_WORK_ITEM_SIZES) to be 256 instead of 1024. That's the case for the Windows driver on the same system, btw.


---

## 评论 (12 条)

### 评论 #1 — oscarbg (2016-12-19T05:46:15Z)

Can you post full clinfo output just for curiosity?
can check if device enqueue feature of OpenCL 2.0 works as ROCM OpenCL is said to support 2.0 kernel features..

---

### 评论 #2 — ekondis (2016-12-19T21:11:16Z)

Sure, here is the full output:

```
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (2300.5)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Fiji [Radeon R9 FURY / NANO Series]
  Device Topology:                               PCI[ B#1, D#0, F#0 ]
  Max compute units:                             64
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           1000Mhz
  Address bits:                                  64
  Max memory allocation:                         3221225472
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    29440
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     No
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            4294967296
  Constant buffer size:                          3221225472
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            0
  Max pipe active reservations:                  0
  Max pipe packet size:                          0
  Max global variable size:                      3221225472
  Max global variable preferred total size:      4294967296
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
  SVM capabilities:
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7f7273868198
  Name:                                          gfx803
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                1.1 (HSA,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images
```


---

### 评论 #3 — oscarbg (2016-12-20T01:11:53Z)

Many thanks!

Interesting it has three diferent versions:
Device OpenCL C version:                       OpenCL C 2.0
Driver version:                                1.1 (HSA,LC)
Version:                                       OpenCL 1.2

driver version shouldn't be interesting but the other seem to assert what
AMD said..
also interesting to note for me is:

*no kernel enqueue support (Max on device queues:
0)

*SVM->Fine grain buffer:                           Yes
when AMD has said doesn't support it!

*Extensions lacking vs "Windows CL driver".. At least:
cl_khr_fp16  cl_khr_gl_depth_images cl_khr_image2d_from_buffer cl_khr_spir
cl_khr_gl_event cl_khr_mipmap_image cl_khr_mipmap_image_writes
cl_amd_liquid_flash
interesting AMDGPU Pro 16.50 CL driver ships with these extensions also?

*also as noted SPIR extension lacking but given CL compiler is based on
clang and there are branches now on Khronos having SPIR-V compilation
(which is a feature of OpenCL 2.1) let's hope we will have this support
also soon on this ROCM driver..



2016-12-19 22:11 GMT+01:00 Elias <notifications@github.com>:

> Sure, here is the full output:
>
> Number of platforms:                             1
>   Platform Profile:                              FULL_PROFILE
>   Platform Version:                              OpenCL 2.0 AMD-APP (2300.5)
>   Platform Name:                                 AMD Accelerated Parallel Processing
>   Platform Vendor:                               Advanced Micro Devices, Inc.
>   Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices
>
>
>   Platform Name:                                 AMD Accelerated Parallel Processing
> Number of devices:                               1
>   Device Type:                                   CL_DEVICE_TYPE_GPU
>   Vendor ID:                                     1002h
>   Board name:                                    Fiji [Radeon R9 FURY / NANO Series]
>   Device Topology:                               PCI[ B#1, D#0, F#0 ]
>   Max compute units:                             64
>   Max work items dimensions:                     3
>     Max work items[0]:                           1024
>     Max work items[1]:                           1024
>     Max work items[2]:                           1024
>   Max work group size:                           256
>   Preferred vector width char:                   4
>   Preferred vector width short:                  2
>   Preferred vector width int:                    1
>   Preferred vector width long:                   1
>   Preferred vector width float:                  1
>   Preferred vector width double:                 1
>   Native vector width char:                      4
>   Native vector width short:                     2
>   Native vector width int:                       1
>   Native vector width long:                      1
>   Native vector width float:                     1
>   Native vector width double:                    1
>   Max clock frequency:                           1000Mhz
>   Address bits:                                  64
>   Max memory allocation:                         3221225472
>   Image support:                                 Yes
>   Max number of images read arguments:           128
>   Max number of images write arguments:          8
>   Max image 2D width:                            16384
>   Max image 2D height:                           16384
>   Max image 3D width:                            2048
>   Max image 3D height:                           2048
>   Max image 3D depth:                            2048
>   Max samplers within kernel:                    29440
>   Max size of kernel argument:                   1024
>   Alignment (bits) of base address:              1024
>   Minimum alignment (bytes) for any datatype:    128
>   Single precision floating point capability
>     Denorms:                                     No
>     Quiet NaNs:                                  Yes
>     Round to nearest even:                       Yes
>     Round to zero:                               Yes
>     Round to +ve and infinity:                   Yes
>     IEEE754-2008 fused multiply-add:             Yes
>   Cache type:                                    Read/Write
>   Cache line size:                               64
>   Cache size:                                    16384
>   Global memory size:                            4294967296
>   Constant buffer size:                          3221225472
>   Max number of constant args:                   8
>   Local memory type:                             Scratchpad
>   Local memory size:                             65536
>   Max pipe arguments:                            0
>   Max pipe active reservations:                  0
>   Max pipe packet size:                          0
>   Max global variable size:                      3221225472
>   Max global variable preferred total size:      4294967296
>   Max read/write image args:                     64
>   Max on device events:                          0
>   Queue on device max size:                      0
>   Max on device queues:                          0
>   Queue on device preferred size:                0
>   SVM capabilities:
>     Coarse grain buffer:                         Yes
>     Fine grain buffer:                           Yes
>     Fine grain system:                           No
>     Atomics:                                     No
>   Preferred platform atomic alignment:           0
>   Preferred global atomic alignment:             0
>   Preferred local atomic alignment:              0
>   Kernel Preferred work group size multiple:     64
>   Error correction support:                      0
>   Unified memory for Host and Device:            0
>   Profiling timer resolution:                    1
>   Device endianess:                              Little
>   Available:                                     Yes
>   Compiler available:                            Yes
>   Execution capabilities:
>     Execute OpenCL kernels:                      Yes
>     Execute native function:                     No
>   Queue on Host properties:
>     Out-of-Order:                                No
>     Profiling :                                  Yes
>   Queue on Device properties:
>     Out-of-Order:                                No
>     Profiling :                                  No
>   Platform ID:                                   0x7f7273868198
>   Name:                                          gfx803
>   Vendor:                                        Advanced Micro Devices, Inc.
>   Device OpenCL C version:                       OpenCL C 2.0
>   Driver version:                                1.1 (HSA,LC)
>   Profile:                                       FULL_PROFILE
>   Version:                                       OpenCL 1.2
>   Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/58#issuecomment-268079585>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAo2eS8qTd9JEnNvtzWdhUuKIsMVtLj4ks5rJvL2gaJpZM4LQO9F>
> .
>


---

### 评论 #4 — gstoner (2016-12-20T01:45:00Z)


Elias,  it not a mistake there is nothing in the spec that limits them to 256.   1024 is also correct answer.

Greg

On Dec 19, 2016, at 7:11 PM, Oscar Barenys <notifications@github.com<mailto:notifications@github.com>> wrote:

Many thanks!

Interesting it has three diferent versions:
Device OpenCL C version: OpenCL C 2.0
Driver version: 1.1 (HSA,LC)
Version: OpenCL 1.2

driver version shouldn't be interesting but the other seem to assert what
AMD said..
also interesting to note for me is:

*no kernel enqueue support (Max on device queues:
0)

*SVM->Fine grain buffer: Yes
when AMD has said doesn't support it!

*Extensions lacking vs "Windows CL driver".. At least:
cl_khr_fp16 cl_khr_gl_depth_images cl_khr_image2d_from_buffer cl_khr_spir
cl_khr_gl_event cl_khr_mipmap_image cl_khr_mipmap_image_writes
cl_amd_liquid_flash
interesting AMDGPU Pro 16.50 CL driver ships with these extensions also?

*also as noted SPIR extension lacking but given CL compiler is based on
clang and there are branches now on Khronos having SPIR-V compilation
(which is a feature of OpenCL 2.1) let's hope we will have this support
also soon on this ROCM driver..



2016-12-19 22:11 GMT+01:00 Elias <notifications@github.com<mailto:notifications@github.com>>:

> Sure, here is the full output:
>
> Number of platforms: 1
> Platform Profile: FULL_PROFILE
> Platform Version: OpenCL 2.0 AMD-APP (2300.5)
> Platform Name: AMD Accelerated Parallel Processing
> Platform Vendor: Advanced Micro Devices, Inc.
> Platform Extensions: cl_khr_icd cl_amd_event_callback cl_amd_offline_devices
>
>
> Platform Name: AMD Accelerated Parallel Processing
> Number of devices: 1
> Device Type: CL_DEVICE_TYPE_GPU
> Vendor ID: 1002h
> Board name: Fiji [Radeon R9 FURY / NANO Series]
> Device Topology: PCI[ B#1, D#0, F#0 ]
> Max compute units: 64
> Max work items dimensions: 3
> Max work items[0]: 1024
> Max work items[1]: 1024
> Max work items[2]: 1024
> Max work group size: 256
> Preferred vector width char: 4
> Preferred vector width short: 2
> Preferred vector width int: 1
> Preferred vector width long: 1
> Preferred vector width float: 1
> Preferred vector width double: 1
> Native vector width char: 4
> Native vector width short: 2
> Native vector width int: 1
> Native vector width long: 1
> Native vector width float: 1
> Native vector width double: 1
> Max clock frequency: 1000Mhz
> Address bits: 64
> Max memory allocation: 3221225472
> Image support: Yes
> Max number of images read arguments: 128
> Max number of images write arguments: 8
> Max image 2D width: 16384
> Max image 2D height: 16384
> Max image 3D width: 2048
> Max image 3D height: 2048
> Max image 3D depth: 2048
> Max samplers within kernel: 29440
> Max size of kernel argument: 1024
> Alignment (bits) of base address: 1024
> Minimum alignment (bytes) for any datatype: 128
> Single precision floating point capability
> Denorms: No
> Quiet NaNs: Yes
> Round to nearest even: Yes
> Round to zero: Yes
> Round to +ve and infinity: Yes
> IEEE754-2008 fused multiply-add: Yes
> Cache type: Read/Write
> Cache line size: 64
> Cache size: 16384
> Global memory size: 4294967296
> Constant buffer size: 3221225472
> Max number of constant args: 8
> Local memory type: Scratchpad
> Local memory size: 65536
> Max pipe arguments: 0
> Max pipe active reservations: 0
> Max pipe packet size: 0
> Max global variable size: 3221225472
> Max global variable preferred total size: 4294967296
> Max read/write image args: 64
> Max on device events: 0
> Queue on device max size: 0
> Max on device queues: 0
> Queue on device preferred size: 0
> SVM capabilities:
> Coarse grain buffer: Yes
> Fine grain buffer: Yes
> Fine grain system: No
> Atomics: No
> Preferred platform atomic alignment: 0
> Preferred global atomic alignment: 0
> Preferred local atomic alignment: 0
> Kernel Preferred work group size multiple: 64
> Error correction support: 0
> Unified memory for Host and Device: 0
> Profiling timer resolution: 1
> Device endianess: Little
> Available: Yes
> Compiler available: Yes
> Execution capabilities:
> Execute OpenCL kernels: Yes
> Execute native function: No
> Queue on Host properties:
> Out-of-Order: No
> Profiling : Yes
> Queue on Device properties:
> Out-of-Order: No
> Profiling : No
> Platform ID: 0x7f7273868198
> Name: gfx803
> Vendor: Advanced Micro Devices, Inc.
> Device OpenCL C version: OpenCL C 2.0
> Driver version: 1.1 (HSA,LC)
> Profile: FULL_PROFILE
> Version: OpenCL 1.2
> Extensions: cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/58#issuecomment-268079585>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAo2eS8qTd9JEnNvtzWdhUuKIsMVtLj4ks5rJvL2gaJpZM4LQO9F>
> .
>

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/58#issuecomment-268125357>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Due9eUiFoF9ottbF53NLYqXRWWMzwks5rJytbgaJpZM4LQO9F>.



---

### 评论 #5 — ekondis (2016-12-20T13:16:59Z)

Greg, this is certainly not a specification limitation. However, since the AMD hardware allows a maximum workgroup size of 256 workitems is there any meaning for reporting a greater number as the maximum allowed for each workgroup dimension?

I noticed this issue because I tested an application which launches 1D workgroups of size equal to the maximum allowed for the 1st dimension (1024, 1, 1) and as such it reported an error as AMD hardware does not allow workgroups with more than 256 workitems.


---

### 评论 #6 — jedwards-AMD (2017-01-03T19:11:19Z)

I can directly run HSA applications (vector_copy) using dimension sizes of 1024. I suspect that the 256 workitem size is a false limitation imposed by the OpenCL implementation. It reports the capabilities of the hardware correctly, but it is limiting the execution size. What application did you test that enforced the 256 workitem limit?

---

### 评论 #7 — ekondis (2017-01-04T08:27:19Z)

It seems that the restriction persists. I tested one of my own OpenCL applications and if I choose to launch a kernel with more than 256 workitems, let's say 64x8=512 workitems, the clEnqueueNDRangeKernel() call returns CL_INVALID_WORK_GROUP_SIZE error.

---

### 评论 #8 — jedwards-AMD (2017-01-04T16:28:39Z)

How was your kernel compiled? Did you specify a required workgroup size? What are the values returned for CL_KERNEL_COMPILE_WORK_GROUP_SIZE and is there a  __attribute__((reqd_work_group_size(X, Y, Z))) qualifier? This may not be a device limitation, but a kernel limitation.

---

### 评论 #9 — gstoner (2017-01-04T16:49:23Z)

Guys, 
   So 256 as Workgroup size is not a hardware limitation, this was a historical limit in our driver and compiler back in the Evergreen days.    Note our driver for  Direct Compute supported default size of 1024.   Our hardware can support up to 2048 Workgroup size with some limitations technically. 

The issue you are seeing above is the Kernel need to compiled for the workgroup size that you want and the runtime run will be specified at as well.  By the Spec, the issue you are seeing when you get a mismatch in workgroup size for runtime and kernel should report the wrong workgroup size. 

Note this is on purpose we have been looking at other Workgroup size with OpenCL as we look at Deep Learning solutions.   Remember the current ROCm driver is optimized for Server Class work.  

---

### 评论 #10 — ekondis (2017-01-05T10:13:21Z)

Thanks for the feedback.

First, there is no such applied attribute qualifier (`reqd_work_group_size`) used. I was concerned if the register usage does permit 512 sized workgroups but it seems not to be a complex kernel. I'll probably write a simple test case for testing the error code of various invocations with different workgroup sizes.

Now, my question is if 1024 sized workgroups are permitted then why the reported maximum workgroup size in clinfo is 256 (`CL_DEVICE_MAX_WORK_GROUP_SIZE`)?

---

### 评论 #11 — jedwards-AMD (2017-01-05T15:42:11Z)

Having a reported maximum workgroup size in clinfo is of 256 ( CL_DEVICE_MAX_WORK_GROUP_SIZE ) would appear to be a defect. I will consult the appropriate engineer about this issue.

---

### 评论 #12 — ekondis (2017-05-22T17:52:02Z)

Current ROCm (v1.5) seems to settle to 256 workitems per workgroup as maximum:

```
  Max work item sizes                             256x256x256
  Max work group size                             256
```



---
