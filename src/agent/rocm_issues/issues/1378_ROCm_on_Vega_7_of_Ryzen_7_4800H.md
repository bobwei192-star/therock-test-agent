# ROCm on Vega 7 of Ryzen 7 4800H

> **Issue #1378**
> **状态**: closed
> **创建时间**: 2021-02-11T22:23:54Z
> **更新时间**: 2024-01-29T23:31:38Z
> **关闭时间**: 2021-02-12T04:49:06Z
> **作者**: jneuhauser
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1378

## 描述

Hello devs,

as I'm doing a lot of ml stuff with tensorflow, i tested to run the rocm port of tensorflow on my renior notebook with integrated GPU.

If i run the container with `drun rocm/tensorflow:latest` and execute `python3 -c "import tensorflow as tf" "tf.config.list_physical_devices('GPU')"` inside a interactive python console, i get the following errror:
```
/src/external/hip-on-vdi/rocclr/hip_code_object.cpp:120: guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")
Aborted (core dumped)
```
Does this mean my integrated GPU isn't supported?

I've installed ROCm on my arch linux with the instructions on: https://github.com/rocm-arch/rocm-arch

My output of rocminfo:
```
[johann@johann-nb ~]$ rocminfo 
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
  Name:                    AMD Ryzen 7 4800H with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 4800H with Radeon Graphics
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
  Max Clock Freq. (MHz):   2900                               
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
      Size:                    15855164(0xf1ee3c) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    15855164(0xf1ee3c) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Renoir                             
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
  Chip ID:                 5686(0x1636)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   1024                               
  Internal Node ID:        1                                  
  Compute Unit:            27                                 
  SIMDs per CU:            4                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
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
      Size:                    524288(0x80000) KB                 
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
      Name:                    amdgcn-amd-amdhsa--gfx902          
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

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-02-12T04:49:06Z)

Thanks @jneuhauser for reaching us.
We are not supporting Renior GPU and any integrated GPUs for now. Basic things might work but not major things like TF etc.,.
Request you to follow our ROCm documenatation for the supported hardware and all other information @ [https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support](url)

---

### 评论 #2 — awehrfritz (2022-05-11T08:45:50Z)

Has there been any update on the GPU support end over the past year? In particular I am wondering whether the integrated GPU in my Lenovo Thinkpad P14s Gen 2, with a Ryzen 7 PRO 5850U APU based on a Radeon Vega 8 (i.e. Renoir) GPU, is supported?

The AMD webpages are less than easy to navigate and information on which hardware is supported has apparently been removed from the above link. @ROCmSupport could you please clarify this and provide some pointers to clear documentation and the correct hardware support page?

---

### 评论 #3 — Fei1Yang (2023-04-02T14:17:05Z)

This should not be "closed as **completed**" if the decision is "not supporting Renior GPU and any integrated GPUs **for now**", please reopen this issue.

---

### 评论 #4 — CataCluj (2024-01-29T23:31:29Z)

The above link to check HW compatibility does not work. Please provide a new one. Especially for Linux.

---
