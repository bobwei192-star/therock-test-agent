# [Issue]: memory visibility for host-pinned buffer in graph host node

- **Issue #:** 6343
- **State:** open
- **Created:** 2026-06-10T17:15:31Z
- **Updated:** 2026-06-10T18:54:05Z
- **Labels:** status: triage
- **Assignees:** mapatel-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6343

### Problem Description

Memory visibility issue for a graph in which a **device node** *writes* to a **host-pinned memory** location, after which a **host node** *reads* the value.

The expected behavior is that the host node reads the value written by the device node.

It used to work at least until ROCm 7.0.2. And, even with ROCM 7.2.4, it works with a device kernel, followed by a stream synchronization (see below reproducer).

It also works on CUDA (at least 12.8).

A potential fix is to add `__threadfence_system` after the device node store, which I'd rather avoid.

### Operating System

Ubuntu 24.04

### CPU

AMD Ryzen 9 9950X 16-Core Processor

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

ROCm 7.2.4

### ROCm Component

HIP

### Steps to Reproduce

This is the reproducer for HIP, typical output:
```bash
PASSED: Got expected value 42
FAILED: Expected 42, got 0
Aborted (core dumped)
```

<details>

```c++
#include <iostream>

#include "hip/hip_runtime.h"

#define CHECK_CALL(statement)                                                                                          \
    {                                                                                                                  \
        const auto error_code = statement;                                                                             \
        if (error_code != hipSuccess) {                                                                                \
            std::cerr << __FILE__ << ':' << __LINE__ << ": " << hipGetErrorString(error_code) << " (" << error_code    \
                      << ')' << std::endl;                                                                             \
            std::abort();                                                                                              \
        }                                                                                                              \
    }

__global__ void write_value(int* ptr) {
    *ptr = 42;
    // __threadfence_system();
}

void check_value(void* ptr) {
    constexpr int expected = 42;

    if (const auto value = *reinterpret_cast<int*>(ptr); value != expected) {
        std::cerr << "FAILED: Expected " << expected << ", got " << value << std::endl;
        std::abort();
    }
    std::cout << "PASSED: Got expected value " << expected << std::endl;
}

int main() {
    //! Allocate pinned memory (accessible by both device and host).
    int* data;
    CHECK_CALL(hipHostAlloc(&data, sizeof(int), hipHostAllocDefault));
    *data = 0;

    //! It works just fine with a device kernel. The stream synchronization seems to take care of the memory visibility issues.
    write_value<<<1, 1, 0, 0>>>(data);
    CHECK_CALL(hipStreamSynchronize(0));
    check_value(data);

    //! Reset to zero.
    *data = 0;

    hipGraph_t graph;
    CHECK_CALL(hipGraphCreate(&graph, 0));

    //! Device node that write to pinned memory.
    hipKernelNodeParams kernelParams{};
    void* kernelArgs[] = {&data};
    kernelParams.func = (void*) write_value;
    kernelParams.gridDim = dim3(1);
    kernelParams.blockDim = dim3(1);
    kernelParams.kernelParams = kernelArgs;
    hipGraphNode_t writeNode;
    CHECK_CALL(hipGraphAddKernelNode(&writeNode, graph, nullptr, 0, &kernelParams));

    //! Host node to read and verify the value written by the device node.
    hipHostNodeParams hostParams{};
    hostParams.fn = (hipHostFn_t) check_value;
    hostParams.userData = data;
    hipGraphNode_t checkNode;
    CHECK_CALL(hipGraphAddHostNode(&checkNode, graph, &writeNode, 1, &hostParams));

    //! For debugging.
    CHECK_CALL(hipGraphDebugDotPrint(graph, "graph.dot", hipGraphDebugDotFlagsVerbose));

    //! Launch the graph.
    hipGraphExec_t graphExec;
    CHECK_CALL(hipGraphInstantiate(&graphExec, graph, nullptr, nullptr, 0));
    CHECK_CALL(hipGraphLaunch(graphExec, nullptr));
    CHECK_CALL(hipDeviceSynchronize());

    //! Cleanup.
    CHECK_CALL(hipGraphExecDestroy(graphExec));
    CHECK_CALL(hipFreeHost(data));
    CHECK_CALL(hipGraphDestroy(graph));

    std::cout << "Test completed successfully." << std::endl;
    return 0;
}
```

</details>

This is the reproducer for CUDA, typical output:
```bash
PASSED: Got expected value 42
Test completed successfully.
```

<details>

```c++
#include "cuda_runtime.h"

#include <iostream>

#define CHECK_CALL(statement)                                                                                          \
    {                                                                                                                  \
        const auto error_code = statement;                                                                             \
        if (error_code != cudaSuccess) {                                                                               \
            std::cerr << __FILE__ << ':' << __LINE__ << ": " << cudaGetErrorString(error_code) << " (" << error_code   \
                      << ')' << std::endl;                                                                             \
            std::abort();                                                                                              \
        }                                                                                                              \
    }

__global__ void write_value(int* ptr) {
    *ptr = 42;
}

void check_value(void* ptr) {
    constexpr int expected = 42;

    if (const auto value = *reinterpret_cast<int*>(ptr); value != expected) {
        std::cerr << "FAILED: Expected " << expected << ", got " << value << std::endl;
        std::abort();
    }
    std::cout << "PASSED: Got expected value " << expected << std::endl;
}

int main() {
    //! Allocate pinned memory (accessible by both device and host).
    int* data;
    CHECK_CALL(cudaHostAlloc(&data, sizeof(int), cudaHostAllocDefault));
    *data = 0;

    cudaGraph_t graph;
    CHECK_CALL(cudaGraphCreate(&graph, 0));

    //!  Device node that write to pinned memory.
    cudaKernelNodeParams kernelParams{};
    void* kernelArgs[] = {&data};
    kernelParams.func = (void*) write_value;
    kernelParams.gridDim = dim3(1);
    kernelParams.blockDim = dim3(1);
    kernelParams.kernelParams = kernelArgs;
    cudaGraphNode_t writeNode;
    CHECK_CALL(cudaGraphAddKernelNode(&writeNode, graph, nullptr, 0, &kernelParams));

    //! Host node to read and verify the value written by the device node.
    cudaHostNodeParams hostParams{};
    hostParams.fn = (cudaHostFn_t) check_value;
    hostParams.userData = data;
    cudaGraphNode_t checkNode;
    CHECK_CALL(cudaGraphAddHostNode(&checkNode, graph, &writeNode, 1, &hostParams));

    //! Launch the graph.
    cudaGraphExec_t graphExec;
    CHECK_CALL(cudaGraphInstantiate(&graphExec, graph, nullptr, nullptr, 0));
    CHECK_CALL(cudaGraphLaunch(graphExec, nullptr));
    CHECK_CALL(cudaDeviceSynchronize());

    //! Cleanup.
    CHECK_CALL(cudaGraphExecDestroy(graphExec));
    CHECK_CALL(cudaFreeHost(data));
    CHECK_CALL(cudaGraphDestroy(graph));

    std::cout << "Test completed successfully." << std::endl;
    return 0;
}
```

</details>

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

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
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 9 9950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 9950X 16-Core Processor
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
    L1:                      49152(0xc000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5756                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    65470032(0x3e6fe50) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65470032(0x3e6fe50) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65470032(0x3e6fe50) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65470032(0x3e6fe50) KB             
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
  Uuid:                    GPU-8c487c8b9e3ccb7a               
  Marketing Name:          AMD Radeon RX 9070 XT              
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
  Packet Processor uCode:: 68                                 
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

</details>


### Additional Information

Joint work with @maartenarnst.