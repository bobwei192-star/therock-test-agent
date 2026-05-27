# [Issue]: amdgpu-install doesn't install hip (to the correct place?)

> **Issue #6285**
> **状态**: closed
> **创建时间**: 2026-05-21T01:44:24Z
> **更新时间**: 2026-05-25T15:04:59Z
> **关闭时间**: 2026-05-25T15:04:59Z
> **作者**: CMTacoTophat
> **标签**: status: triage
> **URL**: https://github.com/ROCm/ROCm/issues/6285

## 标签

- **status: triage** (颜色: #585dd7)

## 负责人

- harkgill-amd

## 描述

### Problem Description

Hello, I'm relatively new here, so I apologize if this is an established issue, or my lack of knowledge is unbecoming, but I couldn't seem to find any fix.
I'm trying to install ROCm and HIP for use with HDF5 with multi-threading to eventually run scientific simulations. I've tried for a long while now, but I can't seem to install ROCm with HIP correctly.

What happens for me is such: even when using "sudo amdgpu-install --usecase=rocm,hip,rocmdev,hiplibsdk", the rocm folder "/opt/rocm-7.2.3" doesn't have a "hip" subdirectory, and several things don't work:

- hipconfig throws errors ("Warning: HIP version file: "/opt/rocm-7.2.3/hip/share/hip/version" not found.  Cannot give HIP version information", and "hip-clang-cxxflags : sh: 1: /opt/rocm-7.2.3/hip/bin/hipcc: not found \ hip-clang-ldflags : sh: 1: /opt/rocm-7.2.3/hip/bin/hipcc: not found")
- compiling a test program also throws errors ("clang++: error: cannot find HIP runtime; provide its path via '--rocm-path', or pass '-nogpuinc' to build without HIP runtime")

However, hipcc is still found with "which hipcc". Also, that second point is the most important - despite running the amdgpu-install command, I wasn't able to run any test programs. In addition, there appears to be no /opt/rocm/

Again, I've also botched several installation attempts before, so I'm not sure if that would cause any part of this either.

### Operating System

Mint 22.3 Zena (Ubuntu 24.04 LTS Noble Numbat)

### CPU

Intel(R) Core(TM) i5-9400F CPU @ 2.90GHz

### GPU

AMD Radeon RX 7600

### ROCm Version

ROCm 7.2.3

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

/opt/rocm-7.2.3/bin/rocminfo --support
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.15
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Core(TM) i5-9400F CPU @ 2.90GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i5-9400F CPU @ 2.90GHz
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
  Max Clock Freq. (MHz):   4100                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            6                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    16296268(0xf8a94c) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16296268(0xf8a94c) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16296268(0xf8a94c) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16296268(0xf8a94c) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
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
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2250                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
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
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*** Done *** 

### Additional Information

_No response_

---

## 评论 (4 条)

### 评论 #1 — harkgill-amd (2026-05-21T14:48:14Z)

Hey @CMTacoTophat, from the warning `HIP version file: "/opt/rocm-7.2.3/hip/share/hip/version" not found`, it looks like you have a stale `HIP_PATH` potentially from one of your previous installs. To get a better baseline to investigate from, could you please clean your installs
```
sudo amdgpu-install --uninstall --rocmrelease=all
sudo apt purge amdgpu-install
sudo apt autoremove
```
At this point, if `HIP_PATH` still persists in your environment, please manually remove it. Then reinstall ROCm with,
```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/7.2.3/ubuntu/noble/amdgpu-install_7.2.3.70203-1_all.deb
sudo apt install ./amdgpu-install_7.2.3.70203-1_all.deb
amdgpu-install -y --usecase=graphics,rocm
```
> In addition, there appears to be no /opt/rocm/

This is likely a bug with ROCm on Linux Mint similar to https://github.com/ROCm/ROCm/issues/5037. Will look into this further but you shouldn't see any of the hipconfig/hipcc compilation issues after following the above.

---

### 评论 #2 — CMTacoTophat (2026-05-22T00:51:02Z)

Sorry for the late reply - I'll try this tomorrow and let you know how it goes then. Thank you for your support!

---

### 评论 #3 — CMTacoTophat (2026-05-22T21:07:53Z)

Hello again, I have success!

First I tried the commands you suggested (and removed the hip/rocm environment variables), including a restart before the reinstall. Afterwards, however, it had the same issue. 

Secondly, I tried it again, with "sudo amdgpu-install -y  --usecase=graphics,rocm,hip" and it ended up working, both in the sense that hipconfig returned no warning and a test program could both be compiled and run. Although, the rocm folder is still named "rocm-7.2.3", there is not a "hip" subfolder (there is hip stuff IN the OTHER subfolders, however), and the paths didn't create or at least persist, despite having done so on the first attempt.

I'll keep moving forward with this for now, but I'll be sure to return if I have any more issues. Thanks again!

---

### 评论 #4 — harkgill-amd (2026-05-25T15:04:59Z)

Nice,looks like the fix was mix of cleaning up the existing installations and adding in the `hip` usecase. The missing `/opt/rocm` folder symlink will also be fixed in a future release. Thanks for the report!

---
