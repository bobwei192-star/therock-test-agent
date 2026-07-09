# Different branches of llvm-project

- **Issue #:** 988
- **State:** closed
- **Created:** 2019-12-31T11:38:47Z
- **Updated:** 2022-05-01T09:06:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/988

There are currently different repositories and branches to build components of ROCm.

To build ROCm-OpenCL-Runtime "roc-ocl-3.0.0" branch from https://github.com/RadeonOpenCompute/llvm-project (fork) should be used.

To build ROCm-Device-Libs "amd-std-open" branch from https://github.com/RadeonOpenCompute/llvm-project.git (fork) should be used.

And to build AOMP "AOMP-191029" branch from https://github.com/ROCm-Developer-Tools/llvm-project (mirror) is used. According to the clone script, for "ROCm-Device-Libs" "roc-ocl-3.0.x" branch, the same compiler is used.


It seems that building "ROCm-OpenCL-Runtime" and "AOMP" (OpenMP) needs two different branches of compilers(?).

Will this be merged together, to get one repository and one branch to build them all?
