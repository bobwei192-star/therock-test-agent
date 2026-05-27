# ROCk module is NOT loaded, possibly no GPU devices

> **Issue #1626**
> **状态**: closed
> **创建时间**: 2021-11-24T02:22:13Z
> **更新时间**: 2024-01-20T02:47:35Z
> **关闭时间**: 2024-01-20T02:47:35Z
> **作者**: xiaomin0416
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1626

## 描述

Hi, I am appreciate to use this excellent products.I tried to install rocm packages in my machine,but I met a proplem.
There is my configuration:

1. Linux Distribution Information

> uname -m && cat /etc/*release

x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.6 LTS"
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic

2. Kernel Information

> uname -srmv

Linux 5.4.0-90-generic #101~18.04.1-Ubuntu SMP Fri Oct 22 09:25:04 UTC 2021 x86_64

3. My GPU
AMD Radeon(TM) Vage 10 Graphics with PCI\VEN_1002&DEV_15DD&SUBSYS_83DA103C&REV_D0

> sudo lshw -class display

*-display                 
       description: VGA compatible controller
       product: SVGA II Adapter
       vendor: VMware
       physical id: f
       bus info: pci@0000:00:0f.0
       version: 00
       width: 32 bits
       clock: 33MHz
       capabilities: vga_controller bus_master cap_list rom
       configuration: driver=vmwgfx latency=64
       resources: irq:16 ioport:1070(size=16) memory:e8000000-efffffff memory:fe000000-fe7fffff memory:c0000-dffff

I followed the steps of the installation guide and didn't have any problems until`/opt/rocm-4.5.0/bin/rocminfo`:
> /opt/rocm-4.5.0/bin/rocminfo

ROCk module is NOT loaded, possibly no GPU devices

> /opt/rocm-4.5.0/opencl/bin/clinfo

Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.2 AMD-APP (3361.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0

I looked [issue#1404](https://github.com/RadeonOpenCompute/ROCm/issues/1404), I tried to run:
> dmesg | grep kfd

I got nothing.

> dmesg | grep amd

[    0.000000] Linux version 5.4.0-90-generic (buildd@lcy01-amd64-026) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #101~18.04.1-Ubuntu SMP Fri Oct 22 09:25:04 UTC 2021 (Ubuntu 5.4.0-90.101~18.04.1-generic 5.4.148)

I tried re-install again, but I met the same wrong.Can you help me? Thank you.

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-11-26T09:48:16Z)

Thanks @xiaomin0416 for reaching out.
Can you please help with dmesg output.
As an additional note, we did not validate ROCm on Ubuntu 18.04.6 anytime. I request to validate on supported oses as mentioned in our docs.
Thank you.

---

### 评论 #2 — xiaomin0416 (2021-11-26T11:06:07Z)

Sorry, I ignored the last number of my os is not correspond with you supported oses. 
Do you mean the output of`dmesg | grep kfd`、`dmesg | grep amd`:
![dmesg](https://user-images.githubusercontent.com/58285558/143570253-b217eab8-fae0-4552-951d-5bb4a19f1927.jpg)
Or the output of`dmesg`. If I have a misperception about your reply, please also correct me.Thanks.:
> $ dmesg
[    0.000000] Linux version 5.4.0-90-generic (buildd@lcy01-amd64-026) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #101~18.04.1-Ubuntu SMP Fri Oct 22 09:25:04 UTC 2021 (Ubuntu 5.4.0-90.101~18.04.1-generic 5.4.148)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-90-generic root=UUID=0f594964-0280-4f0e-88ad-93bf18d70e48 ro quiet splash
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Hygon HygonGenuine
[    0.000000]   Centaur CentaurHauls
[    0.000000]   zhaoxin   Shanghai  
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'compacted' format.
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009e7ff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009e800-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000000dc000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000bfecffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000bfed0000-0x00000000bfefefff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000bfeff000-0x00000000bfefffff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000bff00000-0x00000000bfffffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000f0000000-0x00000000f7ffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec0ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fffe0000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000013fffffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] SMBIOS 2.7 present.
[    0.000000] DMI: VMware, Inc. VMware Virtual Platform/440BX Desktop Reference Platform, BIOS 6.00 02/27/2020
[    0.000000] vmware: hypercall mode: 0x00
[    0.000000] Hypervisor detected: VMware
[    0.000000] vmware: TSC freq read from hypervisor : 2195.872 MHz
[    0.000000] vmware: Host bus clock speed read from hypervisor : 66000000 Hz
[    0.000001] vmware: using sched offset of 8762927953 ns
[    0.000002] tsc: Detected 2195.872 MHz processor
[    0.003961] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.003963] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.003968] last_pfn = 0x140000 max_arch_pfn = 0x400000000
[    0.003988] MTRR default type: uncachable
[    0.003989] MTRR fixed ranges enabled:
[    0.003991]   00000-9FFFF write-back
[    0.003992]   A0000-BFFFF uncachable
[    0.003992]   C0000-CFFFF write-protect
[    0.003993]   D0000-EFFFF uncachable
[    0.003994]   F0000-FFFFF write-protect
[    0.003995] MTRR variable ranges enabled:
[    0.003996]   0 base 00000000000 mask 7E000000000 write-back
[    0.003997]   1 base 000C0000000 mask 7FFC0000000 uncachable
[    0.003998]   2 disabled
[    0.003998]   3 disabled
[    0.003999]   4 disabled
[    0.003999]   5 disabled
[    0.004000]   6 disabled
[    0.004000]   7 disabled
[    0.004034] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.004049] total RAM covered: 130048M
[    0.004692] Found optimal setting for mtrr clean up
[    0.004694]  gran_size: 64K 	chunk_size: 64K 	num_reg: 7  	lose cover RAM: 0G
[    0.004750] e820: update [mem 0xc0000000-0xffffffff] usable ==> reserved
[    0.004757] last_pfn = 0xc0000 max_arch_pfn = 0x400000000
[    0.008055] found SMP MP-table at [mem 0x000f6a70-0x000f6a7f]
[    0.008286] check: Scanning 1 areas for low memory corruption
[    0.008355] Using GB pages for direct mapping
[    0.008957] RAMDISK: [mem 0x2ffdb000-0x33fe4fff]
[    0.008970] ACPI: Early table checksum verification disabled
[    0.008979] ACPI: RSDP 0x00000000000F6A00 000024 (v02 PTLTD )
[    0.008985] ACPI: XSDT 0x00000000BFEDC633 00005C (v01 INTEL  440BX    06040000 VMW  01324272)
[    0.008995] ACPI: FACP 0x00000000BFEFEE73 0000F4 (v04 INTEL  440BX    06040000 PTL  000F4240)
[    0.009005] ACPI: DSDT 0x00000000BFEDD9E8 02148B (v01 PTLTD  Custom   06040000 MSFT 03000001)
[    0.009015] ACPI: FACS 0x00000000BFEFFFC0 000040
[    0.009019] ACPI: FACS 0x00000000BFEFFFC0 000040
[    0.009023] ACPI: BOOT 0x00000000BFEDD9C0 000028 (v01 PTLTD  $SBFTBL$ 06040000  LTP 00000001)
[    0.009028] ACPI: APIC 0x00000000BFEDD27E 000742 (v01 PTLTD  ? APIC   06040000  LTP 00000000)
[    0.009032] ACPI: MCFG 0x00000000BFEDD242 00003C (v01 PTLTD  $PCITBL$ 06040000  LTP 00000001)
[    0.009037] ACPI: SRAT 0x00000000BFEDC72F 0008D0 (v02 VMWARE MEMPLUG  06040000 VMW  00000001)
[    0.009041] ACPI: HPET 0x00000000BFEDC6F7 000038 (v01 VMWARE VMW HPET 06040000 VMW  00000001)
[    0.009047] ACPI: WAET 0x00000000BFEDC6CF 000028 (v01 VMWARE VMW WAET 06040000 VMW  00000001)
[    0.009053] ACPI: Reserving FACP table memory at [mem 0xbfefee73-0xbfefef66]
[    0.009055] ACPI: Reserving DSDT table memory at [mem 0xbfedd9e8-0xbfefee72]
[    0.009058] ACPI: Reserving FACS table memory at [mem 0xbfefffc0-0xbfefffff]
[    0.009060] ACPI: Reserving FACS table memory at [mem 0xbfefffc0-0xbfefffff]
[    0.009062] ACPI: Reserving BOOT table memory at [mem 0xbfedd9c0-0xbfedd9e7]
[    0.009064] ACPI: Reserving APIC table memory at [mem 0xbfedd27e-0xbfedd9bf]
[    0.009066] ACPI: Reserving MCFG table memory at [mem 0xbfedd242-0xbfedd27d]
[    0.009068] ACPI: Reserving SRAT table memory at [mem 0xbfedc72f-0xbfedcffe]
[    0.009070] ACPI: Reserving HPET table memory at [mem 0xbfedc6f7-0xbfedc72e]
[    0.009071] ACPI: Reserving WAET table memory at [mem 0xbfedc6cf-0xbfedc6f6]
[    0.009115] ACPI: Local APIC address 0xfee00000
[    0.009122] system APIC only can use physical flat
[    0.009124] Setting APIC routing to physical flat.
[    0.009208] SRAT: PXM 0 -> APIC 0x00 -> Node 0
[    0.009210] SRAT: PXM 0 -> APIC 0x02 -> Node 0
[    0.009211] SRAT: PXM 0 -> APIC 0x04 -> Node 0
[    0.009212] SRAT: PXM 0 -> APIC 0x06 -> Node 0
[    0.009213] SRAT: PXM 0 -> APIC 0x08 -> Node 0
[    0.009214] SRAT: PXM 0 -> APIC 0x0a -> Node 0
[    0.009215] SRAT: PXM 0 -> APIC 0x0c -> Node 0
[    0.009216] SRAT: PXM 0 -> APIC 0x0e -> Node 0
[    0.009217] SRAT: PXM 0 -> APIC 0x10 -> Node 0
[    0.009218] SRAT: PXM 0 -> APIC 0x12 -> Node 0
[    0.009219] SRAT: PXM 0 -> APIC 0x14 -> Node 0
[    0.009220] SRAT: PXM 0 -> APIC 0x16 -> Node 0
[    0.009221] SRAT: PXM 0 -> APIC 0x18 -> Node 0
[    0.009222] SRAT: PXM 0 -> APIC 0x1a -> Node 0
[    0.009223] SRAT: PXM 0 -> APIC 0x1c -> Node 0
[    0.009224] SRAT: PXM 0 -> APIC 0x1e -> Node 0
[    0.009225] SRAT: PXM 0 -> APIC 0x20 -> Node 0
[    0.009226] SRAT: PXM 0 -> APIC 0x22 -> Node 0
[    0.009227] SRAT: PXM 0 -> APIC 0x24 -> Node 0
[    0.009228] SRAT: PXM 0 -> APIC 0x26 -> Node 0
[    0.009229] SRAT: PXM 0 -> APIC 0x28 -> Node 0
[    0.009230] SRAT: PXM 0 -> APIC 0x2a -> Node 0
[    0.009231] SRAT: PXM 0 -> APIC 0x2c -> Node 0
[    0.009232] SRAT: PXM 0 -> APIC 0x2e -> Node 0
[    0.009233] SRAT: PXM 0 -> APIC 0x30 -> Node 0
[    0.009253] SRAT: PXM 0 -> APIC 0x32 -> Node 0
[    0.009255] SRAT: PXM 0 -> APIC 0x34 -> Node 0
[    0.009256] SRAT: PXM 0 -> APIC 0x36 -> Node 0
[    0.009256] SRAT: PXM 0 -> APIC 0x38 -> Node 0
[    0.009258] SRAT: PXM 0 -> APIC 0x3a -> Node 0
[    0.009259] SRAT: PXM 0 -> APIC 0x3c -> Node 0
[    0.009260] SRAT: PXM 0 -> APIC 0x3e -> Node 0
[    0.009261] SRAT: PXM 0 -> APIC 0x40 -> Node 0
[    0.009262] SRAT: PXM 0 -> APIC 0x42 -> Node 0
[    0.009263] SRAT: PXM 0 -> APIC 0x44 -> Node 0
[    0.009264] SRAT: PXM 0 -> APIC 0x46 -> Node 0
[    0.009265] SRAT: PXM 0 -> APIC 0x48 -> Node 0
[    0.009266] SRAT: PXM 0 -> APIC 0x4a -> Node 0
[    0.009267] SRAT: PXM 0 -> APIC 0x4c -> Node 0
[    0.009268] SRAT: PXM 0 -> APIC 0x4e -> Node 0
[    0.009269] SRAT: PXM 0 -> APIC 0x50 -> Node 0
[    0.009270] SRAT: PXM 0 -> APIC 0x52 -> Node 0
[    0.009271] SRAT: PXM 0 -> APIC 0x54 -> Node 0
[    0.009272] SRAT: PXM 0 -> APIC 0x56 -> Node 0
[    0.009273] SRAT: PXM 0 -> APIC 0x58 -> Node 0
[    0.009274] SRAT: PXM 0 -> APIC 0x5a -> Node 0
[    0.009275] SRAT: PXM 0 -> APIC 0x5c -> Node 0
[    0.009276] SRAT: PXM 0 -> APIC 0x5e -> Node 0
[    0.009278] SRAT: PXM 0 -> APIC 0x60 -> Node 0
[    0.009279] SRAT: PXM 0 -> APIC 0x62 -> Node 0
[    0.009280] SRAT: PXM 0 -> APIC 0x64 -> Node 0
[    0.009281] SRAT: PXM 0 -> APIC 0x66 -> Node 0
[    0.009282] SRAT: PXM 0 -> APIC 0x68 -> Node 0
[    0.009283] SRAT: PXM 0 -> APIC 0x6a -> Node 0
[    0.009284] SRAT: PXM 0 -> APIC 0x6c -> Node 0
[    0.009285] SRAT: PXM 0 -> APIC 0x6e -> Node 0
[    0.009286] SRAT: PXM 0 -> APIC 0x70 -> Node 0
[    0.009287] SRAT: PXM 0 -> APIC 0x72 -> Node 0
[    0.009288] SRAT: PXM 0 -> APIC 0x74 -> Node 0
[    0.009289] SRAT: PXM 0 -> APIC 0x76 -> Node 0
[    0.009290] SRAT: PXM 0 -> APIC 0x78 -> Node 0
[    0.009291] SRAT: PXM 0 -> APIC 0x7a -> Node 0
[    0.009292] SRAT: PXM 0 -> APIC 0x7c -> Node 0
[    0.009293] SRAT: PXM 0 -> APIC 0x7e -> Node 0
[    0.009295] SRAT: PXM 0 -> APIC 0x80 -> Node 0
[    0.009296] SRAT: PXM 0 -> APIC 0x82 -> Node 0
[    0.009297] SRAT: PXM 0 -> APIC 0x84 -> Node 0
[    0.009298] SRAT: PXM 0 -> APIC 0x86 -> Node 0
[    0.009299] SRAT: PXM 0 -> APIC 0x88 -> Node 0
[    0.009300] SRAT: PXM 0 -> APIC 0x8a -> Node 0
[    0.009301] SRAT: PXM 0 -> APIC 0x8c -> Node 0
[    0.009302] SRAT: PXM 0 -> APIC 0x8e -> Node 0
[    0.009303] SRAT: PXM 0 -> APIC 0x90 -> Node 0
[    0.009304] SRAT: PXM 0 -> APIC 0x92 -> Node 0
[    0.009305] SRAT: PXM 0 -> APIC 0x94 -> Node 0
[    0.009306] SRAT: PXM 0 -> APIC 0x96 -> Node 0
[    0.009307] SRAT: PXM 0 -> APIC 0x98 -> Node 0
[    0.009308] SRAT: PXM 0 -> APIC 0x9a -> Node 0
[    0.009309] SRAT: PXM 0 -> APIC 0x9c -> Node 0
[    0.009310] SRAT: PXM 0 -> APIC 0x9e -> Node 0
[    0.009312] SRAT: PXM 0 -> APIC 0xa0 -> Node 0
[    0.009313] SRAT: PXM 0 -> APIC 0xa2 -> Node 0
[    0.009313] SRAT: PXM 0 -> APIC 0xa4 -> Node 0
[    0.009314] SRAT: PXM 0 -> APIC 0xa6 -> Node 0
[    0.009315] SRAT: PXM 0 -> APIC 0xa8 -> Node 0
[    0.009316] SRAT: PXM 0 -> APIC 0xaa -> Node 0
[    0.009318] SRAT: PXM 0 -> APIC 0xac -> Node 0
[    0.009319] SRAT: PXM 0 -> APIC 0xae -> Node 0
[    0.009320] SRAT: PXM 0 -> APIC 0xb0 -> Node 0
[    0.009321] SRAT: PXM 0 -> APIC 0xb2 -> Node 0
[    0.009322] SRAT: PXM 0 -> APIC 0xb4 -> Node 0
[    0.009323] SRAT: PXM 0 -> APIC 0xb6 -> Node 0
[    0.009324] SRAT: PXM 0 -> APIC 0xb8 -> Node 0
[    0.009325] SRAT: PXM 0 -> APIC 0xba -> Node 0
[    0.009326] SRAT: PXM 0 -> APIC 0xbc -> Node 0
[    0.009327] SRAT: PXM 0 -> APIC 0xbe -> Node 0
[    0.009328] SRAT: PXM 0 -> APIC 0xc0 -> Node 0
[    0.009329] SRAT: PXM 0 -> APIC 0xc2 -> Node 0
[    0.009330] SRAT: PXM 0 -> APIC 0xc4 -> Node 0
[    0.009331] SRAT: PXM 0 -> APIC 0xc6 -> Node 0
[    0.009332] SRAT: PXM 0 -> APIC 0xc8 -> Node 0
[    0.009334] SRAT: PXM 0 -> APIC 0xca -> Node 0
[    0.009335] SRAT: PXM 0 -> APIC 0xcc -> Node 0
[    0.009336] SRAT: PXM 0 -> APIC 0xce -> Node 0
[    0.009337] SRAT: PXM 0 -> APIC 0xd0 -> Node 0
[    0.009338] SRAT: PXM 0 -> APIC 0xd2 -> Node 0
[    0.009339] SRAT: PXM 0 -> APIC 0xd4 -> Node 0
[    0.009340] SRAT: PXM 0 -> APIC 0xd6 -> Node 0
[    0.009341] SRAT: PXM 0 -> APIC 0xd8 -> Node 0
[    0.009342] SRAT: PXM 0 -> APIC 0xda -> Node 0
[    0.009343] SRAT: PXM 0 -> APIC 0xdc -> Node 0
[    0.009344] SRAT: PXM 0 -> APIC 0xde -> Node 0
[    0.009345] SRAT: PXM 0 -> APIC 0xe0 -> Node 0
[    0.009346] SRAT: PXM 0 -> APIC 0xe2 -> Node 0
[    0.009347] SRAT: PXM 0 -> APIC 0xe4 -> Node 0
[    0.009348] SRAT: PXM 0 -> APIC 0xe6 -> Node 0
[    0.009349] SRAT: PXM 0 -> APIC 0xe8 -> Node 0
[    0.009350] SRAT: PXM 0 -> APIC 0xea -> Node 0
[    0.009351] SRAT: PXM 0 -> APIC 0xec -> Node 0
[    0.009352] SRAT: PXM 0 -> APIC 0xee -> Node 0
[    0.009353] SRAT: PXM 0 -> APIC 0xf0 -> Node 0
[    0.009354] SRAT: PXM 0 -> APIC 0xf2 -> Node 0
[    0.009355] SRAT: PXM 0 -> APIC 0xf4 -> Node 0
[    0.009356] SRAT: PXM 0 -> APIC 0xf6 -> Node 0
[    0.009357] SRAT: PXM 0 -> APIC 0xf8 -> Node 0
[    0.009358] SRAT: PXM 0 -> APIC 0xfa -> Node 0
[    0.009360] SRAT: PXM 0 -> APIC 0xfc -> Node 0
[    0.009361] SRAT: PXM 0 -> APIC 0xfe -> Node 0
[    0.009367] ACPI: SRAT: Node 0 PXM 0 [mem 0x00000000-0x0009ffff]
[    0.009369] ACPI: SRAT: Node 0 PXM 0 [mem 0x00100000-0xbfffffff]
[    0.009370] ACPI: SRAT: Node 0 PXM 0 [mem 0x100000000-0x13fffffff]
[    0.009372] ACPI: SRAT: Node 0 PXM 0 [mem 0x140000000-0x103fffffff] hotplug
[    0.009376] NUMA: Node 0 [mem 0x00000000-0x0009ffff] + [mem 0x00100000-0xbfffffff] -> [mem 0x00000000-0xbfffffff]
[    0.009378] NUMA: Node 0 [mem 0x00000000-0xbfffffff] + [mem 0x100000000-0x13fffffff] -> [mem 0x00000000-0x13fffffff]
[    0.009395] NODE_DATA(0) allocated [mem 0x13ffd3000-0x13fffdfff]
[    0.010828] Zone ranges:
[    0.010830]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.010832]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.010833]   Normal   [mem 0x0000000100000000-0x000000013fffffff]
[    0.010834]   Device   empty
[    0.010835] Movable zone start for each node
[    0.010838] Early memory node ranges
[    0.010839]   node   0: [mem 0x0000000000001000-0x000000000009dfff]
[    0.010840]   node   0: [mem 0x0000000000100000-0x00000000bfecffff]
[    0.010841]   node   0: [mem 0x00000000bff00000-0x00000000bfffffff]
[    0.010841]   node   0: [mem 0x0000000100000000-0x000000013fffffff]
[    0.010974] Zeroed struct page in unavailable ranges: 147 pages
[    0.010976] Initmem setup node 0 [mem 0x0000000000001000-0x000000013fffffff]
[    0.010978] On node 0 totalpages: 1048429
[    0.010979]   DMA zone: 64 pages used for memmap
[    0.010980]   DMA zone: 21 pages reserved
[    0.010981]   DMA zone: 3997 pages, LIFO batch:0
[    0.012248]   DMA32 zone: 12224 pages used for memmap
[    0.012252]   DMA32 zone: 782288 pages, LIFO batch:63
[    0.261962]   Normal zone: 4096 pages used for memmap
[    0.261964]   Normal zone: 262144 pages, LIFO batch:63
[    0.346078] ACPI: PM-Timer IO Port: 0x1008
[    0.346081] ACPI: Local APIC address 0xfee00000
[    0.346086] system APIC only can use physical flat
[    0.346098] ACPI: LAPIC_NMI (acpi_id[0x00] high edge lint[0x1])
[    0.346098] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
[    0.346099] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
[    0.346099] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
[    0.346100] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
[    0.346100] ACPI: LAPIC_NMI (acpi_id[0x05] high edge lint[0x1])
[    0.346101] ACPI: LAPIC_NMI (acpi_id[0x06] high edge lint[0x1])
[    0.346101] ACPI: LAPIC_NMI (acpi_id[0x07] high edge lint[0x1])
[    0.346101] ACPI: LAPIC_NMI (acpi_id[0x08] high edge lint[0x1])
[    0.346102] ACPI: LAPIC_NMI (acpi_id[0x09] high edge lint[0x1])
[    0.346102] ACPI: LAPIC_NMI (acpi_id[0x0a] high edge lint[0x1])
[    0.346103] ACPI: LAPIC_NMI (acpi_id[0x0b] high edge lint[0x1])
[    0.346103] ACPI: LAPIC_NMI (acpi_id[0x0c] high edge lint[0x1])
[    0.346103] ACPI: LAPIC_NMI (acpi_id[0x0d] high edge lint[0x1])
[    0.346104] ACPI: LAPIC_NMI (acpi_id[0x0e] high edge lint[0x1])
[    0.346104] ACPI: LAPIC_NMI (acpi_id[0x0f] high edge lint[0x1])
[    0.346105] ACPI: LAPIC_NMI (acpi_id[0x10] high edge lint[0x1])
[    0.346105] ACPI: LAPIC_NMI (acpi_id[0x11] high edge lint[0x1])
[    0.346106] ACPI: LAPIC_NMI (acpi_id[0x12] high edge lint[0x1])
[    0.346106] ACPI: LAPIC_NMI (acpi_id[0x13] high edge lint[0x1])
[    0.346106] ACPI: LAPIC_NMI (acpi_id[0x14] high edge lint[0x1])
[    0.346107] ACPI: LAPIC_NMI (acpi_id[0x15] high edge lint[0x1])
[    0.346107] ACPI: LAPIC_NMI (acpi_id[0x16] high edge lint[0x1])
[    0.346108] ACPI: LAPIC_NMI (acpi_id[0x17] high edge lint[0x1])
[    0.346108] ACPI: LAPIC_NMI (acpi_id[0x18] high edge lint[0x1])
[    0.346108] ACPI: LAPIC_NMI (acpi_id[0x19] high edge lint[0x1])
[    0.346109] ACPI: LAPIC_NMI (acpi_id[0x1a] high edge lint[0x1])
[    0.346109] ACPI: LAPIC_NMI (acpi_id[0x1b] high edge lint[0x1])
[    0.346110] ACPI: LAPIC_NMI (acpi_id[0x1c] high edge lint[0x1])
[    0.346110] ACPI: LAPIC_NMI (acpi_id[0x1d] high edge lint[0x1])
[    0.346110] ACPI: LAPIC_NMI (acpi_id[0x1e] high edge lint[0x1])
[    0.346111] ACPI: LAPIC_NMI (acpi_id[0x1f] high edge lint[0x1])
[    0.346111] ACPI: LAPIC_NMI (acpi_id[0x20] high edge lint[0x1])
[    0.346112] ACPI: LAPIC_NMI (acpi_id[0x21] high edge lint[0x1])
[    0.346112] ACPI: LAPIC_NMI (acpi_id[0x22] high edge lint[0x1])
[    0.346112] ACPI: LAPIC_NMI (acpi_id[0x23] high edge lint[0x1])
[    0.346113] ACPI: LAPIC_NMI (acpi_id[0x24] high edge lint[0x1])
[    0.346113] ACPI: LAPIC_NMI (acpi_id[0x25] high edge lint[0x1])
[    0.346114] ACPI: LAPIC_NMI (acpi_id[0x26] high edge lint[0x1])
[    0.346114] ACPI: LAPIC_NMI (acpi_id[0x27] high edge lint[0x1])
[    0.346114] ACPI: LAPIC_NMI (acpi_id[0x28] high edge lint[0x1])
[    0.346115] ACPI: LAPIC_NMI (acpi_id[0x29] high edge lint[0x1])
[    0.346115] ACPI: LAPIC_NMI (acpi_id[0x2a] high edge lint[0x1])
[    0.346116] ACPI: LAPIC_NMI (acpi_id[0x2b] high edge lint[0x1])
[    0.346116] ACPI: LAPIC_NMI (acpi_id[0x2c] high edge lint[0x1])
[    0.346117] ACPI: LAPIC_NMI (acpi_id[0x2d] high edge lint[0x1])
[    0.346117] ACPI: LAPIC_NMI (acpi_id[0x2e] high edge lint[0x1])
[    0.346117] ACPI: LAPIC_NMI (acpi_id[0x2f] high edge lint[0x1])
[    0.346118] ACPI: LAPIC_NMI (acpi_id[0x30] high edge lint[0x1])
[    0.346118] ACPI: LAPIC_NMI (acpi_id[0x31] high edge lint[0x1])
[    0.346119] ACPI: LAPIC_NMI (acpi_id[0x32] high edge lint[0x1])
[    0.346119] ACPI: LAPIC_NMI (acpi_id[0x33] high edge lint[0x1])
[    0.346119] ACPI: LAPIC_NMI (acpi_id[0x34] high edge lint[0x1])
[    0.346120] ACPI: LAPIC_NMI (acpi_id[0x35] high edge lint[0x1])
[    0.346120] ACPI: LAPIC_NMI (acpi_id[0x36] high edge lint[0x1])
[    0.346121] ACPI: LAPIC_NMI (acpi_id[0x37] high edge lint[0x1])
[    0.346121] ACPI: LAPIC_NMI (acpi_id[0x38] high edge lint[0x1])
[    0.346121] ACPI: LAPIC_NMI (acpi_id[0x39] high edge lint[0x1])
[    0.346122] ACPI: LAPIC_NMI (acpi_id[0x3a] high edge lint[0x1])
[    0.346122] ACPI: LAPIC_NMI (acpi_id[0x3b] high edge lint[0x1])
[    0.346123] ACPI: LAPIC_NMI (acpi_id[0x3c] high edge lint[0x1])
[    0.346123] ACPI: LAPIC_NMI (acpi_id[0x3d] high edge lint[0x1])
[    0.346123] ACPI: LAPIC_NMI (acpi_id[0x3e] high edge lint[0x1])
[    0.346124] ACPI: LAPIC_NMI (acpi_id[0x3f] high edge lint[0x1])
[    0.346124] ACPI: LAPIC_NMI (acpi_id[0x40] high edge lint[0x1])
[    0.346125] ACPI: LAPIC_NMI (acpi_id[0x41] high edge lint[0x1])
[    0.346125] ACPI: LAPIC_NMI (acpi_id[0x42] high edge lint[0x1])
[    0.346125] ACPI: LAPIC_NMI (acpi_id[0x43] high edge lint[0x1])
[    0.346126] ACPI: LAPIC_NMI (acpi_id[0x44] high edge lint[0x1])
[    0.346126] ACPI: LAPIC_NMI (acpi_id[0x45] high edge lint[0x1])
[    0.346127] ACPI: LAPIC_NMI (acpi_id[0x46] high edge lint[0x1])
[    0.346127] ACPI: LAPIC_NMI (acpi_id[0x47] high edge lint[0x1])
[    0.346127] ACPI: LAPIC_NMI (acpi_id[0x48] high edge lint[0x1])
[    0.346128] ACPI: LAPIC_NMI (acpi_id[0x49] high edge lint[0x1])
[    0.346128] ACPI: LAPIC_NMI (acpi_id[0x4a] high edge lint[0x1])
[    0.346129] ACPI: LAPIC_NMI (acpi_id[0x4b] high edge lint[0x1])
[    0.346129] ACPI: LAPIC_NMI (acpi_id[0x4c] high edge lint[0x1])
[    0.346129] ACPI: LAPIC_NMI (acpi_id[0x4d] high edge lint[0x1])
[    0.346130] ACPI: LAPIC_NMI (acpi_id[0x4e] high edge lint[0x1])
[    0.346130] ACPI: LAPIC_NMI (acpi_id[0x4f] high edge lint[0x1])
[    0.346131] ACPI: LAPIC_NMI (acpi_id[0x50] high edge lint[0x1])
[    0.346131] ACPI: LAPIC_NMI (acpi_id[0x51] high edge lint[0x1])
[    0.346131] ACPI: LAPIC_NMI (acpi_id[0x52] high edge lint[0x1])
[    0.346132] ACPI: LAPIC_NMI (acpi_id[0x53] high edge lint[0x1])
[    0.346132] ACPI: LAPIC_NMI (acpi_id[0x54] high edge lint[0x1])
[    0.346133] ACPI: LAPIC_NMI (acpi_id[0x55] high edge lint[0x1])
[    0.346133] ACPI: LAPIC_NMI (acpi_id[0x56] high edge lint[0x1])
[    0.346133] ACPI: LAPIC_NMI (acpi_id[0x57] high edge lint[0x1])
[    0.346134] ACPI: LAPIC_NMI (acpi_id[0x58] high edge lint[0x1])
[    0.346134] ACPI: LAPIC_NMI (acpi_id[0x59] high edge lint[0x1])
[    0.346135] ACPI: LAPIC_NMI (acpi_id[0x5a] high edge lint[0x1])
[    0.346135] ACPI: LAPIC_NMI (acpi_id[0x5b] high edge lint[0x1])
[    0.346135] ACPI: LAPIC_NMI (acpi_id[0x5c] high edge lint[0x1])
[    0.346136] ACPI: LAPIC_NMI (acpi_id[0x5d] high edge lint[0x1])
[    0.346136] ACPI: LAPIC_NMI (acpi_id[0x5e] high edge lint[0x1])
[    0.346137] ACPI: LAPIC_NMI (acpi_id[0x5f] high edge lint[0x1])
[    0.346137] ACPI: LAPIC_NMI (acpi_id[0x60] high edge lint[0x1])
[    0.346137] ACPI: LAPIC_NMI (acpi_id[0x61] high edge lint[0x1])
[    0.346138] ACPI: LAPIC_NMI (acpi_id[0x62] high edge lint[0x1])
[    0.346138] ACPI: LAPIC_NMI (acpi_id[0x63] high edge lint[0x1])
[    0.346139] ACPI: LAPIC_NMI (acpi_id[0x64] high edge lint[0x1])
[    0.346139] ACPI: LAPIC_NMI (acpi_id[0x65] high edge lint[0x1])
[    0.346139] ACPI: LAPIC_NMI (acpi_id[0x66] high edge lint[0x1])
[    0.346140] ACPI: LAPIC_NMI (acpi_id[0x67] high edge lint[0x1])
[    0.346140] ACPI: LAPIC_NMI (acpi_id[0x68] high edge lint[0x1])
[    0.346141] ACPI: LAPIC_NMI (acpi_id[0x69] high edge lint[0x1])
[    0.346141] ACPI: LAPIC_NMI (acpi_id[0x6a] high edge lint[0x1])
[    0.346141] ACPI: LAPIC_NMI (acpi_id[0x6b] high edge lint[0x1])
[    0.346142] ACPI: LAPIC_NMI (acpi_id[0x6c] high edge lint[0x1])
[    0.346142] ACPI: LAPIC_NMI (acpi_id[0x6d] high edge lint[0x1])
[    0.346143] ACPI: LAPIC_NMI (acpi_id[0x6e] high edge lint[0x1])
[    0.346143] ACPI: LAPIC_NMI (acpi_id[0x6f] high edge lint[0x1])
[    0.346144] ACPI: LAPIC_NMI (acpi_id[0x70] high edge lint[0x1])
[    0.346144] ACPI: LAPIC_NMI (acpi_id[0x71] high edge lint[0x1])
[    0.346144] ACPI: LAPIC_NMI (acpi_id[0x72] high edge lint[0x1])
[    0.346145] ACPI: LAPIC_NMI (acpi_id[0x73] high edge lint[0x1])
[    0.346145] ACPI: LAPIC_NMI (acpi_id[0x74] high edge lint[0x1])
[    0.346146] ACPI: LAPIC_NMI (acpi_id[0x75] high edge lint[0x1])
[    0.346146] ACPI: LAPIC_NMI (acpi_id[0x76] high edge lint[0x1])
[    0.346146] ACPI: LAPIC_NMI (acpi_id[0x77] high edge lint[0x1])
[    0.346147] ACPI: LAPIC_NMI (acpi_id[0x78] high edge lint[0x1])
[    0.346147] ACPI: LAPIC_NMI (acpi_id[0x79] high edge lint[0x1])
[    0.346148] ACPI: LAPIC_NMI (acpi_id[0x7a] high edge lint[0x1])
[    0.346148] ACPI: LAPIC_NMI (acpi_id[0x7b] high edge lint[0x1])
[    0.346148] ACPI: LAPIC_NMI (acpi_id[0x7c] high edge lint[0x1])
[    0.346149] ACPI: LAPIC_NMI (acpi_id[0x7d] high edge lint[0x1])
[    0.346149] ACPI: LAPIC_NMI (acpi_id[0x7e] high edge lint[0x1])
[    0.346150] ACPI: LAPIC_NMI (acpi_id[0x7f] high edge lint[0x1])
[    0.346191] IOAPIC[0]: apic_id 1, version 32, address 0xfec00000, GSI 0-23
[    0.346194] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 high edge)
[    0.346197] ACPI: IRQ0 used by override.
[    0.346198] ACPI: IRQ9 used by override.
[    0.346200] Using ACPI (MADT) for SMP configuration information
[    0.346202] ACPI: HPET id: 0x8086af01 base: 0xfed00000
[    0.346214] smpboot: Allowing 128 CPUs, 126 hotplug CPUs
[    0.346230] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.346231] PM: Registered nosave memory: [mem 0x0009e000-0x0009efff]
[    0.346231] PM: Registered nosave memory: [mem 0x0009f000-0x0009ffff]
[    0.346232] PM: Registered nosave memory: [mem 0x000a0000-0x000dbfff]
[    0.346232] PM: Registered nosave memory: [mem 0x000dc000-0x000fffff]
[    0.346233] PM: Registered nosave memory: [mem 0xbfed0000-0xbfefefff]
[    0.346234] PM: Registered nosave memory: [mem 0xbfeff000-0xbfefffff]
[    0.346277] PM: Registered nosave memory: [mem 0xc0000000-0xefffffff]
[    0.346278] PM: Registered nosave memory: [mem 0xf0000000-0xf7ffffff]
[    0.346279] PM: Registered nosave memory: [mem 0xf8000000-0xfebfffff]
[    0.346279] PM: Registered nosave memory: [mem 0xfec00000-0xfec0ffff]
[    0.346280] PM: Registered nosave memory: [mem 0xfec10000-0xfedfffff]
[    0.346280] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.346281] PM: Registered nosave memory: [mem 0xfee01000-0xfffdffff]
[    0.346281] PM: Registered nosave memory: [mem 0xfffe0000-0xffffffff]
[    0.346283] [mem 0xc0000000-0xefffffff] available for PCI devices
[    0.346284] Booting paravirtualized kernel on VMware hypervisor
[    0.346287] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.346294] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:128 nr_cpu_ids:128 nr_node_ids:1
[    0.513701] percpu: Embedded 55 pages/cpu s188416 r8192 d28672 u262144
[    0.513716] pcpu-alloc: s188416 r8192 d28672 u262144 alloc=1*2097152
[    0.513717] pcpu-alloc: [0] 000 001 002 003 004 005 006 007 
[    0.513719] pcpu-alloc: [0] 008 009 010 011 012 013 014 015 
[    0.513721] pcpu-alloc: [0] 016 017 018 019 020 021 022 023 
[    0.513722] pcpu-alloc: [0] 024 025 026 027 028 029 030 031 
[    0.513724] pcpu-alloc: [0] 032 033 034 035 036 037 038 039 
[    0.513726] pcpu-alloc: [0] 040 041 042 043 044 045 046 047 
[    0.513727] pcpu-alloc: [0] 048 049 050 051 052 053 054 055 
[    0.513729] pcpu-alloc: [0] 056 057 058 059 060 061 062 063 
[    0.513730] pcpu-alloc: [0] 064 065 066 067 068 069 070 071 
[    0.513732] pcpu-alloc: [0] 072 073 074 075 076 077 078 079 
[    0.513733] pcpu-alloc: [0] 080 081 082 083 084 085 086 087 
[    0.513735] pcpu-alloc: [0] 088 089 090 091 092 093 094 095 
[    0.513736] pcpu-alloc: [0] 096 097 098 099 100 101 102 103 
[    0.513738] pcpu-alloc: [0] 104 105 106 107 108 109 110 111 
[    0.513739] pcpu-alloc: [0] 112 113 114 115 116 117 118 119 
[    0.513741] pcpu-alloc: [0] 120 121 122 123 124 125 126 127 
[    0.513864] Built 1 zonelists, mobility grouping on.  Total pages: 1032024
[    0.513865] Policy zone: Normal
[    0.513867] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-90-generic root=UUID=0f594964-0280-4f0e-88ad-93bf18d70e48 ro quiet splash
[    0.513944] printk: log_buf_len individual max cpu contribution: 4096 bytes
[    0.513944] printk: log_buf_len total cpu_extra contributions: 520192 bytes
[    0.513945] printk: log_buf_len min size: 262144 bytes
[    0.520330] printk: log_buf_len: 1048576 bytes
[    0.520333] printk: early log buf free: 235068(89%)
[    0.540957] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.552438] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.553832] mem auto-init: stack:off, heap alloc:on, heap free:off
[    0.714643] Calgary: detecting Calgary via BIOS EBDA area
[    0.714646] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.729203] Memory: 3928160K/4193716K available (14339K kernel code, 2381K rwdata, 4988K rodata, 2716K init, 5004K bss, 265556K reserved, 0K cma-reserved)
[    0.729215] random: get_random_u64 called from __kmem_cache_create+0x41/0x550 with crng_init=0
[    0.730618] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=128, Nodes=1
[    0.730730] ftrace: allocating 44342 entries in 174 pages
[    0.752811] rcu: Hierarchical RCU implementation.
[    0.752814] rcu: 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=128.
[    0.752815] 	Tasks RCU enabled.
[    0.752816] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.752816] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=128
[    0.757365] NR_IRQS: 524544, nr_irqs: 1448, preallocated irqs: 16
[    0.758492] random: crng done (trusting CPU's manufacturer)
[    0.760740] Console: colour VGA+ 80x25
[    0.760749] printk: console [tty0] enabled
[    0.760944] ACPI: Core revision 20190816
[    0.761547] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484882848 ns
[    0.761653] APIC: Switch to symmetric I/O mode setup
[    0.761809] x2apic enabled
[    0.762032] Switched APIC routing to physical x2apic.
[    0.763598] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.763653] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x1fa6f7706c9, max_idle_ns: 440795287389 ns
[    0.763661] Calibrating delay loop (skipped) preset value.. 4391.74 BogoMIPS (lpj=8783488)
[    0.763665] pid_max: default: 131072 minimum: 1024
[    0.763953] LSM: Security Framework initializing
[    0.764009] Yama: becoming mindful.
[    0.779215] AppArmor: AppArmor initialized
[    0.779731] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.780063] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.780210] *** VALIDATE tmpfs ***
[    0.781192] *** VALIDATE proc ***
[    0.781310] *** VALIDATE cgroup1 ***
[    0.781312] *** VALIDATE cgroup2 ***
[    0.781858] LVT offset 2 assigned for vector 0xf4
[    0.781871] Last level iTLB entries: 4KB 1024, 2MB 1024, 4MB 512
[    0.781871] Last level dTLB entries: 4KB 1536, 2MB 1536, 4MB 768, 1GB 0
[    0.781876] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
[    0.781877] Spectre V2 : Mitigation: Full AMD retpoline
[    0.781877] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    0.781879] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
[    0.781880] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.782162] Freeing SMP alternatives memory: 40K
[    0.786159] smpboot: CPU0: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx (family: 0x17, model: 0x11, stepping: 0x0)
[    0.788652] Performance Events: AMD PMU driver.
[    0.788666] ... version:                0
[    0.788666] ... bit width:              48
[    0.788666] ... generic registers:      4
[    0.788667] ... value mask:             0000ffffffffffff
[    0.788667] ... max period:             00007fffffffffff
[    0.788668] ... fixed-purpose events:   0
[    0.788668] ... event mask:             000000000000000f
[    0.788828] rcu: Hierarchical SRCU implementation.
[    0.790313] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.811039] smp: Bringing up secondary CPUs ...
[    0.812186] x86: Booting SMP configuration:
[    0.812188] .... node  #0, CPUs:          #1
[    0.005787] smpboot: CPU 1 Converting physical 2 to logical package 1
[    0.005787] smpboot: CPU 1 Converting physical 2 to logical die 1
[    0.813946] smp: Brought up 1 node, 2 CPUs
[    0.813946] smpboot: Max logical packages: 128
[    0.813946] smpboot: Total of 2 processors activated (8783.48 BogoMIPS)
[    0.816420] devtmpfs: initialized
[    0.816420] x86/mm: Memory block size: 128MB
[    0.817491] PM: Registering ACPI NVS region [mem 0xbfeff000-0xbfefffff] (4096 bytes)
[    0.819768] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.831360] futex hash table entries: 32768 (order: 9, 2097152 bytes, linear)
[    0.831655] pinctrl core: initialized pinctrl subsystem
[    0.831857] PM: RTC time: 10:38:56, date: 2021-11-26
[    0.833125] NET: Registered protocol family 16
[    0.833460] audit: initializing netlink subsys (disabled)
[    0.833927] audit: type=2000 audit(1637923136.072:1): state=initialized audit_enabled=0 res=1
[    0.833927] EISA bus registered
[    0.833927] cpuidle: using governor ladder
[    0.833927] cpuidle: using governor menu
[    0.833927] Simple Boot Flag at 0x36 set to 0x80
[    0.833927] ACPI: bus type PCI registered
[    0.833927] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.836217] PCI: MMCONFIG for domain 0000 [bus 00-7f] at [mem 0xf0000000-0xf7ffffff] (base 0xf0000000)
[    0.836221] PCI: MMCONFIG at [mem 0xf0000000-0xf7ffffff] reserved in E820
[    0.836266] PCI: Using configuration type 1 for base access
[    0.840334] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.840334] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.856318] ACPI: Added _OSI(Module Device)
[    0.856318] ACPI: Added _OSI(Processor Device)
[    0.856318] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.856318] ACPI: Added _OSI(Processor Aggregator Device)
[    0.856318] ACPI: Added _OSI(Linux-Dell-Video)
[    0.856318] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    0.856318] ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
[    0.894721] ACPI: 1 ACPI AML tables successfully acquired and loaded
[    0.897965] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.926355] ACPI: Interpreter enabled
[    0.926374] ACPI: (supports S0 S1 S4 S5)
[    0.926377] ACPI: Using IOAPIC for interrupt routing
[    0.926418] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.929077] ACPI: Enabled 4 GPEs in block 00 to 0F
[    1.246928] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-7f])
[    1.246939] acpi PNP0A03:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[    1.247197] acpi PNP0A03:00: _OSC: platform does not support [AER LTR]
[    1.247470] acpi PNP0A03:00: _OSC: OS now controls [PCIeHotplug SHPCHotplug PME PCIeCapability]
[    1.250206] PCI host bridge to bus 0000:00
[    1.250211] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    1.250213] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000d3fff window]
[    1.250214] pci_bus 0000:00: root bus resource [mem 0x000d4000-0x000d7fff window]
[    1.250214] pci_bus 0000:00: root bus resource [mem 0x000d8000-0x000dbfff window]
[    1.250216] pci_bus 0000:00: root bus resource [mem 0xc0000000-0xfebfffff window]
[    1.250217] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    1.250218] pci_bus 0000:00: root bus resource [io  0x0d00-0xfeff window]
[    1.250219] pci_bus 0000:00: root bus resource [bus 00-7f]
[    1.250284] pci 0000:00:00.0: [8086:7190] type 00 class 0x060000
[    1.251257] pci 0000:00:01.0: [8086:7191] type 01 class 0x060400
[    1.253344] pci 0000:00:07.0: [8086:7110] type 00 class 0x060100
[    1.254967] pci 0000:00:07.1: [8086:7111] type 00 class 0x01018a
[    1.256331] pci 0000:00:07.1: reg 0x20: [io  0x1060-0x106f]
[    1.256835] pci 0000:00:07.1: legacy IDE quirk: reg 0x10: [io  0x01f0-0x01f7]
[    1.256837] pci 0000:00:07.1: legacy IDE quirk: reg 0x14: [io  0x03f6]
[    1.256837] pci 0000:00:07.1: legacy IDE quirk: reg 0x18: [io  0x0170-0x0177]
[    1.256838] pci 0000:00:07.1: legacy IDE quirk: reg 0x1c: [io  0x0376]
[    1.257208] pci 0000:00:07.3: [8086:7113] type 00 class 0x068000
[    1.258727] pci 0000:00:07.3: quirk: [io  0x1000-0x103f] claimed by PIIX4 ACPI
[    1.258739] pci 0000:00:07.3: quirk: [io  0x1040-0x104f] claimed by PIIX4 SMB
[    1.259247] pci 0000:00:07.7: [15ad:0740] type 00 class 0x088000
[    1.259663] pci 0000:00:07.7: reg 0x10: [io  0x1080-0x10bf]
[    1.260116] pci 0000:00:07.7: reg 0x14: [mem 0xfebfe000-0xfebfffff 64bit]
[    1.263382] pci 0000:00:0f.0: [15ad:0405] type 00 class 0x030000
[    1.265317] pci 0000:00:0f.0: reg 0x10: [io  0x1070-0x107f]
[    1.266723] pci 0000:00:0f.0: reg 0x14: [mem 0xe8000000-0xefffffff pref]
[    1.267663] pci 0000:00:0f.0: reg 0x18: [mem 0xfe000000-0xfe7fffff]
[    1.274282] pci 0000:00:0f.0: reg 0x30: [mem 0x00000000-0x00007fff pref]
[    1.275171] pci 0000:00:10.0: [1000:0030] type 00 class 0x010000
[    1.276083] pci 0000:00:10.0: reg 0x10: [io  0x1400-0x14ff]
[    1.276906] pci 0000:00:10.0: reg 0x14: [mem 0xfeba0000-0xfebbffff 64bit]
[    1.277719] pci 0000:00:10.0: reg 0x1c: [mem 0xfebc0000-0xfebdffff 64bit]
[    1.279268] pci 0000:00:10.0: reg 0x30: [mem 0x00000000-0x00003fff pref]
[    1.280052] pci 0000:00:11.0: [15ad:0790] type 01 class 0x060401
[    1.281594] pci 0000:00:15.0: [15ad:07a0] type 01 class 0x060400
[    1.282826] pci 0000:00:15.0: PME# supported from D0 D3hot D3cold
[    1.283540] pci 0000:00:15.1: [15ad:07a0] type 01 class 0x060400
[    1.284793] pci 0000:00:15.1: PME# supported from D0 D3hot D3cold
[    1.285319] pci 0000:00:15.2: [15ad:07a0] type 01 class 0x060400
[    1.286476] pci 0000:00:15.2: PME# supported from D0 D3hot D3cold
[    1.287079] pci 0000:00:15.3: [15ad:07a0] type 01 class 0x060400
[    1.288248] pci 0000:00:15.3: PME# supported from D0 D3hot D3cold
[    1.288964] pci 0000:00:15.4: [15ad:07a0] type 01 class 0x060400
[    1.290276] pci 0000:00:15.4: PME# supported from D0 D3hot D3cold
[    1.290859] pci 0000:00:15.5: [15ad:07a0] type 01 class 0x060400
[    1.292049] pci 0000:00:15.5: PME# supported from D0 D3hot D3cold
[    1.292558] pci 0000:00:15.6: [15ad:07a0] type 01 class 0x060400
[    1.293769] pci 0000:00:15.6: PME# supported from D0 D3hot D3cold
[    1.294263] pci 0000:00:15.7: [15ad:07a0] type 01 class 0x060400
[    1.295379] pci 0000:00:15.7: PME# supported from D0 D3hot D3cold
[    1.295977] pci 0000:00:16.0: [15ad:07a0] type 01 class 0x060400
[    1.297081] pci 0000:00:16.0: PME# supported from D0 D3hot D3cold
[    1.297835] pci 0000:00:16.1: [15ad:07a0] type 01 class 0x060400
[    1.298984] pci 0000:00:16.1: PME# supported from D0 D3hot D3cold
[    1.299459] pci 0000:00:16.2: [15ad:07a0] type 01 class 0x060400
[    1.300582] pci 0000:00:16.2: PME# supported from D0 D3hot D3cold
[    1.301039] pci 0000:00:16.3: [15ad:07a0] type 01 class 0x060400
[    1.302171] pci 0000:00:16.3: PME# supported from D0 D3hot D3cold
[    1.302659] pci 0000:00:16.4: [15ad:07a0] type 01 class 0x060400
[    1.303867] pci 0000:00:16.4: PME# supported from D0 D3hot D3cold
[    1.304522] pci 0000:00:16.5: [15ad:07a0] type 01 class 0x060400
[    1.305748] pci 0000:00:16.5: PME# supported from D0 D3hot D3cold
[    1.306281] pci 0000:00:16.6: [15ad:07a0] type 01 class 0x060400
[    1.307390] pci 0000:00:16.6: PME# supported from D0 D3hot D3cold
[    1.308027] pci 0000:00:16.7: [15ad:07a0] type 01 class 0x060400
[    1.309439] pci 0000:00:16.7: PME# supported from D0 D3hot D3cold
[    1.310154] pci 0000:00:17.0: [15ad:07a0] type 01 class 0x060400
[    1.311317] pci 0000:00:17.0: PME# supported from D0 D3hot D3cold
[    1.311966] pci 0000:00:17.1: [15ad:07a0] type 01 class 0x060400
[    1.313008] pci 0000:00:17.1: PME# supported from D0 D3hot D3cold
[    1.313412] pci 0000:00:17.2: [15ad:07a0] type 01 class 0x060400
[    1.314452] pci 0000:00:17.2: PME# supported from D0 D3hot D3cold
[    1.314871] pci 0000:00:17.3: [15ad:07a0] type 01 class 0x060400
[    1.315936] pci 0000:00:17.3: PME# supported from D0 D3hot D3cold
[    1.316432] pci 0000:00:17.4: [15ad:07a0] type 01 class 0x060400
[    1.317515] pci 0000:00:17.4: PME# supported from D0 D3hot D3cold
[    1.317970] pci 0000:00:17.5: [15ad:07a0] type 01 class 0x060400
[    1.319025] pci 0000:00:17.5: PME# supported from D0 D3hot D3cold
[    1.319946] pci 0000:00:17.6: [15ad:07a0] type 01 class 0x060400
[    1.322009] pci 0000:00:17.6: PME# supported from D0 D3hot D3cold
[    1.322966] pci 0000:00:17.7: [15ad:07a0] type 01 class 0x060400
[    1.324372] pci 0000:00:17.7: PME# supported from D0 D3hot D3cold
[    1.324960] pci 0000:00:18.0: [15ad:07a0] type 01 class 0x060400
[    1.326142] pci 0000:00:18.0: PME# supported from D0 D3hot D3cold
[    1.326776] pci 0000:00:18.1: [15ad:07a0] type 01 class 0x060400
[    1.327874] pci 0000:00:18.1: PME# supported from D0 D3hot D3cold
[    1.328815] pci 0000:00:18.2: [15ad:07a0] type 01 class 0x060400
[    1.330088] pci 0000:00:18.2: PME# supported from D0 D3hot D3cold
[    1.330972] pci 0000:00:18.3: [15ad:07a0] type 01 class 0x060400
[    1.332206] pci 0000:00:18.3: PME# supported from D0 D3hot D3cold
[    1.332642] pci 0000:00:18.4: [15ad:07a0] type 01 class 0x060400
[    1.333676] pci 0000:00:18.4: PME# supported from D0 D3hot D3cold
[    1.334084] pci 0000:00:18.5: [15ad:07a0] type 01 class 0x060400
[    1.335256] pci 0000:00:18.5: PME# supported from D0 D3hot D3cold
[    1.335810] pci 0000:00:18.6: [15ad:07a0] type 01 class 0x060400
[    1.337001] pci 0000:00:18.6: PME# supported from D0 D3hot D3cold
[    1.337490] pci 0000:00:18.7: [15ad:07a0] type 01 class 0x060400
[    1.338647] pci 0000:00:18.7: PME# supported from D0 D3hot D3cold
[    1.339928] pci_bus 0000:01: extended config space not accessible
[    1.342836] pci 0000:00:01.0: PCI bridge to [bus 01]
[    1.343120] pci_bus 0000:02: extended config space not accessible
[    1.343820] acpiphp: Slot [32] registered
[    1.343913] acpiphp: Slot [33] registered
[    1.343947] acpiphp: Slot [34] registered
[    1.343979] acpiphp: Slot [35] registered
[    1.344010] acpiphp: Slot [36] registered
[    1.344039] acpiphp: Slot [37] registered
[    1.344074] acpiphp: Slot [38] registered
[    1.344104] acpiphp: Slot [39] registered
[    1.344137] acpiphp: Slot [40] registered
[    1.344167] acpiphp: Slot [41] registered
[    1.344196] acpiphp: Slot [42] registered
[    1.344226] acpiphp: Slot [43] registered
[    1.344255] acpiphp: Slot [44] registered
[    1.344367] acpiphp: Slot [45] registered
[    1.344416] acpiphp: Slot [46] registered
[    1.344448] acpiphp: Slot [47] registered
[    1.344509] acpiphp: Slot [48] registered
[    1.344542] acpiphp: Slot [49] registered
[    1.344572] acpiphp: Slot [50] registered
[    1.344602] acpiphp: Slot [51] registered
[    1.344636] acpiphp: Slot [52] registered
[    1.344666] acpiphp: Slot [53] registered
[    1.344696] acpiphp: Slot [54] registered
[    1.344726] acpiphp: Slot [55] registered
[    1.344756] acpiphp: Slot [56] registered
[    1.344844] acpiphp: Slot [57] registered
[    1.344876] acpiphp: Slot [58] registered
[    1.344907] acpiphp: Slot [59] registered
[    1.344938] acpiphp: Slot [60] registered
[    1.344968] acpiphp: Slot [61] registered
[    1.344998] acpiphp: Slot [62] registered
[    1.345027] acpiphp: Slot [63] registered
[    1.345126] pci 0000:02:00.0: [15ad:0774] type 00 class 0x0c0300
[    1.347426] pci 0000:02:00.0: reg 0x20: [io  0x2080-0x209f]
[    1.349042] pci 0000:02:01.0: [8086:100f] type 00 class 0x020000
[    1.350051] pci 0000:02:01.0: reg 0x10: [mem 0xfd5c0000-0xfd5dffff 64bit]
[    1.350792] pci 0000:02:01.0: reg 0x18: [mem 0xfdff0000-0xfdffffff 64bit]
[    1.351478] pci 0000:02:01.0: reg 0x20: [io  0x2000-0x203f]
[    1.352631] pci 0000:02:01.0: reg 0x30: [mem 0x00000000-0x0000ffff pref]
[    1.352964] pci 0000:02:01.0: PME# supported from D0 D3hot D3cold
[    1.353530] pci 0000:02:02.0: [1274:1371] type 00 class 0x040100
[    1.353954] pci 0000:02:02.0: reg 0x10: [io  0x2040-0x207f]
[    1.356422] pci 0000:02:03.0: [15ad:0770] type 00 class 0x0c0320
[    1.357117] pci 0000:02:03.0: reg 0x10: [mem 0xfd5ef000-0xfd5effff]
[    1.361073] pci 0000:02:05.0: [15ad:07e0] type 00 class 0x010601
[    1.363023] pci 0000:02:05.0: reg 0x24: [mem 0xfd5ee000-0xfd5eefff]
[    1.363315] pci 0000:02:05.0: reg 0x30: [mem 0x00000000-0x0000ffff pref]
[    1.363813] pci 0000:02:05.0: PME# supported from D3hot
[    1.366870] pci 0000:00:11.0: PCI bridge to [bus 02] (subtractive decode)
[    1.366895] pci 0000:00:11.0:   bridge window [io  0x2000-0x3fff]
[    1.366917] pci 0000:00:11.0:   bridge window [mem 0xfd500000-0xfdffffff]
[    1.366958] pci 0000:00:11.0:   bridge window [mem 0xe7b00000-0xe7ffffff 64bit pref]
[    1.366961] pci 0000:00:11.0:   bridge window [mem 0x000a0000-0x000bffff window] (subtractive decode)
[    1.366962] pci 0000:00:11.0:   bridge window [mem 0x000d0000-0x000d3fff window] (subtractive decode)
[    1.366963] pci 0000:00:11.0:   bridge window [mem 0x000d4000-0x000d7fff window] (subtractive decode)
[    1.366964] pci 0000:00:11.0:   bridge window [mem 0x000d8000-0x000dbfff window] (subtractive decode)
[    1.366964] pci 0000:00:11.0:   bridge window [mem 0xc0000000-0xfebfffff window] (subtractive decode)
[    1.366965] pci 0000:00:11.0:   bridge window [io  0x0000-0x0cf7 window] (subtractive decode)
[    1.366966] pci 0000:00:11.0:   bridge window [io  0x0d00-0xfeff window] (subtractive decode)
[    1.367572] pci 0000:03:00.0: [15ad:0779] type 00 class 0x0c0330
[    1.368102] pci 0000:03:00.0: reg 0x10: [mem 0xfd4e0000-0xfd4fffff 64bit]
[    1.370136] pci 0000:03:00.0: PME# supported from D0 D3hot D3cold
[    1.370759] pci 0000:03:00.0: disabling ASPM on pre-1.1 PCIe device.  You can enable it with 'pcie_aspm=force'
[    1.372764] pci 0000:00:15.0: PCI bridge to [bus 03]
[    1.372811] pci 0000:00:15.0:   bridge window [mem 0xfd400000-0xfd4fffff]
[    1.376594] pci 0000:00:15.1: PCI bridge to [bus 04]
[    1.376660] pci 0000:00:15.1:   bridge window [io  0x7000-0x7fff]
[    1.376688] pci 0000:00:15.1:   bridge window [mem 0xfd000000-0xfd0fffff]
[    1.376739] pci 0000:00:15.1:   bridge window [mem 0xe7700000-0xe77fffff 64bit pref]
[    1.380249] pci 0000:00:15.2: PCI bridge to [bus 05]
[    1.380281] pci 0000:00:15.2:   bridge window [io  0xb000-0xbfff]
[    1.380303] pci 0000:00:15.2:   bridge window [mem 0xfcc00000-0xfccfffff]
[    1.380346] pci 0000:00:15.2:   bridge window [mem 0xe7300000-0xe73fffff 64bit pref]
[    1.383637] pci 0000:00:15.3: PCI bridge to [bus 06]
[    1.383710] pci 0000:00:15.3:   bridge window [mem 0xfc800000-0xfc8fffff]
[    1.383753] pci 0000:00:15.3:   bridge window [mem 0xe6f00000-0xe6ffffff 64bit pref]
[    1.387095] pci 0000:00:15.4: PCI bridge to [bus 07]
[    1.387699] pci 0000:00:15.4:   bridge window [mem 0xfc400000-0xfc4fffff]
[    1.387741] pci 0000:00:15.4:   bridge window [mem 0xe6b00000-0xe6bfffff 64bit pref]
[    1.391187] pci 0000:00:15.5: PCI bridge to [bus 08]
[    1.391231] pci 0000:00:15.5:   bridge window [mem 0xfc000000-0xfc0fffff]
[    1.391274] pci 0000:00:15.5:   bridge window [mem 0xe6700000-0xe67fffff 64bit pref]
[    1.395143] pci 0000:00:15.6: PCI bridge to [bus 09]
[    1.395220] pci 0000:00:15.6:   bridge window [mem 0xfbc00000-0xfbcfffff]
[    1.395269] pci 0000:00:15.6:   bridge window [mem 0xe6300000-0xe63fffff 64bit pref]
[    1.398961] pci 0000:00:15.7: PCI bridge to [bus 0a]
[    1.399013] pci 0000:00:15.7:   bridge window [mem 0xfb800000-0xfb8fffff]
[    1.399053] pci 0000:00:15.7:   bridge window [mem 0xe5f00000-0xe5ffffff 64bit pref]
[    1.401327] pci 0000:00:16.0: PCI bridge to [bus 0b]
[    1.401350] pci 0000:00:16.0:   bridge window [io  0x4000-0x4fff]
[    1.401372] pci 0000:00:16.0:   bridge window [mem 0xfd300000-0xfd3fffff]
[    1.401412] pci 0000:00:16.0:   bridge window [mem 0xe7a00000-0xe7afffff 64bit pref]
[    1.404872] pci 0000:00:16.1: PCI bridge to [bus 0c]
[    1.404900] pci 0000:00:16.1:   bridge window [io  0x8000-0x8fff]
[    1.404922] pci 0000:00:16.1:   bridge window [mem 0xfcf00000-0xfcffffff]
[    1.404966] pci 0000:00:16.1:   bridge window [mem 0xe7600000-0xe76fffff 64bit pref]
[    1.407810] pci 0000:00:16.2: PCI bridge to [bus 0d]
[    1.407842] pci 0000:00:16.2:   bridge window [io  0xc000-0xcfff]
[    1.407865] pci 0000:00:16.2:   bridge window [mem 0xfcb00000-0xfcbfffff]
[    1.407904] pci 0000:00:16.2:   bridge window [mem 0xe7200000-0xe72fffff 64bit pref]
[    1.410913] pci 0000:00:16.3: PCI bridge to [bus 0e]
[    1.411691] pci 0000:00:16.3:   bridge window [mem 0xfc700000-0xfc7fffff]
[    1.411730] pci 0000:00:16.3:   bridge window [mem 0xe6e00000-0xe6efffff 64bit pref]
[    1.414811] pci 0000:00:16.4: PCI bridge to [bus 0f]
[    1.414860] pci 0000:00:16.4:   bridge window [mem 0xfc300000-0xfc3fffff]
[    1.414900] pci 0000:00:16.4:   bridge window [mem 0xe6a00000-0xe6afffff 64bit pref]
[    1.417158] pci 0000:00:16.5: PCI bridge to [bus 10]
[    1.417199] pci 0000:00:16.5:   bridge window [mem 0xfbf00000-0xfbffffff]
[    1.417237] pci 0000:00:16.5:   bridge window [mem 0xe6600000-0xe66fffff 64bit pref]
[    1.420910] pci 0000:00:16.6: PCI bridge to [bus 11]
[    1.421017] pci 0000:00:16.6:   bridge window [mem 0xfbb00000-0xfbbfffff]
[    1.421103] pci 0000:00:16.6:   bridge window [mem 0xe6200000-0xe62fffff 64bit pref]
[    1.425852] pci 0000:00:16.7: PCI bridge to [bus 12]
[    1.425927] pci 0000:00:16.7:   bridge window [mem 0xfb700000-0xfb7fffff]
[    1.425983] pci 0000:00:16.7:   bridge window [mem 0xe5e00000-0xe5efffff 64bit pref]
[    1.430640] pci 0000:00:17.0: PCI bridge to [bus 13]
[    1.430695] pci 0000:00:17.0:   bridge window [io  0x5000-0x5fff]
[    1.430722] pci 0000:00:17.0:   bridge window [mem 0xfd200000-0xfd2fffff]
[    1.430829] pci 0000:00:17.0:   bridge window [mem 0xe7900000-0xe79fffff 64bit pref]
[    1.433171] pci 0000:00:17.1: PCI bridge to [bus 14]
[    1.433208] pci 0000:00:17.1:   bridge window [io  0x9000-0x9fff]
[    1.433229] pci 0000:00:17.1:   bridge window [mem 0xfce00000-0xfcefffff]
[    1.433267] pci 0000:00:17.1:   bridge window [mem 0xe7500000-0xe75fffff 64bit pref]
[    1.436218] pci 0000:00:17.2: PCI bridge to [bus 15]
[    1.436243] pci 0000:00:17.2:   bridge window [io  0xd000-0xdfff]
[    1.436264] pci 0000:00:17.2:   bridge window [mem 0xfca00000-0xfcafffff]
[    1.436302] pci 0000:00:17.2:   bridge window [mem 0xe7100000-0xe71fffff 64bit pref]
[    1.439184] pci 0000:00:17.3: PCI bridge to [bus 16]
[    1.439688] pci 0000:00:17.3:   bridge window [mem 0xfc600000-0xfc6fffff]
[    1.439726] pci 0000:00:17.3:   bridge window [mem 0xe6d00000-0xe6dfffff 64bit pref]
[    1.442988] pci 0000:00:17.4: PCI bridge to [bus 17]
[    1.443058] pci 0000:00:17.4:   bridge window [mem 0xfc200000-0xfc2fffff]
[    1.443117] pci 0000:00:17.4:   bridge window [mem 0xe6900000-0xe69fffff 64bit pref]
[    1.446745] pci 0000:00:17.5: PCI bridge to [bus 18]
[    1.446788] pci 0000:00:17.5:   bridge window [mem 0xfbe00000-0xfbefffff]
[    1.446829] pci 0000:00:17.5:   bridge window [mem 0xe6500000-0xe65fffff 64bit pref]
[    1.449063] pci 0000:00:17.6: PCI bridge to [bus 19]
[    1.449109] pci 0000:00:17.6:   bridge window [mem 0xfba00000-0xfbafffff]
[    1.449147] pci 0000:00:17.6:   bridge window [mem 0xe6100000-0xe61fffff 64bit pref]
[    1.453307] pci 0000:00:17.7: PCI bridge to [bus 1a]
[    1.453454] pci 0000:00:17.7:   bridge window [mem 0xfb600000-0xfb6fffff]
[    1.453559] pci 0000:00:17.7:   bridge window [mem 0xe5d00000-0xe5dfffff 64bit pref]
[    1.459655] pci 0000:00:18.0: PCI bridge to [bus 1b]
[    1.459681] pci 0000:00:18.0:   bridge window [io  0x6000-0x6fff]
[    1.459713] pci 0000:00:18.0:   bridge window [mem 0xfd100000-0xfd1fffff]
[    1.459784] pci 0000:00:18.0:   bridge window [mem 0xe7800000-0xe78fffff 64bit pref]
[    1.464137] pci 0000:00:18.1: PCI bridge to [bus 1c]
[    1.464177] pci 0000:00:18.1:   bridge window [io  0xa000-0xafff]
[    1.464208] pci 0000:00:18.1:   bridge window [mem 0xfcd00000-0xfcdfffff]
[    1.464266] pci 0000:00:18.1:   bridge window [mem 0xe7400000-0xe74fffff 64bit pref]
[    1.468177] pci 0000:00:18.2: PCI bridge to [bus 1d]
[    1.468209] pci 0000:00:18.2:   bridge window [io  0xe000-0xefff]
[    1.468232] pci 0000:00:18.2:   bridge window [mem 0xfc900000-0xfc9fffff]
[    1.468276] pci 0000:00:18.2:   bridge window [mem 0xe7000000-0xe70fffff 64bit pref]
[    1.471291] pci 0000:00:18.3: PCI bridge to [bus 1e]
[    1.471693] pci 0000:00:18.3:   bridge window [mem 0xfc500000-0xfc5fffff]
[    1.471735] pci 0000:00:18.3:   bridge window [mem 0xe6c00000-0xe6cfffff 64bit pref]
[    1.474930] pci 0000:00:18.4: PCI bridge to [bus 1f]
[    1.475010] pci 0000:00:18.4:   bridge window [mem 0xfc100000-0xfc1fffff]
[    1.475052] pci 0000:00:18.4:   bridge window [mem 0xe6800000-0xe68fffff 64bit pref]
[    1.478909] pci 0000:00:18.5: PCI bridge to [bus 20]
[    1.478977] pci 0000:00:18.5:   bridge window [mem 0xfbd00000-0xfbdfffff]
[    1.479026] pci 0000:00:18.5:   bridge window [mem 0xe6400000-0xe64fffff 64bit pref]
[    1.482738] pci 0000:00:18.6: PCI bridge to [bus 21]
[    1.482815] pci 0000:00:18.6:   bridge window [mem 0xfb900000-0xfb9fffff]
[    1.483701] pci 0000:00:18.6:   bridge window [mem 0xe6000000-0xe60fffff 64bit pref]
[    1.487655] pci 0000:00:18.7: PCI bridge to [bus 22]
[    1.487725] pci 0000:00:18.7:   bridge window [mem 0xfb500000-0xfb5fffff]
[    1.487789] pci 0000:00:18.7:   bridge window [mem 0xe5c00000-0xe5cfffff 64bit pref]
[    1.493262] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 7 *9 10 11 14 15)
[    1.493392] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 7 9 10 *11 14 15)
[    1.493518] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 7 9 *10 11 14 15)
[    1.493640] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 *7 9 10 11 14 15)
[    1.554687] iommu: Default domain type: Translated 
[    1.555721] SCSI subsystem initialized
[    1.555921] libata version 3.00 loaded.
[    1.556011] pci 0000:00:0f.0: vgaarb: setting as boot VGA device
[    1.556011] pci 0000:00:0f.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    1.556011] pci 0000:00:0f.0: vgaarb: bridge control possible
[    1.556011] vgaarb: loaded
[    1.556011] ACPI: bus type USB registered
[    1.556011] usbcore: registered new interface driver usbfs
[    1.556011] usbcore: registered new interface driver hub
[    1.556011] usbcore: registered new device driver usb
[    1.556011] pps_core: LinuxPPS API ver. 1 registered
[    1.556011] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    1.556011] PTP clock support registered
[    1.556191] EDAC MC: Ver: 3.0.0
[    1.559708] PCI: Using ACPI for IRQ routing
[    1.573186] PCI: pci_cache_line_size set to 64 bytes
[    1.574196] e820: reserve RAM buffer [mem 0x0009e800-0x0009ffff]
[    1.574200] e820: reserve RAM buffer [mem 0xbfed0000-0xbfffffff]
[    1.576017] NetLabel: Initializing
[    1.576019] NetLabel:  domain hash size = 128
[    1.576020] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    1.576039] NetLabel:  unlabeled traffic allowed by default
[    1.576095] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
[    1.576095] hpet0: 16 comparators, 64-bit 14.318180 MHz counter
[    1.577926] clocksource: Switched to clocksource tsc-early
[    1.645034] *** VALIDATE bpf ***
[    1.645194] VFS: Disk quotas dquot_6.6.0
[    1.645289] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    1.645331] *** VALIDATE ramfs ***
[    1.645340] *** VALIDATE hugetlbfs ***
[    1.646049] AppArmor: AppArmor Filesystem Enabled
[    1.646085] pnp: PnP ACPI init
[    1.646617] system 00:00: [io  0x1000-0x103f] has been reserved
[    1.646619] system 00:00: [io  0x1040-0x104f] has been reserved
[    1.646622] system 00:00: [io  0x0cf0-0x0cf1] has been reserved
[    1.646628] system 00:00: Plug and Play ACPI device, IDs PNP0c02 (active)
[    1.646663] pnp 00:01: Plug and Play ACPI device, IDs PNP0b00 (active)
[    1.646790] pnp 00:02: Plug and Play ACPI device, IDs PNP0303 (active)
[    1.646817] pnp 00:03: Plug and Play ACPI device, IDs VMW0003 PNP0f13 (active)
[    1.647179] system 00:04: [mem 0xfed00000-0xfed003ff] has been reserved
[    1.647185] system 00:04: Plug and Play ACPI device, IDs PNP0103 PNP0c01 (active)
[    1.650498] system 00:05: [io  0xfce0-0xfcff] has been reserved
[    1.650504] system 00:05: [mem 0xf0000000-0xf7ffffff] has been reserved
[    1.650506] system 00:05: [mem 0xfe800000-0xfe9fffff] has been reserved
[    1.650519] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    1.697437] pnp: PnP ACPI: found 6 devices
[    1.709170] thermal_sys: Registered thermal governor 'fair_share'
[    1.709172] thermal_sys: Registered thermal governor 'bang_bang'
[    1.709173] thermal_sys: Registered thermal governor 'step_wise'
[    1.709173] thermal_sys: Registered thermal governor 'user_space'
[    1.709174] thermal_sys: Registered thermal governor 'power_allocator'
[    1.713707] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    1.713789] pci 0000:00:15.0: bridge window [io  0x1000-0x0fff] to [bus 03] add_size 1000
[    1.713792] pci 0000:00:15.0: bridge window [mem 0x00100000-0x000fffff 64bit pref] to [bus 03] add_size 200000 add_align 100000
[    1.713794] pci 0000:00:15.3: bridge window [io  0x1000-0x0fff] to [bus 06] add_size 1000
[    1.713796] pci 0000:00:15.4: bridge window [io  0x1000-0x0fff] to [bus 07] add_size 1000
[    1.713798] pci 0000:00:15.5: bridge window [io  0x1000-0x0fff] to [bus 08] add_size 1000
[    1.713799] pci 0000:00:15.6: bridge window [io  0x1000-0x0fff] to [bus 09] add_size 1000
[    1.713800] pci 0000:00:15.7: bridge window [io  0x1000-0x0fff] to [bus 0a] add_size 1000
[    1.713802] pci 0000:00:16.3: bridge window [io  0x1000-0x0fff] to [bus 0e] add_size 1000
[    1.713803] pci 0000:00:16.4: bridge window [io  0x1000-0x0fff] to [bus 0f] add_size 1000
[    1.713805] pci 0000:00:16.5: bridge window [io  0x1000-0x0fff] to [bus 10] add_size 1000
[    1.713806] pci 0000:00:16.6: bridge window [io  0x1000-0x0fff] to [bus 11] add_size 1000
[    1.713807] pci 0000:00:16.7: bridge window [io  0x1000-0x0fff] to [bus 12] add_size 1000
[    1.713809] pci 0000:00:17.3: bridge window [io  0x1000-0x0fff] to [bus 16] add_size 1000
[    1.713811] pci 0000:00:17.4: bridge window [io  0x1000-0x0fff] to [bus 17] add_size 1000
[    1.713812] pci 0000:00:17.5: bridge window [io  0x1000-0x0fff] to [bus 18] add_size 1000
[    1.713813] pci 0000:00:17.6: bridge window [io  0x1000-0x0fff] to [bus 19] add_size 1000
[    1.713915] pci 0000:00:17.7: bridge window [io  0x1000-0x0fff] to [bus 1a] add_size 1000
[    1.713919] pci 0000:00:18.3: bridge window [io  0x1000-0x0fff] to [bus 1e] add_size 1000
[    1.713921] pci 0000:00:18.4: bridge window [io  0x1000-0x0fff] to [bus 1f] add_size 1000
[    1.713923] pci 0000:00:18.5: bridge window [io  0x1000-0x0fff] to [bus 20] add_size 1000
[    1.713925] pci 0000:00:18.6: bridge window [io  0x1000-0x0fff] to [bus 21] add_size 1000
[    1.713927] pci 0000:00:18.7: bridge window [io  0x1000-0x0fff] to [bus 22] add_size 1000
[    1.713982] pci 0000:00:15.0: BAR 15: assigned [mem 0xc0000000-0xc01fffff 64bit pref]
[    1.713985] pci 0000:00:0f.0: BAR 6: assigned [mem 0xc0200000-0xc0207fff pref]
[    1.713988] pci 0000:00:10.0: BAR 6: assigned [mem 0xc0208000-0xc020bfff pref]
[    1.713992] pci 0000:00:15.0: BAR 13: no space for [io  size 0x1000]
[    1.713993] pci 0000:00:15.0: BAR 13: failed to assign [io  size 0x1000]
[    1.713996] pci 0000:00:15.3: BAR 13: no space for [io  size 0x1000]
[    1.713997] pci 0000:00:15.3: BAR 13: failed to assign [io  size 0x1000]
[    1.713999] pci 0000:00:15.4: BAR 13: no space for [io  size 0x1000]
[    1.714001] pci 0000:00:15.4: BAR 13: failed to assign [io  size 0x1000]
[    1.714003] pci 0000:00:15.5: BAR 13: no space for [io  size 0x1000]
[    1.714004] pci 0000:00:15.5: BAR 13: failed to assign [io  size 0x1000]
[    1.714007] pci 0000:00:15.6: BAR 13: no space for [io  size 0x1000]
[    1.714008] pci 0000:00:15.6: BAR 13: failed to assign [io  size 0x1000]
[    1.714010] pci 0000:00:15.7: BAR 13: no space for [io  size 0x1000]
[    1.714012] pci 0000:00:15.7: BAR 13: failed to assign [io  size 0x1000]
[    1.714015] pci 0000:00:16.3: BAR 13: no space for [io  size 0x1000]
[    1.714018] pci 0000:00:16.3: BAR 13: failed to assign [io  size 0x1000]
[    1.714022] pci 0000:00:16.4: BAR 13: no space for [io  size 0x1000]
[    1.714024] pci 0000:00:16.4: BAR 13: failed to assign [io  size 0x1000]
[    1.714028] pci 0000:00:16.5: BAR 13: no space for [io  size 0x1000]
[    1.714031] pci 0000:00:16.5: BAR 13: failed to assign [io  size 0x1000]
[    1.714034] pci 0000:00:16.6: BAR 13: no space for [io  size 0x1000]
[    1.714036] pci 0000:00:16.6: BAR 13: failed to assign [io  size 0x1000]
[    1.714038] pci 0000:00:16.7: BAR 13: no space for [io  size 0x1000]
[    1.714039] pci 0000:00:16.7: BAR 13: failed to assign [io  size 0x1000]
[    1.714041] pci 0000:00:17.3: BAR 13: no space for [io  size 0x1000]
[    1.714042] pci 0000:00:17.3: BAR 13: failed to assign [io  size 0x1000]
[    1.714044] pci 0000:00:17.4: BAR 13: no space for [io  size 0x1000]
[    1.714045] pci 0000:00:17.4: BAR 13: failed to assign [io  size 0x1000]
[    1.714047] pci 0000:00:17.5: BAR 13: no space for [io  size 0x1000]
[    1.714049] pci 0000:00:17.5: BAR 13: failed to assign [io  size 0x1000]
[    1.714051] pci 0000:00:17.6: BAR 13: no space for [io  size 0x1000]
[    1.714052] pci 0000:00:17.6: BAR 13: failed to assign [io  size 0x1000]
[    1.714054] pci 0000:00:17.7: BAR 13: no space for [io  size 0x1000]
[    1.714055] pci 0000:00:17.7: BAR 13: failed to assign [io  size 0x1000]
[    1.714057] pci 0000:00:18.3: BAR 13: no space for [io  size 0x1000]
[    1.714058] pci 0000:00:18.3: BAR 13: failed to assign [io  size 0x1000]
[    1.714061] pci 0000:00:18.4: BAR 13: no space for [io  size 0x1000]
[    1.714062] pci 0000:00:18.4: BAR 13: failed to assign [io  size 0x1000]
[    1.714064] pci 0000:00:18.5: BAR 13: no space for [io  size 0x1000]
[    1.714065] pci 0000:00:18.5: BAR 13: failed to assign [io  size 0x1000]
[    1.714067] pci 0000:00:18.6: BAR 13: no space for [io  size 0x1000]
[    1.714069] pci 0000:00:18.6: BAR 13: failed to assign [io  size 0x1000]
[    1.714071] pci 0000:00:18.7: BAR 13: no space for [io  size 0x1000]
[    1.714072] pci 0000:00:18.7: BAR 13: failed to assign [io  size 0x1000]
[    1.714077] pci 0000:00:18.7: BAR 13: no space for [io  size 0x1000]
[    1.714078] pci 0000:00:18.7: BAR 13: failed to assign [io  size 0x1000]
[    1.714080] pci 0000:00:18.6: BAR 13: no space for [io  size 0x1000]
[    1.714081] pci 0000:00:18.6: BAR 13: failed to assign [io  size 0x1000]
[    1.714083] pci 0000:00:18.5: BAR 13: no space for [io  size 0x1000]
[    1.714085] pci 0000:00:18.5: BAR 13: failed to assign [io  size 0x1000]
[    1.714087] pci 0000:00:18.4: BAR 13: no space for [io  size 0x1000]
[    1.714088] pci 0000:00:18.4: BAR 13: failed to assign [io  size 0x1000]
[    1.714090] pci 0000:00:18.3: BAR 13: no space for [io  size 0x1000]
[    1.714091] pci 0000:00:18.3: BAR 13: failed to assign [io  size 0x1000]
[    1.714094] pci 0000:00:17.7: BAR 13: no space for [io  size 0x1000]
[    1.714095] pci 0000:00:17.7: BAR 13: failed to assign [io  size 0x1000]
[    1.714097] pci 0000:00:17.6: BAR 13: no space for [io  size 0x1000]
[    1.714098] pci 0000:00:17.6: BAR 13: failed to assign [io  size 0x1000]
[    1.714101] pci 0000:00:17.5: BAR 13: no space for [io  size 0x1000]
[    1.714103] pci 0000:00:17.5: BAR 13: failed to assign [io  size 0x1000]
[    1.714105] pci 0000:00:17.4: BAR 13: no space for [io  size 0x1000]
[    1.714106] pci 0000:00:17.4: BAR 13: failed to assign [io  size 0x1000]
[    1.714108] pci 0000:00:17.3: BAR 13: no space for [io  size 0x1000]
[    1.714108] pci 0000:00:17.3: BAR 13: failed to assign [io  size 0x1000]
[    1.714110] pci 0000:00:16.7: BAR 13: no space for [io  size 0x1000]
[    1.714111] pci 0000:00:16.7: BAR 13: failed to assign [io  size 0x1000]
[    1.714113] pci 0000:00:16.6: BAR 13: no space for [io  size 0x1000]
[    1.714114] pci 0000:00:16.6: BAR 13: failed to assign [io  size 0x1000]
[    1.714116] pci 0000:00:16.5: BAR 13: no space for [io  size 0x1000]
[    1.714116] pci 0000:00:16.5: BAR 13: failed to assign [io  size 0x1000]
[    1.714119] pci 0000:00:16.4: BAR 13: no space for [io  size 0x1000]
[    1.714120] pci 0000:00:16.4: BAR 13: failed to assign [io  size 0x1000]
[    1.714122] pci 0000:00:16.3: BAR 13: no space for [io  size 0x1000]
[    1.714124] pci 0000:00:16.3: BAR 13: failed to assign [io  size 0x1000]
[    1.714126] pci 0000:00:15.7: BAR 13: no space for [io  size 0x1000]
[    1.714127] pci 0000:00:15.7: BAR 13: failed to assign [io  size 0x1000]
[    1.714129] pci 0000:00:15.6: BAR 13: no space for [io  size 0x1000]
[    1.714131] pci 0000:00:15.6: BAR 13: failed to assign [io  size 0x1000]
[    1.714133] pci 0000:00:15.5: BAR 13: no space for [io  size 0x1000]
[    1.714134] pci 0000:00:15.5: BAR 13: failed to assign [io  size 0x1000]
[    1.714136] pci 0000:00:15.4: BAR 13: no space for [io  size 0x1000]
[    1.714138] pci 0000:00:15.4: BAR 13: failed to assign [io  size 0x1000]
[    1.714140] pci 0000:00:15.3: BAR 13: no space for [io  size 0x1000]
[    1.714141] pci 0000:00:15.3: BAR 13: failed to assign [io  size 0x1000]
[    1.714143] pci 0000:00:15.0: BAR 13: no space for [io  size 0x1000]
[    1.714144] pci 0000:00:15.0: BAR 13: failed to assign [io  size 0x1000]
[    1.714147] pci 0000:00:01.0: PCI bridge to [bus 01]
[    1.714319] pci 0000:02:01.0: BAR 6: assigned [mem 0xfd500000-0xfd50ffff pref]
[    1.714321] pci 0000:02:05.0: BAR 6: assigned [mem 0xfd510000-0xfd51ffff pref]
[    1.714324] pci 0000:00:11.0: PCI bridge to [bus 02]
[    1.714343] pci 0000:00:11.0:   bridge window [io  0x2000-0x3fff]
[    1.714393] pci 0000:00:11.0:   bridge window [mem 0xfd500000-0xfdffffff]
[    1.714422] pci 0000:00:11.0:   bridge window [mem 0xe7b00000-0xe7ffffff 64bit pref]
[    1.714465] pci 0000:00:15.0: PCI bridge to [bus 03]
[    1.714497] pci 0000:00:15.0:   bridge window [mem 0xfd400000-0xfd4fffff]
[    1.714519] pci 0000:00:15.0:   bridge window [mem 0xc0000000-0xc01fffff 64bit pref]
[    1.714602] pci 0000:00:15.1: PCI bridge to [bus 04]
[    1.714614] pci 0000:00:15.1:   bridge window [io  0x7000-0x7fff]
[    1.714646] pci 0000:00:15.1:   bridge window [mem 0xfd000000-0xfd0fffff]
[    1.714668] pci 0000:00:15.1:   bridge window [mem 0xe7700000-0xe77fffff 64bit pref]
[    1.714726] pci 0000:00:15.2: PCI bridge to [bus 05]
[    1.714739] pci 0000:00:15.2:   bridge window [io  0xb000-0xbfff]
[    1.714770] pci 0000:00:15.2:   bridge window [mem 0xfcc00000-0xfccfffff]
[    1.714791] pci 0000:00:15.2:   bridge window [mem 0xe7300000-0xe73fffff 64bit pref]
[    1.714849] pci 0000:00:15.3: PCI bridge to [bus 06]
[    1.714881] pci 0000:00:15.3:   bridge window [mem 0xfc800000-0xfc8fffff]
[    1.714902] pci 0000:00:15.3:   bridge window [mem 0xe6f00000-0xe6ffffff 64bit pref]
[    1.714959] pci 0000:00:15.4: PCI bridge to [bus 07]
[    1.714991] pci 0000:00:15.4:   bridge window [mem 0xfc400000-0xfc4fffff]
[    1.715012] pci 0000:00:15.4:   bridge window [mem 0xe6b00000-0xe6bfffff 64bit pref]
[    1.715068] pci 0000:00:15.5: PCI bridge to [bus 08]
[    1.715101] pci 0000:00:15.5:   bridge window [mem 0xfc000000-0xfc0fffff]
[    1.715122] pci 0000:00:15.5:   bridge window [mem 0xe6700000-0xe67fffff 64bit pref]
[    1.715182] pci 0000:00:15.6: PCI bridge to [bus 09]
[    1.715214] pci 0000:00:15.6:   bridge window [mem 0xfbc00000-0xfbcfffff]
[    1.715238] pci 0000:00:15.6:   bridge window [mem 0xe6300000-0xe63fffff 64bit pref]
[    1.715295] pci 0000:00:15.7: PCI bridge to [bus 0a]
[    1.715327] pci 0000:00:15.7:   bridge window [mem 0xfb800000-0xfb8fffff]
[    1.715348] pci 0000:00:15.7:   bridge window [mem 0xe5f00000-0xe5ffffff 64bit pref]
[    1.715404] pci 0000:00:16.0: PCI bridge to [bus 0b]
[    1.715416] pci 0000:00:16.0:   bridge window [io  0x4000-0x4fff]
[    1.715447] pci 0000:00:16.0:   bridge window [mem 0xfd300000-0xfd3fffff]
[    1.715468] pci 0000:00:16.0:   bridge window [mem 0xe7a00000-0xe7afffff 64bit pref]
[    1.715525] pci 0000:00:16.1: PCI bridge to [bus 0c]
[    1.715537] pci 0000:00:16.1:   bridge window [io  0x8000-0x8fff]
[    1.715569] pci 0000:00:16.1:   bridge window [mem 0xfcf00000-0xfcffffff]
[    1.715590] pci 0000:00:16.1:   bridge window [mem 0xe7600000-0xe76fffff 64bit pref]
[    1.715646] pci 0000:00:16.2: PCI bridge to [bus 0d]
[    1.715658] pci 0000:00:16.2:   bridge window [io  0xc000-0xcfff]
[    1.715719] pci 0000:00:16.2:   bridge window [mem 0xfcb00000-0xfcbfffff]
[    1.715741] pci 0000:00:16.2:   bridge window [mem 0xe7200000-0xe72fffff 64bit pref]
[    1.715799] pci 0000:00:16.3: PCI bridge to [bus 0e]
[    1.715831] pci 0000:00:16.3:   bridge window [mem 0xfc700000-0xfc7fffff]
[    1.715852] pci 0000:00:16.3:   bridge window [mem 0xe6e00000-0xe6efffff 64bit pref]
[    1.715909] pci 0000:00:16.4: PCI bridge to [bus 0f]
[    1.715941] pci 0000:00:16.4:   bridge window [mem 0xfc300000-0xfc3fffff]
[    1.715962] pci 0000:00:16.4:   bridge window [mem 0xe6a00000-0xe6afffff 64bit pref]
[    1.716019] pci 0000:00:16.5: PCI bridge to [bus 10]
[    1.716052] pci 0000:00:16.5:   bridge window [mem 0xfbf00000-0xfbffffff]
[    1.716078] pci 0000:00:16.5:   bridge window [mem 0xe6600000-0xe66fffff 64bit pref]
[    1.716139] pci 0000:00:16.6: PCI bridge to [bus 11]
[    1.716171] pci 0000:00:16.6:   bridge window [mem 0xfbb00000-0xfbbfffff]
[    1.716193] pci 0000:00:16.6:   bridge window [mem 0xe6200000-0xe62fffff 64bit pref]
[    1.716252] pci 0000:00:16.7: PCI bridge to [bus 12]
[    1.716284] pci 0000:00:16.7:   bridge window [mem 0xfb700000-0xfb7fffff]
[    1.716305] pci 0000:00:16.7:   bridge window [mem 0xe5e00000-0xe5efffff 64bit pref]
[    1.716362] pci 0000:00:17.0: PCI bridge to [bus 13]
[    1.716375] pci 0000:00:17.0:   bridge window [io  0x5000-0x5fff]
[    1.716406] pci 0000:00:17.0:   bridge window [mem 0xfd200000-0xfd2fffff]
[    1.716428] pci 0000:00:17.0:   bridge window [mem 0xe7900000-0xe79fffff 64bit pref]
[    1.716484] pci 0000:00:17.1: PCI bridge to [bus 14]
[    1.716496] pci 0000:00:17.1:   bridge window [io  0x9000-0x9fff]
[    1.716528] pci 0000:00:17.1:   bridge window [mem 0xfce00000-0xfcefffff]
[    1.716549] pci 0000:00:17.1:   bridge window [mem 0xe7500000-0xe75fffff 64bit pref]
[    1.716604] pci 0000:00:17.2: PCI bridge to [bus 15]
[    1.716616] pci 0000:00:17.2:   bridge window [io  0xd000-0xdfff]
[    1.716648] pci 0000:00:17.2:   bridge window [mem 0xfca00000-0xfcafffff]
[    1.716669] pci 0000:00:17.2:   bridge window [mem 0xe7100000-0xe71fffff 64bit pref]
[    1.716725] pci 0000:00:17.3: PCI bridge to [bus 16]
[    1.716757] pci 0000:00:17.3:   bridge window [mem 0xfc600000-0xfc6fffff]
[    1.716778] pci 0000:00:17.3:   bridge window [mem 0xe6d00000-0xe6dfffff 64bit pref]
[    1.716834] pci 0000:00:17.4: PCI bridge to [bus 17]
[    1.716866] pci 0000:00:17.4:   bridge window [mem 0xfc200000-0xfc2fffff]
[    1.716888] pci 0000:00:17.4:   bridge window [mem 0xe6900000-0xe69fffff 64bit pref]
[    1.716944] pci 0000:00:17.5: PCI bridge to [bus 18]
[    1.716975] pci 0000:00:17.5:   bridge window [mem 0xfbe00000-0xfbefffff]
[    1.716996] pci 0000:00:17.5:   bridge window [mem 0xe6500000-0xe65fffff 64bit pref]
[    1.717052] pci 0000:00:17.6: PCI bridge to [bus 19]
[    1.717084] pci 0000:00:17.6:   bridge window [mem 0xfba00000-0xfbafffff]
[    1.717105] pci 0000:00:17.6:   bridge window [mem 0xe6100000-0xe61fffff 64bit pref]
[    1.717161] pci 0000:00:17.7: PCI bridge to [bus 1a]
[    1.717193] pci 0000:00:17.7:   bridge window [mem 0xfb600000-0xfb6fffff]
[    1.717214] pci 0000:00:17.7:   bridge window [mem 0xe5d00000-0xe5dfffff 64bit pref]
[    1.717280] pci 0000:00:18.0: PCI bridge to [bus 1b]
[    1.717293] pci 0000:00:18.0:   bridge window [io  0x6000-0x6fff]
[    1.717324] pci 0000:00:18.0:   bridge window [mem 0xfd100000-0xfd1fffff]
[    1.717345] pci 0000:00:18.0:   bridge window [mem 0xe7800000-0xe78fffff 64bit pref]
[    1.717402] pci 0000:00:18.1: PCI bridge to [bus 1c]
[    1.717414] pci 0000:00:18.1:   bridge window [io  0xa000-0xafff]
[    1.717446] pci 0000:00:18.1:   bridge window [mem 0xfcd00000-0xfcdfffff]
[    1.717467] pci 0000:00:18.1:   bridge window [mem 0xe7400000-0xe74fffff 64bit pref]
[    1.717535] pci 0000:00:18.2: PCI bridge to [bus 1d]
[    1.717547] pci 0000:00:18.2:   bridge window [io  0xe000-0xefff]
[    1.717579] pci 0000:00:18.2:   bridge window [mem 0xfc900000-0xfc9fffff]
[    1.717601] pci 0000:00:18.2:   bridge window [mem 0xe7000000-0xe70fffff 64bit pref]
[    1.717658] pci 0000:00:18.3: PCI bridge to [bus 1e]
[    1.717690] pci 0000:00:18.3:   bridge window [mem 0xfc500000-0xfc5fffff]
[    1.717711] pci 0000:00:18.3:   bridge window [mem 0xe6c00000-0xe6cfffff 64bit pref]
[    1.717767] pci 0000:00:18.4: PCI bridge to [bus 1f]
[    1.717800] pci 0000:00:18.4:   bridge window [mem 0xfc100000-0xfc1fffff]
[    1.717821] pci 0000:00:18.4:   bridge window [mem 0xe6800000-0xe68fffff 64bit pref]
[    1.717878] pci 0000:00:18.5: PCI bridge to [bus 20]
[    1.717910] pci 0000:00:18.5:   bridge window [mem 0xfbd00000-0xfbdfffff]
[    1.717932] pci 0000:00:18.5:   bridge window [mem 0xe6400000-0xe64fffff 64bit pref]
[    1.717988] pci 0000:00:18.6: PCI bridge to [bus 21]
[    1.718020] pci 0000:00:18.6:   bridge window [mem 0xfb900000-0xfb9fffff]
[    1.718042] pci 0000:00:18.6:   bridge window [mem 0xe6000000-0xe60fffff 64bit pref]
[    1.718098] pci 0000:00:18.7: PCI bridge to [bus 22]
[    1.718130] pci 0000:00:18.7:   bridge window [mem 0xfb500000-0xfb5fffff]
[    1.718152] pci 0000:00:18.7:   bridge window [mem 0xe5c00000-0xe5cfffff 64bit pref]
[    1.718209] pci_bus 0000:00: resource 4 [mem 0x000a0000-0x000bffff window]
[    1.718211] pci_bus 0000:00: resource 5 [mem 0x000d0000-0x000d3fff window]
[    1.718212] pci_bus 0000:00: resource 6 [mem 0x000d4000-0x000d7fff window]
[    1.718212] pci_bus 0000:00: resource 7 [mem 0x000d8000-0x000dbfff window]
[    1.718213] pci_bus 0000:00: resource 8 [mem 0xc0000000-0xfebfffff window]
[    1.718214] pci_bus 0000:00: resource 9 [io  0x0000-0x0cf7 window]
[    1.718216] pci_bus 0000:00: resource 10 [io  0x0d00-0xfeff window]
[    1.718218] pci_bus 0000:02: resource 0 [io  0x2000-0x3fff]
[    1.718219] pci_bus 0000:02: resource 1 [mem 0xfd500000-0xfdffffff]
[    1.718220] pci_bus 0000:02: resource 2 [mem 0xe7b00000-0xe7ffffff 64bit pref]
[    1.718221] pci_bus 0000:02: resource 4 [mem 0x000a0000-0x000bffff window]
[    1.718222] pci_bus 0000:02: resource 5 [mem 0x000d0000-0x000d3fff window]
[    1.718222] pci_bus 0000:02: resource 6 [mem 0x000d4000-0x000d7fff window]
[    1.718223] pci_bus 0000:02: resource 7 [mem 0x000d8000-0x000dbfff window]
[    1.718224] pci_bus 0000:02: resource 8 [mem 0xc0000000-0xfebfffff window]
[    1.718225] pci_bus 0000:02: resource 9 [io  0x0000-0x0cf7 window]
[    1.718226] pci_bus 0000:02: resource 10 [io  0x0d00-0xfeff window]
[    1.718227] pci_bus 0000:03: resource 1 [mem 0xfd400000-0xfd4fffff]
[    1.718228] pci_bus 0000:03: resource 2 [mem 0xc0000000-0xc01fffff 64bit pref]
[    1.718229] pci_bus 0000:04: resource 0 [io  0x7000-0x7fff]
[    1.718230] pci_bus 0000:04: resource 1 [mem 0xfd000000-0xfd0fffff]
[    1.718231] pci_bus 0000:04: resource 2 [mem 0xe7700000-0xe77fffff 64bit pref]
[    1.718232] pci_bus 0000:05: resource 0 [io  0xb000-0xbfff]
[    1.718232] pci_bus 0000:05: resource 1 [mem 0xfcc00000-0xfccfffff]
[    1.718233] pci_bus 0000:05: resource 2 [mem 0xe7300000-0xe73fffff 64bit pref]
[    1.718235] pci_bus 0000:06: resource 1 [mem 0xfc800000-0xfc8fffff]
[    1.718235] pci_bus 0000:06: resource 2 [mem 0xe6f00000-0xe6ffffff 64bit pref]
[    1.718237] pci_bus 0000:07: resource 1 [mem 0xfc400000-0xfc4fffff]
[    1.718237] pci_bus 0000:07: resource 2 [mem 0xe6b00000-0xe6bfffff 64bit pref]
[    1.718239] pci_bus 0000:08: resource 1 [mem 0xfc000000-0xfc0fffff]
[    1.718239] pci_bus 0000:08: resource 2 [mem 0xe6700000-0xe67fffff 64bit pref]
[    1.718241] pci_bus 0000:09: resource 1 [mem 0xfbc00000-0xfbcfffff]
[    1.718241] pci_bus 0000:09: resource 2 [mem 0xe6300000-0xe63fffff 64bit pref]
[    1.718243] pci_bus 0000:0a: resource 1 [mem 0xfb800000-0xfb8fffff]
[    1.718243] pci_bus 0000:0a: resource 2 [mem 0xe5f00000-0xe5ffffff 64bit pref]
[    1.718256] pci_bus 0000:0b: resource 0 [io  0x4000-0x4fff]
[    1.718257] pci_bus 0000:0b: resource 1 [mem 0xfd300000-0xfd3fffff]
[    1.718258] pci_bus 0000:0b: resource 2 [mem 0xe7a00000-0xe7afffff 64bit pref]
[    1.718259] pci_bus 0000:0c: resource 0 [io  0x8000-0x8fff]
[    1.718260] pci_bus 0000:0c: resource 1 [mem 0xfcf00000-0xfcffffff]
[    1.718265] pci_bus 0000:0c: resource 2 [mem 0xe7600000-0xe76fffff 64bit pref]
[    1.718267] pci_bus 0000:0d: resource 0 [io  0xc000-0xcfff]
[    1.718268] pci_bus 0000:0d: resource 1 [mem 0xfcb00000-0xfcbfffff]
[    1.718270] pci_bus 0000:0d: resource 2 [mem 0xe7200000-0xe72fffff 64bit pref]
[    1.718272] pci_bus 0000:0e: resource 1 [mem 0xfc700000-0xfc7fffff]
[    1.718273] pci_bus 0000:0e: resource 2 [mem 0xe6e00000-0xe6efffff 64bit pref]
[    1.718274] pci_bus 0000:0f: resource 1 [mem 0xfc300000-0xfc3fffff]
[    1.718275] pci_bus 0000:0f: resource 2 [mem 0xe6a00000-0xe6afffff 64bit pref]
[    1.718277] pci_bus 0000:10: resource 1 [mem 0xfbf00000-0xfbffffff]
[    1.718278] pci_bus 0000:10: resource 2 [mem 0xe6600000-0xe66fffff 64bit pref]
[    1.718280] pci_bus 0000:11: resource 1 [mem 0xfbb00000-0xfbbfffff]
[    1.718281] pci_bus 0000:11: resource 2 [mem 0xe6200000-0xe62fffff 64bit pref]
[    1.718282] pci_bus 0000:12: resource 1 [mem 0xfb700000-0xfb7fffff]
[    1.718283] pci_bus 0000:12: resource 2 [mem 0xe5e00000-0xe5efffff 64bit pref]
[    1.718284] pci_bus 0000:13: resource 0 [io  0x5000-0x5fff]
[    1.718285] pci_bus 0000:13: resource 1 [mem 0xfd200000-0xfd2fffff]
[    1.718286] pci_bus 0000:13: resource 2 [mem 0xe7900000-0xe79fffff 64bit pref]
[    1.718288] pci_bus 0000:14: resource 0 [io  0x9000-0x9fff]
[    1.718289] pci_bus 0000:14: resource 1 [mem 0xfce00000-0xfcefffff]
[    1.718290] pci_bus 0000:14: resource 2 [mem 0xe7500000-0xe75fffff 64bit pref]
[    1.718291] pci_bus 0000:15: resource 0 [io  0xd000-0xdfff]
[    1.718292] pci_bus 0000:15: resource 1 [mem 0xfca00000-0xfcafffff]
[    1.718293] pci_bus 0000:15: resource 2 [mem 0xe7100000-0xe71fffff 64bit pref]
[    1.718295] pci_bus 0000:16: resource 1 [mem 0xfc600000-0xfc6fffff]
[    1.718296] pci_bus 0000:16: resource 2 [mem 0xe6d00000-0xe6dfffff 64bit pref]
[    1.718298] pci_bus 0000:17: resource 1 [mem 0xfc200000-0xfc2fffff]
[    1.718299] pci_bus 0000:17: resource 2 [mem 0xe6900000-0xe69fffff 64bit pref]
[    1.718301] pci_bus 0000:18: resource 1 [mem 0xfbe00000-0xfbefffff]
[    1.718302] pci_bus 0000:18: resource 2 [mem 0xe6500000-0xe65fffff 64bit pref]
[    1.718303] pci_bus 0000:19: resource 1 [mem 0xfba00000-0xfbafffff]
[    1.718304] pci_bus 0000:19: resource 2 [mem 0xe6100000-0xe61fffff 64bit pref]
[    1.718306] pci_bus 0000:1a: resource 1 [mem 0xfb600000-0xfb6fffff]
[    1.718307] pci_bus 0000:1a: resource 2 [mem 0xe5d00000-0xe5dfffff 64bit pref]
[    1.718308] pci_bus 0000:1b: resource 0 [io  0x6000-0x6fff]
[    1.718309] pci_bus 0000:1b: resource 1 [mem 0xfd100000-0xfd1fffff]
[    1.718310] pci_bus 0000:1b: resource 2 [mem 0xe7800000-0xe78fffff 64bit pref]
[    1.718311] pci_bus 0000:1c: resource 0 [io  0xa000-0xafff]
[    1.718312] pci_bus 0000:1c: resource 1 [mem 0xfcd00000-0xfcdfffff]
[    1.718313] pci_bus 0000:1c: resource 2 [mem 0xe7400000-0xe74fffff 64bit pref]
[    1.718315] pci_bus 0000:1d: resource 0 [io  0xe000-0xefff]
[    1.718316] pci_bus 0000:1d: resource 1 [mem 0xfc900000-0xfc9fffff]
[    1.718317] pci_bus 0000:1d: resource 2 [mem 0xe7000000-0xe70fffff 64bit pref]
[    1.718318] pci_bus 0000:1e: resource 1 [mem 0xfc500000-0xfc5fffff]
[    1.718319] pci_bus 0000:1e: resource 2 [mem 0xe6c00000-0xe6cfffff 64bit pref]
[    1.718321] pci_bus 0000:1f: resource 1 [mem 0xfc100000-0xfc1fffff]
[    1.718322] pci_bus 0000:1f: resource 2 [mem 0xe6800000-0xe68fffff 64bit pref]
[    1.718323] pci_bus 0000:20: resource 1 [mem 0xfbd00000-0xfbdfffff]
[    1.718325] pci_bus 0000:20: resource 2 [mem 0xe6400000-0xe64fffff 64bit pref]
[    1.718326] pci_bus 0000:21: resource 1 [mem 0xfb900000-0xfb9fffff]
[    1.718327] pci_bus 0000:21: resource 2 [mem 0xe6000000-0xe60fffff 64bit pref]
[    1.718329] pci_bus 0000:22: resource 1 [mem 0xfb500000-0xfb5fffff]
[    1.718330] pci_bus 0000:22: resource 2 [mem 0xe5c00000-0xe5cfffff 64bit pref]
[    1.718679] NET: Registered protocol family 2
[    1.721282] IP idents hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    1.732923] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    1.734696] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    1.737477] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
[    1.737517] TCP: Hash tables configured (established 32768 bind 32768)
[    1.740203] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.740552] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.742202] NET: Registered protocol family 1
[    1.742210] NET: Registered protocol family 44
[    1.742219] pci 0000:00:00.0: Limiting direct PCI/PCI transfers
[    1.742395] pci 0000:00:0f.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    1.743992] pci 0000:02:01.0: CLS mismatch (32 != 64), using 64 bytes
[    1.746111] Trying to unpack rootfs image as initramfs...
[    3.843125] Freeing initrd memory: 65576K
[    3.843206] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    3.843208] software IO TLB: mapped [mem 0xbbed0000-0xbfed0000] (64MB)
[    3.843537] check: Scanning for low memory corruption every 60 seconds
[    3.846708] Initialise system trusted keyrings
[    3.846810] Key type blacklist registered
[    3.847022] workingset: timestamp_bits=36 max_order=20 bucket_order=0
[    3.851647] zbud: loaded
[    3.853171] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    3.854057] fuse: init (API version 7.31)
[    3.854183] *** VALIDATE fuse ***
[    3.854186] *** VALIDATE fuse ***
[    3.854904] Platform Keyring initialized
[    3.860795] Key type asymmetric registered
[    3.860798] Asymmetric key parser 'x509' registered
[    3.860886] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 244)
[    3.861303] io scheduler mq-deadline registered
[    3.862819] pcieport 0000:00:15.0: PME: Signaling with IRQ 24
[    3.862970] pcieport 0000:00:15.0: pciehp: Slot #160 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.865587] pcieport 0000:00:15.1: PME: Signaling with IRQ 25
[    3.865726] pcieport 0000:00:15.1: pciehp: Slot #161 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.867987] pcieport 0000:00:15.2: PME: Signaling with IRQ 26
[    3.868149] pcieport 0000:00:15.2: pciehp: Slot #162 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.869892] pcieport 0000:00:15.3: PME: Signaling with IRQ 27
[    3.870072] pcieport 0000:00:15.3: pciehp: Slot #163 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.871593] pcieport 0000:00:15.4: PME: Signaling with IRQ 28
[    3.871728] pcieport 0000:00:15.4: pciehp: Slot #164 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.873507] pcieport 0000:00:15.5: PME: Signaling with IRQ 29
[    3.874037] pcieport 0000:00:15.5: pciehp: Slot #165 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.875982] pcieport 0000:00:15.6: PME: Signaling with IRQ 30
[    3.876248] pcieport 0000:00:15.6: pciehp: Slot #166 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.878095] pcieport 0000:00:15.7: PME: Signaling with IRQ 31
[    3.878215] pcieport 0000:00:15.7: pciehp: Slot #167 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.880809] pcieport 0000:00:16.0: PME: Signaling with IRQ 32
[    3.881066] pcieport 0000:00:16.0: pciehp: Slot #192 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.882616] pcieport 0000:00:16.1: PME: Signaling with IRQ 33
[    3.882793] pcieport 0000:00:16.1: pciehp: Slot #193 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.884675] pcieport 0000:00:16.2: PME: Signaling with IRQ 34
[    3.885010] pcieport 0000:00:16.2: pciehp: Slot #194 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.886895] pcieport 0000:00:16.3: PME: Signaling with IRQ 35
[    3.887023] pcieport 0000:00:16.3: pciehp: Slot #195 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.888730] pcieport 0000:00:16.4: PME: Signaling with IRQ 36
[    3.888849] pcieport 0000:00:16.4: pciehp: Slot #196 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.890590] pcieport 0000:00:16.5: PME: Signaling with IRQ 37
[    3.890696] pcieport 0000:00:16.5: pciehp: Slot #197 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.892230] pcieport 0000:00:16.6: PME: Signaling with IRQ 38
[    3.892372] pcieport 0000:00:16.6: pciehp: Slot #198 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.894215] pcieport 0000:00:16.7: PME: Signaling with IRQ 39
[    3.894336] pcieport 0000:00:16.7: pciehp: Slot #199 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.896011] pcieport 0000:00:17.0: PME: Signaling with IRQ 40
[    3.896111] pcieport 0000:00:17.0: pciehp: Slot #224 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.897788] pcieport 0000:00:17.1: PME: Signaling with IRQ 41
[    3.897928] pcieport 0000:00:17.1: pciehp: Slot #225 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.899562] pcieport 0000:00:17.2: PME: Signaling with IRQ 42
[    3.899676] pcieport 0000:00:17.2: pciehp: Slot #226 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.901252] pcieport 0000:00:17.3: PME: Signaling with IRQ 43
[    3.901373] pcieport 0000:00:17.3: pciehp: Slot #227 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.902892] pcieport 0000:00:17.4: PME: Signaling with IRQ 44
[    3.903032] pcieport 0000:00:17.4: pciehp: Slot #228 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.904283] pcieport 0000:00:17.5: PME: Signaling with IRQ 45
[    3.904561] pcieport 0000:00:17.5: pciehp: Slot #229 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.905933] pcieport 0000:00:17.6: PME: Signaling with IRQ 46
[    3.906028] pcieport 0000:00:17.6: pciehp: Slot #230 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.907983] pcieport 0000:00:17.7: PME: Signaling with IRQ 47
[    3.908129] pcieport 0000:00:17.7: pciehp: Slot #231 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.909747] pcieport 0000:00:18.0: PME: Signaling with IRQ 48
[    3.909849] pcieport 0000:00:18.0: pciehp: Slot #256 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.911508] pcieport 0000:00:18.1: PME: Signaling with IRQ 49
[    3.911623] pcieport 0000:00:18.1: pciehp: Slot #257 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.913325] pcieport 0000:00:18.2: PME: Signaling with IRQ 50
[    3.913555] pcieport 0000:00:18.2: pciehp: Slot #258 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.915242] pcieport 0000:00:18.3: PME: Signaling with IRQ 51
[    3.915358] pcieport 0000:00:18.3: pciehp: Slot #259 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.917307] pcieport 0000:00:18.4: PME: Signaling with IRQ 52
[    3.917420] pcieport 0000:00:18.4: pciehp: Slot #260 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.918794] pcieport 0000:00:18.5: PME: Signaling with IRQ 53
[    3.918934] pcieport 0000:00:18.5: pciehp: Slot #261 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.920340] pcieport 0000:00:18.6: PME: Signaling with IRQ 54
[    3.920460] pcieport 0000:00:18.6: pciehp: Slot #262 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.922045] pcieport 0000:00:18.7: PME: Signaling with IRQ 55
[    3.922157] pcieport 0000:00:18.7: pciehp: Slot #263 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ LLActRep+
[    3.923098] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    3.923961] ACPI: AC Adapter [ACAD] (on-line)
[    3.924202] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
[    3.924423] ACPI: Power Button [PWRF]
[    3.926268] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    3.930065] Linux agpgart interface v0.103
[    3.930216] agpgart-intel 0000:00:00.0: Intel 440BX Chipset
[    3.932119] agpgart-intel 0000:00:00.0: AGP aperture is 256M @ 0x0
[    4.124651] loop: module loaded
[    4.125644] ata_piix 0000:00:07.1: version 2.13
[    4.128025] scsi host0: ata_piix
[    4.129165] scsi host1: ata_piix
[    4.129339] ata1: PATA max UDMA/33 cmd 0x1f0 ctl 0x3f6 bmdma 0x1060 irq 14
[    4.129341] ata2: PATA max UDMA/33 cmd 0x170 ctl 0x376 bmdma 0x1068 irq 15
[    4.129551] libphy: Fixed MDIO Bus: probed
[    4.129552] tun: Universal TUN/TAP device driver, 1.6
[    4.130149] PPP generic driver version 2.4.2
[    4.130252] VFIO - User Level meta-driver version: 0.3
[    4.130808] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    4.130815] ehci-pci: EHCI PCI platform driver
[    4.131502] ehci-pci 0000:02:03.0: EHCI Host Controller
[    4.131509] ehci-pci 0000:02:03.0: new USB bus registered, assigned bus number 1
[    4.132168] ehci-pci 0000:02:03.0: cache line size of 64 is not supported
[    4.132199] ehci-pci 0000:02:03.0: irq 17, io mem 0xfd5ef000
[    4.148704] ehci-pci 0000:02:03.0: USB 2.0 started, EHCI 1.00
[    4.148965] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
[    4.148968] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    4.148970] usb usb1: Product: EHCI Host Controller
[    4.148972] usb usb1: Manufacturer: Linux 5.4.0-90-generic ehci_hcd
[    4.148974] usb usb1: SerialNumber: 0000:02:03.0
[    4.149401] hub 1-0:1.0: USB hub found
[    4.149414] hub 1-0:1.0: 6 ports detected
[    4.149987] ehci-platform: EHCI generic platform driver
[    4.150007] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    4.150015] ohci-pci: OHCI PCI platform driver
[    4.150035] ohci-platform: OHCI generic platform driver
[    4.150114] uhci_hcd: USB Universal Host Controller Interface driver
[    4.151193] uhci_hcd 0000:02:00.0: UHCI Host Controller
[    4.151201] uhci_hcd 0000:02:00.0: new USB bus registered, assigned bus number 2
[    4.151260] uhci_hcd 0000:02:00.0: detected 2 ports
[    4.151888] uhci_hcd 0000:02:00.0: irq 18, io base 0x00002080
[    4.152051] usb usb2: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 5.04
[    4.152052] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    4.152054] usb usb2: Product: UHCI Host Controller
[    4.152055] usb usb2: Manufacturer: Linux 5.4.0-90-generic uhci_hcd
[    4.152056] usb usb2: SerialNumber: 0000:02:00.0
[    4.152242] hub 2-0:1.0: USB hub found
[    4.152248] hub 2-0:1.0: 2 ports detected
[    4.153878] xhci_hcd 0000:03:00.0: xHCI Host Controller
[    4.153887] xhci_hcd 0000:03:00.0: new USB bus registered, assigned bus number 3
[    4.154561] xhci_hcd 0000:03:00.0: hcc params 0x0388f081 hci version 0x100 quirks 0x0000000000000010
[    4.154615] xhci_hcd 0000:03:00.0: cache line size of 64 is not supported
[    4.156826] xhci_hcd 0000:03:00.0: xHCI Host Controller
[    4.156833] xhci_hcd 0000:03:00.0: new USB bus registered, assigned bus number 4
[    4.156838] xhci_hcd 0000:03:00.0: Host supports USB 3.0 SuperSpeed
[    4.156975] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
[    4.156978] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    4.156980] usb usb3: Product: xHCI Host Controller
[    4.156981] usb usb3: Manufacturer: Linux 5.4.0-90-generic xhci-hcd
[    4.156982] usb usb3: SerialNumber: 0000:03:00.0
[    4.157183] hub 3-0:1.0: USB hub found
[    4.157220] hub 3-0:1.0: 4 ports detected
[    4.157758] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
[    4.157783] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.04
[    4.157784] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    4.157785] usb usb4: Product: xHCI Host Controller
[    4.157786] usb usb4: Manufacturer: Linux 5.4.0-90-generic xhci-hcd
[    4.157787] usb usb4: SerialNumber: 0000:03:00.0
[    4.157939] hub 4-0:1.0: USB hub found
[    4.157974] hub 4-0:1.0: 4 ports detected
[    4.158366] i8042: PNP: PS/2 Controller [PNP0303:KBC,PNP0f13:MOUS] at 0x60,0x64 irq 1,12
[    4.159459] serio: i8042 KBD port at 0x60,0x64 irq 1
[    4.159485] serio: i8042 AUX port at 0x60,0x64 irq 12
[    4.159883] mousedev: PS/2 mouse device common for all mice
[    4.181223] rtc_cmos 00:01: registered as rtc0
[    4.181238] rtc_cmos 00:01: alarms up to one month, y3k, 114 bytes nvram, hpet irqs
[    4.181247] i2c /dev entries driver
[    4.181399] device-mapper: uevent: version 1.0.3
[    4.181498] device-mapper: ioctl: 4.41.0-ioctl (2019-09-16) initialised: dm-devel@redhat.com
[    4.181521] platform eisa.0: Probing EISA bus 0
[    4.181522] platform eisa.0: EISA: Cannot allocate resource for mainboard
[    4.181524] platform eisa.0: Cannot allocate resource for EISA slot 1
[    4.181524] platform eisa.0: Cannot allocate resource for EISA slot 2
[    4.181525] platform eisa.0: Cannot allocate resource for EISA slot 3
[    4.181526] platform eisa.0: Cannot allocate resource for EISA slot 4
[    4.181527] platform eisa.0: Cannot allocate resource for EISA slot 5
[    4.181528] platform eisa.0: Cannot allocate resource for EISA slot 6
[    4.181528] platform eisa.0: Cannot allocate resource for EISA slot 7
[    4.181529] platform eisa.0: Cannot allocate resource for EISA slot 8
[    4.181530] platform eisa.0: EISA: Detected 0 cards
[    4.181961] ledtrig-cpu: registered to indicate activity on CPUs
[    4.182284] drop_monitor: Initializing network drop monitor service
[    4.183201] NET: Registered protocol family 10
[    4.184111] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input1
[    4.197631] Segment Routing with IPv6
[    4.197674] NET: Registered protocol family 17
[    4.197954] Key type dns_resolver registered
[    4.198397] RAS: Correctable Errors collector initialized.
[    4.198406] IPI shorthand broadcast: enabled
[    4.198416] sched_clock: Marking stable (4196356960, 1787551)->(4198277955, -133444)
[    4.198926] registered taskstats version 1
[    4.198940] Loading compiled-in X.509 certificates
[    4.200255] Loaded X.509 cert 'Build time autogenerated kernel key: f80580535d43d6e70af8167fd0c3c4e0597192a3'
[    4.201106] Loaded X.509 cert 'Canonical Ltd. Live Patch Signing: 14df34d1a87cf37625abec039ef2bf521249b969'
[    4.201920] Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing: 88f752e560a1e0737e31163a466ad7b70a850c19'
[    4.202201] zswap: loaded using pool lzo/zbud
[    4.203083] Key type ._fscrypt registered
[    4.203084] Key type .fscrypt registered
[    4.210275] Key type big_key registered
[    4.213186] Key type encrypted registered
[    4.213190] AppArmor: AppArmor sha1 policy hashing enabled
[    4.213197] ima: No TPM chip found, activating TPM-bypass!
[    4.213210] ima: Allocated hash algorithm: sha1
[    4.213217] ima: No architecture policies found
[    4.213226] evm: Initialising EVM extended attributes:
[    4.213226] evm: security.selinux
[    4.213227] evm: security.SMACK64
[    4.213227] evm: security.SMACK64EXEC
[    4.213228] evm: security.SMACK64TRANSMUTE
[    4.213228] evm: security.SMACK64MMAP
[    4.213228] evm: security.apparmor
[    4.213228] evm: security.ima
[    4.213229] evm: security.capability
[    4.213229] evm: HMAC attrs: 0x1
[    4.216015] PM:   Magic number: 13:625:629
[    4.216138] pci_bus 0000:0b: hash matches
[    4.216169] acpi PNP0C80:18b: hash matches
[    4.216546] rtc_cmos 00:01: setting system clock to 2021-11-26T10:39:00 UTC (1637923140)
[    4.315011] Freeing unused decrypted memory: 2040K
[    4.315787] Freeing unused kernel image memory: 2716K
[    4.315800] Write protecting the kernel read-only data: 22528k
[    4.316750] Freeing unused kernel image memory: 2008K
[    4.317131] Freeing unused kernel image memory: 1156K
[    4.328257] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    4.328263] Run /init as init process
[    4.423733] usb 3-1: new full-speed USB device number 2 using xhci_hcd
[    4.573143] usb 3-1: New USB device found, idVendor=0e0f, idProduct=0003, bcdDevice= 1.03
[    4.573146] usb 3-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    4.573147] usb 3-1: Product: VMware Virtual USB Mouse
[    4.573149] usb 3-1: Manufacturer: VMware
[    4.579516] hidraw: raw HID events driver (C) Jiri Kosina
[    4.583271] usbcore: registered new interface driver usbhid
[    4.583272] usbhid: USB HID core driver
[    4.586202] input: VMware VMware Virtual USB Mouse as /devices/pci0000:00/0000:00:15.0/0000:03:00.0/usb3/3-1/3-1:1.0/0003:0E0F:0003.0001/input/input3
[    4.586518] hid-generic 0003:0E0F:0003.0001: input,hidraw0: USB HID v1.10 Mouse [VMware VMware Virtual USB Mouse] on usb-0000:03:00.0-1/input0
[    4.855819] tsc: Refined TSC clocksource calibration: 2195.871 MHz
[    4.855856] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x1fa6f63757a, max_idle_ns: 440795221982 ns
[    4.855900] clocksource: Switched to clocksource tsc
[    4.859044] piix4_smbus 0000:00:07.3: SMBus Host Controller not enabled!
[    4.862151] Fusion MPT base driver 3.04.20
[    4.862152] Copyright (c) 1999-2008 LSI Corporation
[    4.865002] Fusion MPT SPI Host driver 3.04.20
[    4.865672] e1000: Intel(R) PRO/1000 Network Driver - version 7.3.21-k8-NAPI
[    4.865673] e1000: Copyright (c) 1999-2006 Intel Corporation.
[    4.870685] mptbase: ioc0: Initiating bringup
[    4.880746] ahci 0000:02:05.0: version 3.0
[    4.884588] ahci 0000:02:05.0: AHCI 0001.0300 32 slots 30 ports 6 Gbps 0x3fffffff impl SATA mode
[    4.884591] ahci 0000:02:05.0: flags: 64bit ncq clo only 
[    4.900117] input: VirtualPS/2 VMware VMMouse as /devices/platform/i8042/serio1/input/input5
[    4.900757] input: VirtualPS/2 VMware VMMouse as /devices/platform/i8042/serio1/input/input4
[    4.976180] ioc0: LSI53C1030 B0: Capabilities={Initiator}
[    4.984105] scsi host2: ahci
[    4.997512] scsi host3: ahci
[    5.008290] scsi host4: ahci
[    5.009991] scsi host5: ahci
[    5.010683] scsi host6: ahci
[    5.011412] scsi host7: ahci
[    5.012613] scsi host8: ahci
[    5.013659] scsi host9: ahci
[    5.014591] scsi host10: ahci
[    5.015530] scsi host11: ahci
[    5.016403] scsi host12: ahci
[    5.017411] scsi host13: ahci
[    5.018281] scsi host14: ahci
[    5.019022] scsi host15: ahci
[    5.020016] scsi host16: ahci
[    5.020666] scsi host17: ahci
[    5.021403] scsi host18: ahci
[    5.021989] scsi host19: ahci
[    5.022856] scsi host20: ahci
[    5.023742] scsi host21: ahci
[    5.024521] scsi host22: ahci
[    5.025314] scsi host23: ahci
[    5.026040] scsi host24: ahci
[    5.026938] scsi host25: ahci
[    5.027503] scsi host26: ahci
[    5.028074] scsi host27: ahci
[    5.028895] scsi host28: ahci
[    5.029704] scsi host29: ahci
[    5.030703] scsi host30: ahci
[    5.031769] scsi host31: ahci
[    5.032529] ata3: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee100 irq 59
[    5.032533] ata4: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee180 irq 59
[    5.032534] ata5: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee200 irq 59
[    5.032535] ata6: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee280 irq 59
[    5.032536] ata7: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee300 irq 59
[    5.032537] ata8: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee380 irq 59
[    5.032539] ata9: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee400 irq 59
[    5.032540] ata10: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee480 irq 59
[    5.032541] ata11: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee500 irq 59
[    5.032542] ata12: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee580 irq 59
[    5.032543] ata13: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee600 irq 59
[    5.032544] ata14: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee680 irq 59
[    5.032545] ata15: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee700 irq 59
[    5.032546] ata16: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee780 irq 59
[    5.032547] ata17: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee800 irq 59
[    5.032548] ata18: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee880 irq 59
[    5.032549] ata19: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee900 irq 59
[    5.032549] ata20: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee980 irq 59
[    5.032550] ata21: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eea00 irq 59
[    5.032551] ata22: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eea80 irq 59
[    5.032552] ata23: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eeb00 irq 59
[    5.032553] ata24: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eeb80 irq 59
[    5.032554] ata25: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eec00 irq 59
[    5.032555] ata26: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eec80 irq 59
[    5.032556] ata27: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eed00 irq 59
[    5.032556] ata28: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eed80 irq 59
[    5.032557] ata29: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eee00 irq 59
[    5.032558] ata30: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eee80 irq 59
[    5.032559] ata31: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eef00 irq 59
[    5.032560] ata32: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eef80 irq 59
[    5.219790] scsi host32: ioc0: LSI53C1030 B0, FwRev=01032920h, Ports=1, MaxQ=128, IRQ=17
[    5.320415] e1000 0000:02:01.0 eth0: (PCI:66MHz:32-bit) 00:0c:29:1d:83:b8
[    5.320424] e1000 0000:02:01.0 eth0: Intel(R) PRO/1000 Network Connection
[    5.323073] e1000 0000:02:01.0 ens33: renamed from eth0
[    5.345874] ata5: SATA link down (SStatus 0 SControl 300)
[    5.345950] ata4: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    5.346024] ata3: SATA link down (SStatus 0 SControl 300)
[    5.346096] ata6: SATA link down (SStatus 0 SControl 300)
[    5.346152] ata4.00: ATAPI: VMware Virtual SATA CDRW Drive, 00000001, max UDMA/33
[    5.346408] ata4.00: configured for UDMA/33
[    5.347063] scsi 3:0:0:0: CD-ROM            NECVMWar VMware SATA CD01 1.00 PQ: 0 ANSI: 5
[    5.351872] ata11: SATA link down (SStatus 0 SControl 300)
[    5.351917] ata10: SATA link down (SStatus 0 SControl 300)
[    5.351927] ata12: SATA link down (SStatus 0 SControl 300)
[    5.351951] ata7: SATA link down (SStatus 0 SControl 300)
[    5.351961] ata13: SATA link down (SStatus 0 SControl 300)
[    5.352031] ata14: SATA link down (SStatus 0 SControl 300)
[    5.352043] ata8: SATA link down (SStatus 0 SControl 300)
[    5.352065] ata9: SATA link down (SStatus 0 SControl 300)
[    5.352085] ata15: SATA link down (SStatus 0 SControl 300)
[    5.357781] ata22: SATA link down (SStatus 0 SControl 300)
[    5.357839] ata24: SATA link down (SStatus 0 SControl 300)
[    5.357854] ata30: SATA link down (SStatus 0 SControl 300)
[    5.357888] ata23: SATA link down (SStatus 0 SControl 300)
[    5.357901] ata17: SATA link down (SStatus 0 SControl 300)
[    5.357932] ata29: SATA link down (SStatus 0 SControl 300)
[    5.357944] ata18: SATA link down (SStatus 0 SControl 300)
[    5.357974] ata25: SATA link down (SStatus 0 SControl 300)
[    5.357985] ata19: SATA link down (SStatus 0 SControl 300)
[    5.358016] ata26: SATA link down (SStatus 0 SControl 300)
[    5.358026] ata31: SATA link down (SStatus 0 SControl 300)
[    5.358057] ata27: SATA link down (SStatus 0 SControl 300)
[    5.358067] ata20: SATA link down (SStatus 0 SControl 300)
[    5.358097] ata28: SATA link down (SStatus 0 SControl 300)
[    5.358108] ata21: SATA link down (SStatus 0 SControl 300)
[    5.358142] ata32: SATA link down (SStatus 0 SControl 300)
[    5.358153] ata16: SATA link down (SStatus 0 SControl 300)
[    5.378722] sr 3:0:0:0: [sr0] scsi3-mmc drive: 1x/1x writer dvd-ram cd/rw xa/form2 cdda tray
[    5.378726] cdrom: Uniform CD-ROM driver Revision: 3.20
[    5.390799] scsi 32:0:0:0: Direct-Access     VMware,  VMware Virtual S 1.0  PQ: 0 ANSI: 2
[    5.405735] scsi target32:0:0: Beginning Domain Validation
[    5.409168] scsi target32:0:0: Domain Validation skipping write tests
[    5.409170] scsi target32:0:0: Ending Domain Validation
[    5.409315] scsi target32:0:0: FAST-40 WIDE SCSI 80.0 MB/s ST (25 ns, offset 127)
[    5.423856] sr 3:0:0:0: Attached scsi CD-ROM sr0
[    5.424471] sr 3:0:0:0: Attached scsi generic sg0 type 5
[    5.427431] sd 32:0:0:0: [sda] 125829120 512-byte logical blocks: (64.4 GB/60.0 GiB)
[    5.427507] sd 32:0:0:0: [sda] Write Protect is off
[    5.427509] sd 32:0:0:0: [sda] Mode Sense: 61 00 00 00
[    5.427953] sd 32:0:0:0: [sda] Cache data unavailable
[    5.427955] sd 32:0:0:0: [sda] Assuming drive cache: write through
[    5.428244] sd 32:0:0:0: Attached scsi generic sg1 type 0
[    5.453086]  sda: sda1 sda2 < sda5 >
[    5.478924] sd 32:0:0:0: [sda] Attached SCSI disk
[    5.746606] EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
[    6.191383] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    6.191412] systemd[1]: Detected virtualization vmware.
[    6.191416] systemd[1]: Detected architecture x86-64.
[    6.220481] systemd[1]: Set hostname to <min>.
[    6.570940] systemd[1]: Created slice User and Session Slice.
[    6.571156] systemd[1]: Reached target Remote File Systems.
[    6.571233] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    6.571508] systemd[1]: Created slice System Slice.
[    6.571594] systemd[1]: Listening on udev Kernel Socket.
[    6.571659] systemd[1]: Listening on fsck to fsckd communication Socket.
[    6.599921] EXT4-fs (sda1): re-mounted. Opts: errors=remount-ro
[    6.653102] lp: driver loaded but no devices found
[    6.682597] ppdev: user-space parallel port driver
[    6.807944] Adding 1459804k swap on /swapfile.  Priority:-2 extents:5 across:1492572k FS
[    6.825377] [drm] DMA map mode: Caching DMA mappings.
[    6.825528] [drm] Capabilities:
[    6.825528] [drm]   Rect copy.
[    6.825529] [drm]   Cursor.
[    6.825529] [drm]   Cursor bypass.
[    6.825529] [drm]   Cursor bypass 2.
[    6.825530] [drm]   8bit emulation.
[    6.825530] [drm]   Alpha cursor.
[    6.825530] [drm]   3D.
[    6.825531] [drm]   Extended Fifo.
[    6.825531] [drm]   Multimon.
[    6.825531] [drm]   Pitchlock.
[    6.825531] [drm]   Irq mask.
[    6.825532] [drm]   Display Topology.
[    6.825532] [drm]   GMR.
[    6.825532] [drm]   Traces.
[    6.825533] [drm]   GMR2.
[    6.825533] [drm]   Screen Object 2.
[    6.825533] [drm]   Command Buffers.
[    6.825534] [drm]   Command Buffers 2.
[    6.825534] [drm]   Guest Backed Resources.
[    6.825535] [drm]   DX Features.
[    6.825535] [drm]   HP Command Queue.
[    6.825535] [drm] Capabilities2:
[    6.825535] [drm]   Grow oTable.
[    6.825536] [drm]   IntraSurface copy.
[    6.825537] [drm] Max GMR ids is 64
[    6.825537] [drm] Max number of GMR pages is 65536
[    6.825538] [drm] Max dedicated hypervisor surface memory is 0 kiB
[    6.825538] [drm] Maximum display memory size is 262144 kiB
[    6.825539] [drm] VRAM at 0xe8000000 size is 4096 kiB
[    6.825539] [drm] MMIO at 0xfe000000 size is 256 kiB
[    6.844253] [TTM] Zone  kernel: Available graphics memory: 2000852 KiB
[    6.844255] [TTM] Initializing pool allocator
[    6.844260] [TTM] Initializing DMA pool allocator
[    6.844654] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    6.844655] [drm] No driver support for vblank timestamp query.
[    6.845201] [drm] Screen Target Display device initialized
[    6.845397] [drm] width 640
[    6.845407] [drm] height 480
[    6.845415] [drm] bpp 32
[    6.846878] [drm] Fifo max 0x00040000 min 0x00001000 cap 0x0000077f
[    6.847769] [drm] Using command buffers with DMA pool.
[    6.847926] [drm] DX: yes.
[    6.847927] [drm] Atomic: yes.
[    6.847928] [drm] SM4_1: yes.
[    6.863950] fbcon: svgadrmfb (fb0) is primary device
[    6.873684] Console: switching to colour frame buffer device 100x37
[    6.910951] [drm] Initialized vmwgfx 2.15.0 20180704 for 0000:00:0f.0 on minor 0
[    7.472580] systemd-journald[364]: Received request to flush runtime journal from PID 1
[    7.755749] audit: type=1400 audit(1637923144.031:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=539 comm="apparmor_parser"
[    7.755755] audit: type=1400 audit(1637923144.035:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=539 comm="apparmor_parser"
[    7.755757] audit: type=1400 audit(1637923144.035:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=539 comm="apparmor_parser"
[    7.755759] audit: type=1400 audit(1637923144.035:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=539 comm="apparmor_parser"
[    7.798252] audit: type=1400 audit(1637923144.079:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=545 comm="apparmor_parser"
[    7.798258] audit: type=1400 audit(1637923144.079:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=545 comm="apparmor_parser"
[    7.798260] audit: type=1400 audit(1637923144.079:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=545 comm="apparmor_parser"
[    7.819231] audit: type=1400 audit(1637923144.095:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince" pid=540 comm="apparmor_parser"
[    7.819237] audit: type=1400 audit(1637923144.095:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//sanitized_helper" pid=540 comm="apparmor_parser"
[    7.819240] audit: type=1400 audit(1637923144.095:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer" pid=540 comm="apparmor_parser"
[    8.230534] vmw_vmci 0000:00:07.7: Found VMCI PCI device at 0x11080, irq 16
[    8.230612] vmw_vmci 0000:00:07.7: Using capabilities 0xc
[    8.234651] Guest personality initialized and is active
[    8.235833] VMCI host device registered (name=vmci, major=10, minor=58)
[    8.235835] Initialized host personality
[    8.249447] NET: Registered protocol family 40
[    9.816414] e1000: ens33 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: None
[    9.823611] IPv6: ADDRCONF(NETDEV_CHANGE): ens33: link becomes ready
[   15.241182] cryptd: max_cpu_qlen set to 1000
[   15.369781] AVX2 version of gcm_enc/dec engaged.
[   15.369783] AES CTR mode by8 optimization enabled
[   15.551069] Decoding supported only on Scalable MCA processors.
[   15.614630] Decoding supported only on Scalable MCA processors.
[   34.735846] rfkill: input handler disabled



---

### 评论 #3 — abhimeda (2023-12-20T19:33:57Z)

@xiaomin0416  Is the issue still reproducible with the latest version of ROCm?  If not, can we please close it?  Thanks!

---

### 评论 #4 — nartmada (2024-01-20T02:36:28Z)

Hi @xiaomin0416, is there any update on the issue?  Do you still need this ticket to be opened?  Thanks.

---
