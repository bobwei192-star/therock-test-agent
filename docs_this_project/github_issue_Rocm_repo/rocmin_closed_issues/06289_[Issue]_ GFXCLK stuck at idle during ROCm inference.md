# [Issue]: GFXCLK stuck at idle during ROCm inference

- **Issue #:** 6289
- **State:** closed
- **Created:** 2026-05-21T15:15:47Z
- **Updated:** 2026-06-26T19:33:50Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6289

### Problem Description

During ROCm inference (Ollama / llama.cpp), the GFXCLK stays stuck at **41 MHz** instead of boosting to the expected ~2400 MHz. Power draw is ~50W instead of ~140-150W. Inference performance is roughly 3x lower than expected.

```
$ rocm-smi
Device  SCLK    MCLK    Power  GPU%
0       41Mhz   1258Mhz  50W   100%   <-- wrong, should be ~2400Mhz
```

The GPU correctly identifies itself as gfx1201 via KFD (verified with `rocminfo`).
`HSA_OVERRIDE_GFX_VERSION=12.0.1` is still required for ROCm 7.2.3 (runtime falls back to gfx1100 without it).

### Operating System

EndeavourOS

### CPU

AMD Ryzen 9 9950X 16-Core Processor

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

ROCm 7.2.3

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

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
  Name:                    AMD Ryzen 9 9950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 9950X 16-Core Processor
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
  Max Clock Freq. (MHz):   5756                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    63374532(0x3c704c4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    63374532(0x3c704c4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    63374532(0x3c704c4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    63374532(0x3c704c4) KB             
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
  Uuid:                    GPU-4904ba80f4e6b186               
  Marketing Name:          AMD Radeon RX 9070 XT              
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
  Max Clock Freq. (MHz):   2400                               
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
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16695296(0xfec000) KB              
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
*******                  
Agent 3                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Ryzen 9 9950X 16-Core Processor
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      256(0x100) KB                      
  Chip ID:                 5056(0x13c0)                       
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2200                               
  BDFID:                   29952                              
  Internal Node ID:        2                                  
  Compute Unit:            2                                  
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
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
  Packet Processor uCode:: 26                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    31687264(0x1e38260) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    31687264(0x1e38260) KB             
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

## Hardware / Software

| Component | Detail |
|-----------|--------|
| GPU | AMD Radeon RX 9070 XT (Navi 48, gfx1201, DID 0x7550) |
| CPU | AMD Ryzen 9 9950X (has display controller DID 0x13c0 -- separate amdgpu device, card0) |
| Motherboard | Gigabyte X870 |
| Kernel | 6.18.32-lts and 7.0.9-arch1 (both tested, same behavior) |
| ROCm | 7.2.3 |
| Driver | amdgpu (in-kernel) |
| Ollama | 0.24.0 with ollama-rocm |
| OS | EndeavourOS (Arch-based, rolling) |

## Investigation

Tested all standard `power_dpm_force_performance_level` values:

| Value | Result |
|-------|--------|
| `auto` | Stuck at 41 MHz during compute |
| `high` | Brief peaks, returns to 41 MHz |
| `manual` (level 2 only) | Drops during inference |
| `profile_peak` | Stable 2400 MHz -- but clock gating fully disabled (see below) |

Tested `pp_power_profile_mode = 5` (COMPUTE): higher peaks than default, but still drops to 41 MHz without `profile_peak`.

Tested `echo on > /sys/bus/pci/devices/0000:03:00.0/power/control` (disable DRM runtime PM): no improvement.

Tested on both kernel 6.18.32-lts and 7.0.9-arch1: **identical behavior on both**. Not a kernel regression.

### Key finding -- gpu_busy_percent is unreliable with profile_peak

With `power_dpm_force_performance_level = profile_peak`, clock gating is fully disabled:

```
$ sudo cat /sys/kernel/debug/dri/1/amdgpu_pm_info
GPU Load: 100 %
MEM Load: 0 %    <-- 0% at idle, correct
```

`gpu_busy_percent` reports 100% even at idle. Use `mem_busy_percent` instead:
- Idle: 0%
- Active inference: >5-80%

### rocm-smi device ordering

On X870 boards, rocm-smi inverts devices vs sysfs:
- `rocm-smi device 0` = DID 0x7550 = RX 9070 XT (card1 in sysfs)
- `rocm-smi device 1` = DID 0x13c0 = AMD Ryzen 9 9950X display controller (card0 in sysfs)

The "low-power state" WARNING in rocm-smi comes from device 1 (AMD Ryzen 9 9950X), not the RX 9070 XT.

MCLK showing 1258 MHz in rocm-smi is the **video memory clock**, not SCLK. Normal for compute.

## Root cause

SMU14 firmware (RDNA4) does not boost GFXCLK for compute/ROCm workloads in any standard power mode. This appears to be a known issue being addressed in ROCm:

- ROCm PR [rocm-systems#2510](https://github.com/ROCm/rocm-systems/pull/2510): "Add DRM-based wake for suspended AMD GPUs" (merged 2026-01)
- ROCm issue [ROCm#5849](https://github.com/ROCm/ROCm/issues/5849)

## Temporary workaround

A dynamic daemon that switches to `profile_peak` only during active inference, using `mem_busy_percent` as the trigger.

### `/usr/local/bin/amdgpu-dynperf.py`

```python
#!/usr/bin/env python3
import time, sys, signal

GPU_MEM_BUSY  = "/sys/class/drm/card1/device/mem_busy_percent"
GPU_PERF      = "/sys/class/drm/card1/device/power_dpm_force_performance_level"
GPU_PROFILE   = "/sys/class/drm/card1/device/pp_power_profile_mode"

THRESHOLD  = 5    # % mem bandwidth to consider GPU active
DELAY_UP   = 2    # seconds of load before switching to profile_peak
DELAY_DOWN = 10   # seconds of idle before returning to auto

def read_busy():
    with open(GPU_MEM_BUSY) as f:
        return int(f.read().strip())

def set_profile(p):
    with open(GPU_PERF, "w") as f:
        f.write(p)
    print(f"[dynperf] --> {p}", flush=True)

def shutdown(sig, frame):
    set_profile("auto")
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

# Set COMPUTE power profile at startup (better peaks than BOOTUP_DEFAULT)
with open(GPU_PROFILE, "w") as f:
    f.write("5")
print("[dynperf] power profile --> COMPUTE", flush=True)

current    = "auto"
busy_since = None
idle_since = None

set_profile("auto")
print("[dynperf] started (tracking mem_busy_percent)", flush=True)

while True:
    busy = read_busy()

    if busy > THRESHOLD:
        idle_since = None
        if current == "auto":
            if busy_since is None:
                busy_since = time.time()
            elif time.time() - busy_since >= DELAY_UP:
                set_profile("profile_peak")
                current = "profile_peak"
                busy_since = None
    else:
        busy_since = None
        if current == "profile_peak":
            if idle_since is None:
                idle_since = time.time()
            elif time.time() - idle_since >= DELAY_DOWN:
                set_profile("auto")
                current = "auto"
                idle_since = None

    time.sleep(1)
```

**Note:** adjust `card1` to match your RX 9070 XT. Verify with:
```bash
cat /sys/class/drm/card1/device/uevent | grep 'PCI_ID'
# Should show: PCI_ID=1002:7550
```

### `/etc/systemd/system/amdgpu-dynperf.service`

```ini
[Unit]
Description=Dynamic AMDGPU performance profile for ROCm (RX 9070 XT)
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /usr/local/bin/amdgpu-dynperf.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo chmod +x /usr/local/bin/amdgpu-dynperf.py
sudo systemctl daemon-reload
sudo systemctl enable --now amdgpu-dynperf.service
```

### Result

```
$ rocm-smi
Device  SCLK      MCLK    Power  Perf         GPU%
0       2400Mhz  1258Mhz  148W   stable_peak  100%
```

GFXCLK boosts to 2400 MHz during inference, returns to idle when done.

## Ollama overrides required (ROCm 7.2.3)

`/etc/systemd/system/ollama.service.d/override.conf`:

```ini
[Service]
Environment="HSA_OVERRIDE_GFX_VERSION=12.0.1"
Environment="HIP_VISIBLE_DEVICES=0"
```

`HSA_OVERRIDE_GFX_VERSION=12.0.1`: ROCm does not map PCI ID 0x7550 to gfx1201 natively.
`HIP_VISIBLE_DEVICES=0`: Without this, the Ryzen 9950X  appears as an HSA agent with 32 GiB "VRAM" (system RAM), distorting context window calculations.