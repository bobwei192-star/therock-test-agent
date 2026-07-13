# Getting hsa api call failure at line 900, when running /opt/rocm/bin/rocminfo 

- **Issue #:** 591
- **State:** closed
- **Created:** 2018-10-29T02:31:28Z
- **Updated:** 2018-10-29T17:36:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/591

I have installed rocm-dkms in my ubuntu os 18.04 LTS as per the instructions.

When I run the command /opt/rocm/bin/rocminfo I am getting the error
```
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
```

When I run /opt/rocm/opencl/bin/x86_64/clinfo, I am getting the error
```
terminate called after throwing an instance of 'cl::Error'
what(): clGetPlatformIDs
Aborted (core dumped)
```

uname -a gives:
```
Linux enio-notebook 4.15.0-38-generic #41-Ubuntu SMP Wed Oct 10 10:59:38 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

 dkms status gives:
```
amdgpu, 1.9-224, 4.15.0-38-generic, x86_64: installed
```

lsmod | grep amdgpu gives:
```
amdgpu               3194880  1
amdchash               16384  1 amdgpu
amd_sched              24576  1 amdgpu
amdttm                110592  1 amdgpu
amdkcl                 28672  4 amdkfd,amd_sched,amdttm,amdgpu
i2c_algo_bit           16384  2 amdgpu,i915
drm_kms_helper        172032  2 amdgpu,i915
drm                   401408  20 drm_kms_helper,amd_sched,amdttm,amdgpu,i915,amdkcl
```

lsmod | grep amdkfd gives:
```
amdkfd                274432  1
amd_iommu_v2           20480  1 amdkfd
amdkcl                 28672  4 amdkfd,amd_sched,amdttm,amdgpu
```

groups gives:
```
enio adm cdrom sudo dip video plugdev lpadmin sambashare
```

lspci | grep VGA gives:
```
00:02.0 VGA compatible controller: Intel Corporation HD Graphics 620 (rev 02)
```

lspci -vvv gives:
```
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 02)
	Subsystem: Dell Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
	Latency: 0
	Capabilities: <access denied>

00:02.0 VGA compatible controller: Intel Corporation HD Graphics 620 (rev 02) (prog-if 00 [VGA controller])
	Subsystem: Dell HD Graphics 620
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 128
	Region 0: Memory at de000000 (64-bit, non-prefetchable) [size=16M]
	Region 2: Memory at b0000000 (64-bit, prefetchable) [size=256M]
	Region 4: I/O ports at f000 [size=64]
	[virtual] Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: i915
	Kernel modules: i915

00:04.0 Signal processing controller: Intel Corporation Skylake Processor Thermal Subsystem (rev 02)
	Subsystem: Dell Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 16
	Region 0: Memory at df320000 (64-bit, non-prefetchable) [size=32K]
	Capabilities: <access denied>
	Kernel driver in use: proc_thermal
	Kernel modules: processor_thermal_device

00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21) (prog-if 30 [XHCI])
	Subsystem: Dell Sunrise Point-LP USB 3.0 xHCI Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 125
	Region 0: Memory at df310000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
	Subsystem: Dell Sunrise Point-LP Thermal subsystem
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin C routed to IRQ 18
	Region 0: Memory at df338000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: intel_pch_thermal
	Kernel modules: intel_pch_thermal

00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 (rev 21)
	Subsystem: Dell Sunrise Point-LP Serial IO I2C Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	Region 0: Memory at df337000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: intel-lpss
	Kernel modules: intel_lpss_pci

00:15.1 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 (rev 21)
	Subsystem: Dell Sunrise Point-LP Serial IO I2C Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin B routed to IRQ 17
	Region 0: Memory at df336000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: intel-lpss
	Kernel modules: intel_lpss_pci

00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
	Subsystem: Dell Sunrise Point-LP CSME HECI
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 130
	Region 0: Memory at df335000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: mei_me
	Kernel modules: mei_me

00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21) (prog-if 01 [AHCI 1.0])
	Subsystem: Dell Sunrise Point-LP SATA Controller [AHCI mode]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 126
	Region 0: Memory at df330000 (32-bit, non-prefetchable) [size=8K]
	Region 1: Memory at df334000 (32-bit, non-prefetchable) [size=256]
	Region 2: I/O ports at f090 [size=8]
	Region 3: I/O ports at f080 [size=4]
	Region 4: I/O ports at f060 [size=32]
	Region 5: Memory at df333000 (32-bit, non-prefetchable) [size=2K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port (rev f1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 122
	Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: df200000-df2fffff
	Prefetchable memory behind bridge: 00000000c0000000-00000000d01fffff
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
	Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: df100000-df1fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1c.5 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #6 (rev f1) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin B routed to IRQ 124
	Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
	I/O behind bridge: 0000d000-0000dfff
	Memory behind bridge: df000000-df0fffff
	Prefetchable memory behind bridge: 00000000d0300000-00000000d03fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1f.0 ISA bridge: Intel Corporation Sunrise Point-LP LPC Controller (rev 21)
	Subsystem: Dell Sunrise Point-LP LPC Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0

00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
	Subsystem: Dell Sunrise Point-LP PMC
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Region 0: Memory at df32c000 (32-bit, non-prefetchable) [size=16K]

00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
	Subsystem: Dell Sunrise Point-LP HD Audio
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 32
	Interrupt: pin A routed to IRQ 131
	Region 0: Memory at df328000 (64-bit, non-prefetchable) [size=16K]
	Region 4: Memory at df300000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel, snd_soc_skl

00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
	Subsystem: Dell Sunrise Point-LP SMBus
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 10
	Region 0: Memory at df332000 (64-bit, non-prefetchable) [size=256]
	Region 4: I/O ports at f040 [size=32]
	Kernel modules: i2c_i801

01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Topaz XT [Radeon R7 M260/M265 / M340/M360 / M440/M445] (rev c3)
	Subsystem: Dell Radeon R7 M445
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 129
	Region 0: Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at d0000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at e000 [size=256]
	Region 5: Memory at df200000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at df240000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

02:00.0 Network controller: Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter (rev 01)
	Subsystem: Dell QCA9565 / AR9565 Wireless Network Adapter
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 16
	Region 0: Memory at df100000 (64-bit, non-prefetchable) [size=512K]
	Expansion ROM at df180000 [disabled] [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: ath9k
	Kernel modules: ath9k

03:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller (rev 07)
	Subsystem: Dell RTL810xE PCI Express Fast Ethernet controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 127
	Region 0: I/O ports at d000 [size=256]
	Region 2: Memory at df000000 (64-bit, non-prefetchable) [size=4K]
	Region 4: Memory at d0300000 (64-bit, prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: r8169
	Kernel modules: r8169
```

lspci -tv gives:
```
-[0000:00]-+-00.0  Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
           +-02.0  Intel Corporation HD Graphics 620
           +-04.0  Intel Corporation Skylake Processor Thermal Subsystem
           +-14.0  Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller
           +-14.2  Intel Corporation Sunrise Point-LP Thermal subsystem
           +-15.0  Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0
           +-15.1  Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1
           +-16.0  Intel Corporation Sunrise Point-LP CSME HECI #1
           +-17.0  Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode]
           +-1c.0-[01]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Topaz XT [Radeon R7 M260/M265 / M340/M360 / M440/M445]
           +-1c.4-[02]----00.0  Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter
           +-1c.5-[03]----00.0  Realtek Semiconductor Co., Ltd. RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller
           +-1f.0  Intel Corporation Sunrise Point-LP LPC Controller
           +-1f.2  Intel Corporation Sunrise Point-LP PMC
           +-1f.3  Intel Corporation Sunrise Point-LP HD Audio
           \-1f.4  Intel Corporation Sunrise Point-LP SMBus
```

lspci -n gives:
```
00:00.0 0600: 8086:5904 (rev 02)
00:02.0 0300: 8086:5916 (rev 02)
00:04.0 1180: 8086:1903 (rev 02)
00:14.0 0c03: 8086:9d2f (rev 21)
00:14.2 1180: 8086:9d31 (rev 21)
00:15.0 1180: 8086:9d60 (rev 21)
00:15.1 1180: 8086:9d61 (rev 21)
00:16.0 0780: 8086:9d3a (rev 21)
00:17.0 0106: 8086:9d03 (rev 21)
00:1c.0 0604: 8086:9d10 (rev f1)
00:1c.4 0604: 8086:9d14 (rev f1)
00:1c.5 0604: 8086:9d15 (rev f1)
00:1f.0 0601: 8086:9d58 (rev 21)
00:1f.2 0580: 8086:9d21 (rev 21)
00:1f.3 0403: 8086:9d71 (rev 21)
00:1f.4 0c05: 8086:9d23 (rev 21)
01:00.0 0380: 1002:6900 (rev c3)
02:00.0 0280: 168c:0036 (rev 01)
03:00.0 0200: 10ec:8136 (rev 07)
```

dmesg | grep gives:
```
[    1.542967] [drm] amdgpu kernel modesetting enabled.
[    1.542968] [drm] amdgpu version: 18.30.2.15
[    1.582035] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    1.582036] amdgpu 0000:01:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    1.582456] [drm] amdgpu: 4096M of VRAM memory ready
[    1.582457] [drm] amdgpu: 7786M of GTT memory ready.
[    1.604836] amdgpu: [powerplay] can't get the mac of 5
[    1.615220] [drm] Initialized amdgpu 3.26.0 20150101 for 0000:01:00.0 on minor 1
[    8.796642] amdgpu: [powerplay] VI should always have 2 performance levels
[    8.839623] amdgpu 0000:01:00.0: GPU pci config reset
[   19.404684] amdgpu: [powerplay] can't get the mac of 5
[   24.796774] amdgpu: [powerplay] VI should always have 2 performance levels
[   24.847196] amdgpu 0000:01:00.0: GPU pci config reset
[   26.060661] amdgpu: [powerplay] can't get the mac of 5
[   36.848756] amdgpu: [powerplay] VI should always have 2 performance levels
[   36.909390] amdgpu 0000:01:00.0: GPU pci config reset
[   46.326426] amdgpu: [powerplay] can't get the mac of 5
[   52.876205] amdgpu: [powerplay] VI should always have 2 performance levels
[   52.923216] amdgpu 0000:01:00.0: GPU pci config reset
[  624.192176] amdgpu: [powerplay] can't get the mac of 5
[  629.969001] amdgpu: [powerplay] VI should always have 2 performance levels
[  630.012612] amdgpu 0000:01:00.0: GPU pci config reset
[  636.641803] amdgpu: [powerplay] can't get the mac of 5
[  642.001511] amdgpu: [powerplay] VI should always have 2 performance levels
[  642.053556] amdgpu 0000:01:00.0: GPU pci config reset
[  692.419116] amdgpu: [powerplay] can't get the mac of 5
[  697.811090] amdgpu: [powerplay] VI should always have 2 performance levels
[  697.858893] amdgpu 0000:01:00.0: GPU pci config reset
[  705.201539] amdgpu: [powerplay] can't get the mac of 5
[  710.867287] amdgpu: [powerplay] VI should always have 2 performance levels
[  710.918029] amdgpu 0000:01:00.0: GPU pci config reset
[ 2777.123730] amdgpu: [powerplay] can't get the mac of 5
[ 2782.916465] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2782.962468] amdgpu 0000:01:00.0: GPU pci config reset
[ 2801.494163] amdgpu: [powerplay] can't get the mac of 5
[ 2806.980131] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2807.031659] amdgpu 0000:01:00.0: GPU pci config reset
[ 2839.971557] amdgpu: [powerplay] can't get the mac of 5
[ 2845.003321] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2845.048056] amdgpu 0000:01:00.0: GPU pci config reset
[ 2890.210611] amdgpu: [powerplay] can't get the mac of 5
[ 2895.810505] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2895.857935] amdgpu 0000:01:00.0: GPU pci config reset
```

Could you please help