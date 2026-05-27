# RX580 question

> **Issue #739**
> **状态**: closed
> **创建时间**: 2019-03-15T18:06:16Z
> **更新时间**: 2019-03-16T02:03:56Z
> **关闭时间**: 2019-03-16T02:03:56Z
> **作者**: tu6ge
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/739

## 描述

```
tu6ge@tu6ge-desktop:~$ rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104
```
my pc info:
```
tu6ge@tu6ge-desktop:~$ groups
tu6ge adm cdrom sudo dip video plugdev lpadmin sambashare
tu6ge@tu6ge-desktop:~$ uname -r
4.15.0-46-generic
tu6ge@tu6ge-desktop:~$ dkms status
amdgpu, 2.2-31, 4.15.0-46-generic, x86_64: installed
tu6ge@tu6ge-desktop:~$ modinfo amdgpu | grep filename
filename:       /lib/modules/4.15.0-46-generic/updates/dkms/amdgpu.ko
tu6ge@tu6ge-desktop:~$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-46-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   14.283967] kfd kfd: Allocated 3969056 bytes on gart
[   14.284558] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-46-generic (buildd@lgw01-amd64-038) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #49-Ubuntu SMP Wed Feb 6 09:33:07 UTC 2019 (Ubuntu 4.15.0-46.49-generic 4.15.18)
[    0.625927] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[   12.132712] amdkcl: loading out-of-tree module taints kernel.
[   12.132743] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   12.999277] [drm] amdgpu kernel modesetting enabled.
[   12.999278] [drm] amdgpu version: 19.10.8.418
[   13.262912] fb: switching to amdgpudrmfb from EFI VGA
[   13.263470] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[   13.382403] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[   13.382405] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   13.382602] [drm] amdgpu: 8192M of VRAM memory ready
[   13.382603] [drm] amdgpu: 8192M of GTT memory ready.
[   14.286409] fbcon: amdgpudrmfb (fb0) is primary device
[   14.286474] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[   14.310745] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:01:00.0 on minor 0
```
help me ,thanks
