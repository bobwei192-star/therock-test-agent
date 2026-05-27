# [Issue]: RX 9060 XT 16GB hard-capped at ~8GB usable VRAM in PyTorch — segfault on allocation beyond cap

> **Issue #6295**
> **状态**: open
> **创建时间**: 2026-05-22T17:28:16Z
> **更新时间**: 2026-05-26T18:52:20Z
> **作者**: Badhunter0303
> **标签**: status: triage
> **URL**: https://github.com/ROCm/ROCm/issues/6295

## 标签

- **status: triage** (颜色: #585dd7)

## 负责人

- darren-amd

## 描述

### Problem Description

I was trying to make images with comfy on Linux Mint 22.2 with my rx 9060 xt 16 gb.
When loading models, they would get stuck at 0% with the gpu at 100% usage, no matter how long I waited, still stuck at 0%.

I am no programmer so I asked claude sonnet 4.6 to help me with this and it thinks it's a bug and I asked it to write the following bug report, I was just trying to make images for fun, to see if it could work.

Bug Report
Summary
On an AMD Radeon RX 9060 XT 16GB (gfx1200, Navi 44), PyTorch/ROCm reports and enforces a hard VRAM limit of ~7915 MB (~8GB), despite the kernel driver and rocminfo correctly seeing the full ~16GB. Attempting to allocate beyond this limit results in a segmentation fault (not a graceful OOM error).
This makes it impossible to use the full VRAM of the card for AI workloads such as ComfyUI with large models (e.g. Lumina2), forcing unnecessary CPU offloading and dramatically degrading performance.

Environment
GPU: AMD Radeon RX 9060 XT 16GB (Navi 44)
GPU Architecture: gfx1200 (RDNA 4)
OS: Linux Mint 22.2
Kernel: 6.17.0-29-generic
PyTorch: 2.13.0a0+rocm7.13.0a20260416
ROCm: 7.13.0a20260416 (nightly)
Python: 3.12.3
Driver: amdgpu (kernel built-in)

Steps to Reproduce

Check what the kernel driver sees (correct):

cat /sys/class/drm/card*/device/mem_info_vram_total
Output: 17095983104 (~16GB ✅)

Check what rocminfo sees (correct):

rocminfo | grep -A3 "Pool 1"
Output: Size: 16211708(0xf75efc) KB (~15.8GB ✅)

Check what rocm-smi sees (correct):

rocm-smi --showmeminfo vram
Output: VRAM Total Memory (B): 17095983104 (~16GB ✅)

Check what PyTorch sees (WRONG):

import torch
print(torch.cuda.get_device_properties(0).total_memory // 1024**2, 'MB')
Output: 7915 MB (~8GB ❌)
Note also that the card is misidentified:
print(torch.cuda.get_device_properties(0).name)
Output: 'AMD Radeon Graphics' (should be 'AMD Radeon RX 9060 XT') ❌

Attempt to allocate beyond the ~8GB cap — segfault instead of graceful OOM:

import torch
t = torch.zeros(14000, 1024, 1024, dtype=torch.float16, device='cuda')
Output: Segmentation fault (core dumped) ❌

Expected Behavior
torch.cuda.get_device_properties(0).total_memory should report ~16GB (~16384 MB).
The card should be correctly identified as AMD Radeon RX 9060 XT.
Allocations up to ~15GB should succeed or fail with a graceful torch.cuda.OutOfMemoryError, not a segfault.

Actual Behavior
PyTorch hard-caps usable VRAM at ~7915 MB (~8GB), exactly half the physical VRAM.
Card is misidentified as AMD Radeon Graphics (generic name).
Allocating beyond the cap causes a segmentation fault instead of a proper OOM error.

Attempted Workarounds (none worked)
All of the following env vars were tested individually and in combination — none changed the reported VRAM:
export GPU_MAX_ALLOC_PERCENT=100
export GPU_SINGLE_ALLOC_PERCENT=100
export HSA_ENABLE_SDMA=0
export ROCR_VISIBLE_DEVICES=0
export HSA_FORCE_FINE_GRAIN_PCIE=1
export PYTORCH_HIP_ALLOC_CONF=expandable_segments:True,max_split_size_mb:512
export HIP_VISIBLE_DEVICES=0
export ROCM_VISIBLE_DEVICES=0

Root Cause Hypothesis
The RX 9060 XT 16GB uses two 8GB GDDR6 modules on a 128-bit bus. It is suspected that PyTorch's HIP memory allocator or the ROCm topology reader is only enumerating one of the two memory modules, resulting in exactly half the VRAM being visible.
Evidence:

The cap is exactly 50% of physical VRAM (8GB out of 16GB)
rocminfo and the kernel driver both correctly see the full 16GB
cat /sys/class/kfd/kfd/topology/nodes//mem_banks//size_in_bytes returns empty output, suggesting the KFD topology layer is not properly enumerating memory banks for this card

Related Issues
https://github.com/deepbeepmeep/Wan2GP/issues/1341
https://github.com/ggml-org/llama.cpp/issues/21376
https://github.com/ROCm/ROCm/issues/5657

Versions
(venv) vinicius@vinicius-pc:~/ComfyUI$ curl -sL https://raw.githubusercontent.com/pytorch/pytorch/main/torch/utils/collect_env.py | python
Collecting environment information...
PyTorch version: 2.13.0a0+rocm7.13.0a20260416
Is debug build: False
CUDA used to build PyTorch: N/A
ROCM used to build PyTorch: 7.13.61040

OS: Linux Mint 22.2 (x86_64)
GCC version: (Ubuntu 15.2.0-14ubuntu124ppa1) 15.2.0
Clang version: 22.1.2 (https://github.com/llvm/llvm-project.git 1ab49a973e210e97d61e5db6557180dcb92c3e98)
CMake version: version 3.28.3
Libc version: glibc-2.39

Python version: 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-6.17.0-29-generic-x86_64-with-glibc2.39
Is CUDA available: True
CUDA runtime version: Could not collect
CUDA_MODULE_LOADING set to:
GPU models and configuration: AMD Radeon Graphics (gfx1200)
Nvidia driver version: Could not collect
cuDNN version: Could not collect
Is XPU available: False
HIP runtime version: 7.13.61040
MIOpen runtime version: 3.5.1
Is XNNPACK available: True
Caching allocator config: {'PYTORCH_HIP_ALLOC_CONF': 'expandable_segments:True'}

CPU:
Architecture: x86_64
CPU op-mode(s): 32-bit, 64-bit
Address sizes: 39 bits physical, 48 bits virtual
Byte Order: Little Endian
CPU(s): 8
On-line CPU(s) list: 0-7
Vendor ID: GenuineIntel
Model name: 12th Gen Intel(R) Core(TM) i3-12100F
CPU family: 6
Model: 151
Thread(s) per core: 2
Core(s) per socket: 4
Socket(s): 1
Stepping: 5
CPU(s) scaling MHz: 15%
CPU max MHz: 5500,0000
CPU min MHz: 800,0000
BogoMIPS: 6604,80
Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
Virtualization: VT-x
L1d cache: 192 KiB (4 instances)
L1i cache: 128 KiB (4 instances)
L2 cache: 5 MiB (4 instances)
L3 cache: 12 MiB (1 instance)
NUMA node(s): 1
NUMA node0 CPU(s): 0-7
Vulnerability Gather data sampling: Not affected
Vulnerability Ghostwrite: Not affected
Vulnerability Indirect target selection: Not affected
Vulnerability Itlb multihit: Not affected
Vulnerability L1tf: Not affected
Vulnerability Mds: Not affected
Vulnerability Meltdown: Not affected
Vulnerability Mmio stale data: Not affected
Vulnerability Old microcode: Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed: Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2: Mitigation; Enhanced / Automatic IBRS; IBPB conditional; PBRSB-eIBRS SW sequence; BHI BHI_DIS_S
Vulnerability Srbds: Not affected
Vulnerability Tsa: Not affected
Vulnerability Tsx async abort: Not affected
Vulnerability Vmscape: Mitigation; IBPB before exit to userspace

Versions of relevant libraries:
[pip3] numpy==2.4.3
[pip3] torch==2.13.0a0+rocm7.13.0a20260416
[pip3] torchaudio==2.11.0+rocm7.13.0a20260425
[pip3] torchsde==0.2.6
[pip3] torchvision==0.27.0a0+rocm7.13.0a20260416
[pip3] triton==3.7.0+git9e2c158e.rocm7.13.0a20260416
[pip3] triton-rocm==3.7.0
[conda] Could not collect
(venv) vinicius@vinicius-pc:~/ComfyUI$

cc @ptrblck @msaroufim @eqy @jerryzh168 @tinglvv @nWEIdia @jeffdaily @sunway513 @jithunnair-amd @pruthvistony @ROCmSupport @jataylo @hongxiayang @naromero77amd @pragupta @jerrymannil @xinyazhang

### Operating System

Linux Mint 22.2

### CPU

I3 12100F

### GPU

RX 9060 XT 16 GB

### ROCm Version

7.13

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.21
Runtime Ext Version:     1.20
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
  Name:                    12th Gen Intel(R) Core(TM) i3-12100F
  Uuid:                    CPU-XX                             
  Marketing Name:          12th Gen Intel(R) Core(TM) i3-12100F
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
  Max Clock Freq. (MHz):   5500                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    16211708(0xf75efc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16211708(0xf75efc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16211708(0xf75efc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16211708(0xf75efc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1200                            
  Uuid:                    GPU-1c5501acaf387d69               
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
    L2:                      4096(0x1000) KB                    
    L3:                      32768(0x8000) KB                   
  Chip ID:                 30096(0x7590)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2780                               
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 58                                 
  SDMA engine uCode::      380                                
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
      Name:                    amdgcn-amd-amdhsa--gfx1200         
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

_No response_

---

## 评论 (1 条)

### 评论 #1 — darren-amd (2026-05-26T18:52:20Z)

Hi @Badhunter0303,

Thanks for reporting the issue! This may be related to https://github.com/ROCm/TheRock/issues/4645 which was fixed with https://github.com/ROCm/rocm-systems/pull/5204. I gave this a try on a 9060 XT system locally and `print(torch.cuda.get_device_properties(0).total_memory // 1024**2, 'MB')` reported 16 GB as expected. Could you please upgrade your torch and give it another try:
```
pip install --force-reinstall --index-url https://rocm.nightlies.amd.com/v2/gfx120X-all/ "torch==2.10.0+rocm7.13.0a20260513" "torchvision==0.25.0+rocm7.13.0a20260513" "torchaudio==2.10.0+rocm7.13.0a20260513"
```

---
