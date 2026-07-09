# Driver loaded but still getting error 4104

- **Issue #:** 693
- **State:** closed
- **Created:** 2019-01-30T15:09:10Z
- **Updated:** 2019-02-06T00:19:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/693

Hi, I'm trying to get the ROCm stack working on the following system:

- Distribution: Arch Linux
- Kernel: 4.20.3-arch1-1-ARCH (distro package)
- GPU: Vega 10 XL/XT [Radeon RX Vega 56/64] (rev c1)
- CPU: Intel(R) Core(TM) i7-4960X CPU @ 3.60GHz
- Motherboard: Gigabyte X79S-UP5

I understand that `amdkfd` was merged into `amdgpu` in 4.20, which is why it's not in `lsmod`:

```console
$ lsmod | grep amd
amdgpu               3756032  39
chash                  16384  1 amdgpu
amd_iommu_v2           20480  1 amdgpu
gpu_sched              36864  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   110592  1 amdgpu
drm_kms_helper        208896  1 amdgpu
drm                   499712  10 gpu_sched,drm_kms_helper,amdgpu,ttm
```

The CPU/MB are pretty old, but the driver isn't complaining in dmesg, so looks like this combination (Ivy Bridge-E) should be supported?

```console
$ dmesg | grep -i kfd
[   10.381974] kfd kfd: Allocated 3969056 bytes on gart
[   10.382148] kfd kfd: added device 1002:687f
```

However, I'm still getting `hsa api call failure at line 900` / `Call returned 4104` from the `rocminfo` binary. strace shows:

```
ioctl(3, _IOC(_IOC_READ|_IOC_WRITE, 0x4b, 0x19, 0x10), 0x7ffcd47c7f10) = -1 EINVAL (Invalid argument)
ioctl(3, AMDKFD_IOC_GET_PROCESS_APERTURES, 0x7ffcd47c7f20) = 0
ioctl(3, _IOC(_IOC_WRITE, 0x4b, 0x21, 0x8), 0x7ffcd47c80b0) = -1 EINVAL (Invalid argument)
```

Any advice or pointers towards further narrowing this down would be appreciated. Thanks!