# PyTorch Group Convolution RuntimeError: miopenStatusUnknownError

- **Issue #:** 2748
- **State:** closed
- **Created:** 2023-12-18T12:11:35Z
- **Updated:** 2023-12-27T16:56:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/2748

**Using group convolution, i.e., the _groups_ parameter in pytorch convolution results in an error with ROCm.** There seems to be a similar issue in https://github.com/ROCm/ROCm/issues/2587

Container: [docker://rocm/pytorch:pytorch_rocm5.7_ubuntu22.04_py3.10_pytorch_2.0.1](https://hub.docker.com/layers/rocm/pytorch/rocm5.7_ubuntu22.04_py3.10_pytorch_2.0.1/images/sha256-21df283b1712f3d73884b9bc4733919374344ceacb694e8fbc2c50bdd3e767ee?context=explore)

GPU: AMD Instinct MI250X

Using _groups=3_ results in an error:
```python
import torch
import torch.nn.functional as F

F.conv2d(torch.ones(1, 3, 512, 512).cuda(), torch.ones(3, 1, 5, 5).cuda(), groups=3, padding=0, stride=1)
```
Open Error: /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/MLOpen/src/hip/handlehip.cpp:643: Failed getting available memory: invalid argument
MIOpen Error: /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/MLOpen/src/hip/handlehip.cpp:643: Failed getting available memory: invalid argument
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: miopenStatusUnknownError

While using _groups=1_ works fine:
```python
F.conv2d(torch.ones(1, 3, 512, 512).cuda(), torch.ones(3, 3, 5, 5).cuda(), groups=1, padding=0, stride=1)
```
tensor([[[[75., 75., 75.,  ..., 75., 75., 75.],
          ...,
          [75., 75., 75.,  ..., 75., 75., 75.]]]], device='cuda:0')