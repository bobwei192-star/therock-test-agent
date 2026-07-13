# [Issue]: Stall / hang in comfyUI gfx1201 above 6.4.4 (7.1 / 7.0.2 / 7.0.0 / nightlies) on Ubuntu 25.04 (pytorch Docker images)

- **Issue #:** 5581
- **State:** closed
- **Created:** 2025-10-28T03:55:14Z
- **Updated:** 2025-11-25T00:19:25Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5581

### Problem Description

ComfyUI eventually stalls generating images (1-30 generations)

GPU% remains 100% forever, but power / heat drop over the course of dozens of minutes until it is clear the card is not doing work.
even after hours, no progress is observed and temps remain low (50-65C, GPU fans cycle on/off)

problem is **not observed** in ROCm 6.4.4 w/ torch 2.7.1

docker images tested: 

rocm7.1_ubuntu24.04_py3.12_pytorch_release_2.8.0
rocm7.0.2_ubuntu24.04_py3.12_pytorch_release_2.8.0
rocm7.0.2_ubuntu24.04_py3.12_pytorch_release_2.7.1
rocm7.0_ubuntu24.04_py3.12_pytorch_release_2.7.1
rocm7.0_ubuntu24.04_py3.12_pytorch_release_2.8.0
rocm6.4.4_ubuntu24.04_py3.12_pytorch_release_2.7.1



### Operating System

25.04 (Plucky Puffin)

### CPU

5700 X3D

### GPU

9070xt

### ROCm Version

everything since 7.0.0

### ROCm Component

_No response_

### Steps to Reproduce

Download rocm/pytorch
Install comfyUI requirements (using existing modules as constraints to prevent breaking rocm-torch compatibility)

generate 10-50 SDXL illustrious images.



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module version 6.14.14 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.11
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
  Name:                    AMD Ryzen 7 5700X3D 8-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 5700X3D 8-Core Processor
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
  Max Clock Freq. (MHz):   4151                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    49252724(0x2ef8974) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    49252724(0x2ef8974) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    49252724(0x2ef8974) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    49252724(0x2ef8974) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-939d3c9fc1d5f803               
  Marketing Name:          AMD Radeon RX 9070 XT              
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
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30032(0x7550)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2400                               
  BDFID:                   11520                              
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 1012                               
  SDMA engine uCode::      838                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16695296(0xfec000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1201         
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx12-generic   
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*** Done *** 

### Additional Information

```
/home/USER/comfy
├── base
│   ├── custom_nodes
│   ├── disabled_custom_nodes
│   ├── input
│   ├── models -> /mnt/ai/models
│   ├── output
│   ├── temp
│   └── user
├── build
├── ComfyUI
│   ├── alembic_db
│   ├── api_server
│   ├── app
...
└── user
    ├── default
    └── huggingface

```

``` Dockerfile
ARG ROCM_MAJOR=6.4
ARG ROCM_MINOR=.4
FROM rocm/pytorch:rocm${ROCM_MAJOR}${ROCM_MINOR}_ubuntu24.04_py3.12_pytorch_release_2.7.1
#FROM rocm/pytorch:rocm7.0_ubuntu24.04_py3.12_pytorch_release_2.7.1
#FROM rocm/pytorch:rocm7.0_ubuntu24.04_py3.12_pytorch_release_2.8.0
#FROM rocm/pytorch:rocm7.0.2_ubuntu24.04_py3.12_pytorch_release_2.8.0
#FROM rocm/pytorch:rocm6.4.4_ubuntu24.04_py3.12_pytorch_release_2.7.1
 
# 7.0 and up use /opt/venv
#ENV UV_VENV=/opt/venv
# 6.4.4 uses conda
ENV UV_VENV=/opt/conda/envs/py_3.12
 
 
ENV ROCM_VERSION=${ROCM_MAJOR}${ROCM_MINOR}
ENV UV_INDEX="https://repo.radeon.com/rocm/manylinux/rocm-rel-${ROCM_VERSION}/ https://download.pytorch.org/whl/nightly/rocm${ROCM_MAJOR}"
 
ENV UV_CACHE_DIR=/.cache/uv
ENV UV_BREAK_SYSTEM_PACKAGES=true
ENV UV_SYSTEM_PYTHON=true
 
ENV CUSTOM_NODES=/comfy/base/custom_nodes
ENV COMFY_DIR=/comfy/ComfyUI
 
RUN apt-get install --yes libcairo2-dev &&\
mkdir -p /mnt
 
WORKDIR /build
 
RUN pip install uv

# host contains up-to-date comfyUI
# ~/comfy/ComfyUI
RUN --mount=type=bind,source=.,target=/comfy                            \
uv pip freeze | sed 's/==\([^+]\+\)$/>=\1/' > frozen                    &&\
grep -hvP "^\s*(#.*)?$|\btorch\b|\btorchvision\b|\bpytorch-triton-rocm\b" $COMFY_DIR/requirements.txt $CUSTOM_NODES/*/requirements.txt | sort | uniq > all_requirements.txt
 
# unsafe-best-match is required to resolve ? opencv ?
RUN --mount=type=cache,target=/.cache                                   \
uv pip install --index-strategy unsafe-best-match -r  all_requirements.txt -c frozen
 
WORKDIR /comfy
```

```
services:
  comfy_srv:
    container_name: "comfy_srv"
    image: "rocm644-torch271"
    restart: unless-stopped
    working_dir: /comfy
    volumes:
      - .:/comfy
      - /mnt/ai:/mnt/ai
    env_file: "comfy.env"
    environment:
      - HOST_DIR=$PWD
      - WORKING_DIR=/comfy
      - COMFY_DIR=/comfy/ComfyUI
      - COMFY_PORT=12345
    command: ["./run_comfy.sh"]
    ports:
      - 12345:12345
    group_add:
      - video
      - 105
    devices:
      - "/dev/dri"
      - "/dev/kfd"
    security_opt: 
      - seccomp=unconfined
    cap_add: 
      - SYS_PTRACE
    network_mode: host
    ipc: host
    shm_size: 12G
```

PS:
rocm644-torch280 (2025-10-26 build) eventually runs out of ... something and wreaks havoc on usability with this:
```
 2025-10-27T21:01:36.451881-04:00 tv kernel: [drm:amdgpu_dm_plane_helper_prepare_fb [amdgpu]] *ERROR* Failed to pin framebuffer with error -12
 2025-10-27T21:01:40.153879-04:00 tv kernel: amdgpu 0000:2d:00.0: amdgpu: 00000000caf88e41 pin failed
```