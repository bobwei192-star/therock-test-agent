# [Issue]: GPU Crashes During LSTM Training on Radeon 7900 XTX with ROCm 6.0.2

- **Issue #:** 2974
- **State:** closed
- **Created:** 2024-03-23T06:45:04Z
- **Updated:** 2024-06-20T00:21:22Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 XTX
- **URL:** https://github.com/ROCm/ROCm/issues/2974

### Problem Description

Environment

    GPU: Radeon 7900 XTX
    CPU: AMD Ryzen 5 5500
    OS: Ubuntu 22.04.4 LTS
    Kernel Version: 6.5.0-26-generic
    ROCm Version: 6.0.2.60002-115~22.04
    Python Version: 3.10.12
    PyTorch Version: 2.1.2

Issue Description

When training LSTMs with text categorization using my [implementation here](https://github.com/brownbat/cipher_classifier_factory.git), the GPU crashes within the first few epochs as I increase dimensions. Sometimes I see overheating, sometimes the crashes happen at low reported junction temperatures. Attempts to capture detailed logs using AMD_LOG_LEVEL and HSAKMT_DEBUG_LEVEL either fail to produce sufficient logs to pinpoint the issue or throttled the GPU to about a third of its speed making it difficult to trigger the issue.

Attempted Solutions and Debugging

Setting AMD_LOG_LEVEL=4 and HSAKMT_DEBUG_LEVEL=7 to capture debug information, which throttled the GPU and prevented crashes but did not identify the issue.

Adjusting the garbage collection threshold with PYTORCH_HIP_ALLOC_CONF=garbage_collection_threshold:0.6,max_split_size_mb:6144 did not have a significant impact.

Error Messages and Logs

I captured logs with AMD_LOG_LEVEL=2 and HSAKMT_DEBUG_LEVEL=4, which generated a 64KB file prior to a crash. The logs contained numerous entries like:

```
:1:hip_code_object.cpp :616 : 24525027673 us: [pid:144693 tid:0x7f15caa3d000] Cannot find the function: Cijk_Alik_Bljk_SB_MT16x16x8_SN_1LDSB0_APM1_ABV0_ACED0_AF0EM1_AF1EM1_AMAS0_ASE_ASGT_ASLT_ASAE01_ASCE01_ASEM1_AAC0_BL1_BS1_DTLA0_DTLB0_DTVA0_DTVB0_DVO0_ETSP_EPS1_FSSC10_FL0_GRPM1_GRVW1_GSU1_GSUAMB_GLS0_ISA1100_IU1_K1_KLA_LBSPP0_LPA0_LPB0_LDL1_LRVW1_LWPMn1_LDW0_FMA_MIAV0_MDA2_MO40_MMFGLC_NTA0_NTB0_NTC0_NTD0_NEPBS0_NLCA1_NLCB1_ONLL1_OPLV0_PK0_PAP0_PGR1_PLR1_SIA1_SS0_SU32_SUM3_SUS128_SCIUI1_SPO0_SRVW0_SSO0_SVW4_SNLL0_TSGRA0_TSGRB0_TT2_2_TLDS0_UMLDSA0_UMLDSB0_USFGROn1_VAW1_VSn1_VW1_WSGRA0_WSGRB0_WS32_WG8_8_1_WGM4

:1:hip_module.cpp :83 : 24525027680 us: [pid:144693 tid:0x7f15caa3d000] Cannot find the function: Cijk_Alik_Bljk_SB_MT16x16x8_SN_1LDSB0_APM1_ABV0_ACED0_AF0EM1_AF1EM1_AMAS0_ASE_ASGT_ASLT_ASAE01_ASCE01_ASEM1_AAC0_BL1_BS1_DTLA0_DTLB0_DTVA0_DTVB0_DVO0_ETSP_EPS1_FSSC10_FL0_GRPM1_GRVW1_GSU1_GSUAMB_GLS0_ISA1100_IU1_K1_KLA_LBSPP0_LPA0_LPB0_LDL1_LRVW1_LWPMn1_LDW0_FMA_MIAV0_MDA2_MO40_MMFGLC_NTA0_NTB0_NTC0_NTD0_NEPBS0_NLCA1_NLCB1_ONLL1_OPLV0_PK0_PAP0_PGR1_PLR1_SIA1_SS0_SU32_SUM3_SUS128_SCIUI1_SPO0_SRVW0_SSO0_SVW4_SNLL0_TSGRA0_TSGRB0_TT2_2_TLDS0_UMLDSA0_UMLDSB0_USFGROn1_VAW1_VSn1_VW1_WSGRA0_WSGRB0_WS32_WG8_8_1_WGM4 for module: 0x1391e270
```

Welcome any insights on what might be happening here, or suggestions for further debugging steps, or relations to any other known issues.

### Operating System

Ubuntu 22.04.4 LTS

### CPU

AMD Ryzen 5 5500

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

This is straightforward to consistently reproduce using the research project I'm working on, but I have not boiled this down to a minimal program that triggers these.

1. Clone the repository: 
```git clone https://github.com/brownbat/cipher_classifier_factory.git```
2. Install required packages: 
```pip install -r requirements.txt```
3. Run the training script with settings that trigger crash: 
```python3 researcher.py --num_samples 1000000 --num_layers 256 --batch_size 256 --embedding_dim 512 --hidden_dim 512```

Lower intensity settings also triggered crashes, the above are probably overkill, but more reliably crash more quickly, in the first epoch. I also received crashes with:
```--num_samples 50000 --num_layers 64 --batch_size 64 --embedding_dim 32 --hidden_dim 256```
But it might take 4-5 epochs with those.

You can instead set various dimensions and hyperparameters by changing the defaults stored at the top of researcher.py as "default_params" -- that would let you then just run `python3 researcher.py` without arguments.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```ROCk module is loaded
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
  Name:                    AMD Ryzen 5 5500                   
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 5500                   
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
  Max Clock Freq. (MHz):   4267                               
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
      Size:                    65619552(0x3e94660) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65619552(0x3e94660) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65619552(0x3e94660) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-af80fc06fd8c76ab               
  Marketing Name:          Radeon RX 7900 XTX                 
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
    L2:                      6144(0x1800) KB                    
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2482                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
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
  Packet Processor uCode:: 550                                
  SDMA engine uCode::      19                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx1100         
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