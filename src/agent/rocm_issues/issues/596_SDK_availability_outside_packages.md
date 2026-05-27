# SDK availability outside packages ?

> **Issue #596**
> **状态**: closed
> **创建时间**: 2018-10-31T18:59:53Z
> **更新时间**: 2018-11-06T17:43:26Z
> **关闭时间**: 2018-11-06T17:43:26Z
> **作者**: lissyx
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/596

## 描述

Reading the documentation, I could see that there is support for several distributions through their package managers, which is a **good** thing. However, it seems to me that what is covered at https://github.com/RadeonOpenCompute/ROCm#ubuntu-support---installing-from-a-debian-repository is only the installation of the whole software stack to run ROCm compatible tools.

Let's say I just want to have the needed bits to be able to make builds of TensorFlow that are ROCm-enabled. For NVIDIA's CUDA and CompteCpp's SDK, I just have to download and extract a tarball that contains the headers and sometimes some tooling required for building.

Thanks for any help!

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-10-31T20:01:47Z)

This is going to depend on the SDKs you want to build for. For OpenCL-backed builds, you should be able to use the `rocm-opencl-dev` package. For lower-level interactions with our ROCr runtime and the ROCt layer, you can get `hsa-rocr-dev` and `hsakmt-roct-dev`.

@pfultz2 @mangupta -- thoughts on this for HIP, and/or what minimum amount of stuff we would need to package up TensorFlow and HIP-using programs even if the user doesn't have an AMD GPU in their system (and thus they don't want to install ROCK, ROCr, ROCT, etc.)

---

### 评论 #2 — lissyx (2018-10-31T20:27:52Z)

> For OpenCL-backed builds, you should be able to use the `rocm-opencl-dev` package.

Thanks, I guess this is what I need. Though is it available in another form than a package ?

---

### 评论 #3 — jlgreathouse (2018-10-31T20:32:21Z)

Our OpenCL runtime is available at https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime

The current public build system doesn't create exactly the same thing as what we build and package internally. The following post may help you with that: https://github.com/RadeonOpenCompute/ROCm/issues/537#issuecomment-423311687

---
