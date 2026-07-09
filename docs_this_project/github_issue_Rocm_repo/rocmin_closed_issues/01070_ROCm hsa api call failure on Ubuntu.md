# ROCm hsa api call failure on Ubuntu

- **Issue #:** 1070
- **State:** closed
- **Created:** 2020-04-02T21:44:33Z
- **Updated:** 2021-04-05T10:10:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1070

CPU: AMD Threadripper 1900x
GPU: AMD Radeon RX Vega 64 Liquid

```
$ /opt/rocm/bin/rocminfo
ROCk module is loaded
aresminos is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

```
$ sudo /opt/rocm/bin/rocminfo
ROCk module is loaded
aresminos is member of video group
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
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 1900X 8-Core Processor
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
  Max Clock Freq. (MHz):   3800                               
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
      Size:                    16312780(0xf8e9cc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16312780(0xf8e9cc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 1900X 8-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    0(0x0) KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    0(0x0) KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 3                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XL/XT [Radeon RX Vega 56/64]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26751(0x687f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1750                               
  BDFID:                   17408                              
  Internal Node ID:        2                                  
  Compute Unit:            64                                 
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
      Size:                    8372224(0x7fc000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx900          
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

```
$ /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3098.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```

```
$ uname -r
5.3.0-45-generic
```
```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 19.10
Release:	19.10
Codename:	eoan
```
```
$ sudo lshw -c video
  *-display                 
       description: VGA compatible controller
       product: Vega 10 XL/XT [Radeon RX Vega 56/64]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:44:00.0
       version: c0
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:125 memory:80000000-8fffffff memory:90000000-901fffff ioport:3000(size=256) memory:9f300000-9f37ffff memory:c0000-dffff
```

```
$ sudo lshw -short
H/W path                      Device     Class          Description
===================================================================
                                         system         To Be Filled By O.E.M. (To Be Filled By O.E.M.)
/0                                       bus            X399 Taichi
/0/0                                     memory         64KiB BIOS
/0/8                                     memory         16GiB System Memory
/0/8/0                                   memory         [empty]
/0/8/1                                   memory         8GiB DIMM DDR4 Synchronous Unbuffered (Unregistered) 3600 MHz (0,3 ns)
/0/8/2                                   memory         [empty]
/0/8/3                                   memory         8GiB DIMM DDR4 Synchronous Unbuffered (Unregistered) 3600 MHz (0,3 ns)
/0/8/4                                   memory         [empty]
/0/8/5                                   memory         [empty]
/0/8/6                                   memory         [empty]
/0/8/7                                   memory         [empty]
/0/b                                     memory         768KiB L1 cache
/0/c                                     memory         4MiB L2 cache
/0/d                                     memory         16MiB L3 cache
/0/e                                     processor      AMD Ryzen Threadripper 1900X 8-Core Processor
/0/100                                   bridge         Family 17h (Models 00h-0fh) Root Complex
/0/100/0.2                               generic        Family 17h (Models 00h-0fh) I/O Memory Management Unit
/0/100/1.1                               bridge         Family 17h (Models 00h-0fh) PCIe GPP Bridge
/0/100/1.1/0                             bus            X399 Series Chipset USB 3.1 xHCI Controller
/0/100/1.1/0/0                usb1       bus            xHCI Host Controller
/0/100/1.1/0/0/9                         communication  Bluetooth wireless interface
/0/100/1.1/0/1                usb2       bus            xHCI Host Controller
/0/100/1.1/0.1                scsi3      storage        X399 Series Chipset SATA Controller
/0/100/1.1/0.1/0.0.0          /dev/sda   disk           500GB Samsung SSD 850
/0/100/1.1/0.1/0.0.0/1                   volume         511MiB Windows FAT volume
/0/100/1.1/0.1/0.0.0/2        /dev/sda2  volume         465GiB EXT4 volume
/0/100/1.1/0.2                           bridge         X399 Series Chipset PCIe Bridge
/0/100/1.1/0.2/0                         bridge         300 Series Chipset PCIe Port
/0/100/1.1/0.2/4                         bridge         300 Series Chipset PCIe Port
/0/100/1.1/0.2/4/0            enp4s0     network        I211 Gigabit Network Connection
/0/100/1.1/0.2/5                         bridge         300 Series Chipset PCIe Port
/0/100/1.1/0.2/5/0            wlp5s0     network        Dual Band Wireless-AC 3168NGW [Stone Peak]
/0/100/1.1/0.2/6                         bridge         300 Series Chipset PCIe Port
/0/100/1.1/0.2/6/0            enp6s0     network        I211 Gigabit Network Connection
/0/100/1.1/0.2/7                         bridge         300 Series Chipset PCIe Port
/0/100/1.2                               bridge         Family 17h (Models 00h-0fh) PCIe GPP Bridge
/0/100/1.2/0                             storage        NVMe SSD Controller SM961/PM961
/0/100/7.1                               bridge         Family 17h (Models 00h-0fh) Internal PCIe GPP Bridge 0 to Bus B
/0/100/7.1/0                             generic        Zeppelin/Raven/Raven2 PCIe Dummy Function
/0/100/7.1/0.2                           generic        Family 17h (Models 00h-0fh) Platform Security Processor
/0/100/7.1/0.3                           bus            Family 17h (Models 00h-0fh) USB 3.0 Host Controller
/0/100/7.1/0.3/0              usb3       bus            xHCI Host Controller
/0/100/7.1/0.3/0/2                       input          Magic Keyboard
/0/100/7.1/0.3/0/4                       bus            USB2.0 Hub
/0/100/7.1/0.3/0/4/4                     input          USB Keyboard
/0/100/7.1/0.3/1              usb4       bus            xHCI Host Controller
/0/100/7.1/0.3/1/4                       bus            USB3.0 Hub
/0/100/7.1/0.3/1/4/2          scsi10     storage        USB Storage
/0/100/7.1/0.3/1/4/2/0.0.0    /dev/sdb   disk           STORAGE DEVICE
/0/100/7.1/0.3/1/4/2/0.0.0/0  /dev/sdb   disk           
/0/100/8.1                               bridge         Family 17h (Models 00h-0fh) Internal PCIe GPP Bridge 0 to Bus B
/0/100/8.1/0                             generic        Zeppelin/Renoir PCIe Dummy Function
/0/100/8.1/0.2                           storage        FCH SATA Controller [AHCI mode]
/0/100/8.1/0.3                           multimedia     Family 17h (Models 00h-0fh) HD Audio Controller
/0/100/14                                bus            FCH SMBus Controller
/0/100/14.3                              bridge         FCH LPC Bridge
/0/101                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/102                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/103                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/104                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/105                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/106                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/107                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 0
/0/108                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 1
/0/109                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 2
/0/10a                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 3
/0/10b                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 4
/0/10c                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 5
/0/10d                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 6
/0/10e                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 7
/0/10f                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 0
/0/110                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 1
/0/111                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 2
/0/112                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 3
/0/113                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 4
/0/114                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 5
/0/115                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 6
/0/116                                   bridge         Family 17h (Models 00h-0fh) Data Fabric: Device 18h; Function 7
/0/117                                   bridge         Family 17h (Models 00h-0fh) Root Complex
/0/117/0.2                               generic        Family 17h (Models 00h-0fh) I/O Memory Management Unit
/0/117/1.2                               bridge         Family 17h (Models 00h-0fh) PCIe GPP Bridge
/0/117/1.2/0                             storage        NVMe SSD Controller SM981/PM981/PM983
/0/117/3.1                               bridge         Family 17h (Models 00h-0fh) PCIe GPP Bridge
/0/117/3.1/0                             bridge         Advanced Micro Devices, Inc. [AMD]
/0/117/3.1/0/0                           bridge         Advanced Micro Devices, Inc. [AMD]
/0/117/3.1/0/0/0                         display        Vega 10 XL/XT [Radeon RX Vega 56/64]
/0/117/3.1/0/0/0.1                       multimedia     Vega 10 HDMI Audio [Radeon Vega 56/64]
/0/117/7.1                               bridge         Family 17h (Models 00h-0fh) Internal PCIe GPP Bridge 0 to Bus B
/0/117/7.1/0                             generic        Zeppelin/Raven/Raven2 PCIe Dummy Function
/0/117/7.1/0.2                           generic        Family 17h (Models 00h-0fh) Platform Security Processor
/0/117/7.1/0.3                           bus            Family 17h (Models 00h-0fh) USB 3.0 Host Controller
/0/117/7.1/0.3/0              usb5       bus            xHCI Host Controller
/0/117/7.1/0.3/0/1                       bus            USB hub
/0/117/7.1/0.3/0/1/1                     input          Mad Catz R.A.T. Pro X
/0/117/7.1/0.3/0/1/2                     input          Apple Cinema HD Display
/0/117/7.1/0.3/0/1/3                     communication  CSR8510 A10
/0/117/7.1/0.3/1              usb6       bus            xHCI Host Controller
/0/117/8.1                               bridge         Family 17h (Models 00h-0fh) Internal PCIe GPP Bridge 0 to Bus B
/0/117/8.1/0                             generic        Zeppelin/Renoir PCIe Dummy Function
/0/117/8.1/0.2                           storage        FCH SATA Controller [AHCI mode]
/0/118                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/119                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/11a                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/11b                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/11c                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/11d                                   bridge         Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
/0/1                                     system         PnP device PNP0c01
/0/2                                     system         PnP device PNP0c02
/0/3                                     system         PnP device PNP0b00
/0/4                                     system         PnP device PNP0c02
/0/5                                     system         PnP device PNP0c02
/0/6                                     system         PnP device PNP0c02

```

