# [Issue]: 100% GPU usage and high power draw during idle after memcpy/memset with HIP streams on RDNA3

- **Issue #:** 2625
- **State:** closed
- **Created:** 2023-11-02T16:07:24Z
- **Updated:** 2026-05-03T02:09:29Z
- **Labels:** Under Investigation, 5.7.1
- **URL:** https://github.com/ROCm/ROCm/issues/2625

### Problem Description

When running llama.cpp's server example on ROCm, using an RDNA3 GPU, GPU usage is shown as 100% and a high power consumption is measured at the wall outlet, even with the server at idle.

Investigating further, it seems that the issue is related to HIP stream usage: GPU usage first shoots up to persistent 100% when llama.cpp tries to create its second HIP stream. If I limit llama.cpp to use only a single stream, then GPU load behaves normally until it begins writing into GPU memory using hipMemcpy or hipMemset, at which point it permanently jumps up to 100%, and stays there until llama.cpp is closed.

In minimal testcases, the following scenarios all yielded 100% GPU usage, despite never actually executing any user code on the GPU:

- Creating a HIP stream while another HIP stream is open. Once triggered, closing the HIP streams doesn't help. (If I open a stream and close it, then open another one, with no overlap in time between the 2 streams, the issue isn't seen.)
- Writing to GPU memory while a HIP stream is open. Once triggered, neither closing the HIP stream nor deallocating the memory previously written will cause the GPU load to come down, only killing the process helps. (If I close the stream before writing to GPU memory, the issue isn't seen, even if that memory was allocated before or during the stream's lifetime.)
- Creating a HIP stream after **any** GPU memory write has taken place, _even if the previously written memory is freed_ before the stream is created. Once triggered, closing the HIP stream doesn't help.

I've attached minimal testcases, as well as strace logs for each of them.

### Operating System

Ubuntu 22.04.3 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 5 4500 6-Core Processor

### GPU

Radeon RX 7900 XT (gfx1100)

### ROCm Version

5.7.1

### ROCm Component

hipBLAS, rocBLAS or amdgpu kernel driver(?)

### Steps to Reproduce

Execute any of the reproX.cpp testcases like this:
`hipcc reproX.cpp; ./a.out`
and watch the output of rocm-smi, or a physical power meter.

Using the noreproX.cpp testcases, normal behavior (no persistent 100% GPU load) is observed.

(The files are renamed to a ".txt" extension because of GitHub's extension filter.)

[norepro1.cpp](https://github.com/RadeonOpenCompute/ROCm/files/13242036/norepro1.cpp.txt)
[norepro1.strace](https://github.com/RadeonOpenCompute/ROCm/files/13242037/norepro1.strace.txt)
[norepro2.cpp](https://github.com/RadeonOpenCompute/ROCm/files/13242038/norepro2.cpp.txt)
[norepro2.strace](https://github.com/RadeonOpenCompute/ROCm/files/13242039/norepro2.strace.txt)
[repro1.cpp](https://github.com/RadeonOpenCompute/ROCm/files/13242040/repro1.cpp.txt)
[repro1.strace](https://github.com/RadeonOpenCompute/ROCm/files/13242041/repro1.strace.txt)
[repro2.cpp](https://github.com/RadeonOpenCompute/ROCm/files/13242042/repro2.cpp.txt)
[repro2.strace](https://github.com/RadeonOpenCompute/ROCm/files/13242043/repro2.strace.txt)
[repro3.cpp](https://github.com/RadeonOpenCompute/ROCm/files/13242044/repro3.cpp.txt)
[repro3.strace](https://github.com/RadeonOpenCompute/ROCm/files/13242045/repro3.strace.txt)


### Output of /opt/rocm/bin/rocminfo --support

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
  Name:                    AMD Ryzen 5 4500 6-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 5 4500 6-Core Processor
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
  Max Clock Freq. (MHz):   4208
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            12
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    32722432(0x1f34e00) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32722432(0x1f34e00) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    32722432(0x1f34e00) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1100
  Uuid:                    GPU-22a3388da1ef8d2a
  Marketing Name:          Radeon RX 7900 XT
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
    L3:                      81920(0x14000) KB
  Chip ID:                 29772(0x744c)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2025
  BDFID:                   768
  Internal Node ID:        1
  Compute Unit:            84
  SIMDs per CU:            2
  Shader Engines:          6
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
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
  Packet Processor uCode:: 546
  SDMA engine uCode::      19
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    20955136(0x13fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS:
      Size:                    20955136(0x13fc000) KB
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