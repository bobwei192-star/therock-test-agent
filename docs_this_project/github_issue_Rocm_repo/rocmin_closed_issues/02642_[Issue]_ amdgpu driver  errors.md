# [Issue]: amdgpu driver  errors

- **Issue #:** 2642
- **State:** closed
- **Created:** 2023-11-14T16:30:59Z
- **Updated:** 2025-09-25T17:10:27Z
- **Labels:** 5.7.0, 5.7.1
- **URL:** https://github.com/ROCm/ROCm/issues/2642

### Problem Description

When running some examples I see errors in dmesg:

/opt/rocm-5.7.0/share/hip/samples/2_Cookbook/0_MatrixTranspose
```
[  262.094619] amdgpu 0000:03:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:158 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[  262.094625] amdgpu 0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x0010 address=0x64a7f000 flags=0x0000]
[  262.094626] amdgpu 0000:03:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
[  262.094630] amdgpu 0000:03:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B3C
[  262.094634] amdgpu 0000:03:00.0: amdgpu:    Faulty UTCL2 client ID: CPC (0x5)
[  262.094637] amdgpu 0000:03:00.0: amdgpu:    MORE_FAULTS: 0x0
[  262.094639] amdgpu 0000:03:00.0: amdgpu:    WALKER_ERROR: 0x6
[  262.094641] amdgpu 0000:03:00.0: amdgpu:    PERMISSION_FAULTS: 0x3
[  262.094643] amdgpu 0000:03:00.0: amdgpu:    MAPPING_ERROR: 0x1
[  262.094645] amdgpu 0000:03:00.0: amdgpu:    RW: 0x0
[  262.094688] amdgpu 0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x0010 address=0x64a7f000 flags=0x0020]
[  262.230974] amdgpu 0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x0010 address=0x64a7f000 flags=0x0020]
```
Same error ^  /opt/rocm-5.7.0/share/hip/samples/2_Cookbook/10_inline_asm

/opt/rocm-5.7.0/share/hip/samples/2_Cookbook/16_assembly_to_executable$ ./square_asm.out
app output:
```
info: running on device Radeon RX 7900 XT
info: allocate host mem (  7.63 MB)
info: allocate device mem (  7.63 MB)
info: copy Host2Device
info: launch 'vector_square' kernel
info: copy Device2Host
info: check result
error: 'unknown error'(999) at square.cpp:92
```

dmesg output:
```
[  456.201981] amdgpu 0000:03:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:158 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[  456.201986] amdgpu 0000:03:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
[  456.201988] amdgpu 0000:03:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B3C
[  456.201989] amdgpu 0000:03:00.0: amdgpu:    Faulty UTCL2 client ID: CPC (0x5)
[  456.201991] amdgpu 0000:03:00.0: amdgpu:    MORE_FAULTS: 0x0
[  456.201992] amdgpu 0000:03:00.0: amdgpu:    WALKER_ERROR: 0x6
[  456.201993] amdgpu 0000:03:00.0: amdgpu:    PERMISSION_FAULTS: 0x3
[  456.201994] amdgpu 0000:03:00.0: amdgpu:    MAPPING_ERROR: 0x1
[  456.201995] amdgpu 0000:03:00.0: amdgpu:    RW: 0x0
[  456.202002] amdgpu 0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x0010 address=0x64a7f000 flags=0x0000]
[  456.202058] amdgpu 0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x0010 address=0x64a7f000 flags=0x0020]
[  456.332547] amdgpu 0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x0010 address=0x64a7f000 flags=0x0020]
```


### Operating System

22.04.3 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 9 7950X3D

### GPU

Radeon RX 7900 XT

### ROCm Version

5.7.1

### ROCm Component

_No response_

### Steps to Reproduce

Run those examples and check the `dmesg` output.

Running the same examples and some LLMs using the FOSS mesa drivers work just fine, is `amdgpu` really needed for ROCm? If not what are the advantages of the `amdgpu`  ?


### Output of /opt/rocm/bin/rocminfo --support

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
  Name:                    AMD Ryzen 9 7950X3D 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 7950X3D 16-Core Processor
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
  Max Clock Freq. (MHz):   5759                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    65564044(0x3e86d8c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65564044(0x3e86d8c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65564044(0x3e86d8c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-0001b7e800000000               
  Marketing Name:          Radeon RX 7900 XT                  
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
    L1:                      32(0x20) KB                        
    L2:                      6144(0x1800) KB                    
    L3:                      81920(0x14000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2075                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            84                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
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
  Packet Processor uCode:: 494                                
  SDMA engine uCode::      19                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    20955136(0x13fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS:                     
      Size:                    20955136(0x13fc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx1100         
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
