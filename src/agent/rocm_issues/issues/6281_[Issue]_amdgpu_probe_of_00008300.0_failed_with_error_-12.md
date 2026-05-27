# [Issue]: amdgpu: probe of 0000:83:00.0 failed with error -12

> **Issue #6281**
> **状态**: closed
> **创建时间**: 2026-05-20T08:44:39Z
> **更新时间**: 2026-05-26T05:45:44Z
> **关闭时间**: 2026-05-26T05:45:44Z
> **作者**: botbw
> **标签**: status: triage
> **URL**: https://github.com/ROCm/ROCm/issues/6281

## 标签

- **status: triage** (颜色: #585dd7)

## 负责人

- harkgill-amd

## 描述

### Problem Description

Hi, I was installing MI210 GPUs on a server (the server came with MI50 GPUs from AMD). After updating the driver, I got the following error when booting up:

```
$ sudo dmesg | grep amdgpu
[    8.798469] [drm] amdgpu kernel modesetting enabled.
[    8.802165] [drm] amdgpu version: 6.16.13
[    8.808036] amdgpu: Virtual CRAT table created for CPU
[    8.820648] amdgpu: Topology: Add CPU node
[    8.833673] amdgpu 0000:c3:00.0: enabling device (0000 -> 0003)
[    8.837907] amdgpu 0000:c3:00.0: amdgpu: initializing kernel modesetting (ALDEBARAN 0x1002:0x740F 0x1002:0x0C34 0x02).
[    8.839735] amdgpu 0000:c3:00.0: amdgpu: Fatal error during GPU init
[    8.841500] amdgpu: probe of 0000:c3:00.0 failed with error -12
[    8.852252] amdgpu 0000:83:00.0: enabling device (0000 -> 0003)
[    8.856429] amdgpu 0000:83:00.0: amdgpu: initializing kernel modesetting (ALDEBARAN 0x1002:0x740F 0x1002:0x0C34 0x02).
[    8.858251] amdgpu 0000:83:00.0: amdgpu: Fatal error during GPU init
[    8.860033] amdgpu: probe of 0000:83:00.0 failed with error -12

$ lspci | grep MI
83:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Aldebaran/MI200 [Instinct MI210] (rev 02)
c3:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Aldebaran/MI200 [Instinct MI210] (rev 02)  
```

I also tried some fixes from online search, some of which resulted in issue #6176 or simply hung during boot up.

# Detailed PCIe info
```
00-740003fffff
        *-pci:1
             description: PCI bridge
             product: Starship/Matisse Internal PCIe GPP Bridge 0 to bus[E:B]
             vendor: Advanced Micro Devices, Inc. [AMD]
             physical id: 7.1
             bus info: pci@0000:80:07.1
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: pci pm pciexpress msi ht normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:66 memory:b0400000-b04fffff
           *-generic:0 UNCLAIMED
                description: Non-Essential Instrumentation
                product: Starship/Matisse PCIe Dummy Function
                vendor: Advanced Micro Devices, Inc. [AMD]
                physical id: 0
                bus info: pci@0000:84:00.0
                version: 00
                width: 32 bits
                clock: 33MHz
--
             clock: 33MHz
             capabilities: pci pm pciexpress msi ht normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:48 ioport:d000(size=4096) ioport:56000000000(size=171798691840)
           *-pci
                description: PCI bridge
                product: Advanced Micro Devices, Inc. [AMD]
                vendor: Advanced Micro Devices, Inc. [AMD]
                physical id: 0
                bus info: pci@0000:c1:00.0
                version: 00
                width: 32 bits
                clock: 33MHz
                capabilities: pci pm pciexpress msi normal_decode bus_master cap_list
                configuration: driver=pcieport
                resources: irq:54 ioport:d000(size=4096) ioport:56000000000(size=171798691840)
              *-pci
                   description: PCI bridge
                   product: Advanced Micro Devices, Inc. [AMD/ATI]
                   vendor: Advanced Micro Devices, Inc. [AMD/ATI]
                   physical id: 0
                   bus info: pci@0000:c2:00.0
                   version: 00
                   width: 32 bits
                   clock: 33MHz
                   capabilities: pci pm pciexpress msi normal_decode bus_master cap_list
                   configuration: driver=pcieport
                   resources: irq:55 ioport:d000(size=4096) ioport:56000000000(size=171798691840)
                 *-display UNCLAIMED
                      description: Display controller
                      product: Aldebaran/MI200 [Instinct MI210]
                      vendor: Advanced Micro Devices, Inc. [AMD/ATI]
                      physical id: 0
                      bus info: pci@0000:c3:00.0
                      version: 02
                      width: 64 bits
                      clock: 33MHz
                      capabilities: pm pciexpress msi msix cap_list
                      configuration: latency=0
                      resources: iomemory:5600-55ff iomemory:5800-57ff memory:56000000000-56fffffffff memory:58000000000-580001fffff ioport:d000(size=256) memory:57000000000-57fffffffff memory:58000200000-580003fffff
```
# Server model
```
$ sudo dmidecode -t system
# dmidecode 3.5
Getting SMBIOS data from sysfs.
SMBIOS 3.2.0 present.

Handle 0x0001, DMI type 1, 27 bytes
System Information
	Manufacturer: Inventec        
	Product Name: Cetus                                
	Version:       
	Serial Number:                 
	UUID: 
	Wake-up Type: Power Switch
	SKU Number:  
	Family:  

Handle 0x0018, DMI type 12, 5 bytes
System Configuration Options
	Option 1: Jumper:Password clear. Jumper location and status:J169. GPIO active:Low. Description:Ignore the Password on BIOS Setup Utility feature.
	Option 2: Jumper:CMOS Clear. Jumper location and status:J36. GPIO active:N/A. Description:CMOS will be cleared during POST.

Handle 0x0019, DMI type 32, 20 bytes
System Boot Information
	Status: No errors detected

Handle 0x002A, DMI type 15, 73 bytes
System Event Log
	Area Length: 0 bytes
	Header Start Offset: 0x0000
	Header Length: 16 bytes
	Data Start Offset: 0x0010
	Access Method: Memory-mapped physical 32-bit address
	Access Address: 0xFF51B000
	Status: Valid, Not Full
	Change Token: 0x00001643
	Header Format: Type 1
	Supported Log Type Descriptors: 25
	Descriptor 1: Single-bit ECC memory error
	Data Format 1: Multiple-event handle
	Descriptor 2: Multi-bit ECC memory error
	Data Format 2: Multiple-event handle
	Descriptor 3: Parity memory error
	Data Format 3: None
	Descriptor 4: Bus timeout
	Data Format 4: None
	Descriptor 5: I/O channel block
	Data Format 5: None
	Descriptor 6: Software NMI
	Data Format 6: None
	Descriptor 7: POST memory resize
	Data Format 7: None
	Descriptor 8: POST error
	Data Format 8: POST results bitmap
	Descriptor 9: PCI parity error
	Data Format 9: Multiple-event handle
	Descriptor 10: PCI system error
	Data Format 10: Multiple-event handle
	Descriptor 11: CPU failure
	Data Format 11: None
	Descriptor 12: EISA failsafe timer timeout
	Data Format 12: None
	Descriptor 13: Correctable memory log disabled
	Data Format 13: None
	Descriptor 14: Logging disabled
	Data Format 14: None
	Descriptor 15: System limit exceeded
	Data Format 15: None
	Descriptor 16: Asynchronous hardware timer expired
	Data Format 16: None
	Descriptor 17: System configuration information
	Data Format 17: None
	Descriptor 18: Hard disk information
	Data Format 18: None
	Descriptor 19: System reconfigured
	Data Format 19: None
	Descriptor 20: Uncorrectable CPU-complex error
	Data Format 20: None
	Descriptor 21: Log area reset/cleared
	Data Format 21: None
	Descriptor 22: System boot
	Data Format 22: None
	Descriptor 23: End of log
	Data Format 23: None
	Descriptor 24: OEM-specific
	Data Format 24: OEM-specific
	Descriptor 25: OEM-specific
	Data Format 25: OEM-specific
```
# BIOS
```
$ sudo dmidecode -t bios
# dmidecode 3.5
Getting SMBIOS data from sysfs.
SMBIOS 3.2.0 present.

Handle 0x0000, DMI type 0, 26 bytes
BIOS Information
	Vendor: American Megatrends Inc.
	Version: 1.0.1
	Release Date: 04/21/2020
	Address: 0xF0000
	Runtime Size: 64 kB
	ROM Size: 16 MB
	Characteristics:
		BIOS is upgradeable
		BIOS shadowing is allowed
		Boot from CD is supported
		Selectable boot is supported
		BIOS ROM is socketed
		ACPI is supported
		USB legacy is supported
		BIOS boot specification is supported
		Targeted content distribution is supported
		UEFI is supported
	BIOS Revision: 5.14
```


### Operating System

Ubuntu 24.04 LTS

### CPU

AMD EPYC 7V12 64-Core Processor

### GPU

AMD Instinct MI210 

### ROCm Version

6.16.13

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

---

## 评论 (7 条)

### 评论 #1 — harkgill-amd (2026-05-21T20:31:44Z)

Hey @botbw, seeing some precedent for these GPU initialization errors being solved with a change to BIOS settings. Can you try enabling Above 4G Decoding + Resizable BAR in the BIOS and sharing the outputs of `uname -r`/ `sudo dmesg | grep BAR`?

---

### 评论 #2 — botbw (2026-05-22T05:27:00Z)

@harkgill-amd Thanks for the reply. I did turn on `Above 4G Decoding`, but cannot find `Resizeable BAR` or related settings in my current BIOS. I will have a try and get back to you.

---

### 评论 #3 — botbw (2026-05-23T08:39:43Z)

@harkgill-amd 

<img width="1622" height="1224" alt="Image" src="https://github.com/user-attachments/assets/3ec56e26-3239-40d0-87ec-0e9704edde35" />

I tried to reinstall the GPU on a supermicro server, and enable two settings above in BIOS, still got the same error:

```
$ sudo uname -r
6.8.0-117-generic

$ sudo dmesg | grep BAR
[    3.859434] pci 0000:62:00.0: BAR 0 [mem 0xce000000-0xceffffff]
[    3.859440] pci 0000:62:00.0: BAR 1 [mem 0xcf000000-0xcf03ffff]
[    3.859445] pci 0000:62:00.0: BAR 2 [io  0x8000-0x807f]
[    3.859707] pci 0000:63:00.0: BAR 0 [io  0x7050-0x7057]
[    3.859712] pci 0000:63:00.0: BAR 1 [io  0x7040-0x7043]
[    3.859717] pci 0000:63:00.0: BAR 2 [io  0x7030-0x7037]
[    3.859722] pci 0000:63:00.0: BAR 3 [io  0x7020-0x7023]
[    3.859726] pci 0000:63:00.0: BAR 4 [io  0x7000-0x701f]
[    3.859731] pci 0000:63:00.0: BAR 5 [mem 0xcf400000-0xcf4001ff]
[    3.860176] pci 0000:64:00.1: BAR 0 [mem 0x20020f80000-0x20020ffffff 64bit pref]
[    3.860182] pci 0000:64:00.1: BAR 2 [mem 0x20020f00000-0x20020f7ffff 64bit pref]
[    3.860331] pci 0000:64:00.4: BAR 0 [mem 0xcf300000-0xcf3fffff 64bit]
[    3.861156] pci 0000:65:00.0: BAR 5 [mem 0xcf201000-0xcf2017ff]
[    3.861329] pci 0000:65:00.1: BAR 5 [mem 0xcf200000-0xcf2007ff]
[    3.888341] pci 0000:48:00.0: BAR 0 [mem 0x30020f00000-0x30020f03fff 64bit pref]
[    3.889327] pci 0000:49:00.1: BAR 0 [mem 0x30020e80000-0x30020efffff 64bit pref]
[    3.889333] pci 0000:49:00.1: BAR 2 [mem 0x30020e00000-0x30020e7ffff 64bit pref]
[    3.918889] pci 0000:08:00.0: BAR 0 [mem 0x4007f000000-0x4007fffffff 64bit pref]
[    3.918897] pci 0000:08:00.0: BAR 3 [mem 0x40080008000-0x4008000ffff 64bit pref]
[    3.919021] pci 0000:08:00.0: VF BAR 0 [mem 0x00000000-0x0000ffff 64bit pref]
[    3.919026] pci 0000:08:00.0: VF BAR 0 [mem 0x00000000-0x003fffff 64bit pref]: contains BAR 0 for 64 VFs
[    3.919034] pci 0000:08:00.0: VF BAR 3 [mem 0x00000000-0x00003fff 64bit pref]
[    3.919039] pci 0000:08:00.0: VF BAR 3 [mem 0x00000000-0x000fffff 64bit pref]: contains BAR 3 for 64 VFs
[    3.919344] pci 0000:08:00.1: BAR 0 [mem 0x4007e000000-0x4007effffff 64bit pref]
[    3.919351] pci 0000:08:00.1: BAR 3 [mem 0x40080000000-0x40080007fff 64bit pref]
[    3.919463] pci 0000:08:00.1: VF BAR 0 [mem 0x00000000-0x0000ffff 64bit pref]
[    3.919467] pci 0000:08:00.1: VF BAR 0 [mem 0x00000000-0x003fffff 64bit pref]: contains BAR 0 for 64 VFs
[    3.919475] pci 0000:08:00.1: VF BAR 3 [mem 0x00000000-0x00003fff 64bit pref]
[    3.919480] pci 0000:08:00.1: VF BAR 3 [mem 0x00000000-0x000fffff 64bit pref]: contains BAR 3 for 64 VFs
[    3.920356] pci 0000:09:00.1: BAR 0 [mem 0x40080280000-0x400802fffff 64bit pref]
[    3.920362] pci 0000:09:00.1: BAR 2 [mem 0x40080200000-0x4008027ffff 64bit pref]
[    3.920513] pci 0000:09:00.4: BAR 0 [mem 0xf6100000-0xf61fffff 64bit]
[    3.920669] pci 0000:09:00.5: BAR 2 [mem 0xf6000000-0xf60fffff]
[    3.920674] pci 0000:09:00.5: BAR 5 [mem 0xf6200000-0xf6201fff]
[    3.920940] pci 0000:0a:00.0: BAR 5 [mem 0xf6301000-0xf63017ff]
[    3.921188] pci 0000:0a:00.1: BAR 5 [mem 0xf6300000-0xf63007ff]
[    3.931230] pci 0000:21:00.1: BAR 0 [mem 0x50080f80000-0x50080ffffff 64bit pref]
[    3.931236] pci 0000:21:00.1: BAR 2 [mem 0x50080f00000-0x50080f7ffff 64bit pref]
[    3.934587] pci 0000:e1:00.1: BAR 0 [mem 0x600e0f80000-0x600e0ffffff 64bit pref]
[    3.934594] pci 0000:e1:00.1: BAR 2 [mem 0x600e0f00000-0x600e0f7ffff 64bit pref]
[    3.934765] pci 0000:e1:00.4: BAR 0 [mem 0xc0000000-0xc00fffff 64bit]
[    3.977081] pci 0000:c5:00.0: BAR 0 [mem 0x6f000000000-0x6ffffffffff 64bit pref]
[    3.977099] pci 0000:c5:00.0: BAR 2 [mem 0x70000000000-0x700001fffff 64bit pref]
[    3.977110] pci 0000:c5:00.0: BAR 4 [io  0xd000-0xd0ff]
[    3.977120] pci 0000:c5:00.0: BAR 5 [mem 0xba200000-0xba27ffff]
[    3.979866] pci 0000:c5:00.0: VF BAR 0 [mem 0x00000000-0xfffffffff 64bit pref]
[    3.979871] pci 0000:c5:00.0: VF BAR 0 [mem 0x00000000-0xfffffffff 64bit pref]: contains BAR 0 for 1 VFs
[    3.979890] pci 0000:c5:00.0: VF BAR 2 [mem 0x00000000-0x001fffff 64bit pref]
[    3.979894] pci 0000:c5:00.0: VF BAR 2 [mem 0x00000000-0x001fffff 64bit pref]: contains BAR 2 for 1 VFs
[    3.979909] pci 0000:c5:00.0: VF BAR 5 [mem 0x00000000-0x0007ffff]
[    3.979913] pci 0000:c5:00.0: VF BAR 5 [mem 0x00000000-0x0007ffff]: contains BAR 5 for 1 VFs
[    3.983412] pci 0000:c8:00.0: BAR 0 [mem 0xba110000-0xba113fff 64bit]
[    3.987814] pci 0000:c9:00.0: BAR 0 [mem 0xba010000-0xba013fff 64bit]
[    3.990632] pci 0000:ca:00.0: BAR 0 [mem 0x70000300000-0x70000303fff 64bit pref]
[    3.993060] pci 0000:cb:00.1: BAR 0 [mem 0x70000580000-0x700005fffff 64bit pref]
[    3.993070] pci 0000:cb:00.1: BAR 2 [mem 0x70000500000-0x7000057ffff 64bit pref]
[    4.030285] pci 0000:88:00.1: BAR 0 [mem 0x80140f80000-0x80140ffffff 64bit pref]
[    4.030292] pci 0000:88:00.1: BAR 2 [mem 0x80140f00000-0x80140f7ffff 64bit pref]
[    4.030466] pci 0000:88:00.4: BAR 0 [mem 0xb6100000-0xb61fffff 64bit]
[    4.030634] pci 0000:88:00.5: BAR 2 [mem 0xb6000000-0xb60fffff]
[    4.030640] pci 0000:88:00.5: BAR 5 [mem 0xb6200000-0xb6201fff]
[    4.039875] pci 0000:a1:00.1: BAR 0 [mem 0x90140f80000-0x90140ffffff 64bit pref]
[    4.039882] pci 0000:a1:00.1: BAR 2 [mem 0x90140f00000-0x90140f7ffff 64bit pref]
[    4.146148] pnp 00:00: disabling [mem 0xe0000000-0xefffffff] because it overlaps 0000:c5:00.0 BAR 7 [mem 0x00000000-0xfffffffff 64bit pref]
[    4.148554] pnp 00:05: disabling [mem 0xfedc0000-0xfedc0fff] because it overlaps 0000:c5:00.0 BAR 7 [mem 0x00000000-0xfffffffff 64bit pref]
[    4.148563] pnp 00:05: disabling [mem 0xfee00000-0xfee00fff] because it overlaps 0000:c5:00.0 BAR 7 [mem 0x00000000-0xfffffffff 64bit pref]
[    4.148570] pnp 00:05: disabling [mem 0xfed80000-0xfed814ff] because it overlaps 0000:c5:00.0 BAR 7 [mem 0x00000000-0xfffffffff 64bit pref]
[    4.148577] pnp 00:05: disabling [mem 0xfed81900-0xfed8ffff] because it overlaps 0000:c5:00.0 BAR 7 [mem 0x00000000-0xfffffffff 64bit pref]
[    4.148584] pnp 00:05: disabling [mem 0xfec10000-0xfec10fff] because it overlaps 0000:c5:00.0 BAR 7 [mem 0x00000000-0xfffffffff 64bit pref]
[    4.148591] pnp 00:05: disabling [mem 0xff000000-0xffffffff] because it overlaps 0000:c5:00.0 BAR 7 [mem 0x00000000-0xfffffffff 64bit pref]
[    4.181312] pci 0000:08:00.0: VF BAR 0 [mem size 0x00400000 64bit pref]: can't assign; no space
[    4.181317] pci 0000:08:00.0: VF BAR 0 [mem size 0x00400000 64bit pref]: failed to assign
[    4.181324] pci 0000:08:00.1: VF BAR 0 [mem size 0x00400000 64bit pref]: can't assign; no space
[    4.181329] pci 0000:08:00.1: VF BAR 0 [mem size 0x00400000 64bit pref]: failed to assign
[    4.181335] pci 0000:08:00.0: VF BAR 3 [mem size 0x00100000 64bit pref]: can't assign; no space
[    4.181340] pci 0000:08:00.0: VF BAR 3 [mem size 0x00100000 64bit pref]: failed to assign
[    4.181346] pci 0000:08:00.1: VF BAR 3 [mem size 0x00100000 64bit pref]: can't assign; no space
[    4.181352] pci 0000:08:00.1: VF BAR 3 [mem size 0x00100000 64bit pref]: failed to assign
[    4.182022] pci 0000:08:00.0: BAR 0 [mem 0x30082000000-0x30082ffffff 64bit pref]: assigned
[    4.182033] pci 0000:08:00.1: BAR 0 [mem 0x30083000000-0x30083ffffff 64bit pref]: assigned
[    4.182044] pci 0000:08:00.0: VF BAR 0 [mem 0x30084000000-0x300843fffff 64bit pref]: assigned
[    4.182053] pci 0000:08:00.1: VF BAR 0 [mem 0x30084400000-0x300847fffff 64bit pref]: assigned
[    4.182060] pci 0000:08:00.0: BAR 3 [mem 0x30084800000-0x30084807fff 64bit pref]: assigned
[    4.182071] pci 0000:08:00.1: BAR 3 [mem 0x30084808000-0x3008480ffff 64bit pref]: assigned
[    4.182082] pci 0000:08:00.0: VF BAR 3 [mem 0x30084810000-0x3008490ffff 64bit pref]: assigned
[    4.182090] pci 0000:08:00.1: VF BAR 3 [mem 0x30084910000-0x30084a0ffff 64bit pref]: assigned
[    4.184135] pci 0000:09:00.4: BAR 0 [mem 0xf6100000-0xf61fffff 64bit]: assigned
[    4.184143] pci 0000:09:00.5: BAR 2 [mem 0xf6200000-0xf62fffff]: assigned
[    4.184149] pci 0000:09:00.5: BAR 5 [mem 0xf6300000-0xf6301fff]: assigned
[    4.184182] pci 0000:0a:00.0: BAR 5 [mem 0xf6400000-0xf64007ff]: assigned
[    4.184187] pci 0000:0a:00.1: BAR 5 [mem 0xf6400800-0xf6400fff]: assigned
[    4.185849] pci 0000:c5:00.0: VF BAR 0 [mem size 0x1000000000 64bit pref]: can't assign; no space
[    4.185854] pci 0000:c5:00.0: VF BAR 0 [mem size 0x1000000000 64bit pref]: failed to assign
[    4.185860] pci 0000:c5:00.0: VF BAR 2 [mem size 0x00200000 64bit pref]: can't assign; no space
[    4.185865] pci 0000:c5:00.0: VF BAR 2 [mem size 0x00200000 64bit pref]: failed to assign
[    4.185871] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.185876] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: failed to assign
[    4.186811] pci 0000:c5:00.0: BAR 0 [mem size 0x1000000000 64bit pref]: can't assign; no space
[    4.186817] pci 0000:c5:00.0: BAR 0 [mem size 0x1000000000 64bit pref]: failed to assign
[    4.186822] pci 0000:c5:00.0: VF BAR 0 [mem size 0x1000000000 64bit pref]: can't assign; no space
[    4.186828] pci 0000:c5:00.0: VF BAR 0 [mem size 0x1000000000 64bit pref]: failed to assign
[    4.186833] pci 0000:c5:00.0: BAR 2 [mem size 0x00200000 64bit pref]: can't assign; no space
[    4.186838] pci 0000:c5:00.0: BAR 2 [mem size 0x00200000 64bit pref]: failed to assign
[    4.186844] pci 0000:c5:00.0: VF BAR 2 [mem size 0x00200000 64bit pref]: can't assign; no space
[    4.186849] pci 0000:c5:00.0: VF BAR 2 [mem size 0x00200000 64bit pref]: failed to assign
[    4.186854] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.186859] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: failed to assign
[    4.186864] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.186869] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: failed to assign
[    4.189433] pci 0000:c5:00.0: BAR 0 [mem size 0x1000000000 64bit pref]: can't assign; no space
[    4.189439] pci 0000:c5:00.0: BAR 0 [mem size 0x1000000000 64bit pref]: failed to assign
[    4.189444] pci 0000:c5:00.0: VF BAR 0 [mem size 0x1000000000 64bit pref]: can't assign; no space
[    4.189450] pci 0000:c5:00.0: VF BAR 0 [mem size 0x1000000000 64bit pref]: failed to assign
[    4.189455] pci 0000:c5:00.0: BAR 2 [mem size 0x00200000 64bit pref]: can't assign; no space
[    4.189460] pci 0000:c5:00.0: BAR 2 [mem size 0x00200000 64bit pref]: failed to assign
[    4.189465] pci 0000:c5:00.0: VF BAR 2 [mem size 0x00200000 64bit pref]: can't assign; no space
[    4.189471] pci 0000:c5:00.0: VF BAR 2 [mem size 0x00200000 64bit pref]: failed to assign
[    4.189476] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.189481] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: failed to assign
[    4.189485] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.189490] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: failed to assign
[    4.189495] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: can't assign; no space
[    4.189499] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: failed to assign
[    4.189831] pci 0000:c8:00.0: BAR 0 [mem size 0x00004000 64bit]: can't assign; no space
[    4.189836] pci 0000:c8:00.0: BAR 0 [mem size 0x00004000 64bit]: failed to assign
[    4.189911] pci 0000:c9:00.0: BAR 0 [mem size 0x00004000 64bit]: can't assign; no space
[    4.189916] pci 0000:c9:00.0: BAR 0 [mem size 0x00004000 64bit]: failed to assign
[    4.189981] pci 0000:ca:00.0: BAR 0 [mem size 0x00004000 64bit pref]: can't assign; no space
[    4.189987] pci 0000:ca:00.0: BAR 0 [mem size 0x00004000 64bit pref]: failed to assign
[    4.190487] pci 0000:c5:00.0: BAR 0 [mem 0x61000000000-0x61fffffffff 64bit pref]: assigned
[    4.190568] pci 0000:c5:00.0: VF BAR 0 [mem 0x62000000000-0x62fffffffff 64bit pref]: assigned
[    4.190601] pci 0000:c5:00.0: BAR 2 [mem 0x60800000000-0x608001fffff 64bit pref]: assigned
[    4.190678] pci 0000:c5:00.0: VF BAR 2 [mem 0x60800200000-0x608003fffff 64bit pref]: assigned
[    4.190710] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.190718] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: failed to assign
[    4.190724] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.190730] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: failed to assign
[    4.190735] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: can't assign; no space
[    4.190741] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: failed to assign
[    4.191094] pci 0000:c8:00.0: BAR 0 [mem size 0x00004000 64bit]: can't assign; no space
[    4.191099] pci 0000:c8:00.0: BAR 0 [mem size 0x00004000 64bit]: failed to assign
[    4.191169] pci 0000:c9:00.0: BAR 0 [mem size 0x00004000 64bit]: can't assign; no space
[    4.191174] pci 0000:c9:00.0: BAR 0 [mem size 0x00004000 64bit]: failed to assign
[    4.191244] pci 0000:ca:00.0: BAR 0 [mem 0x60400800000-0x60400803fff 64bit pref]: assigned
[    4.191817] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.191822] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: failed to assign
[    4.191827] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.191831] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: failed to assign
[    4.191836] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: can't assign; no space
[    4.191841] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: failed to assign
[    4.192183] pci 0000:c8:00.0: BAR 0 [mem size 0x00004000 64bit]: can't assign; no space
[    4.192188] pci 0000:c8:00.0: BAR 0 [mem size 0x00004000 64bit]: failed to assign
[    4.192258] pci 0000:c9:00.0: BAR 0 [mem size 0x00004000 64bit]: can't assign; no space
[    4.192263] pci 0000:c9:00.0: BAR 0 [mem size 0x00004000 64bit]: failed to assign
[    4.192896] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.192901] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: failed to assign
[    4.192906] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.192911] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: failed to assign
[    4.192915] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: can't assign; no space
[    4.192920] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: failed to assign
[    4.192924] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.192929] pci 0000:c5:00.0: BAR 5 [mem size 0x00080000]: failed to assign
[    4.192934] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: can't assign; no space
[    4.192938] pci 0000:c5:00.0: BAR 4 [io  size 0x0100]: failed to assign
[    4.192943] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: can't assign; no space
[    4.192948] pci 0000:c5:00.0: VF BAR 5 [mem size 0x00080000]: failed to assign
[    4.193293] pci 0000:c8:00.0: BAR 0 [mem size 0x00004000 64bit]: can't assign; no space
[    4.193299] pci 0000:c8:00.0: BAR 0 [mem size 0x00004000 64bit]: failed to assign
[    4.193368] pci 0000:c9:00.0: BAR 0 [mem size 0x00004000 64bit]: can't assign; no space
[    4.193373] pci 0000:c9:00.0: BAR 0 [mem size 0x00004000 64bit]: failed to assign
[   19.894681] amdgpu 0000:c5:00.0: amdgpu: initializing kernel modesetting (ALDEBARAN 0x1002:0x740F 0x1002:0x0C34 0x02).
```

---

### 评论 #4 — harkgill-amd (2026-05-25T14:57:30Z)

Thanks for giving that a try. From your dmesg output, the driver is failing to initialize due to BAR being exhausted. Can you disable SR-IOV in your BIOS as well as per https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi200.html#system-bios-settings. This should prevent the VF BARs from being created and causing overlap.

---

### 评论 #5 — botbw (2026-05-25T15:02:19Z)

@harkgill-amd I did try that option, but after `SR-IOV` is set to disabled, the whole system cannot boot. Is there any other way to bypass that setting?

---

### 评论 #6 — harkgill-amd (2026-05-25T15:57:56Z)

The alternative would be to set `pci=realloc=off` in your kernel boot parameters 
```
sudo nano /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT= "pci=realloc=off" #Add this to the existing parameters                                                                                                                                                     
sudo update-grub && sudo reboot
```
This'll prevent the reallocation that allowed the VF BARs to overwrite the physical BARs in the first place. This is more of a workaround as we'd expect the original SR-IOV disable to prevent this but with it causing the crashing, we can give this a try and go from there.

---

### 评论 #7 — botbw (2026-05-26T05:45:41Z)

@harkgill-amd Thanks a lot for your help! The grub setting worked on both machines (btw I tried disabling `SR-IOV` on the first machine, and it also hung, not sure what the cause is).

---
