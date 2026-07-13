# BOINC Vega-based GPU processing does not work with ROCm

- **Issue #:** 1569
- **State:** closed
- **Created:** 2021-09-01T08:49:08Z
- **Updated:** 2021-12-31T08:09:48Z
- **URL:** https://github.com/ROCm/ROCm/issues/1569

**Background**
For many years now (even back during fglrx days) I've been using [BOINC](https://boinc.berkeley.edu/) successfully with AMD GPUs on Linux via amdgpu-pro. However, that changed with amdgpu-pro 20.45 onwards, when PAL-based OpenCL was dropped in favour of ROCr. While my Fiji-based GPUs still work okay using the 'legacy' OpenCL support in amdgpu-pro, my Vega-based GPUs (both Vega10 and Vega20) cannot process GPU tasks with ROCr-based OpenCL From amdgpu-pro versions 20.45 through to 21.10 inclusive, GPU tasks would crash immediately on attempting to run. With amdgpu-pro 21.20 to 21.30 (current release at time of writing), GPU tasks don't crash but instead appear to stall indefinitely - GPUs appear idle and there is no application progress.

This saga is documented in https://community.amd.com/t5/opencl/amdgpu-pro-20-45-rocr-vs-pal-opencl-breaks-boinc-gpu-processing/td-p/453227

**Relevance to ROCm**
I'm still not entirely clear on the relationship between ROCm and ROCr other than ROCr seems to be a run-time sub-set of ROCm?

The reason I'm reporting this here is because I finally managed to get BOINC running with ROCm 4.3 on Ubuntu 20.04.3 (kernel 5.11.0-27) yesterday. However, my experience appears to be identical to the aforementioned stalled processing with ROCr-based OpenCL support from amdgpu-pro. I've been told that BOINC and ROCm appear to work just fine on Polaris-based GPUs.

As a work-around, I've been relying on the last PAL-based OpenCL release of amdgpu-pro, version 20.40. That's not a feasible long-term solution, however, as amdgpu-pro 20.40 does not install with Ubuntu kernels beyond 5.4.0-54. If there is indeed a connection between the behaviour I'm observing for ROCm and ROCr-based OpenCL support from amdgpu-pro, I can report my findings here as well as on AMD Community.