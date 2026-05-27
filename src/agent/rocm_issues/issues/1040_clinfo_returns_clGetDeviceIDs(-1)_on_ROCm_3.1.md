# clinfo returns clGetDeviceIDs(-1) on ROCm 3.1

> **Issue #1040**
> **状态**: closed
> **创建时间**: 2020-03-12T18:46:09Z
> **更新时间**: 2021-04-05T11:55:59Z
> **关闭时间**: 2021-04-05T11:55:59Z
> **作者**: emoon
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1040

## 描述

Hi,
When I run `/opt/rocm-3.1.0/opencl/bin/x86_64/clinfo` I get the following output

```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3084.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```
rocminfo gives

```
/opt/rocm-3.1.0/bin/rocminfo 
ROCk module is loaded
emoon is member of video group
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
  Name:                    AMD Ryzen Threadripper 2950X 16-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 2950X 16-Core Processor
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
  Max Clock Freq. (MHz):   3500                               
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
      Size:                    32805864(0x1f493e8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32805864(0x1f493e8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    AMD Ryzen Threadripper 2950X 16-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 2950X 16-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3500                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32805864(0x1f493e8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 3                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
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
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   2560                               
  Internal Node ID:        2                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
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
  Max Waves Per CU:        40(0x28)                           
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
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
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
Agent 4                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    3                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   3328                               
  Internal Node ID:        3                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
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
  Max Waves Per CU:        40(0x28)                           
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
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
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
Agent 5                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    4                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   17664                              
  Internal Node ID:        4                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
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
  Max Waves Per CU:        40(0x28)                           
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
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
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
Agent 6                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    5                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   18432                              
  Internal Node ID:        5                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
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
  Max Waves Per CU:        40(0x28)                           
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
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
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
it was suggested at the end of https://github.com/RadeonOpenCompute/ROCm/issues/977 to open a new issue for 3.1 as things had changed.

I'm on Ubuntu 18.04

---

## 评论 (20 条)

### 评论 #1 — emoon (2020-03-13T13:40:04Z)

Here is an strace of clinfo if that his helpful https://www.dropbox.com/s/bsiafogvpvjhyyo/clinfo_strace.txt?dl=0

---

### 评论 #2 — avimanyu786 (2020-03-17T16:39:41Z)

I'm using a Radeon VII with Ubuntu 18.04. My `clinfo` reports fine but I get that error on Folding@home:

![image](https://user-images.githubusercontent.com/28894462/76878183-7a0ac580-689a-11ea-9996-28c0e03a2d56.png)

However, when I run `rocminfo`, it produces all info correctly but also reports:

> Failed to get user name to check for video group membership

My current user and future users were added to the video group when rocm was first installed. I'm also currently on version 3.1.




---

### 评论 #3 — akostadinov (2020-03-18T17:50:26Z)

To make it work I need to make sure the folding client has access to `/dev/kfd`. Running as an appropriate group or having the file with permissive enough permissions. 

To make GPU be tedected I had to do:
```
export LD_LIBRARY_PATH=/opt/rocm/lib64:/opt/rocm/lib:/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:/opt/rocm/hip/lib
```
In addition using RHEL 7.7 I also have to run like:
```
/usr/bin/scl enable devtoolset-7 -- /usr/bin/FAHClient
```

See my `systemd` gist I wrote because I couldn't set the necessary configuration with the standard init.d file:
https://gist.github.com/akostadinov/a5acbb95c8142306f9c27597d16451db

But then receiving a work unit I am hitting:
```
Digital signatures verified
Folding@home GPU Core22 Folding@home Core
Version 0.0.2
Caught signal SIGABRT(6) on PID 5954
WARNING:Unexpected exit from science code
Saving result file ../logfile_01.txt
Saving result file science.log
Folding@home Core Shutdown: BAD_WORK_UNIT
```

There is an older issue #575 about folding. btw on RHEL 7.7 you may need to reinstall RPMs. See #1011

---

### 评论 #4 — avimanyu786 (2020-03-18T20:32:47Z)

Thank you so much @akostadinov 🙏 !

---

### 评论 #5 — Penguio (2020-03-18T20:57:00Z)

Hi
@avimanyu786 you are using Ubuntu and I'm using Debian so the solution should be comparable but I couldn't get it running with the infos from @akostadinov . Is it because rocm3.10 is installed to 
`/opt/rocm-3.1.0/`
and the exported Library path is pointing to
`/opt/rocm/`
?

Additionally I could not find
`/opt/rocm-3.1.0/lib64` and
`/opt/rocm-3.1.0/hip/lib`
Do I have to install something else eventually the package `hip` or should the exported library PATH point to an directory which does not exist?

If you need more infos:
output of
`/opt/rocm-3.1.0/opencl/bin/x86_64/clinfo`
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3084.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 10 XL/XT [Radeon RX Vega 56/64]
  Device Topology:				 PCI[ B#68, D#0, F#0 ]
  Max compute units:				 64
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
  Max clock frequency:				 1630Mhz
  Address bits:					 64
  Max memory allocation:			 7287183769
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26751
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
  Global memory size:				 8573157376
  Constant buffer size:				 7287183769
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 2992216473
  Max global variable size:			 7287183769
  Max global variable preferred total size:	 8573157376
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
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
  Platform ID:					 0x7ff9b13bdd30
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3084.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```

output from
`/opt/rocm-3.1.0/bin/rocminfo`
```
ROCk module is loaded
tobsi is member of video group
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
  Name:                    AMD Ryzen Threadripper 1950X 16-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 1950X 16-Core Processor
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
  Max Clock Freq. (MHz):   3400                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131784960(0x7dae100) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131784960(0x7dae100) KB            
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
  Marketing Name:          Vega 10 XL/XT [Radeon RX Vega 56/64]
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
  Chip ID:                 26751(0x687f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1630                               
  BDFID:                   17408                              
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
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
  Max Waves Per CU:        40(0x28)                           
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
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
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

and the first lines of
`/var/lib/fahclient/log.txt`
```
*********************** Log Started 2020-03-18T20:25:51Z ***********************
20:25:51:************************* Folding@home Client *************************
20:25:51:    Website: https://foldingathome.org/
20:25:51:  Copyright: (c) 2009-2018 foldingathome.org
20:25:51:     Author: Joseph Coffland <joseph@cauldrondevelopment.com>
20:25:51:       Args: --child --lifeline 2996 /etc/fahclient/config.xml --run-as
20:25:51:             fahclient --pid-file=/var/run/fahclient.pid --daemon
20:25:51:     Config: /etc/fahclient/config.xml
20:25:51:******************************** Build ********************************
20:25:51:    Version: 7.5.1
20:25:51:       Date: May 11 2018
20:25:51:       Time: 19:59:04
20:25:51: Repository: Git
20:25:51:   Revision: 4705bf53c635f88b8fe85af7675557e15d491ff0
20:25:51:     Branch: master
20:25:51:   Compiler: GNU 6.3.0 20170516
20:25:51:    Options: -std=gnu++98 -O3 -funroll-loops
20:25:51:   Platform: linux2 4.14.0-3-amd64
20:25:51:       Bits: 64
20:25:51:       Mode: Release
20:25:51:******************************* System ********************************
20:25:51:        CPU: AMD Ryzen Threadripper 1950X 16-Core Processor
20:25:51:     CPU ID: AuthenticAMD Family 23 Model 1 Stepping 1
20:25:51:       CPUs: 32
20:25:51:     Memory: 125.68GiB
20:25:51:Free Memory: 122.78GiB
20:25:51:    Threads: POSIX_THREADS
20:25:51: OS Version: 5.4
20:25:51:Has Battery: false
20:25:51: On Battery: false
20:25:51: UTC Offset: 1
20:25:51:        PID: 2998
20:25:51:        CWD: /var/lib/fahclient
20:25:51:         OS: Linux 5.4.0-4-amd64 x86_64
20:25:51:    OS Arch: AMD64
20:25:51:       GPUs: 1
20:25:51:      GPU 0: Bus:68 Slot:0 Func:0 AMD:5 Vega 10 XL/XT [Radeon RX Vega 56/64]
20:25:51:       CUDA: Not detected: Failed to open dynamic library 'libcuda.so':
20:25:51:             libcuda.so: cannot open shared object file: No such file or
20:25:51:             directory
20:25:51:     OpenCL: Not detected: clGetDeviceIDs() returned -1
20:25:51:***********************************************************************
20:25:51:<config>
20:25:51:  <!-- Client Control -->
20:25:51:  <client-threads v='2'/>
20:25:51:  <fold-anon v='true'/>
20:25:51:
20:25:51:  <!-- Folding Slot Configuration -->
20:25:51:  <cpus v='1'/>
20:25:51:
20:25:51:  <!-- Slot Control -->
20:25:51:  <power v='FULL'/>
20:25:51:
20:25:51:  <!-- User Information -->
20:25:51:  <user v='xxxxxxx'/>
20:25:51:
20:25:51:  <!-- Folding Slots -->
20:25:51:  <slot id='0' type='CPU'/>
20:25:51:</config>
20:25:51:Switching to user fahclient
20:25:51:Trying to access database...
20:25:51:Successfully acquired database lock
20:25:51:Enabled folding slot 00: READY cpu:1
20:25:51:WU00:FS00:Starting
```
Yes one core and two threads is right because I would like to have FaH running on GPU and Boinc Rosetta@Home on the CPU.

If somebody could help a beginner to get this working I would be very thankful.
Thanks

---

### 评论 #6 — avimanyu786 (2020-03-18T21:13:51Z)

@Penguio I just tested following along similar lines but still getting the same issue on FAH control. `/opt/rocm` is being shown as a symbolic link that points to `/opt/rocm-3.1.0/`. Like yours, I also cannot find `/opt/rocm-3.1.0/lib64/`. But `/opt/rocm-3.1.0/hip/lib/` is present.

![image](https://user-images.githubusercontent.com/28894462/77007366-19f34c80-698a-11ea-9abe-cd86e3b17ce5.png)

![image](https://user-images.githubusercontent.com/28894462/77007890-0b596500-698b-11ea-803a-4c4f5cda6a4e.png)

---

### 评论 #7 — Penguio (2020-03-18T21:33:41Z)

I just installed `hip-hcc` than `/opt/rocm-3.1.0/hip/lib` is there too.

Then I exported the Library path like this:
`export LD_LIBRARY_PATH=/opt/rocm-3.1.0/lib:/opt/rocm-3.1.0/opencl/lib/x86_64:/opt/rocm-3.1.0/hsa/lib:/opt/rocm-3.1.0/hip/lib`

But this didn't solve the problem that `/opt/rocm-3.1.0/opencl/bin/x86_64/clinfo` finds the `clGetDeviceIDs() ` and Folding@Home doesn't find it.

---

### 评论 #8 — akostadinov (2020-03-18T22:51:48Z)

I would recommend you to first get `FAHClient` working manually from command line and then see how to fix service. I had troubles making sure it runs with correct group and LD_LIBRARY_PATH.

---

### 评论 #9 — Penguio (2020-03-18T23:09:57Z)

For me it is working from command line with only one CPU core. 
The only missing part is that `FAHclient` does not detect the GPU because `FAHclient` did not get the `clGetDeviceIDs` so it could only use the CPU.
`/dev/kfd` has the owner `root.video` and permissions `660`

---

### 评论 #10 — kochd (2020-03-19T05:42:24Z)


![2020-03-19-1584596809](https://user-images.githubusercontent.com/1825660/77035634-7ddb3c80-69ad-11ea-82f0-d5144841e1ba.png)


For Debian (or alike) users:

```
adduser fahclient video 
```
_(because /dev/kfd is owned by the video group)_

Edit the old fashioned initd script /etc/init.d/FAHClient and add <pre>export LD_LIBRARY_PATH=/opt/rocm/lib:/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:/opt/rocm/hip/lib</pre> at the head of the file where USER,NAME,CONFIG,... is defined (make sure to add the **export** in front)

```
systemctl daemon-reload
```

now reboot _(as I didn't find a way to make the group change live)_.

However the next thing that will hit you is https://github.com/RadeonOpenCompute/ROCm/issues/575 which is unsolved by now.

```



```
 
@avimanyu786 
For Debian it its:
<pre>LD_LIBRARY_PATH=/opt/rocm/lib...</pre>
not 
<pre>LD_LIBRARY_PATH=/opt/rocm/lib64...</pre>
like on RHEL

---

### 评论 #11 — avimanyu786 (2020-03-19T12:52:35Z)

@kochd Thank you for your reply. I followed your instructions but still got the same issue: `OpenCL not detected: clGetDeviceIDs() returned -1` (on FAH control). `clinfo` reports fine on the terminal. I have a radeon 7 and an rx 550 with a ryzen 2700x cpu. FAHClient works fine from command line but with only cpu.

This is what `ls -l` reports on `/dev/` for `kfd`:

![image](https://user-images.githubusercontent.com/28894462/77059001-43e55700-69fc-11ea-90ff-88c720f4d796.png)

Later I found this [resource](https://foldingforum.org/viewtopic.php?f=74&t=31096) on the F@H forums.

Perhaps I need to login as fahclient as setting the user as the current user in the initd script would'nt make it work. So far I tested the user as root in the script and I was able to get OpenCL detected. But the GPUs still wouldn't get noticed. Later I edited the config.xml file at `/etc/fahclient/`. `gpu v` was initially set as `false` and there were no slot ids for gpus. Since I have exactly two, I added them.

```
<config>
  <!-- Client Control -->
  <fold-anon v='true'/>

  <!-- Folding Slot Configuration -->
  <gpu v='true'/>

  <!-- Slot Control -->
  <power v='full'/>

  <!-- User Information -->
  <user v='yourusername'/>

  <!-- Folding Slots -->
  <slot id='0' type='CPU'>
  </slot>

  <slot id='1' type='GPU'>
  </slot>

  <slot id='2' type='GPU'>
  </slot>

</config>
```

![image](https://user-images.githubusercontent.com/28894462/77068905-6e8bdb80-6a0d-11ea-97f5-ba8a2b61ba71.png)

 Hit #575. Hope it gets resolved soon.

```
12:22:28:WU01:FS01:0x22:WARNING:Unexpected exit from science code
12:22:28:WU01:FS01:0x22:Saving result file ../logfile_01.txt
12:22:28:WU01:FS01:0x22:Saving result file science.log
12:22:28:WU01:FS01:0x22:Folding@home Core Shutdown: BAD_WORK_UNIT
12:22:38:WU00:FS00:0xa7:Completed 165000 out of 500000 steps (33%)
12:23:00:WU00:FS00:0xa7:Completed 170000 out of 500000 steps (34%)
12:23:22:WU00:FS00:0xa7:Completed 175000 out of 500000 steps (35%)
12:23:45:WU00:FS00:0xa7:Completed 180000 out of 500000 steps (36%)
12:24:07:WU00:FS00:0xa7:Completed 185000 out of 500000 steps (37%)
```
@Penguio I hope this helps you as well.


---

### 评论 #12 — patvdleer (2020-03-19T18:26:47Z)

I still get the initial error of `clGetDeviceIDs(-1)` but I updated my config.xml as @avimanyu786 suggested, set the GPU to true and my VEGA64 does show up now...

![image](https://user-images.githubusercontent.com/1138136/77101371-7d778b80-6a17-11ea-9aea-18a35198dd57.png)

![image](https://user-images.githubusercontent.com/1138136/77101410-8cf6d480-6a17-11ea-870c-c6537494d3c4.png)

-- EDIT -- 

it does not work...
```
19:33:12:WU02:FS01:Received Unit: id:02 state:DOWNLOAD error:NO_ERROR project:11746 run:0 clone:4081 gen:1 core:0x22 unit:0x000000028ca304f15e6aa9cfa32ffe03
19:33:12:WU02:FS01:Starting
19:33:12:ERROR:WU02:FS01:Failed to start core: OpenCL device matching slot 1 not found, try setting 'opencl-index' manually
```


---

### 评论 #13 — avimanyu786 (2020-03-20T09:40:59Z)

@patvdleer Try editing `/etc/fahclient/config.xml` to:

```
<slot id='1' type='GPU'>
  <opencl-index v='0'/>
</slot>
```
Are you logging in as `fahclient` username into Linux? So far I've tested it as regular Linux user but root user set in the `/etc/init.d/FAHClient` script. Your GPU and OpenCL info is still not detected in your first screenshot. Please tally it with the last screenshot of my previous post.

---

### 评论 #14 — patvdleer (2020-03-20T11:22:46Z)

I had already added that to the config. I did add `fahclient` to the video group but that doesn't seem to be enough, running fahclient as `root` does work.
Sadly I know run into:

```
11:13:33:WU01:FS00:0x22:Folding@home GPU Core22 Folding@home Core
11:13:33:WU01:FS00:0x22:Version 0.0.2
11:13:39:WU01:FS00:0x22:Caught signal SIGABRT(6) on PID 3612
11:13:39:WU01:FS00:0x22:WARNING:Unexpected exit from science code
11:13:39:WU01:FS00:0x22:Saving result file ../logfile_01.txt
11:13:39:WU01:FS00:0x22:Saving result file science.log
11:13:39:WU01:FS00:0x22:Folding@home Core Shutdown: BAD_WORK_UNIT
```

![image](https://user-images.githubusercontent.com/1138136/77159172-228c7580-6aa5-11ea-8f55-5b2f30d5b1ba.png)



---

### 评论 #15 — Frogging101 (2020-03-23T20:36:14Z)

@patvdleer I think I know why adding the `fahclient` user to the `video` group does not work. If it's being launched with the default init script that passes `--run-as fahclient`, the FAHClient process does not give itself the supplementary groups of the `run-as` user. It probably only does `setuid()`, which is not enough. You can see for yourself with `sudo cat /proc/[fahclient PID]/status | grep Groups:`. If there are no group IDs on the line that it returns, then it means the process does not have any supplementary groups and therefore does not have the access privileges of the `video` group.

This could be fixed by writing a systemd unit to replace the `init.d` script, with the appropriate options to run FAHClient as the desired user. There are probably other possible workarounds too.

---

### 评论 #16 — akostadinov (2020-03-23T22:20:18Z)

@Frogging101 , check my [earlier comment](https://github.com/RadeonOpenCompute/ROCm/issues/1040#issuecomment-600774465) :)

There are needed no special systemd service flags because user already has all supplementary groups.

I guess you will need a little adaptation for ubuntu. Because on RHEL 7 i needed to use scl. You should not need such thing.

---

### 评论 #17 — patvdleer (2020-04-04T13:38:50Z)

Sadly is doesn't matter on what user I run it as long as it's cpu only, see https://github.com/RadeonOpenCompute/ROCm/issues/575

---

### 评论 #18 — DaDummy (2020-04-08T18:08:28Z)

For Ubuntu 19.10 at least, documentation needs an adjustment:

According to an strace `/dev/dri/renderD128` needs to be accessed for clGetDeviceIDs to succeed. Access to this file is controlled through membership in the `render` group as opposed to the `video` group here. So users will need to be added to that group, too, for ROCm OpenCL to be correctly detected.

---

### 评论 #19 — ilia2s (2020-07-31T22:02:57Z)

If you successfuly install an amdgpu-pro latest (20.10-20.30) driver in ubuntu 20.04, 20.20
(dkms successfuly build) linux can not load it without amd_iommu module. (see dmesg | grep amdgpu for "symbol error")
and clinfo for "no openCL device found". Simple try to install linux-modules-extra for your kernel version:
for example: sudo apt install linux-modules-extra-4.15.0-20-generic


---

### 评论 #20 — ROCmSupport (2021-04-05T11:55:59Z)

Thanks @emoon for reaching out.
This issue is fixed long back and no more observed with the latest ROCm builds, I tried with the same on the latest ROCm 4.1, issue is no more seen. Request you to try the same.
Feel free to open a new issue, if any, for quick resolution.
Thank you.

---
