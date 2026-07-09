# [Issue]: Crash when doing large workloads in ComfyUI

- **Issue #:** 5519
- **State:** closed
- **Created:** 2025-10-15T11:20:13Z
- **Updated:** 2025-10-28T12:33:28Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5519

### Problem Description

AMDGPU crashes with large work loads. I was originally noticing this with torch 2.9.0+rocm7.0 and reverted back to torch 2.8.0+rocm6.4 and had no issues but since upgrading back to 2.9.0+rocm6.4 the issue has returned. 


 

### Operating System

OS: NAME="Linux Mint" VERSION="22.2 (Zara)"

### CPU

 CPU:  model name	: AMD Ryzen 7 5700X3D 8-Core Processor 

### GPU

GPU:   
    Name:                    AMD Ryzen 7 5700X3D 8-Core Processor
    Marketing Name:          AMD Ryzen 7 5700X3D 8-Core Processor
    Name:                    gfx1100                               
    Marketing Name:          Radeon RX 7900 XTX                        
    Name:                    amdgcn-amd-amdhsa--gfx1100               
    Name:                    amdgcn-amd-amdhsa--gfx11-generic

### ROCm Version

ROCM 7.0.2

### ROCm Component

_No response_

### Steps to Reproduce

Originally it was reproduced by https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/t2v_comfyui_radeon.html

but after I switched to https://civitai.com/models/1802623/wan-21-lightspeed the issue was visible again.

I am running ComfyUI with --reserve-vram 4 which seemed to help with the issue

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

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
VMM Support:             NO

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 5700X3D 8-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 5700X3D 8-Core Processor
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
  Max Clock Freq. (MHz):   3000                               
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
      Size:                    32781504(0x1f434c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32781504(0x1f434c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32781504(0x1f434c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32781504(0x1f434c0) KB             
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
  Uuid:                    GPU-d210e43beedf0dd6               
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
  BDFID:                   10240                              
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
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
  Packet Processor uCode:: 550                                
  SDMA engine uCode::      19                                 
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

```
Oct 15 12:05:54 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
Oct 15 12:05:54 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
Oct 15 12:05:54 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
Oct 15 12:05:54 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: Failed to evict queue 1
Oct 15 12:05:54 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: Failed to evict queue 0
Oct 15 12:05:54 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: GPU reset begin!
Oct 15 12:05:54 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: Failed to restore queue 2
Oct 15 12:05:54 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: Failed to restore process queues
Oct 15 12:05:54 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=14
Oct 15 12:05:54 Desktop-Mint kernel: [drm:amdgpu_mes_reg_write_reg_wait [amdgpu]] *ERROR* failed to reg_write_reg_wait
Oct 15 12:05:55 Desktop-Mint NetworkManager[1025]: <warn>  [1760526355.8167] platform-linux: do-add-ip6-address[2: fe80::366d:5b89:363a:c5af]: failure 13 (Permission denied - ipv6: IPv6 is disabled on this device)
Oct 15 12:05:57 Desktop-Mint NetworkManager[1025]: <warn>  [1760526357.8169] platform-linux: do-add-ip6-address[2: fe80::336e:2cac:5026:dfeb]: failure 13 (Permission denied - ipv6: IPv6 is disabled on this device)
Oct 15 12:05:58 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: failed to suspend display audio
Oct 15 12:05:58 Desktop-Mint systemd[1]: Created slice system-systemd\x2dcoredump.slice - Slice /system/systemd-coredump.
Oct 15 12:05:58 Desktop-Mint systemd[1]: Started systemd-coredump@0-10872-0.service - Process Core Dump (PID 10872/UID 0).
Oct 15 12:05:59 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
Oct 15 12:05:59 Desktop-Mint kernel: [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
Oct 15 12:05:59 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
Oct 15 12:05:59 Desktop-Mint kernel: [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
Oct 15 12:05:59 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
Oct 15 12:05:59 Desktop-Mint kernel: [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
Oct 15 12:05:59 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
Oct 15 12:05:59 Desktop-Mint kernel: [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
Oct 15 12:05:59 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
Oct 15 12:05:59 Desktop-Mint kernel: [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
Oct 15 12:05:59 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
Oct 15 12:05:59 Desktop-Mint kernel: [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
Oct 15 12:05:59 Desktop-Mint NetworkManager[1025]: <warn>  [1760526359.8172] platform-linux: do-add-ip6-address[2: fe80::d1ed:c30c:477f:bd7d]: failure 13 (Permission denied - ipv6: IPv6 is disabled on this device)
Oct 15 12:05:59 Desktop-Mint kernel: [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
Oct 15 12:05:59 Desktop-Mint kernel: [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
Oct 15 12:05:59 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: MODE1 reset
Oct 15 12:05:59 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: GPU mode1 reset
Oct 15 12:05:59 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: GPU smu mode1 reset
Oct 15 12:06:00 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: GPU reset succeeded, trying to resume
Oct 15 12:06:00 Desktop-Mint kernel: [drm] PCIE GART of 512M enabled (table at 0x0000008000F00000).
Oct 15 12:06:00 Desktop-Mint kernel: [drm] VRAM is lost due to GPU reset!
Oct 15 12:06:00 Desktop-Mint kernel: [drm] PSP is resuming...
Oct 15 12:06:00 Desktop-Mint kernel: [drm] reserve 0x1300000 from 0x85fc000000 for PSP TMR
Oct 15 12:06:00 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: RAP: optional rap ta ucode is not available
Oct 15 12:06:00 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
Oct 15 12:06:00 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: SMU is resuming...
Oct 15 12:06:00 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: smu driver if version = 0x0000003d, smu fw if version = 0x0000003f, smu fw program = 0, smu fw version = 0x004e7900 (78.121.0)
Oct 15 12:06:00 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: SMU driver if version not matched
Oct 15 12:06:00 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: SMU is resumed successfully!
Oct 15 12:06:00 Desktop-Mint kernel: [drm] DMUB hardware initialized: version=0x07002900
Oct 15 12:06:01 Desktop-Mint kernel: [drm] kiq ring mec 3 pipe 1 q 0
Oct 15 12:06:01 Desktop-Mint kernel: [drm] VCN decode and encode initialized successfully(under DPG Mode).
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: [drm:jpeg_v4_0_hw_init [amdgpu]] JPEG decode initialized successfully.
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring sdma1 uses VM inv eng 13 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring jpeg_dec uses VM inv eng 4 on hub 8
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 14 on hub 0
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: recover vram bo from shadow start
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: recover vram bo from shadow done
Oct 15 12:06:01 Desktop-Mint kernel: amdgpu 0000:28:00.0: amdgpu: GPU reset(1) succeeded!
Oct 15 12:06:01 Desktop-Mint kernel: show_signal_msg: 115 callbacks suppressed
Oct 15 12:06:01 Desktop-Mint kernel: browser 4 :cs0[4002]: segfault at 0 ip 00005a8655d2ee31 sp 000076b83a3fea30 error 6 in firefox-bin[5a8655ccd000+98000] likely on CPU 7 (core 7, socket 0)
Oct 15 12:06:01 Desktop-Mint kernel: Code: 4c 8b 35 0a 7c 03 00 49 8b 36 e8 fa 50 03 00 49 8b 36 bf 0a 00 00 00 e8 0d 52 03 00 48 89 1d 96 b7 03 00 31 c0 b9 23 00 00 00 <48> 89 08 e8 e7 84 fb ff cc cc cc cc cc cc cc 48 83 ec 38 0f 28 05
Oct 15 12:06:01 Desktop-Mint systemd[1]: Started systemd-coredump@1-10881-0.service - Process Core Dump (PID 10881/UID 0).
Oct 15 12:06:01 Desktop-Mint NetworkManager[1025]: <warn>  [1760526361.8173] ipv6ll[bafc422a1561043a,ifindex=2]: changed: no IPv6 link local address to retry after Duplicate Address Detection failures (back off)
Oct 15 12:06:03 Desktop-Mint systemd-coredump[10882]: [🡕] Process 3233 (RDD Process) of user 1000 dumped core.
                                                      
                                                      Module libgomp.so.1 from deb gcc-14-14.2.0-4ubuntu2~24.04.amd64
                                                      Module libzstd.so.1 from deb libzstd-1.5.5+dfsg2-2build1.1.amd64
                                                      Module libsystemd.so.0 from deb systemd-255.4-1ubuntu8.11.amd64
                                                      Module libgcc_s.so.1 from deb gcc-14-14.2.0-4ubuntu2~24.04.amd64
                                                      Module libstdc++.so.6 from deb gcc-14-14.2.0-4ubuntu2~24.04.amd64
                                                      Stack trace of thread 4002:
                                                      #0  0x00005a8655d2ee31 mozalloc_abort (firefox-bin + 0x86e31)
                                                      #1  0x00005a8655ce732d abort (firefox-bin + 0x3f32d)
                                                      #2  0x000076b843844270 n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0xa44270)
                                                      #3  0x000076b843849246 n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0xa49246)
                                                      #4  0x000076b843360621 n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x560621)
                                                      #5  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #6  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #7  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #8  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 3233:
                                                      #0  0x000076b86331b4fd __GI___poll (libc.so.6 + 0x11b4fd)
                                                      #1  0x000076b85dee001b n/a (libxul.so + 0x7ce001b)
                                                      #2  0x000076b86187868e n/a (libglib-2.0.so.0 + 0xbc68e)
                                                      #3  0x000076b861818a63 g_main_context_iteration (libglib-2.0.so.0 + 0x5ca63)
                                                      #4  0x000076b859b4e8cb n/a (libxul.so + 0x394e8cb)
                                                      #5  0x000076b859b4cee3 n/a (libxul.so + 0x394cee3)
                                                      #6  0x000076b85b2743da n/a (libxul.so + 0x50743da)
                                                      #7  0x000076b85b2741ea n/a (libxul.so + 0x50741ea)
                                                      #8  0x000076b85b27410d n/a (libxul.so + 0x507410d)
                                                      #9  0x000076b85aff031a n/a (libxul.so + 0x4df031a)
                                                      #10 0x00005a8655d22869 n/a (firefox-bin + 0x7a869)
                                                      #11 0x000076b86322a1ca __libc_start_call_main (libc.so.6 + 0x2a1ca)
                                                      #12 0x000076b86322a28b __libc_start_main_impl (libc.so.6 + 0x2a28b)
                                                      #13 0x00005a8655d26e22 _start (firefox-bin + 0x7ee22)
                                                      
                                                      Stack trace of thread 3236:
                                                      #0  0x000076b86331baca __GI___libc_read (libc.so.6 + 0x11baca)
                                                      #1  0x000076b85acf5cda n/a (libxul.so + 0x4af5cda)
                                                      #2  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #3  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #4  0x000076b863329c6c __clone3 (libc.so.6 + 0x129c6c)
                                                      
                                                      Stack trace of thread 3238:
                                                      #0  0x000076b86332728d syscall (libc.so.6 + 0x12728d)
                                                      #1  0x000076b85a15b314 n/a (libxul.so + 0x3f5b314)
                                                      #2  0x000076b85a159e52 n/a (libxul.so + 0x3f59e52)
                                                      #3  0x000076b85acf634c n/a (libxul.so + 0x4af634c)
                                                      #4  0x000076b85acf6187 n/a (libxul.so + 0x4af6187)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329c6c __clone3 (libc.so.6 + 0x129c6c)
                                                      
                                                      Stack trace of thread 4003:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 3264:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x00005a8655d58d46 _ZN7mozilla6detail21ConditionVariableImpl4waitERNS0_9MutexImplE (firefox-bin + 0xb0d46)
                                                      #3  0x000076b859b4f33d n/a (libxul.so + 0x394f33d)
                                                      #4  0x000076b859b4e0f3 n/a (libxul.so + 0x394e0f3)
                                                      #5  0x000076b85acf97ce n/a (libxul.so + 0x4af97ce)
                                                      #6  0x000076b8638f270f n/a (libnspr4.so + 0x1e70f)
                                                      #7  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #8  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #9  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4021:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 3624:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x00005a8655d58efa _ZN7mozilla6detail21ConditionVariableImpl8wait_forERNS0_9MutexImplERKNS_16BaseTimeDurationINS_27TimeDurationValueCalculatorEEE (firefox-bin + 0xb0efa)
                                                      #3  0x000076b85a504c6f n/a (libxul.so + 0x4304c6f)
                                                      #4  0x000076b859b4fe1d n/a (libxul.so + 0x394fe1d)
                                                      #5  0x000076b859b4e012 n/a (libxul.so + 0x394e012)
                                                      #6  0x000076b85acf97ce n/a (libxul.so + 0x4af97ce)
                                                      #7  0x000076b8638f270f n/a (libnspr4.so + 0x1e70f)
                                                      #8  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #9  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #10 0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4004:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4007:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4006:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4020:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4022:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4023:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4024:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4005:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 10852:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329bc8e __pthread_cond_wait_common (libc.so.6 + 0x9bc8e)
                                                      #2  0x00005a8655d58e7f _ZN7mozilla6detail21ConditionVariableImpl8wait_forERNS0_9MutexImplERKNS_16BaseTimeDurationINS_27TimeDurationValueCalculatorEEE (firefox-bin + 0xb0e7f)
                                                      #3  0x000076b859c46b9d n/a (libxul.so + 0x3a46b9d)
                                                      #4  0x000076b859b4fe1d n/a (libxul.so + 0x394fe1d)
                                                      #5  0x000076b859b4e012 n/a (libxul.so + 0x394e012)
                                                      #6  0x000076b85acf97ce n/a (libxul.so + 0x4af97ce)
                                                      #7  0x000076b8638f270f n/a (libnspr4.so + 0x1e70f)
                                                      #8  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #9  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #10 0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 7042:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 10856:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4025:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 10859:
                                                      #0  0x000076b86332728d syscall (libc.so.6 + 0x12728d)
                                                      #1  0x000076b8433530ca n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5530ca)
                                                      #2  0x000076b8433601bf n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5601bf)
                                                      #3  0x000076b843846d31 n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0xa46d31)
                                                      #4  0x000076b8437ee432 n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x9ee432)
                                                      #5  0x000076b842eff3b3 n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0xff3b3)
                                                      #6  0x000076b84cfd7764 vaEndPicture (libva.so.2 + 0x7764)
                                                      #7  0x000076b84f8021fc n/a (libavcodec.so.60 + 0x8021fc)
                                                      #8  0x000076b84f811617 n/a (libavcodec.so.60 + 0x811617)
                                                      #9  0x000076b84f3c1a47 n/a (libavcodec.so.60 + 0x3c1a47)
                                                      #10 0x000076b84f3d5631 n/a (libavcodec.so.60 + 0x3d5631)
                                                      #11 0x000076b84f2a9a45 n/a (libavcodec.so.60 + 0x2a9a45)
                                                      #12 0x000076b84f2aa044 avcodec_send_packet (libavcodec.so.60 + 0x2aa044)
                                                      #13 0x000076b85d601c4b n/a (libxul.so + 0x7401c4b)
                                                      #14 0x000076b85d5be5a6 n/a (libxul.so + 0x73be5a6)
                                                      #15 0x000076b85d5f95a4 n/a (libxul.so + 0x73f95a4)
                                                      #16 0x000076b85d572bbb n/a (libxul.so + 0x7372bbb)
                                                      #17 0x000076b859c47b96 n/a (libxul.so + 0x3a47b96)
                                                      #18 0x000076b859c46d5f n/a (libxul.so + 0x3a46d5f)
                                                      #19 0x000076b859b4fe1d n/a (libxul.so + 0x394fe1d)
                                                      #20 0x000076b859b4e012 n/a (libxul.so + 0x394e012)
                                                      #21 0x000076b85acf97ce n/a (libxul.so + 0x4af97ce)
                                                      #22 0x000076b8638f270f n/a (libnspr4.so + 0x1e70f)
                                                      #23 0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #24 0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #25 0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4026:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4718:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 4717:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 7043:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 7044:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 7045:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 7046:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 7047:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 10851:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329bc8e __pthread_cond_wait_common (libc.so.6 + 0x9bc8e)
                                                      #2  0x00005a8655d58e7f _ZN7mozilla6detail21ConditionVariableImpl8wait_forERNS0_9MutexImplERKNS_16BaseTimeDurationINS_27TimeDurationValueCalculatorEEE (firefox-bin + 0xb0e7f)
                                                      #3  0x000076b859c46b9d n/a (libxul.so + 0x3a46b9d)
                                                      #4  0x000076b859b4fe1d n/a (libxul.so + 0x394fe1d)
                                                      #5  0x000076b859b4e012 n/a (libxul.so + 0x394e012)
                                                      #6  0x000076b85acf97ce n/a (libxul.so + 0x4af97ce)
                                                      #7  0x000076b8638f270f n/a (libnspr4.so + 0x1e70f)
                                                      #8  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #9  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #10 0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 10853:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329bc8e __pthread_cond_wait_common (libc.so.6 + 0x9bc8e)
                                                      #2  0x00005a8655d58e7f _ZN7mozilla6detail21ConditionVariableImpl8wait_forERNS0_9MutexImplERKNS_16BaseTimeDurationINS_27TimeDurationValueCalculatorEEE (firefox-bin + 0xb0e7f)
                                                      #3  0x000076b859c46b9d n/a (libxul.so + 0x3a46b9d)
                                                      #4  0x000076b859b4fe1d n/a (libxul.so + 0x394fe1d)
                                                      #5  0x000076b859b4e012 n/a (libxul.so + 0x394e012)
                                                      #6  0x000076b85acf97ce n/a (libxul.so + 0x4af97ce)
                                                      #7  0x000076b8638f270f n/a (libnspr4.so + 0x1e70f)
                                                      #8  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #9  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #10 0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 10854:
                                                      #0  0x000076b863298f70 futex_wait (libc.so.6 + 0x98f70)
                                                      #1  0x000076b8632a0101 lll_mutex_lock_optimized (libc.so.6 + 0xa0101)
                                                      #2  0x000076b84339367d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59367d)
                                                      #3  0x000076b842ef869d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0xf869d)
                                                      #4  0x000076b84cfd6ca5 vaCreateBuffer (libva.so.2 + 0x6ca5)
                                                      #5  0x000076b84f801e29 n/a (libavcodec.so.60 + 0x801e29)
                                                      #6  0x000076b84f8130d6 n/a (libavcodec.so.60 + 0x8130d6)
                                                      #7  0x000076b84f3d5b85 n/a (libavcodec.so.60 + 0x3d5b85)
                                                      #8  0x000076b84f2a9a45 n/a (libavcodec.so.60 + 0x2a9a45)
                                                      #9  0x000076b84f2aa044 avcodec_send_packet (libavcodec.so.60 + 0x2aa044)
                                                      #10 0x000076b85d601c4b n/a (libxul.so + 0x7401c4b)
                                                      #11 0x000076b85d5be5a6 n/a (libxul.so + 0x73be5a6)
                                                      #12 0x000076b85d5f95a4 n/a (libxul.so + 0x73f95a4)
                                                      #13 0x000076b85d572bbb n/a (libxul.so + 0x7372bbb)
                                                      #14 0x000076b859c47b96 n/a (libxul.so + 0x3a47b96)
                                                      #15 0x000076b859c46d5f n/a (libxul.so + 0x3a46d5f)
                                                      #16 0x000076b859b4fe1d n/a (libxul.so + 0x394fe1d)
                                                      #17 0x000076b859b4e012 n/a (libxul.so + 0x394e012)
                                                      #18 0x000076b85acf97ce n/a (libxul.so + 0x4af97ce)
                                                      #19 0x000076b8638f270f n/a (libnspr4.so + 0x1e70f)
                                                      #20 0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #21 0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #22 0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      
                                                      Stack trace of thread 10855:
                                                      #0  0x000076b863298d71 __futex_abstimed_wait_common64 (libc.so.6 + 0x98d71)
                                                      #1  0x000076b86329b7ed __pthread_cond_wait_common (libc.so.6 + 0x9b7ed)
                                                      #2  0x000076b84339359d n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x59359d)
                                                      #3  0x000076b84336054b n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x56054b)
                                                      #4  0x000076b8433934cc n/a (libgallium-25.0.7-0ubuntu0.24.04.2.so + 0x5934cc)
                                                      #5  0x00005a8655d13ee0 n/a (firefox-bin + 0x6bee0)
                                                      #6  0x000076b86329caa4 start_thread (libc.so.6 + 0x9caa4)
                                                      #7  0x000076b863329a64 __clone (libc.so.6 + 0x129a64)
                                                      ELF object binary architecture: AMD x86-64
Oct 15 12:06:03 Desktop-Mint systemd[1]: systemd-coredump@1-10881-0.service: Deactivated successfully.
```