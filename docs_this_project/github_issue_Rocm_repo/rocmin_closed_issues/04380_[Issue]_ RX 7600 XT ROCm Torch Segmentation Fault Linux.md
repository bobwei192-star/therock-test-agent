# [Issue]: RX 7600 XT ROCm Torch Segmentation Fault Linux

- **Issue #:** 4380
- **State:** closed
- **Created:** 2025-02-15T02:02:25Z
- **Updated:** 2026-01-16T14:33:30Z
- **Labels:** Under Investigation, ROCm 6.2.1
- **URL:** https://github.com/ROCm/ROCm/issues/4380

### Problem Description

Whenever I attempt to use my GPU with pytorch, it produces a Segmentation Fault.  From the information I could find online, it seemed this was the best place to ask for guidance.

### Operating System

Nobara Linux 41 6.13.2-200

### CPU

AMD Ryzen 5 5500

### GPU

AMD RX 6700 XT

### ROCm Version

ROCm 6.2.1

### ROCm Component

_No response_

### Steps to Reproduce

```python
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
x = torch.randn(1000, 1000).to(device)
y = torch.randn(1000, 1000).to(device)
z = x @ y
print("Computation successful on:", device)
```
Environment Variables:
export HSA_OVERRIDE_GFX_VERSION=11.0.0
export PYTORCH_HIP_ALLOC_CONF=garbage_collection_threshold:0.6,max_split_size_mb:512
export HIP_VISIBLE_DEVICES=0
export ROCR_VISIBLE_DEVICES=0
export AMD_SERIALIZE_KERNEL=3 
export AMD_LOG_LEVEL=4
export PYTORCH_HIP_LAUNCH_BLOCKING=1 

Result:
python /opt/ComfyUI/torchtensortest.py
:3:rocdevice.cpp            :468 : 95707883831 us: [pid:2117053 tid:0x7ca06301e740] Initializing HSA stack.
:3:rocdevice.cpp            :528 : 95708205307 us: [pid:2117053 tid:0x7ca06301e740] Enumerated GPU agents = 1
:3:rocdevice.cpp            :234 : 95708205346 us: [pid:2117053 tid:0x7ca06301e740] Numa selects cpu agent[0]=0x64f8b9e88fd0(fine=0x64f8bd2f6e30,coarse=0x64f8b6927f00) for gpu agent=0x64f8b695fc80 CPU<->GPU XGMI=0
:3:comgrctx.cpp             :33  : 95708205356 us: [pid:2117053 tid:0x7ca06301e740] Loading COMGR library.
:3:rocdevice.cpp            :1772: 95708205576 us: [pid:2117053 tid:0x7ca06301e740] Gfx Major/Minor/Stepping: 11/0/0
:3:rocdevice.cpp            :1774: 95708205582 us: [pid:2117053 tid:0x7ca06301e740] HMM support: 1, XNACK: 0, Direct host access: 0
:3:rocdevice.cpp            :1776: 95708205586 us: [pid:2117053 tid:0x7ca06301e740] Max SDMA Read Mask: 0x3, Max SDMA Write Mask: 0x3
:4:rocdevice.cpp            :2169: 95708205884 us: [pid:2117053 tid:0x7ca06301e740] Allocate hsa host memory 0x7c9d13200000, size 0x101000, numa_node = 0
:4:rocdevice.cpp            :2169: 95708207333 us: [pid:2117053 tid:0x7ca06301e740] Allocate hsa host memory 0x7c9d13000000, size 0x101000, numa_node = 0
:4:rocdevice.cpp            :2169: 95708208980 us: [pid:2117053 tid:0x7ca06301e740] Allocate hsa host memory 0x7c9d12a00000, size 0x400000, numa_node = 0
:4:rocdevice.cpp            :2169: 95708209154 us: [pid:2117053 tid:0x7ca06301e740] Allocate hsa host memory 0x7ca053e71000, size 0x38, numa_node = 0
:4:runtime.cpp              :83  : 95708209272 us: [pid:2117053 tid:0x7ca06301e740] init
:3:hip_context.cpp          :49  : 95708209279 us: [pid:2117053 tid:0x7ca06301e740] Direct Dispatch: 1
:1:hip_fatbin.cpp           :255 : 95708404069 us: [pid:2117053 tid:0x7ca06301e740] Cannot find CO in the bundle /usr/local/lib64/python3.13/site-packages/torch/lib/libhipblaslt.so for ISA: amdgcn-amd-amdhsa--gfx1100
:1:hip_fatbin.cpp           :109 : 95708404081 us: [pid:2117053 tid:0x7ca06301e740] Missing CO for these ISAs - 
:1:hip_fatbin.cpp           :112 : 95708404085 us: [pid:2117053 tid:0x7ca06301e740]      amdgcn-amd-amdhsa--gfx1100
:3:hip_platform.cpp         :703 : 95708404094 us: [pid:2117053 tid:0x7ca06301e740] init: Returned hipErrorNoBinaryForGpu : continue parsing remaining modules
:1:hip_fatbin.cpp           :255 : 95708416541 us: [pid:2117053 tid:0x7ca06301e740] Cannot find CO in the bundle /usr/local/lib64/python3.13/site-packages/torch/lib/libhipblaslt.so for ISA: amdgcn-amd-amdhsa--gfx1100
:1:hip_fatbin.cpp           :109 : 95708416551 us: [pid:2117053 tid:0x7ca06301e740] Missing CO for these ISAs - 
:1:hip_fatbin.cpp           :112 : 95708416554 us: [pid:2117053 tid:0x7ca06301e740]      amdgcn-amd-amdhsa--gfx1100
:3:hip_platform.cpp         :703 : 95708416560 us: [pid:2117053 tid:0x7ca06301e740] init: Returned hipErrorNoBinaryForGpu : continue parsing remaining modules
:1:hip_fatbin.cpp           :255 : 95708417569 us: [pid:2117053 tid:0x7ca06301e740] Cannot find CO in the bundle /usr/local/lib64/python3.13/site-packages/torch/lib/libhipblaslt.so for ISA: amdgcn-amd-amdhsa--gfx1100
:1:hip_fatbin.cpp           :109 : 95708417574 us: [pid:2117053 tid:0x7ca06301e740] Missing CO for these ISAs - 
:1:hip_fatbin.cpp           :112 : 95708417576 us: [pid:2117053 tid:0x7ca06301e740]      amdgcn-amd-amdhsa--gfx1100
:3:hip_platform.cpp         :703 : 95708417580 us: [pid:2117053 tid:0x7ca06301e740] init: Returned hipErrorNoBinaryForGpu : continue parsing remaining modules
:3:hip_device_runtime.cpp   :638 : 95708470502 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDeviceCount ( 0x7ffc61b146ac ) 
:3:hip_device_runtime.cpp   :640 : 95708470518 us: [pid:2117053 tid:0x7ca06301e740] hipGetDeviceCount: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :638 : 95708475286 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDeviceCount ( 0x7ffc61b140b0 ) 
:3:hip_device_runtime.cpp   :640 : 95708475294 us: [pid:2117053 tid:0x7ca06301e740] hipGetDeviceCount: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :638 : 95708475311 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDeviceCount ( 0x7c9f8fda56bc ) 
:3:hip_device_runtime.cpp   :640 : 95708475317 us: [pid:2117053 tid:0x7ca06301e740] hipGetDeviceCount: Returned hipSuccess : 
:3:hip_device.cpp           :471 : 95708475323 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevicePropertiesR0600 ( 0x7ffc61b13ba8, 0 ) 
:3:hip_device.cpp           :473 : 95708475327 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevicePropertiesR0600: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708475344 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b13c8c ) 
:3:hip_device_runtime.cpp   :631 : 95708475348 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :638 : 95708475352 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDeviceCount ( 0x7ffc61b13bdc ) 
:3:hip_device_runtime.cpp   :640 : 95708475356 us: [pid:2117053 tid:0x7ca06301e740] hipGetDeviceCount: Returned hipSuccess : 
:3:hip_context.cpp          :340 : 95708475571 us: [pid:2117053 tid:0x7ca06301e740]  hipDevicePrimaryCtxGetState ( 0, 0x7ffc61b13ca8, 0x7ffc61b13cac ) 
:3:hip_context.cpp          :354 : 95708475578 us: [pid:2117053 tid:0x7ca06301e740] hipDevicePrimaryCtxGetState: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708475583 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b13cdc ) 
:3:hip_device_runtime.cpp   :631 : 95708475587 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_context.cpp          :340 : 95708475592 us: [pid:2117053 tid:0x7ca06301e740]  hipDevicePrimaryCtxGetState ( 0, 0x7ffc61b13cf8, 0x7ffc61b13cfc ) 
:3:hip_context.cpp          :354 : 95708475595 us: [pid:2117053 tid:0x7ca06301e740] hipDevicePrimaryCtxGetState: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708475604 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b13c7c ) 
:3:hip_device_runtime.cpp   :631 : 95708475608 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_context.cpp          :340 : 95708475612 us: [pid:2117053 tid:0x7ca06301e740]  hipDevicePrimaryCtxGetState ( 0, 0x7ffc61b13c98, 0x7ffc61b13c9c ) 
:3:hip_context.cpp          :354 : 95708475617 us: [pid:2117053 tid:0x7ca06301e740] hipDevicePrimaryCtxGetState: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708476119 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b14364 ) 
:3:hip_device_runtime.cpp   :631 : 95708476126 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708476185 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b135a4 ) 
:3:hip_device_runtime.cpp   :631 : 95708476190 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708476195 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b13464 ) 
:3:hip_device_runtime.cpp   :631 : 95708476199 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708476210 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b1327c ) 
:3:hip_device_runtime.cpp   :631 : 95708476214 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_stream.cpp           :404 : 95708476223 us: [pid:2117053 tid:0x7ca06301e740]  hipDeviceGetStreamPriorityRange ( 0x7ffc61b13230, 0x7ffc61b13250 ) 
:3:hip_stream.cpp           :412 : 95708476228 us: [pid:2117053 tid:0x7ca06301e740] hipDeviceGetStreamPriorityRange: Returned hipSuccess : 
:3:hip_error.cpp            :36  : 95708476240 us: [pid:2117053 tid:0x7ca06301e740]  hipGetLastError (  ) 
:3:hip_device_runtime.cpp   :623 : 95708476245 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b12b1c ) 
:3:hip_device_runtime.cpp   :631 : 95708476248 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_graph.cpp            :826 : 95708476257 us: [pid:2117053 tid:0x7ca06301e740]  hipStreamIsCapturing ( stream:<null>, 0x7ffc61b12d90 ) 
:3:hip_graph.cpp            :827 : 95708476263 us: [pid:2117053 tid:0x7ca06301e740] hipStreamIsCapturing: Returned hipSuccess : 
:3:hip_memory.cpp           :599 : 95708476271 us: [pid:2117053 tid:0x7ca06301e740]  hipMalloc ( 0x7ffc61b12e80, 20971520 ) 
:4:rocdevice.cpp            :2310: 95708476552 us: [pid:2117053 tid:0x7ca06301e740] Allocate hsa device memory 0x7c9d11200000, size 0x1400000
:3:rocdevice.cpp            :2349: 95708476558 us: [pid:2117053 tid:0x7ca06301e740] device=0x64f8bd30b450, freeMem_ = 0x3fdc00000
:3:hip_memory.cpp           :601 : 95708476566 us: [pid:2117053 tid:0x7ca06301e740] hipMalloc: Returned hipSuccess : 0x7c9d11200000: duration: 295 us
:3:hip_device_runtime.cpp   :653 : 95708476581 us: [pid:2117053 tid:0x7ca06301e740]  hipSetDevice ( 0 ) 
:3:hip_device_runtime.cpp   :657 : 95708476585 us: [pid:2117053 tid:0x7ca06301e740] hipSetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :653 : 95708476589 us: [pid:2117053 tid:0x7ca06301e740]  hipSetDevice ( 0 ) 
:3:hip_device_runtime.cpp   :657 : 95708476592 us: [pid:2117053 tid:0x7ca06301e740] hipSetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708476636 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b134d4 ) 
:3:hip_device_runtime.cpp   :631 : 95708476640 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :623 : 95708476644 us: [pid:2117053 tid:0x7ca06301e740]  hipGetDevice ( 0x7ffc61b132ec ) 
:3:hip_device_runtime.cpp   :631 : 95708476649 us: [pid:2117053 tid:0x7ca06301e740] hipGetDevice: Returned hipSuccess : 
:3:hip_memory.cpp           :685 : 95708476659 us: [pid:2117053 tid:0x7ca06301e740]  hipMemcpyWithStream ( 0x7c9d11200000, 0x7c9d1262f040, 4000000, hipMemcpyHostToDevice, stream:<null> ) 
:3:rocdevice.cpp            :2925: 95708476672 us: [pid:2117053 tid:0x7ca06301e740] number of allocated hardware queues with low priority: 0, with normal priority: 0, with high priority: 0, maximum per priority is: 4
:4:command.cpp              :347 : 95708513211 us: [pid:2117053 tid:0x7ca06301e740] Command (CopyHostToDevice) enqueued: 0x64f8bd6213e0
Segmentation fault (core dumped)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
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
  Name:                    AMD Ryzen 5 5500                   
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 5500                   
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
  Max Clock Freq. (MHz):   4267                               
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
      Size:                    65622308(0x3e95124) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65622308(0x3e95124) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65622308(0x3e95124) KB             
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
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 7600 XT              
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
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2539                               
  BDFID:                   768                                
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
  Packet Processor uCode:: 462                                
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

```python
import torch
print("CUDA Available:", torch.cuda.is_available())
print("CUDA Device Count:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))
    print("Current Device:", torch.cuda.current_device())
```
Output:
```
CUDA Available: True
CUDA Device Count: 1
GPU Name: AMD Radeon RX 7600 XT
Current Device: 0
```

```python
import torch
device = "cpu"  # Force CPU mode
x = torch.randn(1000, 1000).to(device)
y = torch.randn(1000, 1000).to(device)
z = x @ y
print("Computation successful on:", device)
```
Output:
` Computation successful on: cpu `

`sudo dnf list --installed | grep rocm`
Output:

![Image](https://github.com/user-attachments/assets/a6640ecd-7b12-4249-b137-97d1bd056b84)

Other Notes:

Removed Mesa clinfo package
Same result with 6.12.11-204 kernel