# Cannt install. (Ubuntu 16/04. Radeon rx 570)

- **Issue #:** 521
- **State:** closed
- **Created:** 2018-09-04T21:55:14Z
- **Updated:** 2018-09-17T23:26:48Z
- **URL:** https://github.com/ROCm/ROCm/issues/521

rx 570
Athlon 950
Asus Prime b350

Ubuntu 16.04


>  hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

>  dmesg | grep kfd
> [    1.354785] kfd kfd: Initialized module
> [    1.355604] kfd kfd: skipped device 1002:67df, PCI rejects atomics

pew

>  dmesg | grep kfd
> [    1.354785] kfd kfd: Initialized module
> [    1.355604] kfd kfd: skipped device 1002:67df, PCI rejects atomics
> root@wateros:~# dmesg | grep amdgpu
> [    1.348650] [drm] amdgpu kernel modesetting enabled.
> [    1.355060] fb: switching to amdgpudrmfb from VESA VGA
> [    1.355594] [drm] add ip block number 3 <amdgpu_powerplay>
> [    1.355977] amdgpu 0000:07:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
> [    1.356122] amdgpu 0000:07:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
> [    1.356124] amdgpu 0000:07:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
> [    1.356245] [drm] amdgpu: 4096M of VRAM memory ready
> [    1.356247] [drm] amdgpu: 7976M of GTT memory ready.
> [    2.112365] fbcon: amdgpudrmfb (fb0) is primary device
> [    2.112447] amdgpu 0000:07:00.0: fb0: amdgpudrmfb frame buffer device
> [    2.295722] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:07:00.0 on minor 0
