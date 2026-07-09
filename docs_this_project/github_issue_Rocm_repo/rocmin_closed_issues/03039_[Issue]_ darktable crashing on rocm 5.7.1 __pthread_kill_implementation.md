# [Issue]: darktable crashing on rocm 5.7.1 __pthread_kill_implementation

- **Issue #:** 3039
- **State:** closed
- **Created:** 2024-04-18T13:21:12Z
- **Updated:** 2024-07-10T21:01:41Z
- **Labels:** AMD Instinct MI300X, AMD Instinct MI300A, AMD Instinct MI250X, ROCm 5.7.1, AMD Instinct MI100, AMD Radeon RX 7900 XTX, AMD Radeon Pro W6800, AMD Radeon Pro VII, AMD Radeon VII, AMD Radeon RX 7900 XT, AMD Radeon Pro W7900, AMD Instinct MI250, AMD Instinct MI210, AMD Radeon Pro V620
- **URL:** https://github.com/ROCm/ROCm/issues/3039

### Problem Description

Disclaimer: the GPU is a Radeon 680M, which is not listed in the limited-options-list in the issue form
darktable Fedora package maintainer here.
When exporting photos, rocm crashed, causing darktable crash.

- kernel 6.8.5-201.fc39.x86_64
- amd-gpu-firmware-20240410-1.fc39.noarch
- darktable-4.6.1-5.fc39.x86_64
- rocm-opencl 5.7.1

**Attaching GDB trace here:**
[darktable_gdb.txt](https://github.com/ROCm/ROCm/files/15025458/darktable_gdb.txt)


### Operating System

Fedora 39 KDE

### CPU

AMD Ryzen 7 PRO 6850U

### GPU

AMD Instinct MI300X, AMD Instinct MI300A, AMD Instinct MI250X, AMD Instinct MI250, AMD Instinct MI210, AMD Instinct MI100, AMD Radeon Pro W7900, AMD Radeon Pro W6800, AMD Radeon Pro V620, AMD Radeon Pro VII, AMD Radeon RX 7900 XTX, AMD Radeon RX 7900 XT, AMD Radeon VII

### ROCm Version

ROCm 5.7.1

### ROCm Component

_No response_

### Steps to Reproduce

enable OpenCL in darktable and export some photos
Advanced Micro Devices, Inc. [AMD/ATI] Rembrandt [Radeon 680M] (rev d1)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 PRO 6850U with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 PRO 6850U with Radeon Graphics
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
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4768                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    31585928(0x1e1f688) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    31585928(0x1e1f688) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    31585928(0x1e1f688) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1035                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon Graphics                
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      2048(0x800) KB                     
  Chip ID:                 5761(0x1681)                       
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2200                               
  BDFID:                   13056                              
  Internal Node ID:        1                                  
  Compute Unit:            12                                 
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 116                                
  SDMA engine uCode::      47                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    1048576(0x100000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS:                     
      Size:                    1048576(0x100000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1035         
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


### Additional Information

_No response_