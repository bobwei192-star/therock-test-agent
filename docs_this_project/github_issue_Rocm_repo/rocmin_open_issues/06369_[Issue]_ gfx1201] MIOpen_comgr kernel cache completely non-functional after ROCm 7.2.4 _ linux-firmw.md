# [Issue]: gfx1201] MIOpen/comgr kernel cache completely non-functional after ROCm 7.2.4 / linux-firmware-amdgpu 20260519 update — every inference run takes ~385s instead of ~6s

- **Issue #:** 6369
- **State:** open
- **Created:** 2026-06-19T11:58:24Z
- **Updated:** 2026-06-19T14:37:56Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6369

### Problem Description

On AMD Radeon RX 9070 (gfx1201, RDNA4), the MIOpen/comgr kernel cache is completely non-persistent — every single inference run (not just the first) takes ~385 seconds for kernel compilation, regardless of tensor shape changes. This is reproducible across multiple independent setups (bare metal, Docker, different PyTorch/ROCm builds including TheRock nightly), but is fully resolved by downgrading to an earlier ROCm/kernel/firmware combination.This appears related to #6008 but differs in that it occurs with plain SDXL checkpoint inference (Conv2D, FP16), not just WAN VAE (Conv3D/BF16) — and the regression is precisely bisected to a specific package update date.

Working configuration (confirmed fast: ~6s first inference, ~5.5s subsequent runs with different tensor shapes):
linux-cachyos:          7.0.9-1
rocm-core:              7.2.3-1.1
rocm-hip-sdk:           7.2.3-1
rocm-llvm:              2:7.2.3-1.1
rocm-device-libs:       2:7.2.3-1.1
linux-firmware-amdgpu:  1:20260410-1
torch (venv):           2.9.1+rocm6.3 (pyenv, Python 3.12.0)
Broken configuration (confirmed slow: ~385s for every single run, no caching benefit ever):
linux-cachyos:          7.0.11-1 (later also 7.0.12-1)
rocm-core:              7.2.4-1.1
rocm-hip-sdk:           7.2.4-1
rocm-llvm:              2:7.2.4-1.1
rocm-device-libs:       2:7.2.4-1.1
linux-firmware-amdgpu:  1:20260519-1
Update applied 2026-06-10 11:53 CEST via pacman -Syu.
Suspected cause: Given the precise bisection, the regression is most likely introduced by linux-firmware-amdgpu 20260410 → 20260519 (gfx1201 microcode changes) or rocm-core/rocm-llvm/rocm-device-libs 7.2.3 → 7.2.4. Since user-space PyTorch builds (both the original 6.3-based and a completely independent fresh TheRock 7.13 nightly build) were unaffected by the fix and only the system package revert mattered, the firmware update seems like the stronger candidate, but a rocm-llvm/comgr regression cannot be ruled out without further bisection.
Workaround: Pinned the following packages via IgnorePkg in /etc/pacman.conf to stay on the working versions until a fix is available: linux-cachyos linux-cachyos-headers rocm-core rocm-hip-sdk rocm-hip-libraries rocm-hip-runtime rocm-llvm rocm-device-libs rocminfo rocm-cmake rocm-language-runtime rocm-opencl-runtime rocm-opencl-sdk linux-firmware-amdgpu linux-firmware

### Operating System

CachyOS Linux

### CPU

AMD Ryzen 7 7800X3D

### GPU

AMD Radeon RX9070

### ROCm Version

7.2.4-1.1 (broken) / 7.2.3-1.1 (working, used as workaround)

### ROCm Component

MIOpen

### Steps to Reproduce

<ol class="[li_&amp;]:mb-0 [li_&amp;]:mt-1 [li_&amp;]:gap-1 [&amp;:not(:last-child)_ul]:pb-1 [&amp;:not(:last-child)_ol]:pb-1 list-decimal flex flex-col gap-1 pl-8 mb-3"><li class="font-claude-response-body whitespace-normal break-words pl-2">Run ComfyUI with an SDXL checkpoint (e.g. JuggernautXL) on gfx1201.</li>
<li class="font-claude-response-body whitespace-normal break-words pl-2">Generate a simple 512x512 image, 4 steps, dpmpp_2m/karras sampler, fp16.</li>
<li class="font-claude-response-body whitespace-normal break-words pl-2">Note the time: <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">Prompt executed in X seconds</code>.</li>
<li class="font-claude-response-body whitespace-normal break-words pl-2">Repeat the run (same or different resolution/seed).</li>
</ol>
<p class="font-claude-response-body break-words whitespace-normal"><strong>Observed on broken config:</strong> every single run takes ~385 seconds, identical down to the decimal across 6+ independent test runs:</p>
<div role="group" aria-label="Code" tabindex="0" class="relative group/copy bg-bg-000/50 border-0.5 border-border-400 rounded-lg focus:outline-none focus-visible:ring-2 focus-visible:ring-accent-100"><div class="sticky opacity-0 group-hover/copy:opacity-100 group-focus-within/copy:opacity-100 top-2 py-2 h-12 w-0 float-right"><div class="absolute right-0 h-8 px-2 items-center inline-flex z-10"><button class="inline-flex
  items-center
  justify-center
  relative
  isolate
  shrink-0
  can-focus
  select-none
  disabled:pointer-events-none
  disabled:opacity-50
  disabled:shadow-none
  disabled:drop-shadow-none border-transparent
          transition
          font-base
          duration-300
          ease-[cubic-bezier(0.165,0.85,0.45,1)] h-8 w-8 rounded-md backdrop-blur-md _fill_10ocf_9 _ghost_10ocf_96" type="button" aria-label="In die Zwischenablage kopieren" data-state="closed"><div class="relative"><div class="transition-all opacity-100 scale-100" style="width: 20px; height: 20px; display: flex; align-items: center; justify-content: center;"><svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="transition-all opacity-100 scale-100" aria-hidden="true" style="flex-shrink: 0;"><path d="M12.5 3A1.5 1.5 0 0 1 14 4.5V6h1.5A1.5 1.5 0 0 1 17 7.5v8a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 6 15.5V14H4.5A1.5 1.5 0 0 1 3 12.5v-8A1.5 1.5 0 0 1 4.5 3zm1.5 9.5a1.5 1.5 0 0 1-1.5 1.5H7v1.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-8a.5.5 0 0 0-.5-.5H14zM4.5 4a.5.5 0 0 0-.5.5v8a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-8a.5.5 0 0 0-.5-.5z"></path></svg></div><div class="absolute inset-0 flex items-center justify-center"><div class="transition-all opacity-0 scale-50" style="width: 20px; height: 20px; display: flex; align-items: center; justify-content: center;"><svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="transition-all opacity-0 scale-50" aria-hidden="true" style="flex-shrink: 0;"><path d="M15.188 5.11a.5.5 0 0 1 .752.626l-.056.084-7.5 9a.5.5 0 0 1-.738.033l-3.5-3.5-.064-.078a.501.501 0 0 1 .693-.693l.078.064 3.113 3.113 7.15-8.58z"></path></svg></div></div></div></button></div></div><div class="overflow-x-auto"><pre class="code-block__code !my-0 !rounded-lg !text-sm !leading-relaxed p-3.5" style="color: rgb(234, 236, 240); background: transparent; font-family: var(--font-mono);"><code style="color: rgb(234, 236, 240); background: transparent; font-family: var(--font-mono); white-space: pre-wrap;"><span><span>385.39s, 385.42s, 385.45s, 385.48s, 386.49s, 386.50s, 387.65s</span></span></code></pre></div></div>
<p class="font-claude-response-body break-words whitespace-normal">spanning bare metal, Docker (<code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">rocm/pytorch:latest</code>, ROCm 7.2.4 inside container), and a fresh TheRock nightly PyTorch build for gfx1201 (<code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">torch==2.11.0+rocm7.13.0a20260425</code>, installed via <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">--index-url https://rocm.nightlies.amd.com/v2/gfx120X-all/</code>). No caching benefit regardless of run order, tensor shape, or attempts to persist <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/root/.cache/comgr</code> and <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">~/.triton/cache</code> across restarts.</p>
<p class="font-claude-response-body break-words whitespace-normal"><strong>Observed on working config:</strong> first run after restart: 6.84s. Second run, different resolution (768x768) and seed: 5.57s. Subsequent runs remain fast.</p>
<p class="font-claude-response-body break-words whitespace-normal"><strong>Isolation testing performed</strong> — all of the following were tested independently on the broken package versions, and all produced the identical ~385s result, ruling each out as the cause:</p>
<div class="overflow-x-auto w-full px-2 mb-6">
Variable tested | Result
-- | --
Bare metal vs. Docker (rocm/pytorch:latest) | No difference — both ~385s
With/without HSA_OVERRIDE_GFX_VERSION=12.0.0 | No difference
Original pyenv venv (torch 2.9.1+rocm6.3) vs. fresh TheRock nightly venv (torch 2.11.0+rocm7.13) | No difference
Original ComfyUI install (with custom nodes) vs. fresh ComfyUI checkout (zero custom nodes) | No difference
Persisting/copying comgr cache directory across container restarts via Docker volume | No difference — cache files present but not used
Fixing llvmcache.timestamp invalidation | No difference
File permission/ownership normalization on cache files | No difference

</div>
<p class="font-claude-response-body break-words whitespace-normal">The only variable that resolved the issue was reverting the system-level ROCm/kernel/firmware packages via a full filesystem snapshot restore (Timeshift, rsync mode) to a state predating the 2026-06-10 update. User-space Python venvs were explicitly excluded from this restore and remained on their original (already-tested, non-fixing) versions, confirming the regression originates in the system ROCm/kernel/firmware stack rather than any Python-level package.</p>

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
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
  Name:                    AMD Ryzen 7 7800X3D 8-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 7800X3D 8-Core Processor
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
  Max Clock Freq. (MHz):   5053                               
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
      Size:                    32593572(0x1f156a4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32593572(0x1f156a4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32593572(0x1f156a4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32593572(0x1f156a4) KB             
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
  Uuid:                    GPU-144647a33717b2f6               
  Marketing Name:          AMD Radeon RX 9070                 
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
  Chip ID:                 30032(0x7550)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2120                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            56                                 
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
  Packet Processor uCode:: 218                                
  SDMA engine uCode::      662                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16695296(0xfec000) KB              
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

During investigation we found the cache directory structure:
~/.cache/comgr/llvmcache-<hash>          # ~1.1GB, 242 files at time of testing
~/.cache/comgr/llvmcache.timestamp       # invalidation marker
On the broken config, the cache appears to not be consulted at all for the relevant kernel compilation path on gfx1201, rather than purely a timestamp-invalidation issue — manually resetting llvmcache.timestamp to be older than the cache file mtimes had no effect.
We did not have MIOPEN_ENABLE_LOGGING_CMD support confirmed working in this ComfyUI build to capture which specific MIOpen solvers/algorithms were being invoked. Happy to capture this with guidance, or attempt further bisection between the firmware and ROCm point releases individually (rather than both at once), if that would help narrow down the root cause.