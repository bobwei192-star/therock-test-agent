# [Issue]: can't build rocm examples 

> **Issue #2639**
> **状态**: closed
> **创建时间**: 2023-11-13T10:07:27Z
> **更新时间**: 2024-02-20T07:35:03Z
> **关闭时间**: 2023-11-13T17:59:56Z
> **作者**: bog-dan-ro
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2639

## 描述

### Problem Description

I can not compile any hip samples, it seems either I didn't install something or the sdk is missing something.
These are the rocm packages that I have installed:
```
# dpkg -l | grep -i rocm
ii  comgr                                      2.5.0.50701-98~22.04                    amd64        Library to provide support functions for ROCm code objects.
ii  hipfft                                     1.0.12.50701-98~22.04                   amd64        ROCm FFT marshalling library
ii  hipfft-dev                                 1.0.12.50701-98~22.04                   amd64        ROCm FFT marshalling library
ii  hsa-rocr                                   1.11.0.50701-98~22.04                   amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime for Boltzmann (ROCm) platforms
ii  libhsa-runtime-dev                         5.0.0-1ubuntu0.1                        amd64        HSA Runtime API and runtime for ROCm - development files
ii  libhsa-runtime64-1                         5.0.0-1ubuntu0.1                        amd64        HSA Runtime API and runtime for ROCm
ii  rccl                                       2.17.1.50701-98~22.04                   amd64        ROCm Communication Collectives Library
ii  rccl-dev                                   2.17.1.50701-98~22.04                   amd64        ROCm Communication Collectives Library
ii  rocblas                                    3.1.0.50701-98~22.04                    amd64        rocBLAS is AMD's library for BLAS on ROCm. It is implemented in HIP and optimized for AMD GPUs.
ii  rocblas-dev                                3.1.0.50701-98~22.04                    amd64        rocBLAS is AMD's library for BLAS on ROCm. It is implemented in HIP and optimized for AMD GPUs.
ii  rocfft                                     1.0.23.50701-98~22.04                   amd64        ROCm FFT library
ii  rocfft-dev                                 1.0.23.50701-98~22.04                   amd64        ROCm FFT library
ii  rocm-clang-ocl                             0.5.0.50701-98~22.04                    amd64        OpenCL compilation with clang compiler.
ii  rocm-cmake                                 0.10.0.50701-98~22.04                   amd64        rocm-cmake built using CMake
ii  rocm-core                                  5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-dbgapi                                0.70.1.50701-98~22.04                   amd64        Library to provide AMD GPU debugger API
ii  rocm-debug-agent                           2.0.3.50701-98~22.04                    amd64        Radeon Open Compute Debug Agent (ROCdebug-agent)
ii  rocm-dev                                   5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                           1.0.0.50701-98~22.04                    amd64        Radeon Open Compute - device libraries
ii  rocm-gdb                                   13.2.50701-98~22.04                     amd64        ROCgdb
ii  rocm-hip-libraries                         5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-runtime                           5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-runtime-dev                       5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-sdk                               5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-language-runtime                      5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-llvm                                  17.0.0.23382.50701-98~22.04             amd64        ROCm compiler
ii  rocm-ml-libraries                          5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-ml-sdk                                5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-ocl-icd                               2.0.0.50701-98~22.04                    amd64        clr built using CMake
ii  rocm-opencl                                2.0.0.50701-98~22.04                    amd64        clr built using CMake
ii  rocm-opencl-dev                            2.0.0.50701-98~22.04                    amd64        clr built using CMake
ii  rocm-opencl-runtime                        5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl-sdk                            5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-openmp-sdk                            5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) OpenMP Software development Kit.
ii  rocm-smi-lib                               5.0.0.50701-98~22.04                    amd64        AMD System Management libraries
ii  rocm-utils                                 5.7.1.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                                   1.0.0.50701-98~22.04                    amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool
ii  rocsolver                                  3.23.0.50701-98~22.04                   amd64        AMD ROCm SOLVER library

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

hip

### Steps to Reproduce

```
root@ubuntu:/opt/rocm/share/hip/samples/0_Intro/square# make
/opt/rocm//hip/bin/hipify-perl square.cu > square.cpp
/opt/rocm//hip/bin/hipcc  square.cpp -o square.out
In file included from <built-in>:1:
In file included from /opt/rocm-5.7.1/llvm/lib/clang/17.0.0/include/__clang_hip_runtime_wrapper.h:50:
/opt/rocm-5.7.1/llvm/lib/clang/17.0.0/include/cuda_wrappers/cmath:27:15: fatal error: 'cmath' file not found
#include_next <cmath>
              ^~~~~~~
1 error generated when compiling for gfx1100.
make: *** [Makefile:44: square.out] Error 1
```

```
root@ubuntu:/opt/rocm/share/hip/samples/0_Intro/square# 
root@ubuntu:/opt/rocm/share/hip/samples/0_Intro/square/b# cmake ..
-- The C compiler identification is GNU 11.4.0
-- The CXX compiler identification is GNU 11.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- hip::amdhip64 is SHARED_LIBRARY
-- /usr/bin/c++: CLANGRT compiler options not supported.
-- Configuring done
-- Generating done
-- Build files have been written to: /opt/rocm/share/hip/samples/0_Intro/square/b
root@ubuntu:/opt/rocm/share/hip/samples/0_Intro/square/b# make
[ 50%] Building CXX object CMakeFiles/square.dir/square.cpp.o
In file included from <built-in>:1:
In file included from /opt/rocm-5.7.1/llvm/lib/clang/17.0.0/include/__clang_hip_runtime_wrapper.h:50:
/opt/rocm-5.7.1/llvm/lib/clang/17.0.0/include/cuda_wrappers/cmath:27:15: fatal error: 'cmath' file not found
#include_next <cmath>
              ^~~~~~~
1 error generated when compiling for gfx1100.
make[2]: *** [CMakeFiles/square.dir/build.make:76: CMakeFiles/square.dir/square.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:83: CMakeFiles/square.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
```


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
      Size:                    65564048(0x3e86d90) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65564048(0x3e86d90) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65564048(0x3e86d90) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-0003d08c00000000               
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
