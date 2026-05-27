# what's the default .config for this kernel can't build

> **Issue #313**
> **状态**: closed
> **创建时间**: 2018-01-26T19:56:48Z
> **更新时间**: 2018-10-09T16:49:42Z
> **关闭时间**: 2018-10-09T16:49:42Z
> **作者**: Macribit
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/313

## 描述

I wasted half day trying to build this kernel it always throws some error usually in drivers/something/built-in.o
I've done the command make rock-rel_defconfig
It's just doesn't work please can someone help .


---

## 评论 (2 条)

### 评论 #1 — kentrussell (2018-09-14T12:39:57Z)

Have you tried copying the defconfig to kernel/.config and running make bindeb-pkg (or make binrpm-pkg for RPM)?

---

### 评论 #2 — jlgreathouse (2018-10-09T16:49:42Z)

Hi @Macribit 

I apologize about the long delay in getting back to you. In the time since you submitted this request, we've released some new versions of ROCm. Rather than requiring a ROCm-specific kernel, we now ship our required kernel support as [a DKMS module](https://linux.die.net/man/8/dkms). As such, you no longer need to compile an entire kernel just to use ROCm. In fact, [as of ROCm 1.9.0](https://github.com/RadeonOpenCompute/ROCm/blob/roc-1.9.0/README.md#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels), our user-land code will also work with upstream kernels (4.17+) so you may not even need to install our DKMS modules.

That said, if you would like to see and rebuild the kernel module, you can grab our rock-dkms package. On Ubuntu OSes, this will put the ROCm 1.9.1 kernel module source code into `/usr/src/amdgpu-1.9-224/` (the version numbers may change depending on the ROCm version). You can see the kernel config parameters used by default in `Makefile`. For instance, we set `CONFIG_DRM_AMDGPU_CIK=y` and `CONFIG_DRM_AMDGPU_SI=y` when building our module, even if your default kernel does not set these parameters.

If you would like to modify this module, this directory contains the source code. You can then rebuild and reinstall the module with the following commands:
```
sudo dkms remove amdgpu/1.9-224 --all
sudo dkms add amdgpu/1.9-224
sudo dkms build amdgpu/1.9-224
sudo dkms install amdgpu/1.9-224
```

Assuming none of these commands fail, the new module should load once you reboot.

---
