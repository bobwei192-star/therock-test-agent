# [Issue]: gfx1151 Constant PERMISSION_FAULTS (0x3) on Strix Halo (Ryzen AI MAX 395) during ROCm workloads

- **Issue #:** 6186
- **State:** open
- **Created:** 2026-04-27T09:10:21Z
- **Updated:** 2026-06-01T18:37:01Z
- **Labels:** status: triage
- **Assignees:** Jonathan03ant
- **URL:** https://github.com/ROCm/ROCm/issues/6186

### Problem Description

### Summary
I am experiencing consistent memory permission faults on the new Strix Halo (gfx1151) platform when running ROCm-based workloads (specifically llama.cpp with the ROCm/HIP backend). The system triggers a page fault almost immediately during the model warmup/inference phase.

### System Information (Command Output)
- **OS:** Ubuntu 24.04.4 LTS (Noble Numbat)
- **CPU:** AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
- **Kernel version:** 6.19.14-061914-generic
- **GPU:** Radeon 8060S (integrated, gfx1151)
- **RAM:** 128GB Unified Memory
- **IOMMU Status:** `iommu=pt` enabled

### Hardware Details
- **Device:** Minisforum AI Server
- **APU:** Ryzen AI MAX+ 395 (Strix Halo)
- **VRAM Configuration:** GTT size set to 120GB via `amdgpu.gttsize=122880`

### Error Logs (dmesg)
The following error appears in the system logs at the moment of the crash:

amdgpu 0000:bd:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:2634)
PERMISSION_FAULTS: 0x3
Faulty UTCL2 client ID: CPF (0x4)

### Steps to Reproduce
1. Start `llama-server` using a ROCm-compiled binary (tested with build b1251).
2. Attempt to load a large GGUF model (e.g., Gemma-4-26B).
3. The system triggers the permission fault during the first compute kernels (warmup).

### Additional Observations
- **Vulkan Backend works perfectly:** On the same hardware and OS, the Vulkan build of llama.cpp works flawlessly, achieving 50-60 TPS on 26B models. This suggests the hardware and general memory allocation are fine, but the HIP/ROCm memory management layer has issues with mapping/permissions on this new UMA architecture.
- I've tried disabling XNACK and SDMA via environment variables (`HSA_ENABLE_SDMA=0`), but the permission faults persist.
- Using `-dio` and `--no-mmap` server flags also does not prevent the crash.

### Operating System

Ubuntu 24.04.4 LTS (Noble Numbat)

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

Radeon 8060S (integrated, gfx1151)

### ROCm Version

7.2.2

### ROCm Component

ROCR-Runtime

### Steps to Reproduce

1. Use a Strix Halo (gfx1151) based system with 128GB of RAM.
2. Configure kernel parameters: `amdgpu.gttsize=122880 iommu=pt`.
3. Run a ROCm-compiled version of llama-server (e.g., build b1251).
4. Attempt to load a large model (Gemma-4-26B Q8) using the following flags:
   `./llama-server -m models/gemma-4-26B-A4B-it-Q8_0.gguf -ngl 99 --no-mmap -dio`
5. Observe the system behavior during the model warmup phase.
6. Check `dmesg` for the GFXHUB page fault error.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_