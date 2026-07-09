# [Feature]: Request for ROCm Support: AMD PRO A8-8650B (R7, 10 Compute Cores)

- **Issue #:** 4359
- **State:** closed
- **Created:** 2025-02-08T16:39:14Z
- **Updated:** 2025-05-26T19:52:51Z
- **Labels:** Feature Request, ROCm 6.3.2
- **URL:** https://github.com/ROCm/ROCm/issues/4359

### Problem Description

### System Information
- **CPU/APU**: AMD PRO A8-8650B (R7, 10 Compute Cores, 3.7 GHz)
- **RAM**: 8GB
- **OS**: NixOS 25.05 (Kernel 6.12.9)
- **GPU Architecture**: GCN 2.0 (Volcanic Islands, Carrizo-based)

### Issue Description
I would like to request ROCm support for older APUs like the AMD PRO A8-8650B.  
This APU has an integrated Radeon R7 GPU based on the **GCN 2.0 (Volcanic Islands)** architecture.  

Currently, ROCm only officially supports **GCN 3.0+ (Hawaii and newer GPUs)**. However, many users with older AMD APUs still want to use ROCm for AI workloads (like Stable Diffusion).  

### Request
- Could ROCm be extended to support GCN 2.0-based APUs?
- Are there any workarounds or patches to enable partial ROCm support?

Thank you for considering this request!


**echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";**
```bash
OS:
NAME=NixOS
VERSION="25.05 (Warbler)"
```

**echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;**
```bash
CPU: 
model name	: AMD PRO A8-8650B R7, 10 Compute Cores 4C+6G
```
 
**echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";**
```bash
GPU:
  Name:                    AMD PRO A8-8650B R7, 10 Compute Cores 4C+6G
  Marketing Name:  AMD PRO A8-8650B R7, 10 Compute Cores 4C+6G
  Name:                    gfx700                             
  Marketing Name:  AMD Radeon R7 Graphics             
  Name:                    amdgcn-amd-amdhsa--gfx700
```

**hashcat -I**              
```bash
hashcat (6.2.6) starting in backend information mode

clGetPlatformIDs(): CL_PLATFORM_NOT_FOUND_KHR

ATTENTION! No OpenCL, HIP or CUDA compatible platform found.

You are probably missing the OpenCL, CUDA or HIP runtime installation.

* AMD GPUs on Linux require this driver:
  "AMDGPU" (21.50 or later) and "ROCm" (5.0 or later)
* Intel CPUs require this runtime:
  "OpenCL Runtime for Intel Core and Intel Xeon Processors" (16.1.1 or later)
* NVIDIA GPUs require this runtime and/or driver (both):
  "NVIDIA Driver" (440.64 or later)
  "CUDA Toolkit" (9.0 or later)
```

**nix-store --query --requisites $(which hipcc) | grep rocm**
```bash
/nix/store/av323b05mfq0qqz324p5v4a2h643ldh5-rocm-llvm-libunwind-6.0.2
```

### Operating System

NixOS 25

### CPU

AMD PRO A8-8650B R7, 10 Compute Cores 4C+6G

### GPU

AMD Radeon R7 Graphics

### ROCm Version

5.7.0

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support
```bash
/opt/rocm/bin/rocminfo --support
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
  Name:                    AMD PRO A8-8650B R7, 10 Compute Cores 4C+6G
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD PRO A8-8650B R7, 10 Compute Cores 4C+6G
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
  Max Clock Freq. (MHz):   3200                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            4                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    7065704(0x6bd068) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    7065704(0x6bd068) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    7065704(0x6bd068) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx700                             
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon R7 Graphics             
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
  Chip ID:                 4883(0x1313)                       
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   757                                
  BDFID:                   8                                  
  Internal Node ID:        1                                  
  Compute Unit:            6                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
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
  Packet Processor uCode:: 421                                
  SDMA engine uCode::      76                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    3532852(0x35e834) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    3532852(0x35e834) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx700          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE HSA_PROFILE_FULL  
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
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


_No response_

### hipcc --version
```bash
hipcc --version

sh: line 1: /opt/rocm/llvm/bin/clang: No such file or directory
/opt/rocm/bin/rocm_agent_enumerator:95: SyntaxWarning: invalid escape sequence '\w'
  @staticVars(search_name=re.compile("gfx[0-9a-fA-F]+(:[-+:\w]+)?"))
/opt/rocm/bin/rocm_agent_enumerator:152: SyntaxWarning: invalid escape sequence '\A'
  line_search_term = re.compile("\A\s+Name:\s+(amdgcn-amd-amdhsa--gfx\d+)")
/opt/rocm/bin/rocm_agent_enumerator:154: SyntaxWarning: invalid escape sequence '\A'
  line_search_term = re.compile("\A\s+Name:\s+(gfx\d+)")
/opt/rocm/bin/rocm_agent_enumerator:175: SyntaxWarning: invalid escape sequence '\w'
  target_search_term = re.compile("1002:\w+")
HIP version: 5.7.0-0
sh: line 1: /opt/rocm/llvm/bin/clang: No such file or directory
```
_No response_