# [Issue]: Segmentation fault trying to use SD.next (torch)

- **Issue #:** 4516
- **State:** closed
- **Created:** 2025-03-20T11:00:45Z
- **Updated:** 2025-04-28T14:41:09Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4516

### Problem Description

I am trying to use `SD.next` with standard Torch implementation.
My `webui-user.sh` contains just:
```
mcon@ikea:~/LLaMaConda/SD.next/sdnext$ cat webui-user.sh 
TORCH_COMMAND="torch==2.4.1+rocm6.1 torchvision==0.19.1+rocm6.1 --index-url https://download.pytorch.org/whl/rocm6.1"
```
I try to start `SD.next`as:
```
HSA_OVERRIDE_GFX_VERSION=11.0.0 PYTORCH_ROCM_ARCH=gfx1100 GPU_DRIVER=rocm AMD_LOG_LEVEL=7 ./webui.sh --debug --use-rocm
```
This bombs with (full log in attach):
```
...
:3:hip_device_runtime.cpp   :636 : 339330727986 us: [pid:723435 tid:0x7eacacbe3140]  hipGetDevice ( 0x7ffd2b25908c ) 
:3:hip_device_runtime.cpp   :644 : 339330727989 us: [pid:723435 tid:0x7eacacbe3140] hipGetDevice: Returned hipSuccess : 
:3:hip_memory.cpp           :701 : 339330727995 us: [pid:723435 tid:0x7eacacbe3140]  hipMemcpyWithStream ( 0x7ea883000000, 0x39961840, 8, hipMemcpyHostToDevice, stream:<null> ) 
:3:rocdevice.cpp            :3030: 339330728010 us: [pid:723435 tid:0x7eacacbe3140] Number of allocated hardware queues with low priority: 0, with normal priority: 0, with high priority: 0, maximum per priority is: 4
:4:command.cpp              :348 : 339330765136 us: [pid:723435 tid:0x7eacacbe3140] Command (CopyHostToDevice) enqueued: 0x398b2490
Segmentation fault (core dumped)
```

[sdnext.log](https://github.com/user-attachments/files/19363520/sdnext.log)

### Operating System

OS: NAME="Linux Mint" VERSION="22.1 (Xia)"

### CPU

CPU:  model name	: AMD Ryzen 9 5950X 16-Core Processor

### GPU

GPU:    Name:                    gfx1102                               Marketing Name:          AMD Radeon™ RX 7600 XT                  Name:                    amdgcn-amd-amdhsa--gfx1102         

### ROCm Version

rocm-6.3.1

### ROCm Component

_No response_

### Steps to Reproduce

```
git clone https://github.com/vladmandic/sdnext.git
cd sdnext
echo 'TORCH_COMMAND="torch==2.4.1+rocm6.1 torchvision==0.19.1+rocm6.1 --index-url https://download.pytorch.org/whl/rocm6.1"' >webui-user.sh
HSA_OVERRIDE_GFX_VERSION=11.0.0 PYTORCH_ROCM_ARCH=gfx1100 GPU_DRIVER=rocm AMD_LOG_LEVEL=7 ./webui.sh --debug --use-rocm
```
NOTE: the `TORCH_COMMAND` line is what was advised by `SD.next` developers (see [this](https://github.com/vladmandic/sdnext/issues/3833)) but I get similar output also with other versions including the latest one.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
mcon@ikea:~/LLaMaConda/SD.next/sdnext$ /opt/rocm/bin/rocminfo --support
ROCk module version 6.10.5 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.14
Runtime Ext Version:     1.6
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
  Name:                    AMD Ryzen 9 5950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 5950X 16-Core Processor
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
  Max Clock Freq. (MHz):   3400                               
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
      Size:                    65762040(0x3eb72f8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65762040(0x3eb72f8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65762040(0x3eb72f8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65762040(0x3eb72f8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1102                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon™ RX 7600 XT           
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
  Chip ID:                 29824(0x7480)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2493                               
  BDFID:                   11520                              
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
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
  Packet Processor uCode:: 412                                
  SDMA engine uCode::      21                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16760832(0xffc000) KB              
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
      Name:                    amdgcn-amd-amdhsa--gfx1102         
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