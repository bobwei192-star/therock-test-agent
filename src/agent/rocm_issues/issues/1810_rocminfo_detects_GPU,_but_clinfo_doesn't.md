# rocminfo detects GPU, but clinfo doesn't

> **Issue #1810**
> **状态**: closed
> **创建时间**: 2022-09-21T00:39:21Z
> **更新时间**: 2023-02-28T08:23:06Z
> **关闭时间**: 2022-09-21T02:40:18Z
> **作者**: ColonelPhantom
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1810

## 描述

clinfo does not detect my GPU:
```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP.dbg (3452.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD
  Platform Host timer resolution                  1ns

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform
```
but the weird thing is, `rocminfo` does detect it!
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
  Name:                    AMD Ryzen 7 5800 8-Core Processor  
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 5800 8-Core Processor  
  Vendor Name:             CPU                                
(skipped)
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 580 Series           
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
  Chip ID:                 26591(0x67df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1411                               
  BDFID:                   1280                               
  Internal Node ID:        1                                  
  Compute Unit:            36                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
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
```
(clinfo also does not detect my CPU, is that normal?)

---

## 评论 (5 条)

### 评论 #1 — ColonelPhantom (2022-09-21T02:40:18Z)

Okay, I reinstalled ROCm using another package based on the .deb files and everything works again. Sorry for the noise!

---

### 评论 #2 — xuhuisheng (2022-09-21T03:03:09Z)

@ColonelPhantom 
Here is the solution for OpenCL with gfx803.
https://github.com/RadeonOpenCompute/ROCm/issues/1659#issuecomment-1219670138

---

### 评论 #3 — stefanharjes (2023-02-28T06:30:28Z)

I have the same issue on gentoo and would be happy if you remember the solution or at least the files you replaced? I emerge 5.3.3-r1 and 5.4.3. Here are the relevant info files:
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/10847177/clinfo.txt)
[lspci.txt](https://github.com/RadeonOpenCompute/ROCm/files/10847178/lspci.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/10847179/rocminfo.txt)
[rocm-smi.txt](https://github.com/RadeonOpenCompute/ROCm/files/10847180/rocm-smi.txt)


---

### 评论 #4 — Moading (2023-02-28T08:17:44Z)

Do you have

ROC_ENABLE_PRE_VEGA=1

in your environment?


Am 28.02.2023 um 07:30 schrieb Stefan Harjes:
>
> I have the same issue on gentoo and would be happy if you remember the
> solution or at least the files you replaced? I emerge 5.3.3-r1 and
> 5.4.3. Here are the relevant info files:
> clinfo.txt
> <https://github.com/RadeonOpenCompute/ROCm/files/10847177/clinfo.txt>
> lspci.txt
> <https://github.com/RadeonOpenCompute/ROCm/files/10847178/lspci.txt>
> rocminfo.txt
> <https://github.com/RadeonOpenCompute/ROCm/files/10847179/rocminfo.txt>
> rocm-smi.txt
> <https://github.com/RadeonOpenCompute/ROCm/files/10847180/rocm-smi.txt>
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1810#issuecomment-1447657093>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AIJI5JNKGYKW3YB6D2KZWVLWZWLRPANCNFSM6AAAAAAQRSKCUY>.
> You are receiving this because you are subscribed to this
> thread.Message ID:
> ***@***.***>
>
--
Dr.-Ing. Martin Rose
Ingenieurbüro Dr.-Ing. Martin Rose
Sommerhofenstr. 148
71067 Sindelfingen
Germany

Tel.: +49 (0)7031 4923040


---

### 评论 #5 — stefanharjes (2023-02-28T08:23:06Z)

yep, at least it is set as a env variable

---
