# [Issue]: Memory access fault by GPU node-1 (Agent handle: ...) on address (nil). Reason: Page not present or supervisor privilege

- **Issue #:** 5616
- **State:** closed
- **Created:** 2025-11-02T14:33:04Z
- **Updated:** 2026-01-11T01:24:48Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5616

### Problem Description

On my TUXEDO InfinityBook Pro 14 - Gen9 laptop I'm regularly doing image processing in darktable and make use of the OpenCL ROCr runtime which comes with ROCm.
Unfortunately I keep experiencing the following program crashes with the following error message:
```
Memory access fault by GPU node-1 (Agent handle: 0x70dcc0d7e460) on address (nil). Reason: Page not present or supervisor privilege
```

This seems to be related with mapped memory from RAM.
I allowed the iGPU to use 4 GB of RAM within the laptop BIOS.

But it looks like the OpenCL system is reporting the amount of memory incorrectly (see attached clinfo log below):

**Platform Name: AMD Accelerated Parallel Processing**
```
  Global memory size                              14599004160 (13.6GiB)
  Global free memory (AMD)                        13966156 (13.32GiB) 13966156 (13.32GiB) <--- wrong!
```

**Platform Name: Clover**
```
  Global memory size                              14599004160 (13.6GiB)
  Max memory allocation                           3649751040 (3.399GiB) <--- seems correct!
```

**Platform Name: rusticl**
No mem info in clinfo :( 

I'm currently on the mainline 6.17.6 kernel with the latest amdgpu linux firmware (from git) and use ROCm 7.0.1, but I have experienced this issues with previous versions as well.

I installed ROCm with the following command:
```
amdgpu-install --usecase=graphics,multimedia,opencl  --opencl=rocr   --no-dkms
```

Here are the system infos:
```
OS:
NAME="Ubuntu"
VERSION="24.04.3 LTS (Noble Numbat)"
CPU: 
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
GPU:
  Name:                    AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
  Marketing Name:          AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
  Name:                    gfx1103                            
  Marketing Name:          AMD Radeon Graphics                
      Name:                    amdgcn-amd-amdhsa--gfx1103         
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
  Name:                    aie2                               
  Marketing Name:          AIE-ML
```

### Operating System

Ubuntu 24.04

### CPU

AMD Ryzen 7 8845HS

### GPU

Radeon 780M

### ROCm Version

ROCm 7.0.1

### ROCm Component

ROCR-Runtime

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
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
  Name:                    AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
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
  Max Clock Freq. (MHz):   2000                               
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
      Size:                    28513680(0x1b31590) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    28513680(0x1b31590) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    28513680(0x1b31590) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    28513680(0x1b31590) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1103                            
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
  Chip ID:                 6400(0x1900)                       
  ASIC Revision:           12(0xc)                            
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2700                               
  BDFID:                   25856                              
  Internal Node ID:        1                                  
  Compute Unit:            12                                 
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
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
  Packet Processor uCode:: 67                                 
  SDMA engine uCode::      23                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    14256840(0xd98ac8) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    14256840(0xd98ac8) KB              
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
      Name:                    amdgcn-amd-amdhsa--gfx1103         
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
  Name:                    aie2                               
  Uuid:                    AIE-XX                             
  Marketing Name:          AIE-ML                             
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
      Size:                    28513680(0x1b31590) KB             
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
      Size:                    28513680(0x1b31590) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***    
```

### Additional Information

OpenCL info from `clinfo`: [clinfo.txt](https://github.com/user-attachments/files/23291781/clinfo.txt)

Kernel log (`dmesg`):
```
[229550.864052] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:88 vmid:8 pasid:32787)
[229550.864069] amdgpu 0000:65:00.0: amdgpu:  Process darktable pid 70131 thread worker 0 pid 70175
[229550.864075] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
[229550.864079] amdgpu 0000:65:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x008012B0
[229550.864083] amdgpu 0000:65:00.0: amdgpu: 	 Faulty UTCL2 client ID: SQC (inst) (0x9)
[229550.864087] amdgpu 0000:65:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[229550.864090] amdgpu 0000:65:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[229550.864093] amdgpu 0000:65:00.0: amdgpu: 	 PERMISSION_FAULTS: 0xb
[229550.864096] amdgpu 0000:65:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[229550.864099] amdgpu 0000:65:00.0: amdgpu: 	 RW: 0x0
[229552.867660] amdgpu 0000:65:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[229552.867671] amdgpu 0000:65:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[229552.867675] amdgpu 0000:65:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[229552.867681] amdgpu 0000:65:00.0: amdgpu: Failed to evict queue 1
[229552.867727] amdgpu 0000:65:00.0: amdgpu: GPU reset begin!
[229552.867838] amdgpu 0000:65:00.0: amdgpu: Failed to evict process queues
[229552.867896] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 0, simd_id 0, wgp_id 0
[229552.867925] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[229552.867933] amdgpu 0000:65:00.0: amdgpu: Dumping IP State
[229552.867949] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 0, simd_id 0, wgp_id 0
[229552.867971] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[229552.867996] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 0, simd_id 0, wgp_id 0
[229552.868019] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[229552.868052] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[229552.868078] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[229552.868101] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 2, simd_id 0, wgp_id 0
[229552.868120] amdgpu 0000:65:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[229552.870187] amdgpu 0000:65:00.0: amdgpu: Dumping IP State Completed
[229552.915324] amdgpu 0000:65:00.0: amdgpu: MODE2 reset
[229552.954067] amdgpu 0000:65:00.0: amdgpu: GPU reset succeeded, trying to resume
[229552.954617] [drm] PCIE GART of 512M enabled (table at 0x00000080FFD00000).
[229552.954744] amdgpu 0000:65:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[229552.954747] amdgpu 0000:65:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[229552.954752] amdgpu 0000:65:00.0: amdgpu: SMU is resuming...
[229552.955886] amdgpu 0000:65:00.0: amdgpu: SMU is resumed successfully!
[229552.961851] amdgpu 0000:65:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005400
[229553.668577] amdgpu 0000:65:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[229553.668593] amdgpu 0000:65:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[229553.668600] amdgpu 0000:65:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[229553.668606] amdgpu 0000:65:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[229553.668612] amdgpu 0000:65:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[229553.668617] amdgpu 0000:65:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[229553.668623] amdgpu 0000:65:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[229553.668628] amdgpu 0000:65:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[229553.668635] amdgpu 0000:65:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[229553.668640] amdgpu 0000:65:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[229553.668646] amdgpu 0000:65:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[229553.668653] amdgpu 0000:65:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[229553.668658] amdgpu 0000:65:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[229553.672192] amdgpu 0000:65:00.0: amdgpu: GPU reset(1) succeeded!
[229553.672211] amdgpu 0000:65:00.0: [drm] device wedged, but recovered through reset
[229652.878954] amdgpu: Freeing queue vital buffer 0x70db22c00000, queue evicted
[229652.878975] amdgpu: Freeing queue vital buffer 0x70dc80c00000, queue evicted
[229652.878980] amdgpu: Freeing queue vital buffer 0x70dc81200000, queue evicted
[232494.801494] amdgpu: Freeing queue vital buffer 0x7dfb2a200000, queue evicted
[232494.801506] amdgpu: Freeing queue vital buffer 0x7dfb2a800000, queue evicted
[233918.552578] amdgpu: Freeing queue vital buffer 0x7d3c2f200000, queue evicted
[233918.552591] amdgpu: Freeing queue vital buffer 0x7d3c2f800000, queue evicted
```