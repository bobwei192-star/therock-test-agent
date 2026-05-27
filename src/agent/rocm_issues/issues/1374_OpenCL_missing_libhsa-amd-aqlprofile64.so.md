# OpenCL missing libhsa-amd-aqlprofile64.so

> **Issue #1374**
> **状态**: closed
> **创建时间**: 2021-02-09T15:30:47Z
> **更新时间**: 2021-02-11T03:49:26Z
> **关闭时间**: 2021-02-10T12:18:10Z
> **作者**: Bogdan107
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1374

## 描述

**hashcat -I --backend-ignore-cuda | head -n 2**
```
hashcat (v6.0.0) starting...

LoadLib(libhsa-amd-aqlprofile64.so) failed: libhsa-amd-aqlprofile64.so: cannot open shared object file: No such file or directory
```

**clinfo | head -n 0**
```
LoadLib(libhsa-amd-aqlprofile64.so) failed: libhsa-amd-aqlprofile64.so: cannot open shared object file: No such file or directory
```

**uname -r**
```
5.10.12-gentoo-x86_64
```

**uname -p**
```
AMD Ryzen 5 4600H with Radeon Graphics
```

**eix -cI opencl**
```
[I] dev-libs/amdgpu-pro-opencl (20.40.1147286@09.02.2021): Proprietary OpenCL implementation for AMD GPUs
[I] dev-libs/rocm-opencl-runtime (4.0.0(0/4.0)@09.02.2021): Radeon Open Compute OpenCL Compatible Runtime
[I] dev-python/pyopencl (2020.3.1@09.02.2021): Python wrapper for OpenCL
[I] dev-util/opencl-headers (2020.06.16@31.01.2021): Unified C language headers for the OpenCL API
[I] virtual/opencl (3-r1@31.01.2021): Virtual for OpenCL API
```

**eix -cI rocm**
```
[I] app-admin/pprocm (1.0-r2@02.02.2021): ncurses-based program to monitor CPU, disk, network and memory usage
[I] dev-libs/rocm-comgr (4.0.0(0/4.0)@09.02.2021): Radeon Open Compute Code Object Manager
[I] dev-libs/rocm-device-libs (4.0.0(0/4.0)@09.02.2021): Radeon Open Compute Device Libraries
[I] dev-libs/rocm-opencl-runtime (4.0.0(0/4.0)@09.02.2021): Radeon Open Compute OpenCL Compatible Runtime
[I] dev-util/amd-rocm-meta (4.0.0(0/4.0)[1]@09.02.2021): Meta package for ROCm
[I] dev-util/rocm-clang-ocl [1] (4.0.0@09.02.2021): OpenCL compilation with clang compiler
[I] dev-util/rocm-cmake (4.0.0@09.02.2021): Radeon Open Compute CMake Modules
[I] dev-util/rocm-smi (4.0.0@09.02.2021): ROCm System Management Interface
[I] dev-util/rocminfo (4.0.0(0/4.0)@09.02.2021): ROCm Application for Reporting System Info
```
**eix -cI rocr**
```
[I] dev-libs/rocr-runtime (4.0.0(0/4.0)@09.02.2021): Radeon Open Compute Runtime
```

**eix -cI roct**
```
[I] dev-libs/roct-thunk-interface (4.0.0(0/4.0)@10.02.2021): Radeon Open Compute Thunk Interface
```

**eix -cI llvm-roc**
```
[I] sys-devel/llvm-roc (4.0.1@09.02.2021): Radeon Open Compute llvm,lld,clang
```

**eix -cI amd**
```
[I] dev-libs/amdgpu-pro-opencl (20.40.1147286@09.02.2021): Proprietary OpenCL implementation for AMD GPUs
[I] dev-util/amd-rocm-meta (4.0.0(0/4.0)[1]@09.02.2021): Meta package for ROCm
[I] x11-drivers/xf86-video-amdgpu (19.1.0@01.02.2021): Accelerated Open Source driver for AMDGPU cards
```

**ldd /usr/bin/clinfo**
```
        linux-vdso.so.1 (0x00007ffea75af000)
        libOpenCL.so.1 => /usr/lib64/libOpenCL.so.1 (0x00007f7875d7a000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f7875d74000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f7875bb1000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f7875b91000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f7875e00000)
```

**clinfo**
```
LoadLib(libhsa-amd-aqlprofile64.so) failed: libhsa-amd-aqlprofile64.so: cannot open shared object file: No such file or directory
Number of platforms                               2
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP.dbg (3212.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback
  Platform Extensions function suffix             AMD

  Platform Name                                   Portable Computing Language
  Platform Vendor                                 The pocl project
  Platform Version                                OpenCL 1.2 pocl 1.6, Gentoo+Asserts, LLVM 11.0.0, RELOC, SPIR, SLEEF, POCL_DEBUG
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             POCL

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx902
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0
  Driver Version                                  3212.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     GPU
  Device Board Name (AMD)                         Renoir
  Device PCI-e ID (AMD)                           0x1636
  Device Topology (AMD)                           PCI-E, 05:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               26
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1500MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     26
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple (kernel)     64
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
  Global memory size                              536870912 (512MiB)
  Global free memory (AMD)                        524288 (512MiB) 524288 (512MiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           456340272 (435.2MiB)
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
  Max size for global variable                    456340272 (435.2MiB)
  Preferred total size of global vars             536870912 (512MiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             5686
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
  Max pipe packet size                            456340272 (435.2MiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory size per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        456340272 (435.2MiB)
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
  Profiling timer offset since Epoch (AMD)        0ns (Thu Jan  1 03:00:00 1970)
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             26
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

  Platform Name                                   Portable Computing Language
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContext(NULL, ...) [other]              жм5ВU
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.12
  ICD loader Profile                              OpenCL 2.2
```

---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-02-10T04:42:52Z)

Thanks @Bogdan107 for reaching us.
Looks like your installation did not go well w.r.to hsa-amd-aqlprofile.
Can you please check whether you have installed this package in your machine as: **sudo dpkg -l | grep hsa**
If its not there, recommend to install as sudo apt install **sudo apt install hsa-amd-aqlprofile**

In my case, the package is available in my machine and no issues with any application.
taccuser@taccuser-SYS-4028GR-TR2:/opt$ sudo dpkg -l | grep hsa
ii  hsa-amd-aqlprofile                         1.0.0                                            amd64        AQLPROFILE library for AMD HSA runtime API extension support
ii  hsa-rocr-dev                               1.2.40000.0-rocm-rel-4.0-23-a5173c90             amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime for Boltzmann (ROCm) platforms
ii  hsakmt-roct                                20201016.1.0269-mainline-20201016-1-g0269ce3     amd64        HSAKMT library for AMD KFD support
ii  hsakmt-roct-dev  


Clinfo runs perfect too.
taccuser@taccuser-SYS-4028GR-TR2:/opt$ /opt/rocm/opencl/bin/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3212.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               2
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Vega 20
  Device Topology:                               PCI[ B#6, D#0, F#0 ]
  Max compute units:                             60
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
  Max clock frequency:                           1726Mhz
  Address bits:                                  64
  Max memory allocation:                         14588628168
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            16384
  Max image 3D height:                           16384
  Max image 3D depth:                            8192
  Max samplers within kernel:                    26273
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            17163091968
  Constant buffer size:                          14588628168
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          1703726280
  Max global variable size:                      14588628168
  Max global variable preferred total size:      17163091968
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
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
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7fd725229cf0
  Name:                                          gfx906
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                3212.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program


  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Vega 20
  Device Topology:                               PCI[ B#10, D#0, F#0 ]
  Max compute units:                             60
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
  Max clock frequency:                           1726Mhz
  Address bits:                                  64
  Max memory allocation:                         14588628168
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            16384
  Max image 3D height:                           16384
  Max image 3D depth:                            8192
  Max samplers within kernel:                    26273
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            17163091968
  Constant buffer size:                          14588628168
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          1703726280
  Max global variable size:                      14588628168
  Max global variable preferred total size:      17163091968
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
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
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7fd725229cf0
  Name:                                          gfx906
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                3212.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

Please let me know if you need any more information.
Thank you.

---

### 评论 #2 — Bogdan107 (2021-02-10T12:03:13Z)

### Usage of binary files from debian (FAIL).
Link (https://bugs.gentoo.org/716948) helps.
Precompiled binaries from [hsa-rocr-dev4.0.0](https://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-rocr-dev4.0.0/) and [hsa-amd-aqlprofile4.0.0](https://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-amd-aqlprofile4.0.0/) unpacked to _/opt_.

### Test 0 - list of supported hardware:
**hashcat -I**
```
hashcat (v6.0.0) starting...

LoadLib(libhsa-amd-aqlprofile64.so) failed: libhsa-amd-aqlprofile64.so: cannot open shared object file: No such file or directory                                                                                                             
CUDA Info:
==========

CUDA.Version.: 11.2

Backend Device ID #1 (Alias: #3)
  Name...........: GeForce GTX 1650
  Processor(s)...: 14
  Clock..........: 1515
  Memory.Total...: 3911 MB
  Memory.Free....: 3859 MB

OpenCL Info:
============

OpenCL Platform ID #1
  Vendor..: Advanced Micro Devices, Inc.
  Name....: AMD Accelerated Parallel Processing
  Version.: OpenCL 2.0 AMD-APP (3212.0)

  Backend Device ID #2
    Type...........: GPU
    Vendor.ID......: 1
    Vendor.........: Advanced Micro Devices, Inc.
    Name...........: gfx902
    Version........: OpenCL 2.0 
    Processor(s)...: 26
    Clock..........: 1500
    Memory.Total...: 512 MB (limited to 435 MB allocatable in one block)
    Memory.Free....: 384 MB
    OpenCL.Version.: OpenCL C 2.0 
    Driver.Version.: 3212.0 (HSA1.1,LC)

OpenCL Platform ID #2
  Vendor..: NVIDIA Corporation
  Name....: NVIDIA CUDA
  Version.: OpenCL 1.2 CUDA 11.2.66

  Backend Device ID #3 (Alias: #1)
    Type...........: GPU
    Vendor.ID......: 32
    Vendor.........: NVIDIA Corporation
    Name...........: GeForce GTX 1650
    Version........: OpenCL 1.2 CUDA
    Processor(s)...: 14
    Clock..........: 1515
    Memory.Total...: 3911 MB (limited to 977 MB allocatable in one block)
    Memory.Free....: 3840 MB
    OpenCL.Version.: OpenCL C 1.2 
    Driver.Version.: 460.27.04

OpenCL Platform ID #3
  Vendor..: The pocl project
  Name....: Portable Computing Language
  Version.: OpenCL 1.2 pocl 1.6, Gentoo+Asserts, LLVM 11.0.0, RELOC, SPIR, SLEEF, POCL_DEBUG

  Backend Device ID #4
    Type...........: CPU
    Vendor.ID......: 1
    Vendor.........: AuthenticAMD
    Name...........: pthread-AMD Ryzen 5 4600H with Radeon Graphics
    Version........: OpenCL 1.2 pocl HSTR: pthread-x86_64-pc-linux-gnu-znver1
    Processor(s)...: 12
    Clock..........: 3000
    Memory.Total...: 5214 MB (limited to 2048 MB allocatable in one block)
    Memory.Free....: 5150 MB
    OpenCL.Version.: OpenCL C 1.2 pocl
    Driver.Version.: 1.6
```

### Test 1 - check CUDA on Nvidia GPU (SUCCESS):
**time LD_LIBRARY_PATH=/opt/rocm-4.0.0/lib hashcat -b -m 0 -D 2 --backend-ignore-opencl**
```
hashcat (v6.0.0) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

nvmlDeviceGetFanSpeed(): Not Supported

CUDA API (CUDA 11.2)
====================
* Device #1: GeForce GTX 1650, 3859/3911 MB, 14MCU

Benchmark relevant options:
===========================
* --opencl-device-types=2
* --optimized-kernel-enable

Hashmode: 0 - MD5

Speed.#1.........: 10979.2 MH/s (86.08ms) @ Accel:64 Loops:1024 Thr:1024 Vec:1

Started: Wed Feb 10 13:58:25 2021
Stopped: Wed Feb 10 13:58:31 2021
LD_LIBRARY_PATH=/opt/rocm-4.0.0/lib hashcat -b -m 0 -D 2   3,40s user 2,58s system 96% cpu 6,218 total
```

### Test 2 - check OpenCL on AMD CPU (SUCCESS):
**time LD_LIBRARY_PATH=/opt/rocm-4.0.0/lib hashcat -b -m 0 -D 1**
```
hashcat (v6.0.0) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

CUDA API (CUDA 11.2)
====================
* Device #1: GeForce GTX 1650, skipped

OpenCL API (OpenCL 2.0 AMD-APP (3212.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #2: gfx902, skipped

OpenCL API (OpenCL 1.2 CUDA 11.2.66) - Platform #2 [NVIDIA Corporation]
=======================================================================
* Device #3: GeForce GTX 1650, skipped

OpenCL API (OpenCL 1.2 pocl 1.6, Gentoo+Asserts, LLVM 11.0.0, RELOC, SPIR, SLEEF, POCL_DEBUG) - Platform #3 [The pocl project]
==============================================================================================================================
* Device #4: pthread-AMD Ryzen 5 4600H with Radeon Graphics, 5150/5214 MB (2048 MB allocatable), 12MCU

Benchmark relevant options:
===========================
* --opencl-device-types=1
* --optimized-kernel-enable

Hashmode: 0 - MD5

Speed.#4.........:  1031.1 MH/s (12.04ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Started: Wed Feb 10 13:59:56 2021
Stopped: Wed Feb 10 14:00:04 2021
LD_LIBRARY_PATH=/opt/rocm-4.0.0/lib hashcat -b -m 0 -D 1  49,36s user 1,84s system 612% cpu 8,361 total
```
### Test 3 - check OpenCL on AMD GPU (FAIL):
**time LD_LIBRARY_PATH=/opt/rocm-4.0.0/lib hashcat -b -m 0 -D 2 --backend-ignore-cuda**
```
hashcat (v6.0.0) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

* Device #2: CUDA SDK Toolkit installation NOT detected.
             CUDA SDK Toolkit installation required for proper device support and utilization
             Falling back to OpenCL Runtime

^C
LD_LIBRARY_PATH=/opt/rocm-4.0.0/lib hashcat -b -m 0 -D 2 --backend-ignore-cud  12,30s user 19,43s system 99% cpu 32,030 total
```

### Results:
Test # 3 was canceled because the system is frozen.
First, the picture on the display froze, then the display blinks 2 times, and then the system does not respond to the keyboard or mouse. The display shows the image as before freezing.
I bring the system back under control in the following steps:
- restore input settings to default by SysRq (Alt-PrtScr-R);
- go to the console by Ctrl-Alt-F1;
- forcibly close hashcat;
- restart xdm.

As result, now I do not use precompiled binary of _libhsa-amd-aqlprofile64.so_.

---

### 评论 #3 — Bogdan107 (2021-02-10T12:24:03Z)

I think, that needed file _**libhsa-amd-aqlprofile64.so**_ was in _**dev-libs/hsa-runtime-amd**_ package, which require _**dev-libs/hsathk-amd**_. 
But I have trouble to compile _**hsathk-amd**_ from sources. Issue opened here - [ROCT-Thunk-Interface/issues/67](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/issues/67)

---

### 评论 #4 — ROCmSupport (2021-02-10T12:28:39Z)

OK.
Can you please share me the exact steps to reproduce.
Like cloning hashcat from github, steps to compile and run the code.
Thank you.

---

### 评论 #5 — Bogdan107 (2021-02-11T00:45:00Z)

No need usage [hashcat](https://github.com/hashcat/hashcat/blob/master/BUILD.md) for reproduce error.
clinfo give an error, as in hashcat:
**clinfo | head -n 0**
```
LoadLib(libhsa-amd-aqlprofile64.so) failed: libhsa-amd-aqlprofile64.so: cannot open shared object file: No such file or directory
```
_**head -n 0**_ filter stdout and show only stderr messages.

Result of test's are for exclude another possible places of trouble.
Result of tests:
- Test 1 - hashcat works normal in System (problem not in hashcat);
- Test 2 - OpenCL works normal in System (problem not in OpenCL);
- Test 3 - OpenCL fails on precompiled debian GPU drivers (problem in binary drivers).

I need to compile _**libhsa-amd-aqlprofile64.so**_ file.
_**hsa-amd-aqlprofile4.0.0_1.0.0_amd64.deb://INFO**_ say, that sources placed at [https://github.com/RadeonOpenCompute/HSA-AqlProfile-AMD-extension](https://github.com/RadeonOpenCompute/HSA-AqlProfile-AMD-extension), but that repository already removed from github.

So, I think, that system, which use _**libhsa-amd-aqlprofile64.so**_  file (which does not exists even in sources), must to be updated.

But which that system? Which package?
**LC_ALL=en_US.UTF-8 grep -r aqlprofile64 /usr/lib64**
```
grep: /usr/lib64/libhsa-runtime64.so.1.2.0: binary file matches
```
File _**ROCR-Runtime-rocm-4.0.0://src/inc/hsa_ven_amd_aqlprofile.h**_ says, that needed file - is an external library.

I unpack just _**libhsa-amd-aqlprofile64.so***_ files from _**hsa-amd-aqlprofile4.0.0_1.0.0_amd64.deb**_ to _**/opt/rocm1**_, and run:
**LD_LIBRARY_PATH=/opt/rocm1 hashcat -b -m 0 -D 2 --backend-ignore-cuda**
```
hashcat (v6.0.0) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

* Device #2: CUDA SDK Toolkit installation NOT detected.
             CUDA SDK Toolkit installation required for proper device support and utilization
             Falling back to OpenCL Runtime

^C
```
hashcat is hang, but system works fine, without frozen.
Without error messages in console or dmesg.
So, problem excatly in _**libhsa-amd-aqlprofile64.so**_ library.

### QUESTION:
Where I can get sources for _**libhsa-amd-aqlprofile**_ library?


---

### 评论 #6 — Bogdan107 (2021-02-11T02:55:41Z)

Page [https://github.com/RadeonOpenCompute/ROCm](https://github.com/RadeonOpenCompute/ROCm) in version of _[Jan 26, 2021](https://github.com/RadeonOpenCompute/ROCm/commit/2874a8ae6c5079f22c65e3e490d1275afe798886#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5)_
have message [supported-gpus](https://github.com/RadeonOpenCompute/ROCm#user-content-supported-gpus):
```
Note: The integrated GPUs of Ryzen are not officially supported targets for ROCm.
```
and [supported-cpus](https://github.com/RadeonOpenCompute/ROCm#user-content-supported-cpus):
```
AMD Ryzen CPUs
The CPUs in AMD Ryzen APUs
```

And my laptop has integrated GPU (Renoir) as part of CPU (Ryzen).

So, I can return to use with my iGPU an OpenCL version, which included in _media-libs/mesa_ (hashcat do not use opencl from mesa, because that driver marked as "Unstable OpenCL driver detected").

Issue may be closed `temporary`, but I still need source code of _**libhsa-amd-aqlprofile**_, when Ryzen iGPU supported.

---
