# [Issue]: Attempting to use hipBLASLt on an unsupported architecture!

- **Issue #:** 4440
- **State:** closed
- **Created:** 2025-03-03T19:42:22Z
- **Updated:** 2025-06-23T14:08:46Z
- **Labels:** Under Investigation, ROCm 6.2.2
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4440

### Problem Description

This issue is posted it on behalf of OP on [this post from discuss.pytorch.org](https://discuss.pytorch.org/t/rocm-hipblaslt-error-with-gfx1103/212721).

PyTorch outputs the following when attempting to use HipBlasLt as the BLAS backend:

`UserWarning: Attempting to use hipBLASLt on an unsupported architecture! Overriding blas backend to hipblas`

The user has set `HSA_OVERRIDE_GFX_VERSION=11.0.0` on a machine using a Radeon 780M (`gfx1103` by default).

ROCm has been installed via [`pacman`](https://gitlab.archlinux.org/archlinux/packaging/packages/rocm-hip-sdk), HipBlasLt has been built/installed from [source](https://github.com/ROCm/hipBLASLt).

This minimal example is enough to reproduce the error:

```
>>> import torch
>>> t = torch.rand((5,5), device=0)
>>> l = torch.nn.Linear(5,5).to(0)
>>> l(t)
```

Arch is not a supported operating system, but this error is consistent with other reports on cards using `gfx1100`.

[Here](https://discuss.pytorch.org/t/rocm6-2-build-of-pytroch-is-faling-for-llama3-2-vision-model/211622) is another post from discuss.pytorch.org that reports a similar issues when using a Radeon 7900 XTX (natively `gfx1100`). For this user, it seems that updating PyTorch resolved the issue.

#4437 outlines a similar error in detail.

#3949 Describes this issue, and links to a relevant [issue](https://github.com/pytorch/pytorch/issues/138067) and [PR](https://github.com/pytorch/pytorch/pull/138267) on the pytorch repo. It seems that this PR was [eventually merged into the ROCm branch of pytorch](https://github.com/ROCm/pytorch/pull/1855).

Could we get verification that this issue no longer persists on `gfx1100`?

### Operating System

Arch Linux

### CPU

Unknown

### GPU

AMD Radeon 780M

### ROCm Version

ROCm 6.2.2

### ROCm Component

hipBLAS

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_