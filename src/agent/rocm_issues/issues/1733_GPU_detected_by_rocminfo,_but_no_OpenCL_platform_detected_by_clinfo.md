# GPU detected by rocminfo, but no OpenCL platform detected by clinfo

> **Issue #1733**
> **状态**: closed
> **创建时间**: 2022-04-28T14:33:42Z
> **更新时间**: 2022-05-29T21:10:48Z
> **关闭时间**: 2022-05-29T21:10:48Z
> **作者**: JacekJagosz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1733

## 描述

I am packaging ROCm stack for Solus and I am facing quite a weird issue. (I'm building all the packages from source and not used AMDGPU-Pro).
When I run `rocminfo` it detects my GPU and I get normal looking output:
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

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 5 PRO 4650G with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 PRO 4650G with Radeon Graphics
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
  Compute Unit:            12                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    12203200(0xba34c0) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    12203200(0xba34c0) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    12203200(0xba34c0) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx90c                             
  Uuid:                    GPU-XX                             
  Marketing Name:                                             
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
    L2:                      1024(0x400) KB                     
  Chip ID:                 5686(0x1636)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1900                               
  BDFID:                   1024                               
  Internal Node ID:        1                                  
  Compute Unit:            7                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
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
      Size:                    4194304(0x400000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx90c:xnack+   
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
But running `clinfo` shipped with ROCm I get `ERROR: clGetPlatformIDs(-1001)`.
Also, it is not like it is not finding the libraries, strace shows it finds all the necessary ones:
```
strace -e openat rocm-clinfo
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/lib/libOpenCL.so.1", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/lib/haswell/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/lib/haswell/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/share/OpenCL/vendors", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
openat(AT_FDCWD, "/usr/share/OpenCL/vendors/amdocl64.icd", O_RDONLY) = 4
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/libamdocl64.so", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/librocclr.so.5.1", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/libamd_comgr.so.2", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/libclang-cpp.so.13", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/libLLVM-13.so", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/glibc-hwcaps/x86-64-v3/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/glibc-hwcaps/x86-64-v2/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/tls/haswell/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/tls/haswell/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/tls/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/haswell/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/haswell/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/haswell/libdrm.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/libdrm.so.2", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/haswell/libdrm_amdgpu.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/libdrm_amdgpu.so.1", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/../lib64/glibc-hwcaps/x86-64-v3/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/glibc-hwcaps/x86-64-v2/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/tls/haswell/x86_64/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/tls/haswell/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/tls/x86_64/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/tls/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/haswell/x86_64/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/haswell/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/x86_64/libffi.so.7", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/libffi.so.7", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/../lib64/haswell/libedit.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/libedit.so.0", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/../lib64/haswell/libz.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/libz.so.1", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/../lib64/haswell/libncursesw.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/libncursesw.so.6", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/../lib64/haswell/libxml2.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (Nie ma takiego pliku ani katalogu)
openat(AT_FDCWD, "/usr/lib/../lib64/libxml2.so.2", O_RDONLY|O_CLOEXEC) = 4
openat(AT_FDCWD, "/usr/lib/liblzma.so.5", O_RDONLY|O_CLOEXEC) = 4
ERROR: clGetPlatformIDs(-1001)
+++ exited with 1 +++
```
**Could anyone suggest what might be causing this problem? Any tips will be helpful.**
PS To make sure it is not just my hardware, I asked another person to test it with his rx 480 and the result is the same (I have enabled Polaris support when building it): https://pastebin.com/dVZXCQw8
PPS Here are the build files I used: https://github.com/JacekJagosz/rocm-Solus

---

## 评论 (2 条)

### 评论 #1 — CosmicFusion (2022-05-29T13:31:28Z)

You probably need one of these patches

https://github.com/xuhuisheng/rocm-build/tree/master/patch

---

### 评论 #2 — JacekJagosz (2022-05-29T21:10:48Z)

> You probably need one of these patches
> 
> https://github.com/xuhuisheng/rocm-build/tree/master/patch

Thanks for reply, but meanwhile I actually found the cause: https://reviews.llvm.org/D119478
It seems AMD renamed renoir from gfx902 to gfx90c, but didn't add 90c to supported architectures in Libomptarget.
So to fix it this one-line patch for LLVM needs to be included. It is a pity it is not in LLVM 14, but fortunately my distribution will include this patch for LLVM.

---
