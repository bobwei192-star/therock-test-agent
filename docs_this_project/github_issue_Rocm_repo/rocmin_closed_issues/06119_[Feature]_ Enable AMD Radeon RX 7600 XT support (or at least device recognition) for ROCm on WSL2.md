# [Feature]: Enable AMD Radeon RX 7600 XT support (or at least device recognition) for ROCm on WSL2

- **Issue #:** 6119
- **State:** closed
- **Created:** 2026-04-04T11:48:18Z
- **Updated:** 2026-05-21T04:42:39Z
- **Labels:** Feature Request, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6119

### Suggestion Description

I would like to formally suggest official support, or at least basic device recognition, for the AMD Radeon RX 7600 XT on WSL2.

Currently, many users (including myself) are successfully using the RX 7600 XT on native Ubuntu environments by utilizing the HSA_OVERRIDE_GFX_VERSION=11.0.0 environment variable. While I understand this specific SKU is not on the official support list, it is proven to be functionally capable of running ROCm workloads with the override.

The primary issue is that on WSL2, the device is not recognized or passed through correctly to the ROCm stack, making it impossible to even attempt the override.

### Operating System

Windows

### GPU

7600XT

### ROCm Component

_No response_