# [Documentation]: PyTorch via PIP installation

- **Issue #:** 5733
- **State:** closed
- **Created:** 2025-12-03T03:37:05Z
- **Updated:** 2025-12-08T14:43:36Z
- **Labels:** Documentation, status: fix submitted
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5733

### Description of errors

## Title: PyTorch Windows Installation - Add `--no-deps` flag to prevent CPU wheel override

### Documentation Page
https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/windows/install-pytorch.html

### Problem

The current installation instructions can fail silently when pip's dependency resolver overwrites the ROCm PyTorch wheel with the CPU-only version from PyPI.

When installing `torchaudio` or `torchvision`, pip sees `torch` as a dependency and may pull `torch==2.9.1` (CPU) from PyPI, replacing the previously installed `torch==2.9.0+rocmsdk20251116` (ROCm).

**Symptom:**
```
python -c "import torch; print(torch.__version__)"
# Expected: 2.9.0+rocmsdk20251116
# Actual:   2.9.1+cpu
```

This is especially likely to occur if:
- The user has previously installed PyTorch in any environment
- pip's cache contains a CPU wheel
- The user installs packages one at a time rather than in a single command

### Current Documentation

```bash
pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torch-2.9.0+rocmsdk20251116-cp312-cp312-win_amd64.whl
pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torchaudio-2.9.0+rocmsdk20251116-cp312-cp312-win_amd64.whl
pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torchvision-0.24.0+rocmsdk20251116-cp312-cp312-win_amd64.whl
```

### Proposed Fix

**Option A: Add `--no-deps` flag and install dependencies separately**

```bash
# Install PyTorch wheels without dependency resolution
pip install --no-cache-dir --no-deps https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torch-2.9.0+rocmsdk20251116-cp312-cp312-win_amd64.whl
pip install --no-cache-dir --no-deps https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torchaudio-2.9.0+rocmsdk20251116-cp312-cp312-win_amd64.whl
pip install --no-cache-dir --no-deps https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torchvision-0.24.0+rocmsdk20251116-cp312-cp312-win_amd64.whl

# Install torch dependencies
pip install filelock fsspec jinja2 networkx sympy typing-extensions pillow numpy
```

**Option B: Install all three in a single command**

```bash
pip install --no-cache-dir \
    https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torch-2.9.0+rocmsdk20251116-cp312-cp312-win_amd64.whl \
    https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torchaudio-2.9.0+rocmsdk20251116-cp312-cp312-win_amd64.whl \
    https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torchvision-0.24.0+rocmsdk20251116-cp312-cp312-win_amd64.whl
```

### Additional Suggestion

Add a verification step immediately after installation to catch this issue early:

```bash
# Verify ROCm wheel is installed (not CPU version)
python -c "import torch; assert 'rocmsdk' in torch.__version__, f'ERROR: CPU wheel installed: {torch.__version__}'"
```

### Environment
- OS: Windows 11 (10.0.26200)
- GPU: AMD Radeon RX 9060 XT
- Python: 3.12
- ROCm: 7.1.1

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_