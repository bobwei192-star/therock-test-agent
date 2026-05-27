# Is there any complete instruction on how to build full ROCm stack from source?

> **Issue #520**
> **状态**: closed
> **创建时间**: 2018-09-04T03:38:40Z
> **更新时间**: 2019-01-05T00:25:07Z
> **关闭时间**: 2018-09-05T13:09:54Z
> **作者**: kneternal
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/520

## 描述

Or otherwise, currently, it is hard to get a 4.15.0-33 linux kernel supported ROCm1.8.3 version installed. Please help

---

## 评论 (16 条)

### 评论 #1 — kneternal (2018-09-04T09:25:39Z)

Some additional question:

Need some help about how install the full stack of ROCm 1.8.3. I tried to build it from source because installing from "apt install rocm-dkms" doesn't work for me and I was always getting a "hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104" error from rocminfo

---

### 评论 #2 — jlgreathouse (2018-09-04T19:47:51Z)

Each part of the ROCm stack has its own build/install directions, and you should be able to go to each page to get directions on building them. That being said, the ROCk / kernel driver stack is compiled as part of the apt install process (since it is a DKMS module), so following its .deb install commands is probably the cleanest way to see how it is built.

I suspect that it's *not* going to be easier for you to build everything from source. The problem you're seeing indicates that something has gone wrong with your install, or that your hardware does not support ROCm.

Could you help me out by giving me:
- The make and model of the GPU(s) you are using
- The model of CPU you are using
- The model of motherboard you are using
- Which PCIe slot(s) on that motherboard your GPU(s) are installed in

In addition, could you run the following commands and show me the output?
- `uname -a`
- `dkms status`
- `lsmod | grep amdgpu`
- `lsmod | grep amdkfd`
- `groups`
- `lspci | grep VGA`
- `lspci -vvv`
- `lspci -tv`
- `lspci -n`
- After a reboot: `dmesg`

---

### 评论 #3 — kneternal (2018-09-05T00:42:24Z)

Thank you so much for your response. Here are the info

CPU: i7-8700
GPU: Rx550
Motherboard: dell's 0J8G6F
PCIe: a 3.0 16x slot

```shell
uname -a
Linux AbcDesktop 4.15.0-33-generic #36-Ubuntu SMP Wed Aug 15 16:00:05 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

```shell
dkms status
amdgpu, 1.8-199, 4.15.0-33-generic, x86_64: installed
```

```shell
lsmod | grep amdgpu
    amdgpu               2703360  2
    chash                  16384  1 amdgpu
    ttm                   106496  1 amdgpu
    i2c_algo_bit           16384  2 amdgpu,i915
    drm_kms_helper        172032  2 amdgpu,i915
    drm                   401408  20 amdgpu,i915,ttm,drm_kms_helper
```

```shell
lsmod | grep amdkfd
    amdkfd                274432  1
    amd_iommu_v2           20480  1 amdkfd
    amdkcl                 28672  4 amdttm,amdgpu,amd_sched,amdkfd
```

```shell
groups
    kneternal adm cdrom sudo dip video plugdev lpadmin sambashare
```

```shell
lspci | grep VGA
    00:02.0 VGA compatible controller: Intel Corporation Device 3e92
    01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Polaris12 (rev c7)
```

```shell
lspci -vvv
    00:00.0 Host bridge: Intel Corporation Device 3ec2 (rev 07)
	Subsystem: Dell Device 085b
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
	Latency: 0
	Capabilities: <access denied>

00:01.0 PCI bridge: Intel Corporation Skylake PCIe Controller (x16) (rev 07) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
	I/O behind bridge: 00003000-00003fff
	Memory behind bridge: e2100000-e21fffff
	Prefetchable memory behind bridge: 00000000d0000000-00000000e01fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:02.0 VGA compatible controller: Intel Corporation Device 3e92 (prog-if 00 [VGA controller])
	Subsystem: Dell Device 085b
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 125
	Region 0: Memory at e1000000 (64-bit, non-prefetchable) [size=16M]
	Region 2: Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Region 4: I/O ports at 4000 [size=64]
	[virtual] Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: i915
	Kernel modules: i915

00:08.0 System peripheral: Intel Corporation Skylake Gaussian Mixture Model
	Subsystem: Dell Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 255
	Region 0: Memory at e223f000 (64-bit, non-prefetchable) [disabled] [size=4K]
	Capabilities: <access denied>

00:12.0 Signal processing controller: Intel Corporation Device a379 (rev 10)
	Subsystem: Dell Device 085b
	Control: I/O- Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 20
	Region 0: Memory at e223e000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: intel_pch_thermal
	Kernel modules: intel_pch_thermal

00:14.0 USB controller: Intel Corporation Device a36d (rev 10) (prog-if 30 [XHCI])
	Subsystem: Dell Device 085b
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin ? routed to IRQ 122
	Region 0: Memory at e2220000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

00:14.2 RAM memory: Intel Corporation Device a36f (rev 10)
	Subsystem: Intel Corporation Device 7270
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Region 0: Memory at e2236000 (64-bit, non-prefetchable) [disabled] [size=8K]
	Region 2: Memory at e223d000 (64-bit, non-prefetchable) [disabled] [size=4K]
	Capabilities: <access denied>

00:15.0 Serial bus controller [0c80]: Intel Corporation Device a368 (rev 10)
	Subsystem: Dell Device 085b
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	Region 0: Memory at e0200000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: intel-lpss
	Kernel modules: intel_lpss_pci

00:16.0 Communication controller: Intel Corporation Device a360 (rev 10)
	Subsystem: Dell Device 085b
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 127
	Region 0: Memory at e223b000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: mei_me
	Kernel modules: mei_me

00:17.0 SATA controller: Intel Corporation Device a352 (rev 10) (prog-if 01 [AHCI 1.0])
	Subsystem: Dell Device 085b
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 123
	Region 0: Memory at e2234000 (32-bit, non-prefetchable) [size=8K]
	Region 1: Memory at e223a000 (32-bit, non-prefetchable) [size=256]
	Region 2: I/O ports at 4090 [size=8]
	Region 3: I/O ports at 4080 [size=4]
	Region 4: I/O ports at 4060 [size=32]
	Region 5: Memory at e2239000 (32-bit, non-prefetchable) [size=2K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

00:1f.0 ISA bridge: Intel Corporation Device a306 (rev 10)
	Subsystem: Dell Device 085b
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0

00:1f.3 Audio device: Intel Corporation Device a348 (rev 10)
	Subsystem: Dell Device 085b
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 129
	Region 0: Memory at e2230000 (64-bit, non-prefetchable) [size=16K]
	Region 4: Memory at e2000000 (64-bit, non-prefetchable) [size=1M]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

00:1f.4 SMBus: Intel Corporation Device a323 (rev 10)
	Subsystem: Dell Device 085b
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 255
	Region 0: Memory at e2238000 (64-bit, non-prefetchable) [size=256]
	Region 4: I/O ports at efa0 [size=32]
	Kernel modules: i2c_i801

00:1f.5 Serial bus controller [0c80]: Intel Corporation Device a324 (rev 10)
	Subsystem: Dell Device 085b
	Control: I/O- Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Region 0: Memory at fe010000 (32-bit, non-prefetchable) [size=4K]

00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (7) I219-V (rev 10)
	Subsystem: Dell Ethernet Connection (7) I219-V
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin D routed to IRQ 124
	Region 0: Memory at e2200000 (32-bit, non-prefetchable) [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: e1000e
	Kernel modules: e1000e

01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Polaris12 (rev c7) (prog-if 00 [VGA controller])
	Subsystem: Dell Lexa PRO [Radeon RX 550]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 126
	Region 0: Memory at d0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at e0000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at 3000 [size=256]
	Region 5: Memory at e2100000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at e2140000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
	Subsystem: Dell Device aae0
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 128
	Region 0: Memory at e2160000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel
```
```shell
lspci -tv
-[0000:00]-+-00.0  Intel Corporation Device 3ec2
           +-01.0-[01]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Polaris12
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
           +-02.0  Intel Corporation Device 3e92
           +-08.0  Intel Corporation Skylake Gaussian Mixture Model
           +-12.0  Intel Corporation Device a379
           +-14.0  Intel Corporation Device a36d
           +-14.2  Intel Corporation Device a36f
           +-15.0  Intel Corporation Device a368
           +-16.0  Intel Corporation Device a360
           +-17.0  Intel Corporation Device a352
           +-1f.0  Intel Corporation Device a306
           +-1f.3  Intel Corporation Device a348
           +-1f.4  Intel Corporation Device a323
           +-1f.5  Intel Corporation Device a324
           \-1f.6  Intel Corporation Ethernet Connection (7) I219-V
```
```shell
lspci -n
00:00.0 0600: 8086:3ec2 (rev 07)
00:01.0 0604: 8086:1901 (rev 07)
00:02.0 0300: 8086:3e92
00:08.0 0880: 8086:1911
00:12.0 1180: 8086:a379 (rev 10)
00:14.0 0c03: 8086:a36d (rev 10)
00:14.2 0500: 8086:a36f (rev 10)
00:15.0 0c80: 8086:a368 (rev 10)
00:16.0 0780: 8086:a360 (rev 10)
00:17.0 0106: 8086:a352 (rev 10)
00:1f.0 0601: 8086:a306 (rev 10)
00:1f.3 0403: 8086:a348 (rev 10)
00:1f.4 0c05: 8086:a323 (rev 10)
00:1f.5 0c80: 8086:a324 (rev 10)
00:1f.6 0200: 8086:15bc (rev 10)
01:00.0 0300: 1002:699f (rev c7)
01:00.1 0403: 1002:aae0
```

```shell
dmesg | grep amd
[    0.000000] Linux version 4.15.0-33-generic (buildd@lcy01-amd64-024) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #36-Ubuntu SMP Wed Aug 15 16:00:05 UTC 2018 (Ubuntu 4.15.0-33.36-generic 4.15.18)
[    1.684577] amdkcl: loading out-of-tree module taints kernel.
[    1.684587] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    1.760925] [drm] amdgpu kernel modesetting enabled.
[    1.766433] amdgpu 0000:01:00.0: enabling device (0100 -> 0103)
[    1.766735] [drm] add ip block number 3 <amdgpu_powerplay>
[    2.812542] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    2.812543] amdgpu 0000:01:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    2.812689] [drm] amdgpu: 4096M of VRAM memory ready
[    2.812689] [drm] amdgpu: 15843M of GTT memory ready.
[    2.992402] amdgpu 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    3.717363] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:01:00.0 on minor 0
```



Please help, thank you. 



---

### 评论 #4 — jlgreathouse (2018-09-05T01:37:01Z)

Hi @kneternal 

I believe the problem here is that your GPU, an AMD Radeon RX 550, is not currently supported in ROCm. While we support Polaris 10 and Polaris 11, this Polaris 12 GPU is not currently supported in ROCm. I apologize for this limitation -- we are working on expanding support for our GPUs in future releases of ROCm. However, at this time, ROCm will not work on your GPU.

---

### 评论 #5 — kneternal (2018-09-05T01:44:13Z)

Oh, I see. Sorry for misunderstanding that the supporting list doesn't include the RX550. And can we reveal a little bit about the schedule of how soon will it be supported in ROCm? 

---

### 评论 #6 — preda (2018-09-05T03:07:16Z)

Build instructions, or a build script, would still be nice to have.

I wonder how does the team internally build a release? -- is each component built individually, following its particular build instructions manually, and then gathered together, or does the team have a "master build script" that can be run once and build a release?


---

### 评论 #7 — kneternal (2018-09-05T10:10:40Z)

@preda Had the same question. I guess that they should have a script or some sort of a system to build and link everything. 

---

### 评论 #8 — jlgreathouse (2018-09-05T13:09:54Z)

@kneternal I apologize that am unable to provide a public timeline for Polaris 12 support. I can tell you that it will not be part of the upcoming ROCm 1.9 release.

@preda we have an automated build system, so no, we don't manually build everything. I can ask internally how much of our automation we could try to make public, but I believe that directions for building every ROCm package are included as either part of that package's open source repository, or (for instance for our KFD DKMS build) are part of our shipping packages themselves. We're always looking for community involvement, if you're interested in automating any of that. :)

---

### 评论 #9 — preda (2018-09-05T23:59:41Z)

@jlgreathouse Having ROCm open-source is a great starting point, and a precondition for community involvement. IMO the community involvement can be facilitated by having a simple build script or recipe that works out-of-the-box with a shallow learning curve. 

If OTOH you expect the community to develop the build of the open-source product, it may have the effect of reducing somehow the involvement because some people (like me) do not make it past the build phase.

If I could build, I would thus have a baseline on top of which I could maybe start experimenting ("hacking").


---

### 评论 #10 — gstoner (2018-09-06T00:26:43Z)

The goal is to have over master build solution, but remember ROCm was built so you can build just sub packages and replace the ones even in a master build.  Like just replace a compiler.  

I some bigger ideas but we need to get more cloud penetration of our GPU's  first.  

---

### 评论 #11 — chriselrod (2018-10-13T21:32:16Z)

I'm a statistics graduate student, and planing on giving a fun presentation demoing image recognition with a few colleagues to the other graduate students on the 26th.
Ideally, I'd like to use ROCm, and have two computers with Vega64 graphics cards. One has Fedora, the other Antergos (pacman/AUR package managers). In particular, I plan on using TensorFlow, or wrapping enough of the BLAS in Julia to use Flux.

If I clone all the packages listed in the [default.xml](https://github.com/RadeonOpenCompute/ROCm/blob/master/default.xml) file, and follow the build instructions, is it likely to work?
Build instructions aren't always ROCm-focused. The [ROCK-Kernel-Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver)'s README in [documentation/admin-guide](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/Documentation/admin-guide/README.rst) looks like regular instructions for building the Linux kernel.

Should I start there, installing the components from the list one by one?
If I run into problems and need help, are folks here likely/willing to provide help/instructions?

I also saw [this](https://github.com/RadeonOpenCompute/ROCm/issues/567#issuecomment-427678812) on possible Fedora support incoming. Although I wouldn't expect anything in the next couple weeks.

EDIT: While the AUR unfortunately doesn't have much for ROCm, it does have interesting things such as the latest [Linux kernel with AMDGPU DC patches](https://aur.archlinux.org/packages/linux-amd-git/).

1. Reading that upstream kernel 4.18+ should be fine, I skipped the ROCK-Kernel-Driver, and went to [ROCT-Thunk-Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface) as the second item on the list. It requires numactl as a dependency. Installing that, and it built fine.
2. ROC-smi. I don't know what to do with this.
3. ROCR-Runtime. Requires "hsakmt.h" and "hsakmttypes.h". There is a "hsakmt.h" that comes with ROCT-Thunk-Interface, but it is not copied or moved anywhere upon installation. Therefore it is better to point cmake to wherever these were built, not installed.
Now I get:
```
/home/chriselrod/Documents/libraries/ROCm/ROCR-Runtime/src/core/runtime/runtime.cpp:260:71: error: ‘void* memset(void*, int, size_t)’ clearing an object of non-trivial type ‘__gnu_cxx::__alloc_traits<std::allocator<core::Runtime::LinkInfo>, core::Runtime::LinkInfo>::value_type’ {aka ‘struct core::Runtime::LinkInfo’}; use assignment or value-initialization instead [-Werror=class-memaccess]
          link_matrix_.size() * sizeof(hsa_amd_memory_pool_link_info_t));
                                                                       ^

In file included from /home/chriselrod/Documents/libraries/ROCm/ROCR-Runtime/src/core/runtime/runtime.cpp:43:
/home/chriselrod/Documents/libraries/ROCm/ROCR-Runtime/src/core/inc/runtime.h:97:10: note: ‘__gnu_cxx::__alloc_traits<std::allocator<core::Runtime::LinkInfo>, core::Runtime::LinkInfo>::value_type’ {aka ‘struct core::Runtime::LinkInfo’} declared here
   struct LinkInfo {
```

---

### 评论 #12 — candrews (2018-12-14T05:07:35Z)

Point 3 is solved by https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/pull/25 - I'm hoping that gets merged sometime soon!

---

### 评论 #13 — jlgreathouse (2018-12-21T01:34:24Z)

@kneternal @preda and others in this thread who have been asking about ROCM build and installation directions:
You may be interested in the newly released Experimental ROC project. This includes scripts and tools for both installing ROCm (so you don't have to type stuff by hand from our README files), but also a full script of scripts for rebuilding ROCm from source.

This allows you to build individual ROCm components and save them into local directories (e.g. to test patches), build and install into other locations (like `/opt/rocm/`) and build .deb and .rpm packages for these components. There are also tools to build and install things "in order" so you don't run into any dependency issues (e.g. if you are not building packages and letting your package manager handle them for you).

https://github.com/RadeonOpenCompute/Experimental_ROC

@chriselrod I know this is far too late to help your group's presentation, but the above repo also contains tools for performing a full ROCm installation (using the upstream kernel driver) onto Fedora 28 and Fedora 29.

---

### 评论 #14 — jlgreathouse (2018-12-22T00:42:13Z)

@kneternal I also forgot to mention in my post from yesterday:
"Polaris 12" should be be enabled in ROCm 2.0. I just sat down and tested a batch of OpenCL, HCC, and HIP applications with a Polaris 12 board, and things appear to be working as expected.

Note that you will need to be on a distro that supports our rock-dkms driver to have this support, since the last bit that needed to be in place was a driver change. Support for this is in the `amd-staging-next` drivers, but will not hit upstream Linux until post-4.20.

---

### 评论 #15 — preda (2019-01-04T22:08:30Z)

I have a request for Experimental_ROC: right now it checks out the sources from the roc-2.0.0 tag by default. I would like a way to either specify a specific branch, or a way to track more up-to-date source than that tag. It seems the branch "amd-common" is more representative of tip-of-tree.

---

### 评论 #16 — jlgreathouse (2019-01-05T00:25:07Z)

Feel free to submit that as a ticket on that repo. I prefer to track project-specific bugs or requests on their own repo so that ROCm doesn't get completely flooded. (And, since this ticket is closed, I will completely forget about your request unless I leave this tab open for eternity).

That said:
- You can pretty quickly modify the tag, branch, or SHA-1 that are being checked out by modifying the [common_options.sh](https://github.com/RadeonOpenCompute/Experimental_ROC/blob/roc-2.0.0/distro_install_scripts/shared_files/common_options.sh) file.
  - Hm.. I wonder if instead of having all the projects with `roc-2.0.0` tags check out `${ROCM_VERSION_TAG}`, I should instead make a variable for each one in `common_options.sh` that is just set to `${ROCM_VERSION_TAG} by default.
- It is not the case that `amd-common` is guaranteed to build or work at all. Not all of our projects work through CI systems like you might normally expect. Many projects only push out major working portions of their code on tagged releases.
  - As such, I worry about putting `amd-master` in the Experimental ROC master branch. Most users who download Experimental ROC will *not* switch over to roc-2.0.0 to build ROCm 2.0. Most users never leave master, and if things are broken (due to some random project being broken), they will blame me. :)
  - Instead, I'm trying to keep Experimental ROC's master branch always pointing to the most up-to-date ROCm "release".

---
