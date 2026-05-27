# OpenCL does not detect second RX5500 gpu

> **Issue #1416**
> **状态**: closed
> **创建时间**: 2021-03-22T17:41:10Z
> **更新时间**: 2021-07-08T11:11:25Z
> **关闭时间**: 2021-05-07T11:48:31Z
> **作者**: ivanmlerner
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1416

## 描述

Hello, I have two rx5500xt and only the one from the motherboards main slot is properly detected in opencl.
I have rocm-smi and rocm-opencl-runtime installed and I am using arch linux with amdgpu. The problem also happens with opencl-amd.
rocm-smi detects both GPU properly, but I can only control the fans for a GPU that is in use (either connected to a monitor or mining for example).

---

## 评论 (20 条)

### 评论 #1 — ivanmlerner (2021-03-22T17:42:37Z)

**clinfo output**

Number of platforms                               3
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP.dbg (3212.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (1800.8)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Extensions function suffix             AMD

  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 21.1.0-devel (git-3e68e7f90d)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx1012
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0 
  Driver Version                                  3212.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Navi 14 [Radeon RX 5500/5500M / Pro 5500M]
  Device PCI-e ID (AMD)                           0x7340
  Device Topology (AMD)                           PCI-E, 0000:0c:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               11
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                32
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1900MHz
  Graphics IP (AMD)                               10.1
  Device Partition                                (core)
    Max number of sub-devices                     11
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple (kernel)     32
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
  Global memory size                              8573157376 (7.984GiB)
  Global free memory (AMD)                        8372224 (7.984GiB) 8372224 (7.984GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7287183768 (6.787GiB)
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
  Max size for global variable                    7287183768 (6.787GiB)
  Preferred total size of global vars             8573157376 (7.984GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             29504
    Max size for 1D images from buffer            4294967295 pixels
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
  Max pipe packet size                            2992216472 (2.787GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory size per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        7287183768 (6.787GiB)
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
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 21:00:00 1969)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             11
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     AMD Ryzen 5 3600X 6-Core Processor
  Device Vendor                                   AuthenticAMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (1800.8)
  Driver Version                                  1800.8 (sse2,avx)
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     CPU
  Device Board Name (AMD)                         (n/a)
  Device Topology (AMD)                           (n/a)
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               12
  Max clock frequency                             2200MHz
  Device Partition                                (core, cl_ext_device_fission)
    Max number of sub-devices                     12
    Supported partition types                     equally, by counts, by affinity domain
    Supported affinity domains                    L3 cache, L2 cache, L1 cache, next partitionable
    Supported partition types (ext)               equally, by counts, by affinity domain
    Supported affinity domains (ext)              L3 cache, L2 cache, L1 cache, next fissionable
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             1024
  Preferred work group size multiple (kernel)     1
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2       
    half                                                 4 / 4        (n/a)
    float                                                8 / 8       
    double                                               4 / 4        (cl_khr_fp64)
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
  Address bits                                    64, Little-Endian
  Global memory size                              16755732480 (15.6GiB)
  Error Correction support                        No
  Max memory allocation                           4188933120 (3.901GiB)
  Unified memory for Host and Device              Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        32768 (32KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             8192x8192 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                64
  Local memory type                               Global
  Local memory size                               32768 (32KiB)
  Max number of constant args                     8
  Max constant buffer size                        65536 (64KiB)
  Max size of kernel argument                     4096 (4KiB)
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1616366618102036665ns (Sun Mar 21 19:43:38 2021)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            Yes
    SPIR versions                                 1.2
  printf() buffer size                            65536 (64KiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_ext_device_fission cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_spir cl_khr_gl_event 


  Platform Name                                   Clover
Number of devices                                 2
  Device Name                                     Radeon RX 5500 XT (NAVI14, DRM 3.40.0, 5.11.7-arch1-1, LLVM 11.1.0)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 21.1.0-devel (git-3e68e7f90d)
  Device Numeric Version                          0x401000 (1.1.0)
  Driver Version                                  21.1.0-devel
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               22
  Max clock frequency                             1900MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
=== CL_PROGRAM_BUILD_LOG ===
fatal error: cannot open file '/usr/share/clc/gfx1012-amdgcn-mesa-mesa3d.bc': No such file or directory
  Preferred work group size multiple (kernel)     <getWGsizes:1504: create kernel : error -46>
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2       
    half                                                 0 / 0        (n/a)
    float                                                4 / 4       
    double                                               2 / 2        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
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
  Error Correction support                        No
  Max memory allocation                           6871947673 (6.4GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       32768 bits (4096 bytes)
  Global Memory cache type                        None
  Image support                                   No
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Max number of constant args                     16
  Max constant buffer size                        67108864 (64MiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Profiling timer resolution                      0ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    ILs with version                              (n/a)
  Built-in kernels with version                   (n/a)
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_extended_versioning
  Device Extensions with Version                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_int64_base_atomics                                        0x400000 (1.0.0)
                                                  cl_khr_int64_extended_atomics                                    0x400000 (1.0.0)
                                                  cl_khr_fp64                                                      0x400000 (1.0.0)
                                                  cl_khr_extended_versioning                                       0x400000 (1.0.0)

  Device Name                                     Radeon RX 5500 XT (NAVI14, DRM 3.40.0, 5.11.7-arch1-1, LLVM 11.1.0)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 21.1.0-devel (git-3e68e7f90d)
  Device Numeric Version                          0x401000 (1.1.0)
  Driver Version                                  21.1.0-devel
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               22
  Max clock frequency                             1900MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
=== CL_PROGRAM_BUILD_LOG ===
fatal error: cannot open file '/usr/share/clc/gfx1012-amdgcn-mesa-mesa3d.bc': No such file or directory
  Preferred work group size multiple (kernel)     <getWGsizes:1504: create kernel : error -46>
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2       
    half                                                 0 / 0        (n/a)
    float                                                4 / 4       
    double                                               2 / 2        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
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
  Error Correction support                        No
  Max memory allocation                           6871947673 (6.4GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       32768 bits (4096 bytes)
  Global Memory cache type                        None
  Image support                                   No
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Max number of constant args                     16
  Max constant buffer size                        67108864 (64MiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Profiling timer resolution                      0ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    ILs with version                              (n/a)
  Built-in kernels with version                   (n/a)
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_extended_versioning
  Device Extensions with Version                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_int64_base_atomics                                        0x400000 (1.0.0)
                                                  cl_khr_int64_extended_atomics                                    0x400000 (1.0.0)
                                                  cl_khr_fp64                                                      0x400000 (1.0.0)
                                                  cl_khr_extended_versioning                                       0x400000 (1.0.0)


NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx1012
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx1012
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx1012

---

### 评论 #2 — ivanmlerner (2021-03-22T17:43:42Z)

**lspci -v output**

00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Root Complex
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: fast devsel

00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Starship/Matisse IOMMU
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: fast devsel
    Capabilities: <access denied>

00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge
    Flags: fast devsel, IOMMU group 0

00:01.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse GPP Bridge (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 27, IOMMU group 1
    Bus: primary=00, secondary=01, subordinate=09, sec-latency=0
    I/O behind bridge: 0000d000-0000efff [size=8K]
    Memory behind bridge: fc400000-fcafffff [size=7M]
    Prefetchable memory behind bridge: 0000007c00000000-0000007e0fffffff [size=8448M]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

00:02.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge
    DeviceName:  Onboard IGD
    Flags: fast devsel, IOMMU group 2

00:03.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge
    Flags: fast devsel, IOMMU group 3

00:03.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse GPP Bridge (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 28, IOMMU group 4
    Bus: primary=00, secondary=0a, subordinate=0c, sec-latency=0
    I/O behind bridge: 0000f000-0000ffff [size=4K]
    Memory behind bridge: fce00000-fcffffff [size=2M]
    Prefetchable memory behind bridge: 0000007800000000-0000007a0fffffff [size=8448M]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

00:04.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge
    Flags: fast devsel, IOMMU group 5

00:05.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge
    Flags: fast devsel, IOMMU group 6

00:07.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge
    Flags: fast devsel, IOMMU group 7

00:07.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Internal PCIe GPP Bridge 0 to bus[E:B] (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 30, IOMMU group 8
    Bus: primary=00, secondary=0d, subordinate=0d, sec-latency=0
    I/O behind bridge: [disabled]
    Memory behind bridge: [disabled]
    Prefetchable memory behind bridge: [disabled]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge
    Flags: fast devsel, IOMMU group 9

00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Internal PCIe GPP Bridge 0 to bus[E:B] (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 31, IOMMU group 10
    Bus: primary=00, secondary=0e, subordinate=0e, sec-latency=0
    I/O behind bridge: [disabled]
    Memory behind bridge: fcb00000-fcdfffff [size=3M]
    Prefetchable memory behind bridge: [disabled]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 61)
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: 66MHz, medium devsel, IOMMU group 11
    Kernel driver in use: piix4_smbus
    Kernel modules: i2c_piix4, sp5100_tco

00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: bus master, 66MHz, medium devsel, latency 0, IOMMU group 11

00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 0
    Flags: fast devsel, IOMMU group 12

00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 1
    Flags: fast devsel, IOMMU group 12

00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 2
    Flags: fast devsel, IOMMU group 12

00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 3
    Flags: fast devsel, IOMMU group 12
    Kernel driver in use: k10temp
    Kernel modules: k10temp

00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 4
    Flags: fast devsel, IOMMU group 12

00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 5
    Flags: fast devsel, IOMMU group 12

00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 6
    Flags: fast devsel, IOMMU group 12

00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 7
    Flags: fast devsel, IOMMU group 12

01:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Matisse Switch Upstream (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 24, IOMMU group 13
    Bus: primary=01, secondary=02, subordinate=09, sec-latency=0
    I/O behind bridge: 0000d000-0000efff [size=8K]
    Memory behind bridge: fc400000-fcafffff [size=7M]
    Prefetchable memory behind bridge: 0000007c00000000-0000007e0fffffff [size=8448M]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

02:02.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Matisse PCIe GPP Bridge (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 32, IOMMU group 14
    Bus: primary=02, secondary=03, subordinate=05, sec-latency=0
    I/O behind bridge: 0000e000-0000efff [size=4K]
    Memory behind bridge: fc600000-fc7fffff [size=2M]
    Prefetchable memory behind bridge: 0000007c00000000-0000007e0fffffff [size=8448M]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

02:05.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Matisse PCIe GPP Bridge (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 33, IOMMU group 15
    Bus: primary=02, secondary=06, subordinate=06, sec-latency=0
    I/O behind bridge: 0000d000-0000dfff [size=4K]
    Memory behind bridge: fca00000-fcafffff [size=1M]
    Prefetchable memory behind bridge: [disabled]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

02:08.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Matisse PCIe GPP Bridge (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 34, IOMMU group 16
    Bus: primary=02, secondary=07, subordinate=07, sec-latency=0
    I/O behind bridge: [disabled]
    Memory behind bridge: fc400000-fc5fffff [size=2M]
    Prefetchable memory behind bridge: [disabled]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

02:09.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Matisse PCIe GPP Bridge (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 36, IOMMU group 17
    Bus: primary=02, secondary=08, subordinate=08, sec-latency=0
    I/O behind bridge: [disabled]
    Memory behind bridge: fc900000-fc9fffff [size=1M]
    Prefetchable memory behind bridge: [disabled]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

02:0a.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Matisse PCIe GPP Bridge (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 38, IOMMU group 18
    Bus: primary=02, secondary=09, subordinate=09, sec-latency=0
    I/O behind bridge: [disabled]
    Memory behind bridge: fc800000-fc8fffff [size=1M]
    Prefetchable memory behind bridge: [disabled]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

03:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Upstream Port of PCI Express Switch (rev c5) (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 39, IOMMU group 19
    Memory at fc700000 (32-bit, non-prefetchable) [size=16K]
    Bus: primary=03, secondary=04, subordinate=05, sec-latency=0
    I/O behind bridge: 0000e000-0000efff [size=4K]
    Memory behind bridge: fc600000-fc6fffff [size=1M]
    Prefetchable memory behind bridge: 0000007c00000000-0000007e0fffffff [size=8448M]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

04:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Downstream Port of PCI Express Switch (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 40, IOMMU group 20
    Bus: primary=04, secondary=05, subordinate=05, sec-latency=0
    I/O behind bridge: 0000e000-0000efff [size=4K]
    Memory behind bridge: fc600000-fc6fffff [size=1M]
    Prefetchable memory behind bridge: 0000007c00000000-0000007e0fffffff [size=8448M]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (rev c5) (prog-if 00 [VGA controller])
    Subsystem: ASUSTeK Computer Inc. Device 0595
    Flags: bus master, fast devsel, latency 0, IRQ 97, IOMMU group 21
    Memory at 7c00000000 (64-bit, prefetchable) [size=8G]
    Memory at 7e00000000 (64-bit, prefetchable) [size=256M]
    I/O ports at e000 [size=256]
    Memory at fc600000 (32-bit, non-prefetchable) [size=512K]
    Expansion ROM at fc680000 [disabled] [size=128K]
    Capabilities: <access denied>
    Kernel driver in use: amdgpu
    Kernel modules: amdgpu

05:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 HDMI Audio
    Subsystem: ASUSTeK Computer Inc. Device 0595
    Flags: bus master, fast devsel, latency 0, IRQ 101, IOMMU group 22
    Memory at fc6a0000 (32-bit, non-prefetchable) [size=16K]
    Capabilities: <access denied>
    Kernel driver in use: snd_hda_intel
    Kernel modules: snd_hda_intel

06:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 26)
    Subsystem: ASUSTeK Computer Inc. Device 87c3
    Flags: bus master, fast devsel, latency 0, IRQ 35, IOMMU group 23
    I/O ports at d000 [size=256]
    Memory at fca04000 (64-bit, non-prefetchable) [size=4K]
    Memory at fca00000 (64-bit, non-prefetchable) [size=16K]
    Capabilities: <access denied>
    Kernel driver in use: r8169
    Kernel modules: r8169

07:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Reserved SPP
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: fast devsel, IOMMU group 16
    Capabilities: <access denied>

07:00.1 USB controller: Advanced Micro Devices, Inc. [AMD] Matisse USB 3.0 Host Controller (prog-if 30 [XHCI])
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: bus master, fast devsel, latency 0, IRQ 76, IOMMU group 16
    Memory at fc500000 (64-bit, non-prefetchable) [size=1M]
    Capabilities: <access denied>
    Kernel driver in use: xhci_hcd
    Kernel modules: xhci_pci

07:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Matisse USB 3.0 Host Controller (prog-if 30 [XHCI])
    Subsystem: Advanced Micro Devices, Inc. [AMD] Device 148c
    Flags: bus master, fast devsel, latency 0, IRQ 37, IOMMU group 16
    Memory at fc400000 (64-bit, non-prefetchable) [size=1M]
    Capabilities: <access denied>
    Kernel driver in use: xhci_hcd
    Kernel modules: xhci_pci

08:00.0 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 51) (prog-if 01 [AHCI 1.0])
    Subsystem: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode]
    Flags: bus master, fast devsel, latency 0, IRQ 44, IOMMU group 17
    Memory at fc900000 (32-bit, non-prefetchable) [size=2K]
    Capabilities: <access denied>
    Kernel driver in use: ahci

09:00.0 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 51) (prog-if 01 [AHCI 1.0])
    Subsystem: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode]
    Flags: bus master, fast devsel, latency 0, IRQ 60, IOMMU group 18
    Memory at fc800000 (32-bit, non-prefetchable) [size=2K]
    Capabilities: <access denied>
    Kernel driver in use: ahci

0a:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Upstream Port of PCI Express Switch (rev c5) (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 42, IOMMU group 24
    Memory at fcf00000 (32-bit, non-prefetchable) [size=16K]
    Bus: primary=0a, secondary=0b, subordinate=0c, sec-latency=0
    I/O behind bridge: 0000f000-0000ffff [size=4K]
    Memory behind bridge: fce00000-fcefffff [size=1M]
    Prefetchable memory behind bridge: 0000007800000000-0000007a0fffffff [size=8448M]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

0b:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Downstream Port of PCI Express Switch (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 43, IOMMU group 25
    Bus: primary=0b, secondary=0c, subordinate=0c, sec-latency=0
    I/O behind bridge: 0000f000-0000ffff [size=4K]
    Memory behind bridge: fce00000-fcefffff [size=1M]
    Prefetchable memory behind bridge: 0000007800000000-0000007a0fffffff [size=8448M]
    Capabilities: <access denied>
    Kernel driver in use: pcieport

0c:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (rev c5) (prog-if 00 [VGA controller])
    Subsystem: ASUSTeK Computer Inc. Device 0595
    Flags: bus master, fast devsel, latency 0, IRQ 98, IOMMU group 26
    Memory at 7800000000 (64-bit, prefetchable) [size=8G]
    Memory at 7a00000000 (64-bit, prefetchable) [size=256M]
    I/O ports at f000 [size=256]
    Memory at fce00000 (32-bit, non-prefetchable) [size=512K]
    Expansion ROM at fce80000 [disabled] [size=128K]
    Capabilities: <access denied>
    Kernel driver in use: amdgpu
    Kernel modules: amdgpu

0c:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 HDMI Audio
    Subsystem: ASUSTeK Computer Inc. Device 0595
    Flags: bus master, fast devsel, latency 0, IRQ 103, IOMMU group 27
    Memory at fcea0000 (32-bit, non-prefetchable) [size=16K]
    Capabilities: <access denied>
    Kernel driver in use: snd_hda_intel
    Kernel modules: snd_hda_intel

0d:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Function
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: fast devsel, IOMMU group 28
    Capabilities: <access denied>

0e:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Reserved SPP
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: fast devsel, IOMMU group 29
    Capabilities: <access denied>

0e:00.1 Encryption controller: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Cryptographic Coprocessor PSPCPP
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: bus master, fast devsel, latency 0, IRQ 94, IOMMU group 30
    Memory at fcc00000 (32-bit, non-prefetchable) [size=1M]
    Memory at fcd08000 (32-bit, non-prefetchable) [size=8K]
    Capabilities: <access denied>
    Kernel driver in use: ccp
    Kernel modules: ccp

0e:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Matisse USB 3.0 Host Controller (prog-if 30 [XHCI])
    Subsystem: ASUSTeK Computer Inc. Device 87c0
    Flags: bus master, fast devsel, latency 0, IRQ 85, IOMMU group 31
    Memory at fcb00000 (64-bit, non-prefetchable) [size=1M]
    Capabilities: <access denied>
    Kernel driver in use: xhci_hcd
    Kernel modules: xhci_pci

0e:00.4 Audio device: Advanced Micro Devices, Inc. [AMD] Starship/Matisse HD Audio Controller
    Subsystem: ASUSTeK Computer Inc. Device 8797
    Flags: bus master, fast devsel, latency 0, IRQ 105, IOMMU group 32
    Memory at fcd00000 (32-bit, non-prefetchable) [size=32K]
    Capabilities: <access denied>
    Kernel driver in use: snd_hda_intel
    Kernel modules: snd_hda_intel

---

### 评论 #3 — ivanmlerner (2021-03-22T19:55:52Z)

**rocminfo output**

ROCk module is loaded
Able to open /dev/kfd read-write
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
  Name:                    AMD Ryzen 5 3600X 6-Core Processor 
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 3600X 6-Core Processor 
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
  Max Clock Freq. (MHz):   4000                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            12                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16363016(0xf9ae08) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16363016(0xf9ae08) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx1012                            
  Uuid:                    GPU-XX                             
  Marketing Name:          Navi 14 [Radeon RX 5500/5500M / Pro 5500M]
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
  Chip ID:                 29504(0x7340)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1900                               
  BDFID:                   3072                               
  Internal Node ID:        1                                  
  Compute Unit:            22                                 
  SIMDs per CU:            4                                  
  Shader Engines:          2                                  
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
  Max Waves Per CU:        80(0x50)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx1012         
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


---

### 评论 #4 — ROCmSupport (2021-03-23T02:49:42Z)

Thanks @ivanmlerner for reaching out.
Have 2 points, Navi14 is not a supported card with ROCm and also ROCm is not validated with arch linux anytime officially.

But still I will try to help from my side.
Request you to do below things.
1. Can you please unplug both cards and keep one card at a time and check whether card is detected(do the same for other card also).
2. Keep both cards now and check again whether both cards are detected?
3. In step2, if only one card is detected, exchange the slots of both cards and check again.
4. While you are in step3, share the output of dmesg also.
Thank you.

---

### 评论 #5 — ivanmlerner (2021-03-23T17:16:20Z)

I know, sorry for the inconvenience. And I am really grateful for your help.
I did the steps as asked, and here is the attached [dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/6191538/dmesg.txt)
With both cards installed opencl only detects the one from the main slot of the motherboard (PCI entry containing 0000:0c... on the double GPU setup)

---

### 评论 #6 — shunonymous (2021-03-23T17:21:48Z)

I met same issue, but RX 5700XT + RX 5500XT.
I used debugger, and found infinity loop on [here](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/ceae52f3e9d58ff71bfff0956ea8d53686eb09b5/src/core/runtime/amd_aql_queue.cpp#L1019) if using 2nd GPU, but issue not resolved yet.

How about on other GPUs(like vega)?

---

### 评论 #7 — ROCmSupport (2021-03-24T04:30:09Z)

Hi @shunonymous and @ivanmlerner 
Looks like its a strange issue.
No issues observed so far with 2 or 4 or 8 Vega10/20.
Even dmesg is also not showing good information.


---

### 评论 #8 — kentrussell (2021-03-24T13:39:45Z)

Can you confirm that both PCIe slots work independently? What wattage PSU have you got, and what model of motherboard? There's nothing in dmesg that shows anything to indicate that it's kernel-driver related, so I am hoping to see if it's possibly a HW config issue.

---

### 评论 #9 — ivanmlerner (2021-03-24T18:33:26Z)

The only configuration I haven't tested is the one with only the second slop occupied. In all the other configurations, apart from opencl on the second slot, everything works fine on both. I'll test this configuration and get back to you.

In regard to the hardware, I have a 700W PSU with an ASUS TUF GAMING X570-PLUS/BR motherboard and a Ryzen 5 3600X.
The main slot is controlled by the processor and the secondary slot is controlled by the chipset, so could it be a BIOS issue? 

---

### 评论 #10 — ivanmlerner (2021-03-24T20:00:32Z)

Now using only one GPU on the secondary slot, and it is not detected by opencl. Video is fine and mesa's opencl detects the card, but rocm's opencl doesn't.

---

### 评论 #11 — ddobreff (2021-03-25T10:47:43Z)

Hi @ivanmlerner, make sure you have PCIe atomics supported on your secondary slot, Navi[10/12/14/21/22/23] require PCIe atomics and must be on PCIe 3.0 x4 at least to get recognized by OpenCL.

---

### 评论 #12 — kentrussell (2021-03-25T11:43:57Z)

@ivanmlerner Could you put a card just in the secondary slot, then get a full dmesg from that? I want to see what it ends up doing when we just have the one card in there, in case dmesg shows anything more useful. I was wondering about PCIe atomics being enabled on there. It's still a PCIe 4.0 x4, so it SHOULD be recognized. Thanks!

---

### 评论 #13 — xuhuisheng (2021-03-25T11:54:57Z)

@ddobreff 
Oh, NO. Why navi required atomic after vega didn't.
I must say atomic is totally a disaster. It leads too many troubles on gfx8. We have to explain to person why this cpu didn't support PCIe atomic, why this motherboard didn't support, why the second slot of PCIe didn't support, why the switch didn't support.

https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/commit/67ac9c3fee777255e93d97f937a5a4de9dc199c6#diff-4618c86aa189be60e693d59e2d82a513d5e3022d9e2a2bb233bcae707a894f82

---

### 评论 #14 — ivanmlerner (2021-03-25T13:35:51Z)

@kentrussell here is the dmesg output: 
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/6205015/dmesg.txt)
@xuhuisheng I believe my setup should support it, how can I check if the second slot supports it? It is a PCIe 4.0 x4

---

### 评论 #15 — kentrussell (2021-03-25T14:08:56Z)

The atomics issue is it:
[    1.101433] kfd kfd: skipped device 1002:7340, PCI rejects atomics
We saw this in https://github.com/RadeonOpenCompute/ROCm/issues/910 as well. Looks like its a restriction with the board. Can you try to contact ASUS to see if there is a BIOS update or a BIOS setting that can enable this?

---

### 评论 #16 — ivanmlerner (2021-03-25T14:22:17Z)

Will sure do, thanks a lot for the help. 
If you need any testing when preparing to support arch or navi just hit me up.

---

### 评论 #17 — ROCmSupport (2021-05-07T11:48:30Z)

Am closing this now as the resolution is provided from @kentrussell 
Thank you.

---

### 评论 #18 — Mushoz (2021-07-07T12:14:51Z)

How is this considered "solved" though? I am using a 6900xt + 6800xt in my rig. Under Windows I can use them both just fine with OpenCL. Under Linux, only the first GPU will ever work with the second GPU complaining in dmesg about missing PCI-E atomic support.

Why does this work properly on Windows, but not on Linux?

---

### 评论 #19 — ROCmSupport (2021-07-07T12:47:11Z)

Hi @Mushoz 
As the issue is already closed, recommend to open a new issue, if any, for faster resolutions.
Thank you.

---

### 评论 #20 — Mushoz (2021-07-08T11:11:25Z)

Sure, I opened a new issue here: https://github.com/RadeonOpenCompute/ROCm/issues/1514

---
