# RX580 Call returned 4104

- **Issue #:** 783
- **State:** closed
- **Created:** 2019-04-30T03:14:12Z
- **Updated:** 2023-12-18T18:55:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/783

Two months ago, I purchased RX580 GPU, which was planned to be used for machine learning to speed up computing. But when I installed it, I encountered some problems. I just started to ask for help on GitHub and got good support. I said that my PCI model was not supported. Then I added the PCI model according to the tips on github. Later, rocm2.2 version had some problems, saying that it was incompatible with Linux kernel 4.18. But my computer is 4.15 core, or not, until the ROCM 2.3 version, found that the problem is still not solved, the current rocm-smi can display graphics card data, but rocminfo error, I have waited for a long time, tried various methods, also changed the Linux kernel several times during the docker has tried.

There's something wrong with the new version.

```
tu6ge@tu6ge-desktop:~$ rocminfo 
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.3/rocminfo/rocminfo.cc. Call returned 4104
```
my computer`s info :
```
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   13.360582] kfd kfd: Allocated 3969056 bytes on gart
[   13.361135] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ uname -a
Linux tu6ge-desktop 4.15.0-041500-generic #201802011154 SMP Thu Feb 1 11:55:45 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
tu6ge@tu6ge-desktop:~$ groups
tu6ge adm cdrom sudo dip video plugdev lpadmin sambashare
tu6ge@tu6ge-desktop:~$ uname -r
4.15.0-041500-generic
tu6ge@tu6ge-desktop:~$ dkms status
amdgpu, 2.3-14, 4.15.0-041500-generic, x86_64: installed
virtualbox, 5.2.18, 4.15.0-041500-generic, x86_64: installed
tu6ge@tu6ge-desktop:~$ modinfo amdgpu | grep filename
filename:       /lib/modules/4.15.0-041500-generic/updates/dkms/amdgpu.ko
tu6ge@tu6ge-desktop:~$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-041500-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   13.360582] kfd kfd: Allocated 3969056 bytes on gart
[   13.361135] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ dmesg | grep amd
[   11.055816] amdkcl: loading out-of-tree module taints kernel.
[   11.055833] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   11.615325] [drm] amdgpu kernel modesetting enabled.
[   11.615326] [drm] amdgpu version: 5.0.19.20.6
[   12.320874] fb: switching to amdgpudrmfb from EFI VGA
[   12.321506] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[   12.772981] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[   12.772983] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   12.773139] [drm] amdgpu: 8192M of VRAM memory ready
[   12.773141] [drm] amdgpu: 8192M of GTT memory ready.
[   13.362648] fbcon: amdgpudrmfb (fb0) is primary device
[   13.401764] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[   13.432512] [drm] Initialized amdgpu 3.31.0 20150101 for 0000:01:00.0 on minor 0
```
