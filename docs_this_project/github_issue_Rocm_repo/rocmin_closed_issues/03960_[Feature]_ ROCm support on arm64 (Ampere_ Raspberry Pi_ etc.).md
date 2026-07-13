# [Feature]: ROCm support on arm64 (Ampere, Raspberry Pi, etc.)

- **Issue #:** 3960
- **State:** closed
- **Created:** 2024-10-30T15:01:18Z
- **Updated:** 2025-03-05T06:43:24Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/3960

### Suggestion Description

I have gotten various generation AMD graphics cards working on the Raspberry Pi 5 (see https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/222), as well as on Ampere Altra and AmpereOne workstations and servers (see https://community.amperecomputing.com/t/amd-gpus-on-the-altra-devkit-and-other-altras-patches-available-now/336).

For many of these systems, running software like Ollama or other LLMs would be beneficial, and having an alternative to Nvidia graphics cards would provide more options for vendors (and more cash to AMD, since Pro/RX/Enterprise cards could be justified on these systems).

As of 2021, [ROCm was not supported on arm64](https://github.com/ROCm/ROCm/issues/1052), but a few years later, we have much better `amdgpu` driver support (though still requiring some fixes for Arm PCIe implementations where cache coherency is different than amd64).

Is it possible for arm64 support to be explored for AMD GPUs?

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_