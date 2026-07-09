# rx 580 Call returned 4104

- **Issue #:** 719
- **State:** closed
- **Created:** 2019-02-26T17:48:14Z
- **Updated:** 2019-05-01T22:15:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/719

help me , my problem is up
```
tu6ge@tu6ge-desktop:/opt/rocm/bin$ ./rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104
tu6ge@tu6ge-desktop:/opt/rocm/bin$ /opt/rocm/opencl/bin/x86_64/clinfo 
ERROR: clGetPlatformIDs(-1001)
```
my pc info:
```
tu6ge@tu6ge-desktop:~$ groups
tu6ge adm cdrom sudo dip video plugdev lpadmin sambashare
tu6ge@tu6ge-desktop:~$ uname -r
4.15.0-45-generic
tu6ge@tu6ge-desktop:~$ dkms status
amdgpu, 2.1-96, 4.15.0-45-generic, x86_64: installed
tu6ge@tu6ge-desktop:~$ modinfo amdgpu | grep filename
filename:       /lib/modules/4.15.0-45-generic/updates/dkms/amdgpu.ko
tu6ge@tu6ge-desktop:~$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-45-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[    1.130512] kfd kfd: DID 6fdf is missing in supported_devices
[    1.130513] kfd kfd: kgd2kfd_probe failed
tu6ge@tu6ge-desktop:~$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-45-generic (buildd@lgw01-amd64-031) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #48-Ubuntu SMP Tue Jan 29 16:28:13 UTC 2019 (Ubuntu 4.15.0-45.48-generic 4.15.18)
[    0.857513] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[    0.996854] amdkcl: loading out-of-tree module taints kernel.
[    0.996868] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    1.128409] [drm] amdgpu kernel modesetting enabled.
[    1.128410] [drm] amdgpu version: 19.10.7.418
[    1.129939] fb: switching to amdgpudrmfb from EFI VGA
[    1.130702] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.130773] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[    1.130774] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    1.130907] [drm] amdgpu: 8192M of VRAM memory ready
[    1.130907] [drm] amdgpu: 8192M of GTT memory ready.
[    1.365826] fbcon: amdgpudrmfb (fb0) is primary device
[    1.365900] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    1.391539] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:01:00.0 on minor 0
```
 My English is so poor ，sorry