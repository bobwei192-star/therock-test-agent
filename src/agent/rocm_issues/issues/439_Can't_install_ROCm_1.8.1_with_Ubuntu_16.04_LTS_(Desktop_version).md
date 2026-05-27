# Can't install ROCm 1.8.1 with Ubuntu 16.04 LTS (Desktop version)

> **Issue #439**
> **状态**: closed
> **创建时间**: 2018-06-20T20:43:37Z
> **更新时间**: 2019-01-08T18:53:15Z
> **关闭时间**: 2018-08-24T00:38:32Z
> **作者**: MoneroCrusher
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/439

## 描述

Hi there,

I have followed every step in https://github.com/RadeonOpenCompute/ROCm and yet when I come to the step where I have to type "rocminfo" it returns "rocminfo: command not found". uname -r also doesn't look like it's a ROCm kernel.."4.13.0-45-generic".
Setup:
Intel Celeron G3930
RX 550 hooked up via a riser into the 16x slot.

amdgpu-pro 18.20 works perfectly. But I need the ROCm kernel. Any suggestions?

edit: also, it was a fresh install of Ubuntu 16.04 LTS, so no old ROCm kernels were present at any moment...
sudo dkms status returns
amdgpu, 1.8-151, 4.13.0-45-generic, x86_64: installed
and yes, I added user to video group
also, cl info outputs Number Of platforms 0

---

## 评论 (19 条)

### 评论 #1 — Bengt (2018-06-21T00:22:40Z)

ROCMinfo gets installed under `/opt/rocm/bin/rocminfo`, so maybe try calling that directly.

---

### 评论 #2 — jlgreathouse (2018-07-03T20:39:50Z)

Is this an OEM-built system (e.g. from HP, Dell, etc.) or did you build it yourself? If the former, what model is it? If the latter, what motherboard are you using? What kind of PCIe riser is this? A passive connector, or are you trying to install the GPU through some kind of active lane-splitter?

Could you please include the outputs of the following commands?

- `lsmod | grep amdgpu`
- `lsmod | grep amdkfd`
- `groups`
- `lspci | grep VGA`
- `lspci -vvv`
- `lspci -tv`
- After a reboot: `dmesg | grep kfd`
- `/opt/rocm/bin/rocminfo`
- `/opt/rocm/opencl/bin/x86_64/clinfo`

Thank you.

---

### 评论 #3 — MoneroCrusher (2018-07-05T15:52:32Z)

@Bengt How do I call it?
@jlgreathouse It's a self-built system with a TB250 BTC-PRO Biostar motherboard. It's a normal PCIe Riser as used in usual cryptocurrency mining setups.
I will provide feedbacks of these commands this saturday. 
Thank you for the feedback.


---

### 评论 #4 — Bengt (2018-07-05T16:52:07Z)

@MoneroCrusher you should be able to call it just like that from a terminal. Here is an example output from my current machine:

```
bengt@Bengt-TR4:~$ /opt/rocm/bin/rocminfo
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
[...]
```

---

### 评论 #5 — odellus (2018-07-06T07:24:35Z)

I'm having the same issue, Ubuntu 16.04, newest ROCm. I had a working version until mine broke for some reason. Now it won't re-install. After autoremoving everything:

Is this my problem? Is there still not ROCm support for 4.15 and ubuntu just upgraded me and broke my ROCm install in the process?
* `uname -r`
```
4.15.0-24-generic
```
I'd really rather not have to uninstall `linux*-generic`.


Other requested info below:

* `lsmod | grep amdgpu`
```
amdgpu               2732032  52
chash                  16384  1 amdgpu
ttm                   106496  1 amdgpu
drm_kms_helper        172032  1 amdgpu
drm                   401408  7 amdgpu,ttm,drm_kms_helper
i2c_algo_bit           16384  2 igb,amdgpu
```
* `lsmod | grep amdkfd`
```
amdkfd                180224  1
amd_iommu_v2           20480  1 amdkfd
```
* `groups`
```
thomas adm dialout cdrom sudo dip video plugdev lpadmin sambashare
```
* `lspci | grep VGA`
```
09:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
```
* `lspci -vvv`
```
00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1450
	Subsystem: Advanced Micro Devices, Inc. [AMD] Device 1450
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Device 1451
	Subsystem: Advanced Micro Devices, Inc. [AMD] Device 1451
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin ? routed to IRQ 27
	Capabilities: <access denied>

00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1452
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:01.3 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1453 (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin ? routed to IRQ 28
	Bus: primary=00, secondary=01, subordinate=08, sec-latency=0
	I/O behind bridge: 0000f000-0000ffff
	Memory behind bridge: fe500000-fe7fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:02.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1452
	DeviceName:  Onboard IGD
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:03.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1452
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:03.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1453 (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin ? routed to IRQ 29
	Bus: primary=00, secondary=09, subordinate=09, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: fe900000-fe9fffff
	Prefetchable memory behind bridge: 00000000e0000000-00000000f01fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA+ MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:04.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1452
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:07.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1452
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:07.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1454 (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 30
	Bus: primary=00, secondary=0a, subordinate=0a, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fe200000-fe4fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1452
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1454 (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 32
	Bus: primary=00, secondary=0b, subordinate=0b, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fe800000-fe8fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 59)
	Subsystem: Gigabyte Technology Co., Ltd FCH SMBus Controller
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap- 66MHz+ UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Kernel driver in use: piix4_smbus
	Kernel modules: i2c_piix4, sp5100_tco

00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
	Subsystem: Gigabyte Technology Co., Ltd FCH LPC Bridge
	Control: I/O+ Mem+ BusMaster+ SpecCycle+ MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz+ UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0

00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1460
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1461
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1462
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1463
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Kernel driver in use: k10temp
	Kernel modules: k10temp

00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1464
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1465
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1466
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 1467
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

01:00.0 USB controller: Advanced Micro Devices, Inc. [AMD] Device 43d0 (rev 01) (prog-if 30 [XHCI])
	Subsystem: ASMedia Technology Inc. Device 1142
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 41
	Region 0: Memory at fe7a0000 (64-bit, non-prefetchable) [size=32K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

01:00.1 SATA controller: Advanced Micro Devices, Inc. [AMD] Device 43c8 (rev 01) (prog-if 01 [AHCI 1.0])
	Subsystem: ASMedia Technology Inc. Device 1062
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 45
	Region 5: Memory at fe780000 (32-bit, non-prefetchable) [size=128K]
	Expansion ROM at fe700000 [disabled] [size=512K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

01:00.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 43c6 (rev 01) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin C routed to IRQ 33
	Bus: primary=01, secondary=02, subordinate=08, sec-latency=0
	I/O behind bridge: 0000f000-0000ffff
	Memory behind bridge: fe500000-fe6fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

02:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 43c7 (rev 01) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 34
	Bus: primary=02, secondary=03, subordinate=03, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

02:01.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 43c7 (rev 01) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 35
	Bus: primary=02, secondary=04, subordinate=04, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

02:02.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 43c7 (rev 01) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 36
	Bus: primary=02, secondary=05, subordinate=05, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

02:03.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 43c7 (rev 01) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 38
	Bus: primary=02, secondary=06, subordinate=06, sec-latency=0
	I/O behind bridge: 0000f000-0000ffff
	Memory behind bridge: fe600000-fe6fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

02:04.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 43c7 (rev 01) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 39
	Bus: primary=02, secondary=07, subordinate=07, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

02:09.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 43c7 (rev 01) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 40
	Bus: primary=02, secondary=08, subordinate=08, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fe500000-fe5fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

06:00.0 Ethernet controller: Intel Corporation I211 Gigabit Network Connection (rev 03)
	Subsystem: Gigabyte Technology Co., Ltd I211 Gigabit Network Connection
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 37
	Region 0: Memory at fe600000 (32-bit, non-prefetchable) [size=128K]
	Region 2: I/O ports at f000 [size=32]
	Region 3: Memory at fe620000 (32-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: igb
	Kernel modules: igb

08:00.0 USB controller: ASMedia Technology Inc. Device 1343 (prog-if 30 [XHCI])
	Subsystem: Gigabyte Technology Co., Ltd Device 5007
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 42
	Region 0: Memory at fe500000 (64-bit, non-prefetchable) [size=32K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

09:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7) (prog-if 00 [VGA controller])
	Subsystem: Gigabyte Technology Co., Ltd Device 22fc
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 64
	Region 0: Memory at e0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at f0000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at e000 [size=256]
	Region 5: Memory at fe900000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

09:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
	Subsystem: Gigabyte Technology Co., Ltd Device aaf0
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 74
	Region 0: Memory at fe960000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

0a:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Device 145a
	Subsystem: Advanced Micro Devices, Inc. [AMD] Device 145a
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Capabilities: <access denied>

0a:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Device 1456
	Subsystem: Advanced Micro Devices, Inc. [AMD] Device 1456
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 70
	Region 2: Memory at fe300000 (32-bit, non-prefetchable) [size=1M]
	Region 5: Memory at fe400000 (32-bit, non-prefetchable) [size=8K]
	Capabilities: <access denied>
	Kernel driver in use: ccp
	Kernel modules: ccp

0a:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Device 145c (prog-if 30 [XHCI])
	Subsystem: Gigabyte Technology Co., Ltd Device 5007
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin C routed to IRQ 44
	Region 0: Memory at fe200000 (64-bit, non-prefetchable) [size=1M]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

0b:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Device 1455
	Subsystem: Advanced Micro Devices, Inc. [AMD] Device 1455
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Capabilities: <access denied>

0b:00.2 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 51) (prog-if 01 [AHCI 1.0])
	Subsystem: Gigabyte Technology Co., Ltd FCH SATA Controller [AHCI mode]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 47
	Region 5: Memory at fe808000 (32-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

0b:00.3 Audio device: Advanced Micro Devices, Inc. [AMD] Device 1457
	Subsystem: Gigabyte Technology Co., Ltd Device a0c3
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin C routed to IRQ 76
	Region 0: Memory at fe800000 (32-bit, non-prefetchable) [size=32K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel
```
* `lspci -tv`
```
-[0000:00]-+-00.0  Advanced Micro Devices, Inc. [AMD] Device 1450
           +-00.2  Advanced Micro Devices, Inc. [AMD] Device 1451
           +-01.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-01.3-[01-08]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 43d0
           |               +-00.1  Advanced Micro Devices, Inc. [AMD] Device 43c8
           |               \-00.2-[02-08]--+-00.0-[03]--
           |                               +-01.0-[04]--
           |                               +-02.0-[05]--
           |                               +-03.0-[06]----00.0  Intel Corporation I211 Gigabit Network Connection
           |                               +-04.0-[07]--
           |                               \-09.0-[08]----00.0  ASMedia Technology Inc. Device 1343
           +-02.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-03.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-03.1-[09]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-04.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-07.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-07.1-[0a]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 145a
           |            +-00.2  Advanced Micro Devices, Inc. [AMD] Device 1456
           |            \-00.3  Advanced Micro Devices, Inc. [AMD] Device 145c
           +-08.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-08.1-[0b]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 1455
           |            +-00.2  Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode]
           |            \-00.3  Advanced Micro Devices, Inc. [AMD] Device 1457
           +-14.0  Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller
           +-14.3  Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge
           +-18.0  Advanced Micro Devices, Inc. [AMD] Device 1460
           +-18.1  Advanced Micro Devices, Inc. [AMD] Device 1461
           +-18.2  Advanced Micro Devices, Inc. [AMD] Device 1462
           +-18.3  Advanced Micro Devices, Inc. [AMD] Device 1463
           +-18.4  Advanced Micro Devices, Inc. [AMD] Device 1464
           +-18.5  Advanced Micro Devices, Inc. [AMD] Device 1465
           +-18.6  Advanced Micro Devices, Inc. [AMD] Device 1466
           \-18.7  Advanced Micro Devices, Inc. [AMD] Device 1467
```
*  `dmesg | grep kfd`
```
[    1.007582] kfd kfd: Initialized module
[    1.762669] amdgpu 0000:09:00.0: kfd not supported on this ASIC
```
* `rocminfo`
```
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104
```
* `clinfo`
```
Number of platforms                               0
```


---

### 评论 #6 — odellus (2018-07-06T07:26:58Z)

okay. this is my problem:
https://github.com/RadeonOpenCompute/ROCm/issues/449

---

### 评论 #7 — jlgreathouse (2018-08-02T21:17:18Z)

Coming back to the original problem reported by @MoneroCrusher -- are you still planning to report the feedback from those commands?

---

### 评论 #8 — MoneroCrusher (2018-08-04T10:24:35Z)

@jlgreathouse  sorry I forgot about it. I got the issued fix by accepting that ROCm doesn't support RX 550 Lexa Pro based GPUs (yet?). Once I plugged in a Vega 56 or a Baffin based RX 550 GPU it worked. rocminfo still didn't work as a universal command. Had to call it from its location.

---

### 评论 #9 — MoneroCrusher (2018-12-28T08:28:50Z)

@jlgreathouse so the latest version seems to fix the issue with Lexa pro (at least partly).
So I have 12 Lexa Pro RX 550 in my system, this is the rocm_smi output:
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  10  21.0c   4.171W   214Mhz   300Mhz   18.82%   auto      0%
  5   21.0c   4.31W    214Mhz   300Mhz   18.82%   auto      0%
  3   21.0c   4.68W    214Mhz   300Mhz   18.82%   auto      0%
  1   25.0c   4.171W   214Mhz   300Mhz   18.82%   auto      0%
  8   27.0c   5.45W    214Mhz   300Mhz   18.82%   auto      0%
  11  23.0c   3.146W   214Mhz   300Mhz   18.82%   auto      0%
  6   24.0c   5.90W    214Mhz   300Mhz   18.82%   auto      0%
  4   23.0c   3.190W   214Mhz   300Mhz   18.82%   auto      0%
  2   21.0c   4.100W   214Mhz   300Mhz   18.82%   auto      0%
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A
  9   21.0c   4.141W   214Mhz   300Mhz   18.82%   auto      0%
  12  19.0c   6.23W    214Mhz   300Mhz   18.82%   auto      0%
  7   20.0c   4.195W   214Mhz   300Mhz   18.82%   auto      0%
================================================================================
====================           End of ROCm SMI Log          ====================
```
But when I do a clinfo, the output is much smaller, in fact it's only 1 device out of the 12 (and it's also wrongly named, it's supposed to be called gfx804, not gfx803).
```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (2783.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx803
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2
  Driver Version                                  2783.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         Device 699f
  Device Topology (AMD)                           PCI-E, 01:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1206MHz
  Graphics IP (AMD)                               8.3
```
I also tried to connect a Vega 56 into a random PCIe x1 slot and it showed up in clinfo. I then also put a Baffin (polaris 11) RX 550 in a random slot but that one didn't show up (in addition to the one Lexa Pro GPU already in the system).


Another strange occurence:
If the rocm output was made *before* the clinfo request, the rocm_smi output came in just instantly without lag.
However, after I did clinfo, the rocm_smi would have a significant lag, after displaying 3 GPUs and the GPU first shown after this lag then seems to show 0W usage instead of 4-5W usage (did that GPU crash?). 
**EDIT:** this problem only appears when using clinfo, rocminfo doesn't cause the "crash".
```
Like so:
GPU 0 is the iGPU, that's why nothing is shown in values.
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  10  21.0c   4.171W   214Mhz   300Mhz   18.82%   auto      0%
  5   21.0c   4.25W    214Mhz   300Mhz   18.82%   auto      0%
  3   21.0c   4.68W    214Mhz   300Mhz   18.82%   auto      0%
LAG LAG LAG 10s LAG LAG LAG
  1   26.0c   *0.0W*     214Mhz   300Mhz   20.0%    auto      0%
  8   26.0c   5.45W    214Mhz   300Mhz   18.82%   auto      0%
  11  23.0c   3.146W   214Mhz   300Mhz   18.82%   auto      0%
  6   24.0c   5.73W    214Mhz   300Mhz   18.82%   auto      0%
  4   23.0c   3.190W   214Mhz   300Mhz   18.82%   auto      0%
  2   21.0c   4.99W    214Mhz   300Mhz   18.82%   auto      0%
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A
  9   22.0c   4.131W   214Mhz   300Mhz   18.82%   auto      0%
  12  19.0c   6.22W    214Mhz   300Mhz   18.82%   auto      0%
  7   21.0c   4.187W   214Mhz   300Mhz   18.82%   auto      0%
================================================================================
====================           End of ROCm SMI Log          ====================
```
```
rocminfo output:
root@A12:/# /opt/rocm/bin/rocminfo
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
  Name:                    Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
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
  Compute Unit:            2
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    3968016KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    3968016KB
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
  Chip ID:                 27039
  Cacheline Size:          64
  Max Clock Frequency (MHz):1206
  BDFID:                   256
  Compute Unit:            8
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
      Size:                    2097152KB
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
```
Output with the new rocm-smi
========================        ROCm System Management Interface        ========================
================================================================================================
GPU   Temp   AvgPwr   SCLK    MCLK    PCLK           Fan     Perf    PwrCap   SCLK OD   MCLK OD  GPU%
0     N/A    N/A      N/A     N/A     N/A            0%      N/A     N/A      N/A       N/A      N/A
1     30c    N/A      214Mhz  300Mhz  N/A            18.82%  auto    36W      0%        0%       1%
10    21c    4.172W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
11    23c    3.146W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
12    18c    6.023W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    35W      0%        0%       0%
2     20c    4.1W     214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
3     21c    4.068W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
4     23c    3.19W    214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
5     21c    4.023W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
6     23c    5.072W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
7     20c    4.176W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
8     26c    5.045W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
9     21c    4.129W   214Mhz  300Mhz  2.5GT/s, x8    18.82%  auto    36W      0%        0%       0%
================================================================================================
========================               End of ROCm SMI Log              ========================

```
Rocm_bandwidth_test
```
root@A12:/opt/rocm/bin/rocm_bandwidth_test/build# ./rocm_bandwidth_test
......
....

          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
          Device: 1,  Device 699f

          Device Access

          D/D       0         1

          0         1         1

          1         1         1


          Device Numa Distance

          D/D       0         1

          0         0         N/A

          1         20        0


          Unidirectional peak bandwidth GB/s

          D/D       0           1

          0         N/A         0.318164

          1         0.341911    34.935936


          Bdirectional peak bandwidth GB/s

          D/D       0           1

          0         N/A         0.532567

          1         0.532834    N/A
```

So the one Lexa Pro GPU that was working (besides the Vega in random x1 PCIe slot) was the one in the x16 slot (connected via x1 riser).
I then removed that to see what opt/rocm/bin/rocminfo would yield and it was the following:
```
root@A12:/# /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104
```

---

### 评论 #10 — MoneroCrusher (2018-12-28T10:12:31Z)

Upon further research I think that this CPU/Chipset only supports atomics on the x16 slot (not sure about this, just speculation from my side) and since Vega can run without atomics, that's the reason why it's showing up.

Here's the rocm_bandwidth_test with Vega 56 in a x1 PCIe slot (without atomics) and the Lexa Pro RX 550 in the x16 slot connected via a x1 PCIe riser (presumably with atomics):
```
root@A12:/# /opt/rocm/bin/rocm_bandwidth_test/build/rocm_bandwidth_test
............
........

          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
          Device: 1,  Device 699f
          Device: 2,  Device 687f

          Device Access

          D/D       0         1         2

          0         1         1         1

          1         1         1         0

          2         1         0         1


          Device Numa Distance

          D/D       0         1         2

          0         0         N/A       N/A

          1         20        0         N/A

          2         20        N/A       0


          Unidirectional peak bandwidth GB/s

          D/D       0           1           2

          0         N/A         0.317793    0.439568

          1         0.342809    35.045983   N/A

          2         0.453472    N/A         169.844045


          Bdirectional peak bandwidth GB/s

          D/D       0           1           2

          0         N/A         0.530917    0.823345

          1         0.530163    N/A         N/A

          2         0.823482    N/A         N/A
```
```
root@A12:/# /opt/rocm/bin/rocm_bandwidth_test/build/rocm_bandwidth_test -v


          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
          Device: 1,  Device 699f
          Device: 2,  Device 687f

          Device Access

          D/D       0         1         2

          0         1         1         1

          1         1         1         0

          2         1         0         1


          Data Path Validation

          D/D       0           1           2

          0         N/A         FAIL        FAIL

          1         FAIL        PASS        N/A

          2         FAIL        N/A         PASS
```
```
root@A12:/# /opt/rocm/bin/rocm_bandwidth_test/build/rocm_bandwidth_test -t

          Device Index:                             0
            Device Type:                            CPU
              Allocatable Memory Size (KB):         3968024

          Device Index:                             1
            Device Type:                            GPU
              Allocatable Memory Size (KB):         2097152

          Device Index:                             2
            Device Type:                            GPU
              Allocatable Memory Size (KB):         8372224


          Device Access

          D/D       0         1         2

          0         1         1         1

          1         1         1         0

          2         1         0         1


          Device Numa Distance

          D/D       0         1         2

          0         0         N/A       N/A

          1         20        0         N/A

          2         20        N/A       0
```

I am looking to potentially transform my low-end GPU mining farm into a lightweight Deep Learning farm. Although as of now it's looking bad that is even possible with ROCm.
Now my question: If one were to "only" have numbers, nothing too complex as a dataset, would it make sense or would it be possible to run everything without atomics?

Or is there an alternative to use tensorflow without ROCm? I'm quite satisfied with the performance of AMDGPU Pro 16.60, I get 1/4 the performance of a Vega 56 mining cryptonight (both at max settings).

And here are the results if I put in the Lexa Pro card into the x16 slot directly:
```
root@A12:/# /opt/rocm/bin/rocm_bandwidth_test/build/rocm_bandwidth_test
............
........

          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
          Device: 1,  Device 67ff
          Device: 2,  Device 687f

          Device Access

          D/D       0         1         2

          0         1         1         1

          1         1         1         0

          2         1         0         1


          Device Numa Distance

          D/D       0         1         2

          0         0         N/A       N/A

          1         20        0         N/A

          2         20        N/A       0


          Unidirectional peak bandwidth GB/s

          D/D       0           1           2

          0         N/A         2.842922    0.439952

          1         2.977221    23.139299   N/A

          2         0.453805    N/A         153.071027


          Bdirectional peak bandwidth GB/s

          D/D       0           1           2

          0         N/A         4.226562    0.823884

          1         4.239721    N/A         N/A

          2         0.823873    N/A         N/A
```
So x1 in x16 slot vs. x16 slot direct is a 8x speedup. Question is, do I have the amount of data and to justify that speed, can my small RX 550 compute 4,5GB of data in 1 s? I would guess not, but I have little idea about DL.
If Deep Learning can be used with light weight data and where you have much less data generated than modern PCIe specs offer, then I think it would make sense to disable atomics requirement for polaris cards so everyone can participate. Not sure if that's possible, if it is, please do it.

---

### 评论 #11 — MoneroCrusher (2018-12-28T13:30:07Z)

Also: I can manually set each PCIe port to gen3 and boot/mine in that mode.

---

### 评论 #12 — jlgreathouse (2019-01-08T16:19:57Z)

Hi @MoneroCrusher 

Sorry about the delay in responding to this. It's difficult for me to keep up on posts in closed issues, since they're "marked as read" as soon as I read the email and then I never see them again unless I make a concerted effort to look for closed issues that were recently updated.

You're right, we added Polaris 12 ("Lexa") support [in ROCm 2.0](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#adds-support-for-vega-7nm-polaris-12-gpus). However, since Polaris 12 is a gfx8 GPU, it still maintains [the same limitations as other gfx8 GPUs with respect to PCIe atomics](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#not-supported).

Thus, I suspect you are right that the reason you are unable to see your GPUs is because you do not have PCIe atomics support for your large number of 1x slots. This is probably because these slots sit behind a PCIe switch that, to reduce costs, [was not designed to route/forward atomic operations](https://rocm.github.io/hardware.html#supported-cpus).

It's not just a question of PCIe 3.0, 2.0, or 1.0. PCIe atomics are an extension to PCIe 3.0 that may not be supported by all CPUs and switches. It's possible to have a system where you have many slots running x1, and each of them properly sees PCIe atomics. However, this requires the PCIe switch being used to split the PCIe connection to be able to properly forward atomics. Most of the switches we have tested that are used in cost-conscious systems like mining rigs do not have this capability and thus the x1 slots cannot be used with gfx8 GPUs.

As discussed in detail in [my posts in this other issue](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422836032), we currently do not offer support for gfx8 GPUs without PCIe atomics. It's not just a question of achievable performance. At this time, our gfx8 GPUs require PCIe atomics to function properly in the ROCm environment. Unfortunately, adding support to our hardware, software, and firmware to work with HSA queues and signals without atomics is not as simple as just "disabling atomics".

---

### 评论 #13 — MoneroCrusher (2019-01-08T16:57:41Z)

Hi @jlgreathouse 
Thanks for your input.

> Thus, I suspect you are right that the reason you are unable to see your GPUs is because you do not have PCIe atomics support for your large number of 1x slots. This is probably because these slots sit behind a PCIe switch that, to reduce costs, was not designed to route/forward atomic operations.

So this means that the x16 slot takes it's lanes from the CPU and that's the reason it has atomics / it supports my Lexa 550 (gfx 8)? If so, would you know if the x1 slots are "hardwired", or would there be a possibility to hack the motherboard BIOS and dynamically route the CPU lanes to the x1 slots individually?
If not, do you know of a atomics PCIE splitter that splits a x16 lane into 12 x1 lanes?
If not, is there any other way to resolve this besides getting another motherboard?

> At this time, our gfx8 GPUs require PCIe atomics to function properly in the ROCm environment. Unfortunately, adding support to our hardware, software, and firmware to work with HSA queues and signals without atomics is not as simple as just "disabling atomics".

So is it fundamentally different to disable the Atomics requirement for gfx 8 (in comparison to gfx 9)?
I think the ROCm team should make a decision here.
There are millions of polaris card out there that currently can't be used for Tensorflow (or is there an AMDGPU Pro implementation?). As a comparison GFX 9 GPUs are a much smaller subset and smaller amount of Exaflops. By enabling GFX 8 support you are opening the door for potentially many people like myself to explore the world of AI/ML/DL.
I really do hope that there is a way.

We can continue this on the open issue: https://github.com/RadeonOpenCompute/ROCm/issues/652

---

### 评论 #14 — jlgreathouse (2019-01-08T17:20:03Z)

Hi @MoneroCrusher 

Yes, it's likely that your x16 slot is connected directly to the CPU's PCIe root complex. Considering [Intel's ark entry for your CPU](https://ark.intel.com/products/97452/Intel-Celeron-Processor-G3930-2M-Cache-2-90-GHz-) claims that it has a total of 16 PCIe lanes, I would wager that all of your other lanes hang off a PCIe switch connected [through the PCH chipset](https://ark.intel.com/products/98086/Intel-B250-Chipset). The [B250 datasheet](https://www.intel.com/content/www/us/en/chipsets/200-series-chipset-pch-datasheet-vol-1.html?wapkw=200+series+chipset) only mentions base specification for PCIe 3.0, which means it does not support the PCIe-optional atomic operations.

I doubt you can make changes to the motherboard BIOS route those x1 slots directly into the CPU's PCIe controller. This sort of setup is related to whee the motherboard wires are actually routed. Based on the previous information, I don't believe you would be able to use atomics on any of these ports.

If you wanted to build your own board, we have had good luck with [Broadcom PEX switches](https://www.broadcom.com/products/pcie-switches-bridges/pcie-switches/), but that's obviously a bare chip and I don't have any splitter boards to recommend (since these chips are usually designed into motherboards or multi-GPU boards directly).

I give a much longer, more detailed description of why we currently require PCIe atomics on gfx8 in [the posts I linked previously](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422836032).

---

### 评论 #15 — MoneroCrusher (2019-01-08T17:41:06Z)

Hi @jlgreathouse 
That's too bad that the x1 slots are directly routed to the chipset. The broadcom splitters seem to be hilariously expensive as well :/

> I cannot guarantee that we will be able to get this capability working on gfx8 GPUs, so for now those devices still require PCIe atomics to work within the ROCm software stack.

Could you say as much, as you're looking into it, or can you guys internally decide about it (or have you already)? As I said, there are Exaflops waiting to be used for all kinds of stuff, especially with current cryptocurrency markets and Ethereum reducing their reward by 33% by next week.

The timing to get people interested in alternatives is very good, so finally instead of bidding against each other in an ever increasing electricity war out of the respective cryptocurrency, people would be able to apply their GPUs to do other important real world stuff.

---

### 评论 #16 — MoneroCrusher (2019-01-08T17:47:01Z)

Just looking at all the comments of this article shows that there's a huge demand for Tensorflow enabled for GFX 8.
https://medium.com/tensorflow/amd-rocm-gpu-support-for-tensorflow-33c78cc6a6cf

---

### 评论 #17 — jlgreathouse (2019-01-08T17:58:07Z)

Hi @MoneroCrusher 

I can say that it's on our "that would be nice to have" list. We have not completely discounted the possibility of offering atomic-free operation in gfx8. We understand the desire for this, as I mention [in this post](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422835753).

That said, I cannot make any public commitments for when, or if, AMD may enable such support.

We must trade off the development effort needed to enable this across multiple teams. For example: if this requires firmware changes in gfx8 GPUs, those teams may need to divert development time that is needed for bugfixes of current GPUs and feature development for future GPUs. Since firmware development may be shared across multiple projects, this could end up delaying gaming GPUs or causing feature loss for future non-ROCm workstation GPUs, etc. Unfortunately, these decisions are made in a larger ecosystem beyond just the ROCm team's desire to support these use-cases.

I am not trying to imply that we do not want to do this, nor that we may not in the future. I can only say that we have not yet made any public commitments to do so. I cannot offer any more details beyond that.

---

### 评论 #18 — MoneroCrusher (2019-01-08T18:08:18Z)

> equires firmware changes in gfx8 GPUs

What do you mean by that? The VBIOS itself would have to be adjusted to work with ROCm?

> current GPUs and feature development for future GPUs

The RX 5xx series is 2017, I'd consider them "current"? Official release date for my Lexa Pros is April 2017. Release date for my Baffins is October 2017.

> I cannot offer any more details beyond that.

Lastly, can you tell me if the implementation of Atomics-free ROCm for GFX 9 fundamentally differs from GFX 8? If not, then there could maybe be a community fork?

---

### 评论 #19 — jlgreathouse (2019-01-08T18:53:15Z)


> What do you mean by that? The VBIOS itself would have to be adjusted to work with ROCm?

There are other firmware besides our VBIOS. For example, you'll see that [this firmware commit](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amdgpu?id=0f22c8527439eaaf5c3fcf87b31c89445b6fa84d) updates the firmware for multiple hardware blocks on Vega 10 GPUs. This includes hardware units such as the MEC, RLC, and SDMA blocks which can consume AQL packets sent to the GPU from HSA queues. As mentioned in one of my previously linked posts, the way these units would would potentially need significant modification to work with ROCm/HSA user-level queues without requiring PCIe atomics. This may require firmware modifications.

> The RX 5xx series is 2017, I'd consider them "current"? Official release date for my Lexa Pros is April 2017. Release date for my Baffins is October 2017.

Note that I said "bugfixes of current GPUs". I am not saying that we do not make firmware changes on gfx8 GPUs to fix bugs. [Take this new firmware push](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amdgpu/polaris12_mec.bin?id=aeec108ba8ed8ced0694ea9137906c088b394edd), for example. Moving from "PCIe atomics required" to "optionally work without PCIe atomics" is an additional feature request, rather than a bug fix.

> Lastly, can you tell me if the implementation of Atomics-free ROCm for GFX 9 fundamentally differs from GFX 8? If not, then there could maybe be a community fork?

The on-chip engines are quite different between gfx8 and gfx9, so the implementation details that would need to change in these firmware blocks may be significantly different.

---
