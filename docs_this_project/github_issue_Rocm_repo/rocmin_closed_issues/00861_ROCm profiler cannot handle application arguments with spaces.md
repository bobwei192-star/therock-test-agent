# ROCm profiler cannot handle application arguments with spaces

- **Issue #:** 861
- **State:** closed
- **Created:** 2019-08-12T13:39:11Z
- **Updated:** 2020-09-30T14:53:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/861

Both rocprof and rcprof have the following issue treating `exe -g "2 2 1"` as `exe -g 2 2 1` and cause application failure.
I make one PR and one issue but got no feedback so far.
https://github.com/ROCm-Developer-Tools/rocprofiler/pull/7
https://github.com/GPUOpen-Tools/RCP/issues/29