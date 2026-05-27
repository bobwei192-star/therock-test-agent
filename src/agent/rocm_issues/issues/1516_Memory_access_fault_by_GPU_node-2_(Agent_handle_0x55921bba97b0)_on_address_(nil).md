# Memory access fault by GPU node-2 (Agent handle: 0x55921bba97b0) on address (nil). Reason: Page not present or supervisor privilege. Aborted (core dumped)

> **Issue #1516**
> **状态**: closed
> **创建时间**: 2021-07-09T09:10:05Z
> **更新时间**: 2021-07-09T09:57:49Z
> **关闭时间**: 2021-07-09T09:57:49Z
> **作者**: bendisco51
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1516

## 描述

Hello,
I'm new to amd computing and have a problem with ROCm and clinfo.

System information :
Ubuntu 20.04 LTS up to date (kernel 5.4.0-77-generic x64)
AMD Ryzen 7 5800x with 2X Radeon 6700 XT

I have installed rocm with : apt install rocm-dkms
How solve this problem please ?

**Result of rocminfo :**

ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 7 5800X 8-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 7 5800X 8-Core Processor
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   3800
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            16
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32857680(0x1f55e50) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    32857680(0x1f55e50) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx1031
  Uuid:                    GPU-XX
  Marketing Name:          Device 73df
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 29663(0x73df)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2725
  BDFID:                   2816
  Internal Node ID:        1
  Compute Unit:            40
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        64(0x40)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    12566528(0xbfc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1031
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*******
Agent 3
*******
  Name:                    gfx1031
  Uuid:                    GPU-XX
  Marketing Name:          Device 73df
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 29663(0x73df)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2855
  BDFID:                   3584
  Internal Node ID:        2
  Compute Unit:            40
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        64(0x40)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    12566528(0xbfc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1031
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***


**Result of clinfo :**

Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (3275.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 2
  Device Name                                     gfx1031
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0
  Driver Version                                  3275.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     GPU
  Device Board Name (AMD)                         Device 73df
  Device Topology (AMD)                           PCI-E, 0b:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               20
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                32
  SIMD instruction width (AMD)                    1
  Max clock frequency                             2725MHz
  Graphics IP (AMD)                               10.3
  Device Partition                                (core)
    Max number of sub-devices                     20
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple              32
  Wavefront width (AMD)                           32
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
  Address bits                                    64, Little-Endian
  Global memory size                              12868124672 (11.98GiB)
  Global free memory (AMD)                        12566528 (11.98GiB)
  Global memory channels (AMD)                    6
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           10937905968 (10.19GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    10937905968 (10.19GiB)
  Preferred total size of global vars             12868124672 (11.98GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             29663
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 8192 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             16384x16384x8192 pixels
    Max number of read image args                 128
    Max number of write image args                8
    Max number of read/write image args           64
  Max number of pipe args                         16
  Max active pipe reservations                    16
  Max pipe packet size                            2347971376 (2.187GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        10937905968 (10.19GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties (on host)
    Out-of-order execution                        No
    Profiling                                     Yes
  Queue properties (on device)
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                262144 (256KiB)
    Max size                                      8388608 (8MiB)
  Max queues on device                            1
  Max events on device                            1024
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
    Max real-time compute units (AMD)             20
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

  Device Name                                     gfx1031
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0
  Driver Version                                  3275.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     GPU
  Device Board Name (AMD)                         Device 73df
  Device Topology (AMD)                           PCI-E, 0e:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               20
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                32
  SIMD instruction width (AMD)                    1
  Max clock frequency                             2855MHz
  Graphics IP (AMD)                               10.3
  Device Partition                                (core)
    Max number of sub-devices                     20
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
**Memory access fault by GPU node-2 (Agent handle: 0x563048cfe7b0) on address (nil). Reason: Page not present or supervisor privilege.
Aborted (core dumped)**


**Extract of dmesg :**
[  749.965092] amdgpu 0000:0e:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process clinfo pid 1303 thread clinfo pid 1303)
[  749.965094] amdgpu 0000:0e:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 0x1b (UTCL2)
[  749.965095] amdgpu 0000:0e:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[  749.965096] amdgpu 0000:0e:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[  749.965097] amdgpu 0000:0e:00.0: amdgpu:      MORE_FAULTS: 0x0
[  749.965098] amdgpu 0000:0e:00.0: amdgpu:      WALKER_ERROR: 0x0
[  749.965099] amdgpu 0000:0e:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[  749.965100] amdgpu 0000:0e:00.0: amdgpu:      MAPPING_ERROR: 0x0
[  749.965101] amdgpu 0000:0e:00.0: amdgpu:      RW: 0x0


**Result of rocm-smi :**
======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK    MCLK   Fan   Perf  PwrCap  VRAM%  GPU%
0    33.0c  9.0W    500Mhz  96Mhz  255%  auto  186.0W    0%   16%
1    32.0c  7.0W    500Mhz  96Mhz  255%  auto  194.0W    0%   14%
================================================================================
============================= End of ROCm SMI Log ==============================



---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-07-09T09:57:49Z)

Hi @bendisco51 
Thanks for reaching out.
We are not officially supporting gfx10 devices right now with ROCm. Hence can not comment more on this.
Thank you.

---
