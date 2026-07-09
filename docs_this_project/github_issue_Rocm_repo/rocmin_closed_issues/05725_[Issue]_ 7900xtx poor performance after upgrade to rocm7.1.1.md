# [Issue]: 7900xtx poor performance after upgrade to rocm7.1.1

- **Issue #:** 5725
- **State:** closed
- **Created:** 2025-11-29T16:26:57Z
- **Updated:** 2026-04-07T04:45:48Z
- **Labels:** status: fix submitted
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5725

### Problem Description

I'm experiencing a major performance degradation on my RX 7900 XTX when running a PyTorch performance [benchmark](https://github.com/zzc0721/torch-performance-test-data) with ROCm 7.1.1, compared to the performance on ROCm 6.4.

Key Observations:

- **Counter-intuitive Clock Speeds**: With ROCm 7.1.1, the SCLK correctly boosts to 2.8-2.9 GHz during the test. However, with the better-performing ROCm 6.4, the SCLK only reaches 2.1 GHz. Higher clocks are resulting in lower performance.
- **rocblas Library Size Discrepancy**: The rocblas library bundled with the PyTorch environment for ROCm 6.4 is significantly larger than the system-wide rocblas library provided by ROCm 7.1.1.

```shell
➜  ~ ls -lSh /home/xxx/miniconda3/envs/rocm6/lib/python3.13/site-packages/torch/lib/rocblas/library | grep gfx1100 |wc -l
96
➜  ~ ls -lhS /opt/rocm-7.1.1/lib/rocblas/library/ | grep gfx1100 |wc -l
96
➜  ~ du -sh /home/xxx/miniconda3/envs/rocm6/lib/python3.13/site-packages/torch/lib/rocblas/library
3.3G    /home/yfy/miniconda3/envs/rocm6/lib/python3.13/site-packages/torch/lib/rocblas/library
➜  ~ du -sh /opt/rocm-7.1.1/lib/rocblas/library/
651M    /opt/rocm-7.1.1/lib/rocblas/library/
```

### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

AMD Ryzen 9 5950X 16-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 7.1.1

### ROCm Component

rocBLAS

### Steps to Reproduce

1. install rocm 7.1.1 and AMD driver according: https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/native_linux/install-radeon.html

2. create conda py13 env and install pytorch using wheel package

```shell
pip3 install https://repo.radeon.com/rocm/manylinux/rocm-rel-7.1.1/triton-3.5.1%2Brocm7.1.1.gita272dfa8-cp313-cp313-linux_x86_64.whl
pip3 install https://repo.radeon.com/rocm/manylinux/rocm-rel-7.1.1/torch-2.9.1%2Brocm7.1.1.lw.git351ff442-cp313-cp313-linux_x86_64.whl
pip3 install https://repo.radeon.com/rocm/manylinux/rocm-rel-7.1.1/torchvision-0.24.0%2Brocm7.1.1.gitb919bd0c-cp313-cp313-linux_x86_64.whl
```

OR just using pytorch docker image `rocm/pytorch:rocm7.1.1_ubuntu24.04_py3.12_pytorch_release_2.9.1`

3. run performance testing

```shell
git clone https://github.com/zzc0721/torch-performance-test-data

python test.py
```

4. get abnormal performance

e.g
```
2.9.1+rocm7.1.1.git351ff442
FP32: 3.35 TFLOPS | TF32: 3.30 TFLOPS | FP16: 79.16 TFLOPS | BF16: 79.98 TFLOPS
```

with rocm6.4
```
2.9.1+rocm6.4
FP32: 26.68 TFLOPS | TF32: 26.05 TFLOPS | FP16: 105.22 TFLOPS | BF16: 102.08 TFLOPS
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

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
  Name:                    AMD Ryzen 9 5950X 16-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 9 5950X 16-Core Processor
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
    L1:                      65536(0x10000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   0
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
      Size:                    49301900(0x2f0498c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    49301900(0x2f0498c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    49301900(0x2f0498c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    49301900(0x2f0498c) KB
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
  Uuid:                    GPU-a56d387a32cf2cbb
  Marketing Name:          Radeon RX 7900 XTX
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
    L3:                      98304(0x18000) KB
  Chip ID:                 29772(0x744c)
  ASIC Revision:           0(0x0)
  Cacheline Size:          128(0x80)
  Max Clock Freq. (MHz):   2526
  BDFID:                   512
  Internal Node ID:        1
  Compute Unit:            96
  SIMDs per CU:            2
  Shader Engines:          6
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
  Packet Processor uCode:: 602
  SDMA engine uCode::      27
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    25149440(0x17fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB
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

_No response_