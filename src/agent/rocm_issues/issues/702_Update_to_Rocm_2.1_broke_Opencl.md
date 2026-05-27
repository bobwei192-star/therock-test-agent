# Update to Rocm 2.1 broke Opencl

> **Issue #702**
> **状态**: closed
> **创建时间**: 2019-02-08T23:24:14Z
> **更新时间**: 2021-01-07T05:26:14Z
> **关闭时间**: 2021-01-07T05:26:14Z
> **作者**: delolat
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/702

## 描述

Upon updating to ROCm 2.1 my system on reboot I received the error "UVD not responding trying to reset the VCPU". I restarted and booted from a lower kernel version and was able to boot, however, I am having issues starting OpenCL where whatever application I launch using OpenCL hangs. Using blender switching to Cycles, or going to preferences clicking the system tab hangs blender. Going to the konsole and doing CLinfo also hangs. I uninstalled and reinstalled and am continuing to have the same issue. 

Also does ROCm support kernel 4.20? 

Kernel version: 4.18.20
OS: Kubuntu 18.10
GPU1: AMD Fury X
GPU2: AMD Firepro w8100  

---

## 评论 (6 条)

### 评论 #1 — jlgreathouse (2019-02-08T23:30:44Z)

As noted in #691 and #640, Hawaii GPUs (such as your FirePro W8100) are currently broken on ROCm 2.0. We are working to fix this, but these fixes did not make it in to ROCm 2.1. If you want to stick with ROCm 2.1, I would recommend removing your Hawaii GPU for now. Alternately, you can roll back to a previous version (e.g. using the roc-1.9.2 branch of our [Experimental ROC installation scripts](https://github.com/RadeonOpenCompute/Experimental_ROC)).

Yes, ROCm user-land software [does support kernel 4.20](https://github.com/RadeonOpenCompute/ROCm#rocm-support-in-upstream-linux-kernels). See [these directions](https://github.com/RadeonOpenCompute/ROCm#using-debian-based-rocm-with-upstream-kernel-drivers) -- you should not install the `rock-dkms` module, but you can install all other software (such as `rocm-dev`). Alternately, you can use the Ubuntu 18.10 installation scripts in the above-linked Experimental ROC repo.



---

### 评论 #2 — delolat (2019-02-18T23:47:10Z)

Installed 1.9.2 using the deb_install, and I'm still experiencing the same issue. Clinfo hangs and blender clicking on the system tab hangs blender. 2.0 for me worked fine also, it was only 2.1 that messed up my system. 

rocminfo:
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
  Name:                    Intel(R) Core(TM) i7-5820K CPU @ 3.30GHz
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
  Max Clock Frequency (MHz):2900                               
  BDFID:                   0                                  
  Compute Unit:            12                                 
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32848712KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32848712KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx701                             
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
  Chip ID:                 26529                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):824                                
  BDFID:                   512                                
  Compute Unit:            40                                 
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
      Size:                    8388608KB                          
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
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
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
  Chip ID:                 29440                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1050                               
  BDFID:                   256                                
  Compute Unit:            64                                 
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
      Name:                    amdgcn-amd-amdhsa--gfx803          
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


---

### 评论 #3 — delolat (2019-02-23T22:23:20Z)

There's no uninstaller script for the experimental ROCm install script?

---

### 评论 #4 — jlgreathouse (2019-03-14T15:44:58Z)

Hi @delolat 

No, there is no uninstaller script for the experimental ROC project. Uninstalling is a lot more dangerous than installing -- deleting files, removing packages, and things like that have a lot higher chance of breaking something if done incorrectly. I am not comfortable writing a script that has a chance of breaking a user's system, because I do not have the bandwidth to help every user fix their system if something goes wrong.

In any case, you're running a number of different things that are going to cause problems:
 - Kernel 4.18 is not supported with our `rock-dkms` driver. You're using an upstream driver. I believe that Hawaii and Fiji both work with the upstream driver, but I have not verified this.
    - ROCm 2.0's `rock-dkms` definitely broke Hawaii. I haven't been able to circle back to fix this, IIRC.
    - However, I can't guarantee that 4.18.20 did not break something.
 - I know that the ROCm OpenCL runtime broke Hawaii when we released ROCm 2.0. I believe we fixed this in ROCm 2.1, but again I have not had the bandwidth to verify this. In any case, Hawaii is only experimentally enabled, and we do not guarantee to support it.
 - I believe Blender is known to be broken, and has been for a long time. There are multiple bugs in flight internally trying to fix this.

Honestly, if it is critical that ROCm work on your system, I recommend removing your Hawaii GPU for now. We are trying to make sure Hawaii continues to work, but it is not our highest priority at this time. Hawaii in ROCm has always been, and will continue to be, best effort but not guaranteed.

---

### 评论 #5 — delolat (2019-03-19T17:41:11Z)

What Kernel is recommended that I use? I am reading that kernel 4.19 and 4.20 have regressions on the Hawaii GPU's. My plan originally was always the Fiji was going to be a temporary card(since it's only 4gb), but after the outrageous GPU pricing I never acquired a vega64, which I always intended to purchase to use alongside my w8100, since they're both 8gb. If i get my Hawaii working using an old Kernel I don't want to be surprised, if I were to purchase a vega64 and it doesn't work with that kernel. 

I also want to note the reasons I was geared toward using ROCm were for flexibility of using an OS outside of the LTS, and simply because the amdgpu-pro drivers broke on every kernel upgrade released by Ubuntu. 

---

### 评论 #6 — ROCmSupport (2021-01-07T05:26:14Z)

Hi All,
Hawaii is no more officially ROCm supported device. Please check for more details:
[https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)

---
