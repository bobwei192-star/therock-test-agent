# amdgpu fails to load on ppc64 systems

- **Issue #:** 599
- **State:** closed
- **Created:** 2018-11-02T21:24:11Z
- **Updated:** 2020-11-09T08:55:48Z
- **URL:** https://github.com/ROCm/ROCm/issues/599

On POWER9 systems with Vega installed, amdgpu from the ROCm kernel fails to load:

```
[  924.138049] [drm] amdgpu kernel modesetting enabled.
[  924.138882] [drm] amdgpu version: 18.30.2.15
[  924.139639] checking generic (600c280010000 300000) vs hw (6000000000000 10000000)
[  924.139911] [drm] initializing kernel modesetting (VEGA10 0x1002:0x6860 0x1002:0x6860 0x00).
[  924.141367] [drm] register mmio base: 0x00000000
[  924.142128] [drm] register mmio size: 524288
[  924.142828] [drm] PCI I/O BAR is not found.
[  924.143502] [drm] probing gen 2 caps for device 1022:1471 = 700d03/e
[  924.144529] [drm] probing mlw for device 1022:1471 = 700d03
[  924.145432] [drm] add ip block number 0 <soc15_common>
[  924.146273] [drm] add ip block number 1 <gmc_v9_0>
[  924.147053] [drm] add ip block number 2 <vega10_ih>
[  924.147847] [drm] add ip block number 3 <psp>
[  924.148547] [drm] add ip block number 4 <powerplay>
[  924.149335] [drm] add ip block number 5 <dm>
[  924.150040] [drm] add ip block number 6 <gfx_v9_0>
[  924.150811] [drm] add ip block number 7 <sdma_v4_0>
[  924.151599] [drm] add ip block number 8 <uvd_v7_0>
[  924.152378] [drm] add ip block number 9 <vce_v4_0>
[  924.155432] [drm] UVD(0) is enabled in VM mode
[  924.156161] [drm] UVD(0) ENC is enabled in VM mode
[  924.156940] [drm] VCE enabled in VM mode
[  924.157631] amdgpu 0000:03:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0x0000
[  924.159270] [drm:amdgpu_get_bios [amdgpu]] *ERROR* Unable to locate a BIOS ROM
[  924.160423] amdgpu 0000:03:00.0: Fatal error during GPU init
[  924.161357] [drm] amdgpu: finishing device.
[  924.162297] amdgpu: probe of 0000:03:00.0 failed with error -22
```