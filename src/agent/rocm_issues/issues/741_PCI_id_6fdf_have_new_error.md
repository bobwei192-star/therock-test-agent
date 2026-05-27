# PCI id 6fdf have new error

> **Issue #741**
> **状态**: closed
> **创建时间**: 2019-03-17T03:31:48Z
> **更新时间**: 2020-12-01T04:15:39Z
> **关闭时间**: 2020-12-01T04:15:39Z
> **作者**: tu6ge
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/741

## 描述

hello, Recently, when I was trying to install MIOPEN, I had some problems, so I reinstalled rocm. I found that both ROCM and libhsakmt had been upgraded. I set them up according to my PCI ID in the previous way, but I couldn't run rocm. 
my computer info:
```
tu6ge@tu6ge-desktop:~$ groups
tu6ge adm cdrom sudo dip video plugdev lpadmin sambashare
tu6ge@tu6ge-desktop:~$ uname -r
4.15.0-46-generic
tu6ge@tu6ge-desktop:~$ dkms status
amdgpu, 2.2-31, 4.15.0-46-generic, x86_64: installed
tu6ge@tu6ge-desktop:~$ modinfo amdgpu | grep filename
filename:       /lib/modules/4.15.0-46-generic/updates/dkms/amdgpu.ko
tu6ge@tu6ge-desktop:~$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-46-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   13.814938] kfd kfd: Allocated 3969056 bytes on gart
[   13.815354] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-46-generic (buildd@lgw01-amd64-038) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #49-Ubuntu SMP Wed Feb 6 09:33:07 UTC 2019 (Ubuntu 4.15.0-46.49-generic 4.15.18)
[    0.629383] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[   12.868428] amdkcl: loading out-of-tree module taints kernel.
[   12.868449] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   13.338088] [drm] amdgpu kernel modesetting enabled.
[   13.338089] [drm] amdgpu version: 19.10.8.418
[   13.363289] fb: switching to amdgpudrmfb from EFI VGA
[   13.363799] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[   13.391983] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[   13.391985] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   13.392099] [drm] amdgpu: 8192M of VRAM memory ready
[   13.392100] [drm] amdgpu: 8192M of GTT memory ready.
[   13.817209] fbcon: amdgpudrmfb (fb0) is primary device
[   13.817277] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[   13.834552] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:01:00.0 on minor 0
```

---

## 评论 (12 条)

### 评论 #1 — jlgreathouse (2019-03-17T06:30:31Z)

As far as I can tell, there are no errors described in this report.

---

### 评论 #2 — tu6ge (2019-03-17T11:55:01Z)

sorry , I forgot to add the error message. 
```
rocminfo 
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.2/rocminfo/rocminfo.cc. Call returned 4104
```

---

### 评论 #3 — tu6ge (2019-03-17T12:12:03Z)

#719 

---

### 评论 #4 — tu6ge (2019-03-20T11:37:06Z)

my pc is not 4.18 kernel
```
tu6ge@tu6ge-desktop:~$ uname -a
Linux tu6ge-desktop 4.15.0-46-generic #49-Ubuntu SMP Wed Feb 6 09:33:07 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```
please tell me how to do it

---

### 评论 #5 — tu6ge (2019-03-20T13:33:14Z)

I change kernel to 4.13.0-041300-generic,the problem is still unsolved.



---

### 评论 #6 — Djip007 (2019-03-24T11:37:01Z)

can you report result of:
```
cat /sys/bus/pci/drivers/amdgpu/*/power/control
cat /sys/bus/pci/drivers/amdgpu/*/power/runtime_status
```

---

### 评论 #7 — tu6ge (2019-03-24T11:46:24Z)

wait me 

---

### 评论 #8 — Djip007 (2019-03-24T12:30:35Z)

OK so different prob as mine...
In my case i have a card that report "auto"... and "desactivate" with make /dev/kdf "lock"...
may be try:
```
export HSAKMT_DEBUG_LEVEL=7
rocminfo
dmesg
```
to see if there is more trace in log...

---

### 评论 #9 — Djip007 (2019-03-24T13:52:34Z)

ho.. have a look 
https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/roc-2.2.x/src/topology.c#L149

your GPU id steel missing (6FDF)... did you rebuild it too?

---

### 评论 #10 — tu6ge (2019-03-24T13:55:30Z)

```
tu6ge@tu6ge-desktop:~$ cat /sys/bus/pci/drivers/amdgpu/*/power/control
on
tu6ge@tu6ge-desktop:~$ cat /sys/bus/pci/drivers/amdgpu/*/power/runtime_status
active
tu6ge@tu6ge-desktop:~$ export HSAKMT_DEBUG_LEVEL=7
tu6ge@tu6ge-desktop:~$ rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.2/rocminfo/rocminfo.cc. Call returned 4104
tu6ge@tu6ge-desktop:~$ dmesg
[    0.000000] random: get_random_bytes called from start_kernel+0x42/0x4e1 with crng_init=0
[    0.000000] Linux version 4.13.0-041300-generic (kernel@gloin) (gcc version 7.2.0 (Ubuntu 7.2.0-2ubuntu1)) #201709031731 SMP Sun Sep 3 21:33:09 UTC 2017
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.13.0-041300-generic root=UUID=e33adee4-fcbd-4d4a-aff2-5e1214a1ec5e ro quiet splash vt.handoff=1
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
[    0.000000] BIOS-e820: [mem 0x0000000000059000-0x000000000009efff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009f000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x000000008a660fff] usable
[    0.000000] BIOS-e820: [mem 0x000000008a661000-0x000000008a661fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x000000008a662000-0x000000008a662fff] reserved
[    0.000000] BIOS-e820: [mem 0x000000008a663000-0x000000008ea96fff] usable
[    0.000000] BIOS-e820: [mem 0x000000008ea97000-0x000000008edc0fff] reserved
[    0.000000] BIOS-e820: [mem 0x000000008edc1000-0x000000008ef53fff] usable
[    0.000000] BIOS-e820: [mem 0x000000008ef54000-0x000000008f5bbfff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x000000008f5bc000-0x000000008faa3fff] reserved
[    0.000000] BIOS-e820: [mem 0x000000008faa4000-0x000000008fafefff] type 20
[    0.000000] BIOS-e820: [mem 0x000000008faff000-0x000000008fafffff] usable
[    0.000000] BIOS-e820: [mem 0x000000008fb00000-0x000000008fffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000e0000000-0x00000000efffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fe000000-0x00000000fe010fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000026effffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] efi: EFI v2.50 by American Megatrends
[    0.000000] efi:  ACPI=0x8f554000  ACPI 2.0=0x8f554000  SMBIOS=0xf05e0  SMBIOS 3.0=0xf0600  MPS=0xfc430  ESRT=0x8d3ec898 
[    0.000000] random: fast init done
[    0.000000] SMBIOS 3.0.0 present.
[    0.000000] DMI: To Be Filled By O.E.M. To Be Filled By O.E.M./B250M-HDV, BIOS P2.30 01/15/2018
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x26f000 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: write-back
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF uncachable
[    0.000000]   C0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 00C0000000 mask 7FC0000000 uncachable
[    0.000000]   1 base 00A0000000 mask 7FE0000000 uncachable
[    0.000000]   2 base 0090000000 mask 7FF0000000 uncachable
[    0.000000]   3 disabled
[    0.000000]   4 disabled
[    0.000000]   5 disabled
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000]   8 disabled
[    0.000000]   9 disabled
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WC  UC- WT  
[    0.000000] e820: last_pfn = 0x8fb00 max_arch_pfn = 0x400000000
[    0.000000] found SMP MP-table at [mem 0x000fc6b0-0x000fc6bf] mapped at [ffff8fe8000fc6b0]
[    0.000000] esrt: Reserving ESRT space from 0x000000008d3ec898 to 0x000000008d3ec8d0.
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [ffff8fe800095000] 95000 size 24576
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x3db23000, 0x3db23fff] PGTABLE
[    0.000000] BRK [0x3db24000, 0x3db24fff] PGTABLE
[    0.000000] BRK [0x3db25000, 0x3db25fff] PGTABLE
[    0.000000] BRK [0x3db26000, 0x3db26fff] PGTABLE
[    0.000000] BRK [0x3db27000, 0x3db27fff] PGTABLE
[    0.000000] BRK [0x3db28000, 0x3db28fff] PGTABLE
[    0.000000] BRK [0x3db29000, 0x3db29fff] PGTABLE
[    0.000000] BRK [0x3db2a000, 0x3db2afff] PGTABLE
[    0.000000] BRK [0x3db2b000, 0x3db2bfff] PGTABLE
[    0.000000] Secure boot could not be determined
[    0.000000] RAMDISK: [mem 0x34175000-0x360b1fff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x000000008F554000 000024 (v02 ALASKA)
[    0.000000] ACPI: XSDT 0x000000008F5540A0 0000BC (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x000000008F575C40 000114 (v06 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: DSDT 0x000000008F5541F0 021A50 (v02 ALASKA A M I    01072009 INTL 20160422)
[    0.000000] ACPI: FACS 0x000000008F5BBC40 000040
[    0.000000] ACPI: APIC 0x000000008F575D58 000084 (v03 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FPDT 0x000000008F575DE0 000044 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: MCFG 0x000000008F575E28 00003C (v01 ALASKA A M I    01072009 MSFT 00000097)
[    0.000000] ACPI: FIDT 0x000000008F575E68 00009C (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: AAFT 0x000000008F575F08 000279 (v01 ALASKA OEMAAFT  01072009 MSFT 00000097)
[    0.000000] ACPI: SSDT 0x000000008F576188 003154 (v02 SaSsdt SaSsdt   00003000 INTL 20160422)
[    0.000000] ACPI: SSDT 0x000000008F5792E0 0023CB (v02 PegSsd PegSsdt  00001000 INTL 20160422)
[    0.000000] ACPI: HPET 0x000000008F57B6B0 000038 (v01 INTEL  KBL      00000001 MSFT 0000005F)
[    0.000000] ACPI: SSDT 0x000000008F57B6E8 000A2A (v02 INTEL  xh_rvp08 00000000 INTL 20160422)
[    0.000000] ACPI: UEFI 0x000000008F57C118 000042 (v01 INTEL  EDK2     00000002      01000013)
[    0.000000] ACPI: SSDT 0x000000008F57C160 000EDE (v02 CpuRef CpuSsdt  00003000 INTL 20160422)
[    0.000000] ACPI: LPIT 0x000000008F57D040 000094 (v01 INTEL  KBL      00000000 MSFT 0000005F)
[    0.000000] ACPI: WSMT 0x000000008F57D0D8 000028 (v01 INTEL  KBL      00000000 MSFT 0000005F)
[    0.000000] ACPI: DBGP 0x000000008F57D100 000034 (v01 INTEL           00000002 MSFT 0000005F)
[    0.000000] ACPI: DBG2 0x000000008F57D138 000054 (v00 INTEL           00000002 MSFT 0000005F)
[    0.000000] ACPI: BGRT 0x000000008F57D190 000038 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: DMAR 0x000000008F57D1C8 000070 (v01 INTEL  KBL      00000001 INTL 00000001)
[    0.000000] ACPI: ASF! 0x000000008F57D238 0000A0 (v32 INTEL   HCG     00000001 TFSM 000F4240)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x000000026effffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x26efd3000-0x26effdfff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000026effffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x0000000000057fff]
[    0.000000]   node   0: [mem 0x0000000000059000-0x000000000009efff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x000000008a660fff]
[    0.000000]   node   0: [mem 0x000000008a663000-0x000000008ea96fff]
[    0.000000]   node   0: [mem 0x000000008edc1000-0x000000008ef53fff]
[    0.000000]   node   0: [mem 0x000000008faff000-0x000000008fafffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000026effffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x000000026effffff]
[    0.000000] On node 0 totalpages: 2087878
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 27 pages reserved
[    0.000000]   DMA zone: 3997 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 9073 pages used for memmap
[    0.000000]   DMA32 zone: 580649 pages, LIFO batch:31
[    0.000000]   Normal zone: 23488 pages used for memmap
[    0.000000]   Normal zone: 1503232 pages, LIFO batch:31
[    0.000000] ACPI: PM-Timer IO Port: 0x1808
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-119
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x8086a201 base: 0xfed00000
[    0.000000] smpboot: Allowing 4 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x00058000-0x00058fff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009f000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x8a661000-0x8a661fff]
[    0.000000] PM: Registered nosave memory: [mem 0x8a662000-0x8a662fff]
[    0.000000] PM: Registered nosave memory: [mem 0x8ea97000-0x8edc0fff]
[    0.000000] PM: Registered nosave memory: [mem 0x8ef54000-0x8f5bbfff]
[    0.000000] PM: Registered nosave memory: [mem 0x8f5bc000-0x8faa3fff]
[    0.000000] PM: Registered nosave memory: [mem 0x8faa4000-0x8fafefff]
[    0.000000] PM: Registered nosave memory: [mem 0x8fb00000-0x8fffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x90000000-0xdfffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xe0000000-0xefffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf0000000-0xfdffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfe000000-0xfe010fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfe011000-0xfebfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec01000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] e820: [mem 0x90000000-0xdfffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:4 nr_cpu_ids:4 nr_node_ids:1
[    0.000000] percpu: Embedded 39 pages/cpu @ffff8fea6ec00000 s119704 r8192 d31848 u524288
[    0.000000] pcpu-alloc: s119704 r8192 d31848 u524288 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1 2 3 
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 2055226
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.13.0-041300-generic root=UUID=e33adee4-fcbd-4d4a-aff2-5e1214a1ec5e ro quiet splash vt.handoff=1
[    0.000000] PID hash table entries: 4096 (order: 3, 32768 bytes)
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 8027380K/8351512K available (9246K kernel code, 2477K rwdata, 4048K rodata, 2320K init, 2388K bss, 324132K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 37581 entries in 147 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=4.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 524544, nr_irqs: 1024, preallocated irqs: 16
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635855245 ns
[    0.000000] hpet clockevent registered
[    0.004000] tsc: Detected 3000.000 MHz processor
[    0.004000] Calibrating delay loop (skipped), value calculated using timer frequency.. 6000.00 BogoMIPS (lpj=12000000)
[    0.004000] pid_max: default: 32768 minimum: 301
[    0.004000] ACPI: Core revision 20170531
[    0.027953] ACPI: 5 ACPI AML tables successfully acquired and loaded
[    0.028557] Security Framework initialized
[    0.028558] Yama: becoming mindful.
[    0.028569] AppArmor: AppArmor initialized
[    0.029693] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.030219] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes)
[    0.030239] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.030256] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.030388] CPU: Physical Processor ID: 0
[    0.030388] CPU: Processor Core ID: 0
[    0.030392] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.030392] ENERGY_PERF_BIAS: View and update with x86_energy_perf_policy(8)
[    0.030396] mce: CPU supports 10 MCE banks
[    0.030403] CPU0: Thermal monitoring enabled (TM1)
[    0.030419] process: using mwait in idle threads
[    0.030421] Last level iTLB entries: 4KB 128, 2MB 8, 4MB 8
[    0.030422] Last level dTLB entries: 4KB 64, 2MB 0, 4MB 0, 1GB 4
[    0.030488] Freeing SMP alternatives memory: 36K
[    0.032684] smpboot: Max logical packages: 1
[    0.032688] DMAR: Host address width 39
[    0.032689] DMAR: DRHD base: 0x000000fed90000 flags: 0x1
[    0.032693] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap d2008c40660462 ecap f050da
[    0.032694] DMAR: RMRR base: 0x0000008ed51000 end: 0x0000008ed70fff
[    0.032696] DMAR-IR: IOAPIC id 2 under DRHD base  0xfed90000 IOMMU 0
[    0.032696] DMAR-IR: HPET id 0 under DRHD base 0xfed90000
[    0.032697] DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
[    0.033991] DMAR-IR: Enabled IRQ remapping in x2apic mode
[    0.033992] x2apic enabled
[    0.034001] Switched APIC routing to cluster x2apic.
[    0.038101] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.077822] TSC deadline timer enabled
[    0.077827] smpboot: CPU0: Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz (family: 0x6, model: 0x9e, stepping: 0x9)
[    0.077866] Performance Events: PEBS fmt3+, Skylake events, 32-deep LBR, full-width counters, Intel PMU driver.
[    0.077889] ... version:                4
[    0.077889] ... bit width:              48
[    0.077889] ... generic registers:      8
[    0.077890] ... value mask:             0000ffffffffffff
[    0.077890] ... max period:             00007fffffffffff
[    0.077891] ... fixed-purpose events:   3
[    0.077891] ... event mask:             00000007000000ff
[    0.077918] Hierarchical SRCU implementation.
[    0.078474] NMI watchdog: enabled on all CPUs, permanently consumes one hw-PMU counter.
[    0.078483] smp: Bringing up secondary CPUs ...
[    0.078526] x86: Booting SMP configuration:
[    0.078527] .... node  #0, CPUs:      #1 #2 #3
[    0.316024] smp: Brought up 1 node, 4 CPUs
[    0.316024] smpboot: Total of 4 processors activated (24003.52 BogoMIPS)
[    0.318622] devtmpfs: initialized
[    0.318622] x86/mm: Memory block size: 128MB
[    0.318622] evm: security.selinux
[    0.318622] evm: security.SMACK64
[    0.318622] evm: security.SMACK64EXEC
[    0.318622] evm: security.SMACK64TRANSMUTE
[    0.318622] evm: security.SMACK64MMAP
[    0.318622] evm: security.ima
[    0.318622] evm: security.capability
[    0.318622] PM: Registering ACPI NVS region [mem 0x8a661000-0x8a661fff] (4096 bytes)
[    0.318622] PM: Registering ACPI NVS region [mem 0x8ef54000-0x8f5bbfff] (6717440 bytes)
[    0.318622] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.318622] futex hash table entries: 1024 (order: 4, 65536 bytes)
[    0.318622] pinctrl core: initialized pinctrl subsystem
[    0.318622] RTC time: 13:50:58, date: 03/24/19
[    0.318622] NET: Registered protocol family 16
[    0.318622] cpuidle: using governor ladder
[    0.318622] cpuidle: using governor menu
[    0.318622] PCCT header not found.
[    0.318622] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.318622] ACPI: bus type PCI registered
[    0.318622] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.318622] PCI: MMCONFIG for domain 0000 [bus 00-ff] at [mem 0xe0000000-0xefffffff] (base 0xe0000000)
[    0.318622] PCI: MMCONFIG at [mem 0xe0000000-0xefffffff] reserved in E820
[    0.318622] PCI: Using configuration type 1 for base access
[    0.320564] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.320564] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.320564] ACPI: Added _OSI(Module Device)
[    0.320564] ACPI: Added _OSI(Processor Device)
[    0.320564] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.320564] ACPI: Added _OSI(Processor Aggregator Device)
[    0.320837] ACPI: Executed 32 blocks of module-level executable AML code
[    0.329366] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.332154] ACPI: Dynamic OEM Table Load:
[    0.332161] ACPI: SSDT 0xFFFF8FEA64D82800 000693 (v02 PmRef  Cpu0Ist  00003000 INTL 20160422)
[    0.332161] ACPI: Executed 1 blocks of module-level executable AML code
[    0.332170] ACPI: \_PR_.CPU0: _OSC native thermal LVT Acked
[    0.332776] ACPI: Dynamic OEM Table Load:
[    0.332780] ACPI: SSDT 0xFFFF8FEA64ECD000 0003FF (v02 PmRef  Cpu0Cst  00003001 INTL 20160422)
[    0.332880] ACPI: Executed 1 blocks of module-level executable AML code
[    0.333170] ACPI: Dynamic OEM Table Load:
[    0.333174] ACPI: SSDT 0xFFFF8FEA64EC0000 00065C (v02 PmRef  ApIst    00003000 INTL 20160422)
[    0.333425] ACPI: Executed 1 blocks of module-level executable AML code
[    0.333567] ACPI: Dynamic OEM Table Load:
[    0.333570] ACPI: SSDT 0xFFFF8FEA64EBF200 00018A (v02 PmRef  ApCst    00003000 INTL 20160422)
[    0.333668] ACPI: Executed 1 blocks of module-level executable AML code
[    0.335088] ACPI: Interpreter enabled
[    0.335121] ACPI: (supports S0 S3 S4 S5)
[    0.335122] ACPI: Using IOAPIC for interrupt routing
[    0.335184] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.340719] ACPI: Power Resource [WRST] (on)
[    0.340975] ACPI: Power Resource [WRST] (on)
[    0.341229] ACPI: Power Resource [WRST] (on)
[    0.341482] ACPI: Power Resource [WRST] (on)
[    0.341734] ACPI: Power Resource [WRST] (on)
[    0.341989] ACPI: Power Resource [WRST] (on)
[    0.342240] ACPI: Power Resource [WRST] (on)
[    0.342493] ACPI: Power Resource [WRST] (on)
[    0.342744] ACPI: Power Resource [WRST] (on)
[    0.342999] ACPI: Power Resource [WRST] (on)
[    0.343275] ACPI: Power Resource [WRST] (on)
[    0.343530] ACPI: Power Resource [WRST] (on)
[    0.343801] ACPI: Power Resource [WRST] (on)
[    0.344057] ACPI: Power Resource [WRST] (on)
[    0.344309] ACPI: Power Resource [WRST] (on)
[    0.344563] ACPI: Power Resource [WRST] (on)
[    0.344816] ACPI: Power Resource [WRST] (on)
[    0.345796] ACPI: Power Resource [WRST] (on)
[    0.346050] ACPI: Power Resource [WRST] (on)
[    0.346308] ACPI: Power Resource [WRST] (on)
[    0.354596] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-fe])
[    0.354600] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.354625] acpi PNP0A08:00: _OSC failed (AE_ERROR); disabling ASPM
[    0.355117] PCI host bridge to bus 0000:00
[    0.355118] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.355119] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.355120] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.355121] pci_bus 0000:00: root bus resource [mem 0x90000000-0xdfffffff window]
[    0.355121] pci_bus 0000:00: root bus resource [mem 0xfd000000-0xfe7fffff window]
[    0.355122] pci_bus 0000:00: root bus resource [bus 00-fe]
[    0.355128] pci 0000:00:00.0: [8086:591f] type 00 class 0x060000
[    0.355213] pci 0000:00:01.0: [8086:1901] type 01 class 0x060400
[    0.355245] pci 0000:00:01.0: PME# supported from D0 D3hot D3cold
[    0.355434] pci 0000:00:14.0: [8086:a2af] type 00 class 0x0c0330
[    0.355453] pci 0000:00:14.0: reg 0x10: [mem 0xdff30000-0xdff3ffff 64bit]
[    0.355509] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    0.355651] pci 0000:00:14.2: [8086:a2b1] type 00 class 0x118000
[    0.355669] pci 0000:00:14.2: reg 0x10: [mem 0xdff4e000-0xdff4efff 64bit]
[    0.355799] pci 0000:00:16.0: [8086:a2ba] type 00 class 0x078000
[    0.355818] pci 0000:00:16.0: reg 0x10: [mem 0xdff4d000-0xdff4dfff 64bit]
[    0.355880] pci 0000:00:16.0: PME# supported from D3hot
[    0.355992] pci 0000:00:17.0: [8086:a282] type 00 class 0x010601
[    0.356007] pci 0000:00:17.0: reg 0x10: [mem 0xdff48000-0xdff49fff]
[    0.356012] pci 0000:00:17.0: reg 0x14: [mem 0xdff4c000-0xdff4c0ff]
[    0.356018] pci 0000:00:17.0: reg 0x18: [io  0xf050-0xf057]
[    0.356024] pci 0000:00:17.0: reg 0x1c: [io  0xf040-0xf043]
[    0.356030] pci 0000:00:17.0: reg 0x20: [io  0xf020-0xf03f]
[    0.356036] pci 0000:00:17.0: reg 0x24: [mem 0xdff4b000-0xdff4b7ff]
[    0.356069] pci 0000:00:17.0: PME# supported from D3hot
[    0.356171] pci 0000:00:1c.0: [8086:a294] type 01 class 0x060400
[    0.356223] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.356348] pci 0000:00:1c.6: [8086:a296] type 01 class 0x060400
[    0.356400] pci 0000:00:1c.6: PME# supported from D0 D3hot D3cold
[    0.356510] pci 0000:00:1d.0: [8086:a298] type 01 class 0x060400
[    0.356569] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
[    0.356703] pci 0000:00:1f.0: [8086:a2c8] type 00 class 0x060100
[    0.356887] pci 0000:00:1f.2: [8086:a2a1] type 00 class 0x058000
[    0.356900] pci 0000:00:1f.2: reg 0x10: [mem 0xdff44000-0xdff47fff]
[    0.357034] pci 0000:00:1f.3: [8086:a2f0] type 00 class 0x040300
[    0.357059] pci 0000:00:1f.3: reg 0x10: [mem 0xdff40000-0xdff43fff 64bit]
[    0.357087] pci 0000:00:1f.3: reg 0x20: [mem 0xdff20000-0xdff2ffff 64bit]
[    0.357131] pci 0000:00:1f.3: PME# supported from D3hot D3cold
[    0.357277] pci 0000:00:1f.4: [8086:a2a3] type 00 class 0x0c0500
[    0.357336] pci 0000:00:1f.4: reg 0x10: [mem 0xdff4a000-0xdff4a0ff 64bit]
[    0.357405] pci 0000:00:1f.4: reg 0x20: [io  0xf000-0xf01f]
[    0.357570] pci 0000:00:1f.6: [8086:15b8] type 00 class 0x020000
[    0.357595] pci 0000:00:1f.6: reg 0x10: [mem 0xdff00000-0xdff1ffff]
[    0.357697] pci 0000:00:1f.6: PME# supported from D0 D3hot D3cold
[    0.357815] pci 0000:01:00.0: [1002:6fdf] type 00 class 0x030000
[    0.357832] pci 0000:01:00.0: reg 0x10: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.357839] pci 0000:01:00.0: reg 0x18: [mem 0xd0000000-0xd01fffff 64bit pref]
[    0.357844] pci 0000:01:00.0: reg 0x20: [io  0xe000-0xe0ff]
[    0.357849] pci 0000:01:00.0: reg 0x24: [mem 0xdfe00000-0xdfe3ffff]
[    0.357854] pci 0000:01:00.0: reg 0x30: [mem 0xdfe40000-0xdfe5ffff pref]
[    0.357897] pci 0000:01:00.0: supports D1 D2
[    0.357898] pci 0000:01:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.357941] pci 0000:01:00.1: [1002:aaf0] type 00 class 0x040300
[    0.357956] pci 0000:01:00.1: reg 0x10: [mem 0xdfe60000-0xdfe63fff 64bit]
[    0.358010] pci 0000:01:00.1: supports D1 D2
[    0.368044] pci 0000:00:01.0: PCI bridge to [bus 01]
[    0.368046] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    0.368047] pci 0000:00:01.0:   bridge window [mem 0xdfe00000-0xdfefffff]
[    0.368049] pci 0000:00:01.0:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.368118] pci 0000:02:00.0: [10ec:8821] type 00 class 0x028000
[    0.368144] pci 0000:02:00.0: reg 0x10: [io  0xd000-0xd0ff]
[    0.368165] pci 0000:02:00.0: reg 0x18: [mem 0xdfd00000-0xdfd03fff 64bit]
[    0.368258] pci 0000:02:00.0: supports D1 D2
[    0.368259] pci 0000:02:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.368367] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    0.368369] pci 0000:00:1c.0:   bridge window [io  0xd000-0xdfff]
[    0.368371] pci 0000:00:1c.0:   bridge window [mem 0xdfd00000-0xdfdfffff]
[    0.368424] pci 0000:00:1c.6: PCI bridge to [bus 03]
[    0.368475] pci 0000:00:1d.0: PCI bridge to [bus 04]
[    0.369961] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.369999] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 *10 11 12 14 15)
[    0.370035] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.370071] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.370106] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.370142] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.370178] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.370214] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.370421] ACPI: Enabled 4 GPEs in block 00 to 7F
[    0.370470] pci 0000:01:00.0: vgaarb: setting as boot VGA device
[    0.370470] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.370470] pci 0000:01:00.0: vgaarb: bridge control possible
[    0.370470] vgaarb: loaded
[    0.370470] SCSI subsystem initialized
[    0.370470] libata version 3.00 loaded.
[    0.370470] ACPI: bus type USB registered
[    0.370470] usbcore: registered new interface driver usbfs
[    0.370470] usbcore: registered new interface driver hub
[    0.370470] usbcore: registered new device driver usb
[    0.370470] EDAC MC: Ver: 3.0.0
[    0.370470] Registered efivars operations
[    0.387205] PCI: Using ACPI for IRQ routing
[    0.415037] PCI: pci_cache_line_size set to 64 bytes
[    0.415077] e820: reserve RAM buffer [mem 0x00058000-0x0005ffff]
[    0.415078] e820: reserve RAM buffer [mem 0x0009f000-0x0009ffff]
[    0.415078] e820: reserve RAM buffer [mem 0x8a661000-0x8bffffff]
[    0.415079] e820: reserve RAM buffer [mem 0x8ea97000-0x8fffffff]
[    0.415080] e820: reserve RAM buffer [mem 0x8ef54000-0x8fffffff]
[    0.415081] e820: reserve RAM buffer [mem 0x8fb00000-0x8fffffff]
[    0.415081] e820: reserve RAM buffer [mem 0x26f000000-0x26fffffff]
[    0.415134] NetLabel: Initializing
[    0.415134] NetLabel:  domain hash size = 128
[    0.415134] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.415144] NetLabel:  unlabeled traffic allowed by default
[    0.415152] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    0.415152] hpet0: 8 comparators, 64-bit 24.000000 MHz counter
[    0.417023] clocksource: Switched to clocksource hpet
[    0.422876] VFS: Disk quotas dquot_6.6.0
[    0.422885] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.422942] AppArmor: AppArmor Filesystem Enabled
[    0.422967] pnp: PnP ACPI init
[    0.423198] system 00:00: [io  0x0280-0x028f] has been reserved
[    0.423199] system 00:00: [io  0x0290-0x029f] has been reserved
[    0.423200] system 00:00: [io  0x02a0-0x02af] has been reserved
[    0.423201] system 00:00: [io  0x02b0-0x02bf] has been reserved
[    0.423203] system 00:00: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.423564] pnp 00:01: [dma 3]
[    0.423663] pnp 00:01: Plug and Play ACPI device, IDs PNP0401 (active)
[    0.423832] pnp 00:02: [dma 0 disabled]
[    0.423856] pnp 00:02: Plug and Play ACPI device, IDs PNP0501 (active)
[    0.423950] system 00:03: [io  0x0680-0x069f] has been reserved
[    0.423951] system 00:03: [io  0xffff] has been reserved
[    0.423951] system 00:03: [io  0xffff] has been reserved
[    0.423952] system 00:03: [io  0xffff] has been reserved
[    0.423953] system 00:03: [io  0x1800-0x18fe] has been reserved
[    0.423954] system 00:03: [io  0x164e-0x164f] has been reserved
[    0.423955] system 00:03: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.424048] system 00:04: [io  0x0800-0x087f] has been reserved
[    0.424049] system 00:04: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.424061] pnp 00:05: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.424084] system 00:06: [io  0x1854-0x1857] has been reserved
[    0.424085] system 00:06: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    0.424248] system 00:07: [mem 0xfed10000-0xfed17fff] has been reserved
[    0.424249] system 00:07: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.424250] system 00:07: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.424251] system 00:07: [mem 0xe0000000-0xefffffff] has been reserved
[    0.424251] system 00:07: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.424252] system 00:07: [mem 0xfed90000-0xfed93fff] could not be reserved
[    0.424253] system 00:07: [mem 0xfed45000-0xfed8ffff] has been reserved
[    0.424254] system 00:07: [mem 0xff000000-0xffffffff] has been reserved
[    0.424255] system 00:07: [mem 0xfee00000-0xfeefffff] could not be reserved
[    0.424256] system 00:07: [mem 0xdffe0000-0xdfffffff] has been reserved
[    0.424257] system 00:07: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.424281] system 00:08: [mem 0xfd000000-0xfdabffff] has been reserved
[    0.424282] system 00:08: [mem 0xfdad0000-0xfdadffff] has been reserved
[    0.424283] system 00:08: [mem 0xfdb00000-0xfdffffff] has been reserved
[    0.424284] system 00:08: [mem 0xfe000000-0xfe01ffff] could not be reserved
[    0.424285] system 00:08: [mem 0xfe036000-0xfe03bfff] has been reserved
[    0.424286] system 00:08: [mem 0xfe03d000-0xfe3fffff] has been reserved
[    0.424286] system 00:08: [mem 0xfe410000-0xfe7fffff] has been reserved
[    0.424288] system 00:08: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.424520] system 00:09: [io  0xff00-0xfffe] has been reserved
[    0.424521] system 00:09: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.425380] system 00:0a: [mem 0xfdaf0000-0xfdafffff] has been reserved
[    0.425381] system 00:0a: [mem 0xfdae0000-0xfdaeffff] has been reserved
[    0.425382] system 00:0a: [mem 0xfdac0000-0xfdacffff] has been reserved
[    0.425383] system 00:0a: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.425866] pnp: PnP ACPI: found 11 devices
[    0.433328] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.433349] pci 0000:00:01.0: PCI bridge to [bus 01]
[    0.433350] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    0.433352] pci 0000:00:01.0:   bridge window [mem 0xdfe00000-0xdfefffff]
[    0.433354] pci 0000:00:01.0:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.433356] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    0.433357] pci 0000:00:1c.0:   bridge window [io  0xd000-0xdfff]
[    0.433360] pci 0000:00:1c.0:   bridge window [mem 0xdfd00000-0xdfdfffff]
[    0.433364] pci 0000:00:1c.6: PCI bridge to [bus 03]
[    0.433370] pci 0000:00:1d.0: PCI bridge to [bus 04]
[    0.433377] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.433378] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.433379] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.433380] pci_bus 0000:00: resource 7 [mem 0x90000000-0xdfffffff window]
[    0.433381] pci_bus 0000:00: resource 8 [mem 0xfd000000-0xfe7fffff window]
[    0.433381] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    0.433382] pci_bus 0000:01: resource 1 [mem 0xdfe00000-0xdfefffff]
[    0.433383] pci_bus 0000:01: resource 2 [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.433383] pci_bus 0000:02: resource 0 [io  0xd000-0xdfff]
[    0.433384] pci_bus 0000:02: resource 1 [mem 0xdfd00000-0xdfdfffff]
[    0.433487] NET: Registered protocol family 2
[    0.433580] TCP established hash table entries: 65536 (order: 7, 524288 bytes)
[    0.433664] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.433801] TCP: Hash tables configured (established 65536 bind 65536)
[    0.433820] UDP hash table entries: 4096 (order: 5, 131072 bytes)
[    0.433839] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes)
[    0.433873] NET: Registered protocol family 1
[    0.434500] pci 0000:01:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.434505] PCI: CLS 64 bytes, default 64
[    0.434527] Unpacking initramfs...
[    0.814415] Freeing initrd memory: 31988K
[    0.814440] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.814443] software IO TLB [mem 0x862c8000-0x8a2c8000] (64MB) mapped at [ffff8fe8862c8000-ffff8fe88a2c7fff]
[    0.814573] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x2b3e459bf4c, max_idle_ns: 440795289890 ns
[    0.814675] Scanning for low memory corruption every 60 seconds
[    0.814919] audit: initializing netlink subsys (disabled)
[    0.814973] audit: type=2000 audit(1553435457.814:1): state=initialized audit_enabled=0 res=1
[    0.815255] Initialise system trusted keyrings
[    0.815261] Key type blacklist registered
[    0.815312] workingset: timestamp_bits=36 max_order=21 bucket_order=0
[    0.816062] zbud: loaded
[    0.816304] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.816436] fuse init (API version 7.26)
[    0.818877] Key type asymmetric registered
[    0.818877] Asymmetric key parser 'x509' registered
[    0.818903] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    0.818954] io scheduler noop registered
[    0.818955] io scheduler deadline registered
[    0.818972] io scheduler cfq registered (default)
[    0.819601] efifb: probing for efifb
[    0.819610] efifb: framebuffer at 0xc0000000, using 8128k, total 8128k
[    0.819611] efifb: mode is 1920x1080x32, linelength=7680, pages=1
[    0.819611] efifb: scrolling: redraw
[    0.819612] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    0.822653] Console: switching to colour frame buffer device 240x67
[    0.825593] fb0: EFI VGA frame buffer device
[    0.825597] intel_idle: MWAIT substates: 0x142120
[    0.825597] intel_idle: v0.4.1 model 0x9E
[    0.825746] intel_idle: lapic_timer_reliable_states 0xffffffff
[    0.825829] input: Sleep Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0E:00/input/input0
[    0.825838] ACPI: Sleep Button [SLPB]
[    0.825856] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input1
[    0.825863] ACPI: Power Button [PWRB]
[    0.825880] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input2
[    0.825927] ACPI: Power Button [PWRF]
[    0.826063] GHES: HEST is not enabled!
[    0.826128] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.846894] 00:02: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    0.848669] Linux agpgart interface v0.103
[    0.849956] loop: module loaded
[    0.850048] libphy: Fixed MDIO Bus: probed
[    0.850049] tun: Universal TUN/TAP device driver, 1.6
[    0.850088] PPP generic driver version 2.4.2
[    0.850131] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.850133] ehci-pci: EHCI PCI platform driver
[    0.850138] ehci-platform: EHCI generic platform driver
[    0.850142] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.850143] ohci-pci: OHCI PCI platform driver
[    0.850148] ohci-platform: OHCI generic platform driver
[    0.850151] uhci_hcd: USB Universal Host Controller Interface driver
[    0.850253] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.850256] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 1
[    0.851336] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x00009810
[    0.851339] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
[    0.851397] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    0.851398] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.851399] usb usb1: Product: xHCI Host Controller
[    0.851399] usb usb1: Manufacturer: Linux 4.13.0-041300-generic xhci-hcd
[    0.851400] usb usb1: SerialNumber: 0000:00:14.0
[    0.851478] hub 1-0:1.0: USB hub found
[    0.851490] hub 1-0:1.0: 12 ports detected
[    0.852128] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.852130] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 2
[    0.852149] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003
[    0.852150] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.852150] usb usb2: Product: xHCI Host Controller
[    0.852151] usb usb2: Manufacturer: Linux 4.13.0-041300-generic xhci-hcd
[    0.852151] usb usb2: SerialNumber: 0000:00:14.0
[    0.852251] hub 2-0:1.0: USB hub found
[    0.852258] hub 2-0:1.0: 6 ports detected
[    0.852583] i8042: PNP: No PS/2 controller found.
[    0.852713] mousedev: PS/2 mouse device common for all mice
[    0.852995] rtc_cmos 00:05: RTC can wake from S4
[    0.853388] rtc_cmos 00:05: rtc core: registered rtc_cmos as rtc0
[    0.853467] rtc_cmos 00:05: alarms up to one month, y3k, 242 bytes nvram, hpet irqs
[    0.853471] i2c /dev entries driver
[    0.853496] device-mapper: uevent: version 1.0.3
[    0.853566] device-mapper: ioctl: 4.36.0-ioctl (2017-06-09) initialised: dm-devel@redhat.com
[    0.853568] intel_pstate: Intel P-state driver initializing
[    0.854064] intel_pstate: HWP enabled
[    0.854264] ledtrig-cpu: registered to indicate activity on CPUs
[    0.854266] EFI Variables Facility v0.08 2004-May-17
[    0.874921] NET: Registered protocol family 10
[    0.877948] Segment Routing with IPv6
[    0.877959] NET: Registered protocol family 17
[    0.877965] Key type dns_resolver registered
[    0.878284] RAS: Correctable Errors collector initialized.
[    0.878299] microcode: sig=0x906e9, pf=0x2, revision=0x80
[    0.878414] microcode: Microcode Update Driver: v2.2.
[    0.878419] sched_clock: Marking stable (878411935, 0)->(877832721, 579214)
[    0.878690] registered taskstats version 1
[    0.878695] Loading compiled-in X.509 certificates
[    0.880244] Loaded X.509 cert 'Build time autogenerated kernel key: 2977791a6bc138cb597bcddff841bb4e6c0cdbe0'
[    0.880253] zswap: loaded using pool lzo/zbud
[    0.881631] Key type big_key registered
[    0.881634] Key type trusted registered
[    0.882776] Key type encrypted registered
[    0.882792] AppArmor: AppArmor sha1 policy hashing enabled
[    0.882794] ima: No TPM chip found, activating TPM-bypass! (rc=-19)
[    0.882805] evm: HMAC attrs: 0x1
[    0.883415]   Magic number: 11:949:837
[    0.883620] rtc_cmos 00:05: setting system clock to 2019-03-24 13:50:58 UTC (1553435458)
[    0.883732] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    0.883732] EDD information not available.
[    0.883757] PM: Hibernation image not present or could not be loaded.
[    0.885023] Freeing unused kernel memory: 2320K
[    0.885024] Write protecting the kernel read-only data: 14336k
[    0.885369] Freeing unused kernel memory: 980K
[    0.885504] Freeing unused kernel memory: 48K
[    0.886563] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    0.922284] hidraw: raw HID events driver (C) Jiri Kosina
[    0.942751] ahci 0000:00:17.0: version 3.0
[    0.942915] pps_core: LinuxPPS API ver. 1 registered
[    0.942916] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.942997] ahci 0000:00:17.0: AHCI 0001.0301 32 slots 6 ports 6 Gbps 0x3f impl SATA mode
[    0.942998] ahci 0000:00:17.0: flags: 64bit ncq sntf led clo only pio slum part ems deso sadm sds apst 
[    0.943686] PTP clock support registered
[    0.956777] e1000e: Intel(R) PRO/1000 Network Driver - 3.2.6-k
[    0.956778] e1000e: Copyright(c) 1999 - 2015 Intel Corporation.
[    1.004557] scsi host0: ahci
[    1.004751] scsi host1: ahci
[    1.004897] scsi host2: ahci
[    1.005338] scsi host3: ahci
[    1.005598] scsi host4: ahci
[    1.005815] scsi host5: ahci
[    1.005862] ata1: SATA max UDMA/133 abar m2048@0xdff4b000 port 0xdff4b100 irq 122
[    1.005866] ata2: SATA max UDMA/133 abar m2048@0xdff4b000 port 0xdff4b180 irq 122
[    1.005867] ata3: SATA max UDMA/133 abar m2048@0xdff4b000 port 0xdff4b200 irq 122
[    1.005868] ata4: SATA max UDMA/133 abar m2048@0xdff4b000 port 0xdff4b280 irq 122
[    1.005869] ata5: SATA max UDMA/133 abar m2048@0xdff4b000 port 0xdff4b300 irq 122
[    1.005870] ata6: SATA max UDMA/133 abar m2048@0xdff4b000 port 0xdff4b380 irq 122
[    1.006083] e1000e 0000:00:1f.6: Interrupt Throttling Rate (ints/sec) set to dynamic conservative mode
[    1.180115] usb 1-1: new low-speed USB device number 2 using xhci_hcd
[    1.276154] e1000e 0000:00:1f.6 0000:00:1f.6 (uninitialized): registered PHC clock
[    1.320830] ata4: SATA link down (SStatus 4 SControl 300)
[    1.320855] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.320867] ata2: SATA link down (SStatus 4 SControl 300)
[    1.320892] ata3: SATA link down (SStatus 4 SControl 300)
[    1.320948] ata5: SATA link down (SStatus 4 SControl 300)
[    1.320977] ata6: SATA link down (SStatus 4 SControl 300)
[    1.321702] ata1.00: ATA-8: ST1000DM010-2EP102, CC43, max UDMA/133
[    1.321704] ata1.00: 1953525168 sectors, multi 16: LBA48 NCQ (depth 31/32), AA
[    1.322483] ata1.00: configured for UDMA/133
[    1.322725] scsi 0:0:0:0: Direct-Access     ATA      ST1000DM010-2EP1 CC43 PQ: 0 ANSI: 5
[    1.325505] usb 1-1: New USB device found, idVendor=1c4f, idProduct=0002
[    1.325506] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    1.325507] usb 1-1: Product: USB Keyboard
[    1.325508] usb 1-1: Manufacturer: SIGMACHIP
[    1.356621] e1000e 0000:00:1f.6 eth0: (PCI Express:2.5GT/s:Width x1) 70:85:c2:5c:65:03
[    1.356622] e1000e 0000:00:1f.6 eth0: Intel(R) PRO/1000 Network Connection
[    1.356732] e1000e 0000:00:1f.6 eth0: MAC: 12, PHY: 12, PBA No: FFFFFF-0FF
[    1.357228] e1000e 0000:00:1f.6 enp0s31f6: renamed from eth0
[    1.360207] sd 0:0:0:0: [sda] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    1.360208] sd 0:0:0:0: [sda] 4096-byte physical blocks
[    1.360224] sd 0:0:0:0: [sda] Write Protect is off
[    1.360225] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    1.360229] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.360248] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    1.400676]  sda: sda1 sda2 sda3 sda4 sda5 sda6 sda7 sda8 sda9
[    1.401528] sd 0:0:0:0: [sda] Attached SCSI disk
[    1.444106] usb 1-2: new low-speed USB device number 3 using xhci_hcd
[    1.587456] usb 1-2: New USB device found, idVendor=093a, idProduct=2521
[    1.587457] usb 1-2: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[    1.587458] usb 1-2: Product: USB OPTICAL MOUSE
[    1.708055] usb 1-7: new full-speed USB device number 4 using xhci_hcd
[    1.820245] clocksource: Switched to clocksource tsc
[    1.849564] usb 1-7: New USB device found, idVendor=0a12, idProduct=0001
[    1.849565] usb 1-7: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.857536] usbcore: registered new interface driver usbhid
[    1.857537] usbhid: USB HID core driver
[    1.858514] input: SIGMACHIP USB Keyboard as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.0/0003:1C4F:0002.0001/input/input3
[    1.916277] hid-generic 0003:1C4F:0002.0001: input,hidraw0: USB HID v1.10 Keyboard [SIGMACHIP USB Keyboard] on usb-0000:00:14.0-1/input0
[    1.916389] input: SIGMACHIP USB Keyboard as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.1/0003:1C4F:0002.0002/input/input4
[    1.976290] hid-generic 0003:1C4F:0002.0002: input,hidraw1: USB HID v1.10 Device [SIGMACHIP USB Keyboard] on usb-0000:00:14.0-1/input1
[    1.976363] input: USB OPTICAL MOUSE as /devices/pci0000:00/0000:00:14.0/usb1/1-2/1-2:1.0/0003:093A:2521.0003/input/input5
[    1.976629] hid-generic 0003:093A:2521.0003: input,hidraw2: USB HID v1.11 Mouse [USB OPTICAL MOUSE] on usb-0000:00:14.0-2/input0
[    2.281737] EXT4-fs (sda9): mounted filesystem with ordered data mode. Opts: (null)
[    3.291077] ip_tables: (C) 2000-2006 Netfilter Core Team
[    3.383425] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    3.390600] systemd[1]: Detected architecture x86-64.
[    3.400704] systemd[1]: Set hostname to <tu6ge-desktop>.
[    3.434529] random: crng init done
[    4.849251] systemd[1]: Created slice User and Session Slice.
[    4.849414] systemd[1]: Created slice System Slice.
[    4.849450] systemd[1]: Listening on udev Kernel Socket.
[    4.849492] systemd[1]: Listening on Journal Socket.
[    4.849877] systemd[1]: Mounting Kernel Debug File System...
[    4.849961] systemd[1]: Listening on Journal Audit Socket.
[    4.850002] systemd[1]: Listening on fsck to fsckd communication Socket.
[    5.360019] lp: driver loaded but no devices found
[    5.361849] ppdev: user-space parallel port driver
[    5.373814] parport_pc 00:01: reported by Plug and Play ACPI
[    5.373876] parport0: PC-style at 0x378 (0x778), irq 5, dma 3 [PCSPP,TRISTATE,COMPAT,EPP,ECP,DMA]
[    5.438786] EXT4-fs (sda9): re-mounted. Opts: errors=remount-ro
[    5.472143] lp0: using parport0 (interrupt-driven).
[    5.569293] systemd-journald[253]: Received request to flush runtime journal from PID 1
[    5.811993] Adding 2097148k swap on /swapfile.  Priority:-1 extents:6 across:2260988k FS
[    7.250562] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    8.655723] mei_me 0000:00:16.0: enabling device (0000 -> 0002)
[    8.996729] RAPL PMU: API unit is 2^-32 Joules, 5 fixed counters, 655360 ms ovfl timer
[    8.996730] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
[    8.996730] RAPL PMU: hw unit of domain package 2^-14 Joules
[    8.996730] RAPL PMU: hw unit of domain dram 2^-14 Joules
[    8.996731] RAPL PMU: hw unit of domain pp1-gpu 2^-14 Joules
[    8.996731] RAPL PMU: hw unit of domain psys 2^-14 Joules
[    8.998157] Bluetooth: Core ver 2.22
[    8.998166] NET: Registered protocol family 31
[    8.998166] Bluetooth: HCI device and connection manager initialized
[    8.998168] Bluetooth: HCI socket layer initialized
[    8.998169] Bluetooth: L2CAP socket layer initialized
[    8.998172] Bluetooth: SCO socket layer initialized
[    9.743607] usbcore: registered new interface driver btusb
[    9.780681] Bluetooth: HCI UART driver ver 2.3
[    9.780682] Bluetooth: HCI UART protocol H4 registered
[    9.780682] Bluetooth: HCI UART protocol BCSP registered
[    9.780690] Bluetooth: HCI UART protocol LL registered
[    9.780691] Bluetooth: HCI UART protocol ATH3K registered
[    9.780691] Bluetooth: HCI UART protocol Three-wire (H5) registered
[    9.780704] Bluetooth: HCI UART protocol Intel registered
[    9.780709] Bluetooth: HCI UART protocol Broadcom registered
[    9.780710] Bluetooth: HCI UART protocol QCA registered
[    9.780710] Bluetooth: HCI UART protocol AG6XX registered
[    9.780710] Bluetooth: HCI UART protocol Marvell registered
[    9.789457] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    9.789458] AMD IOMMUv2 functionality not available on this system
[    9.794332] PKCS#7 signature not signed with a trusted key
[    9.794352] amdkcl: loading out-of-tree module taints kernel.
[    9.794370] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    9.847941] Warning: fail to get symbol drm_fb_helper_release_fbi, replace it with kcl stub
[   10.128459] PKCS#7 signature not signed with a trusted key
[   10.136841] PKCS#7 signature not signed with a trusted key
[   10.137779] PKCS#7 signature not signed with a trusted key
[   10.189842] rtl8821ae 0000:02:00.0: enabling device (0000 -> 0003)
[   10.202651] rtl8821ae: Using firmware rtlwifi/rtl8821aefw_29.bin
[   10.202653] rtl8821ae: Using firmware rtlwifi/rtl8821aefw_wowlan.bin
[   10.234742] AVX2 version of gcm_enc/dec engaged.
[   10.234743] AES CTR mode by8 optimization enabled
[   10.340107] ieee80211 phy0: Selected rate control algorithm 'rtl_rc'
[   10.340240] rtlwifi: rtlwifi: wireless switch is on
[   10.406307] rtl8821ae 0000:02:00.0 wlp2s0: renamed from wlan0
[   10.646183] snd_hda_intel 0000:01:00.1: Handle vga_switcheroo audio client
[   10.646185] snd_hda_intel 0000:01:00.1: Force to non-snoop mode
[   10.703251] input: HDA ATI HDMI HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input6
[   10.703286] input: HDA ATI HDMI HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input7
[   10.703312] input: HDA ATI HDMI HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input8
[   10.703340] input: HDA ATI HDMI HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input9
[   10.703366] input: HDA ATI HDMI HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input10
[   10.703393] input: HDA ATI HDMI HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input11
[   10.774680] PKCS#7 signature not signed with a trusted key
[   10.785150] [drm] amdgpu kernel modesetting enabled.
[   10.785151] [drm] amdgpu version: 19.10.8.418
[   10.785151] [drm] OS DRM version: 4.13.0
[   10.785189] CRAT table not found
[   10.785190] Virtual CRAT table created for CPU
[   10.785190] Parsing CRAT table with 1 nodes
[   10.785191] Creating topology SYSFS entries
[   10.785198] Topology: Add CPU node
[   10.785198] Finished initializing topology
[   11.095041] checking generic (c0000000 7f0000) vs hw (c0000000 10000000)
[   11.095042] fb: switching to amdgpudrmfb from EFI VGA
[   11.095186] Console: switching to colour dummy device 80x25
[   11.095370] [drm] initializing kernel modesetting (POLARIS10 0x1002:0x6FDF 0x1002:0x0B31 0xEF).
[   11.095377] [drm] register mmio base: 0xDFE00000
[   11.095378] [drm] register mmio size: 262144
[   11.095382] [drm] add ip block number 0 <vi_common>
[   11.095383] [drm] add ip block number 1 <gmc_v8_0>
[   11.095383] [drm] add ip block number 2 <tonga_ih>
[   11.095384] [drm] add ip block number 3 <gfx_v8_0>
[   11.095384] [drm] add ip block number 4 <sdma_v3_0>
[   11.095385] [drm] add ip block number 5 <powerplay>
[   11.095385] [drm] add ip block number 6 <dm>
[   11.095386] [drm] add ip block number 7 <uvd_v6_0>
[   11.095386] [drm] add ip block number 8 <vce_v3_0>
[   11.095393] [drm] UVD is enabled in VM mode
[   11.095394] [drm] UVD ENC is enabled in VM mode
[   11.095395] [drm] VCE enabled in VM mode
[   11.095569] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[   11.095597] ATOM BIOS: 113-D80-X65
[   11.095617] [drm] vm size is 64 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[   12.423793] snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALC887-VD: line_outs=1 (0x14/0x0/0x0/0x0/0x0) type:line
[   12.423795] snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=1 (0x15/0x0/0x0/0x0/0x0)
[   12.423795] snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
[   12.423796] snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
[   12.423797] snd_hda_codec_realtek hdaudioC0D0:    inputs:
[   12.423797] snd_hda_codec_realtek hdaudioC0D0:      Front Mic=0x19
[   12.423798] snd_hda_codec_realtek hdaudioC0D0:      Rear Mic=0x18
[   12.423799] snd_hda_codec_realtek hdaudioC0D0:      Line=0x1a
[   12.435334] input: HDA Intel PCH Front Mic as /devices/pci0000:00/0000:00:1f.3/sound/card0/input12
[   12.435364] input: HDA Intel PCH Rear Mic as /devices/pci0000:00/0000:00:1f.3/sound/card0/input13
[   12.435389] input: HDA Intel PCH Line as /devices/pci0000:00/0000:00:1f.3/sound/card0/input14
[   12.435413] input: HDA Intel PCH Line Out as /devices/pci0000:00/0000:00:1f.3/sound/card0/input15
[   12.435439] input: HDA Intel PCH Front Headphone as /devices/pci0000:00/0000:00:1f.3/sound/card0/input16
[   12.517938] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[   12.517943] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   12.517965] [drm] Detected VRAM RAM=8192M, BAR=256M
[   12.517966] [drm] RAM width 256bits GDDR5
[   12.518013] [TTM] Zone  kernel: Available graphics memory: 7626506 kiB
[   12.518014] [TTM] Initializing pool allocator
[   12.518028] [TTM] Initializing DMA pool allocator
[   12.518050] [drm] amdgpu: 8192M of VRAM memory ready
[   12.518050] [drm] amdgpu: 8192M of GTT memory ready.
[   12.518064] [drm] GART: num cpu pages 65536, num gpu pages 65536
[   12.518658] [drm] PCIE GART of 256M enabled (table at 0x000000F4007E9000).
[   12.932489] [drm] Chained IB support enabled!
[   13.075115] intel_rapl: Found RAPL domain package
[   13.075116] intel_rapl: Found RAPL domain core
[   13.075117] intel_rapl: Found RAPL domain dram
[   13.426654] [drm] Found UVD firmware Version: 1.130 Family ID: 16
[   13.448472] [drm] Found VCE firmware Version: 53.26 Binary ID: 3
[   13.522116] [drm] DM_PPLIB: values for Engine clock
[   13.522117] [drm] DM_PPLIB:	 300000
[   13.522118] [drm] DM_PPLIB:	 588000
[   13.522118] [drm] DM_PPLIB:	 952000
[   13.522118] [drm] DM_PPLIB:	 1041000
[   13.522119] [drm] DM_PPLIB:	 1106000
[   13.522119] [drm] DM_PPLIB:	 1168000
[   13.522119] [drm] DM_PPLIB:	 1209000
[   13.522119] [drm] DM_PPLIB:	 1284000
[   13.522120] [drm] DM_PPLIB: Validation clocks:
[   13.522120] [drm] DM_PPLIB:    engine_max_clock: 128400
[   13.522120] [drm] DM_PPLIB:    memory_max_clock: 175000
[   13.522121] [drm] DM_PPLIB:    level           : 8
[   13.522121] [drm] DM_PPLIB: values for Memory clock
[   13.522122] [drm] DM_PPLIB:	 300000
[   13.522122] [drm] DM_PPLIB:	 1000000
[   13.522122] [drm] DM_PPLIB:	 1750000
[   13.522123] [drm] DM_PPLIB: Validation clocks:
[   13.522123] [drm] DM_PPLIB:    engine_max_clock: 128400
[   13.522123] [drm] DM_PPLIB:    memory_max_clock: 175000
[   13.522123] [drm] DM_PPLIB:    level           : 8
[   13.544132] [drm] Display Core initialized with v3.2.14!
[   13.557632] [drm] SADs count is: -2, don't need to read it
[   13.557637] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   13.557637] [drm] Driver supports precise vblank timestamp query.
[   13.586653] [drm] UVD and UVD ENC initialized successfully.
[   13.686638] [drm] VCE initialized successfully.
[   13.687562] kfd kfd: Allocated 3969056 bytes on gart
[   13.687577] Virtual CRAT table created for GPU
[   13.687577] Parsing CRAT table with 1 nodes
[   13.687581] Creating topology SYSFS entries
[   13.687635] Topology: Add dGPU node [0x6fdf:0x1002]
[   13.688136] kfd kfd: added device 1002:6fdf
[   13.689472] [drm] fb mappable at 0xC0D19000
[   13.689473] [drm] vram apper at 0xC0000000
[   13.689474] [drm] size 8294400
[   13.689474] [drm] fb depth is 24
[   13.689474] [drm]    pitch is 7680
[   13.689511] fbcon: amdgpudrmfb (fb0) is primary device
[   13.755503] Console: switching to colour frame buffer device 240x67
[   13.771915] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[   13.786282] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:01:00.0 on minor 0
[   20.525989] audit: type=1400 audit(1553435478.142:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=790 comm="apparmor_parser"
[   20.525991] audit: type=1400 audit(1553435478.142:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=790 comm="apparmor_parser"
[   20.525992] audit: type=1400 audit(1553435478.142:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=790 comm="apparmor_parser"
[   20.551802] audit: type=1400 audit(1553435478.168:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=787 comm="apparmor_parser"
[   20.551804] audit: type=1400 audit(1553435478.168:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=787 comm="apparmor_parser"
[   20.551805] audit: type=1400 audit(1553435478.168:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=787 comm="apparmor_parser"
[   20.551806] audit: type=1400 audit(1553435478.168:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=787 comm="apparmor_parser"
[   20.598074] audit: type=1400 audit(1553435478.214:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=793 comm="apparmor_parser"
[   20.698382] audit: type=1400 audit(1553435478.314:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince" pid=788 comm="apparmor_parser"
[   20.698384] audit: type=1400 audit(1553435478.314:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//sanitized_helper" pid=788 comm="apparmor_parser"
[   21.443847] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[   21.443848] Bluetooth: BNEP filters: protocol multicast
[   21.443850] Bluetooth: BNEP socket layer initialized
[   24.357463] IPv6: ADDRCONF(NETDEV_UP): enp0s31f6: link is not ready
[   24.568159] IPv6: ADDRCONF(NETDEV_UP): enp0s31f6: link is not ready
[   24.702586] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[   24.985855] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[   25.035224] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[   28.186135] wlp2s0: authenticate with 12:da:43:9c:8a:00
[   28.186452] wlp2s0: send auth to 12:da:43:9c:8a:00 (try 1/3)
[   28.189778] wlp2s0: authenticated
[   28.192053] wlp2s0: associate with 12:da:43:9c:8a:00 (try 1/3)
[   28.195717] wlp2s0: RX AssocResp from 12:da:43:9c:8a:00 (capab=0x1011 status=0 aid=2)
[   28.195905] wlp2s0: associated
[   28.195941] IPv6: ADDRCONF(NETDEV_CHANGE): wlp2s0: link becomes ready
[   28.385094] wlp2s0: Limiting TX power to 20 (20 - 0) dBm as advertised by 12:da:43:9c:8a:00
[   32.759746] kauditd_printk_skb: 23 callbacks suppressed
[   32.759748] audit: type=1400 audit(1553435490.376:35): apparmor="STATUS" operation="profile_load" profile="unconfined" name="docker-default" pid=1947 comm="apparmor_parser"
[   33.267705] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[   33.271372] Bridge firewalling registered
[   33.309286] nf_conntrack version 0.5.0 (65536 buckets, 262144 max)
[   33.506051] Initializing XFRM netlink socket
[   33.516563] Netfilter messages via NETLINK v0.30.
[   33.520585] ctnetlink v0.93: registering with nfnetlink.
[   33.595655] IPv6: ADDRCONF(NETDEV_UP): docker0: link is not ready
[   42.397576] Bluetooth: RFCOMM TTY layer initialized
[   42.397586] Bluetooth: RFCOMM socket layer initialized
[   42.397594] Bluetooth: RFCOMM ver 1.11
[   44.646328] rfkill: input handler disabled
```
thanks

---

### 评论 #11 — tu6ge (2019-03-24T13:59:02Z)

yes,I is rebuilded it

---

### 评论 #12 — kentrussell (2019-06-07T12:16:27Z)

Can you try the 2.5 release and see if you're still seeing the same issue?

---
