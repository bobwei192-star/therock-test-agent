# [Issue]: Is there a ROCm version that supports gfx1151?

- **Issue #:** 4499
- **State:** open
- **Created:** 2025-03-14T11:44:36Z
- **Updated:** 2025-06-03T20:37:12Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4499

### Problem Description

When I build the Pytorch with ROCm6.3.4,there are many errors!
[29/616] cd /home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels && /home/moon/miniconda3/envs/ktransformers/lib/python3.12/site-packages/cmake/data/bin/cmake -E make_directory /home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels/. && /home/moon/miniconda3/envs/ktransformers/lib/python3.12/site-packages/cmake/data/bin/cmake -D verbose:BOOL=OFF -D build_configuration:STRING=RELEASE -D generated_file:STRING=/home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels/./torch_hip_generated_bgemm_kernel_bf16bf16bf16_256_16x256x64_16x16_1x4_8x16x1_8x16x1_1x16x1x16_4_Intrawave_v2.hip.o -P /home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels/torch_hip_generated_bgemm_kernel_bf16bf16bf16_256_16x256x64_16x16_1x4_8x16x1_8x16x1_1x16x1x16_4_Intrawave_v2.hip.o.cmake
FAILED: caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels/torch_hip_generated_bgemm_kernel_bf16bf16bf16_256_16x256x64_16x16_1x4_8x16x1_8x16x1_1x16x1x16_4_Intrawave_v2.hip.o /home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels/torch_hip_generated_bgemm_kernel_bf16bf16bf16_256_16x256x64_16x16_1x4_8x16x1_8x16x1_1x16x1x16_4_Intrawave_v2.hip.o 
cd /home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels && /home/moon/miniconda3/envs/ktransformers/lib/python3.12/site-packages/cmake/data/bin/cmake -E make_directory /home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels/. && /home/moon/miniconda3/envs/ktransformers/lib/python3.12/site-packages/cmake/data/bin/cmake -D verbose:BOOL=OFF -D build_configuration:STRING=RELEASE -D generated_file:STRING=/home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels/./torch_hip_generated_bgemm_kernel_bf16bf16bf16_256_16x256x64_16x16_1x4_8x16x1_8x16x1_1x16x1x16_4_Intrawave_v2.hip.o -P /home/moon/kt/pytorch/build/caffe2/CMakeFiles/torch_hip.dir/__/aten/src/ATen/native/hip/bgemm_kernels/torch_hip_generated_bgemm_kernel_bf16bf16bf16_256_16x256x64_16x16_1x4_8x16x1_8x16x1_1x16x1x16_4_Intrawave_v2.hip.o.cmake
In file included from /home/moon/kt/pytorch/aten/src/ATen/native/hip/bgemm_kernels/bgemm_kernel_bf16bf16bf16_256_16x256x64_16x16_1x4_8x16x1_8x16x1_1x16x1x16_4_Intrawave_v2.hip:3:
In file included from /home/moon/kt/pytorch/aten/src/ATen/native/hip/bgemm_kernels/bgemm_kernel_template.h:11:
In file included from /home/moon/kt/pytorch/aten/src/ATen/../../../third_party/composable_kernel/include/ck/tensor_operation/gpu/device/impl/device_batched_gemm_multiple_d_xdl_cshuffle_v3.hpp:9:
In file included from /home/moon/kt/pytorch/aten/src/ATen/../../../third_party/composable_kernel/include/ck/utility/common_header.hpp:36:
/home/moon/kt/pytorch/aten/src/ATen/../../../third_party/composable_kernel/include/ck/utility/amd_buffer_addressing.hpp:32:48: error: use of undeclared identifier 'CK_BUFFER_RESOURCE_3RD_DWORD'
   32 |     wave_buffer_resource.config(Number<3>{}) = CK_BUFFER_RESOURCE_3RD_DWORD;
      |                                                ^
/home/moon/kt/pytorch/aten/src/ATen/../../../third_party/composable_kernel/include/ck/utility/amd_buffer_addressing.hpp:47:48: error: use of undeclared identifier 'CK_BUFFER_RESOURCE_3RD_DWORD'
   47 |     wave_buffer_resource.config(Number<3>{}) = CK_BUFFER_RESOURCE_3RD_DWORD;
      |                                                ^


### Operating System

NAME="Ubuntu" VERSION="22.04.5 LTS (Jammy Jellyfish)"

### CPU

AMD Eng Sample: 100-000001243-50_Y

### GPU

 amdgcn-amd-amdhsa--gfx1151   

### ROCm Version

ROCm 6.3.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

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
  Name:                    AMD Eng Sample: 100-000001243-50_Y 
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Eng Sample: 100-000001243-50_Y 
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
  Max Clock Freq. (MHz):   5172                               
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
      Size:                    131015728(0x7cf2430) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    131015728(0x7cf2430) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131015728(0x7cf2430) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131015728(0x7cf2430) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1151                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon Graphics                
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
    L3:                      16384(0x4000) KB                   
  Chip ID:                 5510(0x1586)                       
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2799                               
  BDFID:                   50432                              
  Internal Node ID:        1                                  
  Compute Unit:            40                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       APU
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
  Packet Processor uCode:: 25                                 
  SDMA engine uCode::      14                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65507864(0x3e79218) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65507864(0x3e79218) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx1151         
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

_No response_