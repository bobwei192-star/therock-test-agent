# Ethminer not runnning without sudo permissions.

> **Issue #301**
> **状态**: closed
> **创建时间**: 2018-01-17T03:16:07Z
> **更新时间**: 2018-06-03T15:33:09Z
> **关闭时间**: 2018-06-03T15:33:09Z
> **作者**: foogolator
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/301

## 描述

[OPENCL]:Using platform: AMD Accelerated Parallel Processing
[OPENCL]:Using device: gfx701(OpenCL 1.2 )
DAG  20:04:06.781|ethminer  DAG Generation Failure. Reason: Permission denied
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<dev::ExternalFunctionFailure>'
  what():  std::exception
Aborted (core dumped)

I am running ubuntu 16.04.3, with kernel 4.8.17. When ethminer tries to initialize the gpu, this output occurs, then the program aborts. So far not a great deal, as running ethminer as root with sudo works just fine.
Also great job with this new release of ROCm! Before I got 6mhs on 1.6, but now (At a glance while it runs), I seem to be getting a somewhat better hashrate than amdgpu-pro 17.40! 

---

## 评论 (3 条)

### 评论 #1 — foogolator (2018-01-21T03:13:52Z)

I was about to say that it is no longer doing this but I was absolutely retarded and jumped the gun; Issue is still persisting.

---

### 评论 #2 — briansp2020 (2018-01-21T05:28:51Z)

Did you put the user account into video group?

> sudo usermod -a -G video $LOGNAME 

It sounds like a permission issue. See the install instructions at https://github.com/RadeonOpenCompute/ROCm

---

### 评论 #3 — foogolator (2018-01-21T05:36:33Z)

@briansp2020 I've done everything in the install instruction, and I've placed myself into the video group.
Is it possible though that the video group isn't functioning properly? I had myself in the video group long before installing rocm, as I had myself in it back when I had to use amdgpu-pro drivers.

---
