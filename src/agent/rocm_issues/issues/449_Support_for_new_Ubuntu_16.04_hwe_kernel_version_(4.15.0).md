# Support for new Ubuntu 16.04 hwe kernel version (4.15.0)

> **Issue #449**
> **状态**: closed
> **创建时间**: 2018-07-02T15:29:20Z
> **更新时间**: 2018-07-20T16:14:28Z
> **关闭时间**: 2018-07-06T19:44:57Z
> **作者**: krrk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/449

## 负责人

- jedwards-AMD

## 描述

Ubuntu 16.04 was updated today to the 4.15 kernel from 18.04, but there were no updates from rocm-dkms so naturally it failed to build for the new kernel version.

> Processing triggers for linux-image-4.15.0-24-generic (4.15.0-24.26~16.04.1) ...
> /etc/kernel/postinst.d/dkms:
> ERROR (dkms apport): kernel package linux-headers-4.15.0-24-generic is not supported
> Error! Bad return status for module build on kernel: 4.15.0-24-generic (x86_64)
> Consult /var/lib/dkms/amdgpu/1.8-151/build/make.log for more information.

[make.log](https://github.com/RadeonOpenCompute/ROCm/files/2155780/make.log)

I realize that this new kernel release is ahead of the proposed schedule (says Aug. 2018) as can be seen [here](https://wiki.ubuntu.com/Kernel/LTSEnablementStack#Kernel.2FSupport.A16.04.x_Ubuntu_Kernel_Support), but will we seen an update to ROCm soon?

---

## 评论 (17 条)

### 评论 #1 — preda (2018-07-03T01:58:15Z)

While you're at it, please also consider verifying that ROCm works with kernel 4.17 (released) and 4.18 (RC). http://kernel.ubuntu.com/~kernel-ppa/mainline/


---

### 评论 #2 — sunway513 (2018-07-03T18:29:08Z)

@krrk , here's the steps you can try to work it around until we have official recommendations:
1. install 4.13 kernel:
`sudo apt update && sudo apt install -y linux-headers-4.13.0-32-generic linux-image-4.13.0-32-generic linux-image-extra-4.13.0-32-generic linux-signed-image-4.13.0-32-generic
`
2. remove 4.15, then reboot:
`sudo apt autoremove -y linux-image-generic-hwe-16.04 linux-image-4.15.0-24-generic linux-headers-4.15 linux-modules-4.15 && sudo reboot
`
3. remove rock-dkms:
`sudo apt autoremove -y rock-dkms
`
4. install rocm-dkms, reboot:
`sudo apt install rocm-dkms && sudo reboot`

---

### 评论 #3 — brian-maher (2018-07-03T22:59:25Z)

@sunway513 for some of us, the 4.13 kernel is unworkable. The latest release seems to proclaim support for many more egpu configurations, but the vast majority of thunderbolt 3 pci-e enclosures are unusable in 4.13.

Tbh, I'm starting to regret my decisions to bet on amd cards. 

---

### 评论 #4 — krrk (2018-07-03T23:01:57Z)

Thanks @sunway513, I'm sure that your solution would work, but you should definitely select the latest 4.13 kernel version 4.13.0-45 for all the latest security updates. I currently have just set `GRUB_DEFAULT` in `/etc/default/grub` to select a 4.13 kernel. This works for now, but I believe the 4.13 security updates end this month with the end of support for Ubuntu 17.10.

---

### 评论 #5 — 3D-360 (2018-07-04T00:21:37Z)

>Tbh, I'm starting to regret my decisions to bet on amd cards:   brian-maher

I know the feeling, but I'm hanging in there because I see the potential (especially with the APUs).  It sounds like Ubuntu 18.04 and ROCm 1.9 is what we are waiting for.  Imagine how nice it will be once ROCm & 18.04 work out of the box!  I have put my ROCm work on hold while I work on other parts of my project, I hope that you can do the same.

---

### 评论 #6 — sunway513 (2018-07-04T00:41:17Z)

@krrk we are going to officially support Ubuntu16.04 with 4.15 kernel as well as Ubuntu18.04 in the ROCm1.9 release. 
And you can surely stick on different 4.13.x minor kernel releases, what I've suggested above is the one that known-to-work on my personal setup. 

---

### 评论 #7 — sunway513 (2018-07-06T17:56:00Z)

@odellus please try to verify if you have added the ROCm apt repository, steps here:
https://github.com/RadeonOpenCompute/ROCm#add-the-rocm-apt-repository

---

### 评论 #8 — odellus (2018-07-06T18:28:53Z)

Oh yeah u know that I've got rocm in my sources list. I'm *re*-installing

---

### 评论 #9 — odellus (2018-07-06T18:29:30Z)

The Ubuntu kernel update to 4.15 on 16.04 broke my ROCm

---

### 评论 #10 — odellus (2018-07-06T18:45:28Z)

This is what I get every, single, time.
```
rocminfo: error while loading shared libraries: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory
```
I've reinstalled rocm-dkms at least a dozen times at this point, trying to figure out what package includes libhsa-runtime64.so.1, trying to make sure it actually sees that package and can load the library above when I'm installing rocminfo.

---

### 评论 #11 — jedwards-AMD (2018-07-06T18:59:00Z)

Can you look in the /opt/rocm/hsa/lib directory and see if you have that library? Also, can you check that that the runtime is in your ldconfig path:
`ldconfig -p | grep rocm'
.
You should see libhsa-runtime64.so.1 in the list.

---

### 评论 #12 — odellus (2018-07-06T19:02:40Z)

Okay so whatever I did after a baker's dozen tries was the charm in getting rid of the libhsa-runtime issue. I didn't have the library installed at first, then even after I did it still wouldn't register. And by not installed I mean /opt/rocm/hsa was *not there*.
I think I installed it __before__ I installed rocm-dkms. So many times through, hard to be sure at the point. Guess I need a lab notebook.

Now I'm seeing 
```
rocminfo: error while loading shared libraries: libhsakmt.so.1: cannot open shared object file: No such file or directory
```
So I'm purging the previously installed hsakmt* packages now. The instructions at https://github.com/RadeonOpenCompute/ROCm#removing-pre-release-packages are out of date. 
`sudo apt purge libhsakmt` doesn't work anymore. Names changed.

I'm reinstalling right now. Will get back with results of `ldconfig -p | grep rocm` after this try.

---

### 评论 #13 — odellus (2018-07-06T19:24:26Z)

OMG Now when I run `rocminfo` I get this gobbledygook!! :angry:
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
  Name:                    AMD Ryzen 3 1300X Quad-Core Processor
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
  Max Clock Frequency (MHz):3500                               
  BDFID:                   0                                  
  Compute Unit:            4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    8176320KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8176320KB                          
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
  Chip ID:                 26591                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1340                               
  BDFID:                   2304                               
  Compute Unit:            36                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  150995968                          
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
```
lmao :laughing: 
Yeah really need to change the README.md for uninstalling ROCm. Purging hsakmt-roct* fixed my issue.

---

### 评论 #14 — jedwards-AMD (2018-07-06T19:44:52Z)

I have updated the instructions to remove the hsakmt-roct package. It looks like you got your driver up. I will close the ticket.

---

### 评论 #15 — sunway513 (2018-07-19T19:17:00Z)

With ROCm1.8.2 released, the Ubuntu 4.15 kernel is now supported by ROCm. 

---

### 评论 #16 — odellus (2018-07-19T19:32:11Z)

Awesome!

---

### 评论 #17 — krrk (2018-07-20T16:14:27Z)

Thanks!

---
