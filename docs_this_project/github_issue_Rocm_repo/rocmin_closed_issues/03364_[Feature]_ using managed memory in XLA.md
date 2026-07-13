# [Feature]: using managed memory in XLA

- **Issue #:** 3364
- **State:** closed
- **Created:** 2024-06-27T01:34:21Z
- **Updated:** 2024-12-02T00:23:09Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3364

### Suggestion Description

Dear ROCm developers,

according to some tests I performed, Managed Memory was not really working in ROCm 5.x but it does work at least in ROCm 6.1.2. Is the XLA implementation able to leverage managed memory to allow CPU memory to be used as extension of the GPU memory? The feature is already supported for NVIDIA GPUs and was wondering whether there are any plans to implement it for AMD too.

### Operating System

_No response_

### GPU

MI250

### ROCm Component

XLA