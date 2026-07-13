# [Issue]: [ollama/ollama] Qwen3.5:9b rocBLAS error from hip error code: 'hipErrorInvalidDeviceFunction':98 ggml_cuda_compute_forward: SOLVE_TRI failed ROCm error: invalid device function

- **Issue #:** 6120
- **State:** closed
- **Created:** 2026-04-06T02:04:24Z
- **Updated:** 2026-04-20T14:05:27Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6120

### Problem Description

PowerShell 7.6.0
PS C:\Users\DaveyBoneZ>   (Get-WmiObject Win32_OperatingSystem).Version
10.0.26200
PS C:\Users\DaveyBoneZ>   (Get-WmiObject win32_Processor).Name
AMD Ryzen 7 5800X3D 8-Core Processor
PS C:\Users\DaveyBoneZ>   (Get-WmiObject win32_VideoController).Name
AMD Radeon RX 9060 XT
PS C:\Users\DaveyBoneZ>

### Additional details & troubleshooting already performed (RX 9060 XT - RDNA 4)

**Hardware:**  
- GPU: AMD Radeon RX 9060 XT 16 GB (RDNA 4 / gfx12xx)  
- OS: Windows 11 Pro 24H2  
- Confirmed working: **LM Studio** runs Qwen3.5 models perfectly on the exact same hardware with zero errors (using its bundled ROCm stack).

**What I already tried:**
- Fresh Ollama install (latest version)
- Multiple ROCm versions (including 6.4 and 7.1)
- Hijacked LM Studio’s entire ROCm stack (copied DLLs + set `HIP_PATH`, `PATH`, `LD_LIBRARY_PATH`, etc.) → still got the exact same `hipErrorInvalidDeviceFunction (98)`
- Confirmed the error happens during model load / rocBLAS kernel launch (`SOLVE_TRI failed`)

**AMD Support Ticket:**  
I already provided full diagnostics to AMD Global Customer Care (Ticket #3520556):
- Complete MSInfo32 (.nfo)
- DxDiag report
- Full Ollama error logs showing the hipErrorInvalidDeviceFunction(98)
- Confirmed the issue has existed since the very first attempt (never worked)

AMD has now asked me to open this GitHub issue so the ROCm team can investigate.

**Related issue:**  
This appears to be the same problem as #14423 (Radeon AI Pro R9700 — also RDNA 4).

**Reproduction steps:**
1. Install latest Ollama
2. `ollama run qwen3.5` (or any Qwen3.5 variant)
3. Immediate 500 error with `hipErrorInvalidDeviceFunction (98)` + rocBLAS failure

Smaller Qwen3 models and other families may work, but all Qwen3.5 models fail.

Happy to provide any additional logs, run specific tests, or share the full AMD diagnostics files if needed.

Thanks for looking into this — really hoping we can get RDNA 4 consumer cards working properly with Ollama + ROCm.

### Additional Context & Deep Troubleshooting (RX 9060 XT - RDNA 4)

**Critical observation that may help narrow this down:**

- **LM Studio runs Qwen3.5 models perfectly** with zero errors on this exact same RX 9060 XT hardware.
- I went **much further** and **completely hijacked LM Studio’s entire working ROCm stack**:
  - Copied all DLLs, libraries, and binaries from LM Studio’s ROCm installation
  - Overrode `HIP_PATH`, `PATH`, `LD_LIBRARY_PATH`, and every relevant environment variable to force Ollama to use LM Studio’s exact ROCm environment
- Even with LM Studio’s proven-working ROCm stack fully in control, **Ollama still immediately fails** with the exact same `hipErrorInvalidDeviceFunction (98)` + `SOLVE_TRI failed`.

This strongly suggests the problem is **not** a missing or broken ROCm install, but something specific in how **Ollama itself** builds/calls the HIP/rocBLAS kernels on RDNA 4 (gfx12xx).

**Other details already provided:**
- Issue has existed since the very first attempt (never worked)
- AMD Support Ticket #3520556 with full MSInfo32 (.nfo), DxDiag, and raw Ollama error logs
- Related issue: #14423 (same error on Radeon AI Pro R9700 — also RDNA 4)

**Reproduction:**
1. Latest Ollama
2. `ollama run qwen3.5` (any size)
3. Immediate 500 error during model load

Happy to run any specific tests, share the full AMD diagnostics files, or provide whatever else is needed.

Thanks for looking into this.

### Operating System

Windows 11

### CPU

AMD Ryzen 7 5800X3D

### GPU

AMD Radeon RX 9060 XT

### ROCm Version

7.1.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_