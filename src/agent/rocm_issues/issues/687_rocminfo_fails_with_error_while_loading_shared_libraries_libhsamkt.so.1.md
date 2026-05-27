# rocminfo fails with "error while loading shared libraries: libhsamkt.so.1"

> **Issue #687**
> **状态**: closed
> **创建时间**: 2019-01-24T12:53:12Z
> **更新时间**: 2019-01-25T04:28:56Z
> **关闭时间**: 2019-01-25T04:27:49Z
> **作者**: eatthoselemons
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/687

## 描述

Trying to run `/opt/rocm/bin/rocminfo` and getting the following output: `/opt/rocm/bin/rocminfo: error while loading shared libraries: libhsakmt.so.1: cannot open shared object file: No such file or directory`

I have removed all of rocm with `sudo apt-get autoremove rocm-dkms` a few times and done a few restarts between that, and tried to manually install some of the components individually

All the debug that should be needed:

`uname -a`
`Linux machine-learning 4.17.0-0.bpo.1-amd64 #1 SMP Debian 4.17.8-1~bpo9+1 (2018-07-23) x86_64 GNU/Linux`

`dkms-status`
`amdgpu, 2.0-89: added`

`lsmod | grep amdgpu`

`amdgpu               3125248  0

chash                  16384  1 amdgpu
gpu_sched              28672  1 amdgpu
ttm                   126976  1 amdgpu
drm_kms_helper        196608  1 amdgpu
drm                   462848  4 gpu_sched,drm_kms_helper,amdgpu,ttm
i2c_algo_bit           16384  1 amdgpu`


`lsmod | grep amdkfd`
None

`lspci | grep VGA`

`28:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)`

`lspci -vvv`

`28:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1) (prog-if 00 [VGA controller])

	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device 6b76
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 10
	Region 0: Memory at e0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at f0000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at f000 [size=256]
	Region 5: Memory at fe600000 (32-bit, non-prefetchable) [size=512K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel modules: amdgpu`

`lspci -tv`

`-[0000:00]-+-00.0  Advanced Micro Devices, Inc. [AMD] Device 1450

           +-00.2  Advanced Micro Devices, Inc. [AMD] Device 1451
           +-01.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-01.1-[01]----00.0  Device 1987:5007
           +-01.3-[03-25]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 43bb
           |               +-00.1  Advanced Micro Devices, Inc. [AMD] Device 43b7
           |               \-00.2-[1d-25]--+-00.0-[1e]--
           |                               +-01.0-[1f]--
           |                               +-04.0-[22]--
           |                               +-05.0-[23]--
           |                               +-06.0-[24]----00.0  ASMedia Technology Inc. ASM1062 Serial ATA Controller
           |                               \-07.0-[25]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           +-02.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-03.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-03.1-[26-28]----00.0-[27-28]----00.0-[28]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 687f
           |                                            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
           +-04.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-07.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-07.1-[29]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 145a
           |            +-00.2  Advanced Micro Devices, Inc. [AMD] Device 1456
           |            \-00.3  Advanced Micro Devices, Inc. [AMD] Device 145c
           +-08.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-08.1-[2a]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 1455
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
           \-18.7  Advanced Micro Devices, Inc. [AMD] Device 1467`

`lspci -n`

`00:00.0 0600: 1022:1450

00:00.2 0806: 1022:1451
00:01.0 0600: 1022:1452
00:01.1 0604: 1022:1453
00:01.3 0604: 1022:1453
00:02.0 0600: 1022:1452
00:03.0 0600: 1022:1452
00:03.1 0604: 1022:1453
00:04.0 0600: 1022:1452
00:07.0 0600: 1022:1452
00:07.1 0604: 1022:1454
00:08.0 0600: 1022:1452
00:08.1 0604: 1022:1454
00:14.0 0c05: 1022:790b (rev 59)
00:14.3 0601: 1022:790e (rev 51)
00:18.0 0600: 1022:1460
00:18.1 0600: 1022:1461
00:18.2 0600: 1022:1462
00:18.3 0600: 1022:1463
00:18.4 0600: 1022:1464
00:18.5 0600: 1022:1465
00:18.6 0600: 1022:1466
00:18.7 0600: 1022:1467
01:00.0 0108: 1987:5007 (rev 01)
03:00.0 0c03: 1022:43bb (rev 02)
03:00.1 0106: 1022:43b7 (rev 02)
03:00.2 0604: 1022:43b2 (rev 02)
1d:00.0 0604: 1022:43b4 (rev 02)
1d:01.0 0604: 1022:43b4 (rev 02)
1d:04.0 0604: 1022:43b4 (rev 02)
1d:05.0 0604: 1022:43b4 (rev 02)
1d:06.0 0604: 1022:43b4 (rev 02)
1d:07.0 0604: 1022:43b4 (rev 02)
24:00.0 0106: 1b21:0612 (rev 02)
25:00.0 0200: 10ec:8168 (rev 11)
26:00.0 0604: 1022:1470 (rev c1)
27:00.0 0604: 1022:1471
28:00.0 0300: 1002:687f (rev c1)
28:00.1 0403: 1002:aaf8
29:00.0 1300: 1022:145a
29:00.2 1080: 1022:1456
29:00.3 0c03: 1022:145c
2a:00.0 1300: 1022:1455
2a:00.2 0106: 1022:7901 (rev 51)
2a:00.3 0403: 1022:1457`

`dmesg | grep amdgpu`

`[    3.365626] [drm] amdgpu kernel modesetting enabled.
[    3.365870] [drm:amdgpu_pci_probe [amdgpu]] *ERROR* amdgpu requires firmware installed`





---

## 评论 (1 条)

### 评论 #1 — eatthoselemons (2019-01-25T04:28:56Z)

Debian with kernel 4.17 doesn't work, creates the errors above (was not a fresh installation so it might work from a fresh debian 9 install)

Worked with Ubuntu 18.04 LTS fresh install

---
