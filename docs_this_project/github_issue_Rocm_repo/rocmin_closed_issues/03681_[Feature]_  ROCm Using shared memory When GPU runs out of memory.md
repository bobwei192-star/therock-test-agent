# [Feature]:  ROCm Using shared memory When GPU runs out of memory

- **Issue #:** 3681
- **State:** closed
- **Created:** 2024-09-05T03:30:38Z
- **Updated:** 2025-07-28T15:49:06Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3681

### Suggestion Description

When I paint with ComfyUI, if the workflow is more complex, more models need to be loaded, or larger images are generated, there is a **HIP out of memory**, even if there is still enough space in shared memory at that point.
But when I switch to windows and run ComfyUI with zluda, I find that when the GPU runs out of memory, it will use shared memory to continue running instead of throwing a **HIP out of memory**, I would like to know if there is a plan to support the use of shared memory in subsequent releases.

### Operating System

Ubuntu

### GPU

RX 7900xtx

### ROCm Component

ROCm 6.2.0