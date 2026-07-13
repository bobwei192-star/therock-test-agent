# [Issue]: segmentation fault calling hipStreamSynchronize

- **Issue #:** 4751
- **State:** closed
- **Created:** 2025-05-18T08:34:51Z
- **Updated:** 2025-10-07T21:48:23Z
- **Labels:** Under Investigation, ROCm 6.2.4, ROCm 6.3.2
- **URL:** https://github.com/ROCm/ROCm/issues/4751

### Problem Description

On a Radeon Pro W7800 (`gfx1100`), calling `hipLaunchHostFunc` or `hipStreamAddCallback` more than ~53000 times on a stream causes a subsequent `hipStreamSynchronize` to crash with a segmentation fault.

Up to 52000 operations seem to work.
More than 53000 operations always fail.
Other values in between fail of succeed seemingly at random.

See the test program below to reproduce the issue.

On an Instinct MI250X the same test program works correctly, tested up to 1000000 operations.

Another symptom is that the call stack looks corrupted: running the test program in `gdb` and looking at the stack trace after the segmentation fault yields an infinite repetition of:
```
#0  0x00007ffff6762651 in amd::Command::releaseResources() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#1  0x00007ffff650a186 in amd::Command::terminate() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#2  0x00007ffff6771ab0 in amd::ReferenceCountedObject::release() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#3  0x00007ffff676267c in amd::Command::releaseResources() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#4  0x00007ffff650a186 in amd::Command::terminate() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#5  0x00007ffff6771ab0 in amd::ReferenceCountedObject::release() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#6  0x00007ffff676267c in amd::Command::releaseResources() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#7  0x00007ffff650a186 in amd::Command::terminate() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#8  0x00007ffff6771ab0 in amd::ReferenceCountedObject::release() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#9  0x00007ffff676267c in amd::Command::releaseResources() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
#10 0x00007ffff650a186 in amd::Command::terminate() () from /opt/rocm-6.4.0/lib/llvm/bin/../../../lib/libamdhip64.so.6
...
```



### Operating System

Red Hat Enterprise Linux 8.10

### CPU

AMD EPYC 9454 (×2)

### GPU

AMD Radeon PRO W7800

### ROCm Version

5.7.1, 6.2.4, 6.3.2, 6.4.0

### ROCm Component

HIP

### Steps to Reproduce

1. Save this as `test.cc`:
```c++
// C++ standard headers
#include <cassert>
#include <cstdlib>
#include <iostream>

// ROCm headers
#include <hip/hip_runtime.h>

#define HIP_CHECK(ARG, ...) assert((ARG) == hipSuccess) 

int main(int argc, char** argv)
{
    int reps = 55000;
    if (argc > 1) {
        reps = std::atoi(argv[1]);
    }

    std::cout << "select the first device... " << std::flush;
    HIP_CHECK(hipSetDevice(0));
    std::cout << "done" << std::endl;

    std::cout << "create the stream... " << std::flush;
    hipStream_t queue;
    HIP_CHECK(hipStreamCreate(&queue));
    std::cout << "done" << std::endl;

    std::cout << "enqueue " << reps << " host functions" << std::endl;
    for (int i = 0; i < reps; i++) {
        if (i % 1000 == 0) {
          std::cout << "... enqueued " << i << " host functions ..." << std::endl;
        }
        HIP_CHECK(hipLaunchHostFunc(
            queue,
            [](void*) {},
            nullptr)
        );
    }
    std::cout << "... enqueued " << reps << " host functions ..." << std::endl;
    std::cout << "done" << std::endl;

    std::cout << "synchronise the stream... " << std::flush;
    // if reps > ~53000, this calls causes a segmentation fault 
    HIP_CHECK(hipStreamSynchronize(queue));
    std::cout << "done" << std::endl;

    std::cout << "destroy the stream... " << std::flush;
    HIP_CHECK(hipStreamDestroy(queue));
    std::cout << "done" << std::endl;

    std::cout << "reset the device... " << std::flush;
    HIP_CHECK(hipDeviceReset());
    std::cout << "done" << std::endl;

    std::cout << "all done" << std::endl;
}
```

2. Compile with
```bash
/opt/rocm/bin/hipcc -O2 -g --offload-arch=gfx1100 test.cc -o test
```

3. Run with
```bash
./test
```

4. I get
```
select the first device... done
create the stream... done
enqueue 55000 host functions
... enqueued 0 host functions ...
... enqueued 1000 host functions ...
... enqueued 2000 host functions ...
... enqueued 3000 host functions ...
... enqueued 4000 host functions ...
... enqueued 5000 host functions ...
... enqueued 6000 host functions ...
... enqueued 7000 host functions ...
... enqueued 8000 host functions ...
... enqueued 9000 host functions ...
... enqueued 10000 host functions ...
... enqueued 11000 host functions ...
... enqueued 12000 host functions ...
... enqueued 13000 host functions ...
... enqueued 14000 host functions ...
... enqueued 15000 host functions ...
... enqueued 16000 host functions ...
... enqueued 17000 host functions ...
... enqueued 18000 host functions ...
... enqueued 19000 host functions ...
... enqueued 20000 host functions ...
... enqueued 21000 host functions ...
... enqueued 22000 host functions ...
... enqueued 23000 host functions ...
... enqueued 24000 host functions ...
... enqueued 25000 host functions ...
... enqueued 26000 host functions ...
... enqueued 27000 host functions ...
... enqueued 28000 host functions ...
... enqueued 29000 host functions ...
... enqueued 30000 host functions ...
... enqueued 31000 host functions ...
... enqueued 32000 host functions ...
... enqueued 33000 host functions ...
... enqueued 34000 host functions ...
... enqueued 35000 host functions ...
... enqueued 36000 host functions ...
... enqueued 37000 host functions ...
... enqueued 38000 host functions ...
... enqueued 39000 host functions ...
... enqueued 40000 host functions ...
... enqueued 41000 host functions ...
... enqueued 42000 host functions ...
... enqueued 43000 host functions ...
... enqueued 44000 host functions ...
... enqueued 45000 host functions ...
... enqueued 46000 host functions ...
... enqueued 47000 host functions ...
... enqueued 48000 host functions ...
... enqueued 49000 host functions ...
... enqueued 50000 host functions ...
... enqueued 51000 host functions ...
... enqueued 52000 host functions ...
... enqueued 53000 host functions ...
... enqueued 54000 host functions ...
... enqueued 55000 host functions ...
done
synchronise the stream... Segmentation fault (core dumped)
```

**Note**: running `./test 52000` completes successfully:
```
select the first device... done
create the stream... done
enqueue 52000 host functions
... enqueued 0 host functions ...
... enqueued 1000 host functions ...
... enqueued 2000 host functions ...
...
... enqueued 51000 host functions ...
... enqueued 52000 host functions ...
done
synchronise the stream... done
destroy the stream... done
reset the device... done
all done
```

The segmentation fault starts to happen between 52000 and 53000 operations.


**Note**: the same test works fine on an Instinct MI250X, tested up to 100k operations. 

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support
```
ROCk module version 6.12.12 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.15
Runtime Ext Version:     1.7
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
[... skipping CPU agents ...]
*******                  
Agent 9                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-c6afa01f760b6075               
  Marketing Name:          AMD Radeon PRO W7800               
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    8                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
  Chip ID:                 29790(0x745e)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1895                               
  BDFID:                   768                                
  Internal Node ID:        8                                  
  Compute Unit:            70                                 
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
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 542                                
  SDMA engine uCode::      24                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    31440896(0x1dfc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    31440896(0x1dfc000) KB             
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
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
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
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             
```

### Additional Information

_No response_