# AMDGPU DKMS Not Compiling Linux 6.1.52

> **Issue #2451**
> **状态**: closed
> **创建时间**: 2023-09-13T02:33:25Z
> **更新时间**: 2024-04-19T10:23:07Z
> **关闭时间**: 2023-11-10T15:55:59Z
> **作者**: blu006
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2451

## 描述

Compiling the AMDGPU present in the jammy repository (1:6.1.5.50600-1609671.20.04) against kernel headers version 6.1.52 

```
CC [M]  /var/lib/dkms/amdgpu/6.1.5-1609671.20.04/build/amd/amdgpu/../display/dc/basics/vector.o
/var/lib/dkms/amdgpu/6.1.5-1609671.20.04/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm.c: In function ‘dm_handle_mst_sideband_msg’:
/var/lib/dkms/amdgpu/6.1.5-1609671.20.04/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm.c:3314:25: error: implicit declaration of function ‘drm_dp_mst_hpd_irq’; did you mean ‘drm_dp_mst_dpcd_write’? [-Werror=implicit-function-declaration]
 3314 |                         drm_dp_mst_hpd_irq(
      |                         ^~~~~~~~~~~~~~~~~~
      |                         drm_dp_mst_dpcd_write
  CC [M]  /var/lib/dkms/amdgpu/6.1.5-1609671.20.04/build/amd/amdgpu/../display/dc/basics/dc_common.o
```

A similar issue was reported on another project https://github.com/strongtz/i915-sriov-dkms/issues/97 I believe the summary from that issue was something like drm_dp_mst_hpd_irq() being split into multiple functions in a later kernel (6.4?) and that change being backported to later versions of kernel 6.1.

Unfortunately, I am not familiar enough with the codebase to make any changes to the code.
