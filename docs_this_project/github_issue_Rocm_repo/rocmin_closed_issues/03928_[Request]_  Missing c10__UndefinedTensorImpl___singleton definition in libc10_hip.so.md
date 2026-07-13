# [Request]:  Missing c10::UndefinedTensorImpl::_singleton definition in libc10_hip.so

- **Issue #:** 3928
- **State:** closed
- **Created:** 2024-10-21T11:01:42Z
- **Updated:** 2024-10-23T08:05:40Z
- **Labels:** Under Investigation, ROCm 6.2.3, mi300
- **URL:** https://github.com/ROCm/ROCm/issues/3928

### Problem Description

hi, rocm expert, when building a rocm /torch project with following link flags:

```py
torch_libs = ["torch", "torch_hip", "torch_python", "c10", "c10_hip"]
torch_link_libs ="-L/opt/conda/envs/py_3.10/lib/python3.10/site-packages/torch/lib/ " + " ".join([f"-l{lib}" for lib in torch_libs])
``` 

but get the following undefined error

```yml
/opt/conda/envs/py_3.10/lib/python3.10/site-packages/torch/lib/libc10.so | grep _singleton
00000000000e3aa0 B c10::UndefinedTensorImpl::_singleton
``` 

rocm/torch image: rocm/pytorch:rocm6.2_ubuntu22.04_py3.10_pytorch_release_2.3.0 

Thanks for clarifying
David 

### Operating System

Ubuntu 22.04

### CPU

Ryzen 

### GPU

mi300

### ROCm Version

ROCm 6.2.3

### ROCm Component

hipBLAS

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_