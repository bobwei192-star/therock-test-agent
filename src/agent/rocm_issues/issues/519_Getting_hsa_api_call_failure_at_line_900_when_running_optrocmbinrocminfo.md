# Getting hsa api call failure at line 900 when running /opt/rocm/bin/rocminfo 

> **Issue #519**
> **状态**: closed
> **创建时间**: 2018-09-01T18:35:00Z
> **更新时间**: 2018-09-17T23:27:01Z
> **关闭时间**: 2018-09-04T18:22:02Z
> **作者**: babujoym
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/519

## 描述

I have installed rocm-dkms in my ubuntu os 16.04 LTS as per the instructions.

When I run the command /opt/rocm/bin/rocminfo I am getting the error
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

When I run /opt/rocm/opencl/bin/x86_64/clinfo, I am getting the error
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)

uname -a gives:
Linux babu-Inspiron-5548 4.15.0-33-generic #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

I am getting the below error messages in some the crash files that got generated today.
In _usr_share_apport_apport-gtk.1000.crash

I am getting the error 
```
PythonArgs: ['/usr/share/apport/apport-gtk']
Traceback:
 Traceback (most recent call last):
   File "/usr/share/apport/apport-gtk", line 597, in <module>
     app.run_argv()
   File "/usr/lib/python3/dist-packages/apport/ui.py", line 688, in run_argv
     return self.run_crashes()
   File "/usr/lib/python3/dist-packages/apport/ui.py", line 239, in run_crashes
     logind_session[1] > self.report.get_timestamp():
 TypeError: unorderable types: float() > NoneType()
UserGroups: adm cdrom dip lpadmin plugdev sambashare sudo video
_LogindSession: c2
```




Could you please help


---

## 评论 (5 条)

### 评论 #1 — jlgreathouse (2018-09-02T18:35:11Z)

This error in rocminfo can happen for a large number of reasons, because all it basically means is "ROCm is not working successfully on this system".

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

### 评论 #2 — rkothako (2018-09-03T03:25:31Z)

Hi @jlgreathouse 
It will be good if we add the below as part of ROCm wiki page for sanity checks.

uname -a
dkms status
lsmod | grep amdgpu
lsmod | grep amdkfd
groups
lspci | grep VGA
lspci -vvv
lspci -tv
lspci -n
After a reboot: dmesg

---

### 评论 #3 — babujoym (2018-09-04T18:11:08Z)

Sorry, I was out for two days.
Thank you for not closing the issue.

Below are the details
```
babu@babu-Inspiron-5548:~$ uname -a
Linux babu-Inspiron-5548 4.15.0-33-generic #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```
```
babu@babu-Inspiron-5548:~$ dkms status
amdgpu, 1.8-199, 4.15.0-33-generic, x86_64: installed
```
```
babu@babu-Inspiron-5548:~$ lsmod | grep amdgpu
babu@babu-Inspiron-5548:~$ lsmod | grep amdkfd
babu@babu-Inspiron-5548:~$ groups
babu adm cdrom sudo dip video plugdev lpadmin sambashare
babu@babu-Inspiron-5548:~$ lspci | grep VGA
00:02.0 VGA compatible controller: Intel Corporation Broadwell-U Integrated Graphics (rev 09)
```
```
babu@babu-Inspiron-5548:~$ lspci -vvv
00:00.0 Host bridge: Intel Corporation Broadwell-U Host Bridge -OPI (rev 09)
	Subsystem: Dell Broadwell-U Host Bridge -OPI
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
	Latency: 0
	Capabilities: <access denied>
	Kernel driver in use: bdw_uncore

00:02.0 VGA compatible controller: Intel Corporation Broadwell-U Integrated Graphics (rev 09) (prog-if 00 [VGA controller])
	Subsystem: Dell Broadwell-U Integrated Graphics
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 49
	Region 0: Memory at d0000000 (64-bit, non-prefetchable) [size=16M]
	Region 2: Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Region 4: I/O ports at 5000 [size=64]
	[virtual] Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: i915
	Kernel modules: i915

00:03.0 Audio device: Intel Corporation Broadwell-U Audio Controller (rev 09)
	Subsystem: Dell Broadwell-U Audio Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 53
	Region 0: Memory at d2310000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

00:14.0 USB controller: Intel Corporation Wildcat Point-LP USB xHCI Controller (rev 03) (prog-if 30 [XHCI])
	Subsystem: Dell Wildcat Point-LP USB xHCI Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 46
	Region 0: Memory at d2300000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

00:16.0 Communication controller: Intel Corporation Wildcat Point-LP MEI Controller #1 (rev 03)
	Subsystem: Dell Wildcat Point-LP MEI Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 50
	Region 0: Memory at d231b000 (64-bit, non-prefetchable) [size=32]
	Capabilities: <access denied>
	Kernel driver in use: mei_me
	Kernel modules: mei_me

00:1b.0 Audio device: Intel Corporation Wildcat Point-LP High Definition Audio Controller (rev 03)
	Subsystem: Dell Wildcat Point-LP High Definition Audio Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 64, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 52
	Region 0: Memory at d2314000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

00:1c.0 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #1 (rev e3) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 42
	Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: fff00000-000fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1c.2 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #3 (rev e3) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin C routed to IRQ 43
	Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
	I/O behind bridge: 00004000-00004fff
	Memory behind bridge: d2200000-d22fffff
	Prefetchable memory behind bridge: 00000000d2000000-00000000d20fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1c.3 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #4 (rev e3) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin D routed to IRQ 44
	Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
	I/O behind bridge: 0000f000-00000fff
	Memory behind bridge: d2100000-d21fffff
	Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1c.4 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #5 (rev e3) (prog-if 00 [Normal decode])
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 45
	Bus: primary=00, secondary=04, subordinate=09, sec-latency=0
	I/O behind bridge: 00003000-00003fff
	Memory behind bridge: d1000000-d1ffffff
	Prefetchable memory behind bridge: 00000000b0000000-00000000bfffffff
	Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
	BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
		PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
	Capabilities: <access denied>
	Kernel driver in use: pcieport
	Kernel modules: shpchp

00:1d.0 USB controller: Intel Corporation Wildcat Point-LP USB EHCI Controller (rev 03) (prog-if 20 [EHCI])
	Subsystem: Dell Wildcat Point-LP USB EHCI Controller
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 23
	Region 0: Memory at d2319000 (32-bit, non-prefetchable) [size=1K]
	Capabilities: <access denied>
	Kernel driver in use: ehci-pci

00:1f.0 ISA bridge: Intel Corporation Wildcat Point-LP LPC Controller (rev 03)
	Subsystem: Dell Wildcat Point-LP LPC Controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Capabilities: <access denied>
	Kernel driver in use: lpc_ich
	Kernel modules: lpc_ich

00:1f.2 SATA controller: Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode] (rev 03) (prog-if 01 [AHCI 1.0])
	Subsystem: Dell Wildcat Point-LP SATA Controller [AHCI Mode]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin B routed to IRQ 48
	Region 0: I/O ports at 5088 [size=8]
	Region 1: I/O ports at 5094 [size=4]
	Region 2: I/O ports at 5080 [size=8]
	Region 3: I/O ports at 5090 [size=4]
	Region 4: I/O ports at 5060 [size=32]
	Region 5: Memory at d2318000 (32-bit, non-prefetchable) [size=2K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

00:1f.3 SMBus: Intel Corporation Wildcat Point-LP SMBus Controller (rev 03)
	Subsystem: Dell Wildcat Point-LP SMBus Controller
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap- 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin C routed to IRQ 255
	Region 0: Memory at d231a000 (64-bit, non-prefetchable) [size=256]
	Region 4: I/O ports at 5040 [size=32]
	Kernel modules: i2c_i801

02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller (rev 07)
	Subsystem: Dell RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 18
	Region 0: I/O ports at 4000 [size=256]
	Region 2: Memory at d2200000 (64-bit, non-prefetchable) [size=4K]
	Region 4: Memory at d2000000 (64-bit, prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: r8169
	Kernel modules: r8169

03:00.0 Network controller: Intel Corporation Wireless 7260 (rev bb)
	Subsystem: Intel Corporation Dual Band Wireless-AC 7260
	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 51
	Region 0: Memory at d2100000 (64-bit, non-prefetchable) [size=8K]
	Capabilities: <access denied>
	Kernel driver in use: iwlwifi
	Kernel modules: iwlwifi

04:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Opal XT [Radeon R7 M265]
	Subsystem: Dell Opal XT [Radeon R7 M265]
	Physical Slot: 4
	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 255
	Region 0: Memory at b0000000 (64-bit, prefetchable) [disabled] [size=256M]
	Region 2: Memory at d1000000 (64-bit, non-prefetchable) [disabled] [size=256K]
	Region 4: I/O ports at 3000 [disabled] [size=256]
	Expansion ROM at d1040000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel modules: radeon, amdgpu
```
```
babu@babu-Inspiron-5548:~$ lspci -tv
-[0000:00]-+-00.0  Intel Corporation Broadwell-U Host Bridge -OPI
           +-02.0  Intel Corporation Broadwell-U Integrated Graphics
           +-03.0  Intel Corporation Broadwell-U Audio Controller
           +-14.0  Intel Corporation Wildcat Point-LP USB xHCI Controller
           +-16.0  Intel Corporation Wildcat Point-LP MEI Controller #1
           +-1b.0  Intel Corporation Wildcat Point-LP High Definition Audio Controller
           +-1c.0-[01]--
           +-1c.2-[02]----00.0  Realtek Semiconductor Co., Ltd. RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller
           +-1c.3-[03]----00.0  Intel Corporation Wireless 7260
           +-1c.4-[04-09]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Opal XT [Radeon R7 M265]
           +-1d.0  Intel Corporation Wildcat Point-LP USB EHCI Controller
           +-1f.0  Intel Corporation Wildcat Point-LP LPC Controller
           +-1f.2  Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode]
           \-1f.3  Intel Corporation Wildcat Point-LP SMBus Controller

```

```
babu@babu-Inspiron-5548:~$ lspci -n
00:00.0 0600: 8086:1604 (rev 09)
00:02.0 0300: 8086:1616 (rev 09)
00:03.0 0403: 8086:160c (rev 09)
00:14.0 0c03: 8086:9cb1 (rev 03)
00:16.0 0780: 8086:9cba (rev 03)
00:1b.0 0403: 8086:9ca0 (rev 03)
00:1c.0 0604: 8086:9c90 (rev e3)
00:1c.2 0604: 8086:9c94 (rev e3)
00:1c.3 0604: 8086:9c96 (rev e3)
00:1c.4 0604: 8086:9c98 (rev e3)
00:1d.0 0c03: 8086:9ca6 (rev 03)
00:1f.0 0601: 8086:9cc3 (rev 03)
00:1f.2 0106: 8086:9c83 (rev 03)
00:1f.3 0c05: 8086:9ca2 (rev 03)
02:00.0 0200: 10ec:8136 (rev 07)
03:00.0 0280: 8086:08b1 (rev bb)
04:00.0 0380: 1002:6604
```


```
babu@babu-Inspiron-5548:~$ dmesg
[    0.000000] microcode: microcode updated early to revision 0x2b, date = 2018-03-22
[    0.000000] Linux version 4.15.0-33-generic (buildd@lgw01-amd64-010) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)) #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 (Ubuntu 4.15.0-33.36~16.04.1-generic 4.15.18)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-33-generic root=UUID=4d4c507d-1915-458e-8b49-7670d50145b4 ro quiet splash vt.handoff=7
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
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000057fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000058000-0x0000000000058fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000059000-0x0000000000085fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000086000-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x000000008a7e9fff] usable
[    0.000000] BIOS-e820: [mem 0x000000008a7ea000-0x000000008b0e9fff] reserved
[    0.000000] BIOS-e820: [mem 0x000000008b0ea000-0x000000009c3eefff] usable
[    0.000000] BIOS-e820: [mem 0x000000009c3ef000-0x000000009cddefff] reserved
[    0.000000] BIOS-e820: [mem 0x000000009cddf000-0x000000009cfbefff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x000000009cfbf000-0x000000009cffefff] ACPI data
[    0.000000] BIOS-e820: [mem 0x000000009cfff000-0x000000009cffffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000e0000000-0x00000000efffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000feb00000-0x00000000feb03fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed10000-0x00000000fed19fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed1c000-0x00000000fed1ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ffa00000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000045effffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] e820: update [mem 0x8911e018-0x8912e057] usable ==> usable
[    0.000000] e820: update [mem 0x8911e018-0x8912e057] usable ==> usable
[    0.000000] e820: update [mem 0x89111018-0x8911d057] usable ==> usable
[    0.000000] e820: update [mem 0x89111018-0x8911d057] usable ==> usable
[    0.000000] e820: update [mem 0x89102018-0x89110a57] usable ==> usable
[    0.000000] e820: update [mem 0x89102018-0x89110a57] usable ==> usable
[    0.000000] extended physical RAM map:
[    0.000000] reserve setup_data: [mem 0x0000000000000000-0x0000000000057fff] usable
[    0.000000] reserve setup_data: [mem 0x0000000000058000-0x0000000000058fff] reserved
[    0.000000] reserve setup_data: [mem 0x0000000000059000-0x0000000000085fff] usable
[    0.000000] reserve setup_data: [mem 0x0000000000086000-0x000000000009ffff] reserved
[    0.000000] reserve setup_data: [mem 0x0000000000100000-0x0000000089102017] usable
[    0.000000] reserve setup_data: [mem 0x0000000089102018-0x0000000089110a57] usable
[    0.000000] reserve setup_data: [mem 0x0000000089110a58-0x0000000089111017] usable
[    0.000000] reserve setup_data: [mem 0x0000000089111018-0x000000008911d057] usable
[    0.000000] reserve setup_data: [mem 0x000000008911d058-0x000000008911e017] usable
[    0.000000] reserve setup_data: [mem 0x000000008911e018-0x000000008912e057] usable
[    0.000000] reserve setup_data: [mem 0x000000008912e058-0x000000008a7e9fff] usable
[    0.000000] reserve setup_data: [mem 0x000000008a7ea000-0x000000008b0e9fff] reserved
[    0.000000] reserve setup_data: [mem 0x000000008b0ea000-0x000000009c3eefff] usable
[    0.000000] reserve setup_data: [mem 0x000000009c3ef000-0x000000009cddefff] reserved
[    0.000000] reserve setup_data: [mem 0x000000009cddf000-0x000000009cfbefff] ACPI NVS
[    0.000000] reserve setup_data: [mem 0x000000009cfbf000-0x000000009cffefff] ACPI data
[    0.000000] reserve setup_data: [mem 0x000000009cfff000-0x000000009cffffff] usable
[    0.000000] reserve setup_data: [mem 0x00000000e0000000-0x00000000efffffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000feb00000-0x00000000feb03fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fed10000-0x00000000fed19fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fed1c000-0x00000000fed1ffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000ffa00000-0x00000000ffffffff] reserved
[    0.000000] reserve setup_data: [mem 0x0000000100000000-0x000000045effffff] usable
[    0.000000] efi: EFI v2.40 by Dell Inc.
[    0.000000] efi:  ESRT=0x9c665b18  SMBIOS=0x9c662000  ACPI 2.0=0x9cffe014 
[    0.000000] secureboot: Secure boot enabled
[    0.000000] Kernel is locked down from EFI secure boot; see man kernel_lockdown.7
[    0.000000] SMBIOS 2.7 present.
[    0.000000] DMI: Dell Inc. Inspiron 5548/079JDM, BIOS A04 05/15/2015
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x45f000 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: uncachable
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF uncachable
[    0.000000]   C0000-E7FFF write-protect
[    0.000000]   E8000-EFFFF write-combining
[    0.000000]   F0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 0000000000 mask 7800000000 write-back
[    0.000000]   1 base 009D000000 mask 7FFF000000 uncachable
[    0.000000]   2 base 009E000000 mask 7FFE000000 uncachable
[    0.000000]   3 base 00A0000000 mask 7FE0000000 uncachable
[    0.000000]   4 base 00C0000000 mask 7FC0000000 uncachable
[    0.000000]   5 disabled
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000]   8 disabled
[    0.000000]   9 disabled
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000000] total RAM covered: 31184M
[    0.000000] Found optimal setting for mtrr clean up
[    0.000000]  gran_size: 64K 	chunk_size: 64M 	num_reg: 7  	lose cover RAM: 0G
[    0.000000] e820: update [mem 0x9d000000-0xffffffff] usable ==> reserved
[    0.000000] e820: last_pfn = 0x9d000 max_arch_pfn = 0x400000000
[    0.000000] esrt: Reserving ESRT space from 0x000000009c665b18 to 0x000000009c665b50.
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [        (ptrval)] 80000 size 24576
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x16053d000, 0x16053dfff] PGTABLE
[    0.000000] BRK [0x16053e000, 0x16053efff] PGTABLE
[    0.000000] BRK [0x16053f000, 0x16053ffff] PGTABLE
[    0.000000] BRK [0x160540000, 0x160540fff] PGTABLE
[    0.000000] BRK [0x160541000, 0x160541fff] PGTABLE
[    0.000000] BRK [0x160542000, 0x160542fff] PGTABLE
[    0.000000] BRK [0x160543000, 0x160543fff] PGTABLE
[    0.000000] BRK [0x160544000, 0x160544fff] PGTABLE
[    0.000000] BRK [0x160545000, 0x160545fff] PGTABLE
[    0.000000] BRK [0x160546000, 0x160546fff] PGTABLE
[    0.000000] RAMDISK: [mem 0x3cbea000-0x3fffafff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x000000009CFFE014 000024 (v02 DELL  )
[    0.000000] ACPI: XSDT 0x000000009CFCA188 0000DC (v01 DELL   CL09     00000001      01000013)
[    0.000000] ACPI: FACP 0x000000009CFF5000 00010C (v05 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: DSDT 0x000000009CFDB000 014698 (v02 DELL   CL09     00000000 ASL  00040000)
[    0.000000] ACPI: FACS 0x000000009CFB7000 000040
[    0.000000] ACPI: SLIC 0x000000009CFFD000 000176 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: UEFI 0x000000009CFFC000 000236 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: UEFI 0x000000009CFFB000 000042 (v01 DELL   CL09     00000000 ASL  00040000)
[    0.000000] ACPI: MSDM 0x000000009CFFA000 000055 (v03 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: ASF! 0x000000009CFF9000 0000A5 (v32 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: ASPT 0x000000009CFF8000 000034 (v07 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: BOOT 0x000000009CFF7000 000028 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: DBGP 0x000000009CFF6000 000034 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: HPET 0x000000009CFF4000 000038 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: LPIT 0x000000009CFF3000 000094 (v01 DELL   CL09     00000000 ASL  00040000)
[    0.000000] ACPI: APIC 0x000000009CFF2000 00008C (v03 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: MCFG 0x000000009CFF1000 00003C (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: SLIC 0x000000009CFF0000 000176 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: SSDT 0x000000009CFD7000 00342F (v02 INSYDE HSW-LPT  00001000 ACPI 00040000)
[    0.000000] ACPI: SSDT 0x000000009CFD6000 000539 (v02 INSYDE HSW-LPT  00003000 ACPI 00040000)
[    0.000000] ACPI: SSDT 0x000000009CFD5000 000B74 (v02 INSYDE HSW-LPT  00003000 ACPI 00040000)
[    0.000000] ACPI: SSDT 0x000000009CFCF000 005C21 (v02 INSYDE HSW-LPT  00003000 ACPI 00040000)
[    0.000000] ACPI: SSDT 0x000000009CFCD000 001B1E (v01 INSYDE HSW-LPT  00001000 ACPI 00040000)
[    0.000000] ACPI: DMAR 0x000000009CFCC000 0000D4 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: CSRT 0x000000009CFCB000 0000C4 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: FPDT 0x000000009CFC9000 000044 (v01 DELL   CL09     00000002 ASL  00040000)
[    0.000000] ACPI: BGRT 0x000000009CFC8000 000038 (v01 DELL   CL09     00000001 ASL  00040000)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x000000045effffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x45efd5000-0x45effffff]
[    0.000000] tsc: Fast TSC calibration using PIT
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000045effffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x0000000000057fff]
[    0.000000]   node   0: [mem 0x0000000000059000-0x0000000000085fff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x000000008a7e9fff]
[    0.000000]   node   0: [mem 0x000000008b0ea000-0x000000009c3eefff]
[    0.000000]   node   0: [mem 0x000000009cfff000-0x000000009cffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000045effffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x000000045effffff]
[    0.000000] On node 0 totalpages: 4172404
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 22 pages reserved
[    0.000000]   DMA zone: 3972 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 9900 pages used for memmap
[    0.000000]   DMA32 zone: 633584 pages, LIFO batch:31
[    0.000000]   Normal zone: 55232 pages used for memmap
[    0.000000]   Normal zone: 3534848 pages, LIFO batch:31
[    0.000000] Reserved but unavailable: 99 pages
[    0.000000] tboot: non-0 tboot_addr but it is not of type E820_TYPE_RESERVED
[    0.000000] Reserving Intel graphics memory at 0x000000009e000000-0x000000009fffffff
[    0.000000] ACPI: PM-Timer IO Port: 0x1808
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-39
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x8086a201 base: 0xfed00000
[    0.000000] smpboot: Allowing 4 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x00058000-0x00058fff]
[    0.000000] PM: Registered nosave memory: [mem 0x00086000-0x0009ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x89102000-0x89102fff]
[    0.000000] PM: Registered nosave memory: [mem 0x89110000-0x89110fff]
[    0.000000] PM: Registered nosave memory: [mem 0x89111000-0x89111fff]
[    0.000000] PM: Registered nosave memory: [mem 0x8911d000-0x8911dfff]
[    0.000000] PM: Registered nosave memory: [mem 0x8911e000-0x8911efff]
[    0.000000] PM: Registered nosave memory: [mem 0x8912e000-0x8912efff]
[    0.000000] PM: Registered nosave memory: [mem 0x8a7ea000-0x8b0e9fff]
[    0.000000] PM: Registered nosave memory: [mem 0x9c3ef000-0x9cddefff]
[    0.000000] PM: Registered nosave memory: [mem 0x9cddf000-0x9cfbefff]
[    0.000000] PM: Registered nosave memory: [mem 0x9cfbf000-0x9cffefff]
[    0.000000] PM: Registered nosave memory: [mem 0x9d000000-0x9dffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x9e000000-0x9fffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xa0000000-0xdfffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xe0000000-0xefffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf0000000-0xfeafffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfeb00000-0xfeb03fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfeb04000-0xfebfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec01000-0xfed0ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed10000-0xfed19fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed1a000-0xfed1bfff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed1c000-0xfed1ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed20000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee01000-0xff9fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xffa00000-0xffffffff]
[    0.000000] e820: [mem 0xa0000000-0xdfffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] random: get_random_bytes called from start_kernel+0x99/0x51b with crng_init=0
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:4 nr_cpu_ids:4 nr_node_ids:1
[    0.000000] percpu: Embedded 46 pages/cpu @        (ptrval) s151552 r8192 d28672 u524288
[    0.000000] pcpu-alloc: s151552 r8192 d28672 u524288 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1 2 3 
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 4107186
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-33-generic root=UUID=4d4c507d-1915-458e-8b49-7670d50145b4 ro quiet splash vt.handoff=7
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 16229148K/16689616K available (12300K kernel code, 2469K rwdata, 4252K rodata, 2404K init, 2416K bss, 460468K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] Kernel/User page tables isolation: enabled
[    0.000000] ftrace: allocating 39127 entries in 153 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=4.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 524544, nr_irqs: 728, preallocated irqs: 16
[    0.000000] vt handoff: transparent VT on vt#7
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] ACPI: Core revision 20170831
[    0.000000] ACPI: 6 ACPI AML tables successfully acquired and loaded
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484882848 ns
[    0.000000] hpet clockevent registered
[    0.000000] APIC: Switch to symmetric I/O mode setup
[    0.000000] DMAR: Host address width 39
[    0.000000] DMAR: DRHD base: 0x000000fed90000 flags: 0x0
[    0.000000] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap 1c0000c40660462 ecap 7e1ff0505e
[    0.000000] DMAR: DRHD base: 0x000000fed91000 flags: 0x1
[    0.000000] DMAR: dmar1: reg_base_addr fed91000 ver 1:0 cap d2008c20660462 ecap f010da
[    0.000000] DMAR: RMRR base: 0x0000009cd85000 end: 0x0000009cda4fff
[    0.000000] DMAR: RMRR base: 0x0000009d800000 end: 0x0000009fffffff
[    0.000000] DMAR: ANDD device: 1 name: \_SB.PCI0.SDMA
[    0.000000] DMAR-IR: IOAPIC id 2 under DRHD base  0xfed91000 IOMMU 1
[    0.000000] DMAR-IR: HPET id 0 under DRHD base 0xfed91000
[    0.000000] DMAR-IR: x2apic is disabled because BIOS sets x2apic opt out bit.
[    0.000000] DMAR-IR: Use 'intremap=no_x2apic_optout' to override the BIOS setting.
[    0.000000] DMAR-IR: Enabled IRQ remapping in xapic mode
[    0.000000] x2apic: IRQ remapping doesn't support X2APIC mode
[    0.000000] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.020000] tsc: Fast TSC calibration using PIT
[    0.024000] tsc: Detected 2394.260 MHz processor
[    0.024000] Calibrating delay loop (skipped), value calculated using timer frequency.. 4788.52 BogoMIPS (lpj=9577040)
[    0.024000] pid_max: default: 32768 minimum: 301
[    0.024000] Security Framework initialized
[    0.024000] Yama: becoming mindful.
[    0.024000] AppArmor: AppArmor initialized
[    0.028967] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes)
[    0.030056] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.030102] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.030135] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.030334] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.030335] ENERGY_PERF_BIAS: View and update with x86_energy_perf_policy(8)
[    0.030339] mce: CPU supports 7 MCE banks
[    0.030350] CPU0: Thermal monitoring enabled (TM1)
[    0.030360] process: using mwait in idle threads
[    0.030363] Last level iTLB entries: 4KB 64, 2MB 8, 4MB 8
[    0.030364] Last level dTLB entries: 4KB 64, 2MB 0, 4MB 0, 1GB 4
[    0.030365] Spectre V2 : Mitigation: Full generic retpoline
[    0.030366] Spectre V2 : Spectre v2 mitigation: Enabling Indirect Branch Prediction Barrier
[    0.030366] Spectre V2 : Enabling Restricted Speculation for firmware calls
[    0.030367] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.036632] Freeing SMP alternatives memory: 36K
[    0.041311] TSC deadline timer enabled
[    0.041314] smpboot: CPU0: Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz (family: 0x6, model: 0x3d, stepping: 0x4)
[    0.041371] Performance Events: PEBS fmt2+, Broadwell events, 16-deep LBR, full-width counters, Intel PMU driver.
[    0.041413] ... version:                3
[    0.041414] ... bit width:              48
[    0.041414] ... generic registers:      4
[    0.041415] ... value mask:             0000ffffffffffff
[    0.041416] ... max period:             00007fffffffffff
[    0.041416] ... fixed-purpose events:   3
[    0.041417] ... event mask:             000000070000000f
[    0.041446] Hierarchical SRCU implementation.
[    0.042447] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.042458] smp: Bringing up secondary CPUs ...
[    0.042526] x86: Booting SMP configuration:
[    0.042527] .... node  #0, CPUs:      #1 #2 #3
[    0.044496] smp: Brought up 1 node, 4 CPUs
[    0.044496] smpboot: Max logical packages: 1
[    0.044496] smpboot: Total of 4 processors activated (19154.08 BogoMIPS)
[    0.048351] devtmpfs: initialized
[    0.048351] x86/mm: Memory block size: 128MB
[    0.049244] evm: security.selinux
[    0.049245] evm: security.SMACK64
[    0.049245] evm: security.SMACK64EXEC
[    0.049246] evm: security.SMACK64TRANSMUTE
[    0.049246] evm: security.SMACK64MMAP
[    0.049247] evm: security.apparmor
[    0.049247] evm: security.ima
[    0.049248] evm: security.capability
[    0.049260] PM: Registering ACPI NVS region [mem 0x9cddf000-0x9cfbefff] (1966080 bytes)
[    0.049260] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.049260] futex hash table entries: 1024 (order: 4, 65536 bytes)
[    0.049260] pinctrl core: initialized pinctrl subsystem
[    0.049260] RTC time: 18:00:24, date: 09/04/18
[    0.049260] NET: Registered protocol family 16
[    0.049260] audit: initializing netlink subsys (disabled)
[    0.049260] audit: type=2000 audit(1536084024.048:1): state=initialized audit_enabled=0 res=1
[    0.049260] cpuidle: using governor ladder
[    0.049260] cpuidle: using governor menu
[    0.049260] Simple Boot Flag at 0x44 set to 0x1
[    0.049260] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.049260] ACPI: bus type PCI registered
[    0.049260] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.049260] PCI: MMCONFIG for domain 0000 [bus 00-ff] at [mem 0xe0000000-0xefffffff] (base 0xe0000000)
[    0.049260] PCI: MMCONFIG at [mem 0xe0000000-0xefffffff] reserved in E820
[    0.049260] PCI: Using configuration type 1 for base access
[    0.049265] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.049265] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.052068] ACPI: Added _OSI(Module Device)
[    0.052069] ACPI: Added _OSI(Processor Device)
[    0.052069] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.052070] ACPI: Added _OSI(Processor Aggregator Device)
[    0.052071] ACPI: Added _OSI(Linux-Dell-Video)
[    0.053933] ACPI: Executed 17 blocks of module-level executable AML code
[    0.065430] ACPI: Dynamic OEM Table Load:
[    0.065439] ACPI: SSDT 0xFFFF98CA8BD33400 0003D3 (v02 PmRef  Cpu0Cst  00003001 INTL 20130117)
[    0.066107] ACPI: Dynamic OEM Table Load:
[    0.066114] ACPI: SSDT 0xFFFF98CA8BCB6000 0005AA (v02 PmRef  ApIst    00003000 INTL 20130117)
[    0.066837] ACPI: Dynamic OEM Table Load:
[    0.066843] ACPI: SSDT 0xFFFF98CA8BDDC400 000119 (v02 PmRef  ApCst    00003000 INTL 20130117)
[    0.068605] ACPI: EC: EC started
[    0.068605] ACPI: EC: interrupt blocked
[    0.069835] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as first EC
[    0.069837] ACPI: \_SB_.PCI0.LPCB.EC0_: GPE=0xa, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.069839] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as boot DSDT EC to handle transactions
[    0.069839] ACPI: Interpreter enabled
[    0.069879] ACPI: (supports S0 S3 S4 S5)
[    0.069880] ACPI: Using IOAPIC for interrupt routing
[    0.069916] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.070656] ACPI: Enabled 6 GPEs in block 00 to 7F
[    0.111856] ACPI: Power Resource [PC05] (on)
[    0.116488] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-fe])
[    0.116494] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.117741] acpi PNP0A08:00: _OSC: OS now controls [PCIeHotplug PME AER PCIeCapability]
[    0.117743] acpi PNP0A08:00: FADT indicates ASPM is unsupported, using BIOS configuration
[    0.118703] PCI host bridge to bus 0000:00
[    0.118705] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.118707] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.118708] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.118710] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000c3fff window]
[    0.118711] pci_bus 0000:00: root bus resource [mem 0x000c4000-0x000c7fff window]
[    0.118712] pci_bus 0000:00: root bus resource [mem 0x000c8000-0x000cbfff window]
[    0.118714] pci_bus 0000:00: root bus resource [mem 0x000cc000-0x000cffff window]
[    0.118715] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000d3fff window]
[    0.118716] pci_bus 0000:00: root bus resource [mem 0x000d4000-0x000d7fff window]
[    0.118717] pci_bus 0000:00: root bus resource [mem 0x000d8000-0x000dbfff window]
[    0.118719] pci_bus 0000:00: root bus resource [mem 0x000dc000-0x000dffff window]
[    0.118720] pci_bus 0000:00: root bus resource [mem 0x000e0000-0x000e3fff window]
[    0.118721] pci_bus 0000:00: root bus resource [mem 0x000e4000-0x000e7fff window]
[    0.118723] pci_bus 0000:00: root bus resource [mem 0x000e8000-0x000ebfff window]
[    0.118724] pci_bus 0000:00: root bus resource [mem 0x000ec000-0x000effff window]
[    0.118725] pci_bus 0000:00: root bus resource [mem 0xa0000000-0xfeafffff window]
[    0.118727] pci_bus 0000:00: root bus resource [bus 00-fe]
[    0.118736] pci 0000:00:00.0: [8086:1604] type 00 class 0x060000
[    0.119064] pci 0000:00:02.0: [8086:1616] type 00 class 0x030000
[    0.119075] pci 0000:00:02.0: reg 0x10: [mem 0xd0000000-0xd0ffffff 64bit]
[    0.119082] pci 0000:00:02.0: reg 0x18: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.119087] pci 0000:00:02.0: reg 0x20: [io  0x5000-0x503f]
[    0.119101] pci 0000:00:02.0: BAR 2: assigned to efifb
[    0.119426] pci 0000:00:03.0: [8086:160c] type 00 class 0x040300
[    0.119436] pci 0000:00:03.0: reg 0x10: [mem 0xd2310000-0xd2313fff 64bit]
[    0.119784] pci 0000:00:14.0: [8086:9cb1] type 00 class 0x0c0330
[    0.119803] pci 0000:00:14.0: reg 0x10: [mem 0xd2300000-0xd230ffff 64bit]
[    0.119860] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    0.120176] pci 0000:00:16.0: [8086:9cba] type 00 class 0x078000
[    0.120195] pci 0000:00:16.0: reg 0x10: [mem 0xd231b000-0xd231b01f 64bit]
[    0.120254] pci 0000:00:16.0: PME# supported from D0 D3hot D3cold
[    0.120587] pci 0000:00:1b.0: [8086:9ca0] type 00 class 0x040300
[    0.120606] pci 0000:00:1b.0: reg 0x10: [mem 0xd2314000-0xd2317fff 64bit]
[    0.120662] pci 0000:00:1b.0: PME# supported from D0 D3hot D3cold
[    0.120986] pci 0000:00:1c.0: [8086:9c90] type 01 class 0x060400
[    0.121054] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.121420] pci 0000:00:1c.2: [8086:9c94] type 01 class 0x060400
[    0.121490] pci 0000:00:1c.2: PME# supported from D0 D3hot D3cold
[    0.121857] pci 0000:00:1c.3: [8086:9c96] type 01 class 0x060400
[    0.121927] pci 0000:00:1c.3: PME# supported from D0 D3hot D3cold
[    0.122294] pci 0000:00:1c.4: [8086:9c98] type 01 class 0x060400
[    0.122364] pci 0000:00:1c.4: PME# supported from D0 D3hot D3cold
[    0.122733] pci 0000:00:1d.0: [8086:9ca6] type 00 class 0x0c0320
[    0.123362] pci 0000:00:1d.0: reg 0x10: [mem 0xd2319000-0xd23193ff]
[    0.125114] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
[    0.125433] pci 0000:00:1f.0: [8086:9cc3] type 00 class 0x060100
[    0.125847] pci 0000:00:1f.2: [8086:9c83] type 00 class 0x010601
[    0.125862] pci 0000:00:1f.2: reg 0x10: [io  0x5088-0x508f]
[    0.125868] pci 0000:00:1f.2: reg 0x14: [io  0x5094-0x5097]
[    0.125874] pci 0000:00:1f.2: reg 0x18: [io  0x5080-0x5087]
[    0.125881] pci 0000:00:1f.2: reg 0x1c: [io  0x5090-0x5093]
[    0.125887] pci 0000:00:1f.2: reg 0x20: [io  0x5060-0x507f]
[    0.125894] pci 0000:00:1f.2: reg 0x24: [mem 0xd2318000-0xd23187ff]
[    0.125928] pci 0000:00:1f.2: PME# supported from D3hot
[    0.126230] pci 0000:00:1f.3: [8086:9ca2] type 00 class 0x0c0500
[    0.126246] pci 0000:00:1f.3: reg 0x10: [mem 0xd231a000-0xd231a0ff 64bit]
[    0.126265] pci 0000:00:1f.3: reg 0x20: [io  0x5040-0x505f]
[    0.126626] pci 0000:00:1c.0: PCI bridge to [bus 01]
[    0.126699] pci 0000:02:00.0: [10ec:8136] type 00 class 0x020000
[    0.126737] pci 0000:02:00.0: reg 0x10: [io  0x4000-0x40ff]
[    0.126773] pci 0000:02:00.0: reg 0x18: [mem 0xd2200000-0xd2200fff 64bit]
[    0.126795] pci 0000:02:00.0: reg 0x20: [mem 0xd2000000-0xd2003fff 64bit pref]
[    0.126910] pci 0000:02:00.0: supports D1 D2
[    0.126912] pci 0000:02:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.136027] pci 0000:00:1c.2: PCI bridge to [bus 02]
[    0.136030] pci 0000:00:1c.2:   bridge window [io  0x4000-0x4fff]
[    0.136033] pci 0000:00:1c.2:   bridge window [mem 0xd2200000-0xd22fffff]
[    0.136037] pci 0000:00:1c.2:   bridge window [mem 0xd2000000-0xd20fffff 64bit pref]
[    0.136209] pci 0000:03:00.0: [8086:08b1] type 00 class 0x028000
[    0.136318] pci 0000:03:00.0: reg 0x10: [mem 0xd2100000-0xd2101fff 64bit]
[    0.136611] pci 0000:03:00.0: PME# supported from D0 D3hot D3cold
[    0.148080] pci 0000:00:1c.3: PCI bridge to [bus 03]
[    0.148084] pci 0000:00:1c.3:   bridge window [mem 0xd2100000-0xd21fffff]
[    0.148166] pci 0000:04:00.0: [1002:6604] type 00 class 0x038000
[    0.148191] pci 0000:04:00.0: reg 0x10: [mem 0xb0000000-0xbfffffff 64bit pref]
[    0.148202] pci 0000:04:00.0: reg 0x18: [mem 0xd1000000-0xd103ffff 64bit]
[    0.148210] pci 0000:04:00.0: reg 0x20: [io  0x3000-0x30ff]
[    0.148222] pci 0000:04:00.0: reg 0x30: [mem 0xfffe0000-0xffffffff pref]
[    0.148229] pci 0000:04:00.0: enabling Extended Tags
[    0.148287] pci 0000:04:00.0: supports D1 D2
[    0.148289] pci 0000:04:00.0: PME# supported from D1 D2 D3hot
[    0.160018] pci 0000:00:1c.4: PCI bridge to [bus 04-09]
[    0.160021] pci 0000:00:1c.4:   bridge window [io  0x3000-0x3fff]
[    0.160023] pci 0000:00:1c.4:   bridge window [mem 0xd1000000-0xd1ffffff]
[    0.160028] pci 0000:00:1c.4:   bridge window [mem 0xb0000000-0xbfffffff 64bit pref]
[    0.189625] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.189699] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.189770] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.189841] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.189912] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.189982] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.190052] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.190122] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    0.190464] ACPI: EC: interrupt unblocked
[    0.190472] ACPI: EC: event unblocked
[    0.190478] ACPI: \_SB_.PCI0.LPCB.EC0_: GPE=0xa, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.190480] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as boot DSDT EC to handle transactions and events
[    0.190683] SCSI subsystem initialized
[    0.190710] libata version 3.00 loaded.
[    0.190710] pci 0000:00:02.0: vgaarb: setting as boot VGA device
[    0.190710] pci 0000:00:02.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.190710] pci 0000:00:02.0: vgaarb: bridge control possible
[    0.190710] vgaarb: loaded
[    0.190710] ACPI: bus type USB registered
[    0.190710] usbcore: registered new interface driver usbfs
[    0.190710] usbcore: registered new interface driver hub
[    0.190710] usbcore: registered new device driver usb
[    0.265844] EDAC MC: Ver: 3.0.0
[    0.265844] Registered efivars operations
[    0.306474] PCI: Using ACPI for IRQ routing
[    0.311926] PCI: pci_cache_line_size set to 64 bytes
[    0.312081] e820: reserve RAM buffer [mem 0x00058000-0x0005ffff]
[    0.312083] e820: reserve RAM buffer [mem 0x00086000-0x0008ffff]
[    0.312084] e820: reserve RAM buffer [mem 0x89102018-0x8bffffff]
[    0.312085] e820: reserve RAM buffer [mem 0x89111018-0x8bffffff]
[    0.312087] e820: reserve RAM buffer [mem 0x8911e018-0x8bffffff]
[    0.312088] e820: reserve RAM buffer [mem 0x8a7ea000-0x8bffffff]
[    0.312089] e820: reserve RAM buffer [mem 0x9c3ef000-0x9fffffff]
[    0.312090] e820: reserve RAM buffer [mem 0x9d000000-0x9fffffff]
[    0.312091] e820: reserve RAM buffer [mem 0x45f000000-0x45fffffff]
[    0.312185] NetLabel: Initializing
[    0.312185] NetLabel:  domain hash size = 128
[    0.312186] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.312198] NetLabel:  unlabeled traffic allowed by default
[    0.312349] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    0.312355] hpet0: 8 comparators, 64-bit 14.318180 MHz counter
[    0.314374] clocksource: Switched to clocksource hpet
[    0.321561] VFS: Disk quotas dquot_6.6.0
[    0.321579] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.321677] AppArmor: AppArmor Filesystem Enabled
[    0.321702] pnp: PnP ACPI init
[    0.321952] system 00:00: [io  0x0680-0x069f] has been reserved
[    0.321955] system 00:00: [io  0xfd60-0xfd63] has been reserved
[    0.321956] system 00:00: [io  0xffff] has been reserved
[    0.321958] system 00:00: [io  0xffff] has been reserved
[    0.321960] system 00:00: [io  0xffff] has been reserved
[    0.321961] system 00:00: [io  0x1800-0x18fe] has been reserved
[    0.321963] system 00:00: [io  0x164e-0x164f] has been reserved
[    0.321969] system 00:00: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.322028] pnp 00:01: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.322076] system 00:02: [io  0x1854-0x1857] has been reserved
[    0.322080] system 00:02: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    0.322114] pnp 00:03: Plug and Play ACPI device, IDs PNP0303 (active)
[    0.322143] pnp 00:04: Plug and Play ACPI device, IDs DLL0642 PNP0f03 (active)
[    0.348635] system 00:05: [mem 0xfe102000-0xfe102fff] has been reserved
[    0.348637] system 00:05: [mem 0xfe106000-0xfe106fff] has been reserved
[    0.348641] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.349414] system 00:06: [mem 0xfed1c000-0xfed1ffff] has been reserved
[    0.349416] system 00:06: [mem 0xfed10000-0xfed17fff] has been reserved
[    0.349418] system 00:06: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.349420] system 00:06: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.349422] system 00:06: [mem 0xe0000000-0xefffffff] has been reserved
[    0.349424] system 00:06: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.349426] system 00:06: [mem 0xfed90000-0xfed93fff] could not be reserved
[    0.349428] system 00:06: [mem 0xfed45000-0xfed8ffff] has been reserved
[    0.349430] system 00:06: [mem 0xff000000-0xff000fff] has been reserved
[    0.349431] system 00:06: [mem 0xff010000-0xffffffff] could not be reserved
[    0.349433] system 00:06: [mem 0xfee00000-0xfeefffff] could not be reserved
[    0.349435] system 00:06: [mem 0xa0010000-0xa001ffff] has been reserved
[    0.349436] system 00:06: [mem 0xa0000000-0xa000ffff] has been reserved
[    0.349440] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.349750] pnp: PnP ACPI: found 7 devices
[    0.355715] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.355720] pci 0000:04:00.0: can't claim BAR 6 [mem 0xfffe0000-0xffffffff pref]: no compatible bridge window
[    0.355746] pci 0000:00:1c.0: PCI bridge to [bus 01]
[    0.355756] pci 0000:00:1c.2: PCI bridge to [bus 02]
[    0.355758] pci 0000:00:1c.2:   bridge window [io  0x4000-0x4fff]
[    0.355762] pci 0000:00:1c.2:   bridge window [mem 0xd2200000-0xd22fffff]
[    0.355765] pci 0000:00:1c.2:   bridge window [mem 0xd2000000-0xd20fffff 64bit pref]
[    0.355770] pci 0000:00:1c.3: PCI bridge to [bus 03]
[    0.355774] pci 0000:00:1c.3:   bridge window [mem 0xd2100000-0xd21fffff]
[    0.355782] pci 0000:04:00.0: BAR 6: assigned [mem 0xd1040000-0xd105ffff pref]
[    0.355784] pci 0000:00:1c.4: PCI bridge to [bus 04-09]
[    0.355786] pci 0000:00:1c.4:   bridge window [io  0x3000-0x3fff]
[    0.355790] pci 0000:00:1c.4:   bridge window [mem 0xd1000000-0xd1ffffff]
[    0.355793] pci 0000:00:1c.4:   bridge window [mem 0xb0000000-0xbfffffff 64bit pref]
[    0.355799] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.355800] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.355802] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.355803] pci_bus 0000:00: resource 7 [mem 0x000c0000-0x000c3fff window]
[    0.355804] pci_bus 0000:00: resource 8 [mem 0x000c4000-0x000c7fff window]
[    0.355806] pci_bus 0000:00: resource 9 [mem 0x000c8000-0x000cbfff window]
[    0.355807] pci_bus 0000:00: resource 10 [mem 0x000cc000-0x000cffff window]
[    0.355809] pci_bus 0000:00: resource 11 [mem 0x000d0000-0x000d3fff window]
[    0.355810] pci_bus 0000:00: resource 12 [mem 0x000d4000-0x000d7fff window]
[    0.355812] pci_bus 0000:00: resource 13 [mem 0x000d8000-0x000dbfff window]
[    0.355813] pci_bus 0000:00: resource 14 [mem 0x000dc000-0x000dffff window]
[    0.355815] pci_bus 0000:00: resource 15 [mem 0x000e0000-0x000e3fff window]
[    0.355816] pci_bus 0000:00: resource 16 [mem 0x000e4000-0x000e7fff window]
[    0.355817] pci_bus 0000:00: resource 17 [mem 0x000e8000-0x000ebfff window]
[    0.355819] pci_bus 0000:00: resource 18 [mem 0x000ec000-0x000effff window]
[    0.355820] pci_bus 0000:00: resource 19 [mem 0xa0000000-0xfeafffff window]
[    0.355822] pci_bus 0000:02: resource 0 [io  0x4000-0x4fff]
[    0.355823] pci_bus 0000:02: resource 1 [mem 0xd2200000-0xd22fffff]
[    0.355825] pci_bus 0000:02: resource 2 [mem 0xd2000000-0xd20fffff 64bit pref]
[    0.355826] pci_bus 0000:03: resource 1 [mem 0xd2100000-0xd21fffff]
[    0.355828] pci_bus 0000:04: resource 0 [io  0x3000-0x3fff]
[    0.355829] pci_bus 0000:04: resource 1 [mem 0xd1000000-0xd1ffffff]
[    0.355831] pci_bus 0000:04: resource 2 [mem 0xb0000000-0xbfffffff 64bit pref]
[    0.355999] NET: Registered protocol family 2
[    0.356194] TCP established hash table entries: 131072 (order: 8, 1048576 bytes)
[    0.356365] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.356473] TCP: Hash tables configured (established 131072 bind 65536)
[    0.356509] UDP hash table entries: 8192 (order: 6, 262144 bytes)
[    0.356548] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes)
[    0.356614] NET: Registered protocol family 1
[    0.356625] pci 0000:00:02.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.356723] pci 0000:00:14.0: can't derive routing for PCI INT A
[    0.356724] pci 0000:00:14.0: PCI INT A: not connected
[    0.376187] PCI: CLS 64 bytes, default 64
[    0.376222] Unpacking initramfs...
[    1.171733] Freeing initrd memory: 53316K
[    1.171769] DMAR: ACPI device "INTL9C60:00" under DMAR at fed91000 as 00:15.0
[    1.171782] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    1.171785] software IO TLB [mem 0x97f3e000-0x9bf3e000] (64MB) mapped at [        (ptrval)-        (ptrval)]
[    1.172024] Scanning for low memory corruption every 60 seconds
[    1.172595] Initialise system trusted keyrings
[    1.172602] Key type blacklist registered
[    1.172629] workingset: timestamp_bits=36 max_order=22 bucket_order=0
[    1.173696] zbud: loaded
[    1.174157] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    1.174268] fuse init (API version 7.26)
[    1.175320] Key type asymmetric registered
[    1.175321] Asymmetric key parser 'x509' registered
[    1.175346] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    1.175374] io scheduler noop registered
[    1.175375] io scheduler deadline registered
[    1.175412] io scheduler cfq registered (default)
[    1.176216] pcieport 0000:00:1c.0: Signaling PME with IRQ 42
[    1.176236] pcieport 0000:00:1c.2: Signaling PME with IRQ 43
[    1.176250] pcieport 0000:00:1c.3: Signaling PME with IRQ 44
[    1.176264] pcieport 0000:00:1c.4: Signaling PME with IRQ 45
[    1.176280] pciehp 0000:00:1c.4:pcie004: Slot #4 AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug+ Surprise+ Interlock- NoCompl+ LLActRep+
[    1.176346] efifb: probing for efifb
[    1.176357] efifb: framebuffer at 0xc0000000, using 8100k, total 8100k
[    1.176358] efifb: mode is 1920x1080x32, linelength=7680, pages=1
[    1.176359] efifb: scrolling: redraw
[    1.176360] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    1.176427] Console: switching to colour frame buffer device 240x67
[    1.176450] fb0: EFI VGA frame buffer device
[    1.176457] intel_idle: MWAIT substates: 0x11142120
[    1.176458] intel_idle: v0.4.1 model 0x3D
[    1.176627] intel_idle: lapic_timer_reliable_states 0xffffffff
[    1.176867] ACPI: AC Adapter [ACAD] (on-line)
[    1.176924] input: Sleep Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/device:18/PNP0C0E:00/input/input0
[    1.176931] ACPI: Sleep Button [SLPB]
[    1.176961] input: Lid Switch as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/device:18/PNP0C0D:00/input/input1
[    1.176981] ACPI: Lid Switch [LID0]
[    1.177036] input: Sleep Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0E:01/input/input2
[    1.177044] ACPI: Sleep Button [SLPB]
[    1.177073] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input3
[    1.177088] ACPI: Power Button [PWRF]
[    1.177509] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    1.344157] random: fast init done
[    1.400179] [Firmware Bug]: battery: (dis)charge rate invalid.
[    1.400222] ACPI: Battery Slot [BAT1] (battery present)
[    1.400440] Linux agpgart interface v0.103
[    1.402516] loop: module loaded
[    1.402672] libphy: Fixed MDIO Bus: probed
[    1.402673] tun: Universal TUN/TAP device driver, 1.6
[    1.402702] PPP generic driver version 2.4.2
[    1.402737] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    1.402740] ehci-pci: EHCI PCI platform driver
[    1.402878] ehci-pci 0000:00:1d.0: EHCI Host Controller
[    1.402882] ehci-pci 0000:00:1d.0: new USB bus registered, assigned bus number 1
[    1.402893] ehci-pci 0000:00:1d.0: debug port 2
[    1.406805] ehci-pci 0000:00:1d.0: cache line size of 64 is not supported
[    1.406818] ehci-pci 0000:00:1d.0: irq 23, io mem 0xd2319000
[    1.420015] ehci-pci 0000:00:1d.0: USB 2.0 started, EHCI 1.00
[    1.420046] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    1.420048] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.420049] usb usb1: Product: EHCI Host Controller
[    1.420051] usb usb1: Manufacturer: Linux 4.15.0-33-generic ehci_hcd
[    1.420052] usb usb1: SerialNumber: 0000:00:1d.0
[    1.420165] hub 1-0:1.0: USB hub found
[    1.420169] hub 1-0:1.0: 2 ports detected
[    1.420298] ehci-platform: EHCI generic platform driver
[    1.420306] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    1.420309] ohci-pci: OHCI PCI platform driver
[    1.420317] ohci-platform: OHCI generic platform driver
[    1.420322] uhci_hcd: USB Universal Host Controller Interface driver
[    1.420425] xhci_hcd 0000:00:14.0: can't derive routing for PCI INT A
[    1.420426] xhci_hcd 0000:00:14.0: PCI INT A: no GSI
[    1.420444] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    1.420449] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 2
[    1.421510] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x0004b810
[    1.421514] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
[    1.421616] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002
[    1.421618] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.421619] usb usb2: Product: xHCI Host Controller
[    1.421620] usb usb2: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    1.421621] usb usb2: SerialNumber: 0000:00:14.0
[    1.421726] hub 2-0:1.0: USB hub found
[    1.421738] hub 2-0:1.0: 11 ports detected
[    1.425568] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    1.425571] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 3
[    1.425574] xhci_hcd 0000:00:14.0: Host supports USB 3.0  SuperSpeed
[    1.425599] usb usb3: New USB device found, idVendor=1d6b, idProduct=0003
[    1.425601] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.425602] usb usb3: Product: xHCI Host Controller
[    1.425603] usb usb3: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    1.425604] usb usb3: SerialNumber: 0000:00:14.0
[    1.425711] hub 3-0:1.0: USB hub found
[    1.425718] hub 3-0:1.0: 4 ports detected
[    1.426747] usb: port power management may be unreliable
[    1.426839] i8042: PNP: PS/2 Controller [PNP0303:PS2K,PNP0f03:PS2M] at 0x60,0x64 irq 1,12
[    1.456254] serio: i8042 KBD port at 0x60,0x64 irq 1
[    1.456257] serio: i8042 AUX port at 0x60,0x64 irq 12
[    1.456395] mousedev: PS/2 mouse device common for all mice
[    1.458868] rtc_cmos 00:01: RTC can wake from S4
[    1.458980] rtc_cmos 00:01: rtc core: registered rtc_cmos as rtc0
[    1.459006] rtc_cmos 00:01: alarms up to one month, 242 bytes nvram, hpet irqs
[    1.459011] i2c /dev entries driver
[    1.459076] device-mapper: uevent: version 1.0.3
[    1.459126] device-mapper: ioctl: 4.37.0-ioctl (2017-09-20) initialised: dm-devel@redhat.com
[    1.459133] intel_pstate: Intel P-state driver initializing
[    1.459334] ledtrig-cpu: registered to indicate activity on CPUs
[    1.459336] EFI Variables Facility v0.08 2004-May-17
[    1.495603] NET: Registered protocol family 10
[    1.498710] Segment Routing with IPv6
[    1.498726] NET: Registered protocol family 17
[    1.498753] Key type dns_resolver registered
[    1.498937] RAS: Correctable Errors collector initialized.
[    1.498962] microcode: sig=0x306d4, pf=0x40, revision=0x2b
[    1.499003] microcode: Microcode Update Driver: v2.2.
[    1.499010] sched_clock: Marking stable (1499000874, 0)->(1484591782, 14409092)
[    1.499154] registered taskstats version 1
[    1.499160] Loading compiled-in X.509 certificates
[    1.501128] Loaded X.509 cert 'Build time autogenerated kernel key: d918b280ed158d77154089242222928ec1ab43e6'
[    1.502772] Loaded UEFI:db cert 'Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53' linked to secondary sys keyring
[    1.502790] Loaded UEFI:db cert 'Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4' linked to secondary sys keyring
[    1.504548] Loaded UEFI:db cert 'CompalA31CSMB: 1e3b690555de0b9542b280303282c6d6' linked to secondary sys keyring
[    1.505435] Loaded UEFI:MokListRT cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63' linked to secondary sys keyring
[    1.506103] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input4
[    1.507075] zswap: loaded using pool lzo/zbud
[    1.510757] Key type big_key registered
[    1.510760] Key type trusted registered
[    1.511952] Key type encrypted registered
[    1.511953] AppArmor: AppArmor sha1 policy hashing enabled
[    1.511955] ima: No TPM chip found, activating TPM-bypass! (rc=-19)
[    1.511969] evm: HMAC attrs: 0x1
[    1.512538]   Magic number: 2:190:38
[    1.512550] bdi 7:3: hash matches
[    1.512601] memory memory74: hash matches
[    1.512646] rtc_cmos 00:01: setting system clock to 2018-09-04 18:00:25 UTC (1536084025)
[    1.512690] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    1.512690] EDD information not available.
[    1.512729] Lockdown: Hibernation is restricted; see man kernel_lockdown.7
[    1.756052] usb 1-1: new high-speed USB device number 2 using ehci-pci
[    1.760052] usb 2-1: new high-speed USB device number 2 using xhci_hcd
[    1.836104] Freeing unused kernel memory: 2404K
[    1.876076] Write protecting the kernel read-only data: 20480k
[    1.877233] Freeing unused kernel memory: 2008K
[    1.880705] Freeing unused kernel memory: 1892K
[    1.886186] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.886186] x86/mm: Checking user space page tables
[    1.891533] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.901133] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.901203] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.901210] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.908472] usb 2-1: New USB device found, idVendor=0bda, idProduct=8179
[    1.908475] usb 2-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    1.908477] usb 2-1: Product: 802.11n NIC
[    1.908478] usb 2-1: Manufacturer: Realtek
[    1.908480] usb 2-1: SerialNumber: 00E04C0001
[    1.916395] usb 1-1: New USB device found, idVendor=8087, idProduct=8001
[    1.916397] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.916551] hub 1-1:1.0: USB hub found
[    1.916643] hub 1-1:1.0: 8 ports detected
[    1.949412] hidraw: raw HID events driver (C) Jiri Kosina
[    1.956228] wmi_bus wmi_bus-PNP0C14:00: WQBC data block query control method not found
[    1.960720] r8169 Gigabit Ethernet driver 2.3LK-NAPI loaded
[    1.960728] r8169 0000:02:00.0: can't disable ASPM; OS doesn't have ASPM control
[    1.961103] ahci 0000:00:1f.2: version 3.0
[    1.961241] r8169 0000:02:00.0 eth0: RTL8106e at 0x        (ptrval), 44:a8:42:ea:f7:e4, XID 04900000 IRQ 47
[    1.968159] i2c_hid i2c-DLL0641:00: i2c-DLL0641:00 supply vdd not found, using dummy regulator
[    1.971402] ahci 0000:00:1f.2: AHCI 0001.0300 32 slots 3 ports 6 Gbps 0x1 impl SATA mode
[    1.971406] ahci 0000:00:1f.2: flags: 64bit ncq pm led clo only pio slum part deso sadm sds apst 
[    1.971723] scsi host0: ahci
[    1.971882] scsi host1: ahci
[    1.972102] scsi host2: ahci
[    1.972135] ata1: SATA max UDMA/133 abar m2048@0xd2318000 port 0xd2318100 irq 48
[    1.972136] ata2: DUMMY
[    1.972136] ata3: DUMMY
[    1.988405] r8169 0000:02:00.0 enp2s0: renamed from eth0
[    1.997874] Lockdown: Loading of unsigned modules is restricted; see man kernel_lockdown.7
[    2.015804] [drm] Memory usable by graphics device = 4096M
[    2.015807] checking generic (c0000000 7e9000) vs hw (c0000000 10000000)
[    2.015808] fb: switching to inteldrmfb from EFI VGA
[    2.015830] Console: switching to colour dummy device 80x25
[    2.015912] [drm] Replacing VGA console driver
[    2.015950] [drm] ACPI BIOS requests an excessive sleep of 10000 ms, using 1500 ms instead
[    2.021908] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    2.021908] [drm] Driver supports precise vblank timestamp query.
[    2.023994] i915 0000:00:02.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=io+mem
[    2.030001] [drm] Initialized i915 1.6.0 20171023 for 0000:00:02.0 on minor 0
[    2.031417] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[    2.031665] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input8
[    2.036088] usb 2-2: new low-speed USB device number 3 using xhci_hcd
[    2.176094] tsc: Refined TSC clocksource calibration: 2394.457 MHz
[    2.176100] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x2283c360c9e, max_idle_ns: 440795302742 ns
[    2.186994] fbcon: inteldrmfb (fb0) is primary device
[    2.187060] Console: switching to colour frame buffer device 240x67
[    2.187086] usb 2-2: New USB device found, idVendor=275d, idProduct=0ba6
[    2.187089] usb 2-2: New USB device strings: Mfr=0, Product=1, SerialNumber=0
[    2.187091] usb 2-2: Product: USB OPTICAL MOUSE 
[    2.187096] i915 0000:00:02.0: fb0: inteldrmfb frame buffer device
[    2.286969] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    2.312103] usb 2-5: new full-speed USB device number 4 using xhci_hcd
[    2.353739] ata1.00: ATA-9: ST1000LM014-1EJ164, DEMB, max UDMA/133
[    2.353741] ata1.00: 1953525168 sectors, multi 0: LBA48 NCQ (depth 31/32), AA
[    2.398099] ata1.00: configured for UDMA/133
[    2.398348] scsi 0:0:0:0: Direct-Access     ATA      ST1000LM014-1EJ1 DEMB PQ: 0 ANSI: 5
[    2.398636] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    2.398676] sd 0:0:0:0: [sda] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    2.398679] sd 0:0:0:0: [sda] 4096-byte physical blocks
[    2.398696] sd 0:0:0:0: [sda] Write Protect is off
[    2.398698] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    2.398728] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    2.401722]  sda: sda1 sda2 sda3 sda4 sda5 sda6 sda7 sda8 sda9
[    2.402488] sd 0:0:0:0: [sda] Attached SCSI disk
[    2.461006] usb 2-5: New USB device found, idVendor=8087, idProduct=07dc
[    2.461008] usb 2-5: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    2.588092] usb 2-6: new full-speed USB device number 5 using xhci_hcd
[    3.200243] clocksource: Switched to clocksource tsc
[    7.905219] usb 2-6: New USB device found, idVendor=04f3, idProduct=2013
[    7.905221] usb 2-6: New USB device strings: Mfr=4, Product=14, SerialNumber=0
[    7.905223] usb 2-6: Product: Touchscreen
[    7.905224] usb 2-6: Manufacturer: ELAN
[    8.032100] usb 2-7: new high-speed USB device number 6 using xhci_hcd
[    8.180561] usb 2-7: New USB device found, idVendor=0bda, idProduct=0129
[    8.180563] usb 2-7: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    8.180564] usb 2-7: Product: USB2.0-CRW
[    8.180565] usb 2-7: Manufacturer: Generic
[    8.180567] usb 2-7: SerialNumber: 20100201396000000
[    8.308062] usb 2-8: new high-speed USB device number 7 using xhci_hcd
[    8.483800] usb 2-8: New USB device found, idVendor=0bda, idProduct=5754
[    8.483803] usb 2-8: New USB device strings: Mfr=3, Product=1, SerialNumber=2
[    8.483804] usb 2-8: Product: Integrated_Webcam_HD
[    8.483805] usb 2-8: Manufacturer: CN06307G72487541BAVCA02
[    8.483816] usb 2-8: SerialNumber: 200901010001
[    8.491107] usbcore: registered new interface driver rtsx_usb
[    8.496500] usbcore: registered new interface driver usbhid
[    8.496501] usbhid: USB HID core driver
[    8.497799] input: USB OPTICAL MOUSE  as /devices/pci0000:00/0000:00:14.0/usb2/2-2/2-2:1.0/0003:275D:0BA6.0002/input/input9
[    8.497885] hid-generic 0003:275D:0BA6.0002: input,hidraw0: USB HID v1.11 Mouse [USB OPTICAL MOUSE ] on usb-0000:00:14.0-2/input0
[    8.627293] EXT4-fs (sda8): mounted filesystem with ordered data mode. Opts: (null)
[    9.035422] systemd[1]: systemd 229 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ -LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN)
[    9.052170] systemd[1]: Detected architecture x86-64.
[    9.052546] systemd[1]: Set hostname to <babu-Inspiron-5548>.
[    9.053596] Lockdown: /dev/mem,kmem,port is restricted; see man kernel_lockdown.7
[    9.212680] random: crng init done
[    9.212682] random: 7 urandom warning(s) missed due to ratelimiting
[    9.240225] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[    9.240308] systemd[1]: Listening on Journal Audit Socket.
[    9.240346] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    9.240368] systemd[1]: Listening on udev Kernel Socket.
[    9.240378] systemd[1]: Reached target Remote File Systems (Pre).
[    9.240410] systemd[1]: Started Trigger resolvconf update for networkd DNS.
[    9.240440] systemd[1]: Listening on /dev/initctl Compatibility Named Pipe.
[    9.444068] lp: driver loaded but no devices found
[    9.450229] ppdev: user-space parallel port driver
[   14.390293] EXT4-fs (sda8): re-mounted. Opts: errors=remount-ro
[   14.399089] systemd-journald[262]: Received request to flush runtime journal from PID 1
[   14.628382] dw_dmac INTL9C60:00: DesignWare DMA Controller, 8 channels
[   14.646441] media: Linux media interface: v0.10
[   14.647733] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[   14.651962] Linux video capture interface: v2.00
[   14.656780] Bluetooth: Core ver 2.22
[   14.656793] NET: Registered protocol family 31
[   14.656794] Bluetooth: HCI device and connection manager initialized
[   14.656797] Bluetooth: HCI socket layer initialized
[   14.656799] Bluetooth: L2CAP socket layer initialized
[   14.656804] Bluetooth: SCO socket layer initialized
[   14.664469] usbcore: registered new interface driver btusb
[   14.667677] uvcvideo: Found UVC 1.00 device Integrated_Webcam_HD (0bda:5754)
[   14.671032] uvcvideo 2-8:1.0: Entity type for entity Extension 4 was not initialized!
[   14.671035] uvcvideo 2-8:1.0: Entity type for entity Extension 7 was not initialized!
[   14.671037] uvcvideo 2-8:1.0: Entity type for entity Processing 2 was not initialized!
[   14.671038] uvcvideo 2-8:1.0: Entity type for entity Camera 1 was not initialized!
[   14.671117] input: Integrated_Webcam_HD: Integrate as /devices/pci0000:00/0000:00:14.0/usb2/2-8/2-8:1.0/input/input10
[   14.671182] usbcore: registered new interface driver uvcvideo
[   14.671183] USB Video Class driver (1.1.1)
[   14.676073] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[   14.676455] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[   14.683759] Bluetooth: hci0: read Intel version: 3707100180012d0d00
[   14.684651] input: DLL0641:00 06CB:7621 Touchpad as /devices/pci0000:00/INT3433:00/i2c-0/i2c-DLL0641:00/0018:06CB:7621.0001/input/input12
[   14.684765] hid-multitouch 0018:06CB:7621.0001: input,hidraw1: I2C HID v1.00 Mouse [DLL0641:00 06CB:7621] on i2c-DLL0641:00
[   14.685698] Bluetooth: hci0: Intel Bluetooth firmware file: intel/ibt-hw-37.7.10-fw-1.80.1.2d.d.bseq
[   14.687233] input: ELAN Touchscreen as /devices/pci0000:00/0000:00:14.0/usb2/2-6/2-6:1.0/0003:04F3:2013.0003/input/input17
[   14.687354] hid-multitouch 0003:04F3:2013.0003: input,hiddev0,hidraw2: USB HID v1.10 Device [ELAN Touchscreen] on usb-0000:00:14.0-6/input0
[   14.689930] Intel(R) Wireless WiFi driver for Linux
[   14.689931] Copyright(c) 2003- 2015 Intel Corporation
[   14.711819] input: Dell WMI hotkeys as /devices/platform/PNP0C14:00/wmi_bus/wmi_bus-PNP0C14:00/9DBB5994-A997-11DA-B012-B622A1EF5492/input/input21
[   14.714508] snd_hda_intel 0000:00:03.0: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
[   14.744957] RAPL PMU: API unit is 2^-32 Joules, 4 fixed counters, 655360 ms ovfl timer
[   14.744958] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
[   14.744959] RAPL PMU: hw unit of domain package 2^-14 Joules
[   14.744959] RAPL PMU: hw unit of domain dram 2^-14 Joules
[   14.744960] RAPL PMU: hw unit of domain pp1-gpu 2^-14 Joules
[   14.747112] input: HDA Intel HDMI HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:03.0/sound/card0/input22
[   14.747159] input: HDA Intel HDMI HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:03.0/sound/card0/input23
[   14.747199] input: HDA Intel HDMI HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:03.0/sound/card0/input24
[   14.747238] input: HDA Intel HDMI HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:03.0/sound/card0/input25
[   14.747277] input: HDA Intel HDMI HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:03.0/sound/card0/input26
[   14.752459] snd_hda_codec_realtek hdaudioC1D0: autoconfig for ALC3234: line_outs=1 (0x14/0x0/0x0/0x0/0x0) type:speaker
[   14.752462] snd_hda_codec_realtek hdaudioC1D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[   14.752464] snd_hda_codec_realtek hdaudioC1D0:    hp_outs=1 (0x21/0x0/0x0/0x0/0x0)
[   14.752465] snd_hda_codec_realtek hdaudioC1D0:    mono: mono_out=0x0
[   14.752467] snd_hda_codec_realtek hdaudioC1D0:    inputs:
[   14.752469] snd_hda_codec_realtek hdaudioC1D0:      Headset Mic=0x19
[   14.752471] snd_hda_codec_realtek hdaudioC1D0:      Headphone Mic=0x1a
[   14.752472] snd_hda_codec_realtek hdaudioC1D0:      Internal Mic=0x12
[   14.761631] AVX2 version of gcm_enc/dec engaged.
[   14.761632] AES CTR mode by8 optimization enabled
[   14.779006] iwlwifi 0000:03:00.0: loaded firmware version 17.948900127.0 op_mode iwlmvm
[   14.789532] dcdbas dcdbas: Dell Systems Management Base Driver (version 5.6.0-3.2)
[   14.789788] dell_smbios: No dell-smbios drivers are loaded
[   14.812884] iwlwifi 0000:03:00.0: Detected Intel(R) Dual Band Wireless AC 7260, REV=0x144
[   14.833384] iwlwifi 0000:03:00.0: base HW address: 10:4a:7d:50:c9:e5
[   14.835845] input: HDA Intel PCH Headphone Mic as /devices/pci0000:00/0000:00:1b.0/sound/card1/input27
[   14.842867] Bluetooth: hci0: Intel firmware patch completed and activated
[   14.844505] intel_rapl: Found RAPL domain package
[   14.844507] intel_rapl: Found RAPL domain core
[   14.844508] intel_rapl: Found RAPL domain uncore
[   14.844509] intel_rapl: Found RAPL domain dram
[   14.844512] intel_rapl: RAPL package 0 domain package locked by BIOS
[   14.844516] intel_rapl: RAPL package 0 domain dram locked by BIOS
[   15.044538] ieee80211 phy0: Selected rate control algorithm 'iwl-mvm-rs'
[   15.045562] iwlwifi 0000:03:00.0 wlp3s0: renamed from wlan0
[   15.400645] Adding 3906556k swap on /dev/sda9.  Priority:-2 extents:1 across:3906556k FS
[   15.540805] audit: type=1400 audit(1536084039.523:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session" pid=729 comm="apparmor_parser"
[   15.540809] audit: type=1400 audit(1536084039.523:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session//chromium" pid=729 comm="apparmor_parser"
[   15.540854] audit: type=1400 audit(1536084039.523:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=730 comm="apparmor_parser"
[   15.540856] audit: type=1400 audit(1536084039.523:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=730 comm="apparmor_parser"
[   15.540858] audit: type=1400 audit(1536084039.523:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=730 comm="apparmor_parser"
[   15.540864] audit: type=1400 audit(1536084039.523:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=730 comm="apparmor_parser"
[   15.546375] audit: type=1400 audit(1536084039.527:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="webbrowser-app" pid=733 comm="apparmor_parser"
[   15.546379] audit: type=1400 audit(1536084039.527:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="webbrowser-app//oxide_helper" pid=733 comm="apparmor_parser"
[   15.547071] audit: type=1400 audit(1536084039.527:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=735 comm="apparmor_parser"
[   15.548209] audit: type=1400 audit(1536084039.531:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/ippusbxd" pid=737 comm="apparmor_parser"
[   15.686433] r8188eu: module is from the staging directory, the quality is unknown, you have been warned.
[   15.687590] Chip Version Info: CHIP_8188E_Normal_Chip_TSMC_D_CUT_1T1R_RomVer(0)
[   15.704331] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[   15.704332] Bluetooth: BNEP filters: protocol multicast
[   15.704336] Bluetooth: BNEP socket layer initialized
[   15.711681] usbcore: registered new interface driver r8188eu
[   15.712949] r8188eu 2-1:1.0 wlx18d6c71c43ac: renamed from wlan0
[   15.934049] Lockdown: ioperm is restricted; see man kernel_lockdown.7
[   16.111952] IPv6: ADDRCONF(NETDEV_UP): wlx18d6c71c43ac: link is not ready
[   16.480300] MAC Address = 18:d6:c7:1c:43:ac
[   16.481645] IPv6: ADDRCONF(NETDEV_UP): wlx18d6c71c43ac: link is not ready
[   16.484267] IPv6: ADDRCONF(NETDEV_UP): wlp3s0: link is not ready
[   16.731760] IPv6: ADDRCONF(NETDEV_UP): wlp3s0: link is not ready
[   16.735347] IPv6: ADDRCONF(NETDEV_UP): enp2s0: link is not ready
[   16.940179] r8169 0000:02:00.0 enp2s0: link down
[   16.940242] IPv6: ADDRCONF(NETDEV_UP): enp2s0: link is not ready
[   17.118215] IPv6: ADDRCONF(NETDEV_UP): wlp3s0: link is not ready
[   17.120615] IPv6: ADDRCONF(NETDEV_UP): wlx18d6c71c43ac: link is not ready
[   18.732436] Bluetooth: RFCOMM TTY layer initialized
[   18.732440] Bluetooth: RFCOMM socket layer initialized
[   18.732444] Bluetooth: RFCOMM ver 1.11
[   21.876713] R8188EU: assoc success
[   21.911716] IPv6: ADDRCONF(NETDEV_CHANGE): wlx18d6c71c43ac: link becomes ready
[   23.848206] wlp3s0: authenticate with 00:17:7c:51:57:61
[   23.851443] wlp3s0: send auth to 00:17:7c:51:57:61 (try 1/3)
[   23.877145] wlp3s0: authenticated
[   23.880082] wlp3s0: associate with 00:17:7c:51:57:61 (try 1/3)
[   23.887154] wlp3s0: RX AssocResp from 00:17:7c:51:57:61 (capab=0x411 status=0 aid=7)
[   23.896971] wlp3s0: associated
[   25.692185] powercap intel-rapl:0: package locked by BIOS, monitoring only
[   25.899384] IPv6: ADDRCONF(NETDEV_CHANGE): wlp3s0: link becomes ready



```

---

### 评论 #4 — jlgreathouse (2018-09-04T18:22:02Z)

Ah, that's the problem.

Your GPU, the Radeon R7 M265, is not supported in ROCm. It is product with the "Southern Islands" ISA (gfx601). ROCm does not offer support for any gfx6 GPUs, and only offers experimental support for a single gfx7 GPU (Hawaii -- gfx701).

I apologize that we do not offer support for ROCm on your device and thus we won't be able to solve this issue for you. I recommend looking into the amdgpu-pro software stack for running on your device.

---

### 评论 #5 — babujoym (2018-09-05T02:29:17Z)

Thanks a lot for checking this issue for me.
Its good to know why it was not working.

On Tue, 4 Sep 2018 at 11:52 PM, Joseph Greathouse <notifications@github.com>
wrote:

> Closed #519 <https://github.com/RadeonOpenCompute/ROCm/issues/519>.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/519#event-1826006476>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AGBYWkYptWOjgXBtqKuDNPfQ656f6dQ5ks5uXsTPgaJpZM4WWU1H>
> .
>


---
