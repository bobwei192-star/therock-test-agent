# rocm-asan 7.x needs libdrm-amdgpu-common which is only available in older (<= 6.x) amdgpu drivers

- **Issue #:** 6144
- **State:** closed
- **Created:** 2026-04-13T11:47:33Z
- **Updated:** 2026-04-20T14:34:59Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6144

Hi,

rocm-asan 7.x needs libdrm-amdgpu-common which is only available in older (<= 6.x) amdgpu drivers.

I guess libdrm-amdgpu-common should be shipped with amdgpu >= 7.x (also >= 25.x).

Regards
Ragnar
