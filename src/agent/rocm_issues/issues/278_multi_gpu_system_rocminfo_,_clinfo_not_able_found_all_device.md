# multi gpu system rocminfo , clinfo not able found all device.

> **Issue #278**
> **状态**: closed
> **创建时间**: 2017-12-21T16:14:11Z
> **更新时间**: 2018-06-03T15:25:25Z
> **关闭时间**: 2018-06-03T15:25:25Z
> **作者**: JiniusDnn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/278

## 描述

I have a multi gpu system,   either rocm1.6 or 1.7 was not able to detect gpu correctly.

here is my GPU list on bus.
```
lspci | grep VGA
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev cb)
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev cb)
```
but in rocminfo , only saw 2 gpu .

```

=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Pentium(R) CPU G4400 @ 3.30GHz
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):2800                               
  BDFID:                   0                                  
  Compute Unit:            2                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    3964544KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    3964544KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 29440                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1000                               
  BDFID:                   256                                
  Compute Unit:            56                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  16778240                           
    Dim[2]:                  0                                  
  Grid Max Size:           4294967295                         
  Waves Per CU:            40                                 
  Max Work-item Per CU:    2560                               
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                         
    Dim[1]:                  4294967295                         
    Dim[2]:                  4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    4194304KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64KB                               
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    AMD:AMDGPU:8:0:3                   
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Dimension: 
        Dim[0]:                  67109888                           
        Dim[1]:                  1024                               
        Dim[2]:                  16777217                           
      Workgroup Max Size:      1024                               
      Grid Max Dimension:      
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      Grid Max Size:           4294967295                         
      FBarrier Max Size:       32                                 
*******                  
Agent 3                  
*******                  
  Name:                    gfx803                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 26591                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1226                               
  BDFID:                   512                                
  Compute Unit:            32                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  33555456                           
    Dim[2]:                  0                                  
  Grid Max Size:           4294967295                         
  Waves Per CU:            40                                 
  Max Work-item Per CU:    2560                               
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                         
    Dim[1]:                  4294967295                         
    Dim[2]:                  4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    4194304KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64KB                               
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    AMD:AMDGPU:8:0:3                   
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Dimension: 
        Dim[0]:                  67109888                           
        Dim[1]:                  1024                               
        Dim[2]:                  16777217                           
      Workgroup Max Size:      1024                               
      Grid Max Dimension:      
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      Grid Max Size:           4294967295                         
      FBarrier Max Size:       32                                 
*** Done ***       
```

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-12-22T22:28:05Z)

Those are RX470 GPU.   What your asking for us is show GPU string for RX470? 

---

### 评论 #2 — gstoner (2017-12-23T16:30:32Z)

Sorry, they are RX580 GPU, note I did look into the source code for the driver they are supported in the base driver.   Are these on PCIe Switch  that is  PCIe Gen2 based  or not PCIe Gen3  link. 

drivers/gpu/drm/amd/amdkfd/kfd_device.c
311 | { 0x67DF, &polaris10_device_info },	/* Polaris10 */

drivers/gpu/drm/amd/amdgpu/amdgpu_cgs.c 

if (type == CGS_UCODE_ID_SMU) {
--
755 | if ((adev->pdev->device == 0x67df) &&
756 | ((adev->pdev->revision == 0xe0) \|\|


drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c
{0x1002, 0x67DF, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_POLARIS10},

---

### 评论 #3 — gstoner (2017-12-23T19:02:15Z)

Ok I found the problem for HCC and HIP,   in rocminfo they did not enumerate 67df 

Replace rocm_agent_enumerator file with this one   I fixed this file    https://github.com/RadeonOpenCompute/rocminfo/blob/master/rocm_agent_enumerator

---

### 评论 #4 — smithakihide (2017-12-25T04:46:44Z)

I replaced it, but it still did not work.

---

### 评论 #5 — th0ma7 (2018-01-21T14:09:58Z)

Having a similar issue as well using RX 560 adaptors:
```
$ /opt/rocm/bin/rocm-smi 
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  3   48.0c   33.218W  1000Mhz  1947Mhz  22.75%   auto      0%       
  1   63.0c   31.204W  1000Mhz  1950Mhz  36.86%   auto      0%       
  2   54.0c   33.150W  1000Mhz  1948Mhz  23.92%   auto      0%       
  0   42.0c   12.42W   214Mhz   1951Mhz  33.73%   auto      0%       
================================================================================
====================           End of ROCm SMI Log          ====================
```

And lspci output:
```
$ lspci | grep -i vga
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67ef (rev e5)
09:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67ef (rev e5)
0a:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67ff (rev cf)
0b:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67ff (rev cf)
```

clinfo only sees 3 devices:
```
$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP.internal (2545.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 3
  Device Name                                     gfx803
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  2545.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
...
```

Same with rocminfo.  It sees 4 agents but the first one is actually the AMD processor:
```
==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 5 1600X Six-Core Processor
  Vendor Name:             CPU                                
..
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Vendor Name:             AMD      
...                          
*******                  
Agent 3                  
*******                  
  Name:                    gfx803                             
  Vendor Name:             AMD              
...                  
*******                  
Agent 4                  
*******                  
  Name:                    gfx803                             
  Vendor Name:             AMD              
```                  

So I reverted to a Legacy OpenCL using latest amdgpu-pro drivers.  Getting lower performance than with ROCm but at least all my adaptors are detected properly.

Forgot to mention, using ubuntu 16.04 with hwe-edge kernel 4.13 and latest ROCm from PPA.

---
