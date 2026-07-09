# parallel build is not working for llvm part of rocm:

- **Issue #:** 1255
- **State:** closed
- **Created:** 2020-10-08T05:48:36Z
- **Updated:** 2020-10-19T18:18:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/1255

parallel build is not working for llvm part of rocm:

Taken from https://github.com/ROCm-Developer-Tools/llvm-project
...
Running a serial build will be slow. To improve speed, try running a parallel build. That's done by default in Ninja; for make, use the option -j NNN, where NNN is the number of parallel jobs, e.g. the number of CPUs you have.
...

However using -j 8 switch is not going through full build an appears to be skipping:

[build-j8.txt](https://github.com/RadeonOpenCompute/ROCm/files/5345553/build-j8.txt)
[build-j8-1.txt](https://github.com/RadeonOpenCompute/ROCm/files/5345554/build-j8-1.txt)
[build.txt](https://github.com/RadeonOpenCompute/ROCm/files/5345555/build.txt)



