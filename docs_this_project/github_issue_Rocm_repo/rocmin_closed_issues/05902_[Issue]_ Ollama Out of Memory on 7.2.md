# [Issue]: Ollama Out of Memory on 7.2

- **Issue #:** 5902
- **State:** closed
- **Created:** 2026-01-26T12:23:44Z
- **Updated:** 2026-03-09T13:23:40Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5902

### Problem Description

ROCm is ooming under ollama with a model that fits easily in memory in ROCm 7.1:

qwen3:14b-q8_0                                             304bf7349c71    15 GB 

### Operating System

NAME="Ubuntu" VERSION="24.04.3 LTS (Noble Numbat)"

### CPU

model name      : AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S   Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S   Name:                    gfx1151                               Marketing Name:          AMD Radeon Graphics                       Name:                    amdgcn-amd-amdhsa--gfx1151                Name:                    amdgcn-amd-amdhsa--gfx11-generic      Name:                    aie2p                                 Marketing Name:          RyzenAI-npu5   

### ROCm Version

ROCm 7.2

### ROCm Component

rocm-core

### Steps to Reproduce

amdgpu reports 96G available (I'd love it if someone can tell me how to increase this to 112G avail).
```
kernel: [drm] amdgpu: 98304M of VRAM memory ready
```
amd-smi:
```
amd-smi 
+------------------------------------------------------------------------------+
| AMD-SMI 26.2.1+fc0010cf6a    amdgpu version: Linuxver ROCm version: 7.2.0    |
| VBIOS version: 023.011.000.039.000001                                        |
| Platform: Linux Baremetal                                                    |
|-------------------------------------+----------------------------------------|
| BDF                        GPU-Name | Mem-Uti   Temp   UEC       Power-Usage |
| GPU  HIP-ID  OAM-ID  Partition-Mode | GFX-Uti    Fan               Mem-Usage |
|=====================================+========================================|
| 0000:c5:00.0    AMD Radeon Graphics | N/A        N/A   0                 N/A |
|   0       0     N/A             N/A | N/A        N/A            161/98304 MB |
+-------------------------------------+----------------------------------------+
+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU        PID  Process Name          GTT_MEM  VRAM_MEM  MEM_USAGE     CU % |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+

```

ROCm appears to report 112G
```
ollama[1297]: time=2026-01-26T12:06:56.209Z level=INFO source=types.go:42 msg="inference compute" id=0 filter_id=0 library=ROCm compute=gfx1151 name=ROCm0 description="AMD Radeon Graphics" libdirs=ollama,rocm driver=60342.13 pci_id=0000:c5:00.0 type=iGPU total="111.5 GiB" available="111.3 GiB"
```

OOM
```
ollama[1297]: ROCm error: out of memory
ollama[1297]:   current device: 0, in function stream at //ml/backend/ggml/ggml/src/ggml-cuda/common.cuh:1248
ollama[1297]:   hipStreamCreateWithFlags(&streams[device][stream], 0x01)
ollama[1297]: //ml/backend/ggml/ggml/src/ggml-cuda/ggml-cuda.cu:94: ROCm error
ollama[1297]: /usr/local/lib/ollama/libggml-base.so.0(+0x1bae8)[0x7dd72c301ae8]
ollama[1297]: /usr/local/lib/ollama/libggml-base.so.0(ggml_print_backtrace+0x1e6)[0x7dd72c301eb6]
ollama[1297]: /usr/local/lib/ollama/libggml-base.so.0(ggml_abort+0x11d)[0x7dd72c30203d]
ollama[1297]: /usr/local/lib/ollama/rocm/libggml-hip.so(+0x1bd1c2)[0x7dd6c2dbd1c2]
ollama[1297]: /usr/local/lib/ollama/rocm/libggml-hip.so(+0x1c2b27)[0x7dd6c2dc2b27]
ollama[1297]: /usr/local/bin/ollama(+0x11fd64e)[0x55661b13164e]
ollama[1297]: /usr/local/bin/ollama(+0x1200430)[0x55661b134430]
ollama[1297]: /usr/local/bin/ollama(+0x119aaff)[0x55661b0ceaff]
ollama[1297]: /usr/local/bin/ollama(+0x3a4841)[0x55661a2d8841]
ollama[1297]: SIGABRT: abort
ollama[1297]: PC=0x7dd77709eb2c m=14 sigcode=18446744073709551610
ollama[1297]: signal arrived during cgo execution
ollama[1297]: goroutine 15 gp=0xc000703180 m=14 mp=0xc000701008 [syscall]:
ollama[1297]: runtime.cgocall(0x55661b0ceac8, 0xc0000490d8)
ollama[1297]:         runtime/cgocall.go:167 +0x4b fp=0xc0000490b0 sp=0xc000049078 pc=0x55661a2cd8ab
ollama[1297]: github.com/ollama/ollama/ml/backend/ggml._Cfunc_ggml_backend_sched_reserve(0x7dd6f4d031b0, 0x7dd5402be210)
```



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ESC[37mROCk module is loadedESC[0m
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.15
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
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
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
  Max Clock Freq. (MHz):   5187                               
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
      Size:                    32484672(0x1efad40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32484672(0x1efad40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32484672(0x1efad40) KB             
      Allocatable:             TRUE                               
:
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32484672(0x1efad40) KB             
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
    L3:                      32768(0x8000) KB                   
  Chip ID:                 5510(0x1586)                       
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2900                               
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 32                                 
  SDMA engine uCode::      14                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    100663296(0x6000000) KB            
      Allocatable:             TRUE                               
     Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    100663296(0x6000000) KB            
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
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
*******                  
Agent 3                  
*******                  
  Name:                    aie2p                              
  Uuid:                    AIE-XX                             
  Marketing Name:          RyzenAI-npu5                       
  Vendor Name:             AMD                                
  Feature:                 AGENT_DISPATCH                     
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        1(0x1)                             
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          64(0x40)                           
 Queue Type:              SINGLE                             
  Node:                    0                                  
  Device Type:             DSP                                
  Cache Info:              
    L2:                      2048(0x800) KB                     
    L3:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          0(0x0)                             
  Max Clock Freq. (MHz):   0                                  
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            0                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:0                                  
  Memory Properties:       
  Features:                AGENT_DISPATCH
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, COARSE GRAINED
      Size:                    32484672(0x1efad40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65536(0x10000) KB                  
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32484672(0x1efad40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***             


### Additional Information

_No response_