# RX 570 on Ubuntu 20.04 crashing and heavy artifacts upon OpenCL GPU rendering.

> **Issue #1276**
> **状态**: closed
> **创建时间**: 2020-11-04T22:19:07Z
> **更新时间**: 2021-01-04T23:12:46Z
> **关闭时间**: 2021-01-04T08:31:30Z
> **作者**: energizerbee
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1276

## 描述

Upon beginning a render in cycles on GPU compute with only the GPU selected, it will load for a second then crash before actually beginning the render in blender 2.82. In blender 2.83 it will render, but will have heavy artifacts, an example is rendering the default cube in GPU compute with only the basic scene provided upon opening the application, the shadow on the left side of the cube will appear brighter than normal look red. Upon rendering a porcelain Suzanne monkey with a white diffuse plane under it, the image with look very corrupted with streaks of white artifacts along with green and occasional red. im using rocm-dkms 3.9

---

## 评论 (13 条)

### 评论 #1 — rkothako (2020-11-09T06:51:45Z)

Thanks @energizerbee for reaching us.
Can you please help us with below logs.
1. /opt/rocm/bin/rocminfo
2. /opt/rocm/opencl/bin/clinfo
3. /opt/rocm/bin/rocm-smi

---

### 评论 #2 — energizerbee (2020-11-09T14:25:23Z)

1. /opt/rocm/bin/rocminfo
```
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
  Name:                    Intel(R) Core(TM) i5-10400 CPU @ 2.90GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i5-10400 CPU @ 2.90GHz
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
  Max Clock Freq. (MHz):   4300                               
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
      Size:                    16332792(0xf937f8) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16332792(0xf937f8) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
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
  Chip ID:                 26591(0x67df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1256                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
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
      Size:                    8388608(0x800000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx803          
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
````      
2./opt/rocm/opencl/bin/clinfo
````
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3204.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
  Device Topology:				 PCI[ B#1, D#0, F#0 ]
  Max compute units:				 32
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
  Max clock frequency:				 1256Mhz
  Address bits:					 64
  Max memory allocation:			 7301444400
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26591
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 8589934592
  Constant buffer size:				 7301444400
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 3006477104
  Max global variable size:			 7301444400
  Max global variable preferred total size:	 8589934592
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
  Platform ID:					 0x7fa8d653ccd0
  Name:						 gfx803
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3204.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program
``` 

3./opt/rocm/bin/rocm-smi

```
======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr   SCLK    MCLK     Fan     Perf  PwrCap  VRAM%  GPU%  
0    31.0c  31.179W  588Mhz  1000Mhz  18.82%  auto  120.0W    4%   0%    
================================================================================
============================= End of ROCm SMI Log ==============================

```
thank you for looking into it for me :)



---

### 评论 #3 — dragontamer (2020-11-09T23:22:58Z)

This is probably related to a long-running bug in ROCm's implementation of OpenCL: https://github.com/RadeonOpenCompute/ROCm/issues/402 

---

### 评论 #4 — energizerbee (2020-11-10T02:38:25Z)

i disagree... But good suggestion but the drivers were updated in late October and before that time (i got this PC in early October) the drivers worked completely fine until i upgraded the packages. Though i could just grab one of the recent versions before this one i just don't know how to... maybe sudo apt-get downgrade lol? 

---

### 评论 #5 — energizerbee (2020-11-12T15:13:52Z)

Is there a way to use apt to possibly reinstall version 3.8? how would i get around to downloading 3.8 or should i wait for the next update for a fix?

---

### 评论 #6 — rkothako (2020-11-13T06:07:56Z)

Hi @energizerbee 
You can install ROCm 3.8 from http://repo.radeon.com/rocm/apt/.apt_3.8/

---

### 评论 #7 — energizerbee (2020-11-13T14:34:13Z)

thanks man :)

---

### 评论 #8 — energizerbee (2020-11-13T15:55:07Z)

3.8 works but im going to keep the issue open and keep an eye on the future updates to see if he issue gets resolved thanks for your help :)

---

### 评论 #9 — amartincolby (2020-12-14T06:41:05Z)

3.8 does _not_ work for me, so this is still very much a pertinent issue. Blender will alternatively work very slowly or simply crash. Luxrender works, but I am suffering significant performance regression on the Hotel Luxmark scene.

---

### 评论 #10 — kode54 (2020-12-23T05:04:49Z)

No version of ROCm OpenCL to date has worked for Blender on my RX 480 8GB. And it appears to also walk all over the VRAM in the process of crashing, as evidenced by this trashed window decoration:

![2020-12-22_20 26 04](https://user-images.githubusercontent.com/796316/102961502-5152d480-4499-11eb-874e-8fd8d9dd0f29.png)


---

### 评论 #11 — ROCmSupport (2020-12-23T06:00:07Z)

Hi @kode54 
We are aware of Blender issue and Developer is working on fixes.
Please stay tuned for the updates.
Thank you

---

### 评论 #12 — ROCmSupport (2021-01-04T08:31:30Z)

AMD ROCm dropped supporting gfx8 officially from ROCm 4.0 as per https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support.
Hence closing this issue.
Thank you.

---

### 评论 #13 — kode54 (2021-01-04T23:12:46Z)

Cool, then I shall forever keep my copy of AMDGPU Pro 19.50 installed. Software deprecation shall not force me to spend money on incremental hardware upgrades.

---
