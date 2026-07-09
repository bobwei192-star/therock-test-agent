# Ryzen APU can not run ROCm? ( clinfo segmentation fault core dumped)

- **Issue #:** 883
- **State:** closed
- **Created:** 2019-09-11T15:48:23Z
- **Updated:** 2020-10-06T11:06:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/883

HI, i bought PIcasso R5 laptop.
i have tried ROCm to install Ubuntu 18.04.

when i check up command as[ /opt/rocm/bin/rocminfo ], it works well.
but [ /opt/rocm/opencl/bin/x86_64/clinfo ] not working.

it shows message -  [ segmentation fault (core dumped) ]

AMD Ryzen Picasso can't run ROCm correctly?

dduzzi@dduzzi-HP-Laptop-15-db1xxx:~$ /opt/rocm/bin/rocminfo 
ROCk module is loaded
dduzzi is member of video group
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
  Name:                    AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
  Marketing Name:          AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
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
    L1:                      32(0x20) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2100                               
  BDFID:                   1280                               
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16776832(0xfffe80) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Marketing Name:          AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1200                               
  BDFID:                   1280                               
  Internal Node ID:        0                                  
  Compute Unit:            11                                 
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
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
  Max Waves Per CU:        160(0xa0)                          
  Max Work-item Per CU:    10240(0x2800)                      
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack    
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
