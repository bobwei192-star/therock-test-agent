# Q: OpenCL preprocessor define to identify ROCm or __asm() support

- **Issue #:** 805
- **State:** closed
- **Created:** 2019-05-29T10:55:12Z
- **Updated:** 2024-10-04T09:06:52Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/805

Is there a way, in the OpenCL source, to identify whether it's the ROCm OpenCL that is compiling the code (as opposed to, e.g. amdgpu-pro or something else).

In particular, I'd like to be able to #if case in OpenCL whether __asm() is supported. Being able to identify ROCm would bring me halfway there as I know that ROCm-OpenCL supports __asm().
