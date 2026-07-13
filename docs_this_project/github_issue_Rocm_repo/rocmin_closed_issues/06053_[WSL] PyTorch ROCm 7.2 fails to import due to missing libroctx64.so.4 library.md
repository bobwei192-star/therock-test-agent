# [WSL] PyTorch ROCm 7.2 fails to import due to missing libroctx64.so.4 library

- **Issue #:** 6053
- **State:** closed
- **Created:** 2026-03-21T16:30:05Z
- **Updated:** 2026-05-01T18:43:34Z
- **Labels:** status: assessed
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6053

### Problem Description

### Description

PyTorch ROCm 7.2 wheel package cannot be imported on WSL2 because the WSL ROCm runtime package (`hsa-runtime-rocr4wsl-amdgpu`) is missing required libraries that PyTorch depends on.

### System Information

- **OS**: Ubuntu 24.04 (WSL2)
- **Kernel**: 6.6.87.2-microsoft-standard-WSL2
- **Python**: 3.12.3
- **PyTorch**: 2.9.1+rocm7.2.0.lw.git7e1940d4
- **Windows Driver**: AMD Software: Adrenalin Edition 26.1.1
- **GPU**: AMD Radeon RX 7900 XTX

### Installed Packages

```bash
# ROCm packages installed via amdgpu-install
ii  hsa-runtime-rocr4wsl-amdgpu:amd64  25.30.13-2281980.24.04
ii  rocm-core                          7.2.0.70200-43~24.04
```

### Error Message

```python
>>> import torch
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/path/to/venv/lib/python3.12/site-packages/torch/__init__.py", line 427, in <module>
    from torch._C import *
ImportError: libroctx64.so.4: cannot open shared object file: No such file or directory
```

### Missing Libraries

The following libraries are required by PyTorch ROCm but are NOT included in the WSL ROCm package:

- `libroctx64.so.4` (ROCm Tracer/ROCTX)
- `librocprofiler64.so` (ROCm Profiler)
- `librocm_smi64.so` (ROCm SMI)

### Steps to Reproduce

1. Install Windows with AMD Adrenalin 26.1.1 driver
2. Install WSL2 with Ubuntu 24.04
3. Install ROCm for WSL:
   ```bash
   wget https://repo.radeon.com/amdgpu-install/7.2/ubuntu/noble/amdgpu-install_7.2.70200-1_all.deb
   apt install ./amdgpu-install_7.2.70200-1_all.deb
   amdgpu-install -y --usecase=wsl,rocm --no-dkms
   ```
4. Install PyTorch ROCm wheel from AMD repo
5. Try to import torch:
   ```bash
   python -c "import torch"
   ```

### Expected Behavior

PyTorch should import successfully and detect the AMD GPU through WSL2 GPU passthrough.

### Actual Behavior

Import fails with `ImportError: libroctx64.so.4: cannot open shared object file`

### Workaround

Currently, the only working workaround is to use Docker container with full ROCm stack.

### Request

Please either:

1. **Include the missing libraries** (`libroctx64.so.4`, etc.) in the WSL ROCm package
2. **OR** Update the PyTorch ROCm wheel to make these libraries optional
3. **OR** Provide a separate WSL-compatible PyTorch wheel

### References

- AMD WSL Installation Guide: https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/wsl/install-radeon.html
- AMD PyTorch Installation Guide: https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/wsl/install-pytorch.html

---

### Operating System

Ubuntu 24.04 (WSL2)

### CPU

AMD Ryzen 7 9700X

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

rocm7.2.0.lw.git7e1940d4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_