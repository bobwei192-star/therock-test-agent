# [Issue]: [Bug] Strix Halo (gfx1151): Stuck in Low Power/Idle Clocks & VRAM Reporting Underflow (ROCm 7.1 / Kernel 6.14)

- **Issue #:** 5750
- **State:** closed
- **Created:** 2025-12-08T19:00:46Z
- **Updated:** 2026-01-14T15:05:08Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5750

### Problem Description

**System Configuration:**
*   **Hardware:** AMD Ryzen AI Max+ 395 (Strix Halo / gfx1151)
*   **OS:** Ubuntu 24.04 LTS
*   **Kernel:** 6.14.0-36-generic
*   **Driver:** ROCm 7.1.1 DKMS (Driver version 6.16.6)
*   **Boot Args:** `amdgpu.ppfeaturemask=0xffffffff amdgpu.runpm=0 pcie_aspm=off`

**Issue Description:**
On Strix Halo hardware, the dGPU partition (`gfx1151`) fails to enter high-performance power states under compute load. Despite `radeontop` showing high pipeline utilization, clock speeds remain stuck at idle (~800-1000MHz SCLK/MCLK), resulting in severely degraded compute performance (e.g., 0.5 t/s on LLM inference).

Additionally, `rocm-smi` reports an integer underflow for VRAM usage, and power profiles (`pp_power_profile_mode`) are missing from sysfs despite `ppfeaturemask` being applied.

**Diagnostic Data (rocm-smi -a):**
*   **Clocks:** Supported max is 2900Mhz, but device is locked at Level 1 (885Mhz).
*   **Power:** Draws ~26W under load (effectively idle/soc overhead).
*   **Memory Reporting:** `VRAM USED: 18446744073709547520` (Underflow).
*   **Features:** `get_power_profiles`, `get_power_cap`, `overdrive` all report "Not supported on the given system".

**Steps Taken:**
1.  Disabled Secure Boot.
2.  Applied `amdgpu.ppfeaturemask=0xffffffff`.
3.  Disabled Runtime PM (`runpm=0`).
4.  Forced CPU Governor to Performance.
5.  Attempted `echo high > /sys/class/drm/card0/device/power_dpm_force_performance_level` (Command accepted, but no change in clocks).

**Logs:**
**System Configuration:**
*   **Hardware:** AMD Ryzen AI Max+ 395 (Strix Halo / gfx1151)
*   **OS:** Ubuntu 24.04 LTS
*   **Kernel:** 6.14.0-36-generic
*   **Driver:** ROCm 7.1.1 DKMS (Driver version 6.16.6)
*   **Boot Args:** `amdgpu.ppfeaturemask=0xffffffff amdgpu.runpm=0 pcie_aspm=off`

**Issue Description:**
On Strix Halo hardware, the dGPU partition (`gfx1151`) fails to enter high-performance power states under compute load. Despite `radeontop` showing high pipeline utilization, clock speeds remain stuck at idle (~800-1000MHz SCLK/MCLK), resulting in severely degraded compute performance (e.g., 0.5 t/s on LLM inference).

Additionally, `rocm-smi` reports an integer underflow for VRAM usage, and power profiles (`pp_power_profile_mode`) are missing from sysfs despite `ppfeaturemask` being applied.

**Diagnostic Data (rocm-smi -a):**
*   **Clocks:** Supported max is 2900Mhz, but device is locked at Level 1 (885Mhz).
*   **Power:** Draws ~26W under load (effectively idle/soc overhead).
*   **Memory Reporting:** `VRAM USED: 18446744073709547520` (Underflow).
*   **Features:** `get_power_profiles`, `get_power_cap`, `overdrive` all report "Not supported on the given system".

**Steps Taken:**
1.  Disabled Secure Boot.
2.  Applied `amdgpu.ppfeaturemask=0xffffffff`.
3.  Disabled Runtime PM (`runpm=0`).
4.  Forced CPU Governor to Performance.
5.  Attempted `echo high > /sys/class/drm/card0/device/power_dpm_force_performance_level` (Command accepted, but no change in clocks).

**Logs:**
[Insert the output of your 'rocm-smi -a' here]

### Operating System

Ubuntu 24.04 LTS

### CPU

AMD Ryzen AI Max+ 395 (Strix Halo / gfx1151)

### GPU

AMD Ryzen AI Max+ 395 (Strix Halo / gfx1151)

### ROCm Version

ROCm 7.1.1 DKMS (Driver version 6.16.6)

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ntennant@magicMax:~$ /opt/rocm/bin/rocminfo --support
ROCk module version 6.16.6 is loaded
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
      Size:                    131009772(0x7cf0cec) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    131009772(0x7cf0cec) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131009772(0x7cf0cec) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131009772(0x7cf0cec) KB            
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
  SDMA engine uCode::      17                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65504884(0x3e78674) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65504884(0x3e78674) KB             
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
      Size:                    131009772(0x7cf0cec) KB            
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
      Size:                    131009772(0x7cf0cec) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***             
ntennant@magicMax:~$ 


### Additional Information

_No response_