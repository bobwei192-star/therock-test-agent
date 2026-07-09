# [Issue]: Strix Halo (gfx1151) gives segfault on any VRAM access with torch nightly package

- **Issue #:** 5853
- **State:** closed
- **Created:** 2026-01-15T03:34:20Z
- **Updated:** 2026-03-17T15:38:29Z
- **Labels:** status: triage
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5853

### Problem Description

I don't know if there is anything wrong with my setup, but on my Strix Halo platform any ROCm VRAM access seems to consistently give me segfault with the torch nightly package. Nightly package from [TheRock](https://github.com/ROCm/TheRock/blob/main/RELEASES.md) seems to work fine though. My problem is that I hope to use pre-built binary version of llama.cpp container images to host LLMs, and they just fail the similar way - upon VRAM allocation throwing out a segfault. While I could build llama.cpp myself with the rock package I would say ideally I just want the prebuilt binary to work.

See below for more details

### Operating System

Arch Linux (rolling)

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

Radeon 8060S

### ROCm Version

ROCm 7.1.0

### ROCm Component

_No response_

### Steps to Reproduce

test.py:
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"Device: {torch.cuda.get_device_name(0)}")
x = torch.tensor([1.0, 2.0, 3.0]).cuda()
y = torch.tensor([1.0, 2.0, 3.0]).cuda()
print(x + y)
```

With torch nightly version:
```
$ uv venv --python 3.12 venv-multi-bin
$ source venv-multi-bin/bin/activate
$ uv pip install --index-url https://download.pytorch.org/whl/nightly/rocm7.1 torch
$ uv run python test.py
/var/home/hkj/venv-multi-bin/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:307: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  cpu = _conversion_method_template(device=torch.device("cpu"))
/opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory
CUDA available: True
Device: AMD Radeon 8060S
Segmentation fault
```
Similar faults happen when I attempt to run any other workloads with other frameworks like llama.cpp, etc. I inspected the dumped cores they seemed to fault at the same point.

With the rock package:
```
$ uv venv --python 3.12 venv-gfx1151-only
$ source venv-gfx1151-only/bin/activate
$ uv pip install --index-url https://rocm.nightlies.amd.com/v2/gfx1151/ torch
$ uv run python test.py
/var/home/hkj/venv-gfx1151-only/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:279: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /__w/TheRock/TheRock/external-builds/pytorch/pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  cpu = _conversion_method_template(device=torch.device("cpu"))
CUDA available: True
Device: Radeon 8060S Graphics
tensor([2., 4., 6.], device='cuda:0')
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

The above test is done bare metal. I can only run "rocminfo" from a container, but the container is the base for the prebuilt llama.cpp binaries I tested that exhibited similar faults so I guess it is still applicable:
```
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
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Uuid:                    CPU-XX
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
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
  Max Clock Freq. (MHz):   5187
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
      Size:                    130488832(0x7c71a00) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    130488832(0x7c71a00) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    130488832(0x7c71a00) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    130488832(0x7c71a00) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1151
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon Graphics
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
    L2:                      2048(0x800) KB
    L3:                      32768(0x8000) KB
  Chip ID:                 5510(0x1586)
  ASIC Revision:           0(0x0)
  Cacheline Size:          128(0x80)
  Max Clock Freq. (MHz):   2900
  BDFID:                   50432
  Internal Node ID:        1
  Compute Unit:            40
  SIMDs per CU:            2
  Shader Engines:          2
  Shader Arrs. per Eng.:   2
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
  Packet Processor uCode:: 32
  SDMA engine uCode::      17
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    125829120(0x7800000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    125829120(0x7800000) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx1151
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

### Additional Information

I have:

```
$ cat /etc/modprobe.d/uma-allocation.conf
# Maximize GTT for LLM usage on 128GB UMA system
options ttm pages_limit=31457280
options ttm page_pool_size=15728640
$ sudo dmesg | grep GTT
[    5.721182] amdgpu 0000:c5:00.0: amdgpu: amdgpu: 122880M of GTT memory ready.
```

I tried setting 
```
HSA_OVERRIDE_GFX_VERSION=11.0.0
HSA_OVERRIDE_GFX_VERSION=11.5.0
HSA_OVERRIDE_GFX_VERSION=11.5.1
```
None worked.

I tried running with `AMD_LOG_LEVEL=5 HSA_ENABLE_DEBUG=1 HSAKMT_DEBUG_LEVEL=7` and got these outputs before segfault:
```
/var/home/hkj/venv/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:307: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  cpu = _conversion_method_template(device=torch.device("cpu"))
udmabuf is not enabled
/opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory
SVM alignment default order is 9.acquiring VM for 11ba using 8
Initialized unreserved SVM apertures: 0x200000 - 0x7fffffffffff
mem_handle_aperture start 0x2800000000000, mem_handle_aperture limit 0x3000000000000
SVM alignment default order is 9.acquiring VM for 11ba using 8
Initialized unreserved SVM apertures: 0x200000 - 0x7fffffffffff
mem_handle_aperture start 0x2800000000000, mem_handle_aperture limit 0x3000000000000
[hsaKmtMapMemoryToGPU] address 0x7ff827f00000
[hsaKmtAllocMemoryAlign] node 0
bind_mem_to_numa mem 0x7ff6bc600000 flags 0x20040 size 0x200000 node_id 0
numa_node_id is out range: numa_node_id 0, num_node 1
[hsaKmtAllocMemoryAlign] node 0 address 0x7ff6bc600000 size 2097152 from host
[hsaKmtMapMemoryToGPUNodes] address 0x7ff6bc600000 number of nodes 1
[hsaKmtAllocMemoryAlign] node 1
[hsaKmtAllocMemoryAlign] node 1 address 0x7ff5bbc00000 size 4294967296 from scratch
[hsaKmtAllocMemoryAlign] node 0
bind_mem_to_numa mem 0x7ff827f0c000 flags 0x821040 size 0x1000 node_id 0
numa_node_id is out range: numa_node_id 0, num_node 1
[hsaKmtAllocMemoryAlign] node 0 address 0x7ff827f0c000 size 4096 from host
[hsaKmtMapMemoryToGPUNodes] address 0x7ff827f0c000 number of nodes 1
:3:rocdevice.cpp            :420 : 6744385914 us: [pid:25927 tid: 0x7ff8286d8740] Initalizing runtime stack, Enumerated GPU agents = 1
:3:rocdevice.cpp            :187 : 6744385940 us: [pid:25927 tid: 0x7ff8286d8740] Numa selects cpu agent[0]=0x29d97290(fine=0x29dacc00,coarse=0x297b2ba0) for gpu agent=0x297b3980 CPU<->GPU XGMI=0
:3:rocsettings.cpp          :277 : 6744385948 us: [pid:25927 tid: 0x7ff8286d8740] Using dev kernel arg wa = 0
:3:comgrctx.cpp             :127 : 6744385981 us: [pid:25927 tid: 0x7ff8286d8740] Loaded COMGR library version 3.0.
[hsaKmtGetTileConfig] node 1
:3:rocdevice.cpp            :1590: 6744386159 us: [pid:25927 tid: 0x7ff8286d8740] addressableNumVGPRs=256, totalNumVGPRs=1536, vGPRAllocGranule=24, availableRegistersPerCU_=196608
:3:rocdevice.cpp            :1604: 6744386168 us: [pid:25927 tid: 0x7ff8286d8740] imageSupport=1
:3:rocdevice.cpp            :1635: 6744386171 us: [pid:25927 tid: 0x7ff8286d8740] Gfx Major/Minor/Stepping: 11/5/1
:3:rocdevice.cpp            :1637: 6744386173 us: [pid:25927 tid: 0x7ff8286d8740] HMM support: 1, XNACK: 0, Direct host access: 0
:3:rocdevice.cpp            :1639: 6744386175 us: [pid:25927 tid: 0x7ff8286d8740] Max SDMA Read Mask: 0x1, Max SDMA Write Mask: 0x1
[hsaKmtAllocMemoryAlign] node 0
bind_mem_to_numa mem 0x7ff5bae00000 flags 0x2040 size 0x400000 node_id 0
numa_node_id is out range: numa_node_id 0, num_node 1
[hsaKmtAllocMemoryAlign] node 0 address 0x7ff5bae00000 size 4194304 from host
:4:rocdevice.cpp            :2007: 6744386887 us: [pid:25927 tid: 0x7ff8286d8740] Allocate hsa host memory 0x7ff5bae00000, size 0x400000, numa_node = 0, mem_seg = 0
[hsaKmtQueryPointerInfo] pointer 0x7ff5bae00000
[hsaKmtMapMemoryToGPUNodes] address 0x7ff5bae00000 number of nodes 1
[hsaKmtAllocMemoryAlign] node 0
bind_mem_to_numa mem 0x7ff827f0a000 flags 0x40 size 0x1000 node_id 0
numa_node_id is out range: numa_node_id 0, num_node 1
[hsaKmtAllocMemoryAlign] node 0 address 0x7ff827f0a000 size 4096 from host
:4:rocdevice.cpp            :2007: 6744386967 us: [pid:25927 tid: 0x7ff8286d8740] Allocate hsa host memory 0x7ff827f0a000, size 0x38, numa_node = 0, mem_seg = 1
[hsaKmtQueryPointerInfo] pointer 0x7ff827f0a000
[hsaKmtMapMemoryToGPUNodes] address 0x7ff827f0a000 number of nodes 1
:3:hip_context.cpp          :60  : 6744386983 us: [pid:25927 tid: 0x7ff8286d8740] HIP Version: 7.1.52802.26aae437f6, Direct Dispatch: 1
:3:os_posix.cpp             :961 : 6744386994 us: [pid:25927 tid: 0x7ff8286d8740] HIP Library Path: /var/home/hkj/venv/lib/python3.12/site-packages/torch/lib/libamdhip64.so
:3:hip_device_runtime.cpp   :703 : 6744399665 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDeviceCount ( 0x7ffeb78ca13c )
:3:hip_device_runtime.cpp   :705 : 6744399672 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDeviceCount: Returned hipSuccess :
CUDA available: True
:3:hip_device_runtime.cpp   :703 : 6744399774 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDeviceCount ( 0x7ffeb78ca0f0 )
:3:hip_device_runtime.cpp   :705 : 6744399777 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDeviceCount: Returned hipSuccess :
:3:hip_device.cpp           :659 : 6744399790 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevicePropertiesR0600 ( 0x2a38a160, 0 )
:3:hip_device.cpp           :661 : 6744399796 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevicePropertiesR0600: Returned hipSuccess :
:3:hip_device_runtime.cpp   :703 : 6744399806 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDeviceCount ( 0x7ffeb78c9f9c )
:3:hip_device_runtime.cpp   :705 : 6744399809 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDeviceCount: Returned hipSuccess :
:3:hip_device_runtime.cpp   :703 : 6744399840 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDeviceCount ( 0x7ff74c46afa4 )
:3:hip_device_runtime.cpp   :705 : 6744399843 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDeviceCount: Returned hipSuccess :
:3:hip_device.cpp           :659 : 6744399847 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevicePropertiesR0600 ( 0x7ffeb78c9bd8, 0 )
:3:hip_device.cpp           :661 : 6744399849 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevicePropertiesR0600: Returned hipSuccess :
:3:hip_device_runtime.cpp   :687 : 6744399871 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c9d0c )
:3:hip_device_runtime.cpp   :699 : 6744399875 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :365 : 6744400132 us: [pid:25927 tid: 0x7ff8286d8740]  hipDevicePrimaryCtxGetState ( 0, 0x7ffeb78c9d24, 0x7ffeb78c9d28 )
:3:hip_context.cpp          :379 : 6744400137 us: [pid:25927 tid: 0x7ff8286d8740] hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :687 : 6744400140 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c9d0c )
:3:hip_device_runtime.cpp   :699 : 6744400142 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :365 : 6744400145 us: [pid:25927 tid: 0x7ff8286d8740]  hipDevicePrimaryCtxGetState ( 0, 0x7ffeb78c9d24, 0x7ffeb78c9d28 )
:3:hip_context.cpp          :379 : 6744400146 us: [pid:25927 tid: 0x7ff8286d8740] hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :687 : 6744400154 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c9efc )
:3:hip_device_runtime.cpp   :699 : 6744400158 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :365 : 6744400162 us: [pid:25927 tid: 0x7ff8286d8740]  hipDevicePrimaryCtxGetState ( 0, 0x7ffeb78c9f14, 0x7ffeb78c9f18 )
:3:hip_context.cpp          :379 : 6744400168 us: [pid:25927 tid: 0x7ff8286d8740] hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device.cpp           :659 : 6744400644 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevicePropertiesR0600 ( 0x7ffeb78c9830, 0 )
:3:hip_device.cpp           :661 : 6744400650 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevicePropertiesR0600: Returned hipSuccess :
Device: AMD Radeon 8060S
:3:hip_device_runtime.cpp   :687 : 6744400848 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c9e74 )
:3:hip_device_runtime.cpp   :699 : 6744400852 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :687 : 6744400890 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c9094 )
:3:hip_device_runtime.cpp   :699 : 6744400894 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :687 : 6744400898 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c8f54 )
:3:hip_device_runtime.cpp   :699 : 6744400902 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :687 : 6744400909 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c8ddc )
:3:hip_device_runtime.cpp   :699 : 6744400912 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_stream.cpp           :316 : 6744400919 us: [pid:25927 tid: 0x7ff8286d8740]  hipDeviceGetStreamPriorityRange ( 0x7ffeb78c8d90, 0x7ffeb78c8db0 )
:3:hip_stream.cpp           :324 : 6744400924 us: [pid:25927 tid: 0x7ff8286d8740] hipDeviceGetStreamPriorityRange: Returned hipSuccess :
:3:hip_error.cpp            :34  : 6744400939 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetLastError (  )
:3:hip_device_runtime.cpp   :687 : 6744400943 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c85bc )
:3:hip_device_runtime.cpp   :699 : 6744400945 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :1075: 6744400954 us: [pid:25927 tid: 0x7ff8286d8740]  hipStreamIsCapturing ( char array:<null>, 0x7ffeb78c8820 )
:3:hip_graph.cpp            :1076: 6744400958 us: [pid:25927 tid: 0x7ff8286d8740] hipStreamIsCapturing: Returned hipSuccess :
:3:hip_memory.cpp           :759 : 6744400968 us: [pid:25927 tid: 0x7ff8286d8740]  hipMalloc ( 0x7ffeb78c8900, 2097152 )
[hsaKmtAllocMemoryAlign] node 1
[hsaKmtAllocMemoryAlign] node 1 address 0x7ff5baa00000 size 2097152 from device
[hsaKmtMapMemoryToGPUNodes] address 0x7ff5baa00000 number of nodes 1
:4:rocdevice.cpp            :2186: 6744401102 us: [pid:25927 tid: 0x7ff8286d8740] Allocate hsa device memory 0x7ff5baa00000, size 0x200000, hsa_mem_flags 0x0h
:3:rocdevice.cpp            :2226: 6744401106 us: [pid:25927 tid: 0x7ff8286d8740] Device=0x29fe6170, freeMem_ = 0x1dffe00000
:3:hip_memory.cpp           :761 : 6744401112 us: [pid:25927 tid: 0x7ff8286d8740] hipMalloc: Returned hipSuccess : 0x7ff5baa00000: duration: 144 us
:3:hip_device_runtime.cpp   :773 : 6744401131 us: [pid:25927 tid: 0x7ff8286d8740]  hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :778 : 6744401134 us: [pid:25927 tid: 0x7ff8286d8740] hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :773 : 6744401137 us: [pid:25927 tid: 0x7ff8286d8740]  hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :778 : 6744401139 us: [pid:25927 tid: 0x7ff8286d8740] hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :687 : 6744401180 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c8d34 )
:3:hip_device_runtime.cpp   :699 : 6744401183 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :687 : 6744401185 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c8b6c )
:3:hip_device_runtime.cpp   :699 : 6744401187 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :365 : 6744401191 us: [pid:25927 tid: 0x7ff8286d8740]  hipDevicePrimaryCtxGetState ( 0, 0x7ffeb78c8b84, 0x7ffeb78c8b88 )
:3:hip_context.cpp          :379 : 6744401195 us: [pid:25927 tid: 0x7ff8286d8740] hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :687 : 6744401199 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c8b4c )
:3:hip_device_runtime.cpp   :699 : 6744401202 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :1075: 6744401207 us: [pid:25927 tid: 0x7ff8286d8740]  hipStreamIsCapturing ( char array:<null>, 0x7ffeb78c8d70 )
:3:hip_graph.cpp            :1076: 6744401212 us: [pid:25927 tid: 0x7ff8286d8740] hipStreamIsCapturing: Returned hipSuccess :
:3:hip_device_runtime.cpp   :687 : 6744401216 us: [pid:25927 tid: 0x7ff8286d8740]  hipGetDevice ( 0x7ffeb78c8b4c )
:3:hip_device_runtime.cpp   :699 : 6744401218 us: [pid:25927 tid: 0x7ff8286d8740] hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :2045: 6744401228 us: [pid:25927 tid: 0x7ff8286d8740]  hipStreamGetCaptureInfo ( char array:<null>, 0x7ffeb78c8d3c, char array:<null> )
:3:hip_graph.cpp            :2046: 6744401231 us: [pid:25927 tid: 0x7ff8286d8740] hipStreamGetCaptureInfo: Returned hipSuccess :
:3:hip_memory.cpp           :809 : 6744401245 us: [pid:25927 tid: 0x7ff8286d8740]  hipMemcpyWithStream ( 0x7ff5baa00000, 0x2a3a4c40, 12, hipMemcpyHostToDevice, char array:<null> )
:5:hip_device.cpp           :35  : 6744401248 us: [pid:25927 tid: 0x7ff8286d8740] NullStream (nil), wait 1
:3:rocdevice.cpp            :2871: 6744401254 us: [pid:25927 tid: 0x7ff8286d8740] Number of allocated hardware queues with low priority: 0, with normal priority: 0, with high priority: 0, maximum per priority is: 4
[hsaKmtAllocMemoryAlign] node 1
[hsaKmtAllocMemoryAlign] node 1 address 0x7ff827efe000 size 4096 from host
[hsaKmtMapMemoryToGPUNodes] address 0x7ff827efe000 number of nodes 1
[hsaKmtAllocMemoryAlign] node 0
bind_mem_to_numa mem 0x7ff827efc000 flags 0x21040 size 0x1000 node_id 0
numa_node_id is out range: numa_node_id 0, num_node 1
[hsaKmtAllocMemoryAlign] node 0 address 0x7ff827efc000 size 4096 from host
[hsaKmtMapMemoryToGPUNodes] address 0x7ff827efc000 number of nodes 1
[hsaKmtMapMemoryToGPUNodes] address 0x7ff827efa000 number of nodes 1
Allocating VRAM for EOP
[hsaKmtMapMemoryToGPUNodes] address 0x7ff827ef8000 number of nodes 1
Allocating GTT for CWSR
hsaKmtSVMSetAttr: address 0x0x7ff5b9c00000 size 0xd56000
[hsaKmtUnmapMemoryToGPU] address 0x7ff827ef8000
[hsaKmtFreeMemory] address 0x7ff827ef8000
[hsaKmtUnmapMemoryToGPU] address 0x7ff827efa000
[hsaKmtFreeMemory] address 0x7ff827efa000
[hsaKmtUnmapMemoryToGPU] address 0x7ff827efe000
[hsaKmtFreeMemory] address 0x7ff827efe000
[hsaKmtUnmapMemoryToGPU] address 0x7ff827efc000
[hsaKmtFreeMemory] address 0x7ff827efc000
```