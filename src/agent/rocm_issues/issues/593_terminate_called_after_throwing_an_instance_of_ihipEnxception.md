# terminate called after throwing an instance of ihipEnxception

> **Issue #593**
> **状态**: closed
> **创建时间**: 2018-10-29T14:32:17Z
> **更新时间**: 2018-10-29T20:02:21Z
> **关闭时间**: 2018-10-29T20:02:21Z
> **作者**: ishanshukla97
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/593

## 描述

Getting this error while running tensorflow. I recently did a clean install of ubuntu and installed rocm following their instructions page.
Error:

```
Using TensorFlow backend.
Epoch 1/1
2018-10-29 19:10:54.225630: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
terminate called after throwing an instance of 'ihipException'
  what():  std::exception
Aborted (core dumped)
```

My system specs:
- CPU: Ryzen 5 1600
- GPU: Rx570 in PCIe x16 slot, Rx570 in PCIe x8 slot
- Ubuntu 16.01 LTS

```
lspci -vnn | grep VGA -A 12
06:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:67df] (rev ef) (prog-if 00 [VGA controller])
	Subsystem: ASUSTeK Computer Inc. Device [1043:04c2]
	Flags: bus master, fast devsel, latency 0, IRQ 44
	Memory at e0000000 (64-bit, prefetchable) [size=256M]
	Memory at f0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at d000 [size=256]
	Memory at fe500000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at fe540000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

06:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:aaf0]
--
07:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:67df] (rev ef) (prog-if 00 [VGA controller])
	Subsystem: ASUSTeK Computer Inc. Device [1043:04c2]
	Flags: bus master, fast devsel, latency 0, IRQ 46
	Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Memory at d0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at f000 [size=256]
	Memory at fe900000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```

```
lsmod | grep amdgpu
amdgpu               2732032  65
chash                  16384  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   106496  1 amdgpu
drm_kms_helper        172032  1 amdgpu
drm                   401408  10 amdgpu,ttm,drm_kms_helper
```

```
lsmod | grep amdkfd
amdkfd                180224  2
amd_iommu_v2           20480  1 amdkfd
```

```
lspci | grep VGA
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev ef)
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev ef)`
```

```
$ lspci -tv
-[0000:00]-+-00.0  Advanced Micro Devices, Inc. [AMD] Device 1450
           +-01.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-01.3-[01-06]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 43bb
           |               +-00.1  Advanced Micro Devices, Inc. [AMD] Device 43b7
           |               \-00.2-[02-06]--+-00.0-[03]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           |                               +-01.0-[04-05]----00.0-[05]--
           |                               \-04.0-[06]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |                                            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-02.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-03.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-03.1-[07]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-04.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-07.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-07.1-[08]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 145a
           |            +-00.2  Advanced Micro Devices, Inc. [AMD] Device 1456
           |            \-00.3  Advanced Micro Devices, Inc. [AMD] Device 145c
           +-08.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-08.1-[09]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 1455
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

```
$ dmesg
[    0.000000] Linux version 4.15.0-36-generic (buildd@lcy01-amd64-017) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)) #39~16.04.1-Ubuntu SMP Tue Sep 25 08:59:23 UTC 2018 (Ubuntu 4.15.0-36.39~16.04.1-generic 4.15.18)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-36-generic root=UUID=879a7a2a-ec16-4fe9-8c58-a9dbf7b00726 ro quiet splash vt.handoff=7
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'compacted' format.
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009d3ff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009d400-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x0000000003ffffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000004000000-0x000000000400ffff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x0000000004010000-0x0000000009bfffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000009c00000-0x0000000009ffffff] reserved
[    0.000000] BIOS-e820: [mem 0x000000000a000000-0x00000000a70f0fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000a70f1000-0x00000000a7109fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000a710a000-0x00000000ba51ffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000ba520000-0x00000000ba687fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ba688000-0x00000000ba691fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000ba692000-0x00000000ba79cfff] usable
[    0.000000] BIOS-e820: [mem 0x00000000ba79d000-0x00000000bab58fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000bab59000-0x00000000bba11fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000bba12000-0x00000000bdffffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000be000000-0x00000000bfffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fea00000-0x00000000fea0ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000feb80000-0x00000000fec01fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec10000-0x00000000fec10fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec30000-0x00000000fec30fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed40000-0x00000000fed44fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed80000-0x00000000fed8ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fedc2000-0x00000000fedcffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fedd4000-0x00000000fedd5fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000feefffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000023f37ffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] SMBIOS 3.0.0 present.
[    0.000000] DMI: System manufacturer System Product Name/PRIME B350-PLUS, BIOS 3401 12/04/2017
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x23f380 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: uncachable
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF write-through
[    0.000000]   C0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 000000000000 mask FFFF80000000 write-back
[    0.000000]   1 base 000080000000 mask FFFFC0000000 write-back
[    0.000000]   2 disabled
[    0.000000]   3 disabled
[    0.000000]   4 disabled
[    0.000000]   5 disabled
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000] TOM2: 0000000240000000 aka 9216M
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000000] e820: update [mem 0xc0000000-0xffffffff] usable ==> reserved
[    0.000000] e820: last_pfn = 0xbe000 max_arch_pfn = 0x400000000
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [        (ptrval)] 97000 size 24576
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x166b3f000, 0x166b3ffff] PGTABLE
[    0.000000] BRK [0x166b40000, 0x166b40fff] PGTABLE
[    0.000000] BRK [0x166b41000, 0x166b41fff] PGTABLE
[    0.000000] BRK [0x166b42000, 0x166b42fff] PGTABLE
[    0.000000] BRK [0x166b43000, 0x166b43fff] PGTABLE
[    0.000000] BRK [0x166b44000, 0x166b44fff] PGTABLE
[    0.000000] BRK [0x166b45000, 0x166b45fff] PGTABLE
[    0.000000] BRK [0x166b46000, 0x166b46fff] PGTABLE
[    0.000000] BRK [0x166b47000, 0x166b47fff] PGTABLE
[    0.000000] BRK [0x166b48000, 0x166b48fff] PGTABLE
[    0.000000] BRK [0x166b49000, 0x166b49fff] PGTABLE
[    0.000000] BRK [0x166b4a000, 0x166b4afff] PGTABLE
[    0.000000] RAMDISK: [mem 0x3180a000-0x34bfcfff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x00000000000F05B0 000024 (v02 ALASKA)
[    0.000000] ACPI: XSDT 0x00000000A70F1090 00009C (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x00000000A70F9DC0 000114 (v06 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI BIOS Warning (bug): Optional FADT field Pm2ControlBlock has valid Length but zero Address: 0x0000000000000000/0x1 (20170831/tbfadt-658)
[    0.000000] ACPI: DSDT 0x00000000A70F11C8 008BF2 (v02 ALASKA A M I    01072009 INTL 20120913)
[    0.000000] ACPI: FACS 0x00000000BAB41E00 000040
[    0.000000] ACPI: APIC 0x00000000A70F9ED8 0000DE (v03 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FPDT 0x00000000A70F9FB8 000044 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FIDT 0x00000000A70FA000 00009C (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: SSDT 0x00000000A7108048 00195E (v01 AMD    AmdTable 00000001 INTL 20120913)
[    0.000000] ACPI: SSDT 0x00000000A70FA0F8 008C4C (v02 AMD    AMD ALIB 00000002 MSFT 04000000)
[    0.000000] ACPI: SSDT 0x00000000A7102D48 002AC4 (v01 AMD    AMD AOD  00000001 INTL 20120913)
[    0.000000] ACPI: MCFG 0x00000000A7105810 00003C (v01 ALASKA A M I    01072009 MSFT 00010013)
[    0.000000] ACPI: SSDT 0x00000000A7105850 001A58 (v01 AMD    AMD CPU  00000001 AMD  00000001)
[    0.000000] ACPI: CRAT 0x00000000A71072A8 000BD0 (v01 AMD    AMD CRAT 00000001 AMD  00000001)
[    0.000000] ACPI: CDIT 0x00000000A7107E78 000029 (v01 AMD    AMD CDIT 00000001 AMD  00000001)
[    0.000000] ACPI: HPET 0x00000000A7107EA8 000038 (v01 ALASKA A M I    01072009 AMI  00000005)
[    0.000000] ACPI: SSDT 0x00000000A7107EE0 000024 (v01 AMDFCH FCHZP    00001000 INTL 20120913)
[    0.000000] ACPI: UEFI 0x00000000A7107F08 000042 (v01                 00000000      00000000)
[    0.000000] ACPI: SSDT 0x00000000A7107F50 0000F8 (v01 AMD    AMD PT   00001000 INTL 20120913)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x000000023f37ffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x23f355000-0x23f37ffff]
[    0.000000] tsc: Fast TSC calibration failed
[    0.000000] tsc: Using PIT calibration value
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000023f37ffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x000000000009cfff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x0000000003ffffff]
[    0.000000]   node   0: [mem 0x0000000004010000-0x0000000009bfffff]
[    0.000000]   node   0: [mem 0x000000000a000000-0x00000000a70f0fff]
[    0.000000]   node   0: [mem 0x00000000a710a000-0x00000000ba51ffff]
[    0.000000]   node   0: [mem 0x00000000ba692000-0x00000000ba79cfff]
[    0.000000]   node   0: [mem 0x00000000bba12000-0x00000000bdffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000023f37ffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x000000023f37ffff]
[    0.000000] On node 0 totalpages: 2079500
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 21 pages reserved
[    0.000000]   DMA zone: 3996 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 12000 pages used for memmap
[    0.000000]   DMA32 zone: 767984 pages, LIFO batch:31
[    0.000000]   Normal zone: 20430 pages used for memmap
[    0.000000]   Normal zone: 1307520 pages, LIFO batch:31
[    0.000000] Reserved but unavailable: 100 pages
[    0.000000] ACPI: PM-Timer IO Port: 0x808
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0xff] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 13, version 33, address 0xfec00000, GSI 0-23
[    0.000000] IOAPIC[1]: apic_id 14, version 33, address 0xfec01000, GSI 24-55
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 low level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x10228201 base: 0xfed00000
[    0.000000] smpboot: Allowing 16 CPUs, 4 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009d000-0x0009dfff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009e000-0x0009ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000dffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000e0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x04000000-0x0400ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x09c00000-0x09ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xa70f1000-0xa7109fff]
[    0.000000] PM: Registered nosave memory: [mem 0xba520000-0xba687fff]
[    0.000000] PM: Registered nosave memory: [mem 0xba688000-0xba691fff]
[    0.000000] PM: Registered nosave memory: [mem 0xba79d000-0xbab58fff]
[    0.000000] PM: Registered nosave memory: [mem 0xbab59000-0xbba11fff]
[    0.000000] PM: Registered nosave memory: [mem 0xbe000000-0xbfffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xc0000000-0xf7ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf8000000-0xfbffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfc000000-0xfe9fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfea00000-0xfea0ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfea10000-0xfeb7ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfeb80000-0xfec01fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec02000-0xfec0ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec10000-0xfec10fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec11000-0xfec2ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec30000-0xfec30fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec31000-0xfecfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed00000-0xfed00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed01000-0xfed3ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed40000-0xfed44fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed45000-0xfed7ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed80000-0xfed8ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed90000-0xfedc1fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedc2000-0xfedcffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd0000-0xfedd3fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd4000-0xfedd5fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd6000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfeefffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfef00000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] e820: [mem 0xc0000000-0xf7ffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] random: get_random_bytes called from start_kernel+0x99/0x51b with crng_init=0
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:16 nr_cpu_ids:16 nr_node_ids:1
[    0.000000] percpu: Embedded 46 pages/cpu @        (ptrval) s151552 r8192 d28672 u262144
[    0.000000] pcpu-alloc: s151552 r8192 d28672 u262144 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 00 01 02 03 04 05 06 07 [0] 08 09 10 11 12 13 14 15 
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 2046985
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-36-generic root=UUID=879a7a2a-ec16-4fe9-8c58-a9dbf7b00726 ro quiet splash vt.handoff=7
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 8036564K/8318000K available (12300K kernel code, 2471K rwdata, 4260K rodata, 2408K init, 2416K bss, 281436K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=16, Nodes=1
[    0.000000] ftrace: allocating 39175 entries in 154 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=16.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=16
[    0.000000] NR_IRQS: 524544, nr_irqs: 1096, preallocated irqs: 16
[    0.000000] spurious 8259A interrupt: IRQ7.
[    0.000000] vt handoff: transparent VT on vt#7
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] ACPI: Core revision 20170831
[    0.000000] ACPI: 7 ACPI AML tables successfully acquired and loaded
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484873504 ns
[    0.000000] hpet clockevent registered
[    0.000000] APIC: Switch to symmetric I/O mode setup
[    0.000000] Switched APIC routing to physical flat.
[    0.000000] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.020000] tsc: Fast TSC calibration failed
[    0.028000] tsc: PIT calibration matches HPET. 1 loops
[    0.028000] tsc: Detected 3193.540 MHz processor
[    0.028000] Calibrating delay loop (skipped), value calculated using timer frequency.. 6387.08 BogoMIPS (lpj=12774160)
[    0.028000] pid_max: default: 32768 minimum: 301
[    0.028000] Security Framework initialized
[    0.028000] Yama: becoming mindful.
[    0.028000] AppArmor: AppArmor initialized
[    0.028000] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.028000] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes)
[    0.028000] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.028000] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.028000] mce: CPU supports 23 MCE banks
[    0.028000] LVT offset 1 assigned for vector 0xf9
[    0.028000] LVT offset 2 assigned for vector 0xf4
[    0.028000] Last level iTLB entries: 4KB 1024, 2MB 1024, 4MB 512
[    0.028000] Last level dTLB entries: 4KB 1536, 2MB 1536, 4MB 768, 1GB 0
[    0.028000] Spectre V2 : Mitigation: Full AMD retpoline
[    0.028000] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    0.028000] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.038643] Freeing SMP alternatives memory: 36K
[    0.044000] smpboot: CPU0: AMD Ryzen 5 1600 Six-Core Processor (family: 0x17, model: 0x1, stepping: 0x1)
[    0.044000] Performance Events: Fam17h core perfctr, AMD PMU driver.
[    0.044000] ... version:                0
[    0.044000] ... bit width:              48
[    0.044000] ... generic registers:      6
[    0.044000] ... value mask:             0000ffffffffffff
[    0.044000] ... max period:             00007fffffffffff
[    0.044000] ... fixed-purpose events:   0
[    0.044000] ... event mask:             000000000000003f
[    0.044000] Hierarchical SRCU implementation.
[    0.044000] smp: Bringing up secondary CPUs ...
[    0.044000] x86: Booting SMP configuration:
[    0.044000] .... node  #0, CPUs:        #1
[    0.044000] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.044000]   #2  #3  #4  #5  #6  #7  #8  #9 #10 #11
[    0.064049] smp: Brought up 1 node, 12 CPUs
[    0.064049] smpboot: Max logical packages: 2
[    0.064049] smpboot: Total of 12 processors activated (76644.96 BogoMIPS)
[    0.065106] devtmpfs: initialized
[    0.065106] x86/mm: Memory block size: 128MB
[    0.065106] evm: security.selinux
[    0.065106] evm: security.SMACK64
[    0.065106] evm: security.SMACK64EXEC
[    0.065106] evm: security.SMACK64TRANSMUTE
[    0.065106] evm: security.SMACK64MMAP
[    0.065106] evm: security.apparmor
[    0.065106] evm: security.ima
[    0.065106] evm: security.capability
[    0.068022] PM: Registering ACPI NVS region [mem 0x04000000-0x0400ffff] (65536 bytes)
[    0.068024] PM: Registering ACPI NVS region [mem 0xba79d000-0xbab58fff] (3915776 bytes)
[    0.068119] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.068119] futex hash table entries: 4096 (order: 6, 262144 bytes)
[    0.068119] pinctrl core: initialized pinctrl subsystem
[    0.068219] RTC time: 16:51:29, date: 10/29/18
[    0.068331] NET: Registered protocol family 16
[    0.068387] audit: initializing netlink subsys (disabled)
[    0.068393] audit: type=2000 audit(1540831889.068:1): state=initialized audit_enabled=0 res=1
[    0.068393] cpuidle: using governor ladder
[    0.068393] cpuidle: using governor menu
[    0.068393] ACPI: bus type PCI registered
[    0.068393] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.068393] PCI: MMCONFIG for domain 0000 [bus 00-3f] at [mem 0xf8000000-0xfbffffff] (base 0xf8000000)
[    0.068393] PCI: MMCONFIG at [mem 0xf8000000-0xfbffffff] reserved in E820
[    0.068393] PCI: Using configuration type 1 for base access
[    0.068393] mtrr: your CPUs had inconsistent variable MTRR settings
[    0.068393] mtrr: probably your BIOS does not setup all CPUs.
[    0.068393] mtrr: corrected configuration.
[    0.069041] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.069041] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.069041] ACPI: Added _OSI(Module Device)
[    0.069041] ACPI: Added _OSI(Processor Device)
[    0.069041] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.069041] ACPI: Added _OSI(Processor Aggregator Device)
[    0.069041] ACPI: Added _OSI(Linux-Dell-Video)
[    0.069041] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    0.069041] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.069041] ACPI: Executed 2 blocks of module-level executable AML code
[    0.072456] ACPI Error: Needed [Integer/String/Buffer], found [Region]         (ptrval) (20170831/exresop-424)
[    0.072461] Executing subtree for Buffer/Package/Region
[    0.072462] ACPI Exception: AE_AML_OPERAND_TYPE, Could not execute arguments for [IOB2] (Region) (20170831/nsinit-426)
[    0.081392] ACPI: Interpreter enabled
[    0.081406] ACPI: (supports S0 S3 S4 S5)
[    0.081407] ACPI: Using IOAPIC for interrupt routing
[    0.081691] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.081992] ACPI: Enabled 4 GPEs in block 00 to 1F
[    0.091994] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.091998] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.092195] acpi PNP0A08:00: _OSC: platform does not support [PCIeHotplug]
[    0.092381] acpi PNP0A08:00: _OSC: OS now controls [PME AER PCIeCapability]
[    0.092393] acpi PNP0A08:00: [Firmware Info]: MMCONFIG for domain 0000 [bus 00-3f] only partially covers this bridge
[    0.092756] PCI host bridge to bus 0000:00
[    0.092758] pci_bus 0000:00: root bus resource [io  0x0000-0x03af window]
[    0.092760] pci_bus 0000:00: root bus resource [io  0x03e0-0x0cf7 window]
[    0.092761] pci_bus 0000:00: root bus resource [io  0x03b0-0x03df window]
[    0.092762] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.092763] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.092764] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000dffff window]
[    0.092765] pci_bus 0000:00: root bus resource [mem 0xc0000000-0xfec2ffff window]
[    0.092766] pci_bus 0000:00: root bus resource [mem 0xfee00000-0xffffffff window]
[    0.092767] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.092773] pci 0000:00:00.0: [1022:1450] type 00 class 0x060000
[    0.092866] pci 0000:00:01.0: [1022:1452] type 00 class 0x060000
[    0.092938] pci 0000:00:01.3: [1022:1453] type 01 class 0x060400
[    0.093056] pci 0000:00:01.3: PME# supported from D0 D3hot D3cold
[    0.093143] pci 0000:00:02.0: [1022:1452] type 00 class 0x060000
[    0.093230] pci 0000:00:03.0: [1022:1452] type 00 class 0x060000
[    0.093300] pci 0000:00:03.1: [1022:1453] type 01 class 0x060400
[    0.093414] pci 0000:00:03.1: PME# supported from D0 D3hot D3cold
[    0.093502] pci 0000:00:04.0: [1022:1452] type 00 class 0x060000
[    0.093588] pci 0000:00:07.0: [1022:1452] type 00 class 0x060000
[    0.093655] pci 0000:00:07.1: [1022:1454] type 01 class 0x060400
[    0.093686] pci 0000:00:07.1: enabling Extended Tags
[    0.093770] pci 0000:00:07.1: PME# supported from D0 D3hot D3cold
[    0.093856] pci 0000:00:08.0: [1022:1452] type 00 class 0x060000
[    0.093922] pci 0000:00:08.1: [1022:1454] type 01 class 0x060400
[    0.093956] pci 0000:00:08.1: enabling Extended Tags
[    0.094047] pci 0000:00:08.1: PME# supported from D0 D3hot D3cold
[    0.094167] pci 0000:00:14.0: [1022:790b] type 00 class 0x0c0500
[    0.094390] pci 0000:00:14.3: [1022:790e] type 00 class 0x060100
[    0.094617] pci 0000:00:18.0: [1022:1460] type 00 class 0x060000
[    0.094682] pci 0000:00:18.1: [1022:1461] type 00 class 0x060000
[    0.094746] pci 0000:00:18.2: [1022:1462] type 00 class 0x060000
[    0.094800] pci 0000:00:18.3: [1022:1463] type 00 class 0x060000
[    0.094852] pci 0000:00:18.4: [1022:1464] type 00 class 0x060000
[    0.094905] pci 0000:00:18.5: [1022:1465] type 00 class 0x060000
[    0.094962] pci 0000:00:18.6: [1022:1466] type 00 class 0x060000
[    0.095019] pci 0000:00:18.7: [1022:1467] type 00 class 0x060000
[    0.095161] pci 0000:01:00.0: [1022:43bb] type 00 class 0x0c0330
[    0.095183] pci 0000:01:00.0: reg 0x10: [mem 0xfe7a0000-0xfe7a7fff 64bit]
[    0.095257] pci 0000:01:00.0: PME# supported from D3hot D3cold
[    0.095313] pci 0000:01:00.1: [1022:43b7] type 00 class 0x010601
[    0.095358] pci 0000:01:00.1: reg 0x24: [mem 0xfe780000-0xfe79ffff]
[    0.095365] pci 0000:01:00.1: reg 0x30: [mem 0xfe700000-0xfe77ffff pref]
[    0.095402] pci 0000:01:00.1: PME# supported from D3hot D3cold
[    0.095445] pci 0000:01:00.2: [1022:43b2] type 01 class 0x060400
[    0.095517] pci 0000:01:00.2: PME# supported from D3hot D3cold
[    0.104023] pci 0000:00:01.3: PCI bridge to [bus 01-06]
[    0.104027] pci 0000:00:01.3:   bridge window [io  0xd000-0xefff]
[    0.104029] pci 0000:00:01.3:   bridge window [mem 0xfe500000-0xfe7fffff]
[    0.104032] pci 0000:00:01.3:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.104148] pci 0000:02:00.0: [1022:43b4] type 01 class 0x060400
[    0.104235] pci 0000:02:00.0: PME# supported from D3hot D3cold
[    0.104308] pci 0000:02:01.0: [1022:43b4] type 01 class 0x060400
[    0.104394] pci 0000:02:01.0: PME# supported from D3hot D3cold
[    0.104462] pci 0000:02:04.0: [1022:43b4] type 01 class 0x060400
[    0.104546] pci 0000:02:04.0: PME# supported from D3hot D3cold
[    0.104618] pci 0000:01:00.2: PCI bridge to [bus 02-06]
[    0.104623] pci 0000:01:00.2:   bridge window [io  0xd000-0xefff]
[    0.104625] pci 0000:01:00.2:   bridge window [mem 0xfe500000-0xfe6fffff]
[    0.104629] pci 0000:01:00.2:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.104688] pci 0000:03:00.0: [10ec:8168] type 00 class 0x020000
[    0.104728] pci 0000:03:00.0: reg 0x10: [io  0xe000-0xe0ff]
[    0.104764] pci 0000:03:00.0: reg 0x18: [mem 0xfe604000-0xfe604fff 64bit]
[    0.104785] pci 0000:03:00.0: reg 0x20: [mem 0xfe600000-0xfe603fff 64bit]
[    0.104911] pci 0000:03:00.0: supports D1 D2
[    0.104912] pci 0000:03:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.116040] pci 0000:02:00.0: PCI bridge to [bus 03]
[    0.116046] pci 0000:02:00.0:   bridge window [io  0xe000-0xefff]
[    0.116049] pci 0000:02:00.0:   bridge window [mem 0xfe600000-0xfe6fffff]
[    0.116130] pci 0000:04:00.0: [1b21:1080] type 01 class 0x060400
[    0.116313] pci 0000:04:00.0: supports D1 D2
[    0.116314] pci 0000:04:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.128025] pci 0000:02:01.0: PCI bridge to [bus 04-05]
[    0.128204] pci 0000:04:00.0: PCI bridge to [bus 05]
[    0.128299] pci 0000:06:00.0: [1002:67df] type 00 class 0x030000
[    0.128353] pci 0000:06:00.0: reg 0x10: [mem 0xe0000000-0xefffffff 64bit pref]
[    0.128370] pci 0000:06:00.0: reg 0x18: [mem 0xf0000000-0xf01fffff 64bit pref]
[    0.128380] pci 0000:06:00.0: reg 0x20: [io  0xd000-0xd0ff]
[    0.128391] pci 0000:06:00.0: reg 0x24: [mem 0xfe500000-0xfe53ffff]
[    0.128401] pci 0000:06:00.0: reg 0x30: [mem 0xfe540000-0xfe55ffff pref]
[    0.128536] pci 0000:06:00.0: supports D1 D2
[    0.128537] pci 0000:06:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.128650] pci 0000:06:00.1: [1002:aaf0] type 00 class 0x040300
[    0.128694] pci 0000:06:00.1: reg 0x10: [mem 0xfe560000-0xfe563fff 64bit]
[    0.128850] pci 0000:06:00.1: supports D1 D2
[    0.140052] pci 0000:02:04.0: PCI bridge to [bus 06]
[    0.140058] pci 0000:02:04.0:   bridge window [io  0xd000-0xdfff]
[    0.140061] pci 0000:02:04.0:   bridge window [mem 0xfe500000-0xfe5fffff]
[    0.140066] pci 0000:02:04.0:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.140173] pci 0000:07:00.0: [1002:67df] type 00 class 0x030000
[    0.140197] pci 0000:07:00.0: reg 0x10: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.140206] pci 0000:07:00.0: reg 0x18: [mem 0xd0000000-0xd01fffff 64bit pref]
[    0.140212] pci 0000:07:00.0: reg 0x20: [io  0xf000-0xf0ff]
[    0.140218] pci 0000:07:00.0: reg 0x24: [mem 0xfe900000-0xfe93ffff]
[    0.140225] pci 0000:07:00.0: reg 0x30: [mem 0xfe940000-0xfe95ffff pref]
[    0.140280] pci 0000:07:00.0: supports D1 D2
[    0.140281] pci 0000:07:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.140363] pci 0000:07:00.1: [1002:aaf0] type 00 class 0x040300
[    0.140382] pci 0000:07:00.1: reg 0x10: [mem 0xfe960000-0xfe963fff 64bit]
[    0.140449] pci 0000:07:00.1: supports D1 D2
[    0.152026] pci 0000:00:03.1: PCI bridge to [bus 07]
[    0.152030] pci 0000:00:03.1:   bridge window [io  0xf000-0xffff]
[    0.152032] pci 0000:00:03.1:   bridge window [mem 0xfe900000-0xfe9fffff]
[    0.152035] pci 0000:00:03.1:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.152125] pci 0000:08:00.0: [1022:145a] type 00 class 0x130000
[    0.152159] pci 0000:08:00.0: enabling Extended Tags
[    0.152227] pci 0000:08:00.2: [1022:1456] type 00 class 0x108000
[    0.152245] pci 0000:08:00.2: reg 0x18: [mem 0xfe300000-0xfe3fffff]
[    0.152256] pci 0000:08:00.2: reg 0x24: [mem 0xfe400000-0xfe401fff]
[    0.152263] pci 0000:08:00.2: enabling Extended Tags
[    0.152333] pci 0000:08:00.3: [1022:145c] type 00 class 0x0c0330
[    0.152346] pci 0000:08:00.3: reg 0x10: [mem 0xfe200000-0xfe2fffff 64bit]
[    0.152367] pci 0000:08:00.3: enabling Extended Tags
[    0.152394] pci 0000:08:00.3: PME# supported from D0 D3hot D3cold
[    0.152453] pci 0000:00:07.1: PCI bridge to [bus 08]
[    0.152457] pci 0000:00:07.1:   bridge window [mem 0xfe200000-0xfe4fffff]
[    0.152542] pci 0000:09:00.0: [1022:1455] type 00 class 0x130000
[    0.152575] pci 0000:09:00.0: enabling Extended Tags
[    0.152634] pci 0000:09:00.2: [1022:7901] type 00 class 0x010601
[    0.152662] pci 0000:09:00.2: reg 0x24: [mem 0xfe808000-0xfe808fff]
[    0.152669] pci 0000:09:00.2: enabling Extended Tags
[    0.152697] pci 0000:09:00.2: PME# supported from D3hot D3cold
[    0.152738] pci 0000:09:00.3: [1022:1457] type 00 class 0x040300
[    0.152748] pci 0000:09:00.3: reg 0x10: [mem 0xfe800000-0xfe807fff]
[    0.152772] pci 0000:09:00.3: enabling Extended Tags
[    0.152799] pci 0000:09:00.3: PME# supported from D0 D3hot D3cold
[    0.152855] pci 0000:00:08.1: PCI bridge to [bus 09]
[    0.152858] pci 0000:00:08.1:   bridge window [mem 0xfe800000-0xfe8fffff]
[    0.153241] ACPI: PCI Interrupt Link [LNKA] (IRQs 4 5 7 10 11 14 15) *0
[    0.153301] ACPI: PCI Interrupt Link [LNKB] (IRQs 4 5 7 10 11 14 15) *0
[    0.153355] ACPI: PCI Interrupt Link [LNKC] (IRQs 4 5 7 10 11 14 15) *0
[    0.153420] ACPI: PCI Interrupt Link [LNKD] (IRQs 4 5 7 10 11 14 15) *0
[    0.153480] ACPI: PCI Interrupt Link [LNKE] (IRQs 4 5 7 10 11 14 15) *0
[    0.153529] ACPI: PCI Interrupt Link [LNKF] (IRQs 4 5 7 10 11 14 15) *0
[    0.153578] ACPI: PCI Interrupt Link [LNKG] (IRQs 4 5 7 10 11 14 15) *0
[    0.153627] ACPI: PCI Interrupt Link [LNKH] (IRQs 4 5 7 10 11 14 15) *0
[    0.154295] SCSI subsystem initialized
[    0.154309] libata version 3.00 loaded.
[    0.154309] pci 0000:06:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    0.154309] pci 0000:07:00.0: vgaarb: setting as boot VGA device
[    0.154309] pci 0000:07:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.154309] pci 0000:07:00.0: vgaarb: bridge control possible
[    0.154309] pci 0000:06:00.0: vgaarb: bridge control possible
[    0.154309] vgaarb: loaded
[    0.154309] ACPI: bus type USB registered
[    0.154309] usbcore: registered new interface driver usbfs
[    0.154309] usbcore: registered new interface driver hub
[    0.154309] usbcore: registered new device driver usb
[    0.154309] EDAC MC: Ver: 3.0.0
[    0.154309] PCI: Using ACPI for IRQ routing
[    0.158977] PCI: pci_cache_line_size set to 64 bytes
[    0.159040] e820: reserve RAM buffer [mem 0x0009d400-0x0009ffff]
[    0.159041] e820: reserve RAM buffer [mem 0x09c00000-0x0bffffff]
[    0.159042] e820: reserve RAM buffer [mem 0xa70f1000-0xa7ffffff]
[    0.159042] e820: reserve RAM buffer [mem 0xba520000-0xbbffffff]
[    0.159043] e820: reserve RAM buffer [mem 0xba79d000-0xbbffffff]
[    0.159043] e820: reserve RAM buffer [mem 0xbe000000-0xbfffffff]
[    0.159044] e820: reserve RAM buffer [mem 0x23f380000-0x23fffffff]
[    0.159107] NetLabel: Initializing
[    0.159108] NetLabel:  domain hash size = 128
[    0.159108] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.159118] NetLabel:  unlabeled traffic allowed by default
[    0.159129] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0
[    0.159129] hpet0: 3 comparators, 32-bit 14.318180 MHz counter
[    0.161046] clocksource: Switched to clocksource hpet
[    0.168058] VFS: Disk quotas dquot_6.6.0
[    0.168074] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.168170] AppArmor: AppArmor Filesystem Enabled
[    0.168197] pnp: PnP ACPI init
[    0.168348] system 00:00: [mem 0xf8000000-0xfbffffff] has been reserved
[    0.168352] system 00:00: Plug and Play ACPI device, IDs PNP0c01 (active)
[    0.168418] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.168535] pnp 00:02: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.168708] system 00:03: [io  0x0300-0x030f] has been reserved
[    0.168709] system 00:03: [io  0x0230-0x023f] has been reserved
[    0.168710] system 00:03: [io  0x0290-0x029f] has been reserved
[    0.168713] system 00:03: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.169001] pnp 00:04: [dma 0 disabled]
[    0.169043] pnp 00:04: Plug and Play ACPI device, IDs PNP0501 (active)
[    0.169309] system 00:05: [io  0x04d0-0x04d1] has been reserved
[    0.169310] system 00:05: [io  0x040b] has been reserved
[    0.169311] system 00:05: [io  0x04d6] has been reserved
[    0.169312] system 00:05: [io  0x0c00-0x0c01] has been reserved
[    0.169314] system 00:05: [io  0x0c14] has been reserved
[    0.169315] system 00:05: [io  0x0c50-0x0c51] has been reserved
[    0.169316] system 00:05: [io  0x0c52] has been reserved
[    0.169317] system 00:05: [io  0x0c6c] has been reserved
[    0.169318] system 00:05: [io  0x0c6f] has been reserved
[    0.169319] system 00:05: [io  0x0cd0-0x0cd1] has been reserved
[    0.169320] system 00:05: [io  0x0cd2-0x0cd3] has been reserved
[    0.169322] system 00:05: [io  0x0cd4-0x0cd5] has been reserved
[    0.169323] system 00:05: [io  0x0cd6-0x0cd7] has been reserved
[    0.169324] system 00:05: [io  0x0cd8-0x0cdf] has been reserved
[    0.169325] system 00:05: [io  0x0800-0x089f] has been reserved
[    0.169326] system 00:05: [io  0x0b00-0x0b0f] has been reserved
[    0.169327] system 00:05: [io  0x0b20-0x0b3f] has been reserved
[    0.169328] system 00:05: [io  0x0900-0x090f] has been reserved
[    0.169329] system 00:05: [io  0x0910-0x091f] has been reserved
[    0.169331] system 00:05: [mem 0xfec00000-0xfec00fff] could not be reserved
[    0.169333] system 00:05: [mem 0xfec01000-0xfec01fff] could not be reserved
[    0.169334] system 00:05: [mem 0xfedc0000-0xfedc0fff] has been reserved
[    0.169335] system 00:05: [mem 0xfee00000-0xfee00fff] has been reserved
[    0.169337] system 00:05: [mem 0xfed80000-0xfed8ffff] could not be reserved
[    0.169338] system 00:05: [mem 0xfec10000-0xfec10fff] has been reserved
[    0.169340] system 00:05: [mem 0xff000000-0xffffffff] has been reserved
[    0.169343] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.169771] pnp: PnP ACPI: found 6 devices
[    0.176150] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.176208] pci 0000:02:00.0: PCI bridge to [bus 03]
[    0.176211] pci 0000:02:00.0:   bridge window [io  0xe000-0xefff]
[    0.176214] pci 0000:02:00.0:   bridge window [mem 0xfe600000-0xfe6fffff]
[    0.176221] pci 0000:04:00.0: PCI bridge to [bus 05]
[    0.176242] pci 0000:02:01.0: PCI bridge to [bus 04-05]
[    0.176251] pci 0000:02:04.0: PCI bridge to [bus 06]
[    0.176253] pci 0000:02:04.0:   bridge window [io  0xd000-0xdfff]
[    0.176256] pci 0000:02:04.0:   bridge window [mem 0xfe500000-0xfe5fffff]
[    0.176259] pci 0000:02:04.0:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.176263] pci 0000:01:00.2: PCI bridge to [bus 02-06]
[    0.176265] pci 0000:01:00.2:   bridge window [io  0xd000-0xefff]
[    0.176268] pci 0000:01:00.2:   bridge window [mem 0xfe500000-0xfe6fffff]
[    0.176271] pci 0000:01:00.2:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.176275] pci 0000:00:01.3: PCI bridge to [bus 01-06]
[    0.176276] pci 0000:00:01.3:   bridge window [io  0xd000-0xefff]
[    0.176278] pci 0000:00:01.3:   bridge window [mem 0xfe500000-0xfe7fffff]
[    0.176280] pci 0000:00:01.3:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.176283] pci 0000:00:03.1: PCI bridge to [bus 07]
[    0.176284] pci 0000:00:03.1:   bridge window [io  0xf000-0xffff]
[    0.176286] pci 0000:00:03.1:   bridge window [mem 0xfe900000-0xfe9fffff]
[    0.176288] pci 0000:00:03.1:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.176290] pci 0000:00:07.1: PCI bridge to [bus 08]
[    0.176293] pci 0000:00:07.1:   bridge window [mem 0xfe200000-0xfe4fffff]
[    0.176296] pci 0000:00:08.1: PCI bridge to [bus 09]
[    0.176298] pci 0000:00:08.1:   bridge window [mem 0xfe800000-0xfe8fffff]
[    0.176303] pci_bus 0000:00: resource 4 [io  0x0000-0x03af window]
[    0.176304] pci_bus 0000:00: resource 5 [io  0x03e0-0x0cf7 window]
[    0.176305] pci_bus 0000:00: resource 6 [io  0x03b0-0x03df window]
[    0.176306] pci_bus 0000:00: resource 7 [io  0x0d00-0xffff window]
[    0.176307] pci_bus 0000:00: resource 8 [mem 0x000a0000-0x000bffff window]
[    0.176308] pci_bus 0000:00: resource 9 [mem 0x000c0000-0x000dffff window]
[    0.176308] pci_bus 0000:00: resource 10 [mem 0xc0000000-0xfec2ffff window]
[    0.176309] pci_bus 0000:00: resource 11 [mem 0xfee00000-0xffffffff window]
[    0.176310] pci_bus 0000:01: resource 0 [io  0xd000-0xefff]
[    0.176311] pci_bus 0000:01: resource 1 [mem 0xfe500000-0xfe7fffff]
[    0.176312] pci_bus 0000:01: resource 2 [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.176313] pci_bus 0000:02: resource 0 [io  0xd000-0xefff]
[    0.176314] pci_bus 0000:02: resource 1 [mem 0xfe500000-0xfe6fffff]
[    0.176314] pci_bus 0000:02: resource 2 [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.176315] pci_bus 0000:03: resource 0 [io  0xe000-0xefff]
[    0.176316] pci_bus 0000:03: resource 1 [mem 0xfe600000-0xfe6fffff]
[    0.176317] pci_bus 0000:06: resource 0 [io  0xd000-0xdfff]
[    0.176318] pci_bus 0000:06: resource 1 [mem 0xfe500000-0xfe5fffff]
[    0.176319] pci_bus 0000:06: resource 2 [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.176320] pci_bus 0000:07: resource 0 [io  0xf000-0xffff]
[    0.176320] pci_bus 0000:07: resource 1 [mem 0xfe900000-0xfe9fffff]
[    0.176321] pci_bus 0000:07: resource 2 [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.176322] pci_bus 0000:08: resource 1 [mem 0xfe200000-0xfe4fffff]
[    0.176323] pci_bus 0000:09: resource 1 [mem 0xfe800000-0xfe8fffff]
[    0.176395] NET: Registered protocol family 2
[    0.176563] TCP established hash table entries: 65536 (order: 7, 524288 bytes)
[    0.176659] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.176795] TCP: Hash tables configured (established 65536 bind 65536)
[    0.176843] UDP hash table entries: 4096 (order: 5, 131072 bytes)
[    0.176869] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes)
[    0.176929] NET: Registered protocol family 1
[    0.177070] pci 0000:07:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.177175] PCI: CLS 64 bytes, default 64
[    0.177203] Unpacking initramfs...
[    0.735488] Freeing initrd memory: 53196K
[    0.735539] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.735542] software IO TLB [mem 0xb6520000-0xba520000] (64MB) mapped at [        (ptrval)-        (ptrval)]
[    0.735586] amd_uncore: AMD NB counters detected
[    0.735593] amd_uncore: AMD LLC counters detected
[    0.736394] Scanning for low memory corruption every 60 seconds
[    0.737033] Initialise system trusted keyrings
[    0.737044] Key type blacklist registered
[    0.737108] workingset: timestamp_bits=36 max_order=21 bucket_order=0
[    0.737885] zbud: loaded
[    0.738276] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.738400] fuse init (API version 7.26)
[    0.740070] Key type asymmetric registered
[    0.740071] Asymmetric key parser 'x509' registered
[    0.740095] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    0.740147] io scheduler noop registered
[    0.740148] io scheduler deadline registered
[    0.740176] io scheduler cfq registered (default)
[    0.741679] pcieport 0000:00:01.3: AER enabled with IRQ 25
[    0.741720] pcieport 0000:00:03.1: AER enabled with IRQ 26
[    0.741757] pcieport 0000:00:07.1: AER enabled with IRQ 27
[    0.741796] pcieport 0000:00:08.1: AER enabled with IRQ 29
[    0.741806] pcieport 0000:00:01.3: Signaling PME with IRQ 25
[    0.741818] pcieport 0000:00:03.1: Signaling PME with IRQ 26
[    0.741829] pcieport 0000:00:07.1: Signaling PME with IRQ 27
[    0.741844] pcieport 0000:00:08.1: Signaling PME with IRQ 29
[    0.741900] vesafb: mode is 1366x768x32, linelength=5632, pages=0
[    0.741901] vesafb: scrolling: redraw
[    0.741902] vesafb: Truecolor: size=0:8:8:8, shift=0:16:8:0
[    0.741910] vesafb: framebuffer at 0xc0000000, mapped to 0x        (ptrval), using 4224k, total 4224k
[    0.741966] Console: switching to colour frame buffer device 170x48
[    0.741979] fb0: VESA VGA frame buffer device
[    0.742065] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
[    0.742071] ACPI: Power Button [PWRB]
[    0.742095] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input1
[    0.742143] ACPI: Power Button [PWRF]
[    0.742262] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.742396] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.742486] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.742607] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.742735] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.742807] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.742924] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.743047] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.743181] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.743318] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.743453] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.743573] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.743801] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.764736] 00:04: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    0.766339] Linux agpgart interface v0.103
[    0.768953] loop: module loaded
[    0.769065] libphy: Fixed MDIO Bus: probed
[    0.769066] tun: Universal TUN/TAP device driver, 1.6
[    0.769099] PPP generic driver version 2.4.2
[    0.769137] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.769139] ehci-pci: EHCI PCI platform driver
[    0.769146] ehci-platform: EHCI generic platform driver
[    0.769152] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.769153] ohci-pci: OHCI PCI platform driver
[    0.769160] ohci-platform: OHCI generic platform driver
[    0.769164] uhci_hcd: USB Universal Host Controller Interface driver
[    0.769224] QUIRK: Enable AMD PLL fix
[    0.769235] xhci_hcd 0000:01:00.0: xHCI Host Controller
[    0.769239] xhci_hcd 0000:01:00.0: new USB bus registered, assigned bus number 1
[    0.824587] xhci_hcd 0000:01:00.0: hcc params 0x0200ef81 hci version 0x110 quirks 0x48000418
[    0.824702] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    0.824703] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.824704] usb usb1: Product: xHCI Host Controller
[    0.824705] usb usb1: Manufacturer: Linux 4.15.0-36-generic xhci-hcd
[    0.824706] usb usb1: SerialNumber: 0000:01:00.0
[    0.824796] hub 1-0:1.0: USB hub found
[    0.824807] hub 1-0:1.0: 10 ports detected
[    0.830215] xhci_hcd 0000:01:00.0: xHCI Host Controller
[    0.830217] xhci_hcd 0000:01:00.0: new USB bus registered, assigned bus number 2
[    0.830219] xhci_hcd 0000:01:00.0: Host supports USB 3.10 Enhanced SuperSpeed
[    0.830244] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.830258] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003
[    0.830259] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.830260] usb usb2: Product: xHCI Host Controller
[    0.830261] usb usb2: Manufacturer: Linux 4.15.0-36-generic xhci-hcd
[    0.830262] usb usb2: SerialNumber: 0000:01:00.0
[    0.830336] hub 2-0:1.0: USB hub found
[    0.830342] hub 2-0:1.0: 4 ports detected
[    0.832487] xhci_hcd 0000:08:00.3: xHCI Host Controller
[    0.832490] xhci_hcd 0000:08:00.3: new USB bus registered, assigned bus number 3
[    0.832592] xhci_hcd 0000:08:00.3: hcc params 0x0270f665 hci version 0x100 quirks 0x00000418
[    0.832671] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002
[    0.832672] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.832673] usb usb3: Product: xHCI Host Controller
[    0.832674] usb usb3: Manufacturer: Linux 4.15.0-36-generic xhci-hcd
[    0.832675] usb usb3: SerialNumber: 0000:08:00.3
[    0.832746] hub 3-0:1.0: USB hub found
[    0.832751] hub 3-0:1.0: 4 ports detected
[    0.832860] xhci_hcd 0000:08:00.3: xHCI Host Controller
[    0.832862] xhci_hcd 0000:08:00.3: new USB bus registered, assigned bus number 4
[    0.832864] xhci_hcd 0000:08:00.3: Host supports USB 3.0  SuperSpeed
[    0.832873] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.832885] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003
[    0.832886] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.832887] usb usb4: Product: xHCI Host Controller
[    0.832887] usb usb4: Manufacturer: Linux 4.15.0-36-generic xhci-hcd
[    0.832888] usb usb4: SerialNumber: 0000:08:00.3
[    0.832962] hub 4-0:1.0: USB hub found
[    0.832967] hub 4-0:1.0: 4 ports detected
[    0.833086] i8042: PNP: No PS/2 controller found.
[    0.833147] mousedev: PS/2 mouse device common for all mice
[    0.833271] rtc_cmos 00:02: RTC can wake from S4
[    0.833483] rtc_cmos 00:02: rtc core: registered rtc_cmos as rtc0
[    0.833532] rtc_cmos 00:02: alarms up to one month, y3k, 114 bytes nvram, hpet irqs
[    0.833536] i2c /dev entries driver
[    0.833538] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[    0.833578] device-mapper: uevent: version 1.0.3
[    0.833632] device-mapper: ioctl: 4.37.0-ioctl (2017-09-20) initialised: dm-devel@redhat.com
[    0.833917] ledtrig-cpu: registered to indicate activity on CPUs
[    0.834285] NET: Registered protocol family 10
[    0.837850] Segment Routing with IPv6
[    0.837864] NET: Registered protocol family 17
[    0.837917] Key type dns_resolver registered
[    0.838472] RAS: Correctable Errors collector initialized.
[    0.839333] microcode: CPU0: patch_level=0x08001129
[    0.839340] microcode: CPU1: patch_level=0x08001129
[    0.839351] microcode: CPU2: patch_level=0x08001129
[    0.839358] microcode: CPU3: patch_level=0x08001129
[    0.839366] microcode: CPU4: patch_level=0x08001129
[    0.839371] microcode: CPU5: patch_level=0x08001129
[    0.839387] microcode: CPU6: patch_level=0x08001129
[    0.839394] microcode: CPU7: patch_level=0x08001129
[    0.839403] microcode: CPU8: patch_level=0x08001129
[    0.839411] microcode: CPU9: patch_level=0x08001129
[    0.839422] microcode: CPU10: patch_level=0x08001129
[    0.839430] microcode: CPU11: patch_level=0x08001129
[    0.839464] microcode: Microcode Update Driver: v2.2.
[    0.839471] sched_clock: Marking stable (839460936, 0)->(928245705, -88784769)
[    0.839714] registered taskstats version 1
[    0.839723] Loading compiled-in X.509 certificates
[    0.841512] Loaded X.509 cert 'Build time autogenerated kernel key: 5fd1c39db3adf7bafe36fc7613e1f53b7a1a61bd'
[    0.841530] zswap: loaded using pool lzo/zbud
[    0.844109] Key type big_key registered
[    0.844112] Key type trusted registered
[    0.845315] Key type encrypted registered
[    0.845317] AppArmor: AppArmor sha1 policy hashing enabled
[    0.845319] ima: No TPM chip found, activating TPM-bypass! (rc=-19)
[    0.845323] ima: Allocated hash algorithm: sha1
[    0.845332] evm: HMAC attrs: 0x1
[    0.845661]   Magic number: 6:242:895
[    0.845812] rtc_cmos 00:02: setting system clock to 2018-10-29 16:51:30 UTC (1540831890)
[    0.846048] acpi_cpufreq: overriding BIOS provided _PSD data
[    0.846402] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    0.846402] EDD information not available.
[    1.176206] usb 3-1: new low-speed USB device number 2 using xhci_hcd
[    1.345797] Freeing unused kernel memory: 2408K
[    1.359062] usb 3-1: New USB device found, idVendor=0461, idProduct=4e54
[    1.359064] usb 3-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    1.359065] usb 3-1: Product: Tiger USB Optical Mouse
[    1.359066] usb 3-1: Manufacturer: PixArt
[    1.364248] Write protecting the kernel read-only data: 20480k
[    1.365801] Freeing unused kernel memory: 2008K
[    1.369309] Freeing unused kernel memory: 1884K
[    1.375325] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.382943] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.383001] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.383009] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.429409] acpi PNP0C14:01: duplicate WMI GUID 05901221-D566-11D1-B2F0-00A0C9062910 (first instance was on PNP0C14:00)
[    1.431165] ahci 0000:01:00.1: version 3.0
[    1.431326] ahci 0000:01:00.1: SSS flag set, parallel bus scan disabled
[    1.431359] ahci 0000:01:00.1: AHCI 0001.0301 32 slots 8 ports 6 Gbps 0x33 impl SATA mode
[    1.431361] ahci 0000:01:00.1: flags: 64bit ncq sntf stag pm led clo only pmp pio slum part sxs deso sadm sds apst 
[    1.432947] r8169 Gigabit Ethernet driver 2.3LK-NAPI loaded
[    1.433306] scsi host0: ahci
[    1.433635] scsi host1: ahci
[    1.434113] scsi host2: ahci
[    1.436130] scsi host3: ahci
[    1.436403] scsi host4: ahci
[    1.439382] scsi host5: ahci
[    1.439496] scsi host6: ahci
[    1.439582] scsi host7: ahci
[    1.439619] ata1: SATA max UDMA/133 abar m131072@0xfe780000 port 0xfe780100 irq 40
[    1.439620] ata2: SATA max UDMA/133 abar m131072@0xfe780000 port 0xfe780180 irq 40
[    1.439621] ata3: DUMMY
[    1.439621] ata4: DUMMY
[    1.439623] ata5: SATA max UDMA/133 abar m131072@0xfe780000 port 0xfe780300 irq 40
[    1.439624] ata6: SATA max UDMA/133 abar m131072@0xfe780000 port 0xfe780380 irq 40
[    1.439625] ata7: DUMMY
[    1.439625] ata8: DUMMY
[    1.439776] ahci 0000:09:00.2: AHCI 0001.0301 32 slots 1 ports 6 Gbps 0x1 impl SATA mode
[    1.439778] ahci 0000:09:00.2: flags: 64bit ncq sntf ilck pm led clo only pmp fbs pio slum part 
[    1.439905] scsi host8: ahci
[    1.439930] ata9: SATA max UDMA/133 abar m4096@0xfe808000 port 0xfe808100 irq 42
[    1.445166] r8169 0000:03:00.0 eth0: RTL8168h/8111h at 0x        (ptrval), 18:31:bf:69:c3:87, XID 14100800 IRQ 43
[    1.445168] r8169 0000:03:00.0 eth0: jumbo features [frames: 9200 bytes, tx checksumming: ko]
[    1.454292] r8169 0000:03:00.0 enp3s0: renamed from eth0
[    1.493806] [drm] amdgpu kernel modesetting enabled.
[    1.495397] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    1.495397] AMD IOMMUv2 functionality not available on this system
[    1.496115] usb 3-3: new low-speed USB device number 3 using xhci_hcd
[    1.497604] Found CRAT image with size=3024
[    1.497605] Parsing CRAT table with 1 nodes
[    1.497605] Found CU entry in CRAT table with proximity_domain=0 caps=0
[    1.497606] CU CPU: cores=12 id_base=0
[    1.497606] Found memory entry in CRAT table with proximity_domain=0
[    1.497607] Found memory entry in CRAT table with proximity_domain=0
[    1.497607] Found memory entry in CRAT table with proximity_domain=0
[    1.497607] Found cache entry in CRAT table with processor_id=0
[    1.497608] Found cache entry in CRAT table with processor_id=0
[    1.497608] Found cache entry in CRAT table with processor_id=0
[    1.497609] Found cache entry in CRAT table with processor_id=0
[    1.497609] Found cache entry in CRAT table with processor_id=2
[    1.497609] Found cache entry in CRAT table with processor_id=2
[    1.497610] Found cache entry in CRAT table with processor_id=2
[    1.497610] Found cache entry in CRAT table with processor_id=4
[    1.497610] Found cache entry in CRAT table with processor_id=4
[    1.497610] Found cache entry in CRAT table with processor_id=4
[    1.497611] Found cache entry in CRAT table with processor_id=8
[    1.497611] Found cache entry in CRAT table with processor_id=8
[    1.497611] Found cache entry in CRAT table with processor_id=8
[    1.497612] Found cache entry in CRAT table with processor_id=8
[    1.497612] Found cache entry in CRAT table with processor_id=10
[    1.497612] Found cache entry in CRAT table with processor_id=10
[    1.497613] Found cache entry in CRAT table with processor_id=10
[    1.497613] Found cache entry in CRAT table with processor_id=12
[    1.497613] Found cache entry in CRAT table with processor_id=12
[    1.497613] Found cache entry in CRAT table with processor_id=12
[    1.497614] Found TLB entry in CRAT table (not processing)
[    1.497614] Found TLB entry in CRAT table (not processing)
[    1.497614] Found TLB entry in CRAT table (not processing)
[    1.497614] Found TLB entry in CRAT table (not processing)
[    1.497615] Found TLB entry in CRAT table (not processing)
[    1.497615] Found TLB entry in CRAT table (not processing)
[    1.497615] Found TLB entry in CRAT table (not processing)
[    1.497615] Found TLB entry in CRAT table (not processing)
[    1.497615] Found TLB entry in CRAT table (not processing)
[    1.497616] Found TLB entry in CRAT table (not processing)
[    1.497616] Found TLB entry in CRAT table (not processing)
[    1.497616] Found TLB entry in CRAT table (not processing)
[    1.497616] Found TLB entry in CRAT table (not processing)
[    1.497616] Found TLB entry in CRAT table (not processing)
[    1.497617] Found TLB entry in CRAT table (not processing)
[    1.497617] Found TLB entry in CRAT table (not processing)
[    1.497617] Found TLB entry in CRAT table (not processing)
[    1.497617] Found TLB entry in CRAT table (not processing)
[    1.497618] Found TLB entry in CRAT table (not processing)
[    1.497618] Found TLB entry in CRAT table (not processing)
[    1.497618] Found TLB entry in CRAT table (not processing)
[    1.497618] Found TLB entry in CRAT table (not processing)
[    1.497618] Found TLB entry in CRAT table (not processing)
[    1.497619] Found TLB entry in CRAT table (not processing)
[    1.497619] Creating topology SYSFS entries
[    1.497629] Finished initializing topology ret=0
[    1.497651] kfd kfd: Initialized module
[    1.497793] checking generic (c0000000 420000) vs hw (e0000000 10000000)
[    1.497836] amdgpu 0000:06:00.0: enabling device (0000 -> 0003)
[    1.497986] [drm] initializing kernel modesetting (POLARIS10 0x1002:0x67DF 0x1043:0x04C2 0xEF).
[    1.497999] [drm] register mmio base: 0xFE500000
[    1.497999] [drm] register mmio size: 262144
[    1.498008] [drm] probing gen 2 caps for device 1022:43b4 = 473dc42/6
[    1.498010] [drm] probing mlw for device 1022:43b4 = 473dc42
[    1.498021] [drm] UVD is enabled in VM mode
[    1.498022] [drm] UVD ENC is enabled in VM mode
[    1.498025] [drm] VCE enabled in VM mode
[    1.726114] ATOM BIOS: 115-C940PI0-100
[    1.726126] [drm] GPU posting now...
[    1.754846] ata1: SATA link down (SStatus 0 SControl 300)
[    1.756334] tsc: Refined TSC clocksource calibration: 3193.998 MHz
[    1.756345] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x2e0a244aeba, max_idle_ns: 440795290469 ns
[    1.763091] ata9: SATA link down (SStatus 0 SControl 300)
[    1.777313] usb 3-3: New USB device found, idVendor=04d9, idProduct=1702
[    1.777314] usb 3-3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    1.777316] usb 3-3: Product: USB Keyboard
[    1.777317] usb 3-3: Manufacturer:  
[    1.916165] usb 3-4: new high-speed USB device number 4 using xhci_hcd
[    2.066771] ata2: SATA link down (SStatus 0 SControl 300)
[    2.083515] usb 3-4: New USB device found, idVendor=0cf3, idProduct=9271
[    2.083516] usb 3-4: New USB device strings: Mfr=16, Product=32, SerialNumber=48
[    2.083517] usb 3-4: Product: USB2.0 WLAN
[    2.083518] usb 3-4: Manufacturer: ATHEROS
[    2.083519] usb 3-4: SerialNumber: 12345
[    2.087593] hidraw: raw HID events driver (C) Jiri Kosina
[    2.216344] [drm] vm size is 64 GB, block size is 13-bit, fragment size is 9-bit
[    2.216373] amdgpu 0000:06:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    2.216374] amdgpu 0000:06:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    2.216378] [drm] Detected VRAM RAM=4096M, BAR=256M
[    2.216378] [drm] RAM width 256bits GDDR5
[    2.216574] [TTM] Zone  kernel: Available graphics memory: 4048048 kiB
[    2.216574] [TTM] Zone   dma32: Available graphics memory: 2097152 kiB
[    2.216575] [TTM] Initializing pool allocator
[    2.216577] [TTM] Initializing DMA pool allocator
[    2.216597] [drm] amdgpu: 4096M of VRAM memory ready
[    2.216598] [drm] amdgpu: 4096M of GTT memory ready.
[    2.216603] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    2.216692] [drm] PCIE GART of 256M enabled (table at 0x000000F400040000).
[    2.216746] amdgpu 0000:06:00.0: amdgpu: using MSI.
[    2.216769] [drm] amdgpu: irq initialized.
[    2.216784] amdgpu: [powerplay] amdgpu: powerplay sw initialized
[    2.216813] [drm] Chained IB support enabled!
[    2.216994] amdgpu 0000:06:00.0: fence driver on ring 0 use gpu addr 0x0000000000400040, cpu addr 0x        (ptrval)
[    2.217047] amdgpu 0000:06:00.0: fence driver on ring 1 use gpu addr 0x00000000004000c0, cpu addr 0x        (ptrval)
[    2.217094] amdgpu 0000:06:00.0: fence driver on ring 2 use gpu addr 0x0000000000400140, cpu addr 0x        (ptrval)
[    2.217140] amdgpu 0000:06:00.0: fence driver on ring 3 use gpu addr 0x00000000004001c0, cpu addr 0x        (ptrval)
[    2.217186] amdgpu 0000:06:00.0: fence driver on ring 4 use gpu addr 0x0000000000400240, cpu addr 0x        (ptrval)
[    2.217230] amdgpu 0000:06:00.0: fence driver on ring 5 use gpu addr 0x00000000004002c0, cpu addr 0x        (ptrval)
[    2.217272] amdgpu 0000:06:00.0: fence driver on ring 6 use gpu addr 0x0000000000400340, cpu addr 0x        (ptrval)
[    2.217315] amdgpu 0000:06:00.0: fence driver on ring 7 use gpu addr 0x00000000004003c0, cpu addr 0x        (ptrval)
[    2.217355] amdgpu 0000:06:00.0: fence driver on ring 8 use gpu addr 0x0000000000400440, cpu addr 0x        (ptrval)
[    2.217373] amdgpu 0000:06:00.0: fence driver on ring 9 use gpu addr 0x00000000004004e0, cpu addr 0x        (ptrval)
[    2.217865] amdgpu 0000:06:00.0: fence driver on ring 10 use gpu addr 0x0000000000400560, cpu addr 0x        (ptrval)
[    2.217905] amdgpu 0000:06:00.0: fence driver on ring 11 use gpu addr 0x00000000004005e0, cpu addr 0x        (ptrval)
[    2.217986] [drm] Found UVD firmware Version: 1.79 Family ID: 16
[    2.219132] amdgpu 0000:06:00.0: fence driver on ring 12 use gpu addr 0x000000f4001e6420, cpu addr 0x        (ptrval)
[    2.219169] amdgpu 0000:06:00.0: fence driver on ring 13 use gpu addr 0x00000000004006e0, cpu addr 0x        (ptrval)
[    2.219219] amdgpu 0000:06:00.0: fence driver on ring 14 use gpu addr 0x0000000000400760, cpu addr 0x        (ptrval)
[    2.219269] [drm] Found VCE firmware Version: 52.4 Binary ID: 3
[    2.219422] amdgpu 0000:06:00.0: fence driver on ring 15 use gpu addr 0x00000000004007e0, cpu addr 0x        (ptrval)
[    2.219463] amdgpu 0000:06:00.0: fence driver on ring 16 use gpu addr 0x0000000000400860, cpu addr 0x        (ptrval)
[    2.229189] usbcore: registered new interface driver usbhid
[    2.229190] usbhid: USB HID core driver
[    2.230717] input: PixArt Tiger USB Optical Mouse as /devices/pci0000:00/0000:00:07.1/0000:08:00.3/usb3/3-1/3-1:1.0/0003:0461:4E54.0001/input/input2
[    2.230834] hid-generic 0003:0461:4E54.0001: input,hidraw0: USB HID v1.11 Mouse [PixArt Tiger USB Optical Mouse] on usb-0000:08:00.3-1/input0
[    2.230925] input:   USB Keyboard as /devices/pci0000:00/0000:00:07.1/0000:08:00.3/usb3/3-3/3-3:1.0/0003:04D9:1702.0002/input/input3
[    2.280422] [drm] DM_PPLIB: values for Engine clock
[    2.280423] [drm] DM_PPLIB:	 30000
[    2.280423] [drm] DM_PPLIB:	 61300
[    2.280423] [drm] DM_PPLIB:	 99400
[    2.280424] [drm] DM_PPLIB:	 108800
[    2.280424] [drm] DM_PPLIB:	 115600
[    2.280424] [drm] DM_PPLIB:	 122100
[    2.280425] [drm] DM_PPLIB:	 126400
[    2.280425] [drm] DM_PPLIB:	 130000
[    2.280425] [drm] DM_PPLIB: Warning: using default validation clocks!
[    2.280426] [drm] DM_PPLIB: Validation clocks:
[    2.280426] [drm] DM_PPLIB:    engine_max_clock: 72000
[    2.280426] [drm] DM_PPLIB:    memory_max_clock: 80000
[    2.280427] [drm] DM_PPLIB:    level           : 0
[    2.280427] [drm] DM_PPLIB: reducing engine clock level from 8 to 2
[    2.280428] [drm] DM_PPLIB: values for Memory clock
[    2.280428] [drm] DM_PPLIB:	 30000
[    2.280428] [drm] DM_PPLIB:	 100000
[    2.280429] [drm] DM_PPLIB:	 175000
[    2.280429] [drm] DM_PPLIB: Warning: using default validation clocks!
[    2.280429] [drm] DM_PPLIB: Validation clocks:
[    2.280429] [drm] DM_PPLIB:    engine_max_clock: 72000
[    2.280430] [drm] DM_PPLIB:    memory_max_clock: 80000
[    2.280430] [drm] DM_PPLIB:    level           : 0
[    2.280430] [drm] DM_PPLIB: reducing memory clock level from 3 to 1
[    2.280432] [drm] DC: create_links: connectors_num: physical:4, virtual:0
[    2.281108] [drm] Display Core initialized!
[    2.281561] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    2.281561] [drm] Driver supports precise vblank timestamp query.
[    2.283011] [drm] ring test on 0 succeeded in 11 usecs
[    2.284180] [drm] ring test on 9 succeeded in 4 usecs
[    2.284212] [drm] ring test on 1 succeeded in 8 usecs
[    2.284224] [drm] ring test on 2 succeeded in 2 usecs
[    2.284235] [drm] ring test on 3 succeeded in 2 usecs
[    2.284247] [drm] ring test on 4 succeeded in 2 usecs
[    2.284262] [drm] ring test on 5 succeeded in 2 usecs
[    2.284273] [drm] ring test on 6 succeeded in 2 usecs
[    2.284285] [drm] ring test on 7 succeeded in 2 usecs
[    2.284296] [drm] ring test on 8 succeeded in 2 usecs
[    2.284401] [drm] ring test on 10 succeeded in 6 usecs
[    2.284410] [drm] ring test on 11 succeeded in 6 usecs
[    2.288358] hid-generic 0003:04D9:1702.0002: input,hidraw1: USB HID v1.10 Keyboard [  USB Keyboard] on usb-0000:08:00.3-3/input0
[    2.288461] input:   USB Keyboard as /devices/pci0000:00/0000:00:07.1/0000:08:00.3/usb3/3-3/3-3:1.1/0003:04D9:1702.0003/input/input4
[    2.310600] [drm] ring test on 12 succeeded in 1 usecs
[    2.310645] [drm] ring test on 13 succeeded in 11 usecs
[    2.310657] [drm] ring test on 14 succeeded in 2 usecs
[    2.310658] [drm] UVD and UVD ENC initialized successfully.
[    2.348396] hid-generic 0003:04D9:1702.0003: input,hidraw2: USB HID v1.10 Device [  USB Keyboard] on usb-0000:08:00.3-3/input1
[    2.410578] [drm] ring test on 15 succeeded in 4 usecs
[    2.410593] [drm] ring test on 16 succeeded in 2 usecs
[    2.410593] [drm] VCE initialized successfully.
[    2.410845] [drm] ib test on ring 0 succeeded
[    2.411050] [drm] ib test on ring 1 succeeded
[    2.411099] [drm] ib test on ring 2 succeeded
[    2.411149] [drm] ib test on ring 3 succeeded
[    2.411199] [drm] ib test on ring 4 succeeded
[    2.411249] [drm] ib test on ring 5 succeeded
[    2.411296] [drm] ib test on ring 6 succeeded
[    2.411342] [drm] ib test on ring 7 succeeded
[    2.411388] [drm] ib test on ring 8 succeeded
[    2.540561] ata5: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    2.541069] ata5.00: ATA-10: WDC WD10EZEX-60WN4A0, 01.01A01, max UDMA/100
[    2.541070] ata5.00: 1953525168 sectors, multi 16: LBA48 NCQ (depth 31/32), AA
[    2.541649] ata5.00: configured for UDMA/100
[    2.541999] scsi 4:0:0:0: Direct-Access     ATA      WDC WD10EZEX-60W 1A01 PQ: 0 ANSI: 5
[    2.542195] sd 4:0:0:0: Attached scsi generic sg0 type 0
[    2.542339] sd 4:0:0:0: [sda] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    2.542341] sd 4:0:0:0: [sda] 4096-byte physical blocks
[    2.542360] sd 4:0:0:0: [sda] Write Protect is off
[    2.542362] sd 4:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    2.542396] sd 4:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    2.555704]  sda: sda1 sda2 sda3 sda4
[    2.556227] sd 4:0:0:0: [sda] Attached SCSI disk
[    2.780449] clocksource: Switched to clocksource tsc
[    2.940551] [drm] ib test on ring 9 succeeded
[    2.940634] [drm] ib test on ring 10 succeeded
[    2.940666] [drm] ib test on ring 11 succeeded
[    2.942285] [drm] ib test on ring 12 succeeded
[    2.942707] [drm] ib test on ring 13 succeeded
[    2.943094] [drm] ib test on ring 14 succeeded
[    2.943370] [drm] ib test on ring 15 succeeded
[    2.943380] [drm] Cannot find any crtc or sizes
[    2.944663] amdgpu 0000:06:00.0: kfd not supported on this ASIC
[    2.944671] [drm] Initialized amdgpu 3.23.0 20150101 for 0000:06:00.0 on minor 0
[    2.944702] checking generic (c0000000 420000) vs hw (c0000000 10000000)
[    2.944702] fb: switching to amdgpudrmfb from VESA VGA
[    2.944720] Console: switching to colour dummy device 80x25
[    2.944962] [drm] initializing kernel modesetting (POLARIS10 0x1002:0x67DF 0x1043:0x04C2 0xEF).
[    2.944969] [drm] register mmio base: 0xFE900000
[    2.944970] [drm] register mmio size: 262144
[    2.944977] [drm] probing gen 2 caps for device 1022:1453 = 733903/e
[    2.944978] [drm] probing mlw for device 1022:1453 = 733903
[    2.944986] [drm] UVD is enabled in VM mode
[    2.944986] [drm] UVD ENC is enabled in VM mode
[    2.944988] [drm] VCE enabled in VM mode
[    2.945169] amdgpu 0000:07:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    2.945184] ATOM BIOS: 115-C940PI0-100
[    2.945191] [drm] GPU post is not needed
[    2.945204] [drm] vm size is 64 GB, block size is 13-bit, fragment size is 9-bit
[    2.945215] amdgpu 0000:07:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    2.945216] amdgpu 0000:07:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    2.945219] [drm] Detected VRAM RAM=4096M, BAR=256M
[    2.945219] [drm] RAM width 256bits GDDR5
[    2.945226] [drm] amdgpu: 4096M of VRAM memory ready
[    2.945226] [drm] amdgpu: 4096M of GTT memory ready.
[    2.945233] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    2.945304] [drm] PCIE GART of 256M enabled (table at 0x000000F400040000).
[    2.945346] amdgpu 0000:07:00.0: amdgpu: using MSI.
[    2.945362] [drm] amdgpu: irq initialized.
[    2.945376] amdgpu: [powerplay] amdgpu: powerplay sw initialized
[    2.945379] [drm] Chained IB support enabled!
[    2.945470] amdgpu 0000:07:00.0: fence driver on ring 0 use gpu addr 0x0000000000400040, cpu addr 0x        (ptrval)
[    2.945514] amdgpu 0000:07:00.0: fence driver on ring 1 use gpu addr 0x00000000004000c0, cpu addr 0x        (ptrval)
[    2.945548] amdgpu 0000:07:00.0: fence driver on ring 2 use gpu addr 0x0000000000400140, cpu addr 0x        (ptrval)
[    2.945584] amdgpu 0000:07:00.0: fence driver on ring 3 use gpu addr 0x00000000004001c0, cpu addr 0x        (ptrval)
[    2.945616] amdgpu 0000:07:00.0: fence driver on ring 4 use gpu addr 0x0000000000400240, cpu addr 0x        (ptrval)
[    2.945649] amdgpu 0000:07:00.0: fence driver on ring 5 use gpu addr 0x00000000004002c0, cpu addr 0x        (ptrval)
[    2.945678] amdgpu 0000:07:00.0: fence driver on ring 6 use gpu addr 0x0000000000400340, cpu addr 0x        (ptrval)
[    2.945710] amdgpu 0000:07:00.0: fence driver on ring 7 use gpu addr 0x00000000004003c0, cpu addr 0x        (ptrval)
[    2.945739] amdgpu 0000:07:00.0: fence driver on ring 8 use gpu addr 0x0000000000400440, cpu addr 0x        (ptrval)
[    2.945757] amdgpu 0000:07:00.0: fence driver on ring 9 use gpu addr 0x00000000004004e0, cpu addr 0x        (ptrval)
[    2.946201] amdgpu 0000:07:00.0: fence driver on ring 10 use gpu addr 0x0000000000400560, cpu addr 0x        (ptrval)
[    2.946233] amdgpu 0000:07:00.0: fence driver on ring 11 use gpu addr 0x00000000004005e0, cpu addr 0x        (ptrval)
[    2.946246] [drm] Found UVD firmware Version: 1.79 Family ID: 16
[    2.946514] amdgpu 0000:07:00.0: fence driver on ring 12 use gpu addr 0x000000f4001e6420, cpu addr 0x        (ptrval)
[    2.946538] amdgpu 0000:07:00.0: fence driver on ring 13 use gpu addr 0x00000000004006e0, cpu addr 0x        (ptrval)
[    2.946561] amdgpu 0000:07:00.0: fence driver on ring 14 use gpu addr 0x0000000000400760, cpu addr 0x        (ptrval)
[    2.946569] [drm] Found VCE firmware Version: 52.4 Binary ID: 3
[    2.946630] amdgpu 0000:07:00.0: fence driver on ring 15 use gpu addr 0x00000000004007e0, cpu addr 0x        (ptrval)
[    2.946655] amdgpu 0000:07:00.0: fence driver on ring 16 use gpu addr 0x0000000000400860, cpu addr 0x        (ptrval)
[    3.005352] [drm] DM_PPLIB: values for Engine clock
[    3.005353] [drm] DM_PPLIB:	 30000
[    3.005354] [drm] DM_PPLIB:	 61300
[    3.005354] [drm] DM_PPLIB:	 99400
[    3.005354] [drm] DM_PPLIB:	 108800
[    3.005354] [drm] DM_PPLIB:	 115600
[    3.005355] [drm] DM_PPLIB:	 122100
[    3.005355] [drm] DM_PPLIB:	 126400
[    3.005355] [drm] DM_PPLIB:	 130000
[    3.005356] [drm] DM_PPLIB: Warning: using default validation clocks!
[    3.005356] [drm] DM_PPLIB: Validation clocks:
[    3.005356] [drm] DM_PPLIB:    engine_max_clock: 72000
[    3.005356] [drm] DM_PPLIB:    memory_max_clock: 80000
[    3.005357] [drm] DM_PPLIB:    level           : 0
[    3.005357] [drm] DM_PPLIB: reducing engine clock level from 8 to 2
[    3.005358] [drm] DM_PPLIB: values for Memory clock
[    3.005358] [drm] DM_PPLIB:	 30000
[    3.005358] [drm] DM_PPLIB:	 100000
[    3.005359] [drm] DM_PPLIB:	 175000
[    3.005359] [drm] DM_PPLIB: Warning: using default validation clocks!
[    3.005359] [drm] DM_PPLIB: Validation clocks:
[    3.005359] [drm] DM_PPLIB:    engine_max_clock: 72000
[    3.005360] [drm] DM_PPLIB:    memory_max_clock: 80000
[    3.005360] [drm] DM_PPLIB:    level           : 0
[    3.005360] [drm] DM_PPLIB: reducing memory clock level from 3 to 1
[    3.005362] [drm] DC: create_links: connectors_num: physical:4, virtual:0
[    3.012562] ata6: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    3.013095] ata6.00: ATA-10: WDC WD10EZEX-60WN4A0, 01.01A01, max UDMA/100
[    3.013097] ata6.00: 1953525168 sectors, multi 16: LBA48 NCQ (depth 31/32), AA
[    3.013651] ata6.00: configured for UDMA/100
[    3.013926] scsi 5:0:0:0: Direct-Access     ATA      WDC WD10EZEX-60W 1A01 PQ: 0 ANSI: 5
[    3.014109] sd 5:0:0:0: Attached scsi generic sg1 type 0
[    3.014116] sd 5:0:0:0: [sdb] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    3.014118] sd 5:0:0:0: [sdb] 4096-byte physical blocks
[    3.014134] sd 5:0:0:0: [sdb] Write Protect is off
[    3.014135] sd 5:0:0:0: [sdb] Mode Sense: 00 3a 00 00
[    3.014156] sd 5:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    3.032218] [drm] Display Core initialized!
[    3.057616] [drm] BenQ G922HDAL: [Block 0] 
[    3.057618] [drm] BenQ G922HDAL: [Block 1] 
[    3.057620] [drm] dc_link_detect: manufacturer_id = D109, product_id = 784C, serial_number = 5445, manufacture_week = 29, manufacture_year = 20, display_name = BenQ G922HDAL, speaker_flag = 1, audio_mode_count = 1
[    3.057621] [drm] dc_link_detect: mode number = 0, format_code = 1, channel_count = 2, sample_rate = 7, sample_size = 7
[    3.057768] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    3.057769] [drm] Driver supports precise vblank timestamp query.
[    3.058083]  sdb: sdb1 sdb2 < sdb5 >
[    3.058349] sd 5:0:0:0: [sdb] Attached SCSI disk
[    3.059174] [drm] ring test on 0 succeeded in 11 usecs
[    3.060063] [drm] ring test on 9 succeeded in 7 usecs
[    3.060086] [drm] ring test on 1 succeeded in 7 usecs
[    3.060095] [drm] ring test on 2 succeeded in 2 usecs
[    3.060105] [drm] ring test on 3 succeeded in 2 usecs
[    3.060113] [drm] ring test on 4 succeeded in 2 usecs
[    3.060131] [drm] ring test on 5 succeeded in 5 usecs
[    3.060147] [drm] ring test on 6 succeeded in 2 usecs
[    3.060156] [drm] ring test on 7 succeeded in 2 usecs
[    3.060165] [drm] ring test on 8 succeeded in 2 usecs
[    3.060253] [drm] ring test on 10 succeeded in 5 usecs
[    3.060262] [drm] ring test on 11 succeeded in 6 usecs
[    3.086618] [drm] ring test on 12 succeeded in 1 usecs
[    3.086663] [drm] ring test on 13 succeeded in 13 usecs
[    3.086677] [drm] ring test on 14 succeeded in 3 usecs
[    3.086677] [drm] UVD and UVD ENC initialized successfully.
[    3.186599] [drm] ring test on 15 succeeded in 5 usecs
[    3.186611] [drm] ring test on 16 succeeded in 2 usecs
[    3.186612] [drm] VCE initialized successfully.
[    3.186841] [drm] ib test on ring 0 succeeded
[    3.187008] [drm] ib test on ring 1 succeeded
[    3.187047] [drm] ib test on ring 2 succeeded
[    3.187085] [drm] ib test on ring 3 succeeded
[    3.187122] [drm] ib test on ring 4 succeeded
[    3.187160] [drm] ib test on ring 5 succeeded
[    3.187199] [drm] ib test on ring 6 succeeded
[    3.187235] [drm] ib test on ring 7 succeeded
[    3.187272] [drm] ib test on ring 8 succeeded
[    3.462710] random: fast init done
[    3.708538] [drm] ib test on ring 9 succeeded
[    3.708577] [drm] ib test on ring 10 succeeded
[    3.708602] [drm] ib test on ring 11 succeeded
[    3.710659] [drm] ib test on ring 12 succeeded
[    3.711024] [drm] ib test on ring 13 succeeded
[    3.711328] [drm] ib test on ring 14 succeeded
[    3.711570] [drm] ib test on ring 15 succeeded
[    3.712439] [drm] fb mappable at 0xC03F2000
[    3.712440] [drm] vram apper at 0xC0000000
[    3.712440] [drm] size 4325376
[    3.712440] [drm] fb depth is 24
[    3.712441] [drm]    pitch is 5632
[    3.712504] fbcon: amdgpudrmfb (fb0) is primary device
[    3.712542] Console: switching to colour frame buffer device 170x48
[    3.712557] amdgpu 0000:07:00.0: fb0: amdgpudrmfb frame buffer device
[    3.742628] amdgpu 0000:07:00.0: kfd not supported on this ASIC
[    3.742639] [drm] Initialized amdgpu 3.23.0 20150101 for 0000:07:00.0 on minor 1
[    3.871017] EXT4-fs (sdb1): mounted filesystem with ordered data mode. Opts: (null)
[    4.641426] systemd[1]: systemd 229 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ -LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN)
[    4.661212] systemd[1]: Detected architecture x86-64.
[    4.661359] systemd[1]: Set hostname to <ishan>.
[    4.869616] random: crng init done
[    4.869618] random: 7 urandom warning(s) missed due to ratelimiting
[    5.306407] systemd[1]: Created slice User and Session Slice.
[    5.306464] systemd[1]: Listening on Journal Socket.
[    5.306480] systemd[1]: Listening on fsck to fsckd communication Socket.
[    5.306502] systemd[1]: Listening on udev Control Socket.
[    5.306514] systemd[1]: Listening on Syslog Socket.
[    5.306559] systemd[1]: Listening on Journal Audit Socket.
[    5.306584] systemd[1]: Started Trigger resolvconf update for networkd DNS.
[   11.514297] lp: driver loaded but no devices found
[   11.516392] ppdev: user-space parallel port driver
[   11.636979] EXT4-fs (sdb1): re-mounted. Opts: errors=remount-ro
[   11.681226] systemd-journald[379]: Received request to flush runtime journal from PID 1
[   11.741694] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[   11.750604] ccp 0000:08:00.2: ccp enabled
[   11.750606] ccp 0000:08:00.2: enabled
[   11.789503] piix4_smbus 0000:00:14.0: SMBus Host Controller at 0xb00, revision 0
[   11.789505] piix4_smbus 0000:00:14.0: Using register 0x02 for SMBus port selection
[   11.791382] asus_wmi: ASUS WMI generic driver loaded
[   11.792448] asus_wmi: Initialization: 0x0
[   11.792492] asus_wmi: BIOS WMI version: 0.9
[   11.792640] asus_wmi: SFUN value: 0x0
[   11.793183] input: Eee PC WMI hotkeys as /devices/platform/eeepc-wmi/input/input5
[   11.793388] asus_wmi: Number of fans: 1
[   11.799160] AVX2 version of gcm_enc/dec engaged.
[   11.799162] AES CTR mode by8 optimization enabled
[   11.833255] snd_hda_intel 0000:06:00.1: Handle vga_switcheroo audio client
[   11.833258] snd_hda_intel 0000:06:00.1: Force to non-snoop mode
[   11.833603] snd_hda_intel 0000:07:00.1: Handle vga_switcheroo audio client
[   11.833604] snd_hda_intel 0000:07:00.1: Force to non-snoop mode
[   11.835302] kvm: disabled by bios
[   11.837468] MCE: In-kernel MCE decoding enabled.
[   11.838926] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.838927] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   11.844704] input: HDA ATI HDMI HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:01.3/0000:01:00.2/0000:02:04.0/0000:06:00.1/sound/card0/input6
[   11.844764] input: HDA ATI HDMI HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:01.3/0000:01:00.2/0000:02:04.0/0000:06:00.1/sound/card0/input7
[   11.844856] input: HDA ATI HDMI HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:01.3/0000:01:00.2/0000:02:04.0/0000:06:00.1/sound/card0/input8
[   11.845015] input: HDA ATI HDMI HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:01.3/0000:01:00.2/0000:02:04.0/0000:06:00.1/sound/card0/input9
[   11.845098] input: HDA ATI HDMI HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:03.1/0000:07:00.1/sound/card1/input12
[   11.845138] input: HDA ATI HDMI HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:01.3/0000:01:00.2/0000:02:04.0/0000:06:00.1/sound/card0/input10
[   11.845201] input: HDA ATI HDMI HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:01.3/0000:01:00.2/0000:02:04.0/0000:06:00.1/sound/card0/input11
[   11.845255] input: HDA ATI HDMI HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:03.1/0000:07:00.1/sound/card1/input13
[   11.845302] input: HDA ATI HDMI HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:03.1/0000:07:00.1/sound/card1/input14
[   11.845356] input: HDA ATI HDMI HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:03.1/0000:07:00.1/sound/card1/input15
[   11.845456] input: HDA ATI HDMI HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:03.1/0000:07:00.1/sound/card1/input16
[   11.845527] input: HDA ATI HDMI HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:03.1/0000:07:00.1/sound/card1/input17
[   11.851278] snd_hda_codec_realtek hdaudioC2D0: autoconfig for ALC887-VD: line_outs=1 (0x14/0x0/0x0/0x0/0x0) type:line
[   11.851281] snd_hda_codec_realtek hdaudioC2D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[   11.851282] snd_hda_codec_realtek hdaudioC2D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
[   11.851283] snd_hda_codec_realtek hdaudioC2D0:    mono: mono_out=0x0
[   11.851284] snd_hda_codec_realtek hdaudioC2D0:    dig-out=0x11/0x0
[   11.851286] snd_hda_codec_realtek hdaudioC2D0:    inputs:
[   11.851287] snd_hda_codec_realtek hdaudioC2D0:      Front Mic=0x19
[   11.851289] snd_hda_codec_realtek hdaudioC2D0:      Rear Mic=0x18
[   11.851290] snd_hda_codec_realtek hdaudioC2D0:      Line=0x1a
[   11.866136] input: HD-Audio Generic Front Mic as /devices/pci0000:00/0000:00:08.1/0000:09:00.3/sound/card2/input18
[   11.866174] input: HD-Audio Generic Rear Mic as /devices/pci0000:00/0000:00:08.1/0000:09:00.3/sound/card2/input19
[   11.866210] input: HD-Audio Generic Line as /devices/pci0000:00/0000:00:08.1/0000:09:00.3/sound/card2/input20
[   11.866247] input: HD-Audio Generic Line Out as /devices/pci0000:00/0000:00:08.1/0000:09:00.3/sound/card2/input21
[   11.866283] input: HD-Audio Generic Front Headphone as /devices/pci0000:00/0000:00:08.1/0000:09:00.3/sound/card2/input22
[   11.920617] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.920619] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   12.214829] audit: type=1400 audit(1540831901.862:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/ipsec/lookip" pid=818 comm="apparmor_parser"
[   12.214904] audit: type=1400 audit(1540831901.862:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/ipsec/stroke" pid=819 comm="apparmor_parser"
[   12.215075] audit: type=1400 audit(1540831901.862:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/ippusbxd" pid=823 comm="apparmor_parser"
[   12.215257] audit: type=1400 audit(1540831901.862:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=821 comm="apparmor_parser"
[   12.215684] audit: type=1400 audit(1540831901.862:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/ipsec/charon" pid=817 comm="apparmor_parser"
[   12.216123] audit: type=1400 audit(1540831901.862:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/tcpdump" pid=825 comm="apparmor_parser"
[   12.216216] audit: type=1400 audit(1540831901.866:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=812 comm="apparmor_parser"
[   12.216219] audit: type=1400 audit(1540831901.866:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=812 comm="apparmor_parser"
[   12.216221] audit: type=1400 audit(1540831901.866:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=812 comm="apparmor_parser"
[   12.216223] audit: type=1400 audit(1540831901.866:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=812 comm="apparmor_parser"
[   12.819412] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[   12.821249] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[   12.838530] usb 3-4: ath9k_htc: Firmware ath9k_htc/htc_9271-1.4.0.fw requested
[   12.838566] usbcore: registered new interface driver ath9k_htc
[   12.919625] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[   12.919628] cfg80211: failed to load regulatory.db
[   13.222223] usb 3-4: ath9k_htc: Transferred FW: ath9k_htc/htc_9271-1.4.0.fw, size: 51008
[   13.472519] ath9k_htc 3-4:1.0: ath9k_htc: HTC initialized with 33 credits
[   13.582129] Adding 9764860k swap on /dev/sdb5.  Priority:-2 extents:1 across:9764860k FS
[   13.656691] [drm] {1366x768, 1792x798@85500Khz}
[   13.701393] ath9k_htc 3-4:1.0: ath9k_htc: FW Version: 1.4
[   13.701395] ath9k_htc 3-4:1.0: FW RMW support: On
[   13.701396] ath: EEPROM regdomain: 0x809c
[   13.701396] ath: EEPROM indicates we should expect a country code
[   13.701397] ath: doing EEPROM country->regdmn map search
[   13.701397] ath: country maps to regdmn code: 0x52
[   13.701398] ath: Country alpha2 being used: CN
[   13.701398] ath: Regpair used: 0x52
[   13.706993] ieee80211 phy0: Atheros AR9271 Rev:1
[   13.707963] ath9k_htc 3-4:1.0 wlxec086b084321: renamed from wlan0
[   15.527083] IPv6: ADDRCONF(NETDEV_UP): wlxec086b084321: link is not ready
[   15.659421] IPv6: ADDRCONF(NETDEV_UP): wlxec086b084321: link is not ready
[   15.662192] IPv6: ADDRCONF(NETDEV_UP): enp3s0: link is not ready
[   15.755018] r8169 0000:03:00.0 enp3s0: link down
[   15.755104] IPv6: ADDRCONF(NETDEV_UP): enp3s0: link is not ready
[   15.899105] IPv6: ADDRCONF(NETDEV_UP): wlxec086b084321: link is not ready
[   16.088412] amdgpu 0000:07:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=io+mem
[   16.088414] amdgpu 0000:06:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[   18.264703] wlxec086b084321: authenticate with 44:c3:46:5f:f0:86
[   18.451166] wlxec086b084321: send auth to 44:c3:46:5f:f0:86 (try 1/3)
[   18.454000] wlxec086b084321: authenticated
[   18.460153] wlxec086b084321: associate with 44:c3:46:5f:f0:86 (try 1/3)
[   18.465192] wlxec086b084321: RX AssocResp from 44:c3:46:5f:f0:86 (capab=0x411 status=0 aid=3)
[   18.471023] wlxec086b084321: associated
[   18.499557] IPv6: ADDRCONF(NETDEV_CHANGE): wlxec086b084321: link becomes ready
[   23.313901] NET: Registered protocol family 15
[   23.326447] Initializing XFRM netlink socket
[   23.570344] NET: Registered protocol family 38
[ 6255.551323] wlxec086b084321: authenticate with 44:c3:46:5f:f0:86
[ 6255.739600] wlxec086b084321: send auth to 44:c3:46:5f:f0:86 (try 1/3)
[ 6255.741342] wlxec086b084321: authenticated
[ 6255.742524] wlxec086b084321: associate with 44:c3:46:5f:f0:86 (try 1/3)
[ 6255.746123] wlxec086b084321: RX AssocResp from 44:c3:46:5f:f0:86 (capab=0x411 status=0 aid=3)
[ 6255.751935] wlxec086b084321: associated
```

```
$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
```

```
$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```

---

## 评论 (14 条)

### 评论 #1 — jlgreathouse (2018-10-29T14:50:34Z)

Looks like the wrong driver is loaded, based on:
```
[    2.944663] amdgpu 0000:06:00.0: kfd not supported on this ASIC
[    3.742628] amdgpu 0000:07:00.0: kfd not supported on this ASIC
```

Could you show the output of:
- `dkms status`
- `modinfo amdkfd | grep filename`

---

### 评论 #2 — ishanshukla97 (2018-10-29T15:44:19Z)

```
$ dkms status
amdgpu, 1.8-192, 4.15.0-29-generic, x86_64: installed
amdgpu, 1.8-192, 4.15.0-30-generic, x86_64: installed

```

```
$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-36-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko

```

---

### 评论 #3 — jlgreathouse (2018-10-29T16:17:17Z)

It looks like you may have installed installed a new kernel and then installed ROCm without rebooting between the two steps. In this case, DKMS will build the new driver for your presently-installed kernel, but after a reboot you will load a new kernel that does not have a driver built for it.

Another question: is there a particular reason that you are running ROCm 1.8 instead of ROCm 1.9?

If you want to stay on ROCm 1.8 for whatever reason, please run the following to build and install the driver on your current kernel:
```bash
sudo dkms build amdgpu/1.8-192
sudo dkms install amdgpu/1.8-192
```

Note, for future reference, that the above commands will only build the ROCm drivers for your currently running kernel. When you install new kernels, a new kernel module *should* be built for that kernel. That appears to have not happened in this case (perhaps because the amdgpu-pro driver was also installed). If you want to build the ROCm drivers for a particular kernel version (e.g. if you swap back and forth between various kernels), you can do:
```
sudo dkms build amdgpu/1.8-192 -k {kernel_version}
sudo dkms install amdgpu/1.8.192 -k {kernel_version}
```

If you want to upgrade to ROCm 1.9, you should be able to do `sudo apt update; sudo apt upgrade` and it will be updated automatically.

---

### 评论 #4 — jlgreathouse (2018-10-29T16:18:54Z)

Oh, I see the problem. 1.8-192 is ROCm 1.8.2. As described in #510, ROCm 1.8.2 is not compatible with Ubuntu kernels above 4.15.0-33. Since you've upgraded your kernel, you must also upgrade to at least ROCm 1.8.3. 

---

### 评论 #5 — jlgreathouse (2018-10-29T16:23:29Z)

Note that if you originally installed ROCm before mid-August, you may need to [update your cached GPG key for our repository](496) to allow the update to succeed.

---

### 评论 #6 — ishanshukla97 (2018-10-29T16:29:59Z)

After
```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
```
and 
```
sudo apt update
sudo apt install rocm-dkms
```
rebooting i get this
```
$ /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
ishan@ishan:~$ 

```

```
$ /opt/rocm/opencl/bin/x86_64/clinfo 
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)

```

---

### 评论 #7 — jlgreathouse (2018-10-29T16:44:48Z)

I assume that if you check your `dkms status` output, it has not changed? What was the output to your `sudo apt install rocm-dkms` command?

---

### 评论 #8 — ishanshukla97 (2018-10-29T16:57:53Z)

After upgrade 
```
dkms status
amdgpu, 1.9-224, 4.15.0-36-generic, x86_64: installed
amdgpu, 1.9-224, 4.15.0-38-generic, x86_64: installed

```
But i still get the ihipException


---

### 评论 #9 — ishanshukla97 (2018-10-29T17:18:38Z)

Sorry I made a mistake. I didnt reboot after upgrade.
Thank you so much it is working now.
And upon running my model everything is freezing and lagging too much. It also says this runnning terminal:

`Allocation of 8456241152 exceeds 10% of system memory.Allocation of 8456241152 exceeds 10% of system memory.Allocation of 8456241152 exceeds 10% of system memory.`

---

### 评论 #10 — ishanshukla97 (2018-10-29T17:27:53Z)

And it only recognized 1 GPU?

```
2018-10-29 22:56:38.538577: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2018-10-29 22:56:38.641885: W tensorflow/stream_executor/rocm/rocm_driver.cc:404] creating context when one is currently active; existing: 0x7f4a5c598f20
2018-10-29 22:56:38.644371: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1451] Found device 0 with properties: 
name: Device 67df
AMDGPU ISA: gfx803
memoryClockRate (GHz) 1.3
pciBusID 0000:07:00.0
Total memory: 4.00GiB
Free memory: 3.75GiB
2018-10-29 22:56:38.644444: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1562] Adding visible gpu devices: 0
2018-10-29 22:56:38.644484: I tensorflow/core/common_runtime/gpu/gpu_device.cc:989] Device interconnect StreamExecutor with strength 1 edge matrix:
2018-10-29 22:56:38.644500: I tensorflow/core/common_runtime/gpu/gpu_device.cc:995]      0 
2018-10-29 22:56:38.644514: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1008] 0:   N 
2018-10-29 22:56:38.644857: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1124] Created TensorFlow device (/device:GPU:0 with 3540 MB memory) -> physical GPU (device: 0, name: Device 67df, pci bus id: 0000:07:00.0)

```

---

### 评论 #11 — jlgreathouse (2018-10-29T17:46:17Z)

You should check with the [tensorflow team](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/) about performance issues.

As for only seeing one GPU: if you look at `dmesg | grep kfd`, what do you see?

---

### 评论 #12 — ishanshukla97 (2018-10-29T19:02:08Z)

```
$ dmesg | grep kfd
[    1.555873] kfd kfd: Initialized module
[    1.556292] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[    2.712166] kfd kfd: Allocated 3969056 bytes on gart
[    2.712305] kfd kfd: added device 1002:67df

```

---

### 评论 #13 — jlgreathouse (2018-10-29T20:00:47Z)

The PCIe slot you're using for your second does not support PCIe atomics, which are [required for your GPU](https://rocm.github.io/hardware.html#supported-cpus).

---

### 评论 #14 — ishanshukla97 (2018-10-29T20:02:21Z)

Thanks a lot for your help!

---
