# rocminfo 4104 / ERROR: clGetPlatformIDs(-1001)

- **Issue #:** 760
- **State:** closed
- **Created:** 2019-04-11T22:35:28Z
- **Updated:** 2019-04-12T00:16:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/760

I'm having an issue installing ROCm, even though all requirements are met.
I followed the steps described at the [Install Guide](https://rocm.github.io/ROCmInstall.html).
Anyway, the [test command's](https://rocm.github.io/ROCmInstall.html#test-basic-rocm-installation) for a successful installation failed.

#### Test commands:

```
/opt/rocm/bin/rocminfo
```
```
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.2/rocminfo/rocminfo.cc. Call returned 4104
```
---
```
/opt/rocm/opencl/bin/x86_64/clinfo
```
```
ERROR: clGetPlatformIDs(-1001)
```


#### Information about the system:

```
uname -a
```
```
Linux sherlock 4.15.0-47-generic #50-Ubuntu SMP Wed Mar 13 10:44:52 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```
---
```
dkms status
```
```
amdgpu, 2.2-31, 4.15.0-47-generic, x86_64: installed
```
---
```
lsmod | grep amdgpu
```
```
amdgpu               2703360  1
chash                  16384  1 amdgpu
ttm                   106496  1 amdgpu
drm_kms_helper        167936  2 amdgpu,i915
drm                   401408  18 drm_kms_helper,amdgpu,i915,ttm
i2c_algo_bit           16384  2 amdgpu,i915
```
---
```
lsmod | grep amdkfd
```
```
amdgpu               2703360  1
chash                  16384  1 amdgpu
ttm                   106496  1 amdgpu
drm_kms_helper        167936  2 amdgpu,i915
drm                   401408  18 drm_kms_helper,amdgpu,i915,ttm
i2c_algo_bit           16384  2 amdgpu,i915
```
---
```
groups
```
```
moritz adm cdrom sudo dip video plugdev lpadmin sambashare
```
---
```
lspci | grep VGA
```
```
00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620 (rev 07)
```
---
```
lspci -vvv
```
```
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 08)
	Subsystem: Lenovo Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
	Latency: 0
	Capabilities: <access denied>

00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620 (rev 07) (prog-if 00 [VGA controller])
	Subsystem: Lenovo UHD Graphics 620
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 139
	Region 0: Memory at f1000000 (64-bit, non-prefetchable) [size=16M]
	Region 2: Memory at d0000000 (64-bit, prefetchable) [size=256M]
	Region 4: I/O ports at e000 [size=64]
	[virtual] Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: i915
	Kernel modules: i915

00:08.0 System peripheral: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model
	Subsystem: Lenovo Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 255
	Region 0: Memory at f252a000 (64-bit, non-prefetchable) [disabled] [size=4K]
	Capabilities: <access denied>

00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21) (prog-if 30 [XHCI])
	Subsystem: Lenovo Sunrise Point-LP USB 3.0 xHCI Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 127
	Region 0: Memory at f2500000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
	Subsystem: Lenovo Sunrise Point-LP Thermal subsystem
	Control: I/O- Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin C routed to IRQ 18
	Region 0: Memory at f252b000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: intel_pch_thermal
	Kernel modules: intel_pch_thermal

00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
	Subsystem: Lenovo Sunrise Point-LP CSME HECI
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 129
	Region 0: Memory at f252c000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: mei_me
	Kernel modules: mei_me

00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21) (prog-if 01 [AHCI 1.0])
	Subsystem: Lenovo Sunrise Point-LP SATA Controller [AHCI mode]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 128
	Region 0: Memory at f2528000 (32-bit, non-prefetchable) [size=8K]
	Region 1: Memory at f252f000 (32-bit, non-prefetchable) [size=256]
	Region 2: I/O ports at e080 [size=8]
	Region 3: I/O ports at e088 [size=4]
	Region 4: I/O ports at e060 [size=32]
	Region 5: Memory at f252d000 (32-bit, non-prefetchable) [size=2K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 122
	Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
	I/O behind bridge: 0000d000-0000dfff
	Memory behind bridge: f2400000-f24fffff
	Prefetchable memory behind bridge: 00000000e0000000-00000000f01fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 123
	Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
	I/O behind bridge: 0000c000-0000cfff
	Memory behind bridge: f2300000-f23fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 124
	Bus: primary=00, secondary=04, subordinate=04, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: f2200000-f22fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1d.2 PCI bridge: Intel Corporation Device 9d1a (rev f1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin C routed to IRQ 125
	Bus: primary=00, secondary=05, subordinate=05, sec-latency=0
	I/O behind bridge: 0000b000-0000bfff
	Memory behind bridge: f2100000-f21fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1d.3 PCI bridge: Intel Corporation Device 9d1b (rev f1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin D routed to IRQ 126
	Bus: primary=00, secondary=06, subordinate=06, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: f2000000-f20fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1f.0 ISA bridge: Intel Corporation Intel(R) 100 Series Chipset Family LPC Controller/eSPI Controller - 9D4E (rev 21)
	Subsystem: Lenovo Device 5068
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0

00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
	Subsystem: Lenovo Sunrise Point-LP PMC
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Region 0: Memory at f2524000 (32-bit, non-prefetchable) [disabled] [size=16K]

00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
	Subsystem: Lenovo Sunrise Point-LP HD Audio
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 64
	Interrupt: pin A routed to IRQ 132
	Region 0: Memory at f2520000 (64-bit, non-prefetchable) [size=16K]
	Region 4: Memory at f2510000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel, snd_soc_skl

00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
	Subsystem: Lenovo Sunrise Point-LP SMBus
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 255
	Region 0: Memory at f252e000 (64-bit, non-prefetchable) [disabled] [size=256]
	Region 4: I/O ports at efa0 [disabled] [size=32]
	Kernel modules: i2c_i801

02:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon RX 550/550X] (rev c0)
	Subsystem: Lenovo Lexa PRO [Radeon RX 550]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 141
	Region 0: Memory at e0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at f0000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at d000 [size=256]
	Region 5: Memory at f2400000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at f2440000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

03:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 10)
	Subsystem: Lenovo RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	Region 0: I/O ports at c000 [size=256]
	Region 2: Memory at f2304000 (64-bit, non-prefetchable) [size=4K]
	Region 4: Memory at f2300000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: r8169
	Kernel modules: r8169

04:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961 (prog-if 02 [NVM Express])
	Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 16
	NUMA node: 0
	Region 0: Memory at f2200000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: nvme
	Kernel modules: nvme

05:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTL8822BE 802.11a/b/g/n/ac WiFi adapter
	Subsystem: Lenovo Device b023
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 140
	Region 0: I/O ports at b000 [size=256]
	Region 2: Memory at f2100000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: r8822be
	Kernel modules: r8822be

06:00.0 SD Host controller: O2 Micro, Inc. SD/MMC Card Reader Controller (rev 01) (prog-if 01)
	Subsystem: Lenovo SD/MMC Card Reader Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 19
	Region 0: Memory at f2001000 (32-bit, non-prefetchable) [size=4K]
	Region 1: Memory at f2000000 (32-bit, non-prefetchable) [size=2K]
	Capabilities: <access denied>
	Kernel driver in use: sdhci-pci
	Kernel modules: sdhci_pci
```
---
```
lspci -tv
```
```
-[0000:00]-+-00.0  Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
           +-02.0  Intel Corporation UHD Graphics 620
           +-08.0  Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model
           +-14.0  Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller
           +-14.2  Intel Corporation Sunrise Point-LP Thermal subsystem
           +-16.0  Intel Corporation Sunrise Point-LP CSME HECI #1
           +-17.0  Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode]
           +-1c.0-[02]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon RX 550/550X]
           +-1c.4-[03]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           +-1d.0-[04]----00.0  Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961
           +-1d.2-[05]----00.0  Realtek Semiconductor Co., Ltd. RTL8822BE 802.11a/b/g/n/ac WiFi adapter
           +-1d.3-[06]----00.0  O2 Micro, Inc. SD/MMC Card Reader Controller
           +-1f.0  Intel Corporation Intel(R) 100 Series Chipset Family LPC Controller/eSPI Controller - 9D4E
           +-1f.2  Intel Corporation Sunrise Point-LP PMC
           +-1f.3  Intel Corporation Sunrise Point-LP HD Audio
           \-1f.4  Intel Corporation Sunrise Point-LP SMBus
```
---
```
lspci -n
```
```
00:00.0 0600: 8086:5914 (rev 08)
00:02.0 0300: 8086:5917 (rev 07)
00:08.0 0880: 8086:1911
00:14.0 0c03: 8086:9d2f (rev 21)
00:14.2 1180: 8086:9d31 (rev 21)
00:16.0 0780: 8086:9d3a (rev 21)
00:17.0 0106: 8086:9d03 (rev 21)
00:1c.0 0604: 8086:9d10 (rev f1)
00:1c.4 0604: 8086:9d14 (rev f1)
00:1d.0 0604: 8086:9d18 (rev f1)
00:1d.2 0604: 8086:9d1a (rev f1)
00:1d.3 0604: 8086:9d1b (rev f1)
00:1f.0 0601: 8086:9d4e (rev 21)
00:1f.2 0580: 8086:9d21 (rev 21)
00:1f.3 0403: 8086:9d71 (rev 21)
00:1f.4 0c05: 8086:9d23 (rev 21)
02:00.0 0380: 1002:699f (rev c0)
03:00.0 0200: 10ec:8168 (rev 10)
04:00.0 0108: 144d:a804
05:00.0 ff00: 10ec:b822
06:00.0 0805: 1217:8621 (rev 01)
```
---
```
dmesg
```
```
[    0.000000] microcode: microcode updated early to revision 0x96, date = 2018-05-15
[    0.000000] Linux version 4.15.0-47-generic (buildd@lgw01-amd64-001) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #50-Ubuntu SMP Wed Mar 13 10:44:52 UTC 2019 (Ubuntu 4.15.0-47.50-generic 4.15.18)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-47-generic root=UUID=fd23178a-79cb-414e-ae26-f056aa9da9e1 ro quiet splash vt.handoff=1
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x008: 'MPX bounds registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x010: 'MPX CSR'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: xstate_offset[3]:  832, xstate_sizes[3]:   64
[    0.000000] x86/fpu: xstate_offset[4]:  896, xstate_sizes[4]:   64
[    0.000000] x86/fpu: Enabled xstate features 0x1f, context size is 960 bytes, using 'compacted' format.
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000057fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000058000-0x0000000000058fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000059000-0x000000000008bfff] usable
[    0.000000] BIOS-e820: [mem 0x000000000008c000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x0000000094fa1fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000094fa2000-0x0000000094fa2fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x0000000094fa3000-0x0000000094fa3fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000094fa4000-0x000000009e90cfff] usable
[    0.000000] BIOS-e820: [mem 0x000000009e90d000-0x000000009e9c1fff] type 20
[    0.000000] BIOS-e820: [mem 0x000000009e9c2000-0x000000009ff22fff] reserved
[    0.000000] BIOS-e820: [mem 0x000000009ff23000-0x000000009ff99fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x000000009ff9a000-0x000000009fffefff] ACPI data
[    0.000000] BIOS-e820: [mem 0x000000009ffff000-0x000000009fffffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000a0000000-0x00000000a7ffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000a8800000-0x00000000ac7fffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fe010000-0x00000000fe010fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x00000002527fffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] efi: EFI v2.50 by Lenovo
[    0.000000] efi:  SMBIOS=0x9f059000  SMBIOS 3.0=0x9f056000  ACPI=0x9fffe000  ACPI 2.0=0x9fffe014  MPS=0x9feb1000  ESRT=0x9ea9e000  MEMATTR=0x99d48018 
[    0.000000] secureboot: Secure boot could not be determined (mode 0)
[    0.000000] SMBIOS 3.0.0 present.
[    0.000000] DMI: LENOVO 20KQS00000/20KQS00000, BIOS R0PET35W (1.12 ) 01/22/2018
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x252800 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: write-back
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF uncachable
[    0.000000]   C0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 00C0000000 mask 7FC0000000 uncachable
[    0.000000]   1 base 00B0000000 mask 7FF0000000 uncachable
[    0.000000]   2 base 00AC000000 mask 7FFC000000 uncachable
[    0.000000]   3 base 00AA000000 mask 7FFE000000 uncachable
[    0.000000]   4 disabled
[    0.000000]   5 disabled
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000]   8 disabled
[    0.000000]   9 disabled
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000000] e820: last_pfn = 0xa0000 max_arch_pfn = 0x400000000
[    0.000000] esrt: Reserving ESRT space from 0x000000009ea9e000 to 0x000000009ea9e088.
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [        (ptrval)] 60000 size 24576
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x1e673f000, 0x1e673ffff] PGTABLE
[    0.000000] BRK [0x1e6740000, 0x1e6740fff] PGTABLE
[    0.000000] BRK [0x1e6741000, 0x1e6741fff] PGTABLE
[    0.000000] BRK [0x1e6742000, 0x1e6742fff] PGTABLE
[    0.000000] BRK [0x1e6743000, 0x1e6743fff] PGTABLE
[    0.000000] BRK [0x1e6744000, 0x1e6744fff] PGTABLE
[    0.000000] BRK [0x1e6745000, 0x1e6745fff] PGTABLE
[    0.000000] BRK [0x1e6746000, 0x1e6746fff] PGTABLE
[    0.000000] BRK [0x1e6747000, 0x1e6747fff] PGTABLE
[    0.000000] RAMDISK: [mem 0x337cd000-0x35bddfff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x000000009FFFE014 000024 (v02 LENOVO)
[    0.000000] ACPI: XSDT 0x000000009FFC1188 0000E4 (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: FACP 0x000000009FFF7000 0000F4 (v05 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: DSDT 0x000000009FFD1000 021991 (v02 LENOVO SKL      00000000 INTL 20160527)
[    0.000000] ACPI: FACS 0x000000009FF46000 000040
[    0.000000] ACPI: UEFI 0x000000009FF5C000 000042 (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: SSDT 0x000000009FFF9000 003244 (v02 LENOVO SaSsdt   00003000 INTL 20160527)
[    0.000000] ACPI: SSDT 0x000000009FFF8000 0005C6 (v02 LENOVO PerfTune 00001000 INTL 20160527)
[    0.000000] ACPI: HPET 0x000000009FFF6000 000038 (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: APIC 0x000000009FFF5000 00012C (v03 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: MCFG 0x000000009FFF4000 00003C (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: ECDT 0x000000009FFF3000 000053 (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: SSDT 0x000000009FFCF000 0016AC (v02 LENOVO ProjSsdt 00000010 INTL 20160527)
[    0.000000] ACPI: BOOT 0x000000009FFCE000 000028 (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: BATB 0x000000009FFCD000 00004A (v02 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: SSDT 0x000000009FFCB000 0017AE (v02 LENOVO CpuSsdt  00003000 INTL 20160527)
[    0.000000] ACPI: SSDT 0x000000009FFCA000 00056D (v02 LENOVO CtdpB    00001000 INTL 20160527)
[    0.000000] ACPI: SSDT 0x000000009FFC9000 000648 (v02 LENOVO UsbCTabl 00001000 INTL 20160527)
[    0.000000] ACPI: DBGP 0x000000009FFC8000 000034 (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: DBG2 0x000000009FFC7000 000054 (v00 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: POAT 0x000000009FFC6000 000055 (v03 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: SSDT 0x000000009FFC5000 0005C4 (v01 LENOVO AmdTabl  00001000 INTL 20160527)
[    0.000000] ACPI: SSDT 0x000000009FFC4000 0005AD (v02 LENOVO SgPch    00001000 INTL 20160527)
[    0.000000] ACPI: SSDT 0x000000009FFC3000 000351 (v02 LENOVO SgUlx    00001000 INTL 20160527)
[    0.000000] ACPI: DMAR 0x000000009FFC2000 0000A8 (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: ASF! 0x000000009FFFD000 0000A0 (v32 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: FPDT 0x000000009FFC0000 000044 (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: UEFI 0x000000009FF32000 00013E (v01 LENOVO TP-R0P   00000350 PTEC 00000002)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x00000002527fffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x2527d5000-0x2527fffff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x00000002527fffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x0000000000057fff]
[    0.000000]   node   0: [mem 0x0000000000059000-0x000000000008bfff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x0000000094fa1fff]
[    0.000000]   node   0: [mem 0x0000000094fa4000-0x000000009e90cfff]
[    0.000000]   node   0: [mem 0x000000009ffff000-0x000000009fffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x00000002527fffff]
[    0.000000] Reserved but unavailable: 5994 pages
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x00000002527fffff]
[    0.000000] On node 0 totalpages: 2035862
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 72 pages reserved
[    0.000000]   DMA zone: 3978 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 10085 pages used for memmap
[    0.000000]   DMA32 zone: 645388 pages, LIFO batch:31
[    0.000000]   Normal zone: 21664 pages used for memmap
[    0.000000]   Normal zone: 1386496 pages, LIFO batch:31
[    0.000000] Reserving Intel graphics memory at 0x00000000aa800000-0x00000000ac7fffff
[    0.000000] ACPI: PM-Timer IO Port: 0x1808
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x05] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x06] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x07] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x08] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x09] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0a] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0b] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0c] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0d] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0e] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0f] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x10] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-119
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x8086a201 base: 0xfed00000
[    0.000000] smpboot: Allowing 8 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x00058000-0x00058fff]
[    0.000000] PM: Registered nosave memory: [mem 0x0008c000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x94fa2000-0x94fa2fff]
[    0.000000] PM: Registered nosave memory: [mem 0x94fa3000-0x94fa3fff]
[    0.000000] PM: Registered nosave memory: [mem 0x9e90d000-0x9e9c1fff]
[    0.000000] PM: Registered nosave memory: [mem 0x9e9c2000-0x9ff22fff]
[    0.000000] PM: Registered nosave memory: [mem 0x9ff23000-0x9ff99fff]
[    0.000000] PM: Registered nosave memory: [mem 0x9ff9a000-0x9fffefff]
[    0.000000] PM: Registered nosave memory: [mem 0xa0000000-0xa7ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xa8000000-0xa87fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xa8800000-0xac7fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xac800000-0xf7ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf8000000-0xfbffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfc000000-0xfe00ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfe010000-0xfe010fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfe011000-0xffffffff]
[    0.000000] e820: [mem 0xac800000-0xf7ffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] random: get_random_bytes called from start_kernel+0x99/0x4fd with crng_init=0
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:8 nr_cpu_ids:8 nr_node_ids:1
[    0.000000] percpu: Embedded 46 pages/cpu @        (ptrval) s151552 r8192 d28672 u262144
[    0.000000] pcpu-alloc: s151552 r8192 d28672 u262144 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1 2 3 4 5 6 7 
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 2003977
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-47-generic root=UUID=fd23178a-79cb-414e-ae26-f056aa9da9e1 ro quiet splash vt.handoff=1
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 7791532K/8143448K available (12300K kernel code, 2473K rwdata, 4252K rodata, 2408K init, 2416K bss, 351916K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=8, Nodes=1
[    0.000000] Kernel/User page tables isolation: enabled
[    0.000000] ftrace: allocating 39206 entries in 154 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=8.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=8
[    0.000000] NR_IRQS: 524544, nr_irqs: 2048, preallocated irqs: 16
[    0.000000] vt handoff: transparent VT on vt#1
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] ACPI: Core revision 20170831
[    0.000000] ACPI: 10 ACPI AML tables successfully acquired and loaded
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635855245 ns
[    0.000000] hpet clockevent registered
[    0.004000] APIC: Switch to symmetric I/O mode setup
[    0.004000] DMAR: Host address width 39
[    0.004000] DMAR: DRHD base: 0x000000fed90000 flags: 0x0
[    0.004000] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap 1c0000c40660462 ecap 19e2ff0505e
[    0.004000] DMAR: DRHD base: 0x000000fed91000 flags: 0x1
[    0.004000] DMAR: dmar1: reg_base_addr fed91000 ver 1:0 cap d2008c40660462 ecap f050da
[    0.004000] DMAR: RMRR base: 0x0000009f47f000 end: 0x0000009f49efff
[    0.004000] DMAR: RMRR base: 0x000000aa000000 end: 0x000000ac7fffff
[    0.004000] DMAR-IR: IOAPIC id 2 under DRHD base  0xfed91000 IOMMU 1
[    0.004000] DMAR-IR: HPET id 0 under DRHD base 0xfed91000
[    0.004000] DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
[    0.004000] DMAR-IR: Enabled IRQ remapping in x2apic mode
[    0.004000] x2apic enabled
[    0.004000] Switched APIC routing to cluster x2apic.
[    0.008000] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.028000] tsc: Detected 1800.000 MHz processor
[    0.028000] Calibrating delay loop (skipped), value calculated using timer frequency.. 3600.00 BogoMIPS (lpj=7200000)
[    0.028000] pid_max: default: 32768 minimum: 301
[    0.028000] Security Framework initialized
[    0.028000] Yama: becoming mindful.
[    0.028000] AppArmor: AppArmor initialized
[    0.028000] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.028000] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes)
[    0.028000] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.028000] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.032173] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.032174] ENERGY_PERF_BIAS: View and update with x86_energy_perf_policy(8)
[    0.032182] mce: CPU supports 10 MCE banks
[    0.032198] CPU0: Thermal monitoring enabled (TM1)
[    0.032232] process: using mwait in idle threads
[    0.032236] Last level iTLB entries: 4KB 64, 2MB 8, 4MB 8
[    0.032237] Last level dTLB entries: 4KB 64, 2MB 0, 4MB 0, 1GB 4
[    0.032239] Spectre V2 : Mitigation: Full generic retpoline
[    0.032240] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    0.032240] Spectre V2 : Spectre v2 mitigation: Enabling Indirect Branch Prediction Barrier
[    0.032241] Spectre V2 : Enabling Restricted Speculation for firmware calls
[    0.032243] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.043682] Freeing SMP alternatives memory: 36K
[    0.052694] TSC deadline timer enabled
[    0.052701] smpboot: CPU0: Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (family: 0x6, model: 0x8e, stepping: 0xa)
[    0.052801] Performance Events: PEBS fmt3+, Skylake events, 32-deep LBR, full-width counters, Intel PMU driver.
[    0.052852] ... version:                4
[    0.052853] ... bit width:              48
[    0.052853] ... generic registers:      4
[    0.052855] ... value mask:             0000ffffffffffff
[    0.052856] ... max period:             00007fffffffffff
[    0.052856] ... fixed-purpose events:   3
[    0.052857] ... event mask:             000000070000000f
[    0.052917] Hierarchical SRCU implementation.
[    0.054892] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.054912] smp: Bringing up secondary CPUs ...
[    0.055020] x86: Booting SMP configuration:
[    0.055022] .... node  #0, CPUs:      #1 #2 #3 #4 #5 #6 #7
[    0.061161] smp: Brought up 1 node, 8 CPUs
[    0.061161] smpboot: Max logical packages: 1
[    0.061161] smpboot: Total of 8 processors activated (28800.00 BogoMIPS)
[    0.064414] devtmpfs: initialized
[    0.064414] x86/mm: Memory block size: 128MB
[    0.065029] evm: security.selinux
[    0.065030] evm: security.SMACK64
[    0.065030] evm: security.SMACK64EXEC
[    0.065031] evm: security.SMACK64TRANSMUTE
[    0.065032] evm: security.SMACK64MMAP
[    0.065033] evm: security.apparmor
[    0.065033] evm: security.ima
[    0.065034] evm: security.capability
[    0.065054] PM: Registering ACPI NVS region [mem 0x94fa2000-0x94fa2fff] (4096 bytes)
[    0.065054] PM: Registering ACPI NVS region [mem 0x9ff23000-0x9ff99fff] (487424 bytes)
[    0.065054] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.065054] futex hash table entries: 2048 (order: 5, 131072 bytes)
[    0.065054] pinctrl core: initialized pinctrl subsystem
[    0.065054] RTC time: 21:44:52, date: 04/11/19
[    0.065054] NET: Registered protocol family 16
[    0.065054] audit: initializing netlink subsys (disabled)
[    0.065054] audit: type=2000 audit(1555019092.064:1): state=initialized audit_enabled=0 res=1
[    0.065054] cpuidle: using governor ladder
[    0.065054] cpuidle: using governor menu
[    0.065054] Simple Boot Flag at 0x47 set to 0x1
[    0.065054] ACPI: bus type PCI registered
[    0.065054] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.065054] PCI: MMCONFIG for domain 0000 [bus 00-3f] at [mem 0xf8000000-0xfbffffff] (base 0xf8000000)
[    0.065054] PCI: MMCONFIG at [mem 0xf8000000-0xfbffffff] reserved in E820
[    0.065054] PCI: Using configuration type 1 for base access
[    0.069195] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.069195] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.069195] ACPI: Added _OSI(Module Device)
[    0.069195] ACPI: Added _OSI(Processor Device)
[    0.069195] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.069195] ACPI: Added _OSI(Processor Aggregator Device)
[    0.069195] ACPI: Added _OSI(Linux-Dell-Video)
[    0.069195] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    0.069195] ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
[    0.069195] ACPI: EC: EC started
[    0.069195] ACPI: EC: interrupt blocked
[    0.073498] ACPI: \: Used as first EC
[    0.073501] ACPI: \: GPE=0x20, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.073503] ACPI: \: Used as boot ECDT EC to handle transactions
[    0.079279] ACPI: Executed 30 blocks of module-level executable AML code
[    0.096507] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.117409] ACPI: Dynamic OEM Table Load:
[    0.117432] ACPI: SSDT 0xFFFF8C57885CE800 00060D (v02 PmRef  Cpu0Ist  00003000 INTL 20160527)
[    0.117940] ACPI: Executed 1 blocks of module-level executable AML code
[    0.118092] ACPI: \_PR_.PR00: _OSC native thermal LVT Acked
[    0.120189] ACPI: Dynamic OEM Table Load:
[    0.120201] ACPI: SSDT 0xFFFF8C57887F7000 0003FF (v02 PmRef  Cpu0Cst  00003001 INTL 20160527)
[    0.120653] ACPI: Executed 1 blocks of module-level executable AML code
[    0.121836] ACPI: Dynamic OEM Table Load:
[    0.121850] ACPI: SSDT 0xFFFF8C57887EF000 000D14 (v02 PmRef  ApIst    00003000 INTL 20160527)
[    0.123608] ACPI: Executed 1 blocks of module-level executable AML code
[    0.124082] ACPI: Dynamic OEM Table Load:
[    0.124092] ACPI: SSDT 0xFFFF8C57887F6000 00030A (v02 PmRef  ApCst    00003000 INTL 20160527)
[    0.124643] ACPI: Executed 1 blocks of module-level executable AML code
[    0.130096] ACPI: Interpreter enabled
[    0.130181] ACPI: (supports S0 S3 S4 S5)
[    0.130183] ACPI: Using IOAPIC for interrupt routing
[    0.130251] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.131435] ACPI: Enabled 8 GPEs in block 00 to 7F
[    0.143749] ACPI: Power Resource [PUBS] (on)
[    0.176755] ACPI: Power Resource [PC01] (on)
[    0.240529] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-3e])
[    0.240540] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.245779] acpi PNP0A08:00: _OSC: OS now controls [PCIeHotplug PME AER PCIeCapability]
[    0.249897] PCI host bridge to bus 0000:00
[    0.249901] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.249903] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.249906] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.249908] pci_bus 0000:00: root bus resource [mem 0xac800000-0xf7ffffff window]
[    0.249910] pci_bus 0000:00: root bus resource [mem 0xfd000000-0xfe7fffff window]
[    0.249912] pci_bus 0000:00: root bus resource [bus 00-3e]
[    0.249926] pci 0000:00:00.0: [8086:5914] type 00 class 0x060000
[    0.251453] pci 0000:00:02.0: [8086:5917] type 00 class 0x030000
[    0.251472] pci 0000:00:02.0: reg 0x10: [mem 0xf1000000-0xf1ffffff 64bit]
[    0.251482] pci 0000:00:02.0: reg 0x18: [mem 0xd0000000-0xdfffffff 64bit pref]
[    0.251489] pci 0000:00:02.0: reg 0x20: [io  0xe000-0xe03f]
[    0.251515] pci 0000:00:02.0: BAR 2: assigned to efifb
[    0.253076] pci 0000:00:08.0: [8086:1911] type 00 class 0x088000
[    0.253097] pci 0000:00:08.0: reg 0x10: [mem 0xf252a000-0xf252afff 64bit]
[    0.254653] pci 0000:00:14.0: [8086:9d2f] type 00 class 0x0c0330
[    0.254684] pci 0000:00:14.0: reg 0x10: [mem 0xf2500000-0xf250ffff 64bit]
[    0.254778] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    0.256496] pci 0000:00:14.2: [8086:9d31] type 00 class 0x118000
[    0.256526] pci 0000:00:14.2: reg 0x10: [mem 0xf252b000-0xf252bfff 64bit]
[    0.258102] pci 0000:00:16.0: [8086:9d3a] type 00 class 0x078000
[    0.258137] pci 0000:00:16.0: reg 0x10: [mem 0xf252c000-0xf252cfff 64bit]
[    0.258234] pci 0000:00:16.0: PME# supported from D3hot
[    0.259865] pci 0000:00:17.0: [8086:9d03] type 00 class 0x010601
[    0.259893] pci 0000:00:17.0: reg 0x10: [mem 0xf2528000-0xf2529fff]
[    0.259904] pci 0000:00:17.0: reg 0x14: [mem 0xf252f000-0xf252f0ff]
[    0.259916] pci 0000:00:17.0: reg 0x18: [io  0xe080-0xe087]
[    0.259928] pci 0000:00:17.0: reg 0x1c: [io  0xe088-0xe08b]
[    0.259939] pci 0000:00:17.0: reg 0x20: [io  0xe060-0xe07f]
[    0.259951] pci 0000:00:17.0: reg 0x24: [mem 0xf252d000-0xf252d7ff]
[    0.260017] pci 0000:00:17.0: PME# supported from D3hot
[    0.261636] pci 0000:00:1c.0: [8086:9d10] type 01 class 0x060400
[    0.261739] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.263378] pci 0000:00:1c.4: [8086:9d14] type 01 class 0x060400
[    0.263479] pci 0000:00:1c.4: PME# supported from D0 D3hot D3cold
[    0.265126] pci 0000:00:1d.0: [8086:9d18] type 01 class 0x060400
[    0.265230] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
[    0.266858] pci 0000:00:1d.2: [8086:9d1a] type 01 class 0x060400
[    0.266958] pci 0000:00:1d.2: PME# supported from D0 D3hot D3cold
[    0.268595] pci 0000:00:1d.3: [8086:9d1b] type 01 class 0x060400
[    0.268699] pci 0000:00:1d.3: PME# supported from D0 D3hot D3cold
[    0.270341] pci 0000:00:1f.0: [8086:9d4e] type 00 class 0x060100
[    0.272081] pci 0000:00:1f.2: [8086:9d21] type 00 class 0x058000
[    0.272100] pci 0000:00:1f.2: reg 0x10: [mem 0xf2524000-0xf2527fff]
[    0.273762] pci 0000:00:1f.3: [8086:9d71] type 00 class 0x040300
[    0.273799] pci 0000:00:1f.3: reg 0x10: [mem 0xf2520000-0xf2523fff 64bit]
[    0.273841] pci 0000:00:1f.3: reg 0x20: [mem 0xf2510000-0xf251ffff 64bit]
[    0.273909] pci 0000:00:1f.3: PME# supported from D3hot D3cold
[    0.275551] pci 0000:00:1f.4: [8086:9d23] type 00 class 0x0c0500
[    0.275606] pci 0000:00:1f.4: reg 0x10: [mem 0xf252e000-0xf252e0ff 64bit]
[    0.275657] pci 0000:00:1f.4: reg 0x20: [io  0xefa0-0xefbf]
[    0.277425] pci 0000:02:00.0: [1002:699f] type 00 class 0x038000
[    0.277470] pci 0000:02:00.0: reg 0x10: [mem 0xe0000000-0xefffffff 64bit pref]
[    0.277491] pci 0000:02:00.0: reg 0x18: [mem 0xf0000000-0xf01fffff 64bit pref]
[    0.277505] pci 0000:02:00.0: reg 0x20: [io  0xd000-0xd0ff]
[    0.277519] pci 0000:02:00.0: reg 0x24: [mem 0xf2400000-0xf243ffff]
[    0.277534] pci 0000:02:00.0: reg 0x30: [mem 0xfffe0000-0xffffffff pref]
[    0.277546] pci 0000:02:00.0: enabling Extended Tags
[    0.277644] pci 0000:02:00.0: supports D1 D2
[    0.277747] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    0.277752] pci 0000:00:1c.0:   bridge window [io  0xd000-0xdfff]
[    0.277756] pci 0000:00:1c.0:   bridge window [mem 0xf2400000-0xf24fffff]
[    0.277762] pci 0000:00:1c.0:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.277894] pci 0000:03:00.0: [10ec:8168] type 00 class 0x020000
[    0.277990] pci 0000:03:00.0: reg 0x10: [io  0xc000-0xc0ff]
[    0.278095] pci 0000:03:00.0: reg 0x18: [mem 0xf2304000-0xf2304fff 64bit]
[    0.278166] pci 0000:03:00.0: reg 0x20: [mem 0xf2300000-0xf2303fff 64bit]
[    0.278500] pci 0000:03:00.0: supports D1 D2
[    0.278503] pci 0000:03:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.288061] pci 0000:00:1c.4: PCI bridge to [bus 03]
[    0.288066] pci 0000:00:1c.4:   bridge window [io  0xc000-0xcfff]
[    0.288070] pci 0000:00:1c.4:   bridge window [mem 0xf2300000-0xf23fffff]
[    0.288346] pci 0000:04:00.0: [144d:a804] type 00 class 0x010802
[    0.288382] pci 0000:04:00.0: reg 0x10: [mem 0xf2200000-0xf2203fff 64bit]
[    0.300223] pci 0000:00:1d.0: PCI bridge to [bus 04]
[    0.300229] pci 0000:00:1d.0:   bridge window [mem 0xf2200000-0xf22fffff]
[    0.300368] pci 0000:05:00.0: [10ec:b822] type 00 class 0xff0000
[    0.300461] pci 0000:05:00.0: reg 0x10: [io  0xb000-0xb0ff]
[    0.300556] pci 0000:05:00.0: reg 0x18: [mem 0xf2100000-0xf210ffff 64bit]
[    0.300936] pci 0000:05:00.0: supports D1 D2
[    0.300938] pci 0000:05:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.312054] pci 0000:00:1d.2: PCI bridge to [bus 05]
[    0.312058] pci 0000:00:1d.2:   bridge window [io  0xb000-0xbfff]
[    0.312062] pci 0000:00:1d.2:   bridge window [mem 0xf2100000-0xf21fffff]
[    0.312224] pci 0000:06:00.0: [1217:8621] type 00 class 0x080501
[    0.312264] pci 0000:06:00.0: reg 0x10: [mem 0xf2001000-0xf2001fff]
[    0.312277] pci 0000:06:00.0: reg 0x14: [mem 0xf2000000-0xf20007ff]
[    0.312461] pci 0000:06:00.0: PME# supported from D3hot D3cold
[    0.324107] pci 0000:00:1d.3: PCI bridge to [bus 06]
[    0.324113] pci 0000:00:1d.3:   bridge window [mem 0xf2000000-0xf20fffff]
[    0.329757] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.329869] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 *10 11 12 14 15)
[    0.329977] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.330085] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.330191] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.330301] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.330407] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.330514] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.331473] ACPI: EC: interrupt unblocked
[    0.331489] ACPI: EC: event unblocked
[    0.331503] ACPI: \_SB_.PCI0.LPCB.EC__: GPE=0x20, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.331506] ACPI: \_SB_.PCI0.LPCB.EC__: Used as boot DSDT EC to handle transactions and events
[    0.331803] SCSI subsystem initialized
[    0.331823] libata version 3.00 loaded.
[    0.331823] pci 0000:00:02.0: vgaarb: setting as boot VGA device
[    0.331823] pci 0000:00:02.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.331823] pci 0000:00:02.0: vgaarb: bridge control possible
[    0.331823] vgaarb: loaded
[    0.331823] ACPI: bus type USB registered
[    0.331823] usbcore: registered new interface driver usbfs
[    0.331823] usbcore: registered new interface driver hub
[    0.332010] usbcore: registered new device driver usb
[    0.332063] EDAC MC: Ver: 3.0.0
[    0.332394] Registered efivars operations
[    0.356048] PCI: Using ACPI for IRQ routing
[    0.362538] PCI: pci_cache_line_size set to 64 bytes
[    0.363075] e820: reserve RAM buffer [mem 0x00058000-0x0005ffff]
[    0.363076] e820: reserve RAM buffer [mem 0x0008c000-0x0008ffff]
[    0.363078] e820: reserve RAM buffer [mem 0x94fa2000-0x97ffffff]
[    0.363079] e820: reserve RAM buffer [mem 0x9e90d000-0x9fffffff]
[    0.363081] e820: reserve RAM buffer [mem 0x252800000-0x253ffffff]
[    0.363195] NetLabel: Initializing
[    0.363196] NetLabel:  domain hash size = 128
[    0.363197] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.363216] NetLabel:  unlabeled traffic allowed by default
[    0.363235] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    0.363235] hpet0: 8 comparators, 64-bit 24.000000 MHz counter
[    0.366056] clocksource: Switched to clocksource hpet
[    0.378707] VFS: Disk quotas dquot_6.6.0
[    0.378729] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.378870] AppArmor: AppArmor Filesystem Enabled
[    0.378904] pnp: PnP ACPI init
[    0.379161] system 00:00: [mem 0xfd000000-0xfdabffff] has been reserved
[    0.379164] system 00:00: [mem 0xfdad0000-0xfdadffff] has been reserved
[    0.379167] system 00:00: [mem 0xfdb00000-0xfdffffff] has been reserved
[    0.379169] system 00:00: [mem 0xfe000000-0xfe01ffff] could not be reserved
[    0.379172] system 00:00: [mem 0xfe036000-0xfe03bfff] has been reserved
[    0.379174] system 00:00: [mem 0xfe03d000-0xfe3fffff] has been reserved
[    0.379176] system 00:00: [mem 0xfe410000-0xfe7fffff] has been reserved
[    0.379184] system 00:00: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.379756] system 00:01: [io  0xff00-0xfffe] has been reserved
[    0.379762] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.381241] system 00:02: [io  0x0680-0x069f] has been reserved
[    0.381244] system 00:02: [io  0xffff] has been reserved
[    0.381247] system 00:02: [io  0xffff] has been reserved
[    0.381249] system 00:02: [io  0xffff] has been reserved
[    0.381252] system 00:02: [io  0x1800-0x18fe] has been reserved
[    0.381254] system 00:02: [io  0x164e-0x164f] has been reserved
[    0.381261] system 00:02: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.381448] pnp 00:03: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.381516] system 00:04: [io  0x1854-0x1857] has been reserved
[    0.381523] system 00:04: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    0.381556] pnp 00:05: Plug and Play ACPI device, IDs LEN0071 PNP0303 (active)
[    0.381759] system 00:06: [io  0x1800-0x189f] could not be reserved
[    0.381762] system 00:06: [io  0x0800-0x087f] has been reserved
[    0.381764] system 00:06: [io  0x0880-0x08ff] has been reserved
[    0.381767] system 00:06: [io  0x0900-0x097f] has been reserved
[    0.381769] system 00:06: [io  0x0980-0x09ff] has been reserved
[    0.381771] system 00:06: [io  0x0a00-0x0a7f] has been reserved
[    0.381774] system 00:06: [io  0x0a80-0x0aff] has been reserved
[    0.381776] system 00:06: [io  0x0b00-0x0b7f] has been reserved
[    0.381778] system 00:06: [io  0x0b80-0x0bff] has been reserved
[    0.381781] system 00:06: [io  0x15e0-0x15ef] has been reserved
[    0.381783] system 00:06: [io  0x1600-0x167f] could not be reserved
[    0.381785] system 00:06: [io  0x1640-0x165f] could not be reserved
[    0.381789] system 00:06: [mem 0xf8000000-0xfbffffff] has been reserved
[    0.381791] system 00:06: [mem 0xfed10000-0xfed13fff] has been reserved
[    0.381794] system 00:06: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.381796] system 00:06: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.381799] system 00:06: [mem 0xfeb00000-0xfebfffff] has been reserved
[    0.381801] system 00:06: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.381804] system 00:06: [mem 0xfed90000-0xfed93fff] could not be reserved
[    0.381807] system 00:06: [mem 0xf7fe0000-0xf7ffffff] has been reserved
[    0.381812] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.381845] pnp 00:07: Plug and Play ACPI device, IDs LEN2054 PNP0f13 (active)
[    0.384412] system 00:08: [mem 0xfdaf0000-0xfdafffff] has been reserved
[    0.384414] system 00:08: [mem 0xfdae0000-0xfdaeffff] has been reserved
[    0.384417] system 00:08: [mem 0xfdac0000-0xfdacffff] has been reserved
[    0.384423] system 00:08: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.385518] system 00:09: [mem 0xfed10000-0xfed17fff] could not be reserved
[    0.385520] system 00:09: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.385523] system 00:09: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.385525] system 00:09: [mem 0xf8000000-0xfbffffff] has been reserved
[    0.385527] system 00:09: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.385530] system 00:09: [mem 0xfed90000-0xfed93fff] could not be reserved
[    0.385532] system 00:09: [mem 0xfed45000-0xfed8ffff] has been reserved
[    0.385535] system 00:09: [mem 0xff000000-0xffffffff] has been reserved
[    0.385537] system 00:09: [mem 0xfee00000-0xfeefffff] has been reserved
[    0.385540] system 00:09: [mem 0xf7fe0000-0xf7ffffff] has been reserved
[    0.385546] system 00:09: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.386157] system 00:0a: [mem 0x00000000-0x0009ffff] could not be reserved
[    0.386159] system 00:0a: [mem 0x000c0000-0x000c3fff] could not be reserved
[    0.386161] system 00:0a: [mem 0x000c8000-0x000cbfff] could not be reserved
[    0.386164] system 00:0a: [mem 0x000d0000-0x000d3fff] could not be reserved
[    0.386166] system 00:0a: [mem 0x000d8000-0x000dbfff] could not be reserved
[    0.386168] system 00:0a: [mem 0x000e0000-0x000e3fff] could not be reserved
[    0.386170] system 00:0a: [mem 0x000e8000-0x000ebfff] could not be reserved
[    0.386173] system 00:0a: [mem 0x000f0000-0x000fffff] could not be reserved
[    0.386175] system 00:0a: [mem 0x00100000-0xac7fffff] could not be reserved
[    0.386178] system 00:0a: [mem 0xfec00000-0xfed3ffff] could not be reserved
[    0.386180] system 00:0a: [mem 0xfed4c000-0xffffffff] could not be reserved
[    0.386186] system 00:0a: Plug and Play ACPI device, IDs PNP0c01 (active)
[    0.386367] pnp: PnP ACPI: found 11 devices
[    0.394585] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.394591] pci 0000:02:00.0: can't claim BAR 6 [mem 0xfffe0000-0xffffffff pref]: no compatible bridge window
[    0.394636] pci 0000:02:00.0: BAR 6: assigned [mem 0xf2440000-0xf245ffff pref]
[    0.394640] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    0.394643] pci 0000:00:1c.0:   bridge window [io  0xd000-0xdfff]
[    0.394648] pci 0000:00:1c.0:   bridge window [mem 0xf2400000-0xf24fffff]
[    0.394652] pci 0000:00:1c.0:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.394659] pci 0000:00:1c.4: PCI bridge to [bus 03]
[    0.394662] pci 0000:00:1c.4:   bridge window [io  0xc000-0xcfff]
[    0.394667] pci 0000:00:1c.4:   bridge window [mem 0xf2300000-0xf23fffff]
[    0.394675] pci 0000:00:1d.0: PCI bridge to [bus 04]
[    0.394680] pci 0000:00:1d.0:   bridge window [mem 0xf2200000-0xf22fffff]
[    0.394688] pci 0000:00:1d.2: PCI bridge to [bus 05]
[    0.394691] pci 0000:00:1d.2:   bridge window [io  0xb000-0xbfff]
[    0.394696] pci 0000:00:1d.2:   bridge window [mem 0xf2100000-0xf21fffff]
[    0.394705] pci 0000:00:1d.3: PCI bridge to [bus 06]
[    0.394710] pci 0000:00:1d.3:   bridge window [mem 0xf2000000-0xf20fffff]
[    0.394719] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.394721] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.394724] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.394726] pci_bus 0000:00: resource 7 [mem 0xac800000-0xf7ffffff window]
[    0.394728] pci_bus 0000:00: resource 8 [mem 0xfd000000-0xfe7fffff window]
[    0.394730] pci_bus 0000:02: resource 0 [io  0xd000-0xdfff]
[    0.394732] pci_bus 0000:02: resource 1 [mem 0xf2400000-0xf24fffff]
[    0.394734] pci_bus 0000:02: resource 2 [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.394737] pci_bus 0000:03: resource 0 [io  0xc000-0xcfff]
[    0.394739] pci_bus 0000:03: resource 1 [mem 0xf2300000-0xf23fffff]
[    0.394741] pci_bus 0000:04: resource 1 [mem 0xf2200000-0xf22fffff]
[    0.394743] pci_bus 0000:05: resource 0 [io  0xb000-0xbfff]
[    0.394745] pci_bus 0000:05: resource 1 [mem 0xf2100000-0xf21fffff]
[    0.394747] pci_bus 0000:06: resource 1 [mem 0xf2000000-0xf20fffff]
[    0.395036] NET: Registered protocol family 2
[    0.395288] TCP established hash table entries: 65536 (order: 7, 524288 bytes)
[    0.395442] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.395688] TCP: Hash tables configured (established 65536 bind 65536)
[    0.395732] UDP hash table entries: 4096 (order: 5, 131072 bytes)
[    0.395766] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes)
[    0.395841] NET: Registered protocol family 1
[    0.395858] pci 0000:00:02.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.396620] PCI: CLS 0 bytes, default 64
[    0.396671] Unpacking initramfs...
[    1.230292] Freeing initrd memory: 36932K
[    1.230340] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    1.230345] software IO TLB [mem 0x8c10e000-0x9010e000] (64MB) mapped at [        (ptrval)-        (ptrval)]
[    1.230712] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x19f2297dd97, max_idle_ns: 440795236593 ns
[    1.230982] Scanning for low memory corruption every 60 seconds
[    1.232049] Initialise system trusted keyrings
[    1.232079] Key type blacklist registered
[    1.232165] workingset: timestamp_bits=36 max_order=21 bucket_order=0
[    1.233743] zbud: loaded
[    1.234554] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    1.234779] fuse init (API version 7.26)
[    1.237832] Key type asymmetric registered
[    1.237833] Asymmetric key parser 'x509' registered
[    1.237871] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    1.237945] io scheduler noop registered
[    1.237946] io scheduler deadline registered
[    1.237979] io scheduler cfq registered (default)
[    1.239855] pcieport 0000:00:1c.0: AER enabled with IRQ 122
[    1.239882] pcieport 0000:00:1c.4: AER enabled with IRQ 123
[    1.239908] pcieport 0000:00:1d.0: AER enabled with IRQ 124
[    1.239932] pcieport 0000:00:1d.2: AER enabled with IRQ 125
[    1.239957] pcieport 0000:00:1d.3: AER enabled with IRQ 126
[    1.239975] pcieport 0000:00:1c.0: Signaling PME with IRQ 122
[    1.239989] pcieport 0000:00:1c.4: Signaling PME with IRQ 123
[    1.240030] pcieport 0000:00:1d.0: Signaling PME with IRQ 124
[    1.240053] pcieport 0000:00:1d.2: Signaling PME with IRQ 125
[    1.240066] pcieport 0000:00:1d.3: Signaling PME with IRQ 126
[    1.240162] efifb: probing for efifb
[    1.240179] efifb: framebuffer at 0xd0000000, using 8128k, total 8128k
[    1.240181] efifb: mode is 1920x1080x32, linelength=7680, pages=1
[    1.240181] efifb: scrolling: redraw
[    1.240184] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    1.240330] Console: switching to colour frame buffer device 240x67
[    1.240368] fb0: EFI VGA frame buffer device
[    1.240379] intel_idle: MWAIT substates: 0x11142120
[    1.240381] intel_idle: v0.4.1 model 0x8E
[    1.241037] intel_idle: lapic_timer_reliable_states 0xffffffff
[    1.242698] ACPI: AC Adapter [AC] (on-line)
[    1.242802] input: Sleep Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0E:00/input/input0
[    1.242872] ACPI: Sleep Button [SLPB]
[    1.242917] input: Lid Switch as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0D:00/input/input1
[    1.242965] ACPI: Lid Switch [LID]
[    1.243007] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input2
[    1.243063] ACPI: Power Button [PWRF]
[    1.250327] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    1.253490] thermal LNXTHERM:00: registered as thermal_zone0
[    1.253491] ACPI: Thermal Zone [THM0] (40 C)
[    1.253701] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    1.257446] Linux agpgart interface v0.103
[    1.261737] loop: module loaded
[    1.262029] libphy: Fixed MDIO Bus: probed
[    1.262030] tun: Universal TUN/TAP device driver, 1.6
[    1.262145] PPP generic driver version 2.4.2
[    1.262352] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    1.262356] ehci-pci: EHCI PCI platform driver
[    1.262373] ehci-platform: EHCI generic platform driver
[    1.262389] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    1.262391] ohci-pci: OHCI PCI platform driver
[    1.262401] ohci-platform: OHCI generic platform driver
[    1.262409] uhci_hcd: USB Universal Host Controller Interface driver
[    1.262651] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    1.262659] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 1
[    1.263843] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x0000000000109810
[    1.263849] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
[    1.264070] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    1.264072] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.264074] usb usb1: Product: xHCI Host Controller
[    1.264077] usb usb1: Manufacturer: Linux 4.15.0-47-generic xhci-hcd
[    1.264078] usb usb1: SerialNumber: 0000:00:14.0
[    1.264290] hub 1-0:1.0: USB hub found
[    1.264309] hub 1-0:1.0: 12 ports detected
[    1.266513] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    1.266518] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 2
[    1.266524] xhci_hcd 0000:00:14.0: Host supports USB 3.0  SuperSpeed
[    1.266570] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003
[    1.266573] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.266575] usb usb2: Product: xHCI Host Controller
[    1.266577] usb usb2: Manufacturer: Linux 4.15.0-47-generic xhci-hcd
[    1.266579] usb usb2: SerialNumber: 0000:00:14.0
[    1.266777] hub 2-0:1.0: USB hub found
[    1.266789] hub 2-0:1.0: 6 ports detected
[    1.267719] usb: port power management may be unreliable
[    1.268395] i8042: PNP: PS/2 Controller [PNP0303:KBD,PNP0f13:MOU] at 0x60,0x64 irq 1,12
[    1.284990] serio: i8042 KBD port at 0x60,0x64 irq 1
[    1.284995] serio: i8042 AUX port at 0x60,0x64 irq 12
[    1.285288] mousedev: PS/2 mouse device common for all mice
[    1.285774] rtc_cmos 00:03: RTC can wake from S4
[    1.286228] rtc_cmos 00:03: rtc core: registered rtc_cmos as rtc0
[    1.286354] rtc_cmos 00:03: alarms up to one month, y3k, 242 bytes nvram, hpet irqs
[    1.286363] i2c /dev entries driver
[    1.286368] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[    1.286471] device-mapper: uevent: version 1.0.3
[    1.286582] device-mapper: ioctl: 4.37.0-ioctl (2017-09-20) initialised: dm-devel@redhat.com
[    1.286587] intel_pstate: Intel P-state driver initializing
[    1.288095] intel_pstate: HWP enabled
[    1.288605] ledtrig-cpu: registered to indicate activity on CPUs
[    1.288606] EFI Variables Facility v0.08 2004-May-17
[    1.317965] intel_pmc_core:  initialized
[    1.318130] NET: Registered protocol family 10
[    1.322022] Segment Routing with IPv6
[    1.322043] NET: Registered protocol family 17
[    1.322248] Key type dns_resolver registered
[    1.323049] RAS: Correctable Errors collector initialized.
[    1.323111] microcode: sig=0x806ea, pf=0x80, revision=0x96
[    1.323339] microcode: Microcode Update Driver: v2.2.
[    1.323346] sched_clock: Marking stable (1323332123, 0)->(1330852784, -7520661)
[    1.323857] registered taskstats version 1
[    1.323863] Loading compiled-in X.509 certificates
[    1.325652] Loaded X.509 cert 'Build time autogenerated kernel key: 7211859d1298c08a101905a3cb814e8c7b4bf4a4'
[    1.326346] Loaded UEFI:db cert 'Lenovo Ltd.: ThinkPad Product CA 2012: 838b1f54c1550463f45f98700640f11069265949' linked to secondary sys keyring
[    1.326357] Loaded UEFI:db cert 'Lenovo(Beijing) Ltd.: ICD-CDC -DB: cf21a31053abf166e8568a3291e019506efea4a8' linked to secondary sys keyring
[    1.326367] Loaded UEFI:db cert 'Lenovo UEFI CA 2014: 4b91a68732eaefdd2c8ffffc6b027ec3449e9c8f' linked to secondary sys keyring
[    1.326382] Loaded UEFI:db cert 'Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4' linked to secondary sys keyring
[    1.326396] Loaded UEFI:db cert 'Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53' linked to secondary sys keyring
[    1.326613] Couldn't get size: 0x800000000000000e
[    1.326615] MODSIGN: Couldn't get UEFI MokListRT
[    1.327264] zswap: loaded using pool lzo/zbud
[    1.330622] Key type big_key registered
[    1.330625] Key type trusted registered
[    1.332123] Key type encrypted registered
[    1.332125] AppArmor: AppArmor sha1 policy hashing enabled
[    1.332127] ima: No TPM chip found, activating TPM-bypass! (rc=-19)
[    1.332130] ima: Allocated hash algorithm: sha1
[    1.332139] evm: HMAC attrs: 0x1
[    1.333569]   Magic number: 15:725:752
[    1.333587] tty ttyS3: hash matches
[    1.333848] rtc_cmos 00:03: setting system clock to 2019-04-11 21:44:53 UTC (1555019093)
[    1.333977] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    1.333977] EDD information not available.
[    1.367130] ACPI: Battery Slot [BAT0] (battery present)
[    1.377148] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input3
[    1.600075] usb 1-1: new full-speed USB device number 2 using xhci_hcd
[    1.697852] Freeing unused kernel memory: 2408K
[    1.732464] Write protecting the kernel read-only data: 20480k
[    1.733590] Freeing unused kernel memory: 2008K
[    1.736123] Freeing unused kernel memory: 1892K
[    1.740347] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.740347] x86/mm: Checking user space page tables
[    1.744489] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.754283] usb 1-1: New USB device found, idVendor=046d, idProduct=c52f
[    1.754285] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    1.754287] usb 1-1: Product: USB Receiver
[    1.754288] usb 1-1: Manufacturer: Logitech
[    1.757733] hidraw: raw HID events driver (C) Jiri Kosina
[    1.760781] usbcore: registered new interface driver usbhid
[    1.760782] usbhid: USB HID core driver
[    1.766362] input: Logitech USB Receiver as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.0/0003:046D:C52F.0001/input/input5
[    1.766460] hid-generic 0003:046D:C52F.0001: input,hidraw0: USB HID v1.11 Mouse [Logitech USB Receiver] on usb-0000:00:14.0-1/input0
[    1.766595] input: Logitech USB Receiver as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.1/0003:046D:C52F.0002/input/input6
[    1.813758] sdhci: Secure Digital Host Controller Interface driver
[    1.813760] sdhci: Copyright(c) Pierre Ossman
[    1.813796] ahci 0000:00:17.0: version 3.0
[    1.814103] ahci 0000:00:17.0: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x0 impl SATA mode
[    1.814105] ahci 0000:00:17.0: flags: 64bit ncq led clo only pio slum part deso sadm sds apst 
[    1.815037] sdhci-pci 0000:06:00.0: SDHCI controller found [1217:8621] (rev 1)
[    1.815131] sdhci-pci 0000:06:00.0: enabling device (0000 -> 0002)
[    1.815228] r8169 Gigabit Ethernet driver 2.3LK-NAPI loaded
[    1.815310] mmc0: Unknown controller version (3). You may experience problems.
[    1.815411] scsi host0: ahci
[    1.815496] mmc0: SDHCI controller on PCI [0000:06:00.0] using ADMA
[    1.815667] scsi host1: ahci
[    1.815723] ata1: DUMMY
[    1.815724] ata2: DUMMY
[    1.816846] nvme nvme0: pci function 0000:04:00.0
[    1.824274] hid-generic 0003:046D:C52F.0002: input,hiddev0,hidraw1: USB HID v1.11 Device [Logitech USB Receiver] on usb-0000:00:14.0-1/input1
[    1.825036] r8169 0000:03:00.0 eth0: RTL8168g/8111g at 0x        (ptrval), 54:e1:ad:e2:b1:27, XID 10900880 IRQ 130
[    1.825038] r8169 0000:03:00.0 eth0: jumbo features [frames: 9200 bytes, tx checksumming: ko]
[    1.853303] r8169 0000:03:00.0 enp3s0: renamed from eth0
[    1.910166] random: fast init done
[    2.037380] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    2.037391] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    2.037393] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    2.060882]  nvme0n1: p1 p2 p3 p4 p5
[    2.095981] EXT4-fs (nvme0n1p5): mounted filesystem with ordered data mode. Opts: (null)
[    2.177224] ip_tables: (C) 2000-2006 Netfilter Core Team
[    2.228453] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    2.236245] clocksource: Switched to clocksource tsc
[    2.248837] systemd[1]: Detected architecture x86-64.
[    2.251209] systemd[1]: Set hostname to <sherlock>.
[    2.318292] systemd[1]: Reached target Remote File Systems.
[    2.318462] systemd[1]: Created slice User and Session Slice.
[    2.318614] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[    2.318645] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    2.318658] systemd[1]: Reached target User and Group Name Lookups.
[    2.318734] systemd[1]: Created slice System Slice.
[    2.318750] systemd[1]: Reached target Slices.
[    2.330834] lp: driver loaded but no devices found
[    2.333845] ppdev: user-space parallel port driver
[    2.335993] EXT4-fs (nvme0n1p5): re-mounted. Opts: errors=remount-ro
[    2.367873] systemd-journald[275]: Received request to flush runtime journal from PID 1
[    2.393893] Adding 2097148k swap on /swapfile.  Priority:-2 extents:6 across:2260988k SSFS
[    2.470394] acpi PNP0C14:02: duplicate WMI GUID 05901221-D566-11D1-B2F0-00A0C9062910 (first instance was on PNP0C14:01)
[    2.470526] acpi PNP0C14:03: duplicate WMI GUID 05901221-D566-11D1-B2F0-00A0C9062910 (first instance was on PNP0C14:01)
[    2.520568] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    2.520576] Non-volatile memory driver v1.3
[    2.524778] thinkpad_acpi: ThinkPad ACPI Extras v0.25
[    2.524779] thinkpad_acpi: http://ibm-acpi.sf.net/
[    2.524780] thinkpad_acpi: ThinkPad BIOS R0PET35W (1.12 ), EC unknown
[    2.524781] thinkpad_acpi: Lenovo ThinkPad E480, model 20KQS00000
[    2.525497] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    2.526564] mei_me 0000:00:16.0: enabling device (0000 -> 0002)
[    2.529881] thinkpad_acpi: radio switch found; radios are enabled
[    2.530090] thinkpad_acpi: This ThinkPad has standard ACPI backlight brightness control, supported by the ACPI video driver
[    2.530090] thinkpad_acpi: Disabling thinkpad-acpi brightness events by default...
[    2.541654] RAPL PMU: API unit is 2^-32 Joules, 5 fixed counters, 655360 ms ovfl timer
[    2.541655] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
[    2.541656] RAPL PMU: hw unit of domain package 2^-14 Joules
[    2.541656] RAPL PMU: hw unit of domain dram 2^-14 Joules
[    2.541657] RAPL PMU: hw unit of domain pp1-gpu 2^-14 Joules
[    2.541657] RAPL PMU: hw unit of domain psys 2^-14 Joules
[    2.550632] random: crng init done
[    2.550634] random: 7 urandom warning(s) missed due to ratelimiting
[    2.563062] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    2.571404] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    2.571406] AMD IOMMUv2 functionality not available on this system
[    2.576444] PKCS#7 signature not signed with a trusted key
[    2.576454] amdkcl: loading out-of-tree module taints kernel.
[    2.576493] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    2.604952] thinkpad_acpi: Standard ACPI backlight interface available, not loading native one
[    2.612096] [drm] Memory usable by graphics device = 4096M
[    2.612099] checking generic (d0000000 7f0000) vs hw (d0000000 10000000)
[    2.612100] fb: switching to inteldrmfb from EFI VGA
[    2.612136] Console: switching to colour dummy device 80x25
[    2.612756] [drm] Replacing VGA console driver
[    2.620160] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    2.620162] [drm] Driver supports precise vblank timestamp query.
[    2.622855] i915 0000:00:02.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=io+mem
[    2.627555] [drm] Finished loading DMC firmware i915/kbl_dmc_ver1_01.bin (v1.1)
[    2.628349] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    2.631970] [drm] Initialized i915 1.6.0 20171023 for 0000:00:02.0 on minor 0
[    2.652285] Warning: fail to get symbol drm_fb_helper_release_fbi, replace it with kcl stub
[    2.654212] r8822be: module is from the staging directory, the quality is unknown, you have been warned.
[    2.656213] r8822be 0000:05:00.0: enabling device (0000 -> 0003)
[    2.681140] PKCS#7 signature not signed with a trusted key
[    2.683595] PKCS#7 signature not signed with a trusted key
[    2.692502] PKCS#7 signature not signed with a trusted key
[    2.715167] r8822be: Using firmware rtlwifi/rtl8822befw.bin
[    2.717233] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[    2.717544] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input9
[    2.726650] PKCS#7 signature not signed with a trusted key
[    2.730655] intel_rapl: Found RAPL domain package
[    2.730658] intel_rapl: Found RAPL domain core
[    2.730659] intel_rapl: Found RAPL domain uncore
[    2.730661] intel_rapl: Found RAPL domain dram
[    2.731889] ieee80211 phy0: Selected rate control algorithm 'rtl_rc'
[    2.732857] r8822be: rtlwifi: wireless switch is on
[    2.741607] r8822be 0000:05:00.0 wlp5s0: renamed from wlan0
[    2.747549] [drm] amdgpu kernel modesetting enabled.
[    2.747554] [drm] amdgpu version: 19.10.8.418
[    2.747556] [drm] OS DRM version: 4.15.0
[    2.747601] vga_switcheroo: detected switching method \_SB_.PCI0.GFX0.ATPX handle
[    2.747690] ATPX version 1, functions 0x00000033
[    2.747784] ATPX Hybrid Graphics
[    2.750299] CRAT table not found
[    2.750307] Virtual CRAT table created for CPU
[    2.750308] Parsing CRAT table with 1 nodes
[    2.750316] Creating topology SYSFS entries
[    2.750339] Topology: Add CPU node
[    2.750339] Finished initializing topology
[    2.754769] [drm] initializing kernel modesetting (POLARIS12 0x1002:0x699F 0x17AA:0x5069 0xC0).
[    2.820951] [drm] register mmio base: 0xF2400000
[    2.820952] [drm] register mmio size: 262144
[    2.820963] [drm] add ip block number 0 <vi_common>
[    2.820964] [drm] add ip block number 1 <gmc_v8_0>
[    2.820965] [drm] add ip block number 2 <tonga_ih>
[    2.820966] [drm] add ip block number 3 <gfx_v8_0>
[    2.820967] [drm] add ip block number 4 <sdma_v3_0>
[    2.820967] [drm] add ip block number 5 <powerplay>
[    2.820968] [drm] add ip block number 6 <dm>
[    2.820969] [drm] add ip block number 7 <uvd_v6_0>
[    2.820969] [drm] add ip block number 8 <vce_v3_0>
[    2.820975] kfd kfd: skipped device 1002:699f, PCI rejects atomics
[    2.820989] [drm] UVD is enabled in VM mode
[    2.820989] [drm] UVD ENC is enabled in VM mode
[    2.820992] [drm] VCE enabled in VM mode
[    2.821003] vga_switcheroo: enabled
[    2.868355] snd_hda_intel 0000:00:1f.3: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
[    2.913845] psmouse serio1: synaptics: queried max coordinates: x [..5676], y [..4690]
[    2.938047] ACPI Error: Field [TBF3] at bit offset/length 262144/32768 exceeds size of target Buffer (262144 bits) (20170831/dsopcode-235)
[    2.938061] 
               Initialized Local Variables for Method [GETB]:
[    2.938062]   Local0: 0000000085c818f3 <Obj>           Integer 0000000000040000
[    2.938067]   Local1: 00000000400516ec <Obj>           Integer 0000000000008000
[    2.938072] Initialized Arguments for Method [GETB]:  (3 arguments defined for method invocation)
[    2.938073]   Arg0:   0000000047f38a98 <Obj>           Integer 0000000000008000
[    2.938076]   Arg1:   00000000174e6b4a <Obj>           Integer 0000000000001000
[    2.938079]   Arg2:   00000000bec1a67e <Obj>           Buffer(32768) 85 0B 4D 4C 87 02 34 00
[    2.938096] ACPI Error: Method parse/execution failed \_SB.PCI0.GFX0.GETB, AE_AML_BUFFER_LIMIT (20170831/psparse-550)
[    2.938131] ACPI Error: Method parse/execution failed \_SB.PCI0.GFX0.ATRM, AE_AML_BUFFER_LIMIT (20170831/psparse-550)
[    2.938232] failed to evaluate ATRM got AE_AML_BUFFER_LIMIT
[    2.939627] ATOM BIOS: BR24844.001
[    2.939695] [drm] GPU posting now...
[    2.964410] input: ThinkPad Extra Buttons as /devices/platform/thinkpad_acpi/input/input8
[    2.969894] [drm] vm size is 64 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[    2.970448] amdgpu 0000:02:00.0: VRAM: 2048M 0x000000F400000000 - 0x000000F47FFFFFFF (2048M used)
[    2.970451] amdgpu 0000:02:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    2.970480] [drm] Detected VRAM RAM=2048M, BAR=256M
[    2.970481] [drm] RAM width 64bits GDDR5
[    2.970583] [TTM] Zone  kernel: Available graphics memory: 7429796 kiB
[    2.970585] [TTM] Initializing pool allocator
[    2.970589] [TTM] Initializing DMA pool allocator
[    2.970624] [drm] amdgpu: 2048M of VRAM memory ready
[    2.970625] [drm] amdgpu: 7739M of GTT memory ready.
[    2.970655] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    2.971592] [drm] PCIE GART of 256M enabled (table at 0x000000F400000000).
[    2.972507] [drm] Chained IB support enabled!
[    2.976738] [drm] Found UVD firmware Version: 1.130 Family ID: 16
[    2.979495] [drm] Found VCE firmware Version: 53.26 Binary ID: 3
[    2.979787] psmouse serio1: synaptics: queried min coordinates: x [1266..], y [1162..]
[    2.979797] psmouse serio1: synaptics: Your touchpad (PNP: LEN2054 PNP0f13) says it can support a different bus. If i2c-hid and hid-rmi are not used, you might want to try setting psmouse.synaptics_intertouch to 1 and report this to linux-input@vger.kernel.org.
[    3.060462] [drm] DM_PPLIB: values for Engine clock
[    3.060463] [drm] DM_PPLIB:	 214000
[    3.060464] [drm] DM_PPLIB:	 547000
[    3.060464] [drm] DM_PPLIB:	 786000
[    3.060465] [drm] DM_PPLIB:	 902000
[    3.060465] [drm] DM_PPLIB: Validation clocks:
[    3.060466] [drm] DM_PPLIB:    engine_max_clock: 90200
[    3.060466] [drm] DM_PPLIB:    memory_max_clock: 150000
[    3.060466] [drm] DM_PPLIB:    level           : 8
[    3.060467] [drm] DM_PPLIB: values for Memory clock
[    3.060468] [drm] DM_PPLIB:	 300000
[    3.060468] [drm] DM_PPLIB:	 625000
[    3.060468] [drm] DM_PPLIB:	 1500000
[    3.060468] [drm] DM_PPLIB: Validation clocks:
[    3.060469] [drm] DM_PPLIB:    engine_max_clock: 90200
[    3.060469] [drm] DM_PPLIB:    memory_max_clock: 150000
[    3.060469] [drm] DM_PPLIB:    level           : 8
[    3.061352] [drm] Display Core initialized with v3.2.14!
[    3.061384] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    3.061384] [drm] Driver supports precise vblank timestamp query.
[    3.077361] psmouse serio1: synaptics: Touchpad model: 1, fw: 8.16, id: 0x1e2b1, caps: 0xf002a3/0x940300/0x12e800/0x400000, board id: 3383, fw id: 2664280
[    3.077365] psmouse serio1: synaptics: serio: Synaptics pass-through port at isa0060/serio1/input0
[    3.097425] fbcon: inteldrmfb (fb0) is primary device
[    3.097510] Console: switching to colour frame buffer device 240x67
[    3.097539] i915 0000:00:02.0: fb0: inteldrmfb frame buffer device
[    3.099930] [drm] UVD and UVD ENC initialized successfully.
[    3.140706] input: SynPS/2 Synaptics TouchPad as /devices/platform/i8042/serio1/input/input7
[    3.199890] [drm] VCE initialized successfully.
[    3.202604] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:02:00.0 on minor 1
[    3.237218] snd_hda_codec_conexant hdaudioC0D0: CX20753/4: BIOS auto-probing.
[    3.237512] snd_hda_codec_conexant hdaudioC0D0: autoconfig for CX20753/4: line_outs=1 (0x17/0x0/0x0/0x0/0x0) type:speaker
[    3.237513] snd_hda_codec_conexant hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[    3.237514] snd_hda_codec_conexant hdaudioC0D0:    hp_outs=1 (0x16/0x0/0x0/0x0/0x0)
[    3.237515] snd_hda_codec_conexant hdaudioC0D0:    mono: mono_out=0x0
[    3.237516] snd_hda_codec_conexant hdaudioC0D0:    inputs:
[    3.237517] snd_hda_codec_conexant hdaudioC0D0:      Internal Mic=0x1a
[    3.237518] snd_hda_codec_conexant hdaudioC0D0:      Mic=0x19
[    3.238281] snd_hda_codec_conexant hdaudioC0D0: Enable sync_write for stable communication
[    3.250573] input: HDA Intel PCH Mic as /devices/pci0000:00/0000:00:1f.3/sound/card0/input11
[    3.250648] input: HDA Intel PCH Headphone as /devices/pci0000:00/0000:00:1f.3/sound/card0/input12
[    3.250698] input: HDA Intel PCH HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input13
[    3.250747] input: HDA Intel PCH HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input14
[    3.250798] input: HDA Intel PCH HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input15
[    3.250844] input: HDA Intel PCH HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input16
[    3.250897] input: HDA Intel PCH HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input17
[    3.740594] [drm] RC6 on
[    3.818346] psmouse serio2: trackpoint: Elan TrackPoint firmware: 0x10, buttons: 3/3
[    4.132998] input: TPPS/2 Elan TrackPoint as /devices/platform/i8042/serio1/serio2/input/input10
[    5.002769] audit: type=1400 audit(1555019097.162:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=801 comm="apparmor_parser"
[    5.002890] audit: type=1400 audit(1555019097.162:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-xpdfimport" pid=803 comm="apparmor_parser"
[    5.003557] audit: type=1400 audit(1555019097.162:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/core/4486/usr/lib/snapd/snap-confine" pid=796 comm="apparmor_parser"
[    5.003560] audit: type=1400 audit(1555019097.162:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/core/4486/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=796 comm="apparmor_parser"
[    5.003583] audit: type=1400 audit(1555019097.162:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oopslash" pid=800 comm="apparmor_parser"
[    5.003992] audit: type=1400 audit(1555019097.162:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=795 comm="apparmor_parser"
[    5.003994] audit: type=1400 audit(1555019097.162:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=795 comm="apparmor_parser"
[    5.003997] audit: type=1400 audit(1555019097.162:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=795 comm="apparmor_parser"
[    5.003999] audit: type=1400 audit(1555019097.162:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=795 comm="apparmor_parser"
[    5.453819] IPv6: ADDRCONF(NETDEV_UP): enp3s0: link is not ready
[    5.497985] r8169 0000:03:00.0 enp3s0: link down
[    5.498055] IPv6: ADDRCONF(NETDEV_UP): enp3s0: link is not ready
[    5.500500] IPv6: ADDRCONF(NETDEV_UP): wlp5s0: link is not ready
[    6.133972] IPv6: ADDRCONF(NETDEV_UP): wlp5s0: link is not ready
[    6.224110] IPv6: ADDRCONF(NETDEV_UP): wlp5s0: link is not ready
[    9.836587] wlp5s0: authenticate with a0:21:b7:68:8b:3a
[    9.873299] wlp5s0: send auth to a0:21:b7:68:8b:3a (try 1/3)
[    9.875115] wlp5s0: authenticated
[    9.880294] wlp5s0: associate with a0:21:b7:68:8b:3a (try 1/3)
[    9.883188] wlp5s0: RX AssocResp from a0:21:b7:68:8b:3a (capab=0x411 status=0 aid=5)
[    9.883620] wlp5s0: associated
[    9.906369] IPv6: ADDRCONF(NETDEV_CHANGE): wlp5s0: link becomes ready
[   13.470682] amdgpu 0000:02:00.0: GPU pci config reset
[   14.830858] [drm] PCIE GART of 256M enabled (table at 0x000000F400000000).
[   14.951849] [drm] UVD and UVD ENC initialized successfully.
[   15.280883] [drm] VCE initialized successfully.
[   21.418261] amdgpu 0000:02:00.0: GPU pci config reset
[   23.103680] [drm] PCIE GART of 256M enabled (table at 0x000000F400000000).
[   23.225686] [drm] UVD and UVD ENC initialized successfully.
[   23.554713] [drm] VCE initialized successfully.
[   26.583914] rfkill: input handler disabled
[   30.211288] amdgpu 0000:02:00.0: GPU pci config reset
```
What could be the problem?

Thank you in advance. :)