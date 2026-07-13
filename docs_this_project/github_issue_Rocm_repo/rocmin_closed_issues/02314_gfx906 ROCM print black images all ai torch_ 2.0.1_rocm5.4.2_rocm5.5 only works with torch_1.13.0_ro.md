# gfx906 ROCM print black images all ai torch: 2.0.1+rocm5.4.2/rocm5.5 only works with torch=1.13.0+rocm5.2

- **Issue #:** 2314
- **State:** closed
- **Created:** 2023-07-04T00:54:12Z
- **Updated:** 2023-09-25T20:34:04Z
- **Labels:** application:pytorch, aimodel:stablediffusion
- **URL:** https://github.com/ROCm/ROCm/issues/2314

Let me summary my problem ( full of it in github links I open multi of them but can't get answer or fix)
I tried my gfx906 Radeon VII card with webui and invoke ai its working with torch==1.13.0+rocm5.2 but with torch==2.0.1+rocm5.4.2 I just got problem as black render. But it work with lots people but in my case I couldn't work it in my case.

Here my history of this:
https://github.com/pytorch/pytorch/issues/103973
https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/9206
https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/10873

At this point I am stuck with out dated pytorch.
Also my card still in rocm support list but my card
https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html

I tried with
directly from rocm https://rocm.docs.amd.com/ 5.5.1/5.6 both of them failed
from https://www.amd.com/en/support/linux-drivers Radeon™ Pro Software for Enterprise on Ubuntu 22.04.1 Installer Revision Number 23.Q1 Release Date 4/27/2023 (Also there is no Ubuntu 22.04.2 and I am using Ubuntu 22.04.2)

python: 3.10.6
working version:
pip install torch==1.13.0+rocm5.2 torchvision==0.14.0+rocm5.2 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/rocm5.2
Not working
pip install torch==2.0.1+rocm5.4.2 torchvision==0.15.2+rocm5.4.2 --index-url https://download.pytorch.org/whl/rocm5.4.2
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm5.5

```
bcansin@BCANSINSMAINUBUNTU:~$ apt show rocm-libs -a
Package: rocm-libs
Version: 5.6.0.50600-67~22.04
Priority: optional
Section: devel
Maintainer: ROCm Libs Support <rocm-libs.support@amd.com>
Installed-Size: 13,3 kB
Depends: hipblas (= 1.0.0.50600-67~22.04), hipblaslt (= 0.2.0.50600-67~22.04), hipfft (= 1.0.12.50600-67~22.04), hipsolver (= 1.8.0.50600-67~22.04), hipsparse (= 2.3.6.50600-67~22.04), miopen-hip (= 2.20.0.50600-67~22.04), rccl (= 2.16.5.50600-67~22.04), rocalution (= 2.1.9.50600-67~22.04), rocblas (= 3.0.0.50600-67~22.04), rocfft (= 1.0.23.50600-67~22.04), rocrand (= 2.10.17.50600-67~22.04), rocsolver (= 3.22.0.50600-67~22.04), rocsparse (= 2.5.2.50600-67~22.04), rocm-core (= 5.6.0.50600-67~22.04), hipblas-dev (= 1.0.0.50600-67~22.04), hipblaslt-dev (= 0.2.0.50600-67~22.04), hipcub-dev (= 2.13.1.50600-67~22.04), hipfft-dev (= 1.0.12.50600-67~22.04), hipsolver-dev (= 1.8.0.50600-67~22.04), hipsparse-dev (= 2.3.6.50600-67~22.04), miopen-hip-dev (= 2.20.0.50600-67~22.04), rccl-dev (= 2.16.5.50600-67~22.04), rocalution-dev (= 2.1.9.50600-67~22.04), rocblas-dev (= 3.0.0.50600-67~22.04), rocfft-dev (= 1.0.23.50600-67~22.04), rocprim-dev (= 2.13.0.50600-67~22.04), rocrand-dev (= 2.10.17.50600-67~22.04), rocsolver-dev (= 3.22.0.50600-67~22.04), rocsparse-dev (= 2.5.2.50600-67~22.04), rocthrust-dev (= 2.18.0.50600-67~22.04), rocwmma-dev (= 1.1.0.50600-67~22.04)
Homepage: https://github.com/RadeonOpenCompute/ROCm
Download-Size: 1.010 B
APT-Sources: https://repo.radeon.com/rocm/apt/5.6 jammy/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime software stack

bcansin@BCANSINSMAINUBUNTU:~$ rocminfo
ROCk module is loaded
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
  Name:                    AMD FX(tm)-9590 Eight-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD FX(tm)-9590 Eight-Core Processor
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
    L1:                      16384(0x4000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4700                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32757548(0x1f3d72c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32757548(0x1f3d72c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32757548(0x1f3d72c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx906                             
  Uuid:                    GPU-be60788172fd5d3e               
  Marketing Name:          AMD Radeon VII                     
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
    L1:                      16(0x10) KB                        
    L2:                      8192(0x2000) KB                    
  Chip ID:                 26287(0x66af)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1801                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            60                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
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
      Size:                    16760832(0xffc000) KB              
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
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
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