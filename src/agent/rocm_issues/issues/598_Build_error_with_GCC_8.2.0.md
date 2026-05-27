# Build error with GCC 8.2.0

> **Issue #598**
> **状态**: closed
> **创建时间**: 2018-11-02T20:27:30Z
> **更新时间**: 2018-12-24T21:51:50Z
> **关闭时间**: 2018-12-24T21:51:50Z
> **作者**: madscientist159
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/598

## 描述

On PPC64:

```
drivers/gpu/drm/amd/amdgpu/../powerplay/hwmgr/smu7_hwmgr.c: In function ‘smu7_notify_link_speed_change_after_state_change’:
drivers/gpu/drm/amd/amdgpu/../powerplay/hwmgr/smu7_hwmgr.c:3897:7: error: implicit declaration of function ‘amdgpu_acpi_pcie_performance_request’; did you mean ‘smu7_pcie_performance_request’? [-Werror=implicit-function-declaration]
   if (amdgpu_acpi_pcie_performance_request(hwmgr->adev, request, false)) {
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       smu7_pcie_performance_request
cc1: some warnings being treated as errors
```

---

## 评论 (2 条)

### 评论 #1 — madscientist159 (2018-11-02T20:33:34Z)

The following patch fixes the issue:

```diff --git a/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c b/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c
index ae4c483e340f..d5086ee9063b 100644
--- a/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c
+++ b/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c
@@ -3894,12 +3894,14 @@ static int smu7_notify_link_speed_change_after_state_change(
                                smu7_get_current_pcie_speed(hwmgr) > 0)
                        return 0;

+#ifdef CONFIG_ACPI
                if (amdgpu_acpi_pcie_performance_request(hwmgr->adev, request, false)) {
                        if (PP_PCIEGen2 == target_link_speed)
                                pr_info("PSPP request to switch to Gen2 from Gen3 Failed!");
                        else
                                pr_info("PSPP request to switch to Gen1 from Gen2 Failed!");
                }
+#endif
        }

        return 0;
```

---

### 评论 #2 — jlgreathouse (2018-12-24T21:51:50Z)

This should be fixed [as of ROCm 2.0.0](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c#L3902). Thanks!

---
