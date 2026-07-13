# [Issue]: PyTorch ROCm issues when using GRU under Windows

- **Issue #:** 6314
- **State:** closed
- **Created:** 2026-05-29T13:05:09Z
- **Updated:** 2026-05-31T13:58:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/6314

### Problem Description

When using a [GRU unit](https://docs.pytorch.org/docs/2.12/generated/torch.nn.GRU.html) and moving it to the gpu, the forward pass will fail with:
```
MIOpen(HIP): Error [Compile] 'hiprtcCompileProgram(prog.get(), c_options.size(), c_options.data())' MIOpenNeuron.cpp: HIPRTC_ERROR_COMPILATION (6)
Buffered 84 messages to file: DESKTOP-FFH0L33:C:\Users\krishkat\AppData\Local\Temp\miopen_error_12248.log
MIOpen(HIP): Error [BuildHip] HIPRTC status = HIPRTC_ERROR_COMPILATION (6), source file: MIOpenNeuron.cpp
Buffered 1 messages to file: DESKTOP-FFH0L33:C:\Users\krishkat\AppData\Local\Temp\miopen_error_12248.log
MIOpen(HIP): Warning [BuildHip] In file included from C:\Users\krishkat\AppData\Local\Temp\comgr-12248-10-fb0bcb\input\MIOpenNeuron.cpp:34:
In file included from C:\Users\krishkat\AppData\Local\Temp\comgr-12248-10-fb0bcb\include\activation_functions.hpp:131:
In file included from C:\Users\krishkat\AppData\Local\Temp\comgr-12248-10-fb0bcb\include\vector_types.hpp:8:
C:\Users\krishkat\AppData\Local\Temp\comgr-12248-10-fb0bcb\include\miopen_type_traits.hpp:151:10: fatal error: 'type_traits' file not found
  151 | #include <type_traits>
      |          ^~~~~~~~~~~~~
1 error generated when compiling for gfx1151.
MIOpen(HIP): Error [C:/home/runner/_work/TheRock/TheRock/rocm-libraries/projects/miopen/src/hipoc/hipoc_program.cpp:299] Code object build failed. Source: MIOpenNeuron.cpp
Buffered 2 messages to file: DESKTOP-FFH0L33:C:\Users\krishkat\AppData\Local\Temp\miopen_error_12248.log
MIOpen Error: DESKTOP-FFH0L33:C:/home/runner/_work/TheRock/TheRock/rocm-libraries/projects/miopen/src/hipoc/hipoc_program.cpp:299: Code object build failed. Source: MIOpenNeuron.cpp
Traceback (most recent call last):
  File "c:\Users\krishkat\...\gruTorch.py", line 19, in <module>
    gpu_pred = gru(data)
               ^^^^^^^^^
  File "C:\Users\krishkat\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\module.py", line 1778, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\krishkat\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\module.py", line 1789, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\krishkat\AppData\Local\Programs\Python\Python312\Lib\site-packages\torch\nn\modules\rnn.py", line 1438, in forward
    result = _VF.gru(
             ^^^^^^^^
RuntimeError: miopenStatusUnknownError
```
However the forward pass will work fine using the CPU.

### Operating System

Windows 11 Pro

### CPU

AMD Ryzen AI MAX 385

### GPU

AMD Radeon 8050S

### ROCm Version

7.2.0

### ROCm Component

MIOpen

### Steps to Reproduce

```python
import torch
from torch import nn
import numpy as np

# Create minimal example
gru = nn.GRU(3, 5, 2)
print(gru)
data = np.asarray([[1.1, 1.2, 1.1], [1.2, 1.3, 1.2], [1.3, 1.4, 1.3]])
data = torch.Tensor(data)
# CPU forward pass
cpu_pred = gru(data)
print("CPU:")
print(cpu_pred)
# GPU forward pass
device = torch.device("cuda")
gru = gru.to(device)
data = data.to(device)

gpu_pred = gru(data)
print("GPU:")
print(gpu_pred)
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

````
python -m torch.utils.collect_env
<frozen runpy>:128: RuntimeWarning: 'torch.utils.collect_env' found in sys.modules after import of package 'torch.utils', but prior to execution of 'torch.utils.collect_env'; this may result in unpredictable behaviour
Collecting environment information...
PyTorch version: 2.12.0a0+rocm7.13.0a20260313
Is debug build: False
CUDA used to build PyTorch: N/A
ROCM used to build PyTorch: 7.2.0

OS: Microsoft Windows 11 Pro (10.0.26200 64-Bit)
GCC version: Could not collect
Clang version: Could not collect
CMake version: Could not collect
Libc version: N/A

Python version: 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] (64-bit runtime)
Python platform: Windows-11-10.0.26200-SP0
Is CUDA available: True
CUDA runtime version: Could not collect
CUDA_MODULE_LOADING set to:
GPU models and configuration: AMD Radeon(TM) 8050S Graphics (gfx1151)
Nvidia driver version: Could not collect
cuDNN version: Could not collect
Is XPU available: False
HIP runtime version: 7.2.0
MIOpen runtime version: 3.5.1
Is XNNPACK available: True
Caching allocator config: N/A

CPU:
Name: AMD RYZEN AI MAX 385 w/ Radeon 8050S
Manufacturer: AuthenticAMD
Family: 107
Architecture: 9
ProcessorType: 3
DeviceID: CPU0
CurrentClockSpeed: 3600
MaxClockSpeed: 3600
L2CacheSize: 8192
L2CacheSpeed: None
Revision: 28672

Versions of relevant libraries:
[pip3] numpy==2.4.4
[pip3] torch==2.12.0a0+rocm7.13.0a20260313
[pip3] torchaudio==2.11.0a0+rocm7.13.0a20260313
[pip3] torchvision==0.26.0a0+rocm7.13.0a20260313
[conda] Could not collect
```