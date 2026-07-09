# [Feature]: torch.distributed support on Windows (workaround available for ComfyUI)

- **Issue #:** 5689
- **State:** closed
- **Created:** 2025-11-24T03:01:13Z
- **Updated:** 2025-12-16T16:04:02Z
- **Labels:** Feature Request, application:pytorch, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5689

### Suggestion Description

## Description
After years of waiting for ROCm to arrive on Windows, the preview release does not include `torch.distributed` or RCCL/Gloo backends for multi‑GPU training. This is a critical gap: developers and researchers expect multi‑GPU support as a baseline, not an optional feature.

Without it, ROCm on Windows is limited to single‑GPU experiments. Anyone with real workloads is forced back to Linux or to NVIDIA hardware. This undermines the potential of ROCm on Windows and makes it difficult to recommend for serious use.

## Expected Behavior
- `torch.distributed` should be available in ROCm Windows builds.
- RCCL or Gloo backends should be enabled so dual‑GPU and cluster systems can be used for training.

## Actual Behavior
- On Windows ROCm preview (Pro Edition HIP driver), multiple GPUs are enumerated (`torch.cuda.device_count()` shows both), but `torch.distributed` is missing.
- DistributedDataParallel cannot be used.

## Environment
- Windows 11
- Dual Radeon RX 7900 XTX
- AMD Software: Pro Edition for HIP (25.Q3)

## Request
Please prioritize enabling `torch.distributed` with RCCL/Gloo backends in ROCm for Windows. Multi‑GPU support is essential for serious AI workloads and should be part of the baseline feature set.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_