# ROCm with upstream kernel drivers?

> **Issue #1816**
> **状态**: closed
> **创建时间**: 2022-09-29T20:57:54Z
> **更新时间**: 2023-02-24T21:54:26Z
> **关闭时间**: 2023-02-24T21:54:26Z
> **作者**: sarunasb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1816

## 描述

Hi,

Is using ROCm with upstream kernel `amdgpu` still possible, like it used to be:

([ROCm with Upstream Kernel Drivers](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#using-debian-based-rocm-with-upstream-kernel-drivers))

If yes, how does one do that?

Thank you!


---

## 评论 (3 条)

### 评论 #1 — xuhuisheng (2022-09-29T23:54:21Z)

Yes, we can use upstream amdgpu module with rocm-dev and rocm-libs. so we don't have to install amdgpu-dkms manually.

The upstream amdgpu installed with linux kernel is an old version of amdgpu-dkms. So It is not properly if you want to play some new features with ROCm.

e.g. If you want to run RDNA cards without PCIe-atomic requirement, you need amdgpu-dkms, since upstream firmware too old to support this.

On the otherway, the new version of amdgpu-dkms may add new bugs.
e.g. gfx803 card cannot run with latest amdgpu-dkms-22.20. I have to fallback to upstream driver from ubuntu-20.04, right now.

---

### 评论 #2 — sarunasb (2022-10-03T18:46:48Z)

Thank you, @xuhuisheng, yes instructions from version 4.x for use with upstream kernel's `amdgpu` module still seem to work, though there is no mention of it in documentation for [5.x](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#installation-methods).

---

### 评论 #3 — kentrussell (2023-02-24T21:54:26Z)

You can use "--nodkms" as a flag for amdgpu-install to not install the kernel DKMS package, thus using the upstream kernel but using the rest of the ROCm stack, as specified in the usecase=* flag . 

---
