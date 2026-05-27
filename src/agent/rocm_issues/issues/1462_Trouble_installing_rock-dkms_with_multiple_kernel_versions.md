# Trouble installing rock-dkms with multiple kernel versions

> **Issue #1462**
> **状态**: closed
> **创建时间**: 2021-04-26T08:50:00Z
> **更新时间**: 2021-05-10T22:59:07Z
> **关闭时间**: 2021-04-26T09:19:15Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1462

## 描述

On Linux 20.04 I have two Linux kernels installed, 5.4.0 and 5.12.0. Using Radeon VII.
When I attempt to install rock-dkms (the requirement to use rock-dkms being a regression in ROCm 4.1.x, as previous versions of ROCm did work with upstream amdgpu thus no requiring dkms),
amdgpu-dkms compiles correctly for 5.4.0, but fails for 5.12.0 (normal), but the error on 5.12.0 leaves amdgpu-dkms not-working on either kernel (thus including not working on 5.4.0, where it did compile successfully).

The workaround for me was to uninstall kernel 5.12.0, at which point the rock-dkms completed successfully.


---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-04-26T09:19:15Z)

Thanks @preda for reaching out.
As there is a non-supported kernel in your machine, kernel modules will be failed to compile.
Way is to disable compiling for non-supported kernels [or] remove specific unsupported kernels before compilation of kernel code.
Thank you.

---

### 评论 #2 — preda (2021-04-26T09:43:23Z)

Is there a way to disable compiling for non-supported kernels?

Is the only "solution" to remove all non-supported kernels -- otherwise the system is left without a working GPU driver on the next boot, not great right? but not a problem?

Where is documented the requirement that "non-suported kernels" must be removed before installing dkms?


---

### 评论 #3 — ROCmSupport (2021-04-26T11:20:42Z)

I got further clarity on kernel part. Sorry for my previous comment.

Normally dkms only installs on the booted kernel. You can manually tell it to install on all kernels, but that's not the normal workflow. Installing the rock-dkms package via apt/yum/dpkg/rpm will just install it on the booted kernel, and ignore all others. That's why we do not tell to remove non supported kernels before installing. The standard workflow only installs it on the booted kernel.
Hope it helps.

---

### 评论 #4 — kentrussell (2021-04-26T12:36:32Z)

Just for a bit of clarity, here are some options that you can do:
1) Boot into the supported kernel to install rock-dkms (rock-dkms installation should only install on the booted kernel by default)
2) Use "dkms" to force installation/removal from various kernels (dkms remove amdgpu/$amdgpuver -k $kernelver; dkms install amdgpu/$amdgpuver -k $kernelver)

Just make sure that if you do a "dkms remove" that you update your ramfs image after (update-initramfs -u or dracut --regenerate-all) to ensure that the rock-dkms version of amdgpu is removed from the ramfs image(s)

---

### 评论 #5 — preda (2021-04-26T14:27:00Z)

@kentrussell thank you for the explanation (on how to use dkms).

Interesting, in my case I did "sudo apt install rock-dkms", and while it did compile *first* on the booted kernel (5.4, which succeeded), it continued to compile on the other kernels that I have installed (such as 5.12, 5.11, 5.10) and it failed on the first of those. I suspect that the needed update-initramfs did not happen anymore afterwards because of the compilation error.


---

### 评论 #6 — cloudishBenne (2021-05-10T22:59:06Z)

@preda this is the behaviour i also observed. i am now searching the www for about 4 hours. the only solution i found so far is: https://github.com/RadeonOpenCompute/ROCm/issues/1311#issuecomment-741904198
but i don't understand if this is a real solution until rocm gets support for newer kernels and don't will break apt.

---
