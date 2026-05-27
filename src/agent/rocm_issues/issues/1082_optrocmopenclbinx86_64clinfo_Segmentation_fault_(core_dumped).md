# /opt/rocm/opencl/bin/x86_64/clinfo  Segmentation fault (core dumped)

> **Issue #1082**
> **状态**: closed
> **创建时间**: 2020-04-13T12:16:09Z
> **更新时间**: 2021-03-17T07:33:42Z
> **关闭时间**: 2021-03-17T07:33:41Z
> **作者**: pjones8404lml
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1082

## 描述

Ubuntu 18.04
The installation went smoothly with no bumps.  However, running CLinfo always ends up with a Core Dump.

My Name is in the vlog.  It is reading both the Ryzen and the RX580 card.

Here is the run from ~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
philip is member of video group
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
  Name:                    AMD Ryzen 5 3400G with Radeon Vega Graphics
  Marketing Name:          AMD Ryzen 5 3400G with Radeon Vega Graphics
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
    L1:                      32(0x20) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3900                               
  BDFID:                   2304                               
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16776832(0xfffe80) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Marketing Name:          AMD Ryzen 5 3400G with Radeon Vega Graphics
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4294967290                         
  BDFID:                   2304                               
  Internal Node ID:        0                                  
  Compute Unit:            11                                 
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
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
  Max Waves Per CU:        160(0xa0)                          
  Max Work-item Per CU:    10240(0x2800)                      
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack    
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
Agent 3                  
*******                  
  Name:                    gfx803                             
  Marketing Name:          Ellesmere [Radeon RX 470/480/570/570X/580/580X]
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
  Chip ID:                 26591(0x67df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1366                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            36                                 
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
      Size:                    8388608(0x800000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx803          
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



---

## 评论 (18 条)

### 评论 #1 — alejandromunozes (2020-04-22T16:53:46Z)

I too get a segmentation fault when I execute the command 'clinfo'. This is my rocminfo output:

```
ROCk module is loaded
alejandro is member of video group
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
  Name:                    AMD Ryzen 7 3700X 8-Core Processor 
  Marketing Name:          AMD Ryzen 7 3700X 8-Core Processor 
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
  Max Clock Freq. (MHz):   3600                               
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
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32901856(0x1f60ae0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32901856(0x1f60ae0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx906                             
  Marketing Name:          Vega 20 [Radeon VII]               
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
  Chip ID:                 26287(0x66af)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1802                               
  BDFID:                   12032                              
  Internal Node ID:        1                                  
  Compute Unit:            60                                 
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
      Name:                    amdgcn-amd-amdhsa--gfx906          
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
If you need more information, please, tell me.

---

### 评论 #2 — jcdutton (2020-04-25T07:58:29Z)

You could try:
strace -f clinfo 2>strace.txt
and then post the strace.txt file.
It might give some indication on where it is failing.


---

### 评论 #3 — LucasCampos (2020-04-26T21:49:49Z)

Not the same person, but similar issue. Using Ubuntu 20.04, and ROCm 3.3.

Output of `rocminfo`

```
[37mROCk module is loaded[0m
[37mlcampos is member of video group[0m
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
  Name:                    AMD Ryzen 5 2600 Six-Core Processor
  Marketing Name:          AMD Ryzen 5 2600 Six-Core Processor
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
  Compute Unit:            12                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16408144(0xfa5e50) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16408144(0xfa5e50) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Marketing Name:          Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
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
  Chip ID:                 26591(0x67df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1360                               
  BDFID:                   1536                               
  Internal Node ID:        1                                  
  Compute Unit:            36                                 
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
      Size:                    4194304(0x400000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx803          
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

output of `strace /opt/rocm/opencl/bin/x86_64/clinfo`

```
execve("/opt/rocm/opencl/bin/x86_64/clinfo", ["/opt/rocm/opencl/bin/x86_64/clin"...], 0x7fffec835390 /* 79 vars */) = 0
brk(NULL)                               = 0x932000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffef0ae2620) = -1 EINVAL (Invalid argument)
readlink("/proc/self/exe", "/opt/rocm-3.3.0/opencl/bin/x86_6"..., 4096) = 40
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f271e804000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/opencl/lib/x86_64/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/opencl/lib/x86_64/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/opencl/lib/x86_64/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/opencl/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/opencl/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/opencl/lib/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm/hsa/lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm/hip/lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hip/lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hip/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hip/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hip/lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hip/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hip/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hip/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hip/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../lib64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hsa/lib", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../hsa/lib", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hcc/lib", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../hip/lib", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../opencl/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/tls/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/tls/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/tls/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/tls/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/tls/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/tls", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/x86_64/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/x86_64/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/x86_64/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/x86_64", 0x7ffef0ae1870) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=130109, ...}) = 0
mmap(NULL, 130109, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f271e7e4000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/librt.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 7\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=40040, ...}) = 0
mmap(NULL, 44000, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f271e7d9000
mprotect(0x7f271e7dc000, 24576, PROT_NONE) = 0
mmap(0x7f271e7dc000, 16384, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f271e7dc000
mmap(0x7f271e7e0000, 4096, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x7000) = 0x7f271e7e0000
mmap(0x7f271e7e2000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x8000) = 0x7f271e7e2000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\300\363\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=1369352, ...}) = 0
mmap(NULL, 1368336, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f271e68a000
mmap(0x7f271e699000, 684032, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xf000) = 0x7f271e699000
mmap(0x7f271e740000, 618496, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xb6000) = 0x7f271e740000
mmap(0x7f271e7d7000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x14c000) = 0x7f271e7d7000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 \22\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=18816, ...}) = 0
mmap(NULL, 20752, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f271e684000
mmap(0x7f271e685000, 8192, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1000) = 0x7f271e685000
mmap(0x7f271e687000, 4096, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f271e687000
mmap(0x7f271e688000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f271e688000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libOpenCL.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libOpenCL.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\2201\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0775, st_size=34920, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f271e682000
mmap(NULL, 37088, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f271e678000
mmap(0x7f271e67b000, 12288, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f271e67b000
mmap(0x7f271e67e000, 8192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x6000) = 0x7f271e67e000
mmap(0x7f271e680000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x7000) = 0x7f271e680000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\3405\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=104984, ...}) = 0
mmap(NULL, 107592, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f271e65d000
mmap(0x7f271e660000, 73728, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f271e660000
mmap(0x7f271e672000, 16384, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x15000) = 0x7f271e672000
mmap(0x7f271e676000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x18000) = 0x7f271e676000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\201\0\0\0\0\0\0"..., 832) = 832
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0w\\\273\377\370\24Ef`xg\200\260\263\264\0"..., 68, 824) = 68
fstat(3, {st_mode=S_IFREG|0755, st_size=157224, ...}) = 0
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0w\\\273\377\370\24Ef`xg\200\260\263\264\0"..., 68, 824) = 68
mmap(NULL, 140408, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f271e63a000
mmap(0x7f271e641000, 69632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x7000) = 0x7f271e641000
mmap(0x7f271e652000, 20480, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x18000) = 0x7f271e652000
mmap(0x7f271e657000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1c000) = 0x7f271e657000
mmap(0x7f271e659000, 13432, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f271e659000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../lib/x86_64/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../hsa/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/bin/x86_64/../../../lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360q\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32, 848) = 32
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0cBR\340\305\370\2609W\242\345)q\235A\1"..., 68, 880) = 68
fstat(3, {st_mode=S_IFREG|0755, st_size=2029224, ...}) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32, 848) = 32
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0cBR\340\305\370\2609W\242\345)q\235A\1"..., 68, 880) = 68
mmap(NULL, 2036952, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f271e448000
mprotect(0x7f271e46d000, 1847296, PROT_NONE) = 0
mmap(0x7f271e46d000, 1540096, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x25000) = 0x7f271e46d000
mmap(0x7f271e5e5000, 303104, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19d000) = 0x7f271e5e5000
mmap(0x7f271e630000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1e7000) = 0x7f271e630000
mmap(0x7f271e636000, 13528, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f271e636000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f271e446000
arch_prctl(ARCH_SET_FS, 0x7f271e447180) = 0
mprotect(0x7f271e630000, 12288, PROT_READ) = 0
mprotect(0x7f271e657000, 4096, PROT_READ) = 0
mprotect(0x7f271e676000, 4096, PROT_READ) = 0
mprotect(0x7f271e7e2000, 4096, PROT_READ) = 0
mprotect(0x7f271e7d7000, 4096, PROT_READ) = 0
mprotect(0x7f271e688000, 4096, PROT_READ) = 0
mprotect(0x7f271e680000, 4096, PROT_READ) = 0
mprotect(0x486000, 20480, PROT_READ)    = 0
mprotect(0x7f271e833000, 4096, PROT_READ) = 0
munmap(0x7f271e7e4000, 130109)          = 0
set_tid_address(0x7f271e447450)         = 10066
set_robust_list(0x7f271e447460, 24)     = 0
rt_sigaction(SIGRTMIN, {sa_handler=0x7f271e641bf0, sa_mask=[], sa_flags=SA_RESTORER|SA_SIGINFO, sa_restorer=0x7f271e64f3c0}, NULL, 8) = 0
rt_sigaction(SIGRT_1, {sa_handler=0x7f271e641c90, sa_mask=[], sa_flags=SA_RESTORER|SA_RESTART|SA_SIGINFO, sa_restorer=0x7f271e64f3c0}, NULL, 8) = 0
rt_sigprocmask(SIG_UNBLOCK, [RTMIN RT_1], NULL, 8) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
brk(NULL)                               = 0x932000
brk(0x953000)                           = 0x953000
openat(AT_FDCWD, "/etc/OpenCL/vendors/", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(3, /* 3 entries */, 32768)   = 80
openat(AT_FDCWD, "/etc/OpenCL/vendors//amdocl64.icd", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=49, ...}) = 0
fstat(4, {st_mode=S_IFREG|0644, st_size=49, ...}) = 0
lseek(4, 0, SEEK_SET)                   = 0
read(4, "/opt/rocm-3.3.0/opencl/lib/x86_6"..., 49) = 49
lseek(4, 49, SEEK_SET)                  = 49
futex(0x7f271e6890c8, FUTEX_WAKE_PRIVATE, 2147483647) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0000q\3\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0775, st_size=3662720, ...}) = 0
mmap(NULL, 3700320, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271e0be000
mmap(0x7f271e0f4000, 2797568, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x36000) = 0x7f271e0f4000
mmap(0x7f271e39f000, 520192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x2e1000) = 0x7f271e39f000
mmap(0x7f271e41e000, 126976, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x35f000) = 0x7f271e41e000
mmap(0x7f271e43d000, 34400, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f271e43d000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0p\"\1\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=974800, ...}) = 0
mmap(NULL, 2869328, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271de01000
mprotect(0x7f271deb7000, 2097152, PROT_NONE) = 0
mmap(0x7f271e0b7000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0xb6000) = 0x7f271e0b7000
mmap(0x7f271e0bd000, 2128, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f271e0bd000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libhsakmt.so.1", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\200F\0\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=189592, ...}) = 0
mmap(NULL, 2261032, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271dbd8000
mprotect(0x7f271dbf2000, 2093056, PROT_NONE) = 0
mmap(0x7f271ddf1000, 61440, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x19000) = 0x7f271ddf1000
mmap(0x7f271de00000, 40, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f271de00000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/tls/x86_64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/tls/x86_64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/tls/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/tls/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/tls/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/tls", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib64/tls/x86_64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib64/tls/x86_64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib64/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib64/tls/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib64/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib64/tls/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib64/tls/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib64/tls", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib64/x86_64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib64/x86_64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib64/tls/x86_64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib64/tls/x86_64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib64/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib64/tls/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib64/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib64/tls/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib64/tls/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib64/tls", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib64/x86_64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib64/x86_64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib64/x86_64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib64", 0x7ffef0ae0a30) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 5
fstat(5, {st_mode=S_IFREG|0644, st_size=130109, ...}) = 0
mmap(NULL, 130109, PROT_READ, MAP_PRIVATE, 5, 0) = 0x7f271e7e4000
close(5)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libelf.so.1", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\2005\0\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=109200, ...}) = 0
mmap(NULL, 110976, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271dbbc000
mmap(0x7f271dbbf000, 73728, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x3000) = 0x7f271dbbf000
mmap(0x7f271dbd1000, 20480, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x15000) = 0x7f271dbd1000
mmap(0x7f271dbd6000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x19000) = 0x7f271dbd6000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\240\341\t\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=1952928, ...}) = 0
mmap(NULL, 1968128, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271d9db000
mprotect(0x7f271da71000, 1286144, PROT_NONE) = 0
mmap(0x7f271da71000, 983040, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x96000) = 0x7f271da71000
mmap(0x7f271db61000, 299008, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x186000) = 0x7f271db61000
mmap(0x7f271dbab000, 57344, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x1cf000) = 0x7f271dbab000
mmap(0x7f271dbb9000, 10240, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f271dbb9000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib64/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib64/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib64/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib64/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib64/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../lib64", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../hsa/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../hsa/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../hsa/lib/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../hsa/lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../hsa/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../hsa/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../hsa/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm/lib/../../hsa/lib/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hsa/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hsa/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hsa/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hsa/lib/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hsa/lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hsa/lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hsa/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hsa/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hsa/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hsa/lib", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../hsa/lib/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../hsa/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../hsa/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../hsa/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../hsa/lib/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../hsa/lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../hsa/lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../hsa/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../hsa/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../hsa/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../../hsa/lib", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hcc/lib/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hcc/lib/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hcc/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hcc/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hcc/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hcc/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hcc/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hcc/lib/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hcc/lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hcc/lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hcc/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hcc/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hcc/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hcc/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hcc/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hcc/lib", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hip/lib/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hip/lib/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hip/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hip/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hip/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hip/lib/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hip/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hip/lib/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hip/lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hip/lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hip/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hip/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hip/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hip/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../hip/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../hip/lib", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../opencl/lib/x86_64/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../opencl/lib/x86_64/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../opencl/lib/x86_64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../opencl/lib/x86_64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../opencl/lib/x86_64/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../opencl/lib/x86_64/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../opencl/lib/x86_64/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../opencl/lib/x86_64/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../opencl/lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../opencl/lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../opencl/lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../opencl/lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../opencl/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../opencl/lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/tls/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64/tls/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64/tls/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64/tls", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/../../lib/x86_64", 0x7ffef0ae09d0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libnuma.so.1", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0204\0\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=47960, ...}) = 0
mmap(NULL, 51104, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271d9ce000
mprotect(0x7f271d9d1000, 32768, PROT_NONE) = 0
mmap(0x7f271d9d1000, 20480, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x3000) = 0x7f271d9d1000
mmap(0x7f271d9d6000, 8192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x8000) = 0x7f271d9d6000
mmap(0x7f271d9d9000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0xa000) = 0x7f271d9d9000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpci.so.3", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\3008\0\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=64280, ...}) = 0
mmap(NULL, 66192, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271d9bd000
mprotect(0x7f271d9c0000, 49152, PROT_NONE) = 0
mmap(0x7f271d9c0000, 32768, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x3000) = 0x7f271d9c0000
mmap(0x7f271d9c8000, 12288, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0xb000) = 0x7f271d9c8000
mmap(0x7f271d9cc000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0xe000) = 0x7f271d9cc000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libz.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libz.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libz.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libz.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libz.so.1", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\200\"\0\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=108936, ...}) = 0
mmap(NULL, 110776, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271d9a1000
mprotect(0x7f271d9a3000, 98304, PROT_NONE) = 0
mmap(0x7f271d9a3000, 69632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x2000) = 0x7f271d9a3000
mmap(0x7f271d9b4000, 24576, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x13000) = 0x7f271d9b4000
mmap(0x7f271d9bb000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x19000) = 0x7f271d9bb000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libresolv.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libresolv.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libresolv.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libresolv.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libresolv.so.2", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 G\0\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=101320, ...}) = 0
mmap(NULL, 113280, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271d985000
mprotect(0x7f271d989000, 81920, PROT_NONE) = 0
mmap(0x7f271d989000, 65536, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x4000) = 0x7f271d989000
mmap(0x7f271d999000, 12288, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x14000) = 0x7f271d999000
mmap(0x7f271d99d000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x17000) = 0x7f271d99d000
mmap(0x7f271d99f000, 6784, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f271d99f000
close(5)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libudev.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libudev.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libudev.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libudev.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libudev.so.1", O_RDONLY|O_CLOEXEC) = 5
read(5, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\20X\0\0\0\0\0\0"..., 832) = 832
fstat(5, {st_mode=S_IFREG|0644, st_size=174272, ...}) = 0
mmap(NULL, 178440, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 5, 0) = 0x7f271d959000
mmap(0x7f271d95e000, 110592, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x5000) = 0x7f271d95e000
mmap(0x7f271d979000, 40960, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x20000) = 0x7f271d979000
mmap(0x7f271d983000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x29000) = 0x7f271d983000
close(5)                                = 0
mprotect(0x7f271d983000, 4096, PROT_READ) = 0
mprotect(0x7f271d99d000, 4096, PROT_READ) = 0
mprotect(0x7f271d9bb000, 4096, PROT_READ) = 0
mprotect(0x7f271d9cc000, 4096, PROT_READ) = 0
mprotect(0x7f271d9d9000, 4096, PROT_READ) = 0
brk(0x974000)                           = 0x974000
mprotect(0x7f271dbab000, 45056, PROT_READ) = 0
mprotect(0x7f271dbd6000, 4096, PROT_READ) = 0
mprotect(0x7f271ddf1000, 12288, PROT_READ) = 0
mprotect(0x7f271e0b7000, 20480, PROT_READ) = 0
mprotect(0x7f271e41e000, 102400, PROT_READ) = 0
openat(AT_FDCWD, "/proc/self/status", O_RDONLY) = 5
fstat(5, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(5, "Name:\tclinfo\nUmask:\t0002\nState:\t"..., 1024) = 1024
read(5, "00,00000000,00000000,00000000,00"..., 1024) = 363
close(5)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 5
fstat(5, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(5, /* 10 entries */, 32768)  = 312
openat(AT_FDCWD, "/sys/devices/system/node/node0/meminfo", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "Node 0 MemTotal:       16408144 "..., 4096) = 1173
read(6, "", 4096)                       = 0
close(6)                                = 0
getdents64(5, /* 0 entries */, 32768)   = 0
close(5)                                = 0
sched_getaffinity(0, 512, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) = 8
openat(AT_FDCWD, "/sys/devices/system/cpu", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 5
fstat(5, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(5, /* 29 entries */, 32768)  = 832
getdents64(5, /* 0 entries */, 32768)   = 0
close(5)                                = 0
openat(AT_FDCWD, "/proc/self/status", O_RDONLY) = 5
fstat(5, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(5, "Name:\tclinfo\nUmask:\t0002\nState:\t"..., 1024) = 1024
read(5, "00,00000000,00000000,00000000,00"..., 1024) = 363
read(5, "", 1024)                       = 0
close(5)                                = 0
uname({sysname="Linux", nodename="desktop", ...}) = 0
futex(0x7f271dbb96bc, FUTEX_WAKE_PRIVATE, 2147483647) = 0
futex(0x7f271dbb96c8, FUTEX_WAKE_PRIVATE, 2147483647) = 0
openat(AT_FDCWD, "/sys/devices/system/cpu", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 5
fstat(5, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(5, /* 29 entries */, 32768)  = 832
getdents64(5, /* 0 entries */, 32768)   = 0
close(5)                                = 0
openat(AT_FDCWD, "/proc/self/maps", O_RDONLY|O_CLOEXEC) = 5
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
fstat(5, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(5, "00400000-00403000 r--p 00000000 "..., 1024) = 1024
read(5, "libudev.so.1.6.17\n7f271d983000-7"..., 1024) = 1024
read(5, "3000 r--p 00000000 08:12 2369070"..., 1024) = 1024
read(5, "71d9cc000 ---p 0000e000 08:12 23"..., 1024) = 1024
read(5, "\n7f271d9db000-7f271da71000 r--p "..., 1024) = 1024
read(5, " 00015000 08:12 2367927         "..., 1024) = 1024
read(5, "    /opt/rocm-3.3.0/hsa/lib/libh"..., 1024) = 1024
read(5, "1e448000-7f271e46d000 r--p 00000"..., 1024) = 1024
read(5, "  /usr/lib/x86_64-linux-gnu/libp"..., 1024) = 1024
read(5, "e67b000-7f271e67e000 r-xp 000030"..., 1024) = 1024
read(5, "08:12 2367877                   "..., 1024) = 1024
read(5, "6                    /usr/lib/x8"..., 1024) = 1024
read(5, "\n7ffef0ac2000-7ffef0ae4000 rw-p "..., 1024) = 326
close(5)                                = 0
sched_getaffinity(10066, 32, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) = 8
brk(0x995000)                           = 0x995000
brk(0x9b6000)                           = 0x9b6000
brk(0x9d7000)                           = 0x9d7000
readlink("/proc/self/exe", "/opt/rocm-3.3.0/opencl/bin/x86_6"..., 1024) = 40
brk(0x9f8000)                           = 0x9f8000
brk(0xa1f000)                           = 0xa1f000
munmap(0x7f271e7e4000, 130109)          = 0
openat(AT_FDCWD, "/opt/rocm/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../lib64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hsa/lib", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../hsa/lib", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hcc/lib", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../hip/lib", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../opencl/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 5
fstat(5, {st_mode=S_IFREG|0644, st_size=130109, ...}) = 0
mmap(NULL, 130109, PROT_READ, MAP_PRIVATE, 5, 0) = 0x7f271e7e4000
close(5)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu", {st_mode=S_IFDIR|0755, st_size=106496, ...}) = 0
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/tls", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu", {st_mode=S_IFDIR|0755, st_size=106496, ...}) = 0
openat(AT_FDCWD, "/lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/tls", 0x7ffef0ae0d70)        = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64", 0x7ffef0ae0d70)     = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64", 0x7ffef0ae0d70)     = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/usr/lib/tls/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/tls/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/tls/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/tls/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/tls/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/tls", 0x7ffef0ae0d70)    = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64", 0x7ffef0ae0d70) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
munmap(0x7f271e7e4000, 130109)          = 0
openat(AT_FDCWD, "/opt/rocm/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../lib/x86_64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../hsa/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 5
fstat(5, {st_mode=S_IFREG|0644, st_size=130109, ...}) = 0
mmap(NULL, 130109, PROT_READ, MAP_PRIVATE, 5, 0) = 0x7f271e7e4000
close(5)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
munmap(0x7f271e7e4000, 130109)          = 0
openat(AT_FDCWD, "./libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "./libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
getpid()                                = 10066
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = 5
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/system_properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "platform_oem 314074538049\nplatfo"..., 4096) = 68
read(6, "", 4096)                       = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 4 entries */, 32768)   = 96
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/gpu_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/gpu_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "7146\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "cpu_cores_count 0\nsimd_count 144"..., 4096) = 634
read(7, "", 4096)                       = 0
openat(AT_FDCWD, "/dev/dri/renderD128", O_RDWR|O_CLOEXEC) = 8
close(7)                                = 0
close(6)                                = 0
access("/sys/bus/pci", R_OK)            = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/gpu_id", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "0\n", 4096)                    = 2
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "cpu_cores_count 12\nsimd_count 0\n"..., 4096) = 488
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/gpu_id", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "7146\n", 4096)                 = 5
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "cpu_cores_count 0\nsimd_count 144"..., 4096) = 634
read(6, "", 4096)                       = 0
openat(AT_FDCWD, "/usr/share/misc/pci.ids.gz", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/misc/pci.ids", O_RDONLY) = 7
lseek(7, 0, SEEK_CUR)                   = 0
read(7, "#\n#\tList of PCI ID's\n#\n#\tVersion"..., 8192) = 8192
read(7, "2 SCSI host adapter\n\t\t1de1 3906 "..., 16384) = 16384
brk(0xa41000)                           = 0xa41000
read(7, "MSP3JD160J\n\t00ac  SAS3416 Fusion"..., 16384) = 16384
read(7, "Motherboard\n\t4381  SB600 SATA Co"..., 16384) = 16384
read(7, "Embedded Radeon 7000-M\n\t\t1028 01"..., 16384) = 16384
read(7, "5 0513  Radeon HD 6650M\n\t\t1025 0"..., 16384) = 16384
read(7, "deon RX 470\n\t\t1462 3413  Radeon "..., 16384) = 16384
read(7, " HD 6550A\n\t\t1462 2246  Radeon HD"..., 16384) = 16384
brk(0xa63000)                           = 0xa63000
read(7, "95E\n\t\t17f2 5000  KI690-AM2 Mothe"..., 16384) = 16384
read(7, " CS5535 ISA bridge\n\t002d  CS5535"..., 16384) = 16384
read(7, " 2 ports\n\t13ef  Ariel ZCN/MP4\n\t1"..., 16384) = 16384
read(7, "2P] System Controller\n\t700d  AMD"..., 16384) = 16384
read(7, "  Millennium G550 LP PCIE\n\t2537 "..., 16384) = 16384
read(7, "oller\n\t\t103c 3237  E500 SAS Cont"..., 16384) = 16384
brk(0xa85000)                           = 0xa85000
read(7, "er\n\t\t175c 8800  ASI88xx Audio Ad"..., 16384) = 16384
read(7, "0  DS-1 Audio\n\t1000  SW1000XG [X"..., 16384) = 16384
read(7, "CI bus bridge [db21554]\n\t6340  I"..., 16384) = 16384
read(7, " 77dc  cRIO-9036\n\t\t1093 77dd  cR"..., 16384) = 16384
read(7, "8747 48-Lane, 5-Port PCI Express"..., 16384) = 16384
brk(0xaa7000)                           = 0xaa7000
read(7, "SB 1.1 Controller\n\t\t1014 0540  T"..., 16384) = 16384
read(7, "infast NF3250K8AA\n\t\t1462 7030  K"..., 16384) = 16384
read(7, "33f  NV35GL [Quadro FX 700]\n\t034"..., 16384) = 16384
read(7, "MCP78S [GeForce 8200] Co-Process"..., 16384) = 16384
read(7, "ce 940MX]\n\t0fc0  GK107 [GeForce "..., 16384) = 16384
read(7, "de 101b  GRID K260Q\n\t11b1  GK104"..., 16384) = 16384
brk(0xac9000)                           = 0xac9000
read(7, "b Fibre Channel Adapter\n\t\t1014 0"..., 16384) = 16384
read(7, " SATA-II Controller\n\t9100  INI-9"..., 16384) = 16384
read(7, "k ALC 650)\n\t\t1297 c160  FX41 mot"..., 16384) = 16384
read(7, " 6113RS/6513RS\n\t0137  GDT 6123RS"..., 16384) = 16384
read(7, "isco Systems Inc\n\t0023  VIC 81 P"..., 16384) = 16384
read(7, "s Communications\n116a  Luminex S"..., 16384) = 16384
brk(0xaeb000)                           = 0xaeb000
read(7, "\t\t11ab 3621  Marvell RDK-8036\n\t\t"..., 16384) = 16384
read(7, "uting Devices International\n11f6"..., 16384) = 16384
read(7, "reless PCI Adapter (rev E1) [ISL"..., 16384) = 16384
read(7, "CTI PCI UART 4\n\t0322  CTI PCI UA"..., 16384) = 16384
read(7, "t Copper Ethernet PCI-X BGE base"..., 16384) = 16384
brk(0xb0d000)                           = 0xb0d000
read(7, " ME-6000/8/DIO\n\t604f  ME-6000/16"..., 16384) = 16384
read(7, "ller\n\t50a4  T540-50A4 Unified Wi"..., 16384) = 16384
read(7, "Wire Ethernet Controller [VF]\n\t5"..., 16384) = 16384
read(7, "802.11bgn Wireless Network Adapt"..., 16384) = 16384
read(7, "40-2T 10GBase-T Network Adapter\n"..., 16384) = 16384
read(7, " combo cardbus [GC89]\n\t4350  BCM"..., 16384) = 16384
brk(0xb2f000)                           = 0xb2f000
read(7, "er\n\t0124  EV1000 Mouse controlle"..., 16384) = 16384
read(7, "GbE MCX4121A-XCAT\n\t\t15b3 0005  M"..., 16384) = 16384
read(7, ") Wireless cardbus adapter\n\t\t118"..., 16384) = 16384
read(7, "nfigurable Virtex-5 FPGA with pl"..., 16384) = 16384
read(7, "80  ARC-1680 8/12/16/24 Port PCI"..., 16384) = 16384
read(7, "NT40E3-4-PTP Network Adapter 4x1"..., 16384) = 16384
brk(0xb51000)                           = 0xb51000
read(7, "NC554FLB 10Gb 2-port FlexFabric "..., 16384) = 16384
read(7, "/ decoder\n\t5310  BC-H16480A 16 p"..., 16384) = 16384
read(7, "Profile SmartNIC\n\t3310  10-Giga "..., 16384) = 16384
read(7, "6ca8  PCI-DA12-8 8x 12-bit Analo"..., 16384) = 16384
read(7, "  P8 series motherboard\n\t\t8086 2"..., 16384) = 16384
read(7, "ss-AC 7265\n# Stone Peak 2 AGN\n\t\t"..., 16384) = 16384
brk(0xb73000)                           = 0xb73000
read(7, "n E5 v2/Core i7 Integrated Memor"..., 16384) = 16384
read(7, "1000 CT Network Connection\n\t1076"..., 16384) = 16384
read(7, "ernet Adapter (10/100)\n\t\t1179 00"..., 16384) = 16384
read(7, "r\n\t\t103c 22fd  Ethernet 10Gb 2-p"..., 16384) = 16384
read(7, "ller 2/SC\n\t\t1028 0467  PowerEdge"..., 16384) = 16384
read(7, "16 Chipset Family PCI Express Ro"..., 16384) = 16384
brk(0xb95000)                           = 0xb95000
read(7, "028 040a  Latitude E6410\n\t\t1028 "..., 16384) = 16384
read(7, "-7065)\n\t\t1565 3101  P4TSV Mother"..., 16384) = 16384
read(7, "34  Compaq nw8240/nx8220\n\t\t103c "..., 16384) = 16384
read(7, " R60e\n\t\t8086 544b  Desktop Board"..., 16384) = 16384
read(7, "6 5044  Desktop Board DP35DP\n\t\te"..., 16384) = 16384
read(7, "hannel 2 Rank Registers\n\t2c33  X"..., 16384) = 16384
brk(0xbb6000)                           = 0xbb6000
read(7, "n E5 v3/Core i7 DDRIO (VMSE) 0 &"..., 16384) = 16384
read(7, "X722 for 10GbE SFP+\n\t\t17aa 4020 "..., 16384) = 16384
read(7, "5/Core i7 QPI Link Reut 1\n\t3ca0 "..., 16384) = 16384
read(7, " Xeon E7 v4/Xeon E5 v4/Xeon E3 v"..., 16384) = 16384
read(7, "ntroller Hub EG20T USB OHCI Cont"..., 16384) = 16384
read(7, "roller\n\t9cc7  Wildcat Point-LP L"..., 16384) = 16384
brk(0xbd8000)                           = 0xbd8000
read(7, "ipset Family USB 3.0 xHCI Contro"..., 16384) = 16384
read(7, "ernal 12G SAS Port/PCIe 3.0\n\t028"..., 16384) = 16384
read(7, "b09  Corvid 24\n\tdb11  T-Tap\n\tdca"..., 16384) = 6067
read(7, "", 10317)                      = 0
read(7, "", 16384)                      = 0
close(7)                                = 0
close(6)                                = 0
brk(0xbd6000)                           = 0xbd6000
brk(0xbd4000)                           = 0xbd4000
brk(0xbd2000)                           = 0xbd2000
brk(0xbd0000)                           = 0xbd0000
brk(0xbce000)                           = 0xbce000
brk(0xbcc000)                           = 0xbcc000
brk(0xbca000)                           = 0xbca000
brk(0xbc8000)                           = 0xbc8000
brk(0xbc6000)                           = 0xbc6000
brk(0xbc4000)                           = 0xbc4000
brk(0xbc2000)                           = 0xbc2000
brk(0xbc0000)                           = 0xbc0000
brk(0xbbe000)                           = 0xbbe000
brk(0xbbc000)                           = 0xbbc000
brk(0xbba000)                           = 0xbba000
brk(0xbb8000)                           = 0xbb8000
brk(0xbb6000)                           = 0xbb6000
brk(0xbb4000)                           = 0xbb4000
brk(0xbb2000)                           = 0xbb2000
brk(0xbb0000)                           = 0xbb0000
brk(0xbae000)                           = 0xbae000
brk(0xbac000)                           = 0xbac000
brk(0xbaa000)                           = 0xbaa000
brk(0xba8000)                           = 0xba8000
brk(0xba6000)                           = 0xba6000
brk(0xba3000)                           = 0xba3000
brk(0xba1000)                           = 0xba1000
brk(0xb9f000)                           = 0xb9f000
brk(0xb9d000)                           = 0xb9d000
brk(0xb9b000)                           = 0xb9b000
brk(0xb99000)                           = 0xb99000
brk(0xb97000)                           = 0xb97000
brk(0xb95000)                           = 0xb95000
brk(0xb93000)                           = 0xb93000
brk(0xb91000)                           = 0xb91000
brk(0xb8f000)                           = 0xb8f000
brk(0xb8d000)                           = 0xb8d000
brk(0xb8b000)                           = 0xb8b000
brk(0xb89000)                           = 0xb89000
brk(0xb87000)                           = 0xb87000
brk(0xb85000)                           = 0xb85000
brk(0xb83000)                           = 0xb83000
brk(0xb81000)                           = 0xb81000
brk(0xb7f000)                           = 0xb7f000
brk(0xb7d000)                           = 0xb7d000
brk(0xb7b000)                           = 0xb7b000
brk(0xb79000)                           = 0xb79000
brk(0xb77000)                           = 0xb77000
brk(0xb75000)                           = 0xb75000
brk(0xb73000)                           = 0xb73000
brk(0xb71000)                           = 0xb71000
brk(0xb6f000)                           = 0xb6f000
brk(0xb6d000)                           = 0xb6d000
brk(0xb6b000)                           = 0xb6b000
brk(0xb69000)                           = 0xb69000
brk(0xb67000)                           = 0xb67000
brk(0xb65000)                           = 0xb65000
brk(0xb63000)                           = 0xb63000
brk(0xb61000)                           = 0xb61000
brk(0xb5f000)                           = 0xb5f000
brk(0xb5d000)                           = 0xb5d000
brk(0xb5b000)                           = 0xb5b000
brk(0xb59000)                           = 0xb59000
brk(0xb57000)                           = 0xb57000
brk(0xb55000)                           = 0xb55000
brk(0xb53000)                           = 0xb53000
brk(0xb51000)                           = 0xb51000
brk(0xb4f000)                           = 0xb4f000
brk(0xb4d000)                           = 0xb4d000
brk(0xb4b000)                           = 0xb4b000
brk(0xb49000)                           = 0xb49000
brk(0xb47000)                           = 0xb47000
brk(0xb45000)                           = 0xb45000
brk(0xb43000)                           = 0xb43000
brk(0xb41000)                           = 0xb41000
brk(0xb3f000)                           = 0xb3f000
brk(0xb3d000)                           = 0xb3d000
brk(0xb3b000)                           = 0xb3b000
brk(0xb39000)                           = 0xb39000
brk(0xb37000)                           = 0xb37000
brk(0xb35000)                           = 0xb35000
brk(0xb33000)                           = 0xb33000
brk(0xb31000)                           = 0xb31000
brk(0xb2f000)                           = 0xb2f000
brk(0xb2d000)                           = 0xb2d000
brk(0xb2b000)                           = 0xb2b000
brk(0xb29000)                           = 0xb29000
brk(0xb27000)                           = 0xb27000
brk(0xb25000)                           = 0xb25000
brk(0xb23000)                           = 0xb23000
brk(0xb21000)                           = 0xb21000
brk(0xb1f000)                           = 0xb1f000
brk(0xb1d000)                           = 0xb1d000
brk(0xb1b000)                           = 0xb1b000
brk(0xb19000)                           = 0xb19000
brk(0xb17000)                           = 0xb17000
brk(0xb15000)                           = 0xb15000
brk(0xb13000)                           = 0xb13000
brk(0xb11000)                           = 0xb11000
brk(0xb0f000)                           = 0xb0f000
brk(0xb0d000)                           = 0xb0d000
brk(0xb0b000)                           = 0xb0b000
brk(0xb09000)                           = 0xb09000
brk(0xb07000)                           = 0xb07000
brk(0xb05000)                           = 0xb05000
brk(0xb03000)                           = 0xb03000
brk(0xb01000)                           = 0xb01000
brk(0xaff000)                           = 0xaff000
brk(0xafd000)                           = 0xafd000
brk(0xafb000)                           = 0xafb000
brk(0xaf9000)                           = 0xaf9000
brk(0xaf7000)                           = 0xaf7000
brk(0xaf5000)                           = 0xaf5000
brk(0xaf3000)                           = 0xaf3000
brk(0xaf1000)                           = 0xaf1000
brk(0xaef000)                           = 0xaef000
brk(0xaed000)                           = 0xaed000
brk(0xaeb000)                           = 0xaeb000
brk(0xae9000)                           = 0xae9000
brk(0xae7000)                           = 0xae7000
brk(0xae5000)                           = 0xae5000
brk(0xae3000)                           = 0xae3000
brk(0xae1000)                           = 0xae1000
brk(0xadf000)                           = 0xadf000
brk(0xadd000)                           = 0xadd000
brk(0xadb000)                           = 0xadb000
brk(0xad9000)                           = 0xad9000
brk(0xad7000)                           = 0xad7000
brk(0xad5000)                           = 0xad5000
brk(0xad3000)                           = 0xad3000
brk(0xad1000)                           = 0xad1000
brk(0xacf000)                           = 0xacf000
brk(0xacd000)                           = 0xacd000
brk(0xacb000)                           = 0xacb000
brk(0xac9000)                           = 0xac9000
brk(0xac7000)                           = 0xac7000
brk(0xac5000)                           = 0xac5000
brk(0xac3000)                           = 0xac3000
brk(0xac1000)                           = 0xac1000
brk(0xabf000)                           = 0xabf000
brk(0xabd000)                           = 0xabd000
brk(0xabb000)                           = 0xabb000
brk(0xab9000)                           = 0xab9000
brk(0xab7000)                           = 0xab7000
brk(0xab5000)                           = 0xab5000
brk(0xab3000)                           = 0xab3000
brk(0xab1000)                           = 0xab1000
brk(0xaaf000)                           = 0xaaf000
brk(0xaad000)                           = 0xaad000
brk(0xaab000)                           = 0xaab000
brk(0xaa9000)                           = 0xaa9000
brk(0xaa7000)                           = 0xaa7000
brk(0xaa5000)                           = 0xaa5000
brk(0xaa3000)                           = 0xaa3000
brk(0xaa1000)                           = 0xaa1000
brk(0xa9f000)                           = 0xa9f000
brk(0xa9d000)                           = 0xa9d000
brk(0xa9b000)                           = 0xa9b000
brk(0xa99000)                           = 0xa99000
brk(0xa97000)                           = 0xa97000
brk(0xa95000)                           = 0xa95000
brk(0xa93000)                           = 0xa93000
brk(0xa91000)                           = 0xa91000
brk(0xa8f000)                           = 0xa8f000
brk(0xa8d000)                           = 0xa8d000
brk(0xa8b000)                           = 0xa8b000
brk(0xa89000)                           = 0xa89000
brk(0xa87000)                           = 0xa87000
brk(0xa85000)                           = 0xa85000
brk(0xa83000)                           = 0xa83000
brk(0xa81000)                           = 0xa81000
brk(0xa7f000)                           = 0xa7f000
brk(0xa7d000)                           = 0xa7d000
brk(0xa7b000)                           = 0xa7b000
brk(0xa79000)                           = 0xa79000
brk(0xa77000)                           = 0xa77000
brk(0xa75000)                           = 0xa75000
brk(0xa73000)                           = 0xa73000
brk(0xa71000)                           = 0xa71000
brk(0xa6f000)                           = 0xa6f000
brk(0xa6d000)                           = 0xa6d000
brk(0xa6b000)                           = 0xa6b000
brk(0xa69000)                           = 0xa69000
brk(0xa67000)                           = 0xa67000
brk(0xa65000)                           = 0xa65000
brk(0xa63000)                           = 0xa63000
brk(0xa61000)                           = 0xa61000
brk(0xa5f000)                           = 0xa5f000
brk(0xa5d000)                           = 0xa5d000
brk(0xa5b000)                           = 0xa5b000
brk(0xa59000)                           = 0xa59000
brk(0xa57000)                           = 0xa57000
brk(0xa55000)                           = 0xa55000
brk(0xa53000)                           = 0xa53000
brk(0xa51000)                           = 0xa51000
brk(0xa4f000)                           = 0xa4f000
brk(0xa4d000)                           = 0xa4d000
brk(0xa4b000)                           = 0xa4b000
brk(0xa49000)                           = 0xa49000
brk(0xa47000)                           = 0xa47000
brk(0xa45000)                           = 0xa45000
brk(0xa43000)                           = 0xa43000
brk(0xa41000)                           = 0xa41000
brk(0xa3f000)                           = 0xa3f000
brk(0xa3d000)                           = 0xa3d000
brk(0xa3b000)                           = 0xa3b000
brk(0xa39000)                           = 0xa39000
brk(0xa25000)                           = 0xa25000
ioctl(5, AMDKFD_IOC_GET_PROCESS_APERTURES_NEW, 0x7ffef0ae1450) = 0
ioctl(5, AMDKFD_IOC_ACQUIRE_VM, 0x7ffef0ae1450) = 0
mmap(0x1000000, 68702699520, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_NORESERVE, -1, 0) = 0x1000000
ioctl(5, AMDKFD_IOC_SET_MEMORY_POLICY, 0x7ffef0ae1450) = 0
ioctl(5, AMDKFD_IOC_ALLOC_MEMORY_OF_GPU, 0x7ffef0ae1310) = -1 ENOMEM (Cannot allocate memory)
mbind(0x1001000, 8192, MPOL_DEFAULT, NULL, 0, 0) = 0
mmap(0x1001000, 8192, PROT_NONE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS|MAP_NORESERVE, -1, 0) = 0x1001000
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 6
fstat(6, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(6, /* 26 entries */, 32768)  = 984
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_pass_pretrans", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x02\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/int_dte_hit", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0f\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/int_dte_mis", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x10\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_iommu_tlb_pde_hit", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x08\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_iommu_tlb_pde_mis", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x09\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/smi_recv", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x17\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_dte_hit", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0a\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_dte_mis", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0b\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/page_tbl_read_nst", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0d\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_trans_total", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x05\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/page_tbl_read_gst", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0e\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/vapic_int_non_guest", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x15\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/tlb_inv", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x13\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/vapic_int_guest", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x16\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/ign_rd_wr_mmio_1ff8h", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x14\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/smi_blk", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x18\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_pass_untrans", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x01\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/cmd_processed_inv", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x12\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_iommu_tlb_pte_hit", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x06\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_target_abort", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x04\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/cmd_processed", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x11\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_iommu_tlb_pte_mis", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x07\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/page_tbl_read_tot", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0c\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_pass_excl", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x03\n", 4096)         = 13
close(7)                                = 0
getdents64(6, /* 0 entries */, 32768)   = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/perf/iommu/max_concurrent", O_RDONLY) = -1 ENOENT (No such file or directory)
close(6)                                = 0
statfs("/dev/shm/", {f_type=TMPFS_MAGIC, f_bsize=4096, f_blocks=2051018, f_bfree=2017064, f_bavail=2017064, f_files=2051018, f_ffree=2050944, f_fsid={val=[0, 0]}, f_namelen=255, f_frsize=4096, f_flags=ST_VALID|ST_NOSUID|ST_NODEV}) = 0
futex(0x7f271e65c390, FUTEX_WAKE_PRIVATE, 2147483647) = 0
openat(AT_FDCWD, "/dev/shm/sem.hsakmt_semaphore", O_RDWR|O_NOFOLLOW) = -1 EACCES (Permission denied)
ioctl(5, AMDKFD_IOC_GET_VERSION, 0x7ffef0ae13d0) = 0
openat(AT_FDCWD, "/sys/devices/system/cpu/online", O_RDONLY|O_CLOEXEC) = 6
read(6, "0-11\n", 8192)                 = 5
close(6)                                = 0
openat(AT_FDCWD, "/proc/cpuinfo", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(6, "processor\t: 0\nvendor_id\t: Authen"..., 1024) = 1024
read(6, "asid decodeassists pausefilter p"..., 1024) = 1024
read(6, "mp_legacy svm extapic cr8_legacy"..., 1024) = 1024
read(6, "_exception\t: yes\ncpuid level\t: 1"..., 1024) = 1024
read(6, "s virtual\npower management: ts t"..., 1024) = 1024
read(6, "f xsaveerptr arat npt lbrv svm_l"..., 1024) = 1024
read(6, "sse3 fma cx16 sse4_1 sse4_2 movb"..., 1024) = 1024
read(6, " 12\ncore id\t\t: 6\ncpu cores\t: 6\na"..., 1024) = 1024
read(6, "lflush size\t: 64\ncache_alignment"..., 1024) = 1024
read(6, " rdseed adx smap clflushopt sha_"..., 1024) = 1024
read(6, "p_good nopl nonstop_tsc cpuid ex"..., 1024) = 1024
read(6, "0x800820d\ncpu MHz\t\t: 1835.756\nca"..., 1024) = 1024
read(6, "spectre_v2 spec_store_bypass\nbog"..., 1024) = 1024
read(6, "waitx cpb hw_pstate sme ssbd sev"..., 1024) = 1024
read(6, "fxsr sse sse2 ht syscall nx mmxe"..., 1024) = 1024
read(6, ": 8\nmodel name\t: AMD Ryzen 5 260"..., 1024) = 1024
read(6, "oad vgif overflow_recov succor s"..., 1024) = 306
read(6, "", 1024)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/generation_id", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "2\n", 4096)                    = 2
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/system_properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "platform_oem 314074538049\nplatfo"..., 4096) = 68
read(6, "", 4096)                       = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 4 entries */, 32768)   = 96
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/gpu_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/gpu_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "7146\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "cpu_cores_count 0\nsimd_count 144"..., 4096) = 634
read(7, "", 4096)                       = 0
close(7)                                = 0
close(6)                                = 0
access("/sys/bus/pci", R_OK)            = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/gpu_id", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "0\n", 4096)                    = 2
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "cpu_cores_count 12\nsimd_count 0\n"..., 4096) = 488
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/mem_banks/0/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "heap_type 0\nsize_in_bytes 168019"..., 4096) = 72
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 6
fstat(6, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(6, /* 153 entries */, 32768) = 4800
getdents64(6, /* 0 entries */, 32768)   = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 6
fstat(6, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(6, /* 153 entries */, 32768) = 4800
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu11/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu11/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "5,11\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu11/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "5,11\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu11/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "5,11\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu11/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3-5,9-11\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu9/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu9/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3,9\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu9/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3,9\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu9/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3,9\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu9/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3-5,9-11\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu7/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu7/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1,7\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu7/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1,7\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu7/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1,7\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu7/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0-2,6-8\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "5,11\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index0/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index0/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Data\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index0/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "32K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index0/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index0/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index0/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index0/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000820\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "5,11\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index1/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index1/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Instruction\n", 4096)          = 12
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index1/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index1/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index1/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index1/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index1/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000820\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "5,11\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index2/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index2/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Unified\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index2/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "512K\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index2/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index2/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index2/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index2/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000820\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu5/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3-5,9-11\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3,9\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index0/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index0/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Data\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index0/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "32K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index0/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index0/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index0/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index0/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000208\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3,9\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index1/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index1/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Instruction\n", 4096)          = 12
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index1/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index1/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index1/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index1/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index1/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000208\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3,9\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index2/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index2/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Unified\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index2/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "512K\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index2/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index2/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index2/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index2/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000208\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3-5,9-11\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index3/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index3/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Unified\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index3/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8192K\n", 4096)                = 6
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index3/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index3/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "16\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index3/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu3/cache/index3/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000e38\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1,7\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index0/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index0/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Data\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index0/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "32K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index0/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index0/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index0/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index0/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000082\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1,7\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index1/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index1/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Instruction\n", 4096)          = 12
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index1/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index1/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index1/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index1/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index1/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000082\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1,7\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index2/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index2/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Unified\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index2/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "512K\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index2/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index2/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index2/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index2/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000082\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu1/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0-2,6-8\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu10/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu10/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4,10\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu10/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4,10\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu10/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4,10\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu10/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3-5,9-11\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu8/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu8/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2,8\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu8/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2,8\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu8/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2,8\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu8/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0-2,6-8\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu6/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu6/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0,6\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu6/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0,6\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu6/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0,6\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu6/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0-2,6-8\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4,10\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index0/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index0/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Data\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index0/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "32K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index0/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index0/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index0/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index0/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000410\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4,10\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index1/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index1/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Instruction\n", 4096)          = 12
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index1/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index1/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index1/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index1/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index1/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000410\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4,10\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index2/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index2/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Unified\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index2/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "512K\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index2/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index2/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index2/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index2/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000410\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu4/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3-5,9-11\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2,8\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index0/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index0/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Data\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index0/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "32K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index0/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index0/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index0/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index0/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000104\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2,8\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index1/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index1/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Instruction\n", 4096)          = 12
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index1/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index1/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index1/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index1/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index1/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000104\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2,8\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index2/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index2/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Unified\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index2/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "512K\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index2/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index2/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index2/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index2/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000104\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu2/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0-2,6-8\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 7
fstat(7, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(7, /* 7 entries */, 32768)   = 208
getdents64(7, /* 0 entries */, 32768)   = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index0/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0,6\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index0/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index0/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Data\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index0/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "32K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index0/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index0/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index0/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index0/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000041\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index1/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0,6\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index1/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index1/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Instruction\n", 4096)          = 12
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index1/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64K\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index1/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index1/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "4\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index1/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index1/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000041\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index2/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0,6\n", 4096)                  = 4
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index2/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index2/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Unified\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index2/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "512K\n", 4096)                 = 5
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index2/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index2/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index2/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index2/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "00000041\n", 4096)             = 9
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index3/shared_cpu_list", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0-2,6-8\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index3/level", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "3\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index3/type", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "Unified\n", 4096)              = 8
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index3/size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "8192K\n", 4096)                = 6
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index3/coherency_line_size", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "64\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index3/ways_of_associativity", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "16\n", 4096)                   = 3
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index3/physical_line_partition", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "1\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node/node0/cpu0/cache/index3/shared_cpu_map", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "000001c7\n", 4096)             = 9
close(7)                                = 0
getdents64(6, /* 0 entries */, 32768)   = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/gpu_id", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "7146\n", 4096)                 = 5
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "cpu_cores_count 0\nsimd_count 144"..., 4096) = 634
read(6, "", 4096)                       = 0
openat(AT_FDCWD, "/usr/share/misc/pci.ids.gz", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/misc/pci.ids", O_RDONLY) = 7
lseek(7, 0, SEEK_CUR)                   = 0
read(7, "#\n#\tList of PCI ID's\n#\n#\tVersion"..., 8192) = 8192
read(7, "2 SCSI host adapter\n\t\t1de1 3906 "..., 16384) = 16384
brk(0xa46000)                           = 0xa46000
read(7, "MSP3JD160J\n\t00ac  SAS3416 Fusion"..., 16384) = 16384
read(7, "Motherboard\n\t4381  SB600 SATA Co"..., 16384) = 16384
read(7, "Embedded Radeon 7000-M\n\t\t1028 01"..., 16384) = 16384
read(7, "5 0513  Radeon HD 6650M\n\t\t1025 0"..., 16384) = 16384
read(7, "deon RX 470\n\t\t1462 3413  Radeon "..., 16384) = 16384
read(7, " HD 6550A\n\t\t1462 2246  Radeon HD"..., 16384) = 16384
brk(0xa68000)                           = 0xa68000
read(7, "95E\n\t\t17f2 5000  KI690-AM2 Mothe"..., 16384) = 16384
read(7, " CS5535 ISA bridge\n\t002d  CS5535"..., 16384) = 16384
read(7, " 2 ports\n\t13ef  Ariel ZCN/MP4\n\t1"..., 16384) = 16384
read(7, "2P] System Controller\n\t700d  AMD"..., 16384) = 16384
read(7, "  Millennium G550 LP PCIE\n\t2537 "..., 16384) = 16384
read(7, "oller\n\t\t103c 3237  E500 SAS Cont"..., 16384) = 16384
brk(0xa8a000)                           = 0xa8a000
read(7, "er\n\t\t175c 8800  ASI88xx Audio Ad"..., 16384) = 16384
read(7, "0  DS-1 Audio\n\t1000  SW1000XG [X"..., 16384) = 16384
read(7, "CI bus bridge [db21554]\n\t6340  I"..., 16384) = 16384
read(7, " 77dc  cRIO-9036\n\t\t1093 77dd  cR"..., 16384) = 16384
read(7, "8747 48-Lane, 5-Port PCI Express"..., 16384) = 16384
brk(0xaac000)                           = 0xaac000
read(7, "SB 1.1 Controller\n\t\t1014 0540  T"..., 16384) = 16384
read(7, "infast NF3250K8AA\n\t\t1462 7030  K"..., 16384) = 16384
read(7, "33f  NV35GL [Quadro FX 700]\n\t034"..., 16384) = 16384
read(7, "MCP78S [GeForce 8200] Co-Process"..., 16384) = 16384
read(7, "ce 940MX]\n\t0fc0  GK107 [GeForce "..., 16384) = 16384
read(7, "de 101b  GRID K260Q\n\t11b1  GK104"..., 16384) = 16384
brk(0xace000)                           = 0xace000
read(7, "b Fibre Channel Adapter\n\t\t1014 0"..., 16384) = 16384
read(7, " SATA-II Controller\n\t9100  INI-9"..., 16384) = 16384
read(7, "k ALC 650)\n\t\t1297 c160  FX41 mot"..., 16384) = 16384
read(7, " 6113RS/6513RS\n\t0137  GDT 6123RS"..., 16384) = 16384
read(7, "isco Systems Inc\n\t0023  VIC 81 P"..., 16384) = 16384
read(7, "s Communications\n116a  Luminex S"..., 16384) = 16384
brk(0xaf0000)                           = 0xaf0000
read(7, "\t\t11ab 3621  Marvell RDK-8036\n\t\t"..., 16384) = 16384
read(7, "uting Devices International\n11f6"..., 16384) = 16384
read(7, "reless PCI Adapter (rev E1) [ISL"..., 16384) = 16384
read(7, "CTI PCI UART 4\n\t0322  CTI PCI UA"..., 16384) = 16384
read(7, "t Copper Ethernet PCI-X BGE base"..., 16384) = 16384
brk(0xb12000)                           = 0xb12000
read(7, " ME-6000/8/DIO\n\t604f  ME-6000/16"..., 16384) = 16384
read(7, "ller\n\t50a4  T540-50A4 Unified Wi"..., 16384) = 16384
read(7, "Wire Ethernet Controller [VF]\n\t5"..., 16384) = 16384
read(7, "802.11bgn Wireless Network Adapt"..., 16384) = 16384
read(7, "40-2T 10GBase-T Network Adapter\n"..., 16384) = 16384
read(7, " combo cardbus [GC89]\n\t4350  BCM"..., 16384) = 16384
brk(0xb34000)                           = 0xb34000
read(7, "er\n\t0124  EV1000 Mouse controlle"..., 16384) = 16384
read(7, "GbE MCX4121A-XCAT\n\t\t15b3 0005  M"..., 16384) = 16384
read(7, ") Wireless cardbus adapter\n\t\t118"..., 16384) = 16384
read(7, "nfigurable Virtex-5 FPGA with pl"..., 16384) = 16384
read(7, "80  ARC-1680 8/12/16/24 Port PCI"..., 16384) = 16384
read(7, "NT40E3-4-PTP Network Adapter 4x1"..., 16384) = 16384
brk(0xb56000)                           = 0xb56000
read(7, "NC554FLB 10Gb 2-port FlexFabric "..., 16384) = 16384
read(7, "/ decoder\n\t5310  BC-H16480A 16 p"..., 16384) = 16384
read(7, "Profile SmartNIC\n\t3310  10-Giga "..., 16384) = 16384
read(7, "6ca8  PCI-DA12-8 8x 12-bit Analo"..., 16384) = 16384
read(7, "  P8 series motherboard\n\t\t8086 2"..., 16384) = 16384
brk(0xb77000)                           = 0xb77000
read(7, "ss-AC 7265\n# Stone Peak 2 AGN\n\t\t"..., 16384) = 16384
read(7, "n E5 v2/Core i7 Integrated Memor"..., 16384) = 16384
read(7, "1000 CT Network Connection\n\t1076"..., 16384) = 16384
read(7, "ernet Adapter (10/100)\n\t\t1179 00"..., 16384) = 16384
read(7, "r\n\t\t103c 22fd  Ethernet 10Gb 2-p"..., 16384) = 16384
read(7, "ller 2/SC\n\t\t1028 0467  PowerEdge"..., 16384) = 16384
read(7, "16 Chipset Family PCI Express Ro"..., 16384) = 16384
brk(0xb99000)                           = 0xb99000
read(7, "028 040a  Latitude E6410\n\t\t1028 "..., 16384) = 16384
read(7, "-7065)\n\t\t1565 3101  P4TSV Mother"..., 16384) = 16384
read(7, "34  Compaq nw8240/nx8220\n\t\t103c "..., 16384) = 16384
read(7, " R60e\n\t\t8086 544b  Desktop Board"..., 16384) = 16384
read(7, "6 5044  Desktop Board DP35DP\n\t\te"..., 16384) = 16384
read(7, "hannel 2 Rank Registers\n\t2c33  X"..., 16384) = 16384
brk(0xbbb000)                           = 0xbbb000
read(7, "n E5 v3/Core i7 DDRIO (VMSE) 0 &"..., 16384) = 16384
read(7, "X722 for 10GbE SFP+\n\t\t17aa 4020 "..., 16384) = 16384
read(7, "5/Core i7 QPI Link Reut 1\n\t3ca0 "..., 16384) = 16384
read(7, " Xeon E7 v4/Xeon E5 v4/Xeon E3 v"..., 16384) = 16384
read(7, "ntroller Hub EG20T USB OHCI Cont"..., 16384) = 16384
read(7, "roller\n\t9cc7  Wildcat Point-LP L"..., 16384) = 16384
brk(0xbdd000)                           = 0xbdd000
read(7, "ipset Family USB 3.0 xHCI Contro"..., 16384) = 16384
read(7, "ernal 12G SAS Port/PCIe 3.0\n\t028"..., 16384) = 16384
read(7, "b09  Corvid 24\n\tdb11  T-Tap\n\tdca"..., 16384) = 6067
read(7, "", 10317)                      = 0
read(7, "", 16384)                      = 0
close(7)                                = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/mem_banks/0/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "heap_type 2\nsize_in_bytes 429496"..., 4096) = 72
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/0/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487744\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/1/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487745\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/2/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487746\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/3/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487747\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/4/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487748\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/5/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487749\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/6/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487750\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/7/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487751\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/8/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487752\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/9/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487753\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/10/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487754\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/11/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487755\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/12/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487756\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/13/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487757\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/14/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487758\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/15/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487759\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/16/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487760\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/17/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487761\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/18/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487762\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/19/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487763\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/20/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487764\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/21/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487765\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/22/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487766\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/23/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487767\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/24/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487768\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/25/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487769\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/26/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487770\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/27/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487771\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/28/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487772\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/29/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487773\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/30/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487774\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/31/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487775\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/32/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487776\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/33/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487777\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/34/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487778\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/35/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487779\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/36/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487744\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/37/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487748\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/38/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487752\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/39/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487756\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/40/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487760\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/41/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487764\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/42/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487768\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/43/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487772\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/44/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487776\nleve"..., 4096) = 639
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/45/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487744\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/46/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487748\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/47/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487752\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/48/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487756\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/49/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487760\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/50/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487764\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/51/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487768\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/52/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487772\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/53/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "processor_id_low 2147487776\nleve"..., 4096) = 638
read(6, "", 4096)                       = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/io_links/0/properties", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "type 2\nversion_major 0\nversion_m"..., 4096) = 167
read(6, "", 4096)                       = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/gpu_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0\n", 4096)                    = 2
close(7)                                = 0
close(6)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/generation_id", O_RDONLY) = 6
fstat(6, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(6, "2\n", 4096)                    = 2
close(6)                                = 0
ioctl(5, AMDKFD_IOC_GET_CLOCK_COUNTERS, 0x7ffef0ae1300) = 0
ioctl(5, AMDKFD_IOC_GET_CLOCK_COUNTERS, 0x7ffef0ae1230) = 0
ioctl(5, AMDKFD_IOC_ALLOC_MEMORY_OF_GPU, 0x7ffef0ae1530) = 0
mmap(0x1008000, 32768, PROT_READ|PROT_WRITE, MAP_SHARED|MAP_FIXED, 8, 0x108c90000) = 0x1008000
ioctl(5, AMDKFD_IOC_MAP_MEMORY_TO_GPU, 0x7ffef0ae1600) = 0
ioctl(5, AMDKFD_IOC_CREATE_EVENT, 0x7ffef0ae1750) = 0
mmap(0x1001000, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x1001000
get_mempolicy(NULL, NULL, 0, NULL, 0)   = 0
madvise(0x1001000, 4096, MADV_DONTFORK) = 0
ioctl(5, AMDKFD_IOC_ALLOC_MEMORY_OF_GPU, 0x7ffef0ae14a0) = 0
ioctl(5, AMDKFD_IOC_MAP_MEMORY_TO_GPU, 0x7ffef0ae14d0) = 0
ioctl(5, AMDKFD_IOC_CREATE_EVENT, 0x7ffef0ae1610) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7f271d158000
mprotect(0x7f271d159000, 8388608, PROT_READ|PROT_WRITE) = 0
clone(child_stack=0x7f271d957fb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7f271d9589d0, tls=0x7f271d958700, child_tidptr=0x7f271d9589d0) = 10069
openat(AT_FDCWD, "/opt/rocm/lib/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 6
fstat(6, {st_mode=S_IFREG|0644, st_size=130109, ...}) = 0
mmap(NULL, 130109, PROT_READ, MAP_PRIVATE, 6, 0) = 0x7f271e7e4000
close(6)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libhsa-ext-finalize64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
munmap(0x7f271e7e4000, 130109)          = 0
openat(AT_FDCWD, "/opt/rocm/lib/libhsa-ext-image64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libhsa-ext-image64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libhsa-ext-image64.so.1", O_RDONLY|O_CLOEXEC) = 6
read(6, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\300F\0\0\0\0\0\0"..., 832) = 832
fstat(6, {st_mode=S_IFREG|0644, st_size=1342768, ...}) = 0
mmap(NULL, 3437944, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 6, 0) = 0x7f271ce10000
mprotect(0x7f271cea6000, 2093056, PROT_NONE) = 0
mmap(0x7f271d0a5000, 733184, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 6, 0x95000) = 0x7f271d0a5000
close(6)                                = 0
mprotect(0x7f271d0a5000, 8192, PROT_READ) = 0
ioctl(5, AMDKFD_IOC_SET_SCRATCH_BACKING_VA, 0x7ffef0ae16d0) = 0
mmap(0x1014000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x1014000
get_mempolicy(NULL, NULL, 0, NULL, 0)   = 0
madvise(0x1014000, 8192, MADV_DONTFORK) = 0
ioctl(5, AMDKFD_IOC_ALLOC_MEMORY_OF_GPU, 0x7ffef0ae1570) = 0
ioctl(5, AMDKFD_IOC_MAP_MEMORY_TO_GPU, 0x7ffef0ae15a0) = 0
mmap(0x1004000, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x1004000
get_mempolicy(NULL, NULL, 0, NULL, 0)   = 0
madvise(0x1004000, 4096, MADV_DONTFORK) = 0
ioctl(5, AMDKFD_IOC_ALLOC_MEMORY_OF_GPU, 0x7ffef0ae1270) = 0
ioctl(5, AMDKFD_IOC_MAP_MEMORY_TO_GPU, 0x7ffef0ae12a0) = 0
ioctl(5, AMDKFD_IOC_SET_TRAP_HANDLER, 0x7ffef0ae17c0) = 0
openat(AT_FDCWD, "/dev/random", O_WRONLY) = 6
write(6, "\270", 1)                     = 1
close(6)                                = 0
openat(AT_FDCWD, "/dev/random", O_WRONLY) = 6
write(6, "\270", 1)                     = 1
close(6)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libamd_comgr.so", O_RDONLY|O_CLOEXEC) = 6
read(6, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\340\371Y\0\0\0\0\0"..., 832) = 832
fstat(6, {st_mode=S_IFREG|0644, st_size=111587656, ...}) = 0
mmap(NULL, 97193904, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 6, 0) = 0x7f271234f000
mprotect(0x7f27179b8000, 2097152, PROT_NONE) = 0
mmap(0x7f2717bb8000, 4128768, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 6, 0x5669000) = 0x7f2717bb8000
mmap(0x7f2717fa8000, 360368, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f2717fa8000
close(6)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 6
fstat(6, {st_mode=S_IFREG|0644, st_size=130109, ...}) = 0
mmap(NULL, 130109, PROT_READ, MAP_PRIVATE, 6, 0) = 0x7f271e7e4000
close(6)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
munmap(0x7f271e7e4000, 130109)          = 0
munmap(0x7f271234f000, 97193904)        = 0
openat(AT_FDCWD, "/opt/rocm/lib/libamd_comgr.so", O_RDONLY|O_CLOEXEC) = 6
read(6, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\340\371Y\0\0\0\0\0"..., 832) = 832
fstat(6, {st_mode=S_IFREG|0644, st_size=111587656, ...}) = 0
mmap(NULL, 97193904, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 6, 0) = 0x7f271234f000
mprotect(0x7f27179b8000, 2097152, PROT_NONE) = 0
mmap(0x7f2717bb8000, 4128768, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 6, 0x5669000) = 0x7f2717bb8000
mmap(0x7f2717fa8000, 360368, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f2717fa8000
close(6)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../../../lib64/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/../hsa/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 6
fstat(6, {st_mode=S_IFREG|0644, st_size=130109, ...}) = 0
mmap(NULL, 130109, PROT_READ, MAP_PRIVATE, 6, 0) = 0x7f271e7e4000
close(6)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
munmap(0x7f271e7e4000, 130109)          = 0
munmap(0x7f271234f000, 97193904)        = 0
openat(AT_FDCWD, "./libamd_comgr.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "./libamd_comgr.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
--- SIGSEGV {si_signo=SIGSEGV, si_code=SI_KERNEL, si_addr=NULL} ---
+++ killed by SIGSEGV (core dumped) +++
```

---

### 评论 #4 — LucasCampos (2020-04-26T21:53:12Z)

My `LD_LIBRARY_PATH` is `/opt/rocm/lib:/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:/opt/rocm/hip/lib`

Which interestingly does contain the library `libamd_comgr.so`,

```
(base) ➜  lib ll /opt/rocm/lib

total 113M
drwxrwxr-x 5 root root 4,0K Apr 26 23:17 cmake
-rw-r--r-- 1 root root  54K Mär 29 01:17 hc.amdgcn.bc
-rw-r--r-- 1 root root 2,7K Mär 29 01:17 hip.amdgcn.bc
lrwxrwxrwx 1 root root   17 Mär 29 01:18 libamd_comgr.so -> libamd_comgr.so.1
lrwxrwxrwx 1 root root   25 Mär 29 01:18 libamd_comgr.so.1 -> libamd_comgr.so.1.6.30300
-rw-r--r-- 1 root root 107M Mär 29 01:18 libamd_comgr.so.1.6.30300
lrwxrwxrwx 1 root root   40 Apr 26 23:17 libclang_rt.builtins-x86_64.a -> ../hcc/lib/libclang_rt.builtins-x86_64.a
lrwxrwxrwx 1 root root   32 Apr 26 23:17 libhc_am.so -> ../hcc/lib/libhc_am.so.3.1.30300
lrwxrwxrwx 1 root root   32 Apr 26 23:17 libhc_am.so.3 -> ../hcc/lib/libhc_am.so.3.1.30300
lrwxrwxrwx 1 root root   32 Apr 26 23:17 libhc_am.so.3.1.30300 -> ../hcc/lib/libhc_am.so.3.1.30300
lrwxrwxrwx 1 root root   34 Apr 26 23:17 libhip_hcc.so -> ../hip/lib/libhip_hcc.so.3.3.30300
lrwxrwxrwx 1 root root   34 Apr 26 23:17 libhip_hcc.so.3 -> ../hip/lib/libhip_hcc.so.3.3.30300
lrwxrwxrwx 1 root root   34 Apr 26 23:17 libhip_hcc.so.3.3.30300 -> ../hip/lib/libhip_hcc.so.3.3.30300
lrwxrwxrwx 1 root root   30 Apr 26 23:17 libhip_hcc_static.a -> ../hip/lib/libhip_hcc_static.a
lrwxrwxrwx 1 root root   33 Apr 26 23:17 libhiprtc.so -> ../hip/lib/libhiprtc.so.3.3.30300
lrwxrwxrwx 1 root root   33 Apr 26 23:17 libhiprtc.so.3 -> ../hip/lib/libhiprtc.so.3.3.30300
lrwxrwxrwx 1 root root   33 Apr 26 23:17 libhiprtc.so.3.3.30300 -> ../hip/lib/libhiprtc.so.3.3.30300
lrwxrwxrwx 1 root root   32 Mär 29 01:17 libhsa-ext-image64.so -> ../hsa/lib/libhsa-ext-image64.so
lrwxrwxrwx 1 root root   14 Mär 29 01:14 libhsakmt.so -> libhsakmt.so.1
lrwxrwxrwx 1 root root   22 Mär 29 01:14 libhsakmt.so.1 -> libhsakmt.so.1.0.30300
-rw-r--r-- 1 root root 186K Mär 29 01:14 libhsakmt.so.1.0.30300
lrwxrwxrwx 1 root root   30 Mär 29 01:14 libhsa-runtime64.so -> ../hsa/lib/libhsa-runtime64.so
lrwxrwxrwx 1 root root   32 Mär 29 01:14 libhsa-runtime64.so.1 -> ../hsa/lib/libhsa-runtime64.so.1
lrwxrwxrwx 1 root root   36 Mär 29 01:17 libhsa-runtime-tools64.so -> ../hsa/lib/libhsa-runtime-tools64.so
lrwxrwxrwx 1 root root   33 Apr 26 23:17 libmcwamp.so -> ../hcc/lib/libmcwamp.so.3.1.30300
lrwxrwxrwx 1 root root   33 Apr 26 23:17 libmcwamp.so.3 -> ../hcc/lib/libmcwamp.so.3.1.30300
lrwxrwxrwx 1 root root   33 Apr 26 23:17 libmcwamp.so.3.1.30300 -> ../hcc/lib/libmcwamp.so.3.1.30300
lrwxrwxrwx 1 root root   24 Mär 29 01:48 librocm-debug-agent.so -> librocm-debug-agent.so.1
lrwxrwxrwx 1 root root   26 Mär 29 01:48 librocm-debug-agent.so.1 -> librocm-debug-agent.so.1.0
-rw-r--r-- 1 root root 2,8M Mär 29 01:48 librocm-debug-agent.so.1.0
lrwxrwxrwx 1 root root   38 Mär 29 01:48 librocprofiler64.so -> ../rocprofiler/lib/librocprofiler64.so
lrwxrwxrwx 1 root root   34 Mär 29 01:48 libroctracer64.so -> ../roctracer/lib/libroctracer64.so
lrwxrwxrwx 1 root root   36 Mär 29 01:48 libroctracer64.so.1 -> ../roctracer/lib/libroctracer64.so.1
lrwxrwxrwx 1 root root   44 Mär 29 01:48 libroctracer64.so.1.0.30300 -> ../roctracer/lib/libroctracer64.so.1.0.30300
lrwxrwxrwx 1 root root   30 Mär 29 01:48 libroctx64.so -> ../roctracer/lib/libroctx64.so
lrwxrwxrwx 1 root root   32 Mär 29 01:48 libroctx64.so.1 -> ../roctracer/lib/libroctx64.so.1
lrwxrwxrwx 1 root root   40 Mär 29 01:48 libroctx64.so.1.0.30300 -> ../roctracer/lib/libroctx64.so.1.0.30300
-rw-r--r-- 1 root root 179K Mär 29 01:17 ockl.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_correctly_rounded_sqrt_off.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_correctly_rounded_sqrt_on.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_daz_opt_off.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_daz_opt_on.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_finite_only_off.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_finite_only_on.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_1010.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_1011.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_1012.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_700.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_701.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_702.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_801.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_802.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_803.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_810.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_900.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_902.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_904.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_906.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_isa_version_908.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_unsafe_math_off.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_unsafe_math_on.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_wavefrontsize64_off.amdgcn.bc
-rw-r--r-- 1 root root 1,9K Mär 29 01:17 oclc_wavefrontsize64_on.amdgcn.bc
-rw-r--r-- 1 root root 219K Mär 29 01:17 ocml.amdgcn.bc
-rw-r--r-- 1 root root 2,8M Mär 29 01:17 opencl.amdgcn.bc
```

---

### 评论 #5 — LucasCampos (2020-04-26T22:10:25Z)

I think I have found the solution. There are two issues.  First, `rocm` does not install a dependency, `libtinfo5`. Second, there is the mistake in the path of `libamd_comgr.so`.

**TL;DR**

Thus, one needs to install the missing library as

```
sudo apt install libtinfo5
```

Second, one needs to run the `clinfo` in the folder `/opt/rocm/lib`

** Long version **

In the line `openat(AT_FDCWD, "./libamd_comgr.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)`, it seems like the library in being searched only on the current folder. Thus, it is needed to run the OpenCL application when one's terminal is `/opt/rocm/lib`.

After that, I tried again to run, with the following shorted `strace` (full version attached)

```
close(6)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.3.0/lib/./libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/lib/./../lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/lib/./../../../lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/lib/./../../../lib64/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm-3.3.0/lib/./../hsa/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/opencl/lib/x86_64/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hip/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 6
fstat(6, {st_mode=S_IFREG|0644, st_size=130109, ...}) = 0
mmap(NULL, 130109, PROT_READ, MAP_PRIVATE, 6, 0) = 0x7fd9fc56a000
close(6)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libtinfo.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
munmap(0x7fd9fc56a000, 130109)          = 0
munmap(0x7fd9ee34f000, 97193904)        = 0
--- SIGSEGV {si_signo=SIGSEGV, si_code=SI_KERNEL, si_addr=NULL} ---
+++ killed by SIGSEGV (core dumped) +++
```

Thus, one needs to install the missing library oneself. Once it was installed, it was possible to run the `clinfo` application, with output 

```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3098.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
  Device Topology:				 PCI[ B#6, D#0, F#0 ]
  Max compute units:				 36
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
  Max clock frequency:				 1360Mhz
  Address bits:					 64
  Max memory allocation:			 3650722201
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26591
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 4294967296
  Constant buffer size:				 3650722201
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 3650722201
  Max global variable size:			 3650722201
  Max global variable preferred total size:	 4294967296
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
  Platform ID:					 0x7f00830eed30
  Name:						 gfx803
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3098.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```
[clinfo_missinglibrary.txt](https://github.com/RadeonOpenCompute/ROCm/files/4536572/clinfo_missinglibrary.txt)



---

### 评论 #6 — LucasCampos (2020-04-26T22:16:54Z)

Using these workarounds, it was possible to make Blender detect the OpenCL driver. I ran Blender with 

```
(base) ➜  lib pwd
/opt/rocm/lib
(base) ➜  lib ~/Downloads/blender-2.82a-linux64/blender
```

and both my CPU and GPU were shown in Blender

![Screenshot from 2020-04-27 00-15-35](https://user-images.githubusercontent.com/2735358/80321315-5da86400-881c-11ea-99e8-637285678b7a.png)

A similar procedure can be done to use the Blender Benchmark

![Screenshot from 2020-04-27 00-18-46](https://user-images.githubusercontent.com/2735358/80321353-bbd54700-881c-11ea-9dfa-9bc2ef0cff9a.png)


---

### 评论 #7 — pjones8404lml (2020-04-27T14:20:23Z)

JC

> You could try:
> strace -f clinfo 2>strace.txt
> and then post the strace.txt file.
> It might give some indication on where it is failing.

JC, when running it, I get :Number of platforms                               0


---

### 评论 #8 — jcdutton (2020-04-27T16:49:53Z)

PJ, please attach the strace.txt file.


---

### 评论 #9 — ableeker (2020-04-27T17:59:37Z)

@LucasCampos, I've used strace to find out why clinfo segfaults, and I've come to the same conclusion, libncurses5 is missing. And as a matter of fact clinfo will run if it's installed.
However, I've had no problems running clinfo from its home /opt/rocm/opencl/bin/x86_64, or from any path, for instance ~, after adding its path, and the path /opt/rocm/bin for rocminfo. As  a matter of fact, I don't see the line you quoted in the trace file, but I do see the following line:

`openat(AT_FDCWD, "/opt/rocm-3.3.0/opencl/lib/x86_64/../../../lib/libamd_comgr.so", O_RDONLY|O_CLOEXEC) = 6`

Granted, it had to look in 5 other opt/rocm-3.3.0/opencl/lib/x86_64 locations, but it got there in the end. Then again, I've added location /opt/rocm/opencl/lib/x86_64 to /etc/ld.so.conf.d with ldconfig because Folding At Home couldn't find libOpenCL.so, and this may have allowed clinfo to find the libs it needs. Still, for me at least, just installing libncurses5 allowed me to run clinfo without errors.

Anyway, since ROCm 2.10 for me Blender recognises the RX Vega 64 as an OpenCL render device. It even started to compile the kernels, but it then aborted with an error about a split kernel, or something. Actually 3.3 (and possibly 3.1) does compile the kernels without errors, and will render the image, but it's NOT faster than the CPU render. Either GPU rendering takes exactly the same time as the CPU render, and may do nothing at all, or it may even be something like 10x slower! For example, a simple scene with a mirror ball renders in 1 minute and a half with just the CPU, but takes 1 minute per tile rendering on the GPU, and there are 128 of them. Still GPU rendering has started to work in Blender, so who knows, the issue may be fixed in ROCm 3.4.

---

### 评论 #10 — pjones8404lml (2020-04-27T23:52:41Z)

> PJ, please attach the strace.txt file.
execve("/usr/bin/clinfo", ["clinfo"], 0x7ffccc6ed938 /* 65 vars */) = 0
brk(NULL)                               = 0x565385835000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=176875, ...}) = 0
mmap(NULL, 176875, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f6d531cf000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libOpenCL.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\200A\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=43072, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f6d531cd000
mmap(NULL, 2138192, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f6d52dc9000
mprotect(0x7f6d52dd2000, 2097152, PROT_NONE) = 0
mmap(0x7f6d52fd2000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x9000) = 0x7f6d52fd2000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\16\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=14560, ...}) = 0
mmap(NULL, 2109712, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f6d52bc5000
mprotect(0x7f6d52bc8000, 2093056, PROT_NONE) = 0
mmap(0x7f6d52dc7000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x7f6d52dc7000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\260\34\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=2030544, ...}) = 0
mmap(NULL, 4131552, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f6d527d4000
mprotect(0x7f6d529bb000, 2097152, PROT_NONE) = 0
mmap(0x7f6d52bbb000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1e7000) = 0x7f6d52bbb000
mmap(0x7f6d52bc1000, 15072, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f6d52bc1000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f6d531ca000
arch_prctl(ARCH_SET_FS, 0x7f6d531ca740) = 0
mprotect(0x7f6d52bbb000, 16384, PROT_READ) = 0
mprotect(0x7f6d52dc7000, 4096, PROT_READ) = 0
mprotect(0x7f6d52fd2000, 4096, PROT_READ) = 0
mprotect(0x5653852a4000, 4096, PROT_READ) = 0
mprotect(0x7f6d531fb000, 4096, PROT_READ) = 0
munmap(0x7f6d531cf000, 176875)          = 0
brk(NULL)                               = 0x565385835000
brk(0x565385856000)                     = 0x565385856000
openat(AT_FDCWD, "/etc/OpenCL/vendors", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents(3, /* 2 entries */, 32768)     = 48
getdents(3, /* 0 entries */, 32768)     = 0
lseek(3, 0, SEEK_SET)                   = 0
close(3)                                = 0
fstat(1, {st_mode=S_IFCHR|0600, st_rdev=makedev(136, 2), ...}) = 0
write(1, "Number of platforms             "..., 52) = 52
exit_group(0)                           = ?
+++ exited with 0 +++



---

### 评论 #11 — jcdutton (2020-04-28T07:41:32Z)

PJ, What is in the folder:
/etc/OpenCL/vendors
Also, what is the contents of each file in there.  
They should be short text files.

---

### 评论 #12 — pjones8404lml (2020-04-28T11:18:53Z)

/etc/OpenCL/vendors is blank, with no text files.

I think we have found it......

---

### 评论 #13 — jcdutton (2020-04-28T12:30:24Z)

I have a vega56. So the file I have there is:
amdocl64.icd
That contains:
/opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so

That is provided by package:
rocm-opencl

I don't know what would work for your GPU. 

---

### 评论 #14 — pjones8404lml (2020-04-28T13:03:48Z)

I have an RX580... should be easy to find.  Thank you!

---

### 评论 #15 — pjones8404lml (2020-04-28T13:05:20Z)

https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime


---

### 评论 #16 — alejandromunozes (2020-04-30T20:12:00Z)

> You could try:
> strace -f clinfo 2>strace.txt
> and then post the strace.txt file.
> It might give some indication on where it is failing.

Here is my strace.txt:

[strace.txt](https://github.com/RadeonOpenCompute/ROCm/files/4560930/strace.txt)




---

### 评论 #17 — alejandromunozes (2020-04-30T20:16:49Z)

I've just installed _libtinfo5_ as suggested by @LucasCampos and it seems to work (at least, LibreOffice Calc doesn't crash if I enable Opencl), but with only one platform (my GPU). This is the output of clinfo now:

```
$ clinfo 
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3098.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Vega 20 [Radeon VII]
  Device Topology:                               PCI[ B#47, D#0, F#0 ]
  Max compute units:                             60
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           1802Mhz
  Address bits:                                  64
  Max memory allocation:                         14588628172
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26287
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            17163091968
  Constant buffer size:                          14588628172
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          1703726284
  Max global variable size:                      14588628172
  Max global variable preferred total size:      17163091968
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:                              
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:                                
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:                              
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:                            
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7f16fc486d30
  Name:                                          gfx906+sram-ecc
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0 
  Driver version:                                3098.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0 
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```


And Darktable seems to work too. This is the output of darktable-cltest:

```console
$ darktable-cltest 
[defaults] found a 64-bit system with 32901840 kb ram and 16 cores (0 atom based)
[defaults] setting very high quality defaults

(process:15768): GLib-CRITICAL **: 22:32:30.953: g_variant_unref: assertion 'value != NULL' failed
0.046361 [opencl_init] opencl related configuration options:
0.046367 [opencl_init] 
0.046369 [opencl_init] opencl: 1
0.046371 [opencl_init] opencl_scheduling_profile: 'default'
0.046373 [opencl_init] opencl_library: ''
0.046375 [opencl_init] opencl_memory_requirement: 768
0.046377 [opencl_init] opencl_memory_headroom: 400
0.046378 [opencl_init] opencl_device_priority: '*/!0,*/*/*/!0,*'
0.046380 [opencl_init] opencl_mandatory_timeout: 200
0.046381 [opencl_init] opencl_size_roundup: 16
0.046384 [opencl_init] opencl_async_pixelpipe: 0
0.046386 [opencl_init] opencl_synch_cache: active module
0.046387 [opencl_init] opencl_number_event_handles: 25
0.046389 [opencl_init] opencl_micro_nap: 1000
0.046392 [opencl_init] opencl_use_pinned_memory: 0
0.046393 [opencl_init] opencl_use_cpu_devices: 0
0.046394 [opencl_init] opencl_avoid_atomics: 0
0.046396 [opencl_init] 
0.046486 [opencl_init] could not find opencl runtime library 'libOpenCL'
0.046507 [opencl_init] could not find opencl runtime library 'libOpenCL.so'
0.046572 [opencl_init] found opencl runtime library 'libOpenCL.so.1'
0.046586 [opencl_init] opencl library 'libOpenCL.so.1' found on your system and loaded
0.085919 [opencl_init] found 1 platform
0.085931 [opencl_init] found 1 device
0.085953 [opencl_init] device 0 `gfx906+sram-ecc' supports image sizes of 16384 x 16384
0.085956 [opencl_init] device 0 `gfx906+sram-ecc' allows GPU memory allocations of up to 13912MB
[opencl_init] device 0: gfx906+sram-ecc 
     GLOBAL_MEM_SIZE:          16368MB
     MAX_WORK_GROUP_SIZE:      256
     MAX_WORK_ITEM_DIMENSIONS: 3
     MAX_WORK_ITEM_SIZES:      [ 1024 1024 1024 ]
     DRIVER_VERSION:           3098.0 (HSA1.1,LC)
     DEVICE_VERSION:           OpenCL 2.0 
0.295557 [opencl_init] options for OpenCL compiler: -w  -DAMD=1 -I"/usr/share/darktable/kernels"
0.298818 [opencl_init] compiling program `demosaic_ppg.cl' ..
0.299114 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/demosaic_ppg.cl.bin'!
0.299124 [opencl_load_program] could not load cached binary program, trying to compile source
0.299137 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/demosaic_ppg.cl' MD5: '10a8fea5c7704c826d007f6d09807a2c'
0.619217 [opencl_build_program] successfully built program
0.619228 [opencl_build_program] BUILD STATUS: 0
0.619229 BUILD LOG:
0.619230 
0.619231 [opencl_build_program] saving binary
0.619287 [opencl_init] compiling program `atrous.cl' ..
0.622010 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/atrous.cl.bin'!
0.622016 [opencl_load_program] could not load cached binary program, trying to compile source
0.622021 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/atrous.cl' MD5: '8383c2a4e32023d51ec5a8b36494ecda'
0.722238 [opencl_build_program] successfully built program
0.722250 [opencl_build_program] BUILD STATUS: 0
0.722251 BUILD LOG:
0.722252 
0.722253 [opencl_build_program] saving binary
0.722298 [opencl_init] compiling program `basic.cl' ..
0.725154 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/basic.cl.bin'!
0.725157 [opencl_load_program] could not load cached binary program, trying to compile source
0.725165 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/basic.cl' MD5: 'd5a1008ff4a6b9bd4575155c1c8a034f'
1.645953 [opencl_build_program] successfully built program
1.645967 [opencl_build_program] BUILD STATUS: 0
1.645970 BUILD LOG:
1.645971 
1.645973 [opencl_build_program] saving binary
1.646149 [opencl_init] compiling program `blendop.cl' ..
1.646516 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/blendop.cl.bin'!
1.646522 [opencl_load_program] could not load cached binary program, trying to compile source
1.646533 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/blendop.cl' MD5: 'b5985b30dbc12abbb9e35beea0a0bc51'
2.513502 [opencl_build_program] successfully built program
2.513516 [opencl_build_program] BUILD STATUS: 0
2.513518 BUILD LOG:
2.513519 
2.513520 [opencl_build_program] saving binary
2.513622 [opencl_init] compiling program `highpass.cl' ..
2.513819 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/highpass.cl.bin'!
2.513824 [opencl_load_program] could not load cached binary program, trying to compile source
2.513829 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/highpass.cl' MD5: '95a89098bcb11eaa854a3edba36055d7'
2.637943 [opencl_build_program] successfully built program
2.637954 [opencl_build_program] BUILD STATUS: 0
2.637956 BUILD LOG:
2.637956 
2.637957 [opencl_build_program] saving binary
2.638003 [opencl_init] compiling program `nlmeans.cl' ..
2.640818 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/nlmeans.cl.bin'!
2.640823 [opencl_load_program] could not load cached binary program, trying to compile source
2.640827 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/nlmeans.cl' MD5: '3100ba35cdf14246f737f40538e87a7a'
2.786096 [opencl_build_program] successfully built program
2.786107 [opencl_build_program] BUILD STATUS: 0
2.786108 BUILD LOG:
2.786109 
2.786110 [opencl_build_program] saving binary
2.786157 [opencl_init] compiling program `gaussian.cl' ..
2.788896 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/gaussian.cl.bin'!
2.788901 [opencl_load_program] could not load cached binary program, trying to compile source
2.788906 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/gaussian.cl' MD5: '5cbefacb6bd66dac20d130b64b347116'
2.944692 [opencl_build_program] successfully built program
2.944703 [opencl_build_program] BUILD STATUS: 0
2.944704 BUILD LOG:
2.944705 
2.944706 [opencl_build_program] saving binary
2.944754 [opencl_init] compiling program `sharpen.cl' ..
2.947449 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/sharpen.cl.bin'!
2.947454 [opencl_load_program] could not load cached binary program, trying to compile source
2.947458 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/sharpen.cl' MD5: '44584e6a2e5bed7d8bd6126c73537821'
3.065084 [opencl_build_program] successfully built program
3.065094 [opencl_build_program] BUILD STATUS: 0
3.065096 BUILD LOG:
3.065097 
3.065098 [opencl_build_program] saving binary
3.065142 [opencl_init] compiling program `extended.cl' ..
3.067996 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/extended.cl.bin'!
3.068000 [opencl_load_program] could not load cached binary program, trying to compile source
3.068008 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/extended.cl' MD5: '691ac71164a647305cfb27debf57f7fb'
3.471104 [opencl_build_program] successfully built program
3.471115 [opencl_build_program] BUILD STATUS: 0
3.471116 BUILD LOG:
3.471117 
3.471118 [opencl_build_program] saving binary
3.471179 [opencl_init] compiling program `soften.cl' ..
3.474015 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/soften.cl.bin'!
3.474020 [opencl_load_program] could not load cached binary program, trying to compile source
3.474026 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/soften.cl' MD5: 'b1094d6a7775423944af19c52e9555a2'
3.607800 [opencl_build_program] successfully built program
3.607811 [opencl_build_program] BUILD STATUS: 0
3.607812 BUILD LOG:
3.607813 
3.607814 [opencl_build_program] saving binary
3.607859 [opencl_init] compiling program `bilateral.cl' ..
3.610593 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/bilateral.cl.bin'!
3.610598 [opencl_load_program] could not load cached binary program, trying to compile source
3.610603 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/bilateral.cl' MD5: '8be21347b10793c85d0aafb2e711d05e'
3.789560 [opencl_build_program] successfully built program
3.789571 [opencl_build_program] BUILD STATUS: 0
3.789572 BUILD LOG:
3.789573 
3.789574 [opencl_build_program] saving binary
3.789620 [opencl_init] compiling program `denoiseprofile.cl' ..
3.792480 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/denoiseprofile.cl.bin'!
3.792485 [opencl_load_program] could not load cached binary program, trying to compile source
3.792491 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/denoiseprofile.cl' MD5: 'fe546b041e2ec1cf714ed2a75ab079d7'
4.044966 [opencl_build_program] successfully built program
4.044976 [opencl_build_program] BUILD STATUS: 0
4.044977 BUILD LOG:
4.044979 
4.044980 [opencl_build_program] saving binary
4.045036 [opencl_init] compiling program `bloom.cl' ..
4.047781 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/bloom.cl.bin'!
4.047785 [opencl_load_program] could not load cached binary program, trying to compile source
4.047790 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/bloom.cl' MD5: '60d42224f8b44343b0adb8636377ddba'
4.167349 [opencl_build_program] successfully built program
4.167360 [opencl_build_program] BUILD STATUS: 0
4.167361 BUILD LOG:
4.167362 
4.167363 [opencl_build_program] saving binary
4.167410 [opencl_init] compiling program `colorreconstruction.cl' ..
4.170203 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/colorreconstruction.cl.bin'!
4.170207 [opencl_load_program] could not load cached binary program, trying to compile source
4.170213 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/colorreconstruction.cl' MD5: 'a08c27f60a410bbc0508b73a5dddf1c4'
4.322068 [opencl_build_program] successfully built program
4.322079 [opencl_build_program] BUILD STATUS: 0
4.322080 BUILD LOG:
4.322081 
4.322083 [opencl_build_program] saving binary
4.322129 [opencl_init] compiling program `demosaic_other.cl' ..
4.324944 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/demosaic_other.cl.bin'!
4.324950 [opencl_load_program] could not load cached binary program, trying to compile source
4.324955 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/demosaic_other.cl' MD5: '98d8ee519726556580f09d97d132b783'
4.418180 [opencl_build_program] successfully built program
4.418192 [opencl_build_program] BUILD STATUS: 0
4.418193 BUILD LOG:
4.418194 
4.418195 [opencl_build_program] saving binary
4.418240 [opencl_init] compiling program `demosaic_vng.cl' ..
4.420994 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/demosaic_vng.cl.bin'!
4.420999 [opencl_load_program] could not load cached binary program, trying to compile source
4.421004 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/demosaic_vng.cl' MD5: '30ed852ae7756ec1bc6ef75ec675dc20'
4.693701 [opencl_build_program] successfully built program
4.693711 [opencl_build_program] BUILD STATUS: 0
4.693713 BUILD LOG:
4.693714 
4.693715 [opencl_build_program] saving binary
4.693764 [opencl_init] compiling program `demosaic_markesteijn.cl' ..
4.696614 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/demosaic_markesteijn.cl.bin'!
4.696619 [opencl_load_program] could not load cached binary program, trying to compile source
4.696626 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/demosaic_markesteijn.cl' MD5: 'a99fb0ebbce59afe5445933bf9144c97'
5.060671 [opencl_build_program] successfully built program
5.060682 [opencl_build_program] BUILD STATUS: 0
5.060683 BUILD LOG:
5.060684 
5.060685 [opencl_build_program] saving binary
5.060744 [opencl_init] compiling program `liquify.cl' ..
5.063474 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/liquify.cl.bin'!
5.063479 [opencl_load_program] could not load cached binary program, trying to compile source
5.063484 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/liquify.cl' MD5: 'a2839d28a40f7967c1c3938d35bbe15d'
5.165349 [opencl_build_program] successfully built program
5.165361 [opencl_build_program] BUILD STATUS: 0
5.165362 BUILD LOG:
5.165363 
5.165364 [opencl_build_program] saving binary
5.165414 [opencl_init] compiling program `basecurve.cl' ..
5.168131 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/basecurve.cl.bin'!
5.168136 [opencl_load_program] could not load cached binary program, trying to compile source
5.168140 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/basecurve.cl' MD5: 'd44378e96a37ee048226bfe5ad34b10c'
5.349749 [opencl_build_program] successfully built program
5.349759 [opencl_build_program] BUILD STATUS: 0
5.349761 BUILD LOG:
5.349762 
5.349763 [opencl_build_program] saving binary
5.349815 [opencl_init] compiling program `locallaplacian.cl' ..
5.350012 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/locallaplacian.cl.bin'!
5.350016 [opencl_load_program] could not load cached binary program, trying to compile source
5.350020 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/locallaplacian.cl' MD5: '24cb31cf231389159947d679d2b5e103'
5.631139 [opencl_build_program] successfully built program
5.631150 [opencl_build_program] BUILD STATUS: 0
5.631151 BUILD LOG:
5.631152 
5.631153 [opencl_build_program] saving binary
5.631203 [opencl_init] compiling program `dwt.cl' ..
5.633922 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/dwt.cl.bin'!
5.633927 [opencl_load_program] could not load cached binary program, trying to compile source
5.633932 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/dwt.cl' MD5: 'caf24bee4dfd472eaf23d6457cf2f27b'
5.738553 [opencl_build_program] successfully built program
5.738564 [opencl_build_program] BUILD STATUS: 0
5.738565 BUILD LOG:
5.738566 
5.738567 [opencl_build_program] saving binary
5.738614 [opencl_init] compiling program `retouch.cl' ..
5.741283 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/retouch.cl.bin'!
5.741287 [opencl_load_program] could not load cached binary program, trying to compile source
5.741292 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/retouch.cl' MD5: 'fd32296209457073c870dbf4d085f490'
5.880937 [opencl_build_program] successfully built program
5.880948 [opencl_build_program] BUILD STATUS: 0
5.880950 BUILD LOG:
5.880950 
5.880951 [opencl_build_program] saving binary
5.881002 [opencl_init] compiling program `filmic.cl' ..
5.883769 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/filmic.cl.bin'!
5.883774 [opencl_load_program] could not load cached binary program, trying to compile source
5.883779 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/filmic.cl' MD5: '7e574589434ae2517298f688ee597d3d'
6.885780 [opencl_build_program] successfully built program
6.885791 [opencl_build_program] BUILD STATUS: 0
6.885792 BUILD LOG:
6.885793 
6.885794 [opencl_build_program] saving binary
6.885892 [opencl_init] compiling program `colorspaces.cl' ..
6.885912 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/colorspaces.cl.bin'!
6.885915 [opencl_load_program] could not load cached binary program, trying to compile source
6.885919 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/colorspaces.cl' MD5: '948de61059c84d0e1c6b3d019bc25b12'
7.029230 [opencl_build_program] successfully built program
7.029239 [opencl_build_program] BUILD STATUS: 0
7.029240 BUILD LOG:
7.029241 
7.029242 [opencl_build_program] saving binary
7.029287 [opencl_init] compiling program `basicadj.cl' ..
7.036682 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/basicadj.cl.bin'!
7.036687 [opencl_load_program] could not load cached binary program, trying to compile source
7.036692 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/basicadj.cl' MD5: '4733e10bc379a46d73bce6d619956675'
7.183369 [opencl_build_program] successfully built program
7.183379 [opencl_build_program] BUILD STATUS: 0
7.183381 BUILD LOG:
7.183381 
7.183382 [opencl_build_program] saving binary
7.183427 [opencl_init] compiling program `rgbcurve.cl' ..
7.186173 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/rgbcurve.cl.bin'!
7.186178 [opencl_load_program] could not load cached binary program, trying to compile source
7.186183 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/rgbcurve.cl' MD5: '7fc4c3a39987adb4146393c07041c293'
7.301284 [opencl_build_program] successfully built program
7.301295 [opencl_build_program] BUILD STATUS: 0
7.301296 BUILD LOG:
7.301297 
7.301298 [opencl_build_program] saving binary
7.301341 [opencl_init] compiling program `guided_filter.cl' ..
7.304246 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/guided_filter.cl.bin'!
7.304251 [opencl_load_program] could not load cached binary program, trying to compile source
7.304258 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/guided_filter.cl' MD5: 'd26b92b15b6d99a48125bdd456632990'
7.470527 [opencl_build_program] successfully built program
7.470538 [opencl_build_program] BUILD STATUS: 0
7.470539 BUILD LOG:
7.470540 
7.470541 [opencl_build_program] saving binary
7.470591 [opencl_init] compiling program `hazeremoval.cl' ..
7.473193 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/hazeremoval.cl.bin'!
7.473198 [opencl_load_program] could not load cached binary program, trying to compile source
7.473203 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/hazeremoval.cl' MD5: '1c322b04c16fbf9fdacf71483f557705'
7.614960 [opencl_build_program] successfully built program
7.614970 [opencl_build_program] BUILD STATUS: 0
7.614971 BUILD LOG:
7.614972 
7.614973 [opencl_build_program] saving binary
7.615020 [opencl_init] compiling program `lut3d.cl' ..
7.617843 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/lut3d.cl.bin'!
7.617848 [opencl_load_program] could not load cached binary program, trying to compile source
7.617853 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/lut3d.cl' MD5: '6f990a69a49c20c284e167cdd9e29214'
7.785385 [opencl_build_program] successfully built program
7.785396 [opencl_build_program] BUILD STATUS: 0
7.785397 BUILD LOG:
7.785398 
7.785399 [opencl_build_program] saving binary
7.785447 [opencl_init] compiling program `rgblevels.cl' ..
7.788170 [opencl_fopen_stat] could not open file `/home/alejandro/.cache/darktable/cached_kernels_for_gfx906sramecc_30980HSA11LC/rgblevels.cl.bin'!
7.788174 [opencl_load_program] could not load cached binary program, trying to compile source
7.788181 [opencl_load_program] successfully loaded program from '/usr/share/darktable/kernels/rgblevels.cl' MD5: 'be8fd33f37d46e11ce5597c64e512903'
7.901832 [opencl_build_program] successfully built program
7.901843 [opencl_build_program] BUILD STATUS: 0
7.901844 BUILD LOG:
7.901845 
7.901846 [opencl_build_program] saving binary
7.901885 [opencl_init] kernel loading time: 7.6032 
7.901891 [opencl_init] OpenCL successfully initialized.
7.901892 [opencl_init] here are the internal numbers and names of OpenCL devices available to darktable:
7.901895 [opencl_init]          0       'gfx906+sram-ecc'
7.901896 [opencl_init] FINALLY: opencl is AVAILABLE on this system.
7.901899 [opencl_init] initial status of opencl enabled flag is ON.
7.904722 [opencl_create_kernel] successfully loaded kernel `blendop_mask_Lab' (0) for device 0
7.904725 [opencl_create_kernel] successfully loaded kernel `blendop_mask_RAW' (1) for device 0
7.904727 [opencl_create_kernel] successfully loaded kernel `blendop_mask_rgb' (2) for device 0
7.904729 [opencl_create_kernel] successfully loaded kernel `blendop_Lab' (3) for device 0
7.904731 [opencl_create_kernel] successfully loaded kernel `blendop_RAW' (4) for device 0
7.904733 [opencl_create_kernel] successfully loaded kernel `blendop_rgb' (5) for device 0
7.904738 [opencl_create_kernel] successfully loaded kernel `blendop_mask_tone_curve' (6) for device 0
7.904740 [opencl_create_kernel] successfully loaded kernel `blendop_set_mask' (7) for device 0
7.904743 [opencl_create_kernel] successfully loaded kernel `blendop_display_channel' (8) for device 0
7.904753 [opencl_create_kernel] successfully loaded kernel `zero' (9) for device 0
7.904756 [opencl_create_kernel] successfully loaded kernel `splat' (10) for device 0
7.904757 [opencl_create_kernel] successfully loaded kernel `blur_line' (11) for device 0
7.904759 [opencl_create_kernel] successfully loaded kernel `blur_line_z' (12) for device 0
7.904761 [opencl_create_kernel] successfully loaded kernel `slice' (13) for device 0
7.904763 [opencl_create_kernel] successfully loaded kernel `slice_to_output' (14) for device 0
7.904767 [opencl_create_kernel] successfully loaded kernel `gaussian_column_1c' (15) for device 0
7.904771 [opencl_create_kernel] successfully loaded kernel `gaussian_transpose_1c' (16) for device 0
7.904773 [opencl_create_kernel] successfully loaded kernel `gaussian_column_4c' (17) for device 0
7.904777 [opencl_create_kernel] successfully loaded kernel `gaussian_transpose_4c' (18) for device 0
7.904782 [opencl_create_kernel] successfully loaded kernel `interpolation_resample' (19) for device 0
7.904789 [opencl_create_kernel] successfully loaded kernel `pad_input' (20) for device 0
7.904792 [opencl_create_kernel] successfully loaded kernel `gauss_expand' (21) for device 0
7.904794 [opencl_create_kernel] successfully loaded kernel `gauss_reduce' (22) for device 0
7.904796 [opencl_create_kernel] successfully loaded kernel `laplacian_assemble' (23) for device 0
7.904799 [opencl_create_kernel] successfully loaded kernel `process_curve' (24) for device 0
7.904802 [opencl_create_kernel] successfully loaded kernel `write_back' (25) for device 0
7.904805 [opencl_create_kernel] successfully loaded kernel `dwt_add_img_to_layer' (26) for device 0
7.904808 [opencl_create_kernel] successfully loaded kernel `dwt_subtract_layer' (27) for device 0
7.904812 [opencl_create_kernel] successfully loaded kernel `dwt_hat_transform_col' (28) for device 0
7.904814 [opencl_create_kernel] successfully loaded kernel `dwt_hat_transform_row' (29) for device 0
7.904816 [opencl_create_kernel] successfully loaded kernel `dwt_init_buffer' (30) for device 0
7.904822 [opencl_create_kernel] successfully loaded kernel `colorspaces_transform_lab_to_rgb_matrix' (31) for device 0
7.904825 [opencl_create_kernel] successfully loaded kernel `colorspaces_transform_rgb_matrix_to_lab' (32) for device 0
7.904829 [opencl_create_kernel] successfully loaded kernel `colorspaces_transform_rgb_matrix_to_rgb' (33) for device 0
7.904832 [opencl_create_kernel] successfully loaded kernel `guided_filter_split_rgb_image' (34) for device 0
7.904835 [opencl_create_kernel] successfully loaded kernel `guided_filter_box_mean_x' (35) for device 0
7.904839 [opencl_create_kernel] successfully loaded kernel `guided_filter_box_mean_y' (36) for device 0
7.904841 [opencl_create_kernel] successfully loaded kernel `guided_filter_covariances' (37) for device 0
7.904844 [opencl_create_kernel] successfully loaded kernel `guided_filter_variances' (38) for device 0
7.904847 [opencl_create_kernel] successfully loaded kernel `guided_filter_update_covariance' (39) for device 0
7.904850 [opencl_create_kernel] successfully loaded kernel `guided_filter_solve' (40) for device 0
7.904852 [opencl_create_kernel] successfully loaded kernel `guided_filter_generate_result' (41) for device 0
8.088214 [opencl_init] benchmarking results: 0.028021 seconds for fastest GPU versus 0.050963 seconds for CPU.
8.088232 [opencl_init] set scheduling profile to default.
8.088258 [opencl_priorities] these are your device priorities:
8.088261 [opencl_priorities]            image   preview export  thumbs  preview2
8.088269 [opencl_priorities]            0       -1      0       0       -1
8.088274 [opencl_priorities] show if opencl use is mandatory for a given pixelpipe:
8.088277 [opencl_priorities]            image   preview export  thumbs  preview2
8.088283 [opencl_priorities]            0       0       0       0       0
8.088289 [opencl_synchronization_timeout] synchronization timeout set to 200
8,156896 [opencl_create_kernel] successfully loaded kernel `colorcontrast' (42) for device 0
8,159725 [opencl_create_kernel] successfully loaded kernel `filmic' (43) for device 0
8,161519 [opencl_create_kernel] successfully loaded kernel `colisa' (44) for device 0
8,163228 [opencl_create_kernel] successfully loaded kernel `colorize' (45) for device 0
8,164802 [opencl_create_kernel] successfully loaded kernel `retouch_clear_alpha' (46) for device 0
8,164810 [opencl_create_kernel] successfully loaded kernel `retouch_copy_alpha' (47) for device 0
8,164815 [opencl_create_kernel] successfully loaded kernel `retouch_copy_buffer_to_buffer' (48) for device 0
8,164819 [opencl_create_kernel] successfully loaded kernel `retouch_copy_buffer_to_image' (49) for device 0
8,164823 [opencl_create_kernel] successfully loaded kernel `retouch_fill' (50) for device 0
8,164826 [opencl_create_kernel] successfully loaded kernel `retouch_copy_image_to_buffer_masked' (51) for device 0
8,164830 [opencl_create_kernel] successfully loaded kernel `retouch_copy_buffer_to_buffer_masked' (52) for device 0
8,164833 [opencl_create_kernel] successfully loaded kernel `retouch_image_rgb2lab' (53) for device 0
8,164837 [opencl_create_kernel] successfully loaded kernel `retouch_image_lab2rgb' (54) for device 0
8,164840 [opencl_create_kernel] successfully loaded kernel `retouch_copy_mask_to_alpha' (55) for device 0
8,167329 [opencl_create_kernel] successfully loaded kernel `profilegamma' (56) for device 0
8,167336 [opencl_create_kernel] successfully loaded kernel `profilegamma_log' (57) for device 0
8,168674 [opencl_create_kernel] successfully loaded kernel `vibrance' (58) for device 0
8,169934 [opencl_create_kernel] successfully loaded kernel `tonecurve' (59) for device 0
8,172030 [opencl_create_kernel] successfully loaded kernel `clip_rotate_bilinear' (60) for device 0
8,172034 [opencl_create_kernel] successfully loaded kernel `clip_rotate_bicubic' (61) for device 0
8,172036 [opencl_create_kernel] successfully loaded kernel `clip_rotate_lanczos2' (62) for device 0
8,172038 [opencl_create_kernel] successfully loaded kernel `clip_rotate_lanczos3' (63) for device 0
8,172792 [opencl_create_kernel] successfully loaded kernel `relight' (64) for device 0
8,173905 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_precondition' (65) for device 0
8,173910 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_precondition_v2' (66) for device 0
8,173912 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_precondition_Y0U0V0' (67) for device 0
8,173914 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_init' (68) for device 0
8,173916 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_dist' (69) for device 0
8,173918 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_horiz' (70) for device 0
8,173920 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_vert' (71) for device 0
8,173922 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_accu' (72) for device 0
8,173923 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_finish' (73) for device 0
8,173926 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_finish_v2' (74) for device 0
8,173928 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_backtransform' (75) for device 0
8,173930 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_backtransform_v2' (76) for device 0
8,173932 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_backtransform_Y0U0V0' (77) for device 0
8,173934 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_decompose' (78) for device 0
8,173936 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_synthesize' (79) for device 0
8,173938 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_reduce_first' (80) for device 0
8,173940 [opencl_create_kernel] successfully loaded kernel `denoiseprofile_reduce_second' (81) for device 0
8,175485 [opencl_create_kernel] successfully loaded kernel `nlmeans_init' (82) for device 0
8,175489 [opencl_create_kernel] successfully loaded kernel `nlmeans_dist' (83) for device 0
8,175491 [opencl_create_kernel] successfully loaded kernel `nlmeans_horiz' (84) for device 0
8,175493 [opencl_create_kernel] successfully loaded kernel `nlmeans_vert' (85) for device 0
8,175495 [opencl_create_kernel] successfully loaded kernel `nlmeans_accu' (86) for device 0
8,175497 [opencl_create_kernel] successfully loaded kernel `nlmeans_finish' (87) for device 0
8,176291 [opencl_create_kernel] successfully loaded kernel `graduatedndp' (88) for device 0
8,176295 [opencl_create_kernel] successfully loaded kernel `graduatedndm' (89) for device 0
8,178902 [opencl_create_kernel] successfully loaded kernel `colorchecker' (90) for device 0
8,180031 [opencl_create_kernel] successfully loaded kernel `rgbcurve' (91) for device 0
8,181558 [opencl_create_kernel] successfully loaded kernel `splittoning' (92) for device 0
8,182901 [opencl_create_kernel] successfully loaded kernel `rgblevels' (93) for device 0
8,184069 [opencl_create_kernel] successfully loaded kernel `monochrome_filter' (94) for device 0
8,184076 [opencl_create_kernel] successfully loaded kernel `monochrome' (95) for device 0
8,186477 [opencl_create_kernel] successfully loaded kernel `eaw_decompose' (96) for device 0
8,186485 [opencl_create_kernel] successfully loaded kernel `eaw_synthesize' (97) for device 0
8,188253 [opencl_create_kernel] successfully loaded kernel `colorbalance' (98) for device 0
8,188260 [opencl_create_kernel] successfully loaded kernel `colorbalance_lgg' (99) for device 0
8,188263 [opencl_create_kernel] successfully loaded kernel `colorbalance_cdl' (100) for device 0
8,189499 [opencl_create_kernel] successfully loaded kernel `colorin_unbound' (101) for device 0
8,189504 [opencl_create_kernel] successfully loaded kernel `colorin_clipping' (102) for device 0
8,190308 [opencl_create_kernel] successfully loaded kernel `shadows_highlights_mix' (103) for device 0
8,191201 [opencl_create_kernel] successfully loaded kernel `basecurve_lut' (104) for device 0
8,191205 [opencl_create_kernel] successfully loaded kernel `basecurve_zero' (105) for device 0
8,191207 [opencl_create_kernel] successfully loaded kernel `basecurve_legacy_lut' (106) for device 0
8,191209 [opencl_create_kernel] successfully loaded kernel `basecurve_compute_features' (107) for device 0
8,191211 [opencl_create_kernel] successfully loaded kernel `basecurve_blur_h' (108) for device 0
8,191213 [opencl_create_kernel] successfully loaded kernel `basecurve_blur_v' (109) for device 0
8,191215 [opencl_create_kernel] successfully loaded kernel `basecurve_expand' (110) for device 0
8,191216 [opencl_create_kernel] successfully loaded kernel `basecurve_reduce' (111) for device 0
8,191218 [opencl_create_kernel] successfully loaded kernel `basecurve_detail' (112) for device 0
8,191220 [opencl_create_kernel] successfully loaded kernel `basecurve_adjust_features' (113) for device 0
8,191222 [opencl_create_kernel] successfully loaded kernel `basecurve_blend_gaussian' (114) for device 0
8,191224 [opencl_create_kernel] successfully loaded kernel `basecurve_blend_laplacian' (115) for device 0
8,191226 [opencl_create_kernel] successfully loaded kernel `basecurve_normalize' (116) for device 0
8,191228 [opencl_create_kernel] successfully loaded kernel `basecurve_reconstruct' (117) for device 0
8,191229 [opencl_create_kernel] successfully loaded kernel `basecurve_finalize' (118) for device 0
8,195308 [opencl_create_kernel] successfully loaded kernel `channelmixer' (119) for device 0
8,197997 [opencl_create_kernel] successfully loaded kernel `colorout' (120) for device 0
8,198834 [opencl_create_kernel] successfully loaded kernel `basicadj' (121) for device 0
8,199601 [opencl_create_kernel] successfully loaded kernel `hazeremoval_transision_map' (122) for device 0
8,199605 [opencl_create_kernel] successfully loaded kernel `hazeremoval_box_min_x' (123) for device 0
8,199607 [opencl_create_kernel] successfully loaded kernel `hazeremoval_box_min_y' (124) for device 0
8,199609 [opencl_create_kernel] successfully loaded kernel `hazeremoval_box_max_x' (125) for device 0
8,199611 [opencl_create_kernel] successfully loaded kernel `hazeremoval_box_max_y' (126) for device 0
8,199613 [opencl_create_kernel] successfully loaded kernel `hazeremoval_dehaze' (127) for device 0
8,200431 [opencl_create_kernel] successfully loaded kernel `colorreconstruction_zero' (128) for device 0
8,200435 [opencl_create_kernel] successfully loaded kernel `colorreconstruction_splat' (129) for device 0
8,200438 [opencl_create_kernel] successfully loaded kernel `colorreconstruction_blur_line' (130) for device 0
8,200440 [opencl_create_kernel] successfully loaded kernel `colorreconstruction_slice' (131) for device 0
8,201931 [opencl_create_kernel] successfully loaded kernel `overexposed' (132) for device 0
8,202677 [opencl_create_kernel] successfully loaded kernel `colorcorrection' (133) for device 0
8,204435 [opencl_create_kernel] successfully loaded kernel `clip_and_zoom_demosaic_half_size' (134) for device 0
8,204440 [opencl_create_kernel] successfully loaded kernel `ppg_demosaic_green' (135) for device 0
8,204442 [opencl_create_kernel] successfully loaded kernel `green_equilibration_lavg' (136) for device 0
8,204444 [opencl_create_kernel] successfully loaded kernel `green_equilibration_favg_reduce_first' (137) for device 0
8,204447 [opencl_create_kernel] successfully loaded kernel `green_equilibration_favg_reduce_second' (138) for device 0
8,204448 [opencl_create_kernel] successfully loaded kernel `green_equilibration_favg_apply' (139) for device 0
8,204450 [opencl_create_kernel] successfully loaded kernel `pre_median' (140) for device 0
8,204452 [opencl_create_kernel] successfully loaded kernel `ppg_demosaic_redblue' (141) for device 0
8,204454 [opencl_create_kernel] successfully loaded kernel `clip_and_zoom' (142) for device 0
8,204456 [opencl_create_kernel] successfully loaded kernel `border_interpolate' (143) for device 0
8,204458 [opencl_create_kernel] successfully loaded kernel `color_smoothing' (144) for device 0
8,204460 [opencl_create_kernel] successfully loaded kernel `passthrough_monochrome' (145) for device 0
8,204462 [opencl_create_kernel] successfully loaded kernel `clip_and_zoom_demosaic_passthrough_monochrome' (146) for device 0
8,204464 [opencl_create_kernel] successfully loaded kernel `vng_border_interpolate' (147) for device 0
8,204466 [opencl_create_kernel] successfully loaded kernel `vng_lin_interpolate' (148) for device 0
8,204467 [opencl_create_kernel] successfully loaded kernel `clip_and_zoom_demosaic_third_size_xtrans' (149) for device 0
8,204469 [opencl_create_kernel] successfully loaded kernel `vng_green_equilibrate' (150) for device 0
8,204471 [opencl_create_kernel] successfully loaded kernel `vng_interpolate' (151) for device 0
8,204474 [opencl_create_kernel] successfully loaded kernel `markesteijn_initial_copy' (152) for device 0
8,204476 [opencl_create_kernel] successfully loaded kernel `markesteijn_green_minmax' (153) for device 0
8,204478 [opencl_create_kernel] successfully loaded kernel `markesteijn_interpolate_green' (154) for device 0
8,204480 [opencl_create_kernel] successfully loaded kernel `markesteijn_solitary_green' (155) for device 0
8,204482 [opencl_create_kernel] successfully loaded kernel `markesteijn_recalculate_green' (156) for device 0
8,204484 [opencl_create_kernel] successfully loaded kernel `markesteijn_red_and_blue' (157) for device 0
8,204486 [opencl_create_kernel] successfully loaded kernel `markesteijn_interpolate_twoxtwo' (158) for device 0
8,204489 [opencl_create_kernel] successfully loaded kernel `markesteijn_convert_yuv' (159) for device 0
8,204491 [opencl_create_kernel] successfully loaded kernel `markesteijn_differentiate' (160) for device 0
8,204492 [opencl_create_kernel] successfully loaded kernel `markesteijn_homo_threshold' (161) for device 0
8,204495 [opencl_create_kernel] successfully loaded kernel `markesteijn_homo_set' (162) for device 0
8,204497 [opencl_create_kernel] successfully loaded kernel `markesteijn_homo_sum' (163) for device 0
8,204499 [opencl_create_kernel] successfully loaded kernel `markesteijn_homo_max' (164) for device 0
8,204501 [opencl_create_kernel] successfully loaded kernel `markesteijn_homo_max_corr' (165) for device 0
8,204502 [opencl_create_kernel] successfully loaded kernel `markesteijn_homo_quench' (166) for device 0
8,204504 [opencl_create_kernel] successfully loaded kernel `markesteijn_zero' (167) for device 0
8,204506 [opencl_create_kernel] successfully loaded kernel `markesteijn_accu' (168) for device 0
8,204508 [opencl_create_kernel] successfully loaded kernel `markesteijn_final' (169) for device 0
8,205311 [opencl_create_kernel] successfully loaded kernel `zonesystem' (170) for device 0
8,206107 [opencl_create_kernel] successfully loaded kernel `lowpass_mix' (171) for device 0
8,206929 [opencl_create_kernel] successfully loaded kernel `invert_1f' (172) for device 0
8,206934 [opencl_create_kernel] successfully loaded kernel `invert_4f' (173) for device 0
8,207742 [opencl_create_kernel] successfully loaded kernel `lowlight' (174) for device 0
8,208718 [opencl_create_kernel] successfully loaded kernel `soften_overexposed' (175) for device 0
8,208723 [opencl_create_kernel] successfully loaded kernel `soften_hblur' (176) for device 0
8,208725 [opencl_create_kernel] successfully loaded kernel `soften_vblur' (177) for device 0
8,208727 [opencl_create_kernel] successfully loaded kernel `soften_mix' (178) for device 0
8,209506 [opencl_create_kernel] successfully loaded kernel `flip' (179) for device 0
8,210523 [opencl_create_kernel] successfully loaded kernel `lut3d_tetrahedral' (180) for device 0
8,210528 [opencl_create_kernel] successfully loaded kernel `lut3d_trilinear' (181) for device 0
8,210529 [opencl_create_kernel] successfully loaded kernel `lut3d_pyramid' (182) for device 0
8,210532 [opencl_create_kernel] successfully loaded kernel `lut3d_none' (183) for device 0
8,211457 [opencl_create_kernel] successfully loaded kernel `colorzones' (184) for device 0
8,211461 [opencl_create_kernel] successfully loaded kernel `colorzones_v3' (185) for device 0
8,212382 [opencl_create_kernel] successfully loaded kernel `highlights_1f_clip' (186) for device 0
8,212387 [opencl_create_kernel] successfully loaded kernel `highlights_1f_lch_bayer' (187) for device 0
8,212389 [opencl_create_kernel] successfully loaded kernel `highlights_1f_lch_xtrans' (188) for device 0
8,212392 [opencl_create_kernel] successfully loaded kernel `highlights_4f_clip' (189) for device 0
8,213248 [opencl_create_kernel] successfully loaded kernel `exposure' (190) for device 0
8,214168 [opencl_create_kernel] successfully loaded kernel `warp_kernel' (191) for device 0
8,215012 [opencl_create_kernel] successfully loaded kernel `vignette' (192) for device 0
8,215865 [opencl_create_kernel] successfully loaded kernel `levels' (193) for device 0
8,216670 [opencl_create_kernel] successfully loaded kernel `sharpen_hblur' (194) for device 0
8,216675 [opencl_create_kernel] successfully loaded kernel `sharpen_vblur' (195) for device 0
8,216676 [opencl_create_kernel] successfully loaded kernel `sharpen_mix' (196) for device 0
8,219193 [opencl_create_kernel] successfully loaded kernel `whitebalance_4f' (197) for device 0
8,219198 [opencl_create_kernel] successfully loaded kernel `whitebalance_1f' (198) for device 0
8,219201 [opencl_create_kernel] successfully loaded kernel `whitebalance_1f_xtrans' (199) for device 0
8,221583 [opencl_create_kernel] successfully loaded kernel `borders_fill' (200) for device 0
8,222416 [opencl_create_kernel] successfully loaded kernel `velvia' (201) for device 0
8,224523 [opencl_create_kernel] successfully loaded kernel `highpass_invert' (202) for device 0
8,224530 [opencl_create_kernel] successfully loaded kernel `highpass_hblur' (203) for device 0
8,224532 [opencl_create_kernel] successfully loaded kernel `highpass_vblur' (204) for device 0
8,224536 [opencl_create_kernel] successfully loaded kernel `highpass_mix' (205) for device 0
8,225736 [opencl_create_kernel] successfully loaded kernel `colormapping_histogram' (206) for device 0
8,225743 [opencl_create_kernel] successfully loaded kernel `colormapping_mapping' (207) for device 0
8,227706 [opencl_create_kernel] successfully loaded kernel `ashift_bilinear' (208) for device 0
8,227717 [opencl_create_kernel] successfully loaded kernel `ashift_bicubic' (209) for device 0
8,227723 [opencl_create_kernel] successfully loaded kernel `ashift_lanczos2' (210) for device 0
8,227728 [opencl_create_kernel] successfully loaded kernel `ashift_lanczos3' (211) for device 0
8,233917 [opencl_create_kernel] successfully loaded kernel `bloom_threshold' (212) for device 0
8,233928 [opencl_create_kernel] successfully loaded kernel `bloom_hblur' (213) for device 0
8,233933 [opencl_create_kernel] successfully loaded kernel `bloom_vblur' (214) for device 0
8,233937 [opencl_create_kernel] successfully loaded kernel `bloom_mix' (215) for device 0
8,235280 [opencl_create_kernel] successfully loaded kernel `pixelmax_first' (216) for device 0
8,235287 [opencl_create_kernel] successfully loaded kernel `pixelmax_second' (217) for device 0
8,235290 [opencl_create_kernel] successfully loaded kernel `global_tonemap_reinhard' (218) for device 0
8,235293 [opencl_create_kernel] successfully loaded kernel `global_tonemap_drago' (219) for device 0
8,235297 [opencl_create_kernel] successfully loaded kernel `global_tonemap_filmic' (220) for device 0
8,236416 [opencl_create_kernel] successfully loaded kernel `rawprepare_1f' (221) for device 0
8,236428 [opencl_create_kernel] successfully loaded kernel `rawprepare_1f_unnormalized' (222) for device 0
8,236433 [opencl_create_kernel] successfully loaded kernel `rawprepare_4f' (223) for device 0
8,237950 [opencl_create_kernel] successfully loaded kernel `lens_distort_bilinear' (224) for device 0
8,237958 [opencl_create_kernel] successfully loaded kernel `lens_distort_bicubic' (225) for device 0
8,237960 [opencl_create_kernel] successfully loaded kernel `lens_distort_lanczos2' (226) for device 0
8,237963 [opencl_create_kernel] successfully loaded kernel `lens_distort_lanczos3' (227) for device 0
8,237967 [opencl_create_kernel] successfully loaded kernel `lens_vignette' (228) for device 0
8,279418 [opencl_create_kernel] successfully loaded kernel `rawoverexposed_mark_cfa' (229) for device 0
8,279425 [opencl_create_kernel] successfully loaded kernel `rawoverexposed_mark_solid' (230) for device 0
8,279428 [opencl_create_kernel] successfully loaded kernel `rawoverexposed_falsecolor' (231) for device 0
8,280341 [opencl_create_kernel] successfully loaded kernel `filmicrgb_split' (232) for device 0
8,280346 [opencl_create_kernel] successfully loaded kernel `filmicrgb_chroma' (233) for device 0
```

---

### 评论 #18 — ROCmSupport (2021-03-17T07:33:41Z)

Thanks @pjones8404lml and all for reaching us with this issue.
This issue is fixed and no more observed with the latest ROCm 4.0.
Request you to try with the same.
Thank you.


---
