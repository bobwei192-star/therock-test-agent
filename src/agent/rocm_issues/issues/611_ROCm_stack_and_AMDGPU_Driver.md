# ROCm stack and AMDGPU Driver

> **Issue #611**
> **状态**: closed
> **创建时间**: 2018-11-13T20:18:43Z
> **更新时间**: 2018-12-25T00:41:02Z
> **关闭时间**: 2018-12-25T00:41:02Z
> **作者**: iamkucuk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/611

## 描述

Hi. I would like to ask a question and possibly it's a stupid one. However, please excuse me since I am a linux and AMD newbie.

I am mainly switching to Linux for using my Vega 64 for deep learning frameworks. This requires the ROCm stack to be installed. Well, I play games too. Should I (or even can I) install AMDGPU drivers too? If not, are they at the same performance level?

Please have a nice day. 

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-11-13T21:15:28Z)

Could you describe what you mean by "AMDGPU drivers"? The open source Linux `amdgpu` driver is used as the basis of the ROCm software stack. However, the AMDGPU-PRO drivers that AMD releases (which include a `amdgpu` and some closed-source components). At the moment, I believe that the ROCm user-land code does not support the drivers included in AMDGPU-PRO, so you shouldn't use them together.

---

### 评论 #2 — boberfly (2018-11-14T21:43:20Z)

Hi @furkan-kucuk I've recently just been running the latest mesa stack atop of linux kernel 4.18.x amdgpu as well as ROCm's OpenCL is also still working in places that it did before on kernel 4.15.x + the ROCm DKMS driver combo. For games I am using RADV which is the Mesa Vulkan stack and Steam+Proton works perfect with Doom2016/GTA5. 

Cheers. This is Ubuntu 18.04 still but using an unsupported kernel from upstream via Ukuu.

---

### 评论 #3 — jlgreathouse (2018-12-25T00:41:02Z)

Indeed, as @boberfly mentions, if you're using an upstream 4.18, 4.19, or 4.20 kernel, you should be able to use the ROCm user-level software without needing to install the `rock-dkms` package. See [this part of our README](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#rocm-support-in-upstream-linux-kernels) for a comparison if upstream drivers vs. the `rock-dkms` package.

If you want to use the upstream drivers that are part of a new kernel, then [this section of our README](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#using-debian-based-rocm-with-upstream-kernel-drivers) explains how to install the ROCm user-level tools.

Note that you will still need to add your main users into the video group, as per [these directions](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#next-set-your-permissions).

You can read [these directions](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#rocm-binary-package-structure) to figure out which packages you want to install.

---
