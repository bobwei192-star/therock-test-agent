# ROCm installation for RX550

- **Issue #:** 1581
- **State:** closed
- **Created:** 2021-09-28T21:09:10Z
- **Updated:** 2021-09-30T16:16:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1581

Hi,

I installed ROCm following the instructions here: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu .
I am using Ubuntu 18.04.5 and I downgraded the kernel to 5.4.0.71 to have the same reported in the instructions.
ROCm 4.3 fails with the problem reported in this issue: https://github.com/RadeonOpenCompute/ROCm/issues/1302
ROCm 4.1 fails with the following error
`ERROR: rocprofiler_iterate_info(), Translate(), ImportMetrics: bad block name 'GRBM', GPU device_id(699f) is not supported`
`/usr/bin/rocprof: line 358:  2582 Aborted                 (core dumped) /opt/rocm-4.1.0/rocprofiler/tool/ctrl`

I am trying to analyze an RX 550.
Could you please report which package versions (Ubuntu, kernel, ROCm, amdgpu) should be used for this GPU?
