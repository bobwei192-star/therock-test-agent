# HIP packages don’t seem to get updated anymore

- **Issue #:** 619
- **State:** closed
- **Created:** 2018-11-19T16:20:34Z
- **Updated:** 2018-11-19T16:44:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/619

Hey there, don’t know whether I’m being totally stupid or the hip packages (mainly `hip_base`) are quite out of date in the Ubuntu Xenial repository. As per link in the README of this repo, I’d expect HIP to be in the state of its roc-1.9.x branch: https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/tree/roc-1.9.x

Yet when I locally inspect the installed `/opt/rocm/hip/include/hip/hcc_detail/device_functions.hpp` for example, they are out of date compared to the file in the github branch. Timestamp says September 5.

Hope we can figure this out!
Cheers!