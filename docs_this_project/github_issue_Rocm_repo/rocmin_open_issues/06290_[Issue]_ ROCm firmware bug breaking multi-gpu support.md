# [Issue]: ROCm firmware bug breaking multi-gpu support

- **Issue #:** 6290
- **State:** open
- **Created:** 2026-05-21T18:08:16Z
- **Updated:** 2026-06-05T16:51:40Z
- **Labels:** status: triage
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6290

### Problem Description

Was assisting a user named Jose in lemonadeSDK discord who has a multi-gpu setup that would crash via certain settings. Turns out to be a ROCm firmware issue.

"1. The Core Culprit: ROCm Memory Allocator & P2P
The most common crash on multi-GPU AMD setups presents a terrifying system log error that looks like this:
Memory access fault by GPU node-1... Reason: Page not present or supervisor privilege.

What's actually happening: When llama.cpp uses --split-mode tensor or transfers data between multiple cards, it relies on ROCm's Peer-to-Peer (P2P) memory access over the PCIe bus.

The ROCm Bug: ROCm’s memory management unit often gets confused about VRAM vs. GTT (System RAM mapped for GPU access) partitioning when handling multi-GPU allocations, especially if the cards are running at mismatched speeds (like their x16 / x4 setup) or if an integrated GPU (iGPU) is active on the CPU. The driver attempts to access unmapped memory space, panics, and dumps the core.

2. The linux-firmware Regression Bug
There is a massive, widely documented bug tracking across the open-source community regarding a regression in the linux-firmware-amdgpu package.

The Root Cause: Recent driver updates introduced a critical bug in the graphics microcode (specifically the MES component that handles hardware scheduling and memory isolation). It triggers a severe memory protection fault (GCVM_L2_PROTECTION_FAULT_STATUS) when LLM inference applications spin up multi-backend threads.

The Blame: Completely on the AMD kernel firmware team. llama.cpp is just executing valid HIP API calls; the underlying firmware is what's failing to safely execute them."

### Operating System

CachyOS

### CPU

9850X3D

### GPU

Dual 9070XT

### ROCm Version

7.14.0a20260519, 7.2.3

### ROCm Component

ROCR-Runtime

### Steps to Reproduce

---
### Steps to Reproduce

1. **Hardware Setup:**
* Mainboard: MSI MAG X870E TOMAHAWK WIFI.
* GPU 0: AMD Radeon RX 9070 XT (16GB VRAM) seated in PCI_E1 slot (CPU-attached PCIe 5.0 x16).
* GPU 1: AMD Radeon RX 9070 XT (16GB VRAM) seated in PCI_E3 slot (Chipset-attached PCIe 4.0 x4).


2. **Software Environment:**
* OS: CachyOS (Arch Linux-based, rolling kernel release).
* Host Driver Runtime: ROCm 7.2.3.
* Application Runtime: llama-server compiled against a bleeding-edge alpha nightlies bundle (ROCm 7.14.0a20260519).


3. **Execution Command:**
Execute llama-server attempting a standard tensor-split cross-GPU memory allocation for a high-parameter model (e.g., Qwen3.6-35B APEX GGUF):
```bash
llama-server --split-mode tensor --tensor-split 1,1 --main-gpu 0 --flash-attn on --reasoning on -c 4096 -b 2048 -ub 2048 --fit off --no-mmap --n-cpu-moe 2 -np 1 --model /path/to/Qwen3.6-35B-A3B-APEX-I-Quality.gguf


```



```

4. **Trigger Condition:**
   Observe the server initiation loop during the initial tensor load phase (load_all_data) as the runtime attempts to set and pin buffers across the asymmetrical PCIe paths.

---

### Expected Behavior
llama-server should cleanly load model weights using the user-defined split across both matching 16GB cards, allocating context frames inside unified memory bounds without hardware-level faults.

### Actual Behavior
The application experiences an immediate segmentation fault and core dump during weight instantiation (ggml_backend_cuda_buffer_set_tensor). The kernel flags a direct memory access page fault over the chipset-bound GPU node:

```text
Memory access fault by GPU node-1 (Agent handle: 0x5583c3f11fc0) on address 0x7f51f2dff000. 
Reason: Page not present or supervisor privilege.
...
Stack trace of thread 1827250:
#12 0x00007f5aa765cd00 _ZL35ggml_backend_cuda_buffer_set_tensorP19ggml_backend_bufferP11ggml_tensorPKvmm (libggml-hip.so)
#13 0x00007f5ab1573401 ggml_backend_tensor_set_2d (libggml-base.so.0)
#14 0x00007f5ab1583af7 _ZL35ggml_backend_meta_buffer_set_tensorP19ggml_backend_bufferP11ggml_tensorPKvmm (libggml-base.so.0)
#15 0x00007f5ab134911d _ZN18llama_model_loader13load_all_dataEP12ggml_context... (libllama.so.0)

```

---

> **footnote**: *"The crash appears tied to memory mapping discrepancies between alpha userspace libraries (7.14.x) interacting with stable host driver interfaces (7.2.3), severely aggravated by the asymmetrical PCIe topology (CPU x16 vs Chipset x4)."*

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

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
  Name:                    AMD Ryzen 7 9850X3D 8-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 7 9850X3D 8-Core Processor
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
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   5653
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            16
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    31696240(0x1e3a570) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    31696240(0x1e3a570) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    31696240(0x1e3a570) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    31696240(0x1e3a570) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1201
  Uuid:                    GPU-81ba7e079f6f7889
  Marketing Name:          AMD Radeon RX 9070 XT
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
    L2:                      8192(0x2000) KB
    L3:                      65536(0x10000) KB
  Chip ID:                 30032(0x7550)
  ASIC Revision:           1(0x1)
  Cacheline Size:          256(0x100)
  Max Clock Freq. (MHz):   2400
  BDFID:                   768
  Internal Node ID:        1
  Compute Unit:            64
  SIMDs per CU:            2
  Shader Engines:          4
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
  Packet Processor uCode:: 218
  SDMA engine uCode::      662
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16695296(0xfec000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1201
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
      Name:                    amdgcn-amd-amdhsa--gfx12-generic
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
*******
Agent 3
*******
  Name:                    gfx1201
  Uuid:                    GPU-5c9359c20ef65d63
  Marketing Name:          AMD Radeon RX 9070 XT
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
    L1:                      32(0x20) KB
    L2:                      8192(0x2000) KB
    L3:                      65536(0x10000) KB
  Chip ID:                 30032(0x7550)
  ASIC Revision:           1(0x1)
  Cacheline Size:          256(0x100)
  Max Clock Freq. (MHz):   2400
  BDFID:                   5120
  Internal Node ID:        2
  Compute Unit:            64
  SIMDs per CU:            2
  Shader Engines:          4
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
  Packet Processor uCode:: 218
  SDMA engine uCode::      662
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16695296(0xfec000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1201
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
      Name:                    amdgcn-amd-amdhsa--gfx12-generic
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
*******
Agent 4
*******
  Name:                    gfx1036
  Uuid:                    GPU-XX
  Marketing Name:          AMD Ryzen 7 9850X3D 8-Core Processor
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
    L2:                      256(0x100) KB
  Chip ID:                 5056(0x13c0)
  ASIC Revision:           1(0x1)
  Cacheline Size:          128(0x80)
  Max Clock Freq. (MHz):   2200
  BDFID:                   32000
  Internal Node ID:        3
  Compute Unit:            2
  SIMDs per CU:            2
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
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
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)
    y                        65535(0xffff)
    z                        65535(0xffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 26
  SDMA engine uCode::      9
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    15848120(0xf1d2b8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    15848120(0xf1d2b8) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx1036
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
      Name:                    amdgcn-amd-amdhsa--gfx10-3-generic
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

Crucial Environment Update

* **Local Build Testing:** The issue persists when compiling llama.cpp directly from the master branch using the stable system-level **ROCm 7.2.3** runtime stack.
* **Isolation Confirmation:** The crash is reproducible across both the bleeding-edge runtime alpha bundle and native stable system libraries. This isolates the fault away from application packaging and firmly points to a structural memory mapping regression inside the **ROCm HSA/KFD runtime** when managing tensor-split data allocations across mismatched PCIe architectures (CPU Native x16 $\leftrightarrow$ Chipset Multiplexed x4).