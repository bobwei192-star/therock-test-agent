# Mistakes in the installation instructions and unecasarly complex

> **Issue #1127**
> **状态**: closed
> **创建时间**: 2020-06-04T13:49:04Z
> **更新时间**: 2021-02-16T12:46:29Z
> **关闭时间**: 2021-02-16T06:13:40Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1127

## 描述

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#using-debian-based-rocm-with-upstream-kernel-drivers

missing pipe, should be:

```
echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules
```

No need for line breaks.

Even better, please do put this into a separate `deb` package, called `rocm-udev:all`, and make it be a dependency of `hsakmt-roct`, and remove it from the `rocm-dkms`, and make also `rocm-dkms` depend on `rocm-udev:all`. This is so easy to do.

I tried this year ago, and had the same issues, and installation of rocm is constantly a pain, but all of this can be fixed so easily!



This section also fails to mention that one probably need to restart the system to fully use. It.

On my Debian testing system, by default /dev/kfd has a group `renderer` (gid 107), but a default user is not in that group. So maybe instead use GROUP="renderer" in the udev rule as it is, and simply ask the user to add them to renderer group instead? (`sudo usermod -a -G renderer $LOGNAME`), not sure about that tho.

Similarly, sections 4, 5, 6 about settings up groups, are just adding complexity. Most of the time the normal user is already in the `video` group. Also setting up groups is not part of installation, it is part of seting it up for use by the user. This should be separate section, and not repeated over and over again in every section and for every distro. The installation guide page is already 5 times too long in my opinion.



---

## 评论 (4 条)

### 评论 #1 — Rmalavally (2020-06-04T13:51:32Z)

Thank you for your feedback. We will review the installation instructions with the team and make the changes as applicable. 

---

### 评论 #2 — ROCmSupport (2021-02-16T06:13:40Z)

Thanks @baryluk for your point on missing pipe and similar mistakes.
This has been corrected.
Thank you.

---

### 评论 #3 — baryluk (2021-02-16T09:16:43Z)

What about creating a separate package with udev rules, so it is easy to install it out of the box, with no extra steps? Just move the `kfd.rules` file from `rocm-dkms` and into new package, like `rocm-udev:all` and make it a dependency of proper packages.

---

### 评论 #4 — ROCmSupport (2021-02-16T12:46:29Z)

Hi @baryluk 
I checked with team and its not required/priority to do for now.

---
