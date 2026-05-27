# ocl_memtest (OpenCL application) is not working with Rocm 3.3

> **Issue #1094**
> **状态**: closed
> **创建时间**: 2020-05-02T12:44:35Z
> **更新时间**: 2020-05-02T18:28:55Z
> **关闭时间**: 2020-05-02T18:28:54Z
> **作者**: xcom169
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1094

## 描述

Dear All!

[]$ sudo ocl_memtest
hostname is csabesz-Ryzen
CL_PLATFORM_NAME: 	AMD Accelerated Parallel Processing
CL_PLATFORM_VERSION: 	OpenCL 2.0 AMD-APP.internal.dbg (3098.0)
                  	Device 0 is CL_DEVICE_TYPE_GPU, "gfx803"
ERROR: opencl call failed with rc(-11), line 385, file ocl_memtest.cpp
Error: Program build failure


hostname is csabesz-Ryzen
CL_PLATFORM_NAME: 	AMD Accelerated Parallel Processing
CL_PLATFORM_VERSION: 	OpenCL 2.0 AMD-APP.internal.dbg (3098.0)
                  	Device 0 is CL_DEVICE_TYPE_GPU, "gfx803"
allocated 6963 Mbytes from device 0
[05/02/2020 14:45:12][csabesz-Ryzen][0]:Test0 [Walking 1 bit]
[05/02/2020 14:45:12][csabesz-Ryzen][0]:Test0: global walk test
Memory access fault by GPU node-1 (Agent handle: 0x55b54f369f20) on address 0x1e00000. Reason: Page not present or supervisor privilege.
Nearby memory map:
0x1100000, 0x40000, System
0x11c0000, 0x20000, System
0x1e60000, 0x60000, System

PtrInfo:
	Address: 0x1100000-0x1140000/0x1100000-0x1140000
	Size: 0x40000
	Type: 1
	Owner: 0x55b54f2c8120
	CanAccess: 1
		0x55b54f369f20
	In block: 0x1100000, 0x80000
PtrInfo:
	Address: 0x11c0000-0x11e0000/0x11c0000-0x11e0000
	Size: 0x20000
	Type: 1
	Owner: 0x55b54f2c8120
	CanAccess: 1
		0x55b54f369f20
	In block: 0x11c0000, 0x20000
PtrInfo:
	Address: 0x1e60000-0x1ec0000/0x1e60000-0x1ec0000
	Size: 0x60000
	Type: 1
	Owner: 0x55b54f2c8120
	CanAccess: 1
		0x55b54f369f20
	In block: 0x1e60000, 0x60000
ocl_memtest: /home/csabesz/.cache/yay/hsa-rocr/src/ROCR-Runtime-rocm-3.3.0/src/core/runtime/runtime.cpp:1249: static bool core::Runtime::VMFaultHandler(hsa_signal_value_t, void*): Assertion `false && "GPU memory access fault."' failed.
Aborted (core dumped)



Link to the App:
https://sourceforge.net/projects/cudagpumemtest/

CLINFO:

`Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP.internal.dbg (3098.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 
  Platform Max metadata object keys (AMD)         8
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx803
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  3098.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
  Device Topology (AMD)                           PCI-E, 08:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               36
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1338MHz
  Graphics IP (AMD)                               8.3
  Device Partition                                (core)
    Max number of sub-devices                     36
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
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
  Address bits                                    64, Little-Endian
  Global memory size                              8589934592 (8GiB)
  Global free memory (AMD)                        8388608 (8GiB)
  Global memory channels (AMD)                    8
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7301444403 (6.8GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   No
    Base address alignment for 2D image buffers   0 bytes
    Pitch alignment for 2D image buffers          0 pixels
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        7301444403 (6.8GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  P2P devices (AMD)                               <printDeviceInfo:147: get number of CL_DEVICE_P2P_DEVICES_AMD : error -30>
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Thu Jan  1 01:00:00 1970)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             36
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803`

---

## 评论 (1 条)

### 评论 #1 — xcom169 (2020-05-02T18:28:54Z)

https://github.com/matszpk/clgpustress works fine, so I'm closing this. 

---
