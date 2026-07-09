# [Issue]: HIP error on rocm/pytorch docker (gfx 1100) for float tensors

- **Issue #:** 2950
- **State:** closed
- **Created:** 2024-03-06T19:38:38Z
- **Updated:** 2024-05-14T04:04:42Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon Pro W7900
- **URL:** https://github.com/ROCm/ROCm/issues/2950

### Problem Description

I'm trying to use my AMD Radeon Pro W7900 to train ML models. I'm using the latest docker image provided to run rocm smoothly with python, despite rocm-smi and rocminfo identifying the gpu connected, python throws the following error when loading and printing a tensor from the gpu.

```
RuntimeError: HIP error: the operation cannot be performed in the present state
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.
```
What's odd is that int64 tensors work perfectly fine.

The host is Ubuntu 22.04 but the docker image is Ubuntu 20.04.

see how to reproduce the error below.

### Operating System

Ubuntu 20.04 LTS (Focal Fossa)

### CPU

12th Gen Intel Core i7-1260P

### GPU

AMD Radeon Pro W7900

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

Pulling and running the latest rocm/pytorch docker container as of 03/06/2024.
```
$ python
>>> import torch
>>> x = torch.tensor([34, 5, 20, 3], dtype=torch.int64, device='cuda')
>>> x # works fine
tensor([34,  5, 20,  3], device='cuda:0')
>>> x = torch.tensor([34, 5, 20, 3], dtype=torch.float32, device='cuda')
>>> x # breaks
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/_tensor.py", line 431, in __repr__
    return torch._tensor_str._str(self, tensor_contents=tensor_contents)
  File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/_tensor_str.py", line 664, in _str
    return _str_intern(self, tensor_contents=tensor_contents)
  File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/_tensor_str.py", line 595, in _str_intern
    tensor_str = _tensor_str(self, indent)
  File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/_tensor_str.py", line 347, in _tensor_str
    formatter = _Formatter(get_summarized_data(self) if summarize else self)
  File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/_tensor_str.py", line 137, in __init__
    nonzero_finite_vals = torch.masked_select(
RuntimeError: HIP error: the operation cannot be performed in the present state
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.

```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

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
  Name:                    12th Gen Intel(R) Core(TM) i7-1260P
  Uuid:                    CPU-XX                             
  Marketing Name:          12th Gen Intel(R) Core(TM) i7-1260P
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
  Max Clock Freq. (MHz):   4700                               
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
      Size:                    32474808(0x1ef86b8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32474808(0x1ef86b8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32474808(0x1ef86b8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-75ef8983826798b1               
  Marketing Name:          AMD Radeon PRO W7900               
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
  Chip ID:                 29768(0x7448)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1760                               
  BDFID:                   2304                               
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
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
  Packet Processor uCode:: 550                                
  SDMA engine uCode::      19                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    47169536(0x2cfc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    47169536(0x2cfc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    47169536(0x2cfc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
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


### Additional Information

The gpu is connected to the system using a egpu (enclosure): Razer Core X Chroma.