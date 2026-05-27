# rocm-smi does not show full clock and voltage information

> **Issue #1715**
> **状态**: closed
> **创建时间**: 2022-03-26T13:17:16Z
> **更新时间**: 2024-02-13T22:38:33Z
> **关闭时间**: 2024-02-13T22:38:33Z
> **作者**: aligirayhanozbay
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1715

## 描述

Despite booting with the `amdgpu.ppfeaturemask=0xffffffff` kernel parameter, I cannot see some clock and voltage related information via `rocm-smi`. I'm using a 6900XT on a X570 motherboard with Ryzen 5900X. Here's the output from `rocm-smi -a` and `rocminfo` - notice the lines saying `ERROR: 15 GPU[0]: od volt: Data (usually from reading a file) was not of the type that was expected`:

```
======================= ROCm System Management Interface =======================
========================= Version of System Component ==========================
Driver version: 5.17.0
================================================================================
====================================== ID ======================================
GPU[0]		: GPU ID: 0x73bf
================================================================================
================================== Unique ID ===================================
GPU[0]		: Unique ID: N/A
================================================================================
==================================== VBIOS =====================================
GPU[0]		: VBIOS version: 113-D4120100-100
================================================================================
================================= Temperature ==================================
GPU[0]		: Temperature (Sensor edge) (C): 52.0
GPU[0]		: Temperature (Sensor junction) (C): 57.0
GPU[0]		: Temperature (Sensor memory) (C): 58.0
GPU[0]		: Temperature (Sensor HBM 0) (C): N/A
GPU[0]		: Temperature (Sensor HBM 1) (C): N/A
GPU[0]		: Temperature (Sensor HBM 2) (C): N/A
GPU[0]		: Temperature (Sensor HBM 3) (C): N/A
================================================================================
========================== Current clock frequencies ===========================
GPU[0]		: dcefclk clock level: 1: (960Mhz)
GPU[0]		: fclk clock level: 1: (1296Mhz)
GPU[0]		: mclk clock level: 3: (1000Mhz)
GPU[0]		: sclk clock level: 0: (500Mhz)
GPU[0]		: socclk clock level: 1: (800Mhz)
GPU[0]		: pcie clock level: 1 (16.0GT/s x16)
================================================================================
============================== Current Fan Metric ==============================
GPU[0]		: Fan Level: 63 (25%)
GPU[0]		: Fan RPM: 570
================================================================================
============================ Show Performance Level ============================
GPU[0]		: Performance Level: auto
================================================================================
=============================== OverDrive Level ================================
GPU[0]		: GPU OverDrive value (%): 0
================================================================================
=============================== OverDrive Level ================================
GPU[0]		: GPU Memory OverDrive value (%): 0
================================================================================
================================== Power Cap ===================================
GPU[0]		: Max Graphics Package Power (W): 293.0
================================================================================
============================= Show Power Profiles ==============================
GPU[0]		: 1. Available power profile (#1 of 7): CUSTOM
GPU[0]		: 2. Available power profile (#2 of 7): VIDEO
GPU[0]		: 3. Available power profile (#3 of 7): POWER SAVING
GPU[0]		: 4. Available power profile (#4 of 7): COMPUTE
GPU[0]		: 5. Available power profile (#5 of 7): VR
GPU[0]		: 6. Available power profile (#6 of 7): 3D FULL SCREEN
GPU[0]		: 7. Available power profile (#7 of 7): BOOTUP DEFAULT*
================================================================================
============================== Power Consumption ===============================
GPU[0]		: Average Graphics Package Power (W): 38.0
================================================================================
========================= Supported clock frequencies ==========================
GPU[0]		: Supported dcefclk frequencies on GPU0
GPU[0]		: 0: 417Mhz
GPU[0]		: 1: 960Mhz *
GPU[0]		: 2: 1200Mhz
GPU[0]		: 
GPU[0]		: Supported fclk frequencies on GPU0
GPU[0]		: 0: 500Mhz
GPU[0]		: 1: 1296Mhz *
GPU[0]		: 2: 1941Mhz
GPU[0]		: 
GPU[0]		: Supported mclk frequencies on GPU0
GPU[0]		: 0: 96Mhz
GPU[0]		: 1: 456Mhz
GPU[0]		: 2: 673Mhz
GPU[0]		: 3: 1000Mhz *
GPU[0]		: 
GPU[0]		: Supported sclk frequencies on GPU0
GPU[0]		: 0: 500Mhz *
GPU[0]		: 1: 2660Mhz
GPU[0]		: 
GPU[0]		: Supported socclk frequencies on GPU0
GPU[0]		: 0: 480Mhz
GPU[0]		: 1: 800Mhz *
GPU[0]		: 2: 1200Mhz
GPU[0]		: 
GPU[0]		: Supported PCIe frequencies on GPU0
GPU[0]		: 0: 2.5GT/s x1
GPU[0]		: 1: 16.0GT/s x16 *
GPU[0]		: 
--------------------------------------------------------------------------------
================================================================================
============================== % time GPU is busy ==============================
GPU[0]		: GPU use (%): 0
GPU[0]		: GFX Activity: N/A
================================================================================
============================== Current Memory Use ==============================
GPU[0]		: GPU memory use (%): 11
GPU[0]		: Memory Activity: N/A
================================================================================
================================ Memory Vendor =================================
GPU[0]		: GPU memory vendor: samsung
================================================================================
============================= PCIe Replay Counter ==============================
GPU[0]		: PCIe Replay Count: 0
================================================================================
================================ Serial Number =================================
GPU[0]		: Serial Number: N/A
================================================================================
================================ KFD Processes =================================
No KFD PIDs currently running
================================================================================
============================= GPUs Indexed by PID ==============================
No KFD PIDs currently running
================================================================================
================== GPU Memory clock frequencies and voltages ===================
ERROR: 15 GPU[0]: od volt: Data (usually from reading a file) was not of the type that was expected	
================================================================================
=============================== Current voltage ================================
GPU[0]		: Voltage (mV): 775
================================================================================
================================== PCI Bus ID ==================================
GPU[0]		: PCI Bus: 0000:2F:00.0
================================================================================
============================= Firmware Information =============================
GPU[0]		: ASD firmware version: 	553648218
GPU[0]		: CE firmware version: 		36
GPU[0]		: DMCU firmware version: 	0
GPU[0]		: MC firmware version: 		0
GPU[0]		: ME firmware version: 		62
GPU[0]		: MEC firmware version: 	88
GPU[0]		: MEC2 firmware version: 	88
GPU[0]		: PFP firmware version: 	86
GPU[0]		: RLC firmware version: 	91
GPU[0]		: RLC SRLC firmware version: 	0
GPU[0]		: RLC SRLG firmware version: 	0
GPU[0]		: RLC SRLS firmware version: 	0
GPU[0]		: SDMA firmware version: 	76
GPU[0]		: SDMA2 firmware version: 	76
GPU[0]		: SMC firmware version: 	00.58.71.00
GPU[0]		: SOS firmware version: 	0x00210862
GPU[0]		: TA RAS firmware version: 	27.00.01.42
GPU[0]		: TA XGMI firmware version: 	32.00.00.11
GPU[0]		: UVD firmware version: 	0x00000000
GPU[0]		: VCE firmware version: 	0x00000000
GPU[0]		: VCN firmware version: 	0x0210d02a
================================================================================
================================= Product Info =================================
GPU[0]		: Card series: 		Navi 21 [Radeon RX 6800/6800 XT / 6900 XT]
GPU[0]		: Card model: 		Radeon RX 6900 XT
GPU[0]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]		: Card SKU: 		D41201
================================================================================
================================== Pages Info ==================================
ERROR: 2 GPU[0]: ras: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.	
============================ Show Valid sclk Range =============================
ERROR: 15 GPU[0]: od volt: Data (usually from reading a file) was not of the type that was expected	
GPU[0]		: Unable to display sclk range
================================================================================
============================ Show Valid mclk Range =============================
ERROR: 15 GPU[0]: od volt: Data (usually from reading a file) was not of the type that was expected	
GPU[0]		: Unable to display mclk range
================================================================================
=========================== Show Valid voltage Range ===========================
ERROR: 15 GPU[0]: od volt: Data (usually from reading a file) was not of the type that was expected	
GPU[0]		: Unable to display voltage range
================================================================================
============================= Voltage Curve Points =============================
ERROR: 15 GPU[0]: od volt: Data (usually from reading a file) was not of the type that was expected	
GPU[0]		: Voltage Curve is not supported
================================================================================
=============================== Consumed Energy ================================
GPU[0]		: Energy counter: 188012754
GPU[0]		: Accumulated Energy (uJ): 2876595172.06
================================================================================
WARNING:  		 One or more commands failed
============================= End of ROCm SMI Log ==============================
```

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
  Name:                    AMD Ryzen 9 5900X 12-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 5900X 12-Core Processor
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
  Max Clock Freq. (MHz):   5034                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            24                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32861432(0x1f56cf8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32861432(0x1f56cf8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32861432(0x1f56cf8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1030                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 6900 XT              
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
    L2:                      4096(0x1000) KB                    
    L3:                      131072(0x20000) KB                 
  Chip ID:                 29631(0x73bf)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2660                               
  BDFID:                   12032                              
  Internal Node ID:        1                                  
  Compute Unit:            80                                 
  SIMDs per CU:            2                                  
  Shader Engines:          8                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
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
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
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

---

## 评论 (3 条)

### 评论 #1 — MatPoliquin (2022-09-01T18:09:27Z)

I have the same issue but with the RX 6700s (cpu is r7 6800HS)
OpenSuse Tumbleweed, kernel 5.19
ROCm 5.2.3
I have set the same boot parameter in grub and still get same error, the maximum memory clock I can set is 875Mhz

---

### 评论 #2 — abhimeda (2024-01-25T03:31:42Z)

 @aligirayhanozbay Hi, is your issue resolved in the latest ROCm? If so can we close this ticket?

---

### 评论 #3 — nartmada (2024-02-13T22:38:33Z)

Closing the ticket as no response from @aligirayhanozbay.  Please re-open if this issue still exists with latest ROCm 6.0.2.  Thanks.

---
