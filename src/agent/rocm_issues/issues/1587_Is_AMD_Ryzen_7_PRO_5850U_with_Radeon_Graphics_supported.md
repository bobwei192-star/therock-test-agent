# Is AMD Ryzen 7 PRO 5850U with Radeon Graphics supported?

> **Issue #1587**
> **状态**: closed
> **创建时间**: 2021-10-12T09:38:56Z
> **更新时间**: 2022-04-05T12:24:45Z
> **关闭时间**: 2021-10-12T10:04:42Z
> **作者**: delijati
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1587

## 描述

Is my hardware supported?

Installed newest version getting this error:
```
$ AMD_LOG_LEVEL=6 ../../env/bin/python 02-Clustering.py
GENERATING EMBEDDING FOR: ATL_X
:3:rocdevice.cpp            :430 : 1885913346 us: Initializing HSA stack.
:3:comgrctx.cpp             :33  : 1885933593 us: Loading COMGR library.
:3:rocdevice.cpp            :196 : 1885936584 us: Numa selects cpu agent[0]=0x5568b74df830(fine=0x5568bb072be0,coarse=0x5568bad2bcf0, kern_arg=0x5568bb6f3f90) for gpu agent=0x7fa4db72ab34
:3:rocdevice.cpp            :1562: 1885937163 us: HMM support: 0, xnack: 0

:4:rocdevice.cpp            :1858: 1885937272 us: Allocate hsa host memory 0x7fa4e0002000, size 0x28
:4:rocdevice.cpp            :1858: 1885937696 us: Allocate hsa host memory 0x7fa460600000, size 0x101000
:4:rocdevice.cpp            :1858: 1885937997 us: Allocate hsa host memory 0x7fa460400000, size 0x101000
:4:runtime.cpp              :82  : 1885938102 us: init
:1:hip_code_object.cpp      :456 : 1885938529 us: hipErrorNoBinaryForGpu: Unable to find code object for all current devices!
:1:hip_code_object.cpp      :458 : 1885938540 us:   Devices:
:1:hip_code_object.cpp      :460 : 1885938542 us:     amdgcn-amd-amdhsa--gfx902:xnack- - [Not Found]
:1:hip_code_object.cpp      :465 : 1885938543 us:   Bundled Code Objects:
:1:hip_code_object.cpp      :482 : 1885938544 us:     host-x86_64-unknown-linux - [Unsupported]
:1:hip_code_object.cpp      :479 : 1885938546 us:     hipv4-amdgcn-amd-amdhsa--gfx1030 - [code object v4 is amdgcn-amd-amdhsa--gfx1030]
:1:hip_code_object.cpp      :479 : 1885938547 us:     hipv4-amdgcn-amd-amdhsa--gfx803 - [code object v4 is amdgcn-amd-amdhsa--gfx803]
:1:hip_code_object.cpp      :479 : 1885938549 us:     hipv4-amdgcn-amd-amdhsa--gfx900:xnack- - [code object v4 is amdgcn-amd-amdhsa--gfx900:xnack-]
:1:hip_code_object.cpp      :479 : 1885938550 us:     hipv4-amdgcn-amd-amdhsa--gfx906:xnack- - [code object v4 is amdgcn-amd-amdhsa--gfx906:xnack-]
:1:hip_code_object.cpp      :479 : 1885938552 us:     hipv4-amdgcn-amd-amdhsa--gfx908:xnack- - [code object v4 is amdgcn-amd-amdhsa--gfx908:xnack-]
:1:hip_code_object.cpp      :479 : 1885938553 us:     hipv4-amdgcn-amd-amdhsa--gfx90a:xnack+ - [code object v4 is amdgcn-amd-amdhsa--gfx90a:xnack+]
:1:hip_code_object.cpp      :479 : 1885938555 us:     hipv4-amdgcn-amd-amdhsa--gfx90a:xnack- - [code object v4 is amdgcn-amd-amdhsa--gfx90a:xnack-]
/home/foo/.cache/yay/hip-rocclr/src/HIP-rocm-4.3.1/rocclr/hip_code_object.cpp:486: "hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
[1]    17615 abort (core dumped)  AMD_LOG_LEVEL=6 ../../env/bin/python 02-Clustering.py
AMD_LOG_LEVEL=6 ../../env/bin/python 02-Clustering.py  2,52s user 3,90s system 141% cpu 4,544 total
```
rocminfo:
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

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 PRO 5850U with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 PRO 5850U with Radeon Graphics
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
  Max Clock Freq. (MHz):   1900                               
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
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    28567612(0x1b3e83c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    28567612(0x1b3e83c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    28567612(0x1b3e83c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Cezanne                            
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
  Chip ID:                 5688(0x1638)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2000                               
  BDFID:                   1792                               
  Internal Node ID:        1                                  
  Compute Unit:            28                                 
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
      Size:                    4194304(0x400000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx902:xnack-   
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
*** Done ***             ```
```

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-10-12T10:04:42Z)

Hi @delijati 
Thanks for reaching out.
I certainly understood the problem.
Integrated GPUs are NOT supported with ROCm. But CPU perspective, Ryzen is supported.
I recommend to look at @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url) for supported cards. Hope this helps.
Thank you.

---

### 评论 #2 — delijati (2021-10-12T10:56:31Z)

> Integrated GPUs are NOT supported with ROCm.

Why? I found literally 100 issues on Github where people are asking the same question over and over again, but never a explanation why "Integrated GPUs" are not supported. Even my 8 year old T430 with a Nvidia card has still some minimal CUDA capabilities.

---

### 评论 #3 — delijati (2021-11-15T17:00:33Z)

@ROCmSupport can this maybe be reconsidered? The current chip shortage makes it kinda impossible to get any alternative GPU :/

---

### 评论 #4 — serge-cohen (2022-04-05T12:24:44Z)

Indeed I got very similar hardware : a Ryzen Pro 7 (5850U) crahsing anytime an OpenCL on ROCm task is run.
Conversely the same type of activity on a AMD Ryzen 5 4500U (with Vega graphics as well) is not causing much troubles.
Both APU are displyaing the same graphics core (gfx902) in rocminfo (and gfx902:xnack+ in clinfo).

Even "just" clinfo sometime is sufficient to completely crash the  Ryzen Pro 7 laptop (the other one is a mini PC/NUC type formfactor).

---
