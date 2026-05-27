# Installing ROCM on Ubuntu - hsa api call failure

> **Issue #1064**
> **状态**: closed
> **创建时间**: 2020-03-28T16:18:24Z
> **更新时间**: 2021-04-05T10:12:00Z
> **关闭时间**: 2021-04-05T10:12:00Z
> **作者**: maxi831
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1064

## 描述

So I am trying to install ROCm on Ubuntu 18.04.3 which is supposedly supported. I have tried reinstalling ubuntu twice and spent quite a few hours trying to get it working. I sticked completely to the official instructions on this github page. One thing that might be relevant is that I ticked `Install third-party software for graphics and Wi-Fi hardware and additional media formats`. When I run `rocminfo` I get the following hsa api call failure:

<pre><code>bauermax@backbone:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
bauermax is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-3.1/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.</code></pre>

Now I could find this issue online and a lot of people seem to have it also, but I could not find any solution.

When I run `clinfo` everything seems to be working exept it says `ERROR: clGetDeviceIDs(-1)` at the end:

<pre><code>bauermax@backbone:~$ /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3084.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
</code></pre>

My current kernel is `5.3.0-42-generic` and in the instruction they say 5.3 is supported, so I think the kernel is right:
<pre><code>bauermax@backbone:~$ uname -r
5.3.0-42-generic
</code></pre>

I downloaded and installed `Ubuntu 18.04.3` however having followed the official instructions my version is now `Ubuntu 18.04.4 LTS` . I suppose that is because of the `sudo apt update` and `sudo apt dist-upgrade` command which however is in the official instructions. In the supported operating systems section it says that only `18.04.3` is supported, so I am not sure if this is a problem:

<pre><code>bauermax@backbone:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.4 LTS
Release:        18.04
Codename:       bionic
</code></pre>

`lshw` shows that my GPU is using the `amdgpu` driver which I think is the open source one:
<pre><code>bauermax@backbone:~$ sudo lshw -c video
[sudo] password for bauermax: 
  *-display                 
       description: VGA compatible controller
       product: Ellesmere [Radeon RX 470/480/570/570X/580/580X]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:01:00.0
       version: e7
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:32 memory:e0000000-efffffff memory:f0000000-f01fffff ioport:e000(size=256) memory:f7e00000-f7e3ffff memory:c0000-dffff
</code></pre>

My specs:
Motherboard: Gigabyte Z77-DS3H
CPU: i7 3770k
GPU: Sapphire RX580 Pulse 4GB

<pre><code>bauermax@backbone:~$ sudo lshw -short
H/W path       Device      Class          Description
=====================================================
                           system         To be filled by O.E.M. (To be filled by O.E.M.)
/0                         bus            Z77-DS3H
/0/0                       memory         64KiB BIOS
/0/4                       memory         128KiB L1 cache
/0/5                       memory         1MiB L2 cache
/0/6                       memory         8MiB L3 cache
/0/7                       memory         32GiB System Memory
/0/7/0                     memory         8GiB DIMM DDR3 Synchronous 1600 MHz (0.6 ns)
/0/7/1                     memory         8GiB DIMM DDR3 Synchronous 1600 MHz (0.6 ns)
/0/7/2                     memory         8GiB DIMM DDR3 Synchronous 1600 MHz (0.6 ns)
/0/7/3                     memory         8GiB DIMM DDR3 Synchronous 1600 MHz (0.6 ns)
/0/43                      processor      Intel(R) Core(TM) i7-3770K CPU @ 3.50GHz
/0/100                     bridge         Xeon E3-1200 v2/3rd Gen Core processor DRAM Controller
/0/100/1                   bridge         Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port
/0/100/1/0                 display        Ellesmere [Radeon RX 470/480/570/570X/580/580X]
/0/100/1/0.1               multimedia     Ellesmere [Radeon RX 580]
/0/100/14                  bus            7 Series/C210 Series Chipset Family USB xHCI Host Controller
/0/100/14/0    usb3        bus            xHCI Host Controller
/0/100/14/0/1              input          USB Receiver
/0/100/14/0/3              communication  Broadcom Bluetooth 3.0 Device
/0/100/14/1    usb4        bus            xHCI Host Controller
/0/100/16                  communication  7 Series/C216 Chipset Family MEI Controller #1
/0/100/1a                  bus            7 Series/C216 Chipset Family USB Enhanced Host Controller #2
/0/100/1a/1    usb1        bus            EHCI Host Controller
/0/100/1a/1/1              bus            Integrated Rate Matching Hub
/0/100/1b                  multimedia     7 Series/C216 Chipset Family High Definition Audio Controller
/0/100/1c                  bridge         7 Series/C216 Chipset Family PCI Express Root Port 1
/0/100/1c.2                bridge         7 Series/C210 Series Chipset Family PCI Express Root Port 3
/0/100/1c.2/0  enp3s0      network        AR8161 Gigabit Ethernet
/0/100/1c.3                bridge         82801 PCI Bridge
/0/100/1c.3/0              bridge         82801 PCI Bridge
/0/100/1c.4                bridge         7 Series/C210 Series Chipset Family PCI Express Root Port 5
/0/100/1c.4/0  wlp6s0      network        BCM4360 802.11ac Wireless Network Adapter
/0/100/1d                  bus            7 Series/C216 Chipset Family USB Enhanced Host Controller #1
/0/100/1d/1    usb2        bus            EHCI Host Controller
/0/100/1d/1/1              bus            Integrated Rate Matching Hub
/0/100/1f                  bridge         Z77 Express Chipset LPC Controller
/0/100/1f.2                storage        7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode]
/0/100/1f.3                bus            7 Series/C216 Chipset Family SMBus Controller
/0/1           scsi0       storage        
/0/1/0.0.0     /dev/sda    disk           256GB SAMSUNG SSD 830
/0/1/0.0.0/1               volume         511MiB Windows FAT volume
/0/1/0.0.0/2   /dev/sda2   volume         237GiB EXT4 volume
/0/2           scsi1       storage        
/0/2/0.0.0     /dev/sdb    disk           256GB Samsung SSD 840
/0/2/0.0.0/1   /dev/sdb1   volume         528MiB Windows NTFS volume
/0/2/0.0.0/2   /dev/sdb2   volume         98MiB Windows FAT volume
/0/2/0.0.0/3   /dev/sdb3   volume         15MiB reserved partition
/0/2/0.0.0/4   /dev/sdb4   volume         237GiB Windows NTFS volume
/0/3           scsi4       storage        
/0/3/0.0.0     /dev/cdrom  disk           DVDRAM GH24NS95
/1                         power          To Be Filled By O.E.M.
</code></pre>

Hope this is enough information, if you need any more just write. I would be grateful for any kind of help

---

## 评论 (4 条)

### 评论 #1 — KristijanZic (2020-04-02T21:46:51Z)

I can confirm that the issue is present on v3.3

```
$ /opt/rocm/bin/rocminfo
ROCk module is loaded
aresminos is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```


Now with sudo:

```
$ sudo /opt/rocm/bin/rocminfo
ROCk module is loaded
aresminos is member of video group
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
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 1900X 8-Core Processor
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
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16312780(0xf8e9cc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16312780(0xf8e9cc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 1900X 8-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    0(0x0) KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    0(0x0) KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 3                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XL/XT [Radeon RX Vega 56/64]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26751(0x687f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1750                               
  BDFID:                   17408                              
  Internal Node ID:        2                                  
  Compute Unit:            64                                 
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
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
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

### 评论 #2 — hrittich (2020-04-04T21:43:14Z)

I have the same issue. I have installed a fresh version ob Ubuntu 18.04 and followed [these](https://rocm-documentation.readthedocs.io/en/latest/Installation_Guide/Installation-Guide.html#ubuntu) instructions. I am running the `5.3.0-45-generic` kernel, DRM 3.36.0, on an Radeon RX 580.

    $ /opt/rocm/bin/rocminfo
    ROCk module is loaded
    hannah is member of video group
    hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
    Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.



---

### 评论 #3 — faust3 (2020-10-03T16:52:43Z)

I got a similar message with Ubuntu 20.04 and Ryzen2400g.
When I set the option amdgpu cwsr_enable=0, I was at least able to execute rocminfo.


---

### 评论 #4 — ROCmSupport (2021-04-05T10:12:00Z)

Thanks @maxi831 for reaching out.
This issue is fixed and no more observed with the latest ROCm 4.1, request you to try the same.
Feel free to open a new issue, if any, for quick resolution.
Thank you.

---
