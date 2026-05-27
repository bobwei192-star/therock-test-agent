# Cannot build OpenCL program

> **Issue #495**
> **状态**: closed
> **创建时间**: 2018-08-10T03:47:30Z
> **更新时间**: 2018-08-11T13:32:51Z
> **关闭时间**: 2018-08-10T19:21:29Z
> **作者**: trace86
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/495

## 描述

I'm using Ubuntu 16.04 and the latest ROCm drivers, with Claymore 11.8 running two Vega64 cards
I've recently installed ROCm, but afterwards cannot run Claymore.  Does anybody know what did i do wrong on the driver install?  I followed the guide here https://rocm.github.io/ROCmInstall.html and I'm using the 4.13 kernel as suggested.

The error message is as below:

```
AMD Cards available: 2
GPU #0: gfx900 (Device 687f), 8176 MB available, 64 compute units (pci bus 5:0:0                               )
GPU #0 recognized as Vega
GPU #1: gfx900 (Device 687f), 8176 MB available, 64 compute units (pci bus 10:0:                               0)
GPU #1 recognized as Vega
POOL/SOLO version
AMD ADL library not found.
Cannot build OpenCL program for GPU 0
Cannot build OpenCL program for GPU 1
GPU #0: algorithm ASM 1
GPU #1: algorithm ASM 1
No NVIDIA CUDA GPUs detected.
Total cards: 2

You can use "+" and "-" keys to achieve best ETH speed, see "FINE TUNING" sectio                               n in Readme for details.

ETH: Stratum - connecting to 'eth-us-west1.nanopool.org' <45.63.61.87> port 9999                                (unsecure)
ETH: Stratum - Connected (eth-us-west1.nanopool.org:9999) (unsecure)
ETHEREUM-ONLY MINING MODE ENABLED (-mode 1)
ETH: eth-proxy stratum mode
Watchdog enabled
Remote management (READ-ONLY MODE) is enabled on port 3333

You did not specify -dcri values directly, so they will be detected automaticall                               y
Automatic detection of best -dcri values started, please wait...

ETH: Authorized
Setting DAG epoch #204...
Setting DAG epoch #204 for GPU1
Create GPU buffer for GPU1
Setting DAG epoch #204 for GPU0
Create GPU buffer for GPU0
GPU0, OpenCL error -48 (0) - cannot create DAG on GPU
GPU1, OpenCL error -48 (0) - cannot create DAG on GPU
Quit signal received...
Quit, please wait...
GPU 0 failed
GPU 1 failed


```

---

## 评论 (7 条)

### 评论 #1 — trace86 (2018-08-10T03:48:00Z)

clinfo runs without problems

```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP.internal (2574.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_object_metadata cl_amd_event_callback
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 2
  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2
  Driver Version                                  2574.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         Device 687f
  Device Topology (AMD)                           PCI-E, 05:00.0
  Max compute units                               64
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1630MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
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
    Correctly-rounded divide and sqrt operations  No
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
  Global free memory (AMD)                        8370176 (7.982GiB)
  Global memory channels (AMD)                    64
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7287183769 (6.787GiB)
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
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        7287183769 (6.787GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 16:00:00 1969)
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2
  Driver Version                                  2574.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         Device 687f
  Device Topology (AMD)                           PCI-E, 0a:00.0
  Max compute units                               64
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1630MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
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
    Correctly-rounded divide and sqrt operations  No
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
  Global free memory (AMD)                        8370176 (7.982GiB)
  Global memory channels (AMD)                    64
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7287183769 (6.787GiB)
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
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        7287183769 (6.787GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 16:00:00 1969)
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

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
        NOTE:   your OpenCL library declares to support OpenCL 1.2,
                but it seems to support up to OpenCL 2.1 too.

```

---

### 评论 #2 — trace86 (2018-08-10T04:01:49Z)

rpcminfo seems to be fine too

```
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0
  Queue Min Size:          0
  Queue Max Size:          0
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768KB
  Chip ID:                 0
  Cacheline Size:          64
  Max Clock Frequency (MHz):2900
  BDFID:                   0
  Compute Unit:            2
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    3928672KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    3928672KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx900
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26751
  Cacheline Size:          64
  Max Clock Frequency (MHz):1630
  BDFID:                   1280
  Compute Unit:            64
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  83887104
    Dim[2]:                  0
  Grid Max Size:           4294967295
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295
    Dim[1]:                  4294967295
    Dim[2]:                  4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8372224KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx900
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Dimension:
        Dim[0]:                  67109888
        Dim[1]:                  1024
        Dim[2]:                  16777217
      Workgroup Max Size:      1024
      Grid Max Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      Grid Max Size:           4294967295
      FBarrier Max Size:       32
*******
Agent 3
*******
  Name:                    gfx900
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26751
  Cacheline Size:          64
  Max Clock Frequency (MHz):1630
  BDFID:                   2560
  Compute Unit:            64
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  167773184
    Dim[2]:                  0
  Grid Max Size:           4294967295
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295
    Dim[1]:                  4294967295
    Dim[2]:                  4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8372224KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx900
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Dimension:
        Dim[0]:                  67109888
        Dim[1]:                  1024
        Dim[2]:                  16777217
      Workgroup Max Size:      1024
      Grid Max Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      Grid Max Size:           4294967295
      FBarrier Max Size:       32
*** Done ***

```

---

### 评论 #3 — trace86 (2018-08-10T09:06:07Z)

Also attached the ROCm info

```=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0
  Queue Min Size:          0
  Queue Max Size:          0
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768KB
  Chip ID:                 0
  Cacheline Size:          64
  Max Clock Frequency (MHz):2900
  BDFID:                   0
  Compute Unit:            2
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    3928672KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    3928672KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx900
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26751
  Cacheline Size:          64
  Max Clock Frequency (MHz):1630
  BDFID:                   1280
  Compute Unit:            64
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  83887104
    Dim[2]:                  0
  Grid Max Size:           4294967295
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295
    Dim[1]:                  4294967295
    Dim[2]:                  4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8372224KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx900
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Dimension:
        Dim[0]:                  67109888
        Dim[1]:                  1024
        Dim[2]:                  16777217
      Workgroup Max Size:      1024
      Grid Max Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      Grid Max Size:           4294967295
      FBarrier Max Size:       32
*******
Agent 3
*******
  Name:                    gfx900
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26751
  Cacheline Size:          64
  Max Clock Frequency (MHz):1630
  BDFID:                   2560
  Compute Unit:            64
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  167773184
    Dim[2]:                  0
  Grid Max Size:           4294967295
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295
    Dim[1]:                  4294967295
    Dim[2]:                  4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8372224KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx900
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Dimension:
        Dim[0]:                  67109888
        Dim[1]:                  1024
        Dim[2]:                  16777217
      Workgroup Max Size:      1024
      Grid Max Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      Grid Max Size:           4294967295
      FBarrier Max Size:       32
*** Done ***
```

---

### 评论 #4 — preda (2018-08-10T13:13:11Z)

-48 is  CL_INVALID_KERNEL. Maybe some precompiled binary is cached somewhere? or something else. Anyway, OpenCL seems to be installed OK.

---

### 评论 #5 — trace86 (2018-08-10T18:47:01Z)

@preda How may i troubleshoot the precompiled binary?

is it possible that the kernel version is not ideal?
```
~/mining/claymore$ dkms status
amdgpu, 1.8-192, 4.15.0-30-generic, x86_64: installed
```

---

### 评论 #6 — jlgreathouse (2018-08-10T19:21:29Z)

Hi @trace86 

"Kernel" in the sense that @preda is using means "function that OpenCL launches to the GPU", rather than "the operating system's supervisor binary".

I agree with the assessment -- this appears to be a problem with the application rather than a problem with ROCm. I would recommend contacting the developers of Claymore to have them try to find what the problem is. If they can point out a situation where they believe ROCm is incorrectly handling a valid kernel in some way, please report that back to us.

However, as it stands, the information you've presented implies that OpenCL is successfully working on your ROCm installation, but that one particular application not written by the ROCm group is not working.

Unfortunately, the ROCm team cannot guarantee that we will debug non-AMD applications. If, however, the developers of those applications can point out situations where they believe that the way ROCm is running incorrectly in a (what they believe to be) correct application, we can try to work to understand where the problem comes from (and if it's in software that AMD controls, they we can try to implement fixes for future releases).

If the Claymore team believes this issue is due to ROCm, please reopen it. For now, I'm going to close it because at this stage it doesn't look like a problem AMD can fix.

---

### 评论 #7 — trace86 (2018-08-11T13:06:08Z)

Update:  Never mind, I got ethminer fixed after executing ```export HSA_ENABLE_SDMA=0```

I now wonder how do I check if my rig supports PCI-E Atomic or not?  I did some reading and believe it's not related to the PCIe port but related to the CPU?

I actually thought the same thing initially, but trying with ethminer, i also get 0 hashrate

```
./ethminer -G -M 8192
 m 06:04:55 ethminer ethminer 0.15.0
 m 06:04:55 ethminer Build: linux/release
 i 06:04:55 ethminer Found suitable OpenCL device [gfx900] with 8573157376 bytes of GPU memory
 i 06:04:55 ethminer Found suitable OpenCL device [gfx900] with 8573157376 bytes of GPU memory
Benchmarking on platform: CL
Preparing DAG for block #8192
cl 06:04:55 cl-0     No work. Pause for 3 s.
cl 06:04:55 cl-1     No work. Pause for 3 s.
Warming up...
cl 06:04:58 cl-0     Platform: AMD Accelerated Parallel Processing
cl 06:04:58 cl-0     Device:   gfx900 / OpenCL 1.2 
cl 06:04:58 cl-1     Platform: AMD Accelerated Parallel Processing
cl 06:04:58 cl-1     Device:   gfx900 / OpenCL 1.2 
cl 06:04:59 cl-1     OpenCL kernel: Stable kernel
cl 06:04:59 cl-0     OpenCL kernel: Stable kernel
cl 06:04:59 cl-1     Build info: 
cl 06:04:59 cl-1     Creating light cache buffer, size: 16776896
cl 06:04:59 cl-1     Creating DAG buffer, size: 1073739904
cl 06:04:59 cl-1     Loading kernels
cl 06:04:59 cl-1     Writing light cache buffer
cl 06:05:00 cl-0     Build info: 
cl 06:05:00 cl-0     Creating light cache buffer, size: 16776896
cl 06:05:00 cl-0     Creating DAG buffer, size: 1073739904
cl 06:05:00 cl-0     Loading kernels
cl 06:05:00 cl-0     Writing light cache buffer
Trial 1... 
0
Trial 2... 
0
Trial 3... 
0
Trial 4... 
0
Trial 5... 
0
min/mean/max: 0/0/0 H/s
inner mean: 0 H/s
```

---
