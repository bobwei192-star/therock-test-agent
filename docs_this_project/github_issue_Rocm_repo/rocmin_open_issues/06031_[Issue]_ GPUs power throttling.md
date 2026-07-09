# [Issue]: GPUs power throttling

- **Issue #:** 6031
- **State:** open
- **Created:** 2026-03-11T12:26:23Z
- **Updated:** 2026-03-20T15:42:33Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6031

### Problem Description

GPUs do not scale beyond 80W limiting throughput.

### Operating System

Proxmox 9.1.1 (Debian 13 base)

### CPU

Intel(R) Core(TM) Ultra 9 285K

### GPU

AMD Instinct mi210

### ROCm Version

ROCm 7.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

/opt/rocm-7.2.0/bin$ /opt/rocm/bin/rocminfo --support
ROCk module version 6.16.13 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.15
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Core(TM) Ultra 9 285K     
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) Ultra 9 285K     
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
  Max Clock Freq. (MHz):   0                                  
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            18                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    64295012(0x3d51064) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    64295012(0x3d51064) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    64295012(0x3d51064) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    64295012(0x3d51064) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx90a                             
  Uuid:                    GPU-327c8626c83ec858               
  Marketing Name:          AMD Instinct MI210                 
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
    L2:                      8192(0x2000) KB                    
  Chip ID:                 29711(0x740f)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   1700                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            104                                
  SIMDs per CU:            4                                  
  Shader Engines:          8                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    2048(0x800)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 96                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*******                  
Agent 3                  
*******                  
  Name:                    gfx90a                             
  Uuid:                    GPU-753ef2efdc04e86d               
  Marketing Name:          AMD Instinct MI210                 
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      8192(0x2000) KB                    
  Chip ID:                 29711(0x740f)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   1700                               
  BDFID:                   512                                
  Internal Node ID:        2                                  
  Compute Unit:            104                                
  SIMDs per CU:            4                                  
  Shader Engines:          8                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    2048(0x800)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 96                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*** Done ***      

### Additional Information

ASPM disabled in BIOS.

Running the validation suite (RVS):

+=====================================================================+
|                 ROCm Validation Suite (RVS) Summary                 |
+=====================================================================+
|                           System Overview                           |
+---------------------------------------------------------------------+
| Operating System                 | Debian GNU/Linux 12              |
| RVS version                      | 1.3.0                            |
| ROCm version                     | 7.2.0-43                         |
| amdgpu version                   | N/A                              |
| GPUs                             | 2                                |
+---------------------------------------------------------------------+
| GPU Name - GPU ID                |                                  |
| ID - Node ID - BDF               |                                  |
+---------------------------------------------------------------------+
| AMD Instinct MI210 - 20068       | AMD Instinct MI210 - 48932       |
| 0 - 1 - 0000:01:00.0             | 1 - 2 - 0000:02:00.0             |
+=====================================================================+
| Action Name                      | Module         | Result          |
+=====================================================================+
| action_1                         | GPUP           | PASS            |
| action_2                         | PEQT           | PASS            |
| action_3                         | PEBB           | PASS            |
| action_4                         | PBQT           | PASS            |
| action_5                         | IET            | FAIL            |
| action_6                         | GST            | FAIL            |
| action_7                         | BABEL          | PASS            |
| action_8                         | MEM            | PASS            |
| action_9                         | PESM           | PASS            |
+---------------------------------------------------------------------+
[RESULT] [   521.259539] [module_terminate] PCIe monitoring ended after wait duration.

[RESULT] [   356.416045] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   357.416583] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   357.416603] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   358.417136] [action_5] [GPU:: 48932] Power(W) 78.000000
[RESULT] [   358.417152] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   359.417652] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   359.417671] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   360.418175] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   360.418177] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   361.418721] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   361.418733] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   362.419176] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   362.419180] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   363.419791] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   363.419796] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   364.420317] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   364.420318] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   365.420849] [action_5] [GPU:: 20068] Power(W) 79.000000
[RESULT] [   365.420863] [action_5] [GPU:: 48932] Power(W) 77.000000
[RESULT] [   365.504184] [action_5] [GPU:: 48932] pass: FALSE
[RESULT] [   365.538665] [action_5] [GPU:: 20068] pass: FALSE
RVS-ERROR [iet] [action_5] Action failed to run successfully.