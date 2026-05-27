# When ROCm will support Vega M?

> **Issue #651**
> **状态**: closed
> **创建时间**: 2018-12-27T14:18:49Z
> **更新时间**: 2021-01-07T11:06:58Z
> **关闭时间**: 2021-01-07T10:44:12Z
> **作者**: JulieMei325
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/651

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Do you consider support Vega M in the future ROCm release? I think there are NUC users besides me want to setup AMD GPU support. Thanks!

---

## 评论 (44 条)

### 评论 #1 — 3D-360 (2018-12-28T20:08:34Z)

Vega M & Raven Ridge APU Vega.
Hopefully they can be released simultaneously.

---

### 评论 #2 — phush0 (2019-01-11T14:43:31Z)

I am also interested in ROCm working on VegaM, I have Precision 5530 2-in-1.


---

### 评论 #3 — RanbirRoshan (2019-01-14T20:57:07Z)

I am also very interested in ROCm support for Vega M. It would be a great support for working with the capabilities on laptops on go.

Adding to the question.. Is the support for Vega M even in the current backlog or pipeline? If yes, what does the tentative timeline looks like?

---

### 评论 #4 — kentrussell (2019-03-21T10:15:18Z)

The upstream kernel already supports VegaM, as does ROCK and the firmware shipped with it. I am adding support to ROCT for it now (hopefully to make it into 2.3). If things don't work (as I expect that they won't, but I could be pleasantly surprised), you can raise a bug report with the respective components (ROCR, HCC, etc), and hopefully they will be able to report whether or not they can/will support Vega M in their component.

@3D-360 As for Raven, the ROCK/ROCT support this (I am adding another Raven GPU ID to ROCT to cover those chips as well), so that's the same thing where you should do a bug report for whichever component isn't working. The generic ROCm Bug Report bucket is monitored by generic ROCm people. The specific component Bug Reports are monitored by the teams in charge of that component, so it's easier to get a response from someone on that specific team.

---

### 评论 #5 — phush0 (2019-03-21T11:44:25Z)

unfortunately in kernel 5.0.3

`amdgpu 0000:01:00.0: kfd not supported on this ASIC`

```
lspci -n
00:00.0 0600: 8086:5910 (rev 05)
00:01.0 0604: 8086:1901 (rev 05)
00:02.0 0300: 8086:591b (rev 04)
00:04.0 1180: 8086:1903 (rev 05)
00:13.0 0000: 8086:a135 (rev 31)
00:14.0 0c03: 8086:a12f (rev 31)
00:14.2 1180: 8086:a131 (rev 31)
00:15.0 1180: 8086:a160 (rev 31)
00:15.1 1180: 8086:a161 (rev 31)
00:16.0 0780: 8086:a13a (rev 31)
00:16.3 0700: 8086:a13d (rev 31)
00:1c.0 0604: 8086:a110 (rev f1)
00:1c.4 0604: 8086:a114 (rev f1)
00:1d.0 0604: 8086:a118 (rev f1)
00:1d.4 0604: 8086:a11c (rev f1)
00:1f.0 0601: 8086:a153 (rev 31)
00:1f.2 0580: 8086:a121 (rev 31)
00:1f.3 0403: 8086:a171 (rev 31)
00:1f.4 0c05: 8086:a123 (rev 31)
01:00.0 0380: 1002:694f (rev c0)
02:00.0 0280: 8086:24fd (rev 78)
03:00.0 ff00: 10ec:525a (rev 01)
04:00.0 0604: 8086:15d3 (rev 02)
05:00.0 0604: 8086:15d3 (rev 02)
05:01.0 0604: 8086:15d3 (rev 02)
05:02.0 0604: 8086:15d3 (rev 02)
05:04.0 0604: 8086:15d3 (rev 02)
06:00.0 0880: 8086:15d2 (rev 02)
07:00.0 0604: 8086:1549
08:00.0 0604: 8086:1549
09:00.0 0200: 14e4:1682
6f:00.0 0108: 144d:a808
```

```
lspci -k
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 05)
	Subsystem: Dell Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) (rev 05)
	Kernel driver in use: pcieport
00:02.0 VGA compatible controller: Intel Corporation Device 591b (rev 04)
	Subsystem: Dell Device 08ac
	Kernel driver in use: i915
	Kernel modules: i915
00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 05)
	Subsystem: Dell Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem
	Kernel driver in use: proc_thermal
	Kernel modules: processor_thermal_device
00:13.0 Non-VGA unclassified device: Intel Corporation 100 Series/C230 Series Chipset Family Integrated Sensor Hub (rev 31)
	Subsystem: Dell Sunrise Point-H Integrated Sensor Hub
	Kernel driver in use: intel_ish_ipc
	Kernel modules: intel_ish_ipc
00:14.0 USB controller: Intel Corporation 100 Series/C230 Series Chipset Family USB 3.0 xHCI Controller (rev 31)
	Subsystem: Dell Sunrise Point-H USB 3.0 xHCI Controller
	Kernel driver in use: xhci_hcd
00:14.2 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Thermal Subsystem (rev 31)
	Subsystem: Dell Sunrise Point-H Thermal subsystem
	Kernel driver in use: intel_pch_thermal
	Kernel modules: intel_pch_thermal
00:15.0 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Serial IO I2C Controller #0 (rev 31)
	Subsystem: Dell Sunrise Point-H Serial IO I2C Controller
	Kernel driver in use: intel-lpss
	Kernel modules: intel_lpss_pci
00:15.1 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Serial IO I2C Controller #1 (rev 31)
	Subsystem: Dell Sunrise Point-H Serial IO I2C Controller
	Kernel driver in use: intel-lpss
	Kernel modules: intel_lpss_pci
00:16.0 Communication controller: Intel Corporation 100 Series/C230 Series Chipset Family MEI Controller #1 (rev 31)
	Subsystem: Dell Sunrise Point-H CSME HECI
	Kernel driver in use: mei_me
	Kernel modules: mei_me
00:16.3 Serial controller: Intel Corporation 100 Series/C230 Series Chipset Family KT Redirection (rev 31)
	Subsystem: Dell Sunrise Point-H KT Redirection
	Kernel driver in use: serial
00:1c.0 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #1 (rev f1)
	Kernel driver in use: pcieport
00:1c.4 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #5 (rev f1)
	Kernel driver in use: pcieport
00:1d.0 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #9 (rev f1)
	Kernel driver in use: pcieport
00:1d.4 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #13 (rev f1)
	Kernel driver in use: pcieport
00:1f.0 ISA bridge: Intel Corporation QM175 Chipset LPC/eSPI Controller (rev 31)
	Subsystem: Dell Sunrise Point-H LPC Controller
00:1f.2 Memory controller: Intel Corporation 100 Series/C230 Series Chipset Family Power Management Controller (rev 31)
	Subsystem: Dell Sunrise Point-H PMC
00:1f.3 Audio device: Intel Corporation CM238 HD Audio Controller (rev 31)
	Subsystem: Dell CM238 HD Audio Controller
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel
00:1f.4 SMBus: Intel Corporation 100 Series/C230 Series Chipset Family SMBus (rev 31)
	Subsystem: Dell Sunrise Point-H SMBus
	Kernel modules: i2c_i801
01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 694f (rev c0)
	Subsystem: Dell Device 08ac
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
02:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)
	Subsystem: Intel Corporation Wireless 8265 / 8275
	Kernel driver in use: iwlwifi
	Kernel modules: iwlwifi
03:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader (rev 01)
	Subsystem: Dell RTS525A PCI Express Card Reader
	Kernel driver in use: rtsx_pci
	Kernel modules: rtsx_pci
04:00.0 PCI bridge: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] (rev 02)
	Kernel driver in use: pcieport
05:00.0 PCI bridge: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] (rev 02)
	Kernel driver in use: pcieport
05:01.0 PCI bridge: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] (rev 02)
	Kernel driver in use: pcieport
05:02.0 PCI bridge: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] (rev 02)
	Kernel driver in use: pcieport
05:04.0 PCI bridge: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] (rev 02)
	Kernel driver in use: pcieport
06:00.0 System peripheral: Intel Corporation JHL6540 Thunderbolt 3 NHI (C step) [Alpine Ridge 4C 2016] (rev 02)
	Subsystem: Dell JHL6540 Thunderbolt 3 NHI (C step) [Alpine Ridge 4C 2016]
	Kernel driver in use: thunderbolt
	Kernel modules: thunderbolt
07:00.0 PCI bridge: Intel Corporation DSL2210 Thunderbolt Controller [Port Ridge 1C 2011]
	Kernel driver in use: pcieport
08:00.0 PCI bridge: Intel Corporation DSL2210 Thunderbolt Controller [Port Ridge 1C 2011]
	Kernel driver in use: pcieport
09:00.0 Ethernet controller: Broadcom Inc. and subsidiaries NetXtreme BCM57762 Gigabit Ethernet PCIe
	Subsystem: Apple Inc. Thunderbolt to Gigabit Ethernet Adapter
	Kernel driver in use: tg3
	Kernel modules: tg3
6f:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981
	Subsystem: Samsung Electronics Co Ltd Device a801
	Kernel driver in use: nvme
	Kernel modules: nvme
```
```
uname -r
5.0.3-050003-generic
```



---

### 评论 #6 — kentrussell (2019-03-21T11:59:52Z)

Indeed, I see that too. My ROCT patch needs a corresponding ROCK patch to get that working. Hopefully I can get that into 2.3 as well (compile-testing it now, since I don't have a VegaM to test on)

---

### 评论 #7 — bastibe (2019-04-28T08:27:38Z)

Thank you for working on this! I am extremely interested in ROCm for Vega M as well, for my new NUC8i7HVK and Darktable.

I'd be happy to help with this if there is anything I can do to help.

---

### 评论 #8 — mirh (2019-04-29T09:12:13Z)

KFD is coming with next kernel cycle likely
https://www.phoronix.com/scan.php?page=news_item&px=AMDKFD-Vega-M-Plus-More

---

### 评论 #9 — HulioVRD (2019-05-22T11:10:26Z)

After building kernel from [Kernel source](https://cgit.freedesktop.org/~agd5f/linux/?h=drm-next) with commit [commit](https://cgit.freedesktop.org/~agd5f/linux/commit/?h=drm-next&id=5c3fc06975a69c77e7126a00841135c40582b416) there's still problem with Vega M support on my machine.

Device: NUC8i7HNK

```
uname -a
Linux user-NUC8i7HNK 5.2.0-rc1-amd+ #1 SMP Tue May 21 11:55:06 CEST 2019 x86_64 x86_64 x86_64 GNU/Linux

cat /sys/class/drm/card0/device/device
0x694e

lsmod | grep amd
amdgpu               3162112  23
gpu_sched              32768  1 amdgpu
drm_kms_helper        184320  1 amdgpu
ttm                   102400  1 amdgpu
drm                   450560  17 gpu_sched,drm_kms_helper,amdgpu,ttm
i2c_algo_bit           16384  2 igb,amdgpu

dkms status
(nothing)

dmesg | grep amd
[    0.000000] Linux version 5.2.0-rc1-amd+ (root@user-NUC8i7HNK) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04)) #1 SMP Tue May 21 11:55:06 CEST 2019
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.2.0-rc1-amd+ root=UUID=a71b4f73-6318-41df-b754-480f21b7ecd8 ro quiet splash vt.handoff=1
[    0.029045] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-5.2.0-rc1-amd+ root=UUID=a71b4f73-6318-41df-b754-480f21b7ecd8 ro quiet splash vt.handoff=1
[    0.535600] usb usb1: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    0.536678] usb usb2: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    0.592518] usb usb3: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    0.592753] usb usb4: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    4.818317] [drm] amdgpu kernel modesetting enabled.
[    4.818353] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 0: 0x2fe0000000 -> 0x2fefffffff
[    4.818355] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 2: 0x2ff0000000 -> 0x2ff01fffff
[    4.818356] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xdb500000 -> 0xdb53ffff
[    4.818358] fb0: switching to amdgpudrmfb from EFI VGA
[    4.819039] amdgpu 0000:01:00.0: vgaarb: deactivate vga console
[    4.819085] amdgpu 0000:01:00.0: enabling device (0006 -> 0007)
[    4.819331] amdgpu 0000:01:00.0: kfd not supported on this ASIC
[    4.819419] amdgpu 0000:01:00.0: BAR 2: releasing [mem 0x2ff0000000-0x2ff01fffff 64bit pref]
[    4.819421] amdgpu 0000:01:00.0: BAR 0: releasing [mem 0x2fe0000000-0x2fefffffff 64bit pref]
[    4.819445] amdgpu 0000:01:00.0: BAR 0: assigned [mem 0x2000000000-0x20ffffffff 64bit pref]
[    4.819450] amdgpu 0000:01:00.0: BAR 2: assigned [mem 0x2100000000-0x21001fffff 64bit pref]
[    4.819474] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    4.819475] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    4.819534] [drm] amdgpu: 4096M of VRAM memory ready
[    4.819536] [drm] amdgpu: 4096M of GTT memory ready.
[    5.104982] fbcon: amdgpudrmfb (fb0) is primary device
[    5.143751] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    5.171670] [drm] Initialized amdgpu 3.32.0 20150101 for 0000:01:00.0 on minor 0
[    7.684194] usb usb5: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    7.685499] usb usb6: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[  265.424968] usb usb5: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[  265.426743] usb usb6: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd

lspci -vvv
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 05)
Subsystem: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort+ <MAbort+ >SERR- <PERR- INTx-
Latency: 0
Capabilities: <access denied>

00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) (rev 05) (prog-if 00 [Normal decode])
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 121
Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
I/O behind bridge: 0000e000-0000efff
Memory behind bridge: db500000-dbefffff
Prefetchable memory behind bridge: 0000002000000000-000000217fffffff
Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
BridgeCtl: Parity- SERR+ NoISA- VGA+ MAbort- >Reset- FastB2B-
PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
Capabilities: <access denied>
Kernel driver in use: pcieport

00:01.1 PCI bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x8) (rev 05) (prog-if 00 [Normal decode])
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 122
Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
I/O behind bridge: 0000d000-0000dfff
Memory behind bridge: dab00000-db4fffff
Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
BridgeCtl: Parity- SERR+ NoISA+ VGA- MAbort- >Reset- FastB2B-
PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
Capabilities: <access denied>
Kernel driver in use: pcieport

00:01.2 PCI bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x4) (rev 05) (prog-if 00 [Normal decode])
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 123
Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
I/O behind bridge: 0000c000-0000cfff
Memory behind bridge: da100000-daafffff
Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
BridgeCtl: Parity- SERR+ NoISA+ VGA- MAbort- >Reset- FastB2B-
PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
Capabilities: <access denied>
Kernel driver in use: pcieport

00:08.0 System peripheral: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model
Subsystem: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model
Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Interrupt: pin A routed to IRQ 255
Region 0: Memory at 2ffff2b000 (64-bit, non-prefetchable) [disabled] [size=4K]
Capabilities: <access denied>

00:14.0 USB controller: Intel Corporation 100 Series/C230 Series Chipset Family USB 3.0 xHCI Controller (rev 31) (prog-if 30 [XHCI])
Subsystem: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0
Interrupt: pin A routed to IRQ 129
Region 0: Memory at 2ffff10000 (64-bit, non-prefetchable) [size=64K]
Capabilities: <access denied>
Kernel driver in use: xhci_hcd

00:14.2 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Thermal Subsystem (rev 31)
Subsystem: Intel Corporation Sunrise Point-H Thermal subsystem
Control: I/O- Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Interrupt: pin C routed to IRQ 18
Region 0: Memory at 2ffff2a000 (64-bit, non-prefetchable) [size=4K]
Capabilities: <access denied>
Kernel driver in use: intel_pch_thermal
Kernel modules: intel_pch_thermal

00:15.0 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Serial IO I2C Controller #0 (rev 31)
Subsystem: Intel Corporation Sunrise Point-H Serial IO I2C Controller
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 16
Region 0: Memory at 2ffff29000 (64-bit, non-prefetchable) [size=4K]
Capabilities: <access denied>
Kernel driver in use: intel-lpss
Kernel modules: intel_lpss_pci

00:15.1 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Serial IO I2C Controller #1 (rev 31)
Subsystem: Intel Corporation Sunrise Point-H Serial IO I2C Controller
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin B routed to IRQ 17
Region 0: Memory at 2ffff28000 (64-bit, non-prefetchable) [size=4K]
Capabilities: <access denied>
Kernel driver in use: intel-lpss
Kernel modules: intel_lpss_pci

00:15.2 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Serial IO I2C Controller #2 (rev 31)
Subsystem: Intel Corporation Device 2073
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin C routed to IRQ 18
Region 0: Memory at 2ffff27000 (64-bit, non-prefetchable) [size=4K]
Capabilities: <access denied>
Kernel driver in use: intel-lpss
Kernel modules: intel_lpss_pci

00:16.0 Communication controller: Intel Corporation 100 Series/C230 Series Chipset Family MEI Controller #1 (rev 31)
Subsystem: Intel Corporation Sunrise Point-H CSME HECI
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0
Interrupt: pin A routed to IRQ 154
Region 0: Memory at 2ffff26000 (64-bit, non-prefetchable) [size=4K]
Capabilities: <access denied>
Kernel driver in use: mei_me
Kernel modules: mei_me

00:1c.0 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #1 (rev f1) (prog-if 00 [Normal decode])
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 124
Bus: primary=00, secondary=04, subordinate=04, sec-latency=0
I/O behind bridge: 0000f000-00000fff
Memory behind bridge: fff00000-000fffff
Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
Capabilities: <access denied>
Kernel driver in use: pcieport

00:1c.1 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #2 (rev f1) (prog-if 00 [Normal decode])
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin B routed to IRQ 125
Bus: primary=00, secondary=05, subordinate=05, sec-latency=0
I/O behind bridge: 0000b000-0000bfff
Memory behind bridge: dc100000-dc1fffff
Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
Capabilities: <access denied>
Kernel driver in use: pcieport

00:1c.2 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #3 (rev f1) (prog-if 00 [Normal decode])
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin C routed to IRQ 126
Bus: primary=00, secondary=06, subordinate=06, sec-latency=0
I/O behind bridge: 0000f000-00000fff
Memory behind bridge: dc000000-dc0fffff
Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
Capabilities: <access denied>
Kernel driver in use: pcieport

00:1c.4 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #5 (rev f1) (prog-if 00 [Normal decode])
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 127
Bus: primary=00, secondary=07, subordinate=71, sec-latency=0
I/O behind bridge: 00002000-00002fff
Memory behind bridge: ac000000-da0fffff
Prefetchable memory behind bridge: 0000002f90000000-0000002fd9ffffff
Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
Capabilities: <access denied>
Kernel driver in use: pcieport

00:1d.0 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #9 (rev f1) (prog-if 00 [Normal decode])
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 128
Bus: primary=00, secondary=72, subordinate=72, sec-latency=0
I/O behind bridge: 0000f000-00000fff
Memory behind bridge: dbf00000-dbffffff
Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
Capabilities: <access denied>
Kernel driver in use: pcieport

00:1e.0 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Serial IO UART #0 (rev 31)
Subsystem: Intel Corporation Sunrise Point-H Serial IO UART
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 20
Region 0: Memory at 2ffff25000 (64-bit, non-prefetchable) [size=4K]
Capabilities: <access denied>
Kernel driver in use: intel-lpss
Kernel modules: intel_lpss_pci

00:1f.0 ISA bridge: Intel Corporation HM175 Chipset LPC/eSPI Controller (rev 31)
Subsystem: Intel Corporation Sunrise Point-H LPC Controller
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0

00:1f.2 Memory controller: Intel Corporation 100 Series/C230 Series Chipset Family Power Management Controller (rev 31)
Subsystem: Intel Corporation Sunrise Point-H PMC
Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Region 0: Memory at dc220000 (32-bit, non-prefetchable) [disabled] [size=16K]

00:1f.3 Audio device: Intel Corporation CM238 HD Audio Controller (rev 31)
Subsystem: Intel Corporation CM238 HD Audio Controller
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 32, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 156
Region 0: Memory at 2ffff20000 (64-bit, non-prefetchable) [size=16K]
Region 4: Memory at 2ffff00000 (64-bit, non-prefetchable) [size=64K]
Capabilities: <access denied>
Kernel driver in use: snd_hda_intel
Kernel modules: snd_hda_intel

00:1f.4 SMBus: Intel Corporation 100 Series/C230 Series Chipset Family SMBus (rev 31)
Subsystem: Intel Corporation Sunrise Point-H SMBus
Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
Status: Cap- 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Interrupt: pin A routed to IRQ 255
Region 0: Memory at 2ffff24000 (64-bit, non-prefetchable) [size=256]
Region 4: I/O ports at f000 [size=32]

00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (2) I219-LM (rev 31)
Subsystem: Intel Corporation Ethernet Connection (2) I219-LM
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0
Interrupt: pin A routed to IRQ 139
Region 0: Memory at dc200000 (32-bit, non-prefetchable) [size=128K]
Capabilities: <access denied>
Kernel driver in use: e1000e
Kernel modules: e1000e

01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Polaris 22 [Radeon RX Vega M GL] (rev c0) (prog-if 00 [VGA controller])
Subsystem: Intel Corporation Device 2073
Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 158
Region 0: Memory at 2000000000 (64-bit, prefetchable) [size=4G]
Region 2: Memory at 2100000000 (64-bit, prefetchable) [size=2M]
Region 4: I/O ports at e000 [size=256]
Region 5: Memory at db500000 (32-bit, non-prefetchable) [size=256K]
Expansion ROM at 000c0000 [disabled] [size=128K]
Capabilities: <access denied>
Kernel driver in use: amdgpu
Kernel modules: amdgpu

01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device ab08
Subsystem: Intel Corporation Device 2073
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin B routed to IRQ 157
Region 0: Memory at db560000 (64-bit, non-prefetchable) [size=16K]
Capabilities: <access denied>
Kernel driver in use: snd_hda_intel
Kernel modules: snd_hda_intel

02:00.0 USB controller: ASMedia Technology Inc. Device 2142 (prog-if 30 [XHCI])
Subsystem: Intel Corporation Device 2073
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 17
Region 0: Memory at dab00000 (64-bit, non-prefetchable) [size=32K]
Capabilities: <access denied>
Kernel driver in use: xhci_hcd

03:00.0 SD Host controller: O2 Micro, Inc. SD/MMC Card Reader Controller (rev 01) (prog-if 01)
Subsystem: Intel Corporation SD/MMC Card Reader Controller
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 138
Region 0: Memory at da101000 (32-bit, non-prefetchable) [size=4K]
Region 1: Memory at da100000 (32-bit, non-prefetchable) [size=2K]
Capabilities: <access denied>
Kernel driver in use: sdhci-pci
Kernel modules: sdhci_pci

05:00.0 Ethernet controller: Intel Corporation I210 Gigabit Network Connection (rev 03)
Subsystem: Intel Corporation I210 Gigabit Network Connection
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 17
Region 0: Memory at dc100000 (32-bit, non-prefetchable) [size=128K]
Region 2: I/O ports at b000 [disabled] [size=32]
Region 3: Memory at dc120000 (32-bit, non-prefetchable) [size=16K]
Capabilities: <access denied>
Kernel driver in use: igb
Kernel modules: igb

06:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)
Subsystem: Intel Corporation Dual Band Wireless-AC 8265
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 155
Region 0: Memory at dc000000 (64-bit, non-prefetchable) [size=8K]
Capabilities: <access denied>
Kernel driver in use: iwlwifi
Kernel modules: iwlwifi

72:00.0 Non-Volatile memory controller: Silicon Motion, Inc. Device 2263 (rev 03) (prog-if 02 [NVM Express])
Subsystem: Silicon Motion, Inc. Device 2263
Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
Latency: 0, Cache Line Size: 64 bytes
Interrupt: pin A routed to IRQ 16
NUMA node: 0
Region 0: Memory at dbf00000 (64-bit, non-prefetchable) [size=16K]
Capabilities: <access denied>
Kernel driver in use: nvme
Kernel modules: nvme


modinfo amdgpu
filename:       /lib/modules/5.2.0-rc1-amd+/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko
license:        GPL and additional rights
description:    AMD GPU
author:         AMD linux driver team
firmware:       amdgpu/raven2_gpu_info.bin
firmware:       amdgpu/picasso_gpu_info.bin
firmware:       amdgpu/raven_gpu_info.bin
firmware:       amdgpu/vega12_gpu_info.bin
firmware:       amdgpu/vega10_gpu_info.bin
firmware:       amdgpu/mullins_mec.bin
firmware:       amdgpu/mullins_rlc.bin
firmware:       amdgpu/mullins_ce.bin
firmware:       amdgpu/mullins_me.bin
firmware:       amdgpu/mullins_pfp.bin
firmware:       amdgpu/kabini_mec.bin
firmware:       amdgpu/kabini_rlc.bin
firmware:       amdgpu/kabini_ce.bin
firmware:       amdgpu/kabini_me.bin
firmware:       amdgpu/kabini_pfp.bin
firmware:       amdgpu/kaveri_mec2.bin
firmware:       amdgpu/kaveri_mec.bin
firmware:       amdgpu/kaveri_rlc.bin
firmware:       amdgpu/kaveri_ce.bin
firmware:       amdgpu/kaveri_me.bin
firmware:       amdgpu/kaveri_pfp.bin
firmware:       amdgpu/hawaii_mec.bin
firmware:       amdgpu/hawaii_rlc.bin
firmware:       amdgpu/hawaii_ce.bin
firmware:       amdgpu/hawaii_me.bin
firmware:       amdgpu/hawaii_pfp.bin
firmware:       amdgpu/bonaire_mec.bin
firmware:       amdgpu/bonaire_rlc.bin
firmware:       amdgpu/bonaire_ce.bin
firmware:       amdgpu/bonaire_me.bin
firmware:       amdgpu/bonaire_pfp.bin
firmware:       amdgpu/mullins_sdma1.bin
firmware:       amdgpu/mullins_sdma.bin
firmware:       amdgpu/kabini_sdma1.bin
firmware:       amdgpu/kabini_sdma.bin
firmware:       amdgpu/kaveri_sdma1.bin
firmware:       amdgpu/kaveri_sdma.bin
firmware:       amdgpu/hawaii_sdma1.bin
firmware:       amdgpu/hawaii_sdma.bin
firmware:       amdgpu/bonaire_sdma1.bin
firmware:       amdgpu/bonaire_sdma.bin
firmware:       amdgpu/si58_mc.bin
firmware:       amdgpu/hainan_mc.bin
firmware:       amdgpu/oland_mc.bin
firmware:       amdgpu/verde_mc.bin
firmware:       amdgpu/pitcairn_mc.bin
firmware:       amdgpu/tahiti_mc.bin
firmware:       amdgpu/hainan_rlc.bin
firmware:       amdgpu/hainan_ce.bin
firmware:       amdgpu/hainan_me.bin
firmware:       amdgpu/hainan_pfp.bin
firmware:       amdgpu/oland_rlc.bin
firmware:       amdgpu/oland_ce.bin
firmware:       amdgpu/oland_me.bin
firmware:       amdgpu/oland_pfp.bin
firmware:       amdgpu/verde_rlc.bin
firmware:       amdgpu/verde_ce.bin
firmware:       amdgpu/verde_me.bin
firmware:       amdgpu/verde_pfp.bin
firmware:       amdgpu/pitcairn_rlc.bin
firmware:       amdgpu/pitcairn_ce.bin
firmware:       amdgpu/pitcairn_me.bin
firmware:       amdgpu/pitcairn_pfp.bin
firmware:       amdgpu/tahiti_rlc.bin
firmware:       amdgpu/tahiti_ce.bin
firmware:       amdgpu/tahiti_me.bin
firmware:       amdgpu/tahiti_pfp.bin
firmware:       amdgpu/banks_k_2_smc.bin
firmware:       amdgpu/hainan_k_smc.bin
firmware:       amdgpu/hainan_smc.bin
firmware:       amdgpu/oland_k_smc.bin
firmware:       amdgpu/oland_smc.bin
firmware:       amdgpu/verde_k_smc.bin
firmware:       amdgpu/verde_smc.bin
firmware:       amdgpu/pitcairn_k_smc.bin
firmware:       amdgpu/pitcairn_smc.bin
firmware:       amdgpu/tahiti_smc.bin
firmware:       amdgpu/topaz_mc.bin
firmware:       amdgpu/hawaii_mc.bin
firmware:       amdgpu/bonaire_mc.bin
firmware:       amdgpu/polaris12_k_mc.bin
firmware:       amdgpu/polaris10_k_mc.bin
firmware:       amdgpu/polaris11_k_mc.bin
firmware:       amdgpu/polaris12_mc.bin
firmware:       amdgpu/polaris10_mc.bin
firmware:       amdgpu/polaris11_mc.bin
firmware:       amdgpu/tonga_mc.bin
firmware:       amdgpu/vega12_asd.bin
firmware:       amdgpu/vega12_sos.bin
firmware:       amdgpu/vega10_asd.bin
firmware:       amdgpu/vega10_sos.bin
firmware:       amdgpu/raven2_asd.bin
firmware:       amdgpu/picasso_asd.bin
firmware:       amdgpu/raven_asd.bin
firmware:       amdgpu/vega20_ta.bin
firmware:       amdgpu/vega20_asd.bin
firmware:       amdgpu/vega20_sos.bin
firmware:       amdgpu/vegam_rlc.bin
firmware:       amdgpu/vegam_mec2.bin
firmware:       amdgpu/vegam_mec.bin
firmware:       amdgpu/vegam_me.bin
firmware:       amdgpu/vegam_pfp.bin
firmware:       amdgpu/vegam_ce.bin
firmware:       amdgpu/polaris12_rlc.bin
firmware:       amdgpu/polaris12_mec2_2.bin
firmware:       amdgpu/polaris12_mec2.bin
firmware:       amdgpu/polaris12_mec_2.bin
firmware:       amdgpu/polaris12_mec.bin
firmware:       amdgpu/polaris12_me_2.bin
firmware:       amdgpu/polaris12_me.bin
firmware:       amdgpu/polaris12_pfp_2.bin
firmware:       amdgpu/polaris12_pfp.bin
firmware:       amdgpu/polaris12_ce_2.bin
firmware:       amdgpu/polaris12_ce.bin
firmware:       amdgpu/polaris11_rlc.bin
firmware:       amdgpu/polaris11_mec2_2.bin
firmware:       amdgpu/polaris11_mec2.bin
firmware:       amdgpu/polaris11_mec_2.bin
firmware:       amdgpu/polaris11_mec.bin
firmware:       amdgpu/polaris11_me_2.bin
firmware:       amdgpu/polaris11_me.bin
firmware:       amdgpu/polaris11_pfp_2.bin
firmware:       amdgpu/polaris11_pfp.bin
firmware:       amdgpu/polaris11_ce_2.bin
firmware:       amdgpu/polaris11_ce.bin
firmware:       amdgpu/polaris10_rlc.bin
firmware:       amdgpu/polaris10_mec2_2.bin
firmware:       amdgpu/polaris10_mec2.bin
firmware:       amdgpu/polaris10_mec_2.bin
firmware:       amdgpu/polaris10_mec.bin
firmware:       amdgpu/polaris10_me_2.bin
firmware:       amdgpu/polaris10_me.bin
firmware:       amdgpu/polaris10_pfp_2.bin
firmware:       amdgpu/polaris10_pfp.bin
firmware:       amdgpu/polaris10_ce_2.bin
firmware:       amdgpu/polaris10_ce.bin
firmware:       amdgpu/fiji_rlc.bin
firmware:       amdgpu/fiji_mec2.bin
firmware:       amdgpu/fiji_mec.bin
firmware:       amdgpu/fiji_me.bin
firmware:       amdgpu/fiji_pfp.bin
firmware:       amdgpu/fiji_ce.bin
firmware:       amdgpu/topaz_rlc.bin
firmware:       amdgpu/topaz_mec.bin
firmware:       amdgpu/topaz_me.bin
firmware:       amdgpu/topaz_pfp.bin
firmware:       amdgpu/topaz_ce.bin
firmware:       amdgpu/tonga_rlc.bin
firmware:       amdgpu/tonga_mec2.bin
firmware:       amdgpu/tonga_mec.bin
firmware:       amdgpu/tonga_me.bin
firmware:       amdgpu/tonga_pfp.bin
firmware:       amdgpu/tonga_ce.bin
firmware:       amdgpu/stoney_rlc.bin
firmware:       amdgpu/stoney_mec.bin
firmware:       amdgpu/stoney_me.bin
firmware:       amdgpu/stoney_pfp.bin
firmware:       amdgpu/stoney_ce.bin
firmware:       amdgpu/carrizo_rlc.bin
firmware:       amdgpu/carrizo_mec2.bin
firmware:       amdgpu/carrizo_mec.bin
firmware:       amdgpu/carrizo_me.bin
firmware:       amdgpu/carrizo_pfp.bin
firmware:       amdgpu/carrizo_ce.bin
firmware:       amdgpu/raven2_rlc.bin
firmware:       amdgpu/raven2_mec2.bin
firmware:       amdgpu/raven2_mec.bin
firmware:       amdgpu/raven2_me.bin
firmware:       amdgpu/raven2_pfp.bin
firmware:       amdgpu/raven2_ce.bin
firmware:       amdgpu/picasso_rlc_am4.bin
firmware:       amdgpu/picasso_rlc.bin
firmware:       amdgpu/picasso_mec2.bin
firmware:       amdgpu/picasso_mec.bin
firmware:       amdgpu/picasso_me.bin
firmware:       amdgpu/picasso_pfp.bin
firmware:       amdgpu/picasso_ce.bin
firmware:       amdgpu/raven_rlc.bin
firmware:       amdgpu/raven_mec2.bin
firmware:       amdgpu/raven_mec.bin
firmware:       amdgpu/raven_me.bin
firmware:       amdgpu/raven_pfp.bin
firmware:       amdgpu/raven_ce.bin
firmware:       amdgpu/vega20_rlc.bin
firmware:       amdgpu/vega20_mec2.bin
firmware:       amdgpu/vega20_mec.bin
firmware:       amdgpu/vega20_me.bin
firmware:       amdgpu/vega20_pfp.bin
firmware:       amdgpu/vega20_ce.bin
firmware:       amdgpu/vega12_rlc.bin
firmware:       amdgpu/vega12_mec2.bin
firmware:       amdgpu/vega12_mec.bin
firmware:       amdgpu/vega12_me.bin
firmware:       amdgpu/vega12_pfp.bin
firmware:       amdgpu/vega12_ce.bin
firmware:       amdgpu/vega10_rlc.bin
firmware:       amdgpu/vega10_mec2.bin
firmware:       amdgpu/vega10_mec.bin
firmware:       amdgpu/vega10_me.bin
firmware:       amdgpu/vega10_pfp.bin
firmware:       amdgpu/vega10_ce.bin
firmware:       amdgpu/topaz_sdma1.bin
firmware:       amdgpu/topaz_sdma.bin
firmware:       amdgpu/vegam_sdma1.bin
firmware:       amdgpu/vegam_sdma.bin
firmware:       amdgpu/polaris12_sdma1.bin
firmware:       amdgpu/polaris12_sdma.bin
firmware:       amdgpu/polaris11_sdma1.bin
firmware:       amdgpu/polaris11_sdma.bin
firmware:       amdgpu/polaris10_sdma1.bin
firmware:       amdgpu/polaris10_sdma.bin
firmware:       amdgpu/stoney_sdma.bin
firmware:       amdgpu/fiji_sdma1.bin
firmware:       amdgpu/fiji_sdma.bin
firmware:       amdgpu/carrizo_sdma1.bin
firmware:       amdgpu/carrizo_sdma.bin
firmware:       amdgpu/tonga_sdma1.bin
firmware:       amdgpu/tonga_sdma.bin
firmware:       amdgpu/raven2_sdma.bin
firmware:       amdgpu/picasso_sdma.bin
firmware:       amdgpu/raven_sdma.bin
firmware:       amdgpu/vega20_sdma1.bin
firmware:       amdgpu/vega20_sdma.bin
firmware:       amdgpu/vega12_sdma1.bin
firmware:       amdgpu/vega12_sdma.bin
firmware:       amdgpu/vega10_sdma1.bin
firmware:       amdgpu/vega10_sdma.bin
firmware:       amdgpu/vega20_uvd.bin
firmware:       amdgpu/vega12_uvd.bin
firmware:       amdgpu/vega10_uvd.bin
firmware:       amdgpu/vegam_uvd.bin
firmware:       amdgpu/polaris12_uvd.bin
firmware:       amdgpu/polaris11_uvd.bin
firmware:       amdgpu/polaris10_uvd.bin
firmware:       amdgpu/stoney_uvd.bin
firmware:       amdgpu/fiji_uvd.bin
firmware:       amdgpu/carrizo_uvd.bin
firmware:       amdgpu/tonga_uvd.bin
firmware:       amdgpu/mullins_uvd.bin
firmware:       amdgpu/hawaii_uvd.bin
firmware:       amdgpu/kaveri_uvd.bin
firmware:       amdgpu/kabini_uvd.bin
firmware:       amdgpu/bonaire_uvd.bin
firmware:       amdgpu/vega20_vce.bin
firmware:       amdgpu/vega12_vce.bin
firmware:       amdgpu/vega10_vce.bin
firmware:       amdgpu/vegam_vce.bin
firmware:       amdgpu/polaris12_vce.bin
firmware:       amdgpu/polaris11_vce.bin
firmware:       amdgpu/polaris10_vce.bin
firmware:       amdgpu/stoney_vce.bin
firmware:       amdgpu/fiji_vce.bin
firmware:       amdgpu/carrizo_vce.bin
firmware:       amdgpu/tonga_vce.bin
firmware:       amdgpu/mullins_vce.bin
firmware:       amdgpu/hawaii_vce.bin
firmware:       amdgpu/kaveri_vce.bin
firmware:       amdgpu/kabini_vce.bin
firmware:       amdgpu/bonaire_vce.bin
firmware:       amdgpu/raven2_vcn.bin
firmware:       amdgpu/picasso_vcn.bin
firmware:       amdgpu/raven_vcn.bin
firmware:       amdgpu/vega20_smc.bin
firmware:       amdgpu/vega12_smc.bin
firmware:       amdgpu/vega10_acg_smc.bin
firmware:       amdgpu/vega10_smc.bin
firmware:       amdgpu/vegam_smc.bin
firmware:       amdgpu/polaris12_k_smc.bin
firmware:       amdgpu/polaris12_smc.bin
firmware:       amdgpu/polaris11_k2_smc.bin
firmware:       amdgpu/polaris11_k_smc.bin
firmware:       amdgpu/polaris11_smc_sk.bin
firmware:       amdgpu/polaris11_smc.bin
firmware:       amdgpu/polaris10_k2_smc.bin
firmware:       amdgpu/polaris10_k_smc.bin
firmware:       amdgpu/polaris10_smc_sk.bin
firmware:       amdgpu/polaris10_smc.bin
firmware:       amdgpu/fiji_smc.bin
firmware:       amdgpu/tonga_k_smc.bin
firmware:       amdgpu/tonga_smc.bin
firmware:       amdgpu/topaz_k_smc.bin
firmware:       amdgpu/topaz_smc.bin
firmware:       amdgpu/hawaii_k_smc.bin
firmware:       amdgpu/hawaii_smc.bin
firmware:       amdgpu/bonaire_k_smc.bin
firmware:       amdgpu/bonaire_smc.bin
firmware:       amdgpu/vega20_smc.bin
firmware:       amdgpu/raven_dmcu.bin
srcversion:     8E43A899FE10A3C28846198
alias:          pci:v00001002d000015D8sv*sd*bc*sc*i*
alias:          pci:v00001002d000015DDsv*sd*bc*sc*i*
alias:          pci:v00001002d000066AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000066A7sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A4sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A0sv*sd*bc*sc*i*
alias:          pci:v00001002d000069AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000069A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000687Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006869sv*sd*bc*sc*i*
alias:          pci:v00001002d00006868sv*sd*bc*sc*i*
alias:          pci:v00001002d00006867sv*sd*bc*sc*i*
alias:          pci:v00001002d00006864sv*sd*bc*sc*i*
alias:          pci:v00001002d00006863sv*sd*bc*sc*i*
alias:          pci:v00001002d00006862sv*sd*bc*sc*i*
alias:          pci:v00001002d00006861sv*sd*bc*sc*i*
alias:          pci:v00001002d00006860sv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000699Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006997sv*sd*bc*sc*i*
alias:          pci:v00001002d00006995sv*sd*bc*sc*i*
alias:          pci:v00001002d00006987sv*sd*bc*sc*i*
alias:          pci:v00001002d00006986sv*sd*bc*sc*i*
alias:          pci:v00001002d00006985sv*sd*bc*sc*i*
alias:          pci:v00001002d00006981sv*sd*bc*sc*i*
alias:          pci:v00001002d00006980sv*sd*bc*sc*i*
alias:          pci:v00001002d00006FDFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CCsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067C9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067DFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067D0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C7sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C4sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C2sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E7sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067FFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067EFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067EBsv*sd*bc*sc*i*
alias:          pci:v00001002d000067E8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E3sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E0sv*sd*bc*sc*i*
alias:          pci:v00001002d000098E4sv*sd*bc*sc*i*
alias:          pci:v00001002d00009877sv*sd*bc*sc*i*
alias:          pci:v00001002d00009876sv*sd*bc*sc*i*
alias:          pci:v00001002d00009875sv*sd*bc*sc*i*
alias:          pci:v00001002d00009874sv*sd*bc*sc*i*
alias:          pci:v00001002d00009870sv*sd*bc*sc*i*
alias:          pci:v00001002d0000730Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00007300sv*sd*bc*sc*i*
alias:          pci:v00001002d00006939sv*sd*bc*sc*i*
alias:          pci:v00001002d00006938sv*sd*bc*sc*i*
alias:          pci:v00001002d00006930sv*sd*bc*sc*i*
alias:          pci:v00001002d0000692Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000692Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00006929sv*sd*bc*sc*i*
alias:          pci:v00001002d00006928sv*sd*bc*sc*i*
alias:          pci:v00001002d00006921sv*sd*bc*sc*i*
alias:          pci:v00001002d00006920sv*sd*bc*sc*i*
alias:          pci:v00001002d00006907sv*sd*bc*sc*i*
alias:          pci:v00001002d00006903sv*sd*bc*sc*i*
alias:          pci:v00001002d00006902sv*sd*bc*sc*i*
alias:          pci:v00001002d00006901sv*sd*bc*sc*i*
alias:          pci:v00001002d00006900sv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Asv*sd*bc*sc*i*
alias:          pci:v00001002d00009859sv*sd*bc*sc*i*
alias:          pci:v00001002d00009858sv*sd*bc*sc*i*
alias:          pci:v00001002d00009857sv*sd*bc*sc*i*
alias:          pci:v00001002d00009856sv*sd*bc*sc*i*
alias:          pci:v00001002d00009855sv*sd*bc*sc*i*
alias:          pci:v00001002d00009854sv*sd*bc*sc*i*
alias:          pci:v00001002d00009853sv*sd*bc*sc*i*
alias:          pci:v00001002d00009852sv*sd*bc*sc*i*
alias:          pci:v00001002d00009851sv*sd*bc*sc*i*
alias:          pci:v00001002d00009850sv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Asv*sd*bc*sc*i*
alias:          pci:v00001002d00009839sv*sd*bc*sc*i*
alias:          pci:v00001002d00009838sv*sd*bc*sc*i*
alias:          pci:v00001002d00009837sv*sd*bc*sc*i*
alias:          pci:v00001002d00009836sv*sd*bc*sc*i*
alias:          pci:v00001002d00009835sv*sd*bc*sc*i*
alias:          pci:v00001002d00009834sv*sd*bc*sc*i*
alias:          pci:v00001002d00009833sv*sd*bc*sc*i*
alias:          pci:v00001002d00009832sv*sd*bc*sc*i*
alias:          pci:v00001002d00009831sv*sd*bc*sc*i*
alias:          pci:v00001002d00009830sv*sd*bc*sc*i*
alias:          pci:v00001002d000067BEsv*sd*bc*sc*i*
alias:          pci:v00001002d000067BAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067B9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067AAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067A9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Csv*sd*bc*sc*i*
alias:          pci:v00001002d00006658sv*sd*bc*sc*i*
alias:          pci:v00001002d00006651sv*sd*bc*sc*i*
alias:          pci:v00001002d00006650sv*sd*bc*sc*i*
alias:          pci:v00001002d00006649sv*sd*bc*sc*i*
alias:          pci:v00001002d00006647sv*sd*bc*sc*i*
alias:          pci:v00001002d00006646sv*sd*bc*sc*i*
alias:          pci:v00001002d00006641sv*sd*bc*sc*i*
alias:          pci:v00001002d00006640sv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00001318sv*sd*bc*sc*i*
alias:          pci:v00001002d00001317sv*sd*bc*sc*i*
alias:          pci:v00001002d00001316sv*sd*bc*sc*i*
alias:          pci:v00001002d00001315sv*sd*bc*sc*i*
alias:          pci:v00001002d00001313sv*sd*bc*sc*i*
alias:          pci:v00001002d00001312sv*sd*bc*sc*i*
alias:          pci:v00001002d00001311sv*sd*bc*sc*i*
alias:          pci:v00001002d00001310sv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Asv*sd*bc*sc*i*
alias:          pci:v00001002d00001309sv*sd*bc*sc*i*
alias:          pci:v00001002d00001307sv*sd*bc*sc*i*
alias:          pci:v00001002d00001306sv*sd*bc*sc*i*
alias:          pci:v00001002d00001305sv*sd*bc*sc*i*
alias:          pci:v00001002d00001304sv*sd*bc*sc*i*
alias:          pci:v00001002d0000666Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006667sv*sd*bc*sc*i*
alias:          pci:v00001002d00006665sv*sd*bc*sc*i*
alias:          pci:v00001002d00006664sv*sd*bc*sc*i*
alias:          pci:v00001002d00006663sv*sd*bc*sc*i*
alias:          pci:v00001002d00006660sv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00006839sv*sd*bc*sc*i*
alias:          pci:v00001002d00006838sv*sd*bc*sc*i*
alias:          pci:v00001002d00006837sv*sd*bc*sc*i*
alias:          pci:v00001002d00006835sv*sd*bc*sc*i*
alias:          pci:v00001002d00006831sv*sd*bc*sc*i*
alias:          pci:v00001002d00006830sv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006829sv*sd*bc*sc*i*
alias:          pci:v00001002d00006828sv*sd*bc*sc*i*
alias:          pci:v00001002d00006827sv*sd*bc*sc*i*
alias:          pci:v00001002d00006826sv*sd*bc*sc*i*
alias:          pci:v00001002d00006825sv*sd*bc*sc*i*
alias:          pci:v00001002d00006824sv*sd*bc*sc*i*
alias:          pci:v00001002d00006823sv*sd*bc*sc*i*
alias:          pci:v00001002d00006822sv*sd*bc*sc*i*
alias:          pci:v00001002d00006821sv*sd*bc*sc*i*
alias:          pci:v00001002d00006820sv*sd*bc*sc*i*
alias:          pci:v00001002d00006631sv*sd*bc*sc*i*
alias:          pci:v00001002d00006623sv*sd*bc*sc*i*
alias:          pci:v00001002d00006621sv*sd*bc*sc*i*
alias:          pci:v00001002d00006620sv*sd*bc*sc*i*
alias:          pci:v00001002d00006617sv*sd*bc*sc*i*
alias:          pci:v00001002d00006613sv*sd*bc*sc*i*
alias:          pci:v00001002d00006611sv*sd*bc*sc*i*
alias:          pci:v00001002d00006610sv*sd*bc*sc*i*
alias:          pci:v00001002d00006608sv*sd*bc*sc*i*
alias:          pci:v00001002d00006607sv*sd*bc*sc*i*
alias:          pci:v00001002d00006606sv*sd*bc*sc*i*
alias:          pci:v00001002d00006605sv*sd*bc*sc*i*
alias:          pci:v00001002d00006604sv*sd*bc*sc*i*
alias:          pci:v00001002d00006603sv*sd*bc*sc*i*
alias:          pci:v00001002d00006602sv*sd*bc*sc*i*
alias:          pci:v00001002d00006601sv*sd*bc*sc*i*
alias:          pci:v00001002d00006600sv*sd*bc*sc*i*
alias:          pci:v00001002d00006819sv*sd*bc*sc*i*
alias:          pci:v00001002d00006818sv*sd*bc*sc*i*
alias:          pci:v00001002d00006817sv*sd*bc*sc*i*
alias:          pci:v00001002d00006816sv*sd*bc*sc*i*
alias:          pci:v00001002d00006811sv*sd*bc*sc*i*
alias:          pci:v00001002d00006810sv*sd*bc*sc*i*
alias:          pci:v00001002d00006809sv*sd*bc*sc*i*
alias:          pci:v00001002d00006808sv*sd*bc*sc*i*
alias:          pci:v00001002d00006806sv*sd*bc*sc*i*
alias:          pci:v00001002d00006802sv*sd*bc*sc*i*
alias:          pci:v00001002d00006801sv*sd*bc*sc*i*
alias:          pci:v00001002d00006800sv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006799sv*sd*bc*sc*i*
alias:          pci:v00001002d00006798sv*sd*bc*sc*i*
alias:          pci:v00001002d00006792sv*sd*bc*sc*i*
alias:          pci:v00001002d00006791sv*sd*bc*sc*i*
alias:          pci:v00001002d00006790sv*sd*bc*sc*i*
alias:          pci:v00001002d0000678Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006788sv*sd*bc*sc*i*
alias:          pci:v00001002d00006784sv*sd*bc*sc*i*
alias:          pci:v00001002d00006780sv*sd*bc*sc*i*
depends:        drm_kms_helper,drm,ttm,gpu-sched,i2c-algo-bit
retpoline:      Y
intree:         Y
name:           amdgpu
vermagic:       5.2.0-rc1-amd+ SMP mod_unload
signat:         PKCS#7
signer:        
sig_key:        
sig_hashalgo:   md4
parm:           vramlimit:Restrict VRAM for testing, in megabytes (int)
parm:           vis_vramlimit:Restrict visible VRAM for testing, in megabytes (int)
parm:           gartsize:Size of GART to setup in megabytes (32, 64, etc., -1=auto) (uint)
parm:           gttsize:Size of the GTT domain in megabytes (-1 = auto) (int)
parm:           moverate:Maximum buffer migration rate in MB/s. (32, 64, etc., -1=auto, 0=1=disabled) (int)
parm:           benchmark:Run benchmark (int)
parm:           test:Run tests (int)
parm:           audio:Audio enable (-1 = auto, 0 = disable, 1 = enable) (int)
parm:           disp_priority:Display Priority (0 = auto, 1 = normal, 2 = high) (int)
parm:           hw_i2c:hw i2c engine enable (0 = disable) (int)
parm:           pcie_gen2:PCIE Gen2 mode (-1 = auto, 0 = disable, 1 = enable) (int)
parm:           msi:MSI support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           lockup_timeout:GPU lockup timeout in ms (default: 10000 for non-compute jobs and no timeout for compute jobs), format is [Non-Compute] or [GFX,Compute,SDMA,Video] (string)
parm:           dpm:DPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           fw_load_type:firmware loading type (0 = direct, 1 = SMU, 2 = PSP, -1 = auto) (int)
parm:           aspm:ASPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           runpm:PX runtime pm (1 = force enable, 0 = disable, -1 = PX only default) (int)
parm:           ip_block_mask:IP Block Mask (all blocks enabled (default)) (uint)
parm:           bapm:BAPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           deep_color:Deep Color support (1 = enable, 0 = disable (default)) (int)
parm:           vm_size:VM address space size in gigabytes (default 64GB) (int)
parm:           vm_fragment_size:VM fragment size in bits (4, 5, etc. 4 = 64K (default), Max 9 = 2M) (int)
parm:           vm_block_size:VM page table size in bits (default depending on vm_size) (int)
parm:           vm_fault_stop:Stop on VM fault (0 = never (default), 1 = print first, 2 = always) (int)
parm:           vm_debug:Debug VM handling (0 = disabled (default), 1 = enabled) (int)
parm:           vm_update_mode:VM update using CPU (0 = never (default except for large BAR(LB)), 1 = Graphics only, 2 = Compute only (default for LB), 3 = Both (int)
parm:           vram_page_split:Number of pages after we split VRAM allocations (default 512, -1 = disable) (int)
parm:           exp_hw_support:experimental hw support (1 = enable, 0 = disable (default)) (int)
parm:           dc:Display Core driver (1 = enable, 0 = disable, -1 = auto (default)) (int)
parm:           sched_jobs:the max number of jobs supported in the sw queue (default 32) (int)
parm:           sched_hw_submission:the max number of HW submissions (default 2) (int)
parm:           ppfeaturemask:all power features enabled (default)) (uint)
parm:           pcie_gen_cap:PCIE Gen Caps (0: autodetect (default)) (uint)
parm:           pcie_lane_cap:PCIE Lane Caps (0: autodetect (default)) (uint)
parm:           cg_mask:Clockgating flags mask (0 = disable clock gating) (uint)
parm:           pg_mask:Powergating flags mask (0 = disable power gating) (uint)
parm:           sdma_phase_quantum:SDMA context switch phase quantum (x 1K GPU clock cycles, 0 = no change (default 32)) (uint)
parm:           disable_cu:Disable CUs (se.sh.cu,...) (charp)
parm:           virtual_display:Enable virtual display feature (the virtual_display will be set like xxxx:xx:xx.x,x;xxxx:xx:xx.x,x) (charp)
parm:           ngg:Next Generation Graphics (1 = enable, 0 = disable(default depending on gfx)) (int)
parm:           prim_buf_per_se:the size of Primitive Buffer per Shader Engine (default depending on gfx) (int)
parm:           pos_buf_per_se:the size of Position Buffer per Shader Engine (default depending on gfx) (int)
parm:           cntl_sb_buf_per_se:the size of Control Sideband per Shader Engine (default depending on gfx) (int)
parm:           param_buf_per_se:the size of Off-Chip Parameter Cache per Shader Engine (default depending on gfx) (int)
parm:           job_hang_limit:how much time allow a job hang and not drop it (default 0) (int)
parm:           lbpw:Load Balancing Per Watt (LBPW) support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           compute_multipipe:Force compute queues to be spread across pipes (1 = enable, 0 = disable, -1 = auto) (int)
parm:           gpu_recovery:Enable GPU recovery mechanism, (1 = enable, 0 = disable, -1 = auto) (int)
parm:           emu_mode:Emulation mode, (1 = enable, 0 = disable) (int)
parm:           ras_enable:Enable RAS features on the GPU (0 = disable, 1 = enable, -1 = auto (default)) (int)
parm:           ras_mask:Mask of RAS features to enable (default 0xffffffff), only valid when ras_enable == 1 (uint)
parm:           si_support:SI support (1 = enabled (default), 0 = disabled) (int)
parm:           cik_support:CIK support (1 = enabled (default), 0 = disabled) (int)
parm:           smu_memory_pool_size:reserve gtt for smu debug usage, 0 = disable,0x1 = 256Mbyte, 0x2 = 512Mbyte, 0x4 = 1 Gbyte, 0x8 = 2GByte (uint)
parm:           dcfeaturemask:all stable DC features enabled (default)) (uint)

clinfo
Number of platforms                               1
  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 19.0.2
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   Clover
Number of devices                                 1
  Device Name                                     AMD VEGAM (DRM 3.32.0, 5.2.0-rc1-amd+, LLVM 8.0.0)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 19.0.2
  Driver Version                                  19.0.2
  Device OpenCL C Version                         OpenCL C 1.1
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               20
  Max clock frequency                             1011MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Preferred / native vector sizes                
    char                                                16 / 16      
    short                                                8 / 8      
    int                                                  4 / 4      
    long                                                 2 / 2      
    half                                                 8 / 8        (cl_khr_fp16)
    float                                                4 / 4      
    double                                               2 / 2        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              4294967296 (4GiB)
  Error Correction support                        No
  Max memory allocation                           3435973836 (3.2GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       32768 bits (4096 bytes)
  Global Memory cache type                        None
  Image support                                   No
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Max number of constant args                     16
  Max constant buffer size                        2147483647 (2GiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Profiling timer resolution                      0ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_fp16

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [MESA]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD VEGAM (DRM 3.32.0, 5.2.0-rc1-amd+, LLVM 8.0.0)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD VEGAM (DRM 3.32.0, 5.2.0-rc1-amd+, LLVM 8.0.0)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD VEGAM (DRM 3.32.0, 5.2.0-rc1-amd+, LLVM 8.0.0)

dmesg
[    0.000000] Linux version 5.2.0-rc1-amd+ (root@user-NUC8i7HNK) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04)) #1 SMP Tue May 21 11:55:06 CEST 2019
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.2.0-rc1-amd+ root=UUID=a71b4f73-6318-41df-b754-480f21b7ecd8 ro quiet splash vt.handoff=1
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
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000057fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000058000-0x0000000000058fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000059000-0x000000000009dfff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009e000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x0000000077cd6fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000077cd7000-0x0000000077cd7fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x0000000077cd8000-0x0000000077cd8fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000077cd9000-0x000000007e701fff] usable
[    0.000000] BIOS-e820: [mem 0x000000007e702000-0x000000007ebc5fff] reserved
[    0.000000] BIOS-e820: [mem 0x000000007ebc6000-0x000000007ec24fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x000000007ec25000-0x000000007ec84fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x000000007ec85000-0x000000007f72bfff] reserved
[    0.000000] BIOS-e820: [mem 0x000000007f72c000-0x000000007f7fdfff] type 20
[    0.000000] BIOS-e820: [mem 0x000000007f7fe000-0x000000007f7fefff] usable
[    0.000000] BIOS-e820: [mem 0x000000007f7ff000-0x000000007fffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000e0000000-0x00000000efffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fe000000-0x00000000fe010fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000027effffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] efi: EFI v2.70 by American Megatrends
[    0.000000] efi:  ACPI 2.0=0x7ebd9000  ACPI=0x7ebd9000  SMBIOS=0x7f5e3000  SMBIOS 3.0=0x7f5e2000  ESRT=0x7f5ab998  MEMATTR=0x7ccba018
[    0.000000] SMBIOS 3.1.1 present.
[    0.000000] DMI: Intel(R) Client Systems NUC8i7HNK/NUC8i7HNB, BIOS HNKBLi70.86A.0049.2018.0801.1601 08/01/2018
[    0.000000] tsc: Detected 3100.000 MHz processor
[    0.001906] tsc: Detected 3096.000 MHz TSC
[    0.001906] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.001907] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.001912] last_pfn = 0x27f000 max_arch_pfn = 0x400000000
[    0.001924] MTRR default type: write-back
[    0.001924] MTRR fixed ranges enabled:
[    0.001925]   00000-9FFFF write-back
[    0.001926]   A0000-BFFFF uncachable
[    0.001927]   C0000-FFFFF write-protect
[    0.001927] MTRR variable ranges enabled:
[    0.001928]   0 base 0080000000 mask 7F80000000 uncachable
[    0.001929]   1 base 2000000000 mask 7000000000 uncachable
[    0.001929]   2 disabled
[    0.001930]   3 disabled
[    0.001930]   4 disabled
[    0.001930]   5 disabled
[    0.001931]   6 disabled
[    0.001931]   7 disabled
[    0.001931]   8 disabled
[    0.001932]   9 disabled
[    0.003009] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.003169] last_pfn = 0x7f7ff max_arch_pfn = 0x400000000
[    0.010062] esrt: Reserving ESRT space from 0x000000007f5ab998 to 0x000000007f5ab9d0.
[    0.010067] check: Scanning 1 areas for low memory corruption
[    0.010073] Using GB pages for direct mapping
[    0.010074] BRK [0x1d1801000, 0x1d1801fff] PGTABLE
[    0.010076] BRK [0x1d1802000, 0x1d1802fff] PGTABLE
[    0.010076] BRK [0x1d1803000, 0x1d1803fff] PGTABLE
[    0.010113] BRK [0x1d1804000, 0x1d1804fff] PGTABLE
[    0.010114] BRK [0x1d1805000, 0x1d1805fff] PGTABLE
[    0.010235] BRK [0x1d1806000, 0x1d1806fff] PGTABLE
[    0.010265] BRK [0x1d1807000, 0x1d1807fff] PGTABLE
[    0.010340] BRK [0x1d1808000, 0x1d1808fff] PGTABLE
[    0.010379] BRK [0x1d1809000, 0x1d1809fff] PGTABLE
[    0.010424] Secure boot could not be determined
[    0.010425] RAMDISK: [mem 0x370b3000-0x37850fff]
[    0.010429] ACPI: Early table checksum verification disabled
[    0.010431] ACPI: RSDP 0x000000007EBD9000 000024 (v02 INTEL )
[    0.010434] ACPI: XSDT 0x000000007EBD90C0 000104 (v01 INTEL  NUC8i7HN 00000031 AMI  00010013)
[    0.010438] ACPI: FACP 0x000000007EC065F0 000114 (v06 INTEL  NUC8i7HN 00000031 AMI  00010013)
[    0.010442] ACPI: DSDT 0x000000007EBD9258 02D395 (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010444] ACPI: FACS 0x000000007EC54F00 000040
[    0.010446] ACPI: APIC 0x000000007EC06708 0000BC (v03 INTEL  NUC8i7HN 00000031 AMI  00010013)
[    0.010448] ACPI: FPDT 0x000000007EC067C8 000044 (v01 INTEL  NUC8i7HN 00000031 AMI  00010013)
[    0.010450] ACPI: FIDT 0x000000007EC06810 00009C (v01 INTEL  NUC8i7HN 00000031 AMI  00010013)
[    0.010451] ACPI: MCFG 0x000000007EC068B0 00003C (v01 INTEL  NUC8i7HN 00000031 MSFT 00000097)
[    0.010453] ACPI: SSDT 0x000000007EC068F0 000359 (v01 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010455] ACPI: SSDT 0x000000007EC06C50 003165 (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010457] ACPI: SSDT 0x000000007EC09DB8 002892 (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010459] ACPI: HPET 0x000000007EC0C650 000038 (v01 INTEL  NUC8i7HN 00000031 MSFT 0000005F)
[    0.010461] ACPI: SSDT 0x000000007EC0C688 0011AA (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010463] ACPI: SSDT 0x000000007EC0D838 0008FC (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010465] ACPI: UEFI 0x000000007EC0E138 000048 (v01 INTEL  NUC8i7HN 00000031      01000013)
[    0.010466] ACPI: SSDT 0x000000007EC0E180 00071D (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010468] ACPI: SSDT 0x000000007EC0E8A0 0017AE (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010470] ACPI: LPIT 0x000000007EC10050 000094 (v01 INTEL  NUC8i7HN 00000031 MSFT 0000005F)
[    0.010472] ACPI: SSDT 0x000000007EC100E8 000141 (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010474] ACPI: SSDT 0x000000007EC10230 00029F (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010476] ACPI: SSDT 0x000000007EC104D0 003002 (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010478] ACPI: SSDT 0x000000007EC134D8 000303 (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010480] ACPI: SSDT 0x000000007EC137E0 0002E9 (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010482] ACPI: DBGP 0x000000007EC13AD0 000034 (v01 INTEL  NUC8i7HN 00000031 MSFT 0000005F)
[    0.010483] ACPI: DBG2 0x000000007EC13B08 000054 (v00 INTEL  NUC8i7HN 00000031 MSFT 0000005F)
[    0.010485] ACPI: SSDT 0x000000007EC13B60 0004F4 (v02 INTEL  NUC8i7HN 00000031 INTL 20160422)
[    0.010487] ACPI: DMAR 0x000000007EC14058 0000FC (v01 INTEL  NUC8i7HN 00000031 INTL 00000001)
[    0.010489] ACPI: VFCT 0x000000007EC14158 00FE84 (v01 INTEL  NUC8i7HN 00000031 AMD  31504F47)
[    0.010491] ACPI: TPM2 0x000000007EC23FE0 000034 (v04 INTEL  NUC8i7HN 00000031 AMI  00000000)
[    0.010493] ACPI: BGRT 0x000000007EC24018 000038 (v01 INTEL  NUC8i7HN 00000031 AMI  00010013)
[    0.010495] ACPI: WSMT 0x000000007EC24050 000028 (v01 INTEL  NUC8i7HN 00000031 AMI  00010013)
[    0.010501] ACPI: Local APIC address 0xfee00000
[    0.010679] No NUMA configuration found
[    0.010680] Faking a node at [mem 0x0000000000000000-0x000000027effffff]
[    0.010686] NODE_DATA(0) allocated [mem 0x27efd5000-0x27effffff]
[    0.010835] Zone ranges:
[    0.010835]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.010836]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.010837]   Normal   [mem 0x0000000100000000-0x000000027effffff]
[    0.010838]   Device   empty
[    0.010838] Movable zone start for each node
[    0.010841] Early memory node ranges
[    0.010841]   node   0: [mem 0x0000000000001000-0x0000000000057fff]
[    0.010842]   node   0: [mem 0x0000000000059000-0x000000000009dfff]
[    0.010842]   node   0: [mem 0x0000000000100000-0x0000000077cd6fff]
[    0.010843]   node   0: [mem 0x0000000077cd9000-0x000000007e701fff]
[    0.010843]   node   0: [mem 0x000000007f7fe000-0x000000007f7fefff]
[    0.010843]   node   0: [mem 0x0000000100000000-0x000000027effffff]
[    0.010882] Zeroed struct page in unavailable ranges: 6499 pages
[    0.010883] Initmem setup node 0 [mem 0x0000000000001000-0x000000027effffff]
[    0.010884] On node 0 totalpages: 2086557
[    0.010885]   DMA zone: 64 pages used for memmap
[    0.010885]   DMA zone: 22 pages reserved
[    0.010886]   DMA zone: 3996 pages, LIFO batch:0
[    0.010917]   DMA32 zone: 8029 pages used for memmap
[    0.010918]   DMA32 zone: 513793 pages, LIFO batch:63
[    0.016268]   Normal zone: 24512 pages used for memmap
[    0.016269]   Normal zone: 1568768 pages, LIFO batch:63
[    0.028801] ACPI: PM-Timer IO Port: 0x1808
[    0.028803] ACPI: Local APIC address 0xfee00000
[    0.028808] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
[    0.028808] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
[    0.028809] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
[    0.028809] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
[    0.028809] ACPI: LAPIC_NMI (acpi_id[0x05] high edge lint[0x1])
[    0.028810] ACPI: LAPIC_NMI (acpi_id[0x06] high edge lint[0x1])
[    0.028810] ACPI: LAPIC_NMI (acpi_id[0x07] high edge lint[0x1])
[    0.028811] ACPI: LAPIC_NMI (acpi_id[0x08] high edge lint[0x1])
[    0.028837] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-119
[    0.028839] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.028840] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.028840] ACPI: IRQ0 used by override.
[    0.028841] ACPI: IRQ9 used by override.
[    0.028843] Using ACPI (MADT) for SMP configuration information
[    0.028844] ACPI: HPET id: 0x8086a201 base: 0xfed00000
[    0.028848] smpboot: Allowing 8 CPUs, 0 hotplug CPUs
[    0.028862] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.028863] PM: Registered nosave memory: [mem 0x00058000-0x00058fff]
[    0.028865] PM: Registered nosave memory: [mem 0x0009e000-0x000fffff]
[    0.028866] PM: Registered nosave memory: [mem 0x77cd7000-0x77cd7fff]
[    0.028866] PM: Registered nosave memory: [mem 0x77cd8000-0x77cd8fff]
[    0.028867] PM: Registered nosave memory: [mem 0x7e702000-0x7ebc5fff]
[    0.028868] PM: Registered nosave memory: [mem 0x7ebc6000-0x7ec24fff]
[    0.028868] PM: Registered nosave memory: [mem 0x7ec25000-0x7ec84fff]
[    0.028868] PM: Registered nosave memory: [mem 0x7ec85000-0x7f72bfff]
[    0.028869] PM: Registered nosave memory: [mem 0x7f72c000-0x7f7fdfff]
[    0.028870] PM: Registered nosave memory: [mem 0x7f7ff000-0x7fffffff]
[    0.028870] PM: Registered nosave memory: [mem 0x80000000-0xdfffffff]
[    0.028871] PM: Registered nosave memory: [mem 0xe0000000-0xefffffff]
[    0.028871] PM: Registered nosave memory: [mem 0xf0000000-0xfdffffff]
[    0.028871] PM: Registered nosave memory: [mem 0xfe000000-0xfe010fff]
[    0.028872] PM: Registered nosave memory: [mem 0xfe011000-0xfebfffff]
[    0.028872] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.028873] PM: Registered nosave memory: [mem 0xfec01000-0xfecfffff]
[    0.028873] PM: Registered nosave memory: [mem 0xfed00000-0xfed00fff]
[    0.028873] PM: Registered nosave memory: [mem 0xfed01000-0xfedfffff]
[    0.028874] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.028874] PM: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
[    0.028874] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.028876] [mem 0x80000000-0xdfffffff] available for PCI devices
[    0.028877] Booting paravirtualized kernel on bare hardware
[    0.028879] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.028883] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:8 nr_cpu_ids:8 nr_node_ids:1
[    0.029019] percpu: Embedded 54 pages/cpu s184320 r8192 d28672 u262144
[    0.029024] pcpu-alloc: s184320 r8192 d28672 u262144 alloc=1*2097152
[    0.029025] pcpu-alloc: [0] 0 1 2 3 4 5 6 7
[    0.029043] Built 1 zonelists, mobility grouping on.  Total pages: 2053930
[    0.029044] Policy zone: Normal
[    0.029045] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-5.2.0-rc1-amd+ root=UUID=a71b4f73-6318-41df-b754-480f21b7ecd8 ro quiet splash vt.handoff=1
[    0.031689] Calgary: detecting Calgary via BIOS EBDA area
[    0.031690] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.044561] Memory: 8062268K/8346228K available (14339K kernel code, 2222K rwdata, 4168K rodata, 2500K init, 5392K bss, 283960K reserved, 0K cma-reserved)
[    0.044656] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=8, Nodes=1
[    0.044663] Kernel/User page tables isolation: enabled
[    0.044674] ftrace: allocating 40959 entries in 160 pages
[    0.057016] rcu: Hierarchical RCU implementation.
[    0.057017] rcu: RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=8.
[    0.057018] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.057018] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=8
[    0.059305] NR_IRQS: 524544, nr_irqs: 2048, preallocated irqs: 16
[    0.059625] random: get_random_bytes called from start_kernel+0x33c/0x520 with crng_init=0
[    0.059641] Console: colour dummy device 80x25
[    0.059644] printk: console [tty0] enabled
[    0.059654] ACPI: Core revision 20190509
[    0.060047] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635855245 ns
[    0.060077] hpet clockevent registered
[    0.060113] APIC: Switch to symmetric I/O mode setup
[    0.060114] DMAR: Host address width 39
[    0.060115] DMAR: DRHD base: 0x000000fed90000 flags: 0x1
[    0.060119] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap d2008c40660462 ecap f050da
[    0.060120] DMAR: RMRR base: 0x0000007ef03000 end: 0x0000007f14cfff
[    0.060121] DMAR: RMRR base: 0x0000007ef03000 end: 0x0000007f14cfff
[    0.060122] DMAR: ANDD device: 1 name: \_SB.PCI0.I2C0
[    0.060122] DMAR: ANDD device: 2 name: \_SB.PCI0.I2C1
[    0.060123] DMAR: ANDD device: 9 name: \_SB.PCI0.UA00
[    0.060124] DMAR-IR: IOAPIC id 2 under DRHD base  0xfed90000 IOMMU 0
[    0.060124] DMAR-IR: HPET id 0 under DRHD base 0xfed90000
[    0.060125] DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
[    0.061434] DMAR-IR: Enabled IRQ remapping in x2apic mode
[    0.061434] x2apic enabled
[    0.061448] Switched APIC routing to cluster x2apic.
[    0.065440] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.084086] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x2ca08564bf3, max_idle_ns: 440795312460 ns
[    0.084089] Calibrating delay loop (skipped), value calculated using timer frequency.. 6192.00 BogoMIPS (lpj=12384000)
[    0.084091] pid_max: default: 32768 minimum: 301
[    0.085812] LSM: Security Framework initializing
[    0.085820] Yama: becoming mindful.
[    0.085836] AppArmor: AppArmor initialized
[    0.085837] TOMOYO Linux initialized
[    0.086566] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.086926] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes)
[    0.086944] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.086956] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.087125] mce: CPU0: Thermal monitoring enabled (TM1)
[    0.087140] process: using mwait in idle threads
[    0.087142] Last level iTLB entries: 4KB 64, 2MB 8, 4MB 8
[    0.087143] Last level dTLB entries: 4KB 64, 2MB 0, 4MB 0, 1GB 4
[    0.087144] Spectre V2 : Mitigation: Full generic retpoline
[    0.087144] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    0.087145] Spectre V2 : Enabling Restricted Speculation for firmware calls
[    0.087146] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
[    0.087146] Spectre V2 : User space: Mitigation: STIBP via seccomp and prctl
[    0.087147] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.087149] MDS: Vulnerable: Clear CPU buffers attempted, no microcode
[    0.087457] Freeing SMP alternatives memory: 36K
[    0.089097] TSC deadline timer enabled
[    0.089102] smpboot: CPU0: Intel(R) Core(TM) i7-8705G CPU @ 3.10GHz (family: 0x6, model: 0x9e, stepping: 0x9)
[    0.089164] Performance Events: PEBS fmt3+, Skylake events, 32-deep LBR, full-width counters, Intel PMU driver.
[    0.089189] ... version:                4
[    0.089189] ... bit width:              48
[    0.089189] ... generic registers:      4
[    0.089190] ... value mask:             0000ffffffffffff
[    0.089190] ... max period:             00007fffffffffff
[    0.089191] ... fixed-purpose events:   3
[    0.089191] ... event mask:             000000070000000f
[    0.089219] rcu: Hierarchical SRCU implementation.
[    0.090037] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.090084] smp: Bringing up secondary CPUs ...
[    0.090130] x86: Booting SMP configuration:
[    0.090131] .... node  #0, CPUs:      #1 #2 #3 #4
[    0.090531] MDS CPU bug present and SMT on, data leak possible. See https://www.kernel.org/doc/html/latest/admin-guide/hw-vuln/mds.html for more details.
[    0.090531]  #5 #6 #7
[    0.092516] smp: Brought up 1 node, 8 CPUs
[    0.092516] smpboot: Max logical packages: 1
[    0.092516] smpboot: Total of 8 processors activated (49536.00 BogoMIPS)
[    0.096293] devtmpfs: initialized
[    0.096293] x86/mm: Memory block size: 128MB
[    0.096580] PM: Registering ACPI NVS region [mem 0x77cd7000-0x77cd7fff] (4096 bytes)
[    0.096580] PM: Registering ACPI NVS region [mem 0x7ec25000-0x7ec84fff] (393216 bytes)
[    0.096580] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.096580] futex hash table entries: 2048 (order: 5, 131072 bytes)
[    0.096580] pinctrl core: initialized pinctrl subsystem
[    0.096580] PM: RTC time: 07:13:55, date: 2019-05-22
[    0.096580] NET: Registered protocol family 16
[    0.096580] audit: initializing netlink subsys (disabled)
[    0.096580] audit: type=2000 audit(1558509234.040:1): state=initialized audit_enabled=0 res=1
[    0.096580] cpuidle: using governor ladder
[    0.096580] cpuidle: using governor menu
[    0.096580] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.096580] ACPI: bus type PCI registered
[    0.096580] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.096580] PCI: MMCONFIG for domain 0000 [bus 00-ff] at [mem 0xe0000000-0xefffffff] (base 0xe0000000)
[    0.096580] PCI: MMCONFIG at [mem 0xe0000000-0xefffffff] reserved in E820
[    0.096580] PCI: Using configuration type 1 for base access
[    0.096580] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.096801] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.096801] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.100141] ACPI: Added _OSI(Module Device)
[    0.100141] ACPI: Added _OSI(Processor Device)
[    0.100142] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.100142] ACPI: Added _OSI(Processor Aggregator Device)
[    0.100143] ACPI: Added _OSI(Linux-Dell-Video)
[    0.100144] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    0.100145] ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
[    0.144037] ACPI: 14 ACPI AML tables successfully acquired and loaded
[    0.152734] ACPI: Dynamic OEM Table Load:
[    0.152740] ACPI: SSDT 0xFFFF8A1FB480B000 0006B4 (v02 PmRef  Cpu0Ist  00003000 INTL 20160422)
[    0.153296] ACPI: \_PR_.PR00: _OSC native thermal LVT Acked
[    0.154750] ACPI: Dynamic OEM Table Load:
[    0.154755] ACPI: SSDT 0xFFFF8A1FB4D8C400 0003FF (v02 PmRef  Cpu0Cst  00003001 INTL 20160422)
[    0.155230] ACPI: Dynamic OEM Table Load:
[    0.155233] ACPI: SSDT 0xFFFF8A1FB4D85D80 0000BA (v02 PmRef  Cpu0Hwp  00003000 INTL 20160422)
[    0.155630] ACPI: Dynamic OEM Table Load:
[    0.155634] ACPI: SSDT 0xFFFF8A1FB480C800 000628 (v02 PmRef  HwpLvt   00003000 INTL 20160422)
[    0.156402] ACPI: Dynamic OEM Table Load:
[    0.156408] ACPI: SSDT 0xFFFF8A1FB6558000 000D14 (v02 PmRef  ApIst    00003000 INTL 20160422)
[    0.157544] ACPI: Dynamic OEM Table Load:
[    0.157547] ACPI: SSDT 0xFFFF8A1FB4D8D800 000317 (v02 PmRef  ApHwp    00003000 INTL 20160422)
[    0.158043] ACPI: Dynamic OEM Table Load:
[    0.158046] ACPI: SSDT 0xFFFF8A1FB4D8A000 00030A (v02 PmRef  ApCst    00003000 INTL 20160422)
[    0.161629] ACPI: EC: EC started
[    0.161630] ACPI: EC: interrupt blocked
[    0.162531] ACPI: \_SB_.PCI0.LPCB.ECDV: Used as first EC
[    0.162532] ACPI: \_SB_.PCI0.LPCB.ECDV: GPE=0x3, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.162533] ACPI: \_SB_.PCI0.LPCB.ECDV: Boot DSDT EC used to handle transactions
[    0.162534] ACPI: Interpreter enabled
[    0.162572] ACPI: (supports S0 S3 S4 S5)
[    0.162572] ACPI: Using IOAPIC for interrupt routing
[    0.162608] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.163711] ACPI: Enabled 7 GPEs in block 00 to 7F
[    0.166624] ACPI: Power Resource [PG00] (on)
[    0.167023] ACPI: Power Resource [PG01] (on)
[    0.167519] ACPI: Power Resource [PG02] (on)
[    0.172466] ACPI: Power Resource [WRST] (on)
[    0.192133] ACPI: Power Resource [FN00] (off)
[    0.192224] ACPI: Power Resource [FN01] (off)
[    0.192315] ACPI: Power Resource [FN02] (off)
[    0.192403] ACPI: Power Resource [FN03] (off)
[    0.192489] ACPI: Power Resource [FN04] (off)
[    0.193741] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-fe])
[    0.193745] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[    0.193949] acpi PNP0A08:00: _OSC: platform does not support [PCIeHotplug SHPCHotplug PME AER]
[    0.194140] acpi PNP0A08:00: _OSC: OS now controls [PCIeCapability LTR]
[    0.194141] acpi PNP0A08:00: FADT indicates ASPM is unsupported, using BIOS configuration
[    0.194932] PCI host bridge to bus 0000:00
[    0.194934] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.194935] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.194935] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.194936] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000c3fff window]
[    0.194937] pci_bus 0000:00: root bus resource [mem 0x000c4000-0x000c7fff window]
[    0.194937] pci_bus 0000:00: root bus resource [mem 0x000c8000-0x000cbfff window]
[    0.194938] pci_bus 0000:00: root bus resource [mem 0x000cc000-0x000cffff window]
[    0.194939] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000d3fff window]
[    0.194939] pci_bus 0000:00: root bus resource [mem 0x000d4000-0x000d7fff window]
[    0.194940] pci_bus 0000:00: root bus resource [mem 0x000d8000-0x000dbfff window]
[    0.194941] pci_bus 0000:00: root bus resource [mem 0x000dc000-0x000dffff window]
[    0.194941] pci_bus 0000:00: root bus resource [mem 0x000e0000-0x000e3fff window]
[    0.194942] pci_bus 0000:00: root bus resource [mem 0x000e4000-0x000e7fff window]
[    0.194943] pci_bus 0000:00: root bus resource [mem 0x000e8000-0x000ebfff window]
[    0.194943] pci_bus 0000:00: root bus resource [mem 0x000ec000-0x000effff window]
[    0.194944] pci_bus 0000:00: root bus resource [mem 0x80000000-0xdfffffff window]
[    0.194945] pci_bus 0000:00: root bus resource [mem 0x2000000000-0x2fffffffff window]
[    0.194945] pci_bus 0000:00: root bus resource [mem 0xfd000000-0xfe7fffff window]
[    0.194946] pci_bus 0000:00: root bus resource [bus 00-fe]
[    0.194952] pci 0000:00:00.0: [8086:5910] type 00 class 0x060000
[    0.195313] pci 0000:00:01.0: [8086:1901] type 01 class 0x060400
[    0.195352] pci 0000:00:01.0: PME# supported from D0 D3hot D3cold
[    0.195523] pci 0000:00:01.1: [8086:1905] type 01 class 0x060400
[    0.195561] pci 0000:00:01.1: PME# supported from D0 D3hot D3cold
[    0.195728] pci 0000:00:01.2: [8086:1909] type 01 class 0x060400
[    0.195764] pci 0000:00:01.2: PME# supported from D0 D3hot D3cold
[    0.195966] pci 0000:00:08.0: [8086:1911] type 00 class 0x088000
[    0.195975] pci 0000:00:08.0: reg 0x10: [mem 0x2ffff2b000-0x2ffff2bfff 64bit]
[    0.196138] pci 0000:00:14.0: [8086:a12f] type 00 class 0x0c0330
[    0.196170] pci 0000:00:14.0: reg 0x10: [mem 0x2ffff10000-0x2ffff1ffff 64bit]
[    0.196268] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    0.196507] pci 0000:00:14.2: [8086:a131] type 00 class 0x118000
[    0.196539] pci 0000:00:14.2: reg 0x10: [mem 0x2ffff2a000-0x2ffff2afff 64bit]
[    0.196850] pci 0000:00:15.0: [8086:a160] type 00 class 0x118000
[    0.197114] pci 0000:00:15.0: reg 0x10: [mem 0x2ffff29000-0x2ffff29fff 64bit]
[    0.198167] pci 0000:00:15.1: [8086:a161] type 00 class 0x118000
[    0.198431] pci 0000:00:15.1: reg 0x10: [mem 0x2ffff28000-0x2ffff28fff 64bit]
[    0.199497] pci 0000:00:15.2: [8086:a162] type 00 class 0x118000
[    0.199761] pci 0000:00:15.2: reg 0x10: [mem 0x2ffff27000-0x2ffff27fff 64bit]
[    0.200756] pci 0000:00:16.0: [8086:a13a] type 00 class 0x078000
[    0.200785] pci 0000:00:16.0: reg 0x10: [mem 0x2ffff26000-0x2ffff26fff 64bit]
[    0.200868] pci 0000:00:16.0: PME# supported from D3hot
[    0.201105] pci 0000:00:1c.0: [8086:a110] type 01 class 0x060400
[    0.201239] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.201440] pci 0000:00:1c.1: [8086:a111] type 01 class 0x060400
[    0.201584] pci 0000:00:1c.1: PME# supported from D0 D3hot D3cold
[    0.201794] pci 0000:00:1c.2: [8086:a112] type 01 class 0x060400
[    0.201937] pci 0000:00:1c.2: PME# supported from D0 D3hot D3cold
[    0.202152] pci 0000:00:1c.4: [8086:a114] type 01 class 0x060400
[    0.202298] pci 0000:00:1c.4: PME# supported from D0 D3hot D3cold
[    0.202515] pci 0000:00:1d.0: [8086:a118] type 01 class 0x060400
[    0.202656] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
[    0.202968] pci 0000:00:1e.0: [8086:a127] type 00 class 0x118000
[    0.203232] pci 0000:00:1e.0: reg 0x10: [mem 0x2ffff25000-0x2ffff25fff 64bit]
[    0.204239] pci 0000:00:1f.0: [8086:a152] type 00 class 0x060100
[    0.204482] pci 0000:00:1f.2: [8086:a121] type 00 class 0x058000
[    0.204499] pci 0000:00:1f.2: reg 0x10: [mem 0xdc220000-0xdc223fff]
[    0.204700] pci 0000:00:1f.3: [8086:a171] type 00 class 0x040300
[    0.204729] pci 0000:00:1f.3: reg 0x10: [mem 0x2ffff20000-0x2ffff23fff 64bit]
[    0.204758] pci 0000:00:1f.3: reg 0x20: [mem 0x2ffff00000-0x2ffff0ffff 64bit]
[    0.204812] pci 0000:00:1f.3: PME# supported from D3hot D3cold
[    0.205078] pci 0000:00:1f.4: [8086:a123] type 00 class 0x0c0500
[    0.205139] pci 0000:00:1f.4: reg 0x10: [mem 0x2ffff24000-0x2ffff240ff 64bit]
[    0.205209] pci 0000:00:1f.4: reg 0x20: [io  0xf000-0xf01f]
[    0.205431] pci 0000:00:1f.6: [8086:15b7] type 00 class 0x020000
[    0.205457] pci 0000:00:1f.6: reg 0x10: [mem 0xdc200000-0xdc21ffff]
[    0.205554] pci 0000:00:1f.6: PME# supported from D0 D3hot D3cold
[    0.205738] pci 0000:01:00.0: [1002:694e] type 00 class 0x030000
[    0.205755] pci 0000:01:00.0: reg 0x10: [mem 0x2fe0000000-0x2fefffffff 64bit pref]
[    0.205763] pci 0000:01:00.0: reg 0x18: [mem 0x2ff0000000-0x2ff01fffff 64bit pref]
[    0.205767] pci 0000:01:00.0: reg 0x20: [io  0xe000-0xe0ff]
[    0.205772] pci 0000:01:00.0: reg 0x24: [mem 0xdb500000-0xdb53ffff]
[    0.205777] pci 0000:01:00.0: reg 0x30: [mem 0xdb540000-0xdb55ffff pref]
[    0.205790] pci 0000:01:00.0: BAR 0: assigned to efifb
[    0.205828] pci 0000:01:00.0: supports D1 D2
[    0.205828] pci 0000:01:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.205882] pci 0000:01:00.1: [1002:ab08] type 00 class 0x040300
[    0.205895] pci 0000:01:00.1: reg 0x10: [mem 0xdb560000-0xdb563fff 64bit]
[    0.205948] pci 0000:01:00.1: supports D1 D2
[    0.206006] pci 0000:00:01.0: PCI bridge to [bus 01]
[    0.206007] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    0.206009] pci 0000:00:01.0:   bridge window [mem 0xdb500000-0xdbefffff]
[    0.206011] pci 0000:00:01.0:   bridge window [mem 0x2fe0000000-0x2ff01fffff 64bit pref]
[    0.206050] pci 0000:02:00.0: [1b21:2142] type 00 class 0x0c0330
[    0.206068] pci 0000:02:00.0: reg 0x10: [mem 0xdab00000-0xdab07fff 64bit]
[    0.206142] pci 0000:02:00.0: PME# supported from D0 D3hot D3cold
[    0.206205] pci 0000:00:01.1: PCI bridge to [bus 02]
[    0.206207] pci 0000:00:01.1:   bridge window [io  0xd000-0xdfff]
[    0.206208] pci 0000:00:01.1:   bridge window [mem 0xdab00000-0xdb4fffff]
[    0.206317] pci 0000:03:00.0: [1217:8621] type 00 class 0x080501
[    0.206335] pci 0000:03:00.0: reg 0x10: [mem 0xda101000-0xda101fff]
[    0.206343] pci 0000:03:00.0: reg 0x14: [mem 0xda100000-0xda1007ff]
[    0.206431] pci 0000:03:00.0: PME# supported from D3hot D3cold
[    0.216173] pci 0000:00:01.2: PCI bridge to [bus 03]
[    0.216174] pci 0000:00:01.2:   bridge window [io  0xc000-0xcfff]
[    0.216176] pci 0000:00:01.2:   bridge window [mem 0xda100000-0xdaafffff]
[    0.216297] acpiphp: Slot [1] registered
[    0.216302] pci 0000:00:1c.0: PCI bridge to [bus 04]
[    0.216454] pci 0000:05:00.0: [8086:157b] type 00 class 0x020000
[    0.216486] pci 0000:05:00.0: reg 0x10: [mem 0xdc100000-0xdc11ffff]
[    0.216503] pci 0000:05:00.0: reg 0x18: [io  0xb000-0xb01f]
[    0.216512] pci 0000:05:00.0: reg 0x1c: [mem 0xdc120000-0xdc123fff]
[    0.216643] pci 0000:05:00.0: PME# supported from D0 D3hot D3cold
[    0.216796] pci 0000:00:1c.1: PCI bridge to [bus 05]
[    0.216800] pci 0000:00:1c.1:   bridge window [io  0xb000-0xbfff]
[    0.216804] pci 0000:00:1c.1:   bridge window [mem 0xdc100000-0xdc1fffff]
[    0.217302] pci 0000:06:00.0: [8086:24fd] type 00 class 0x028000
[    0.217463] pci 0000:06:00.0: reg 0x10: [mem 0xdc000000-0xdc001fff 64bit]
[    0.217844] pci 0000:06:00.0: PME# supported from D0 D3hot D3cold
[    0.218855] pci 0000:00:1c.2: PCI bridge to [bus 06]
[    0.218862] pci 0000:00:1c.2:   bridge window [mem 0xdc000000-0xdc0fffff]
[    0.218997] pci 0000:00:1c.4: PCI bridge to [bus 07-71]
[    0.219004] pci 0000:00:1c.4:   bridge window [mem 0xac000000-0xda0fffff]
[    0.219010] pci 0000:00:1c.4:   bridge window [mem 0x2f90000000-0x2fd9ffffff 64bit pref]
[    0.219136] pci 0000:72:00.0: [126f:2263] type 00 class 0x010802
[    0.219175] pci 0000:72:00.0: reg 0x10: [mem 0xdbf00000-0xdbf03fff 64bit]
[    0.219434] pci 0000:00:1d.0: PCI bridge to [bus 72]
[    0.219440] pci 0000:00:1d.0:   bridge window [mem 0xdbf00000-0xdbffffff]
[    0.222232] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.222290] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 *10 11 12 14 15)
[    0.222347] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.222403] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.222460] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.222515] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.222571] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.222627] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.223439] ACPI: EC: interrupt unblocked
[    0.223459] ACPI: EC: event unblocked
[    0.223473] ACPI: \_SB_.PCI0.LPCB.ECDV: GPE=0x3, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.223474] ACPI: \_SB_.PCI0.LPCB.ECDV: Boot DSDT EC used to handle transactions and events
[    0.223528] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=mem,locks=none
[    0.223528] pci 0000:01:00.0: vgaarb: bridge control possible
[    0.223528] pci 0000:01:00.0: vgaarb: setting as boot device
[    0.223528] vgaarb: loaded
[    0.223528] SCSI subsystem initialized
[    0.223528] libata version 3.00 loaded.
[    0.223528] ACPI: bus type USB registered
[    0.223528] usbcore: registered new interface driver usbfs
[    0.223528] usbcore: registered new interface driver hub
[    0.223528] usbcore: registered new device driver usb
[    0.223528] pps_core: LinuxPPS API ver. 1 registered
[    0.223528] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.223528] PTP clock support registered
[    0.223528] EDAC MC: Ver: 3.0.0
[    0.224152] Registered efivars operations
[    0.244091] PCI: Using ACPI for IRQ routing
[    0.264779] PCI: pci_cache_line_size set to 64 bytes
[    0.265632] e820: reserve RAM buffer [mem 0x00058000-0x0005ffff]
[    0.265633] e820: reserve RAM buffer [mem 0x0009e000-0x0009ffff]
[    0.265634] e820: reserve RAM buffer [mem 0x77cd7000-0x77ffffff]
[    0.265634] e820: reserve RAM buffer [mem 0x7e702000-0x7fffffff]
[    0.265635] e820: reserve RAM buffer [mem 0x7f7ff000-0x7fffffff]
[    0.265636] e820: reserve RAM buffer [mem 0x27f000000-0x27fffffff]
[    0.265694] NetLabel: Initializing
[    0.265694] NetLabel:  domain hash size = 128
[    0.265695] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.265705] NetLabel:  unlabeled traffic allowed by default
[    0.265713] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    0.265713] hpet0: 8 comparators, 64-bit 24.000000 MHz counter
[    0.265713] clocksource: Switched to clocksource tsc-early
[    0.272199] VFS: Disk quotas dquot_6.6.0
[    0.272210] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.272287] AppArmor: AppArmor Filesystem Enabled
[    0.272302] pnp: PnP ACPI init
[    0.272782] system 00:00: [io  0x0a00-0x0a1f] has been reserved
[    0.272783] system 00:00: [io  0x0a20-0x0a2f] has been reserved
[    0.272784] system 00:00: [io  0x0a30-0x0a3f] has been reserved
[    0.272784] system 00:00: [io  0x0a40-0x0a4f] has been reserved
[    0.272785] system 00:00: [io  0x0a50-0x0a5f] has been reserved
[    0.272786] system 00:00: [io  0x0a60-0x0a6f] has been reserved
[    0.272789] system 00:00: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.273129] system 00:01: [io  0x0680-0x069f] has been reserved
[    0.273131] system 00:01: [io  0xffff] has been reserved
[    0.273131] system 00:01: [io  0xffff] has been reserved
[    0.273132] system 00:01: [io  0xffff] has been reserved
[    0.273133] system 00:01: [io  0x1800-0x18fe] has been reserved
[    0.273134] system 00:01: [io  0x164e-0x164f] has been reserved
[    0.273136] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.273231] system 00:02: [io  0x0800-0x087f] has been reserved
[    0.273233] system 00:02: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.273248] pnp 00:03: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.273283] system 00:04: [io  0x1854-0x1857] has been reserved
[    0.273286] system 00:04: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    0.273539] system 00:05: [mem 0xfed10000-0xfed17fff] has been reserved
[    0.273540] system 00:05: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.273540] system 00:05: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.273541] system 00:05: [mem 0xe0000000-0xefffffff] has been reserved
[    0.273542] system 00:05: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.273543] system 00:05: [mem 0xfed90000-0xfed93fff] could not be reserved
[    0.273544] system 00:05: [mem 0xfed45000-0xfed8ffff] has been reserved
[    0.273545] system 00:05: [mem 0xff000000-0xffffffff] has been reserved
[    0.273546] system 00:05: [mem 0xfee00000-0xfeefffff] could not be reserved
[    0.273547] system 00:05: [mem 0xdffe0000-0xdfffffff] has been reserved
[    0.273549] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.273589] system 00:06: [mem 0xfd000000-0xfdabffff] has been reserved
[    0.273590] system 00:06: [mem 0xfdad0000-0xfdadffff] has been reserved
[    0.273591] system 00:06: [mem 0xfdb00000-0xfdffffff] has been reserved
[    0.273592] system 00:06: [mem 0xfe000000-0xfe01ffff] could not be reserved
[    0.273593] system 00:06: [mem 0xfe036000-0xfe03bfff] has been reserved
[    0.273594] system 00:06: [mem 0xfe03d000-0xfe3fffff] has been reserved
[    0.273595] system 00:06: [mem 0xfe410000-0xfe7fffff] has been reserved
[    0.273597] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.273925] system 00:07: [io  0xff00-0xfffe] has been reserved
[    0.273927] system 00:07: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.275131] system 00:08: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.276215] pnp: PnP ACPI: found 9 devices
[    0.281506] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.281513] pci 0000:00:1c.4: bridge window [io  0x1000-0x0fff] to [bus 07-71] add_size 1000
[    0.281517] pci 0000:00:1c.4: BAR 13: assigned [io  0x2000-0x2fff]
[    0.281518] pci 0000:00:01.0: PCI bridge to [bus 01]
[    0.281520] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    0.281522] pci 0000:00:01.0:   bridge window [mem 0xdb500000-0xdbefffff]
[    0.281524] pci 0000:00:01.0:   bridge window [mem 0x2fe0000000-0x2ff01fffff 64bit pref]
[    0.281526] pci 0000:00:01.1: PCI bridge to [bus 02]
[    0.281527] pci 0000:00:01.1:   bridge window [io  0xd000-0xdfff]
[    0.281529] pci 0000:00:01.1:   bridge window [mem 0xdab00000-0xdb4fffff]
[    0.281532] pci 0000:00:01.2: PCI bridge to [bus 03]
[    0.281533] pci 0000:00:01.2:   bridge window [io  0xc000-0xcfff]
[    0.281534] pci 0000:00:01.2:   bridge window [mem 0xda100000-0xdaafffff]
[    0.281538] pci 0000:00:1c.0: PCI bridge to [bus 04]
[    0.281552] pci 0000:00:1c.1: PCI bridge to [bus 05]
[    0.281554] pci 0000:00:1c.1:   bridge window [io  0xb000-0xbfff]
[    0.281559] pci 0000:00:1c.1:   bridge window [mem 0xdc100000-0xdc1fffff]
[    0.281568] pci 0000:00:1c.2: PCI bridge to [bus 06]
[    0.281573] pci 0000:00:1c.2:   bridge window [mem 0xdc000000-0xdc0fffff]
[    0.281583] pci 0000:00:1c.4: PCI bridge to [bus 07-71]
[    0.281586] pci 0000:00:1c.4:   bridge window [io  0x2000-0x2fff]
[    0.281591] pci 0000:00:1c.4:   bridge window [mem 0xac000000-0xda0fffff]
[    0.281594] pci 0000:00:1c.4:   bridge window [mem 0x2f90000000-0x2fd9ffffff 64bit pref]
[    0.281601] pci 0000:00:1d.0: PCI bridge to [bus 72]
[    0.281606] pci 0000:00:1d.0:   bridge window [mem 0xdbf00000-0xdbffffff]
[    0.281616] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.281617] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.281618] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.281618] pci_bus 0000:00: resource 7 [mem 0x000c0000-0x000c3fff window]
[    0.281619] pci_bus 0000:00: resource 8 [mem 0x000c4000-0x000c7fff window]
[    0.281620] pci_bus 0000:00: resource 9 [mem 0x000c8000-0x000cbfff window]
[    0.281621] pci_bus 0000:00: resource 10 [mem 0x000cc000-0x000cffff window]
[    0.281621] pci_bus 0000:00: resource 11 [mem 0x000d0000-0x000d3fff window]
[    0.281622] pci_bus 0000:00: resource 12 [mem 0x000d4000-0x000d7fff window]
[    0.281623] pci_bus 0000:00: resource 13 [mem 0x000d8000-0x000dbfff window]
[    0.281623] pci_bus 0000:00: resource 14 [mem 0x000dc000-0x000dffff window]
[    0.281624] pci_bus 0000:00: resource 15 [mem 0x000e0000-0x000e3fff window]
[    0.281625] pci_bus 0000:00: resource 16 [mem 0x000e4000-0x000e7fff window]
[    0.281625] pci_bus 0000:00: resource 17 [mem 0x000e8000-0x000ebfff window]
[    0.281626] pci_bus 0000:00: resource 18 [mem 0x000ec000-0x000effff window]
[    0.281627] pci_bus 0000:00: resource 19 [mem 0x80000000-0xdfffffff window]
[    0.281628] pci_bus 0000:00: resource 20 [mem 0x2000000000-0x2fffffffff window]
[    0.281628] pci_bus 0000:00: resource 21 [mem 0xfd000000-0xfe7fffff window]
[    0.281629] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    0.281630] pci_bus 0000:01: resource 1 [mem 0xdb500000-0xdbefffff]
[    0.281630] pci_bus 0000:01: resource 2 [mem 0x2fe0000000-0x2ff01fffff 64bit pref]
[    0.281631] pci_bus 0000:02: resource 0 [io  0xd000-0xdfff]
[    0.281632] pci_bus 0000:02: resource 1 [mem 0xdab00000-0xdb4fffff]
[    0.281633] pci_bus 0000:03: resource 0 [io  0xc000-0xcfff]
[    0.281633] pci_bus 0000:03: resource 1 [mem 0xda100000-0xdaafffff]
[    0.281634] pci_bus 0000:05: resource 0 [io  0xb000-0xbfff]
[    0.281635] pci_bus 0000:05: resource 1 [mem 0xdc100000-0xdc1fffff]
[    0.281635] pci_bus 0000:06: resource 1 [mem 0xdc000000-0xdc0fffff]
[    0.281636] pci_bus 0000:07: resource 0 [io  0x2000-0x2fff]
[    0.281637] pci_bus 0000:07: resource 1 [mem 0xac000000-0xda0fffff]
[    0.281637] pci_bus 0000:07: resource 2 [mem 0x2f90000000-0x2fd9ffffff 64bit pref]
[    0.281638] pci_bus 0000:72: resource 1 [mem 0xdbf00000-0xdbffffff]
[    0.281786] NET: Registered protocol family 2
[    0.281856] tcp_listen_portaddr_hash hash table entries: 4096 (order: 4, 65536 bytes)
[    0.281877] TCP established hash table entries: 65536 (order: 7, 524288 bytes)
[    0.281953] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.282023] TCP: Hash tables configured (established 65536 bind 65536)
[    0.282042] UDP hash table entries: 4096 (order: 5, 131072 bytes)
[    0.282058] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes)
[    0.282094] NET: Registered protocol family 1
[    0.282097] NET: Registered protocol family 44
[    0.282411] pci 0000:01:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.282970] PCI: CLS 64 bytes, default 64
[    0.282994] Unpacking initramfs...
[    0.373839] Freeing initrd memory: 7800K
[    0.373885] DMAR: ACPI device "device:85" under DMAR at fed90000 as 00:15.0
[    0.373887] DMAR: ACPI device "device:86" under DMAR at fed90000 as 00:15.1
[    0.373889] DMAR: ACPI device "device:88" under DMAR at fed90000 as 00:1e.0
[    0.373897] DMAR: [Firmware Bug]: RMRR entry for device 02:00.0 is broken - applying workaround
[    0.392148] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.392149] software IO TLB: mapped [mem 0x71b53000-0x75b53000] (64MB)
[    0.392272] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x2ca08564bf3, max_idle_ns: 440795312460 ns
[    0.392281] clocksource: Switched to clocksource tsc
[    0.392346] check: Scanning for low memory corruption every 60 seconds
[    0.393427] Initialise system trusted keyrings
[    0.393433] Key type blacklist registered
[    0.393455] workingset: timestamp_bits=36 max_order=21 bucket_order=0
[    0.394377] zbud: loaded
[    0.394638] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.394737] fuse: init (API version 7.30)
[    0.394860] Key type asymmetric registered
[    0.394861] Asymmetric key parser 'x509' registered
[    0.394865] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 244)
[    0.396265] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    0.396304] efifb: probing for efifb
[    0.396314] efifb: framebuffer at 0x2fe0000000, using 8128k, total 8128k
[    0.396314] efifb: mode is 1920x1080x32, linelength=7680, pages=1
[    0.396315] efifb: scrolling: redraw
[    0.396315] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    0.396368] Console: switching to colour frame buffer device 240x67
[    0.399254] fb0: EFI VGA frame buffer device
[    0.399259] intel_idle: MWAIT substates: 0x11142120
[    0.399259] intel_idle: v0.4.1 model 0x9E
[    0.399557] intel_idle: lapic_timer_reliable_states 0xffffffff
[    0.399696] input: Sleep Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0E:00/input/input0
[    0.399701] ACPI: Sleep Button [SLPB]
[    0.399721] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input1
[    0.399725] ACPI: Power Button [PWRB]
[    0.399746] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input2
[    0.399752] ACPI: Power Button [PWRF]
[    0.516469] thermal LNXTHERM:00: registered as thermal_zone0
[    0.516470] ACPI: Thermal Zone [TZ00] (28 C)
[    0.516643] thermal LNXTHERM:01: registered as thermal_zone1
[    0.516644] ACPI: Thermal Zone [TZ01] (30 C)
[    0.516869] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.518289] Linux agpgart interface v0.103
[    0.533922] loop: module loaded
[    0.534048] libphy: Fixed MDIO Bus: probed
[    0.534049] tun: Universal TUN/TAP device driver, 1.6
[    0.534066] PPP generic driver version 2.4.2
[    0.534089] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.534091] ehci-pci: EHCI PCI platform driver
[    0.534099] ehci-platform: EHCI generic platform driver
[    0.534107] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.534108] ohci-pci: OHCI PCI platform driver
[    0.534116] ohci-platform: OHCI generic platform driver
[    0.534121] uhci_hcd: USB Universal Host Controller Interface driver
[    0.534278] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.534283] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 1
[    0.535388] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x0000000001109810
[    0.535394] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
[    0.535598] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.02
[    0.535599] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.535599] usb usb1: Product: xHCI Host Controller
[    0.535600] usb usb1: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    0.535601] usb usb1: SerialNumber: 0000:00:14.0
[    0.535692] hub 1-0:1.0: USB hub found
[    0.535724] hub 1-0:1.0: 16 ports detected
[    0.536646] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.536648] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 2
[    0.536650] xhci_hcd 0000:00:14.0: Host supports USB 3.0  SuperSpeed
[    0.536676] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.02
[    0.536677] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.536677] usb usb2: Product: xHCI Host Controller
[    0.536678] usb usb2: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    0.536679] usb usb2: SerialNumber: 0000:00:14.0
[    0.536762] hub 2-0:1.0: USB hub found
[    0.536780] hub 2-0:1.0: 8 ports detected
[    0.537539] xhci_hcd 0000:02:00.0: xHCI Host Controller
[    0.537543] xhci_hcd 0000:02:00.0: new USB bus registered, assigned bus number 3
[    0.592340] xhci_hcd 0000:02:00.0: hcc params 0x0200ef81 hci version 0x110 quirks 0x0000000000000010
[    0.592516] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.02
[    0.592516] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.592517] usb usb3: Product: xHCI Host Controller
[    0.592518] usb usb3: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    0.592519] usb usb3: SerialNumber: 0000:02:00.0
[    0.592643] hub 3-0:1.0: USB hub found
[    0.592648] hub 3-0:1.0: 2 ports detected
[    0.592708] xhci_hcd 0000:02:00.0: xHCI Host Controller
[    0.592711] xhci_hcd 0000:02:00.0: new USB bus registered, assigned bus number 4
[    0.592712] xhci_hcd 0000:02:00.0: Host supports USB 3.1 Enhanced SuperSpeed
[    0.592740] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.592751] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.02
[    0.592752] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.592753] usb usb4: Product: xHCI Host Controller
[    0.592753] usb usb4: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    0.592754] usb usb4: SerialNumber: 0000:02:00.0
[    0.592867] hub 4-0:1.0: USB hub found
[    0.592872] hub 4-0:1.0: 2 ports detected
[    0.592942] i8042: PNP: No PS/2 controller found.
[    0.592943] i8042: Probing ports directly.
[    0.629520] i8042: Detected active multiplexing controller, rev 1.1
[    0.634935] serio: i8042 KBD port at 0x60,0x64 irq 1
[    0.634938] serio: i8042 AUX0 port at 0x60,0x64 irq 12
[    0.634958] serio: i8042 AUX1 port at 0x60,0x64 irq 12
[    0.634971] serio: i8042 AUX2 port at 0x60,0x64 irq 12
[    0.634983] serio: i8042 AUX3 port at 0x60,0x64 irq 12
[    0.635168] mousedev: PS/2 mouse device common for all mice
[    0.635437] rtc_cmos 00:03: RTC can wake from S4
[    0.635895] rtc_cmos 00:03: registered as rtc0
[    0.635904] rtc_cmos 00:03: alarms up to one month, y3k, 242 bytes nvram, hpet irqs
[    0.635908] i2c /dev entries driver
[    0.635952] device-mapper: uevent: version 1.0.3
[    0.636010] device-mapper: ioctl: 4.40.0-ioctl (2019-01-18) initialised: dm-devel@redhat.com
[    0.636012] intel_pstate: Intel P-state driver initializing
[    0.636025] intel_pstate: Disabling energy efficiency optimization
[    0.636415] intel_pstate: HWP enabled
[    0.636623] ledtrig-cpu: registered to indicate activity on CPUs
[    0.636625] EFI Variables Facility v0.08 2004-May-17
[    0.661724] resource sanity check: requesting [mem 0xfdffe800-0xfe0007ff], which spans more than pnp 00:06 [mem 0xfdb00000-0xfdffffff]
[    0.661726] caller pmc_core_probe+0x92/0x310 mapping multiple BARs
[    0.661733] intel_pmc_core intel_pmc_core.0:  initialized
[    0.661901] NET: Registered protocol family 10
[    0.665236] Segment Routing with IPv6
[    0.665246] NET: Registered protocol family 17
[    0.665318] Key type dns_resolver registered
[    0.665716] mce: Using 10 MCE banks
[    0.665723] RAS: Correctable Errors collector initialized.
[    0.665761] microcode: sig=0x906e9, pf=0x8, revision=0x8e
[    0.665946] microcode: Microcode Update Driver: v2.2.
[    0.665950] sched_clock: Marking stable (669441160, -3497129)->(674775330, -8831299)
[    0.666188] registered taskstats version 1
[    0.666194] Loading compiled-in X.509 certificates
[    0.667151] Loaded X.509 cert 'Build time autogenerated kernel key: ac82e0406d85768045f11e3925492d0297ed7b4c'
[    0.667162] zswap: loaded using pool lzo/zbud
[    0.670222] Key type big_key registered
[    0.689435] Key type trusted registered
[    0.691294] Key type encrypted registered
[    0.691310] AppArmor: AppArmor sha1 policy hashing enabled
[    0.691316] ima: Allocated hash algorithm: sha1
[    0.716781] No architecture policies found
[    0.716788] evm: Initialising EVM extended attributes:
[    0.716789] evm: security.selinux
[    0.716789] evm: security.SMACK64
[    0.716789] evm: security.SMACK64EXEC
[    0.716790] evm: security.SMACK64TRANSMUTE
[    0.716790] evm: security.SMACK64MMAP
[    0.716790] evm: security.apparmor
[    0.716790] evm: security.ima
[    0.716791] evm: security.capability
[    0.716791] evm: HMAC attrs: 0x1
[    0.717901] PM:   Magic number: 3:555:218
[    0.717943] acpi device:69: hash matches
[    0.717947] acpi device:3c: hash matches
[    0.718118] rtc_cmos 00:03: setting system clock to 2019-05-22T07:13:55 UTC (1558509235)
[    0.719159] Freeing unused decrypted memory: 2040K
[    0.719499] Freeing unused kernel image memory: 2500K
[    0.744231] Write protecting the kernel read-only data: 22528k
[    0.744759] Freeing unused kernel image memory: 2012K
[    0.745181] Freeing unused kernel image memory: 1976K
[    0.751081] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    0.751082] x86/mm: Checking user space page tables
[    0.756561] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    0.756562] Run /init as init process
[    0.794981] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input3
[    0.806424] sdhci: Secure Digital Host Controller Interface driver
[    0.806425] sdhci: Copyright(c) Pierre Ossman
[    0.806514] dca service started, version 1.12.1
[    0.810088] e1000e: Intel(R) PRO/1000 Network Driver - 3.2.6-k
[    0.810089] e1000e: Copyright(c) 1999 - 2015 Intel Corporation.
[    0.810095] sdhci-pci 0000:03:00.0: SDHCI controller found [1217:8621] (rev 1)
[    0.810175] e1000e 0000:00:1f.6: enabling device (0000 -> 0002)
[    0.810663] e1000e 0000:00:1f.6: Interrupt Throttling Rate (ints/sec) set to dynamic conservative mode
[    0.810818] mmc0: SDHCI controller on PCI [0000:03:00.0] using ADMA
[    0.811275] igb: Intel(R) Gigabit Ethernet Network Driver - version 5.6.0-k
[    0.811275] igb: Copyright (c) 2007-2014 Intel Corporation.
[    0.811301] igb 0000:05:00.0: enabling device (0000 -> 0002)
[    0.813069] nvme nvme0: pci function 0000:72:00.0
[    0.840796] pps pps0: new PPS source ptp0
[    0.840798] igb 0000:05:00.0: added PHC on eth0
[    0.840798] igb 0000:05:00.0: Intel(R) Gigabit Ethernet Network Connection
[    0.840799] igb 0000:05:00.0: eth0: (PCIe:2.5Gb/s:Width x1) 54:b2:03:1b:fb:67
[    0.840800] igb 0000:05:00.0: eth0: PBA No: FFFFFF-0FF
[    0.840800] igb 0000:05:00.0: Using MSI-X interrupts. 4 rx queue(s), 4 tx queue(s)
[    0.841481] igb 0000:05:00.0 enp5s0: renamed from eth0
[    0.845530] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    0.845531] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    0.880137] usb 1-4: new high-speed USB device number 2 using xhci_hcd
[    1.029913] nvme nvme0: missing or invalid SUBNQN field.
[    1.032022] nvme nvme0: allocated 64 MiB host memory buffer.
[    1.047923] nvme nvme0: 8/0/0 default/read/poll queues
[    1.048527] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    1.048528] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    1.053312] nvme nvme0: nvme_report_ns_ids: Identify Descriptors failed
[    1.054980] nvme nvme0: nvme_report_ns_ids: Identify Descriptors failed
[    1.056222]  nvme0n1: p1 p2
[    1.088319] e1000e 0000:00:1f.6 0000:00:1f.6 (uninitialized): registered PHC clock
[    1.176460] e1000e 0000:00:1f.6 eth0: (PCI Express:2.5GT/s:Width x1) 54:b2:03:1b:fb:66
[    1.176461] e1000e 0000:00:1f.6 eth0: Intel(R) PRO/1000 Network Connection
[    1.176534] e1000e 0000:00:1f.6 eth0: MAC: 12, PHY: 12, PBA No: FFFFFF-0FF
[    1.177155] e1000e 0000:00:1f.6 eno1: renamed from eth0
[    1.249651] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    1.249652] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    1.453640] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    1.453641] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    1.657664] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    1.657665] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    1.862497] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    1.862498] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    2.075529] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    2.075530] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    2.277672] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    2.277673] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    2.481680] atkbd serio0: Unknown key released (translated set 2, code 0x7c on isa0060/serio0).
[    2.481681] atkbd serio0: Use 'setkeycodes 7c <keycode>' to make it known.
[    3.275187] usb 1-4: New USB device found, idVendor=046d, idProduct=082d, bcdDevice= 0.11
[    3.275188] usb 1-4: New USB device strings: Mfr=0, Product=2, SerialNumber=1
[    3.275189] usb 1-4: Product: HD Pro Webcam C920
[    3.275190] usb 1-4: SerialNumber: 6B9EB73F
[    3.404253] usb 1-9: new full-speed USB device number 3 using xhci_hcd
[    3.553864] usb 1-9: New USB device found, idVendor=8087, idProduct=0a2b, bcdDevice= 0.10
[    3.553865] usb 1-9: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    3.684250] usb 1-10: new full-speed USB device number 4 using xhci_hcd
[    3.834987] usb 1-10: New USB device found, idVendor=046d, idProduct=c534, bcdDevice=29.01
[    3.834988] usb 1-10: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    3.834989] usb 1-10: Product: USB Receiver
[    3.834990] usb 1-10: Manufacturer: Logitech
[    3.964254] usb 1-11: new low-speed USB device number 5 using xhci_hcd
[    4.118106] usb 1-11: New USB device found, idVendor=046d, idProduct=c31c, bcdDevice=64.00
[    4.118108] usb 1-11: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    4.118108] usb 1-11: Product: USB Keyboard
[    4.118109] usb 1-11: Manufacturer: Logitech
[    4.126486] hidraw: raw HID events driver (C) Jiri Kosina
[    4.129665] input: Logitech USB Receiver as /devices/pci0000:00/0000:00:14.0/usb1/1-10/1-10:1.0/0003:046D:C534.0001/input/input12
[    4.188416] hid-generic 0003:046D:C534.0001: input,hidraw0: USB HID v1.11 Keyboard [Logitech USB Receiver] on usb-0000:00:14.0-10/input0
[    4.191145] input: Logitech USB Receiver Mouse as /devices/pci0000:00/0000:00:14.0/usb1/1-10/1-10:1.1/0003:046D:C534.0002/input/input13
[    4.191310] input: Logitech USB Receiver Consumer Control as /devices/pci0000:00/0000:00:14.0/usb1/1-10/1-10:1.1/0003:046D:C534.0002/input/input14
[    4.248354] input: Logitech USB Receiver System Control as /devices/pci0000:00/0000:00:14.0/usb1/1-10/1-10:1.1/0003:046D:C534.0002/input/input15
[    4.248563] hid-generic 0003:046D:C534.0002: input,hiddev0,hidraw1: USB HID v1.11 Mouse [Logitech USB Receiver] on usb-0000:00:14.0-10/input1
[    4.251455] input: Logitech USB Keyboard as /devices/pci0000:00/0000:00:14.0/usb1/1-11/1-11:1.0/0003:046D:C31C.0003/input/input18
[    4.308415] hid-generic 0003:046D:C31C.0003: input,hidraw2: USB HID v1.10 Keyboard [Logitech USB Keyboard] on usb-0000:00:14.0-11/input0
[    4.313591] input: Logitech USB Keyboard Consumer Control as /devices/pci0000:00/0000:00:14.0/usb1/1-11/1-11:1.1/0003:046D:C31C.0004/input/input19
[    4.372378] input: Logitech USB Keyboard System Control as /devices/pci0000:00/0000:00:14.0/usb1/1-11/1-11:1.1/0003:046D:C31C.0004/input/input20
[    4.372498] hid-generic 0003:046D:C31C.0004: input,hidraw3: USB HID v1.10 Device [Logitech USB Keyboard] on usb-0000:00:14.0-11/input1
[    4.372532] usbcore: registered new interface driver usbhid
[    4.372533] usbhid: USB HID core driver
[    4.399853] EXT4-fs (nvme0n1p2): mounted filesystem with ordered data mode. Opts: (null)
[    4.407515] random: fast init done
[    4.410091] Not activating Mandatory Access Control as /sbin/tomoyo-init does not exist.
[    4.497027] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    4.516646] systemd[1]: Detected architecture x86-64.
[    4.519585] systemd[1]: Set hostname to <user-NUC8i7HNK>.
[    4.571253] random: systemd: uninitialized urandom read (16 bytes read)
[    4.571260] systemd[1]: Reached target Remote File Systems.
[    4.571301] random: systemd: uninitialized urandom read (16 bytes read)
[    4.571305] systemd[1]: Reached target User and Group Name Lookups.
[    4.571311] random: systemd: uninitialized urandom read (16 bytes read)
[    4.571397] systemd[1]: Created slice User and Session Slice.
[    4.571460] systemd[1]: Created slice System Slice.
[    4.571500] systemd[1]: Listening on udev Control Socket.
[    4.571526] systemd[1]: Listening on fsck to fsckd communication Socket.
[    4.571558] systemd[1]: Listening on Journal Socket (/dev/log).
[    4.581718] EXT4-fs (nvme0n1p2): re-mounted. Opts: errors=remount-ro
[    4.588065] lp: driver loaded but no devices found
[    4.591354] ppdev: user-space parallel port driver
[    4.631632] systemd-journald[335]: Received request to flush runtime journal from PID 1
[    4.649349] Adding 2097148k swap on /swapfile.  Priority:-2 extents:6 across:2260988k SSFS
[    4.710259] intel-lpss 0000:00:15.0: enabling device (0000 -> 0002)
[    4.713141] mei_me 0000:00:16.0: enabling device (0004 -> 0006)
[    4.717342] idma64 idma64.0: Found Intel integrated DMA 64-bit
[    4.725831] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    4.726496] intel-lpss 0000:00:15.1: enabling device (0000 -> 0002)
[    4.726749] idma64 idma64.1: Found Intel integrated DMA 64-bit
[    4.726873] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    4.728913] media: Linux media interface: v0.10
[    4.738656] Bluetooth: Core ver 2.22
[    4.738667] NET: Registered protocol family 31
[    4.738668] Bluetooth: HCI device and connection manager initialized
[    4.738670] Bluetooth: HCI socket layer initialized
[    4.738671] Bluetooth: L2CAP socket layer initialized
[    4.738674] Bluetooth: SCO socket layer initialized
[    4.741127] intel-lpss 0000:00:15.2: enabling device (0000 -> 0002)
[    4.741328] idma64 idma64.2: Found Intel integrated DMA 64-bit
[    4.742118] videodev: Linux video capture interface: v2.00
[    4.742746] Intel(R) Wireless WiFi driver for Linux
[    4.742746] Copyright(c) 2003- 2015 Intel Corporation
[    4.743104] iwlwifi 0000:06:00.0: enabling device (0000 -> 0002)
[    4.751297] intel-lpss 0000:00:1e.0: enabling device (0000 -> 0002)
[    4.751575] idma64 idma64.3: Found Intel integrated DMA 64-bit
[    4.757974] usbcore: registered new interface driver btusb
[    4.759598] Bluetooth: hci0: Firmware revision 0.1 build 185 week 49 2017
[    4.765107] iwlwifi 0000:06:00.0: loaded firmware version 36.9f0a2d68.0 op_mode iwlmvm
[    4.771471] uvcvideo: Found UVC 1.00 device HD Pro Webcam C920 (046d:082d)
[    4.772399] uvcvideo 1-4:1.0: Entity type for entity Processing 3 was not initialized!
[    4.772400] uvcvideo 1-4:1.0: Entity type for entity Extension 6 was not initialized!
[    4.772400] uvcvideo 1-4:1.0: Entity type for entity Extension 12 was not initialized!
[    4.772401] uvcvideo 1-4:1.0: Entity type for entity Camera 1 was not initialized!
[    4.772402] uvcvideo 1-4:1.0: Entity type for entity Extension 8 was not initialized!
[    4.772402] uvcvideo 1-4:1.0: Entity type for entity Extension 9 was not initialized!
[    4.772403] uvcvideo 1-4:1.0: Entity type for entity Extension 10 was not initialized!
[    4.772403] uvcvideo 1-4:1.0: Entity type for entity Extension 11 was not initialized!
[    4.772461] input: HD Pro Webcam C920 as /devices/pci0000:00/0000:00:14.0/usb1/1-4/1-4:1.0/input/input21
[    4.772498] usbcore: registered new interface driver uvcvideo
[    4.772498] USB Video Class driver (1.1.1)
[    4.779294] RAPL PMU: API unit is 2^-32 Joules, 5 fixed counters, 655360 ms ovfl timer
[    4.779295] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
[    4.779296] RAPL PMU: hw unit of domain package 2^-14 Joules
[    4.779296] RAPL PMU: hw unit of domain dram 2^-14 Joules
[    4.779297] RAPL PMU: hw unit of domain pp1-gpu 2^-14 Joules
[    4.779297] RAPL PMU: hw unit of domain psys 2^-14 Joules
[    4.785102] snd_hda_intel 0000:00:1f.3: enabling device (0000 -> 0002)
[    4.785379] snd_hda_intel 0000:01:00.1: enabling device (0000 -> 0002)
[    4.785441] snd_hda_intel 0000:01:00.1: Handle vga_switcheroo audio client
[    4.800167] iwlwifi 0000:06:00.0: Detected Intel(R) Dual Band Wireless AC 8265, REV=0x230
[    4.800988] snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALC700: line_outs=1 (0x1b/0x0/0x0/0x0/0x0) type:line
[    4.800990] snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[    4.800991] snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x21/0x0/0x0/0x0/0x0)
[    4.800992] snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
[    4.800993] snd_hda_codec_realtek hdaudioC0D0:    dig-out=0x1e/0x0
[    4.800993] snd_hda_codec_realtek hdaudioC0D0:    inputs:
[    4.800995] snd_hda_codec_realtek hdaudioC0D0:      Internal Mic=0x13
[    4.800995] snd_hda_codec_realtek hdaudioC0D0:      Internal Mic=0x12
[    4.801737] input: HD-Audio Generic HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input22
[    4.801765] input: HD-Audio Generic HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input23
[    4.801795] input: HD-Audio Generic HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input24
[    4.801828] input: HD-Audio Generic HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input25
[    4.801861] input: HD-Audio Generic HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input26
[    4.801884] input: HD-Audio Generic HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input27
[    4.807404] cryptd: max_cpu_qlen set to 1000
[    4.818317] [drm] amdgpu kernel modesetting enabled.
[    4.818353] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 0: 0x2fe0000000 -> 0x2fefffffff
[    4.818355] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 2: 0x2ff0000000 -> 0x2ff01fffff
[    4.818356] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xdb500000 -> 0xdb53ffff
[    4.818357] checking generic (2fe0000000 7f0000) vs hw (2fe0000000 10000000)
[    4.818358] fb0: switching to amdgpudrmfb from EFI VGA
[    4.818385] Console: switching to colour dummy device 80x25
[    4.819039] amdgpu 0000:01:00.0: vgaarb: deactivate vga console
[    4.819085] amdgpu 0000:01:00.0: enabling device (0006 -> 0007)
[    4.819310] [drm] initializing kernel modesetting (VEGAM 0x1002:0x694E 0x8086:0x2073 0xC0).
[    4.819321] [drm] register mmio base: 0xDB500000
[    4.819321] [drm] register mmio size: 262144
[    4.819325] [drm] add ip block number 0 <vi_common>
[    4.819326] [drm] add ip block number 1 <gmc_v8_0>
[    4.819327] [drm] add ip block number 2 <tonga_ih>
[    4.819327] [drm] add ip block number 3 <gfx_v8_0>
[    4.819328] [drm] add ip block number 4 <sdma_v3_0>
[    4.819328] [drm] add ip block number 5 <powerplay>
[    4.819329] [drm] add ip block number 6 <dm>
[    4.819330] [drm] add ip block number 7 <uvd_v6_0>
[    4.819330] [drm] add ip block number 8 <vce_v3_0>
[    4.819331] amdgpu 0000:01:00.0: kfd not supported on this ASIC
[    4.819332] AVX2 version of gcm_enc/dec engaged.
[    4.819332] AES CTR mode by8 optimization enabled
[    4.819338] [drm] UVD is enabled in VM mode
[    4.819339] [drm] UVD ENC is enabled in VM mode
[    4.819340] [drm] VCE enabled in VM mode
[    4.819368] ATOM BIOS: 408436.180301.04s
[    4.819404] [drm] RAS INFO: ras initialized successfully, hardware ability[0] ras_mask[0]
[    4.819407] [drm] vm size is 64 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[    4.819419] amdgpu 0000:01:00.0: BAR 2: releasing [mem 0x2ff0000000-0x2ff01fffff 64bit pref]
[    4.819421] amdgpu 0000:01:00.0: BAR 0: releasing [mem 0x2fe0000000-0x2fefffffff 64bit pref]
[    4.819433] pcieport 0000:00:01.0: BAR 15: releasing [mem 0x2fe0000000-0x2ff01fffff 64bit pref]
[    4.819442] pcieport 0000:00:01.0: BAR 15: assigned [mem 0x2000000000-0x217fffffff 64bit pref]
[    4.819445] amdgpu 0000:01:00.0: BAR 0: assigned [mem 0x2000000000-0x20ffffffff 64bit pref]
[    4.819450] amdgpu 0000:01:00.0: BAR 2: assigned [mem 0x2100000000-0x21001fffff 64bit pref]
[    4.819457] pcieport 0000:00:01.0: PCI bridge to [bus 01]
[    4.819458] pcieport 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    4.819460] pcieport 0000:00:01.0:   bridge window [mem 0xdb500000-0xdbefffff]
[    4.819462] pcieport 0000:00:01.0:   bridge window [mem 0x2000000000-0x217fffffff 64bit pref]
[    4.819474] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    4.819475] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    4.819480] [drm] Detected VRAM RAM=4096M, BAR=4096M
[    4.819481] [drm] RAM width 256bits HBM
[    4.819511] [TTM] Zone  kernel: Available graphics memory: 4061172 KiB
[    4.819512] [TTM] Zone   dma32: Available graphics memory: 2097152 KiB
[    4.819513] [TTM] Initializing pool allocator
[    4.819515] [TTM] Initializing DMA pool allocator
[    4.819534] [drm] amdgpu: 4096M of VRAM memory ready
[    4.819536] [drm] amdgpu: 4096M of GTT memory ready.
[    4.819548] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    4.819580] [drm] PCIE GART of 256M enabled (table at 0x000000F4007E9000).
[    4.825499] [drm] Chained IB support enabled!
[    4.832986] [drm] Found UVD firmware Version: 1.130 Family ID: 16
[    4.835752] [drm] Found VCE firmware Version: 53.21 Binary ID: 3
[    4.844612] random: crng init done
[    4.844613] random: 7 urandom warning(s) missed due to ratelimiting
[    4.865936] iwlwifi 0000:06:00.0: base HW address: a0:a4:c5:6a:5a:86
[    4.907774] [drm] DM_PPLIB: values for Engine clock
[    4.907776] [drm] DM_PPLIB: 225000
[    4.907776] [drm] DM_PPLIB: 400000
[    4.907777] [drm] DM_PPLIB: 535000
[    4.907777] [drm] DM_PPLIB: 715000
[    4.907777] [drm] DM_PPLIB: 850000
[    4.907778] [drm] DM_PPLIB: 960000
[    4.907778] [drm] DM_PPLIB: 985000
[    4.907779] [drm] DM_PPLIB: 1011000
[    4.907779] [drm] DM_PPLIB: Validation clocks:
[    4.907780] [drm] DM_PPLIB:    engine_max_clock: 101100
[    4.907780] [drm] DM_PPLIB:    memory_max_clock: 70000
[    4.907781] [drm] DM_PPLIB:    level           : 8
[    4.907782] [drm] DM_PPLIB: values for Memory clock
[    4.907782] [drm] DM_PPLIB: 300000
[    4.907783] [drm] DM_PPLIB: 500000
[    4.907783] [drm] DM_PPLIB: 700000
[    4.907783] [drm] DM_PPLIB: Validation clocks:
[    4.907784] [drm] DM_PPLIB:    engine_max_clock: 101100
[    4.907784] [drm] DM_PPLIB:    memory_max_clock: 70000
[    4.907785] [drm] DM_PPLIB:    level           : 8
[    4.907881] [drm] dce110_link_encoder_construct: Failed to get encoder_cap_info from VBIOS with error code 4!
[    4.907900] [drm] dce110_link_encoder_construct: Failed to get encoder_cap_info from VBIOS with error code 4!
[    4.920153] [drm] Display Core initialized with v3.2.31!
[    4.945919] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    4.945920] [drm] Driver supports precise vblank timestamp query.
[    4.956689] ieee80211 phy0: Selected rate control algorithm 'iwl-mvm-rs'
[    4.956849] thermal thermal_zone3: failed to read out thermal zone (-61)
[    4.969217] usbcore: registered new interface driver snd-usb-audio
[    4.983038] iwlwifi 0000:06:00.0 wlp6s0: renamed from wlan0
[    4.992929] [drm] UVD and UVD ENC initialized successfully.
[    4.994600] intel_rapl: Found RAPL domain package
[    4.994601] intel_rapl: Found RAPL domain core
[    4.994603] intel_rapl: Found RAPL domain dram
[    4.999888] audit: type=1400 audit(1558509239.776:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/ippusbxd" pid=678 comm="apparmor_parser"
[    5.000251] audit: type=1400 audit(1558509239.780:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=676 comm="apparmor_parser"
[    5.000935] audit: type=1400 audit(1558509239.780:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=675 comm="apparmor_parser"
[    5.000937] audit: type=1400 audit(1558509239.780:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=675 comm="apparmor_parser"
[    5.001314] audit: type=1400 audit(1558509239.780:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=671 comm="apparmor_parser"
[    5.001316] audit: type=1400 audit(1558509239.780:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=671 comm="apparmor_parser"
[    5.001318] audit: type=1400 audit(1558509239.780:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=671 comm="apparmor_parser"
[    5.001319] audit: type=1400 audit(1558509239.780:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=671 comm="apparmor_parser"
[    5.001513] audit: type=1400 audit(1558509239.780:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=674 comm="apparmor_parser"
[    5.004380] dw-apb-uart.3: ttyS4 at MMIO 0x2ffff25000 (irq = 20, base_baud = 115200) is a 16550A
[    5.102929] [drm] VCE initialized successfully.
[    5.104941] [drm] fb mappable at 0x2000D19000
[    5.104942] [drm] vram apper at 0x2000000000
[    5.104942] [drm] size 8294400
[    5.104942] [drm] fb depth is 24
[    5.104943] [drm]    pitch is 7680
[    5.104982] fbcon: amdgpudrmfb (fb0) is primary device
[    5.123049] Console: switching to colour frame buffer device 240x67
[    5.143751] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    5.171670] [drm] Initialized amdgpu 3.32.0 20150101 for 0000:01:00.0 on minor 0
[    5.181072] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[    5.181073] Bluetooth: BNEP filters: protocol multicast
[    5.181076] Bluetooth: BNEP socket layer initialized
[    6.273185] input: HDA Intel PCH Line Out as /devices/pci0000:00/0000:00:1f.3/sound/card0/input28
[    6.273253] input: HDA Intel PCH Front Headphone as /devices/pci0000:00/0000:00:1f.3/sound/card0/input29
[    7.664353] pci 0000:07:00.0: [8086:15d3] type 01 class 0x060400
[    7.664436] pci 0000:07:00.0: enabling Extended Tags
[    7.664565] pci 0000:07:00.0: supports D1 D2
[    7.664566] pci 0000:07:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    7.676240] pci 0000:08:00.0: [8086:15d3] type 01 class 0x060400
[    7.676325] pci 0000:08:00.0: enabling Extended Tags
[    7.676450] pci 0000:08:00.0: supports D1 D2
[    7.676451] pci 0000:08:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    7.676579] pci 0000:08:01.0: [8086:15d3] type 01 class 0x060400
[    7.676662] pci 0000:08:01.0: enabling Extended Tags
[    7.676781] pci 0000:08:01.0: supports D1 D2
[    7.676782] pci 0000:08:01.0: PME# supported from D0 D1 D2 D3hot D3cold
[    7.676897] pci 0000:08:02.0: [8086:15d3] type 01 class 0x060400
[    7.676981] pci 0000:08:02.0: enabling Extended Tags
[    7.677097] pci 0000:08:02.0: supports D1 D2
[    7.677098] pci 0000:08:02.0: PME# supported from D0 D1 D2 D3hot D3cold
[    7.677226] pci 0000:08:04.0: [8086:15d3] type 01 class 0x060400
[    7.677309] pci 0000:08:04.0: enabling Extended Tags
[    7.677429] pci 0000:08:04.0: supports D1 D2
[    7.677430] pci 0000:08:04.0: PME# supported from D0 D1 D2 D3hot D3cold
[    7.677574] pci 0000:07:00.0: PCI bridge to [bus 08-71]
[    7.677585] pci 0000:07:00.0:   bridge window [mem 0xac000000-0xda0fffff]
[    7.677593] pci 0000:07:00.0:   bridge window [mem 0x2f90000000-0x2fd9ffffff 64bit pref]
[    7.677663] pci 0000:09:00.0: [8086:15d2] type 00 class 0x088000
[    7.677704] pci 0000:09:00.0: reg 0x10: [mem 0xda000000-0xda03ffff]
[    7.677716] pci 0000:09:00.0: reg 0x14: [mem 0xda040000-0xda040fff]
[    7.677777] pci 0000:09:00.0: enabling Extended Tags
[    7.677890] pci 0000:09:00.0: supports D1 D2
[    7.677891] pci 0000:09:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    7.678068] pci 0000:08:00.0: PCI bridge to [bus 09]
[    7.678078] pci 0000:08:00.0:   bridge window [mem 0xda000000-0xda0fffff]
[    7.678137] pci 0000:08:01.0: PCI bridge to [bus 0a-3c]
[    7.678147] pci 0000:08:01.0:   bridge window [mem 0xac000000-0xc3efffff]
[    7.678154] pci 0000:08:01.0:   bridge window [mem 0x2f90000000-0x2fafffffff 64bit pref]
[    7.678233] pci 0000:3d:00.0: [8086:15d4] type 00 class 0x0c0330
[    7.678270] pci 0000:3d:00.0: reg 0x10: [mem 0xc3f00000-0xc3f0ffff]
[    7.678452] pci 0000:3d:00.0: supports D1 D2
[    7.678453] pci 0000:3d:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    7.678523] pci 0000:3d:00.0: 8.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s x4 link at 0000:08:02.0 (capable of 31.504 Gb/s with 8 GT/s x4 link)
[    7.678649] pci 0000:08:02.0: PCI bridge to [bus 3d]
[    7.678659] pci 0000:08:02.0:   bridge window [mem 0xc3f00000-0xc3ffffff]
[    7.678717] pci 0000:08:04.0: PCI bridge to [bus 3e-71]
[    7.678727] pci 0000:08:04.0:   bridge window [mem 0xc4000000-0xd9ffffff]
[    7.678734] pci 0000:08:04.0:   bridge window [mem 0x2fb0000000-0x2fd9ffffff 64bit pref]
[    7.678768] pci_bus 0000:08: Allocating resources
[    7.678791] pci 0000:08:01.0: bridge window [io  0x1000-0x0fff] to [bus 0a-3c] add_size 1000
[    7.678792] pci 0000:08:02.0: bridge window [io  0x1000-0x0fff] to [bus 3d] add_size 1000
[    7.678794] pci 0000:08:02.0: bridge window [mem 0x00100000-0x000fffff 64bit pref] to [bus 3d] add_size 200000 add_align 100000
[    7.678795] pci 0000:08:04.0: bridge window [io  0x1000-0x0fff] to [bus 3e-71] add_size 1000
[    7.678797] pci 0000:07:00.0: bridge window [io  0x1000-0x0fff] to [bus 08-71] add_size 4000
[    7.678800] pci 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[    7.678801] pci 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[    7.678802] pci 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[    7.678803] pci 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[    7.678807] pci 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[    7.678808] pci 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[    7.678809] pci 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[    7.678810] pci 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678811] pci 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[    7.678812] pci 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678813] pci 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[    7.678814] pci 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678815] pci 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[    7.678816] pci 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678818] pci 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[    7.678819] pci 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[    7.678820] pci 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[    7.678821] pci 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678822] pci 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[    7.678823] pci 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678825] pci 0000:08:00.0: PCI bridge to [bus 09]
[    7.678831] pci 0000:08:00.0:   bridge window [mem 0xda000000-0xda0fffff]
[    7.678841] pci 0000:08:01.0: PCI bridge to [bus 0a-3c]
[    7.678846] pci 0000:08:01.0:   bridge window [mem 0xac000000-0xc3efffff]
[    7.678850] pci 0000:08:01.0:   bridge window [mem 0x2f90000000-0x2fafffffff 64bit pref]
[    7.678857] pci 0000:08:02.0: PCI bridge to [bus 3d]
[    7.678863] pci 0000:08:02.0:   bridge window [mem 0xc3f00000-0xc3ffffff]
[    7.678873] pci 0000:08:04.0: PCI bridge to [bus 3e-71]
[    7.678879] pci 0000:08:04.0:   bridge window [mem 0xc4000000-0xd9ffffff]
[    7.678883] pci 0000:08:04.0:   bridge window [mem 0x2fb0000000-0x2fd9ffffff 64bit pref]
[    7.678889] pci 0000:07:00.0: PCI bridge to [bus 08-71]
[    7.678895] pci 0000:07:00.0:   bridge window [mem 0xac000000-0xda0fffff]
[    7.678899] pci 0000:07:00.0:   bridge window [mem 0x2f90000000-0x2fd9ffffff 64bit pref]
[    7.680235] xhci_hcd 0000:3d:00.0: xHCI Host Controller
[    7.680239] xhci_hcd 0000:3d:00.0: new USB bus registered, assigned bus number 5
[    7.681388] xhci_hcd 0000:3d:00.0: hcc params 0x200077c1 hci version 0x110 quirks 0x0000000200009810
[    7.684190] usb usb5: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.02
[    7.684192] usb usb5: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    7.684193] usb usb5: Product: xHCI Host Controller
[    7.684194] usb usb5: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    7.684195] usb usb5: SerialNumber: 0000:3d:00.0
[    7.684408] hub 5-0:1.0: USB hub found
[    7.684487] hub 5-0:1.0: 2 ports detected
[    7.685458] xhci_hcd 0000:3d:00.0: xHCI Host Controller
[    7.685461] xhci_hcd 0000:3d:00.0: new USB bus registered, assigned bus number 6
[    7.685464] xhci_hcd 0000:3d:00.0: Host supports USB 3.1 Enhanced SuperSpeed
[    7.685495] usb usb6: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.02
[    7.685497] usb usb6: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    7.685498] usb usb6: Product: xHCI Host Controller
[    7.685499] usb usb6: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[    7.685500] usb usb6: SerialNumber: 0000:3d:00.0
[    7.685588] hub 6-0:1.0: USB hub found
[    7.685598] hub 6-0:1.0: 2 ports detected
[    9.230476] wlp6s0: authenticate with fe:ec:da:82:6c:a6
[    9.241160] wlp6s0: send auth to fe:ec:da:82:6c:a6 (try 1/3)
[    9.247689] wlp6s0: authenticated
[    9.248117] wlp6s0: associate with fe:ec:da:82:6c:a6 (try 1/3)
[    9.252499] wlp6s0: RX AssocResp from fe:ec:da:82:6c:a6 (capab=0x411 status=0 aid=8)
[    9.255376] wlp6s0: associated
[    9.280339] IPv6: ADDRCONF(NETDEV_CHANGE): wlp6s0: link becomes ready
[   32.333033] pci_raw_set_power_state: 24 callbacks suppressed
[   32.333047] xhci_hcd 0000:3d:00.0: Refused to change power state, currently in D3
[   32.416236] xhci_hcd 0000:3d:00.0: Refused to change power state, currently in D3
[   32.416266] xhci_hcd 0000:3d:00.0: WARN: xHC restore state timeout
[   32.416267] xhci_hcd 0000:3d:00.0: PCI post-resume error -110!
[   32.416268] xhci_hcd 0000:3d:00.0: HC died; cleaning up
[   32.416311] xhci_hcd 0000:3d:00.0: remove, state 4
[   32.416314] usb usb6: USB disconnect, device number 1
[   32.416540] xhci_hcd 0000:3d:00.0: USB bus 6 deregistered
[   32.416543] xhci_hcd 0000:3d:00.0: remove, state 4
[   32.416545] usb usb5: USB disconnect, device number 1
[   32.416720] xhci_hcd 0000:3d:00.0: Host halt failed, -19
[   32.416722] xhci_hcd 0000:3d:00.0: Host not accessible, reset failed.
[   32.416770] xhci_hcd 0000:3d:00.0: USB bus 5 deregistered
[   32.476468] pci_bus 0000:08: Allocating resources
[   32.476485] pcieport 0000:08:01.0: bridge window [io  0x1000-0x0fff] to [bus 0a-3c] add_size 1000
[   32.476487] pcieport 0000:08:02.0: bridge window [io  0x1000-0x0fff] to [bus 3d] add_size 1000
[   32.476488] pcieport 0000:08:02.0: bridge window [mem 0x00100000-0x000fffff 64bit pref] to [bus 3d] add_size 200000 add_align 100000
[   32.476489] pcieport 0000:08:04.0: bridge window [io  0x1000-0x0fff] to [bus 3e-71] add_size 1000
[   32.476491] pcieport 0000:07:00.0: bridge window [io  0x1000-0x0fff] to [bus 08-71] add_size 4000
[   32.476494] pcieport 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[   32.476495] pcieport 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[   32.476496] pcieport 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[   32.476496] pcieport 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[   32.476501] pcieport 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[   32.476501] pcieport 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[   32.476502] pcieport 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[   32.476503] pcieport 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[   32.476504] pcieport 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[   32.476505] pcieport 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[   32.476505] pcieport 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[   32.476506] pcieport 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[   32.476507] pcieport 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[   32.476508] pcieport 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[   32.476510] pcieport 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[   32.476511] pcieport 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[   32.476512] pcieport 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[   32.476512] pcieport 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[   32.476513] pcieport 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[   32.476514] pcieport 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[   37.259319] pcieport 0000:08:00.0: Refused to change power state, currently in D3
[   37.263793] pci_bus 0000:09: busn_res: [bus 09] is released
[   37.263826] pci_bus 0000:0a: busn_res: [bus 0a-3c] is released
[   37.263851] pci_bus 0000:3d: busn_res: [bus 3d] is released
[   37.263887] pci_bus 0000:3e: busn_res: [bus 3e-71] is released
[   37.263910] pci_bus 0000:08: busn_res: [bus 08-71] is released
[  202.860339] usb 1-4: reset high-speed USB device number 2 using xhci_hcd
[  203.273766] Bluetooth: RFCOMM TTY layer initialized
[  203.273770] Bluetooth: RFCOMM socket layer initialized
[  203.273773] Bluetooth: RFCOMM ver 1.11
[  203.940755] rfkill: input handler disabled
[  265.403551] pci 0000:07:00.0: [8086:15d3] type 01 class 0x060400
[  265.403633] pci 0000:07:00.0: enabling Extended Tags
[  265.403758] pci 0000:07:00.0: supports D1 D2
[  265.403759] pci 0000:07:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[  265.403937] pcieport 0000:00:1c.4: ASPM: current common clock configuration is broken, reconfiguring
[  265.419512] pci 0000:08:00.0: [8086:15d3] type 01 class 0x060400
[  265.419599] pci 0000:08:00.0: enabling Extended Tags
[  265.419729] pci 0000:08:00.0: supports D1 D2
[  265.419730] pci 0000:08:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[  265.419856] pci 0000:08:01.0: [8086:15d3] type 01 class 0x060400
[  265.419940] pci 0000:08:01.0: enabling Extended Tags
[  265.420064] pci 0000:08:01.0: supports D1 D2
[  265.420065] pci 0000:08:01.0: PME# supported from D0 D1 D2 D3hot D3cold
[  265.420181] pci 0000:08:02.0: [8086:15d3] type 01 class 0x060400
[  265.420266] pci 0000:08:02.0: enabling Extended Tags
[  265.420384] pci 0000:08:02.0: supports D1 D2
[  265.420384] pci 0000:08:02.0: PME# supported from D0 D1 D2 D3hot D3cold
[  265.420507] pci 0000:08:04.0: [8086:15d3] type 01 class 0x060400
[  265.420592] pci 0000:08:04.0: enabling Extended Tags
[  265.420714] pci 0000:08:04.0: supports D1 D2
[  265.420716] pci 0000:08:04.0: PME# supported from D0 D1 D2 D3hot D3cold
[  265.420865] pci 0000:07:00.0: PCI bridge to [bus 08-71]
[  265.420876] pci 0000:07:00.0:   bridge window [mem 0xac000000-0xda0fffff]
[  265.420883] pci 0000:07:00.0:   bridge window [mem 0x2f90000000-0x2fd9ffffff 64bit pref]
[  265.420953] pci 0000:09:00.0: [8086:15d2] type 00 class 0x088000
[  265.420990] pci 0000:09:00.0: reg 0x10: [mem 0xda000000-0xda03ffff]
[  265.421002] pci 0000:09:00.0: reg 0x14: [mem 0xda040000-0xda040fff]
[  265.421064] pci 0000:09:00.0: enabling Extended Tags
[  265.421186] pci 0000:09:00.0: supports D1 D2
[  265.421187] pci 0000:09:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[  265.421383] pci 0000:08:00.0: PCI bridge to [bus 09]
[  265.421394] pci 0000:08:00.0:   bridge window [mem 0xda000000-0xda0fffff]
[  265.421458] pci 0000:08:01.0: PCI bridge to [bus 0a-3c]
[  265.421469] pci 0000:08:01.0:   bridge window [mem 0xac000000-0xc3efffff]
[  265.421476] pci 0000:08:01.0:   bridge window [mem 0x2f90000000-0x2fafffffff 64bit pref]
[  265.421561] pci 0000:3d:00.0: [8086:15d4] type 00 class 0x0c0330
[  265.421600] pci 0000:3d:00.0: reg 0x10: [mem 0xc3f00000-0xc3f0ffff]
[  265.421789] pci 0000:3d:00.0: supports D1 D2
[  265.421790] pci 0000:3d:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[  265.421865] pci 0000:3d:00.0: 8.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s x4 link at 0000:08:02.0 (capable of 31.504 Gb/s with 8 GT/s x4 link)
[  265.421995] pci 0000:08:02.0: PCI bridge to [bus 3d]
[  265.422007] pci 0000:08:02.0:   bridge window [mem 0xc3f00000-0xc3ffffff]
[  265.422069] pci 0000:08:04.0: PCI bridge to [bus 3e-71]
[  265.422079] pci 0000:08:04.0:   bridge window [mem 0xc4000000-0xd9ffffff]
[  265.422087] pci 0000:08:04.0:   bridge window [mem 0x2fb0000000-0x2fd9ffffff 64bit pref]
[  265.422124] pci_bus 0000:08: Allocating resources
[  265.422145] pci 0000:08:01.0: bridge window [io  0x1000-0x0fff] to [bus 0a-3c] add_size 1000
[  265.422146] pci 0000:08:02.0: bridge window [io  0x1000-0x0fff] to [bus 3d] add_size 1000
[  265.422148] pci 0000:08:02.0: bridge window [mem 0x00100000-0x000fffff 64bit pref] to [bus 3d] add_size 200000 add_align 100000
[  265.422150] pci 0000:08:04.0: bridge window [io  0x1000-0x0fff] to [bus 3e-71] add_size 1000
[  265.422153] pci 0000:07:00.0: bridge window [io  0x1000-0x0fff] to [bus 08-71] add_size 4000
[  265.422156] pci 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[  265.422157] pci 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[  265.422158] pci 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[  265.422159] pci 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[  265.422163] pci 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[  265.422165] pci 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[  265.422166] pci 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[  265.422167] pci 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[  265.422168] pci 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[  265.422169] pci 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[  265.422170] pci 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[  265.422170] pci 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[  265.422172] pci 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[  265.422173] pci 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[  265.422175] pci 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[  265.422175] pci 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[  265.422176] pci 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[  265.422177] pci 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[  265.422178] pci 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[  265.422179] pci 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[  265.422181] pci 0000:08:00.0: PCI bridge to [bus 09]
[  265.422186] pci 0000:08:00.0:   bridge window [mem 0xda000000-0xda0fffff]
[  265.422196] pci 0000:08:01.0: PCI bridge to [bus 0a-3c]
[  265.422202] pci 0000:08:01.0:   bridge window [mem 0xac000000-0xc3efffff]
[  265.422206] pci 0000:08:01.0:   bridge window [mem 0x2f90000000-0x2fafffffff 64bit pref]
[  265.422212] pci 0000:08:02.0: PCI bridge to [bus 3d]
[  265.422218] pci 0000:08:02.0:   bridge window [mem 0xc3f00000-0xc3ffffff]
[  265.422227] pci 0000:08:04.0: PCI bridge to [bus 3e-71]
[  265.422232] pci 0000:08:04.0:   bridge window [mem 0xc4000000-0xd9ffffff]
[  265.422236] pci 0000:08:04.0:   bridge window [mem 0x2fb0000000-0x2fd9ffffff 64bit pref]
[  265.422243] pci 0000:07:00.0: PCI bridge to [bus 08-71]
[  265.422248] pci 0000:07:00.0:   bridge window [mem 0xac000000-0xda0fffff]
[  265.422252] pci 0000:07:00.0:   bridge window [mem 0x2f90000000-0x2fd9ffffff 64bit pref]
[  265.423580] xhci_hcd 0000:3d:00.0: xHCI Host Controller
[  265.423584] xhci_hcd 0000:3d:00.0: new USB bus registered, assigned bus number 5
[  265.424734] xhci_hcd 0000:3d:00.0: hcc params 0x200077c1 hci version 0x110 quirks 0x0000000200009810
[  265.424965] usb usb5: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.02
[  265.424966] usb usb5: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[  265.424967] usb usb5: Product: xHCI Host Controller
[  265.424968] usb usb5: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[  265.424969] usb usb5: SerialNumber: 0000:3d:00.0
[  265.425786] hub 5-0:1.0: USB hub found
[  265.425849] hub 5-0:1.0: 2 ports detected
[  265.426642] xhci_hcd 0000:3d:00.0: xHCI Host Controller
[  265.426646] xhci_hcd 0000:3d:00.0: new USB bus registered, assigned bus number 6
[  265.426648] xhci_hcd 0000:3d:00.0: Host supports USB 3.1 Enhanced SuperSpeed
[  265.426740] usb usb6: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.02
[  265.426741] usb usb6: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[  265.426742] usb usb6: Product: xHCI Host Controller
[  265.426743] usb usb6: Manufacturer: Linux 5.2.0-rc1-amd+ xhci-hcd
[  265.426744] usb usb6: SerialNumber: 0000:3d:00.0
[  265.426834] hub 6-0:1.0: USB hub found
[  265.426842] hub 6-0:1.0: 2 ports detected
[  305.046836] xhci_hcd 0000:3d:00.0: Refused to change power state, currently in D3
[  305.122649] xhci_hcd 0000:3d:00.0: Refused to change power state, currently in D3
[  305.122681] xhci_hcd 0000:3d:00.0: WARN: xHC restore state timeout
[  305.122682] xhci_hcd 0000:3d:00.0: PCI post-resume error -110!
[  305.122683] xhci_hcd 0000:3d:00.0: HC died; cleaning up
[  305.122742] xhci_hcd 0000:3d:00.0: remove, state 4
[  305.122745] usb usb6: USB disconnect, device number 1
[  305.122936] xhci_hcd 0000:3d:00.0: USB bus 6 deregistered
[  305.122939] xhci_hcd 0000:3d:00.0: remove, state 4
[  305.122942] usb usb5: USB disconnect, device number 1
[  305.123141] xhci_hcd 0000:3d:00.0: Host halt failed, -19
[  305.123143] xhci_hcd 0000:3d:00.0: Host not accessible, reset failed.
[  305.123199] xhci_hcd 0000:3d:00.0: USB bus 5 deregistered
[  305.178875] pci_bus 0000:08: Allocating resources
[  305.178892] pcieport 0000:08:01.0: bridge window [io  0x1000-0x0fff] to [bus 0a-3c] add_size 1000
[  305.178894] pcieport 0000:08:02.0: bridge window [io  0x1000-0x0fff] to [bus 3d] add_size 1000
[  305.178895] pcieport 0000:08:02.0: bridge window [mem 0x00100000-0x000fffff 64bit pref] to [bus 3d] add_size 200000 add_align 100000
[  305.178896] pcieport 0000:08:04.0: bridge window [io  0x1000-0x0fff] to [bus 3e-71] add_size 1000
[  305.178898] pcieport 0000:07:00.0: bridge window [io  0x1000-0x0fff] to [bus 08-71] add_size 4000
[  305.178900] pcieport 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[  305.178901] pcieport 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[  305.178902] pcieport 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[  305.178903] pcieport 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[  305.178907] pcieport 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[  305.178908] pcieport 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[  305.178909] pcieport 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[  305.178910] pcieport 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[  305.178910] pcieport 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[  305.178911] pcieport 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[  305.178912] pcieport 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[  305.178913] pcieport 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[  305.178914] pcieport 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[  305.178915] pcieport 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[  305.178916] pcieport 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[  305.178917] pcieport 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[  305.178918] pcieport 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[  305.178919] pcieport 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[  305.178919] pcieport 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[  305.178920] pcieport 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[  309.942836] pcieport 0000:08:00.0: Refused to change power state, currently in D3
[  309.947391] pci_bus 0000:09: busn_res: [bus 09] is released
[  309.947425] pci_bus 0000:0a: busn_res: [bus 0a-3c] is released
[  309.947450] pci_bus 0000:3d: busn_res: [bus 3d] is released
[  309.947486] pci_bus 0000:3e: busn_res: [bus 3e-71] is released
[  309.947509] pci_bus 0000:08: busn_res: [bus 08-71] is released
```








---

### 评论 #10 — kentrussell (2019-05-22T11:17:12Z)

@HulioVRD , it looks like VegaM is being seen correctly by ROCm. clinfo running to completion means that the kernel/thunk/runtime are all working together correctly, so that's a plus. Here's what I find concerning in your dmesg:
[    4.907881] [drm] dce110_link_encoder_construct: Failed to get encoder_cap_info from VBIOS with error code 4!
[    4.907900] [drm] dce110_link_encoder_construct: Failed to get encoder_cap_info from VBIOS with error code 4!
...
[    7.678800] pci 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[    7.678801] pci 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[    7.678802] pci 0000:07:00.0: BAR 13: no space for [io  size 0x4000]
[    7.678803] pci 0000:07:00.0: BAR 13: failed to assign [io  size 0x4000]
[    7.678807] pci 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[    7.678808] pci 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[    7.678809] pci 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[    7.678810] pci 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678811] pci 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[    7.678812] pci 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678813] pci 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[    7.678814] pci 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678815] pci 0000:08:04.0: BAR 13: no space for [io  size 0x1000]
[    7.678816] pci 0000:08:04.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678818] pci 0000:08:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[    7.678819] pci 0000:08:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[    7.678820] pci 0000:08:02.0: BAR 13: no space for [io  size 0x1000]
[    7.678821] pci 0000:08:02.0: BAR 13: failed to assign [io  size 0x1000]
[    7.678822] pci 0000:08:01.0: BAR 13: no space for [io  size 0x1000]
[    7.678823] pci 0000:08:01.0: BAR 13: failed to assign [io  size 0x1000]

If the BAR can't be assigned, that's a big problem. I would try to update the VBIOS for the GPU first, as that may also address the VCE errors. If that doesn't work, try look for a BIOS update for the board and see if there is an issue with the PCI bar allocation caused by that. Good luck!

---

### 评论 #11 — phush0 (2019-05-22T11:29:56Z)

All boards with VegaM have this problem, I am on laptop with 8706G and I have same problem with BAR13 and 15

```
[    4.323676] pcieport 0000:05:02.0: bridge window [mem 0x00100000-0x000fffff 64bit pref] to [bus 3a] add_size 200000 add_align 100000
[    4.323679] pcieport 0000:05:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[    4.323680] pcieport 0000:05:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
[    4.323681] pcieport 0000:05:02.0: BAR 15: no space for [mem size 0x00200000 64bit pref]
[    4.323682] pcieport 0000:05:02.0: BAR 15: failed to assign [mem size 0x00200000 64bit pref]
```

but in the same time 

```
[    9.892998] ATOM BIOS: 412926.180424.002
[    9.893022] [drm] GPU posting now...
[    9.926858] [drm] vm size is 64 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[    9.927147] amdgpu 0000:01:00.0: BAR 2: releasing [mem 0xb0000000-0xb01fffff 64bit pref]
[    9.927149] amdgpu 0000:01:00.0: BAR 0: releasing [mem 0xa0000000-0xafffffff 64bit pref]
[    9.927161] amdgpu 0000:01:00.0: BAR 0: assigned [mem 0xa0000000-0xafffffff 64bit pref]
[    9.927168] amdgpu 0000:01:00.0: BAR 2: assigned [mem 0xb0000000-0xb01fffff 64bit pref]
[    9.927182] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    9.927183] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    9.927191] [drm] Detected VRAM RAM=4096M, BAR=256M
[    9.927192] [drm] RAM width 256bits HBM
[    9.927310] [TTM] Zone  kernel: Available graphics memory: 8132236 kiB
[    9.927311] [TTM] Zone   dma32: Available graphics memory: 2097152 kiB
[    9.927311] [TTM] Initializing pool allocator
[    9.927314] [TTM] Initializing DMA pool allocator
[    9.927343] [drm] amdgpu: 4096M of VRAM memory ready
[    9.927344] [drm] amdgpu: 4096M of GTT memory ready.
[    9.927384] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    9.927420] [drm] PCIE GART of 256M enabled (table at 0x000000F400000000).
[    9.945082] [drm] Chained IB support enabled!
[    9.950566] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input9
[    9.950753] snd_hda_intel 0000:00:1f.3: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
[    9.955604] [drm] Found UVD firmware Version: 1.130 Family ID: 16
[    9.956618] [drm] Found VCE firmware Version: 53.21 Binary ID: 3
[    9.960683] fbcon: inteldrmfb (fb0) is primary device
[   10.025435] [drm] DM_PPLIB: values for Engine clock
[   10.025436] [drm] DM_PPLIB:	 225000
[   10.025437] [drm] DM_PPLIB:	 400000
[   10.025437] [drm] DM_PPLIB:	 535000
[   10.025437] [drm] DM_PPLIB:	 715000
[   10.025438] [drm] DM_PPLIB:	 850000
[   10.025438] [drm] DM_PPLIB:	 960000
[   10.025438] [drm] DM_PPLIB:	 985000
[   10.025439] [drm] DM_PPLIB:	 1011000
[   10.025448] [drm] DM_PPLIB: Validation clocks:
[   10.025448] [drm] DM_PPLIB:    engine_max_clock: 101100
[   10.025449] [drm] DM_PPLIB:    memory_max_clock: 70000
[   10.025450] [drm] DM_PPLIB:    level           : 8
[   10.025452] [drm] DM_PPLIB: values for Memory clock
[   10.025453] [drm] DM_PPLIB:	 300000
[   10.025453] [drm] DM_PPLIB:	 500000
[   10.025454] [drm] DM_PPLIB:	 700000
[   10.025455] [drm] DM_PPLIB: Validation clocks:
[   10.025456] [drm] DM_PPLIB:    engine_max_clock: 101100
[   10.025457] [drm] DM_PPLIB:    memory_max_clock: 70000
[   10.025458] [drm] DM_PPLIB:    level           : 8
[   10.025849] [drm] Display Core initialized with v3.2.17!
[   10.025889] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   10.025889] [drm] Driver supports precise vblank timestamp query.
[   10.072492] [drm] UVD and UVD ENC initialized successfully.
[   10.182433] [drm] VCE initialized successfully.
```

my init is ok

---

### 评论 #12 — HulioVRD (2019-05-22T11:45:01Z)

@phush0 
Could you post informations about your system and kernel version? Is ROCm working on your machine?

---

### 评论 #13 — phush0 (2019-05-22T12:18:40Z)

Dell Precision 5530 2-in-1 with Ubuntu 18.04.2, kernel 5.1.4, ROCm is not working because I don't have patched kernel. If I figure out how to compile only AMDGPU module will try, for now I am waiting for official release

---

### 评论 #14 — kentrussell (2019-05-22T13:13:27Z)

@phush0 The whole modules thing is difficult. We managed to leverage the work that the amdgpu-pro guys use, because trying to just do it ourselves was such a pain. The monolithic kernel works, but there are other components that could hit issues, especially on laptops, so I understand wanting to wait until the next release. Hopefully the addition of these to the kernel/thunk will be sufficient, and 2.5 should hopefully be quick enough that we can get it on your systems soon. Thanks for your patience in this matter.

---

### 评论 #15 — kentrussell (2019-06-07T12:20:07Z)

2,5 is out or will be released to the repo shortly, you should be able to give it a shot for the VegaM support. Good luck!

---

### 评论 #16 — phush0 (2019-06-11T12:08:54Z)

```
[    9.545686] amdgpu 0000:01:00.0: enabling device (0006 -> 0007)
[    9.545917] [drm] initializing kernel modesetting (VEGAM 0x1002:0x694F 0x1028:0x08AC 0xC0).
[    9.547459] acpi PNP0C14:03: duplicate WMI GUID 05901221-D566-11D1-B2F0-00A0C9062910 (first instance was on PNP0C14:01)
[    9.548578] i915 0000:00:02.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=io+mem
[    9.549270] [drm] Finished loading DMC firmware i915/kbl_dmc_ver1_04.bin (v1.4)
[    9.551033] [drm] register mmio base: 0xEC300000
[    9.551034] [drm] register mmio size: 262144
[    9.551039] [drm] add ip block number 0 <vi_common>
[    9.551040] [drm] add ip block number 1 <gmc_v8_0>
[    9.551041] [drm] add ip block number 2 <tonga_ih>
[    9.551041] [drm] add ip block number 3 <gfx_v8_0>
[    9.551042] [drm] add ip block number 4 <sdma_v3_0>
[    9.551043] [drm] add ip block number 5 <powerplay>
[    9.551044] [drm] add ip block number 6 <dm>
[    9.551044] [drm] add ip block number 7 <uvd_v6_0>
[    9.551045] [drm] add ip block number 8 <vce_v3_0>
[    9.551047] amdgpu 0000:01:00.0: kfd not supported on this ASIC
[    9.551057] [drm] UVD is enabled in VM mode
[    9.551057] [drm] UVD ENC is enabled in VM mode
[    9.551059] [drm] VCE enabled in VM mode
[    9.551069] vga_switcheroo: enabled
[    9.559356] iwlwifi 0000:02:00.0: base HW address: 64:5d:86:ee:90:a8
[    9.600443] dcdbas dcdbas: Dell Systems Management Base Driver (version 5.6.0-3.2)
[    9.640677] ieee80211 phy0: Selected rate control algorithm 'iwl-mvm-rs'
[    9.640859] thermal thermal_zone11: failed to read out thermal zone (-61)
[    9.676896] iwlwifi 0000:02:00.0 wlp2s0: renamed from wlan0
[    9.677042] audit: type=1400 audit(1560254094.324:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-xpdfimport" pid=642 comm="apparmor_parser"
[    9.677704] audit: type=1400 audit(1560254094.324:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=640 comm="apparmor_parser"
[    9.677845] audit: type=1400 audit(1560254094.324:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oopslash" pid=639 comm="apparmor_parser"
[    9.677876] audit: type=1400 audit(1560254094.324:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=638 comm="apparmor_parser"
[    9.677878] audit: type=1400 audit(1560254094.324:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=638 comm="apparmor_parser"
[    9.677880] audit: type=1400 audit(1560254094.324:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=638 comm="apparmor_parser"
[    9.679167] audit: type=1400 audit(1560254094.324:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/ippusbxd" pid=647 comm="apparmor_parser"
[    9.679169] audit: type=1400 audit(1560254094.324:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=645 comm="apparmor_parser"
[    9.680131] audit: type=1400 audit(1560254094.328:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/tcpdump" pid=649 comm="apparmor_parser"
[    9.680586] audit: type=1400 audit(1560254094.328:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-soffice" pid=641 comm="apparmor_parser"
[    9.713172] ATOM BIOS: 412926.180424.002
[    9.713185] [drm] GPU posting now...
[    9.786251] input: Dell WMI hotkeys as /devices/platform/PNP0C14:01/wmi_bus/wmi_bus-PNP0C14:01/9DBB5994-A997-11DA-B012-B622A1EF5492/input/input8
[    9.808127] [drm] RAS INFO: ras initialized successfully, hardware ability[0] ras_mask[0]
[    9.808133] [drm] vm size is 64 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[    9.808150] amdgpu 0000:01:00.0: BAR 2: releasing [mem 0xb0000000-0xb01fffff 64bit pref]
[    9.808151] amdgpu 0000:01:00.0: BAR 0: releasing [mem 0xa0000000-0xafffffff 64bit pref]
[    9.808189] amdgpu 0000:01:00.0: BAR 0: assigned [mem 0xa0000000-0xafffffff 64bit pref]
[    9.808195] amdgpu 0000:01:00.0: BAR 2: assigned [mem 0xb0000000-0xb01fffff 64bit pref]
[    9.808247] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    9.808248] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    9.808258] [drm] Detected VRAM RAM=4096M, BAR=256M
[    9.808259] [drm] RAM width 4096bits HBM
[    9.808354] [TTM] Zone  kernel: Available graphics memory: 15250541 KiB
[    9.808354] [TTM] Zone   dma32: Available graphics memory: 2097152 KiB
[    9.808355] [TTM] Initializing pool allocator
[    9.808357] [TTM] Initializing DMA pool allocator
[    9.808384] [drm] amdgpu: 4096M of VRAM memory ready
[    9.808385] [drm] amdgpu: 15885M of GTT memory ready.
[    9.808394] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    9.808452] [drm] PCIE GART of 256M enabled (table at 0x000000F400000000).
[    9.810048] [drm] Chained IB support enabled!
[    9.813890] [drm] Found UVD firmware Version: 1.130 Family ID: 16
[    9.815575] [drm] Found VCE firmware Version: 53.21 Binary ID: 3
[    9.894823] [drm] DM_PPLIB: values for Engine clock
[    9.894824] [drm] DM_PPLIB:	 225000
[    9.894824] [drm] DM_PPLIB:	 400000
[    9.894824] [drm] DM_PPLIB:	 535000
[    9.894825] [drm] DM_PPLIB:	 715000
[    9.894825] [drm] DM_PPLIB:	 850000
[    9.894825] [drm] DM_PPLIB:	 960000
[    9.894826] [drm] DM_PPLIB:	 985000
[    9.894826] [drm] DM_PPLIB:	 1011000
[    9.894826] [drm] DM_PPLIB: Validation clocks:
[    9.894827] [drm] DM_PPLIB:    engine_max_clock: 101100
[    9.894827] [drm] DM_PPLIB:    memory_max_clock: 70000
[    9.894827] [drm] DM_PPLIB:    level           : 8
[    9.894828] [drm] DM_PPLIB: values for Memory clock
[    9.894829] [drm] DM_PPLIB:	 300000
[    9.894829] [drm] DM_PPLIB:	 500000
[    9.894829] [drm] DM_PPLIB:	 700000
[    9.894830] [drm] DM_PPLIB: Validation clocks:
[    9.894830] [drm] DM_PPLIB:    engine_max_clock: 101100
[    9.894830] [drm] DM_PPLIB:    memory_max_clock: 70000
[    9.894830] [drm] DM_PPLIB:    level           : 8
[    9.895270] [drm] Display Core initialized with v3.2.31!
[    9.895306] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    9.895307] [drm] Driver supports precise vblank timestamp query.
[    9.942764] [drm] UVD and UVD ENC initialized successfully.
[   10.052712] [drm] VCE initialized successfully.
[   10.082097] [drm] Initialized amdgpu 3.32.0 20150101 for 0000:01:00.0 on minor 1
[   10.082592] [drm] Initialized i915 1.6.0 20180514 for 0000:00:02.0 on minor 0
[   10.123084] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[   10.152362] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input9
[   10.154542] snd_hda_intel 0000:00:1f.3: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
[   10.159796] fbcon: inteldrmfb (fb0) is primary device
[   10.159942] Console: switching to colour frame buffer device 480x135
[   10.160061] i915 0000:00:02.0: fb0: inteldrmfb frame buffer device
```

With 2.5 GPU will init but KFD is not available. There is no mainline support still for Vega M.

```
/opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.5/rocminfo/rocminfo.cc. Call returned 4104
```
```
/opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 
  Platform Name:				 Intel(R) OpenCL HD Graphics
  Platform Vendor:				 Intel(R) Corporation
  Platform Extensions:				 cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_depth_images cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_icd cl_khr_image2d_from_buffer cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_intel_subgroups cl_intel_required_subgroup_size cl_intel_subgroups_short cl_khr_spir cl_intel_accelerator cl_intel_media_block_io cl_intel_driver_diagnostics cl_intel_device_side_avc_motion_estimation cl_khr_priority_hints cl_khr_throttle_hints cl_khr_create_command_queue cl_khr_fp64 cl_khr_subgroups cl_khr_il_program cl_intel_spirv_device_side_avc_motion_estimation cl_intel_spirv_media_block_io cl_intel_spirv_subgroups cl_khr_spirv_no_integer_wrap_decoration cl_khr_mipmap_image cl_khr_mipmap_image_writes cl_intel_planar_yuv cl_intel_packed_yuv cl_intel_motion_estimation cl_intel_advanced_motion_estimation cl_intel_va_api_media_sharing 


  Platform Name:				 Intel(R) OpenCL HD Graphics
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 8086h
  Max compute units:				 23
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 16
  Preferred vector width short:			 8
  Preferred vector width int:			 4
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 16
  Native vector width short:			 8
  Native vector width int:			 4
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1100Mhz
  Address bits:					 64
  Max memory allocation:			 4294959104
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 128
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 16384
  Max image 3D height:				 16384
  Max image 3D depth:				 2048
  Max samplers within kernel:			 16
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 524288
  Global memory size:				 13326123008
  Constant buffer size:				 4294959104
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 1
  Max pipe packet size:				 1024
  Max global variable size:			 65536
  Max global variable preferred total size:	 4294959104
  Max read/write image args:			 128
  Max on device events:				 1024
  Queue on device max size:			 67108864
  Max on device queues:				 1
  Queue on device preferred size:		 131072
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 No
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 64
  Preferred global atomic alignment:		 64
  Preferred local atomic alignment:		 64
  Kernel Preferred work group size multiple:	 32
  Error correction support:			 0
  Unified memory for Host and Device:		 1
  Profiling timer resolution:			 83
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x189b8c0
  Name:						 Intel(R) Gen9 HD Graphics NEO
  Vendor:					 Intel(R) Corporation
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 19.21.13045
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.1 NEO 
  Extensions:					 cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_depth_images cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_icd cl_khr_image2d_from_buffer cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_intel_subgroups cl_intel_required_subgroup_size cl_intel_subgroups_short cl_khr_spir cl_intel_accelerator cl_intel_media_block_io cl_intel_driver_diagnostics cl_intel_device_side_avc_motion_estimation cl_khr_priority_hints cl_khr_throttle_hints cl_khr_create_command_queue cl_khr_fp64 cl_khr_subgroups cl_khr_il_program cl_intel_spirv_device_side_avc_motion_estimation cl_intel_spirv_media_block_io cl_intel_spirv_subgroups cl_khr_spirv_no_integer_wrap_decoration cl_khr_mipmap_image cl_khr_mipmap_image_writes cl_intel_planar_yuv cl_intel_packed_yuv cl_intel_motion_estimation cl_intel_advanced_motion_estimation cl_intel_va_api_media_sharing 

```



---

### 评论 #17 — kentrussell (2019-06-11T12:33:12Z)

I included the ASIC IDs but I didn't include the actual family during the amdgpu_amdkfd_device_probe. I didn't have a VegaM to test on, so I was just deducing the work needing to be done. Sorry about that. If you're willing to build your own kernel, can you try to add one line to amdgpu_amdkfd.c ? 

Change:
        case CHIP_POLARIS12:
                kfd2kgd = amdgpu_amdkfd_gfx_8_0_get_functions();
                break;

To:
        case CHIP_POLARIS12:
        case CHIP_VEGAM:
                kfd2kgd = amdgpu_amdkfd_gfx_8_0_get_functions();
                break;


---

### 评论 #18 — kentrussell (2019-06-11T14:04:55Z)

I just made the change to upstream (https://lists.freedesktop.org/archives/amd-gfx/2019-June/034955.html) . It will be in 2.6.

---

### 评论 #19 — phush0 (2019-06-28T13:11:58Z)

I have tried newest code in DRM-tip branch, even calling clinfo will lead to hardlock of the system, KFD is now initting. 

---

### 评论 #20 — phush0 (2019-07-09T14:08:34Z)

```
[   56.916112] [drm] PCIE GART of 256M enabled (table at 0x000000F400000000).
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.019047] [drm] UVD and UVD ENC initialized successfully.
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.118963] [drm] VCE initialized successfully.
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120048] Started restoring pasid 32769
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120052] BUG: unable to handle kernel NULL pointer dereference at 0000000000000060
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120054] PGD 0 P4D 0 
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120056] Oops: 0000 [#1] SMP PTI
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120058] CPU: 1 PID: 234 Comm: kworker/u16:3 Tainted: G           OE     4.18.0-25-generic #26~18.04.1-Ubuntu
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120059] Hardware name: Dell Inc. Precision 5530 2-in-1/02TH5P, BIOS 1.0.5 10/15/2018
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120103] Workqueue: kfd_restore_wq restore_process_worker [amdgpu]
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120175] RIP: 0010:amdgpu_amdkfd_gpuvm_restore_process_bos+0x23/0x490 [amdgpu]
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120178] Code: 5d c3 0f 1f 44 00 00 0f 1f 44 00 00 55 48 89 e5 41 57 41 56 41 55 41 54 53 48 89 fb 48 81 ec 58 01 00 00 48 89 b5 88 fe ff ff <8b> 7f 60 be c0 80 60 00 48 c1 e7 06 65 48 8b 04 25 28 00 00 00 48 
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120200] RSP: 0018:ffffa07201f4fcc8 EFLAGS: 00010292
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120201] RAX: 00000000ffff126e RBX: 0000000000000000 RCX: 0000000000000000
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120202] RDX: 0000000000000000 RSI: ffff937053a7fd40 RDI: 0000000000000000
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120205] RBP: ffffa07201f4fe48 R08: 0000000000000519 R09: 0000000000000004
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120208] R10: 0000000000000010 R11: 0000000000000001 R12: ffff937053a7fda0
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120209] R13: ffff937053a7fc00 R14: ffff937053a7fda0 R15: 0ffff937059efe30
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120210] FS:  0000000000000000(0000) GS:ffff93706e440000(0000) knlGS:0000000000000000
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120211] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120212] CR2: 0000000000000060 CR3: 0000000482e0a005 CR4: 00000000003606e0
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120215] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120217] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120220] Call Trace:
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120242]  ? down_trylock+0x2e/0x40
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120244]  ? irq_work_queue+0x99/0xa0
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120246]  ? vprintk_emit+0xec/0x290
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120250]  ? __switch_to_asm+0x34/0x70
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120252]  ? vprintk_default+0x29/0x50
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120254]  ? vprintk_func+0x47/0xc0
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120256]  ? __switch_to_asm+0x40/0x70
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120258]  ? printk+0x52/0x6e
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120260]  ? __switch_to_asm+0x40/0x70
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120321]  restore_process_worker+0x8e/0xa0 [amdgpu]
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120326]  process_one_work+0x1fd/0x3f0
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120329]  worker_thread+0x34/0x410
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120330]  kthread+0x121/0x140
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120332]  ? process_one_work+0x3f0/0x3f0
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120336]  ? kthread_create_worker_on_cpu+0x70/0x70
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120338]  ret_from_fork+0x35/0x40
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120339] Modules linked in: rfcomm thunderbolt ccm cmac dell_rbu bnep snd_hda_codec_hdmi msr joydev hid_multitouch wacom usbhid uvcvideo videobuf2_vmalloc videobuf2_memops btusb videobuf2_v4l2 btrtl btbcm videobuf2_common btintel videodev bluetooth media ecdh_generic dell_rbtn nls_iso8859_1 dell_laptop dell_wmi dell_smbios snd_hda_codec_realtek snd_hda_codec_generic wmi_bmof intel_wmi_thunderbolt dell_wmi_descriptor dcdbas arc4 dell_smm_hwmon intel_rapl idma64 x86_pkg_temp_thermal virt_dma intel_powerclamp amdgpu(OE) kvm_intel kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc iwlmvm mac80211 aesni_intel aes_x86_64 crypto_simd cryptd glue_helper amdttm(OE) intel_cstate amd_sched(OE) snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120379]  snd_seq snd_seq_device snd_timer intel_rapl_perf snd input_leds i915 serio_raw iwlwifi rtsx_pci_ms soundcore cfg80211 memstick amdkcl(OE) amd_iommu_v2 mei_me intel_lpss_pci drm_kms_helper intel_lpss mei hid_sensor_gyro_3d drm hid_sensor_incl_3d ucsi_acpi intel_pch_thermal hid_sensor_accel_3d hid_sensor_magn_3d hid_sensor_rotation hid_sensor_trigger i2c_algo_bit industrialio_triggered_buffer fb_sys_fops typec_ucsi kfifo_buf processor_thermal_device hid_sensor_iio_common syscopyarea sysfillrect industrialio sysimgblt intel_soc_dts_iosf typec wmi int3403_thermal int340x_thermal_zone intel_vbtn soc_button_array video intel_hid sparse_keymap acpi_pad int3400_thermal acpi_thermal_rel mac_hid sch_fq_codel coretemp parport_pc ppdev lp parport ip_tables x_tables autofs4 hid_sensor_custom hid_sensor_hub
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120420]  hid_generic intel_ishtp_hid rtsx_pci_sdmmc nvme nvme_core rtsx_pci intel_ish_ipc intel_ishtp i2c_hid hid
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120439] CR2: 0000000000000060
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120441] ---[ end trace fa6cc165ae08ceef ]---
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120491] RIP: 0010:amdgpu_amdkfd_gpuvm_restore_process_bos+0x23/0x490 [amdgpu]
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120492] Code: 5d c3 0f 1f 44 00 00 0f 1f 44 00 00 55 48 89 e5 41 57 41 56 41 55 41 54 53 48 89 fb 48 81 ec 58 01 00 00 48 89 b5 88 fe ff ff <8b> 7f 60 be c0 80 60 00 48 c1 e7 06 65 48 8b 04 25 28 00 00 00 48 
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120541] RSP: 0018:ffffa07201f4fcc8 EFLAGS: 00010292
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120542] RAX: 00000000ffff126e RBX: 0000000000000000 RCX: 0000000000000000
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120543] RDX: 0000000000000000 RSI: ffff937053a7fd40 RDI: 0000000000000000
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120544] RBP: ffffa07201f4fe48 R08: 0000000000000519 R09: 0000000000000004
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120545] R10: 0000000000000010 R11: 0000000000000001 R12: ffff937053a7fda0
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120546] R13: ffff937053a7fc00 R14: ffff937053a7fda0 R15: 0ffff937059efe30
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120547] FS:  0000000000000000(0000) GS:ffff93706e440000(0000) knlGS:0000000000000000
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120548] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120549] CR2: 0000000000000060 CR3: 0000000482e0a005 CR4: 00000000003606e0
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120550] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
Jul  9 17:00:38 phusho-Precision-5530-2-in-1 kernel: [   57.120551] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
Jul  9 17:00:43 phusho-Precision-5530-2-in-1 kernel: [   62.709808] amdgpu 0000:01:00.0: GPU pci config reset
```

complete system freeze, mouse move but nothing else is working

---

### 评论 #21 — phush0 (2019-07-23T12:58:12Z)

same for dkms and 5.3 rc1

---

### 评论 #22 — kentrussell (2019-07-23T14:17:09Z)

I'm taking a look at this. I have a hunch or two. Thanks for keeping this alive @phush0 

My first thought:
```
diff --git a/drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c b/drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c
index f5ecf28eb37c..3179117ac434 100644
--- a/drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c
+++ b/drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c
@@ -1139,7 +1139,8 @@ int amdgpu_amdkfd_gpuvm_alloc_memory_of_gpu(
                        adev->asic_type != CHIP_FIJI &&
                        adev->asic_type != CHIP_POLARIS10 &&
                        adev->asic_type != CHIP_POLARIS11 &&
-                       adev->asic_type != CHIP_POLARIS12) ?
+                       adev->asic_type != CHIP_POLARIS12 &&
+                       adev->asic_type != CHIP_VEGAM) ?
                        VI_BO_SIZE_ALIGN : 1;

```
I just put this out for review. I needed to ask @fxkamd about the TLB workaround on older VI chips, but he's out of office for a week. Waiting for upstream review to take a look, but do you want to try that out as well? Thanks for being willing to be my guinea pig

---

### 评论 #23 — phush0 (2019-08-05T11:50:26Z)

I have tested align patch for VegaM

```
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.898346] [drm] VCE initialized successfully.
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899425] BUG: kernel NULL pointer dereference, address: 0000000000000060
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899427] #PF: supervisor read access in kernel mode
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899428] #PF: error_code(0x0000) - not-present page
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899429] PGD 0 P4D 0 
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899430] Oops: 0000 [#1] SMP PTI
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899432] CPU: 1 PID: 289 Comm: kworker/u16:4 Tainted: G     U            5.3.0-050300rc3-generic #201908042232
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899432] Hardware name: Dell Inc. Precision 5530 2-in-1/02TH5P, BIOS 1.0.5 10/15/2018
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899530] Workqueue: kfd_restore_wq restore_process_worker [amdgpu]
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899569] RIP: 0010:amdgpu_amdkfd_gpuvm_restore_process_bos+0x2a/0x530 [amdgpu]
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899570] Code: 0f 1f 44 00 00 55 48 89 e5 41 57 41 56 41 55 41 54 4c 8d a5 18 ff ff ff 53 48 89 fb 48 81 ec 58 01 00 00 48 89 b5 88 fe ff ff <8b> 7f 60 be c0 0d 00 00 48 c1 e7 06 65 48 8b 04 25 28 00 00 00 48
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899571] RSP: 0000:ffffb1e1403ebcc0 EFLAGS: 00010286
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899572] RAX: 00000000fffefd09 RBX: 0000000000000000 RCX: ffff959b9c418c20
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899572] RDX: ffff959b9c418c20 RSI: ffff959b24ad0130 RDI: 0000000000000000
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899573] RBP: ffffb1e1403ebe40 R08: 000071775f65726f R09: 8080808080808080
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899573] R10: ffff959b92b0f7f4 R11: 0000000000000018 R12: ffffb1e1403ebd58
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899574] R13: ffff959b24ad0000 R14: 0000000000000000 R15: ffff959b92b0f780
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899575] FS:  0000000000000000(0000) GS:ffff959b9e240000(0000) knlGS:0000000000000000
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899575] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899576] CR2: 0000000000000060 CR3: 000000042ee0a002 CR4: 00000000003606e0
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899577] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899577] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899578] Call Trace:
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899599]  ? i915_sw_fence_complete+0x1b/0x20 [i915]
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899601]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899602]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899603]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899603]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899604]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899605]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899606]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899606]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899607]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899608]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899608]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899609]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899610]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899611]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899611]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899612]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899613]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899614]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899614]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899615]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899616]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899616]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899617]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899618]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899619]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899619]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899620]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899621]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899622]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899624]  ? __switch_to+0x7f/0x470
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899624]  ? __switch_to_asm+0x40/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899625]  ? __switch_to_asm+0x34/0x70
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899661]  restore_process_worker+0x38/0xf0 [amdgpu]
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899663]  process_one_work+0x1db/0x380
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899664]  worker_thread+0x4d/0x400
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899684]  kthread+0x104/0x140
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899685]  ? process_one_work+0x380/0x380
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899686]  ? kthread_park+0x80/0x80
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899687]  ret_from_fork+0x35/0x40
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899689] Modules linked in: rfcomm thunderbolt ccm hid_multitouch msr cmac wacom bnep dell_rbtn joydev uvcvideo videobuf2_vmalloc videobuf2_memops videobuf2_v4l2 btusb videobuf2_common btrtl btbcm videodev btintel mc bluetooth ecdh_generic ecc snd_hda_codec_hdmi snd_hda_codec_realtek snd_hda_codec_generic mei_hdcp intel_rapl_msr dell_laptop ledtrig_audio dell_smm_hwmon x86_pkg_temp_thermal intel_powerclamp dell_rbu kvm_intel kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_intel snd_hda_codec aesni_intel snd_hda_core snd_hwdep snd_pcm aes_x86_64 crypto_simd cryptd glue_helper iwlmvm snd_seq_midi snd_seq_midi_event intel_cstate mac80211 snd_rawmidi intel_rapl_perf libarc4 snd_seq nls_iso8859_1 input_leds dell_wmi snd_seq_device dell_smbios iwlwifi snd_timer serio_raw dcdbas snd rtsx_pci_ms amdgpu intel_wmi_thunderbolt dell_wmi_descriptor wmi_bmof soundcore memstick cfg80211 i915 hid_sensor_magn_3d amd_iommu_v2 gpu_sched hid_sensor_gyro_3d hid_sensor_incl_3d
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899706]  hid_sensor_accel_3d hid_sensor_rotation ttm hid_sensor_trigger industrialio_triggered_buffer kfifo_buf drm_kms_helper hid_sensor_iio_common industrialio idma64 drm virt_dma mei_me cros_ec_ishtp mei processor_thermal_device cros_ec_core i2c_algo_bit intel_lpss_pci intel_rapl_common fb_sys_fops intel_lpss intel_pch_thermal ucsi_acpi syscopyarea sysfillrect sysimgblt intel_soc_dts_iosf typec_ucsi typec soc_button_array int3403_thermal intel_vbtn int340x_thermal_zone intel_hid int3400_thermal acpi_thermal_rel acpi_pad sparse_keymap mac_hid sch_fq_codel coretemp parport_pc ppdev lp parport ip_tables x_tables autofs4 usbhid hid_sensor_custom hid_sensor_hub hid_generic intel_ishtp_loader intel_ishtp_hid rtsx_pci_sdmmc nvme nvme_core intel_ish_ipc rtsx_pci intel_ishtp i2c_hid wmi hid video
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899752] CR2: 0000000000000060
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899753] ---[ end trace a76abeb883b340b1 ]---
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899804] RIP: 0010:amdgpu_amdkfd_gpuvm_restore_process_bos+0x2a/0x530 [amdgpu]
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899805] Code: 0f 1f 44 00 00 55 48 89 e5 41 57 41 56 41 55 41 54 4c 8d a5 18 ff ff ff 53 48 89 fb 48 81 ec 58 01 00 00 48 89 b5 88 fe ff ff <8b> 7f 60 be c0 0d 00 00 48 c1 e7 06 65 48 8b 04 25 28 00 00 00 48
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899806] RSP: 0000:ffffb1e1403ebcc0 EFLAGS: 00010286
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899806] RAX: 00000000fffefd09 RBX: 0000000000000000 RCX: ffff959b9c418c20
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899807] RDX: ffff959b9c418c20 RSI: ffff959b24ad0130 RDI: 0000000000000000
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899808] RBP: ffffb1e1403ebe40 R08: 000071775f65726f R09: 8080808080808080
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899808] R10: ffff959b92b0f7f4 R11: 0000000000000018 R12: ffffb1e1403ebd58
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899809] R13: ffff959b24ad0000 R14: 0000000000000000 R15: ffff959b92b0f780
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899809] FS:  0000000000000000(0000) GS:ffff959b9e240000(0000) knlGS:0000000000000000
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899810] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899811] CR2: 0000000000000060 CR3: 000000042ee0a002 CR4: 00000000003606e0
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899811] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
Aug  5 14:45:54 phusho-Precision-5530-2-in-1 kernel: [   34.899831] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400

```

---

### 评论 #24 — phush0 (2019-10-09T10:34:57Z)

OK, so status update. To make it work you have to add 

```amdgpu.runpm=0```

to boot parameters. Then you follow installation instruction, and will work from next boot. What I have tried:
- clinfo - original and one from rocm, work perfect - before it will crash entire machine;
- clpeak - works good - around level of GTX 1650;
- darktable - see both Intel and VegaM cards and work perfect;
- LuxMark - see both cards and work perfect;

So far so good, only problem is that VegaM is always power on and will consume 7W all the time. If you work on battery it is not good. May be some fix for power ? Working both with rocm-dkms and upstream kernel (5.3 and 5.4 rc)

---

### 评论 #25 — bastibe (2019-10-09T12:15:02Z)

That is fantastic news! What kernel release will this be part of?

---

### 评论 #26 — phush0 (2019-10-09T12:21:44Z)

It is part of 5.3 up or rocm-dkms

---

### 评论 #27 — bastibe (2019-10-09T19:39:05Z)

Thank you all! It seems openCL is finally working! According to `clinfo`, that is.

However, darktable can't use it "due to missing image support" (OpenSuse Tumbleweed, kernel 5.3.2). @phush0, you commented that you got darktable working with openCL. I believe it might currently be trying Mesa-libOpenGL. Is this the right way to do it, or am I missing something? Any help would be greatly appreciated.

Sorry if this is the wrong place to ask this question.

---

### 评论 #28 — JLTastet (2019-10-09T19:59:01Z)

@phush0 Out of curiosity, which distro are you using? If I can get Vega M to work on Fedora, I'll make sure to test Darktable!

---

### 评论 #29 — phush0 (2019-10-09T20:01:47Z)

> Thank you all! It seems openCL is finally working! According to `clinfo`, that is.
> 
> However, darktable can't use it "due to missing image support" (OpenSuse Tumbleweed, kernel 5.3.2). @phush0, you commented that you got darktable working with openCL. I believe it might currently be trying Mesa-libOpenGL. Is this the right way to do it, or am I missing something? Any help would be greatly appreciated.
> 
> Sorry if this is the wrong place to ask this question.

You have to install rocm-opencl-dev package. Mesa is not working 

---

### 评论 #30 — phush0 (2019-10-09T20:02:10Z)

> @phush0 Out of curiosity, which distro are you using? If I can get Vega M to work on Fedora, I'll make sure to test Darktable!

Ubuntu 18.04 with 5.4 rc2, but it work with any 5.3.x

---

### 评论 #31 — JLTastet (2019-10-09T20:04:09Z)

> > @phush0 Out of curiosity, which distro are you using? If I can get Vega M to work on Fedora, I'll make sure to test Darktable!
> 
> Ubuntu 18.04

Thanks! Did you build from source, or are you using some PPA?

---

### 评论 #32 — phush0 (2019-10-09T20:05:32Z)

> > > @phush0 Out of curiosity, which distro are you using? If I can get Vega M to work on Fedora, I'll make sure to test Darktable!
> > 
> > 
> > Ubuntu 18.04
> 
> Thanks! Did you build from source, or are you using some PPA?

PPA! Build is so slow but it is doable

---

### 评论 #33 — bastibe (2019-10-09T20:05:53Z)

I see, I need to use ROCm. Thank you!

---

### 评论 #34 — JLTastet (2019-10-09T20:07:53Z)

> PPA! Build is so slow but it is doable

Thanks! I'll probably try to set up some dual boot when I have time.

---

### 评论 #35 — securelyfitz (2019-10-29T07:35:24Z)

Thanks for this thread. Got a used Hades Canyon for photo purposes and spent too long trying to understand all the different options. In the end:

1. Fresh install of 18.04.3
2. Darktable 2.6.3 via OBS
3. rocm install directions for ubuntu

No changes to kernel parameters needed and darktable finds and uses opencl

neither amdgpu-pro or ubuntu 19.10 worked for me.

---

### 评论 #36 — carlosbravoa (2019-12-15T13:44:12Z)

Hi there. Is there any instructions for dummies? (Or not so dummies) I've been waiting for official support but it doesn't seem to happen anytime soon. 

---

### 评论 #37 — bastibe (2019-12-16T07:41:42Z)

@securelyfitz same here. 18.04 and Darktable master work for me.

---

### 评论 #38 — securelyfitz (2019-12-16T17:05:11Z)

@carlosbravoa some more details of what i did:

1. Fresh install of 18.04.3
http://releases.ubuntu.com/18.04/

2. Darktable 2.6.3 via OBS
details at https://www.darktable.org/install/#3rdparty
choose 'snapshots from latest stable release, then choose 'ubuntu' and follow instructions under 'add repository and install manually'

I'm currently testing darktable 3.0rc2 from 'snapshots from master', it's working well and likely to be released imminently.

3. rocm install directions for ubuntu:
follow steps shown at https://rocm.github.io/install.html#ubuntu-support---installing-from-a-debian-repository

---

### 评论 #39 — oogetyboogety (2019-12-22T16:23:23Z)

works on gentoo 5.4. I think it was fixed in ROCM 2.10/3.0 runtimes with the upstream kernel. I was having difficulties until that specific change.

@carlosbravoa try this

1) gentoo/funtoo/cloveros/any distribution with portage and with latest kernel sources 5.4 
```
jesush@localhost /usr/src/linux-5.4.0-gentoo $ cat .config | grep SWITCHEROO
# CONFIG_VGA_SWITCHEROO is not set
```
```
jesush@localhost ~ $ uname -r
5.4.0-gentoo
```
```
jesush@localhost ~ $ cat /etc/portage/make.conf | grep VIDEO
VIDEO_CARDS="amdgpu i965"
```
2) add `justxi` rocm overlay's runtimes, I'm not sure about the kernel sources there because they are 5.2. just install the runtimes
https://rocm.github.io/install.html#rocm-support-in-upstream-linux-kernels
```

    ROCm Core Components
        ROCk Kernel Driver
        ROCr Runtime
        ROCt Thunk Interface
    ROCm Support Software
        ROCm SMI
        ROCm cmake
        rocminfo
        ROCm Bandwidth Test
    ROCm Development Tools
        HCC compiler
        HIP
        ROCm Device Libraries
        ROCm OpenCL, which is created from the following components:
            ROCm OpenCL Runtime
            ROCm OpenCL Driver
            The ROCm OpenCL compiler, which is created from the following components:
                ROCm LLVM OCL
                ROCm LLVM HCC
                ROCm Clang
                ROCm lld OCL
                ROCm lld HCC
                ROCm Device Libraries
        ROCM Clang-OCL Kernel Compiler
        Asynchronous Task and Memory Interface (ATMI)
        ROCr Debug Agent
        ROCm Code Object Manager
        ROC Profiler
        ROC Tracer
        Radeon Compute Profiler
        Example Applications:
            HCC Examples
            HIP Examples
    ROCm Libraries
        rocBLAS
        hipBLAS
        rocFFT
        rocRAND
        rocSPARSE
        hipSPARSE
        rocALUTION
        MIOpenGEMM
        MIOpen
        rocThrust
        ROCm SMI Lib
        RCCL
        MIVisionX
        hipCUB
```
https://github.com/justxi/rocm
https://github.com/justxi/vulkan
```

*  dev-libs/rocm-comgr
      Latest version available: 2.10.0
      Latest version installed: 2.10.0
      Size of files: 86 KiB
      Homepage:      https://github.com/RadeonOpenCompute/ROCm-CompilerSupport
      Description:   Radeon Open Compute Code Object Manager
      License:       MIT

*  dev-libs/rocm-device-libs
      Latest version available: 2.10.0
      Latest version installed: 2.10.0
      Size of files: 223 KiB
      Homepage:      https://github.com/RadeonOpenCompute/ROCm-Device-Libs
      Description:   Radeon Open Compute Device Libraries
      License:       MIT

*  dev-libs/rocm-hostcall
      Latest version available: 2.7.0
      Latest version installed: 2.7.0
      Size of files: 1,466 KiB
      Homepage:      https://github.com/RadeonOpenCompute/ROCm-CompilerSupport
      Description:   Radeon Open Compute hostcall API
      License:       MIT

*  dev-libs/rocm-opencl-driver
      Latest version available: 2.7.0
      Latest version installed: [ Not Installed ]
      Size of files: 21 KiB
      Homepage:      https://github.com/RadeonOpenCompute/ROCm-OpenCL-Driver
      Description:   Radeon Open Compute OpenCL Compiler Tool Driver
      License:       MIT

*  dev-libs/rocm-opencl-runtime
      Latest version available: 2.10.0
      Latest version installed: 2.10.0
      Size of files: 1,005 KiB
      Homepage:      https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime
      Description:   Radeon Open Compute OpenCL Compatible Runtime
      License:       Apache-2.0 MIT

*  dev-libs/rocm-smi-lib
      Latest version available: 9999
      Latest version installed: [ Not Installed ]
      Size of files: 0 KiB
      Homepage:      https://github.com/RadeonOpenCompute/rocm_smi_lib
      Description:   User space interface for applications to monitor and control GPU applications.
      License:

*  dev-util/rocm-clang-ocl
      Latest version available: 2.10.0
      Latest version installed: 2.10.0
      Size of files: 3 KiB
      Homepage:      https://github.com/RadeonOpenCompute/clang-ocl.git
      Description:   OpenCL compilation with clang compiler
      License:

*  dev-util/rocm-cmake
      Latest version available: 2.10.0
      Latest version installed: 2.10.0
      Size of files: 14 KiB
      Homepage:      https://github.com/RadeonOpenCompute/rocm-cmake
      Description:   Radeon Open Compute CMake Modules
      License:       MIT

*  dev-util/rocm-smi
      Latest version available: 2.9.0
      Latest version installed: 2.9.0
      Size of files: 42 KiB
      Homepage:      https://github.com/RadeonOpenCompute/ROC-smi
      Description:   ROCm System Management Interface
      License:

*  dev-util/rocminfo
      Latest version available: 2.10.0-r1
      Latest version installed: 2.10.0-r1
      Size of files: 15 KiB
      Homepage:      https://github.com/RadeonOpenCompute/rocminfo
      Description:   ROCm Application for Reporting System Info
      License:       MIT
```

3) appears to work


```
jesush@localhost ~ $ rocminfo
ROCk module is loaded
Failed to get user name to check for video group membership
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
  Name:                    Intel(R) Core(TM) i7-8705G CPU @ 3.10GHz
  Marketing Name:          Intel(R) Core(TM) i7-8705G CPU @ 3.10GHz
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
  Max Clock Freq. (MHz):   4100
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            8
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    15883472(0xf25cd0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    15883472(0xf25cd0) KB
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
  Marketing Name:          Polaris 22 XL [Radeon RX Vega M GL]
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
  Chip ID:                 26958(0x694e)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1011
  BDFID:                   256
  Internal Node ID:        1
  Compute Unit:            20
  SIMDs per CU:            4
  Shader Engines:          4
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
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
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

---

### 评论 #40 — maxharicot (2020-01-12T18:31:28Z)

I am trying to build ROCm on my Solus machine with a Vega M.  So far I have build everything in the following repo :
https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime
https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface
https://github.com/RadeonOpenCompute/ROCR-Runtime/
https://github.com/RadeonOpenCompute/rocminfo/
and installed the files :
libhsa-runtime64.so
libhsakmt.so
libOpenCL.so
libamdocl64.so
amdocl64.icd

I just want to run OpenCL application (darktable in fact).

When I run the clinfo build with ROCm-OpenCL-Runtime I get :
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP.internal (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

```

When I run rocminfo
```
ROCk module is loaded
Failed to get user name to check for video group membership
hsa api call failure at: /home/build/YPKG/root/rocminfo/build/rocminfo-roc-3.0.0/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

Am I missing something to build or files to install ?

---

### 评论 #41 — securelyfitz (2020-01-12T23:06:56Z)

are you a member of the group 'video'?
to find out:
`groups`
if not, run:
`sudo usermod -a -G video $LOGNAME`
you may have to logout completely and log back in for your groups to be updated so that running `groups` shows video.

---

### 评论 #42 — maxharicot (2020-01-13T08:55:05Z)

@securelyfitz Yes my user is in video.

---

### 评论 #43 — JLTastet (2020-06-07T16:35:30Z)

> @phush0 Out of curiosity, which distro are you using? If I can get Vega M to work on Fedora, I'll make sure to test Darktable!

I can report that ROCm 3.5 now works fine with my Vega M GPU on Fedora 32 :tada:

I mostly followed [these instructions from issue #567](https://github.com/RadeonOpenCompute/ROCm/issues/567#issuecomment-621408488), and set `amdgpu.runpm=0` as suggested above. In addition, I had to add myself to the `render` group (I also added myself to `video`, just in case).

I was still missing the image support. So I tried to follow these instructions: https://discuss.pixls.us/t/how-to-install-amd-rocm-for-opencl-support/16212, more specifically steps 3 and 4. Not sure what exactly did the trick, but Darktable now recognizes and uses my GPU!

EDIT (January 2021): this fix does not seem to work any more.

---

### 评论 #44 — ROCmSupport (2021-01-07T10:44:12Z)

Thank you all for your trials and support.
Finally issue is resolved with amdgpu.runpm=0 parameter. 
Thanks to know.
There is no offifical support of Vega M till today and not sure about future plans.
Thank you.

---
