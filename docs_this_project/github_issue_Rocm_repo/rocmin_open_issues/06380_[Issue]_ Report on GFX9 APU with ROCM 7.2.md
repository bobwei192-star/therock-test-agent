# [Issue]: Report on GFX9 APU with ROCM 7.2

- **Issue #:** 6380
- **State:** open
- **Created:** 2026-06-24T06:43:35Z
- **Updated:** 2026-06-25T15:22:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/6380

### Problem Description

/proc/cmdline
```
initrd=\EFI\nixos\jx9z8afn8nd9df3fivdiz6z6nly1klic-initrd-linux-7.1.1-initrd.efi init=/nix/store/62ia5360d5sih24mfc5v93rkzcascqrh-nixos-system-DESKTOP-LNAWHND-26.11.20260623.9e09bc1/init ttm.pages_limit=778240 ttm.page_pool_size=778240 amdgpu.enforce_isolation=1 amd_iommu=pgtbl_v2 iommu.strict=1 iommu=pt pci=big_root_window amdgpu.vm_update_mode=3 amdgpu.vm_fragment_size=4 amd_iommu_dump mem_sleep_default=s2idle amdgpu.tmz=0 processor.max_cstate=5 nvme_core.default_ps_max_latency_us=0 pcie_aspm=off quiet splash boot.shell_on_fail udev.log_priority=3 rd.systemd.show_status=auto root=fstab loglevel=3 lsm=landlock,yama,bpf
```

<details>


<summary>python ./test_gfx_support.py (second run)</summary>

```
============================================================
  Level 1 — CPU Basics
============================================================
  [PASS] Import torch  (v2.11.0)
  [PASS] Tensor creation
  [PASS] Element-wise add
  [PASS] CPU matmul (64x64)
  [PASS] Autograd (dy/dx of x²)

============================================================
  Level 2 — Device Detection
============================================================
  [PASS] GPU available (torch.cuda)  (ROCm/HIP)
  [PASS] Device count  (1)
  [PASS] GPU 0 properties  (AMD Radeon Vega 3 Graphics — 3.0 GB, SM/CU 3)
  [PASS] Runtime version  (7.2.53211)

============================================================
  Level 3 — GPU Fundamentals
============================================================
  [PASS] Tensor on GPU
  [PASS] CPU→GPU transfer
  [PASS] GPU→CPU transfer
  [PASS] GPU arithmetic (512x512)
  [PASS] GPU memory alloc/free  (peak 19.2 MB → 3.2 MB)

============================================================
  Level 4 — Intermediate Compute
============================================================
  [PASS] Large matmul (1024x1024)  (472.06 ms)
  [PASS] Batched matmul (8x512x512)
  [PASS] Einsum (bij,bjk->bik)
  [PASS] NN forward pass (MLP)
  [PASS] NN backward pass  (loss=2.3123)
  [PASS] Float16 matmul (1024²)
  [PASS] BFloat16 matmul (1024²)

============================================================
  Level 5 — Intermediate System
============================================================
  [PASS] CUDA streams
  [PASS] Stream synchronization
  [PASS] Pinned memory transfer  (1.15 ms)
  [PASS] DNN backend available  (MIOpen)
  [SKIP] Multi-GPU P2P access  (single GPU)
  [PASS] Conv2d forward (DNN backend)  (70.88 ms)
  [PASS] torch.compile

============================================================
  Summary
============================================================
  Total : 28
  PASS  : 27
  FAIL  : 0
  SKIP  : 1
```

</details>

### Operating System

NixOS 26.11

### CPU

AMD Ryzen 3 3250U with Radeon Graphics

### GPU

Raven2, gfx902, integrated graphics

### ROCm Version

7.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>

<summary>rocminfo --support output</summary>

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
XNACK enabled:           YES
DMAbuf Support:          YES
VMM Support:             YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 3 3250U with Radeon Graphics
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 3 3250U with Radeon Graphics
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
  Max Clock Freq. (MHz):   2600
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            4
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    8000524(0x7a140c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    8000524(0x7a140c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    8000524(0x7a140c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8000524(0x7a140c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx902
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon Vega 3 Graphics
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
    L2:                      1024(0x400) KB
  Chip ID:                 5592(0x15d8)
  ASIC Revision:           9(0x9)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1200
  BDFID:                   1280
  Internal Node ID:        1
  Compute Unit:            3
  SIMDs per CU:            4
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:       APU
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    2560(0xa00)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)
    y                        65535(0xffff)
    z                        65535(0xffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 472
  SDMA engine uCode::      169
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    3112960(0x2f8000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    3112960(0x2f8000) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx902:xnack+
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
      Name:                    amdgcn-amd-amdhsa--gfx9-generic:xnack+
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

</details>


### Additional Information

_No response_