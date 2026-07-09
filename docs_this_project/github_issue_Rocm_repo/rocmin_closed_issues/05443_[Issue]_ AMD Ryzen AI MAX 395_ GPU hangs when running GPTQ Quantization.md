# [Issue]: AMD Ryzen AI MAX 395+ GPU hangs when running GPTQ Quantization

- **Issue #:** 5443
- **State:** closed
- **Created:** 2025-09-29T12:35:53Z
- **Updated:** 2025-12-08T10:02:12Z
- **Labels:** status: assessed
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5443

### Problem Description

GPU Hangs when running GPTQ quantization

### Operating System

CachyOS Linux

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### ROCm Version

6.4.4

### ROCm Component

HIP, rocBLAS

### Steps to Reproduce

Run docker with rocm 6.4.4 with pytorch 
```
docker run -it  --name rocm6.4.4_vllm \
  --device /dev/kfd \
  --device /dev/dri \
  --security-opt seccomp=unconfined \
  --net=host \
  rocm/pytorch:rocm6.4.4_ubuntu24.04_py3.12_pytorch_release_2.7.1 bash 
```

# Install GPTQmodel to quantize weights
```
pip install -v gptqmodel --no-build-isolation
pip install logbar
pip install tokenicer
pip install device_smi
pip install random_word
```
# Run the script 
```
from gptqmodel import GPTQModel, QuantizeConfig
from datasets import load_dataset


# tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

MODEL_ID = "Qwen/Qwen3-30B-A3B-Instruct-2507"
QUANT_PATH ="Qwewn3-30B-A3B-Insturct-2507-4bit" 
# Select calibration dataset.
DATASET_ID = "HuggingFaceH4/ultrachat_200k"
DATASET_SPLIT = "train_sft"
NUM_CALIBRATION_SAMPLES = 512
MAX_SEQUENCE_LENGTH = 2048

# ds = load_dataset(DATASET_ID, split=DATASET_SPLIT).select(range(1024))['text']

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
  ).select(range(1024))["text"]

quant_config = QuantizeConfig(bits=4, group_size=128)

model= GPTQModel.load(MODEL_ID, quant_config,)

model.quantize(calibration_dataset, batch_size=2)
model.save(QUANT_PATH)
```

# Error
Quantizing mlp.experts.14.up_proj in layer     [1 of 47] ██-------------------------------------------------------------| 0:19:08 / 7:39:12 [2/48] 4.2%Memory access fault by GPU node-1 (Agent handle: 0x556e9b7e3360) on address 0x7f52c3f5f000. Reason: Page not present or supervisor privilege.
HW Exception by GPU node-1 (Agent handle: 0x563e71f098b0) reason :GPU Hang
Aborted (core dumped)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.14
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
      Size:                    131009976(0x7cf0db8) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    131009976(0x7cf0db8) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131009976(0x7cf0db8) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131009976(0x7cf0db8) KB            
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
  Packet Processor uCode:: 31                                 
  SDMA engine uCode::      14                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    125829120(0x7800000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    125829120(0x7800000) KB            
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
*** Done ***             

### Additional Information

this is what i see in ```dmseg | grep amd``` 

[244504.829208] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[244546.988929] amdgpu: Freeing queue vital buffer 0x7f4445000000, queue evicted
[244546.988935] amdgpu: Freeing queue vital buffer 0x7f444d000000, queue evicted
[244546.988937] amdgpu: Freeing queue vital buffer 0x7f444f000000, queue evicted
[244546.988939] amdgpu: Freeing queue vital buffer 0x7f4450800000, queue evicted
[245848.086124] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086130] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086131] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f5f000 from client 10
[245848.086133] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
[245848.086135] amdgpu 0000:c5:00.0: amdgpu:     Faulty UTCL2 client ID: TCP (0x8)
[245848.086136] amdgpu 0000:c5:00.0: amdgpu:     MORE_FAULTS: 0x1
[245848.086137] amdgpu 0000:c5:00.0: amdgpu:     WALKER_ERROR: 0x0
[245848.086137] amdgpu 0000:c5:00.0: amdgpu:     PERMISSION_FAULTS: 0x3
[245848.086138] amdgpu 0000:c5:00.0: amdgpu:     MAPPING_ERROR: 0x0
[245848.086139] amdgpu 0000:c5:00.0: amdgpu:     RW: 0x0
[245848.086146] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086147] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086147] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f7c000 from client 10
[245848.086154] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086154] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086155] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f6b000 from client 10
[245848.086161] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086162] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086162] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f68000 from client 10
[245848.086168] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086169] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086169] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f59000 from client 10
[245848.086175] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086176] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086176] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f61000 from client 10
[245848.086182] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086183] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086183] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f64000 from client 10
[245848.086189] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086189] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086190] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f6f000 from client 10
[245848.086196] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086196] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086197] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f75000 from client 10
[245848.086202] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32771)
[245848.086203] amdgpu 0000:c5:00.0: amdgpu:  in process python3 pid 2261545 thread python3 pid 2261545)
[245848.086204] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f52c3f72000 from client 10
[245850.667623] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=SUSPEND
[245850.667629] [drm:amdgpu_mes_suspend [amdgpu]] *ERROR* failed to suspend all gangs
[245850.667845] amdgpu 0000:c5:00.0: amdgpu: failed to suspend gangs from MES
[245850.667846] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[245850.667849] amdgpu 0000:c5:00.0: amdgpu: Suspending all queues failed
[245850.667871] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!
[245851.086396] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 4
[245851.086403] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 3
[245851.086404] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 2
[245851.086405] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
[245851.086405] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 0
[245851.086441] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[245851.086454] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[245851.086463] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[245851.086464] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[245851.086473] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[245851.086479] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[245851.086484] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[245851.086488] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[245851.086494] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[245851.086501] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[245851.086505] amdgpu 0000:c5:00.0: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[245851.088427] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[245851.096704] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[245851.129821] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[245851.130359] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[245851.130361] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card0/device/devcoredump/data
[245851.130363] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[245851.139255] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[245851.151027] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x09002600
[245851.157761] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[245851.157764] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[245851.157765] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[245851.157766] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[245851.157767] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[245851.157768] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[245851.157768] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[245851.157769] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[245851.157769] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[245851.157770] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[245851.157770] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[245851.157771] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
[245851.157771] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_0 uses VM inv eng 4 on hub 8
[245851.157772] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_1 uses VM inv eng 6 on hub 8
[245851.157772] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[245851.157773] amdgpu 0000:c5:00.0: amdgpu: ring vpe uses VM inv eng 7 on hub 8
[245851.160282] amdgpu 0000:c5:00.0: amdgpu: GPU reset(15) succeeded!
[245851.160291] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[245895.778362] amdgpu: Freeing queue vital buffer 0x7f52bd600000, queue evicted
[245895.778367] amdgpu: Freeing queue vital buffer 0x7f52c1400000, queue evicted
[245895.778367] amdgpu: Freeing queue vital buffer 0x7f52c3200000, queue evicted
[245895.778368] amdgpu: Freeing queue vital buffer 0x7f52c8e00000, queue evicted


