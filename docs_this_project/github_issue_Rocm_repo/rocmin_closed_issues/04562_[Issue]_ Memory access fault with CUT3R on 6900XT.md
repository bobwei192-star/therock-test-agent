# [Issue]: Memory access fault with CUT3R on 6900XT

- **Issue #:** 4562
- **State:** closed
- **Created:** 2025-04-03T17:56:12Z
- **Updated:** 2025-04-11T18:36:20Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4562

### Problem Description


```
OS:
NAME="Arch Linux"
CPU: 
model name      : AMD Ryzen 9 3950X 16-Core Processor
GPU:
  Name:                    AMD Ryzen 9 3950X 16-Core Processor
  Marketing Name:          AMD Ryzen 9 3950X 16-Core Processor
  Name:                    gfx1030                            
  Marketing Name:          AMD Radeon RX 6900 XT              
      Name:                    amdgcn-amd-amdhsa--gfx1030
```

Error message: `Memory access fault by GPU node-1 (Agent handle: 0x55d8390cfe70) on address 0x7fad48bfa000. Reason: Page not present or supervisor privilege.`

kernel log:
```
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32863)
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu:  in process python pid 2945597 thread python pid 2945597
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu:   in page starting at address 0x00007fad48bfa000 from client 0x1b (UTCL2)
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801030
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu:          Faulty UTCL2 client ID: TCP (0x8)
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu:          MORE_FAULTS: 0x0
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu:          WALKER_ERROR: 0x0
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu:          PERMISSION_FAULTS: 0x3
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu:          MAPPING_ERROR: 0x0
Apr 03 19:44:28 c-pc kernel: amdgpu 0000:0c:00.0: amdgpu:          RW: 0x0
```

### Operating System

Arch Linux

### CPU

AMD Ryzen 9 3950X 16-Core Processor

### GPU

AMD Radeon RX 6900 XT

### ROCm Version

6.3.3

### ROCm Component

_No response_

### Steps to Reproduce

https://github.com/CUT3R/CUT3R

(From memory:)

Make a virtualenv

```
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.3
```
(pretty sure the same happens with rocm6.2.4)

update for current python and torch:
```diff
diff --git a/requirements.txt b/requirements.txt
index c4ad28b..424547d 100644
--- a/requirements.txt
+++ b/requirements.txt
@@ -16,8 +16,8 @@ viser
 gradio
 lpips
 hydra-core
-pillow==10.3.0
+pillow
 h5py
 accelerate
 transformers
-scikit-learn
\ No newline at end of file
+scikit-learn
diff --git a/src/dust3r/model.py b/src/dust3r/model.py
index 7ed9f61..90a4ddf 100644
--- a/src/dust3r/model.py
+++ b/src/dust3r/model.py
@@ -72,7 +72,7 @@ def strip_module(state_dict):
 def load_model(model_path, device, verbose=True):
     if verbose:
         print("... loading model from", model_path)
-    ckpt = torch.load(model_path, map_location="cpu")
+    ckpt = torch.load(model_path, map_location="cpu", weights_only=False)
     args = ckpt["args"].model.replace(
         "ManyAR_PatchEmbed", "PatchEmbedDust3R"
     )  # ManyAR only for aspect ratio not consistent
```

Otherwise follow the readme (iirc open3d is not available and I didn't install it). Make sure the checkpoints are in src/ or you get weird errors. Then this causes the issue:
```
python demo.py --model_path src/cut3r_512_dpt_4_64.pth --seq_path /path/to/image/directory --size 224 --vis_threshold 1.4 --output_dir out/
```

-> Memory access fault.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
Runtime Ext Version:     1.6
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
  Name:                    AMD Ryzen 9 3950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 3950X 16-Core Processor
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
  Max Clock Freq. (MHz):   4763                               
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
      Size:                    65746296(0x3eb3578) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65746296(0x3eb3578) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65746296(0x3eb3578) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65746296(0x3eb3578) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1030                            
  Uuid:                    GPU-b1ece36f29489405               
  Marketing Name:          AMD Radeon RX 6900 XT              
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
    L2:                      4096(0x1000) KB                    
    L3:                      131072(0x20000) KB                 
  Chip ID:                 29631(0x73bf)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2660                               
  BDFID:                   3072                               
  Internal Node ID:        1                                  
  Compute Unit:            80                                 
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
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 120                                
  SDMA engine uCode::      85                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16760832(0xffc000) KB              
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

### Additional Information

_No response_