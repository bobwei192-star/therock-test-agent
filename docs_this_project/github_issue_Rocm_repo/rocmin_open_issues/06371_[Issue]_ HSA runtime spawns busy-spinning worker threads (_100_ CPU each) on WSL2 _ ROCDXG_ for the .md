# [Issue]: HSA runtime spawns busy-spinning worker threads (~100% CPU each) on WSL2 + ROCDXG, for the life of the process

- **Issue #:** 6371
- **State:** open
- **Created:** 2026-06-20T02:53:44Z
- **Updated:** 2026-06-22T16:57:12Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6371

### Problem Description

> Note: I used AI assistance for parts of this investigation, particularly the binary-level digging behind the hypothesis below.

I noticed this while running ComfyUI on WSL2: two CPU threads stay pinned at ~99–100% for as long as a workflow with a GPU node is loaded, including while ComfyUI is sitting idle waiting for a prompt. To check whether this was specific to ComfyUI, I reproduced the same behavior with a minimal PyTorch script and a minimal HIP C++ program that each just touch the GPU once and then sit idle. Both show the same two threads spinning, which points to this being an HSA runtime / ROCm issue rather than something in ComfyUI itself.

What I've confirmed directly:

- The same behavior reproduces with a minimal PyTorch script (`torch.zeros(1, device='cuda')`) and a minimal HIP C++ program that only calls `hipGetDeviceCount`/`hipMalloc`. Since neither does any ongoing GPU work, this happens as soon as the HSA runtime initializes, not because of anything ComfyUI does.
- `top -H` / `ps -To pid,tid,pcpu,state` show two threads pinned at ~99–100% CPU in state `R` for as long as the process lives.
- `strace -p <TID> -c -e trace=all` attached to either thread for several seconds produces **zero syscalls**. They're not blocked in the kernel; they're spinning entirely in user space.
- `/proc/<TID>/wchan` reads `0` and `/proc/<TID>/stack` is empty for these threads, consistent with a pure user-space busy loop.
- `/proc/<TID>/status` shows nonvoluntary context switches far outweighing voluntary ones (e.g. 158 nonvoluntary vs. 4 voluntary over the same window). They're only taken off-CPU by time-slice expiry, not because they're waiting on anything.
- For comparison, the ROCDXG queue-processing threads in the same process show close to zero involuntary context switches, i.e. they block/sleep properly. Whatever is spinning looks specific to a different part of the runtime.

**My working hypothesis** (not a confirmed finding): since WSL2 has no `/dev/kfd`, `/dev/dri`, or amdgpu kernel module, the HSA runtime falls back to the ROCDXG/DirectX12-interop signal path, which has no hardware interrupt for signal completion, and ends up polling in user space without any backoff (no `pause`, sleep, `sched_yield`, or futex-based wait). I used AI-assisted disassembly of the stripped `libhsa-runtime64.so` to try to locate this loop, but I can't verify those low-level details myself, so I'm leaving the raw offsets out of this report. Happy to share what I have if it's useful for triage.

I'm also not sure whether this is a regression or has always been true of the WSL2/ROCDXG path. Mentioning it in case it's useful context.

**Possibly related:** #4797 (WSL2, one core stuck at 100% with Whisper/PyTorch, reported May 2025). Similar symptoms; may or may not share the same cause.


### Operating System

Ubuntu 24.04.4 LTS, WSL2 (kernel: 6.18.33.1-microsoft-standard-WSL2), under Windows 11

### CPU

AMD Ryzen 7 3700X 8-Core Processor (16 threads)

### GPU

1 x AMD Radeon RX 7900 XTX (gfx1100, Chip ID 0x744c)

### ROCm Version

ROCm 7.2.1

### ROCm Component

HIP

### Steps to Reproduce

### Minimal PyTorch reproduction

- PyTorch: 2.9.1+rocm7.2.1.gitff65f5bc (HIP 7.2.53211)

```bash
python3 -c "import torch; x=torch.zeros(1,device='cuda'); import time; time.sleep(600)" &
# In another terminal:
top -H -p $(pgrep -f "torch.zeros")   # two threads pinned near 100% CPU
```

### Minimal HIP C++ reproduction

```cpp
#include <hip/hip_runtime.h>
#include <unistd.h>
int main() {
    int count; hipGetDeviceCount(&count);
    void* ptr; hipMalloc(&ptr, 256);
    pause();  // two threads pinned near 100% in `top -H` while we sit here
    hipFree(ptr);
}
```

### Confirmation commands

```bash
# Find the spinning threads
PID=$(pgrep -f "python.*torch")
ps -To pid,tid,pcpu,state -p $PID | awk '$4=="R" && $3>90'

# Confirm busy-wait (no syscalls)
sudo strace -p <TID> -c -e trace=all   # produces empty output over several seconds

# Confirm pure user-space spin (no kernel stack)
cat /proc/<TID>/stack   # empty
cat /proc/<TID>/wchan   # "0"

# Context-switch ratio (nonvoluntary >> voluntary == CPU-bound spinning, not blocking)
grep -E "voluntary|nonvoluntary" /proc/<TID>/status
```

### What I tested

| Configuration | Spinning observed? | Notes |
|---|---|---|
| PyTorch import + GPU tensor | Yes | 2 threads near 100% |
| PyTorch import only (no tensor op) | No | HSA initializes lazily on first GPU op, not on import |
| PyTorch `--cpu` flag | No | No GPU context created, so no HSA threads start |
| `HSA_ENABLE_DXG_DETECTION=0` | N/A | GPU stops working entirely (`RuntimeError: No HIP GPUs are available`) |

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
WSL environment detected.
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
  Name:                    AMD Ryzen 7 3700X 8-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 7 3700X 8-Core Processor
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
  Cacheline Size:          64(0x40)
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            16
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    28698256(0x1b5e690) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    28698256(0x1b5e690) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    28698256(0x1b5e690) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    28698256(0x1b5e690) KB
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
  Uuid:                    GPU-a06023418c081c00
  Marketing Name:          AMD Radeon RX 7900 XTX
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
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2482
  BDFID:                   1792
  Internal Node ID:        1
  Compute Unit:            96
  SIMDs per CU:            2
  Shader Engines:          6
  Shader Arrs. per Eng.:   2
  Coherent Host Access:    FALSE
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
  Packet Processor uCode:: 632
  SDMA engine uCode::      27
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    25105384(0x17f13e8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25105384(0x17f13e8) KB
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
```

</details>


### Additional Information

### Context switch profile

| TID | Role | voluntary CS | nonvoluntary CS | Pattern |
|-----|------|-------------|-----------------|---------|
| 13802 | spinning HSA thread | 4 | 158 | ~97% involuntary (CPU-bound) |
| 13803 | spinning HSA thread | 4 | 184 | ~98% involuntary (CPU-bound) |
| 13805 | ROCDXG queue thread | 7 | 0 | blocks properly |
| 13806 | ROCDXG queue thread | 6 | 0 | blocks properly |

### WSL2 environment

```bash
$ ls /dev/dri/ /dev/kfd
ls: cannot access '/dev/dri/': No such file or directory
ls: cannot access '/dev/kfd': No such file or directory

$ lsmod | grep -iE "amdgpu|drm|kfd"
(no output)

$ env | grep HSA
HSA_ENABLE_DXG_DETECTION=1
```

### Environment variables tried (none resolved the issue)

| Variable | Value tried | Effect |
|---|---|---|
| `HSA_ENABLE_DXG_DETECTION` | `0` | Breaks GPU access entirely |
| `HSA_ENABLE_INTERRUPT` | `1` | No observed effect |
| `HSA_SIGNAL_WAIT_ABORT_TIMEOUT` | various | No observed effect |
| `OMP_NUM_THREADS` | `1` | No observed effect |
| `CUDA_VISIBLE_DEVICES` | various | No observed effect |
