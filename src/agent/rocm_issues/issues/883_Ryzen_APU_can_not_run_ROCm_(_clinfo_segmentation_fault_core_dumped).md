# Ryzen APU can not run ROCm? ( clinfo segmentation fault core dumped)

> **Issue #883**
> **状态**: closed
> **创建时间**: 2019-09-11T15:48:23Z
> **更新时间**: 2020-10-06T11:06:42Z
> **关闭时间**: 2020-10-06T03:12:56Z
> **作者**: dduzzi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/883

## 描述

HI, i bought PIcasso R5 laptop.
i have tried ROCm to install Ubuntu 18.04.

when i check up command as[ /opt/rocm/bin/rocminfo ], it works well.
but [ /opt/rocm/opencl/bin/x86_64/clinfo ] not working.

it shows message -  [ segmentation fault (core dumped) ]

AMD Ryzen Picasso can't run ROCm correctly?

dduzzi@dduzzi-HP-Laptop-15-db1xxx:~$ /opt/rocm/bin/rocminfo 
ROCk module is loaded
dduzzi is member of video group
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
  Name:                    AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
  Marketing Name:          AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
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
    L1:                      32(0x20) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2100                               
  BDFID:                   1280                               
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16776832(0xfffe80) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Marketing Name:          AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1200                               
  BDFID:                   1280                               
  Internal Node ID:        0                                  
  Compute Unit:            11                                 
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        160(0xa0)                          
  Max Work-item Per CU:    10240(0x2800)                      
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack    
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

## 评论 (17 条)

### 评论 #1 — luyatshimbalanga (2019-09-15T17:50:56Z)

I successfully reproduced the issue after installing rocm-opencl with Ryzen 2500U. 
```
  Name:                    AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
...

 Package             Architecture   Version                  Repository    Size
================================================================================
Installing:
 rocm-opencl         x86_64         1.2.0-2019082856         ROCm          51 M

Transaction Summary
================================================================================
Install  1 Package

Total download size: 51 M
Installed size: 169 M
Is this ok [y/N]: y
Downloading Packages:
rocm-opencl-1.2.0-2019082856.x86_64.rpm         910 kB/s |  51 MB     00:57    
--------------------------------------------------------------------------------
Total                                           910 kB/s |  51 MB     00:57     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                        1/1 
  Running scriptlet: rocm-opencl-1.2.0-2019082856.x86_64                    1/1 
  Installing       : rocm-opencl-1.2.0-2019082856.x86_64                    1/1 
  Running scriptlet: rocm-opencl-1.2.0-2019082856.x86_64                    1/1 
  Verifying        : rocm-opencl-1.2.0-2019082856.x86_64                    1/1 

Installed:
  rocm-opencl-1.2.0-2019082856.x86_64                                           

Complete!
 
clinfo
Segmentation fault (core dumped)
```

Current workaround is using OpenCL from official AMD Linux driver and the slower Mesa version.

---

### 评论 #2 — dduzzi (2019-09-18T03:39:27Z)

You have also error message relative clinfo
- Segmentation fault (core dumped)

I do success to command 'rocminfo'
APU only support by OpenCL but you and i also fail to load ROCm opencl

---

### 评论 #3 — luyatshimbalanga (2019-11-13T04:57:34Z)

Newer version of rocm-opencl (rocm-opencl-1.2.0-2019100124.x86_64
) should restore its functionality on Ryzen APU
```
 clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (2982.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx902+xnack
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0 
  Driver Version                                  2982.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
  Device Topology (AMD)                           PCI-E, 03:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               11
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1100MHz
  Graphics IP (AMD)                               9.2
  Device Partition                                (core)
    Max number of sub-devices                     11
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
  Global memory size                              7876274176 (7.335GiB)
  Global free memory (AMD)                        7691674 (7.335GiB)
  Global memory channels (AMD)                    2
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           6694833049 (6.235GiB)
  Unified memory for Host and Device              Yes
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   Yes
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    6694833049 (6.235GiB)
  Preferred total size of global vars             7876274176 (7.335GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             5597
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
    Max number of read/write image args           64
  Max number of pipe args                         16
  Max active pipe reservations                    16
  Max pipe packet size                            2399865753 (2.235GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        6694833049 (6.235GiB)
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
  P2P devices (AMD)                               (n/a)
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 16:00:00 1969)
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

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902+xnack
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902+xnack
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902+xnack
```
 Additionally, that version run slower than the opencl-amdgpu-pro meaning optimization for speed is not there yet.

---

### 评论 #4 — WalterPiTheScienceGuy (2020-01-03T18:35:26Z)

I just produced the exact same readout with AMD Ryzen 5 3500U as dduzzi (except my BFID was 768).
My rocm-opencl version is '2.0.0-rocm-rel-3.0-6-9a4afec'
Regarding the 'Segmentation fault (core dumped)', I also got that last night when trying a customized ROCm implementation specifically for AMD Ryzen (gfx902) by 'Bruhnspace ROCm project for AMD APUs'.  I decided to reinstall Ubuntu today and try AMD's newest ROCm (v3.0) to see if it would be better, but I guess something is persistently wrong.

Reading other threads... https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/68 seems to be the most substantial discussion.  Looks like the problem has been fixed for some people, but not others.  They supposedly patched this in v2.9, but here I am with v3.0 having the same problem.

---

### 评论 #5 — WalterPiTheScienceGuy (2020-01-03T19:48:05Z)

Update:  I installed ROCm v2.9 instead of v3.0, and now 'clinfo' works!

Results of rocminfo and clinfo below:
---------------------------------

waltp@waltp-HP-Pavilion-Laptop-15z-cw100:~$  /opt/rocm/bin/rocminfo
ROCk module is loaded
waltp is member of video group
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
  Name:                    AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
  Marketing Name:          AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
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
    L1:                      32(0x20) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2100                               
  BDFID:                   768                                
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16776832(0xfffe80) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Marketing Name:          AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1200                               
  BDFID:                   768                                
  Internal Node ID:        0                                  
  Compute Unit:            11                                 
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        160(0xa0)                          
  Max Work-item Per CU:    10240(0x2800)                      
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack    
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
waltp@waltp-HP-Pavilion-Laptop-15z-cw100:~$  /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
  Device Topology:				 PCI[ B#3, D#0, F#0 ]
  Max compute units:				 11
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1200Mhz
  Address bits:					 64
  Max memory allocation:			 6237514444
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 5592
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 7338252288
  Constant buffer size:				 6237514444
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 1942547148
  Max global variable size:			 6237514444
  Max global variable preferred total size:	 7338252288
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 Yes
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 1
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f3074913d30
  Name:						 gfx902+xnack
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 2982.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

---

### 评论 #6 — JoranMichiels (2020-01-15T14:29:16Z)

Same problem with AMD Ryzen 7 PRO 3700U, installing ROCm v2.9 instead of v3.0 solved it.

---

### 评论 #7 — dduzzi (2020-02-09T11:38:02Z)

@JoranMichiels  @WalterPiTheScienceGuy  @luyatshimbalanga 

Thanks a lot for everyone.
I sell the R5 laptop and back to MacBookPro 13.

there are solution after I sell the laptop. lol I should maintain keep it.

I have plan to buy Ryzen Renoir laptop and I will use non-gpu mode of machine learning library for a while. the problem may appear agin.


Thanks again, and take care virus.

---

### 评论 #8 — simone-nai (2020-02-11T17:00:21Z)

Hi everyone

I have similar problem, but a little different.
**Looks like it can't get my username.**

And I add also this, if can be helpful to find the bug: user and group for folder opencl looks like this number **1001**

You're doing a great work with this software...
I kindly ask to try to find the bug, I need to use ROCm asap  ^_^

Peace and love, 
Simone

```
simone@simone-HP:~$ ls -al /opt/rocm/
totale 56
drwxrwxr-x 14 root root 4096 feb 11 17:30 .
drwxr-xr-x  3 root root 4096 feb 11 17:29 ..
drwxrwxr-x  2 root root 4096 feb 11 17:34 bin
drwxrwxr-x  8 root root 4096 feb 11 17:30 hcc
drwxrwxr-x  8 root root 4096 feb 11 17:30 hip
drwxrwxr-x  4 root root 4096 feb 11 17:30 hsa
drwxrwxr-x  3 root root 4096 feb 11 17:30 hsa-amd-aqlprofile
drwxrwxr-x  2 root root 4096 feb 11 17:34 include
drwxrwxr-x  2 root root 4096 feb 11 17:30 .info
drwxrwxr-x  3 root root 4096 feb 11 17:34 lib
drwxrwxr-x  5 1001 1001 4096 feb 11 17:30 opencl
drwxrwxr-x  4 root root 4096 feb 11 17:30 rocm_smi
drwxrwxr-x  6 root root 4096 feb 11 17:30 rocprofiler
drwxrwxr-x  6 root root 4096 feb 11 17:30 share

```

```
/opt/rocm/bin/rocminfo
ROCk module is loaded
Failed to get user name to check for video group membership
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
  Name:                    AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
  Marketing Name:          AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
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
    L1:                      32(0x20) KB                        
  Chip ID:                 5597(0x15dd)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2000                               
  BDFID:                   1024                               
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    8388224(0x7ffe80) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Marketing Name:          AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 5597(0x15dd)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1100                               
  BDFID:                   1024                               
  Internal Node ID:        0                                  
  Compute Unit:            11                                 
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        160(0xa0)                          
  Max Work-item Per CU:    10240(0x2800)                      
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack    
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

---

### 评论 #9 — dduzzi (2020-03-01T06:06:58Z)

> Failed to get user name to check for video group membership

it seems your hostname is not included, 'video' group.

check the installation guide.

[https://github.com/RadeonOpenCompute/ROCm](url)



To add your user to the video group, use the following command for the sudo password:

 sudo usermod -a -G video $LOGNAME

By default, add any future users to the video group. Run the following command to add users to the video group:

 echo 'ADD_EXTRA_GROUPS=1' 		
 sudo tee -a /etc/adduser.conf   
 echo 'EXTRA_GROUPS=video' 		
 sudo tee -a /etc/adduser.conf

Restart the system.


---

### 评论 #10 — simone-nai (2020-03-01T23:15:15Z)

> > Failed to get user name to check for video group membership
> 
> it seems your hostname is not included, 'video' group.
> 
> check the installation guide.
> 
> [https://github.com/RadeonOpenCompute/ROCm](url)
> 
> To add your user to the video group, use the following command for the sudo password:
> 
> sudo usermod -a -G video $LOGNAME
> 
> By default, add any future users to the video group. Run the following command to add users to the video group:
> 
> echo 'ADD_EXTRA_GROUPS=1'
> sudo tee -a /etc/adduser.conf
> echo 'EXTRA_GROUPS=video'
> sudo tee -a /etc/adduser.conf
> 
> Restart the system.

Thank you for your quick reply,
unfortunately, this doesn't solve my problem because as you can see groups are ok (according to guide)
```
groups simone 
simone : simone adm cdrom sudo dip video plugdev lpadmin sambashare
```

Can I ask you also to check again the code you pasted? because I think the char **|** is missing. Is this the code that you wanted me to run instead?
```
echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
```

Anyway, any other ideas about how to fix the problem I said? :)

Thank you very much!
Simone


---

### 评论 #11 — grigio (2020-05-26T09:04:09Z)

Can somebody do a recap? Is Amd 3500u supported by ROCm ?

---

### 评论 #12 — ghost (2020-06-06T20:08:15Z)

Hi folks, also keen to know whether any support for the 3500u is present. :)

---

### 评论 #13 — grigio (2020-08-22T09:56:50Z)

is possible to have an update is AMD Radeon 3500u is supported by rocm?

---

### 评论 #14 — dduzzi (2020-09-03T10:19:33Z)

> is possible to have an update is AMD Radeon 3500u is supported by rocm?

I don't know 3500U working. It runs on recently version of ROCm.

I use 4500U. It works good.

---

### 评论 #15 — a-repko (2020-10-05T09:30:22Z)

> I use 4500U. It works good.

@dduzzi How did you manage to run ROCm OpenCL on 4500U? I'm not able to run it on Ryzen 7 PRO 4750G. In particular, what is your kernel version (output of `uname -a`) and ROCm version? Did you apply any special configuration in your kernel? I'm suspecting memory encryption (which is anyway disabled), or another kernel option, but I was not able to pinpoint it (I tried kernels 5.7.19 and 5.8.11, and ROCm 3.8 and 3.5.1).

---

### 评论 #16 — dduzzi (2020-10-06T03:17:28Z)

@a-repko 

I tested Ubuntu 20.04 , Linux kernel 5.4(default kernel) , and It works good. I tried to kernel 5.6 over, It failed.
It had system stopping symptom on kernel 5.6 over when 'clinfo' checking up.

I strongly recommend use linux kernel 5.4 and Ubuntu 20.04. Don't use linux kerenel 5.6 over. 
referenced by this video for install ROCm

https://youtu.be/efKjfBkjPlM

i hope my reply helps you.

---

### 评论 #17 — a-repko (2020-10-06T11:06:42Z)

@dduzzi 
Thank you very much for the information. So it seems that you used ROCk kernel driver from the ROCm stack, because amdgpu from linux kernel 5.4 doesn't support APU Renoir yet. I'm using Gentoo, where ROCm stack depends on the upstream kernel driver (no ROCk). Recently, I tried again to build kernel 5.8.13, where I removed support for memory encryption and hibernate+suspend features, and I also rebuilt ROCm 3.7. It seemed a little bit more stable, I even managed to run some short OpenCL self-test calculation (which was apparently successful), but still, the GPU driver crashed soon after, causing the system lock-up.

Another parameter, which might be related, is that I'm using ECC UDIMM memory with my APU (yes, it indeed appears to work! Linux EDAC driver reports multi-bit ECC with "x4 syndromes"), but rocminfo denies the presence od error correction.

Next week, there will be new linux kernel 5.9, and your result gives me some confidence that it can finally work (let's hope that the AMD developers managed to push the driver updates from ROCk to upstream kernel).

---
