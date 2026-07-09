# 🐞 Bug Report: Strix Halo (Ryzen AI Max 395+) + ROCm 7.1 + AI workloads + Video Encoding → GPU Hang, VRAM Loss, GNOME  Crash

- **Issue #:** 5665
- **State:** closed
- **Created:** 2025-11-14T00:54:21Z
- **Updated:** 2026-03-04T14:51:46Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5665

### Problem Description

**System:**

* **Device:** Evo-x2 AI Max 395+ (Strix Halo, Ryzen AI Max 395+)
* **RAM:** 128GB
* **OS:** Ubuntu 24.04 OEM
* **Kernel:** 6.14.0-1015-oem
* **ROCm:** ROCm 7.1.25424-4179531dcd

* **Display Server:** GNOME Shell on Wayland (also reproducible on Xorg)
* **Other software:** Ollama (ROCm backend), Open-WebUI (PyTorch 2.8.0+rocm7.1.0), Sunshine (streaming, various encoders)

## Firmware details

linux-firmware: 20240318.git3b128b60-0ubuntu2.19
Firmware blobs present in /lib/firmware/amdgpu/:
- navi10_*.bin.zst
- navi12_*.bin.zst
- navi14_*.bin.zst

(No strix_halo or gfx1151 blobs found in this firmware version, but all up-to-date navi blobs present.)

No explicit amdgpu firmware load lines appear in dmesg, but the driver is working and ROCm detects the GPU (gfx1151) with correct VRAM and PCI ID.

---

## **Description**

Running *heavy AI workloads* (Ollama, PyTorch, WebUI) with **ROCm 7.1** on the Strix Halo iGPU is stable **unless** the **Sunshine streaming server** (hardware video encoding for game streaming) is also running.

When **AI compute and Sunshine streaming (using hardware encoder/VPE)** run at the same time, the system will eventually:

* Freeze or hang
* Crash the GNOME Shell session 
* Drop all GPU VRAM (“VRAM is lost due to GPU reset!”)
* Cause full GPU reset/failure to recover
* Show *catastrophic* MES/SDMA/VPE driver errors

This makes Strix Halo APUs **unusable for simultaneous AI + game/desktop streaming**, even though both are stable when run separately.

> **NOTE:**
> I can successfully run a **Shadow of the Tomb Raider** benchmark **at the same time** as I use **Gemma3:27B** with Open-WebUI (Ollama ROCm backend) with *no crash or instability*.
> The issue only appears when combining AI workloads with Sunshine streaming (video encoding).



## **What I Expected**

* Both AI compute (e.g., **Gemma3:27B** inference) and hardware-accelerated streaming should be possible at the same time on a high-end APU.
* ROCm/AMDGPU drivers should recover gracefully from heavy/parallel workloads.
* No session or GPU crash.

---

## **What Actually Happens**

* Catastrophic driver failure, logs show:

  * `amdgpu: MES failed to respond to msg=REMOVE_QUEUE`
  * `amdgpu: GPU reset begin!`
  * `amdgpu: VRAM is lost due to GPU reset!`
  * `amdgpu: Ring sdma0 reset failure`
  * `amdgpu: resume of IP block <vpe_v6_1> failed -110`
  * `amdgpu: suspend of IP block <mes_v11_0> failed -110`
  * Full context loss: “fatal server error”, “Xwayland exited unexpectedly”, “context is innocent”, etc.

---

## **Full Log Excerpt**

```text
amdgpu: MES failed to respond to msg=REMOVE_QUEUE
amdgpu: MES might be in unrecoverable state, issue a GPU reset
amdgpu: GPU reset begin!
amdgpu: Failed to evict process queues
amdgpu: VRAM is lost due to GPU reset!
amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu: suspend of IP block <mes_v11_0> failed -110
amdgpu: resume of IP block <vpe_v6_1> failed -110
amdgpu: Ring sdma0 reset failure
amdgpu: GPU reset begin!
...
gnome-shell: JS ERROR: Gio.IOErrorEnum: Xwayland exited unexpectedly
[drm:do_aquire_global_lock.isra.0 [amdgpu]] *ERROR* [CRTC:79:crtc-0] hw_done or flip_done timed out
```

**Full dmesg/syslog available on request.**

---

## **Workarounds**

* **Disabling hardware video encoding (forcing Sunshine to use software encoder, `libx264`)** eliminates the crash entirely, but at the cost of high CPU use.
* Running only AI or only streaming is stable; running both with hardware encoding = crash.
* Latest firmware, kernel, ROCm, PyTorch (all ROCm 7.1 matched) — no change.
* All kernel tuning and `iommu`/`amdgpu` GRUB parameters tested — no improvement.

---

## **Impact**

* **Cannot use Strix Halo iGPU for simultaneous AI and hardware-accelerated game/desktop streaming**
* **Blocks advanced multi-modal workloads (AI + AV/streaming)**
* **Major regression vs. expectations for top-end APU**

> **Again, note:**
> Running **Shadow of the Tomb Raider benchmark** **at the same time as Gemma3:27B/Open-WebUI** works fine—no crash.
> **The crash is uniquely triggered by AI + hardware video encoding via Sunshine.**

---

## **What Help Do I Need?**

* **Bug acknowledgement**
* **Instructions for advanced debug tracing if needed**
* **ETA for fix in ROCm/amdgpu/firmware**
* **Beta firmware or kernel to try**

---

## **Environment Details**

```
Device: Evo-x2 AI Max 395+ (Strix Halo, Ryzen AI Max 395+)
RAM: 128GB
OS: Ubuntu 24.04 OEM
Kernel: 6.14.0-1015-oem
ROCm: 7.1.0
firmware: [EDIT: paste output of `apt show linux-firmware`]
PyTorch: 2.8.0+rocm7.1.0
Ollama: [latest ROCm backend]
Sunshine: 2025.924.154138 commit: 86188d47a7463b0f73b35de18a628353adeaa20e
```

---

## **Attachments**

* [Include full dmesg/syslog excerpts as files, or provide a pastebin link.]

---

**Thank you! If you need extra logs, traces, or want me to test a patch, I’m happy to help.**

---

Let me know if you want it as a Markdown file or with any other formatting!
This is the ideal format to post on [[ROCm GitHub Issues](https://github.com/RadeonOpenCompute/ROCm/issues)](https://github.com/RadeonOpenCompute/ROCm/issues) or the AMD Community forums.

### Operating System

Ubuntu 24.04 OEM

### CPU

Ryzen AI Max 395+

### GPU

Integrated Radeon 8060s

### ROCm Version

ROCm 7.1.25424-4179531dcd

### ROCm Component

_No response_

### Steps to Reproduce

## **How to Reproduce**

1. Boot Ubuntu 24.04 OEM on Evo-x2 AI Max 395+ (Strix Halo)
2. Confirm ROCm stack (`hipconfig`, `rocminfo`) is working and AI workloads are stable.
3. Start **Ollama** or Open-WebUI and run a large language model (**Gemma3:27B**, with 80+ layers on GPU, batch size 256, ROCm backend).
4. While the AI workload is running, start **Sunshine** and connect a streaming client (default encoder, or VPE hardware encoder).
5. Within minutes (sometimes hour), the system hangs/crashes. Graphics session dies; must restart.


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
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
      Size:                    32486536(0x1efb488) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32486536(0x1efb488) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32486536(0x1efb488) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32486536(0x1efb488) KB             
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
      Size:                    100663296(0x6000000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    100663296(0x6000000) KB            
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
      Size:                    32486536(0x1efb488) KB             
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
      Size:                    32486536(0x1efb488) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***
```

### Additional Information

Workarounds

Disabling hardware video encoding (forcing Sunshine to use software encoder, libx264) eliminates the crash entirely, but at the cost of high CPU use.

Running only AI or only streaming is stable; running both with hardware encoding = crash.

Latest firmware, kernel, ROCm, PyTorch (all ROCm 7.1 matched) — no change.

All kernel tuning and iommu/amdgpu GRUB parameters tested — no improvement.

Attached the output of: `journalctl -b -1 | grep -Ei "amdgpu|rocm|gpu|error" | tee journal_grepped.txt`

[journal_grepped.txt](https://github.com/user-attachments/files/23537090/journal_grepped.txt)