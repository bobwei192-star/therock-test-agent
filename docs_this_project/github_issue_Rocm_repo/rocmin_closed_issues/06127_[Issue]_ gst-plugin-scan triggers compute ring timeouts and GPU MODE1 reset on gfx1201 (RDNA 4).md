# [Issue]: gst-plugin-scan triggers compute ring timeouts and GPU MODE1 reset on gfx1201 (RDNA 4)

- **Issue #:** 6127
- **State:** closed
- **Created:** 2026-04-08T03:03:53Z
- **Updated:** 2026-06-15T09:39:16Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6127

### Problem Description

GStreamer's gst-plugin-scan process causes repeated compute ring timeouts, null-pointer page faults, and ultimately a MODE1 GPU reset (with VRAM loss / black screen) when the libgstvaapi.so plugin probes GPU compute queues at login time.                                                                                                                              **Environment:** 
  - OS: Ubuntu 24.04.3 LTS (Noble Numbat)
  - CPU: 12th Gen Intel(R) Core(TM) i5-12600KF
  - GPU: gfx1201 — AMD Radeon AI PRO R9700 (PCI 1002:7551)
  - ROCm: 7.2.0 
  - Kernel: 6.17.0-1012-oem 
  - GStreamer VA-API: gstreamer1.0-vaapi 1.24.2-1                                     
                                                                                                                                                                                              **Observed Behavior**
                                                                                                                                                                                            
  Sequential compute ring timeouts escalate to a full GPU reset:                                                                                                                              
   
  [34.96] ring comp_1.1.0 timeout — Process gst-plugin-scan pid 4087                                                                                                                          
          [gfxhub] page fault (src_id:0 ring:32 vmid:0 pasid:0) addr 0x0000000000000000                                                                                                       
          Ring comp_1.1.0 reset succeeded                                                                                                                                                     
                                                                                                                                                                                              
  [37.00] ring comp_1.0.1 timeout — same process, same null-address page fault                                                                                                                
          Ring comp_1.0.1 reset succeeded                                                                                                                                                     
                                                                                                                                                                                              
  [39.05] ring comp_1.1.1 timeout — same pattern                                                                                                                                              
          Ring comp_1.1.1 reset FAILED
                                                                                                                                                                                              
  [39.78] MODE1 reset
  [40.84] VRAM is lost due to GPU reset!
                                                                                                                                                                                              
Result: black screen / display lockup. If the MODE1 reset succeeds, the desktop eventually recovers. If it doesn't, the system requires a hard reboot.                                      
   


### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

12th Gen Intel(R) Core(TM) i5-12600KF

### GPU

AMD Radeon AI PRO R9700

### ROCm Version

7.2.0 

### ROCm Component

_No response_

### Steps to Reproduce

  1. Boot/login with gstreamer1.0-vaapi installed and libgstvaapi.so present in /usr/lib/x86_64-linux-gnu/gstreamer-1.0/                                                                      
  2. GStreamer's gst-plugin-scan runs automatically to probe hardware codec capabilities
  3. The scanner submits compute work to the GPU that triggers null-pointer page faults                                                                                                       
                                                                                                                                                                                              
The issue is intermittent timing depends on whether gst-plugin-scan hits the GPU before or after the display compositor is fully initialized.        

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

mROCk module version 6.16.13 is loaded
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
  Name:                    12th Gen Intel(R) Core(TM) i5-12600KF
  Uuid:                    CPU-XX                             
  Marketing Name:          12th Gen Intel(R) Core(TM) i5-12600KF
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
  Max Clock Freq. (MHz):   4900                               
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
      Size:                    65628776(0x3e96a68) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65628776(0x3e96a68) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65628776(0x3e96a68) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65628776(0x3e96a68) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-bacdbed38da9cb26               
  Marketing Name:          AMD Radeon AI PRO R9700            
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
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30033(0x7551)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2350                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 128                                
  SDMA engine uCode::      662                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    33406976(0x1fdc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1201         
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
      Name:                    amdgcn-amd-amdhsa--gfx12-generic   
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

  **Workaround**
                                                                                                                                                                                            
  Disabling the GStreamer VA-API plugin resolves the issue:
  sudo mv /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgstvaapi.so /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgstvaapi.so.disabled
                                                                                                                                              
  **Additional Notes**
  - dmesg also shows an SMU firmware version mismatch: driver expects 0x2e, firmware reports 0x32                                                                                             
  - The GPU (gfx1201 / RDNA 4) is relatively new and kernel/mesa driver support
  