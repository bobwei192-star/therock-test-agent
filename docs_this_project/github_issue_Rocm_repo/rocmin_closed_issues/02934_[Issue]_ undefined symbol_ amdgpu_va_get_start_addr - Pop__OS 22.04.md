# [Issue]: undefined symbol: amdgpu_va_get_start_addr - Pop!_OS 22.04

- **Issue #:** 2934
- **State:** closed
- **Created:** 2024-02-27T22:15:05Z
- **Updated:** 2024-09-17T17:36:54Z
- **Labels:** ROCm 6.0.0, AMD Radeon RX 7900 XT
- **URL:** https://github.com/ROCm/ROCm/issues/2934

### Problem Description

Hi, apologies if the bug report is of bad quality, but I am a beginner at this.
I have a RX 7600 that I'd like to use for OpenCL computing. With mesa-opencl-icd OpenCL fails with an error message `No such file or directory: /usr/lib/clc/gfx1102-amdgcn-mesa-mesa3d.bc`

Therefore, I thought that maybe I need AMDGPU-pro to make it work. So I installed it following the procedure below, and it worked flawlessly for a while, but then stopped working all of a sudden.

If I run clinfo, I get:
```
jacopo@prodesk:~$ clinfo
clinfo: symbol lookup error: /usr/lib/x86_64-linux-gnu/gallium-pipe/pipe_[radeonsi.so](http://radeonsi.so/): undefined symbol: amdgpu_va_get_start_addr
```

As soon as I run `amdgpu-uninstall` even without rebooting, clinfo starts working again (but no compute can be done due to the mesa error above)

I am at a loss, and any pointer can help. Thanks!

### Operating System

Pop!_OS 22.04 LTS

### CPU

Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz

### GPU

AMD Radeon RX 7600

### ROCm Version

ROCm 6.0.0

### ROCm Component

ROCm (OpenCL)

### Steps to Reproduce

Installation steps:
```
sudo amdgpu-install --usecase=opencl --no-dkms
sudo usermod -a -G video $LOGNAME
sudo usermod -a -G render $LOGNAME
sudo apt install opencl-headers ocl-icd-libopencl1 clinfo -y
sudo apt-get install amdgpu-lib rocm-opencl-runtime rocm-hip-runtime -y
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
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
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4400                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32779032(0x1f42b18) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32779032(0x1f42b18) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32779032(0x1f42b18) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1102                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 7600                 
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      2048(0x800) KB                     
  Chip ID:                 29824(0x7480)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2250                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 550                                
  SDMA engine uCode::      16                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1102         
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
```

### Additional Information

Kernel is: `6.6.10-76060610-generic #202401051437~1704728131~22.04~24d69e2` 

clinfo **WITHOUT ROCm INSTALLED** (mesa-opencl-icd)
```
DRM_IOCTL_I915_GEM_APERTURE failed: Invalid argument
Assuming 131072kB available aperture size.
May lead to reduced performance or incorrect rendering.
get chip id failed: -1 [2]
param: 4, val: 0
i915 does not support EXECBUFER2
DRM_IOCTL_I915_GEM_APERTURE failed: Invalid argument
Assuming 131072kB available aperture size.
May lead to reduced performance or incorrect rendering.
get chip id failed: -1 [2]
param: 4, val: 0
i915 does not support EXECBUFER2
beignet-opencl-icd: no supported GPU found, this is probably the wrong opencl-icd package for this hardware
(If you have multiple ICDs installed and OpenCL works, you can ignore this message)
DRM_IOCTL_I915_GEM_APERTURE failed: Invalid argument
Assuming 131072kB available aperture size.
May lead to reduced performance or incorrect rendering.
get chip id failed: -1 [2]
param: 4, val: 0
i915 does not support EXECBUFER2
DRM_IOCTL_I915_GEM_APERTURE failed: Invalid argument
Assuming 131072kB available aperture size.
May lead to reduced performance or incorrect rendering.
get chip id failed: -1 [2]
param: 4, val: 0
i915 does not support EXECBUFER2
beignet-opencl-icd: no supported GPU found, this is probably the wrong opencl-icd package for this hardware
(If you have multiple ICDs installed and OpenCL works, you can ignore this message)
Number of platforms                               2
  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 24.0.0-1pop0~1706872735~22.04~0fa430c
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   Intel Gen OCL Driver
  Platform Vendor                                 Intel
  Platform Version                                OpenCL 2.0 beignet 1.3
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_3d_image_writes cl_khr_image2d_from_buffer cl_khr_depth_images cl_khr_spir cl_khr_icd cl_intel_accelerator cl_intel_subgroups cl_intel_subgroups_short
  Platform Extensions function suffix             Intel
DRM_IOCTL_I915_GEM_APERTURE failed: Invalid argument
Assuming 131072kB available aperture size.
May lead to reduced performance or incorrect rendering.
get chip id failed: -1 [2]
param: 4, val: 0
i915 does not support EXECBUFER2
beignet-opencl-icd: no supported GPU found, this is probably the wrong opencl-icd package for this hardware
(If you have multiple ICDs installed and OpenCL works, you can ignore this message)

  Platform Name                                   Clover
Number of devices                                 1
  Device Name                                     AMD Radeon RX 7600 (radeonsi, navi33, LLVM 15.0.7, DRM 3.54, 6.6.10-76060610-generic)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 24.0.0-1pop0~1706872735~22.04~0fa430c
  Device Numeric Version                          0x401000 (1.1.0)
  Driver Version                                  24.0.0-1pop0~1706872735~22.04~0fa430c
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               32
  Max clock frequency                             2250MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
=== CL_PROGRAM_BUILD_LOG ===
fatal error: cannot open file '/usr/lib/clc/gfx1102-amdgcn-mesa-mesa3d.bc': No such file or directory
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
  Max memory allocation                           2147483648 (2GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       32768 bits (4096 bytes)
  Global Memory cache type                        None
  Image support                                   No
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
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
    ILs with version                              SPIR-V                                                           0x400000 (1.0.0)
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

  Platform Name                                   Intel Gen OCL Driver
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  Clover
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [MESA]
  clCreateContext(NULL, ...) [default]            Success [MESA]
  clCreateContext(NULL, ...) [other]              
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD Radeon RX 7600 (radeonsi, navi33, LLVM 15.0.7, DRM 3.54, 6.6.10-76060610-generic)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD Radeon RX 7600 (radeonsi, navi33, LLVM 15.0.7, DRM 3.54, 6.6.10-76060610-generic)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD Radeon RX 7600 (radeonsi, navi33, LLVM 15.0.7, DRM 3.54, 6.6.10-76060610-generic)

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.14
  ICD loader Profile                              OpenCL 3.0
```