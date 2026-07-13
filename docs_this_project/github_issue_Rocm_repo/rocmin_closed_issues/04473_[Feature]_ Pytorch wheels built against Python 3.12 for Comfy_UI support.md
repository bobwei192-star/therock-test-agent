# [Feature]: Pytorch wheels built against Python 3.12 for Comfy_UI support

- **Issue #:** 4473
- **State:** closed
- **Created:** 2025-03-10T15:52:15Z
- **Updated:** 2025-05-27T15:46:20Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4473

### Suggestion Description

TLDR; Add a pytorch wheel with ROCm support built against Python 3.12 in addition to Python 3.10.


In triaging issues for users, I've found that there's strong interest in using [Comfy_UI[(https://github.com/comfyanonymous/ComfyUI) for running diffusion models on AMD GPUs, particularly in WSL2 environments and with Radeon GPUs. (e.g. [r/ROCm subbreddit discussion](https://www.reddit.com/r/ROCm/comments/1j3eyp5/comment/mgnia05/), [discuss.pytorch.org](https://discuss.pytorch.org/t/comfy-ui-attempting-to-use-hipblaslt-on-a-unsupported-architecture/215776/19) )

Users have pointed out that Comfy_UI requires Python 3.12, but the Pytorch wheels packages for AMD GPUs are built against  Python 3.10 (See the notes in [ROCm docs](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-pytorch.html#install-methods) ), which may be causing problems out of the box.

The workaround of course, is to [build pytorch from source with the preferred Python version](https://github.com/pytorch/pytorch/?tab=readme-ov-file#amd-rocm-support). However, this is a time-intensive process that does not contribute to a good user experience (for those that don't like installing packages from source).




### Operating System

WSL2

### GPU

_No response_

### ROCm Component

pytorch