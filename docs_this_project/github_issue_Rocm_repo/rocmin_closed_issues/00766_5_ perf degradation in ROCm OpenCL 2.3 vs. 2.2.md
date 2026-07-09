# 5% perf degradation in ROCm OpenCL 2.3 vs. 2.2

- **Issue #:** 766
- **State:** closed
- **Created:** 2019-04-14T14:15:53Z
- **Updated:** 2021-05-09T20:08:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/766

Using GpuOwl https://github.com/preda/gpuowl
Ubuntu 19.04, Linux kernel 5.0.7, Radeon VII

Upon upgrade ROCm 2.2 -> 2.3, without changing anything else, there is a performance degradation of 5-6% in GpuOwl.

Upon seeing this I tried to move back to ROCm 2.2, but it seems 2.2 is missing from the archive
http://repo.radeon.com/rocm/archive/ , so I downgraded to ROCm 2.1.

For comparison I attach isa dump with "old" (ROCm 2.1) and "new" (ROCm 2.3), where new is 5% slower.

Also please provide a way to install back ROCm 2.2 (e.g. by uploading it to archive).

[new.txt](https://github.com/RadeonOpenCompute/ROCm/files/3077435/new.txt)
[old.txt](https://github.com/RadeonOpenCompute/ROCm/files/3077436/old.txt)
