# [Issue]: Fail to verify PyTorch installation via PIP on WSL according to the official guide

- **Issue #:** 4881
- **State:** open
- **Created:** 2025-06-04T12:33:34Z
- **Updated:** 2025-07-02T17:53:16Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4881

### Problem Description

After install ROCm & PyTorch in Windows 11 WSL (with Ubuntu 24.04 inside) according to the official guide ([rocm](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html) & [torch](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-pytorch.html)), I cannot verify the installation:
+ Problem 1: When execute `python3 -m torch.utils.collect_env`, it reported
```
<frozen runpy>:128: RuntimeWarning: 'torch.utils.collect_env' found in sys.modules after import of package 'torch.utils', but prior to execution of 'torch.utils.collect_env'; this may result in unpredictable behaviour
Collecting environment information...
```
And then it got stucked, print nothing, and cannot terminate by Ctrl+C. Ctrl+Z still worked.
+ Problem 2: When execute `python3 -c "import torch; print(f'device name [0]:', torch.cuda.get_device_name(0))"`, there was no reponse, and the program cannot be terminated by Ctrl+C. Ctrl+Z still worked.
+ `rocm-smi` does not work, but `rocminfo` works.
+ If I run a simple Python Program: 
```
import torch
print(torch.cuda.is_available())
a = torch.tensor([1,2,3])
a = a.to("cuda")
print(a)
```
It will print somthing strange:
```
True
tensor([1, 2, 3], device='cuda:0')
pid:1643 tid:0x74b897e49080 [~VaMgr] free_list_ size is not 1.
pid:1643 tid:0x74b897e49080 [~VaMgr] frag_map_ size is not 1.
```
The last two lines seems to be abnormal. I wonder how can I fix these problems.

It should be mentioned that:
- In the last step of installing PyTorch, the guide asked me to execute `cp /opt/rocm/lib/libhsa-runtime64.so.1.2 libhsa-runtime64.so`
- However, `/opt/rocm/lib/libhsa-runtime64.so.1.2` did not exist, so I used `/opt/rocm/lib/libhsa-runtime64.so.1.14.0` instead.

Other information which may be relevant:
- The driver used was AMD Software: Adrenalin Edition 25.3.1 on Windows.
- I did not try Docker method since I cannot pull docker images due to network problems.

### Operating System

Windows 11 with WSL (Ubuntu 24.04.2 LTS installed in WSL)

### CPU

AMD Ryzen 7 9700X 8-Core Processor

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.3.4

### ROCm Component

_No response_

### Steps to Reproduce

In a newly install WSL with ubuntu 24.04: 
1. Install Raedon software according to: https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html
2. Install PyTorch via PIP according to: https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-pytorch.html, but the last step modified as described above.
3. Run `python3 -c "import torch; print(f'device name [0]:', torch.cuda.get_device_name(0))"` or `python3 -m torch.utils.collect_env` according to official guide.

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
  Name:                    AMD Ryzen 7 9700X 8-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 7 9700X 8-Core Processor
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
  Compute Unit:            16
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    24144080(0x17068d0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    24144080(0x17068d0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    24144080(0x17068d0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    24144080(0x17068d0) KB
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
  Marketing Name:          AMD Radeon RX 7900 XT
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
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2175
  Internal Node ID:        1
  Compute Unit:            84
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
  Packet Processor uCode:: 372
  SDMA engine uCode::      24
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    20884136(0x13eaaa8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    20884136(0x13eaaa8) KB
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