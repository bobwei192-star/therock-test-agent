# RX550/i7-8850u PCI reject atomics

> **Issue #827**
> **状态**: closed
> **创建时间**: 2019-06-24T01:36:48Z
> **更新时间**: 2023-04-14T17:29:31Z
> **关闭时间**: 2019-07-04T18:28:28Z
> **作者**: algoton
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/827

## 描述

I have checked the ROCm supported hardware before purchasing the Samsung notebook NP940X5N. But still rocm driver is not working after apt-get install the rocm binary. Detailed info below. Can anyone guide what to debug next?

OS: Ubuntu 19.04

Intel® Core™ i7-8550U CPU @ 1.80GHz × 8 

lspci | grep Display
01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon RX 550/550X] (rev c3)

dmesg | grep kfd
[    4.324747] kfd kfd: skipped device 1002:699f, PCI rejects atomics

dkms status
amdgpu, 2.5-27, 5.0.0-17-generic, x86_64: installed


---

## 评论 (10 条)

### 评论 #1 — JMadgwick (2019-06-24T20:51:27Z)

This looks to be identical to #806. Your PCI bus ID looks the same and the kfd message is identical.
The output of `lspci` and `lspci -t` should show how the GPU is connected. Look for _AtomicOpsCap_ (using -vvv) you should see a line reporting the atomics supported unless none are supported (likely the case).

In #806 it appeared that the GPU was connected to a so called "Chipset PCI Express Root Port" which appeared to be different to the _direct to CPU_ Root Port. It wasn't clear in that issue why this was. I speculated that it might be related to how the laptop's motherboard had been designed. 

Unfortunately, it doesn't look like these laptops can actually use ROCm. In short this is because the chipset link used appears to reject atomics (although according to Intel specs it supports them, more detail in #806).

You could try looking in the BIOS and examining PCIe related options. Without any feedback from the manufacturer it's impossible to determine why support for atomics is not being reported (appears to be a design oversight).

As this is not a fault with ROCm I don't think there is much that can be done by the developers to correct it, although they might want to inform somebody at AMD so they can pass the information along to manufacturers.

---

### 评论 #2 — algoton (2019-06-25T02:46:35Z)

Right. lspci -vvv | grep Atomic does not return anything.
I can return this laptop. Do you have the recommended laptops or desktops on which ROCm works?


---

### 评论 #3 — JMadgwick (2019-06-25T07:58:43Z)

> Do you have the recommended laptops or desktops on which ROCm works?

It's difficult to say for laptops, but it looks like those with the RX 550 are unlikely to work.
Support for Vega M GL based laptops was recently added (#651). The Vega M chip is significantly better performing than the RX 550. It's built with the Intel i7-8705G CPU but it's only used in a few laptops.
Another Laptop option _might_ be those with the RX 560, many of these use Ryzen CPUs and should (in theory) work with ROCm. Again, as you have found, manufacturers might cut corners in design that prevent ROCm from working. I think AMD should probably make a list of known tested and working laptops in future to avoid the problem you have been facing.

It's far simpler for desktops. Anything which has a supported CPU and GPU will work unless the manufacturer has designed it badly (very rare I think). Any desktop tower from a major brand that is equipped with an RX 500 series or Vega GPU will work. I would personally recommend a desktop for ROCm because there are few good laptops using AMD GPUs and desktops are not power constrained and so offer much better performance and therefore value for money.

---

### 评论 #4 — kentrussell (2019-06-28T13:48:09Z)

A bit of a summary/re-hash of https://github.com/RadeonOpenCompute/ROCm/issues/827, but modified since it's a laptop, not a desktop (running ROCm on a mobile platform is a bit of a crapshoot, as you'll see below)

We require PCI Atomics for ROCm for GFX8 GPUs, and if the motherboard doesn't support it, then we can't run ROCm on that GPU .

Because your RX550 is GFX8 (Polaris12), it requires PCIe atomics in order to run ROCm. The i7-8850u  CPU (at least based on its architecture) can support PCI atomics, but if it's not reporting it as available (as @JMadgwick confirmed in your lspci output), then you're out of luck since the laptop manufacturer either disabled that in the motherboard, or the 8850u is a special CPU designed to fit a certain price point and the PCI atomics functionality isn't there.

GFX9-and-newer (Vega) can get by without PCI atomics, so if you find a Vega-based GPU (not VegaM, that's a misnomer and is really GFX8), then you can definitely get ROCm going regardless of the motherboard support.

Unfortunately, as @JMadgwick said, some manufacturers remove support for certain things to maintain a certain price point or performance level for their hardware, either in the CPU, GPU or motherboard. And since there are so many laptops that have AMD GPUs inside, it's impossible to keep a master list of what works and what doesn't. Mostly it comes down to anecdotal information from other github users. It would be great to have it, but unfortunately the majority of testing for ROCm comes down to the desktops and specific GPUs, since we have control over those instead of the numerous variants on the same chip that we find in mobile offerings. Even the "same" mobile GPUs with the same chip ID can have different features added/removed based on what the laptop manufacturer wants (again, price point and performance levels, trying to provide a balanced catalog of offerings), which makes kernel support really difficult. The only way to know for sure is to either get GFX9-based GPUs, or to contact the laptop manufacturer to confirm PCIe Atomics support. 

For more information, see https://github.com/RadeonOpenCompute/ROCm_Documentation/blob/master/Installation_Guide/More-about-how-ROCm-uses-PCIe-Atomics.rst

You can also refer to https://github.com/RadeonOpenCompute/ROCm#supported-gpus for the whole supported list of GPUs and below that the supported GPUs, with the atomics caveats.

---

### 评论 #5 — vulturm (2019-06-29T00:42:07Z)

I am aware that current focus is on future generations of hardware.

But my question is: given that vega is capable to be used without PCI-E
atomics, could polaris also achieve the same result purely through software
or it is missing the required hardware capability?
I am asking because the old driver didn't had this requirement. And also
because it might be very benefical for AMD to support it for polaris also
due to the amount of mobile devices in the market, this might increase the
adoption among ML engineers on ROCm.

---
Sent from mobile, apologies for typos.


---

### 评论 #6 — kentrussell (2019-06-29T19:19:01Z)

Unfortunately GFX8 doesn't have the ability to work around the Atomics issue like GFX9+ does, which is why we're stuck in this situation. The old driver didn't use the Atomics functionality, but this resulted in an incredibly noticeable performance drop compared to the newer releases. So you can use pre-1.8 ROCm, to get around the HW limitations, but the performance is really not great there. It's unfortunate, but it's something we're stuck with due to the hardware, and how we use Atomics in ROCm.

---

### 评论 #7 — algoton (2019-07-04T18:28:28Z)

Appreciated for all the advises. I agree. Desktop with the dGPU is the preferred way to mess with rocm. In case you have space limitation like me, I have been able to install rocm on 
[Acer Predator Helios 500](https://www.acer.com/ac/en/US/content/predator-series-features/predatorhelios500) after disable secure boot.
Here is the output of rocminfo:

*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
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
  Chip ID:                 26751                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1301                               
  BDFID:                   2048                               
  Compute Unit:            56                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  134218752                          
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
      Size:                    8372224KB                          
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
      Name:                    amdgcn-amd-amdhsa--gfx900          
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

### 评论 #8 — kafran (2019-12-30T13:45:40Z)

I'm facing the same problem. I bought a new Lenovo Laptop with RX550X + i7-8565U in the hope of using ROCm to learn and prototype and now I have a machine with a useless GPU (since I do not game). I tried to install a prior version of ROCm (1.7.2) to see if it works on my HW, no luck either. rocminfo just hangs with no feedback or error.

Now I regret of not saving a little more money to buy a NVIDIA GPU and go with CUDA.

---

### 评论 #9 — xuhuisheng (2020-06-27T13:47:33Z)

@JMadgwick Thank you very much. You are the only person, who can tell whether hardware could support atomics exactly. It is so painful that I can merely find out which cpu/motherboard could support atomics, moreover, the PCIe from pch cannot support atomic too, even if cpu supports.
I think the ROCm team should add `how to judge atomic` into the offical document.

---

### 评论 #10 — esginmurat (2023-04-14T17:29:31Z)

**Hello.** i have a same problem. Lenovo e580 Latest 1.49 bios installed.  In Linux distros; In boot messages, I tried LTS kernel (5.15) or 6.1x new version or distributions using the latest software, unfortunately I get these error messages.
(I have tried this on all 10 of the most used linux distributions known. I am getting the same error on all of them.) 

It has been going on for years and no fix has been released by either amd or lenovo. It's very sad.


```
[ 9.298192] kfd kfd: amdgpu: skipped device 1002:699f, PCI rejects atomics 730<0

---
ACPI BIOS Error (bug): AE_AML_BUFFER_LIMIT, Field [TBF3] at bit offset/length 262144/32768 exceeds size of target Buffer (262144 bits) (20220331/dsopcode-198)
ACPI Error: Aborting method \_SB.PCI0.GFX0.GETB due to previous error (AE_AML_BUFFER_LIMIT) (20220331/psparse-529)
ACPI Error: Aborting method \_SB.PCI0.GFX0.ATRM due to previous error (AE_AML_BUFFER_LIMIT) (20220331/psparse-529)
failed to evaluate ATRM got AE_AML_BUFFER_LIMIT
```


**My hardware list:**
```
glc@glc-pc:~$ lspci -nnk
00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [8086:5914] (rev 08)
Subsystem: Lenovo Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [17aa:5068]
Kernel driver in use: skl_uncore
00:02.0 VGA compatible controller [0300]: Intel Corporation UHD Graphics 620 [8086:5917] (rev 07)
Subsystem: Lenovo UHD Graphics 620 [17aa:5069]
Kernel driver in use: i915
Kernel modules: i915
00:08.0 System peripheral [0880]: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model [8086:1911]
Subsystem: Lenovo Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model [17aa:5068]
00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
Subsystem: Lenovo Sunrise Point-LP USB 3.0 xHCI Controller [17aa:5068]
Kernel driver in use: xhci_hcd
Kernel modules: xhci_pci
00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
Subsystem: Lenovo Sunrise Point-LP Thermal subsystem [17aa:5068]
Kernel driver in use: intel_pch_thermal
Kernel modules: intel_pch_thermal
00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
Subsystem: Lenovo Sunrise Point-LP CSME HECI [17aa:5068]
Kernel driver in use: mei_me
Kernel modules: mei_me
00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03] (rev 21)
Subsystem: Lenovo Sunrise Point-LP SATA Controller [AHCI mode] [17aa:5068]
Kernel driver in use: ahci
Kernel modules: ahci
00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 [8086:9d10] (rev f1)
Kernel driver in use: pcieport
00:1c.4 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 [8086:9d14] (rev f1)
Kernel driver in use: pcieport
00:1d.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 [8086:9d18] (rev f1)
Kernel driver in use: pcieport
00:1d.2 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #11 [8086:9d1a] (rev f1)
Kernel driver in use: pcieport
00:1d.3 PCI bridge [0604]: Intel Corporation Device [8086:9d1b] (rev f1)
Kernel driver in use: pcieport
00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point LPC Controller/eSPI Controller [8086:9d4e] (rev 21)
Subsystem: Lenovo Sunrise Point LPC Controller/eSPI Controller [17aa:5068]
00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
Subsystem: Lenovo Sunrise Point-LP PMC [17aa:5068]
00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d71] (rev 21)
Subsystem: Lenovo Sunrise Point-LP HD Audio [17aa:5068]
Kernel driver in use: snd_hda_intel
Kernel modules: snd_hda_intel, snd_soc_skl, snd_soc_avs, snd_sof_pci_intel_skl
00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
Subsystem: Lenovo Sunrise Point-LP SMBus [17aa:5068]
Kernel driver in use: i801_smbus
Kernel modules: i2c_i801
02:00.0 Display controller [0380]: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon 540/540X/550/550X / RX 540X/550/550X] [1002:699f] (rev c0)
Subsystem: Lenovo Lexa PRO [Radeon 540/540X/550/550X / RX 540X/550/550X] [17aa:5069]
Kernel driver in use: amdgpu
Kernel modules: amdgpu
03:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 10)
Subsystem: Lenovo RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [17aa:5068]
Kernel driver in use: r8169
Kernel modules: r8169
04:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961/SM963 [144d:a804]
Subsystem: Samsung Electronics Co Ltd SM963 2.5" NVMe PCIe SSD [144d:a801]
Kernel driver in use: nvme
Kernel modules: nvme
05:00.0 Network controller [0280]: Intel Corporation Dual Band Wireless-AC 3165 Plus Bluetooth [8086:3166] (rev 99)
Subsystem: Intel Corporation Dual Band Wireless-AC 3165 [8086:4210]
Kernel driver in use: iwlwifi
Kernel modules: iwlwifi
06:00.0 SD Host controller [0805]: O2 Micro, Inc. SD/MMC Card Reader Controller [1217:8621] (rev 01)
Subsystem: Lenovo SD/MMC Card Reader Controller [17aa:5068]
Kernel driver in use: sdhci-pci
Kernel modules: sdhci_pci
glc@glc-pc:~$
```

Continue:..    
```
glc@glc-pc:~$ sudo lspci -t
-[0000:00]-+-00.0
+-02.0
+-08.0
+-14.0
+-14.2
+-16.0
+-17.0
+-1c.0-[02]----00.0
+-1c.4-[03]----00.0
+-1d.0-[04]----00.0
+-1d.2-[05]----00.0
+-1d.3-[06]----00.0
+-1f.0
+-1f.2
+-1f.3
\-1f.4

```

Continue:....
```
glc@glc-pc:~$ lspci -tnnv
-[0000:00]-+-00.0 Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [8086:5914]
+-02.0 Intel Corporation UHD Graphics 620 [8086:5917]
+-08.0 Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model [8086:1911]
+-14.0 Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f]
+-14.2 Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31]
+-16.0 Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a]
+-17.0 Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03]
+-1c.0-[02]----00.0 Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon 540/540X/550/550X / RX 540X/550/550X] [1002:699f]
+-1c.4-[03]----00.0 Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168]
+-1d.0-[04]----00.0 Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961/SM963 [144d:a804]
+-1d.2-[05]----00.0 Intel Corporation Dual Band Wireless-AC 3165 Plus Bluetooth [8086:3166]
+-1d.3-[06]----00.0 O2 Micro, Inc. SD/MMC Card Reader Controller [1217:8621]
+-1f.0 Intel Corporation Sunrise Point LPC Controller/eSPI Controller [8086:9d4e]
+-1f.2 Intel Corporation Sunrise Point-LP PMC [8086:9d21]
+-1f.3 Intel Corporation Sunrise Point-LP HD Audio [8086:9d71]
\-1f.4 Intel Corporation Sunrise Point-LP SMBus [8086:9d23]
glc@glc-pc:~$
```

Is there a way to completely disable this external / discrete video card in linux distributions? Thank you in advance for your help. have a nice day.

---
