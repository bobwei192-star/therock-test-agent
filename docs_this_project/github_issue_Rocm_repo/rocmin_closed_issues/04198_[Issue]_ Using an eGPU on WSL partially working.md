# [Issue]: Using an eGPU on WSL partially working

- **Issue #:** 4198
- **State:** closed
- **Created:** 2024-12-24T18:02:44Z
- **Updated:** 2025-01-06T14:56:05Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 GRE, ROCm 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4198

### Problem Description

I'm using an Asus Zenbook S16 that's equipped with a Ryzen AI 9 365, where I've connected a 7900 GRE through an eGPU setup (via USB4). 

I've confirmed that I can run HIP applications via Windows normally (using the ROCM examples, and by disabling the iGPU), but when trying to run this via WSL2, I run into an odd issue. 

Using `rocm-examples` as the testbed, if I try running any of the examples (e.g. `hip_saxpy`), I get the following error and message from the logs

```
:3:rocvirtual.cpp           :3056: 0368660738d us:  ShaderName : _Z12saxpy_kernelfPKfPfj
:1:rocvirtual.cpp           :3103: 0368660788d us:  Pcie atomics not enabled, hostcall not supported
:1:rocvirtual.cpp           :3465: 0368660830d us:  AQL dispatch failed!
:4:command.cpp              :169 : 0368660838d us:  Command 0x324b51d8 complete
:3:hip_module.cpp           :687 : 0368660842d us:  hipLaunchKernel: Returned hipErrorIllegalState :
``` 

Do note that memory transfers work normally, but kernel execution is where the error occurs. What's funny is that if I run a kernel that's been loaded in via RTC (using `hip_runtime_compilation` from `rocm-examples`), it works!

```
:3:rocvirtual.cpp           :3056: 0476093984d us:  ShaderName : saxpy_kernel
:4:rocvirtual.cpp           :905 : 0476093991d us:  SWq=0x7f20902c0000, HWq=0x7f20902d0000, id=1, Dispatch Header = 0xb02 (type=2, barrier=1, acquire=1, release=1), setup=3, grid=[4096, 1, 1], workgroup=[128, 1, 1], private_seg_size=0, group_seg_size=0, kernel_obj=0x7f288fc08880, kernarg_address=0x7f2090580000, completion_signal=0x0, correlation_id=0, rptr=2, wptr=2
:3:hip_module.cpp           :463 : 0476094066d us:  hipModuleLaunchKernel: Returned hipSuccess :
```

Any ideas on how to fix the above via WSL? I've listed my specs, and rocm version below.

### Operating System

Windows 11 (WSL2: Ubuntu 24.04.1 LTS)

### CPU

AMD Ryzen AI 9 365 w/ Radeon 880M

### GPU

AMD Radeon RX 7900 GRE

### ROCm Version

ROCm 6.3.0

### ROCm Component

HIP, ROCm

### Steps to Reproduce

Not sure if you would have the right setup to reproduce this, given the setup I'm using. For the USB4 egpu setup, I'm using an ADT-Link UT4G board which is based off the ASMedia ASM2464PDX chipset.

As for the code reproduction, I'm using `rocm-examples`, specifically any binary compiled under `HIP-Basic`.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
WSL environment detected.
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
Runtime Ext Version:     1.6
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
  Name:                    AMD Ryzen AI 9 365 w/ Radeon 880M
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen AI 9 365 w/ Radeon 880M
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
  Cacheline Size:          64(0x40)
  Internal Node ID:        0
  Compute Unit:            20
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    16378220(0xf9e96c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16378220(0xf9e96c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16378220(0xf9e96c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16378220(0xf9e96c) KB
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
  Marketing Name:          AMD Radeon RX 7900 GRE
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
    L3:                      65536(0x10000) KB
  Chip ID:                 29772(0x744c)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1927
  Internal Node ID:        1
  Compute Unit:            80
  SIMDs per CU:            2
  Shader Engines:          6
  Shader Arrs. per Eng.:   2
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
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 232
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16691368(0xfeb0a8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16691368(0xfeb0a8) KB
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
```

### Additional Information

_No response_