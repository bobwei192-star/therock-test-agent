# [Issue]: Illegal seek for GPU arch : gfx1103 

- **Issue #:** 2719
- **State:** closed
- **Created:** 2023-12-14T22:32:13Z
- **Updated:** 2024-10-01T15:41:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/2719

### Problem Description

I compiled llama.cpp with support for rocblas on Ubuntu 22.04. 

When I try to run llama.cpp I get the following error

>> sudo ~/llama.cpp/build/bin/main \
    -ngl 35 -m ~/llama.cpp/mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf \
    --color -c 32768 --temp 0.7 --repeat_penalty 1.1 -n -1 \
    -p "<s>[INST] say hello to me in french [/INST]"

main: build = 1641 (6744dbe)
main: built with cc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 for x86_64-linux-gnu
main: seed  = 1702592822

rocBLAS error: Cannot read /opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary.dat: Illegal seek for GPU arch : gfx1103
 List of available TensileLibrary Files : 
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx941.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx900.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx908.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx1102.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx90a.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx1101.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx1030.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx942.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx940.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx1100.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx906.dat"
"/opt/rocm-5.7.0/lib/rocblas/library/TensileLibrary_lazy_gfx803.dat"

### Operating System

22.04.3 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 9 PRO 7940HS

### GPU

780M

### ROCm Version

5.7.0

### ROCm Component

rocBLAS

### Steps to Reproduce

Expect rocblas to work with gpu arch gfx1103

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
  Name:                    AMD Ryzen 9 PRO 7940HS w/ Radeon 780M Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 PRO 7940HS w/ Radeon 780M Graphics
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
  Max Clock Freq. (MHz):   4000                               
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
      Size:                    65025468(0x3e035bc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65025468(0x3e035bc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65025468(0x3e035bc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1103                            
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
    L1:                      32(0x20) KB                        
    L2:                      2048(0x800) KB                     
  Chip ID:                 5567(0x15bf)                       
  ASIC Revision:           9(0x9)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2799                               
  BDFID:                   49920                              
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
  Packet Processor uCode:: 33                                 
  SDMA engine uCode::      16                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    524288(0x80000) KB                 
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS:                     
      Size:                    524288(0x80000) KB                 
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
      Name:                    amdgcn-amd-amdhsa--gfx1103         
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