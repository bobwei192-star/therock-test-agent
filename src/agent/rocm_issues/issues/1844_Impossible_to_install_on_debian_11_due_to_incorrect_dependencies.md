# Impossible to install on debian 11 due to incorrect dependencies

> **Issue #1844**
> **状态**: closed
> **创建时间**: 2022-10-25T15:56:04Z
> **更新时间**: 2024-05-21T15:40:12Z
> **关闭时间**: 2024-05-21T15:40:12Z
> **作者**: joelandman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1844

## 描述

Unfortunately, the dependency list for rocm-llvm includes these:

```
 rocm-llvm : Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable or
                      libstdc++-11-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable or
                      libgcc-11-dev but it is not installable
```

but not this:

```
root@hermes:~# dpkg -l | grep libgcc-10
ii  libgcc-10-dev:amd64                              10.2.1-6                                                         amd64        GCC support library (development files)
root@hermes:~# dpkg -l | grep libgcc-9
ii  libgcc-9-dev:amd64                               9.3.0-22                                                         amd64        GCC support library (development files)
```

Please update the dependencies to include debian's versions, or, remove this dependency check in the .deb, and put it in the `amdgpu-install` script, specifically to check to see that a version of libgcc-number-dev is installed.

---

## 评论 (5 条)

### 评论 #1 — madmadman (2022-11-17T11:51:09Z)

yep, same problem. they don't seem to care. either you use ubuntu or you get the middle-finger

---

### 评论 #2 — joelandman (2022-11-17T17:34:50Z)

If anyone @AMD reads this, I'd be happy to contribute a fix/PR, if you would only be so kind as to expose your deb builder environment.  Right now it is impossible for me to build, unless I use https://github.com/xuhuisheng/rocm-build which also has issues in the repositories it pulls down.

As I've said to a number of @AMD people (at the $dayjob), you need a runfile format like nvidia, so that people can deploy/use this.  

---

### 评论 #3 — bzizou (2023-03-09T15:59:45Z)

Same problem here... I was unable to install any ROCm packages on a fresh Debian 11. Any idea to be able to use AMD MI210 GPUS from Debian?

---

### 评论 #4 — ppanchad-amd (2024-05-09T17:07:03Z)

@joelandman Apologies for the lack of response. Debian is not officially supported. Thanks!

---

### 评论 #5 — nairboon (2024-05-18T12:27:45Z)

> Same problem here... I was unable to install any ROCm packages on a fresh Debian 11. Any idea to be able to use AMD MI210 GPUS from Debian?

it kind of works now on Debian 12 Bookworm

---
