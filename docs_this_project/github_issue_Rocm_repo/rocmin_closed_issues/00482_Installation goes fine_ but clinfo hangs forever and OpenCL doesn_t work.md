# Installation goes fine, but clinfo hangs forever and OpenCL doesn't work

- **Issue #:** 482
- **State:** closed
- **Created:** 2018-07-30T17:30:38Z
- **Updated:** 2019-12-26T13:49:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/482

I am filing this as an upstream version of https://github.com/nixos-rocm/nixos-rocm/issues/7

In short, I am using the 1.8.2 versions of everything here (with NixOS Linux – but in a configuration exactly matching that of another NixOS user, for whom it is working perfectly), and while the installation appears to succeed just fine, OpenCL is not working for me at runtime.

Note, this is a Radeon Vega FE card in an older (Ivy Bridge) system, with a Z77 Express chipset which, although is advertised to have PCIe Gen3 in the link below, I believe either has PCIe Gen2 in my configuration, or at least does not support atomics, given I got the ~`This system does not support atomics` error from ROCm in the 1.7.x series).

My system:
CPU: Intel Core-i5 3570
Motherboard: [Gigabyte Z77N-WIFI](https://www.gigabyte.com/Motherboard/GA-Z77N-WIFI-rev-10#sp)
GPU: Radeon Vega FE 16GB

My primary symptoms are:
1) if I run `clinfo`, it hangs forever. A truncated `strace` output is [here](https://github.com/nixos-rocm/nixos-rocm/files/2233563/cldebug_trunc.txt); it just repeats the last `sched_yield()` lines forever.

2) If I run XMR-stak. it sits forever at the line: `Compiling code and initializing GPUs. This will take a while...`. My CPU usage goes up to 100% (of one core), but it never progresses to actually mining anything.

Please let me know if there is anything I can try, to collect useful info, or if you there's a chance I have something configured wrong. As mentioned in the other thread, I have just replaced my PSU with an 850W Seasonic, which should have about 3x the power this system needs, and I get the same result... so I don't think power is the problem!


```
# lspci
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor DRAM Controller (rev 09)
00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port (rev 09)
00:02.0 Display controller: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor Graphics Controller (rev 09)
00:14.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller (rev 04)
00:16.0 Communication controller: Intel Corporation 7 Series/C216 Chipset Family MEI Controller #1 (rev 04)
00:1a.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #2 (rev 04)
00:1c.0 PCI bridge: Intel Corporation 7 Series/C216 Chipset Family PCI Express Root Port 1 (rev c4)
00:1c.4 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 5 (rev c4)
00:1c.5 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 6 (rev c4)
00:1c.6 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 7 (rev c4)
00:1d.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #1 (rev 04)
00:1f.0 ISA bridge: Intel Corporation Z77 Express Chipset LPC Controller (rev 04)
00:1f.2 SATA controller: Intel Corporation 7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode] (rev 04)
00:1f.3 SMBus: Intel Corporation 7 Series/C216 Chipset Family SMBus Controller (rev 04)
01:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470
02:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition]
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
05:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)
06:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)
07:00.0 Network controller: Intel Corporation Centrino Wireless-N 2230 (rev c4)
```


```
# rocminfo
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Core(TM) i5-3570 CPU @ 3.40GHz
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):3800                               
  BDFID:                   0                                  
  Compute Unit:            4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16322420KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16322420KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 26723                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1600                               
  BDFID:                   768                                
  Compute Unit:            64                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size per Dimension:
    x                        1024                               
    y                        1024                               
    z                        1024                               
  Waves Per CU:            40                                 
  Max Work-item Per CU:    2560                               
  Grid Max Size:           4294967295                         
  Grid Max Size per Dimension:
    x                        4294967295                         
    y                        4294967295                         
    z                        4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64KB                               
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
      Workgroup Max Size:      1024                               
      Workgroup Max Size per Dimension:
        x                        1024                               
        y                        1024                               
        z                        1024                               
      Grid Max Size:           4294967295                         
      Grid Max Size per Dimension:
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      FBarrier Max Size:       32                                 
*** Done ***             
```