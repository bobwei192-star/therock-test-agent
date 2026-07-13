# [Issue]: hipMallocAsync / hipMallocFromPoolAsync fail (OOM / segfault) on gfx1100/gfx1101 + ROCm 7.x

- **Issue #:** 6178
- **State:** closed
- **Created:** 2026-04-23T07:52:28Z
- **Updated:** 2026-05-11T07:01:37Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6178

### Problem Description

`hipMallocAsync` and `hipMallocFromPoolAsync` return `hipErrorOutOfMemory` (or segfault) on **gfx1100/gfx1101** with ROCm 7.x (AMD Radeon RX 7800 XT, AMD Radeon RX 7900 XTX). The synchronous `hipMalloc` works correctly on the same devices and allocation size.

### Additional context

- Works correctly with ROCm 6.4.x on the same hardware.
- Regression introduced in ROCm 7.x.
- Impacts downstream projects that rely on stream-ordered allocations (e.g. [AMDGPU.jl](https://github.com/JuliaGPU/AMDGPU.jl)); see https://github.com/JuliaGPU/AMDGPU.jl/issues/901

### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

AMD Ryzen 7 5800X 8-Core Processor

### GPU

AMD Radeon RX 7800 XT, AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 7.2.2

### ROCm Component

_No response_

### Steps to Reproduce

Compile and run:

```bash
hipcc -o debug_rocm debug_rocm.cpp && ./debug_rocm
```

<details>
<summary>debug_rocm.cpp</summary>

```cpp
#include <hip/hip_runtime.h>
#include <cstdio>
#include <cstdint>

#define CHECK(cmd) do {                                         \
    hipError_t e = (cmd);                                       \
    if (e != hipSuccess) {                                      \
        printf("FAIL [%s]: %s\n", #cmd, hipGetErrorString(e));  \
        return 1;                                               \
    }                                                           \
} while(0)

int main() {
    hipDeviceProp_t prop;
    CHECK(hipGetDeviceProperties(&prop, 0));
    printf("Device: %s  arch: %s\n\n", prop.name, prop.gcnArchName);

    hipStream_t stream;
    CHECK(hipStreamCreate(&stream));

    // TEST 1: hipMalloc (synchronous) — expected to work
    {
        void* ptr = nullptr;
        hipError_t e = hipMalloc(&ptr, 64);
        printf("[hipMalloc]              %s\n", (e == hipSuccess && ptr) ? "OK" : hipGetErrorString(e));
        if (ptr) (void)hipFree(ptr);
    }

    // TEST 2: hipMallocAsync
    {
        void* ptr = nullptr;
        hipError_t e = hipMallocAsync(&ptr, 64, stream);
        (void)hipStreamSynchronize(stream);
        printf("[hipMallocAsync]         %s\n", (e == hipSuccess && ptr) ? "OK" : hipGetErrorString(e));
        if (ptr) { (void)hipFreeAsync(ptr, stream); (void)hipStreamSynchronize(stream); }
    }

    // TEST 3: hipMallocFromPoolAsync
    {
        hipMemPoolProps pool_props{};
        pool_props.allocType     = hipMemAllocationTypePinned;
        pool_props.location.type = hipMemLocationTypeDevice;
        pool_props.location.id   = 0;
        hipMemPool_t pool;
        CHECK(hipMemPoolCreate(&pool, &pool_props));

        void* ptr = nullptr;
        hipError_t e = hipMallocFromPoolAsync(&ptr, 64, pool, stream);
        (void)hipStreamSynchronize(stream);
        printf("[hipMallocFromPoolAsync] %s\n", (e == hipSuccess && ptr) ? "OK" : hipGetErrorString(e));
        if (ptr) { (void)hipFreeAsync(ptr, stream); (void)hipStreamSynchronize(stream); }
        (void)hipMemPoolDestroy(pool);
    }

    (void)hipStreamDestroy(stream);
    return 0;
}
```

</details>

### Observed output

```
Device: <name>  arch: gfx1100

[hipMalloc]              OK
[hipMallocAsync]         out of memory
[hipMallocFromPoolAsync] out of memory
```

### Expected output

All three tests print `OK`.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
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
VMM Support:             NO

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 5800X 8-Core Processor 
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 5800X 8-Core Processor 
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
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32753972(0x1f3c934) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32753972(0x1f3c934) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32753972(0x1f3c934) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32753972(0x1f3c934) KB             
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
  Uuid:                    GPU-444b93155e506d02               
  Marketing Name:          AMD Radeon RX 7900 XTX             
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
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2526                               
  BDFID:                   2816                               
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
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
  Packet Processor uCode:: 602                                
  SDMA engine uCode::      27                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB             
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
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

Seems to work okay on a gfx1030

```
user@machine ~> ./debug_pool
Device: AMD Radeon RX 6800 XT  arch: gfx1030

[hipMalloc]             OK
[hipMallocAsync]        OK
[hipMallocFromPoolAsync] OK
 
user@machine ~> hipcc --version
HIP version: 7.2.53211-9999
AMD clang version 22.0.0git (/srcdest/rocm-llvm f58b06dce1f9c15707c5f808fd002e18c2accf7e)
Target: x86_64-pc-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/lib/llvm/bin
```