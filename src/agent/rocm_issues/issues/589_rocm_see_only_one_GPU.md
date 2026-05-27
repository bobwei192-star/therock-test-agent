# rocm see only one GPU

> **Issue #589**
> **状态**: closed
> **创建时间**: 2018-10-27T14:04:10Z
> **更新时间**: 2021-01-26T12:28:33Z
> **关闭时间**: 2018-11-06T17:44:21Z
> **作者**: T3KX
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/589

## 描述

Hi guys , after many format i got rocm  to cooperate.
The problem is it only see one GPU
the goal is to get this running hashcat. (hc only see 1 gpuas well)

i should say this is a old mining rig i bought used, could it be something in the bios ?

```
root@x:/home/x/Desktop/hashcat-4.2.1# /opt/rocm/bin/rocminfo
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
  Max Clock Frequency (MHz):3300
  BDFID:                   0
  Compute Unit:            2
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    3910956KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    3910956KB
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
  Max Clock Frequency (MHz):1281
  BDFID:                   256
  Compute Unit:            32
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
root@x:/home/x/Desktop/hashcat-4.2.1# lspci | grep 470
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
08:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
root@x:/home/x/Desktop/hashcat-4.2.1#
```

---

## 评论 (13 条)

### 评论 #1 — T3KX (2018-10-27T14:19:02Z)

Poking in the logs i found this suspicious 

```
 cat /var/log/kern.log


Oct 27 08:56:02 x kernel: [   36.127674] pcieport 0000:00:1c.5:   device [8086:a295] error status/mask=00000001/00002000
Oct 27 08:56:02 x kernel: [   36.127675] pcieport 0000:00:1c.5:    [ 0] Receiver Error         (First)
Oct 27 08:56:02 x kernel: [   36.135340] pcieport 0000:00:1c.5: AER: Corrected error received: id=00e5
Oct 27 08:56:02 x kernel: [   36.135350] pcieport 0000:00:1c.5: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e5(Receiver ID)
Oct 27 08:56:02 x kernel: [   36.135358] pcieport 0000:00:1c.5:   device [8086:a295] error status/mask=00000001/00002000
Oct 27 08:56:02 x kernel: [   36.135365] pcieport 0000:00:1c.5:    [ 0] Receiver Error         (First)
Oct 27 08:56:02 x kernel: [   36.147980] pcieport 0000:00:1c.5: AER: Corrected error received: id=00e5
Oct 27 08:56:02 x kernel: [   36.147984] pcieport 0000:00:1c.5: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e5(Receiver ID)
Oct 27 08:56:02 x kernel: [   36.147986] pcieport 0000:00:1c.5:   device [8086:a295] error status/mask=00000001/00002000
Oct 27 08:56:02 x kernel: [   36.147987] pcieport 0000:00:1c.5:    [ 0] Receiver Error         (First)
Oct 27 08:56:02 x kernel: [   36.157033] pcieport 0000:00:1c.6: AER: Corrected error received: id=00e6
Oct 27 08:56:02 x kernel: [   36.157044] pcieport 0000:00:1c.6: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e6(Receiver ID)
Oct 27 08:56:02 x kernel: [   36.157054] pcieport 0000:00:1c.6:   device [8086:a296] error status/mask=00000001/00002000
Oct 27 08:56:02 x kernel: [   36.157061] pcieport 0000:00:1c.6:    [ 0] Receiver Error         (First)
Oct 27 08:56:07 x kernel: [   40.874544] IPv6: ADDRCONF(NETDEV_UP): enp9s0: link is not ready
Oct 27 08:56:07 x kernel: [   40.978970] r8169 0000:09:00.0 enp9s0: link down
Oct 27 08:56:07 x kernel: [   40.979004] r8169 0000:09:00.0 enp9s0: link down
Oct 27 08:56:07 x kernel: [   40.979222] IPv6: ADDRCONF(NETDEV_UP): enp9s0: link is not ready
Oct 27 08:56:10 x kernel: [   43.966554] r8169 0000:09:00.0 enp9s0: link up
Oct 27 08:56:10 x kernel: [   43.966562] IPv6: ADDRCONF(NETDEV_CHANGE): enp9s0: link becomes ready
Oct 27 08:56:21 x kernel: [   55.303084] rfkill: input handler disabled
Oct 27 08:57:07 x kernel: [  100.991207] amdgpu: [powerplay]
Oct 27 08:57:07 x kernel: [  100.991207]  failed to send message 18a ret is 0
Oct 27 08:57:07 x kernel: [  101.345307] amdgpu: [powerplay]
Oct 27 08:57:07 x kernel: [  101.345307]  last message was failed ret is 0
Oct 27 08:57:07 x kernel: [  101.699391] amdgpu: [powerplay]
Oct 27 08:57:07 x kernel: [  101.699391]  failed to send message 18b ret is 0
Oct 27 08:57:08 x kernel: [  102.053452] amdgpu: [powerplay]
Oct 27 08:57:08 x kernel: [  102.053452]  last message was failed ret is 0
Oct 27 08:57:08 x kernel: [  102.407558] amdgpu: [powerplay]
Oct 27 08:57:08 x kernel: [  102.407558]  failed to send message 18c ret is 0
Oct 27 08:57:09 x kernel: [  103.115709] amdgpu: [powerplay]
Oct 27 08:57:09 x kernel: [  103.115709]  last message was failed ret is 0
```

---

### 评论 #2 — T3KX (2018-10-27T15:41:41Z)

ok so little update i upgraded the bios to the last version, and setup the bios as per mining rig using this tuto https://blockoperations.com/motherboard-bios-settings-for-asus-z270-a-and-z270-p/

it get rid the error in kernel.log

But i still only see one gpu in rocminfo, or hashcat

in the mining tuto they set the pcie to 2x , is this ok ?

---

### 评论 #3 — T3KX (2018-10-27T15:45:05Z)

i notice when i run hashcat i get this in
kernel.log

```
Oct 27 11:39:29 x kernel: [ 292.666346] amdgpu: [powerplay]
Oct 27 11:39:29 x kernel: [ 292.666346] failed to send message 145 ret is 0
Oct 27 11:39:29 x kernel: [ 293.072037] amdgpu: [powerplay]
Oct 27 11:39:29 x kernel: [ 293.072037] last message was failed ret is 0
Oct 27 11:39:30 x kernel: [ 293.426088] amdgpu: [powerplay]
Oct 27 11:39:30 x kernel: [ 293.426088] failed to send message 189 ret is 0
Oct 27 11:39:30 x kernel: [ 293.780168] amdgpu: [powerplay]
Oct 27 11:39:30 x kernel: [ 293.780168] last message was failed ret is 0
Oct 27 11:39:30 x kernel: [ 294.134225] amdgpu: [powerplay]
Oct 27 11:39:30 x kernel: [ 294.134225] failed to send message 18a ret is 0
Oct 27 11:39:31 x kernel: [ 294.488322] amdgpu: [powerplay]
Oct 27 11:39:31 x kernel: [ 294.488322] last message was failed ret is 0
Oct 27 11:39:31 x kernel: [ 294.842383] amdgpu: [powerplay]
Oct 27 11:39:31 x kernel: [ 294.842383] failed to send message 18b ret is 0
Oct 27 11:39:31 x kernel: [ 295.196427] amdgpu: [powerplay]
Oct 27 11:39:31 x kernel: [ 295.196427] last message was failed ret is 0
Oct 27 11:39:32 x kernel: [ 295.550513] amdgpu: [powerplay]
Oct 27 11:39:32 x kernel: [ 295.550513] failed to send message 18c ret is 0
Oct 27 11:39:32 x kernel: [ 296.258638] amdgpu: [powerplay]
Oct 27 11:39:32 x kernel: [ 296.258638] last message was failed ret is 0
Oct 27 11:39:33 x kernel: [ 296.612694] amdgpu: [powerplay]
Oct 27 11:39:33 x kernel: [ 296.612694] failed to send message 145 ret is 0
```

---

### 评论 #4 — T3KX (2018-10-27T16:43:19Z)

using the usb flash that came with the rig.. i can see it mines on all cards

---

### 评论 #5 — jlgreathouse (2018-10-27T16:47:28Z)

[Your motherboard](https://www.asus.com/us/Motherboards/PRIME-Z270-A/specifications/) only has up to three PCIe Gen 3 slots, and [your CPU](https://ark.intel.com/products/88179/Intel-Pentium-Processor-G4400-3M-Cache-3-30-GHz-) only has can only be configured to have up to 3 PCIe connections directly to the CPU. The Ark listing says that the 16 PCIe lanes can be configured as "1x16, 2x8, [or] 1x8+2x4". As such, I suspect that you're hooking some or most of your GPUs through a PCIe switch.

I would guess the problem here is that your connection between the missing GPUs and your CPU does not [support PCIe gen 3 atomics](https://github.com/RadeonOpenCompute/ROCm#supported-cpus), which is a requirement for your GPUs.

Could you run `dmesg | grep kfd` and show its output?

---

### 评论 #6 — T3KX (2018-10-27T17:39:48Z)

i got this


root@x:/home/x# dmesg | grep kfd
[    1.574252] kfd kfd: Initialized module
[    3.171005] kfd kfd: Allocated 3969056 bytes on gart
[    3.171104] kfd kfd: added device 1002:67df
[    3.176243] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[    4.806404] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[    6.438475] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[    8.070061] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[    9.698513] kfd kfd: skipped device 1002:67df, PCI rejects atomics


---

### 评论 #7 — jlgreathouse (2018-10-27T18:03:49Z)

Yep, five of your GPUs are connected to your CPU through a path (e.g a PCIe switch) that does not [support PCIe gen 3 atomics](https://github.com/RadeonOpenCompute/ROCm#supported-cpus), which are required for your GPUs to use the ROCm software stack.

---

### 评论 #8 — T3KX (2018-10-27T18:40:09Z)

I am trying to confirm this . i plug only 2 gpus in the 2x16x slots
 and i get 

root@x:/home/x# dmesg | grep kfd
[    1.562084] kfd kfd: Initialized module
[    3.157690] kfd kfd: Allocated 3969056 bytes on gart
[    3.157793] kfd kfd: added device 1002:67df
[    3.161309] kfd kfd: skipped device 1002:67df, PCI rejects atomics

I am gonna try playing in thte bios to set it to gen3 , most mining tuto i found said to put everything in gen2

---

### 评论 #9 — T3KX (2018-10-27T19:07:25Z)

so i tried only the 2 16x slots 
same , only 1 detected.

then i tried putting everything in gen3 in the bios...
it give me the error below in dmesg and kernel.log

looks like i will have to find another route to get hashcat running . thanks for you help jl


[   52.489257] pcieport 0000:00:1c.5: PCIe Bus Error: severity=Corrected, type=P                                                                                             hysical Layer, id=00e5(Receiver ID)
[   52.489260] pcieport 0000:00:1c.5:   device [8086:a295] error status/mask=000                                                                                             00001/00002000
[   52.489264] pcieport 0000:00:1c.5:    [ 0] Receiver Error         (First)
[   52.489268] pcieport 0000:00:1c.5: AER: Corrected error received: id=00e5
[   52.489274] pcieport 0000:00:1c.5: can't find device of ID00e5
[   52.489276] pcieport 0000:00:1c.5: AER: Corrected error received: id=00e5
[   52.489282] pcieport 0000:00:1c.5: can't find device of ID00e5
[   52.489284] pcieport 0000:00:1c.5: AER: Corrected error received: id=00e5
[   52.489292] pcieport 0000:00:1c.5: PCIe Bus Error: severity=Corrected, type=P                                                                                             hysical Layer, id=00e5(Receiver ID)
[   52.489296] pcieport 0000:00:1c.5:   device [8086:a295] error status/mask=000                                                                                             00001/00002000
[   52.489299] pcieport 0000:00:1c.5:    [ 0] Receiver Error         (First)


in kernel.log

Oct 27 14:58:30 x kernel: [   52.509379] pcieport 0000:00:1c.5: can't find devic                                                                                             e of ID00e5
Oct 27 14:58:30 x kernel: [   52.509381] pcieport 0000:00:1c.5: AER: Corrected e                                                                                             rror received: id=00e5
Oct 27 14:58:30 x kernel: [   52.509388] pcieport 0000:00:1c.5: can't find devic                                                                                             e of ID00e5
Oct 27 14:58:30 x kernel: [   52.509390] pcieport 0000:00:1c.5: AER: Corrected e                                                                                             rror received: id=00e5
Oct 27 14:58:30 x kernel: [   52.509397] pcieport 0000:00:1c.5: can't find devic                                                                                             e of ID00e5
Oct 27 14:58:30 x kernel: [   52.509399] pcieport 0000:00:1c.5: AER: Corrected e                                                                                             rror received: id=00e5
Oct 27 14:58:30 x kernel: [   52.509406] pcieport 0000:00:1c.5: can't find devic                                                                                             e of ID00e5
Oct 27 14:58:30 x kernel: [   52.509408] pcieport 0000:00:1c.5: AER: Corrected e                                                                                             rror received: id=00e5
Oct 27 14:58:30 x kernel: [   52.509415] pcieport 0000:00:1c.5: can't find devic                                                                                             e of ID00e5


---

### 评论 #10 — jlgreathouse (2018-10-27T19:13:06Z)

For reference, depending on the slots you use on your motherboard and the BIOS configurations for running them at gen 3, the slots you're plugging your second card into may still be set up as gen 2. I haven't tested your exact motherboard or your processor with it, so I'm also not sure of the exact settings you would need to ensure gen 3 operation with your processor.

Many mining tutorials are not written with ROCm in mind -- while PCIe gen 2 may be useful for mining on other software stacks, but it is not a supported operating mode for gfx8 GPUs on the ROCm software stack. If you have gfx9 GPUs (e.g. Vega 10), then you can run them without PCIe gen 3 atomics. However, the GPUs you are using require PCIe gen 3 atomics in the ROCm software stack. See [this thread](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422836032) for many more details.

---

### 评论 #11 — T3KX (2018-10-29T04:53:28Z)

is there a way to see if the cards are connected directly to the cpu or tough the plx / bridge ?

---

### 评论 #12 — jlgreathouse (2018-10-29T14:16:03Z)

`lspci -tv` will show the topology of how the PCIe system (including GPUs) are logically connected in your system.

---

### 评论 #13 — brauliobo (2021-01-26T12:22:37Z)

confirmed this problem with https://aur.archlinux.org/packages/rocm-opencl-runtime/ version 4.0.0 and that I can use my 2 GPUs with AMDGPU driver 20.40 https://aur.archlinux.org/packages/opencl-amd (20.45 segfaults) with phoenixminer and lolMiner

---
