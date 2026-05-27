# MI50 hangs - UBSAN: shift-out-of-bounds

> **Issue #1886**
> **状态**: closed
> **创建时间**: 2023-01-06T20:31:31Z
> **更新时间**: 2024-04-07T20:18:48Z
> **关闭时间**: 2024-04-07T20:18:48Z
> **作者**: alexschroeter
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1886

## 描述

Somewhere recently our MI50 stopped working. All I was able to find so far is this in dmesg:

Same Node also runs MI100 and MI210 successfully. I don't see any hardware errors and this MI50 was working correctly beginning of the week.

[Fri Jan  6 18:42:01 2023] ================================================================================
[Fri Jan  6 18:42:01 2023] UBSAN: shift-out-of-bounds in /var/lib/dkms/amdgpu/5.18.2.22.40-1504718.22.04/build/amd/amdgpu/gfx_v9_0.c:2514:23
[Fri Jan  6 18:42:01 2023] shift exponent 32 is too large for 32-bit type 'unsigned int'
[Fri Jan  6 18:42:01 2023] CPU: 32 PID: 1240 Comm: kworker/32:3 Tainted: P           OE     5.15.0-57-generic #63-Ubuntu
[Fri Jan  6 18:42:01 2023] Hardware name: Supermicro AS -4124GS-TNR/H12DSG-O-CPU, BIOS 2.4 04/22/2022
[Fri Jan  6 18:42:01 2023] Workqueue: events work_for_cpu_fn
[Fri Jan  6 18:42:01 2023] Call Trace:
[Fri Jan  6 18:42:01 2023]  <TASK>
[Fri Jan  6 18:42:01 2023]  show_stack+0x52/0x5c
[Fri Jan  6 18:42:01 2023]  dump_stack_lvl+0x4a/0x63
[Fri Jan  6 18:42:01 2023]  dump_stack+0x10/0x16
[Fri Jan  6 18:42:01 2023]  ubsan_epilogue+0x9/0x49
[Fri Jan  6 18:42:01 2023]  __ubsan_handle_shift_out_of_bounds.cold+0x61/0xef
[Fri Jan  6 18:42:01 2023]  ? amdgpu_device_wreg+0x38/0x50 [amdgpu]
[Fri Jan  6 18:42:01 2023]  gfx_v9_0_setup_rb.cold+0x2a/0x79 [amdgpu]
[Fri Jan  6 18:42:01 2023]  gfx_v9_0_hw_init+0xe2/0x2ee0 [amdgpu]
[Fri Jan  6 18:42:01 2023]  ? smu_hw_init.cold+0x16/0xbd [amdgpu]
[Fri Jan  6 18:42:01 2023]  amdgpu_device_init.cold+0x19ff/0x1f3e [amdgpu]
[Fri Jan  6 18:42:01 2023]  ? pci_bus_read_config_word+0x4a/0x70
[Fri Jan  6 18:42:01 2023]  amdgpu_driver_load_kms+0x1a/0x110 [amdgpu]
[Fri Jan  6 18:42:01 2023]  amdgpu_pci_probe+0x18d/0x3a0 [amdgpu]
[Fri Jan  6 18:42:01 2023]  local_pci_probe+0x4b/0x90
[Fri Jan  6 18:42:01 2023]  ? drm_fb_helper_damage_work+0x94/0x200 [drm_kms_helper]
[Fri Jan  6 18:42:01 2023]  work_for_cpu_fn+0x1a/0x30
[Fri Jan  6 18:42:01 2023]  process_one_work+0x22b/0x3d0
[Fri Jan  6 18:42:01 2023]  worker_thread+0x223/0x420
[Fri Jan  6 18:42:01 2023]  ? process_one_work+0x3d0/0x3d0
[Fri Jan  6 18:42:01 2023]  kthread+0x12a/0x150
[Fri Jan  6 18:42:01 2023]  ? set_kthread_struct+0x50/0x50
[Fri Jan  6 18:42:01 2023]  ret_from_fork+0x22/0x30
[Fri Jan  6 18:42:01 2023]  </TASK>
[Fri Jan  6 18:42:01 2023] ================================================================================

System is Ubuntu 22.04 
Kernel 5.15.0-57-generic #63-Ubuntu SMP Thu Nov 24 13:43:17 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
With ROCm 5.3.3
CPU AMD EPYC 7452 32-Core Processor
https://www.supermicro.com/en/Aplus/system/4U/4124/AS-4124GS-TNR.cfm

<details>
rocminfo
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD EPYC 7452 32-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD EPYC 7452 32-Core Processor
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
  Max Clock Freq. (MHz):   2350
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            64
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    264016376(0xfbc91f8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    264016376(0xfbc91f8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    264016376(0xfbc91f8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    AMD EPYC 7452 32-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD EPYC 7452 32-Core Processor
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             CPU
  Cache Info:
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2350
  BDFID:                   0
  Internal Node ID:        1
  Compute Unit:            64
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    264181660(0xfbf179c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    264181660(0xfbf179c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    264181660(0xfbf179c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 3
*******
  Name:                    gfx90a
  Uuid:                    GPU-21e4cb94e63377ab
  Marketing Name:          AMD Instinct MI210
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
    L2:                      8192(0x2000) KB
  Chip ID:                 29711(0x740f)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1700
  BDFID:                   25344
  Internal Node ID:        2
  Compute Unit:            104
  SIMDs per CU:            4
  Shader Engines:          8
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    67092480(0x3ffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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
*******
Agent 4
*******
  Name:                    gfx906
  Uuid:                    GPU-c88e588172fd62d5
  Marketing Name:          AMD Instinct MI50/MI60
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    3
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      8192(0x2000) KB
  Chip ID:                 26273(0x66a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1725
  BDFID:                   58112
  Internal Node ID:        3
  Compute Unit:            60
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
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
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16760832(0xffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
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
*******
Agent 5
*******
  Name:                    gfx908
  Uuid:                    GPU-22fde47f6f30ba4d
  Marketing Name:          AMD Instinct MI100
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    4
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      8192(0x2000) KB
  Chip ID:                 29580(0x738c)
  ASIC Revision:           2(0x2)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1502
  BDFID:                   49920
  Internal Node ID:        4
  Compute Unit:            120
  SIMDs per CU:            4
  Shader Engines:          8
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
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
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    33538048(0x1ffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx908:sramecc+:xnack-
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
*******
Agent 6
*******
  Name:                    gfx90a
  Uuid:                    GPU-4c3f9530d9c4ca56
  Marketing Name:          AMD Instinct MI210
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    5
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      8192(0x2000) KB
  Chip ID:                 29711(0x740f)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1700
  BDFID:                   33536
  Internal Node ID:        5
  Compute Unit:            104
  SIMDs per CU:            4
  Shader Engines:          8
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    67092480(0x3ffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    67092480(0x3ffc000) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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
*******
Agent 7
*******
  Name:                    gfx90a
  Uuid:                    GPU-4c649cd29ae83b81
  Marketing Name:          AMD Instinct MI210
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    6
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      8192(0x2000) KB
  Chip ID:                 29711(0x740f)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1700
  BDFID:                   41728
  Internal Node ID:        6
  Compute Unit:            104
  SIMDs per CU:            4
  Shader Engines:          8
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    67092480(0x3ffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    67092480(0x3ffc000) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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

sudo /opt/rocm/bin/rocm-smi -a


======================= ROCm System Management Interface =======================
========================= Version of System Component ==========================
Driver version: 5.18.2.22.40
================================================================================
====================================== ID ======================================
GPU[0]          : GPU ID: 0x740f
GPU[1]          : GPU ID: 0x66a1
GPU[2]          : GPU ID: 0x738c
GPU[3]          : GPU ID: 0x740f
GPU[4]          : GPU ID: 0x740f
================================================================================
================================== Unique ID ===================================
GPU[0]          : Unique ID: 0x21e4cb94e63377ab
GPU[1]          : Unique ID: 0xc88e588172fd62d5
GPU[2]          : Unique ID: 0x22fde47f6f30ba4d
GPU[3]          : Unique ID: 0x4c3f9530d9c4ca56
GPU[4]          : Unique ID: 0x4c649cd29ae83b81
================================================================================
==================================== VBIOS =====================================
GPU[0]          : VBIOS version: 113-D67301-063
GPU[1]          : VBIOS version: 113-D1631400-111
GPU[2]          : VBIOS version: 113-D3431401-100
GPU[3]          : VBIOS version: 113-D67301-063
GPU[4]          : VBIOS version: 113-D67301-063
================================================================================
================================= Temperature ==================================
GPU[0]          : Temperature (Sensor edge) (C): 30.0
GPU[0]          : Temperature (Sensor junction) (C): 30.0
GPU[0]          : Temperature (Sensor memory) (C): 44.0
GPU[0]          : Temperature (Sensor HBM 0) (C): 42.0
GPU[0]          : Temperature (Sensor HBM 1) (C): 41.0
GPU[0]          : Temperature (Sensor HBM 2) (C): 44.0
GPU[0]          : Temperature (Sensor HBM 3) (C): 41.0
GPU[1]          : Temperature (Sensor edge) (C): 19.0
GPU[1]          : Temperature (Sensor junction) (C): 21.0
GPU[1]          : Temperature (Sensor memory) (C): 19.0
GPU[1]          : Temperature (Sensor HBM 0) (C): 0.0
GPU[1]          : Temperature (Sensor HBM 1) (C): 0.0
GPU[1]          : Temperature (Sensor HBM 2) (C): 0.0
GPU[1]          : Temperature (Sensor HBM 3) (C): 0.0
GPU[2]          : Temperature (Sensor edge) (C): 26.0
GPU[2]          : Temperature (Sensor junction) (C): 29.0
GPU[2]          : Temperature (Sensor memory) (C): 27.0
GPU[3]          : Temperature (Sensor edge) (C): 23.0
GPU[3]          : Temperature (Sensor junction) (C): 32.0
GPU[3]          : Temperature (Sensor memory) (C): 43.0
GPU[3]          : Temperature (Sensor HBM 0) (C): 43.0
GPU[3]          : Temperature (Sensor HBM 1) (C): 41.0
GPU[3]          : Temperature (Sensor HBM 2) (C): 42.0
GPU[3]          : Temperature (Sensor HBM 3) (C): 40.0
GPU[4]          : Temperature (Sensor edge) (C): 30.0
GPU[4]          : Temperature (Sensor junction) (C): 30.0
GPU[4]          : Temperature (Sensor memory) (C): 42.0
GPU[4]          : Temperature (Sensor HBM 0) (C): 42.0
GPU[4]          : Temperature (Sensor HBM 1) (C): 42.0
GPU[4]          : Temperature (Sensor HBM 2) (C): 40.0
GPU[4]          : Temperature (Sensor HBM 3) (C): 42.0
================================================================================
========================== Current clock frequencies ===========================
GPU[0]          : fclk clock level: 0: (400Mhz)
GPU[0]          : mclk clock level: 3: (1600Mhz)
GPU[0]          : sclk clock level: 1: (800Mhz)
GPU[0]          : socclk clock level: 3: (1090Mhz)
GPU[1]          : dcefclk clock level: 0: (357Mhz)
GPU[1]          : fclk clock level: 0: (550Mhz)
GPU[1]          : mclk clock level: 0: (350Mhz)
GPU[1]          : sclk clock level: 1: (930Mhz)
GPU[1]          : socclk clock level: 0: (309Mhz)
GPU[1]          : pcie clock level: 1 (16.0GT/s x16)
GPU[2]          : fclk clock level: 0: (1402Mhz)
GPU[2]          : mclk clock level: 0: (1200Mhz)
GPU[2]          : sclk clock level: 0: (300Mhz)
GPU[2]          : socclk clock level: 0: (1000Mhz)
GPU[2]          : pcie clock level: 0 (16.0GT/s x16)
GPU[3]          : fclk clock level: 0: (400Mhz)
GPU[3]          : mclk clock level: 3: (1600Mhz)
GPU[3]          : sclk clock level: 1: (800Mhz)
GPU[3]          : socclk clock level: 3: (1090Mhz)
GPU[4]          : fclk clock level: 0: (400Mhz)
GPU[4]          : mclk clock level: 3: (1600Mhz)
GPU[4]          : sclk clock level: 1: (800Mhz)
GPU[4]          : socclk clock level: 3: (1090Mhz)
================================================================================
============================== Current Fan Metric ==============================
GPU[0]          : Unable to detect fan speed for GPU 0
GPU[1]          : Fan Level: 37 (15%)
GPU[1]          : Fan RPM: 0
GPU[2]          : Unable to detect fan speed for GPU 2
GPU[3]          : Unable to detect fan speed for GPU 3
GPU[4]          : Unable to detect fan speed for GPU 4
================================================================================
============================ Show Performance Level ============================
GPU[0]          : Performance Level: auto
GPU[1]          : Performance Level: auto
GPU[2]          : Performance Level: auto
GPU[3]          : Performance Level: auto
GPU[4]          : Performance Level: auto
================================================================================
=============================== OverDrive Level ================================
GPU[0]          : GPU OverDrive value (%): 0
GPU[1]          : GPU OverDrive value (%): 0
GPU[2]          : GPU OverDrive value (%): 0
GPU[3]          : GPU OverDrive value (%): 0
GPU[4]          : GPU OverDrive value (%): 0
================================================================================
=============================== OverDrive Level ================================
GPU[0]          : GPU Memory OverDrive value (%): 0
GPU[1]          : GPU Memory OverDrive value (%): 0
GPU[2]          : GPU Memory OverDrive value (%): 0
GPU[3]          : GPU Memory OverDrive value (%): 0
GPU[4]          : GPU Memory OverDrive value (%): 0
================================================================================
================================== Power Cap ===================================
GPU[0]          : Max Graphics Package Power (W): 300.0
GPU[1]          : Max Graphics Package Power (W): 225.0
GPU[2]          : Max Graphics Package Power (W): 290.0
GPU[3]          : Max Graphics Package Power (W): 300.0
GPU[4]          : Max Graphics Package Power (W): 300.0
================================================================================
============================= Show Power Profiles ==============================
GPU[0]          : Not supported on the given system
GPU[1]          : 1. Available power profile (#1 of 7): CUSTOM
GPU[1]          : 2. Available power profile (#2 of 7): VIDEO
GPU[1]          : 3. Available power profile (#3 of 7): POWER SAVING
GPU[1]          : 4. Available power profile (#4 of 7): COMPUTE
GPU[1]          : 5. Available power profile (#5 of 7): VR
GPU[1]          : 6. Available power profile (#6 of 7): 3D FULL SCREEN
GPU[1]          : 7. Available power profile (#7 of 7): BOOTUP DEFAULT*
GPU[2]          : 1. Available power profile (#1 of 7): CUSTOM
GPU[2]          : 2. Available power profile (#2 of 7): VIDEO
GPU[2]          : 3. Available power profile (#3 of 7): POWER SAVING
GPU[2]          : 4. Available power profile (#4 of 7): COMPUTE
GPU[2]          : 5. Available power profile (#7 of 7): BOOTUP DEFAULT*
GPU[3]          : Not supported on the given system
GPU[4]          : Not supported on the given system
================================================================================
============================== Power Consumption ===============================
GPU[0]          : Average Graphics Package Power (W): 40.0
GPU[1]          : Average Graphics Package Power (W): 15.0
GPU[2]          : Average Graphics Package Power (W): 34.0
GPU[3]          : Average Graphics Package Power (W): 40.0
GPU[4]          : Average Graphics Package Power (W): 42.0
================================================================================
========================= Supported clock frequencies ==========================
GPU[0]          :
GPU[0]          : Supported fclk frequencies on GPU0
GPU[0]          : 0: 400Mhz *
GPU[0]          :
GPU[0]          : Supported mclk frequencies on GPU0
GPU[0]          : 0: 400Mhz
GPU[0]          : 1: 700Mhz
GPU[0]          : 2: 1200Mhz
GPU[0]          : 3: 1600Mhz *
GPU[0]          :
GPU[0]          : Supported sclk frequencies on GPU0
GPU[0]          : 0: 500Mhz
GPU[0]          : 1: 800Mhz *
GPU[0]          : 2: 1700Mhz
GPU[0]          :
GPU[0]          : Supported socclk frequencies on GPU0
GPU[0]          : 0: 666Mhz
GPU[0]          : 1: 857Mhz
GPU[0]          : 2: 1000Mhz
GPU[0]          : 3: 1090Mhz *
GPU[0]          : 4: 1333Mhz
GPU[0]          :
--------------------------------------------------------------------------------
GPU[1]          : Supported dcefclk frequencies on GPU1
GPU[1]          : 0: 357Mhz *
GPU[1]          : 1: 453Mhz
GPU[1]          : 2: 566Mhz
GPU[1]          : 3: 680Mhz
GPU[1]          : 4: 755Mhz
GPU[1]          : 5: 850Mhz
GPU[1]          : 6: 971Mhz
GPU[1]          : 7: 1133Mhz
GPU[1]          :
GPU[1]          : Supported fclk frequencies on GPU1
GPU[1]          : 0: 550Mhz *
GPU[1]          : 1: 610Mhz
GPU[1]          : 2: 690Mhz
GPU[1]          : 3: 760Mhz
GPU[1]          : 4: 870Mhz
GPU[1]          : 5: 960Mhz
GPU[1]          : 6: 1080Mhz
GPU[1]          : 7: 1278Mhz
GPU[1]          :
GPU[1]          : Supported mclk frequencies on GPU1
GPU[1]          : 0: 350Mhz *
GPU[1]          : 1: 800Mhz
GPU[1]          : 2: 1000Mhz
GPU[1]          :
GPU[1]          : Supported sclk frequencies on GPU1
GPU[1]          : 0: 925Mhz
GPU[1]          : 1: 930Mhz *
GPU[1]          : 2: 1032Mhz
GPU[1]          : 3: 1143Mhz
GPU[1]          : 4: 1282Mhz
GPU[1]          : 5: 1386Mhz
GPU[1]          : 6: 1485Mhz
GPU[1]          : 7: 1606Mhz
GPU[1]          : 8: 1725Mhz
GPU[1]          :
GPU[1]          : Supported socclk frequencies on GPU1
GPU[1]          : 0: 309Mhz *
GPU[1]          : 1: 523Mhz
GPU[1]          : 2: 566Mhz
GPU[1]          : 3: 618Mhz
GPU[1]          : 4: 680Mhz
GPU[1]          : 5: 755Mhz
GPU[1]          : 6: 850Mhz
GPU[1]          : 7: 971Mhz
GPU[1]          :
GPU[1]          : Supported PCIe frequencies on GPU1
GPU[1]          : 0: 2.5GT/s x16
GPU[1]          : 1: 16.0GT/s x16 *
GPU[1]          :
--------------------------------------------------------------------------------
GPU[2]          :
GPU[2]          : Supported fclk frequencies on GPU2
GPU[2]          : 0: 1402Mhz *
GPU[2]          :
GPU[2]          : Supported mclk frequencies on GPU2
GPU[2]          : 0: 1200Mhz *
GPU[2]          :
GPU[2]          : Supported sclk frequencies on GPU2
GPU[2]          : 0: 300Mhz *
GPU[2]          : 1: 495Mhz
GPU[2]          : 2: 731Mhz
GPU[2]          : 3: 962Mhz
GPU[2]          : 4: 1029Mhz
GPU[2]          : 5: 1087Mhz
GPU[2]          : 6: 1147Mhz
GPU[2]          : 7: 1189Mhz
GPU[2]          : 8: 1235Mhz
GPU[2]          : 9: 1283Mhz
GPU[2]          : 10: 1319Mhz
GPU[2]          : 11: 1363Mhz
GPU[2]          : 12: 1404Mhz
GPU[2]          : 13: 1430Mhz
GPU[2]          : 14: 1472Mhz
GPU[2]          : 15: 1502Mhz
GPU[2]          :
GPU[2]          : Supported socclk frequencies on GPU2
GPU[2]          : 0: 1000Mhz *
GPU[2]          :
GPU[2]          : Supported PCIe frequencies on GPU2
GPU[2]          : 0: 16.0GT/s x16 *
GPU[2]          :
--------------------------------------------------------------------------------
GPU[3]          :
GPU[3]          : Supported fclk frequencies on GPU3
GPU[3]          : 0: 400Mhz *
GPU[3]          :
GPU[3]          : Supported mclk frequencies on GPU3
GPU[3]          : 0: 400Mhz
GPU[3]          : 1: 700Mhz
GPU[3]          : 2: 1200Mhz
GPU[3]          : 3: 1600Mhz *
GPU[3]          :
GPU[3]          : Supported sclk frequencies on GPU3
GPU[3]          : 0: 500Mhz
GPU[3]          : 1: 800Mhz *
GPU[3]          : 2: 1700Mhz
GPU[3]          :
GPU[3]          : Supported socclk frequencies on GPU3
GPU[3]          : 0: 666Mhz
GPU[3]          : 1: 857Mhz
GPU[3]          : 2: 1000Mhz
GPU[3]          : 3: 1090Mhz *
GPU[3]          : 4: 1333Mhz
GPU[3]          :
--------------------------------------------------------------------------------
GPU[4]          :
GPU[4]          : Supported fclk frequencies on GPU4
GPU[4]          : 0: 400Mhz *
GPU[4]          :
GPU[4]          : Supported mclk frequencies on GPU4
GPU[4]          : 0: 400Mhz
GPU[4]          : 1: 700Mhz
GPU[4]          : 2: 1200Mhz
GPU[4]          : 3: 1600Mhz *
GPU[4]          :
GPU[4]          : Supported sclk frequencies on GPU4
GPU[4]          : 0: 500Mhz
GPU[4]          : 1: 800Mhz *
GPU[4]          : 2: 1700Mhz
GPU[4]          :
GPU[4]          : Supported socclk frequencies on GPU4
GPU[4]          : 0: 666Mhz
GPU[4]          : 1: 857Mhz
GPU[4]          : 2: 1000Mhz
GPU[4]          : 3: 1090Mhz *
GPU[4]          : 4: 1333Mhz
GPU[4]          :
--------------------------------------------------------------------------------
================================================================================
============================== % time GPU is busy ==============================
GPU[0]          : GPU use (%): 0
GPU[0]          : GFX Activity: 6507895
GPU[1]          : GPU use (%): 0
GPU[1]          : GFX Activity: 0
GPU[2]          : GPU use (%): 0
GPU[3]          : GPU use (%): 0
GPU[3]          : GFX Activity: 572
GPU[4]          : GPU use (%): 0
GPU[4]          : GFX Activity: 571
================================================================================
============================== Current Memory Use ==============================
GPU[0]          : GPU memory use (%): 0
GPU[0]          : Memory Activity: 123
GPU[1]          : GPU memory use (%): 0
GPU[1]          : Memory Activity: 0
GPU[2]          : GPU memory use (%): 0
GPU[2]          : Memory Activity: N/A
GPU[3]          : GPU memory use (%): 0
GPU[3]          : Memory Activity: 0
GPU[4]          : GPU memory use (%): 0
GPU[4]          : Memory Activity: 0
================================================================================
================================ Memory Vendor =================================
GPU[0]          : GPU memory vendor: hynix
GPU[1]          : GPU memory vendor: hynix
GPU[2]          : GPU memory vendor: hynix
GPU[3]          : GPU memory vendor: hynix
GPU[4]          : GPU memory vendor: hynix
================================================================================
============================= PCIe Replay Counter ==============================
GPU[0]          : PCIe Replay Count: 0
GPU[1]          : PCIe Replay Count: 0
GPU[2]          : PCIe Replay Count: 0
GPU[3]          : PCIe Replay Count: 0
GPU[4]          : PCIe Replay Count: 0
================================================================================
================================ Serial Number =================================
ERROR: GPU[0]   : FRU Serial Number contains non-alphanumeric characters. FRU is likely corrupted
GPU[1]          : Serial Number: 691939000092
GPU[2]          : Serial Number: 22fde47f6f30ba4d
ERROR: GPU[3]   : FRU Serial Number contains non-alphanumeric characters. FRU is likely corrupted
ERROR: GPU[4]   : FRU Serial Number contains non-alphanumeric characters. FRU is likely corrupted
================================================================================
================================ KFD Processes =================================
No KFD PIDs currently running
================================================================================
============================= GPUs Indexed by PID ==============================
No KFD PIDs currently running
================================================================================
================== GPU Memory clock frequencies and voltages ===================
GPU[0]          : OD_SCLK:
GPU[0]          : 0: 500Mhz
GPU[0]          : 1: 1700Mhz
GPU[0]          : OD_MCLK:
GPU[0]          : 1: 1600Mhz
GPU[0]          : OD_VDDC_CURVE:
GPU[0]          : 0: 0Mhz 0mV
GPU[0]          : 1: 0Mhz 0mV
GPU[0]          : 2: 0Mhz 0mV
GPU[0]          : OD_RANGE:
GPU[0]          : SCLK:     0Mhz        0Mhz
GPU[0]          : MCLK:     0Mhz        0Mhz
GPU[0]          : VDDC_CURVE_SCLK[0]:     0Mhz
GPU[0]          : VDDC_CURVE_VOLT[0]:     0mV
GPU[0]          : VDDC_CURVE_SCLK[1]:     0Mhz
GPU[0]          : VDDC_CURVE_VOLT[1]:     0mV
GPU[0]          : VDDC_CURVE_SCLK[2]:     0Mhz
GPU[0]          : VDDC_CURVE_VOLT[2]:     0mV
GPU[1]          : Not supported on the given system
GPU[2]          : Not supported on the given system
GPU[3]          : OD_SCLK:
GPU[3]          : 0: 500Mhz
GPU[3]          : 1: 1700Mhz
GPU[3]          : OD_MCLK:
GPU[3]          : 1: 1600Mhz
GPU[3]          : OD_VDDC_CURVE:
GPU[3]          : 0: 0Mhz 0mV
GPU[3]          : 1: 0Mhz 0mV
GPU[3]          : 2: 0Mhz 0mV
GPU[3]          : OD_RANGE:
GPU[3]          : SCLK:     0Mhz        0Mhz
GPU[3]          : MCLK:     0Mhz        0Mhz
GPU[3]          : VDDC_CURVE_SCLK[0]:     0Mhz
GPU[3]          : VDDC_CURVE_VOLT[0]:     0mV
GPU[3]          : VDDC_CURVE_SCLK[1]:     0Mhz
GPU[3]          : VDDC_CURVE_VOLT[1]:     0mV
GPU[3]          : VDDC_CURVE_SCLK[2]:     0Mhz
GPU[3]          : VDDC_CURVE_VOLT[2]:     0mV
GPU[4]          : OD_SCLK:
GPU[4]          : 0: 500Mhz
GPU[4]          : 1: 1700Mhz
GPU[4]          : OD_MCLK:
GPU[4]          : 1: 1600Mhz
GPU[4]          : OD_VDDC_CURVE:
GPU[4]          : 0: 0Mhz 0mV
GPU[4]          : 1: 0Mhz 0mV
GPU[4]          : 2: 0Mhz 0mV
GPU[4]          : OD_RANGE:
GPU[4]          : SCLK:     0Mhz        0Mhz
GPU[4]          : MCLK:     0Mhz        0Mhz
GPU[4]          : VDDC_CURVE_SCLK[0]:     0Mhz
GPU[4]          : VDDC_CURVE_VOLT[0]:     0mV
GPU[4]          : VDDC_CURVE_SCLK[1]:     0Mhz
GPU[4]          : VDDC_CURVE_VOLT[1]:     0mV
GPU[4]          : VDDC_CURVE_SCLK[2]:     0Mhz
GPU[4]          : VDDC_CURVE_VOLT[2]:     0mV
================================================================================
=============================== Current voltage ================================
GPU[0]          : Voltage (mV): 793
GPU[1]          : Voltage (mV): 737
GPU[2]          : Voltage (mV): 668
GPU[3]          : Voltage (mV): 793
GPU[4]          : Voltage (mV): 793
================================================================================
================================== PCI Bus ID ==================================
GPU[0]          : PCI Bus: 0000:63:00.0
GPU[1]          : PCI Bus: 0000:E3:00.0
GPU[2]          : PCI Bus: 0000:C3:00.0
GPU[3]          : PCI Bus: 0000:83:00.0
GPU[4]          : PCI Bus: 0000:A3:00.0
================================================================================
============================= Firmware Information =============================
GPU[0]          : ASD firmware version:         0x00000000
GPU[0]          : CE firmware version:          0
GPU[0]          : DMCU firmware version:        0
GPU[0]          : MC firmware version:          0
GPU[0]          : ME firmware version:          0
GPU[0]          : MEC firmware version:         69
GPU[0]          : MEC2 firmware version:        69
GPU[0]          : PFP firmware version:         0
GPU[0]          : RLC firmware version:         17
GPU[0]          : RLC SRLC firmware version:    0
GPU[0]          : RLC SRLG firmware version:    0
GPU[0]          : RLC SRLS firmware version:    0
GPU[0]          : SDMA firmware version:        8
GPU[0]          : SDMA2 firmware version:       8
GPU[0]          : SMC firmware version:         00.68.56.00
GPU[0]          : SOS firmware version:         0x0027007f
GPU[0]          : TA RAS firmware version:      27.00.01.60
GPU[0]          : TA XGMI firmware version:     32.00.00.13
GPU[0]          : UVD firmware version:         0x00000000
GPU[0]          : VCE firmware version:         0x00000000
GPU[0]          : VCN firmware version:         0x0110101b
GPU[1]          : ASD firmware version:         0x21000089
GPU[1]          : CE firmware version:          79
GPU[1]          : DMCU firmware version:        0
GPU[1]          : MC firmware version:          0
GPU[1]          : ME firmware version:          166
GPU[1]          : MEC firmware version:         467
GPU[1]          : MEC2 firmware version:        467
GPU[1]          : PFP firmware version:         194
GPU[1]          : RLC firmware version:         50
GPU[1]          : RLC SRLC firmware version:    1
GPU[1]          : RLC SRLG firmware version:    1
GPU[1]          : RLC SRLS firmware version:    1
GPU[1]          : SDMA firmware version:        145
GPU[1]          : SDMA2 firmware version:       145
GPU[1]          : SMC firmware version:         00.40.60.00
GPU[1]          : SOS firmware version:         0x00080b67
GPU[1]          : TA RAS firmware version:      27.00.01.43
GPU[1]          : TA XGMI firmware version:     32.00.00.02
GPU[1]          : UVD firmware version:         0x42002b13
GPU[1]          : VCE firmware version:         0x39060400
GPU[1]          : VCN firmware version:         0x00000000
GPU[2]          : ASD firmware version:         0x21000059
GPU[2]          : CE firmware version:          0
GPU[2]          : DMCU firmware version:        0
GPU[2]          : MC firmware version:          0
GPU[2]          : ME firmware version:          0
GPU[2]          : MEC firmware version:         63
GPU[2]          : MEC2 firmware version:        63
GPU[2]          : PFP firmware version:         0
GPU[2]          : RLC firmware version:         24
GPU[2]          : RLC SRLC firmware version:    0
GPU[2]          : RLC SRLG firmware version:    0
GPU[2]          : RLC SRLS firmware version:    0
GPU[2]          : SDMA firmware version:        18
GPU[2]          : SDMA2 firmware version:       18
GPU[2]          : SMC firmware version:         00.54.29.00
GPU[2]          : SOS firmware version:         0x0017004f
GPU[2]          : TA RAS firmware version:      27.00.01.37
GPU[2]          : TA XGMI firmware version:     32.00.00.13
GPU[2]          : UVD firmware version:         0x00000000
GPU[2]          : VCE firmware version:         0x00000000
GPU[2]          : VCN firmware version:         0x01101015
GPU[3]          : ASD firmware version:         0x00000000
GPU[3]          : CE firmware version:          0
GPU[3]          : DMCU firmware version:        0
GPU[3]          : MC firmware version:          0
GPU[3]          : ME firmware version:          0
GPU[3]          : MEC firmware version:         69
GPU[3]          : MEC2 firmware version:        69
GPU[3]          : PFP firmware version:         0
GPU[3]          : RLC firmware version:         17
GPU[3]          : RLC SRLC firmware version:    0
GPU[3]          : RLC SRLG firmware version:    0
GPU[3]          : RLC SRLS firmware version:    0
GPU[3]          : SDMA firmware version:        8
GPU[3]          : SDMA2 firmware version:       8
GPU[3]          : SMC firmware version:         00.68.56.00
GPU[3]          : SOS firmware version:         0x0027007f
GPU[3]          : TA RAS firmware version:      27.00.01.60
GPU[3]          : TA XGMI firmware version:     32.00.00.13
GPU[3]          : UVD firmware version:         0x00000000
GPU[3]          : VCE firmware version:         0x00000000
GPU[3]          : VCN firmware version:         0x0110101b
GPU[4]          : ASD firmware version:         0x00000000
GPU[4]          : CE firmware version:          0
GPU[4]          : DMCU firmware version:        0
GPU[4]          : MC firmware version:          0
GPU[4]          : ME firmware version:          0
GPU[4]          : MEC firmware version:         69
GPU[4]          : MEC2 firmware version:        69
GPU[4]          : PFP firmware version:         0
GPU[4]          : RLC firmware version:         17
GPU[4]          : RLC SRLC firmware version:    0
GPU[4]          : RLC SRLG firmware version:    0
GPU[4]          : RLC SRLS firmware version:    0
GPU[4]          : SDMA firmware version:        8
GPU[4]          : SDMA2 firmware version:       8
GPU[4]          : SMC firmware version:         00.68.56.00
GPU[4]          : SOS firmware version:         0x0027007f
GPU[4]          : TA RAS firmware version:      27.00.01.60
GPU[4]          : TA XGMI firmware version:     32.00.00.13
GPU[4]          : UVD firmware version:         0x00000000
GPU[4]          : VCE firmware version:         0x00000000
GPU[4]          : VCN firmware version:         0x0110101b
================================================================================
================================= Product Info =================================
ERROR: GPU[0]   : Unable to read card series
GPU[0]          : Card model:           0x0c34
GPU[0]          : Card vendor:          Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]          : Card SKU:             D67301
GPU[1]          : Card series:          Radeon Instinct MI50 16GB
GPU[1]          : Card model:           0x0834
GPU[1]          : Card vendor:          Advanced Micro Devices, Inc. [AMD/ATI]
GPU[1]          : Card SKU:             D16314
GPU[2]          : Card series:          Arcturus GL-XL [Instinct MI100]
GPU[2]          : Card model:           0x0c34
GPU[2]          : Card vendor:          Advanced Micro Devices, Inc. [AMD/ATI]
GPU[2]          : Card SKU:             D34314
ERROR: GPU[3]   : Unable to read card series
GPU[3]          : Card model:           0x0c34
GPU[3]          : Card vendor:          Advanced Micro Devices, Inc. [AMD/ATI]
GPU[3]          : Card SKU:             D67301
ERROR: GPU[4]   : Unable to read card series
GPU[4]          : Card model:           0x0c34
GPU[4]          : Card vendor:          Advanced Micro Devices, Inc. [AMD/ATI]
GPU[4]          : Card SKU:             D67301
================================================================================
================================== Pages Info ==================================
================================================================================
============================ Show Valid sclk Range =============================
GPU[0]          : Valid sclk range: 500Mhz - 1700Mhz
GPU[1]          : Not supported on the given system
GPU[2]          : Not supported on the given system
GPU[3]          : Valid sclk range: 500Mhz - 1700Mhz
GPU[4]          : Valid sclk range: 500Mhz - 1700Mhz
================================================================================
============================ Show Valid mclk Range =============================
GPU[0]          : Valid mclk range: 400Mhz - 1600Mhz
GPU[1]          : Not supported on the given system
GPU[2]          : Not supported on the given system
GPU[3]          : Valid mclk range: 400Mhz - 1600Mhz
GPU[4]          : Valid mclk range: 400Mhz - 1600Mhz
================================================================================
=========================== Show Valid voltage Range ===========================
ERROR: GPU[0]   : Voltage curve regions unsupported.
GPU[1]          : Not supported on the given system
GPU[2]          : Not supported on the given system
ERROR: GPU[3]   : Voltage curve regions unsupported.
ERROR: GPU[4]   : Voltage curve regions unsupported.
================================================================================
============================= Voltage Curve Points =============================
GPU[0]          : Voltage point 0: 0Mhz 0mV
GPU[0]          : Voltage point 1: 0Mhz 0mV
GPU[0]          : Voltage point 2: 0Mhz 0mV
GPU[1]          : Not supported on the given system
GPU[2]          : Not supported on the given system
GPU[3]          : Voltage point 0: 0Mhz 0mV
GPU[3]          : Voltage point 1: 0Mhz 0mV
GPU[3]          : Voltage point 2: 0Mhz 0mV
GPU[4]          : Voltage point 0: 0Mhz 0mV
GPU[4]          : Voltage point 1: 0Mhz 0mV
GPU[4]          : Voltage point 2: 0Mhz 0mV
================================================================================
=============================== Consumed Energy ================================
GPU[0]          : Energy counter: 25411064577
GPU[0]          : Accumulated Energy (uJ): 388789292874.88
GPU[1]          : Energy counter: 4294967295
GPU[1]          : Accumulated Energy (uJ): 65713000432.7
GPU[2]          : Energy counter: 309511
GPU[2]          : Accumulated Energy (uJ): 4735518.36
GPU[3]          : Energy counter: 25230782310
GPU[3]          : Accumulated Energy (uJ): 386030974155.39
GPU[4]          : Energy counter: 26683913354
GPU[4]          : Accumulated Energy (uJ): 408263879405.75
================================================================================
============================= End of ROCm SMI Log ==============================


</details>

---

## 评论 (3 条)

### 评论 #1 — alexschroeter (2023-01-07T14:37:47Z)

I checked what is happening when I try to run a simple sycl example. Even though this suggests a hardware error when testing a different MI50 the same thing happens. I will try a different slot to make sure it's not that but I don't understand why this would suddenly start.

[Sat Jan  7 14:25:56 2023] amdgpu 0000:e3:00.0: amdgpu: MEM ECC is active.
[Sat Jan  7 14:25:56 2023] amdgpu 0000:e3:00.0: amdgpu: SRAM ECC is active.
[Sat Jan  7 14:25:56 2023] amdgpu 0000:e3:00.0: amdgpu: uncorrectable hardware error(ERREVENT_ATHUB_INTERRUPT) detected!
[Sat Jan  7 14:25:56 2023] amdgpu 0000:e3:00.0: amdgpu: GPU reset begin!
[Sat Jan  7 14:25:56 2023] [drm] UVD VCPU state may lost due to RAS ERREVENT_ATHUB_INTERRUPT
[Sat Jan  7 14:25:59 2023] amdgpu 0000:e3:00.0: amdgpu: Failed to send message 0x26, response 0x0
[Sat Jan  7 14:25:59 2023] amdgpu: [powerplay] Failed to set soft min gfxclk !
[Sat Jan  7 14:25:59 2023] amdgpu: [powerplay] Failed to upload DPM Bootup Levels!
[Sat Jan  7 14:26:04 2023] amdgpu 0000:e3:00.0: amdgpu: Failed to send message 0x7, response 0x0
[Sat Jan  7 14:26:04 2023] amdgpu: [powerplay] [DisableAllSMUFeatures] Failed to disable all smu features!
[Sat Jan  7 14:26:04 2023] amdgpu: [powerplay] [DisableDpmTasks] Failed to disable all smu features!
[Sat Jan  7 14:26:04 2023] amdgpu: [powerplay] [PowerOffAsic] Failed to disable DPM!
[Sat Jan  7 14:26:04 2023] [drm:amdgpu_device_ip_suspend_phase2 [amdgpu]] *ERROR* suspend of IP block <powerplay> failed -5
[Sat Jan  7 14:26:04 2023] amdkcl: cancel_work function is not supported
[Sat Jan  7 14:26:04 2023] amdgpu 0000:e3:00.0: amdgpu: BACO reset
[Sat Jan  7 14:26:08 2023] amdgpu 0000:e3:00.0: amdgpu: Failed to send message 0x25, response 0x0
[Sat Jan  7 14:26:08 2023] amdgpu 0000:e3:00.0: amdgpu: GPU reset succeeded, trying to resume
[Sat Jan  7 14:26:08 2023] [drm] PCIE GART of 512M enabled.
[Sat Jan  7 14:26:08 2023] [drm] PTB located at 0x0000008000000000
[Sat Jan  7 14:26:08 2023] [drm] VRAM is lost due to GPU reset!
[Sat Jan  7 14:26:08 2023] [drm] PSP is resuming...
[Sat Jan  7 14:26:09 2023] [drm:psp_hw_start [amdgpu]] *ERROR* PSP create ring failed!
[Sat Jan  7 14:26:09 2023] [drm:psp_resume [amdgpu]] *ERROR* PSP resume failed
[Sat Jan  7 14:26:09 2023] [drm:amdgpu_device_fw_loading [amdgpu]] *ERROR* resume of IP block <psp> failed -62
[Sat Jan  7 14:26:09 2023] amdgpu 0000:e3:00.0: amdgpu: GPU reset(1) failed
[Sat Jan  7 14:26:18 2023] amdgpu: qcm fence wait loop timeout expired
[Sat Jan  7 14:26:18 2023] amdgpu: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
[Sat Jan  7 14:26:18 2023] amdgpu 0000:e3:00.0: amdgpu: GPU reset end with ret = -62
[Sat Jan  7 14:26:18 2023] amdgpu 0000:e3:00.0: amdgpu: GPU reset begin!
[Sat Jan  7 14:26:20 2023] [drm] psp gfx command UNKNOWN CMD(0xFFFFFFFF) failed and response status is (0xFFFFFFFF)
[Sat Jan  7 14:26:20 2023] [drm] RAS: Unsupported Interface
[Sat Jan  7 14:26:20 2023] amdgpu 0000:e3:00.0: amdgpu: ras disable gfx failed poison:0 ret:-22

---

### 评论 #2 — nartmada (2024-04-07T17:11:50Z)

@alexschroeter, apologies for the delayed response.  Can you please share your repro steps?  Any update on trying a different slot?  Thanks.

---

### 评论 #3 — alexschroeter (2024-04-07T20:18:48Z)

I believe we either returned or replaced the card. It has been too long.

---
