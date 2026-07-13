# lockups and performance issues running iterative algorithms via OpenCL

- **Issue #:** 68
- **State:** closed
- **Created:** 2017-01-03T19:06:49Z
- **Updated:** 2017-01-16T02:49:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/68

First - I've not validated output - I suspect invalid data - but I have been using arrayfire benchmarks to track performance of OpenCL on  ROCm and AMDGPU Pro (and OpenCL/CUDA, on NVidia boxen).

Please give this program a try (after installing arrayfire).
https://github.com/nevion/arrayfire-benchmark

You will note that Cholesky_f32/ Cholesky_f64 can soft lock or hardlock the machine (ROCm= softlock, AMDGPU-Pro=hardlock)

You will also note atrocious performance on sorting benchmarks.  The 2 could be related as these are data-driven iterative algorithms and possibly the only such in the benchmarks available.  The remainder of the benchmarks run seemingly run at acceptable (not necessarily performant) rates on the AMD stacks.  They all run acceptably on NVidia's OpenCL runtime.

You can list benchmarks with the -l argument.  All benchmarks function on CUDA's OpenCL