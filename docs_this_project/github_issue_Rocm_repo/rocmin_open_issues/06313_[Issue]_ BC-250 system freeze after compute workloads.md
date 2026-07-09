# [Issue]: BC-250 system freeze after compute workloads

- **Issue #:** 6313
- **State:** open
- **Created:** 2026-05-28T23:36:41Z
- **Updated:** 2026-07-01T15:02:58Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6313

### Problem Description

gfx1013 worked with ROCm 5.2 (Linux Ubuntu Ubuntu 20.04.6 LTS [5.4.0-216-generic|libc 2.31]), but in newer versions, it leads to full system freezes.

I observed the same behavior on Ubuntu 24.04 and CatchyOS.

I know gfx1013 isn’t officially supported (it’s RDNA 1.5), but it is correctly detected, and older ROCm versions used to run on it without issues. The GPU also works fine with OpenCL workloads using RustiCL.

I suspect it might be a power or memory management bug, since this is an APU with shared system memory.

Any help or explanation of what might be happening would be appreciated.

### Operating System

Linux bc250 7.0.10-1-cachyos x86_64

### CPU

AMD BC-250

### GPU

AMD Oberon APU (gfx1013)

### ROCm Version

ROCm 7.2.3

### ROCm Component

_No response_

### Steps to Reproduce

install latest rocm
run any GPU workload - opencl or hip

For example, clinfo outputs its results, and then the system hangs.
clpeak runs for a few seconds, prints a few results, and then causes a complete system freeze again.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
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
  Name:                    AMD BC-250
  Uuid:                    CPU-XX
  Marketing Name:          AMD BC-250
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
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            12
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    9892080(0x96f0f0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    9892080(0x96f0f0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    9892080(0x96f0f0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    9892080(0x96f0f0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1013
  Uuid:                    GPU-XX
  Marketing Name:          AMD BC-250
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
    L2:                      4096(0x1000) KB
  Chip ID:                 5118(0x13fe)
  ASIC Revision:           2(0x2)
  Cacheline Size:          128(0x80)
  Max Clock Freq. (MHz):   2000
  BDFID:                   256
  Internal Node ID:        1
  Compute Unit:            24
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
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    1280(0x500)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)
    y                        65535(0xffff)
    z                        65535(0xffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 144
  SDMA engine uCode::      52
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    6291456(0x600000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    6291456(0x600000) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx1013:xnack-
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
      Name:                    amdgcn-amd-amdhsa--gfx10-1-generic:xnack-
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
```

### Additional Information

```
kvě 25 19:29:48 bc250 kernel: amdgpu 0000:01:00.0: Dumping IP State
kvě 25 19:29:48 bc250 kernel: amdgpu 0000:01:00.0: Dumping IP State Completed
kvě 25 19:29:48 bc250 kernel: amdgpu 0000:01:00.0: [drm] AMDGPU device coredump file has been created
kvě 25 19:29:48 bc250 kernel: amdgpu 0000:01:00.0: [drm] Check your /sys/class/drm/card0/device/devcoredump/data
kvě 25 19:29:48 bc250 kernel: amdgpu 0000:01:00.0: ring sdma0 timeout, signaled seq=309, emitted seq=313
kvě 25 19:29:48 bc250 kernel: amdgpu 0000:01:00.0: Starting sdma0 ring reset
kvě 25 19:29:55 bc250 sudo[3572]: pam_unix(sudo:session): session opened for user root(uid=0) by ahorek(uid=1000)
kvě 25 19:29:57 bc250 kernel: amdgpu 0000:01:00.0: qcm fence wait loop timeout expired
kvě 25 19:29:57 bc250 kernel: amdgpu 0000:01:00.0: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
kvě 25 19:29:57 bc250 kernel: amdgpu 0000:01:00.0: Failed to evict process queues
kvě 25 19:29:57 bc250 kernel: amdgpu: Failed to suspend process pid 3484
kvě 25 19:29:58 bc250 kernel: amdgpu 0000:01:00.0: timeout waiting for kiq fence
kvě 25 19:30:06 bc250 kernel: amdgpu 0000:01:00.0: qcm fence wait loop timeout expired
kvě 25 19:30:06 bc250 kernel: amdgpu 0000:01:00.0: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
kvě 25 19:30:06 bc250 kernel: amdgpu 0000:01:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring kiq_0.2.1.0 test failed (-110)
kvě 25 19:30:15 bc250 kernel: amdgpu 0000:01:00.0: qcm fence wait loop timeout expired
kvě 25 19:30:15 bc250 kernel: amdgpu 0000:01:00.0: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
kvě 25 19:30:24 bc250 kernel: amdgpu 0000:01:00.0: qcm fence wait loop timeout expired
kvě 25 19:30:24 bc250 kernel: amdgpu 0000:01:00.0: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
kvě 25 19:30:24 bc250 kernel: amdgpu 0000:01:00.0: Failed to restore process queues
kvě 25 19:30:24 bc250 kernel: amdgpu: Failed to restore queues of process pid 3484
kvě 25 19:30:24 bc250 kernel: amdgpu: Restore process pid 3484 failed during resume
kvě 25 19:30:24 bc250 kernel: amdgpu 0000:01:00.0: Ring sdma0 reset succeeded
kvě 25 19:30:24 bc250 kernel: amdgpu 0000:01:00.0: [drm] device wedged, but recovered through reset
kvě 25 19:30:24 bc250 kernel: amdgpu 0000:01:00.0: GPU reset begin!. Source:  4
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: failed to suspend display audio
kvě 25 19:30:28 bc250 kernel: amdgpu: Failed to suspend process pid 3484
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: Dumping IP State
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: Dumping IP State Completed
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: MODE1 reset
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: GPU mode1 reset
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: GPU psp mode1 reset
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: GPU reset succeeded, trying to resume
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: Timeout waiting for VM flush hub: 0!
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: [drm] PCIE GART of 512M enabled (table at 0x000000F57FE00000).
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: [drm] AMDGPU device coredump file has been created
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: [drm] Check your /sys/class/drm/card0/device/devcoredump/data
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: VRAM is lost due to GPU reset!
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: PSP is resuming...
kvě 25 19:30:28 bc250 kernel: amdgpu 0000:01:00.0: reserve 0x400000 from 0xf57f800000 for PSP TMR
```

```
kvě 24 01:00:34 bc250 kernel: amdgpu 0000:01:00.0: timeout waiting for kiq fence
kvě 24 01:00:36 bc250 kernel: amdgpu 0000:01:00.0: Dumping IP State
kvě 24 01:00:36 bc250 kernel: amdgpu 0000:01:00.0: Dumping IP State Completed
kvě 24 01:00:36 bc250 kernel: amdgpu 0000:01:00.0: [drm] AMDGPU device coredump file has been created
kvě 24 01:00:36 bc250 kernel: amdgpu 0000:01:00.0: [drm] Check your /sys/class/drm/card0/device/devcoredump/data
kvě 24 01:00:36 bc250 kernel: amdgpu 0000:01:00.0: ring sdma0 timeout, signaled seq=194, emitted seq=198
kvě 24 01:00:36 bc250 kernel: amdgpu 0000:01:00.0: Starting sdma0 ring reset
kvě 24 01:00:45 bc250 kernel: amdgpu 0000:01:00.0: qcm fence wait loop timeout expired
kvě 24 01:00:45 bc250 kernel: amdgpu 0000:01:00.0: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
```
kvě 24 01:00:45 bc250 kernel: amdgpu 0000:01:00.0: Failed to evict process queues
kvě 24 01:00:45 bc250 kernel: amdgpu: Failed to suspend process pid 5524
kvě 24 01:00:46 bc250 kernel: amdgpu 0000:01:00.0: timeout waiting for kiq fence
kvě 24 01:00:46 bc250 kernel: amdgpu: amdgpu_vm_bo_update failed
kvě 24 01:00:46 bc250 kernel: amdgpu: update_gpuvm_pte() failed
kvě 24 01:00:46 bc250 kernel: amdgpu: Failed to map bo to gpuvm
kvě 24 01:00:46 bc250 kernel: amdgpu 0000:01:00.0: Failed to map peer:0000:01:00.0 mem_domain:4
kvě 24 01:00:46 bc250 kernel: amdgpu: amdgpu_vm_bo_update failed
kvě 24 01:00:46 bc250 kernel: amdgpu: update_gpuvm_pte() failed
kvě 24 01:00:46 bc250 kernel: amdgpu: Failed to map bo to gpuvm
kvě 24 01:00:46 bc250 kernel: amdgpu 0000:01:00.0: Failed to map peer:0000:01:00.0 mem_domain:4
kvě 24 01:00:47 bc250 kernel: amdgpu: amdgpu_vm_bo_update failed
kvě 24 01:00:47 bc250 kernel: amdgpu: update_gpuvm_pte() failed
kvě 24 01:00:47 bc250 kernel: amdgpu: Failed to map bo to gpuvm
kvě 24 01:00:47 bc250 kernel: amdgpu 0000:01:00.0: Failed to map peer:0000:01:00.0 mem_domain:4
kvě 24 01:00:47 bc250 kernel: amdgpu: amdgpu_vm_bo_update failed
kvě 24 01:00:47 bc250 kernel: amdgpu: update_gpuvm_pte() failed
kvě 24 01:00:47 bc250 kernel: amdgpu: Failed to map bo to gpuvm
kvě 24 01:00:47 bc250 kernel: amdgpu 0000:01:00.0: Failed to map peer:0000:01:00.0 mem_domain:4