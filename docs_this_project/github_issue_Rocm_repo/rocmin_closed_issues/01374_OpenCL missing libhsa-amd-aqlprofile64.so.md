# OpenCL missing libhsa-amd-aqlprofile64.so

- **Issue #:** 1374
- **State:** closed
- **Created:** 2021-02-09T15:30:47Z
- **Updated:** 2021-02-11T03:49:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/1374

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