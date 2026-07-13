# Build error with GCC 8.2.0

- **Issue #:** 598
- **State:** closed
- **Created:** 2018-11-02T20:27:30Z
- **Updated:** 2018-12-24T21:51:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/598

On PPC64:

```
drivers/gpu/drm/amd/amdgpu/../powerplay/hwmgr/smu7_hwmgr.c: In function ‘smu7_notify_link_speed_change_after_state_change’:
drivers/gpu/drm/amd/amdgpu/../powerplay/hwmgr/smu7_hwmgr.c:3897:7: error: implicit declaration of function ‘amdgpu_acpi_pcie_performance_request’; did you mean ‘smu7_pcie_performance_request’? [-Werror=implicit-function-declaration]
   if (amdgpu_acpi_pcie_performance_request(hwmgr->adev, request, false)) {
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       smu7_pcie_performance_request
cc1: some warnings being treated as errors
```