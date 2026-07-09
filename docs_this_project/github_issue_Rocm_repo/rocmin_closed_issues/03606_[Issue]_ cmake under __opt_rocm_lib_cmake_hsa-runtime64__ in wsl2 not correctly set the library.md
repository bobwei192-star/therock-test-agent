# [Issue]: cmake under "/opt/rocm/lib/cmake/hsa-runtime64/" in wsl2 not correctly set the library

- **Issue #:** 3606
- **State:** closed
- **Created:** 2024-08-17T01:02:51Z
- **Updated:** 2024-08-21T14:20:49Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XT, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3606

### Problem Description

using rocm under WSL2.
install following instruct under https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html.

when I tried build llama.cpp using cmake, I got an error:

 CMake Error at /opt/rocm/lib/cmake/hsa-runtime64/hsa-runtime64Targets.cmake:80 (message):
 The imported target "hsa-runtime64::hsa-runtime64" references the file
         /opt/rocm/lib/libhsa-runtime64.so.1.13.60103
        but this file does not exist.  Possible reasons include:
...

then llama.cpp will failed to build.

but when I use makefile, everything is OK.

I list the lib in `/opt/rocm/lib/` but only got `libhsa-runtime64.so.1.2`, so I replace all `1.13.60103` to  `1.2` in  `/opt/rocm/lib/cmake/hsa-runtime64`, then cmake check passed and build success.

I want to know this is a common issue or just an install error? 


### Operating System

22.04.4 LTS (Jammy Jellyfish) under Windows 10.0.22631

### CPU

AMD Ryzen 7 7700

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.1.0

### ROCm Component

rocm-cmake

### Steps to Reproduce

1. setup wsl2
2. install rocm using `amdgpu-install -y --usecase=wsl,rocm --no-dkms`
3. install llama.cpp-python using `CC=hipcc CXX=hipcc CMAKE_ARGS="-DGGML_HIPBLAS=on" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir`, using cmake to build llama.cpp is also affected
4. cmake will report the error
5. execute `ls /opt/rocm/lib/`, only got 'libhsa-runtime64.so.1.2'
6. modify cmake under /opt/rocm/lib/cmake/hsa-runtime64
7. build passed


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          NO

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    CPU                                
  Uuid:                    CPU-XX                             
  Marketing Name:          CPU                                
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
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    15841624(0xf1b958) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    15841624(0xf1b958) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Marketing Name:          AMD Radeon RX 7900 XT              
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        16(0x10)                           
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      6144(0x1800) KB                    
    L3:                      81920(0x14000) KB                  
  Chip ID:                 29772(0x744c)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2075                               
  Internal Node ID:        1                                  
  Compute Unit:            84                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
  Shader Arrs. per Eng.:   2                                  
  Coherent Host Access:    FALSE                              
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
  Packet Processor uCode:: 2250                               
  SDMA engine uCode::      20                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    20906156(0x13f00ac) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
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

### Additional Information

windows driver version is 24.7.1