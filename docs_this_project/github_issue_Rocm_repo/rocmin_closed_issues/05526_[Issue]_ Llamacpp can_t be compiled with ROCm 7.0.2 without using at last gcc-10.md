# [Issue]: Llamacpp can't be compiled with ROCm 7.0.2 without using at last gcc-10

- **Issue #:** 5526
- **State:** closed
- **Created:** 2025-10-16T07:45:48Z
- **Updated:** 2025-11-11T16:13:34Z
- **Labels:** status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5526

### Problem Description

I am trying to compile llamacpp with ROCm 7.0 with the official Almalinux container and if I use gcc-8 that comes with Almalinux it won't compile:

```
[ 66%] Linking CXX executable ../bin/test-regex-partial
[ 67%] Linking CXX executable ../bin/test-thread-safety
/usr/bin/ld: ../common/libcommon.a(arg.cpp.o): undefined reference to symbol '_ZNSt10filesystem6statusERKNS_7__cxx114pathE'
/opt/rocm-7.0.2/lib/librocsolver.so.0: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
gmake[2]: *** [tests/CMakeFiles/test-thread-safety.dir/build.make:119: bin/test-thread-safety] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:2431: tests/CMakeFiles/test-thread-safety.dir/all] Error 2
gmake[1]: *** Waiting for unfinished jobs....
[ 68%] Building CXX object tests/CMakeFiles/test-opt.dir/get-model.cpp.o
[ 68%] Linking CXX executable ../bin/test-chat-template
[ 68%] Built target test-regex-partial
[ 68%] Building CXX object tests/CMakeFiles/test-gguf.dir/get-model.cpp.o
[ 68%] Linking CXX executable ../bin/test-arg-parser
/usr/bin/ld: ../common/libcommon.a(arg.cpp.o): undefined reference to symbol '_ZNSt10filesystem6statusERKNS_7__cxx114pathE'
/opt/rocm-7.0.2/lib/librocsolver.so.0: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
gmake[2]: *** [tests/CMakeFiles/test-arg-parser.dir/build.make:119: bin/test-arg-parser] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:2463: tests/CMakeFiles/test-arg-parser.dir/all] Error 2
[ 68%] Linking CXX executable ../bin/test-gguf
[ 68%] Linking CXX executable ../bin/test-opt
[ 68%] Built target test-chat-template
[ 68%] Built target test-gguf
[ 68%] Built target test-opt
[ 68%] Linking CXX executable ../bin/test-quantize-stats
[ 69%] Linking CXX executable ../bin/test-json-partial
[ 69%] Built target test-quantize-stats
[ 69%] Built target test-json-partial
[ 69%] Linking CXX executable ../bin/test-grammar-integration
[ 69%] Built target test-grammar-integration
[ 69%] Linking CXX executable ../bin/test-chat-parser
[ 69%] Built target test-chat-parser
[ 70%] Linking CXX executable ../bin/test-json-schema-to-grammar
[ 70%] Built target test-json-schema-to-grammar
[ 70%] Linking CXX executable ../bin/test-chat
[ 70%] Built target test-chat
gmake: *** [Makefile:146: all] Error 2

```

If I use gcc-14 with gcc-toolset-14 it will compile and it will also work

### Operating System

Almalinux 8.10

### CPU

AMD Ryzen 5 7600 6-Core Processor

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

ROCm 7.0.2

### ROCm Component

rocSOLVER

### Steps to Reproduce

```
HIPCXX="$(hipconfig -l)/clang" HIP_PATH="$(hipconfig -R)" \
  cmake -S . -B build -DGGML_HIP=ON -DLLAMA_CURL=OFF -DGGML_HIP_ROCWMMA_FATTN=ON -DGPU_TARGETS=gfx1201 -DCMAKE_BUILD_TYPE=Release \
  && cmake --build build --config Release -- -j$(nproc)
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

/opt/rocm/bin/rocminfo --support

```

ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.11
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
  Name:                    AMD Ryzen 5 7600 6-Core Processor  
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 7600 6-Core Processor  
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
  Max Clock Freq. (MHz):   5392                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            12                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32449904(0x1ef2570) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32449904(0x1ef2570) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32449904(0x1ef2570) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32449904(0x1ef2570) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-979f676c0389f9bf               
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
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30032(0x7550)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2400                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 108                                
  SDMA engine uCode::      662                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16695296(0xfec000) KB              
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
      Name:                    amdgcn-amd-amdhsa--gfx1201         
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
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx12-generic   
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
```

### Additional Information

_No response_