# amdgpu XXXX:XX:XX.X: kfd not supported on this ASIC (RX 550, ROCm 1.9, Linux 4.19, amdgpu)

> **Issue #539**
> **状态**: closed
> **创建时间**: 2018-09-16T13:35:51Z
> **更新时间**: 2019-01-08T15:45:23Z
> **关闭时间**: 2018-09-17T14:40:34Z
> **作者**: mdPlusPlus
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/539

## 描述

First of all thanks for releasing a ROCm version compatible with mainline kfd. Now I can finally use my Vega64 with newer kernels.

However, my problem occurs when I try to use my RX ~~560~~ 550 as an OpenCL device.  
Apparently mainline kernels do not have kfd support for these cards (yet?).

Is there a workaround for using a RX ~~560~~ 550 with ROCm?

My system details:  
Ubuntu 18.04  
Kernel 4.19-rc3
ROCm 1.9.211
Using `amdgpu` as driver

```
$ dmesg | grep -i kfd
[    1.549222] kfd kfd: Initialized module
[    1.549574] amdgpu XXXX:XX:XX.X: kfd not supported on this ASIC
```
```
$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104
```
```
$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```

---

## 评论 (8 条)

### 评论 #1 — jlgreathouse (2018-09-16T19:59:50Z)

Could you please show me the output of the following commands:
- `lspci -v`
- `lspci -n`
- `lspci -tn`
- `dkms status`

In addition, just to verify some things:
Does your error message actually say "XXXX:XX:XX.X", or did you replace those numbers yourself?
Are you running in secure boot mode?

---

### 评论 #2 — mdPlusPlus (2018-09-17T10:39:49Z)

>Does your error message actually say "XXXX:XX:XX.X"

No, it says `0000:2d:00.0` but I retracted it since it is nonrelevant information.

```
$ lspci -vnn
00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Root Complex [1022:1450]
	Subsystem: ASRock Incorporation Family 17h (Models 00h-0fh) Root Complex [1849:1450]
	Flags: fast devsel

00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) I/O Memory Management Unit [1022:1451]
	Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) I/O Memory Management Unit [1022:1451]
	Flags: fast devsel, IRQ 27
	Capabilities: <access denied>

00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge [1022:1452]
	Flags: fast devsel

00:01.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe GPP Bridge [1022:1453] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 28
	Bus: primary=00, secondary=03, subordinate=2c, sec-latency=0
	I/O behind bridge: 0000c000-0000dfff
	Memory behind bridge: fcc00000-fd0fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge [1022:1452]
	Flags: fast devsel

00:03.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge [1022:1452]
	Flags: fast devsel

00:03.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe GPP Bridge [1022:1453] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 29
	Bus: primary=00, secondary=2d, subordinate=2d, sec-latency=0
	I/O behind bridge: 0000f000-0000ffff
	Memory behind bridge: fd700000-fd7fffff
	Prefetchable memory behind bridge: 00000000e0000000-00000000f01fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:03.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe GPP Bridge [1022:1453] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 30
	Bus: primary=00, secondary=2e, subordinate=30, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: fd400000-fd5fffff
	Prefetchable memory behind bridge: 00000000c0000000-00000000d01fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:04.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge [1022:1452]
	Flags: fast devsel

00:07.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge [1022:1452]
	Flags: fast devsel

00:07.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Internal PCIe GPP Bridge 0 to Bus B [1022:1454] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 31
	Bus: primary=00, secondary=31, subordinate=31, sec-latency=0
	Memory behind bridge: fd100000-fd3fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge [1022:1452]
	Flags: fast devsel

00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Internal PCIe GPP Bridge 0 to Bus B [1022:1454] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 33
	Bus: primary=00, secondary=32, subordinate=32, sec-latency=0
	Memory behind bridge: fd600000-fd6fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 59)
	Subsystem: ASRock Incorporation FCH SMBus Controller [1849:ffff]
	Flags: 66MHz, medium devsel
	Kernel driver in use: piix4_smbus
	Kernel modules: i2c_piix4, sp5100_tco

00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
	Subsystem: ASRock Incorporation FCH LPC Bridge [1849:ffff]
	Flags: bus master, 66MHz, medium devsel, latency 0

00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 0 [1022:1460]
	Flags: fast devsel

00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 1 [1022:1461]
	Flags: fast devsel

00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 2 [1022:1462]
	Flags: fast devsel

00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 3 [1022:1463]
	Flags: fast devsel
	Kernel driver in use: k10temp
	Kernel modules: k10temp

00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 4 [1022:1464]
	Flags: fast devsel

00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 5 [1022:1465]
	Flags: fast devsel

00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 6 [1022:1466]
	Flags: fast devsel

00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 7 [1022:1467]
	Flags: fast devsel

03:00.0 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:43b9] (rev 02) (prog-if 30 [XHCI])
	Subsystem: ASMedia Technology Inc. Device [1b21:1142]
	Flags: bus master, fast devsel, latency 0, IRQ 48
	Memory at fd0a0000 (64-bit, non-prefetchable) [size=32K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

03:00.1 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] Device [1022:43b5] (rev 02) (prog-if 01 [AHCI 1.0])
	Subsystem: ASMedia Technology Inc. Device [1b21:1062]
	Flags: bus master, fast devsel, latency 0, IRQ 58
	Memory at fd080000 (32-bit, non-prefetchable) [size=128K]
	Expansion ROM at fd000000 [disabled] [size=512K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

03:00.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:43b0] (rev 02) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 34
	Bus: primary=03, secondary=1d, subordinate=2c, sec-latency=0
	I/O behind bridge: 0000c000-0000dfff
	Memory behind bridge: fcc00000-fcffffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

1d:00.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] 300 Series Chipset PCIe Port [1022:43b4] (rev 02) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 36
	Bus: primary=1d, secondary=1e, subordinate=1e, sec-latency=0
	Capabilities: <access denied>
	Kernel driver in use: pcieport

1d:02.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] 300 Series Chipset PCIe Port [1022:43b4] (rev 02) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 37
	Bus: primary=1d, secondary=20, subordinate=20, sec-latency=0
	I/O behind bridge: 0000d000-0000dfff
	Memory behind bridge: fcf00000-fcffffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

1d:03.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] 300 Series Chipset PCIe Port [1022:43b4] (rev 02) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 38
	Bus: primary=1d, secondary=21, subordinate=2b, sec-latency=0
	I/O behind bridge: 0000c000-0000cfff
	Memory behind bridge: fcc00000-fcefffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

1d:04.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] 300 Series Chipset PCIe Port [1022:43b4] (rev 02) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 39
	Bus: primary=1d, secondary=2c, subordinate=2c, sec-latency=0
	Capabilities: <access denied>
	Kernel driver in use: pcieport

20:00.0 SATA controller [0106]: ASMedia Technology Inc. ASM1062 Serial ATA Controller [1b21:0612] (rev 02) (prog-if 01 [AHCI 1.0])
	Subsystem: ASRock Incorporation Motherboard [1849:0612]
	Flags: bus master, fast devsel, latency 0, IRQ 5
	I/O ports at d050 [size=8]
	I/O ports at d040 [size=4]
	I/O ports at d030 [size=8]
	I/O ports at d020 [size=4]
	I/O ports at d000 [size=32]
	Memory at fcf00000 (32-bit, non-prefetchable) [size=512]
	Capabilities: <access denied>
	Kernel driver in use: vfio-pci
	Kernel modules: ahci

21:00.0 PCI bridge [0604]: ASMedia Technology Inc. Device [1b21:1184] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 40
	Bus: primary=21, secondary=26, subordinate=2b, sec-latency=0
	I/O behind bridge: 0000c000-0000cfff
	Memory behind bridge: fcc00000-fcefffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

26:01.0 PCI bridge [0604]: ASMedia Technology Inc. Device [1b21:1184] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 41
	Bus: primary=26, secondary=27, subordinate=27, sec-latency=0
	Memory behind bridge: fce00000-fcefffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

26:03.0 PCI bridge [0604]: ASMedia Technology Inc. Device [1b21:1184] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 42
	Bus: primary=26, secondary=28, subordinate=28, sec-latency=0
	Capabilities: <access denied>
	Kernel driver in use: pcieport

26:05.0 PCI bridge [0604]: ASMedia Technology Inc. Device [1b21:1184] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 43
	Bus: primary=26, secondary=2a, subordinate=2a, sec-latency=0
	I/O behind bridge: 0000c000-0000cfff
	Memory behind bridge: fcd00000-fcdfffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

26:07.0 PCI bridge [0604]: ASMedia Technology Inc. Device [1b21:1184] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 44
	Bus: primary=26, secondary=2b, subordinate=2b, sec-latency=0
	Memory behind bridge: fcc00000-fccfffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

27:00.0 Network controller [0280]: Intel Corporation Dual Band Wireless-AC 3168NGW [Stone Peak] [8086:24fb] (rev 10)
	Subsystem: Intel Corporation Device [8086:2110]
	Flags: bus master, fast devsel, latency 0, IRQ 66
	Memory at fce00000 (64-bit, non-prefetchable) [size=8K]
	Capabilities: <access denied>
	Kernel driver in use: iwlwifi
	Kernel modules: iwlwifi

2a:00.0 Ethernet controller [0200]: Intel Corporation I211 Gigabit Network Connection [8086:1539] (rev 03)
	Subsystem: ASRock Incorporation I211 Gigabit Network Connection [1849:1539]
	Flags: bus master, fast devsel, latency 0, IRQ 35
	Memory at fcd00000 (32-bit, non-prefetchable) [size=128K]
	I/O ports at c000 [size=32]
	Memory at fcd20000 (32-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: igb
	Kernel modules: igb

2b:00.0 USB controller [0c03]: Fresco Logic FL1100 USB 3.0 Host Controller [1b73:1100] (rev 10) (prog-if 30 [XHCI])
	Subsystem: Fresco Logic FL1100 USB 3.0 Host Controller [1b73:1100]
	Flags: bus master, fast devsel, latency 0, IRQ 49
	Memory at fcc00000 (64-bit, non-prefetchable) [size=64K]
	Memory at fcc11000 (64-bit, non-prefetchable) [size=4K]
	Memory at fcc10000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

2d:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Polaris12 [1002:699f] (rev c7) (prog-if 00 [VGA controller])
	Subsystem: XFX Pine Group Inc. Lexa PRO [Radeon RX 550] [1682:9550]
	Flags: bus master, fast devsel, latency 0, IRQ 62
	Memory at e0000000 (64-bit, prefetchable) [size=256M]
	Memory at f0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at f000 [size=256]
	Memory at fd700000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

2d:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:aae0]
	Subsystem: XFX Pine Group Inc. Device [1682:aae0]
	Flags: bus master, fast devsel, latency 0, IRQ 68
	Memory at fd760000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

2e:00.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:1470] (rev c1) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 46
	Memory at fd500000 (32-bit, non-prefetchable) [size=16K]
	Bus: primary=2e, secondary=2f, subordinate=30, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: fd400000-fd4fffff
	Prefetchable memory behind bridge: 00000000c0000000-00000000d01fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

2f:00.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:1471] (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 47
	Bus: primary=2f, secondary=30, subordinate=30, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: fd400000-fd4fffff
	Prefetchable memory behind bridge: 00000000c0000000-00000000d01fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

30:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Vega [Radeon RX Vega] [1002:687f] (rev c1) (prog-if 00 [VGA controller])
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XT [Radeon RX Vega 64] [1002:6b76]
	Flags: fast devsel, IRQ 5
	Memory at c0000000 (64-bit, prefetchable) [disabled] [size=256M]
	Memory at d0000000 (64-bit, prefetchable) [disabled] [size=2M]
	I/O ports at e000 [disabled] [size=256]
	Memory at fd400000 (32-bit, non-prefetchable) [disabled] [size=512K]
	Expansion ROM at fd480000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: vfio-pci
	Kernel modules: amdgpu

30:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:aaf8]
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:aaf8]
	Flags: fast devsel, IRQ 4
	Memory at fd4a0000 (32-bit, non-prefetchable) [disabled] [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: vfio-pci
	Kernel modules: snd_hda_intel

31:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Device [1022:145a]
	Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:145a]
	Flags: fast devsel
	Capabilities: <access denied>

31:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Platform Security Processor [1022:1456]
	Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) Platform Security Processor [1022:1456]
	Flags: bus master, fast devsel, latency 0, IRQ 63
	Memory at fd200000 (32-bit, non-prefetchable) [size=1M]
	Memory at fd300000 (32-bit, non-prefetchable) [size=8K]
	Capabilities: <access denied>
	Kernel driver in use: ccp
	Kernel modules: ccp

31:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) USB 3.0 Host Controller [1022:145c] (prog-if 30 [XHCI])
	Subsystem: ASRock Incorporation Family 17h (Models 00h-0fh) USB 3.0 Host Controller [1849:ffff]
	Flags: bus master, fast devsel, latency 0, IRQ 51
	Memory at fd100000 (64-bit, non-prefetchable) [size=1M]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

32:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Device [1022:1455]
	Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1455]
	Flags: fast devsel
	Capabilities: <access denied>

32:00.2 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 51) (prog-if 01 [AHCI 1.0])
	Subsystem: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901]
	Flags: bus master, fast devsel, latency 0, IRQ 60
	Memory at fd608000 (32-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

32:00.3 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) HD Audio Controller [1022:1457]
	Subsystem: ASRock Incorporation Family 17h (Models 00h-0fh) HD Audio Controller [1849:1220]
	Flags: bus master, fast devsel, latency 0, IRQ 70
	Memory at fd600000 (32-bit, non-prefetchable) [size=32K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

```

```
$ lspci -tvn
-[0000:00]-+-00.0  1022:1450
           +-00.2  1022:1451
           +-01.0  1022:1452
           +-01.3-[03-2c]--+-00.0  1022:43b9
           |               +-00.1  1022:43b5
           |               \-00.2-[1d-2c]--+-00.0-[1e]--
           |                               +-02.0-[20]----00.0  1b21:0612
           |                               +-03.0-[21-2b]----00.0-[26-2b]--+-01.0-[27]----00.0  8086:24fb
           |                               |                               +-03.0-[28]--
           |                               |                               +-05.0-[2a]----00.0  8086:1539
           |                               |                               \-07.0-[2b]----00.0  1b73:1100
           |                               \-04.0-[2c]--
           +-02.0  1022:1452
           +-03.0  1022:1452
           +-03.1-[2d]--+-00.0  1002:699f
           |            \-00.1  1002:aae0
           +-03.2-[2e-30]----00.0-[2f-30]----00.0-[30]--+-00.0  1002:687f
           |                                            \-00.1  1002:aaf8
           +-04.0  1022:1452
           +-07.0  1022:1452
           +-07.1-[31]--+-00.0  1022:145a
           |            +-00.2  1022:1456
           |            \-00.3  1022:145c
           +-08.0  1022:1452
           +-08.1-[32]--+-00.0  1022:1455
           |            +-00.2  1022:7901
           |            \-00.3  1022:1457
           +-14.0  1022:790b
           +-14.3  1022:790e
           +-18.0  1022:1460
           +-18.1  1022:1461
           +-18.2  1022:1462
           +-18.3  1022:1463
           +-18.4  1022:1464
           +-18.5  1022:1465
           +-18.6  1022:1466
           \-18.7  1022:1467
```

```
$ dkms status
amdgpu, 1.9-211: added
```

~~Could this be firmware related as in #527?~~

---

### 评论 #3 — jlgreathouse (2018-09-17T14:40:34Z)

Hi @mdPlusPlus 

Thanks for the information. Your GPU is a Polaris 12/Lexa GPU, which is unfortunately not currently on our[ list of supported GPUs](https://github.com/RadeonOpenCompute/ROCm/blob/roc-1.9.0/README.md#supported-gpus). The `amdkfd` ROCK driver and the Thunk (ROCT) do not currently contain support for this device.

If you're interested in trying to build your own kernel driver and Thunk, you can try applying patches akin to the following PRs:
- https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/pull/15/commits/481e08af9bca760adfb49d5dcecf10617daab0fa
- https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/pull/33/commits/f5be011ca82271fbe4b1c0cd290e3d74f7d79553

I can't guarantee that these will work, as I haven't tested them. But if you're interested in trying ROCm on your GPU, we would be interested to see if these work for you. :)

---

### 评论 #4 — mdPlusPlus (2018-09-18T09:56:43Z)

Are you aware of any plans to support this in `amdkfd` in the future? Any estimates?

Also, I've just realized that I am an idiot and that I don't have a RX 560 (Polaris 21) as stated in the title, but instead a RX 550 as you have correctly seen from my logs.

---

### 评论 #5 — jlgreathouse (2018-09-18T13:29:50Z)

Hi @mdPlusPlus 

Unfortunately, I can't really give you a timeline about whether Polaris 12 will be officially supported in ROCm any time soon. My gut feeling tells me that the patches you see above aren't too complicated and thus ought to be relatively simple to implement. However, the ROCm team has not had time to validate them. As such, if there are problems that would need deeper knowledge to fix, I can't tell you when those would make it onto our development cycle.

---

### 评论 #6 — jlgreathouse (2018-12-22T00:43:22Z)

@mdPlusPlus I've switched up the tag because "Polaris 12" should be be enabled in ROCm 2.0. I just sat down and tested a batch of OpenCL, HCC, and HIP applications with a Polaris 12 board, and things appear to be working as expected.

Note that you will need to be on a distro that supports our rock-dkms driver to have this support, since the last bit that needed to be in place was a driver change. Support for this is in the `amd-staging-next` drivers, but will not hit upstream Linux until post-4.20.

---

### 评论 #7 — mdPlusPlus (2019-01-05T20:16:27Z)

>post-4.20

Does this mean 4.21 or is it a more general "sometime in the future"?
And will the `rocm-opencl` package be sufficient to run OpenCL tasks?

---

### 评论 #8 — jlgreathouse (2019-01-08T15:45:22Z)

Hi @mdPlusPlus 

The patch for Polaris 12 [was pulled into the Linux master branch](https://github.com/torvalds/linux/commit/4971f090aa7f6ce5daa094ce4334f6618f93a7eb) in the middle of December. As such, I suspect it will be in 5.0. However, upstream being upstream, it's somewhat out of our hands if some part of this ends up being rolled back or not included for reasons outside of our control.

You can see more about the required packages for an OpenCL-only installation [here](https://github.com/RadeonOpenCompute/ROCm#performing-an-opencl-only-installation-of-rocm). You'll see that those directions include the `rock-dkms` driver. If you want to use an upstream driver instead, please see [these directions](https://github.com/RadeonOpenCompute/ROCm#using-debian-based-rocm-with-upstream-kernel-drivers). The [following directions](https://github.com/RadeonOpenCompute/ROCm#rocm-binary-package-structure) show information about our package structure so that you can see what packages you may need to install for various combinations of kernel support and what user-land programs we have. We do not plan on adding a comprehensive list of installation directions for all possible permutations of these packages.

---
