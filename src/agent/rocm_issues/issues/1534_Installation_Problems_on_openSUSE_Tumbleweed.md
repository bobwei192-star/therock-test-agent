# Installation Problems on openSUSE Tumbleweed.

> **Issue #1534**
> **状态**: closed
> **创建时间**: 2021-07-25T17:34:19Z
> **更新时间**: 2021-07-27T07:20:16Z
> **关闭时间**: 2021-07-27T07:20:16Z
> **作者**: Photonico
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1534

## 描述

Hi,

My PC has AMD CPU(Ryzen 5900X) and an AMD graphic card(RX6800XT) (Of course, I'm a super AMD fan), so I want to use my GPU to do some scientific computation. The operating system is openSUSE Tumbleweed(20210726). I want the minimal installation of ROCm on my PC.

I add the repository resource via: `sudo zypper addrepo --no-gpgcheck http://repo.radeon.com/rocm/zyp/zypper/ rocm`
But I don't know which are the necessary packages for the ROCm.
And I find that:

Some packages can be installed directly.
`rock-dkms`
`rocm-gdb`: requires me to install python36 (My OS has python38 installed)
`rocminfo`
`rocm-opencl`
`rocm-opencl-devel`
`rocm-device-libs`
`hsakmt-roct`
`hipify-clang`
...

Some packages cannot be installed with dependencies problems.
`rocm-dkms` 
`rocm-dev`
`rccl`
`rocm-libs`
`hip-samples`
...

I'm new to computational science, could you tell me the minimal installation of ROCm environment requires me to install which packages from the [official repo](http://repo.radeon.com/rocm/zyp/zypper/)?
I just want to use [tensorflow-rocm](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream) and [CuPy-ROCm](https://pypi.org/project/cupy-rocm-4-0/).

I would appreciate it if you can respond to me.





---

## 评论 (3 条)

### 评论 #1 — leofang (2021-07-26T03:18:55Z)

Taking the discussion from cupy/cupy#5559 to here, as this is largely a ROCm issue instead of a CuPy issue. 

@Photonico reported that following the standard ROCm installation guide for SUSE-based distros would result in [`libffi` not found](https://github.com/cupy/cupy/issues/5559#issuecomment-886260644). Maybe @ROCmSupport could share insight on whether this is a known issue for openSUSE Tumbleweed?

cc: @amathews-amd (for vis)

---

### 评论 #2 — ROCmSupport (2021-07-27T07:16:11Z)

Hi @Photonico 
Thanks for reaching out.
Let me check this for you.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-07-27T07:20:16Z)

Hi @Photonico 
When I go through the description of the ticket, I came to know that you are using Suse Tumbleweed.

2 points I wish to highlight here.
ROCm supports the latest SLES SP2 and it does not support any other variants of OpenSUSE currently.
And also RX6800XT is not a supported card with ROCm right now.

Anyhow, I will try to help you as much as I can.
Installation steps you followed are not proper and so recommend to use the one @ [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#sles-15-service-pack-2](url)

Hope this solves your problem.
Thank you.


---
