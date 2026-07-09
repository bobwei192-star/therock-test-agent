# [Issue]: torch 2.9 + rocm7.1 release as a docker image in `rocm/pytorch`

- **Issue #:** 5695
- **State:** closed
- **Created:** 2025-11-25T19:35:04Z
- **Updated:** 2025-12-12T17:43:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/5695

### Problem Description

Hi,

I noticed there is no docker image for torch 2.9 + rocm 7.1 at https://hub.docker.com/r/rocm/pytorch/tags. Do you know why is that?

`rocm/vllm-dev:nightly_main_20251117` contains a certain `2.9.0a0+git1c57644`, which seems to come from https://github.com/vllm-project/vllm/blob/c32a18cbe7342ac0700802b94ae98bbf928a00f0/docker/Dockerfile.rocm_base#L4 i.e. https://github.com/ROCm/pytorch/commit/1c57644d4cb3aff84642e1326d88681a656507ce

Any chance to get a pytorch 2.9 stable + rocm 7.1 release, as a standalone docker image?

PyTorch 2.10 release is only planned end January (see https://dev-discuss.pytorch.org/t/pytorch-release-2-10-key-dates-updated/3259), and using nightly is not the greatest of ideas.

Thank you!

### Operating System

Irrelevant

### CPU

Irrelevant

### GPU

Irrelevant

### ROCm Version

Irrelevant

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_