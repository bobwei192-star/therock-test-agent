# [Issue]: Ollama compatibility issue with kernel/drivers causes ROCm container conflict

- **Issue #:** 5679
- **State:** closed
- **Created:** 2025-11-20T02:15:30Z
- **Updated:** 2025-12-09T19:02:17Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5679

### Problem Description

Description:
There is a compatibility issue when running Ollama with AMD GPU drivers on different Linux kernel versions, which conflicts with running ROCm-based containers like vLLM.

Environment:

Ollama version: [v0.12.11](https://github.com/ollama/ollama/releases/tag/v0.12.11)

Kernel versions tested:

6.8.x + AMD official driver → Ollama runs initially but triggers GPU driver crash under certain conditions

6.17.8 + open-source amdgpu driver → Ollama runs stably

Problem:

On 6.8 kernel + official AMD driver:

Ollama starts and can process initial prompts

When Ollama automatically unloads models after some time, subsequent prompts cause GPU driver crash

Likely cause: official driver has issues with VRAM handling or model unloading

On 6.17.8 kernel + open-source driver:

Ollama runs stably without driver crashes

However, ROCm containers (e.g., vLLM) cannot run because /dev/kfd does not exist in the open-source driver environment

Steps to Reproduce:

Install Ollama on 6.8 kernel with official AMD driver

Run Ollama and process several prompts

Wait for Ollama to automatically unload a model, then send additional prompts

Observe GPU driver crash

Upgrade to 6.17.8 kernel and switch to open-source amdgpu driver

Ollama runs stably

Attempt to run vLLM ROCm container

Container fails to start: OCI runtime create failed: failed to create shim task, because /dev/kfd is missing

Impact:

Cannot use Ollama and ROCm GPU containers on the same system

Official driver is unstable with Ollama

Open-source driver prevents running ROCm containers on GPU

Expected Behavior:

Ollama runs stably with open-source drivers

Or official driver does not crash when models are automatically unloaded

Ideally, allow running both Ollama and ROCm containers on the same system

Additional Information:

Attach dmesg or kernel logs showing GPU driver crash

Attach ROCm container error logs if available

### Operating System

ubuntu24.4.3

### CPU

AMD 3960X

### GPU

AI pro R9700

### ROCm Version

latest（2025/11/15）

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_