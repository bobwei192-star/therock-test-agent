# Repository signing key has expired

> **Issue #1538**
> **状态**: closed
> **创建时间**: 2021-08-01T14:38:13Z
> **更新时间**: 2021-08-03T13:34:49Z
> **关闭时间**: 2021-08-03T05:30:31Z
> **作者**: teruteru128
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1538

## 描述

```
pub   rsa4096 2016-08-01 [SC] [expired: 2021-08-01]
      CA8B B472 7A47 B4D0 9B4E  E896 9386 B48A 1A69 3C5C
uid           [ expired] James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
```

---

## 评论 (3 条)

### 评论 #1 — bayuah (2021-08-01T15:27:28Z)

Additional info:
```
sub rsa4096/2b2afe47a094dc2d1013777c30c07af01a6d36ba 2016-08-01T20:29:20Z            
sig sbind 9386b48a1a693c5c 2019-08-02T00:52:26Z ____________________ 2021-08-01T00:52:19Z
```
[Source](https://keyserver.ubuntu.com/pks/lookup?fingerprint=on&op=index&search=0x9386B48A1A693C5C)

I try download from the repository and check it too.
```
$ wget https://repo.radeon.com/rocm/apt/debian/rocm.gpg.key
$ gpg rocm.gpg.key
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
pub rsa4096 2016-08-01 [SC] [expired: 2021-08-01]
 CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
uid James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
sub rsa4096 2016-08-01 [E] [expired: 2021-08-01]
```
Also still expired.

---

### 评论 #2 — claforte (2021-08-02T18:18:28Z)

I apologize for the inconvenience. While I don't work in that team at AMD, we bumped into the same problem, and were told:

```
Re-importing the updated gpg key would fix this issue:

wget -qO - http://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -

Someone at the MLSE devops team has updated the expired key (on Aug 1st 2021) in ROCm repository already.
```

I hope this helps,

Christian

---

### 评论 #3 — ROCmSupport (2021-08-03T05:30:31Z)

Thanks @teruteru128 and @bayuah for reaching out.
I certainly understood the problem.
Looks like you people are using the old gpgkey, which is obsolete.

Request you to try the latest/updated key available at [https://repo.radeon.com/rocm/rocm.gpg.key](url)
Please check this for more information: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu
Hope this helps.
Thank you.

---
