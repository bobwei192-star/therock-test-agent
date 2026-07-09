# Help with ROCm & OpenCL

- **Issue #:** 236
- **State:** closed
- **Created:** 2017-10-25T06:30:21Z
- **Updated:** 2017-10-27T01:06:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/236

Hi,
I do not know where I can go to get help. If there's a proper platform to ask, please refer me!
While Linux is the only distribution I've used for years, I am nonetheless broadly unfamiliar with kernels, systems programming, runtimes, etc. I have no idea what I'm talking about. If there are guides / tutorials applicable to this sort of thing so that I can have some grasp of things and not just metaphorically mash buttons, that would help.

That said, I am having trouble getting ROCm to work. Currently, I am on Fedora 26. If necessary, I will install (the supported by ROCm, but otherwise no longer supported) Fedora 24.

I bought three GPUs -- my plan is to run a lot of simulations:
```bash
[celrod@localhost Documents]$ lspci | grep VGA
0c:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XT [Radeon RX Vega 64] (rev c0)
43:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XT [Radeon RX Vega 64] (rev c0)
46:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XT [Radeon RX Vega 64] (rev c0)
```
I do realize that only the Vega FE is listed among supported GPUs in the README, but imagine the RX series ought to work for OpenCL somehow.

I have installed rocm:
```bash
[celrod@localhost Documents]$ dnf info rocm-opencl-devel
Last metadata expiration check: 22:46:39 ago on Tue 24 Oct 2017 02:12:02 AM CDT.
Installed Packages
Name         : rocm-opencl-devel
Version      : 1.2.0
Release      : 1430311
Arch         : x86_64
Size         : 52 M
Source       : rocm-opencl-1.2.0-1430311.src.rpm
Repo         : @System
From repo    : remote
Summary      : OpenCL/ROCm
License      : unknown
Description  : DESCRIPTION
             : ===========
```
Following suggestions here: https://rocm.github.io/install_issues.html
It is obvious I had trouble initializing the GPU.
```bash
[celrod@localhost Documents]$ dmesg | grep kfd
[celrod@localhost Documents]$ dmesg | grep amdgpu
[    4.599972] [drm] amdgpu kernel modesetting enabled.
[celrod@localhost Documents]$ 
```

The output of clinfo:
```bash
[celrod@localhost Documents]$ clinfo
X server found. dri2 connection failed! 
Device open failed, aborting...
Number of platforms                               3
  Platform Name                                   Portable Computing Language
  Platform Vendor                                 The pocl project
  Platform Version                                OpenCL 2.0 pocl 0.14, LLVM 4.0.0
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             POCL

  Platform Name                                   Intel Gen OCL Driver
  Platform Vendor                                 Intel
  Platform Version                                OpenCL 2.0 beignet 1.4
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_3d_image_writes cl_khr_image2d_from_buffer cl_khr_depth_images cl_khr_spir cl_khr_icd cl_intel_accelerator cl_intel_subgroups cl_intel_subgroups_short cl_intel_media_block_io cl_intel_planar_yuv cl_khr_gl_sharing
  Platform Extensions function suffix             Intel
X server found. dri2 connection failed! 
Device open failed, aborting...
cl_get_gt_device(): error, unknown device: ffffffff

  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 17.2.2
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   Portable Computing Language
Number of devices                                 1
  Device Name                                     pthread-AMD Ryzen Threadripper 1950X 16-Core Processor
  Device Vendor                                   AuthenticAMD
  Device Vendor ID                                0x1022
  Device Version                                  OpenCL 2.0 pocl HSTR: pthread-x86_64-unknown-linux-gnu-haswell
  Driver Version                                  0.14
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     CPU, Default
  Device Available                                Yes
  Device Profile                                  FULL_PROFILE
  Max compute units                               32
  Max clock frequency                             3400MHz
  Device Partition                                (core)
    Max number of sub-devices                     32
    Supported partition types                     equally, by counts
  Max work item dimensions                        3
  Max work item sizes                             4096x4096x4096
  Max work group size                             4096
  Compiler Available                              Yes
  Linker Available                                Yes
  Preferred work group size multiple              8
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2       
    half                                                 8 / 8        (n/a)
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
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              69619585024 (64.84GiB)
  Error Correction support                        No
  Max memory allocation                           69619585024 (64.84GiB)
  Unified memory for Host and Device              Yes
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    0
  Preferred total size of global vars             0
  Global Memory cache type                        Read/Write
  Global Memory cache size                        32768 (32KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            4351224064 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             65536x65536 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                128
    Max number of read/write image args           128
  Max number of pipe args                         16
  Max active pipe reservations                    1
  Max pipe packet size                            1024
  Local memory type                               Global
  Local memory size                               69619585024 (64.84GiB)
  Max constant buffer size                        69619585024 (64.84GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties (on host)                      
    Out-of-order execution                        No
    Profiling                                     Yes
  Queue properties (on device)                    
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                16384 (16KiB)
    Max size                                      262144 (256KiB)
  Max queues on device                            1
  Max events on device                            1024
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_spir cl_khr_int64 cl_khr_fp64 cl_khr_int64_base_atomics cl_khr_int64_extended_atomics

  Platform Name                                   Intel Gen OCL Driver
Number of devices                                 0

  Platform Name                                   Clover
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [POCL]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No platform
```

Now, I also do not know what I should or could modify the grub kernel to.
It is currently:
```
GRUB_DEFAULT=saved
```

Perhaps I've mucked things up enough enough that by now it would be easier to wipe everything and start fresh. Like, I did install mesa drivers at some point:
```bash
Last metadata expiration check: 23:09:32 ago on Tue 24 Oct 2017 02:12:02 AM CDT.
Installed Packages
Name         : mesa-libOpenCL
Version      : 17.2.2
Release      : 2.fc26
Arch         : x86_64
Size         : 2.0 M
Source       : mesa-17.2.2-2.fc26.src.rpm
Repo         : @System
From repo    : updates
Summary      : Mesa OpenCL runtime library
URL          : http://www.mesa3d.org
License      : MIT
Description  : Mesa OpenCL runtime library.
```
Perhaps that was a mistake, and causes conflict with, eg, rocm-opencl.

