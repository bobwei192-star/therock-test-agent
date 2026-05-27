# `rocminfo` deb package has wrong (or no) dependencies

> **Issue #1129**
> **状态**: closed
> **创建时间**: 2020-06-04T14:04:59Z
> **更新时间**: 2024-08-14T15:26:33Z
> **关闭时间**: 2024-08-14T15:26:33Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1129

## 描述

```
$ apt show rocminfo
Package: rocminfo
Version: 1.30500.0
Priority: optional
Section: devel
Maintainer: Advanced Micro Devices Inc.
Installed-Size: 76.8 kB
Download-Size: 25.1 kB
APT-Manual-Installed: no
APT-Sources: http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime rocminfo tool
```

this is simply wrong.

You are missing dependency on `libstdc++6:amd64` and `hsa-rocr-dev`. It is also very unfortunate that the `/opt/rocm-3.5.0/lib/libhsa-runtime64.so.1` is in `hsa-rocr-dev` and not in the `libhsa1` with headers (and any potential static libraries in the future) in `libhsa-dev`.



---

## 评论 (19 条)

### 评论 #1 — ye-luo (2020-06-23T18:39:41Z)

Also found it very broken.
```
$ rocminfo
rocminfo: error while loading shared libraries: libhsakmt.so.1: cannot open shared object file: No such file or directory
```
I cannot find  libhsakmt.so.1 under /opt/rocm
but hsakmt-roct is shown installed.
After forcing a reinstall, the problem goes away.
```
sudo apt reinstall hsakmt-roct
```


---

### 评论 #2 — baryluk (2020-09-22T19:57:17Z)

Still broken in 3.8.0, just like it was also broken in 3.7.0 and 3.5.0.


---

### 评论 #3 — ROCmSupport (2021-02-15T14:48:58Z)

Thanks @baryluk for reaching out.
I will take a look and update soon on this.
Thank you.

---

### 评论 #4 — bugparty (2021-03-29T08:10:19Z)

I tried in rocm4.1, `sudo apt reinstall hsakmt-roct` works

---

### 评论 #5 — baryluk (2021-03-29T09:56:43Z)

Still broken in rocm 4.1, same way as before.


---

### 评论 #6 — ROCmSupport (2021-06-03T09:23:25Z)

Update:
Assigned to dev and he is looking into it.
I will keep you posted.
Thank you.

---

### 评论 #7 — ROCmSupport (2021-07-08T16:09:18Z)

Fix is ready and changes are pushed to internal code and fix is available most likely in 4.3 or less likely in 4.4 code.
Thank you.

---

### 评论 #8 — baryluk (2021-08-08T12:51:36Z)

Still broken in rocm 4.3. Hopefully it got fixed in 4.4.

Unfortunately in 4.3, doing `apt reinstall hsakmt-roct` is not enough, even after calling `ldconfig` later. `libhsa-runtime64.so.1` is still missing, and incorrectly put in `hsa-rocr-dev` package, instead of something like `libhsa1`



---

### 评论 #9 — keryell (2022-04-05T20:53:42Z)

@baryluk I guess if it is not already fixed yet you can send a PR. It might be more efficient than opening an issue... :-/

---

### 评论 #10 — nartmada (2023-12-14T04:10:02Z)

Hi @baryluk, please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #11 — baryluk (2023-12-17T03:04:07Z)

@nartmada Unfortunately ROCm 5.7.1 cannot be installed (the instructions to install ROCm 5.7.1 mention unversioned ROCm repo, so it actually tries to install 6.0.0), plus it breaks anyway, as it is referencing some old Python versions.

I cannot install ROCm 6.0.0 either, because install instructions are broken, and apt is getting 404 from web servers hosting repos when following install instructions.


---

### 评论 #12 — nartmada (2023-12-18T17:36:42Z)

Hi @baryluk, thanks for getting back.  Let me talk to the internal team for next steps on this ticket.  

---

### 评论 #13 — nartmada (2023-12-21T19:14:24Z)

Hi @baryluk, thank you for your patience.  Can you please try updating the Ubuntu version and try installing ROCm 6.0 again?  Please include info on any installation error encountered.  Thanks.

---

### 评论 #14 — nartmada (2024-01-19T04:55:24Z)

Hi @baryluk, can you please provide the CPU, GPU, and Operating System info?  We will try to repro your issue here at AMD using ROCm 5.7.1.  Thanks.

---

### 评论 #15 — nartmada (2024-02-06T20:33:13Z)

Hi @baryluk, can you please try ROCm 6.0.2?  An internal developer has looked over the rocminfo package for 6.0.2 and the dependency appear to be correct. Thanks.

---

### 评论 #16 — baryluk (2024-02-08T21:03:25Z)

Let me try


---

### 评论 #17 — baryluk (2024-02-08T21:25:34Z)

So, now it is:

`Depends: hsa-rocr, kmod, pciutils, rocm-core`

It is now way better than what it was originally (initially it was empty). It does technically work.

Still, technically stdc++ is not properly mentioned.

Nor is hsa-rocr has any version constraints.

Here are deps graph for the main binary:

![image](https://github.com/ROCm/ROCm/assets/110322/a2daab33-707e-4999-8e09-26f378131944)

Also it missed dependency on `python3`, used by another script in `rocminfo` package.

Adding something like this:

`libgcc-s1 (>= 3.0), libstdc++6 (>= 11), python3`

and possibly also `libc6 (>= 2.34)`

should help, but of course exact libc6 and stdc++6 version depends on a build environment.



---

### 评论 #18 — nartmada (2024-02-08T21:28:10Z)

Thank you @baryluk.  I will pass your feedback to internal team.

---

### 评论 #19 — ppanchad-amd (2024-08-14T15:26:33Z)

@baryluk This is fixed in the latest ROCm 6.2. Thanks!

---
