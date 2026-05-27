# Plans for Arch Linux ?

> **Issue #1691**
> **状态**: closed
> **创建时间**: 2022-02-24T13:21:19Z
> **更新时间**: 2022-02-25T11:55:07Z
> **关闭时间**: 2022-02-25T11:55:07Z
> **作者**: EduMio
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1691

## 描述

There are any development plans for official support for the Arch Linux distribution? Right now there is a [package](https://github.com/rocm-arch/rocm-arch) in the [AUR](https://wiki.archlinux.org/title/Arch_User_Repository) for installing, but is not the same as the official support and requires building from source.

---

## 评论 (5 条)

### 评论 #1 — sofiageo (2022-02-24T13:26:54Z)

@EduMio 

I'm not sure if you know but until an official support is available, there is also package [opencl-amd](https://aur.archlinux.org/packages/opencl-amd) for OpenCL / HIP Runtimes and [opencl-amd-dev](https://aur.archlinux.org/packages/opencl-amd-dev) for ROCm SDK which is based on the Ubuntu releases. It's not exactly the same (probably missing some things) and it's unofficial. 

---

### 评论 #2 — EduMio (2022-02-24T14:18:50Z)

Well that is interesting indeed. Does it work with the 6900xt, pytorch and tensorflow? I just need the stack for machine leaning framework. 

> @EduMio
> 
> I'm not sure if you know but until an official support is available, there is also package [opencl-amd](https://aur.archlinux.org/packages/opencl-amd) for OpenCL / HIP Runtimes and [opencl-amd-dev](https://aur.archlinux.org/packages/opencl-amd-dev) for ROCm SDK which is based on the Ubuntu releases. It's not exactly the same (probably missing some things) and it's unofficial.



---

### 评论 #3 — sofiageo (2022-02-24T14:33:05Z)

It should work but I don't have a 6900XT to test it myself. I would try to use the docker [images](https://hub.docker.com/r/rocm/pytorch/tags) first if I were you.

You can also compile Pytorch yourself but it needs a lot of RAM to do so, 16GB is not enough (so I can't test that either). If you try it comment on the AUR package so we don't spam this issue tracker.

---

### 评论 #4 — EduMio (2022-02-24T15:03:19Z)

I see, I am going to try that in some near future, thank you

---

### 评论 #5 — ROCmSupport (2022-02-25T11:55:07Z)

Hi @EduMio 
Thanks for reaching out.
ROCm does not support ArchLinux officially and no current plans as of now.
Request to keep track of our documentation for the updates in future.
Thank you.

---
