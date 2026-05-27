# Unable to install ROCm

> **Issue #1384**
> **状态**: closed
> **创建时间**: 2021-02-18T15:13:48Z
> **更新时间**: 2022-09-17T03:17:53Z
> **关闭时间**: 2021-02-19T11:24:35Z
> **作者**: HuBohy
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1384

## 描述

Hi, 

I hope it is not a copy of another issue, i've been searching for days for the solution.

After installing/uninstalling several times ROCm 4.0 on Ubuntu 20.04.2 TLS (kernel 5.4), I always come to the same issue:
<pre><font color="#4E9A06"><b>hugo@hugo-HP-ZBook-15u-G6</b></font>:<font color="#3465A4"><b>~</b></font>$ /opt/rocm/bin/rocminfo 
<font color="#CC0000">ROCk module is NOT loaded, possibly no GPU devices</font>
<font color="#CC0000">Unable to open /dev/kfd read-write: No such file or directory</font>
<font color="#D3D7CF">hugo is member of video group</font>
<font color="#CC0000">hsa api call failure at: /src/rocminfo/rocminfo.cc:1142</font>
<font color="#CC0000">Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.</font>
</pre>

I have a AMD Radeon Pro WX3200, which uses a Polaris 12 (which is in the list of supported GPU)

Does anyone has a solution for such issue?

---

## 评论 (13 条)

### 评论 #1 — xuhuisheng (2021-02-18T19:43:28Z)

please run dmesg|grep kfd , and check whether there is errors.

---

### 评论 #2 — HuBohy (2021-02-18T20:04:17Z)

When I run the command, it shows nothing, as kfd is not existing

---

### 评论 #3 — xuhuisheng (2021-02-18T20:36:34Z)

Normally amd kernel driver will register gpu. `dmesg | grep kfd`  , `dmesg | grep amdgpu` will show some infos.
Make sure we are using amdgpu, not radeon driver. `lsmod | grep amd`.

`lspci -tv` will show the topology of pci devices, try to find vga devices, on my computer it is a RX580.

```
 \-[0000:00]-+-00.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMI2
             +-01.0-[01]--
             +-03.0-[02]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
             |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere HDMI Audio [Radeon RX 470/480 / 570/580/590]

```

---

### 评论 #4 — ROCmSupport (2021-02-19T05:01:36Z)

Hi @HuBohy 
Thanks for reaching us.
We are not officially giving full support on Polaris12 and we have mentioned the same in our documentation too. But things might work in some cards.

 _**The following list of GPUs are enabled in the ROCm software, **though full support is not guaranteed**:**

    GFX8 GPUs
        "Polaris 11" chips, such as on the AMD Radeon RX 570 and Radeon Pro WX 4100
        "Polaris 12" chips, such as on the AMD Radeon RX 550 and Radeon RX 540
    GFX7 GPUs
        "Hawaii" chips, such as the AMD Radeon R9 390X and FirePro W9100_


---

### 评论 #5 — ROCmSupport (2021-02-19T05:19:11Z)

Let me still try to help you if I can.
Can you please share a few details of your machine: kernel, groups, dmesg | grep kfd , dmesg | grep amdgpu, lspci -nn | grep "AMD/ATI"
Thank you.

---

### 评论 #6 — HuBohy (2021-02-19T10:50:46Z)

Thank you both for the quick response.

@xuhuisheng: here's the output of the commands
<pre>(base) <font color="#4E9A06"><b>hugo@hugo-HP-ZBook-15u-G6</b></font>:<font color="#3465A4"><b>~</b></font>$ dmesg | grep kfd
[    3.867206] <font color="#CC0000"><b>kfd</b></font> <font color="#CC0000"><b>kfd</b></font>: skipped device 1002:6981, PCI rejects atomics
(base) <font color="#4E9A06"><b>hugo@hugo-HP-ZBook-15u-G6</b></font>:<font color="#3465A4"><b>~</b></font>$ dmesg | grep amdgpu
[    3.805226] [drm] <font color="#CC0000"><b>amdgpu</b></font> kernel modesetting enabled.
[    3.844783] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: remove_conflicting_pci_framebuffers: bar 0: 0xc0000000 -&gt; 0xcfffffff
[    3.844786] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: remove_conflicting_pci_framebuffers: bar 2: 0xd0000000 -&gt; 0xd01fffff
[    3.844787] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xec100000 -&gt; 0xec13ffff
[    3.844831] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: enabling device (0006 -&gt; 0007)
[    3.991111] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: BAR 2: releasing [mem 0xd0000000-0xd01fffff 64bit pref]
[    3.991115] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: BAR 0: releasing [mem 0xc0000000-0xcfffffff 64bit pref]
[    3.991131] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: BAR 0: assigned [mem 0xc0000000-0xcfffffff 64bit pref]
[    3.991148] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: BAR 2: assigned [mem 0xd0000000-0xd01fffff 64bit pref]
[    3.991182] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    3.991184] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    3.994882] [drm] <font color="#CC0000"><b>amdgpu</b></font>: 4096M of VRAM memory ready
[    3.994888] [drm] <font color="#CC0000"><b>amdgpu</b></font>: 4096M of GTT memory ready.
[    4.027333] <font color="#CC0000"><b>amdgpu</b></font>: [powerplay] hwmgr_sw_init smu backed is polaris10_smu
[    4.281377] [drm] Initialized <font color="#CC0000"><b>amdgpu</b></font> 3.35.0 20150101 for 0000:3a:00.0 on minor 1
[   14.309691] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: GPU pci config reset
[   27.311795] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: GPU pci config reset
[  123.804029] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: GPU pci config reset
[  187.356170] <font color="#CC0000"><b>amdgpu</b></font> 0000:3a:00.0: GPU pci config reset
(base) <font color="#4E9A06"><b>hugo@hugo-HP-ZBook-15u-G6</b></font>:<font color="#3465A4"><b>~</b></font>$ lsmod | grep amd
<font color="#CC0000"><b>amd</b></font>gpu               4579328  1
<font color="#CC0000"><b>amd</b></font>_iommu_v2           20480  1 <font color="#CC0000"><b>amd</b></font>gpu
gpu_sched              32768  1 <font color="#CC0000"><b>amd</b></font>gpu
ttm                   106496  1 <font color="#CC0000"><b>amd</b></font>gpu
drm_kms_helper        184320  2 <font color="#CC0000"><b>amd</b></font>gpu,i915
i2c_algo_bit           16384  2 <font color="#CC0000"><b>amd</b></font>gpu,i915
drm                   491520  11 gpu_sched,drm_kms_helper,<font color="#CC0000"><b>amd</b></font>gpu,i915,ttm
</pre>

<pre>(base) <font color="#4E9A06"><b>hugo@hugo-HP-ZBook-15u-G6</b></font>:<font color="#3465A4"><b>~</b></font>$ lspci -tv
-[0000:00]-+-00.0  Intel Corporation Coffee Lake HOST and DRAM Controller
           +-02.0  Intel Corporation UHD Graphics 620 (Whiskey Lake)
           +-04.0  Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem
           +-12.0  Intel Corporation Cannon Point-LP Thermal Controller
           +-13.0  Intel Corporation Cannon Point-LP Integrated Sensor Hub
           +-14.0  Intel Corporation Cannon Point-LP USB 3.1 xHCI Controller
           +-14.2  Intel Corporation Cannon Point-LP Shared SRAM
           +-14.3  Intel Corporation Cannon Point-LP CNVi [Wireless-AC]
           +-15.0  Intel Corporation Cannon Point-LP Serial IO I2C Controller #0
           +-15.1  Intel Corporation Cannon Point-LP Serial IO I2C Controller #1
           +-16.0  Intel Corporation Cannon Point-LP MEI Controller #1
           +-1c.0-[01-39]----00.0-[02-39]--+-00.0-[03]----00.0  Intel Corporation JHL7540 Thunderbolt 3 NHI [Titan Ridge 2C 2018]
           |                               +-01.0-[04-38]--
           |                               \-02.0-[39]----00.0  Intel Corporation JHL7540 Thunderbolt 3 USB Controller [Titan Ridge 2C 2018]
           +-1d.0-[3a]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Lexa XT [Radeon PRO WX 3200]
           +-1d.4-[3b]----00.0  Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
           +-1f.0  Intel Corporation Cannon Point-LP LPC Controller
           +-1f.3  Intel Corporation Cannon Point-LP High Definition Audio Controller
           +-1f.4  Intel Corporation Cannon Point-LP SMBus Controller
           +-1f.5  Intel Corporation Cannon Point-LP SPI Controller
           \-1f.6  Intel Corporation Ethernet Connection (6) I219-V
</pre>

@ROCmSupport: added to the previous output, here's the groups left after uninstalling one last time ROCm and not knowing what to do
<pre>(base) <font color="#4E9A06"><b>hugo@hugo-HP-ZBook-15u-G6</b></font>:<font color="#3465A4"><b>~</b></font>$ groups
hugo adm cdrom sudo dip plugdev lpadmin sambashare
</pre>

<pre>(base) <font color="#4E9A06"><b>hugo@hugo-HP-ZBook-15u-G6</b></font>:<font color="#3465A4"><b>~</b></font>$ lspci -nn | grep &quot;AMD/ATI&quot;
3a:00.0 Display controller [0380]: Advanced Micro Devices, Inc. [<font color="#CC0000"><b>AMD/ATI</b></font>] Lexa XT [Radeon PRO WX 3200] [1002:6981] (rev 01)
</pre>

---

### 评论 #7 — ROCmSupport (2021-02-19T11:01:04Z)

Here the problem is:
_(base) hugo@hugo-HP-ZBook-15u-G6:~$ dmesg | grep kfd
[    3.867206] kfd kfd: skipped device 1002:6981, PCI rejects atomics_

(base) hugo@hugo-HP-ZBook-15u-G6:~$ lspci -nn | grep "AMD/ATI"
3a:00.0 Display controller [0380]: Advanced Micro Devices, Inc. [AMD/ATI] **Lexa XT**

Your device is rejected due to unsupported PCI/CPU configuration or the problem with the device itself. 
Recommend to use a supported GPU and CPU as mentioned below.
Please check for supported CPUs: https://github.com/RadeonOpenCompute/ROCm#supported-cpus

---

### 评论 #8 — HuBohy (2021-02-19T11:12:57Z)

But doesn't this line show that it is an Intel Xeon E3 v5?
_+-04.0  Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem_

Plus my CPU is said to be <pre><font color="#CC0000"><b>model name</b></font>	: Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz
</pre>

---

### 评论 #9 — ROCmSupport (2021-02-19T11:23:59Z)

Got it. So looks like you have a supported CPU then, the problem is with the GPU then.
We are not supporting Lexa XT.

---

### 评论 #10 — HuBohy (2021-02-19T11:24:35Z)

Ok, Thank you !

---

### 评论 #11 — algo99 (2021-10-15T15:13:49Z)

> I have a AMD Radeon Pro WX3200

I can confirm at the mean time the same card seems to work with OpenCL (ROCm 4.3.1) after I have installed it into another PCIe slot. My system Dell Precision 3620 has two PCIe x16 slots and it looks they have different specification. So initially I installed the card into the wrong slot with the same result as the TC above. The other slot is _PCI Express® x16 Gen 3_ that in addition means atomic operations are supported. 

<details><summary>rocminfo output</summary>

```sh

$ LD_LIBRARY_PATH=/opt/rocm-4.3.1/lib rocminfo 
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
  Name:                    Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz
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
  Max Clock Freq. (MHz):   3400                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            4                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    16264852(0xf82e94) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16264852(0xf82e94) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16264852(0xf82e94) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Lexa XT [Radeon PRO WX 3200]       
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
  Chip ID:                 27009(0x6981)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1295                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            10                                 
  SIMDs per CU:            4                                  
  Shader Engines:          2                                  
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
</details>


---

### 评论 #12 — ddkn (2022-02-27T19:27:06Z)

Sorry to ask a question here on a closed topic, but does that mean one could use a WX3200 with ROCm with PyTorch? I am looking to get some mid range hardware to work with it.

---

### 评论 #13 — pszemraj (2022-09-17T03:17:53Z)


> Sorry to ask a question here on a closed topic, but does that mean one could use a WX3200 with ROCm with PyTorch? I am looking to get some mid range hardware to work with it.

hey @ddkn, any chance you figured this out? was hoping to leverage the GPU on this old laptop I have :) 

---
