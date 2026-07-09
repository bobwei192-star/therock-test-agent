# 2x RX 6600 XT - AMDGPUPRO Clinfo - ERROR: clBuildProgram(-11) - Only one GPU listed

- **Issue #:** 1575
- **State:** closed
- **Created:** 2021-09-21T01:42:33Z
- **Updated:** 2021-09-23T10:31:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/1575

Hello everyone,

I'm looking for help about the issue i am facing on my system:
Motherboard: MSI B450-A PRO MAX with latest BIOS
CPU: AMD Athlon 3000G
OS: Ubuntu 20.04.3 LTS
Kernel: 5.11.0-34-generic
AMD Drivers: amdgpu-pro-21.30-1290604-ubuntu-20.04 built with --opencl=rocr,legacy
Mesa: 21.2.0
GPUs: XFX QICK 308 RX6600XT & Powercolor Fighter RX6600XT

When i run `sudo /opt/amdgpu-pro/bin/clinfo`, it is ending on an error:
```
Number of platforms:				 2
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.1 Mesa 21.0.3
  Platform Name:				 Clover
  Platform Vendor:				 Mesa
  Platform Extensions:				 cl_khr_icd
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3314.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 Clover
Number of devices:				 3
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Max compute units:				 32
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 16
  Preferred vector width short:			 8
  Preferred vector width int:			 4
  Preferred vector width long:			 2
  Preferred vector width float:			 4
  Preferred vector width double:		 2
  Native vector width char:			 16
  Native vector width short:			 8
  Native vector width int:			 4
  Native vector width long:			 2
  Native vector width float:			 4
  Native vector width double:			 2
  Max clock frequency:				 1200Mhz
  Address bits:					 64
  Max memory allocation:			 6871947673
  Image support:				 No
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 32768
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 No
    Round to +ve and infinity:			 No
    IEEE754-2008 fused multiply-add:		 No
  Cache type:					 None
  Cache line size:				 0
  Cache size:					 0
  Global memory size:				 8589934592
  Constant buffer size:				 67108864
  Max number of constant args:			 16
  Local memory type:				 Scratchpad
  Local memory size:				 32768
ERROR: clBuildProgram(-11)
```
If i use the command line `clinfo` from the Ubuntu repository (`sudo apt-get install clinfo`), i'm actually getting more details about the error:
```
Number of platforms                               2
  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 21.0.3
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (3314.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD

  Platform Name                                   Clover
Number of devices                                 3
  Device Name                                     AMD DIMGREY_CAVEFISH (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 21.0.3
  Driver Version                                  21.0.3
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               32
  Max clock frequency                             1200MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
=== CL_PROGRAM_BUILD_LOG ===
fatal error: cannot open file '/usr/local//usr/lib/clc/gfx1030-amdgcn-mesa-mesa3d.bc': No such file or directory
  Preferred work group size multiple              <getWGsizes:1200: create kernel : error -46>
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
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_extended_versioning

  Device Name                                     AMD DIMGREY_CAVEFISH (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 21.0.3
  Driver Version                                  21.0.3
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               32
  Max clock frequency                             2900MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
=== CL_PROGRAM_BUILD_LOG ===
fatal error: cannot open file '/usr/local//usr/lib/clc/gfx1030-amdgcn-mesa-mesa3d.bc': No such file or directory
  Preferred work group size multiple              <getWGsizes:1200: create kernel : error -46>
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
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_extended_versioning

  Device Name                                     AMD RAVEN2 (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 21.0.3
  Driver Version                                  21.0.3
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               3
  Max clock frequency                             1100MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
=== CL_PROGRAM_BUILD_LOG ===
fatal error: cannot open file '/usr/local//usr/lib/clc/gfx909-amdgcn-mesa-mesa3d.bc': No such file or directory
  Preferred work group size multiple              <getWGsizes:1200: create kernel : error -46>
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
  Global memory size                              7993212928 (7.444GiB)
  Error Correction support                        No
  Max memory allocation                           5595249049 (5.211GiB)
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
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_extended_versioning

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx1032
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0 
  Driver Version                                  3314.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Device 73ff
  Device Topology (AMD)                           PCI-E, 12:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               16
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                32
  SIMD instruction width (AMD)                    1
  Max clock frequency                             2900MHz
  Graphics IP (AMD)                               10.3
  Device Partition                                (core)
    Max number of sub-devices                     16
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
  Global memory size                              8573157376 (7.984GiB)
  Global free memory (AMD)                        8372224 (7.984GiB)
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
    Max number of samplers per kernel             29695
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
  Max pipe packet size                            2992216472 (2.787GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
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
  P2P devices (AMD)                               <printDeviceInfo:147: get number of CL_DEVICE_P2P_DEVICES_AMD : error -30>
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Thu Jan  1 00:00:00 1970)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             16
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 


NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [MESA]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD DIMGREY_CAVEFISH (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (3)
    Platform Name                                 Clover
    Device Name                                   AMD DIMGREY_CAVEFISH (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
    Device Name                                   AMD DIMGREY_CAVEFISH (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
    Device Name                                   AMD RAVEN2 (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (3)
    Platform Name                                 Clover
    Device Name                                   AMD DIMGREY_CAVEFISH (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
    Device Name                                   AMD DIMGREY_CAVEFISH (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
    Device Name                                   AMD RAVEN2 (DRM 3.42.0, 5.11.0-34-generic, LLVM 12.0.0)
```
So what is the problem here? Is it again another drivers issue from the Team Red?