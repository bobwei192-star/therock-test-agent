# TensorFlow cannot allocate >4GB on RX-480 8GB

> **Issue #1206**
> **状态**: closed
> **创建时间**: 2020-08-26T11:33:57Z
> **更新时间**: 2020-09-14T09:19:59Z
> **关闭时间**: 2020-09-14T09:19:59Z
> **作者**: gsedej
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1206

## 描述

I have installed ROCm-TensorFlow 2.3 via pypi (pip) on Ubuntu 18.04 + kernel 5.4, rocm version 3.7
My GPU is Polaris 10, RX 480 8GB (Sapphire nitro+)

I can run basic TF sample (`python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`) using ROCm, but when I try to load my model, it fails
```
[TerminalIPythonApp] WARNING | Subcommand `ipython qtconsole` is deprecated and will be removed in future versions.
[TerminalIPythonApp] WARNING | You likely want to use `jupyter qtconsole` in the future
2020-08-26 12:38:10.399423: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
2020-08-26 12:38:10.414464: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:09:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.306GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 0B/s
2020-08-26 12:38:10.415639: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-26 12:38:10.416303: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-08-26 12:38:10.419893: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-08-26 12:38:10.420034: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-08-26 12:38:10.420150: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-08-26 12:38:49.082800: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2020-08-26 12:38:49.087009: I tensorflow/core/platform/profile_utils/cpu_utils.cc:104] CPU Frequency: 3593325000 Hz
2020-08-26 12:38:49.087371: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5ae8590 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-08-26 12:38:49.087380: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-08-26 12:38:49.088526: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5b3c170 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-08-26 12:38:49.088534: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Ellesmere [Radeon RX 470/480/570/570X/580/580X], AMDGPU ISA version: gfx803
2020-08-26 12:38:49.334271: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:09:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.306GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 0B/s
2020-08-26 12:38:49.334352: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-26 12:38:49.334374: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-08-26 12:38:49.334394: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-08-26 12:38:49.334412: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-08-26 12:38:49.334617: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-08-26 12:38:49.334642: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-08-26 12:38:49.334651: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      0 
2020-08-26 12:38:49.334658: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1276] 0:   N 
2020-08-26 12:38:49.334904: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1402] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7700 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X], pci bus id: 0000:09:00.0)
2020-08-26 12:39:27.932393: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-26 12:39:27.937286: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-26 12:39:29.109164: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-26 12:39:29.123620: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-26 12:39:29.125847: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-26 12:39:29.127728: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-26 12:39:29.264293: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-08-26 12:39:29.386881: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-26 12:39:29.680115: F tensorflow/stream_executor/rocm/rocm_dnn.cc:3527] Failed to allocate scratch memory - Requested memory size (6576668672) exceeds the max memory limit (4294967296).
	You can set the env var TF_CUDNN_WORKSPACE_LIMIT_IN_MB to a larger number (e.g. 8192) to increase the max memory limit.
	Increasing the max memory limit might help resolve this error
[JupyterQtConsoleApp] WARNING | kernel died: 3.002070903778076

```

My GPU has 8GB, but output says "exceeds the max memory limit (4294967296)."  The number also correlates with output of rocminfo:


```
$ /opt/rocm/bin/rocminfo
ROCk module is loaded
Able to open /dev/kfd read-write
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
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65864460(0x3ed030c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65864460(0x3ed030c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Ellesmere [Radeon RX 470/480/570/570X/580/580X]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26591(0x67df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1306                               
  BDFID:                   2304                               
  Internal Node ID:        1                                  
  Compute Unit:            36                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
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
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8388608(0x800000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx803          
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

The number tensorflow limit `max memory limit (4294967296)`  correlates with  ˙Grid Max Size:  4294967295(0xffffffff)             ˙

I have found similar output in this issue https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/pull/629

---

## 评论 (2 条)

### 评论 #1 — gsedej (2020-08-28T13:03:17Z)

I have tried another model, where I can set network size by size of input image.

I can run with size of 488 x 488 pixels it runs fine. By using `radeontop` I can see VRAM growth for ~4GB. I can even run 2 instances and it works fine. It takes almost all VRAM and even takes some GTT (system memory for gpu). Both instances works!

But if i try 512 x 512, the network loads. After output of `Epoch 1/100` I get following error :
```
Memory access fault by GPU node-1 (Agent handle: 0x62c7e10) on address 0x10f5c74000. Reason: Page not present or supervisor privilege.
```
the DMESG output:
```
[  +0,000005] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 146 0x03a0480c for process python pid 572 thread python pid 572
[  +0,000003] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x010F5C74
[  +0,000002] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x1004800C
[  +0,000002] amdgpu 0000:09:00.0: amdgpu: VM fault (0x0c, vmid 8, pasid 32771) at page 17783924, read from 'TC4' (0x54433400) (72)
[  +0,000009] amdgpu: Evicting PASID 0x8003 queues
[  +0,000001] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x0bb84402 for process python pid 572 thread python pid 572
[  +0,000002] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x00FF74FB
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x310C8002
[  +0,000002] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 16741627, write from 'TC2' (0x54433200) (200)
[  +0,000006] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x02e84802 for process python pid 572 thread python pid 572
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x011E6854
[  +0,000002] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10084002
[  +0,000001] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 18770004, read from 'TC7' (0x54433700) (132)
[  +0,000006] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x03784802 for process python pid 572 thread python pid 572
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x00F7492C
[  +0,000002] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10008002
[  +0,000001] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 16206124, read from 'TC0' (0x54433000) (8)
[  +0,000006] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x02104402 for process python pid 572 thread python pid 572
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x01288111
[  +0,000002] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10008002
[  +0,000001] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 19431697, read from 'TC0' (0x54433000) (8)
[  +0,000006] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x04204402 for process python pid 572 thread python pid 572
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x01098F78
[  +0,000002] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10044002
[  +0,000002] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 17403768, read from 'TC5' (0x54433500) (68)
[  +0,000005] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x02c04402 for process python pid 572 thread python pid 572
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x01265438
[  +0,000002] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10008002
[  +0,000001] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 19289144, read from 'TC0' (0x54433000) (8)
[  +0,000006] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x01788802 for process python pid 572 thread python pid 572
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x00FA33F1
[  +0,000002] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10008002
[  +0,000001] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 16397297, read from 'TC0' (0x54433000) (8)
[  +0,000006] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x0d3e0402 for process python pid 572 thread python pid 572
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x00FBC473
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x100C8002
[  +0,000002] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 16499827, read from 'TC2' (0x54433200) (200)
[  +0,000006] amdgpu 0000:09:00.0: amdgpu: GPU fault detected: 147 0x08e04402 for process python pid 572 thread python pid 572
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x011F829A
[  +0,000001] amdgpu 0000:09:00.0: amdgpu:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10004002
[  +0,000002] amdgpu 0000:09:00.0: amdgpu: VM fault (0x02, vmid 8, pasid 32771) at page 18842266, read from 'TC1' (0x54433100) (4)
[  +0,003547] amdgpu 0000:09:00.0: amdgpu: IH ring buffer overflow (0x000850C0, 0x00007380, 0x000050D0)
[  +0,105399] amdgpu: Started evicting pasid 0x8003
[  +0,000005] amdgpu: Finished evicting pasid 0x8003

```
The issue might be connected with MIOpen https://github.com/ROCmSoftwarePlatform/MIOpen and tensorflow-upsteream https://github.com/ROCmSoftwarePlatform/tensorflow-upstream

@sunway513 @parallelo maybe you have some idea?

_The "GPU fault" and "VM falit" might also indicate bad GDDR5 memory chips (the gpu is quite old now), but I tried running 12 instances of "Unigine Heaven" benchmark, the VRAM was fully utilized, but NO artifact was visible_

---

### 评论 #2 — gsedej (2020-09-14T09:19:59Z)

I am closing this issue (in ROCm), since there exists (tensorflow ) model, that can utilize full 8GB of vram. The issue in my model is probably in higher layers (tensorflow/miopen/hip) and not lower ROCm levels.

---
