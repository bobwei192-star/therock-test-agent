# [Issue]: *ERROR* MES failed to response msg=3

- **Issue #:** 3265
- **State:** closed
- **Created:** 2024-06-07T00:00:53Z
- **Updated:** 2024-07-23T14:06:59Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 XTX, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3265

### Problem Description

Running Stable Diffusion on Radeon 7900XTX regularly crashes display driver, filling screen with tiling, colored static. System becomes unresponsive; I am unable to recover Wayland/X, and unable to access TTY plain-text terminals. However, I am able to reboot with alt+sysreq+REISUB.

Graphics card works fine for gaming, including during graphically-intensive games (such as Cyberpunk 2077).

An excerpt from one of the '/var/log/messages' is shown below under 'Additional Information'.

I have tried ROCm 6.0.0 from Fedora 40 and ROCm 6.1.0 from Fedora Rawhide. I have tried reinstalling Fedora from known good media twice.

### Operating System

Fedora Linux 40 (KDE Plasma)

### CPU

Intel(R) Core(TM) i7-8086K CPU @ 4.00GHz

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.1.0, ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

1. Start any stable diffusion process (Automatic1111, ComfyUI).
2. Open UI (ie through Firefox, Chromium, etc)
3. Run one or more tasks.
4. Display driver crashes, sometimes on first task, otherwise on second or third. (System recoverable only through hard reboot or 'alt + SysReq + REISUB').

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
Runtime Ext Version:     1.4
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
  Name:                    Intel(R) Core(TM) i7-8086K CPU @ 4.00GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i7-8086K CPU @ 4.00GHz
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
  Max Clock Freq. (MHz):   5000                               
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
      Size:                    32785016(0x1f44278) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32785016(0x1f44278) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32785016(0x1f44278) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-4370ae80e03b5ed9               
  Marketing Name:          AMD Radeon RX 7900 XTX             
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
  Max Clock Freq. (MHz):   2304                               
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
  Packet Processor uCode:: 102                                
  SDMA engine uCode::      20                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB             
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

### Additional Information

Originally reported here: https://discussion.fedoraproject.org/t/how-to-stop-display-from-crashing-when-using-rocm/118041

/var/log/messages from one crash includes this at time of crash:

```
May 26 18:09:55 fedora kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
May 26 18:09:55 fedora kernel: amdgpu 0000:03:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1006
May 26 18:09:55 fedora kernel: amdgpu 0000:03:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
May 26 18:09:55 fedora kernel: amdgpu 0000:03:00.0: amdgpu: Failed to evict queue 5
May 26 18:09:55 fedora kernel: amdgpu: Failed to evict process queues
May 26 18:09:55 fedora kernel: amdgpu: Failed to quiesce KFD
May 26 18:09:55 fedora kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset begin!
May 26 18:09:55 fedora kwin_wayland[2209]: kwin_scene_opengl: A graphics reset not attributable to the current GL context occurred.
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: IP block:gfx_v11_0 is hung!
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:169 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00040B53
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 Faulty UTCL2 client ID: CPC (0x5)
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 MORE_FAULTS: 0x1
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 WALKER_ERROR: 0x1
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 PERMISSION_FAULTS: 0x5
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 MAPPING_ERROR: 0x1
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 RW: 0x1
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:169 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 Faulty UTCL2 client ID: CB/DB (0x0)
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 MORE_FAULTS: 0x0
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 WALKER_ERROR: 0x0
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 PERMISSION_FAULTS: 0x0
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 MAPPING_ERROR: 0x0
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: #011 RW: 0x0
May 26 18:09:57 fedora kernel: [drm] kiq ring mec 3 pipe 1 q 0
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: recover vram bo from shadow start
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: recover vram bo from shadow done
May 26 18:09:57 fedora kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset(1) succeeded!
```

…followed by a massive amount of repeating…

```
May 26 18:09:57 fedora kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=14
May 26 18:09:57 fedora kernel: [drm:amdgpu_mes_reg_write_reg_wait [amdgpu]] *ERROR* failed to reg_write_reg_wait
```

...until reboot. Note that it reports that GPU reset succeeded, but Wayland/X will not recover, and TTY plain-text terminals are inaccessible.