# Is the RX 590 compatible with WSL2?

> **Issue #1249**
> **状态**: closed
> **创建时间**: 2020-09-29T09:19:37Z
> **更新时间**: 2025-04-12T20:18:15Z
> **关闭时间**: 2020-12-03T12:18:45Z
> **作者**: plasticbit
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1249

## 描述

```
Environment:
Windows 10 Home (Version 2004)
Sapphire RX 590 (Driver 20.9.1)
Ryzen 5 2600

WSL2 Ubuntu 20.04 (kernel: 5.4.51-microsoft-standard-WSL2+)
````

I followed [this link](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu) to install it, but I get an error.

```
$ /opt/rocm/bin/rocminfo
ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
Failed to get user name to check for video group membership
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

~~clinfo doesn't seem to be a problem.~~
No error in clinfo, but it does not seem to recognize the GPU.
```
$ /opt/rocm/opencl/bin/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3186.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               0
```

---

## 评论 (4 条)

### 评论 #1 — Grench6 (2020-10-31T16:39:10Z)

> Is the RX 590 compatible with WSL2?
### In theory: yes. Actually: no.

I assume you already know you need to have the WSL2 features that by the time of writing are only available in the windows insiders build (just to be able to _hypothetically_ use rocm on windows) and that it is still experimental.

But here is the real problem:

> Sapphire RX 590 (Driver 20.9.1)

There are lots of guys having issues with these graphics card (including me, I have a RX580). Our graphics doesn't work, but we are using pure Linux!. **As long as these graphic cards are not working on Linux, they wont work on WSL either!.** They are supposed to be supported on pure Linux (its written everywhere) but well... this problem seems recent so nobody knows why it is not working, not yet.

I will include a few issues so you can track the progress on this topic:
#1269  #1265

---

### 评论 #2 — plasticbit (2020-11-02T13:08:54Z)

I see, that's what you mean.
Grench6, thank you for your comment. I will refer to it.

---

### 评论 #3 — ROCmSupport (2020-12-03T12:17:58Z)

Hi @BinaryDolphin29 
Hope you got reasonable answers.
Thank you.

---

### 评论 #4 — vitaliibudnyi (2025-04-12T20:18:14Z)

Are the stars aligned yet?

Looks like ROCm and WSL2 are now friends. And there are successful cases of making ROCm 6.3 work with regular Linux (Ubuntu-24.04) on RX570/580/590, even in multi-GPU setups.

If you combine 570, 580 and their variations (GME, 2048SP etc), that's a lot of GPUs people own right now. At least several % on steam, which is significant. Including those dirt cheap used ones on sale everywhere, you know, the crypto survivors.

---
