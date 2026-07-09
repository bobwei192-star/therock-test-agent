# [Issue][OMPT]: Data transfers may fail to collect timestamps

- **Issue #:** 6006
- **State:** open
- **Created:** 2026-02-27T15:46:22Z
- **Updated:** 2026-03-12T13:20:31Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6006

### Problem Description

While investigating the current state of the device tracing interface in ROCm v7.2.0 and one of the latest development snapshots of TheRock, I've noticed several tests crashing in the performance measurement infrastructure Score-P.

In all cases, one could see the following warning showing up one or more times:

```
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
```

Checking with ROCm v7.0.0 and earlier, these warnings did not show up.
While not all our tests are affected, we see this behavior for ~10-15 tests. The actual amount of these warnings is dependent both on the test case and program run. It is not deterministic.

Now, the actual crash in Score-P is our fault. I've worked on a [fix](https://perftools.pages.jsc.fz-juelich.de/cicd/scorep/branches/MR704/latest.tar.gz) on our side, which should hopefully get merged soon and also works around #6005.
However, the warning might still be worth investigating, especially as this did not show up in earlier ROCm versions.

### Operating System

Ubuntu 22.04 LTS

### CPU

Intel Core i7-12700

### GPU

AMD Radeon RX 7700 XT

### ROCm Version

ROCm 7.2.0 // TheRock 20260225

### ROCm Component

llvm-project

### Steps to Reproduce

Below, you can find all reproducers triggering the behavior. Note that all samples are taken from the OpenMP Examples, but partially modified to be executable. I don't guarantee that all are entirely correct though:

- [reproducer.zip](https://github.com/user-attachments/files/25608018/reproducer.zip)

To reproduce, I'd recommend attaching any tool which uses the device tracing interface. For simplicity here, I'm using [`ompt-printf`](https://github.com/FZJ-JSC/ompt-printf). We can prepare it like this:

```bash
# Build ompt-printf
git clone https://github.com/FZJ-JSC/ompt-printf.git
cd ompt-printf
cmake -S . -B _build -DCOMPILER_TOOLCHAIN=AMDClang
cmake --build _build
export OMP_TOOL_LIBRARIES=$(pwd)/_build/src/libompt-printf.so
```

Once that is done, we can pick any reproducer, then build and execute it:

```console
$ amdclang -fopenmp --offload-arch=gfx1101 target.5.c
$ for i in $(seq 1 10); do; OMPT_PRINTF_MODE=1 ./a.out; done
```

This should print something like this:

```
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
[-1][ompt_start_tool] Chosen printf mode: 1
AMDGPU message: "unknown or internal error" WARNING Could not retrieve data-copy timestamps: HSA_STATUS_ERROR: A generic error has occurred.
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>Click to open</summary>

```
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    65578992(0x3e8a7f0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65578992(0x3e8a7f0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65578992(0x3e8a7f0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65578992(0x3e8a7f0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1101
  Uuid:                    GPU-1cf1a6db839c29d5
  Marketing Name:          AMD Radeon RX 7700 XT
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
    L2:                      4096(0x1000) KB
    L3:                      49152(0xc000) KB
  Chip ID:                 29822(0x747e)
  ASIC Revision:           0(0x0)
  Cacheline Size:          128(0x80)
  Max Clock Freq. (MHz):   2171
  BDFID:                   768
  Internal Node ID:        1
  Compute Unit:            54
  SIMDs per CU:            2
  Shader Engines:          3
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
  Packet Processor uCode:: 412
  SDMA engine uCode::      25
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    12566528(0xbfc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    12566528(0xbfc000) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx1101
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
```

</details>

### Additional Information

CC @jplehr