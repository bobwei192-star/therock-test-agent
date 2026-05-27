# rocminfo works, but clinfo does not -> ERROR: clGetDeviceIDs(-1)

> **Issue #1063**
> **状态**: closed
> **创建时间**: 2020-03-28T14:22:44Z
> **更新时间**: 2021-04-05T10:14:21Z
> **关闭时间**: 2021-04-05T10:14:21Z
> **作者**: robinchrist
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1063

## 描述

OS: Kubuntu 19.10, Kernel 5.3.0-42
Hardware: TR1950X + Vega FE

Installing rocm succeeds, but OpenCL does not work.

```
opt/rocm/bin/rocminfo 
ROCk module is loaded
robin is member of video group
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
  Name:                    AMD Ryzen Threadripper 1950X 16-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 1950X 16-Core Processor
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
  Max Clock Freq. (MHz):   3400                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65778180(0x3ebb204) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65778180(0x3ebb204) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   3072                               
  Internal Node ID:        1                                  
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
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
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


```
/opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3084.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```

---

## 评论 (7 条)

### 评论 #1 — theedge456 (2020-04-02T07:47:48Z)

same symptoms with debian/buster.
 AMD Ryzen 7 2700U with Radeon Vega Mobile Gfx
 kernel 5.5.13
```
./clinfo -v
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3098.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

```

---

### 评论 #2 — preda (2020-04-02T11:44:59Z)

Try #1067

---

### 评论 #3 — theedge456 (2020-04-02T17:03:43Z)

strace showed that it could not find libtinfo.so.5, which I installed although libtinfo.so.6 is installed.
Now gdb shows a crash with libOpenCL.so.
```
#0  0x00007ffff628cdb0 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/libhsa-ext-image64.so.1
#1  0x00007ffff760d719 in amd::GpuAgent::GetInfo(hsa_agent_info_t, void*) const ()
   from /opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/libhsa-runtime64.so.1
#2  0x00007ffff76226c8 in HSA::hsa_agent_get_info(hsa_agent_s, hsa_agent_info_t, void*) ()
   from /opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/libhsa-runtime64.so.1
#3  0x00007ffff7a0d35f in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#4  0x00007ffff7a0dd5a in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#5  0x00007ffff7a0f563 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#6  0x00007ffff79d74bf in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#7  0x00007ffff79d2096 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#8  0x00007ffff79a4b15 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#9  0x00007ffff7b22e39 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#10 0x00007ffff79a4c4c in clIcdGetPlatformIDsKHR () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#11 0x00007ffff7e363c5 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libOpenCL.so.1
#12 0x00007ffff7e3818f in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libOpenCL.so.1
#13 0x00007ffff7e05997 in __pthread_once_slow (once_control=0x7ffff7e3c0d8, init_routine=0x7ffff7e37fb0)
    at pthread_once.c:116
#14 0x00007ffff7e368f1 in clGetPlatformIDs () from /opt/rocm-3.3.0/opencl/lib/x86_64/libOpenCL.so.1
#15 0x000000000040cdd1 in ?? ()
#16 0x0000000000403b8c in ?? ()
#17 0x00007ffff7c5909b in __libc_start_main (main=0x403aa0, argc=1, argv=0x7fffffffe148, init=<optimized out>, 
    fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe138) at ../csu/libc-start.c:308
#18 0x000000000040c1fe in ?? ()
(gdb) 
```
I will try to use the github repo instead of the xenial one.

---

### 评论 #4 — pqyptixa (2020-04-23T09:11:41Z)

@theedge456 were you able to fix/find a workaround for this issue?

---

### 评论 #5 — theedge456 (2020-05-16T11:11:32Z)

I tried to perform a build from the sources detailed [here](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#getting-the-rocm-source-code)
The problem is that there is no instruction about the directories to build to get OpenCL to work.

FYI, the available directories are:
```
# ls ROCm 
AMDMIGraphX              hipBLAS            MIOpenGEMM  ROCK-Kernel-Driver    rocm_smi_lib         ROC-smi
aomp                     hipCUB             MIVisionX   rocm_bandwidth_test   ROCmValidationSuite  rocSPARSE
atmi                     HIP-Examples       rccl        rocm-cmake            rocPRIM              rocThrust
clang-ocl                hipSPARSE          RCP         ROCm-CompilerSupport  rocprofiler          roctracer
hcc                      rocALUTION  ROCm-Device-Libs      rocRAND              ROCT-Thunk-Interface
HCC-Example-Application  llvm_amd-stg-open  rocBLAS     rocminfo              rocr_debug_agent
HIP                      MIOpen             rocFFT      ROCm-OpenCL-Runtime   ROCR-Runtime
```

---

### 评论 #6 — Rmalavally (2020-05-16T16:51:24Z)

Thank you for your feedback. Let me check with my team and get back to you about the missing instructions. 

---

### 评论 #7 — ROCmSupport (2021-04-05T10:14:21Z)

Thanks @robinchrist for reaching out.
This issue is fixed and no more observed with the latest ROCm 4.1, request you try with the same.
Feel free to open a new issue, if any, for quick resolution.
Thank you.

---
