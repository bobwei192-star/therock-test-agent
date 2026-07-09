# [Issue]: RX 6800 GPU reset when using ROCm (GPU not listed but I think it's in error)

- **Issue #:** 2935
- **State:** closed
- **Created:** 2024-02-28T05:11:03Z
- **Updated:** 2024-07-04T19:41:49Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 XT, ROCm 5.5.1
- **URL:** https://github.com/ROCm/ROCm/issues/2935

### Problem Description

note: this GPU isn't listed, but older GPUs like Radeon VII are and they are not enterprise cards so I can only assume this is in error please fix. The RX 6800 is also listed as supported to my understanding by ROCm, so I am very confused why it's not listed in the issue template. If anyone can reproduce this on a card listed in the issue template that would be great I think it's likely issue with all cards, but for now the card listed in the issue template is inaccurate since it's required

I have been having constant crashes where my system will just reboot when trying to generate a image in Stable Diffusion, my screen goes black suddenly, then resets and I usually get a MCE error after that looks like this. I also noticed audio will keep playing, then become distorted and stutter as if the CPU is having a hard time keeping up until it stops completely then resets shortly after 
```
Feb 27 15:09:35 nixos kernel: mce: [Hardware Error]: Machine check events logged
Feb 27 15:09:35 nixos kernel: mce: [Hardware Error]: CPU 9: Machine Check: 0 Bank 5: bea0000000000108
Feb 27 15:09:35 nixos kernel: mce: [Hardware Error]: TSC 0 ADDR 1ffffc0754f4a MISC d012000100000000 SYND 4d000000 IPID 500b000000000
Feb 27 15:09:35 nixos kernel: mce: [Hardware Error]: PROCESSOR 2:870f10 TIME 1709068166 SOCKET 0 APIC 3 microcode 8701030
Feb 27 15:09:36 nixos kernel: MCE: In-kernel MCE decoding enabled.
```
My system is otherwise very stable so it seemed odd not to mention I have played full length games and had zero issues whatsoever, also I have tested the memory it is not the problem. so I decided to try to ssh into my computer from my phone when I get this error and discovered this
```
Feb 27 22:08:15 nixos systemd[1]: Starting Cleanup of Temporary Directories...
Feb 27 22:08:15 nixos systemd[1]: systemd-tmpfiles-clean.service: Deactivated successfully.
Feb 27 22:08:15 nixos systemd[1]: Finished Cleanup of Temporary Directories.
Feb 27 22:08:24 nixos kernel: amdgpu 0000:09:00.0: amdgpu: SMU: I'm not done with your previous command: SMN_C2PMSG_66:0x00000028 SMN_C2PMSG_82:0x00000000
Feb 27 22:08:24 nixos kernel: amdgpu 0000:09:00.0: amdgpu: Failed to enable gfxoff!
Feb 27 22:08:29 nixos kernel: amdgpu 0000:09:00.0: amdgpu: SMU: I'm not done with your previous command: SMN_C2PMSG_66:0x00000028 SMN_C2PMSG_82:0x00000000
Feb 27 22:08:29 nixos kernel: amdgpu 0000:09:00.0: amdgpu: Failed to enable gfxoff!
Feb 27 22:08:30 nixos kernel: amdgpu 0000:09:00.0: [drm] *ERROR* [CRTC:95:crtc-1] flip_done timed out
Feb 27 22:08:31 nixos kernel: [drm:amdgpu_job_timedout [amdgpu]] *ERROR* ring sdma0 timeout, signaled seq=3400, emitted seq=3401
Feb 27 22:08:31 nixos kernel: [drm:amdgpu_job_timedout [amdgpu]] *ERROR* Process information: process  pid 0 thread  pid 0
Feb 27 22:08:31 nixos kernel: amdgpu 0000:09:00.0: amdgpu: GPU reset begin!
Feb 27 22:08:31 nixos kernel: amdgpu: Failed to suspend process 0x800c
```
I am not a expert in drivers but this seems to be a issue with AMDGPU, but it could also be ROCm or Torch issue, since I am not sure I am reporting it here and I have reported it to the respective projects. Thanks

### Operating System

NixOS VERSION 24.05 (Uakari)

### CPU

AMD Ryzen 7 3700X 8-Core Processor

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.0.0, ROCm 5.5.1

### ROCm Component

ROCm

### Steps to Reproduce

1. Install mostly any Stable Diffusion WebUI e.g. ComfyUI, InvokeAI, Automatic1111, etc.
2. Install a SDXL model
3. Generate a image, crashes seem to depend on resolution used. e.g. 1024x1024 is fine, 512x512 also fine, but 832x1152 will crash
4. See crash

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
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
  Name:                    AMD Ryzen 7 3700X 8-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 7 3700X 8-Core Processor
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
  Max Clock Freq. (MHz):   3600
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
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    65773952(0x3eba180) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65773952(0x3eba180) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65773952(0x3eba180) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1030
  Uuid:                    GPU-6200dec08b9272cf
  Marketing Name:          AMD Radeon RX 6800
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
    L1:                      16(0x10) KB
  Chip ID:                 29631(0x73bf)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2475
  BDFID:                   2304
  Internal Node ID:        1
  Compute Unit:            60
  SIMDs per CU:            2
  Shader Engines:          4
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
  Packet Processor uCode:: 116
  SDMA engine uCode::      83
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16760832(0xffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16760832(0xffc000) KB
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

### Additional Information

Issue on AMDGPU: https://gitlab.freedesktop.org/drm/amd/-/issues/3220
Issue on PyTorch: https://github.com/pytorch/pytorch/issues/120775