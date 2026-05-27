# RFC Support Debian Distribution with ROCm and add Repo support #65 (APT repository not usable on Debian)

> **Issue #101**
> **状态**: closed
> **创建时间**: 2017-03-28T17:21:49Z
> **更新时间**: 2018-09-16T20:24:44Z
> **关闭时间**: 2018-09-16T20:24:44Z
> **作者**: anewusername
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/101

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

See https://github.com/RadeonOpenCompute/ROCm/issues/65 - issue is still unsolved.

---

## 评论 (4 条)

### 评论 #1 — illwieckz (2017-05-28T01:45:17Z)

Same problem on Ubuntu Zesty.

`apt-key list` tells me:

```
pub   rsa4096 2016-08-01 [SC] [expire : 2018-08-01]
      CA8B B472 7A47 B4D0 9B4E  E896 9386 B48A 1A69 3C5C
uid          [ inconnue] James Adrian Edwards (ROCm Release Manager) <J----A-----.E------@amd.com>
sub   rsa4096 2016-08-01 [E] [expire : 2018-08-01]
```

I just removed the key from the keyring and reimported it, it fixed nothing.

Perhaps it can help: I faced the same issue with some obsolete repositories using crypt methods that were notified as weak while running yakkety and that are now notified as invalid keys on zesty with the same error message. Can this rocm repository signing issue be related to the way the signing key was done?

---

### 评论 #2 — gstoner (2017-07-02T17:40:48Z)

We moved to new repo server and key can you try it now  here are the instructions https://rocm.github.io/ROCmInstall.html

---

### 评论 #3 — reanimastudios (2017-07-10T20:15:00Z)

Debian rejects the key.

Err:6 http://repo.radeon.com/rocm/apt/debian xenial InRelease
  The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
Reading package lists... Done
W: GPG error: http://repo.radeon.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
E: The repository 'http://repo.radeon.com/rocm/apt/debian xenial InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
dselect: warning: subprocess update available list script returned error exit status 1
Press <enter> to continue.

I'd contact them to fix it.


---

### 评论 #4 — jlgreathouse (2018-09-16T20:24:44Z)

Considering there are folks on Phoronix [describing that ROCm 1.9.0 works on Debian](https://www.phoronix.com/forums/forum/phoronix/latest-phoronix-articles/1047471-amd-rocm-1-9-available-with-vega-20-support-plus-upstream-kernel-compatibility?p=1047503#post1047503), I assume this bug has been fixed along the way. :)

---
