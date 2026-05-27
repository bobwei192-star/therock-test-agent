# hipErrorNoBinaryForGpu: Unable to find code object for all current devices!

> **Issue #1867**
> **状态**: closed
> **创建时间**: 2022-11-25T20:30:59Z
> **更新时间**: 2024-02-16T16:43:11Z
> **关闭时间**: 2024-02-16T16:43:11Z
> **作者**: Martinc4321
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1867

## 描述

Context:
Want to use tensorflow-rocm to train and run some model.
Ubuntu 22.04.1 LTS with ROCm 5.3.3

Before you tell me it is not supported for my GPU I managed to run it on 
Ubuntu 20.04 and ROCm 5.2.0 (on official tensorflow image and sharing my GPU in docker) and using ENV var: `export HSA_OVERRIDE_GFX_VERSION=10.3.0` (It is described here [discusion in another issue](https://github.com/RadeonOpenCompute/ROCm/issues/1713#issuecomment-1327860841))

However when I use same `export HSA_OVERRIDE_GFX_VERSION=10.3.0` now I get this message:
```
Memory access fault by GPU node-1 (Agent handle: 0x562ca9677860) on address 0x7efbeeedc000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)
```

This is my GPU:
```
*-display                 
       description: VGA compatible controller
       product: Navi 10 [Radeon RX 5600 OEM/5600 XT / 5700/5700 XT]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:28:00.0
       logical name: /dev/fb0
       version: c4
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom fb
       configuration: depth=32 driver=amdgpu latency=0 resolution=2560,1080
       resources: irq:92 memory:d0000000-dfffffff memory:e0000000-e01fffff ioport:e000(size=256) memory:fcd00000-fcd7ffff memory:c0000-dffff
```
`rockminfo`:
```
ROCk module is loaded
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
  Name:                    AMD Ryzen 7 3700X 8-Core Processor 
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 3700X 8-Core Processor 
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
  Max Clock Freq. (MHz):   3600                               
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
      Size:                    82289060(0x4e7a1a4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    82289060(0x4e7a1a4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    82289060(0x4e7a1a4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1010                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 5700                 
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
    L2:                      4096(0x1000) KB                    
  Chip ID:                 29471(0x731f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1750                               
  BDFID:                   10240                              
  Internal Node ID:        1                                  
  Compute Unit:            36                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
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
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    1280(0x500)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1010:xnack-  
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
```
`hipconfig --full` :
```
HIP version  : 5.3.22062-659cc197

== hipconfig
HIP_PATH     : /opt/rocm-5.3.3
ROCM_PATH    : /opt/rocm-5.3.3
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/opt/rocm-5.3.3/include -I/opt/rocm-5.3.3/llvm/bin/../lib/clang/15.0.0 -I/opt/rocm-5.3.3/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm-5.3.3/hsa
HIP_CLANG_PATH   : /opt/rocm-5.3.3/llvm/bin
AMD clang version 15.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.3.3 22414 b4eabb4b000fedc027fe0075b2b1ea4becc5d6bd)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-5.3.3/llvm/bin
AMD LLVM version 15.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver2

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags :  -std=c++11 -isystem "/opt/rocm-5.3.3/llvm/lib/clang/15.0.0/include/.." -isystem /opt/rocm-5.3.3/hsa/include -isystem "/opt/rocm-5.3.3/include" -O3
hip-clang-ldflags  :  -L"/opt/rocm-5.3.3/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/home/conto/.local/bin:/home/conto/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin:/home/conto/.dotnet/tools:/opt/rocm/bin:/opt/rocm/rocprofiler/bin:/opt/rocm/opencl/bin:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/:/opt/rocm/bin:/opt/rocm/rocprofiler/bin:/opt/rocm/opencl/bin:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/

== Linux Kernel
Hostname     : conto-MS-7B85
Linux conto-MS-7B85 5.15.0-53-generic #59-Ubuntu SMP Mon Oct 17 18:53:30 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.1 LTS
Release:        22.04
Codename:       jammy
```

---

## 评论 (5 条)

### 评论 #1 — Martinc4321 (2022-11-25T20:34:50Z)

I am happy to help, to provide any information or run test, so it is possible to make support for my GPU once again in some newer version.

---

### 评论 #2 — YellowRoseCx (2023-02-19T03:01:02Z)

did you ever figure out a way around this?

---

### 评论 #3 — Apisteftos (2023-02-23T22:47:07Z)

I have the same issue with my RX 480 without overriding the GPU, on Ubuntu 22.04 and with ROCm 5.3.3

---

### 评论 #4 — abhimeda (2024-01-30T04:05:55Z)

@Martinc4321  Hi, is this resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #5 — nartmada (2024-02-16T16:43:11Z)

Closing the ticket as no response from @Martinc4321.  Please re-open the ticket if your issue still exists with latest ROCm 6.0.2.  Thanks.

---
