# Status of Hawaii support under ROCm 3.0?

- **Issue #:** 1006
- **State:** closed
- **Created:** 2020-01-27T08:54:14Z
- **Updated:** 2024-07-05T14:01:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/1006

My test server runs under Ubuntu 18.04 with the 4.15.0-60-generic kernel. There are 2 GPUs in the system: 1) Radeon RX Vega gfx900 card that works correctly with ROCm 3.0 and 2) S9150 gfx701 card that experiences problems.

As far as I understand from https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/68, the problems with Hawaii architecture support have been solved.

However on my system I can see the correct output from `rocm-smi` and `rocminfo` but `clinfo`  gives not output and hangs up to the ctrl-c cancelation.

Please let me know if ROCm 3.0 is supposed to work with Hawaii (and S9150)?
I cite the key information about this system below:

```
rocminfo
ROCk module is loaded
user is member of video group
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
  Name:                    Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz
  Marketing Name:          Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz
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
  Max Clock Freq. (MHz):   3000                               
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
      Size:                    16308652(0xf8d9ac) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16308652(0xf8d9ac) KB              
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
  Marketing Name:          Vega [Radeon RX Vega]              
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
  Chip ID:                 26751(0x687f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1590                               
  BDFID:                   1024                               
  Internal Node ID:        1                                  
  Compute Unit:            56                                 
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
      Size:                    8372224(0x7fc000) KB               
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
*******                  
Agent 3                  
*******                  
  Name:                    gfx701                             
  Marketing Name:          Hawaii XT GL [FirePro W9100]       
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26528(0x67a0)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   900                                
  BDFID:                   1280                               
  Internal Node ID:        2                                  
  Compute Unit:            44                                 
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
      Size:                    16777216(0x1000000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
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
```
lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.1 LTS
Release:	18.04
Codename:	bionic
```
```
uname -r
4.15.0-60-generic
```
```
lsmod | grep amd
amdgpu               4681728  1
amdttm                 98304  1 amdgpu
amd_sched              28672  1 amdgpu
amdkcl                 28672  3 amd_sched,amdttm,amdgpu
amd_iommu_v2           20480  1 amdgpu
drm_kms_helper        172032  3 ast,amdgpu,amdkcl
i2c_algo_bit           16384  3 igb,ast,amdgpu
drm                   401408  9 drm_kms_helper,amd_sched,amdttm,ast,amdgpu,ttm
```
```
modinfo amdgpu
filename:       /lib/modules/4.15.0-60-generic/updates/dkms/amdgpu.ko
version:        5.2.4
license:        GPL and additional rights
description:    AMD GPU
author:         AMD linux driver team
firmware:       amdgpu/navi12_gpu_info.bin
firmware:       amdgpu/navi14_gpu_info.bin
firmware:       amdgpu/navi10_gpu_info.bin
firmware:       amdgpu/renoir_gpu_info.bin
firmware:       amdgpu/arcturus_gpu_info.bin
firmware:       amdgpu/raven2_gpu_info.bin
firmware:       amdgpu/picasso_gpu_info.bin
firmware:       amdgpu/raven_gpu_info.bin
firmware:       amdgpu/vega12_gpu_info.bin
firmware:       amdgpu/vega10_gpu_info.bin
firmware:       amdgpu/mullins_mec.bin
firmware:       amdgpu/mullins_rlc.bin
firmware:       amdgpu/mullins_ce.bin
firmware:       amdgpu/mullins_me.bin
firmware:       amdgpu/mullins_pfp.bin
firmware:       amdgpu/kabini_mec.bin
firmware:       amdgpu/kabini_rlc.bin
firmware:       amdgpu/kabini_ce.bin
firmware:       amdgpu/kabini_me.bin
firmware:       amdgpu/kabini_pfp.bin
firmware:       amdgpu/kaveri_mec2.bin
firmware:       amdgpu/kaveri_mec.bin
firmware:       amdgpu/kaveri_rlc.bin
firmware:       amdgpu/kaveri_ce.bin
firmware:       amdgpu/kaveri_me.bin
firmware:       amdgpu/kaveri_pfp.bin
firmware:       amdgpu/hawaii_mec.bin
firmware:       amdgpu/hawaii_rlc.bin
firmware:       amdgpu/hawaii_ce.bin
firmware:       amdgpu/hawaii_me.bin
firmware:       amdgpu/hawaii_pfp.bin
firmware:       amdgpu/bonaire_mec.bin
firmware:       amdgpu/bonaire_rlc.bin
firmware:       amdgpu/bonaire_ce.bin
firmware:       amdgpu/bonaire_me.bin
firmware:       amdgpu/bonaire_pfp.bin
firmware:       amdgpu/mullins_sdma1.bin
firmware:       amdgpu/mullins_sdma.bin
firmware:       amdgpu/kabini_sdma1.bin
firmware:       amdgpu/kabini_sdma.bin
firmware:       amdgpu/kaveri_sdma1.bin
firmware:       amdgpu/kaveri_sdma.bin
firmware:       amdgpu/hawaii_sdma1.bin
firmware:       amdgpu/hawaii_sdma.bin
firmware:       amdgpu/bonaire_sdma1.bin
firmware:       amdgpu/bonaire_sdma.bin
firmware:       amdgpu/si58_mc.bin
firmware:       amdgpu/hainan_mc.bin
firmware:       amdgpu/oland_mc.bin
firmware:       amdgpu/verde_mc.bin
firmware:       amdgpu/pitcairn_mc.bin
firmware:       amdgpu/tahiti_mc.bin
firmware:       amdgpu/hainan_rlc.bin
firmware:       amdgpu/hainan_ce.bin
firmware:       amdgpu/hainan_me.bin
firmware:       amdgpu/hainan_pfp.bin
firmware:       amdgpu/oland_rlc.bin
firmware:       amdgpu/oland_ce.bin
firmware:       amdgpu/oland_me.bin
firmware:       amdgpu/oland_pfp.bin
firmware:       amdgpu/verde_rlc.bin
firmware:       amdgpu/verde_ce.bin
firmware:       amdgpu/verde_me.bin
firmware:       amdgpu/verde_pfp.bin
firmware:       amdgpu/pitcairn_rlc.bin
firmware:       amdgpu/pitcairn_ce.bin
firmware:       amdgpu/pitcairn_me.bin
firmware:       amdgpu/pitcairn_pfp.bin
firmware:       amdgpu/tahiti_rlc.bin
firmware:       amdgpu/tahiti_ce.bin
firmware:       amdgpu/tahiti_me.bin
firmware:       amdgpu/tahiti_pfp.bin
firmware:       amdgpu/banks_k_2_smc.bin
firmware:       amdgpu/hainan_k_smc.bin
firmware:       amdgpu/hainan_smc.bin
firmware:       amdgpu/oland_k_smc.bin
firmware:       amdgpu/oland_smc.bin
firmware:       amdgpu/verde_k_smc.bin
firmware:       amdgpu/verde_smc.bin
firmware:       amdgpu/pitcairn_k_smc.bin
firmware:       amdgpu/pitcairn_smc.bin
firmware:       amdgpu/tahiti_smc.bin
firmware:       amdgpu/topaz_mc.bin
firmware:       amdgpu/hawaii_mc.bin
firmware:       amdgpu/bonaire_mc.bin
firmware:       amdgpu/polaris12_k_mc.bin
firmware:       amdgpu/polaris10_k_mc.bin
firmware:       amdgpu/polaris11_k_mc.bin
firmware:       amdgpu/polaris12_mc.bin
firmware:       amdgpu/polaris10_mc.bin
firmware:       amdgpu/polaris11_mc.bin
firmware:       amdgpu/tonga_mc.bin
firmware:       amdgpu/vega12_asd.bin
firmware:       amdgpu/vega12_sos.bin
firmware:       amdgpu/vega10_asd.bin
firmware:       amdgpu/vega10_sos.bin
firmware:       amdgpu/raven_ta.bin
firmware:       amdgpu/raven2_ta.bin
firmware:       amdgpu/picasso_ta.bin
firmware:       amdgpu/raven2_asd.bin
firmware:       amdgpu/picasso_asd.bin
firmware:       amdgpu/raven_asd.bin
firmware:       amdgpu/arcturus_ta.bin
firmware:       amdgpu/arcturus_asd.bin
firmware:       amdgpu/arcturus_sos.bin
firmware:       amdgpu/navi12_asd.bin
firmware:       amdgpu/navi12_sos.bin
firmware:       amdgpu/navi14_asd.bin
firmware:       amdgpu/navi14_sos.bin
firmware:       amdgpu/navi10_asd.bin
firmware:       amdgpu/navi10_sos.bin
firmware:       amdgpu/vega20_ta.bin
firmware:       amdgpu/vega20_asd.bin
firmware:       amdgpu/vega20_sos.bin
firmware:       amdgpu/renoir_asd.bin
firmware:       amdgpu/vegam_rlc.bin
firmware:       amdgpu/vegam_mec2.bin
firmware:       amdgpu/vegam_mec.bin
firmware:       amdgpu/vegam_me.bin
firmware:       amdgpu/vegam_pfp.bin
firmware:       amdgpu/vegam_ce.bin
firmware:       amdgpu/polaris12_rlc.bin
firmware:       amdgpu/polaris12_mec2_2.bin
firmware:       amdgpu/polaris12_mec2.bin
firmware:       amdgpu/polaris12_mec_2.bin
firmware:       amdgpu/polaris12_mec.bin
firmware:       amdgpu/polaris12_me_2.bin
firmware:       amdgpu/polaris12_me.bin
firmware:       amdgpu/polaris12_pfp_2.bin
firmware:       amdgpu/polaris12_pfp.bin
firmware:       amdgpu/polaris12_ce_2.bin
firmware:       amdgpu/polaris12_ce.bin
firmware:       amdgpu/polaris11_rlc.bin
firmware:       amdgpu/polaris11_mec2_2.bin
firmware:       amdgpu/polaris11_mec2.bin
firmware:       amdgpu/polaris11_mec_2.bin
firmware:       amdgpu/polaris11_mec.bin
firmware:       amdgpu/polaris11_me_2.bin
firmware:       amdgpu/polaris11_me.bin
firmware:       amdgpu/polaris11_pfp_2.bin
firmware:       amdgpu/polaris11_pfp.bin
firmware:       amdgpu/polaris11_ce_2.bin
firmware:       amdgpu/polaris11_ce.bin
firmware:       amdgpu/polaris10_rlc.bin
firmware:       amdgpu/polaris10_mec2_2.bin
firmware:       amdgpu/polaris10_mec2.bin
firmware:       amdgpu/polaris10_mec_2.bin
firmware:       amdgpu/polaris10_mec.bin
firmware:       amdgpu/polaris10_me_2.bin
firmware:       amdgpu/polaris10_me.bin
firmware:       amdgpu/polaris10_pfp_2.bin
firmware:       amdgpu/polaris10_pfp.bin
firmware:       amdgpu/polaris10_ce_2.bin
firmware:       amdgpu/polaris10_ce.bin
firmware:       amdgpu/fiji_rlc.bin
firmware:       amdgpu/fiji_mec2.bin
firmware:       amdgpu/fiji_mec.bin
firmware:       amdgpu/fiji_me.bin
firmware:       amdgpu/fiji_pfp.bin
firmware:       amdgpu/fiji_ce.bin
firmware:       amdgpu/topaz_rlc.bin
firmware:       amdgpu/topaz_mec.bin
firmware:       amdgpu/topaz_me.bin
firmware:       amdgpu/topaz_pfp.bin
firmware:       amdgpu/topaz_ce.bin
firmware:       amdgpu/tonga_rlc.bin
firmware:       amdgpu/tonga_mec2.bin
firmware:       amdgpu/tonga_mec.bin
firmware:       amdgpu/tonga_me.bin
firmware:       amdgpu/tonga_pfp.bin
firmware:       amdgpu/tonga_ce.bin
firmware:       amdgpu/stoney_rlc.bin
firmware:       amdgpu/stoney_mec.bin
firmware:       amdgpu/stoney_me.bin
firmware:       amdgpu/stoney_pfp.bin
firmware:       amdgpu/stoney_ce.bin
firmware:       amdgpu/carrizo_rlc.bin
firmware:       amdgpu/carrizo_mec2.bin
firmware:       amdgpu/carrizo_mec.bin
firmware:       amdgpu/carrizo_me.bin
firmware:       amdgpu/carrizo_pfp.bin
firmware:       amdgpu/carrizo_ce.bin
firmware:       amdgpu/renoir_rlc.bin
firmware:       amdgpu/renoir_mec2.bin
firmware:       amdgpu/renoir_mec.bin
firmware:       amdgpu/renoir_me.bin
firmware:       amdgpu/renoir_pfp.bin
firmware:       amdgpu/renoir_ce.bin
firmware:       amdgpu/arcturus_rlc.bin
firmware:       amdgpu/arcturus_mec2.bin
firmware:       amdgpu/arcturus_mec.bin
firmware:       amdgpu/raven_kicker_rlc.bin
firmware:       amdgpu/raven2_rlc.bin
firmware:       amdgpu/raven2_mec2.bin
firmware:       amdgpu/raven2_mec.bin
firmware:       amdgpu/raven2_me.bin
firmware:       amdgpu/raven2_pfp.bin
firmware:       amdgpu/raven2_ce.bin
firmware:       amdgpu/picasso_rlc_am4.bin
firmware:       amdgpu/picasso_rlc.bin
firmware:       amdgpu/picasso_mec2.bin
firmware:       amdgpu/picasso_mec.bin
firmware:       amdgpu/picasso_me.bin
firmware:       amdgpu/picasso_pfp.bin
firmware:       amdgpu/picasso_ce.bin
firmware:       amdgpu/raven_rlc.bin
firmware:       amdgpu/raven_mec2.bin
firmware:       amdgpu/raven_mec.bin
firmware:       amdgpu/raven_me.bin
firmware:       amdgpu/raven_pfp.bin
firmware:       amdgpu/raven_ce.bin
firmware:       amdgpu/vega20_rlc.bin
firmware:       amdgpu/vega20_mec2.bin
firmware:       amdgpu/vega20_mec.bin
firmware:       amdgpu/vega20_me.bin
firmware:       amdgpu/vega20_pfp.bin
firmware:       amdgpu/vega20_ce.bin
firmware:       amdgpu/vega12_rlc.bin
firmware:       amdgpu/vega12_mec2.bin
firmware:       amdgpu/vega12_mec.bin
firmware:       amdgpu/vega12_me.bin
firmware:       amdgpu/vega12_pfp.bin
firmware:       amdgpu/vega12_ce.bin
firmware:       amdgpu/vega10_rlc.bin
firmware:       amdgpu/vega10_mec2.bin
firmware:       amdgpu/vega10_mec.bin
firmware:       amdgpu/vega10_me.bin
firmware:       amdgpu/vega10_pfp.bin
firmware:       amdgpu/vega10_ce.bin
firmware:       amdgpu/navi12_rlc.bin
firmware:       amdgpu/navi12_mec2.bin
firmware:       amdgpu/navi12_mec.bin
firmware:       amdgpu/navi12_me.bin
firmware:       amdgpu/navi12_pfp.bin
firmware:       amdgpu/navi12_ce.bin
firmware:       amdgpu/navi14_rlc.bin
firmware:       amdgpu/navi14_mec2.bin
firmware:       amdgpu/navi14_mec.bin
firmware:       amdgpu/navi14_me.bin
firmware:       amdgpu/navi14_pfp.bin
firmware:       amdgpu/navi14_ce.bin
firmware:       amdgpu/navi14_mec2_wks.bin
firmware:       amdgpu/navi14_mec_wks.bin
firmware:       amdgpu/navi14_me_wks.bin
firmware:       amdgpu/navi14_pfp_wks.bin
firmware:       amdgpu/navi14_ce_wks.bin
firmware:       amdgpu/navi10_rlc.bin
firmware:       amdgpu/navi10_mec2.bin
firmware:       amdgpu/navi10_mec.bin
firmware:       amdgpu/navi10_me.bin
firmware:       amdgpu/navi10_pfp.bin
firmware:       amdgpu/navi10_ce.bin
firmware:       amdgpu/topaz_sdma1.bin
firmware:       amdgpu/topaz_sdma.bin
firmware:       amdgpu/vegam_sdma1.bin
firmware:       amdgpu/vegam_sdma.bin
firmware:       amdgpu/polaris12_sdma1.bin
firmware:       amdgpu/polaris12_sdma.bin
firmware:       amdgpu/polaris11_sdma1.bin
firmware:       amdgpu/polaris11_sdma.bin
firmware:       amdgpu/polaris10_sdma1.bin
firmware:       amdgpu/polaris10_sdma.bin
firmware:       amdgpu/stoney_sdma.bin
firmware:       amdgpu/fiji_sdma1.bin
firmware:       amdgpu/fiji_sdma.bin
firmware:       amdgpu/carrizo_sdma1.bin
firmware:       amdgpu/carrizo_sdma.bin
firmware:       amdgpu/tonga_sdma1.bin
firmware:       amdgpu/tonga_sdma.bin
firmware:       amdgpu/renoir_sdma.bin
firmware:       amdgpu/arcturus_sdma.bin
firmware:       amdgpu/raven2_sdma.bin
firmware:       amdgpu/picasso_sdma.bin
firmware:       amdgpu/raven_sdma.bin
firmware:       amdgpu/vega20_sdma1.bin
firmware:       amdgpu/vega20_sdma.bin
firmware:       amdgpu/vega12_sdma1.bin
firmware:       amdgpu/vega12_sdma.bin
firmware:       amdgpu/vega10_sdma1.bin
firmware:       amdgpu/vega10_sdma.bin
firmware:       amdgpu/navi12_sdma1.bin
firmware:       amdgpu/navi12_sdma.bin
firmware:       amdgpu/navi14_sdma1.bin
firmware:       amdgpu/navi14_sdma.bin
firmware:       amdgpu/navi10_sdma1.bin
firmware:       amdgpu/navi10_sdma.bin
firmware:       amdgpu/navi10_mes.bin
firmware:       amdgpu/vega20_uvd.bin
firmware:       amdgpu/vega12_uvd.bin
firmware:       amdgpu/vega10_uvd.bin
firmware:       amdgpu/vegam_uvd.bin
firmware:       amdgpu/polaris12_uvd.bin
firmware:       amdgpu/polaris11_uvd.bin
firmware:       amdgpu/polaris10_uvd.bin
firmware:       amdgpu/stoney_uvd.bin
firmware:       amdgpu/fiji_uvd.bin
firmware:       amdgpu/carrizo_uvd.bin
firmware:       amdgpu/tonga_uvd.bin
firmware:       amdgpu/mullins_uvd.bin
firmware:       amdgpu/hawaii_uvd.bin
firmware:       amdgpu/kaveri_uvd.bin
firmware:       amdgpu/kabini_uvd.bin
firmware:       amdgpu/bonaire_uvd.bin
firmware:       amdgpu/vega20_vce.bin
firmware:       amdgpu/vega12_vce.bin
firmware:       amdgpu/vega10_vce.bin
firmware:       amdgpu/vegam_vce.bin
firmware:       amdgpu/polaris12_vce.bin
firmware:       amdgpu/polaris11_vce.bin
firmware:       amdgpu/polaris10_vce.bin
firmware:       amdgpu/stoney_vce.bin
firmware:       amdgpu/fiji_vce.bin
firmware:       amdgpu/carrizo_vce.bin
firmware:       amdgpu/tonga_vce.bin
firmware:       amdgpu/mullins_vce.bin
firmware:       amdgpu/hawaii_vce.bin
firmware:       amdgpu/kaveri_vce.bin
firmware:       amdgpu/kabini_vce.bin
firmware:       amdgpu/bonaire_vce.bin
firmware:       amdgpu/navi12_vcn.bin
firmware:       amdgpu/navi14_vcn.bin
firmware:       amdgpu/navi10_vcn.bin
firmware:       amdgpu/renoir_vcn.bin
firmware:       amdgpu/arcturus_vcn.bin
firmware:       amdgpu/raven2_vcn.bin
firmware:       amdgpu/picasso_vcn.bin
firmware:       amdgpu/raven_vcn.bin
firmware:       amdgpu/vega20_smc.bin
firmware:       amdgpu/vega12_smc.bin
firmware:       amdgpu/vega10_acg_smc.bin
firmware:       amdgpu/vega10_smc.bin
firmware:       amdgpu/vegam_smc.bin
firmware:       amdgpu/polaris12_k_smc.bin
firmware:       amdgpu/polaris12_smc.bin
firmware:       amdgpu/polaris11_k2_smc.bin
firmware:       amdgpu/polaris11_k_smc.bin
firmware:       amdgpu/polaris11_smc_sk.bin
firmware:       amdgpu/polaris11_smc.bin
firmware:       amdgpu/polaris10_k2_smc.bin
firmware:       amdgpu/polaris10_k_smc.bin
firmware:       amdgpu/polaris10_smc_sk.bin
firmware:       amdgpu/polaris10_smc.bin
firmware:       amdgpu/fiji_smc.bin
firmware:       amdgpu/tonga_k_smc.bin
firmware:       amdgpu/tonga_smc.bin
firmware:       amdgpu/topaz_k_smc.bin
firmware:       amdgpu/topaz_smc.bin
firmware:       amdgpu/hawaii_k_smc.bin
firmware:       amdgpu/hawaii_smc.bin
firmware:       amdgpu/bonaire_k_smc.bin
firmware:       amdgpu/bonaire_smc.bin
firmware:       amdgpu/navi12_smc.bin
firmware:       amdgpu/navi14_smc.bin
firmware:       amdgpu/navi10_smc.bin
firmware:       amdgpu/arcturus_smc.bin
firmware:       amdgpu/vega20_smc.bin
firmware:       amdgpu/raven_dmcu.bin
firmware:       amdgpu/renoir_dmcub.bin
srcversion:     533BB7E5866E52F63B9ACCB
alias:          pci:v00001002d00007362sv*sd*bc*sc*i*
alias:          pci:v00001002d00007360sv*sd*bc*sc*i*
alias:          pci:v00001002d00001636sv*sd*bc*sc*i*
alias:          pci:v00001002d0000734Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00007347sv*sd*bc*sc*i*
alias:          pci:v00001002d00007341sv*sd*bc*sc*i*
alias:          pci:v00001002d00007340sv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Asv*sd*bc*sc*i*
alias:          pci:v00001002d00007319sv*sd*bc*sc*i*
alias:          pci:v00001002d00007318sv*sd*bc*sc*i*
alias:          pci:v00001002d00007312sv*sd*bc*sc*i*
alias:          pci:v00001002d00007310sv*sd*bc*sc*i*
alias:          pci:v00001002d00007390sv*sd*bc*sc*i*
alias:          pci:v00001002d0000738Esv*sd*bc*sc*i*
alias:          pci:v00001002d00007388sv*sd*bc*sc*i*
alias:          pci:v00001002d0000738Csv*sd*bc*sc*i*
alias:          pci:v00001002d000015D8sv*sd*bc*sc*i*
alias:          pci:v00001002d000015DDsv*sd*bc*sc*i*
alias:          pci:v00001002d000066AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000066A7sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A4sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A0sv*sd*bc*sc*i*
alias:          pci:v00001002d000069AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000069A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000687Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006869sv*sd*bc*sc*i*
alias:          pci:v00001002d00006868sv*sd*bc*sc*i*
alias:          pci:v00001002d00006867sv*sd*bc*sc*i*
alias:          pci:v00001002d00006864sv*sd*bc*sc*i*
alias:          pci:v00001002d00006863sv*sd*bc*sc*i*
alias:          pci:v00001002d00006862sv*sd*bc*sc*i*
alias:          pci:v00001002d00006861sv*sd*bc*sc*i*
alias:          pci:v00001002d00006860sv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000699Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006997sv*sd*bc*sc*i*
alias:          pci:v00001002d00006995sv*sd*bc*sc*i*
alias:          pci:v00001002d00006987sv*sd*bc*sc*i*
alias:          pci:v00001002d00006986sv*sd*bc*sc*i*
alias:          pci:v00001002d00006985sv*sd*bc*sc*i*
alias:          pci:v00001002d00006981sv*sd*bc*sc*i*
alias:          pci:v00001002d00006980sv*sd*bc*sc*i*
alias:          pci:v00001002d00006FDFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CCsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067C9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067DFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067D0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C7sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C4sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C2sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E7sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067FFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067EFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067EBsv*sd*bc*sc*i*
alias:          pci:v00001002d000067E8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E3sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E0sv*sd*bc*sc*i*
alias:          pci:v00001002d000098E4sv*sd*bc*sc*i*
alias:          pci:v00001002d00009877sv*sd*bc*sc*i*
alias:          pci:v00001002d00009876sv*sd*bc*sc*i*
alias:          pci:v00001002d00009875sv*sd*bc*sc*i*
alias:          pci:v00001002d00009874sv*sd*bc*sc*i*
alias:          pci:v00001002d00009870sv*sd*bc*sc*i*
alias:          pci:v00001002d0000730Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00007300sv*sd*bc*sc*i*
alias:          pci:v00001002d00006939sv*sd*bc*sc*i*
alias:          pci:v00001002d00006938sv*sd*bc*sc*i*
alias:          pci:v00001002d00006930sv*sd*bc*sc*i*
alias:          pci:v00001002d0000692Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000692Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00006929sv*sd*bc*sc*i*
alias:          pci:v00001002d00006928sv*sd*bc*sc*i*
alias:          pci:v00001002d00006921sv*sd*bc*sc*i*
alias:          pci:v00001002d00006920sv*sd*bc*sc*i*
alias:          pci:v00001002d00006907sv*sd*bc*sc*i*
alias:          pci:v00001002d00006903sv*sd*bc*sc*i*
alias:          pci:v00001002d00006902sv*sd*bc*sc*i*
alias:          pci:v00001002d00006901sv*sd*bc*sc*i*
alias:          pci:v00001002d00006900sv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Asv*sd*bc*sc*i*
alias:          pci:v00001002d00009859sv*sd*bc*sc*i*
alias:          pci:v00001002d00009858sv*sd*bc*sc*i*
alias:          pci:v00001002d00009857sv*sd*bc*sc*i*
alias:          pci:v00001002d00009856sv*sd*bc*sc*i*
alias:          pci:v00001002d00009855sv*sd*bc*sc*i*
alias:          pci:v00001002d00009854sv*sd*bc*sc*i*
alias:          pci:v00001002d00009853sv*sd*bc*sc*i*
alias:          pci:v00001002d00009852sv*sd*bc*sc*i*
alias:          pci:v00001002d00009851sv*sd*bc*sc*i*
alias:          pci:v00001002d00009850sv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Asv*sd*bc*sc*i*
alias:          pci:v00001002d00009839sv*sd*bc*sc*i*
alias:          pci:v00001002d00009838sv*sd*bc*sc*i*
alias:          pci:v00001002d00009837sv*sd*bc*sc*i*
alias:          pci:v00001002d00009836sv*sd*bc*sc*i*
alias:          pci:v00001002d00009835sv*sd*bc*sc*i*
alias:          pci:v00001002d00009834sv*sd*bc*sc*i*
alias:          pci:v00001002d00009833sv*sd*bc*sc*i*
alias:          pci:v00001002d00009832sv*sd*bc*sc*i*
alias:          pci:v00001002d00009831sv*sd*bc*sc*i*
alias:          pci:v00001002d00009830sv*sd*bc*sc*i*
alias:          pci:v00001002d000067BEsv*sd*bc*sc*i*
alias:          pci:v00001002d000067BAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067B9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067AAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067A9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Csv*sd*bc*sc*i*
alias:          pci:v00001002d00006658sv*sd*bc*sc*i*
alias:          pci:v00001002d00006651sv*sd*bc*sc*i*
alias:          pci:v00001002d00006650sv*sd*bc*sc*i*
alias:          pci:v00001002d00006649sv*sd*bc*sc*i*
alias:          pci:v00001002d00006647sv*sd*bc*sc*i*
alias:          pci:v00001002d00006646sv*sd*bc*sc*i*
alias:          pci:v00001002d00006641sv*sd*bc*sc*i*
alias:          pci:v00001002d00006640sv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00001318sv*sd*bc*sc*i*
alias:          pci:v00001002d00001317sv*sd*bc*sc*i*
alias:          pci:v00001002d00001316sv*sd*bc*sc*i*
alias:          pci:v00001002d00001315sv*sd*bc*sc*i*
alias:          pci:v00001002d00001313sv*sd*bc*sc*i*
alias:          pci:v00001002d00001312sv*sd*bc*sc*i*
alias:          pci:v00001002d00001311sv*sd*bc*sc*i*
alias:          pci:v00001002d00001310sv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Asv*sd*bc*sc*i*
alias:          pci:v00001002d00001309sv*sd*bc*sc*i*
alias:          pci:v00001002d00001307sv*sd*bc*sc*i*
alias:          pci:v00001002d00001306sv*sd*bc*sc*i*
alias:          pci:v00001002d00001305sv*sd*bc*sc*i*
alias:          pci:v00001002d00001304sv*sd*bc*sc*i*
alias:          pci:v00001002d0000666Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006667sv*sd*bc*sc*i*
alias:          pci:v00001002d00006665sv*sd*bc*sc*i*
alias:          pci:v00001002d00006664sv*sd*bc*sc*i*
alias:          pci:v00001002d00006663sv*sd*bc*sc*i*
alias:          pci:v00001002d00006660sv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00006839sv*sd*bc*sc*i*
alias:          pci:v00001002d00006838sv*sd*bc*sc*i*
alias:          pci:v00001002d00006837sv*sd*bc*sc*i*
alias:          pci:v00001002d00006835sv*sd*bc*sc*i*
alias:          pci:v00001002d00006831sv*sd*bc*sc*i*
alias:          pci:v00001002d00006830sv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006829sv*sd*bc*sc*i*
alias:          pci:v00001002d00006828sv*sd*bc*sc*i*
alias:          pci:v00001002d00006827sv*sd*bc*sc*i*
alias:          pci:v00001002d00006826sv*sd*bc*sc*i*
alias:          pci:v00001002d00006825sv*sd*bc*sc*i*
alias:          pci:v00001002d00006824sv*sd*bc*sc*i*
alias:          pci:v00001002d00006823sv*sd*bc*sc*i*
alias:          pci:v00001002d00006822sv*sd*bc*sc*i*
alias:          pci:v00001002d00006821sv*sd*bc*sc*i*
alias:          pci:v00001002d00006820sv*sd*bc*sc*i*
alias:          pci:v00001002d00006631sv*sd*bc*sc*i*
alias:          pci:v00001002d00006623sv*sd*bc*sc*i*
alias:          pci:v00001002d00006621sv*sd*bc*sc*i*
alias:          pci:v00001002d00006620sv*sd*bc*sc*i*
alias:          pci:v00001002d00006617sv*sd*bc*sc*i*
alias:          pci:v00001002d00006613sv*sd*bc*sc*i*
alias:          pci:v00001002d00006611sv*sd*bc*sc*i*
alias:          pci:v00001002d00006610sv*sd*bc*sc*i*
alias:          pci:v00001002d00006608sv*sd*bc*sc*i*
alias:          pci:v00001002d00006607sv*sd*bc*sc*i*
alias:          pci:v00001002d00006606sv*sd*bc*sc*i*
alias:          pci:v00001002d00006605sv*sd*bc*sc*i*
alias:          pci:v00001002d00006604sv*sd*bc*sc*i*
alias:          pci:v00001002d00006603sv*sd*bc*sc*i*
alias:          pci:v00001002d00006602sv*sd*bc*sc*i*
alias:          pci:v00001002d00006601sv*sd*bc*sc*i*
alias:          pci:v00001002d00006600sv*sd*bc*sc*i*
alias:          pci:v00001002d00006819sv*sd*bc*sc*i*
alias:          pci:v00001002d00006818sv*sd*bc*sc*i*
alias:          pci:v00001002d00006817sv*sd*bc*sc*i*
alias:          pci:v00001002d00006816sv*sd*bc*sc*i*
alias:          pci:v00001002d00006811sv*sd*bc*sc*i*
alias:          pci:v00001002d00006810sv*sd*bc*sc*i*
alias:          pci:v00001002d00006809sv*sd*bc*sc*i*
alias:          pci:v00001002d00006808sv*sd*bc*sc*i*
alias:          pci:v00001002d00006806sv*sd*bc*sc*i*
alias:          pci:v00001002d00006802sv*sd*bc*sc*i*
alias:          pci:v00001002d00006801sv*sd*bc*sc*i*
alias:          pci:v00001002d00006800sv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006799sv*sd*bc*sc*i*
alias:          pci:v00001002d00006798sv*sd*bc*sc*i*
alias:          pci:v00001002d00006792sv*sd*bc*sc*i*
alias:          pci:v00001002d00006791sv*sd*bc*sc*i*
alias:          pci:v00001002d00006790sv*sd*bc*sc*i*
alias:          pci:v00001002d0000678Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006788sv*sd*bc*sc*i*
alias:          pci:v00001002d00006784sv*sd*bc*sc*i*
alias:          pci:v00001002d00006780sv*sd*bc*sc*i*
depends:        amdttm,drm_kms_helper,drm,amdkcl,amd_iommu_v2,amd-sched,i2c-algo-bit
retpoline:      Y
name:           amdgpu
vermagic:       4.15.0-60-generic SMP mod_unload 
parm:           vramlimit:Restrict VRAM for testing, in megabytes (int)
parm:           vis_vramlimit:Restrict visible VRAM for testing, in megabytes (int)
parm:           gartsize:Size of GART to setup in megabytes (32, 64, etc., -1=auto) (uint)
parm:           gttsize:Size of the GTT domain in megabytes (-1 = auto) (int)
parm:           moverate:Maximum buffer migration rate in MB/s. (32, 64, etc., -1=auto, 0=1=disabled) (int)
parm:           benchmark:Run benchmark (int)
parm:           test:Run tests (int)
parm:           audio:Audio enable (-1 = auto, 0 = disable, 1 = enable) (int)
parm:           disp_priority:Display Priority (0 = auto, 1 = normal, 2 = high) (int)
parm:           hw_i2c:hw i2c engine enable (0 = disable) (int)
parm:           pcie_gen2:PCIE Gen2 mode (-1 = auto, 0 = disable, 1 = enable) (int)
parm:           msi:MSI support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           lockup_timeout:GPU lockup timeout in ms (default: for bare metal 10000 for non-compute jobs and infinity timeout for compute jobs; for passthrough or sriov, 10000 for all jobs. 0: keep default value. negative: infinity timeout), format: for bare metal [Non-Compute] or [GFX,Compute,SDMA,Video]; for passthrough or sriov [all jobs] or [GFX,Compute,SDMA,Video]. (string)
parm:           dpm:DPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           fw_load_type:firmware loading type (0 = direct, 1 = SMU, 2 = PSP, -1 = auto) (int)
parm:           aspm:ASPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           runpm:PX runtime pm (1 = force enable, 0 = disable, -1 = PX only default) (int)
parm:           ip_block_mask:IP Block Mask (all blocks enabled (default)) (uint)
parm:           bapm:BAPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           deep_color:Deep Color support (1 = enable, 0 = disable (default)) (int)
parm:           vm_size:VM address space size in gigabytes (default 64GB) (int)
parm:           vm_fragment_size:VM fragment size in bits (4, 5, etc. 4 = 64K (default), Max 9 = 2M) (int)
parm:           vm_block_size:VM page table size in bits (default depending on vm_size) (int)
parm:           vm_fault_stop:Stop on VM fault (0 = never (default), 1 = print first, 2 = always) (int)
parm:           vm_debug:Debug VM handling (0 = disabled (default), 1 = enabled) (int)
parm:           vm_update_mode:VM update using CPU (0 = never (default except for large BAR(LB)), 1 = Graphics only, 2 = Compute only (default for LB), 3 = Both (int)
parm:           exp_hw_support:experimental hw support (1 = enable, 0 = disable (default)) (int)
parm:           dc:Display Core driver (1 = enable, 0 = disable, -1 = auto (default)) (int)
parm:           sched_jobs:the max number of jobs supported in the sw queue (default 32) (int)
parm:           sched_hw_submission:the max number of HW submissions (default 2) (int)
parm:           ppfeaturemask:all power features enabled (default)) (uint)
parm:           no_evict:Support pinning request from user space (1 = enable, 0 = disable (default)) (int)
parm:           direct_gma_size:Direct GMA size in megabytes (max 96MB) (int)
parm:           ssg:SSG support (1 = enable, 0 = disable (default)) (int)
parm:           forcelongtraining:force memory long training (uint)
parm:           pcie_gen_cap:PCIE Gen Caps (0: autodetect (default)) (uint)
parm:           pcie_lane_cap:PCIE Lane Caps (0: autodetect (default)) (uint)
parm:           cg_mask:Clockgating flags mask (0 = disable clock gating) (uint)
parm:           pg_mask:Powergating flags mask (0 = disable power gating) (uint)
parm:           sdma_phase_quantum:SDMA context switch phase quantum (x 1K GPU clock cycles, 0 = no change (default 32)) (uint)
parm:           disable_cu:Disable CUs (se.sh.cu,...) (charp)
parm:           virtual_display:Enable virtual display feature (the virtual_display will be set like xxxx:xx:xx.x,x;xxxx:xx:xx.x,x) (charp)
parm:           job_hang_limit:how much time allow a job hang and not drop it (default 0) (int)
parm:           lbpw:Load Balancing Per Watt (LBPW) support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           compute_multipipe:Force compute queues to be spread across pipes (1 = enable, 0 = disable, -1 = auto) (int)
parm:           gpu_recovery:Enable GPU recovery mechanism, (1 = enable, 0 = disable, -1 = auto) (int)
parm:           emu_mode:Emulation mode, (1 = enable, 0 = disable) (int)
parm:           ras_enable:Enable RAS features on the GPU (0 = disable, 1 = enable, -1 = auto (default)) (int)
parm:           ras_mask:Mask of RAS features to enable (default 0xffffffff), only valid when ras_enable == 1 (uint)
parm:           si_support:SI support (1 = enabled (default), 0 = disabled) (int)
parm:           cik_support:CIK support (1 = enabled (default), 0 = disabled) (int)
parm:           smu_memory_pool_size:reserve gtt for smu debug usage, 0 = disable,0x1 = 256Mbyte, 0x2 = 512Mbyte, 0x4 = 1 Gbyte, 0x8 = 2GByte (uint)
parm:           async_gfx_ring:Asynchronous GFX rings that could be configured with either different priorities (HP3D ring and LP3D ring), or equal priorities (0 = disabled, 1 = enabled (default)) (int)
parm:           mcbp:Enable Mid-command buffer preemption (0 = disabled (default), 1 = enabled) (int)
parm:           discovery:Allow driver to discover hardware IPs from IP Discovery table at the top of VRAM (int)
parm:           mes:Enable Micro Engine Scheduler (0 = disabled (default), 1 = enabled) (int)
parm:           noretry:Disable retry faults (0 = retry enabled, 1 = retry disabled (default)) (int)
parm:           force_asic_type:A non negative value used to specify the asic type for all supported GPUs (int)
parm:           sched_policy:Scheduling policy (0 = HWS (Default), 1 = HWS without over-subscription, 2 = Non-HWS (Used for debugging only) (int)
parm:           hws_max_conc_proc:Max # processes HWS can execute concurrently when sched_policy=0 (0 = no concurrency, #VMIDs for KFD = Maximum(default)) (int)
parm:           cwsr_enable:CWSR enable (0 = Off, 1 = On (Default)) (int)
parm:           max_num_of_queues_per_device:Maximum number of supported queues per device (1 = Minimum, 4096 = default) (int)
parm:           send_sigterm:Send sigterm to HSA process on unhandled exception (0 = disable, 1 = enable) (int)
parm:           debug_largebar:Debug large-bar flag used to simulate large-bar capability on non-large bar machine (0 = disable, 1 = enable) (int)
parm:           ignore_crat:Ignore CRAT table during KFD initialization (0 = use CRAT (default), 1 = ignore CRAT) (int)
parm:           halt_if_hws_hang:Halt if HWS hang is detected (0 = off (default), 1 = on) (int)
parm:           hws_gws_support:MEC FW support gws barriers (false = not supported (Default), true = supported) (bool)
parm:           queue_preemption_timeout_ms:queue preemption timeout in ms (1 = Minimum, 9000 = default) (int)
parm:           priv_cp_queues:Enable privileged mode for CP queues (0 = off (default), 1 = on) (int)
parm:           keep_idle_process_evicted:Restore evicted process only if queues are active (N = off(default), Y = on) (bool)
parm:           pcie_p2p:Enable PCIe P2P (requires large-BAR). (N = off, Y = on(default)) (bool)
parm:           dcfeaturemask:all stable DC features enabled (default)) (uint)
parm:           abmlevel:ABM level (0 = off (default), 1-4 = backlight reduction level)  (uint)
parm:           tmz:Enable TMZ feature (-1 = auto, 0 = off (default), 1 = on) (int)
```
```
lspci -n
00:00.0 0600: 8086:6f00 (rev 01)
00:01.0 0604: 8086:6f02 (rev 01)
00:02.0 0604: 8086:6f04 (rev 01)
00:03.0 0604: 8086:6f08 (rev 01)
00:04.0 0880: 8086:6f20 (rev 01)
00:04.1 0880: 8086:6f21 (rev 01)
00:04.2 0880: 8086:6f22 (rev 01)
00:04.3 0880: 8086:6f23 (rev 01)
00:04.4 0880: 8086:6f24 (rev 01)
00:04.5 0880: 8086:6f25 (rev 01)
00:04.6 0880: 8086:6f26 (rev 01)
00:04.7 0880: 8086:6f27 (rev 01)
00:05.0 0880: 8086:6f28 (rev 01)
00:05.1 0880: 8086:6f29 (rev 01)
00:05.2 0880: 8086:6f2a (rev 01)
00:05.4 0800: 8086:6f2c (rev 01)
00:11.0 ff00: 8086:8d7c (rev 05)
00:11.4 0106: 8086:8d62 (rev 05)
00:14.0 0c03: 8086:8d31 (rev 05)
00:16.0 0780: 8086:8d3a (rev 05)
00:16.1 0780: 8086:8d3b (rev 05)
00:1a.0 0c03: 8086:8d2d (rev 05)
00:1c.0 0604: 8086:8d10 (rev d5)
00:1c.2 0604: 8086:8d14 (rev d5)
00:1c.4 0604: 8086:8d18 (rev d5)
00:1d.0 0c03: 8086:8d26 (rev 05)
00:1f.0 0601: 8086:8d44 (rev 05)
00:1f.2 0106: 8086:8d02 (rev 05)
00:1f.3 0c05: 8086:8d22 (rev 05)
02:00.0 0604: 1022:1470 (rev c3)
03:00.0 0604: 1022:1471
04:00.0 0300: 1002:687f (rev c3)
04:00.1 0403: 1002:aaf8
05:00.0 0380: 1002:67a0
07:00.0 0604: 1a03:1150 (rev 03)
08:00.0 0300: 1a03:2000 (rev 30)
09:00.0 0200: 8086:1521 (rev 01)
09:00.1 0200: 8086:1521 (rev 01)
ff:0b.0 0880: 8086:6f81 (rev 01)
ff:0b.1 1101: 8086:6f36 (rev 01)
ff:0b.2 1101: 8086:6f37 (rev 01)
ff:0b.3 0880: 8086:6f76 (rev 01)
ff:0c.0 0880: 8086:6fe0 (rev 01)
ff:0c.1 0880: 8086:6fe1 (rev 01)
ff:0c.2 0880: 8086:6fe2 (rev 01)
ff:0c.3 0880: 8086:6fe3 (rev 01)
ff:0c.4 0880: 8086:6fe4 (rev 01)
ff:0c.5 0880: 8086:6fe5 (rev 01)
ff:0c.6 0880: 8086:6fe6 (rev 01)
ff:0c.7 0880: 8086:6fe7 (rev 01)
ff:0f.0 0880: 8086:6ff8 (rev 01)
ff:0f.1 0880: 8086:6ff9 (rev 01)
ff:0f.4 0880: 8086:6ffc (rev 01)
ff:0f.5 0880: 8086:6ffd (rev 01)
ff:0f.6 0880: 8086:6ffe (rev 01)
ff:10.0 0880: 8086:6f1d (rev 01)
ff:10.1 1101: 8086:6f34 (rev 01)
ff:10.5 0880: 8086:6f1e (rev 01)
ff:10.6 1101: 8086:6f7d (rev 01)
ff:10.7 0880: 8086:6f1f (rev 01)
ff:12.0 0880: 8086:6fa0 (rev 01)
ff:12.1 1101: 8086:6f30 (rev 01)
ff:13.0 0880: 8086:6fa8 (rev 01)
ff:13.1 0880: 8086:6f71 (rev 01)
ff:13.2 0880: 8086:6faa (rev 01)
ff:13.3 0880: 8086:6fab (rev 01)
ff:13.4 0880: 8086:6fac (rev 01)
ff:13.5 0880: 8086:6fad (rev 01)
ff:13.6 0880: 8086:6fae (rev 01)
ff:13.7 0880: 8086:6faf (rev 01)
ff:14.0 0880: 8086:6fb0 (rev 01)
ff:14.1 0880: 8086:6fb1 (rev 01)
ff:14.2 0880: 8086:6fb2 (rev 01)
ff:14.3 0880: 8086:6fb3 (rev 01)
ff:14.4 0880: 8086:6fbc (rev 01)
ff:14.5 0880: 8086:6fbd (rev 01)
ff:14.6 0880: 8086:6fbe (rev 01)
ff:14.7 0880: 8086:6fbf (rev 01)
ff:15.0 0880: 8086:6fb4 (rev 01)
ff:15.1 0880: 8086:6fb5 (rev 01)
ff:15.2 0880: 8086:6fb6 (rev 01)
ff:15.3 0880: 8086:6fb7 (rev 01)
ff:16.0 0880: 8086:6f68 (rev 01)
ff:16.6 0880: 8086:6f6e (rev 01)
ff:16.7 0880: 8086:6f6f (rev 01)
ff:17.0 0880: 8086:6fd0 (rev 01)
ff:17.4 0880: 8086:6fb8 (rev 01)
ff:17.5 0880: 8086:6fb9 (rev 01)
ff:17.6 0880: 8086:6fba (rev 01)
ff:17.7 0880: 8086:6fbb (rev 01)
ff:1e.0 0880: 8086:6f98 (rev 01)
ff:1e.1 0880: 8086:6f99 (rev 01)
ff:1e.2 0880: 8086:6f9a (rev 01)
ff:1e.3 0880: 8086:6fc0 (rev 01)
ff:1e.4 0880: 8086:6f9c (rev 01)
ff:1f.0 0880: 8086:6f88 (rev 01)
ff:1f.2 0880: 8086:6f8a (rev 01)
```
```
lspci -t
-+-[0000:ff]-+-0b.0
 |           +-0b.1
 |           +-0b.2
 |           +-0b.3
 |           +-0c.0
 |           +-0c.1
 |           +-0c.2
 |           +-0c.3
 |           +-0c.4
 |           +-0c.5
 |           +-0c.6
 |           +-0c.7
 |           +-0f.0
 |           +-0f.1
 |           +-0f.4
 |           +-0f.5
 |           +-0f.6
 |           +-10.0
 |           +-10.1
 |           +-10.5
 |           +-10.6
 |           +-10.7
 |           +-12.0
 |           +-12.1
 |           +-13.0
 |           +-13.1
 |           +-13.2
 |           +-13.3
 |           +-13.4
 |           +-13.5
 |           +-13.6
 |           +-13.7
 |           +-14.0
 |           +-14.1
 |           +-14.2
 |           +-14.3
 |           +-14.4
 |           +-14.5
 |           +-14.6
 |           +-14.7
 |           +-15.0
 |           +-15.1
 |           +-15.2
 |           +-15.3
 |           +-16.0
 |           +-16.6
 |           +-16.7
 |           +-17.0
 |           +-17.4
 |           +-17.5
 |           +-17.6
 |           +-17.7
 |           +-1e.0
 |           +-1e.1
 |           +-1e.2
 |           +-1e.3
 |           +-1e.4
 |           +-1f.0
 |           \-1f.2
 \-[0000:00]-+-00.0
             +-01.0-[01]--
             +-02.0-[02-04]----00.0-[03-04]----00.0-[04]--+-00.0
             |                                            \-00.1
             +-03.0-[05]----00.0
             +-04.0
             +-04.1
             +-04.2
             +-04.3
             +-04.4
             +-04.5
             +-04.6
             +-04.7
             +-05.0
             +-05.1
             +-05.2
             +-05.4
             +-11.0
             +-11.4
             +-14.0
             +-16.0
             +-16.1
             +-1a.0
             +-1c.0-[06]--
             +-1c.2-[07-08]----00.0-[08]----00.0
             +-1c.4-[09]--+-00.0
             |            \-00.1
             +-1d.0
             +-1f.0
             +-1f.2
             \-1f.3
```