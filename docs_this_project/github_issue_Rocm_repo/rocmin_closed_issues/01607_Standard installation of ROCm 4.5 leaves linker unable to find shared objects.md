# Standard installation of ROCm 4.5 leaves linker unable to find shared objects

- **Issue #:** 1607
- **State:** closed
- **Created:** 2021-11-02T09:09:20Z
- **Updated:** 2021-11-21T22:21:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1607

Following the installation guide [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html) using the `amdgpu-install --usecase=hiplibsdk,rocm` method leaves the system unable to run Tensorflow-rocm. This is due to several necessary libraries being missing from locations in the LD_LIBRARY_PATH. Prepending a manually extended LD_LIBRARY_PATH fixes this and enables training on the GPU:
`$ LD_LIBRARY_PATH="/opt/rocm/rocblas/lib/:/opt/rocm/rccl/lib/:/opt/rocm/hsa/lib/:/opt/rocm/hip/lib/:/opt/rocm/miopen/lib/:/opt/rocm/hipfft/lib/:/opt/rocm/rocrand/lib/::$LD_LIBRARY_PATH" python3 mlp\ classifier.py`

OpenCL is unaffected by this.

OS: Ubuntu 20.4.3
CPU: Ryzen9 5900X
GPU: AMD Radeon RX6800