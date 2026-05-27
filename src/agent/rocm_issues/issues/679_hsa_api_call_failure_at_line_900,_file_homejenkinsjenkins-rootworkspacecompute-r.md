# hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104

> **Issue #679**
> **状态**: closed
> **创建时间**: 2019-01-18T21:34:52Z
> **更新时间**: 2019-01-18T22:50:12Z
> **关闭时间**: 2019-01-18T22:50:04Z
> **作者**: kentenzer
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/679

## 描述

I saw similar errors reported and couldn't find the answer for my problem, help is appreciated. 

With `sudo /opt/rocm/bin/rocminfo`, I get the following output: `hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104`

As per other tickets I'm providing the following information:
-     uname -a
-     dkms status
-     lsmod | grep amdgpu
-     lsmod | grep amdkfd
-     groups
-     lspci | grep VGA
-     lspci -vvv
-     lspci -tv
-     lspci -n
-     After a reboot: dmesg

`uname -a`
`Linux test 4.19.0-041900-generic #201810221809 SMP Mon Oct 22 22:11:45 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux`

`dkms status`
`amdgpu, 2.0-89, 4.15.0-29-generic, x86_64: installed`

`lsmod | grep amdgpu`
`amdgpu               2985984  0
chash                  16384  1 amdgpu
gpu_sched              24576  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   106496  1 amdgpu
drm_kms_helper        176128  1 amdgpu
drm                   466944  4 gpu_sched,drm_kms_helper,amdgpu,ttm`

` lsmod | grep amdkfd`
`amdkfd                253952  1
amd_iommu_v2           20480  1 amdkfd`

`groups`
`test adm cdrom sudo dip video plugdev lpadmin sambashare docker`

` lspci | grep VGA`
`05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Tahiti PRO [Radeon HD 7950/8950 OEM / R9 280]`

` lspci -vvv`
`00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD/ATI] RD9x0/RX980 Host Bridge (rev 02)
	Subsystem: Micro-Star International Co., Ltd. [MSI] RD9x0/RX980 Host Bridge
	Control: I/O- Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
	NUMA node: 0
	Capabilities: <access denied>

00:04.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] RD890/RD9x0/RX980 PCI to PCI bridge (PCI Express GPP Port 0) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 25
	NUMA node: 0
	Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: fea00000-feafffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:05.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] RD890/RD9x0/RX980 PCI to PCI bridge (PCI Express GPP Port 1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 25
	NUMA node: 0
	Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
	I/O behind bridge: 0000d000-0000dfff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000d0000000-00000000d00fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:06.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] RD890/RD9x0/RX980 PCI to PCI bridge (PCI Express GPP Port 2) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 24
	NUMA node: 0
	Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fe900000-fe9fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:07.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] RD890/RD9x0/RX980 PCI to PCI bridge (PCI Express GPP Port 3) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 24
	NUMA node: 0
	Bus: primary=00, secondary=04, subordinate=04, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fe800000-fe8fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:09.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] RD890/RD9x0/RX980 PCI to PCI bridge (PCI Express GPP Port 4) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 24
	NUMA node: 0
	Bus: primary=00, secondary=05, subordinate=05, sec-latency=0
	I/O behind bridge: 0000c000-0000cfff
	Memory behind bridge: fe700000-fe7fffff
	Prefetchable memory behind bridge: 00000000c0000000-00000000cfffffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA+ MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:11.0 SATA controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 SATA Controller [IDE mode] (rev 40) (prog-if 01 [AHCI 1.0])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 SATA Controller [IDE mode]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz+ UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32
	Interrupt: pin A routed to IRQ 19
	NUMA node: 0
	Region 0: I/O ports at f090 [size=8]
	Region 1: I/O ports at f080 [size=4]
	Region 2: I/O ports at f070 [size=8]
	Region 3: I/O ports at f060 [size=4]
	Region 4: I/O ports at f050 [size=16]
	Region 5: Memory at feb0b000 (32-bit, non-prefetchable) [size=1K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

00:12.0 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller (prog-if 10 [OHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 18
	NUMA node: 0
	Region 0: Memory at feb0a000 (32-bit, non-prefetchable) [size=4K]
	Kernel driver in use: ohci-pci

00:12.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller (prog-if 20 [EHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV+ VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 17
	NUMA node: 0
	Region 0: Memory at feb09000 (32-bit, non-prefetchable) [size=256]
	Capabilities: <access denied>
	Kernel driver in use: ehci-pci

00:13.0 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller (prog-if 10 [OHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 18
	NUMA node: 0
	Region 0: Memory at feb08000 (32-bit, non-prefetchable) [size=4K]
	Kernel driver in use: ohci-pci

00:13.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller (prog-if 20 [EHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV+ VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 17
	NUMA node: 0
	Region 0: Memory at feb07000 (32-bit, non-prefetchable) [size=256]
	Capabilities: <access denied>
	Kernel driver in use: ehci-pci

00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 SMBus Controller (rev 42)
	Subsystem: Micro-Star International Co., Ltd. [MSI] SBx00 SMBus Controller
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap- 66MHz+ UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	NUMA node: 0
	Kernel driver in use: piix4_smbus
	Kernel modules: i2c_piix4, sp5100_tco

00:14.1 IDE interface: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 IDE Controller (rev 40) (prog-if 8a [Master SecP PriP])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 IDE Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz+ UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32
	Interrupt: pin B routed to IRQ 17
	NUMA node: 0
	Region 0: I/O ports at 01f0 [size=8]
	Region 1: I/O ports at 03f4
	Region 2: I/O ports at 0170 [size=8]
	Region 3: I/O ports at 0374
	Region 4: I/O ports at f000 [size=16]
	Kernel driver in use: pata_atiixp
	Kernel modules: pata_atiixp, pata_acpi, atiixp, ide_pci_generic

00:14.2 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 Azalia (Intel HDA) (rev 40)
	Subsystem: Micro-Star International Co., Ltd. [MSI] SBx00 Azalia (Intel HDA)
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=slow >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	NUMA node: 0
	Region 0: Memory at feb00000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 LPC host controller (rev 40)
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 LPC host controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle+ MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz+ UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	NUMA node: 0

00:14.4 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 PCI to PCI Bridge (rev 40) (prog-if 01 [Subtractive decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop+ ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 64
	NUMA node: 0
	Bus: primary=00, secondary=06, subordinate=06, sec-latency=64
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: fff00000-000fffff
	Secondary status: 66MHz- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-

00:14.5 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI2 Controller (prog-if 10 [OHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 USB OHCI2 Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin C routed to IRQ 18
	NUMA node: 0
	Region 0: Memory at feb06000 (32-bit, non-prefetchable) [size=4K]
	Kernel driver in use: ohci-pci

00:15.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] SB700/SB800/SB900 PCI to PCI bridge (PCIE port 0) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	NUMA node: 0
	Bus: primary=00, secondary=07, subordinate=07, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:15.1 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] SB700/SB800/SB900 PCI to PCI bridge (PCIE port 1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	NUMA node: 0
	Bus: primary=00, secondary=08, subordinate=08, sec-latency=0
	I/O behind bridge: 0000b000-0000bfff
	Memory behind bridge: fe600000-fe6fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.0 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller (prog-if 10 [OHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 18
	NUMA node: 0
	Region 0: Memory at feb05000 (32-bit, non-prefetchable) [size=4K]
	Kernel driver in use: ohci-pci

00:16.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller (prog-if 20 [EHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV+ VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 17
	NUMA node: 0
	Region 0: Memory at feb04000 (32-bit, non-prefetchable) [size=256]
	Capabilities: <access denied>
	Kernel driver in use: ehci-pci

00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor HyperTransport Configuration
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	NUMA node: 0
	Capabilities: <access denied>

00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor Address Map
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	NUMA node: 0

00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor DRAM Controller
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	NUMA node: 0

00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor Miscellaneous Control
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	NUMA node: 0
	Capabilities: <access denied>
	Kernel driver in use: k10temp
	Kernel modules: k10temp

00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor Link Control
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	NUMA node: 0

01:00.0 SATA controller: JMicron Technology Corp. JMB362 SATA Controller (rev 10) (prog-if 01 [AHCI 1.0])
	Subsystem: Micro-Star International Co., Ltd. [MSI] JMB362 SATA Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 34
	NUMA node: 0
	Region 0: I/O ports at e040 [size=8]
	Region 1: I/O ports at e030 [size=4]
	Region 2: I/O ports at e020 [size=8]
	Region 3: I/O ports at e010 [size=4]
	Region 4: I/O ports at e000 [size=16]
	Region 5: Memory at fea00000 (32-bit, non-prefetchable) [size=512]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)
	Subsystem: Micro-Star International Co., Ltd. [MSI] RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 32
	NUMA node: 0
	Region 0: I/O ports at d000 [size=256]
	Region 2: Memory at d0004000 (64-bit, prefetchable) [size=4K]
	Region 4: Memory at d0000000 (64-bit, prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: r8169
	Kernel modules: r8169

03:00.0 USB controller: NEC Corporation uPD720200 USB 3.0 Host Controller (rev 04) (prog-if 30 [XHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] uPD720200 USB 3.0 Host Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 26
	NUMA node: 0
	Region 0: Memory at fe900000 (64-bit, non-prefetchable) [size=8K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

04:00.0 USB controller: NEC Corporation uPD720200 USB 3.0 Host Controller (rev 04) (prog-if 30 [XHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] uPD720200 USB 3.0 Host Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 29
	NUMA node: 0
	Region 0: Memory at fe800000 (64-bit, non-prefetchable) [size=8K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Tahiti PRO [Radeon HD 7950/8950 OEM / R9 280] (prog-if 00 [VGA controller])
	Subsystem: Micro-Star International Co., Ltd. [MSI] Tahiti PRO [Radeon HD 7950/8950 OEM / R9 280]
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 35
	NUMA node: 0
	Region 0: Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at fe700000 (64-bit, non-prefetchable) [size=256K]
	Region 4: I/O ports at c000 [size=256]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel modules: radeon, amdgpu

05:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Tahiti HDMI Audio [Radeon HD 7870 XT / 7950/7970]
	Subsystem: Micro-Star International Co., Ltd. [MSI] Tahiti HDMI Audio [Radeon HD 7870 XT / 7950/7970]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 36
	NUMA node: 0
	Region 0: Memory at fe760000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

08:00.0 FireWire (IEEE 1394): VIA Technologies, Inc. VT6315 Series Firewire Controller (rev 01) (prog-if 10 [OHCI])
	Subsystem: Micro-Star International Co., Ltd. [MSI] VT6315 Series Firewire Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 17
	NUMA node: 0
	Region 0: Memory at fe600000 (64-bit, non-prefetchable) [size=2K]
	Region 2: I/O ports at b000 [size=256]
	Capabilities: <access denied>
	Kernel driver in use: firewire_ohci
	Kernel modules: firewire_ohci`
`lspci -tv`
`-[0000:00]-+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] RD9x0/RX980 Host Bridge
           +-04.0-[01]----00.0  JMicron Technology Corp. JMB362 SATA Controller
           +-05.0-[02]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           +-06.0-[03]----00.0  NEC Corporation uPD720200 USB 3.0 Host Controller
           +-07.0-[04]----00.0  NEC Corporation uPD720200 USB 3.0 Host Controller
           +-09.0-[05]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Tahiti PRO [Radeon HD 7950/8950 OEM / R9 280]
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Tahiti HDMI Audio [Radeon HD 7870 XT / 7950/7970]
           +-11.0  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 SATA Controller [IDE mode]
           +-12.0  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
           +-12.2  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
           +-13.0  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
           +-13.2  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
           +-14.0  Advanced Micro Devices, Inc. [AMD/ATI] SBx00 SMBus Controller
           +-14.1  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 IDE Controller
           +-14.2  Advanced Micro Devices, Inc. [AMD/ATI] SBx00 Azalia (Intel HDA)
           +-14.3  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 LPC host controller
           +-14.4-[06]--
           +-14.5  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI2 Controller
           +-15.0-[07]--
           +-15.1-[08]----00.0  VIA Technologies, Inc. VT6315 Series Firewire Controller
           +-16.0  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
           +-16.2  Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
           +-18.0  Advanced Micro Devices, Inc. [AMD] Family 10h Processor HyperTransport Configuration
           +-18.1  Advanced Micro Devices, Inc. [AMD] Family 10h Processor Address Map
           +-18.2  Advanced Micro Devices, Inc. [AMD] Family 10h Processor DRAM Controller
           +-18.3  Advanced Micro Devices, Inc. [AMD] Family 10h Processor Miscellaneous Control
           \-18.4  Advanced Micro Devices, Inc. [AMD] Family 10h Processor Link Control`

` lspci -n`
`00:00.0 0600: 1002:5a14 (rev 02)
00:04.0 0604: 1002:5a18
00:05.0 0604: 1002:5a19
00:06.0 0604: 1002:5a1a
00:07.0 0604: 1002:5a1b
00:09.0 0604: 1002:5a1c
00:11.0 0106: 1002:4390 (rev 40)
00:12.0 0c03: 1002:4397
00:12.2 0c03: 1002:4396
00:13.0 0c03: 1002:4397
00:13.2 0c03: 1002:4396
00:14.0 0c05: 1002:4385 (rev 42)
00:14.1 0101: 1002:439c (rev 40)
00:14.2 0403: 1002:4383 (rev 40)
00:14.3 0601: 1002:439d (rev 40)
00:14.4 0604: 1002:4384 (rev 40)
00:14.5 0c03: 1002:4399
00:15.0 0604: 1002:43a0
00:15.1 0604: 1002:43a1
00:16.0 0c03: 1002:4397
00:16.2 0c03: 1002:4396
00:18.0 0600: 1022:1200
00:18.1 0600: 1022:1201
00:18.2 0600: 1022:1202
00:18.3 0600: 1022:1203
00:18.4 0600: 1022:1204
01:00.0 0106: 197b:2362 (rev 10)
02:00.0 0200: 10ec:8168 (rev 06)
03:00.0 0c03: 1033:0194 (rev 04)
04:00.0 0c03: 1033:0194 (rev 04)
05:00.0 0300: 1002:679a
05:00.1 0403: 1002:aaa0
08:00.0 0c00: 1106:3403 (rev 01)`

`lspci -n`
`00:00.0 0600: 1002:5a14 (rev 02)
00:04.0 0604: 1002:5a18
00:05.0 0604: 1002:5a19
00:06.0 0604: 1002:5a1a
00:07.0 0604: 1002:5a1b
00:09.0 0604: 1002:5a1c
00:11.0 0106: 1002:4390 (rev 40)
00:12.0 0c03: 1002:4397
00:12.2 0c03: 1002:4396
00:13.0 0c03: 1002:4397
00:13.2 0c03: 1002:4396
00:14.0 0c05: 1002:4385 (rev 42)
00:14.1 0101: 1002:439c (rev 40)
00:14.2 0403: 1002:4383 (rev 40)
00:14.3 0601: 1002:439d (rev 40)
00:14.4 0604: 1002:4384 (rev 40)
00:14.5 0c03: 1002:4399
00:15.0 0604: 1002:43a0
00:15.1 0604: 1002:43a1
00:16.0 0c03: 1002:4397
00:16.2 0c03: 1002:4396
00:18.0 0600: 1022:1200
00:18.1 0600: 1022:1201
00:18.2 0600: 1022:1202
00:18.3 0600: 1022:1203
00:18.4 0600: 1022:1204
01:00.0 0106: 197b:2362 (rev 10)
02:00.0 0200: 10ec:8168 (rev 06)
03:00.0 0c03: 1033:0194 (rev 04)
04:00.0 0c03: 1033:0194 (rev 04)
05:00.0 0300: 1002:679a
05:00.1 0403: 1002:aaa0
08:00.0 0c00: 1106:3403 (rev 01)`

`dmesg`
`[    0.000000] Linux version 4.19.0-041900-generic (kernel@tangerine) (gcc version 8.2.0 (Ubuntu 8.2.0-7ubuntu1)) #201810221809 SMP Mon Oct 22 22:11:45 UTC 2018
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.19.0-041900-generic root=UUID=be47b0e5-ca1c-4d9a-8a97-0ced262d16a9 ro quiet splash vt.handoff=1
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: x87 FPU will use FXSAVE
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009ebff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009ec00-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000beed7fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000beed8000-0x00000000bef59fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000bef5a000-0x00000000bf03afff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000bf03b000-0x00000000bf042fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000bf043000-0x00000000bf2a8fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000bf2a9000-0x00000000bf2a9fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000bf2aa000-0x00000000bf2b9fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000bf2ba000-0x00000000bf2bafff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000bf2bb000-0x00000000bf2bbfff] usable
[    0.000000] BIOS-e820: [mem 0x00000000bf2bc000-0x00000000bf2c7fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000bf2c8000-0x00000000bf2eefff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000bf2ef000-0x00000000bf4f1fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000bf4f2000-0x00000000bf779fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000bf77a000-0x00000000bfeebfff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000bfeec000-0x00000000bfefffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec10000-0x00000000fec10fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec20000-0x00000000fec20fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed61000-0x00000000fed70fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed80000-0x00000000fed8ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fef00000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100001000-0x000000043fffffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] SMBIOS 2.7 present.
[    0.000000] DMI: MSI MS-7640/990FXA-GD80 (MS-7640), BIOS V11.13 10/09/2012
[    0.000000] tsc: Fast TSC calibration using PIT
[    0.000000] tsc: Detected 2800.371 MHz processor
[    0.004560] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.004563] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.010505] AGP: No AGP bridge found
[    0.010560] last_pfn = 0x440000 max_arch_pfn = 0x400000000
[    0.010565] MTRR default type: uncachable
[    0.010565] MTRR fixed ranges enabled:
[    0.010567]   00000-9FFFF write-back
[    0.010568]   A0000-BFFFF write-through
[    0.010569]   C0000-CFFFF write-protect
[    0.010569]   D0000-EBFFF uncachable
[    0.010570]   EC000-FFFFF write-protect
[    0.010571] MTRR variable ranges enabled:
[    0.010572]   0 base 000000000000 mask FFFF80000000 write-back
[    0.010574]   1 base 000080000000 mask FFFFC0000000 write-back
[    0.010575]   2 base 0000BFF00000 mask FFFFFFF00000 uncachable
[    0.010576]   3 disabled
[    0.010576]   4 disabled
[    0.010577]   5 disabled
[    0.010577]   6 disabled
[    0.010578]   7 disabled
[    0.010579] TOM2: 0000000440000000 aka 17408M
[    0.010839] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.010899] total RAM covered: 3071M
[    0.011338] Found optimal setting for mtrr clean up
[    0.011340]  gran_size: 64K 	chunk_size: 2M 	num_reg: 3  	lose cover RAM: 0G
[    0.011517] e820: update [mem 0xbff00000-0xffffffff] usable ==> reserved
[    0.011523] last_pfn = 0xbff00 max_arch_pfn = 0x400000000
[    0.015156] found SMP MP-table at [mem 0x000fce30-0x000fce3f] mapped at [(____ptrval____)]
[    0.074069] Scanning 1 areas for low memory corruption
[    0.074071] Base memory trampoline at [(____ptrval____)] 98000 size 24576
[    0.074075] Using GB pages for direct mapping
[    0.074077] BRK [0x102e01000, 0x102e01fff] PGTABLE
[    0.074079] BRK [0x102e02000, 0x102e02fff] PGTABLE
[    0.074080] BRK [0x102e03000, 0x102e03fff] PGTABLE
[    0.074109] BRK [0x102e04000, 0x102e04fff] PGTABLE
[    0.074160] BRK [0x102e05000, 0x102e05fff] PGTABLE
[    0.074178] BRK [0x102e06000, 0x102e06fff] PGTABLE
[    0.074225] BRK [0x102e07000, 0x102e07fff] PGTABLE
[    0.074321] BRK [0x102e08000, 0x102e08fff] PGTABLE
[    0.074324] BRK [0x102e09000, 0x102e09fff] PGTABLE
[    0.074354] BRK [0x102e0a000, 0x102e0afff] PGTABLE
[    0.074478] RAMDISK: [mem 0x3175d000-0x34ba5fff]
[    0.074488] ACPI: Early table checksum verification disabled
[    0.099703] ACPI: RSDP 0x00000000000F0450 000024 (v02 ALASKA)
[    0.099706] ACPI: XSDT 0x00000000BF03B068 000054 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.099713] ACPI: FACP 0x00000000BF041CE0 0000F4 (v04 ALASKA A M I    01072009 AMI  00010013)
[    0.099718] ACPI BIOS Warning (bug): Optional FADT field Pm2ControlBlock has valid Length but zero Address: 0x0000000000000000/0x1 (20180810/tbfadt-624)
[    0.099722] ACPI: DSDT 0x00000000BF03B150 006B8B (v02 ALASKA A M I    00000000 INTL 20051117)
[    0.099726] ACPI: FACS 0x00000000BF2C2F80 000040
[    0.099728] ACPI: APIC 0x00000000BF041DD8 00009E (v03 ALASKA A M I    01072009 AMI  00010013)
[    0.099731] ACPI: MCFG 0x00000000BF041E78 00003C (v01 ALASKA A M I    01072009 MSFT 00010013)
[    0.099734] ACPI: HPET 0x00000000BF041EB8 000038 (v01 ALASKA A M I    01072009 AMI  00000004)
[    0.099737] ACPI: SSDT 0x00000000BF041EF0 00022C (v01 AMD    POWERNOW 00000001 AMD  00000001)
[    0.099741] ACPI: BGRT 0x00000000BF042120 00003C (v00 ALASKA A M I    01072009 AMI  00010013)
[    0.099748] ACPI: Local APIC address 0xfee00000
[    0.099853] Scanning NUMA topology in Northbridge 24
[    0.099893] No NUMA configuration found
[    0.099894] Faking a node at [mem 0x0000000000000000-0x000000043fffffff]
[    0.099903] NODE_DATA(0) allocated [mem 0x43ffd3000-0x43fffdfff]
[    0.100245] Zone ranges:
[    0.100246]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.100248]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.100249]   Normal   [mem 0x0000000100000000-0x000000043fffffff]
[    0.100250]   Device   empty
[    0.100251] Movable zone start for each node
[    0.100255] Early memory node ranges
[    0.100256]   node   0: [mem 0x0000000000001000-0x000000000009dfff]
[    0.100257]   node   0: [mem 0x0000000000100000-0x00000000beed7fff]
[    0.100258]   node   0: [mem 0x00000000bf2a9000-0x00000000bf2a9fff]
[    0.100258]   node   0: [mem 0x00000000bf2bb000-0x00000000bf2bbfff]
[    0.100259]   node   0: [mem 0x00000000bf4f2000-0x00000000bf779fff]
[    0.100259]   node   0: [mem 0x00000000bfeec000-0x00000000bfefffff]
[    0.100260]   node   0: [mem 0x0000000100001000-0x000000043fffffff]
[    0.100334] Reserved but unavailable: 3822 pages
[    0.100336] Initmem setup node 0 [mem 0x0000000000001000-0x000000043fffffff]
[    0.100338] On node 0 totalpages: 4190482
[    0.100339]   DMA zone: 64 pages used for memmap
[    0.100340]   DMA zone: 21 pages reserved
[    0.100341]   DMA zone: 3997 pages, LIFO batch:0
[    0.100447]   DMA32 zone: 12166 pages used for memmap
[    0.100447]   DMA32 zone: 778614 pages, LIFO batch:63
[    0.125756]   Normal zone: 53248 pages used for memmap
[    0.125757]   Normal zone: 3407871 pages, LIFO batch:63
[    0.230894] ACPI: PM-Timer IO Port: 0x808
[    0.230896] ACPI: Local APIC address 0xfee00000
[    0.230904] ACPI: LAPIC_NMI (acpi_id[0xff] high edge lint[0x1])
[    0.230912] IOAPIC[0]: apic_id 2, version 33, address 0xfec00000, GSI 0-23
[    0.230915] IOAPIC[1]: apic_id 3, version 33, address 0xfec20000, GSI 24-55
[    0.230918] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.230919] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 low level)
[    0.230921] ACPI: IRQ0 used by override.
[    0.230922] ACPI: IRQ9 used by override.
[    0.230924] Using ACPI (MADT) for SMP configuration information
[    0.230925] ACPI: HPET id: 0x43538210 base: 0xfed00000
[    0.230931] smpboot: Allowing 8 CPUs, 7 hotplug CPUs
[    0.230963] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.230965] PM: Registered nosave memory: [mem 0x0009e000-0x0009efff]
[    0.230965] PM: Registered nosave memory: [mem 0x0009f000-0x0009ffff]
[    0.230966] PM: Registered nosave memory: [mem 0x000a0000-0x000dffff]
[    0.230967] PM: Registered nosave memory: [mem 0x000e0000-0x000fffff]
[    0.230968] PM: Registered nosave memory: [mem 0xbeed8000-0xbef59fff]
[    0.230969] PM: Registered nosave memory: [mem 0xbef5a000-0xbf03afff]
[    0.230969] PM: Registered nosave memory: [mem 0xbf03b000-0xbf042fff]
[    0.230970] PM: Registered nosave memory: [mem 0xbf043000-0xbf2a8fff]
[    0.230972] PM: Registered nosave memory: [mem 0xbf2aa000-0xbf2b9fff]
[    0.230972] PM: Registered nosave memory: [mem 0xbf2ba000-0xbf2bafff]
[    0.230974] PM: Registered nosave memory: [mem 0xbf2bc000-0xbf2c7fff]
[    0.230975] PM: Registered nosave memory: [mem 0xbf2c8000-0xbf2eefff]
[    0.230975] PM: Registered nosave memory: [mem 0xbf2ef000-0xbf4f1fff]
[    0.230977] PM: Registered nosave memory: [mem 0xbf77a000-0xbfeebfff]
[    0.230979] PM: Registered nosave memory: [mem 0xbff00000-0xfebfffff]
[    0.230979] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.230980] PM: Registered nosave memory: [mem 0xfec01000-0xfec0ffff]
[    0.230980] PM: Registered nosave memory: [mem 0xfec10000-0xfec10fff]
[    0.230981] PM: Registered nosave memory: [mem 0xfec11000-0xfec1ffff]
[    0.230982] PM: Registered nosave memory: [mem 0xfec20000-0xfec20fff]
[    0.230982] PM: Registered nosave memory: [mem 0xfec21000-0xfecfffff]
[    0.230983] PM: Registered nosave memory: [mem 0xfed00000-0xfed00fff]
[    0.230983] PM: Registered nosave memory: [mem 0xfed01000-0xfed60fff]
[    0.230984] PM: Registered nosave memory: [mem 0xfed61000-0xfed70fff]
[    0.230984] PM: Registered nosave memory: [mem 0xfed71000-0xfed7ffff]
[    0.230985] PM: Registered nosave memory: [mem 0xfed80000-0xfed8ffff]
[    0.230986] PM: Registered nosave memory: [mem 0xfed90000-0xfeefffff]
[    0.230986] PM: Registered nosave memory: [mem 0xfef00000-0xffffffff]
[    0.230987] PM: Registered nosave memory: [mem 0x100000000-0x100000fff]
[    0.230989] [mem 0xbff00000-0xfebfffff] available for PCI devices
[    0.230990] Booting paravirtualized kernel on bare hardware
[    0.230993] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.231004] random: get_random_bytes called from start_kernel+0x99/0x545 with crng_init=0
[    0.231013] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:8 nr_cpu_ids:8 nr_node_ids:1
[    0.232196] percpu: Embedded 47 pages/cpu @(____ptrval____) s155648 r8192 d28672 u262144
[    0.232204] pcpu-alloc: s155648 r8192 d28672 u262144 alloc=1*2097152
[    0.232205] pcpu-alloc: [0] 0 1 2 3 4 5 6 7 
[    0.232243] Built 1 zonelists, mobility grouping on.  Total pages: 4124983
[    0.232243] Policy zone: Normal
[    0.232245] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.19.0-041900-generic root=UUID=be47b0e5-ca1c-4d9a-8a97-0ced262d16a9 ro quiet splash vt.handoff=1
[    0.254204] AGP: Checking aperture...
[    0.260139] AGP: No AGP bridge found
[    0.260142] AGP: Node 0: aperture [bus addr 0xb4000000-0xb5ffffff] (32MB)
[    0.260143] Aperture pointing to e820 RAM. Ignoring.
[    0.260144] AGP: Your BIOS doesn't leave an aperture memory hole
[    0.260145] AGP: Please enable the IOMMU option in the BIOS setup
[    0.260145] AGP: This costs you 64MB of RAM
[    0.260149] AGP: Mapping aperture over RAM [mem 0xb4000000-0xb7ffffff] (65536KB)
[    0.260152] PM: Registered nosave memory: [mem 0xb4000000-0xb7ffffff]
[    0.365351] Memory: 16279908K/16761928K available (14348K kernel code, 2691K rwdata, 4272K rodata, 2440K init, 4984K bss, 482020K reserved, 0K cma-reserved)
[    0.365511] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=8, Nodes=1
[    0.365521] ftrace: allocating 41258 entries in 162 pages
[    0.381572] rcu: Hierarchical RCU implementation.
[    0.381574] rcu: 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=8.
[    0.381576] 	Tasks RCU enabled.
[    0.381576] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=8
[    0.385060] NR_IRQS: 524544, nr_irqs: 1032, preallocated irqs: 16
[    0.385381] spurious 8259A interrupt: IRQ7.
[    0.385398] Console: colour dummy device 80x25
[    0.385405] console [tty0] enabled
[    0.385427] ACPI: Core revision 20180810
[    0.385629] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484873504 ns
[    0.385640] hpet clockevent registered
[    0.385644] APIC: Switch to symmetric I/O mode setup
[    0.386101] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.405643] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x285d9f4c957, max_idle_ns: 440795290008 ns
[    0.405657] Calibrating delay loop (skipped), value calculated using timer frequency.. 5600.74 BogoMIPS (lpj=11201484)
[    0.405659] pid_max: default: 32768 minimum: 301
[    0.405705] Security Framework initialized
[    0.405707] Yama: becoming mindful.
[    0.405729] AppArmor: AppArmor initialized
[    0.411801] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes)
[    0.414870] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.414994] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.415090] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.415375] mce: CPU supports 6 MCE banks
[    0.415382] LVT offset 0 assigned for vector 0xf9
[    0.415385] Last level iTLB entries: 4KB 512, 2MB 16, 4MB 8
[    0.415386] Last level dTLB entries: 4KB 512, 2MB 128, 4MB 64, 1GB 0
[    0.415388] Spectre V2 : Mitigation: Full AMD retpoline
[    0.415389] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    0.429645] smpboot: CPU0: AMD Sempron(tm) 145 Processor (family: 0x10, model: 0x6, stepping: 0x3)
[    0.429645] Performance Events: AMD PMU driver.
[    0.429645] ... version:                0
[    0.429645] ... bit width:              48
[    0.429645] ... generic registers:      4
[    0.429645] ... value mask:             0000ffffffffffff
[    0.429645] ... max period:             00007fffffffffff
[    0.429645] ... fixed-purpose events:   0
[    0.429645] ... event mask:             000000000000000f
[    0.429645] rcu: Hierarchical SRCU implementation.
[    0.429645] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.429645] smp: Bringing up secondary CPUs ...
[    0.429645] smp: Brought up 1 node, 1 CPU
[    0.429645] smpboot: Max logical packages: 8
[    0.429645] smpboot: Total of 1 processors activated (5600.74 BogoMIPS)
[    0.429645] devtmpfs: initialized
[    0.429645] x86/mm: Memory block size: 128MB
[    0.429645] PM: Registering ACPI NVS region [mem 0xbeed8000-0xbef59fff] (532480 bytes)
[    0.429645] PM: Registering ACPI NVS region [mem 0xbf2ba000-0xbf2bafff] (4096 bytes)
[    0.429645] PM: Registering ACPI NVS region [mem 0xbf2bc000-0xbf2c7fff] (49152 bytes)
[    0.429645] PM: Registering ACPI NVS region [mem 0xbf2ef000-0xbf4f1fff] (2109440 bytes)
[    0.429645] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.429645] futex hash table entries: 2048 (order: 5, 131072 bytes)
[    0.429645] pinctrl core: initialized pinctrl subsystem
[    0.429645] RTC time: 20:53:18, date: 01/18/19
[    0.430354] NET: Registered protocol family 16
[    0.430458] audit: initializing netlink subsys (disabled)
[    0.430612] cpuidle: using governor ladder
[    0.430613] cpuidle: using governor menu
[    0.430619] node 0 link 0: io port [b000, ffff]
[    0.430620] TOM: 00000000c0000000 aka 3072M
[    0.430622] Fam 10h mmconf [mem 0xe0000000-0xefffffff]
[    0.430623] node 0 link 0: mmio [c0000000, fef0ffff] ==> [c0000000, dfffffff] and [f0000000, fef0ffff]
[    0.430627] TOM2: 0000000440000000 aka 17408M
[    0.430628] bus: [bus 00-1f] on node 0 link 0
[    0.430629] bus: 00 [io  0x0000-0xffff]
[    0.430629] bus: 00 [mem 0xc0000000-0xdfffffff]
[    0.430630] bus: 00 [mem 0xf0000000-0xffffffff]
[    0.430631] bus: 00 [mem 0x440000000-0xfcffffffff]
[    0.430684] ACPI: bus type PCI registered
[    0.430686] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.430753] PCI: MMCONFIG for domain 0000 [bus 00-ff] at [mem 0xe0000000-0xefffffff] (base 0xe0000000)
[    0.430756] PCI: not using MMCONFIG
[    0.430757] PCI: Using configuration type 1 for base access
[    0.430758] PCI: Using configuration type 1 for extended access
[    0.432221] audit: type=2000 audit(1547844798.044:1): state=initialized audit_enabled=0 res=1
[    0.432318] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.432319] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.432567] ACPI: Added _OSI(Module Device)
[    0.432568] ACPI: Added _OSI(Processor Device)
[    0.432568] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.432569] ACPI: Added _OSI(Processor Aggregator Device)
[    0.432570] ACPI: Added _OSI(Linux-Dell-Video)
[    0.432571] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    0.438398] ACPI: 2 ACPI AML tables successfully acquired and loaded
[    0.440253] ACPI: Interpreter enabled
[    0.440274] ACPI: (supports S0 S1 S3 S4 S5)
[    0.440275] ACPI: Using IOAPIC for interrupt routing
[    0.440479] PCI: MMCONFIG for domain 0000 [bus 00-ff] at [mem 0xe0000000-0xefffffff] (base 0xe0000000)
[    0.440534] PCI: MMCONFIG at [mem 0xe0000000-0xefffffff] reserved in ACPI motherboard resources
[    0.440549] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.440753] ACPI: Enabled 10 GPEs in block 00 to 1F
[    0.449670] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.449676] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.449681] acpi PNP0A08:00: _OSC failed (AE_NOT_FOUND); disabling ASPM
[    0.450168] PCI host bridge to bus 0000:00
[    0.450171] pci_bus 0000:00: root bus resource [io  0x0000-0x03af window]
[    0.450172] pci_bus 0000:00: root bus resource [io  0x03e0-0x0cf7 window]
[    0.450174] pci_bus 0000:00: root bus resource [io  0x03b0-0x03df window]
[    0.450175] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.450176] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.450177] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000dffff window]
[    0.450179] pci_bus 0000:00: root bus resource [mem 0xc0000000-0xffffffff window]
[    0.450180] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.450189] pci 0000:00:00.0: [1002:5a14] type 00 class 0x060000
[    0.450329] pci 0000:00:04.0: [1002:5a18] type 01 class 0x060400
[    0.450344] pci 0000:00:04.0: enabling Extended Tags
[    0.450363] pci 0000:00:04.0: PME# supported from D0 D3hot D3cold
[    0.450465] pci 0000:00:05.0: [1002:5a19] type 01 class 0x060400
[    0.450479] pci 0000:00:05.0: enabling Extended Tags
[    0.450497] pci 0000:00:05.0: PME# supported from D0 D3hot D3cold
[    0.450597] pci 0000:00:06.0: [1002:5a1a] type 01 class 0x060400
[    0.450611] pci 0000:00:06.0: enabling Extended Tags
[    0.450629] pci 0000:00:06.0: PME# supported from D0 D3hot D3cold
[    0.450726] pci 0000:00:07.0: [1002:5a1b] type 01 class 0x060400
[    0.450740] pci 0000:00:07.0: enabling Extended Tags
[    0.450758] pci 0000:00:07.0: PME# supported from D0 D3hot D3cold
[    0.450860] pci 0000:00:09.0: [1002:5a1c] type 01 class 0x060400
[    0.450874] pci 0000:00:09.0: enabling Extended Tags
[    0.450892] pci 0000:00:09.0: PME# supported from D0 D3hot D3cold
[    0.450997] pci 0000:00:11.0: [1002:4390] type 00 class 0x01018f
[    0.451013] pci 0000:00:11.0: reg 0x10: [io  0xf090-0xf097]
[    0.451019] pci 0000:00:11.0: reg 0x14: [io  0xf080-0xf083]
[    0.451026] pci 0000:00:11.0: reg 0x18: [io  0xf070-0xf077]
[    0.451032] pci 0000:00:11.0: reg 0x1c: [io  0xf060-0xf063]
[    0.451039] pci 0000:00:11.0: reg 0x20: [io  0xf050-0xf05f]
[    0.451045] pci 0000:00:11.0: reg 0x24: [mem 0xfeb0b000-0xfeb0b3ff]
[    0.451061] pci 0000:00:11.0: set SATA to AHCI mode
[    0.451172] pci 0000:00:12.0: [1002:4397] type 00 class 0x0c0310
[    0.451185] pci 0000:00:12.0: reg 0x10: [mem 0xfeb0a000-0xfeb0afff]
[    0.451321] pci 0000:00:12.2: [1002:4396] type 00 class 0x0c0320
[    0.451336] pci 0000:00:12.2: reg 0x10: [mem 0xfeb09000-0xfeb090ff]
[    0.451393] pci 0000:00:12.2: supports D1 D2
[    0.451394] pci 0000:00:12.2: PME# supported from D0 D1 D2 D3hot
[    0.451495] pci 0000:00:13.0: [1002:4397] type 00 class 0x0c0310
[    0.451508] pci 0000:00:13.0: reg 0x10: [mem 0xfeb08000-0xfeb08fff]
[    0.451646] pci 0000:00:13.2: [1002:4396] type 00 class 0x0c0320
[    0.451661] pci 0000:00:13.2: reg 0x10: [mem 0xfeb07000-0xfeb070ff]
[    0.451717] pci 0000:00:13.2: supports D1 D2
[    0.451718] pci 0000:00:13.2: PME# supported from D0 D1 D2 D3hot
[    0.451821] pci 0000:00:14.0: [1002:4385] type 00 class 0x0c0500
[    0.451962] pci 0000:00:14.1: [1002:439c] type 00 class 0x01018a
[    0.451974] pci 0000:00:14.1: reg 0x10: [io  0xf040-0xf047]
[    0.451981] pci 0000:00:14.1: reg 0x14: [io  0xf030-0xf033]
[    0.451987] pci 0000:00:14.1: reg 0x18: [io  0xf020-0xf027]
[    0.451994] pci 0000:00:14.1: reg 0x1c: [io  0xf010-0xf013]
[    0.452000] pci 0000:00:14.1: reg 0x20: [io  0xf000-0xf00f]
[    0.452014] pci 0000:00:14.1: legacy IDE quirk: reg 0x10: [io  0x01f0-0x01f7]
[    0.452015] pci 0000:00:14.1: legacy IDE quirk: reg 0x14: [io  0x03f6]
[    0.452017] pci 0000:00:14.1: legacy IDE quirk: reg 0x18: [io  0x0170-0x0177]
[    0.452018] pci 0000:00:14.1: legacy IDE quirk: reg 0x1c: [io  0x0376]
[    0.452113] pci 0000:00:14.2: [1002:4383] type 00 class 0x040300
[    0.452130] pci 0000:00:14.2: reg 0x10: [mem 0xfeb00000-0xfeb03fff 64bit]
[    0.452178] pci 0000:00:14.2: PME# supported from D0 D3hot D3cold
[    0.452274] pci 0000:00:14.3: [1002:439d] type 00 class 0x060100
[    0.452416] pci 0000:00:14.4: [1002:4384] type 01 class 0x060401
[    0.452535] pci 0000:00:14.5: [1002:4399] type 00 class 0x0c0310
[    0.452548] pci 0000:00:14.5: reg 0x10: [mem 0xfeb06000-0xfeb06fff]
[    0.452684] pci 0000:00:15.0: [1002:43a0] type 01 class 0x060400
[    0.452712] pci 0000:00:15.0: enabling Extended Tags
[    0.452743] pci 0000:00:15.0: supports D1 D2
[    0.452851] pci 0000:00:15.1: [1002:43a1] type 01 class 0x060400
[    0.452879] pci 0000:00:15.1: enabling Extended Tags
[    0.452910] pci 0000:00:15.1: supports D1 D2
[    0.453017] pci 0000:00:16.0: [1002:4397] type 00 class 0x0c0310
[    0.453030] pci 0000:00:16.0: reg 0x10: [mem 0xfeb05000-0xfeb05fff]
[    0.453166] pci 0000:00:16.2: [1002:4396] type 00 class 0x0c0320
[    0.453181] pci 0000:00:16.2: reg 0x10: [mem 0xfeb04000-0xfeb040ff]
[    0.453238] pci 0000:00:16.2: supports D1 D2
[    0.453239] pci 0000:00:16.2: PME# supported from D0 D1 D2 D3hot
[    0.453340] pci 0000:00:18.0: [1022:1200] type 00 class 0x060000
[    0.453431] pci 0000:00:18.1: [1022:1201] type 00 class 0x060000
[    0.453520] pci 0000:00:18.2: [1022:1202] type 00 class 0x060000
[    0.453610] pci 0000:00:18.3: [1022:1203] type 00 class 0x060000
[    0.453705] pci 0000:00:18.4: [1022:1204] type 00 class 0x060000
[    0.453858] pci 0000:01:00.0: [197b:2362] type 00 class 0x010185
[    0.453887] pci 0000:01:00.0: reg 0x10: [io  0xe040-0xe047]
[    0.453896] pci 0000:01:00.0: reg 0x14: [io  0xe030-0xe033]
[    0.453906] pci 0000:01:00.0: reg 0x18: [io  0xe020-0xe027]
[    0.453915] pci 0000:01:00.0: reg 0x1c: [io  0xe010-0xe013]
[    0.453924] pci 0000:01:00.0: reg 0x20: [io  0xe000-0xe00f]
[    0.453934] pci 0000:01:00.0: reg 0x24: [mem 0xfea00000-0xfea001ff]
[    0.453986] pci 0000:01:00.0: PME# supported from D3hot
[    0.454006] pci 0000:01:00.0: 2.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s x1 link at 0000:00:04.0 (capable of 7.876 Gb/s with 8 GT/s x1 link)
[    0.454069] pci 0000:00:04.0: PCI bridge to [bus 01]
[    0.454071] pci 0000:00:04.0:   bridge window [io  0xe000-0xefff]
[    0.454073] pci 0000:00:04.0:   bridge window [mem 0xfea00000-0xfeafffff]
[    0.454109] pci 0000:02:00.0: [10ec:8168] type 00 class 0x020000
[    0.454129] pci 0000:02:00.0: reg 0x10: [io  0xd000-0xd0ff]
[    0.454147] pci 0000:02:00.0: reg 0x18: [mem 0xd0004000-0xd0004fff 64bit pref]
[    0.454158] pci 0000:02:00.0: reg 0x20: [mem 0xd0000000-0xd0003fff 64bit pref]
[    0.454222] pci 0000:02:00.0: supports D1 D2
[    0.454223] pci 0000:02:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.454255] pci 0000:02:00.0: 2.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s x1 link at 0000:00:05.0 (capable of 7.876 Gb/s with 8 GT/s x1 link)
[    0.454310] pci 0000:00:05.0: PCI bridge to [bus 02]
[    0.454313] pci 0000:00:05.0:   bridge window [io  0xd000-0xdfff]
[    0.454316] pci 0000:00:05.0:   bridge window [mem 0xd0000000-0xd00fffff 64bit pref]
[    0.454351] pci 0000:03:00.0: [1033:0194] type 00 class 0x0c0330
[    0.454372] pci 0000:03:00.0: reg 0x10: [mem 0xfe900000-0xfe901fff 64bit]
[    0.454447] pci 0000:03:00.0: PME# supported from D0 D3hot D3cold
[    0.454474] pci 0000:03:00.0: 4.000 Gb/s available PCIe bandwidth, limited by 5 GT/s x1 link at 0000:00:06.0 (capable of 7.876 Gb/s with 8 GT/s x1 link)
[    0.454526] pci 0000:00:06.0: PCI bridge to [bus 03]
[    0.454529] pci 0000:00:06.0:   bridge window [mem 0xfe900000-0xfe9fffff]
[    0.454563] pci 0000:04:00.0: [1033:0194] type 00 class 0x0c0330
[    0.454583] pci 0000:04:00.0: reg 0x10: [mem 0xfe800000-0xfe801fff 64bit]
[    0.454661] pci 0000:04:00.0: PME# supported from D0 D3hot D3cold
[    0.454688] pci 0000:04:00.0: 4.000 Gb/s available PCIe bandwidth, limited by 5 GT/s x1 link at 0000:00:07.0 (capable of 7.876 Gb/s with 8 GT/s x1 link)
[    0.454738] pci 0000:00:07.0: PCI bridge to [bus 04]
[    0.454741] pci 0000:00:07.0:   bridge window [mem 0xfe800000-0xfe8fffff]
[    0.454777] pci 0000:05:00.0: [1002:679a] type 00 class 0x030000
[    0.454804] pci 0000:05:00.0: reg 0x10: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.454816] pci 0000:05:00.0: reg 0x18: [mem 0xfe700000-0xfe73ffff 64bit]
[    0.454824] pci 0000:05:00.0: reg 0x20: [io  0xc000-0xc0ff]
[    0.454838] pci 0000:05:00.0: reg 0x30: [mem 0xfe740000-0xfe75ffff pref]
[    0.454844] pci 0000:05:00.0: enabling Extended Tags
[    0.454904] pci 0000:05:00.0: supports D1 D2
[    0.454905] pci 0000:05:00.0: PME# supported from D1 D2 D3hot
[    0.454943] pci 0000:05:00.0: 2.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s x1 link at 0000:00:09.0 (capable of 126.016 Gb/s with 8 GT/s x16 link)
[    0.454987] pci 0000:05:00.1: [1002:aaa0] type 00 class 0x040300
[    0.455011] pci 0000:05:00.1: reg 0x10: [mem 0xfe760000-0xfe763fff 64bit]
[    0.455049] pci 0000:05:00.1: enabling Extended Tags
[    0.455098] pci 0000:05:00.1: supports D1 D2
[    0.455177] pci 0000:00:09.0: PCI bridge to [bus 05]
[    0.455180] pci 0000:00:09.0:   bridge window [io  0xc000-0xcfff]
[    0.455182] pci 0000:00:09.0:   bridge window [mem 0xfe700000-0xfe7fffff]
[    0.455184] pci 0000:00:09.0:   bridge window [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.455193] pci_bus 0000:06: extended config space not accessible
[    0.455242] pci 0000:00:14.4: PCI bridge to [bus 06] (subtractive decode)
[    0.455248] pci 0000:00:14.4:   bridge window [io  0x0000-0x03af window] (subtractive decode)
[    0.455249] pci 0000:00:14.4:   bridge window [io  0x03e0-0x0cf7 window] (subtractive decode)
[    0.455251] pci 0000:00:14.4:   bridge window [io  0x03b0-0x03df window] (subtractive decode)
[    0.455252] pci 0000:00:14.4:   bridge window [io  0x0d00-0xffff window] (subtractive decode)
[    0.455253] pci 0000:00:14.4:   bridge window [mem 0x000a0000-0x000bffff window] (subtractive decode)
[    0.455254] pci 0000:00:14.4:   bridge window [mem 0x000c0000-0x000dffff window] (subtractive decode)
[    0.455256] pci 0000:00:14.4:   bridge window [mem 0xc0000000-0xffffffff window] (subtractive decode)
[    0.455290] pci 0000:00:15.0: PCI bridge to [bus 07]
[    0.455343] pci 0000:08:00.0: [1106:3403] type 00 class 0x0c0010
[    0.455373] pci 0000:08:00.0: reg 0x10: [mem 0xfe600000-0xfe6007ff 64bit]
[    0.455383] pci 0000:08:00.0: reg 0x18: [io  0xb000-0xb0ff]
[    0.455478] pci 0000:08:00.0: supports D2
[    0.455479] pci 0000:08:00.0: PME# supported from D2 D3hot D3cold
[    0.455509] pci 0000:08:00.0: 2.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s x1 link at 0000:00:15.1 (capable of 7.876 Gb/s with 8 GT/s x1 link)
[    0.465682] pci 0000:00:15.1: PCI bridge to [bus 08]
[    0.465689] pci 0000:00:15.1:   bridge window [io  0xb000-0xbfff]
[    0.465691] pci 0000:00:15.1:   bridge window [mem 0xfe600000-0xfe6fffff]
[    0.466303] ACPI: PCI Interrupt Link [LNKA] (IRQs 4 7 10 11 14 15) *0
[    0.466400] ACPI: PCI Interrupt Link [LNKB] (IRQs 4 7 10 11 14 15) *0
[    0.466499] ACPI: PCI Interrupt Link [LNKC] (IRQs 4 7 10 11 14 15) *0
[    0.466594] ACPI: PCI Interrupt Link [LNKD] (IRQs 4 7 10 11 14 15) *0
[    0.466675] ACPI: PCI Interrupt Link [LNKE] (IRQs 4 7 10 11 14 15) *0
[    0.466739] ACPI: PCI Interrupt Link [LNKF] (IRQs 4 7 10 11 14 15) *0
[    0.466801] ACPI: PCI Interrupt Link [LNKG] (IRQs 4 7 10 11 14 15) *0
[    0.466864] ACPI: PCI Interrupt Link [LNKH] (IRQs 4 7 10 11 14 15) *0
[    0.467078] pci 0000:05:00.0: vgaarb: setting as boot VGA device
[    0.467079] pci 0000:05:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.467081] pci 0000:05:00.0: vgaarb: bridge control possible
[    0.467081] vgaarb: loaded
[    0.467287] SCSI subsystem initialized
[    0.467337] libata version 3.00 loaded.
[    0.467354] ACPI: bus type USB registered
[    0.467368] usbcore: registered new interface driver usbfs
[    0.467375] usbcore: registered new interface driver hub
[    0.467385] usbcore: registered new device driver usb
[    0.467411] pps_core: LinuxPPS API ver. 1 registered
[    0.467412] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.467414] PTP clock support registered
[    0.467450] EDAC MC: Ver: 3.0.0
[    0.467601] PCI: Using ACPI for IRQ routing
[    0.473460] PCI: pci_cache_line_size set to 64 bytes
[    0.473524] e820: reserve RAM buffer [mem 0x0009ec00-0x0009ffff]
[    0.473525] e820: reserve RAM buffer [mem 0xbeed8000-0xbfffffff]
[    0.473527] e820: reserve RAM buffer [mem 0xbf2aa000-0xbfffffff]
[    0.473528] e820: reserve RAM buffer [mem 0xbf2bc000-0xbfffffff]
[    0.473529] e820: reserve RAM buffer [mem 0xbf77a000-0xbfffffff]
[    0.473530] e820: reserve RAM buffer [mem 0xbff00000-0xbfffffff]
[    0.473632] NetLabel: Initializing
[    0.473633] NetLabel:  domain hash size = 128
[    0.473634] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.473655] NetLabel:  unlabeled traffic allowed by default
[    0.473771] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0
[    0.473774] hpet0: 3 comparators, 32-bit 14.318180 MHz counter
[    0.475808] clocksource: Switched to clocksource tsc-early
[    0.487563] VFS: Disk quotas dquot_6.6.0
[    0.487585] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.487724] AppArmor: AppArmor Filesystem Enabled
[    0.487756] pnp: PnP ACPI init
[    0.487930] system 00:00: [mem 0xe0000000-0xefffffff] has been reserved
[    0.487936] system 00:00: Plug and Play ACPI device, IDs PNP0c01 (active)
[    0.488304] system 00:01: [io  0x040b] has been reserved
[    0.488306] system 00:01: [io  0x04d6] has been reserved
[    0.488307] system 00:01: [io  0x0c00-0x0c01] has been reserved
[    0.488308] system 00:01: [io  0x0c14] has been reserved
[    0.488309] system 00:01: [io  0x0c50-0x0c51] has been reserved
[    0.488311] system 00:01: [io  0x0c52] has been reserved
[    0.488312] system 00:01: [io  0x0c6c] has been reserved
[    0.488313] system 00:01: [io  0x0c6f] has been reserved
[    0.488314] system 00:01: [io  0x0cd0-0x0cd1] has been reserved
[    0.488315] system 00:01: [io  0x0cd2-0x0cd3] has been reserved
[    0.488316] system 00:01: [io  0x0cd4-0x0cd5] has been reserved
[    0.488318] system 00:01: [io  0x0cd6-0x0cd7] has been reserved
[    0.488319] system 00:01: [io  0x0cd8-0x0cdf] has been reserved
[    0.488320] system 00:01: [io  0x0800-0x089f] has been reserved
[    0.488321] system 00:01: [io  0x0b20-0x0b3f] has been reserved
[    0.488323] system 00:01: [io  0x0900-0x090f] has been reserved
[    0.488324] system 00:01: [io  0x0910-0x091f] has been reserved
[    0.488326] system 00:01: [io  0xfe00-0xfefe] has been reserved
[    0.488327] system 00:01: [io  0x0485-0x0486] has been reserved
[    0.488333] system 00:01: [mem 0xfec00000-0xfec00fff] could not be reserved
[    0.488334] system 00:01: [mem 0xfee00000-0xfee00fff] has been reserved
[    0.488336] system 00:01: [mem 0xfed80000-0xfed8ffff] has been reserved
[    0.488337] system 00:01: [mem 0xfed61000-0xfed70fff] has been reserved
[    0.488339] system 00:01: [mem 0xfec10000-0xfec10fff] has been reserved
[    0.488340] system 00:01: [mem 0xfed00000-0xfed00fff] could not be reserved
[    0.488342] system 00:01: [mem 0xff800000-0xffffffff] has been reserved
[    0.488345] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.488551] system 00:02: [io  0x0a00-0x0a0f] has been reserved
[    0.488554] system 00:02: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.488622] pnp 00:03: Plug and Play ACPI device, IDs PNP0f03 PNP0f13 (active)
[    0.488812] pnp 00:04: [dma 0 disabled]
[    0.488858] pnp 00:04: Plug and Play ACPI device, IDs PNP0501 (active)
[    0.488885] pnp 00:05: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.488950] system 00:06: [io  0x04d0-0x04d1] has been reserved
[    0.488953] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.488997] system 00:07: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.489042] pnp 00:08: Plug and Play ACPI device, IDs PNP0303 PNP030b (active)
[    0.489200] system 00:09: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.489353] system 00:0a: [mem 0xfec20000-0xfec200ff] could not be reserved
[    0.489357] system 00:0a: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.489510] pnp: PnP ACPI: found 11 devices
[    0.495239] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.495277] pci 0000:00:04.0: PCI bridge to [bus 01]
[    0.495279] pci 0000:00:04.0:   bridge window [io  0xe000-0xefff]
[    0.495282] pci 0000:00:04.0:   bridge window [mem 0xfea00000-0xfeafffff]
[    0.495285] pci 0000:00:05.0: PCI bridge to [bus 02]
[    0.495286] pci 0000:00:05.0:   bridge window [io  0xd000-0xdfff]
[    0.495289] pci 0000:00:05.0:   bridge window [mem 0xd0000000-0xd00fffff 64bit pref]
[    0.495291] pci 0000:00:06.0: PCI bridge to [bus 03]
[    0.495293] pci 0000:00:06.0:   bridge window [mem 0xfe900000-0xfe9fffff]
[    0.495296] pci 0000:00:07.0: PCI bridge to [bus 04]
[    0.495298] pci 0000:00:07.0:   bridge window [mem 0xfe800000-0xfe8fffff]
[    0.495302] pci 0000:00:09.0: PCI bridge to [bus 05]
[    0.495303] pci 0000:00:09.0:   bridge window [io  0xc000-0xcfff]
[    0.495305] pci 0000:00:09.0:   bridge window [mem 0xfe700000-0xfe7fffff]
[    0.495306] pci 0000:00:09.0:   bridge window [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.495309] pci 0000:00:14.4: PCI bridge to [bus 06]
[    0.495317] pci 0000:00:15.0: PCI bridge to [bus 07]
[    0.495324] pci 0000:00:15.1: PCI bridge to [bus 08]
[    0.495326] pci 0000:00:15.1:   bridge window [io  0xb000-0xbfff]
[    0.495329] pci 0000:00:15.1:   bridge window [mem 0xfe600000-0xfe6fffff]
[    0.495335] pci_bus 0000:00: resource 4 [io  0x0000-0x03af window]
[    0.495336] pci_bus 0000:00: resource 5 [io  0x03e0-0x0cf7 window]
[    0.495337] pci_bus 0000:00: resource 6 [io  0x03b0-0x03df window]
[    0.495338] pci_bus 0000:00: resource 7 [io  0x0d00-0xffff window]
[    0.495340] pci_bus 0000:00: resource 8 [mem 0x000a0000-0x000bffff window]
[    0.495341] pci_bus 0000:00: resource 9 [mem 0x000c0000-0x000dffff window]
[    0.495342] pci_bus 0000:00: resource 10 [mem 0xc0000000-0xffffffff window]
[    0.495343] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    0.495345] pci_bus 0000:01: resource 1 [mem 0xfea00000-0xfeafffff]
[    0.495346] pci_bus 0000:02: resource 0 [io  0xd000-0xdfff]
[    0.495347] pci_bus 0000:02: resource 2 [mem 0xd0000000-0xd00fffff 64bit pref]
[    0.495348] pci_bus 0000:03: resource 1 [mem 0xfe900000-0xfe9fffff]
[    0.495350] pci_bus 0000:04: resource 1 [mem 0xfe800000-0xfe8fffff]
[    0.495351] pci_bus 0000:05: resource 0 [io  0xc000-0xcfff]
[    0.495352] pci_bus 0000:05: resource 1 [mem 0xfe700000-0xfe7fffff]
[    0.495353] pci_bus 0000:05: resource 2 [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.495355] pci_bus 0000:06: resource 4 [io  0x0000-0x03af window]
[    0.495356] pci_bus 0000:06: resource 5 [io  0x03e0-0x0cf7 window]
[    0.495357] pci_bus 0000:06: resource 6 [io  0x03b0-0x03df window]
[    0.495358] pci_bus 0000:06: resource 7 [io  0x0d00-0xffff window]
[    0.495360] pci_bus 0000:06: resource 8 [mem 0x000a0000-0x000bffff window]
[    0.495361] pci_bus 0000:06: resource 9 [mem 0x000c0000-0x000dffff window]
[    0.495362] pci_bus 0000:06: resource 10 [mem 0xc0000000-0xffffffff window]
[    0.495364] pci_bus 0000:08: resource 0 [io  0xb000-0xbfff]
[    0.495365] pci_bus 0000:08: resource 1 [mem 0xfe600000-0xfe6fffff]
[    0.495474] NET: Registered protocol family 2
[    0.495684] tcp_listen_portaddr_hash hash table entries: 8192 (order: 5, 131072 bytes)
[    0.495774] TCP established hash table entries: 131072 (order: 8, 1048576 bytes)
[    0.496149] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.496526] TCP: Hash tables configured (established 131072 bind 65536)
[    0.496625] UDP hash table entries: 8192 (order: 6, 262144 bytes)
[    0.496744] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes)
[    0.496980] NET: Registered protocol family 1
[    0.496986] NET: Registered protocol family 44
[    0.587629] pci 0000:00:12.0: quirk_usb_early_handoff+0x0/0x6c4 took 88489 usecs
[    0.675625] pci 0000:00:13.0: quirk_usb_early_handoff+0x0/0x6c4 took 85789 usecs
[    0.763616] pci 0000:00:14.5: quirk_usb_early_handoff+0x0/0x6c4 took 85775 usecs
[    0.851611] pci 0000:00:16.0: quirk_usb_early_handoff+0x0/0x6c4 took 85913 usecs
[    0.852003] pci 0000:05:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.852014] pci 0000:05:00.1: Linked as a consumer to 0000:05:00.0
[    0.852023] PCI: CLS 64 bytes, default 64
[    0.852109] Unpacking initramfs...
[    1.691574] Freeing initrd memory: 53540K
[    1.692038] PCI-DMA: Disabling AGP.
[    1.692113] PCI-DMA: aperture base @ b4000000 size 65536 KB
[    1.692114] PCI-DMA: using GART IOMMU.
[    1.692115] PCI-DMA: Reserving 64MB of IOMMU area in the AGP aperture
[    1.694230] LVT offset 1 assigned for vector 0x400
[    1.694242] LVT offset 1 assigned
[    1.694268] perf: AMD IBS detected (0x0000001f)
[    1.694336] Scanning for low memory corruption every 60 seconds
[    1.695014] Initialise system trusted keyrings
[    1.695024] Key type blacklist registered
[    1.695085] workingset: timestamp_bits=36 max_order=22 bucket_order=0
[    1.696491] zbud: loaded
[    1.696922] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    1.697144] fuse init (API version 7.27)
[    1.697202] pstore: using deflate compression
[    1.698281] Key type asymmetric registered
[    1.698282] Asymmetric key parser 'x509' registered
[    1.698292] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 243)
[    1.698320] io scheduler noop registered
[    1.698321] io scheduler deadline registered
[    1.698354] io scheduler cfq registered (default)
[    1.699011] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    1.699065] vesafb: mode is 1366x768x32, linelength=5632, pages=0
[    1.699066] vesafb: scrolling: redraw
[    1.699067] vesafb: Truecolor: size=0:8:8:8, shift=0:16:8:0
[    1.699082] vesafb: framebuffer at 0xc0000000, mapped to 0x(____ptrval____), using 4224k, total 4224k
[    1.833499] Console: switching to colour frame buffer device 170x48
[    1.967540] fb0: VESA VGA frame buffer device
[    1.967657] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
[    1.967673] ACPI: Power Button [PWRB]
[    1.967706] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input1
[    1.967713] ACPI: Power Button [PWRF]
[    1.967943] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    1.988437] 00:04: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    2.008925] serial8250: ttyS1 at I/O 0x2f8 (irq = 3, base_baud = 115200) is a 16550A
[    2.010405] Linux agpgart interface v0.103
[    2.011931] loop: module loaded
[    2.012337] libphy: Fixed MDIO Bus: probed
[    2.012337] tun: Universal TUN/TAP device driver, 1.6
[    2.012367] PPP generic driver version 2.4.2
[    2.012404] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    2.012407] ehci-pci: EHCI PCI platform driver
[    2.012546] QUIRK: Enable AMD PLL fix
[    2.012568] ehci-pci 0000:00:12.2: EHCI Host Controller
[    2.012574] ehci-pci 0000:00:12.2: new USB bus registered, assigned bus number 1
[    2.012579] ehci-pci 0000:00:12.2: applying AMD SB700/SB800/Hudson-2/3 EHCI dummy qh workaround
[    2.012586] ehci-pci 0000:00:12.2: debug port 1
[    2.012630] ehci-pci 0000:00:12.2: irq 17, io mem 0xfeb09000
[    2.025682] ehci-pci 0000:00:12.2: USB 2.0 started, EHCI 1.00
[    2.025749] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 4.19
[    2.025751] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.025753] usb usb1: Product: EHCI Host Controller
[    2.025754] usb usb1: Manufacturer: Linux 4.19.0-041900-generic ehci_hcd
[    2.025755] usb usb1: SerialNumber: 0000:00:12.2
[    2.025873] hub 1-0:1.0: USB hub found
[    2.025879] hub 1-0:1.0: 5 ports detected
[    2.026166] ehci-pci 0000:00:13.2: EHCI Host Controller
[    2.026172] ehci-pci 0000:00:13.2: new USB bus registered, assigned bus number 2
[    2.026175] ehci-pci 0000:00:13.2: applying AMD SB700/SB800/Hudson-2/3 EHCI dummy qh workaround
[    2.026182] ehci-pci 0000:00:13.2: debug port 1
[    2.026211] ehci-pci 0000:00:13.2: irq 17, io mem 0xfeb07000
[    2.041682] ehci-pci 0000:00:13.2: USB 2.0 started, EHCI 1.00
[    2.041755] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 4.19
[    2.041757] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.041758] usb usb2: Product: EHCI Host Controller
[    2.041759] usb usb2: Manufacturer: Linux 4.19.0-041900-generic ehci_hcd
[    2.041760] usb usb2: SerialNumber: 0000:00:13.2
[    2.041871] hub 2-0:1.0: USB hub found
[    2.041877] hub 2-0:1.0: 5 ports detected
[    2.042122] ehci-pci 0000:00:16.2: EHCI Host Controller
[    2.042127] ehci-pci 0000:00:16.2: new USB bus registered, assigned bus number 3
[    2.042130] ehci-pci 0000:00:16.2: applying AMD SB700/SB800/Hudson-2/3 EHCI dummy qh workaround
[    2.042137] ehci-pci 0000:00:16.2: debug port 1
[    2.042165] ehci-pci 0000:00:16.2: irq 17, io mem 0xfeb04000
[    2.057683] ehci-pci 0000:00:16.2: USB 2.0 started, EHCI 1.00
[    2.057753] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 4.19
[    2.057754] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.057756] usb usb3: Product: EHCI Host Controller
[    2.057757] usb usb3: Manufacturer: Linux 4.19.0-041900-generic ehci_hcd
[    2.057758] usb usb3: SerialNumber: 0000:00:16.2
[    2.057871] hub 3-0:1.0: USB hub found
[    2.057876] hub 3-0:1.0: 4 ports detected
[    2.058004] ehci-platform: EHCI generic platform driver
[    2.058018] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    2.058020] ohci-pci: OHCI PCI platform driver
[    2.058155] ohci-pci 0000:00:12.0: OHCI PCI host controller
[    2.058159] ohci-pci 0000:00:12.0: new USB bus registered, assigned bus number 4
[    2.058184] ohci-pci 0000:00:12.0: irq 18, io mem 0xfeb0a000
[    2.121733] usb usb4: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 4.19
[    2.121735] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.121737] usb usb4: Product: OHCI PCI host controller
[    2.121738] usb usb4: Manufacturer: Linux 4.19.0-041900-generic ohci_hcd
[    2.121738] usb usb4: SerialNumber: 0000:00:12.0
[    2.121859] hub 4-0:1.0: USB hub found
[    2.121865] hub 4-0:1.0: 5 ports detected
[    2.122104] ohci-pci 0000:00:13.0: OHCI PCI host controller
[    2.122109] ohci-pci 0000:00:13.0: new USB bus registered, assigned bus number 5
[    2.122129] ohci-pci 0000:00:13.0: irq 18, io mem 0xfeb08000
[    2.185735] usb usb5: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 4.19
[    2.185737] usb usb5: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.185738] usb usb5: Product: OHCI PCI host controller
[    2.185739] usb usb5: Manufacturer: Linux 4.19.0-041900-generic ohci_hcd
[    2.185740] usb usb5: SerialNumber: 0000:00:13.0
[    2.185857] hub 5-0:1.0: USB hub found
[    2.185864] hub 5-0:1.0: 5 ports detected
[    2.186095] ohci-pci 0000:00:14.5: OHCI PCI host controller
[    2.186100] ohci-pci 0000:00:14.5: new USB bus registered, assigned bus number 6
[    2.186120] ohci-pci 0000:00:14.5: irq 18, io mem 0xfeb06000
[    2.249734] usb usb6: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 4.19
[    2.249737] usb usb6: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.249738] usb usb6: Product: OHCI PCI host controller
[    2.249739] usb usb6: Manufacturer: Linux 4.19.0-041900-generic ohci_hcd
[    2.249740] usb usb6: SerialNumber: 0000:00:14.5
[    2.249861] hub 6-0:1.0: USB hub found
[    2.249868] hub 6-0:1.0: 2 ports detected
[    2.250087] ohci-pci 0000:00:16.0: OHCI PCI host controller
[    2.250092] ohci-pci 0000:00:16.0: new USB bus registered, assigned bus number 7
[    2.250116] ohci-pci 0000:00:16.0: irq 18, io mem 0xfeb05000
[    2.313755] usb usb7: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 4.19
[    2.313756] usb usb7: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.313757] usb usb7: Product: OHCI PCI host controller
[    2.313758] usb usb7: Manufacturer: Linux 4.19.0-041900-generic ohci_hcd
[    2.313759] usb usb7: SerialNumber: 0000:00:16.0
[    2.313878] hub 7-0:1.0: USB hub found
[    2.313885] hub 7-0:1.0: 4 ports detected
[    2.314007] ohci-platform: OHCI generic platform driver
[    2.314021] uhci_hcd: USB Universal Host Controller Interface driver
[    2.314164] xhci_hcd 0000:03:00.0: xHCI Host Controller
[    2.314169] xhci_hcd 0000:03:00.0: new USB bus registered, assigned bus number 8
[    2.314264] xhci_hcd 0000:03:00.0: hcc params 0x014042cb hci version 0x96 quirks 0x0000000000000004
[    2.314398] usb usb8: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 4.19
[    2.314399] usb usb8: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.314400] usb usb8: Product: xHCI Host Controller
[    2.314401] usb usb8: Manufacturer: Linux 4.19.0-041900-generic xhci-hcd
[    2.314402] usb usb8: SerialNumber: 0000:03:00.0
[    2.314472] hub 8-0:1.0: USB hub found
[    2.314478] hub 8-0:1.0: 2 ports detected
[    2.314559] xhci_hcd 0000:03:00.0: xHCI Host Controller
[    2.314562] xhci_hcd 0000:03:00.0: new USB bus registered, assigned bus number 9
[    2.314564] xhci_hcd 0000:03:00.0: Host supports USB 3.0  SuperSpeed
[    2.317796] usb usb9: We don't know the algorithms for LPM for this host, disabling LPM.
[    2.317811] usb usb9: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 4.19
[    2.317812] usb usb9: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.317813] usb usb9: Product: xHCI Host Controller
[    2.317814] usb usb9: Manufacturer: Linux 4.19.0-041900-generic xhci-hcd
[    2.317815] usb usb9: SerialNumber: 0000:03:00.0
[    2.317882] hub 9-0:1.0: USB hub found
[    2.317889] hub 9-0:1.0: 2 ports detected
[    2.318019] xhci_hcd 0000:04:00.0: xHCI Host Controller
[    2.318022] xhci_hcd 0000:04:00.0: new USB bus registered, assigned bus number 10
[    2.318108] xhci_hcd 0000:04:00.0: hcc params 0x014042cb hci version 0x96 quirks 0x0000000000000004
[    2.318225] usb usb10: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 4.19
[    2.318226] usb usb10: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.318227] usb usb10: Product: xHCI Host Controller
[    2.318228] usb usb10: Manufacturer: Linux 4.19.0-041900-generic xhci-hcd
[    2.318229] usb usb10: SerialNumber: 0000:04:00.0
[    2.318296] hub 10-0:1.0: USB hub found
[    2.318302] hub 10-0:1.0: 2 ports detected
[    2.318379] xhci_hcd 0000:04:00.0: xHCI Host Controller
[    2.318382] xhci_hcd 0000:04:00.0: new USB bus registered, assigned bus number 11
[    2.318384] xhci_hcd 0000:04:00.0: Host supports USB 3.0  SuperSpeed
[    2.321579] usb usb11: We don't know the algorithms for LPM for this host, disabling LPM.
[    2.321594] usb usb11: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 4.19
[    2.321595] usb usb11: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.321596] usb usb11: Product: xHCI Host Controller
[    2.321597] usb usb11: Manufacturer: Linux 4.19.0-041900-generic xhci-hcd
[    2.321598] usb usb11: SerialNumber: 0000:04:00.0
[    2.321674] hub 11-0:1.0: USB hub found
[    2.321680] hub 11-0:1.0: 2 ports detected
[    2.321794] i8042: PNP: PS/2 Controller [PNP0303:PS2K,PNP0f03:PS2M] at 0x60,0x64 irq 1,12
[    2.322121] serio: i8042 KBD port at 0x60,0x64 irq 1
[    2.322124] serio: i8042 AUX port at 0x60,0x64 irq 12
[    2.322172] mousedev: PS/2 mouse device common for all mice
[    2.322263] rtc_cmos 00:05: RTC can wake from S4
[    2.322360] rtc_cmos 00:05: registered as rtc0
[    2.322376] rtc_cmos 00:05: alarms up to one month, y3k, 114 bytes nvram, hpet irqs
[    2.322381] i2c /dev entries driver
[    2.322440] device-mapper: uevent: version 1.0.3
[    2.322493] device-mapper: ioctl: 4.39.0-ioctl (2018-04-03) initialised: dm-devel@redhat.com
[    2.322507] ledtrig-cpu: registered to indicate activity on CPUs
[    2.322741] NET: Registered protocol family 10
[    2.326301] Segment Routing with IPv6
[    2.326332] NET: Registered protocol family 17
[    2.326367] Key type dns_resolver registered
[    2.326500] RAS: Correctable Errors collector initialized.
[    2.326546] microcode: CPU0: patch_level=0x010000c8
[    2.326570] microcode: Microcode Update Driver: v2.2.
[    2.326583] sched_clock: Marking stable (2325359140, 292721)->(2455801984, -130150123)
[    2.326687] registered taskstats version 1
[    2.326704] Loading compiled-in X.509 certificates
[    2.327774] Loaded X.509 cert 'Build time autogenerated kernel key: 83e62c06a0d7768f6d28a01db6bbca2d8bf8fa26'
[    2.327793] zswap: loaded using pool lzo/zbud
[    2.330996] Key type big_key registered
[    2.331000] Key type trusted registered
[    2.332494] Key type encrypted registered
[    2.332497] AppArmor: AppArmor sha1 policy hashing enabled
[    2.332505] ima: No TPM chip found, activating TPM-bypass!
[    2.332510] ima: Allocated hash algorithm: sha1
[    2.332524] evm: Initialising EVM extended attributes:
[    2.332525] evm: security.selinux
[    2.332525] evm: security.SMACK64
[    2.332526] evm: security.SMACK64EXEC
[    2.332526] evm: security.SMACK64TRANSMUTE
[    2.332527] evm: security.SMACK64MMAP
[    2.332527] evm: security.apparmor
[    2.332527] evm: security.ima
[    2.332528] evm: security.capability
[    2.332528] evm: HMAC attrs: 0x1
[    2.332920]   Magic number: 3:782:902
[    2.332943] usb usb2-port3: hash matches
[    2.333073] rtc_cmos 00:05: setting system clock to 2019-01-18 20:53:20 UTC (1547844800)
[    2.333222] acpi_cpufreq: overriding BIOS provided _PSD data
[    2.336631] Freeing unused decrypted memory: 2040K
[    2.338706] Freeing unused kernel image memory: 2440K
[    2.341742] Write protecting the kernel read-only data: 22528k
[    2.342593] Freeing unused kernel image memory: 2008K
[    2.343347] Freeing unused kernel image memory: 1872K
[    2.355025] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    2.355037] Run /init as init process
[    2.377680] usb 2-3: new high-speed USB device number 2 using ehci-pci
[    2.535024] usb 2-3: New USB device found, idVendor=048d, idProduct=1234, bcdDevice= 2.00
[    2.535026] usb 2-3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    2.535028] usb 2-3: Product: Disk 2.0
[    2.535029] usb 2-3: Manufacturer: USB
[    2.535030] usb 2-3: SerialNumber: 9207025296156524183
[    2.564017] libphy: r8169: probed
[    2.564329] r8169 0000:02:00.0 eth0: RTL8168evl/8111evl, 8c:89:a5:e4:92:3e, XID 2c900800, IRQ 33
[    2.564331] r8169 0000:02:00.0 eth0: jumbo features [frames: 9200 bytes, tx checksumming: ko]
[    2.564339] ahci 0000:00:11.0: version 3.0
[    2.564539] ahci 0000:00:11.0: AHCI 0001.0200 32 slots 4 ports 6 Gbps 0xf impl SATA mode
[    2.564541] ahci 0000:00:11.0: flags: 64bit ncq sntf ilck pm led clo pmp pio slum part 
[    2.569204] scsi host0: ahci
[    2.576001] scsi host1: ahci
[    2.577725] scsi host2: ahci
[    2.581200] scsi host3: ahci
[    2.581271] ata1: SATA max UDMA/133 abar m1024@0xfeb0b000 port 0xfeb0b100 irq 19
[    2.581273] ata2: SATA max UDMA/133 abar m1024@0xfeb0b000 port 0xfeb0b180 irq 19
[    2.581275] ata3: SATA max UDMA/133 abar m1024@0xfeb0b000 port 0xfeb0b200 irq 19
[    2.581277] ata4: SATA max UDMA/133 abar m1024@0xfeb0b000 port 0xfeb0b280 irq 19
[    2.581586] ahci 0000:01:00.0: AHCI 0001.0100 32 slots 2 ports 3 Gbps 0x3 impl SATA mode
[    2.581588] ahci 0000:01:00.0: flags: 64bit ncq pm led clo pmp pio slum part 
[    2.585175] piix4_smbus 0000:00:14.0: SMBus Host Controller at 0xb00, revision 0
[    2.585182] piix4_smbus 0000:00:14.0: Using register 0x2c for SMBus port selection
[    2.585396] piix4_smbus 0000:00:14.0: Auxiliary SMBus Host Controller at 0xb20
[    2.585467] scsi host4: ahci
[    2.589337] scsi host5: ahci
[    2.589403] ata5: SATA max UDMA/133 abar m512@0xfea00000 port 0xfea00100 irq 34
[    2.589406] ata6: SATA max UDMA/133 abar m512@0xfea00000 port 0xfea00180 irq 34
[    2.591032] scsi host6: pata_atiixp
[    2.593554] scsi host7: pata_atiixp
[    2.593614] ata7: PATA max UDMA/100 cmd 0x1f0 ctl 0x3f6 bmdma 0xf000 irq 14
[    2.593615] ata8: PATA max UDMA/100 cmd 0x170 ctl 0x376 bmdma 0xf008 irq 15
[    2.622438] Uniform Multi-Platform E-IDE driver
[    2.661672] usb 2-5: new high-speed USB device number 3 using ehci-pci
[    2.685698] usb 7-1: new low-speed USB device number 2 using ohci-pci
[    2.692729] r8169 0000:02:00.0 enp2s0: renamed from eth0
[    2.715658] firewire_ohci 0000:08:00.0: added OHCI v1.10 device as card 0, 4 IR + 8 IT contexts, quirks 0x10
[    2.746647] tsc: Refined TSC clocksource calibration: 2800.217 MHz
[    2.746658] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x285d0db652a, max_idle_ns: 440795334687 ns
[    2.746668] clocksource: Switched to clocksource tsc
[    2.784157] [drm] amdgpu kernel modesetting enabled.
[    2.786827] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    2.786829] AMD IOMMUv2 functionality not available on this system
[    2.792195] CRAT table not found
[    2.792200] Virtual CRAT table created for CPU
[    2.792201] Parsing CRAT table with 1 nodes
[    2.792203] Creating topology SYSFS entries
[    2.792216] Topology: Add CPU node
[    2.792216] Finished initializing topology
[    2.792278] kfd kfd: Initialized module
[    2.792474] checking generic (c0000000 420000) vs hw (c0000000 10000000)
[    2.792475] fb: switching to amdgpudrmfb from VESA VGA
[    2.792501] Console: switching to colour dummy device 80x25
[    2.792776] amdgpu 0000:05:00.0: SI support provided by radeon.
[    2.792777] amdgpu 0000:05:00.0: Use radeon.si_support=0 amdgpu.si_support=1 to override.
[    2.835486] usb 2-5: New USB device found, idVendor=0951, idProduct=1666, bcdDevice= 1.10
[    2.835489] usb 2-5: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    2.835490] usb 2-5: Product: DataTraveler 3.0
[    2.835491] usb 2-5: Manufacturer: Kingston
[    2.835492] usb 2-5: SerialNumber: 50E549C695ADB1A15907603E
[    2.843483] usb-storage 2-3:1.0: USB Mass Storage device detected
[    2.843592] scsi host8: usb-storage 2-3:1.0
[    2.843782] usb-storage 2-5:1.0: USB Mass Storage device detected
[    2.843838] scsi host9: usb-storage 2-5:1.0
[    2.844196] usbcore: registered new interface driver usb-storage
[    2.847358] usbcore: registered new interface driver uas
[    2.896362] ata2: SATA link down (SStatus 0 SControl 300)
[    2.896392] ata3: SATA link down (SStatus 0 SControl 300)
[    2.896421] ata1: SATA link down (SStatus 0 SControl 300)
[    2.901475] ata4: SATA link down (SStatus 0 SControl 300)
[    2.906516] ata5: SATA link down (SStatus 0 SControl 300)
[    2.906570] ata6: SATA link down (SStatus 0 SControl 300)
[    2.913709] usb 7-1: New USB device found, idVendor=046d, idProduct=c31c, bcdDevice=64.00
[    2.913711] usb 7-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    2.913712] usb 7-1: Product: USB Keyboard
[    2.913713] usb 7-1: Manufacturer: Logitech
[    2.930331] hidraw: raw HID events driver (C) Jiri Kosina
[    2.944040] usbcore: registered new interface driver usbhid
[    2.944042] usbhid: USB HID core driver
[    2.948396] input: Logitech USB Keyboard as /devices/pci0000:00/0000:00:16.0/usb7/7-1/7-1:1.0/0003:046D:C31C.0001/input/input8
[    3.005913] hid-generic 0003:046D:C31C.0001: input,hidraw0: USB HID v1.10 Keyboard [Logitech USB Keyboard] on usb-0000:00:16.0-1/input0
[    3.006253] input: Logitech USB Keyboard Consumer Control as /devices/pci0000:00/0000:00:16.0/usb7/7-1/7-1:1.1/0003:046D:C31C.0002/input/input9
[    3.065948] input: Logitech USB Keyboard System Control as /devices/pci0000:00/0000:00:16.0/usb7/7-1/7-1:1.1/0003:046D:C31C.0002/input/input10
[    3.066073] hid-generic 0003:046D:C31C.0002: input,hidraw1: USB HID v1.10 Device [Logitech USB Keyboard] on usb-0000:00:16.0-1/input1
[    3.265782] firewire_core 0000:08:00.0: created device fw0: GUID 0010dc0001d32554, S400
[    3.329685] usb 7-2: new low-speed USB device number 3 using ohci-pci
[    3.524720] usb 7-2: New USB device found, idVendor=0458, idProduct=003a, bcdDevice= 1.00
[    3.524722] usb 7-2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    3.524724] usb 7-2: Product: Optical Mouse
[    3.524725] usb 7-2: Manufacturer: Genius
[    3.534155] input: Genius Optical Mouse as /devices/pci0000:00/0000:00:16.0/usb7/7-2/7-2:1.0/0003:0458:003A.0003/input/input11
[    3.534342] hid-generic 0003:0458:003A.0003: input,hidraw2: USB HID v1.11 Mouse [Genius Optical Mouse] on usb-0000:00:16.0-2/input0
[    3.874377] scsi 8:0:0:0: Direct-Access     Generic  Flash-Disk       2.00 PQ: 0 ANSI: 4
[    3.874680] scsi 9:0:0:0: Direct-Access     Kingston DataTraveler 3.0 PMAP PQ: 0 ANSI: 6
[    3.874754] sd 8:0:0:0: Attached scsi generic sg0 type 0
[    3.874893] sd 9:0:0:0: Attached scsi generic sg1 type 0
[    3.875325] sd 8:0:0:0: [sda] 15728640 512-byte logical blocks: (8.05 GB/7.50 GiB)
[    3.875575] sd 9:0:0:0: [sdb] 30277632 512-byte logical blocks: (15.5 GB/14.4 GiB)
[    3.875945] sd 8:0:0:0: [sda] Write Protect is off
[    3.875947] sd 8:0:0:0: [sda] Mode Sense: 03 00 00 00
[    3.876197] sd 9:0:0:0: [sdb] Write Protect is off
[    3.876198] sd 9:0:0:0: [sdb] Mode Sense: 45 00 00 00
[    3.876571] sd 8:0:0:0: [sda] No Caching mode page found
[    3.876577] sd 8:0:0:0: [sda] Assuming drive cache: write through
[    3.876824] sd 9:0:0:0: [sdb] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    3.879582]  sda: sda1
[    3.882075] sd 8:0:0:0: [sda] Attached SCSI removable disk
[    3.890321] random: fast init done
[    3.917683] usb 3-4: new high-speed USB device number 4 using ehci-pci
[    4.074656] usb 3-4: New USB device found, idVendor=0204, idProduct=6025, bcdDevice= 1.00
[    4.074658] usb 3-4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    4.074660] usb 3-4: Product: Flash Disk      
[    4.074661] usb 3-4: Manufacturer: USB2.0  
[    4.074662] usb 3-4: SerialNumber: 308202337030
[    4.074899] usb-storage 3-4:1.0: USB Mass Storage device detected
[    4.075052] scsi host10: usb-storage 3-4:1.0
[    5.090298] scsi 10:0:0:0: Direct-Access     USB2.0   Flash Disk       4.00 PQ: 0 ANSI: 2
[    5.092059] sd 10:0:0:0: Attached scsi generic sg2 type 0
[    5.092748] sd 10:0:0:0: [sdc] 1034751 512-byte logical blocks: (530 MB/505 MiB)
[    5.093364] sd 10:0:0:0: [sdc] Write Protect is off
[    5.093366] sd 10:0:0:0: [sdc] Mode Sense: 00 00 00 00
[    5.094005] sd 10:0:0:0: [sdc] Asking for cache data failed
[    5.094013] sd 10:0:0:0: [sdc] Assuming drive cache: write through
[    5.099533]  sdc: sdc1
[    5.102415] sd 10:0:0:0: [sdc] Attached SCSI removable disk
[    5.493539]  sdb: sdb1
[    5.496113] sd 9:0:0:0: [sdb] Attached SCSI removable disk
[    5.718397] EXT4-fs (sdb1): mounted filesystem with ordered data mode. Opts: (null)
[    6.299280] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    6.301951] systemd[1]: Detected architecture x86-64.
[    6.304587] systemd[1]: Set hostname to <test>.
[    6.887176] random: systemd: uninitialized urandom read (16 bytes read)
[    6.887320] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[    6.887364] random: systemd: uninitialized urandom read (16 bytes read)
[    6.887370] systemd[1]: Reached target Remote File Systems.
[    6.887392] random: systemd: uninitialized urandom read (16 bytes read)
[    6.887423] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    6.887962] systemd[1]: Created slice System Slice.
[    6.888110] systemd[1]: Listening on udev Kernel Socket.
[    6.888228] systemd[1]: Listening on Journal Audit Socket.
[    6.888291] systemd[1]: Listening on fsck to fsckd communication Socket.
[    7.079778] lp: driver loaded but no devices found
[    7.142818] ppdev: user-space parallel port driver
[    7.315309] EXT4-fs (sdb1): re-mounted. Opts: errors=remount-ro
[    7.475505] systemd-journald[264]: Received request to flush runtime journal from PID 1
[    7.480184] Adding 700960k swap on /swapfile.  Priority:-2 extents:3 across:717344k FS
[    8.735884] random: crng init done
[    8.735886] random: 7 urandom warning(s) missed due to ratelimiting
[    9.263265] snd_hda_intel 0000:05:00.1: Handle vga_switcheroo audio client
[    9.263268] snd_hda_intel 0000:05:00.1: Force to non-snoop mode
[    9.550196] input: HDA ATI HDMI HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:09.0/0000:05:00.1/sound/card1/input12
[    9.550247] input: HDA ATI HDMI HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:09.0/0000:05:00.1/sound/card1/input13
[    9.550290] input: HDA ATI HDMI HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:09.0/0000:05:00.1/sound/card1/input14
[    9.550333] input: HDA ATI HDMI HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:09.0/0000:05:00.1/sound/card1/input15
[    9.550377] input: HDA ATI HDMI HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:09.0/0000:05:00.1/sound/card1/input16
[    9.550420] input: HDA ATI HDMI HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:09.0/0000:05:00.1/sound/card1/input17
[    9.564395] snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALC892: line_outs=4 (0x14/0x15/0x16/0x17/0x0) type:line
[    9.564398] snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[    9.564399] snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
[    9.564400] snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
[    9.564401] snd_hda_codec_realtek hdaudioC0D0:    dig-out=0x11/0x1e
[    9.564402] snd_hda_codec_realtek hdaudioC0D0:    inputs:
[    9.564404] snd_hda_codec_realtek hdaudioC0D0:      Front Mic=0x19
[    9.564408] snd_hda_codec_realtek hdaudioC0D0:      Rear Mic=0x18
[    9.564409] snd_hda_codec_realtek hdaudioC0D0:      Line=0x1a
[    9.594340] input: HDA ATI SB Front Mic as /devices/pci0000:00/0000:00:14.2/sound/card0/input18
[    9.594393] input: HDA ATI SB Rear Mic as /devices/pci0000:00/0000:00:14.2/sound/card0/input19
[    9.594436] input: HDA ATI SB Line as /devices/pci0000:00/0000:00:14.2/sound/card0/input20
[    9.594481] input: HDA ATI SB Line Out Front as /devices/pci0000:00/0000:00:14.2/sound/card0/input21
[    9.594530] input: HDA ATI SB Line Out Surround as /devices/pci0000:00/0000:00:14.2/sound/card0/input22
[    9.594572] input: HDA ATI SB Line Out CLFE as /devices/pci0000:00/0000:00:14.2/sound/card0/input23
[    9.594614] input: HDA ATI SB Line Out Side as /devices/pci0000:00/0000:00:14.2/sound/card0/input24
[    9.594658] input: HDA ATI SB Front Headphone as /devices/pci0000:00/0000:00:14.2/sound/card0/input25
[    9.607901] kvm: Nested Virtualization enabled
[    9.607904] kvm: Nested Paging enabled
[    9.746361] MCE: In-kernel MCE decoding enabled.
[    9.812252] EDAC amd64: Node 0: DRAM ECC disabled.
[    9.812254] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   13.573890] audit: type=1400 audit(1547844811.737:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=464 comm="apparmor_parser"
[   13.573901] audit: type=1400 audit(1547844811.737:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=464 comm="apparmor_parser"
[   13.573903] audit: type=1400 audit(1547844811.737:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=464 comm="apparmor_parser"
[   13.573905] audit: type=1400 audit(1547844811.737:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=464 comm="apparmor_parser"
[   15.540721] audit: type=1400 audit(1547844813.701:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince" pid=477 comm="apparmor_parser"
[   15.540726] audit: type=1400 audit(1547844813.701:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//sanitized_helper" pid=477 comm="apparmor_parser"
[   15.540728] audit: type=1400 audit(1547844813.701:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer" pid=477 comm="apparmor_parser"
[   15.540730] audit: type=1400 audit(1547844813.701:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer//sanitized_helper" pid=477 comm="apparmor_parser"
[   15.540731] audit: type=1400 audit(1547844813.701:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-thumbnailer" pid=477 comm="apparmor_parser"
[   15.540733] audit: type=1400 audit(1547844813.701:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-thumbnailer//sanitized_helper" pid=477 comm="apparmor_parser"
[   22.621406] IPv6: ADDRCONF(NETDEV_UP): enp2s0: link is not ready
[   22.638614] RTL8211E Gigabit Ethernet r8169-200:00: attached PHY driver [RTL8211E Gigabit Ethernet] (mii_bus:phy_addr=r8169-200:00, irq=IGNORE)
[   22.848087] r8169 0000:02:00.0 enp2s0: Link is Down
[   22.848284] IPv6: ADDRCONF(NETDEV_UP): enp2s0: link is not ready
[   29.301606] r8169 0000:02:00.0 enp2s0: Link is Up - 100Mbps/Full - flow control off
[   29.301619] IPv6: ADDRCONF(NETDEV_CHANGE): enp2s0: link becomes ready
[   32.908651] kauditd_printk_skb: 23 callbacks suppressed
[   32.908653] audit: type=1400 audit(1547844831.069:35): apparmor="STATUS" operation="profile_load" profile="unconfined" name="docker-default" pid=1322 comm="apparmor_parser"
[   33.679731] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[   33.692304] Bridge firewalling registered
[   33.849794] bpfilter: Loaded bpfilter_umh pid 1363
[   34.174249] Initializing XFRM netlink socket
[   34.348410] IPv6: ADDRCONF(NETDEV_UP): docker0: link is not ready
[  128.388740] no MTRR for c0000000,1000000 found
[  236.749036] rfkill: input handler disabled
[  244.429517] FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
[  245.408333] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 0, start 53177e5f)
[  245.408339] FAT-fs (sda1): Filesystem has been set read-only
[  245.408420] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  245.408442] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  245.408444] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  245.408446] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  245.408447] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  245.408449] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  245.408451] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  245.408452] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  245.408454] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697739] fat_get_cluster: 701 callbacks suppressed
[  972.697742] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697748] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697750] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697752] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697753] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697755] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697757] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697758] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663249, start ffe81a38)
[  972.697774] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663250, start 7d808ab1)
[  972.697776] FAT-fs (sda1): error, fat_get_cluster: invalid start cluster (i_pos 23663250, start 7d808ab1)
[  992.486890] usb 3-4: USB disconnect, device number 4`

Feel free to ask any other information to solve this issue. 
Thanks in advance. 



---

## 评论 (2 条)

### 评论 #1 — nioroso-x3 (2019-01-18T21:56:05Z)

Isn't that a 7950? The oldest cards supported by rocm are the r9 290 series.

---

### 评论 #2 — jlgreathouse (2019-01-18T22:50:04Z)

@nioroso-x3 it's correct. [Tahiti is not on our list of supported GPUs for ROCm](https://rocm.github.io/hardware.html#gpus-that-are-known-not-to-work-with-rocm).

---
