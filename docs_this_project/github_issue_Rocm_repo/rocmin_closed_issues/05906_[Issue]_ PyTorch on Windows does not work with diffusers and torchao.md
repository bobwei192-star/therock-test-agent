# [Issue]: PyTorch on Windows does not work with diffusers and torchao

- **Issue #:** 5906
- **State:** closed
- **Created:** 2026-01-26T19:27:13Z
- **Updated:** 2026-06-25T15:56:28Z
- **Labels:** status: triage
- **Assignees:** benrichard-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5906

### Problem Description

With these packages installed (`install -r requirements.txt`):
```
accelerate==1.12.0
diffusers==0.36.0
transformers==4.57.6
```
the following Python code runs without errors:
```
import torch
from diffusers import AutoPipelineForText2Image
```

However, if I add torchao (`pip install torchao==0.15.0`) the Python code exits with the following error:
```
ModuleNotFoundError                       Traceback (most recent call last)
File c:\Users\andju\rocm-test\venv\Lib\site-packages\diffusers\utils\import_utils.py:1016, in _LazyModule._get_module(self, module_name)
   1015 try:
-> 1016     return importlib.import_module("." + module_name, self.__name__)
   1017 except Exception as e:

File C:\Program Files\Python312\Lib\importlib\__init__.py:90, in import_module(name, package)
     89         level += 1
---> 90 return _bootstrap._gcd_import(name[level:], package, level)

File <frozen importlib._bootstrap>:1387, in _gcd_import(name, package, level)

File <frozen importlib._bootstrap>:1360, in _find_and_load(name, import_)

File <frozen importlib._bootstrap>:1331, in _find_and_load_unlocked(name, import_)

File <frozen importlib._bootstrap>:935, in _load_unlocked(spec)

File <frozen importlib._bootstrap_external>:999, in exec_module(self, module)

File <frozen importlib._bootstrap>:488, in _call_with_frames_removed(f, *args, **kwds)

File c:\Users\andju\rocm-test\venv\Lib\site-packages\diffusers\pipelines\auto_pipeline.py:21
     20 from ..configuration_utils import ConfigMixin
...
   1020         f" traceback):\n{e}"
   1021     ) from e

RuntimeError: Failed to import diffusers.pipelines.auto_pipeline because of the following error (look up to see its traceback):
No module named 'torch._C._distributed_c10d'; 'torch._C' is not a package
```

### Operating System

Windows 11 10.0.26200

### CPU

AMD Ryzen 7 7800X3D 8-Core Processor

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

ROCm 7.2

### ROCm Component

_No response_

### Steps to Reproduce

1. Install Python 3.12.
2. Create and activate a venv.
3. Follow the steps described here: https://rocm.docs.amd.com/projects/radeon-ryzen/en/docs-7.2/docs/install/installrad/windows/install-pytorch.html.
4. Follow the steps described in the "Problem Description".

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_