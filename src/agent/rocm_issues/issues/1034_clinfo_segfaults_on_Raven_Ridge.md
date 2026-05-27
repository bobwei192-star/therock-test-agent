# clinfo segfaults on Raven Ridge

> **Issue #1034**
> **状态**: closed
> **创建时间**: 2020-03-02T21:27:23Z
> **更新时间**: 2021-04-19T12:47:45Z
> **关闭时间**: 2021-04-19T12:47:45Z
> **作者**: stefan-reich
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1034

## 描述

Please advise... OS is Peppermint Linux 10. User is in the "video" group, not sure what that one line is about.

```
stefan@ryzen5 ~ $ /opt/rocm/bin/rocminfo
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
stefan@ryzen5 ~ $ /opt/rocm/opencl/bin/x86_64/clinfo
Segmentation fault
```


---

## 评论 (2 条)

### 评论 #1 — dundir (2020-04-13T07:34:51Z)

That error could be any number of things. The error only indicates that OpenCL isn't working. Pytorch/Tensorflow may work even if OpenCL isn't working.

The Ryzen CPU has the vendor listed as CPU whereas the APU vendor is listed as AMD. That's how you tell the two apart. The rock module being used will depend on the kernel you are running. AFAIK the DKMS module isn't compatible for kernels beyond 5.0.

The video group warning usually indicates you aren't running with the correct privileges or you aren't part of the video group or both.

rocm-smi should display correctly, and you should be able to load python code into tensorflow/pytorch to test whether its working properly.

Some people have had OpenCL failing since v2.10. Others have been running into what looks like a complex firmware/amdkfd/rocm issue which may depend on the motherboard model, and its firmware. There have been some QA issues for some subsets of hardware.

I had a similar issue, you can read more about it here (#1013). Overall I had a 2 month non-response so no idea when it will be resolved, if ever.

---

### 评论 #2 — ROCmSupport (2021-04-19T12:47:45Z)

This issue is fixed and no more observed with the latest ROCm 4.1.
Recommend to try with the same.
More over Raven is not a supported config with ROCm.
Thank you.

---
