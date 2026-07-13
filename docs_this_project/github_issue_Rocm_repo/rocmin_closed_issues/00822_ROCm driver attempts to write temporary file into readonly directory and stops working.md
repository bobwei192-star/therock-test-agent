# ROCm driver attempts to write temporary file into readonly directory and stops working

- **Issue #:** 822
- **State:** closed
- **Created:** 2019-06-16T17:46:42Z
- **Updated:** 2024-01-14T04:42:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/822

The problem:
Hashcat is unable to use the OpenCL device unless it is run as root.

See issue filed for Hashcat: https://github.com/hashcat/hashcat/issues/2062

A Hashcat developer analyzed the problem and came up with a workaround that enables me to run their application without root privileges:
`export TMPDIR=$HOME/`

The conclusion from their end is that the problem is not with Hashcat. See their [comment](https://github.com/hashcat/hashcat/issues/2062#issuecomment-502664272).

The part of the strace command they pointed at:
```
12147 openat(AT_FDCWD, "/usr/local/share/hashcat/OpenCL/t_12147_16-f6e20b.o", O_RDWR|O_CREAT|O_EXCL|O_CLOEXEC, 0600) = -1 EACCES (Permissão negada)
```

I've attached the output of two strace commands used by Hashcat to study the problem.

[strace-clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/3297591/strace-clinfo.txt)
[strace-hashcat.txt](https://github.com/RadeonOpenCompute/ROCm/files/3297592/strace-hashcat.txt)

ROCm runtime version: **2.4.0-1** (from [AUR](https://aur.archlinux.org/packages/rocm-opencl-runtime/))
OS: Arch Linux
Kernel version: 5.1.9-arch1-1-ARCH
Device: AMD RX 560 4GB

**Running with an unprivileged, default user:**
```
$ hashcat -a 3 -m 0 -O 8743b52063cd84097a65d1633f5c74f5
hashcat (v5.1.0-1151-g5e0eb288) starting...

clGetPlatformIDs(): CL_PLATFORM_NOT_FOUND_KHR

ATTENTION! No OpenCL-compatible or CUDA-compatible platform found.

You are probably missing the OpenCL or CUDA runtime installation.

* AMD GPUs on Linux require this driver:
  "RadeonOpenCompute (ROCm)" Software Platform (1.6.180 or later)
* Intel CPUs require this runtime:
  "OpenCL Runtime for Intel Core and Intel Xeon Processors" (16.1.1 or later)
* Intel GPUs on Linux require this driver:
  "OpenCL 2.0 GPU Driver Package for Linux" (2.0 or later)
* NVIDIA GPUs require this runtime and/or driver (both):
  "NVIDIA Driver" (418.56 or later)
  "CUDA Toolkit" (10.1 or later)

Started: Sun Jun 16 14:31:15 2019
Stopped: Sun Jun 16 14:31:15 2019
```

**Running as root: device found**
```
$ sudo hashcat -a 3 -m 0 -O 8743b52063cd84097a65d1633f5c74f5
hashcat (v5.1.0-1151-g5e0eb288) starting...

OpenCL API (OpenCL 2.0 AMD-APP.internal (2874.0)) - Platform #1 [Advanced Micro Devices, Inc.]
==============================================================================================
* Device #1: gfx803, 3481/4096 MB allocatable, 14MCU

(...) Job starts and completes successfully.
```

**`clinfo` output:**
```
$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP.internal (2874.0)
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
  Driver Version                                  2874.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X]
  Device Topology (AMD)                           PCI-E, 01:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               14
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1176MHz
  Graphics IP (AMD)                               8.3
  Device Partition                                (core)
    Max number of sub-devices                     14
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
  Global memory size                              4294967296 (4GiB)
  Global free memory (AMD)                        4192256 (3.998GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           3650722201 (3.4GiB)
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
  Max constant buffer size                        3650722201 (3.4GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  P2P devices (AMD)                               (n/a)
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 21:00:00 1969)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             14
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
    Device Name                                   gfx803
```