# RX Vega56 Only: Installed Driver 17.30 for Linux & ROCm 1.6-148 clinfo outputs: Number of platforms 0

> **Issue #216**
> **状态**: closed
> **创建时间**: 2017-09-28T13:34:54Z
> **更新时间**: 2018-02-03T22:01:50Z
> **关闭时间**: 2017-10-18T13:09:27Z
> **作者**: MoneroCrusher
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/216

## 描述

I have a Vega 56 installed in my system and it is even recognized in "About this Computer" as Radeon RX Vega.
Why is Number of platforms = 0?
I need OpenCl to be recognized for mining (got a problem in XMR-STAK-AMD)

I hope you can help me

---

## 评论 (87 条)

### 评论 #1 — gstoner (2017-09-29T12:08:33Z)

Right now we see the issue in the forum with Consumer RX Vega56, we looking into,  the consumer group did not send us final hardware prior to shipping.      ROCm is testing on Frontier, MI25  Vega10 extensively.    We are working on a new ROCm release for the next two weeks, we see what we can do pull the fix in for this, once we settle down on the issue.  

---

### 评论 #2 — MoneroCrusher (2017-09-29T23:14:21Z)

Is that problem only occuring on Vega 56 or also Vega 64?
If not:
Would it help to flash Vega 56 with 64 BIOS? Or would that change nothing?
Thanks for your effort
I hope you can resolve this issue soon
Btw: will the linux driver have HBCC support and maybe even a Wattman like feature? Or where should I be looning for that?
Kind regards

---

### 评论 #3 — gstoner (2017-09-29T23:53:37Z)

No that would not help,  this looking to be 56 CU only issue,  We are checking out new firmware package that will be part of 1.6.4 to see it address the issue.  We  hoping to finally release 1.6.4 next week.

Greg

On Sep 29, 2017, at 6:14 PM, MoneroCrusher <notifications@github.com<mailto:notifications@github.com>> wrote:


Is that problem only occuring on Vega 56 or also Vega 64?
If not:
Would it help to flash Vega 56 with 64 BIOS? Or would that change nothing?
Thanks for your effort
I hope you can resolve this issue soon
Btw: will the linux driver have HBCC support and maybe even a Wattman like feature? Or where should I be looning for that?
Kind regards

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/216#issuecomment-333259855>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQD1Sapj2STi0k_Hwwmg4OWsVfaqks5snXnOgaJpZM4PnRmZ>.



---

### 评论 #4 — MoneroCrusher (2017-09-30T18:07:14Z)

So next week with 1.6.4 I should be able to use OpenCL with Vega 56 and can start mining on Linux?

---

### 评论 #5 — MoneroCrusher (2017-09-30T20:24:58Z)

Another user seems to have the sae problem but with a Vega 64 card

---

### 评论 #6 — gstoner (2017-09-30T22:48:44Z)

The CLinfo issue on 64 CU card they were using the wrong CPU.  

---

### 评论 #7 — gstoner (2017-09-30T22:51:47Z)

This is CLINFO working  MI25 ( Vega10 64 CU)  system running ROCm 1.6.3 with KFD-148  on Ubuntu 16.04 sp2 

server1:/opt/rocm/opencl/bin/x86_64$ ./clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (2450.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 4
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Device 6860
  Device Topology:				 PCI[ B#6, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1500Mhz
  Address bits:					 64
  Max memory allocation:			 12872318976
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26720
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 12872318976
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 12872318976
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7fcfc4f53598
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 1.1 (HSA,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 


  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Device 6860
  Device Topology:				 PCI[ B#35, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1500Mhz
  Address bits:					 64
  Max memory allocation:			 12872318976
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26720
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 12872318976
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 12872318976
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7fcfc4f53598
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 1.1 (HSA,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 


  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Device 6860
  Device Topology:				 PCI[ B#67, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1500Mhz
  Address bits:					 64
  Max memory allocation:			 12872318976
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26720
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 12872318976
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 12872318976
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7fcfc4f53598
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 1.1 (HSA,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 


  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Device 6860
  Device Topology:				 PCI[ B#99, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1500Mhz
  Address bits:					 64
  Max memory allocation:			 12872318976
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26720
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 12872318976
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 12872318976
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7fcfc4f53598
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 1.1 (HSA,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 


---

### 评论 #8 — MoneroCrusher (2017-09-30T23:04:06Z)

Sorry I don't get your answer. Does this mean Vega 56 & 64 can run OpenCL as of now or not?
If yes, what did I do wrong?

---

### 评论 #9 — gstoner (2017-10-01T14:04:28Z)

Vega 10 with 64 CU work today,  we trying to understand why the commercial 56 CU board are showing an issue.    Which I have said multiple times 

---

### 评论 #10 — MoneroCrusher (2017-10-01T14:56:53Z)

What kernel are you using?

---

### 评论 #11 — gstoner (2017-10-01T15:18:08Z)

Follow these instructions exactly  it will install 4.11 Linux kernel with all the patches needed 
https://rocm.github.io/ROCmInstall.html to run on Ubuntu 16.04 sp2

I am running, the stock set up from ROCm 1.6.3 using the instruction above 

~$ uname -r
4.11.0-kfd-compute-rocm-rel-1.6-148

---

### 评论 #12 — MoneroCrusher (2017-10-01T19:41:29Z)

Ok I got a good clinfo output on the Vega 64 card now

```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (2450.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  1.1 (HSA,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Max compute units                               64
  Max clock frequency                             1630MHz
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (n/a)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
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
  Global memory size                              8573157376 (7.984GiB)
  Error Correction support                        No
  Max memory allocation                           6429868032 (5.988GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26751
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max constant buffer size                        6429868032 (5.988GiB)
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
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.8
  ICD loader Profile                              OpenCL 1.2
	NOTE:	your OpenCL library declares to support OpenCL 1.2,
		but it seems to support up to OpenCL 2.1 too.
```

However, after I install 17.30 driver my clinfo output says
Number of platforms 0

is there a conflict between the two?

xmr-stak-amd had the following error when only trying to run it with ROCm (driver 17-30 not installed yet):
```
[2017-10-01 23:49:00] : Compiling code and initializing GPUs. This will take a while...
[2017-10-01 23:49:00] : Device 0 work size 8 / 256.
clang version 4.0 
Target: amdgcn-amd-amdhsa-opencl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
[2017-10-01 23:49:03] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram.
Build log:
warning: argument unused during compilation: '-I .'
error: unable to execute command: Segmentation fault (core dumped)
error: clang frontend command failed due to signal (use -v to see invocation)
note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated run script.
note: diagnostic msg: Error generating preprocessed source(s) - no preprocessable inputs.
/opt/rocm/opencl/bin/x86_64/clang[0x223cbca]
/opt/rocm/opencl/bin/x86_64/clang[0x223af5e]
/opt/rocm/opencl/bin/x86_64/clang[0x223b0b0]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x11390)[0x7fc4b7d3a390]
/opt/rocm/opencl/bin/x86_64/clang[0x1448e94]
/opt/rocm/opencl/bin/x86_64/clang[0x1429b81]
/opt/rocm/opencl/bin/x86_64/clang[0x17d2677]
/opt/rocm/opencl/bin/x86_64/clang[0x218586a]
/opt/rocm/opencl/bin/x86_64/clang[0x2185903]
/opt/rocm/opencl/bin/x86_64/clang[0x21862ff]
/opt/rocm/opencl/bin/x86_64/clang[0x58f356]
/opt/rocm/opencl/bin/x86_64/clang[0x5917d3]
/opt/rocm/opencl/bin/x86_64/clang[0x56da79]
/opt/rocm/opencl/bin/x86_64/clang[0x90093e]
/opt/rocm/opencl/bin/x86_64/clang[0x8d345d]
/opt/rocm/opencl/bin/x86_64/clang[0x568e5d]
/opt/rocm/opencl/bin/x86_64/clang[0x565dc8]
/opt/rocm/opencl/bin/x86_64/clang[0x5189d9]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7fc4b797f830]
/opt/rocm/opencl/bin/x86_64/clang[0x55fde1]
Stack dump:
0.	Program arguments: /opt/rocm/opencl/bin/x86_64/clang -cc1 -triple amdgcn-amd-amdhsa-opencl -emit-obj -disable-free -disable-llvm-verifier -discard-value-names -main-file-name t_5220_66.bc -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -target-cpu gfx900 -dwarf-column-info -debugger-tuning=gdb -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -O3 -fdebug-compilation-dir /home/monero/xmr-stak-amd/bin -ferror-limit 19 -fmessage-length 80 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -vectorize-loops -vectorize-slp -mllvm -amdgpu-internalize-symbols -mllvm -amdgpu-early-inline-all -o /tmp/t_5220_66-49a06d.o -x ir /tmp/AMD_5220_53/t_5220_66.bc 
1.	Code generation
2.	Running pass 'Function Pass Manager' on module '/tmp/AMD_5220_53/t_5220_66.bc'.
3.	Running pass 'SI Fix SGPR copies' on function '@cn0'
Error: Creating the executable failed: Compiling LLVM IRs to executable
```
Do you know what's causing this? Is it trivial?

---

### 评论 #13 — MoneroCrusher (2017-10-01T20:02:54Z)

Actually:
Both my Vega 56 and also my Vega 64 are being recognized by clinfo. I just installed Vega 56 and 64 in the same system.

clinfo:

```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (2450.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 2
  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  1.1 (HSA,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Max compute units                               56
  Max clock frequency                             1590MHz
  Device Partition                                (core)
    Max number of sub-devices                     56
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (n/a)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
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
  Global memory size                              8573157376 (7.984GiB)
  Error Correction support                        No
  Max memory allocation                           6429868032 (5.988GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26751
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max constant buffer size                        6429868032 (5.988GiB)
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
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 

  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  1.1 (HSA,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Max compute units                               64
  Max clock frequency                             1630MHz
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (n/a)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
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
  Global memory size                              8573157376 (7.984GiB)
  Error Correction support                        No
  Max memory allocation                           6429868032 (5.988GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26751
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max constant buffer size                        6429868032 (5.988GiB)
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
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (2)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
    Device Name                                   gfx900
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (2)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
    Device Name                                   gfx900

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.8
  ICD loader Profile                              OpenCL 1.2
	NOTE:	your OpenCL library declares to support OpenCL 1.2,
		but it seems to support up to OpenCL 2.1 too.
```

---

### 评论 #14 — MoneroCrusher (2017-10-01T20:13:54Z)

#209

---

### 评论 #15 — gstoner (2017-10-01T20:47:31Z)

That is great..  Note  #209 is on 17.30 AMDGPUpro driver which is using an older version of OpenCL and ROCm.  

---

### 评论 #16 — MoneroCrusher (2017-10-01T20:52:10Z)

So with ROCm-only install both Vega 56 and 64 are working under 4.11.0-kfd-compute-rocm-rel-1.6-148
but we get the same "warning: argument unused during compilation: '-I .'" error when starting program.
Any idea how I can start xmr-stak-amd without all those errors?

---

### 评论 #17 — MoneroCrusher (2017-10-01T20:53:11Z)

https://github.com/fireice-uk/xmr-stak-amd/issues/48

---

### 评论 #18 — MoneroCrusher (2017-10-01T21:29:08Z)

also when the crash happens I get this report from the system:
![screenshot from 2017-10-01 23-23-08](https://user-images.githubusercontent.com/32360383/31059177-4fbcd146-a700-11e7-9755-4ec617255a38.png)


---

### 评论 #19 — OhGodAPet (2017-10-02T04:23:30Z)

That's an issue from my public kernel, which the xmr-stak dev ripped off - the new compiler stack doesn't like part of it, and actually causes compilation to fail, even though it's legal OpenCL C.

---

### 评论 #20 — MoneroCrusher (2017-10-02T04:29:39Z)

gstoner got it to work with their new opencl project check https://github.com/fireice-uk/xmr-stak-amd/issues/48
Do you know if there would be a simple fix for your public kernel with the new compiler stack?
Or do I need for gstoner and his team to roll out new opencl?

---

### 评论 #21 — OhGodAPet (2017-10-02T06:24:20Z)

Neither - I highly down the new ROCm version is going to have that specific bug fixed - it's in the toolchain.

---

### 评论 #22 — gstoner (2017-10-02T12:37:25Z)

 The next release of stack fixes the issue with fireice-uk/xmr-stak-amd#48. We have it compiling and running in-house.  

---

### 评论 #23 — MoneroCrusher (2017-10-02T13:00:16Z)

Nice! When is it coming out?
Would it be possible for you to give me the relevant file(s) so I can compile it myself and start mining today?
My vegas are getting dusty in the corner ;)

---

### 评论 #24 — gstoner (2017-10-02T13:21:53Z)

Soon.  and no we can not release bits early. 

---

### 评论 #25 — MoneroCrusher (2017-10-02T13:41:00Z)

Can't wait! Maybe this week?
Btw is HBCC supported on linux? Or will it be supported soon?

---

### 评论 #26 — OhGodAPet (2017-10-03T02:01:57Z)

I pray the ROCK kernel has been updated too - the current one cripples any sort of memory read from a compute kernel.

---

### 评论 #27 — RedChina1949 (2017-10-03T10:39:53Z)

We are having exactly the same issues here... We really hope that it will be released soon, 
and even more important: is **HBCC** supported on Linux then? 

thanks for your effort!

---

### 评论 #28 — gstoner (2017-10-03T11:30:34Z)

@RedChina1949  What benefit are you expecting from HBCC?    

---

### 评论 #29 — RedChina1949 (2017-10-03T11:34:40Z)

@gstoner a supposedly better hashrate in mining monero 

---

### 评论 #30 — gstoner (2017-10-03T11:40:03Z)

HBCC what it does increase available memory to your GPU by swapping memory pools from main memory into Local GPU Memory when your problem set of larger than the memory on the card, it is transparent to you.     It is like Paging in the OS.   

@OhGodAPet is your GPU a Frontier Edition  

---

### 评论 #31 — RedChina1949 (2017-10-03T15:55:50Z)

@gstoner thanks a lot for your reply friend! So it doesn't matter on Linux then? I read reviews ( https://www.reddit.com/r/MoneroMining/comments/6yvpm8/vega_mining_guide/ for example ) where the hashrate with windows was around **1300-1400 H/s without HBCC and 1800+ H/s with activated HBCC**, so I was worried that this hashrate can't be achieved on Linux without HBCC. I have 13 Vega 56s installed per mainboard, that's why I want to use Linux as OS.

---

### 评论 #32 — gstoner (2017-10-03T16:09:50Z)

We look and see what really going on with Windows Driver with HBCC, especially with the cycling of page retry. 

---

### 评论 #33 — kisow (2017-10-03T17:48:20Z)

It seems that there is no **direct relation** between HBCC Memory Segment option and xmr hashrate.
I can achieve 1800+ H/s using RX VEGA 56 with deactivated HBCC Memory Segment option in windows.

I think that there is some bugs blockchain driver for windows with wattman.
Unless HBCC Memory Segment option is activate, wattman settings are released with hashrate drop after rebooting. So many people say that HBCC Memory Segment option need to be activated for RX VEGA.

By the way, HBCC Memory Segment option can NOT be activated with system memory less than 9893MB :(
so, including my system, most mining rigs that have 4GB system memory can NOT activate that option to avoid that bug. :(

I also look forward to amd driver for linux that is equivalent window's blockchain driver.
And please make GPU usage functionality to rocm-smi like as nvidia-smi

I'm sorry for poor explain because I have very poor english.

---

### 评论 #34 — gstoner (2017-10-03T18:22:41Z)

That is what I was wondering we found turning off  HBCC ( Page Retry) off with heavy optimized algorithm gave the best performance. 

---

### 评论 #35 — ekondis (2017-10-03T20:04:31Z)

@gstoner Could HBCC be leveraged in order to provide a similar page faulting support as on GP100 GPU or that wouldn't be possible on current hardware?

---

### 评论 #36 — MoneroCrusher (2017-10-03T22:14:05Z)

@gstoner
I would be really glad if you could provide us with an estimated date for the next ROCm release, my hardware choice is depending on it, and I need to decide whether I should wait for Linux or invest in more hardware and go the windows/pain in the ass route.

Like 2-3 days? 1 week? 2 weeks? 1 month? Longer?

Thank you!

---

### 评论 #37 — OhGodAPet (2017-10-11T01:35:37Z)

@gstoner The issue was fixed with the roc-1.6.3 tag on the ROCK-Kernel-Driver repo... but that segfaults on load if my Vega 64 is also in the rig. xD

---

### 评论 #38 — rhlug (2017-10-11T02:27:47Z)

@OhGodAPet  I find that rx470 + vega56 will boot, but kfd can only load the vega.  rx470+rx570+vega56 will kernel panic on boot.   rx470+rx570 works, and vega56 alone works.  But mixing them on rocm 1.6.148 is a no-go.    this is on a ryzen 1700 w/ msi x370 mb, so those may be factors.  I should really try to replicate on my asrock+intel

---

### 评论 #39 — OhGodAPet (2017-10-11T02:52:41Z)

@rhlug Vega FE + Vega 64 == death. I could debug it, but... there's also the issue of the kernel getting REAL pissy if I change the DPM states (I only tried memory so far) to OC via the sysfs pp_table. It locks the memory to the lowest state. 

---

### 评论 #40 — rhlug (2017-10-11T14:11:57Z)

@OhGodAPet Right.  Any overwrite of pp_table locks sclk and mclk at level 0.  I reported this on issue 221 (https://github.com/RadeonOpenCompute/ROCm/issues/221).

With my vega56 in, I set the following before launching ethash.

/opt/rocm/bin/rocm-smi  -d 0 --setsclk 3
/opt/rocm/bin/rocm-smi  -d 0 --setmclk 3
echo 17 >  /sys/class/drm/card0/device/pp_mclk_od 

Which does work...

$ cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz 
1: 991Mhz 
2: 1138Mhz 
3: 1269Mhz *
4: 1312Mhz 
5: 1474Mhz 
6: 1538Mhz 
7: 1590Mhz 

$ cat /sys/class/drm/card0/device/pp_dpm_mclk 
0: 167Mhz 
1: 500Mhz 
2: 700Mhz 
3: 936Mhz *

And gives me 38.5-39mh/s on ubiq.


---

### 评论 #41 — rhlug (2017-10-16T04:30:46Z)

Well, would you look at that...   Vega56 with xmr-stak-amd on Ubuntu 16.04
 
```./xmr-stak-amd 
[2017-10-15 23:28:42] : Compiling code and initializing GPUs. This will take a while...
[2017-10-15 23:28:43] : Device 0 work size 8 / 256.
[2017-10-15 23:28:49] : Device 0 work size 8 / 256.
-------------------------------------------------------------------
xmr-stak-amd 1.1.0-1.4.0-dev mining software, AMD Version.
AMD mining code was written by wolf9466.
Brought to you by fireice_uk under GPLv3.

Configurable dev donation level is set to 1.0 %

You can use following keys to display reports:
'h' - hashrate
'r' - results
'c' - connection
-------------------------------------------------------------------
[2017-10-15 23:28:55] : Starting GPU thread, no affinity.
[2017-10-15 23:28:55] : Starting GPU thread, no affinity.
[2017-10-15 23:28:55] : Connecting to pool pool.supportxmr.com:7777 ...
[2017-10-15 23:28:56] : Connected. Logging in...
[2017-10-15 23:28:56] : Difficulty changed. Now: 25000.
[2017-10-15 23:28:56] : New block detected.
[2017-10-15 23:29:07] : Result accepted by the pool.
HASHRATE REPORT
| ID |   10s |   60s |   15m | ID |   10s |   60s |   15m |
|  0 | 533.9 |  (na) |  (na) |  1 | 533.8 |  (na) |  (na) |
-----------------------------------------------------
Totals:   1067.7  (na)  (na) H/s
Highest:  0.0 H/s
RESULT REPORT
Difficulty       : 59190
Good results     : 4 / 4 (100.0 %)
Avg result time  : 23.0 sec
Pool-side hashes : 134190

```



---

### 评论 #42 — rhlug (2017-10-16T04:36:47Z)

@gstoner Please tell me 1.6.180 is not the next release!  

---

### 评论 #43 — rhlug (2017-10-16T05:06:10Z)

148 kernel and 180 userland allow me to tune core and mem frequencies and compile the cryptonight.cl kernel..   

Here are XMR rates on linux.  Sadly, no 1800-1900 like on Windows w/HBCC

```
HASHRATE REPORT
| ID |   10s |   60s |   15m | ID |   10s |   60s |   15m |
|  0 | 708.6 |  (na) |  (na) |  1 | 607.2 |  (na) |  (na) |
-----------------------------------------------------
Totals:   1315.8  (na)  (na) H/s
Highest:  1318.9 H/s
RESULT REPORT
Difficulty       : 25000
Good results     : 3 / 3 (100.0 %)
Avg result time  : 11.7 sec
Pool-side hashes : 75000
```

---

### 评论 #44 — MoneroCrusher (2017-10-16T08:32:56Z)

@rhlug wow awesome! Do you know why the lower hashrate? Let us know how you compiled that, please! 

---

### 评论 #45 — kisow (2017-10-16T11:16:12Z)

@rhlug Wow awesome! 
How do you make success building xmr-stak-amd against RX VEGA 56?
Do you have fixed cryptonight.cl for it? Btw, what is 180 userland?
Is 2MB fragment crucial to make it on par with Windows blockchain drivers?

---

### 评论 #46 — gstoner (2017-10-16T12:24:33Z)

ROCm 1.6.4 is rolling out this week. 

@rhlug  can you run this flag, it turns off Page Retry, which what they doing on windows to get better performance by shutting off HBCC 

sudo –s
echo 1 > /sys/module/amdkfd/parameters/noretry 

---

### 评论 #47 — rhlug (2017-10-16T13:19:58Z)

@gstoner  Only small increase it seems

noretry=0 1260-1270 h/s
noretry=1 1280-1290 h/s
 
(note speeds above are with intensity backed off a bit because I was having gpu crashes at 2016/1600 like I run on windows)

---

### 评论 #48 — rhlug (2017-10-16T13:35:31Z)

@MoneroCrusher I didnt have to re-compile xmr-stak-amd.  Once I installed the new rocm-opencl clang could compile the cryptonight.cl, which happens during startup of xmr-stak-amd.   

Sgminer-gm didnt have same luck..  I need to dig into that still.
```
[08:34:00] Building binary cryptonightgfx900gw8l8.bin                    
[08:34:07] Initialising kernel cryptonight.cl with nfactor 10, n 1024                    
[08:34:07] Error -46: Creating Kernel from program. (clCreateKernel)     
```

---

### 评论 #49 — rhlug (2017-10-16T14:21:19Z)

 https://github.com/RadeonOpenCompute/ROCm/issues/221 still present in rocm-1.6.180

If we cant modify clocks and undervolt via pp_table,  RX Vega on linux is severely crippled

---

### 评论 #50 — gstoner (2017-10-16T14:39:46Z)

You can modify clock,  but not voltage, this correct behavior.  Your asking for a new feature.  

---

### 评论 #51 — rhlug (2017-10-16T15:10:46Z)

@gstoner 
The pp_table on linux contains the same data that we edit on windows via the PP_PhmSoftPowerPlayTable key in 
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0001]

In that reg key, we easily change vddc to undervolt rx vega.   Making same changes to the pp_table in linux at /sys/class/drm/card0/device/pp_table  will break all powerplay functionality.  Core and mem get stuck at level 0 and only a reboot can save it.   

I dont see how I'm asking for a new feature here.

---

### 评论 #52 — MoneroCrusher (2017-10-16T23:10:55Z)

Undervolting really is essential. Why can't we just modify it like in windows?

---

### 评论 #53 — OhGodAPet (2017-10-17T21:21:12Z)

Please don't add voltage control! I'm doing just fine :3

---

### 评论 #54 — MoneroCrusher (2017-10-17T21:22:40Z)

@OhGodAPet do you get 1900 H/s like on windows? Wanna share a little info with us? ;-)

---

### 评论 #55 — gstoner (2017-10-17T22:19:38Z)

One thing this is all set up by the base Linux driver, in the PPLIB, so this where you find the logic https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/master/drivers/gpu/drm/amd/powerplay This same on all AMD Linux drivers

---

### 评论 #56 — OhGodAPet (2017-10-17T22:24:40Z)

@MoneroCrusher 

a) I'm not allowed to answer that.
b) I can modify voltage just fine.

---

### 评论 #57 — rhlug (2017-10-18T04:29:50Z)

@OhGodAPet your humblebrag is unbecoming.  If you have nothing of value to add, go toot your horn on bitcointalk

---

### 评论 #58 — OhGodAPet (2017-10-18T04:56:09Z)

@rhlug It's honestly not like that. I'm not allowed to speak on Vega results period - it doesn't mean that it is not attainable using simple methods. @gstoner pointed you damn near RIGHT to one method of doing it.

---

### 评论 #59 — MoneroCrusher (2017-10-18T08:11:51Z)

@OhGodAPet are you allowed to say that there is an equivalent of "HBCC" toggle in Linux as in Windows?
@gstoner
Thanks for the new release!
Regarding the volt modifications... could you be more specific for the unexperienced? I'm just trying to load hex code (like in windows) into some sort of PP table to undervolt my Vega 56

I'm sure dozens if not thousands of sre looking for that exact same answer

---

### 评论 #60 — OhGodAPet (2017-10-18T08:17:56Z)

@MoneroCrusher I can say this - first, I don't know about HBCC, because I don't use Windows.

I'm... probably overstepping my bounds a little here... >.> but...

drivers/gpu/drm/amd/powerplay/hwmgr/vega10_hwmgr.c -- there's a few ways to force the voltage to behave as you please in here. I limit its max, personally, but... IMO, it's not... *clean* like I want it to be. 

I plan to do a realtime method that doesn't rely on the driver at all, but doing it right takes a while.

---

### 评论 #61 — MoneroCrusher (2017-10-18T08:28:16Z)

@OhGodAPet thanks for the directions!
Will your tool be available/for sale?

---

### 评论 #62 — OhGodAPet (2017-10-18T08:50:15Z)

@MoneroCrusher I honestly don't know. If my owner lifts the restriction on Vega, I'll definitely consider it, but that's up to her.

---

### 评论 #63 — gstoner (2017-10-18T13:07:43Z)


@MoneroCrusher  take a look at this file and file near it to understand what going on https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/7a8d764bced9ed5c2e60ac2c3c820f0f77b902eb/drivers/gpu/drm/amd/powerplay/hwmgr/processpptables.c

---

### 评论 #64 — MoneroCrusher (2017-10-18T13:17:20Z)

@rhlug do these informations help you get further in narrowing down voltage solution for Vega cards in Linux? If they do please let me know! Because I have zero to none knowledge in coding..

@gstoner @OhGodAPet thanks for the informations!
Could you maybe tell me from the top of your head what I would have to do to set min fanspeed to 2500, msx 4900, target temp to 65, max temp to 80, mem freq to 920-940, mem voltagw to 850-920mV, frequencies to 1408 & 1360 with corresponding P0-P7 states from 810 to 880mV and "general voltage" to manual? And HBCC on (to simulate Windows performance?)

Should I create a new feature request or How-to guide only for that?

---

### 评论 #65 — boxerab (2017-10-18T23:12:50Z)

Reddit thread on getting highest hash rate on Vega 56 and 64

https://www.reddit.com/r/MoneroMining/comments/74hjqn/monero_and_vega_the_definitive_guide/

---

### 评论 #66 — MoneroCrusher (2017-10-19T13:07:40Z)

@rhlug any developments?

---

### 评论 #67 — rhlug (2017-10-19T13:46:08Z)

@MoneroCrusher havent had any time. been upgrading linux drivers to 17.40.   i really dont want to have to rebuild a custom kernel just to force load a custom pptable.

---

### 评论 #68 — gstoner (2017-10-19T13:47:11Z)

the Beta 17.40 is running newer version OpenCL on ROCm 

---

### 评论 #69 — gstoner (2017-10-19T13:47:34Z)

It also use LLVM to HSAIL/SC compiler  

---

### 评论 #70 — MoneroCrusher (2017-10-19T13:51:34Z)

@gstoner I got my vegas to work but they only mine at about 1200 H/s on linux instead of 1900 like on windows. Is there anything I can do? If I put page retry to 1 and reboot the page retry is automatically set to 0 again..

---

### 评论 #71 — MoneroCrusher (2017-10-19T13:51:56Z)

@rhlug still same 1200-1300 h/s?

---

### 评论 #72 — rhlug (2017-10-19T17:50:12Z)

@MoneroCrusher  honestly i havent had time to check.  probably the same.   you can put 

```
echo 1 > /sys/module/amdkfd/parameters/noretry
```

in your rc.local so it sets on boot.   but i dont see much improvement from it.


---

### 评论 #73 — lamba84 (2017-10-22T15:25:20Z)

@MoneroCrusher how did you solve xmr-stak issue with vega 64? thanks

---

### 评论 #74 — MoneroCrusher (2017-10-23T05:40:02Z)

Installed newest ROCm kernel and gave it a try and only got 1200 H/s and switched to windows.
So, I couldnt solve it.

---

### 评论 #75 — lamba84 (2017-10-23T07:07:55Z)

which version of ROCm? I installed 1.6-180 and card is recognized by
clinfo, but xmr-stak fail to load due to opencl/clang issue.
Also, even under windows i'm not going over 900 H/s (intesity 1000,
worksize 7, HBBC enabled at 11600).
What settings were you using under linux and now under windows?
Thanks

On Mon, Oct 23, 2017 at 7:40 AM, MoneroCrusher <notifications@github.com>
wrote:

> Installed newest ROCm kernel and gave it a try and only got 1200 H/s and
> switched to windows.
> So, I couldnt solve it.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/216#issuecomment-338552827>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Ae4BYNfYdeEskejl5yLPQMrIS-Ni4Ot0ks5svCa0gaJpZM4PnRmZ>
> .
>


---

### 评论 #76 — calvintam236 (2017-10-23T17:43:11Z)

@lamba84 I think your intensity too low. I am running intensity 1792 worksize 8 for 1220H/s with 960MHz memory clock. You might want to check out here: https://www.reddit.com/r/MoneroMining/comments/74hjqn/monero_and_vega_the_definitive_guide/

---

### 评论 #77 — lamba84 (2017-10-24T19:20:02Z)

thanks @calvintam236. I already started from that guide and tried different settings. Here it is my results:

intensity | worksize | H/s | power @ wall (W) | note
1000 | 8 | 980 |   |  
2016 | 7 | 820 | 210 |  
1600 | 8 | 818 |   |  
1200 | 8 | 922 |   |  
980 | 7 | 925 | 210 | HBCC enabled
990 | 8 | 960 | 260 | HBCC enabled
1024 | 8 | 935 | 225 | HBCC enabled



---

### 评论 #78 — eronquillo (2017-10-30T17:37:41Z)

Any news on getting 1800+ h/s?

---

### 评论 #79 — lamba84 (2017-11-04T19:08:21Z)

@Calvin Tam, the trick for me was to install other 8gb of ram (total of 16)
and push the vram over 16Gb (currently at 32Gb) the same guide you linked.
For now I'm stable at 1650H/s with total power at wall of  280W. next step
for me is to use also the 3 RX580 on same rig.
It's a real shame that these results can be achieved only under windows

On Mon, Oct 30, 2017 at 6:37 PM, eronquillo <notifications@github.com>
wrote:

> Any news on getting 1800+ h/s?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/216#issuecomment-340524240>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Ae4BYPDebtebVpSGb3vumNTDMxx20RDgks5sxglogaJpZM4PnRmZ>
> .
>


---

### 评论 #80 — calvintam236 (2017-11-05T20:28:20Z)

@gstoner is that something we can do to tell why hashrate on ROCm and windows have a big difference in the same hardware setup?

---

### 评论 #81 — gstoner (2017-11-05T20:38:53Z)

@calvintam236   MS Windows uses a proprietary compiler that uses LLVM to HSAIL and then HSAIl IL get compiled by a second compiler called SC or  Shader compiler,    The AMDGPUpro 17.40 is now using this same compiler flow.      ROCm is using fully open source compiler that supports native code generation and bit younger and still be optimized.  But when you want it, it gives direct access to GCN ISA assembly which many time is the best way to tune a hot loop.    We also find you have build your shader differently on LC compiler for ROCM since it has different optimization flow. 

Now windows and Linux at the core use different kernel drivers,  AMDGPU Kernel driver or KGD on Linux and for Windows is KMD based.    

---

### 评论 #82 — avfedorov (2017-11-14T14:08:32Z)

Under the same conditions(the same cards, the same memory and core freq) Linux ROCm and MS Windows performance is the same in my setup.
But after disabling and enabling cards in MS Windows performance gain is about 40%.
Performance gain on MS Windows does not relate to HBCC or RAM size.
Here is instructions - https://bitcointalk.org/index.php?topic=2002025.msg23619746#msg23619746
It seems like on MS Windows cards initialization at boot differs when disable/enable initialization on running system. What are the differences?
If you can understand this, you can be sure to fix the driver for linux to gain performance.

---

### 评论 #83 — rhlug (2017-11-18T20:51:02Z)

Tested rx vega 64 on amdgpu-pro 17.40 and rocm 1.6.4.  Both get about 1275 h/s (1400 core, 1025 mem).  No undervolts because pp_table is broken on both amdgpu-pro and rocm.

On my test rig of 1 rx570 and 1 vega64 with amdgpu-pro 17.40, they end up being on different opencl platforms.  Thats annoying.  Note to self, dont mix VEGA with POLARIS.


---

### 评论 #84 — gstoner (2017-11-18T21:44:28Z)

As I said before they changed the format of the PPLIB in Vega10 from what we had earlier, it also impacted how we were setting up ROCm-SMI.   

---

### 评论 #85 — ghost (2017-12-09T23:59:46Z)

Is this working now? I'm planning on buying a Vega 64 when it comes back into stock. ROCm still doesn't list RX Vega under supported hardware and I would like to use this gpu for machine learning.

---

### 评论 #86 — VeeeneX (2017-12-11T16:53:37Z)

@vicci1209 I've tried latest driver ( amdgpu-pro 17.40 @ ubuntu 16.04) and then I installed roc (latest) I was able to get 1300mh/s from amd driver and 1200 from roc. It looks like it's problem only in drivers.

---

### 评论 #87 — rhlug (2018-02-03T22:01:50Z)

Running Aug 23 blockchain drivers on windows, I get 1800-1900h cryptonight, and 39Mh ethash.
Running ROCm 1.7 on ubuntu, I get 1200-1300h cryptonight, and 39Mh ethash.   

So the fact that I can get like rates on ethash means the opencl stack is just as good.  

I gave windows 64GB of virtual memory and ubuntu 64GB of swap.   Tested amdkfd.noretry 1 and 0.

I guess its the kernel llvm produces that is less efficient.  I dont know what else to try to get 1800+ cryptonight on linux.  


---
