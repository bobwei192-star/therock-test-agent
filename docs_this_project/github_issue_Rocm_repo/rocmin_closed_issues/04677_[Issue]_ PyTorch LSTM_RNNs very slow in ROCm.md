# [Issue]: PyTorch LSTM/RNNs very slow in ROCm

- **Issue #:** 4677
- **State:** closed
- **Created:** 2025-04-23T22:50:21Z
- **Updated:** 2025-05-21T19:42:02Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4677

### Problem Description

When running LSTM, the speed is extremely slow compared to an equivalent, or even _much lesser_ NVIDIA GPU. Discovered while trying to train a reimplementation of Tacotron 2. Asked o3 to make me an LSTM speed test script and tested it in 

### RTX 3080 Ti, Win10
```
PS C:\Users\REDACTED\Internal Docs\Code-Proj> python .\lstm_speed_test.py
Using device: cuda
C:\Users\REDACTED\AppData\Local\Programs\Python\Python39\lib\site-packages\torch\onnx\_internal\_beartype.py:35: UserWarning: unhashable type: 'list'
  warnings.warn(f"{e}")
C:\Users\REDACTED\AppData\Local\Programs\Python\Python39\lib\site-packages\onnxscript\function_libs\torch_lib\graph_building.py:23: UserWarning: unhashable type: 'list'
  from onnxscript._internal import param_manipulation, runtime_typing
Dataset size: 50000  |  Steps/epoch: 196  |  Total params: 0.06 M
Epoch  1 ▸ 1.261s  (0.0064s / step, 39,779 seq/s)
Epoch  2 ▸ 1.091s  (0.0056s / step, 45,976 seq/s)
Epoch  3 ▸ 1.043s  (0.0053s / step, 48,114 seq/s)
Epoch  4 ▸ 1.060s  (0.0054s / step, 47,347 seq/s)
Epoch  5 ▸ 1.110s  (0.0057s / step, 45,212 seq/s)

Finished 5 epochs (250,000 sequences) in 5.57s → 44,916 sequences/s overall.
```

### MI300X, Ubuntu
```
root@enc1-gpuvm013:/var/lib/jenkins# python lstm_speed_test.py 
/var/lib/jenkins/lstm_speed_test.py:120: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  scaler = torch.cuda.amp.GradScaler(enabled=args.amp)
Using device: cuda
Dataset size: 50000  |  Steps/epoch: 196  |  Total params: 0.06 M
/var/lib/jenkins/lstm_speed_test.py:65: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with torch.cuda.amp.autocast(args.amp), torch.no_grad():
/var/lib/jenkins/lstm_speed_test.py:79: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with torch.cuda.amp.autocast(args.amp):
Epoch  1 ▸ 10.382s  (0.0530s / step, 4,833 seq/s)
Epoch  2 ▸ 3.525s  (0.0180s / step, 14,233 seq/s)
Epoch  3 ▸ 3.619s  (0.0185s / step, 13,864 seq/s)
Epoch  4 ▸ 3.654s  (0.0186s / step, 13,731 seq/s)
Epoch  5 ▸ 3.841s  (0.0196s / step, 13,063 seq/s)

Finished 5 epochs (250,000 sequences) in 25.02s → 9,991 sequences/s overall.
```
To investigate further, I ran the profiler on both* and printed the 30 most latency consuming ops after finishing the passes
### CUDA
![Image](https://github.com/user-attachments/assets/b8562699-3d6d-4775-9f98-caced80e2021)
### ROCm
![Image](https://github.com/user-attachments/assets/ca0f7dff-6386-414e-9551-8e73446ee41c)

My observation is that PyTorch w/CUDA ships with a dedicated CuDNN kernel for RNNs, while ROCm does everything naively. 

*: The MI300X machine has ROCm 6.4 and enabling the profiler on that one made the backwards pass error out. So the profiler image is from another with a 7900XTX w/ ROCm 6.3 - which gets a similar speed in the benchmark.

### Operating System

22.04.5 LTS (Jammy Jellyfish)

### CPU

Intel(R) Xeon(R) Platinum 8470

### GPU

AMD Instinct MI300X VF

### ROCm Version

ROCm 6.4.0

### ROCm Component

_No response_

### Steps to Reproduce

1. Acquire pytorch-rocm docker image
2. Grab [this script](https://drive.google.com/file/d/1DyhQV_Y_zaMQhXLkaOfibR4OJxLwBRsL/view?usp=drive_link)
3. `python lstm_speed_test.py`


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
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Xeon(R) Platinum 8470     
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Platinum 8470     
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
  Max Clock Freq. (MHz):   0                                  
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            13                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    230893620(0xdc32834) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    230893620(0xdc32834) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    230893620(0xdc32834) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    230893620(0xdc32834) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx942                             
  Uuid:                    GPU-f91d9f93a2e6d19d               
  Marketing Name:          AMD Instinct MI300X VF             
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
    L2:                      4096(0x1000) KB                    
    L3:                      262144(0x40000) KB                 
  Chip ID:                 29877(0x74b5)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2100                               
  BDFID:                   1280                               
  Internal Node ID:        1                                  
  Compute Unit:            304                                
  SIMDs per CU:            4                                  
  Shader Engines:          32                                 
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    2048(0x800)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 177                                
  SDMA engine uCode::      24                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    200998912(0xbfb0000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    200998912(0xbfb0000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    200998912(0xbfb0000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
      Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-
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

Using JupyterLab and [this docker image](https://hub.docker.com/layers/rocm/pytorch/rocm6.4_ubuntu22.04_py3.10_pytorch_release_2.6.0/images/sha256-130536fdfceb374626a7bcb8d00b9d796ddfc3115677d51229e5b852d96b5ef4)