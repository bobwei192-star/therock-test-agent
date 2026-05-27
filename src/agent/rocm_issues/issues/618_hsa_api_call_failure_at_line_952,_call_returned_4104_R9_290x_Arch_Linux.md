# hsa api call failure at line 952, call returned 4104 R9 290x Arch Linux

> **Issue #618**
> **状态**: closed
> **创建时间**: 2018-11-19T08:14:53Z
> **更新时间**: 2018-12-02T02:45:53Z
> **关闭时间**: 2018-11-25T15:26:00Z
> **作者**: maxcr
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/618

## 描述

secret sauce

---

## 评论 (9 条)

### 评论 #1 — jlgreathouse (2018-11-19T16:45:44Z)

Is your user in the `video` group? The strace appears to show that you do not have access to `/dev/kfd/`

---

### 评论 #2 — maxcr (2018-11-19T23:51:41Z)

Yessir I am.

`video:x:986:maxr`

---

### 评论 #3 — maxcr (2018-11-20T11:54:22Z)

I fixed it. Looks like arch will have a working ROCm stack after all. lov u @jlgreathouse 

---

### 评论 #4 — maxcr (2018-11-20T11:57:03Z)

Yo if I get these packages working and accepted into AUR, and then update your ReadTheDocs page with the Arch install process can I get a namedrop somewhere in there? It'll look good on the resume you know?

And well all your docs actually. They're all extremely outdated.

---

### 评论 #5 — maxcr (2018-11-20T12:09:31Z)

Also if/when you read this @jlgreathouse you mind just deleting the issue entirely? I don't want somebody stealing my secret sauce and uploading the packages to AUR before I do.

---

### 评论 #6 — maxcr (2018-11-20T12:56:22Z)

How do I get the rocr package to build these two files. I found them at https://github.com/HSAFoundation/HSA-Runtime-AMD, but apparently this repo is hosting super old versions whereas the thunk/rocr package builds the new ones except it doesn't spit out the `libhsa-ext-image` and `libhsa-ext-finalize` libraries needed.

```
26 Nov 20 05:45 libhsa-ext-finalize64.so -> libhsa-ext-finalize64.so.1
12M Nov 20 05:45 libhsa-ext-finalize64.so.1
23 Nov 20 05:45 libhsa-ext-image64.so -> libhsa-ext-image64.so.1
1.1M Nov 20 05:45 libhsa-ext-image64.so.1
```

Is this the same binary/release vs source build problem @sjug was having?

---

### 评论 #7 — jlgreathouse (2018-11-27T05:51:25Z)

Hi @maxcr 

If you get some build directions together (and get things into AUR), I would definitely be interested in seeing them and giving credit where credit is due.

I actually have a plan (once I return from holiday vacation) to release scripts for installing ROCm on various distros, both from packages and from source. The packages for Ubuntu and CentOS/RHEL are already available, and I'm almost done with the scripts to build from source on those distros. If you have similar directions from Arch, I can add them to that script repo once it's available.

We are aware that various pieces of documentation are out of date. I've tried to keep the installation directions and hardware requirements pages up-to-date. I, personally, don't have the time to own every piece of documentation, however. Your concern is noted.

As for the two files you're looking for with ROCr: those are closed-source components at this time and are thus only available in our binary .deb/.rpm packages. However, the ROCm stack can (mostly) function without them. The HSAIL finalizer has been deprecated and is no longer shipped as part of ROCm, while the HSA image extensions are primarily used for OpenCL images. Without that library available, images types will be disabled in our OpenCL runtime but everything else will continue to function.

---

### 评论 #8 — maxcr (2018-11-28T17:43:43Z)

I've got a PKGBUILD for the THUNK portion of the package. I'll have the ROCR portion working in a few hours and then eventually all the packages.

---

### 评论 #9 — sjug (2018-12-02T02:45:52Z)

The AUR already has packages for all the components, they just need to have
some tweaking.

On Wed, Nov 28, 2018 at 5:43 PM Max Robbins <notifications@github.com>
wrote:

> I've got a PKGBUILD for the thunk portion of the package. I'll have the
> ROCR portion working in a few hours and then eventually all the packages.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/618#issuecomment-442538829>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AHM2sRiW9cTTZvp0Vdp7k60NpGxg1wvOks5uzstUgaJpZM4YomV1>
> .
>


---
