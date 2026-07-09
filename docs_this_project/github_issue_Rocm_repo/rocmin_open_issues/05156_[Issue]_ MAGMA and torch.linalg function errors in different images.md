# [Issue]: MAGMA and torch.linalg function errors in different images

- **Issue #:** 5156
- **State:** open
- **Created:** 2025-08-06T03:41:52Z
- **Updated:** 2025-10-01T17:03:05Z
- **Labels:** Under Investigation, AMD Instinct MI300X
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5156

### Problem Description

When using `hf_model.model.resize_token_embeddings`, there is an error:
```
RuntimeError: Calling torch.linalg.cholesky on a CUDA tensor requires compiling PyTorch with MAGMA. Please use PyTorch built with MAGMA support
```

Seems it's related to docker image building without MAGMA.

More discussions are here:

https://github.com/huggingface/transformers/issues/36660#issuecomment-3153166699

### Operating System

Unknown

### CPU

Unknown

### GPU

Mi300x

### ROCm Version

ROCm 6.4.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_