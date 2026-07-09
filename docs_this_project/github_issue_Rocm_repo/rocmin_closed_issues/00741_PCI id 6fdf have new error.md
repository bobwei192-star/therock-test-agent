# PCI id 6fdf have new error

- **Issue #:** 741
- **State:** closed
- **Created:** 2019-03-17T03:31:48Z
- **Updated:** 2020-12-01T04:15:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/741

hello, Recently, when I was trying to install MIOPEN, I had some problems, so I reinstalled rocm. I found that both ROCM and libhsakmt had been upgraded. I set them up according to my PCI ID in the previous way, but I couldn't run rocm. 
my computer info:
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
[   13.814938] kfd kfd: Allocated 3969056 bytes on gart
[   13.815354] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-46-generic (buildd@lgw01-amd64-038) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #49-Ubuntu SMP Wed Feb 6 09:33:07 UTC 2019 (Ubuntu 4.15.0-46.49-generic 4.15.18)
[    0.629383] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[   12.868428] amdkcl: loading out-of-tree module taints kernel.
[   12.868449] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   13.338088] [drm] amdgpu kernel modesetting enabled.
[   13.338089] [drm] amdgpu version: 19.10.8.418
[   13.363289] fb: switching to amdgpudrmfb from EFI VGA
[   13.363799] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[   13.391983] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[   13.391985] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   13.392099] [drm] amdgpu: 8192M of VRAM memory ready
[   13.392100] [drm] amdgpu: 8192M of GTT memory ready.
[   13.817209] fbcon: amdgpudrmfb (fb0) is primary device
[   13.817277] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[   13.834552] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:01:00.0 on minor 0
```