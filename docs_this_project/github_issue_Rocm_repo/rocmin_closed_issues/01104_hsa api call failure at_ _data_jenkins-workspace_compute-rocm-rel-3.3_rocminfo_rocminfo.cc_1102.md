# hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102

- **Issue #:** 1104
- **State:** closed
- **Created:** 2020-05-08T19:38:50Z
- **Updated:** 2021-03-04T09:45:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/1104

**OS:** Debian 10
**KERNEL:** 4.19.0-8-amd64
**GPU:** RX550

Output of `/opt/rocm/bin/rocminfo`

> hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
> Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

Output of `sudo dmesg | grep amdgpu`

> [    2.850571] [drm] amdgpu kernel modesetting enabled.
> [    2.850571] [drm] amdgpu version: 5.4.8
> [    2.893869] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_mc.bin
> [    2.893878] amdgpu 0000:03:00.0: VRAM: 2048M 0x000000F400000000 - 0x000000F47FFFFFFF (2048M used)
> [    2.893879] amdgpu 0000:03:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
> [    2.894033] [drm] amdgpu: 2048M of VRAM memory ready
> [    2.894035] [drm] amdgpu: 15883M of GTT memory ready.
> [    2.894718] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_pfp_2.bin
> [    2.894727] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_me_2.bin
> [    2.894734] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_ce_2.bin
> [    2.894744] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_rlc.bin
> [    2.894811] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_mec_2.bin
> [    2.894897] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_mec2_2.bin
> [    2.895652] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_sdma.bin
> [    2.895675] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_sdma1.bin
> [    2.895728] amdgpu: [powerplay] hwmgr_sw_init smu backed is polaris10_smu
> [    2.895846] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_uvd.bin
> [    2.897947] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_vce.bin
> [    2.898595] amdgpu 0000:03:00.0: firmware: direct-loading firmware amdgpu/polaris12_smc.bin
> [    3.143266] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:03:00.0 on minor 1

What could be the case here?

EDIT:

I will try to debug this through the steps that are mentioned in #1088 