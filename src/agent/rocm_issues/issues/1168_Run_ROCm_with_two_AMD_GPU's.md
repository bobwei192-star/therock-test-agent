# Run ROCm with two AMD GPU's

> **Issue #1168**
> **状态**: closed
> **创建时间**: 2020-06-28T20:02:28Z
> **更新时间**: 2020-12-17T04:32:35Z
> **关闭时间**: 2020-12-17T04:32:35Z
> **作者**: Q2Learn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1168

## 描述

Hey, 

I am trying to install a second AMD GPU on my machine to run machine learning problems. 

My setup:

Motherboard: Asus Prime Z270-P
CPU: Intel Core i5-7500
Graphics: Radeon RX 570 Series (POLARIS10, DRM 3.37.0, 5.3.0-61-generic, LLVM 9.0.0)
GPU 0: MSI Ellesmere [Radeon RX 470/480/570/570X/580/580X]
GPU 1: ASUS Ellesmere [Radeon RX 470/480/570/570X/580/580X]
ROCm Version: Version: 3.5.1-34
Linux OS: Ubuntu 18.04.1
Kernel: 5.3.0-61-generic
ROCm installation guide: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html
ROCm-tensorflow instructions: pip3 install tensorflow-rocm
tensorflow version: 2.2.0

Running "rocm-smi -s" I see the two GPUs (added above). 

Running dmesg I see it's rejecting atomics: dmesg | grep kfd
[    1.460499] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    1.461213] kfd kfd: amdgpu: added device 1002:67df
[    1.487376] kfd kfd: amdgpu: skipped device 1002:67df, PCI rejects atomics

I don't understand the PCIe atomics to be honest, but I have read about it a few times and I thought that was relative to the CPU/GPU of which I though I was good? In my motherboard BIOS I set it to Gen3 for the PCIe slots. My GPU's are connected into PCIEX16_1 and PCIEX16_2 where the GPU in PCIEX16_1 is working. 
 
Testing the working GPU: I am running a virtual environment. I tested rocm tensorflow on the resnet50 after I download the tensorflow benchmark: "python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=64 --model=resnet50" and in another tab I am running: "watch -n 1 rocm-smi" and I see GPU [0] running and I get results returned from the benchmark test (20 images a second lol)

But when I try --num_gpus=2 I get a long list of errors. 

Is there any solution to run two GPUs with ROCm that I am not doing? Why is it rejecting atomics but working on one of the GPU's? Is my motherboard the issue? Maybe reset my motherboard bios to default? 

Thank you all for your help!


---

## 评论 (8 条)

### 评论 #1 — xuhuisheng (2020-06-29T00:54:00Z)

I think you could use `sudo lspci -t` to see the topologic of the pci-e.
Then run `sudo lspci -vvv` to check whether both of video pci-e had AtomicOpsCap support.
Moreover only GFX8(RX580, etc), need atomic support. GFX9(Vega 56) can run without atomics.

You can see some more disscution from here : https://github.com/RadeonOpenCompute/ROCm/issues/1146



---

### 评论 #2 — Q2Learn (2020-07-01T01:24:05Z)

I don't know pcie topology. 
**I ran "sudo lspci -t" here are my results:**

-[0000:00]-+-00.0
           +-01.0-[01]--+-00.0
           |            \-00.1
           +-14.0
           +-16.0
           +-17.0
           +-1b.0-[02]--
           +-1b.4-[03]--+-00.0
           |            \-00.1
           +-1c.0-[04]--
           +-1c.7-[05]----00.0
           +-1d.0-[06]--
           +-1f.0
           +-1f.2
           +-1f.3
           \-1f.4


**and then I ran "lspci -vvv" and I get a long list:**

00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 05)
	Subsystem: ASUSTeK Computer Inc. Intel Kaby Lake Host Bridge
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
	Latency: 0
	Capabilities: <access denied>
	Kernel driver in use: skl_uncore

00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) (rev 05) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 120
	Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: f7e00000-f7efffff
	Prefetchable memory behind bridge: 0000002080000000-00000021ffffffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR+ NoISA- VGA+ MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:14.0 USB controller: Intel Corporation 200 Series/Z370 Chipset Family USB 3.0 xHCI Controller (prog-if 30 [XHCI])
	Subsystem: ASUSTeK Computer Inc. 200 Series PCH USB 3.0 xHCI Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 126
	Region 0: Memory at 2ffff10000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

00:16.0 Communication controller: Intel Corporation 200 Series PCH CSME HECI #1
	Subsystem: ASUSTeK Computer Inc. 200 Series PCH CSME HECI
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 131
	Region 0: Memory at 2ffff25000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: mei_me
	Kernel modules: mei_me

00:17.0 SATA controller: Intel Corporation 200 Series PCH SATA controller [AHCI mode] (prog-if 01 [AHCI 1.0])
	Subsystem: ASUSTeK Computer Inc. 200 Series PCH SATA controller [AHCI mode]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 127
	Region 0: Memory at f7f04000 (32-bit, non-prefetchable) [size=8K]
	Region 1: Memory at f7f07000 (32-bit, non-prefetchable) [size=256]
	Region 2: I/O ports at f050 [size=8]
	Region 3: I/O ports at f040 [size=4]
	Region 4: I/O ports at f020 [size=32]
	Region 5: Memory at f7f06000 (32-bit, non-prefetchable) [size=2K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

00:1b.0 PCI bridge: Intel Corporation 200 Series PCH PCI Express Root Port #17 (rev f0) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 121
	Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
	I/O behind bridge: 00002000-00002fff
	Memory behind bridge: a8000000-a81fffff
	Prefetchable memory behind bridge: 0000002000000000-00000020001fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:1b.4 PCI bridge: Intel Corporation 200 Series PCH PCI Express Root Port #21 (rev f0) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 122
	Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
	I/O behind bridge: 0000d000-0000dfff
	Memory behind bridge: f7d00000-f7dfffff
	Prefetchable memory behind bridge: 0000002200000000-000000237fffffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:1c.0 PCI bridge: Intel Corporation 200 Series PCH PCI Express Root Port #1 (rev f0) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 123
	Bus: primary=00, secondary=04, subordinate=04, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:1c.7 PCI bridge: Intel Corporation 200 Series PCH PCI Express Root Port #8 (rev f0) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin D routed to IRQ 124
	Bus: primary=00, secondary=05, subordinate=05, sec-latency=0
	I/O behind bridge: 0000c000-0000cfff
	Memory behind bridge: f7c00000-f7cfffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:1d.0 PCI bridge: Intel Corporation 200 Series PCH PCI Express Root Port #9 (rev f0) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 125
	Bus: primary=00, secondary=06, subordinate=06, sec-latency=0
	I/O behind bridge: 00003000-00003fff
	Memory behind bridge: a8200000-a83fffff
	Prefetchable memory behind bridge: 0000002000200000-00000020003fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:1f.0 ISA bridge: Intel Corporation 200 Series PCH LPC Controller (Z270)
	Subsystem: ASUSTeK Computer Inc. 200 Series PCH LPC Controller (Z270)
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0

00:1f.2 Memory controller: Intel Corporation 200 Series/Z370 Chipset Family Power Management Controller
	Subsystem: ASUSTeK Computer Inc. 200 Series PCH PMC
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Region 0: Memory at f7f00000 (32-bit, non-prefetchable) [size=16K]

00:1f.3 Audio device: Intel Corporation 200 Series PCH HD Audio
	Subsystem: ASUSTeK Computer Inc. 200 Series PCH HD Audio
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 132
	Region 0: Memory at 2ffff20000 (64-bit, non-prefetchable) [size=16K]
	Region 4: Memory at 2ffff00000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

00:1f.4 SMBus: Intel Corporation 200 Series/Z370 Chipset Family SMBus Controller
	Subsystem: ASUSTeK Computer Inc. 200 Series PCH SMBus Controller
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 11
	Region 0: Memory at 2ffff24000 (64-bit, non-prefetchable) [size=256]
	Region 4: I/O ports at f000 [size=32]
	Kernel modules: i2c_i801

01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X] (rev ef) (prog-if 00 [VGA controller])
	Subsystem: Micro-Star International Co., Ltd. [MSI] Radeon RX 570
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 129
	Region 0: Memory at 2100000000 (64-bit, prefetchable) [size=4G]
	Region 2: Memory at 2080000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at e000 [size=256]
	Region 5: Memory at f7e00000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 580]
	Subsystem: Micro-Star International Co., Ltd. [MSI] Ellesmere [Radeon RX 580]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 133
	Region 0: Memory at f7e60000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X] (rev ef) (prog-if 00 [VGA controller])
	Subsystem: ASUSTeK Computer Inc. Ellesmere [Radeon RX 470/480/570/580]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 130
	Region 0: Memory at 2200000000 (64-bit, prefetchable) [size=4G]
	Region 2: Memory at 2300000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at d000 [size=256]
	Region 5: Memory at f7d00000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at f7d40000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 580]
	Subsystem: ASUSTeK Computer Inc. Ellesmere [Radeon RX 580]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 134
	Region 0: Memory at f7d60000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

05:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 15)
	Subsystem: ASUSTeK Computer Inc. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 19
	Region 0: I/O ports at c000 [size=256]
	Region 2: Memory at f7c04000 (64-bit, non-prefetchable) [size=4K]
	Region 4: Memory at f7c00000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: r8169
	Kernel modules: r8169

I don't see AtomicOpsCap support. What does that mean?

---

### 评论 #3 — xuhuisheng (2020-07-01T02:17:10Z)

GFX8(rx580) series need PCI-e connect CPU directly, and support the AtomicOpsCap. you can use `sudo lspci`(remember sudo for more details) to see whether your cpu and motherboard support this feature.

something like this:

```
sudo lspci -vvv -s 01:00.0|grep Atomic
AtomicOpsCap: 32bit- 64bit- 128bitCAS-
```

Please reference official announcement from README.md <https://github.com/RadeonOpenCompute/ROCm/#supported-cpus>

---

### 评论 #4 — Q2Learn (2020-07-02T02:44:46Z)

It comes back with no results. So the Asus Z270 does not have PCIe Atomics. My CPU and GPU do it's just the motherboard now. One GPU works, the one that's in the main PCIe so I will have to work with that for now. Thanks. 

---

### 评论 #5 — dundir (2020-07-19T03:50:02Z)

@xuhuisheng how do you go about testing for the PCI-e connecting to the cpu directly? 

When I ran these tests on an Asus Prime B450-Plus with Ryzen 5 Raven Ridge APU, both VGA controllers (APU/dGPU RX560) show Atomics support (AtomicsOpsCap 32bit- 64bit- 128bitCAS-, Atomics OpsCtl: ReqEn+), but rocm is definitely not usable (/dev/kfd bad address, or /dev/kfd cannot be read/write operation not permitted ). 

Edit: I should mention the issue is not one of permissions as /dev/kfd is set with mode 0660 with the proper group perms set and tests were done with root.

---

### 评论 #6 — xuhuisheng (2020-07-20T01:39:14Z)

@dundir using lspci -vt, and we will get the following message (sorry this compute is not using the AMD card.)
```
work@work-ThinkCentre-M920x:~$ lspci -vt
-[0000:00]-+-00.0  Intel Corporation 8th Gen Core 4-core Desktop Processor Host Bridge/DRAM Registers [Coffee Lake S]
           +-01.0-[01]--+-00.0  NVIDIA Corporation GP107GL [Quadro P620]
           |            \-00.1  NVIDIA Corporation GP107GL High Definition Audio Controller
           +-02.0  Intel Corporation 8th Gen Core Processor Gaussian Mixture Model
           +-08.0  Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model
           +-14.0  Intel Corporation Cannon Lake PCH USB 3.1 xHCI Host Controller
           +-14.2  Intel Corporation Cannon Lake PCH Shared SRAM
           +-16.0  Intel Corporation Cannon Lake PCH HECI Controller
           +-16.3  Intel Corporation Cannon Lake PCH Active Management Technology - SOL
           +-17.0  Intel Corporation Cannon Lake PCH SATA AHCI Controller
           +-1b.0-[02]----00.0  Silicon Motion, Inc. Device 2263
           +-1c.0-[03]----00.0  Intel Corporation Dual Band Wireless-AC 3165 Plus Bluetooth
           +-1f.0  Intel Corporation Q370 Chipset LPC/eSPI Controller
           +-1f.3  Intel Corporation Cannon Lake PCH cAVS
           +-1f.4  Intel Corporation Cannon Lake PCH SMBus Controller
           +-1f.5  Intel Corporation Cannon Lake PCH SPI Controller
           \-1f.6  Intel Corporation Ethernet Connection (7) I219-LM
```
14.0 said its name contains PCH, so I guess My video card maybe using the CPU PCIe directly.

And You got the not permitted error. try `ls -l /dev/kfd` to see the group of the kernel module, and `sudo usermod -a -G video $LOGNAME` - if the group of kfd is video.

please referenece the installation guide of ubuntu : https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu


---

### 评论 #7 — dundir (2020-07-20T04:20:00Z)

Unfortunately, the not permitted error isn't related to the actual permissions. Most likely a BIOS issue with ASUS. 
Running as root gets the exact same output, group is 0660 render, and the user is in the correct group as well. I was just wondering if there was a good way of telling if it was direct connected. Both my trees don't contain PCH and each card has a PCIE dummy host.

<summary>
lspci -tv
</summary>

<details>
...
#lspci -vt

<kbd><pre> <Compose>  
-[0000:00]-+-00.0  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Root Complex
|          +-00.2  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 IOMMU
|          +-01.0  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
|          +-01.1-[01]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X]
|                        \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Baffin HDMI/DP Audio [Radeon RX 550 640SP / RX 560/560X]
|          +-01.2-[02-08]--+-00.0  Advanced Micro Devices, Inc. [AMD] 400 Series Chipset USB 3.1 XHCI Controller
|                          +-00.1  Advanced Micro Devices, Inc. [AMD] 400 Series Chipset SATA Controller
|                           \-00.2-[03-08]--+-00.0-[04]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           |                               +-01.0-[05]--
           |                               +-04.0-[06]--
           |                               +-06.0-[07]--
           |                               \-07.0-[08]--
|           +-08.0  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
|           +-08.1-[09]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series]
|                       +-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller
|                       +-00.2  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
|                       +-00.3  Advanced Micro Devices, Inc. [AMD] Raven USB 3.1
|                       +-00.4  Advanced Micro Devices, Inc. [AMD] Raven USB 3.1
|                       \-00.6  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller
|           +-08.2-[0a]----00.0  Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode]
|           +-14.0  Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller
|           +-14.3  Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge
|           +-18.0  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 0
|           +-18.1  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 1
|           +-18.2  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 2
|           +-18.3  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 3
|           +-18.4  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 4
|           +-18.5  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 5
|           +-18.6  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 6
|           \-18.7  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 7
</kbd>
</details>



---

### 评论 #8 — ROCmSupport (2020-12-17T04:32:35Z)

> 
> 
> It comes back with no results. So the Asus Z270 does not have PCIe Atomics. My CPU and GPU do it's just the motherboard now. One GPU works, the one that's in the main PCIe so I will have to work with that for now. Thanks.

Thanks @Q2Learn for the update.
Hope you are proceeding with detected GPU.
Thank you.

---
