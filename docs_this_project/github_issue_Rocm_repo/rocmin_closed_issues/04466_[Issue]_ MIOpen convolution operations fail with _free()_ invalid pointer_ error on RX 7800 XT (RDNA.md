# [Issue]: MIOpen convolution operations fail with 'free(): invalid pointer' error on RX 7800 XT (RDNA 3/gfx11xx)

- **Issue #:** 4466
- **State:** closed
- **Created:** 2025-03-08T06:45:30Z
- **Updated:** 2025-05-26T19:37:01Z
- **Labels:** Under Investigation, ROCm 6.3.4
- **URL:** https://github.com/ROCm/ROCm/issues/4466

### Problem Description

When using PyTorch with ROCm on my AMD Radeon RX 7800 XT (RDNA 3/gfx11xx architecture), any convolution operations result in a "free(): invalid pointer" error and program crash. The issue appears to be related to the absence of precompiled kernel packages for RDNA 3 GPUs in the current ROCm 6.3 release.
Simple matrix operations and basic custom CNNs work correctly, but any model using standard CNN architectures like ResNet, VGG, or MobileNetV2 crashes during the forward pass at the convolution operations.

### Operating System

OS: NAME="Ubuntu" VERSION="24.04 (Noble Numbat)"

### CPU

model name      : 13th Gen Intel(R) Core(TM) i5-13600KF

### GPU

AMD Radeon RX 7800 XT                    

### ROCm Version

6.3.4

### ROCm Component

MIOpen

### Steps to Reproduce

Attempt to load and run a pretrained model with convolution operations
Create a minimal test case as follows:

import os
import torch
import torch.nn as nn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

device = torch.device("cuda")
logger.info(f"Using device: {device}")

# Test with simple CNN components
class ComponentTestCNN(nn.Module):
    def __init__(self):
        super(ComponentTestCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        
    def forward(self, x):
        return self.conv1(x)

# Test components
model = ComponentTestCNN().to(device)
x = torch.randn(1, 3, 64, 64, device=device)

# This line causes "free(): invalid pointer" crash
y = model(x)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

bruno@PC:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
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
  Name:                    13th Gen Intel(R) Core(TM) i5-13600KF
  Uuid:                    CPU-XX                             
  Marketing Name:          13th Gen Intel(R) Core(TM) i5-13600KF
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
  Max Clock Freq. (MHz):   5100                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            20                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    65664792(0x3e9f718) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65664792(0x3e9f718) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65664792(0x3e9f718) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65664792(0x3e9f718) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1101                            
  Uuid:                    GPU-6a249ead25ccfaeb               
  Marketing Name:          AMD Radeon RX 7800 XT              
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
    L3:                      65536(0x10000) KB                  
  Chip ID:                 29822(0x747e)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2169                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            60                                 
  SIMDs per CU:            2                                  
  Shader Engines:          3                                  
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
  Packet Processor uCode:: 550                                
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
      Name:                    amdgcn-amd-amdhsa--gfx1101         
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
bruno@PC:~$ 

### Additional Information

**No packages for RDNA 3 (gfx11xx) are available, which appears to be the root cause of the issue.**

$ apt-cache search miopen-hip | grep kdb
miopen-hip-gfx1030kdb - AMD DNN Library
miopen-hip-gfx1030kdb-rpath6.3.4 - AMD DNN Library
miopen-hip-gfx1030kdb6.3.4 - AMD DNN Library
miopen-hip-gfx900kdb - AMD DNN Library
miopen-hip-gfx900kdb-rpath6.3.4 - AMD DNN Library
miopen-hip-gfx900kdb6.3.4 - AMD DNN Library
miopen-hip-gfx906kdb - AMD DNN Library
miopen-hip-gfx906kdb-rpath6.3.4 - AMD DNN Library
miopen-hip-gfx906kdb6.3.4 - AMD DNN Library
miopen-hip-gfx908kdb - AMD DNN Library
miopen-hip-gfx908kdb-rpath6.3.4 - AMD DNN Library
miopen-hip-gfx908kdb6.3.4 - AMD DNN Library
miopen-hip-gfx90akdb - AMD DNN Library
miopen-hip-gfx90akdb-rpath6.3.4 - AMD DNN Library
miopen-hip-gfx90akdb6.3.4 - AMD DNN Library
miopen-hip-gfx942kdb - AMD DNN Library
miopen-hip-gfx942kdb-rpath6.3.4 - AMD DNN Library
miopen-hip-gfx942kdb6.3.4 - AMD DNN Library

**Installed MIOpen Packages**
$ apt list --installed | grep miopen
miopen-hip-dev6.3.4/noble,now 3.3.0.60304-76~24.04 amd64 [installed,automatic]
miopen-hip6.3.4/noble,now 3.3.0.60304-76~24.04 amd64 [installed,automatic]

**My Pytorch/ROCm details:**
$ python3 -c "import torch; print(torch.__version__); print(torch.version.hip)"
2.7.0.dev20250306+rocm6.3
6.3.42131-fa1d09cbd

**The exact Error message**
free(): invalid pointer
Aborted (core dumped)

**I've tried various MIOpen environment variable settings including:**

MIOPEN_DEBUG_CONV_DIRECT=0
MIOPEN_DEBUG_CONV_GEMM=1
MIOPEN_FIND_ENFORCE=3
MIOPEN_DEBUG_CONV_IMPLICIT_GEMM=1
MIOPEN_FIND_MODE=NORMAL
MIOPEN_DEBUG_CONV_WINOGRAD=0

None of these resolved the issue, suggesting the fundamental problem is the missing architecture support in MIOpen for RDNA 3 GPUs.
A workaround that allows me to continue development is to use a custom CNN implementation that avoids complex convolution operations, but this severely limits the architectures that can be used effectively.
