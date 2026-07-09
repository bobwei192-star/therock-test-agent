# [Issue]: Sporadic page faults with comfyui/pytorch - heavy persisting performance drop afterwards

- **Issue #:** 5225
- **State:** closed
- **Created:** 2025-08-23T11:39:46Z
- **Updated:** 2026-01-14T19:21:20Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5225

### Problem Description

With comfyui image generation generally works very good (5s/it on an sdxl model) and then on a sporadic base (sometimes after 2 image generations, sometimes after ~15) I get this:

 35%|███████████████▍                            | 7/20 [00:47<01:27,  6.77s/it]Memory access fault by GPU node-1 (Agent handle: 0xeea28e0) on address 0x7a6eedb80000. Reason: Page not present or supervisor privilege.
Failed to fetch queues snapshot.
GPU core dump failed
Aborted (core dumped)

In dmesg:
```
[  499.707618] amdgpu 0000:74:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[  499.707632] amdgpu 0000:74:00.0: amdgpu:  in process python3 pid 3710 thread python3 pid 3710
[  499.707639] amdgpu 0000:74:00.0: amdgpu:   in page starting at address 0x00007a6e20839000 from client 0x1b (UTCL2)
[  499.707646] amdgpu 0000:74:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
[  499.707651] amdgpu 0000:74:00.0: amdgpu: 	 Faulty UTCL2 client ID: TCP (0x8)
[  499.707656] amdgpu 0000:74:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[  499.707661] amdgpu 0000:74:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[  499.707665] amdgpu 0000:74:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[  499.707669] amdgpu 0000:74:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[  499.707673] amdgpu 0000:74:00.0: amdgpu: 	 RW: 0x0
[  499.707689] amdgpu 0000:74:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[  499.707696] amdgpu 0000:74:00.0: amdgpu:  in process python3 pid 3710 thread python3 pid 3710
[  499.707701] amdgpu 0000:74:00.0: amdgpu:   in page starting at address 0x00007a6efabbb000 from client 0x1b (UTCL2)
```

... a lot of those ...

```
[  499.707838] amdgpu 0000:74:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[  499.707843] amdgpu 0000:74:00.0: amdgpu:  in process python3 pid 3710 thread python3 pid 3710
[  499.707848] amdgpu 0000:74:00.0: amdgpu:   in page starting at address 0x00007a6e086a0000 from client 0x1b (UTCL2)
```


After that event, the performance drops heavily and the image generation usually is 3 or 4 times as slow as before.
Interestingly, this state persists until a system cold restart. Then it's back to "normal".

I couldn't find any differences in metrics or settings that are different before or after this event. Hence, I could need some advice on either the problem source, how to dig in into this issue further, or some workaround.
I also did another install with Ubuntu 25, built TheRock rocm version from scratch for my gpu model. **Complete same issue.**

It's a fresh ubuntu 24LTS installation. Drivers from default ubuntu repositories. Pytorch install from their website. Extensive system info below.

Please let me know, if you need more logs/info.



### Operating System

Ubuntu 24.04.3 LTS

### CPU

AMD Ryzen 7 6800H with Radeon Graphics

### GPU

AMD Radeon 680M

### ROCm Version

ROCm 5.7.0 ?

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

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
  Name:                    AMD Ryzen 7 6800H with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 6800H with Radeon Graphics
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
  Max Clock Freq. (MHz):   4787                               
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
      Size:                    32077704(0x1e97788) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32077704(0x1e97788) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32077704(0x1e97788) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1030                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon 680M                    
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
    L2:                      2048(0x800) KB                     
  Chip ID:                 5761(0x1681)                       
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2200                               
  BDFID:                   29696                              
  Internal Node ID:        1                                  
  Compute Unit:            12                                 
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
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
  Packet Processor uCode:: 116                                
  SDMA engine uCode::      47                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16038852(0xf4bbc4) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS:                     
      Size:                    16038852(0xf4bbc4) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1030         
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


--------------------------------------- *** ---------------------------------------
SYSTEM INFO:
```
OS:
NAME="Ubuntu"
VERSION="24.04.3 LTS (Noble Numbat)"
CPU: 
model name	: AMD Ryzen 7 6800H with Radeon Graphics
GPU:
  Name:                    AMD Ryzen 7 6800H with Radeon Graphics
  Marketing Name:          AMD Ryzen 7 6800H with Radeon Graphics
  Name:                    gfx1030                            
  Marketing Name:          AMD Radeon 680M                    
      Name:                    amdgcn-amd-amdhsa--gfx1030 
```

--------------------------------------- *** ---------------------------------------
environment:

```
HSA_OVERRIDE_GFX_VERSION=10.3.0
USE_CUDA=0
```



--------------------------------------- *** ---------------------------------------
rocminfo:
```

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
  Name:                    AMD Ryzen 7 6800H with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 6800H with Radeon Graphics
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
  Max Clock Freq. (MHz):   4787                               
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
      Size:                    32077704(0x1e97788) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32077704(0x1e97788) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32077704(0x1e97788) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1030                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon 680M                    
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
    L2:                      2048(0x800) KB                     
  Chip ID:                 5761(0x1681)                       
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2200                               
  BDFID:                   29696                              
  Internal Node ID:        1                                  
  Compute Unit:            12                                 
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
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
  Packet Processor uCode:: 116                                
  SDMA engine uCode::      47                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16038852(0xf4bbc4) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS:                     
      Size:                    16038852(0xf4bbc4) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1030         
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

--------------------------------------- *** ---------------------------------------

rocm-smi


```
========================= ROCm System Management Interface =========================
=================================== Concise Info ===================================
GPU[0]		: get_power_avg, Not supported on the given system
Exception caught: map::at
ERROR: GPU[0]	: sclk clock is unsupported
====================================================================================
GPU[0]		: get_power_cap, Not supported on the given system
GPU  Temp (DieEdge)  AvgPwr  SCLK  MCLK     Fan  Perf  PwrCap       VRAM%  GPU%  
0    45.0c           N/A     None  2400Mhz  0%   auto  Unsupported   83%   0%    
====================================================================================
=============================== End of ROCm SMI Log ================================
```


--------------------------------------- *** ---------------------------------------

rocm-smi --showdriverversion

```
========================= ROCm System Management Interface =========================
=========================== Version of System Component ============================
Driver version: 6.14.0-28-generic
====================================================================================
=============================== End of ROCm SMI Log ================================

--------------------------------------- *** ---------------------------------------

```
pip list
```
Package                    Version
-------------------------- --------------
aiofiles                   24.1.0
aiohappyeyeballs           2.6.1
aiohttp                    3.12.15
aiohttp_socks              0.10.1
aiosignal                  1.4.0
alembic                    1.16.4
annotated-types            0.7.0
attrs                      25.3.0
av                         15.0.0
certifi                    2025.8.3
cffi                       1.17.1
chardet                    5.2.0
charset-normalizer         3.4.3
click                      8.2.1
comfyui-embedded-docs      0.2.6
comfyui_frontend_package   1.25.9
comfyui_workflow_templates 0.1.65
cryptography               45.0.6
einops                     0.8.1
filelock                   3.13.1
frozenlist                 1.7.0
fsspec                     2025.7.0
gitdb                      4.0.12
GitPython                  3.1.45
greenlet                   3.2.4
h11                        0.16.0
h2                         4.2.0
hf-xet                     1.1.8
hpack                      4.1.0
huggingface-hub            0.34.4
hyperframe                 6.1.0
idna                       3.10
Jinja2                     3.1.4
jsonschema                 4.25.1
jsonschema-specifications  2025.4.1
kornia                     0.8.1
kornia_rs                  0.1.9
Mako                       1.3.10
markdown-it-py             4.0.0
MarkupSafe                 2.1.5
matrix-nio                 0.25.2
mdurl                      0.1.2
mpmath                     1.3.0
multidict                  6.6.4
networkx                   3.3
numpy                      2.1.2
packaging                  25.0
piexif                     1.1.3
pillow                     11.0.0
pip                        24.0
propcache                  0.3.2
psutil                     7.0.0
pycparser                  2.22
pycryptodome               3.23.0
pydantic                   2.11.7
pydantic_core              2.33.2
pydantic-settings          2.10.1
PyGithub                   2.7.0
Pygments                   2.19.2
PyJWT                      2.10.1
PyNaCl                     1.5.0
python-dotenv              1.1.1
python-socks               2.7.2
pytorch-triton-rocm        3.4.0
PyYAML                     6.0.2
referencing                0.36.2
regex                      2025.7.34
requests                   2.32.5
rich                       14.1.0
rpds-py                    0.27.0
safetensors                0.6.2
scipy                      1.16.1
sentencepiece              0.2.1
setuptools                 70.2.0
shellingham                1.5.4
smmap                      5.0.2
soundfile                  0.13.1
spandrel                   0.4.1
SQLAlchemy                 2.0.43
sympy                      1.13.3
tokenizers                 0.21.4
toml                       0.10.2
torch                      2.8.0+rocm6.4
torchaudio                 2.8.0
torchsde                   0.2.6
torchvision                0.23.0+rocm6.4
tqdm                       4.67.1
trampoline                 0.1.2
transformers               4.55.4
typer                      0.16.1
typing_extensions          4.12.2
typing-inspection          0.4.1
unpaddedbase64             2.1.0
urllib3                    2.5.0
uv                         0.8.13
yarl                       1.20.1
```

--------------------------------------- *** ---------------------------------------
comfyui-startup:

```
python3 main.py --fp16-unet --cpu-vae --preview-method none --fp16-text-enc --disable-smart-memory --async-offload
[START] Security scan
Using Python 3.12.3 environment at: venv
[DONE] Security scan
## ComfyUI-Manager: installing dependencies done.
** ComfyUI startup time: 2025-08-23 12:45:48.511
** Platform: Linux
** Python version: 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0]
...
Using Python 3.12.3 environment at: venv
Using Python 3.12.3 environment at: venv

Prestartup times for custom nodes:
   0.5 seconds: /home/*/ComfyUI/custom_nodes/comfyui-manager

Checkpoint files will always be loaded safely.
Total VRAM 15663 MB, total RAM 31326 MB
pytorch version: 2.8.0+rocm6.4
AMD arch: gfx1030
ROCm version: (6, 4)
Set vram state to: NORMAL_VRAM
Disabling smart memory management
Device: cuda:0 AMD Radeon 680M : native
Using async weight offloading with 2 streams
Using sub quadratic optimization for attention, if you have memory or speed issues try using: --use-split-cross-attention
torchaudio missing, ACE model will be broken
torchaudio missing, ACE model will be broken
Python version: 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0]
ComfyUI version: 0.3.51
ComfyUI frontend version: 1.25.9
```

--------------------------------------- *** ---------------------------------------

rocm-smi -a:
```
========================= ROCm System Management Interface =========================
=========================== Version of System Component ============================
Driver version: 6.14.0-28-generic
====================================================================================
======================================== ID ========================================
GPU[0]		: GPU ID: 0x1681
====================================================================================
==================================== Unique ID =====================================
GPU[0]		: Unique ID: N/A
====================================================================================
====================================== VBIOS =======================================
GPU[0]		: VBIOS version: 113-REMBRANDT-X37
====================================================================================
=================================== Temperature ====================================
GPU[0]		: Temperature (Sensor edge) (C): 44.0
====================================================================================
============================ Current clock frequencies =============================
Exception caught: map::at
GPU[0]		: fclk clock level: 1: (1800Mhz)
GPU[0]		: mclk clock level: 1: (2400Mhz)
GPU[0]		: sclk clock level: 1: (400Mhz)
GPU[0]		: socclk clock level: 0: (400Mhz)
====================================================================================
================================ Current Fan Metric ================================
GPU[0]		: Unable to detect fan speed for GPU 0
====================================================================================
============================== Show Performance Level ==============================
GPU[0]		: Performance Level: auto
====================================================================================
================================= OverDrive Level ==================================
GPU[0]		: get_overdrive_level_sclk, Not supported on the given system
====================================================================================
================================= OverDrive Level ==================================
GPU[0]		: get_mem_overdrive_level_mclk, Not supported on the given system
====================================================================================
==================================== Power Cap =====================================
GPU[0]		: get_power_cap, Not supported on the given system
GPU[0]		: Max Graphics Package Power Unsupported
====================================================================================
=============================== Show Power Profiles ================================
GPU[0]		: get_power_profiles, Not supported on the given system
====================================================================================
================================ Power Consumption =================================
, Not supported on the given system
GPU[0]		: get_power_avg, Not supported on the given system
GPU[0]		: get_power_avg, Not supported on the given system
GPU[0]		: Average Graphics Package Power (W): N/A
====================================================================================
=========================== Supported clock frequencies ============================
GPU[0]		: Supported fclk frequencies on GPU0
GPU[0]		: 0: 500Mhz
GPU[0]		: 1: 1800Mhz *
GPU[0]		: 
GPU[0]		: Supported mclk frequencies on GPU0
GPU[0]		: 0: 1000Mhz
GPU[0]		: 1: 2400Mhz *
GPU[0]		: 
GPU[0]		: Supported sclk frequencies on GPU0
GPU[0]		: 0: 200Mhz
GPU[0]		: 1: 533Mhz *
GPU[0]		: 2: 2200Mhz
GPU[0]		: 
GPU[0]		: Supported socclk frequencies on GPU0
GPU[0]		: 0: 400Mhz
GPU[0]		: 1: 600Mhz
GPU[0]		: 2: 720Mhz
GPU[0]		: 3: 800Mhz
GPU[0]		: 4: 900Mhz
GPU[0]		: 5: 1028Mhz
GPU[0]		: 6: 1028Mhz
GPU[0]		: 7: 1200Mhz *
GPU[0]		: 
------------------------------------------------------------------------------------
====================================================================================
================================ % time GPU is busy ================================
GPU[0]		: GPU use (%): 0
====================================================================================
================================ Current Memory Use ================================
GPU[0]		: % memory use, Not supported on the given system
GPU[0]		: Memory Activity: N/A
====================================================================================
================================== Memory Vendor ===================================
GPU[0]		: get_vram_vendor, Not supported on the given system
====================================================================================
=============================== PCIe Replay Counter ================================
GPU[0]		: PCIe Replay Count: 0
====================================================================================
================================== Serial Number ===================================
GPU[0]		: get_serial_number, Not supported on the given system
GPU[0]		: Serial Number: N/A
====================================================================================
================================== KFD Processes ===================================
No KFD PIDs currently running
====================================================================================
=============================== GPUs Indexed by PID ================================
No KFD PIDs currently running
====================================================================================
==================== GPU Memory clock frequencies and voltages =====================
GPU[0]		: get_od_volt, Requested function is not implemented on this setup
====================================================================================
================================= Current voltage ==================================
GPU[0]		: Voltage (mV): 885
====================================================================================
==================================== PCI Bus ID ====================================
GPU[0]		: PCI Bus: 0000:74:00.0
====================================================================================
=============================== Firmware Information ===============================
GPU[0]		: ASD firmware version: 	0x210000c7
GPU[0]		: CE firmware version: 		37
GPU[0]		: get_firmware_version_DMCU, Not supported on the given system
GPU[0]		: get_firmware_version_MC, Not supported on the given system
GPU[0]		: ME firmware version: 		64
GPU[0]		: MEC firmware version: 	116
GPU[0]		: MEC2 firmware version: 	116
GPU[0]		: PFP firmware version: 	97
GPU[0]		: RLC firmware version: 	83
GPU[0]		: RLC SRLC firmware version: 	1
GPU[0]		: RLC SRLG firmware version: 	1
GPU[0]		: RLC SRLS firmware version: 	1
GPU[0]		: SDMA firmware version: 	47
GPU[0]		: get_firmware_version_SDMA2, Not supported on the given system
GPU[0]		: SMC firmware version: 	04.69.61.00
GPU[0]		: get_firmware_version_SOS, Not supported on the given system
GPU[0]		: get_firmware_version_TA RAS, Not supported on the given system
GPU[0]		: get_firmware_version_TA XGMI, Not supported on the given system
GPU[0]		: get_firmware_version_UVD, Not supported on the given system
GPU[0]		: get_firmware_version_VCE, Not supported on the given system
GPU[0]		: VCN firmware version: 	0x0311e004
====================================================================================
=================================== Product Info ===================================
GPU[0]		: Card series: 		Rembrandt [Radeon 680M]
GPU[0]		: Card model: 		0x1001
GPU[0]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]		: Card SKU: 		REMBRANDT
====================================================================================
==================================== Pages Info ====================================
GPU[0]		: ras, Not supported on the given system
============================== Show Valid sclk Range ===============================
GPU[0]		: get_od_volt, Requested function is not implemented on this setup
====================================================================================
============================== Show Valid mclk Range ===============================
GPU[0]		: get_od_volt, Requested function is not implemented on this setup
====================================================================================
============================= Show Valid voltage Range =============================
GPU[0]		: get_od_volt, Requested function is not implemented on this setup
====================================================================================
=============================== Voltage Curve Points ===============================
GPU[0]		: get_od_volt_info, Requested function is not implemented on this setup
====================================================================================
================================= Consumed Energy ==================================
GPU[0]		: % Energy Counter, Not supported on the given system
====================================================================================
============================ Current Compute Partition =============================
GPU[0]		: Not supported on the given system
====================================================================================
================================= Current NPS Mode =================================
GPU[0]		: Not supported on the given system
====================================================================================
=============================== End of ROCm SMI Log ================================

```
```
dpkg -l | grep rocm
ii  librocm-smi64-1                               5.7.0-1                                  amd64        ROCm System Management Interface (ROCm SMI) library
ii  rocm-device-libs-17                           6.0+git20231212.5a852ed-2                amd64        AMD specific device-side language runtime libraries
ii  rocm-smi                                      5.7.0-1                                  amd64        ROCm System Management Interface (ROCm SMI) command-line interface
ii  rocminfo                                      5.7.1-3build1                            amd64        ROCm Application for Reporting System Info
```