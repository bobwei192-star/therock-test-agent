# [Bug] crash and invalid behaviour with DETR model on pytorch

> **Issue #1355**
> **状态**: closed
> **创建时间**: 2021-01-04T09:09:52Z
> **更新时间**: 2021-07-29T10:44:35Z
> **关闭时间**: 2021-07-29T10:44:34Z
> **作者**: nlgranger
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1355

## 描述

Running the DETR model from https://github.com/facebookresearch/detr leads to the following issues:
- ROCm spends a lot of time compiling kernels (clang processes spawning all the time and /tmp getting filled with temporary files, presumably the kernels).
- GPU memory usage is abnormally low for the selected batch size.
- Computations seem to be valid (no NaN showing up) althought quite slow.
- Training crashes after a while with:
```
terminate called after throwing an instance of 'miopen::Exception'
  what():  /root/driver/MLOpen/src/hipoc/hipoc_program.cpp:94: Failed creating module hipErrorSharedObjectInitFailed
```

Environment:
- mi50 GPU
- ROCm 3.9
- pytorch from pip package compiled in a centos 8 docker environment
- conda env:
```
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
blas                      1.0                         mkl  
ca-certificates           2020.10.14                    0  
certifi                   2020.6.20          pyhd3eb1b0_3  
cycler                    0.10.0                   pypi_0    pypi
cython                    0.29.21          py38h2531618_0  
intel-openmp              2020.2                      254  
kiwisolver                1.3.1                    pypi_0    pypi
ld_impl_linux-64          2.33.1               h53a641e_7  
libedit                   3.1.20191231         h14c3975_1  
libffi                    3.3                  he6710b0_2  
libgcc-ng                 9.1.0                hdf63c60_0  
libgfortran-ng            7.3.0                hdf63c60_0  
libstdcxx-ng              9.1.0                hdf63c60_0  
matplotlib                3.3.3                    pypi_0    pypi
mkl                       2020.2                      256  
mkl-service               2.3.0            py38he904b0f_0  
mkl_fft                   1.2.0            py38h23d657b_0  
mkl_random                1.1.1            py38h0573a6f_0  
ncurses                   6.2                  he6710b0_1  
numpy                     1.19.2           py38h54aff64_0  
numpy-base                1.19.2           py38hfa32c7d_0  
omegaconf                 2.0.5                    pypi_0    pypi
openssl                   1.1.1h               h7b6447c_0  
pillow                    8.0.1                    pypi_0    pypi
pillow-simd               7.0.0.post3              pypi_0    pypi
pip                       20.2.4           py38h06a4308_0  
pycocotools               2.0.2                    pypi_0    pypi
pyparsing                 2.4.7                    pypi_0    pypi
python                    3.8.5                h7579374_1  
python-dateutil           2.8.1                    pypi_0    pypi
pyyaml                    5.3.1            py38h7b6447c_1  
readline                  8.0                  h7b6447c_0  
scipy                     1.5.2            py38h0b6359f_0  
setuptools                50.3.1           py38h06a4308_1  
six                       1.15.0           py38h06a4308_0  
sqlite                    3.33.0               h62c20be_0  
timm                      0.3.1                    pypi_0    pypi
tk                        8.6.10               hbc83047_0  
torch                     1.8.0a0                  pypi_0    pypi
torchvision               0.9.0a0+74de51d          pypi_0    pypi
typing-extensions         3.7.4.3                  pypi_0    pypi
wheel                     0.35.1             pyhd3eb1b0_0  
xz                        5.2.5                h7b6447c_0  
yaml                      0.2.5                h7b6447c_0  
zlib                      1.2.11               h7b6447c_3  
```

I don't have access to the test server anymore and didn't have admin rights anyways, so a first step would be to have someone else reproduce the problem. I can provide more information on how to do so.

---

## 评论 (20 条)

### 评论 #1 — ROCmSupport (2021-01-04T09:34:35Z)

Thanks @nlgranger for reaching us out.
Can you please share the step by step procedure to reproduce the problem.
Before that, please help us with outputs of /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-01-11T06:08:28Z)

Hi @nlgranger 
Request you to help us with more information as requested in above comment to move further.
Thank you.

---

### 评论 #3 — nlgranger (2021-01-11T07:55:34Z)

I'm working on it, I'm waiting for someone to power up again the node.

---

### 评论 #4 — nlgranger (2021-01-19T11:26:34Z)

I have reproduced the problem on a completely different platform.

# System configuration

- 4 x Vega 10 XTX [Radeon Vega Frontier Edition]
- OS: centos 8.2
- ROCm: 4.0.0 from the rocm rpm repo
- `uname -r`: 4.18.0-193.el8.x86_64
- `docker -v`: Docker version 20.10.2, build 2291f61
- docker image: rocm/pytorch

<details><summary>`cat /etc/os-release`</summary>
<p>

```
NAME="CentOS Linux"
VERSION="8 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="8"
PLATFORM_ID="platform:el8"
PRETTY_NAME="CentOS Linux 8 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:8"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"

CENTOS_MANTISBT_PROJECT="CentOS-8"
CENTOS_MANTISBT_PROJECT_VERSION="8"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="8"
```

</p>
</details>

<details><summary>`modinfo amdgpu`</summary>
<p>

```
filename:       /lib/modules/4.18.0-193.el8.x86_64/extra/amdgpu.ko.xz
version:        5.6.19
license:        GPL and additional rights
description:    AMD GPU
author:         AMD linux driver team
```

</p>
</details>

<details><summary>`/opt/rocm-4.0.0/bin/rocminfo`</summary>
<p>

```
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
  Name:                    Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz
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
  Max Clock Freq. (MHz):   3700                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            24                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65349760(0x3e52880) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65349760(0x3e52880) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3700                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            24                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    66054340(0x3efe8c4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    66054340(0x3efe8c4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 3                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-0213f2ea95100944               
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   6656                               
  Internal Node ID:        2                                  
  Compute Unit:            64                                 
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
      Name:                    amdgcn-amd-amdhsa--gfx900          
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
*******                  
Agent 4                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-0214feb230304064               
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    3                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   15616                              
  Internal Node ID:        3                                  
  Compute Unit:            64                                 
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
      Name:                    amdgcn-amd-amdhsa--gfx900          
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
*******                  
Agent 5                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-0213f2ba74224164               
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    4                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   24576                              
  Internal Node ID:        4                                  
  Compute Unit:            64                                 
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
      Name:                    amdgcn-amd-amdhsa--gfx900          
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
*******                  
Agent 6                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-0214feb230281164               
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    5                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   34816                              
  Internal Node ID:        5                                  
  Compute Unit:            64                                 
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
      Name:                    amdgcn-amd-amdhsa--gfx900          
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

</p>
</details>

<details><summary>`clinfo`</summary>
<p>

```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3212.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 4
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 10 XTX [Radeon Vega Frontier Edition]
  Device Topology:				 PCI[ B#26, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1600Mhz
  Address bits:					 64
  Max memory allocation:			 14588628168
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 16384
  Max image 3D height:				 16384
  Max image 3D depth:				 8192
  Max samplers within kernel:			 26723
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 14588628168
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 1703726280
  Max global variable size:			 14588628168
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f4854533df0
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3212.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 


  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 10 XTX [Radeon Vega Frontier Edition]
  Device Topology:				 PCI[ B#61, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1600Mhz
  Address bits:					 64
  Max memory allocation:			 14588628168
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 16384
  Max image 3D height:				 16384
  Max image 3D depth:				 8192
  Max samplers within kernel:			 26723
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 14588628168
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 1703726280
  Max global variable size:			 14588628168
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f4854533df0
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3212.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 


  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 10 XTX [Radeon Vega Frontier Edition]
  Device Topology:				 PCI[ B#96, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1600Mhz
  Address bits:					 64
  Max memory allocation:			 14588628168
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 16384
  Max image 3D height:				 16384
  Max image 3D depth:				 8192
  Max samplers within kernel:			 26723
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 14588628168
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 1703726280
  Max global variable size:			 14588628168
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f4854533df0
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3212.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 


  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 10 XTX [Radeon Vega Frontier Edition]
  Device Topology:				 PCI[ B#136, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1600Mhz
  Address bits:					 64
  Max memory allocation:			 14588628168
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 16384
  Max image 3D height:				 16384
  Max image 3D depth:				 8192
  Max samplers within kernel:			 26723
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 14588628168
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 1703726280
  Max global variable size:			 14588628168
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f4854533df0
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3212.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```

</p>
</details>

# Steps to reproduce

- `git clone https://github.com/facebookresearch/detr`
- download and extract [COCO 2017 dataset](https://cocodataset.org/#download), see detr README for the expected directory layout
- `docker run -it --rm --network=host --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 8G -v $PWD/COCO:/COCO -v $PWD/detr:/detr rocm/pytorch:latest bash`
- `cd /detr`
- `conda install -y cython scipy`
- `pip install -r requirements.txt`
- `python main.py --coco_path /COCO`

# What happens

The script spends time running clang sub-processes, the experiments seems to run very slowly (presumably on CPU), there is very little GPU RAM usage and no activity. It terminated with a segfault this time.

<details><summary>`rocm-smi` while running the script</summary>
<p>

```
========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
1    32.0c  14.0W   852Mhz  945Mhz  14.9%   auto  220.0W   13%   0%    
2    22.0c  3.0W    852Mhz  167Mhz  15.69%  auto  220.0W    0%   0%    
3    23.0c  3.0W    852Mhz  167Mhz  12.94%  auto  220.0W    0%   0%    
4    25.0c  3.0W    852Mhz  167Mhz  14.9%   auto  220.0W    0%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================
```

</p>
</details>

<details><summary>`ps -aux --forest` while running the script</summary>
<p>

```
root      218852  0.0  0.0 113384 10280 ?        Sl   11:03   0:00 /usr/bin/containerd-shim-runc-v2 -namespace moby -id 8d00567ca1a1035b490ee321f9f2f0fb8cbc17fcfac5638fd3f0b2127ae84615 -address /run/conta
root      218873  0.0  0.0  20388  3836 pts/0    Ss   11:03   0:00  \_ bash
root      219677 11.6  3.5 27760656 4624884 pts/0 Sl+ 11:22   5:02      \_ python main.py --coco_path /COCO
root      219714  0.0  2.0 23784508 2743360 pts/0 Sl+ 11:23   0:00          \_ python main.py --coco_path /COCO
root      219715  0.0  2.0 23792348 2750984 pts/0 Sl+ 11:23   0:00          \_ python main.py --coco_path /COCO
root      321788  0.0  0.0   4636   932 pts/0    S+   12:06   0:00          \_ sh -c cd /tmp/miopen-MIOpenConv1x1S.cl-f30e-c234-4d10-fb04; /opt/rocm-4.0.0/bin/clang-ocl  -DMLO_DIR_FORWARD=0 -DMLO_FILTER_S
root      321790  0.0  0.0  20264  3624 pts/0    S+   12:06   0:00          |   \_ /bin/bash /opt/rocm-4.0.0/bin/clang-ocl -DMLO_DIR_FORWARD=0 -DMLO_FILTER_SIZE0=1 -DMLO_FILTER_SIZE1=1 -DMLO_FILTER_STRIDE
root      321796  0.0  0.0 128124 48488 pts/0    R+   12:06   0:00          |       \_ /opt/rocm-4.0.0/llvm/bin/clang -c -emit-llvm -target amdgcn-amd-amdhsa -x cl -D__AMD__=1 -D__gfx900__=1 -D__gfx900=1 
root      321789  0.0  0.0   4636   780 pts/0    S+   12:06   0:00          \_ sh -c cd /tmp/miopen-MIOpenUtilKernels3.cl-5f3f-ffbe-93a6-790b; /opt/rocm-4.0.0/bin/clang-ocl  -DDATA_TYPE=float -DMLO_GRP0_S
root      321798  0.0  0.0  20264  3508 pts/0    S+   12:06   0:00              \_ /bin/bash /opt/rocm-4.0.0/bin/clang-ocl -DDATA_TYPE=float -DMLO_GRP0_SZ0=256 -DMLO_GRP0_SZ1=1 -DMLO_GRP0_SZ2=1 -DMLO_FILT
root      321804  0.0  0.0 126188 46672 pts/0    R+   12:06   0:00                  \_ /opt/rocm-4.0.0/llvm/bin/clang -c -emit-llvm -target amdgcn-amd-amdhsa -x cl -D__AMD__=1 -D__gfx900__=1 -D__gfx900=1 
```

---

### 评论 #5 — ROCmSupport (2021-01-27T04:42:11Z)

@nlgranger ,
    Thank you for the info.  We have been able to reproduce this problem once. We are checking this more.

---

### 评论 #6 — ROCmSupport (2021-01-27T10:46:47Z)

Hi @nlgranger 
Latest update on this issue:
We have assigned to MIOpen team and the dev will start working on it.
Thank you.

---

### 评论 #7 — ROCmSupport (2021-02-11T05:04:51Z)

Hi @nlgranger 
From the logs it appears the system runs out of file handles. Can you please check the file limits on the system (ulimit -a) and increase them. For now you can possibly circumvent the compilation of many files by setting 'MIOPEN_FIND_MODE=5' environment variable. we are working on making this behavior default. 

For ex: We are not able to reproduce this issue with env MIOPEN_FIND_MODE=5 and setting ulimit -n 65535.

Please try the above settings and share an update.
Thank you.

---

### 评论 #8 — nlgranger (2021-02-17T17:50:18Z)

Hi and thank you for looking into this.
The file count limit was already above 65535, I have set MIOPEN_FIND_MODE and it does not crash anymore.
Clang processes still appear regularly during the run but less frequently I think.

However GPU RAM usage is still abnormally low considering the batch size and the GPU activity is low. The same experiment running on nvidia v100 16G consumes almost all the memory instead of 12% here and runs about 30 times faster.

---

### 评论 #9 — ROCmSupport (2021-03-01T08:23:21Z)

> 
> 
> Hi and thank you for looking into this.
> The file count limit was already above 65535, I have set MIOPEN_FIND_MODE and it does not crash anymore.
> Clang processes still appear regularly during the run but less frequently I think.
> 
Thanks. So the flag addresses the issue.

> However GPU RAM usage is still abnormally low considering the batch size and the GPU activity is low. The same experiment running on nvidia v100 16G consumes almost all the memory instead of 12% here and runs about 30 times faster.

We have assigned this, now, to our frameworks team for understanding more.




---

### 评论 #10 — ROCmSupport (2021-03-30T10:46:27Z)

Hi @nlgranger 
Can you please validate this issue with recently released ROCm version: 4.1 and share an update asap.
Thank you.

---

### 评论 #11 — nlgranger (2021-05-06T17:08:36Z)

Sorry for the delay we cannot upgrade servers very frequently.
After updating to Centos 8.3 and rocm 4.1.0 (clean install), I can still reproduce the bug.

---

### 评论 #12 — ROCmSupport (2021-05-07T04:41:51Z)

Thanks @nlgranger for the update.

---

### 评论 #13 — ROCmSupport (2021-06-03T09:44:53Z)

Hi @nlgranger 
Got an update for you.
The issue should be addressed with MIOpen find mode 5. 
Can you rerun the workload using ROCm4.2, with MIOPEN_FIND_MODE=5 env var?


---

### 评论 #14 — ROCmSupport (2021-07-08T09:01:51Z)

Hi @nlgranger 
Can you please do the needful as mentioned in above comment and confirm.
Thank you.

---

### 评论 #15 — nlgranger (2021-07-13T11:51:28Z)

torchvision is broken in the docker rocm/pytorch image and the pytorch from the official pytorch rocm build doesn't see the GPUs.

---

### 评论 #16 — ROCmSupport (2021-07-14T06:59:53Z)

Hi @nlgranger 
Can you please share more details on rocm/pytorch image and steps to reproduce.
Thank you.

---

### 评论 #17 — nlgranger (2021-07-16T07:04:05Z)

~~Running the commands to reproduce the bug above, I now get:~~
```
Traceback (most recent call last):
  File "main.py", line 13, in <module>
    import datasets
  File "/detr/datasets/__init__.py", line 5, in <module>
    from .coco import build as build_coco
  File "/detr/datasets/coco.py", line 14, in <module>
    import datasets.transforms as T
  File "/detr/datasets/transforms.py", line 13, in <module>
    from util.misc import interpolate
  File "/detr/util/misc.py", line 22, in <module>
    from torchvision.ops import _new_empty_tensor
ImportError: cannot import name '_new_empty_tensor'
```
~~Which is symptomatic from torchvision not being in sync with the version of pytorch.~~

**The bug with torchvision was solved by cleaning python cache files left over in the detr repo from a previous experiment.**

---

### 评论 #18 — nlgranger (2021-07-16T08:14:30Z)

I think I have identified an issue:

Pytorch automatically sets OMP_NUM_THREADS=1 to prevent an explosion of the number of threads when running distributed experiments on servers with many cores. By raising that to 8, the experiment runs faster: 5 days -> 1 day.

When running the experiment now:
- CPU usage is the same as before: ~1 core at 100%, it can't go below that because I think pytorch uses a busy loop.
- GPU usage is high, confirmed by power consumption
- GPU memory is still 12% which is likely wrong

My guess is that you guys use OMP threads with locks somewhere to manage kernel execution and single threading forced execution to be sequential without any pipelining.

---

### 评论 #19 — nlgranger (2021-07-16T09:45:37Z)

FYI one training epoch on a single NVIDIA p5000 takes 5H, on the vega frontier it is estimated to about one day, the time spent on each iteration seems unstable with the first few iterations being faster than subsequent ones.

---

### 评论 #20 — ROCmSupport (2021-07-29T10:44:34Z)

Thanks @nlgranger for the update that issue is resolved with changing OMP_NUM_THREADS flag value.
I am closing this then.
Feel free to file new issues, if any, fr quick resolutions.
Thank you.

---
