# [Issue]: Continued APU support required for newer versions of ROCm and Linux

- **Issue #:** 5967
- **State:** open
- **Created:** 2026-02-15T08:28:06Z
- **Updated:** 2026-05-04T23:58:24Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5967

### Problem Description

Latest ROCm versions (6 & 7) [do not appear to work](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html) on Linux Mint 22 / Ubuntu 24 for the GPU/APU integrated with the CPU. The last known working version was version 5.4.5, on Linux Mint 21. There have been some complaints about it mentioned in [this thread](https://github.com/ROCm/ROCm/issues/2216#issuecomment-2001933917) too.
  
**Problems:**  
* I had to switch back to using Mint 21 because of this. It prevents me from making use of the newest features and security updates of the newer operating systems.
* High-profile third party frameworks like Mojo struggle to provide support for such APU's as mentioned [here](https://forum.modular.com/t/how-to-get-mojo-to-detect-amd-integrated-gpu-apu/2727). This is a systemic technical hurdle.  
* GPU prices have skyrocketed, and for various segments of users it is uneconomical to purchase a new GPU, so it would help to be able to continue to use the integrated GPU which we spent our hard earned money to purchase. Especially for hobby projects and basic machine learning and even gaming, it is useful.
  
Could AMD ensure that such hardware is supported with software updates for at least 10 to 15 years? Would it be possible for y'all to put forward such a request to your managers and obtain approval? Or would it help if users like me send an email to perhaps `rocm-feedback@amd.com` regarding this to request for support?

### Operating System

Linux Mint 21.3 (Virginia)

### CPU

AMD Ryzen 5 5600G with Radeon Graphics

### GPU

gfx90c amdgcn-amd-amdhsa--gfx90c:xnack- AMD Ryzen 5 5600G with Radeon Graphics

### ROCm Version

6 or 7 (the last working version was 5.4.5. Even 5.5.5 didn't work on my hardware (gets installed but pytorch was unable to use the GPU, if I remember correctly))

### ROCm Component

_No response_

### Steps to Reproduce

Install Linux Mint 22. Try installing ROCm versions compatible with Linux Mint 22. Then try running PyTorch and see if it can detect and use the GPU like in [this page](https://github.com/ROCm/ROCm/issues/2216#issuecomment-1637054248).

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

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
  Name:                    AMD Ryzen 5 5600G with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 5600G with Radeon Graphics
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
  Max Clock Freq. (MHz):   3900                               
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
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    28619192(0x1b4b1b8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    28619192(0x1b4b1b8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    28619192(0x1b4b1b8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx90c                             
  Uuid:                    GPU-XX                             
  Marketing Name:                                             
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
    L1:                      16(0x10) KB                        
    L2:                      1024(0x400) KB                     
  Chip ID:                 5688(0x1638)                       
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1900                               
  BDFID:                   12288                              
  Internal Node ID:        1                                  
  Compute Unit:            7                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
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
      Name:                    amdgcn-amd-amdhsa--gfx90c:xnack-   
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

### Additional Information

_No response_