# Q: how to build ROCm OpenCL for kernel 4.18

> **Issue #513**
> **状态**: closed
> **创建时间**: 2018-08-24T11:41:19Z
> **更新时间**: 2018-12-24T21:39:28Z
> **关闭时间**: 2018-12-24T21:39:28Z
> **作者**: preda
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/513

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I would like to try OpenCL on kernel 4.18 on Ubuntu 18.04. I have this plan:

1. checkout master branch of rock-dkms, compile and install.
2. install these pre-built packages:
Setting up hsa-ext-rocr-dev (1.1.8-15-ge851b7a) ...
Setting up hsakmt-roct (1.0.8-1-ge3dd067) ...
Setting up hsakmt-roct-dev (1.0.8-1-ge3dd067) ...
Setting up hsa-rocr-dev (1.1.8-15-ge851b7a) ...
Setting up rocm-opencl (1.2.0-2018071109) ...

Would it work? what do I need to do differently?
thanks

---

## 评论 (9 条)

### 评论 #1 — gstoner (2018-08-24T13:38:41Z)

There are changes in the Thunk layer to simplify swapping upstream kernel driver,  It not that far our for 1.9 to release weeks, I would wait for this update 

---

### 评论 #2 — evgeniyosipov (2018-08-24T14:29:45Z)

**gstoner**
It's will be brilliant, thank you.

---

### 评论 #3 — Moading (2018-08-24T18:08:29Z)

@gstoner 
will 1.9 include opencl device side enqueue? For clarification, when can we expect the release of 1.9?

---

### 评论 #4 — cryptomilk (2018-08-28T09:55:59Z)

I have ROCm OpenCL working with Linux Kernel 4.18 on openSUSE Tumbleweed, I've just installed the RHEL7 RPMs.

```
hsa-rocr-dev-1.1.8-15-ge851b7a-Linux.rpm
hsakmt-roct-1.0.8-1-ge3dd067-Linux.rpm
rocm-opencl-1.2.0-2018071635.x86_64.rpm
rocm-opencl-devel-1.2.0-2018071635.x86_64.rpm
```

---

### 评论 #5 — rkothako (2018-08-31T04:01:00Z)

Hi @Moading 
As per the current information, Device enqueue will be part of ROCm2.0

---

### 评论 #6 — cryptomilk (2018-08-31T05:30:59Z)

Sorry, I was wrong, it doesn't work with Kernel 4.18 and the RHEL RPMs :-(

---

### 评论 #7 — jlgreathouse (2018-09-15T22:14:37Z)

Hi @preda 

With the release of ROCm 1.9 yesterday, you may be able to do what you want. It looks like a user over at Phoronix [has ROCm working under a custom 4.18 kernel](https://www.phoronix.com/forums/forum/phoronix/latest-phoronix-articles/1047471-amd-rocm-1-9-available-with-vega-20-support-plus-upstream-kernel-compatibility/page2). This user shows directions as well.

---

### 评论 #8 — shimmervoid (2018-09-15T23:38:06Z)

The information provided here is invaluable. I can confirm this works. Thanks @jlgreathouse & perpetually high from phoronix 

---

### 评论 #9 — jlgreathouse (2018-12-24T21:39:28Z)

Hi @preda 

If you're interested, I have updated the ROCm [README](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md), [website](https://rocm.github.io/ROCmInstall.html), and [documentation](https://rocm-documentation.readthedocs.io/en/latest/Installation_Guide/Installation-Guide.html) to better address your questions.

In particular:

- [This section](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#rocm-support-in-upstream-linux-kernels) should better explain the tradeoffs between using the upstream kernel driver and the `rock-dkms` driver module supplied as part of the ROCm repository.
- [This section](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#rocm-binary-package-structure) should explain the binary packages, what software they provide, and their dependencies.
- [This section](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#performing-an-opencl-only-installation-of-rocm) describes how to install only ROCm OpenCL and its required dependencies along with the kernel driver.
- [This section](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#using-debian-based-rocm-with-upstream-kernel-drivers) describes how to install the ROCm user-space software on Ubuntu when you want to use an upstream driver.

Note that I don't explicitly have a section that describes installing just ROCm OpenCL without the kernel driver, but the above information should hopefully allow you to understand how this all fits together and install just the packages you need for that.

I would like to avoid trying to document how to install every permutation of all software offered by ROCm, to prevent our README file from becoming a novel.

In addition, if you are interested in compiling any of your own ROCm software, please feel free to see our [Experimental ROC](https://github.com/RadeonOpenCompute/Experimental_ROC) project, which includes tools and scripts that show how to build all of the ROCm packages from source.

---
