# Stuck on OpenCl 1.1

- **Issue #:** 601
- **State:** closed
- **Created:** 2018-11-05T11:37:49Z
- **Updated:** 2018-11-16T15:02:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/601

Added repo http://repo.radeon.com/rocm/yum/rpm/
Installed rocm-opencl-1.2.0
clinfo says:
```
Number of platforms:				 2
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.1 Mesa 18.0.5
  Platform Name:				 Clover
  Platform Vendor:				 Mesa
  Platform Extensions:				 cl_khr_icd
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.2 pocl 1.1 RelWithDebInfo, LLVM 6.0.1, SPIR, SLEEF, DISTRO, POCL_DEBUG
  Platform Name:				 Portable Computing Language
  Platform Vendor:				 The pocl project
  Platform Extensions:				 cl_khr_icd
```
My system:
Fedora 28 on linux 4.18
Cpu: Intel core i5 8600k
Gpu: Amd RX 560

Is it a mesa issue?