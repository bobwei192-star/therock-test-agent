# [Issue]: ROCm 6.4 -> ROCm 7.1 GEMM fp32 kernel regression

- **Issue #:** 5805
- **State:** open
- **Created:** 2025-12-19T21:14:24Z
- **Updated:** 2026-04-20T13:55:57Z
- **Labels:** Under Investigation, status: assessed
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5805

### Problem Description

This is forked from https://github.com/ROCm/ROCm/issues/5674#issuecomment-3668793386. Opened on behalf of @briansp2020

rocm/pytorch:rocm7.1.1_ubuntu24.04_py3.12_pytorch_release_2.7.1 text processing is slow. 

Performance of ROCm 7.1

````
root@rocm:~# PYTORCH_MIOPEN_SUGGEST_NHWC=0 python /pwd/Downloads/quickstart.py
/opt/venv/lib/python3.12/site-packages/apex/transformer/functional/fused_rope.py:54: UserWarning: Using the native apex kernel for RoPE.
  warnings.warn("Using the native apex kernel for RoPE.", UserWarning)
CUDA is available! PyTorch can use your GPU.
Number of GPUs available: 1
GPU Name: Radeon RX 7900 XTX
/opt/venv/lib/python3.12/site-packages/torchvision/models/_utils.py:208: UserWarning: The parameter 'pretrained' is deprecated since 0.13 and may be removed in the future, please use 'weights' instead.
  warnings.warn(
/opt/venv/lib/python3.12/site-packages/torchvision/models/_utils.py:223: UserWarning: Arguments other than a weight enum or `None` for 'weights' are deprecated since 0.13 and may be removed in the future. The current behavior is equivalent to passing `weights=ConvNeXt_Small_Weights.IMAGENET1K_V1`. You can also use `weights=ConvNeXt_Small_Weights.DEFAULT` to get the most up-to-date weights.
  warnings.warn(msg)
epoch     train_loss  valid_loss  error_rate  time
0         0.113572    0.000550    0.000000    00:32
epoch     train_loss  valid_loss  error_rate  time
0         0.021682    0.003351    0.001353    00:45
Training text processing model
epoch     train_loss  valid_loss  accuracy  time
0         0.463307    0.410007    0.814280  01:09
epoch     train_loss  valid_loss  accuracy  time
0         0.301669    0.253234    0.897920  02:53
1         0.234085    0.203753    0.919200  02:50

```

Performance of ROCm 6.4
```
(pt) root@rocm:~# python tmp/quickstart.py
/root/pt/lib/python3.10/site-packages/torchvision/models/_utils.py:208: UserWarning: The parameter 'pretrained' is deprecated since 0.13 and may be removed in the future, please use 'weights' instead.
  warnings.warn(
/root/pt/lib/python3.10/site-packages/torchvision/models/_utils.py:223: UserWarning: Arguments other than a weight enum or `None` for 'weights' are deprecated since 0.13 and may be removed in the future. The current behavior is equivalent to passing `weights=ConvNeXt_Small_Weights.IMAGENET1K_V1`. You can also use `weights=ConvNeXt_Small_Weights.DEFAULT` to get the most up-to-date weights.
  warnings.warn(msg)
epoch     train_loss  valid_loss  error_rate  time
0         0.117716    0.001144    0.000677    00:35
epoch     train_loss  valid_loss  error_rate  time
0         0.013864    0.000865    0.000677    00:48
Training text processing model
epoch     train_loss  valid_loss  accuracy  time
0         0.464525    0.385803    0.827080  01:09
epoch     train_loss  valid_loss  accuracy  time
0         0.289083    0.221270    0.913160  02:03
1         0.228864    0.199963    0.922200  02:04
```

### Operating System

Ubuntu 24.04

### CPU

AMD Ryzen 9 9900X 12-Core Processor

### GPU

AMD Radeon AI PRO R9700

### ROCm Version

7.1

### ROCm Component

_No response_

### Steps to Reproduce

docker pull rocm/pytorch:rocm7.1_ubuntu22.04_py3.10_pytorch_release_2.8.0
drun --name pt rocm/pytorch:rocm7.1_ubuntu22.04_py3.10_pytorch_release_2.8.0

cd
git clone https://github.com/fastai/fastai
pip install -e "fastai[dev]"
python quickstart.py

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

/opt/rocm/bin/rocminfo --support
ROCk module version 6.16.6 is loaded
HSA System Attributes
Runtime Version: 1.18
Runtime Ext Version: 1.14
System Timestamp Freq.: 1000.000000MHz
Sig. Max Wait Duration: 18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model: LARGE
System Endianness: LITTLE
Mwaitx: DISABLED
XNACK enabled: NO
DMAbuf Support: YES
VMM Support: YES

==========
HSA Agents
Agent 1

Name: AMD Ryzen 9 9900X 12-Core Processor
Uuid: CPU-XX
Marketing Name: AMD Ryzen 9 9900X 12-Core Processor
Vendor Name: CPU
Feature: None specified
Profile: FULL_PROFILE
Float Round Mode: NEAR
Max Queue Number: 0(0x0)
Queue Min Size: 0(0x0)
Queue Max Size: 0(0x0)
Queue Type: MULTI
Node: 0
Device Type: CPU
Cache Info:
L1: 49152(0xc000) KB
Chip ID: 0(0x0)
ASIC Revision: 0(0x0)
Cacheline Size: 64(0x40)
Max Clock Freq. (MHz): 5662
BDFID: 0
Internal Node ID: 0
Compute Unit: 24
SIMDs per CU: 0
Shader Engines: 0
Shader Arrs. per Eng.: 0
WatchPts on Addr. Ranges:1
Memory Properties:
Features: None
Pool Info:
Pool 1
Segment: GLOBAL; FLAGS: FINE GRAINED
Size: 65488328(0x3e745c8) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
Pool 2
Segment: GLOBAL; FLAGS: EXTENDED FINE GRAINED
Size: 65488328(0x3e745c8) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
Pool 3
Segment: GLOBAL; FLAGS: KERNARG, FINE GRAINED
Size: 65488328(0x3e745c8) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
Pool 4
Segment: GLOBAL; FLAGS: COARSE GRAINED
Size: 65488328(0x3e745c8) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
ISA Info:

Agent 2

Name: gfx1201
Uuid: GPU-b84b4aa8c7598291
Marketing Name: AMD Radeon AI PRO R9700
Vendor Name: AMD
Feature: KERNEL_DISPATCH
Profile: BASE_PROFILE
Float Round Mode: NEAR
Max Queue Number: 128(0x80)
Queue Min Size: 64(0x40)
Queue Max Size: 131072(0x20000)
Queue Type: MULTI
Node: 1
Device Type: GPU
Cache Info:
L1: 32(0x20) KB
L2: 8192(0x2000) KB
L3: 65536(0x10000) KB
Chip ID: 30033(0x7551)
ASIC Revision: 1(0x1)
Cacheline Size: 256(0x100)
Max Clock Freq. (MHz): 2350
BDFID: 768
Internal Node ID: 1
Compute Unit: 64
SIMDs per CU: 2
Shader Engines: 4
Shader Arrs. per Eng.: 2
WatchPts on Addr. Ranges:4
Coherent Host Access: FALSE
Memory Properties:
Features: KERNEL_DISPATCH
Fast F16 Operation: TRUE
Wavefront Size: 32(0x20)
Workgroup Max Size: 1024(0x400)
Workgroup Max Size per Dimension:
x 1024(0x400)
y 1024(0x400)
z 1024(0x400)
Max Waves Per CU: 32(0x20)
Max Work-item Per CU: 1024(0x400)
Grid Max Size: 4294967295(0xffffffff)
Grid Max Size per Dimension:
x 2147483647(0x7fffffff)
y 65535(0xffff)
z 65535(0xffff)
Max fbarriers/Workgrp: 32
Packet Processor uCode:: 108
SDMA engine uCode:: 662
IOMMU Support:: None
Pool Info:
Pool 1
Segment: GLOBAL; FLAGS: COARSE GRAINED
Size: 33406976(0x1fdc000) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:2048KB
Alloc Alignment: 4KB
Accessible by all: FALSE
Pool 2
Segment: GROUP
Size: 64(0x40) KB
Allocatable: FALSE
Alloc Granule: 0KB
Alloc Recommended Granule:0KB
Alloc Alignment: 0KB
Accessible by all: FALSE
ISA Info:
ISA 1
Name: amdgcn-amd-amdhsa--gfx1201
Machine Models: HSA_MACHINE_MODEL_LARGE
Profiles: HSA_PROFILE_BASE
Default Rounding Mode: NEAR
Default Rounding Mode: NEAR
Fast f16: TRUE
Workgroup Max Size: 1024(0x400)
Workgroup Max Size per Dimension:
x 1024(0x400)
y 1024(0x400)
z 1024(0x400)
Grid Max Size: 4294967295(0xffffffff)
Grid Max Size per Dimension:
x 2147483647(0x7fffffff)
y 65535(0xffff)
z 65535(0xffff)
FBarrier Max Size: 32
ISA 2
Name: amdgcn-amd-amdhsa--gfx12-generic
Machine Models: HSA_MACHINE_MODEL_LARGE
Profiles: HSA_PROFILE_BASE
Default Rounding Mode: NEAR
Default Rounding Mode: NEAR
Fast f16: TRUE
Workgroup Max Size: 1024(0x400)
Workgroup Max Size per Dimension:
x 1024(0x400)
y 1024(0x400)
z 1024(0x400)
Grid Max Size: 4294967295(0xffffffff)
Grid Max Size per Dimension:
x 2147483647(0x7fffffff)
y 65535(0xffff)
z 65535(0xffff)
FBarrier Max Size: 32
*** Done ***

### Additional Information

_No response_