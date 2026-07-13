# [Feature]: tensorflow on gfx1102 / RX7600

- **Issue #:** 2945
- **State:** closed
- **Created:** 2024-03-06T07:13:35Z
- **Updated:** 2024-04-05T15:23:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/2945

### Suggestion Description

On Linux, RX7600 do not seems to be supported :
```
# docker run -it --network=host --device=/dev/kfd --device=/dev/dri \
                 --ipc=host --shm-size 16G --group-add video --cap-add=SYS_PTRACE \
                 --security-opt seccomp=unconfined rocm/tensorflow:latest
tf-docker / > python
Python 3.9.18 (main, Aug 25 2023, 13:20:04)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow
2024-03-06 07:00:40.549184: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
/usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.18) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
>>> tensorflow.config.list_physical_devices('GPU')
2024-03-06 07:01:21.149888: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:756] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-03-06 07:01:26.856968: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:756] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-03-06 07:01:26.857151: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:756] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-03-06 07:01:26.857236: I tensorflow/core/common_runtime/gpu/gpu_device.cc:2266] Ignoring visible gpu device (device: 0, name: AMD Radeon RX 7600, pci bus id: 0000:0d:00.0) with AMDGPU version : gfx1102. The supported AMDGPU versions are gfx1030gfx1100, gfx900, gfx906, gfx908, gfx90a, gfx940, gfx941, gfx942.
[]
```
(empty list of supported GPU)

Did I make a mistake ?
Is it planned ?

### Operating System

Arch Linux

### GPU

gfx1102

### ROCm Component

_No response_