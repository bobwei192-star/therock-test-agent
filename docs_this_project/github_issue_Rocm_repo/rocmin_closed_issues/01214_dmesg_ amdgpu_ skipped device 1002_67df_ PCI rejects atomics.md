# dmesg: amdgpu: skipped device 1002:67df, PCI rejects atomics

- **Issue #:** 1214
- **State:** closed
- **Created:** 2020-09-08T23:36:30Z
- **Updated:** 2020-09-09T22:35:19Z
- **URL:** https://github.com/ROCm/ROCm/issues/1214

Hi it seems like my motherboard does not support the AMD RX 580 4G RAM. `/opt/rocm/bin/rocminfo` does not find the AMD GPU. And with dmesg I get `PCI rejects atomics`. I will post some system machine information and some graphics card information as well as CPU information.

Any idea what I could do to get my RX 580 accepted at the PCI bus?


`dmesg | grep kfd`

```
[    7.026427] kfd kfd: amdgpu: skipped device 1002:67df, PCI rejects atomics
```

`inxi -Gxxx`

```
Graphics:  Device-1: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] 
           vendor: Sapphire Limited Nitro+ driver: amdgpu v: 5.6.12 bus ID: 03:00.0 chip ID: 1002:67df 
           Display: x11 server: X.Org 1.20.5 compositor: gnome-shell v: 3.34.3 driver: amdgpu,ati 
           unloaded: fbdev,modesetting,vesa resolution: 1920x1080~60Hz s-dpi: 96 
           OpenGL: renderer: Radeon RX 580 Series (POLARIS10 DRM 3.39.0 5.3.0-64-generic LLVM 9.0.0) v: 4.5 Mesa 19.2.8 
           direct render: Yes
```


`inxi -Mxxx`

```
Machine:   Type: Desktop Mobo: MSI model: MSI X58 Pro (MS-7522) v: 3.0 serial: N/A BIOS: American Megatrends v: 8.15 
           date: 03/19/2011
```


`inxi -Cxxx`

```
CPU:       Info: 6-Core model: Intel Xeon X5650 bits: 64 type: MT MCP arch: Nehalem rev: 2 L1 cache: 384 KiB 
           L2 cache: 12.0 MiB L3 cache: 12.0 MiB 
           flags: lm nx pae sse sse2 sse3 sse4_1 sse4_2 ssse3 vmx bogomips: 64157 
           Speed: 1604 MHz min/max: 1600/2668 MHz boost: enabled ext-clock: 133 MHz Core speeds (MHz): 1: 1604 2: 1604 3: 1604 
           4: 1604 5: 1604 6: 1604 7: 1604 8: 1604 9: 1604 10: 1604 11: 1604 12: 1604
```



`/opt/rocm/bin/rocminfo`

```
ROCk module is loaded
Able to open /dev/kfd read-write
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
  Name:                    Intel(R) Xeon(R) CPU           X5650  @ 2.67GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) CPU           X5650  @ 2.67GHz
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
  Max Clock Freq. (MHz):   2668                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            12                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32878208(0x1f5ae80) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32878208(0x1f5ae80) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*** Done ***             
```

`/opt/rocm/bin/rocm-smi`

```
========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr   SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
0    27.0c  31.185W  600Mhz  300Mhz  16.86%  auto  175.0W    6%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================
```
