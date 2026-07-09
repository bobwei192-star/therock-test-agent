# Documentation for OpenCL-only ROCm install

- **Issue #:** 474
- **State:** closed
- **Created:** 2018-07-27T10:13:57Z
- **Updated:** 2020-02-10T15:57:00Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/474

Looking at this page https://github.com/RadeonOpenCompute/ROCm for installation instructions,
I install rocm-dkms. But this package install many other dependencies:
dkms hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs rocm-smi rocm-utils rocminfo

I would like instructions for installing a minimal OpenCL-only ROCm. For example, is "hcc" needed for an OpenCL-only install?
