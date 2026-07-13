# hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8

- **Issue #:** 524
- **State:** closed
- **Created:** 2018-09-07T22:35:29Z
- **Updated:** 2018-09-20T01:14:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/524

Hey Im using ubuntu 16.04 and i have some issues seeing the t/rocm/bin/rocminfo.

Info of my graphic card.
Btw if it's a graphic card issue can u tell me witch type of GPU is supported for the 580 rx (because i got more types ) ? Thank you very much.
```
 uname -aLinux alex-System-Product-Name-Invalid-entry-length-16-Fixed-up-to-11 4.15.0-33-generic #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```
```
amdgpu, 1.8-199, 4.15.0-33-generic, x86_64: installed
```
```
lsmod | grep amdgpu
amdgpu               2719744  57
amdchash               16384  1 amdgpu
amd_sched              24576  1 amdgpu
amdttm                110592  1 amdgpu
amdkcl                 28672  4 amdttm,amdgpu,amd_sched,amdkfd
i2c_algo_bit           16384  1 amdgpu
drm_kms_helper        172032  1 amdgpu
drm                   401408  9 amdttm,amdgpu,amdkcl,amd_sched,drm_kms_helper
```
```
 lsmod | grep amdkfd
amdkfd                274432  1
amd_iommu_v2           20480  1 amdkfd
amdkcl                 28672  4 amdttm,amdgpu,amd_sched,amdkfd
```
```
groups
alex adm cdrom sudo dip video plugdev lpadmin sambashare
```
```
 lspci | grep VGA
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
```
```
 lspci -vvv
00:00.0 Host bridge: Intel Corporation 2nd Generation Core Processor Family DRAM Controller (rev 09)
	Subsystem: ASUSTeK Computer Inc. 2nd Generation Core Processor Family DRAM Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
	Latency: 0
	Capabilities: <access denied>
	Kernel driver in use: snb_uncore

00:01.0 PCI bridge: Intel Corporation Xeon E3-1200/2nd Generation Core Processor Family PCI Express Root Port (rev 09) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: f7e00000-f7efffff
	Prefetchable memory behind bridge: 00000000e0000000-00000000f01fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA+ MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:14.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller (rev 04) (prog-if 30 [XHCI])
	Subsystem: ASUSTeK Computer Inc. P8 series motherboard
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 24
	Region 0: Memory at f7f00000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

00:16.0 Communication controller: Intel Corporation 7 Series/C210 Series Chipset Family MEI Controller #1 (rev 04)
	Subsystem: ASUSTeK Computer Inc. P8 series motherboard
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 33
	Region 0: Memory at f7f1a000 (64-bit, non-prefetchable) [size=16]
	Capabilities: <access denied>
	Kernel driver in use: mei_me
	Kernel modules: mei_me

00:1a.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2 (rev 04) (prog-if 20 [EHCI])
	Subsystem: ASUSTeK Computer Inc. P8 series motherboard
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 23
	Region 0: Memory at f7f18000 (32-bit, non-prefetchable) [size=1K]
	Capabilities: <access denied>
	Kernel driver in use: ehci-pci

00:1b.0 Audio device: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller (rev 04)
	Subsystem: ASUSTeK Computer Inc. 7 Series/C210 Series Chipset Family High Definition Audio Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 34
	Region 0: Memory at f7f10000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

00:1c.0 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 1 (rev c4) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1c.5 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 6 (rev c4) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 17
	Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
	I/O behind bridge: 0000d000-0000dfff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000f0300000-00000000f03fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1c.6 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 7 (rev c4) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin C routed to IRQ 18
	Bus: primary=00, secondary=04, subordinate=04, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: f7d00000-f7dfffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1d.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 (rev 04) (prog-if 20 [EHCI])
	Subsystem: ASUSTeK Computer Inc. P8 series motherboard
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 23
	Region 0: Memory at f7f17000 (32-bit, non-prefetchable) [size=1K]
	Capabilities: <access denied>
	Kernel driver in use: ehci-pci

00:1f.0 ISA bridge: Intel Corporation Z77 Express Chipset LPC Controller (rev 04)
	Subsystem: ASUSTeK Computer Inc. P8 series motherboard
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Capabilities: <access denied>
	Kernel driver in use: lpc_ich
	Kernel modules: lpc_ich

00:1f.2 SATA controller: Intel Corporation 7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode] (rev 04) (prog-if 01 [AHCI 1.0])
	Subsystem: ASUSTeK Computer Inc. P8 series motherboard
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin B routed to IRQ 31
	Region 0: I/O ports at f070 [size=8]
	Region 1: I/O ports at f060 [size=4]
	Region 2: I/O ports at f050 [size=8]
	Region 3: I/O ports at f040 [size=4]
	Region 4: I/O ports at f020 [size=32]
	Region 5: Memory at f7f16000 (32-bit, non-prefetchable) [size=2K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

00:1f.3 SMBus: Intel Corporation 7 Series/C210 Series Chipset Family SMBus Controller (rev 04)
	Subsystem: ASUSTeK Computer Inc. P8 series motherboard
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin C routed to IRQ 10
	Region 0: Memory at f7f15000 (64-bit, non-prefetchable) [size=256]
	Region 4: I/O ports at f000 [size=32]
	Kernel modules: i2c_i801

01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7) (prog-if 00 [VGA controller])
	Subsystem: Device 1da2:e366
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 32
	Region 0: Memory at e0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at f0000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at e000 [size=256]
	Region 5: Memory at f7e00000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
	Subsystem: Device 1da2:aaf0
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 35
	Region 0: Memory at f7e60000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

03:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 09)
	Subsystem: ASUSTeK Computer Inc. P8 series motherboard
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 17
	Region 0: I/O ports at d000 [size=256]
	Region 2: Memory at f0304000 (64-bit, prefetchable) [size=4K]
	Region 4: Memory at f0300000 (64-bit, prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: r8169
	Kernel modules: r8169

04:00.0 USB controller: ASMedia Technology Inc. ASM1042 SuperSpeed USB Host Controller (prog-if 30 [XHCI])
	Subsystem: ASUSTeK Computer Inc. P8B WS Motherboard
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 18
	Region 0: Memory at f7d00000 (64-bit, non-prefetchable) [size=32K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd
```
```
lspci -tv
-[0000:00]-+-00.0  Intel Corporation 2nd Generation Core Processor Family DRAM Controller
           +-01.0-[01]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-14.0  Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller
           +-16.0  Intel Corporation 7 Series/C210 Series Chipset Family MEI Controller #1
           +-1a.0  Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2
           +-1b.0  Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller
           +-1c.0-[02]--
           +-1c.5-[03]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           +-1c.6-[04]----00.0  ASMedia Technology Inc. ASM1042 SuperSpeed USB Host Controller
           +-1d.0  Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1
           +-1f.0  Intel Corporation Z77 Express Chipset LPC Controller
           +-1f.2  Intel Corporation 7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode]
           \-1f.3  Intel Corporation 7 Series/C210 Series Chipset Family SMBus Controller
```

```
lspci -n00:00.0 0600: 8086:0100 (rev 09)
00:01.0 0604: 8086:0101 (rev 09)
00:14.0 0c03: 8086:1e31 (rev 04)
00:16.0 0780: 8086:1e3a (rev 04)
00:1a.0 0c03: 8086:1e2d (rev 04)
00:1b.0 0403: 8086:1e20 (rev 04)
00:1c.0 0604: 8086:1e10 (rev c4)
00:1c.5 0604: 8086:1e1a (rev c4)
00:1c.6 0604: 8086:1e1c (rev c4)
00:1d.0 0c03: 8086:1e26 (rev 04)
00:1f.0 0601: 8086:1e44 (rev 04)
00:1f.2 0106: 8086:1e02 (rev 04)
00:1f.3 0c05: 8086:1e22 (rev 04)
01:00.0 0300: 1002:67df (rev e7)
01:00.1 0403: 1002:aaf0
03:00.0 0200: 10ec:8168 (rev 09)
04:00.0 0c03: 1b21:1042
```

```
dmesg
[    0.000000] microcode: microcode updated early to revision 0x2e, date = 2018-04-10
[    0.000000] Linux version 4.15.0-33-generic (buildd@lgw01-amd64-010) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)) #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 (Ubuntu 4.15.0-33.36~16.04.1-generic 4.15.18)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-33-generic root=UUID=537a0185-a596-407a-9425-534ecf354d60 ro quiet splash vt.handoff=7
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'standard' format.
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009d7ff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009d800-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000dd250fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000dd251000-0x00000000ddaa9fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ddaaa000-0x00000000ddab9fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000ddaba000-0x00000000ddbddfff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000ddbde000-0x00000000de804fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000de805000-0x00000000de805fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000de806000-0x00000000de848fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000de849000-0x00000000dec6efff] usable
[    0.000000] BIOS-e820: [mem 0x00000000dec6f000-0x00000000deff3fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000deff4000-0x00000000deffffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed03fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed1c000-0x00000000fed1ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x00000001feffffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] SMBIOS 2.7 present.
[    0.000000] DMI: System manufacturer System Product Name/P8Z77-M PRO, BIOS 1616 10/05/2012
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x1ff000 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: uncachable
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF uncachable
[    0.000000]   C0000-CFFFF write-protect
[    0.000000]   D0000-E7FFF uncachable
[    0.000000]   E8000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 000000000 mask F00000000 write-back
[    0.000000]   1 base 100000000 mask F00000000 write-back
[    0.000000]   2 base 0E0000000 mask FE0000000 uncachable
[    0.000000]   3 base 1FF000000 mask FFF000000 uncachable
[    0.000000]   4 disabled
[    0.000000]   5 disabled
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000]   8 disabled
[    0.000000]   9 disabled
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000000] total RAM covered: 7664M
[    0.000000] Found optimal setting for mtrr clean up
[    0.000000]  gran_size: 64K 	chunk_size: 1G 	num_reg: 4  	lose cover RAM: 0G
[    0.000000] e820: update [mem 0xe0000000-0xffffffff] usable ==> reserved
[    0.000000] e820: last_pfn = 0xdf000 max_arch_pfn = 0x400000000
[    0.000000] found SMP MP-table at [mem 0x000fd7a0-0x000fd7af] mapped at [        (ptrval)]
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [        (ptrval)] 97000 size 24576
[    0.000000] BRK [0x9ff3d000, 0x9ff3dfff] PGTABLE
[    0.000000] BRK [0x9ff3e000, 0x9ff3efff] PGTABLE
[    0.000000] BRK [0x9ff3f000, 0x9ff3ffff] PGTABLE
[    0.000000] BRK [0x9ff40000, 0x9ff40fff] PGTABLE
[    0.000000] BRK [0x9ff41000, 0x9ff41fff] PGTABLE
[    0.000000] BRK [0x9ff42000, 0x9ff42fff] PGTABLE
[    0.000000] BRK [0x9ff43000, 0x9ff43fff] PGTABLE
[    0.000000] BRK [0x9ff44000, 0x9ff44fff] PGTABLE
[    0.000000] BRK [0x9ff45000, 0x9ff45fff] PGTABLE
[    0.000000] BRK [0x9ff46000, 0x9ff46fff] PGTABLE
[    0.000000] BRK [0x9ff47000, 0x9ff47fff] PGTABLE
[    0.000000] RAMDISK: [mem 0x317d0000-0x34bdffff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x00000000000F0490 000024 (v02 ALASKA)
[    0.000000] ACPI: XSDT 0x00000000DDAAD070 00005C (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x00000000DDAB8420 00010C (v05 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: DSDT 0x00000000DDAAD168 00B2B1 (v02 ALASKA A M I    00000022 INTL 20051117)
[    0.000000] ACPI: FACS 0x00000000DDBDC080 000040
[    0.000000] ACPI: APIC 0x00000000DDAB8530 000072 (v03 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FPDT 0x00000000DDAB85A8 000044 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: MCFG 0x00000000DDAB85F0 00003C (v01 ALASKA A M I    01072009 MSFT 00000097)
[    0.000000] ACPI: SSDT 0x00000000DDAB8630 00036D (v01 SataRe SataTabl 00001000 INTL 20091112)
[    0.000000] ACPI: SSDT 0x00000000DDAB89A0 0009AA (v01 PmRef  Cpu0Ist  00003000 INTL 20051117)
[    0.000000] ACPI: SSDT 0x00000000DDAB9350 000A92 (v01 PmRef  CpuPm    00003000 INTL 20051117)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x00000001feffffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x1fefd1000-0x1feffbfff]
[    0.000000] tsc: Fast TSC calibration using PIT
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x00000001feffffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x000000000009cfff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x00000000dd250fff]
[    0.000000]   node   0: [mem 0x00000000de805000-0x00000000de805fff]
[    0.000000]   node   0: [mem 0x00000000de849000-0x00000000dec6efff]
[    0.000000]   node   0: [mem 0x00000000deff4000-0x00000000deffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x00000001feffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x00000001feffffff]
[    0.000000] On node 0 totalpages: 1951264
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 21 pages reserved
[    0.000000]   DMA zone: 3996 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 14107 pages used for memmap
[    0.000000]   DMA32 zone: 902788 pages, LIFO batch:31
[    0.000000]   Normal zone: 16320 pages used for memmap
[    0.000000]   Normal zone: 1044480 pages, LIFO batch:31
[    0.000000] Reserved but unavailable: 100 pages
[    0.000000] ACPI: PM-Timer IO Port: 0x408
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0xff] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-23
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] smpboot: Allowing 4 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009d000-0x0009dfff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009e000-0x0009ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000dffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000e0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xdd251000-0xddaa9fff]
[    0.000000] PM: Registered nosave memory: [mem 0xddaaa000-0xddab9fff]
[    0.000000] PM: Registered nosave memory: [mem 0xddaba000-0xddbddfff]
[    0.000000] PM: Registered nosave memory: [mem 0xddbde000-0xde804fff]
[    0.000000] PM: Registered nosave memory: [mem 0xde806000-0xde848fff]
[    0.000000] PM: Registered nosave memory: [mem 0xdec6f000-0xdeff3fff]
[    0.000000] PM: Registered nosave memory: [mem 0xdf000000-0xf7ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf8000000-0xfbffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfc000000-0xfebfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec01000-0xfecfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed00000-0xfed03fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed04000-0xfed1bfff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed1c000-0xfed1ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed20000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] e820: [mem 0xdf000000-0xf7ffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] random: get_random_bytes called from start_kernel+0x99/0x51b with crng_init=0
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:4 nr_cpu_ids:4 nr_node_ids:1
[    0.000000] percpu: Embedded 46 pages/cpu @        (ptrval) s151552 r8192 d28672 u524288
[    0.000000] pcpu-alloc: s151552 r8192 d28672 u524288 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1 2 3 
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1920752
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-33-generic root=UUID=537a0185-a596-407a-9425-534ecf354d60 ro quiet splash vt.handoff=7
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 7533900K/7805056K available (12300K kernel code, 2469K rwdata, 4252K rodata, 2404K init, 2416K bss, 271156K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] Kernel/User page tables isolation: enabled
[    0.000000] ftrace: allocating 39127 entries in 153 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=4.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 524544, nr_irqs: 456, preallocated irqs: 16
[    0.000000] vt handoff: transparent VT on vt#7
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] ACPI: Core revision 20170831
[    0.000000] ACPI: 4 ACPI AML tables successfully acquired and loaded
[    0.000000] APIC: Switch to symmetric I/O mode setup
[    0.000000] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.020000] tsc: Fast TSC calibration using PIT
[    0.024000] tsc: Detected 3309.890 MHz processor
[    0.024000] Calibrating delay loop (skipped), value calculated using timer frequency.. 6619.78 BogoMIPS (lpj=13239560)
[    0.024000] pid_max: default: 32768 minimum: 301
[    0.024000] Security Framework initialized
[    0.024000] Yama: becoming mindful.
[    0.024000] AppArmor: AppArmor initialized
[    0.024000] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.028766] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes)
[    0.028805] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.028834] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.029016] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.029017] ENERGY_PERF_BIAS: View and update with x86_energy_perf_policy(8)
[    0.029021] mce: CPU supports 9 MCE banks
[    0.029027] CPU0: Thermal monitoring enabled (TM1)
[    0.029034] process: using mwait in idle threads
[    0.029037] Last level iTLB entries: 4KB 512, 2MB 8, 4MB 8
[    0.029037] Last level dTLB entries: 4KB 512, 2MB 32, 4MB 32, 1GB 0
[    0.029038] Spectre V2 : Mitigation: Full generic retpoline
[    0.029039] Spectre V2 : Spectre v2 mitigation: Enabling Indirect Branch Prediction Barrier
[    0.029039] Spectre V2 : Enabling Restricted Speculation for firmware calls
[    0.029040] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.029122] Freeing SMP alternatives memory: 36K
[    0.032067] TSC deadline timer enabled
[    0.032069] smpboot: CPU0: Intel(R) Core(TM) i5-2500K CPU @ 3.30GHz (family: 0x6, model: 0x2a, stepping: 0x7)
[    0.032124] Performance Events: PEBS fmt1+, SandyBridge events, 16-deep LBR, full-width counters, Intel PMU driver.
[    0.032142] ... version:                3
[    0.032142] ... bit width:              48
[    0.032142] ... generic registers:      8
[    0.032143] ... value mask:             0000ffffffffffff
[    0.032144] ... max period:             00007fffffffffff
[    0.032144] ... fixed-purpose events:   3
[    0.032144] ... event mask:             00000007000000ff
[    0.032177] Hierarchical SRCU implementation.
[    0.032901] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.032914] smp: Bringing up secondary CPUs ...
[    0.032976] x86: Booting SMP configuration:
[    0.032977] .... node  #0, CPUs:      #1 #2 #3
[    0.040053] smp: Brought up 1 node, 4 CPUs
[    0.040053] smpboot: Max logical packages: 1
[    0.040053] smpboot: Total of 4 processors activated (26479.12 BogoMIPS)
[    0.042250] devtmpfs: initialized
[    0.042250] x86/mm: Memory block size: 128MB
[    0.042250] evm: security.selinux
[    0.042250] evm: security.SMACK64
[    0.042250] evm: security.SMACK64EXEC
[    0.042250] evm: security.SMACK64TRANSMUTE
[    0.042250] evm: security.SMACK64MMAP
[    0.042250] evm: security.apparmor
[    0.042250] evm: security.ima
[    0.042250] evm: security.capability
[    0.042250] PM: Registering ACPI NVS region [mem 0xddaba000-0xddbddfff] (1196032 bytes)
[    0.042250] PM: Registering ACPI NVS region [mem 0xde806000-0xde848fff] (274432 bytes)
[    0.042250] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.042250] futex hash table entries: 1024 (order: 4, 65536 bytes)
[    0.042250] pinctrl core: initialized pinctrl subsystem
[    0.042250] RTC time: 22:32:21, date: 09/07/18
[    0.042250] NET: Registered protocol family 16
[    0.042250] audit: initializing netlink subsys (disabled)
[    0.042250] audit: type=2000 audit(1536359540.040:1): state=initialized audit_enabled=0 res=1
[    0.042250] cpuidle: using governor ladder
[    0.042250] cpuidle: using governor menu
[    0.042250] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.042250] ACPI: bus type PCI registered
[    0.042250] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.042250] PCI: MMCONFIG for domain 0000 [bus 00-3f] at [mem 0xf8000000-0xfbffffff] (base 0xf8000000)
[    0.042250] PCI: MMCONFIG at [mem 0xf8000000-0xfbffffff] reserved in E820
[    0.042250] pmd_set_huge: Cannot satisfy [mem 0xf8000000-0xf8200000] with a huge-page mapping due to MTRR override.
[    0.042250] PCI: Using configuration type 1 for base access
[    0.042250] core: PMU erratum BJ122, BV98, HSD29 workaround disabled, HT off
[    0.044855] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.044855] ACPI: Added _OSI(Module Device)
[    0.044855] ACPI: Added _OSI(Processor Device)
[    0.044855] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.044855] ACPI: Added _OSI(Processor Aggregator Device)
[    0.044855] ACPI: Added _OSI(Linux-Dell-Video)
[    0.044855] ACPI: Executed 1 blocks of module-level executable AML code
[    0.048535] ACPI: Dynamic OEM Table Load:
[    0.048540] ACPI: SSDT 0xFFFF9FA375B11000 00083B (v01 PmRef  Cpu0Cst  00003001 INTL 20051117)
[    0.048673] ACPI: Dynamic OEM Table Load:
[    0.048673] ACPI: SSDT 0xFFFF9FA3755A8800 000303 (v01 PmRef  ApIst    00003000 INTL 20051117)
[    0.048673] ACPI: Dynamic OEM Table Load:
[    0.048673] ACPI: SSDT 0xFFFF9FA375504E00 000119 (v01 PmRef  ApCst    00003000 INTL 20051117)
[    0.048675] ACPI: EC: EC started
[    0.048675] ACPI: EC: interrupt blocked
[    0.048675] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as first EC
[    0.048675] ACPI: \_SB_.PCI0.LPCB.EC0_: GPE=0x18, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.048675] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as boot DSDT EC to handle transactions
[    0.048675] ACPI: Interpreter enabled
[    0.048675] ACPI: (supports S0 S3 S4 S5)
[    0.048675] ACPI: Using IOAPIC for interrupt routing
[    0.048675] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.048729] ACPI: Enabled 10 GPEs in block 00 to 3F
[    0.056673] ACPI: Power Resource [FN00] (off)
[    0.056759] ACPI: Power Resource [FN01] (off)
[    0.056844] ACPI: Power Resource [FN02] (off)
[    0.056928] ACPI: Power Resource [FN03] (off)
[    0.057013] ACPI: Power Resource [FN04] (off)
[    0.057695] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-3e])
[    0.057700] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.057998] acpi PNP0A08:00: _OSC: platform does not support [PCIeHotplug PME]
[    0.058187] acpi PNP0A08:00: _OSC: OS now controls [AER PCIeCapability]
[    0.058188] acpi PNP0A08:00: FADT indicates ASPM is unsupported, using BIOS configuration
[    0.058707] PCI host bridge to bus 0000:00
[    0.058709] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.058711] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.058712] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.058713] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000d3fff window]
[    0.058714] pci_bus 0000:00: root bus resource [mem 0x000d4000-0x000d7fff window]
[    0.058715] pci_bus 0000:00: root bus resource [mem 0x000d8000-0x000dbfff window]
[    0.058716] pci_bus 0000:00: root bus resource [mem 0x000dc000-0x000dffff window]
[    0.058717] pci_bus 0000:00: root bus resource [mem 0x000e0000-0x000e3fff window]
[    0.058718] pci_bus 0000:00: root bus resource [mem 0x000e4000-0x000e7fff window]
[    0.058719] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xfeafffff window]
[    0.058720] pci_bus 0000:00: root bus resource [bus 00-3e]
[    0.058727] pci 0000:00:00.0: [8086:0100] type 00 class 0x060000
[    0.058812] pci 0000:00:01.0: [8086:0101] type 01 class 0x060400
[    0.058841] pci 0000:00:01.0: PME# supported from D0 D3hot D3cold
[    0.058934] pci 0000:00:14.0: [8086:1e31] type 00 class 0x0c0330
[    0.058956] pci 0000:00:14.0: reg 0x10: [mem 0xf7f00000-0xf7f0ffff 64bit]
[    0.059020] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    0.059094] pci 0000:00:16.0: [8086:1e3a] type 00 class 0x078000
[    0.059117] pci 0000:00:16.0: reg 0x10: [mem 0xf7f1a000-0xf7f1a00f 64bit]
[    0.059186] pci 0000:00:16.0: PME# supported from D0 D3hot D3cold
[    0.059262] pci 0000:00:1a.0: [8086:1e2d] type 00 class 0x0c0320
[    0.059282] pci 0000:00:1a.0: reg 0x10: [mem 0xf7f18000-0xf7f183ff]
[    0.059360] pci 0000:00:1a.0: PME# supported from D0 D3hot D3cold
[    0.059437] pci 0000:00:1b.0: [8086:1e20] type 00 class 0x040300
[    0.059456] pci 0000:00:1b.0: reg 0x10: [mem 0xf7f10000-0xf7f13fff 64bit]
[    0.059523] pci 0000:00:1b.0: PME# supported from D0 D3hot D3cold
[    0.059608] pci 0000:00:1c.0: [8086:1e10] type 01 class 0x060400
[    0.059746] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.059834] pci 0000:00:1c.5: [8086:1e1a] type 01 class 0x060400
[    0.059910] pci 0000:00:1c.5: PME# supported from D0 D3hot D3cold
[    0.059987] pci 0000:00:1c.6: [8086:1e1c] type 01 class 0x060400
[    0.064063] pci 0000:00:1c.6: PME# supported from D0 D3hot D3cold
[    0.064143] pci 0000:00:1d.0: [8086:1e26] type 00 class 0x0c0320
[    0.064163] pci 0000:00:1d.0: reg 0x10: [mem 0xf7f17000-0xf7f173ff]
[    0.064240] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
[    0.064314] pci 0000:00:1f.0: [8086:1e44] type 00 class 0x060100
[    0.064482] pci 0000:00:1f.2: [8086:1e02] type 00 class 0x010601
[    0.064497] pci 0000:00:1f.2: reg 0x10: [io  0xf070-0xf077]
[    0.064504] pci 0000:00:1f.2: reg 0x14: [io  0xf060-0xf063]
[    0.064510] pci 0000:00:1f.2: reg 0x18: [io  0xf050-0xf057]
[    0.064517] pci 0000:00:1f.2: reg 0x1c: [io  0xf040-0xf043]
[    0.064523] pci 0000:00:1f.2: reg 0x20: [io  0xf020-0xf03f]
[    0.064529] pci 0000:00:1f.2: reg 0x24: [mem 0xf7f16000-0xf7f167ff]
[    0.064566] pci 0000:00:1f.2: PME# supported from D3hot
[    0.064634] pci 0000:00:1f.3: [8086:1e22] type 00 class 0x0c0500
[    0.064651] pci 0000:00:1f.3: reg 0x10: [mem 0xf7f15000-0xf7f150ff 64bit]
[    0.064669] pci 0000:00:1f.3: reg 0x20: [io  0xf000-0xf01f]
[    0.064784] pci 0000:01:00.0: [1002:67df] type 00 class 0x030000
[    0.064804] pci 0000:01:00.0: reg 0x10: [mem 0xe0000000-0xefffffff 64bit pref]
[    0.064812] pci 0000:01:00.0: reg 0x18: [mem 0xf0000000-0xf01fffff 64bit pref]
[    0.064817] pci 0000:01:00.0: reg 0x20: [io  0xe000-0xe0ff]
[    0.064823] pci 0000:01:00.0: reg 0x24: [mem 0xf7e00000-0xf7e3ffff]
[    0.064829] pci 0000:01:00.0: reg 0x30: [mem 0xf7e40000-0xf7e5ffff pref]
[    0.064833] pci 0000:01:00.0: enabling Extended Tags
[    0.064880] pci 0000:01:00.0: supports D1 D2
[    0.064881] pci 0000:01:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.064931] pci 0000:01:00.1: [1002:aaf0] type 00 class 0x040300
[    0.064948] pci 0000:01:00.1: reg 0x10: [mem 0xf7e60000-0xf7e63fff 64bit]
[    0.064975] pci 0000:01:00.1: enabling Extended Tags
[    0.065011] pci 0000:01:00.1: supports D1 D2
[    0.076027] pci 0000:00:01.0: PCI bridge to [bus 01]
[    0.076031] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    0.076035] pci 0000:00:01.0:   bridge window [mem 0xf7e00000-0xf7efffff]
[    0.076039] pci 0000:00:01.0:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.076122] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    0.076198] pci 0000:03:00.0: [10ec:8168] type 00 class 0x020000
[    0.076232] pci 0000:03:00.0: reg 0x10: [io  0xd000-0xd0ff]
[    0.076264] pci 0000:03:00.0: reg 0x18: [mem 0xf0304000-0xf0304fff 64bit pref]
[    0.076284] pci 0000:03:00.0: reg 0x20: [mem 0xf0300000-0xf0303fff 64bit pref]
[    0.076402] pci 0000:03:00.0: supports D1 D2
[    0.076403] pci 0000:03:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.088026] pci 0000:00:1c.5: PCI bridge to [bus 03]
[    0.088031] pci 0000:00:1c.5:   bridge window [io  0xd000-0xdfff]
[    0.088040] pci 0000:00:1c.5:   bridge window [mem 0xf0300000-0xf03fffff 64bit pref]
[    0.088136] pci 0000:04:00.0: [1b21:1042] type 00 class 0x0c0330
[    0.088176] pci 0000:04:00.0: reg 0x10: [mem 0xf7d00000-0xf7d07fff 64bit]
[    0.088339] pci 0000:04:00.0: PME# supported from D3hot D3cold
[    0.100023] pci 0000:00:1c.6: PCI bridge to [bus 04]
[    0.100030] pci 0000:00:1c.6:   bridge window [mem 0xf7d00000-0xf7dfffff]
[    0.100618] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.100683] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 *10 11 12 14 15)
[    0.100746] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 *10 11 12 14 15)
[    0.100809] ACPI: PCI Interrupt Link [LNKD] (IRQs *3 4 5 6 10 11 12 14 15)
[    0.100871] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.100935] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 *5 6 10 11 12 14 15)
[    0.101001] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.101064] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 *4 5 6 10 11 12 14 15)
[    0.101332] ACPI: EC: interrupt unblocked
[    0.101337] ACPI: EC: event unblocked
[    0.101342] ACPI: \_SB_.PCI0.LPCB.EC0_: GPE=0x18, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.101343] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as boot DSDT EC to handle transactions and events
[    0.101504] SCSI subsystem initialized
[    0.101514] libata version 3.00 loaded.
[    0.101514] pci 0000:01:00.0: vgaarb: setting as boot VGA device
[    0.101514] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.101514] pci 0000:01:00.0: vgaarb: bridge control possible
[    0.101514] vgaarb: loaded
[    0.101514] ACPI: bus type USB registered
[    0.101514] usbcore: registered new interface driver usbfs
[    0.101514] usbcore: registered new interface driver hub
[    0.101514] usbcore: registered new device driver usb
[    0.101514] EDAC MC: Ver: 3.0.0
[    0.101514] PCI: Using ACPI for IRQ routing
[    0.101514] PCI: pci_cache_line_size set to 64 bytes
[    0.101514] e820: reserve RAM buffer [mem 0x0009d800-0x0009ffff]
[    0.101514] e820: reserve RAM buffer [mem 0xdd251000-0xdfffffff]
[    0.101514] e820: reserve RAM buffer [mem 0xde806000-0xdfffffff]
[    0.101514] e820: reserve RAM buffer [mem 0xdec6f000-0xdfffffff]
[    0.101514] e820: reserve RAM buffer [mem 0xdf000000-0xdfffffff]
[    0.101514] e820: reserve RAM buffer [mem 0x1ff000000-0x1ffffffff]
[    0.101514] NetLabel: Initializing
[    0.101514] NetLabel:  domain hash size = 128
[    0.101514] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.101514] NetLabel:  unlabeled traffic allowed by default
[    0.101514] clocksource: Switched to clocksource refined-jiffies
[    0.109530] VFS: Disk quotas dquot_6.6.0
[    0.109545] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.109632] AppArmor: AppArmor Filesystem Enabled
[    0.109657] pnp: PnP ACPI init
[    0.112003] system 00:00: [mem 0xfed40000-0xfed44fff] has been reserved
[    0.112003] system 00:00: Plug and Play ACPI device, IDs PNP0c01 (active)
[    0.112003] system 00:01: [io  0x0680-0x069f] has been reserved
[    0.112003] system 00:01: [io  0x1000-0x100f] has been reserved
[    0.112003] system 00:01: [io  0xffff] has been reserved
[    0.112003] system 00:01: [io  0xffff] has been reserved
[    0.112003] system 00:01: [io  0x0400-0x0453] has been reserved
[    0.112003] system 00:01: [io  0x0458-0x047f] has been reserved
[    0.112003] system 00:01: [io  0x0500-0x057f] has been reserved
[    0.112003] system 00:01: [io  0x164e-0x164f] has been reserved
[    0.112003] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.112003] pnp 00:02: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.112003] system 00:03: [io  0x0454-0x0457] has been reserved
[    0.112003] system 00:03: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    0.112003] system 00:04: [io  0x0a00-0x0a1f] has been reserved
[    0.112003] system 00:04: [io  0x0290-0x029f] has been reserved
[    0.112003] system 00:04: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.112003] system 00:05: [io  0x04d0-0x04d1] has been reserved
[    0.112003] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.112003] system 00:06: [mem 0xfed1c000-0xfed1ffff] has been reserved
[    0.112003] system 00:06: [mem 0xfed10000-0xfed17fff] has been reserved
[    0.112003] system 00:06: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.112003] system 00:06: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.112003] system 00:06: [mem 0xf8000000-0xfbffffff] has been reserved
[    0.112003] system 00:06: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.112003] system 00:06: [mem 0xfed90000-0xfed93fff] has been reserved
[    0.112003] system 00:06: [mem 0xfed45000-0xfed8ffff] has been reserved
[    0.112003] system 00:06: [mem 0xff000000-0xffffffff] has been reserved
[    0.112003] system 00:06: [mem 0xfee00000-0xfeefffff] could not be reserved
[    0.112003] system 00:06: [mem 0xf0400000-0xf0400fff] has been reserved
[    0.112003] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.112003] pnp: PnP ACPI: found 7 devices
[    0.116134] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.116144] clocksource: Switched to clocksource acpi_pm
[    0.116176] pci 0000:00:01.0: PCI bridge to [bus 01]
[    0.116178] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    0.116181] pci 0000:00:01.0:   bridge window [mem 0xf7e00000-0xf7efffff]
[    0.116183] pci 0000:00:01.0:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.116185] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    0.116202] pci 0000:00:1c.5: PCI bridge to [bus 03]
[    0.116203] pci 0000:00:1c.5:   bridge window [io  0xd000-0xdfff]
[    0.116209] pci 0000:00:1c.5:   bridge window [mem 0xf0300000-0xf03fffff 64bit pref]
[    0.116214] pci 0000:00:1c.6: PCI bridge to [bus 04]
[    0.116218] pci 0000:00:1c.6:   bridge window [mem 0xf7d00000-0xf7dfffff]
[    0.116225] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.116227] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.116228] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.116229] pci_bus 0000:00: resource 7 [mem 0x000d0000-0x000d3fff window]
[    0.116230] pci_bus 0000:00: resource 8 [mem 0x000d4000-0x000d7fff window]
[    0.116231] pci_bus 0000:00: resource 9 [mem 0x000d8000-0x000dbfff window]
[    0.116232] pci_bus 0000:00: resource 10 [mem 0x000dc000-0x000dffff window]
[    0.116233] pci_bus 0000:00: resource 11 [mem 0x000e0000-0x000e3fff window]
[    0.116234] pci_bus 0000:00: resource 12 [mem 0x000e4000-0x000e7fff window]
[    0.116235] pci_bus 0000:00: resource 13 [mem 0xe0000000-0xfeafffff window]
[    0.116237] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    0.116238] pci_bus 0000:01: resource 1 [mem 0xf7e00000-0xf7efffff]
[    0.116239] pci_bus 0000:01: resource 2 [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.116240] pci_bus 0000:03: resource 0 [io  0xd000-0xdfff]
[    0.116241] pci_bus 0000:03: resource 2 [mem 0xf0300000-0xf03fffff 64bit pref]
[    0.116242] pci_bus 0000:04: resource 1 [mem 0xf7d00000-0xf7dfffff]
[    0.116330] NET: Registered protocol family 2
[    0.116505] TCP established hash table entries: 65536 (order: 7, 524288 bytes)
[    0.116631] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.116830] TCP: Hash tables configured (established 65536 bind 65536)
[    0.116860] UDP hash table entries: 4096 (order: 5, 131072 bytes)
[    0.116890] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes)
[    0.116942] NET: Registered protocol family 1
[    0.117392] pci 0000:01:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.117397] PCI: CLS mismatch (64 != 32), using 64 bytes
[    0.117569] Unpacking initramfs...
[    0.730881] Freeing initrd memory: 53312K
[    0.730933] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.730936] software IO TLB [mem 0xd9251000-0xdd251000] (64MB) mapped at [        (ptrval)-        (ptrval)]
[    0.731172] Scanning for low memory corruption every 60 seconds
[    0.731695] Initialise system trusted keyrings
[    0.731703] Key type blacklist registered
[    0.731729] workingset: timestamp_bits=36 max_order=21 bucket_order=0
[    0.732596] zbud: loaded
[    0.732955] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.733054] fuse init (API version 7.26)
[    0.734069] Key type asymmetric registered
[    0.734070] Asymmetric key parser 'x509' registered
[    0.734089] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    0.734114] io scheduler noop registered
[    0.734114] io scheduler deadline registered
[    0.734146] io scheduler cfq registered (default)
[    0.734699] vesafb: mode is 1920x1080x32, linelength=7680, pages=0
[    0.734699] vesafb: scrolling: redraw
[    0.734701] vesafb: Truecolor: size=0:8:8:8, shift=0:16:8:0
[    0.734715] vesafb: framebuffer at 0xe0000000, mapped to 0x        (ptrval), using 8128k, total 8128k
[    0.734779] Console: switching to colour frame buffer device 240x67
[    0.734801] fb0: VESA VGA frame buffer device
[    0.734811] intel_idle: MWAIT substates: 0x1120
[    0.734812] intel_idle: v0.4.1 model 0x2A
[    0.734911] intel_idle: lapic_timer_reliable_states 0xffffffff
[    0.734984] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
[    0.735008] ACPI: Power Button [PWRB]
[    0.735035] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input1
[    0.735051] ACPI: Power Button [PWRF]
[    0.735725] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    0.735878] thermal LNXTHERM:00: registered as thermal_zone0
[    0.735879] ACPI: Thermal Zone [TZ00] (28 C)
[    0.736164] thermal LNXTHERM:01: registered as thermal_zone1
[    0.736165] ACPI: Thermal Zone [TZ01] (30 C)
[    0.736262] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.737815] Linux agpgart interface v0.103
[    0.738984] loop: module loaded
[    0.739103] libphy: Fixed MDIO Bus: probed
[    0.739104] tun: Universal TUN/TAP device driver, 1.6
[    0.739127] PPP generic driver version 2.4.2
[    0.739157] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.739158] ehci-pci: EHCI PCI platform driver
[    0.739252] ehci-pci 0000:00:1a.0: EHCI Host Controller
[    0.739256] ehci-pci 0000:00:1a.0: new USB bus registered, assigned bus number 1
[    0.739266] ehci-pci 0000:00:1a.0: debug port 2
[    0.743174] ehci-pci 0000:00:1a.0: cache line size of 64 is not supported
[    0.743183] ehci-pci 0000:00:1a.0: irq 23, io mem 0xf7f18000
[    0.756033] ehci-pci 0000:00:1a.0: USB 2.0 started, EHCI 1.00
[    0.756096] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    0.756098] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.756101] usb usb1: Product: EHCI Host Controller
[    0.756103] usb usb1: Manufacturer: Linux 4.15.0-33-generic ehci_hcd
[    0.756105] usb usb1: SerialNumber: 0000:00:1a.0
[    0.756271] hub 1-0:1.0: USB hub found
[    0.756278] hub 1-0:1.0: 2 ports detected
[    0.756466] ehci-pci 0000:00:1d.0: EHCI Host Controller
[    0.756470] ehci-pci 0000:00:1d.0: new USB bus registered, assigned bus number 2
[    0.756480] ehci-pci 0000:00:1d.0: debug port 2
[    0.760386] ehci-pci 0000:00:1d.0: cache line size of 64 is not supported
[    0.760390] ehci-pci 0000:00:1d.0: irq 23, io mem 0xf7f17000
[    0.776039] ehci-pci 0000:00:1d.0: USB 2.0 started, EHCI 1.00
[    0.776092] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002
[    0.776102] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.776103] usb usb2: Product: EHCI Host Controller
[    0.776104] usb usb2: Manufacturer: Linux 4.15.0-33-generic ehci_hcd
[    0.776105] usb usb2: SerialNumber: 0000:00:1d.0
[    0.776247] hub 2-0:1.0: USB hub found
[    0.776252] hub 2-0:1.0: 2 ports detected
[    0.776368] ehci-platform: EHCI generic platform driver
[    0.776374] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.776377] ohci-pci: OHCI PCI platform driver
[    0.776382] ohci-platform: OHCI generic platform driver
[    0.776387] uhci_hcd: USB Universal Host Controller Interface driver
[    0.776479] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.776484] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 3
[    0.777556] xhci_hcd 0000:00:14.0: hcc params 0x20007181 hci version 0x100 quirks 0x0000b930
[    0.777560] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
[    0.777664] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002
[    0.777665] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.777666] usb usb3: Product: xHCI Host Controller
[    0.777667] usb usb3: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    0.777668] usb usb3: SerialNumber: 0000:00:14.0
[    0.777807] hub 3-0:1.0: USB hub found
[    0.777816] hub 3-0:1.0: 4 ports detected
[    0.778139] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.778142] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 4
[    0.778144] xhci_hcd 0000:00:14.0: Host supports USB 3.0  SuperSpeed
[    0.778168] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003
[    0.778169] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.778170] usb usb4: Product: xHCI Host Controller
[    0.778171] usb usb4: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    0.778172] usb usb4: SerialNumber: 0000:00:14.0
[    0.778308] hub 4-0:1.0: USB hub found
[    0.778317] hub 4-0:1.0: 4 ports detected
[    0.778713] xhci_hcd 0000:04:00.0: xHCI Host Controller
[    0.778717] xhci_hcd 0000:04:00.0: new USB bus registered, assigned bus number 5
[    0.838095] xhci_hcd 0000:04:00.0: hcc params 0x0200f180 hci version 0x96 quirks 0x00080000
[    0.838285] usb usb5: New USB device found, idVendor=1d6b, idProduct=0002
[    0.838287] usb usb5: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.838288] usb usb5: Product: xHCI Host Controller
[    0.838289] usb usb5: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    0.838290] usb usb5: SerialNumber: 0000:04:00.0
[    0.838422] hub 5-0:1.0: USB hub found
[    0.838431] hub 5-0:1.0: 2 ports detected
[    0.838500] xhci_hcd 0000:04:00.0: xHCI Host Controller
[    0.838502] xhci_hcd 0000:04:00.0: new USB bus registered, assigned bus number 6
[    0.838505] xhci_hcd 0000:04:00.0: Host supports USB 3.0  SuperSpeed
[    0.838522] usb usb6: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.838536] usb usb6: New USB device found, idVendor=1d6b, idProduct=0003
[    0.838537] usb usb6: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.838538] usb usb6: Product: xHCI Host Controller
[    0.838539] usb usb6: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    0.838540] usb usb6: SerialNumber: 0000:04:00.0
[    0.838662] hub 6-0:1.0: USB hub found
[    0.838671] hub 6-0:1.0: 2 ports detected
[    0.838763] i8042: PNP: No PS/2 controller found.
[    0.838875] mousedev: PS/2 mouse device common for all mice
[    0.839118] rtc_cmos 00:02: RTC can wake from S4
[    0.839287] rtc_cmos 00:02: rtc core: registered rtc_cmos as rtc0
[    0.839309] rtc_cmos 00:02: alarms up to one month, y3k, 242 bytes nvram
[    0.839313] i2c /dev entries driver
[    0.839347] device-mapper: uevent: version 1.0.3
[    0.839427] device-mapper: ioctl: 4.37.0-ioctl (2017-09-20) initialised: dm-devel@redhat.com
[    0.839431] intel_pstate: Intel P-state driver initializing
[    0.839703] ledtrig-cpu: registered to indicate activity on CPUs
[    0.840135] NET: Registered protocol family 10
[    0.843672] Segment Routing with IPv6
[    0.843684] NET: Registered protocol family 17
[    0.843717] Key type dns_resolver registered
[    0.843897] RAS: Correctable Errors collector initialized.
[    0.843919] microcode: sig=0x206a7, pf=0x2, revision=0x2e
[    0.843953] microcode: Microcode Update Driver: v2.2.
[    0.843960] sched_clock: Marking stable (843950781, 0)->(893469186, -49518405)
[    0.844121] registered taskstats version 1
[    0.844131] Loading compiled-in X.509 certificates
[    0.846128] Loaded X.509 cert 'Build time autogenerated kernel key: d918b280ed158d77154089242222928ec1ab43e6'
[    0.846142] zswap: loaded using pool lzo/zbud
[    0.848961] Key type big_key registered
[    0.848964] Key type trusted registered
[    0.850197] Key type encrypted registered
[    0.850199] AppArmor: AppArmor sha1 policy hashing enabled
[    0.850201] ima: No TPM chip found, activating TPM-bypass! (rc=-19)
[    0.850223] evm: HMAC attrs: 0x1
[    0.850423]   Magic number: 2:357:552
[    0.850433] tty ttyS28: hash matches
[    0.850441] clockevents clockevent3: hash matches
[    0.850456] acpi PNP0C0F:03: hash matches
[    0.850528] rtc_cmos 00:02: setting system clock to 2018-09-07 22:32:21 UTC (1536359541)
[    0.850565] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    0.850566] EDD information not available.
[    0.852440] Freeing unused kernel memory: 2404K
[    0.872038] Write protecting the kernel read-only data: 20480k
[    0.872634] Freeing unused kernel memory: 2008K
[    0.875923] Freeing unused kernel memory: 1892K
[    0.881623] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    0.881623] x86/mm: Checking user space page tables
[    0.887469] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    0.896227] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    0.896294] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    0.896303] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    0.952467] r8169 Gigabit Ethernet driver 2.3LK-NAPI loaded
[    0.952477] r8169 0000:03:00.0: can't disable ASPM; OS doesn't have ASPM control
[    0.953649] r8169 0000:03:00.0 eth0: RTL8168f/8111f at 0x        (ptrval), 50:46:5d:b7:16:b7, XID 08000800 IRQ 30
[    0.953650] r8169 0000:03:00.0 eth0: jumbo features [frames: 9200 bytes, tx checksumming: ko]
[    0.955377] ahci 0000:00:1f.2: version 3.0
[    0.955523] ahci 0000:00:1f.2: AHCI 0001.0300 32 slots 6 ports 6 Gbps 0x2 impl SATA mode
[    0.955525] ahci 0000:00:1f.2: flags: 64bit ncq led clo pio slum part ems apst 
[    0.958172] r8169 0000:03:00.0 enp3s0: renamed from eth0
[    0.959489] scsi host0: ahci
[    0.959570] scsi host1: ahci
[    0.963325] amdkcl: loading out-of-tree module taints kernel.
[    0.963341] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    0.968016] scsi host2: ahci
[    0.968194] scsi host3: ahci
[    0.996025] scsi host4: ahci
[    0.996190] scsi host5: ahci
[    0.996243] ata1: DUMMY
[    0.996245] ata2: SATA max UDMA/133 abar m2048@0xf7f16000 port 0xf7f16180 irq 31
[    0.996246] ata3: DUMMY
[    0.996247] ata4: DUMMY
[    0.996247] ata5: DUMMY
[    0.996248] ata6: DUMMY
[    1.013095] Warning: fail to get symbol drm_fb_helper_release_fbi, replace it with kcl stub
[    1.048306] [drm] amdgpu kernel modesetting enabled.
[    1.050215] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    1.050215] AMD IOMMUv2 functionality not available on this system
[    1.051304] CRAT table not found
[    1.051306] Virtual CRAT table created for CPU
[    1.051307] Parsing CRAT table with 1 nodes
[    1.051308] Creating topology SYSFS entries
[    1.051315] Topology: Add CPU node
[    1.051315] Finished initializing topology
[    1.052769] kfd kfd: Initialized module
[    1.052962] checking generic (e0000000 7f0000) vs hw (e0000000 10000000)
[    1.052963] fb: switching to amdgpudrmfb from VESA VGA
[    1.052984] Console: switching to colour dummy device 80x25
[    1.053302] [drm] initializing kernel modesetting (POLARIS10 0x1002:0x67DF 0x1DA2:0xE366 0xE7).
[    1.053307] [drm] register mmio base: 0xF7E00000
[    1.053308] [drm] register mmio size: 262144
[    1.053312] [drm] add ip block number 0 <vi_common>
[    1.053312] [drm] add ip block number 1 <gmc_v8_0>
[    1.053313] [drm] add ip block number 2 <tonga_ih>
[    1.053314] [drm] add ip block number 3 <amdgpu_powerplay>
[    1.053315] [drm] add ip block number 4 <dm>
[    1.053315] [drm] add ip block number 5 <gfx_v8_0>
[    1.053316] [drm] add ip block number 6 <sdma_v3_0>
[    1.053317] [drm] add ip block number 7 <uvd_v6_0>
[    1.053317] [drm] add ip block number 8 <vce_v3_0>
[    1.053320] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[    1.053324] [drm] probing gen 2 caps for device 8086:101 = 2212d02/0
[    1.053326] [drm] probing mlw for device 8086:101 = 2212d02
[    1.053332] [drm] UVD is enabled in VM mode
[    1.053333] [drm] UVD ENC is enabled in VM mode
[    1.053334] [drm] VCE enabled in VM mode
[    1.053507] resource sanity check: requesting [mem 0x000c0000-0x000dffff], which spans more than PCI Bus 0000:00 [mem 0x000d0000-0x000d3fff window]
[    1.053511] caller pci_map_rom+0x5d/0xf0 mapping multiple BARs
[    1.053512] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.053533] ATOM BIOS: 113-1E3660U-O51
[    1.053554] [drm] vm size is 64 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[    1.053580] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[    1.053582] amdgpu 0000:01:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    1.053585] [drm] Detected VRAM RAM=8192M, BAR=256M
[    1.053585] [drm] RAM width 256bits GDDR5
[    1.053623] [TTM] Zone  kernel: Available graphics memory: 7118955 kiB
[    1.053624] [TTM] Initializing pool allocator
[    1.053627] [TTM] Initializing DMA pool allocator
[    1.053902] [drm] amdgpu: 8192M of VRAM memory ready
[    1.053903] [drm] amdgpu: 8192M of GTT memory ready.
[    1.053909] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    1.053939] [drm] PCIE GART of 256M enabled (table at 0x000000F400040000).
[    1.054036] [drm] Chained IB support enabled!
[    1.055031] [drm] Found UVD firmware Version: 1.79 Family ID: 16
[    1.055035] [drm] UVD ENC is disabled
[    1.055348] [drm] Found VCE firmware Version: 52.4 Binary ID: 3
[    1.107693] usb 1-1: new high-speed USB device number 2 using ehci-pci
[    1.107777] [drm] DM_PPLIB: values for Engine clock
[    1.107778] [drm] DM_PPLIB:	 30000
[    1.107778] [drm] DM_PPLIB:	 60000
[    1.107779] [drm] DM_PPLIB:	 90000
[    1.107779] [drm] DM_PPLIB:	 114500
[    1.107779] [drm] DM_PPLIB:	 121500
[    1.107780] [drm] DM_PPLIB:	 125700
[    1.107780] [drm] DM_PPLIB:	 130000
[    1.107780] [drm] DM_PPLIB:	 141100
[    1.107781] [drm] DM_PPLIB: Validation clocks:
[    1.107781] [drm] DM_PPLIB:    engine_max_clock: 141100
[    1.107782] [drm] DM_PPLIB:    memory_max_clock: 200000
[    1.107782] [drm] DM_PPLIB:    level           : 0
[    1.107783] [drm] DM_PPLIB: values for Memory clock
[    1.107783] [drm] DM_PPLIB:	 30000
[    1.107784] [drm] DM_PPLIB:	 100000
[    1.107784] [drm] DM_PPLIB:	 200000
[    1.107784] [drm] DM_PPLIB: Validation clocks:
[    1.107785] [drm] DM_PPLIB:    engine_max_clock: 141100
[    1.107785] [drm] DM_PPLIB:    memory_max_clock: 200000
[    1.107786] [drm] DM_PPLIB:    level           : 0
[    1.120053] [drm] Display Core initialized with v3.1.32!
[    1.133624] [drm] SADs count is: -2, don't need to read it
[    1.133643] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.133643] [drm] Driver supports precise vblank timestamp query.
[    1.156001] usb 2-1: new high-speed USB device number 2 using ehci-pci
[    1.182215] usb 5-1: new high-speed USB device number 2 using xhci_hcd
[    1.182466] [drm] UVD initialized successfully.
[    1.282240] [drm] VCE initialized successfully.
[    1.308706] usb 1-1: New USB device found, idVendor=8087, idProduct=0024
[    1.308708] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.309017] hub 1-1:1.0: USB hub found
[    1.309100] hub 1-1:1.0: 6 ports detected
[    1.310354] ata2: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.312241] ACPI Error: [DSSP] Namespace lookup failure, AE_NOT_FOUND (20170831/psargs-364)
[    1.312249] No Local Variables are initialized for Method [_GTF]
[    1.312250] No Arguments are initialized for method [_GTF]
[    1.312252] ACPI Error: Method parse/execution failed \_SB.PCI0.SAT0.SPT1._GTF, AE_NOT_FOUND (20170831/psparse-550)
[    1.312339] usb 2-1: New USB device found, idVendor=8087, idProduct=0024
[    1.312343] usb 2-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.312512] ata2.00: ATA-8: WDC WD10EARX-00N0YB0, 51.0AB51, max UDMA/133
[    1.312513] ata2.00: 1953525168 sectors, multi 16: LBA48 NCQ (depth 31/32), AA
[    1.312596] hub 2-1:1.0: USB hub found
[    1.312691] hub 2-1:1.0: 8 ports detected
[    1.314332] ACPI Error: [DSSP] Namespace lookup failure, AE_NOT_FOUND (20170831/psargs-364)
[    1.314339] No Local Variables are initialized for Method [_GTF]
[    1.314340] No Arguments are initialized for method [_GTF]
[    1.314341] ACPI Error: Method parse/execution failed \_SB.PCI0.SAT0.SPT1._GTF, AE_NOT_FOUND (20170831/psparse-550)
[    1.314540] ata2.00: configured for UDMA/133
[    1.314725] scsi 1:0:0:0: Direct-Access     ATA      WDC WD10EARX-00N AB51 PQ: 0 ANSI: 5
[    1.314986] sd 1:0:0:0: Attached scsi generic sg0 type 0
[    1.315017] sd 1:0:0:0: [sda] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    1.315018] sd 1:0:0:0: [sda] 4096-byte physical blocks
[    1.315038] sd 1:0:0:0: [sda] Write Protect is off
[    1.315040] sd 1:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    1.315061] sd 1:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.349202]  sda: sda1 sda2 < sda5 >
[    1.350189] sd 1:0:0:0: [sda] Attached SCSI disk
[    1.518021] usb 5-1: New USB device found, idVendor=0951, idProduct=1665
[    1.518025] usb 5-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    1.518027] usb 5-1: Product: DataTraveler 2.0
[    1.518029] usb 5-1: Manufacturer: Kingston
[    1.518031] usb 5-1: SerialNumber: 60A44C413AC0FEC0C991264C
[    1.521655] usb-storage 5-1:1.0: USB Mass Storage device detected
[    1.521839] scsi host6: usb-storage 5-1:1.0
[    1.521899] usbcore: registered new interface driver usb-storage
[    1.522898] usbcore: registered new interface driver uas
[    1.599996] usb 2-1.6: new high-speed USB device number 3 using ehci-pci
[    1.709060] usb 2-1.6: New USB device found, idVendor=1a40, idProduct=0201
[    1.709063] usb 2-1.6: New USB device strings: Mfr=0, Product=1, SerialNumber=0
[    1.709073] usb 2-1.6: Product: USB 2.0 Hub [MTT]
[    1.709352] hub 2-1.6:1.0: USB hub found
[    1.709450] hub 2-1.6:1.0: 7 ports detected
[    1.759995] tsc: Refined TSC clocksource calibration: 3309.719 MHz
[    1.760005] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x2fb5294632d, max_idle_ns: 440795265502 ns
[    1.787986] usb 2-1.8: new full-speed USB device number 4 using ehci-pci
[    1.795660] [drm] fb mappable at 0xE03F2000
[    1.795662] [drm] vram apper at 0xE0000000
[    1.795663] [drm] size 8294400
[    1.795664] [drm] fb depth is 24
[    1.795665] [drm]    pitch is 7680
[    1.795792] fbcon: amdgpudrmfb (fb0) is primary device
[    1.795844] Console: switching to colour frame buffer device 240x67
[    1.795866] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    1.898698] usb 2-1.8: New USB device found, idVendor=058f, idProduct=9360
[    1.898700] usb 2-1.8: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    1.898701] usb 2-1.8: Product: USB Reader
[    1.898702] usb 2-1.8: Manufacturer:  
[    1.898703] usb 2-1.8: SerialNumber: 2004888
[    1.899153] usb-storage 2-1.8:1.0: USB Mass Storage device detected
[    1.899373] scsi host7: usb-storage 2-1.8:1.0
[    1.971282] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:01:00.0 on minor 0
[    2.001853] random: fast init done
[    2.015989] usb 2-1.6.1: new low-speed USB device number 5 using ehci-pci
[    2.124568] EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
[    2.150378] usb 2-1.6.1: New USB device found, idVendor=1c4f, idProduct=0024
[    2.150382] usb 2-1.6.1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    2.150384] usb 2-1.6.1: Product: USB Keyboard
[    2.150387] usb 2-1.6.1: Manufacturer: SIGMACHIP
[    2.154141] hidraw: raw HID events driver (C) Jiri Kosina
[    2.159915] usbcore: registered new interface driver usbhid
[    2.159915] usbhid: USB HID core driver
[    2.161397] input: SIGMACHIP USB Keyboard as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.6/2-1.6.1/2-1.6.1:1.0/0003:1C4F:0024.0001/input/input2
[    2.224242] hid-generic 0003:1C4F:0024.0001: input,hidraw0: USB HID v1.11 Keyboard [SIGMACHIP USB Keyboard] on usb-0000:00:1d.0-1.6.1/input0
[    2.224351] input: SIGMACHIP USB Keyboard as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.6/2-1.6.1/2-1.6.1:1.1/0003:1C4F:0024.0002/input/input3
[    2.247987] usb 2-1.6.5: new full-speed USB device number 6 using ehci-pci
[    2.284224] hid-generic 0003:1C4F:0024.0002: input,hidraw1: USB HID v1.11 Device [SIGMACHIP USB Keyboard] on usb-0000:00:1d.0-1.6.1/input1
[    2.378384] usb 2-1.6.5: New USB device found, idVendor=1d57, idProduct=ad03
[    2.378386] usb 2-1.6.5: New USB device strings: Mfr=2, Product=1, SerialNumber=0
[    2.378387] usb 2-1.6.5: Product: Gaming Mouse
[    2.378388] usb 2-1.6.5: Manufacturer: SOAI
[    2.379438] input: SOAI Gaming Mouse as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.6/2-1.6.5/2-1.6.5:1.0/0003:1D57:AD03.0003/input/input4
[    2.436178] hid-generic 0003:1D57:AD03.0003: input,hidraw2: USB HID v1.10 Keyboard [SOAI Gaming Mouse] on usb-0000:00:1d.0-1.6.5/input0
[    2.437495] input: SOAI Gaming Mouse as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.6/2-1.6.5/2-1.6.5:1.1/0003:1D57:AD03.0004/input/input5
[    2.496265] hid-generic 0003:1D57:AD03.0004: input,hidraw3: USB HID v1.10 Mouse [SOAI Gaming Mouse] on usb-0000:00:1d.0-1.6.5/input1
[    2.549121] scsi 6:0:0:0: Direct-Access     Kingston DataTraveler 2.0 1.00 PQ: 0 ANSI: 4
[    2.549474] sd 6:0:0:0: Attached scsi generic sg1 type 0
[    2.549713] sd 6:0:0:0: [sdb] 15131636 512-byte logical blocks: (7.75 GB/7.21 GiB)
[    2.549930] sd 6:0:0:0: [sdb] Write Protect is off
[    2.549932] sd 6:0:0:0: [sdb] Mode Sense: 45 00 00 00
[    2.550146] sd 6:0:0:0: [sdb] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    2.552233]  sdb: sdb1
[    2.553193] sd 6:0:0:0: [sdb] Attached SCSI removable disk
[    2.784169] clocksource: Switched to clocksource tsc
[    2.913166] scsi 7:0:0:0: Direct-Access     Generic  USB SD Reader    1.00 PQ: 0 ANSI: 0
[    2.913916] scsi 7:0:0:1: Direct-Access     Generic  USB CF Reader    1.01 PQ: 0 ANSI: 0
[    2.914667] scsi 7:0:0:2: Direct-Access     Generic  USB SM Reader    1.02 PQ: 0 ANSI: 0
[    2.915435] scsi 7:0:0:3: Direct-Access     Generic  USB MS Reader    1.03 PQ: 0 ANSI: 0
[    2.915640] sd 7:0:0:0: Attached scsi generic sg2 type 0
[    2.915728] sd 7:0:0:1: Attached scsi generic sg3 type 0
[    2.915817] sd 7:0:0:2: Attached scsi generic sg4 type 0
[    2.915890] sd 7:0:0:3: Attached scsi generic sg5 type 0
[    2.923152] sd 7:0:0:0: [sdc] Attached SCSI removable disk
[    2.923795] sd 7:0:0:1: [sdd] Attached SCSI removable disk
[    2.924667] sd 7:0:0:2: [sde] Attached SCSI removable disk
[    2.925539] sd 7:0:0:3: [sdf] Attached SCSI removable disk
[    3.259299] systemd[1]: systemd 229 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ -LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN)
[    3.276075] systemd[1]: Detected architecture x86-64.
[    3.276265] systemd[1]: Set hostname to <alex-System-Product-Name-Invalid-entry-length-16-Fixed-up-to-11>.
[    3.815776] random: crng init done
[    3.815779] random: 7 urandom warning(s) missed due to ratelimiting
[    3.961418] systemd[1]: Listening on udev Kernel Socket.
[    3.961459] systemd[1]: Reached target User and Group Name Lookups.
[    3.961478] systemd[1]: Listening on fsck to fsckd communication Socket.
[    3.961506] systemd[1]: Started Trigger resolvconf update for networkd DNS.
[    3.961515] systemd[1]: Reached target Remote File Systems (Pre).
[    3.961520] systemd[1]: Reached target Remote File Systems.
[    3.961631] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[    4.793010] lp: driver loaded but no devices found
[    4.801558] ppdev: user-space parallel port driver
[   10.882414] EXT4-fs (sda1): re-mounted. Opts: errors=remount-ro
[   10.942384] systemd-journald[305]: Received request to flush runtime journal from PID 1
[   10.997561] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[   11.012442] ACPI Warning: SystemIO range 0x0000000000000428-0x000000000000042F conflicts with OpRegion 0x0000000000000400-0x000000000000047F (\PMIO) (20170831/utaddress-247)
[   11.012448] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver
[   11.012450] ACPI Warning: SystemIO range 0x0000000000000540-0x000000000000054F conflicts with OpRegion 0x0000000000000500-0x0000000000000563 (\GPIO) (20170831/utaddress-247)
[   11.012453] ACPI Warning: SystemIO range 0x0000000000000540-0x000000000000054F conflicts with OpRegion 0x0000000000000500-0x000000000000057F (\_SB.PCI0.LPCB.GPBX) (20170831/utaddress-247)
[   11.012456] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver
[   11.012457] ACPI Warning: SystemIO range 0x0000000000000530-0x000000000000053F conflicts with OpRegion 0x0000000000000500-0x0000000000000563 (\GPIO) (20170831/utaddress-247)
[   11.012459] ACPI Warning: SystemIO range 0x0000000000000530-0x000000000000053F conflicts with OpRegion 0x0000000000000500-0x000000000000057F (\_SB.PCI0.LPCB.GPBX) (20170831/utaddress-247)
[   11.012462] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver
[   11.012462] ACPI Warning: SystemIO range 0x0000000000000500-0x000000000000052F conflicts with OpRegion 0x0000000000000500-0x0000000000000563 (\GPIO) (20170831/utaddress-247)
[   11.012465] ACPI Warning: SystemIO range 0x0000000000000500-0x000000000000052F conflicts with OpRegion 0x0000000000000500-0x000000000000057F (\_SB.PCI0.LPCB.GPBX) (20170831/utaddress-247)
[   11.012467] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver
[   11.012468] lpc_ich: Resource conflict(s) found affecting gpio_ich
[   11.038850] RAPL PMU: API unit is 2^-32 Joules, 3 fixed counters, 163840 ms ovfl timer
[   11.038851] RAPL PMU: hw unit of domain pp0-core 2^-16 Joules
[   11.038852] RAPL PMU: hw unit of domain package 2^-16 Joules
[   11.038852] RAPL PMU: hw unit of domain pp1-gpu 2^-16 Joules
[   11.046963] AVX version of gcm_enc/dec engaged.
[   11.046964] AES CTR mode by8 optimization enabled
[   11.053283] snd_hda_intel 0000:01:00.1: Handle vga_switcheroo audio client
[   11.053285] snd_hda_intel 0000:01:00.1: Force to non-snoop mode
[   11.063508] input: HDA ATI HDMI HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input6
[   11.063587] input: HDA ATI HDMI HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input7
[   11.063662] input: HDA ATI HDMI HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input8
[   11.063727] input: HDA ATI HDMI HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input9
[   11.063789] input: HDA ATI HDMI HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input10
[   11.064019] input: HDA ATI HDMI HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input11
[   11.066761] snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALC892: line_outs=4 (0x14/0x15/0x16/0x17/0x0) type:line
[   11.066763] snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[   11.066764] snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
[   11.066765] snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
[   11.066766] snd_hda_codec_realtek hdaudioC0D0:    dig-out=0x11/0x1e
[   11.066767] snd_hda_codec_realtek hdaudioC0D0:    inputs:
[   11.066768] snd_hda_codec_realtek hdaudioC0D0:      Front Mic=0x19
[   11.066770] snd_hda_codec_realtek hdaudioC0D0:      Rear Mic=0x18
[   11.066771] snd_hda_codec_realtek hdaudioC0D0:      Line=0x1a
[   11.081589] input: HDA Intel PCH Rear Mic as /devices/pci0000:00/0000:00:1b.0/sound/card0/input12
[   11.081629] input: HDA Intel PCH Line as /devices/pci0000:00/0000:00:1b.0/sound/card0/input13
[   11.081668] input: HDA Intel PCH Line Out Front as /devices/pci0000:00/0000:00:1b.0/sound/card0/input14
[   11.081708] input: HDA Intel PCH Line Out Surround as /devices/pci0000:00/0000:00:1b.0/sound/card0/input15
[   11.081744] input: HDA Intel PCH Line Out CLFE as /devices/pci0000:00/0000:00:1b.0/sound/card0/input16
[   11.081777] input: HDA Intel PCH Line Out Side as /devices/pci0000:00/0000:00:1b.0/sound/card0/input17
[   11.091479] intel_rapl: Found RAPL domain package
[   11.091480] intel_rapl: Found RAPL domain core
[   11.091481] intel_rapl: Found RAPL domain uncore
[   11.091485] intel_rapl: RAPL package 0 domain package locked by BIOS
[   11.108427] asus_wmi: ASUS WMI generic driver loaded
[   11.109400] asus_wmi: Initialization: 0x0
[   11.109430] asus_wmi: BIOS WMI version: 0.9
[   11.109484] asus_wmi: SFUN value: 0x0
[   11.109978] input: Eee PC WMI hotkeys as /devices/platform/eeepc-wmi/input/input18
[   11.110424] asus_wmi: Number of fans: 1
[   11.699432] audit: type=1400 audit(1536359552.341:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=710 comm="apparmor_parser"
[   11.699435] audit: type=1400 audit(1536359552.341:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=710 comm="apparmor_parser"
[   11.699437] audit: type=1400 audit(1536359552.341:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=710 comm="apparmor_parser"
[   11.699439] audit: type=1400 audit(1536359552.341:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=710 comm="apparmor_parser"
[   11.699831] audit: type=1400 audit(1536359552.341:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session" pid=709 comm="apparmor_parser"
[   11.699833] audit: type=1400 audit(1536359552.341:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session//chromium" pid=709 comm="apparmor_parser"
[   11.706439] audit: type=1400 audit(1536359552.349:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince" pid=712 comm="apparmor_parser"
[   11.706442] audit: type=1400 audit(1536359552.349:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//sanitized_helper" pid=712 comm="apparmor_parser"
[   11.706443] audit: type=1400 audit(1536359552.349:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer" pid=712 comm="apparmor_parser"
[   11.706444] audit: type=1400 audit(1536359552.349:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer//sanitized_helper" pid=712 comm="apparmor_parser"
[   13.351497] Adding 7803900k swap on /dev/sda5.  Priority:-2 extents:1 across:7803900k FS
[   16.852897] IPv6: ADDRCONF(NETDEV_UP): enp3s0: link is not ready
[   17.194224] r8169 0000:03:00.0 enp3s0: link down
[   17.194282] IPv6: ADDRCONF(NETDEV_UP): enp3s0: link is not ready
[   20.147993] r8169 0000:03:00.0 enp3s0: link up
[   20.148000] IPv6: ADDRCONF(NETDEV_CHANGE): enp3s0: link becomes ready
```