# [Issue]: amdgpu: probe of 0000:83:00.0 failed with error -12

- **Issue #:** 6281
- **State:** closed
- **Created:** 2026-05-20T08:44:39Z
- **Updated:** 2026-05-26T05:45:44Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6281

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