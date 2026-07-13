# [Issue]: hsa_queue_create causes GPU page fault on gfx1151 APU (Ryzen AI Max+ 395, Radeon 8060S)

- **Issue #:** 6118
- **State:** closed
- **Created:** 2026-04-04T11:26:17Z
- **Updated:** 2026-04-08T06:41:46Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6118

### Problem Description

## Environment
- APU: AMD Ryzen AI Max+ 395 (Strix Halo)
- GPU: Radeon 8060S (gfx1151, RDNA 3.5, Chip ID 0x1586)
- ROCm: 7.2.1 (hsa-rocr 1.18.0.70201-81)
- Driver: amdgpu-dkms 6.19.0 (31.20 series)
- Kernel: 6.17.0-20-generic (Ubuntu 24.04)
- Also tested: amdgpu-dkms 6.16.13 (30.30), kernel 6.17.0-19

## Problem
hsa_queue_create() on the gfx1151 GPU agent causes an immediate
GPU memory access fault and crashes:

  Memory access fault by GPU node-1 (Agent handle: 0x5b19b86e7090) 
  on address 0x767500478000. 
  Reason: Page not present or supervisor privilege.

dmesg shows:
  amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8)
  GCVM_L2_PROTECTION_FAULT_STATUS: 0x00800932
  Faulty UTCL2 client ID: CPF (0x4)
  WALKER_ERROR: 0x1, PERMISSION_FAULTS: 0x3, MAPPING_ERROR: 0x1

This blocks ALL GPU compute: hipStreamCreate, hipMalloc, 
hipModuleLoadData all hang because they go through hsa_queue_create.

## What works
- rocminfo detects the GPU correctly (gfx1151, 40 CUs, KERNEL_DISPATCH)
- rocm-smi shows healthy GPU (32°C, 23W)
- hipInit, hipHostMalloc, hipDeviceSynchronize all work
- hiprtcCompileProgram produces valid code objects
- Display output works fine

## Minimal reproducer (Python)
```python
import ctypes

hsa = ctypes.CDLL('/opt/rocm/lib/libhsa-runtime64.so')

class hsa_agent_t(ctypes.Structure):
    _fields_ = [('handle', ctypes.c_uint64)]

hsa.hsa_init()

AGENT_CB = ctypes.CFUNCTYPE(ctypes.c_int, hsa_agent_t, ctypes.c_void_p)
gpu = hsa_agent_t()

def find_gpu(agent, data):
    dev = ctypes.c_uint32()
    hsa.hsa_agent_get_info(agent, 17, ctypes.byref(dev))
    if dev.value == 1:
        gpu.handle = agent.handle
    return 0

hsa.hsa_iterate_agents(AGENT_CB(find_gpu), None)
queue = ctypes.c_void_p()
# This line crashes with page fault:
hsa.hsa_queue_create(gpu, 1024, 0, None, None, 
    ctypes.c_uint32(0xFFFFFFFF), ctypes.c_uint32(0xFFFFFFFF),
    ctypes.byref(queue))
```

## Impact
Completely blocks GPU compute on Ryzen AI Max+ 395.

## rocminfo GPU output
  Name: gfx1151
  Marketing Name: Radeon 8060S Graphics
  Feature: KERNEL_DISPATCH
  Max Queue Number: 128
  Chip ID: 5510 (0x1586)
  Compute Unit: 40
  Wavefront Size: 32

### Operating System

24.04.4 LTS (Noble Numbat)

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon™ 8060S × 32

### GPU

Radeon™ 8060S Graphics

### ROCm Version

7.2.1 (hsa-rocr 1.18.0.70201-81)

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_