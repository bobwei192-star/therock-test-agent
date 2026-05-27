# Clarify text wrt closed-source: "These components are only available through the ROCm repositories"

> **Issue #267**
> **状态**: closed
> **创建时间**: 2017-12-05T11:43:35Z
> **更新时间**: 2018-09-17T21:10:55Z
> **关闭时间**: 2018-09-17T21:10:55Z
> **作者**: alexanderkjeldaas
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/267

## 描述

The README states:

```
These components are only available through the ROCm repositories, 
and will either be deprecated or become open source components in 
the future. These components are made available in the following packages:
      hsa-ext-rocr-dev
```

could you please clarify?  If closed-source components are available through repos, are we talking about binaries in the github repositories, or are we talking about deb repositories? 

Also, is this required?

The reason for asking is that I'd like to generally know how to build ROCm on NixOS.  We can build from source, or we can unpack the debian archives.  Also, specifically knowing how this relates to the 4.15rc2 kernel (which is the latest as of today) would be good.

A general update wrt the 4.15 kernel would be good.

---

## 评论 (5 条)

### 评论 #1 — alexanderkjeldaas (2017-12-05T11:44:38Z)

Related #257 

---

### 评论 #2 — gstoner (2017-12-05T13:39:46Z)

The DC component will help ROCm have a better experience when we have Head aka display this fixes a lot of the issues earlier uses had when enabling X11 and OpenGL with a number of displays.  We removed all the closed source components from core ROCm stack,  Major piece was the old HSAIL SC compiler path this has been replaced the native LLVM compiler backend. 

---

### 评论 #3 — alexanderkjeldaas (2017-12-05T21:34:50Z)

In #256, you said that the next kernel will be based on 4.13 which doesn't have those 4.15 changes.  So I'm interpreting this as:

- ROCm 1.7 uses ROCK which is linux 4.13
- The closed source components will exist until some 1.8 or later ROCm release

is that correct?

---

### 评论 #4 — jlgreathouse (2018-09-17T21:08:58Z)

Hi @alexanderkjeldaas 

These closed source components are available as binaries in the .deb and .rpm packages on repo.radeon.com. As of ROCm 1.9, the remaining mechanisms that are available in these closed-source libraries are the `hsa_amd_image_*`, `hsa_ext_image_*` and `hsa_ext_sampler_*` functions (`libhsa-ext-image64.so.1`) and `hsa_ext_tools_*` functions (`libhsa-runtime-tools64.so`).

The former are used by, for example, our OpenCL runtime for "image" types. If you don't have `libhsa-ext-image64.so.1` installed on your system, our OpenCL runtime will not offer image support for ROCm GPU devices. For example, [clGetDeviceInfo()](https://www.khronos.org/registry/OpenCL/sdk/2.1/docs/man/xhtml/clGetDeviceInfo.html) will return `CL_FALSE` for `CL_DEVICE_IMAGE_SUPPORT`.

The HSA tools extension library is used by our older [ROCm debugger](https://github.com/RadeonOpenCompute/ROCm-Debugger) and I believe by [GPUPerfAPI ](https://github.com/GPUOpen-Tools/GPA) for debugging and profiling, respectively. I'm not sure if the old debugger works (we are in the process of replacing it for a future revision). Our low-level [rocProfiler](https://github.com/ROCmSoftwarePlatform/rocprofiler) does not need the closed-source profiling extension, but we are currently in the process of converting GPA to use this new open source low-level mechanism.

As such, you can likely choose to not include these closed-source libraries. But you may lose some runtime and/or profiling functionality if you do not include them.

To note, we recently removed the closed-source HSAIL finalizer extension in our ROCm 1.9.0 release. As @gstoner mentioned, all of our ROCm components now directly use LLVM IR instead of going through the HSAIL intermediate language.

If you do want to include these closed source libraries, I believe you will need to unpack an archive to extract them. We don't provide them in a GitHub repo (since they're just closed-source binaries).

---

### 评论 #5 — jlgreathouse (2018-09-17T21:10:55Z)

With respect to kernel release info:

As of ROCm 1.9.0, the ROCm distribution that we make available is compatible with kernel 4.15.0-34 on Ubuntu (which is what is available right now). In addition, you can choose to skip installing the ROCK kernel drivers if you are using the upstream Linux 4.17+. If you are using one of these newer kernels, you can choose to simply install the user-land components such as ROCR and ROCT, and it should work with the upstream drivers.

Note that our ROCm-supplied drivers may offer more features and newer hardware support than the upstream drivers.

Sorry for taking so long to answer your questions, but I hope this helps!

---
