# debian repository not signed

> **Issue #127**
> **状态**: closed
> **创建时间**: 2017-06-13T04:09:07Z
> **更新时间**: 2017-07-02T20:19:45Z
> **关闭时间**: 2017-07-02T17:13:52Z
> **作者**: canesin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/127

## 描述

Hi, looks like the current repository is not signed or the current GPG key on the servcer is invalid.

```
canesin@escritorio:~$ sudo apt-key list
/etc/apt/trusted.gpg
--------------------
pub   dsa1024 2007-03-08 [SC]
      4CCA 1EAF 950C EE4A B839  76DC A040 830F 7FAC 5991
uid           [ unknown] Google, Inc. Linux Package Signing Key <linux-packages-keymaster@google.com>
sub   elg2048 2007-03-08 [E]

pub   rsa4096 2016-04-12 [SC]
      EB4C 1BFD 4F04 2F6D DDCC  EC91 7721 F63B D38B 4796
uid           [ unknown] Google Inc. (Linux Packages Signing Authority) <linux-packages-keymaster@google.com>
sub   rsa4096 2016-04-12 [S] [expires: 2019-04-12]

pub   rsa4096 2016-08-01 [SC] [expires: 2018-08-01]
      CA8B B472 7A47 B4D0 9B4E  E896 9386 B48A 1A69 3C5C
uid           [ unknown] James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
sub   rsa4096 2016-08-01 [E] [expires: 2018-08-01]

/etc/apt/trusted.gpg.d/ubuntu-keyring-2012-archive.gpg
------------------------------------------------------
pub   rsa4096 2012-05-11 [SC]
      790B C727 7767 219C 42C8  6F93 3B4F E6AC C0B2 1F32
uid           [ unknown] Ubuntu Archive Automatic Signing Key (2012) <ftpmaster@ubuntu.com>

/etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg
------------------------------------------------------
pub   rsa4096 2012-05-11 [SC]
      8439 38DF 228D 22F7 B374  2BC0 D94A A3F0 EFE2 1092
uid           [ unknown] Ubuntu CD Image Automatic Signing Key (2012) <cdimage@ubuntu.com>

canesin@escritorio:~$ sudo apt update 
Get:1 http://security.ubuntu.com/ubuntu zesty-security InRelease [89.2 kB]
Hit:2 http://us.archive.ubuntu.com/ubuntu zesty InRelease                                                                               
Get:3 http://us.archive.ubuntu.com/ubuntu zesty-updates InRelease [89.2 kB]                                                             
Get:4 http://packages.amd.com/rocm/apt/debian xenial InRelease [1,831 B]                                                                   
Ign:5 http://dl.google.com/linux/chrome/deb stable InRelease                                                                                             
Get:6 http://us.archive.ubuntu.com/ubuntu zesty-backports InRelease [89.2 kB]                                         
Hit:7 http://dl.google.com/linux/chrome/deb stable Release                           
Err:4 http://packages.amd.com/rocm/apt/debian xenial InRelease                       
  The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
Reading package lists... Done
W: GPG error: http://packages.amd.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
E: The repository 'http://packages.amd.com/rocm/apt/debian xenial InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
canesin@escritorio:~$ 
```

regards

---

## 评论 (4 条)

### 评论 #1 — PhilipDeegan (2017-06-24T14:26:56Z)

This affects me also since upgrading to debian stretch

---

### 评论 #2 — gstoner (2017-06-24T19:25:17Z)

We are changing out the repo, this is one of the thing we are addressing.


On Jun 24, 2017, at 9:26 AM, ♦♣♠♥ <notifications@github.com<mailto:notifications@github.com>> wrote:


This affects me also since upgrading to debian stretch

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/127#issuecomment-310841727>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuaC5qR3qIsvM7V1B77jfcAx-QB3zks5sHRyxgaJpZM4N39m7>.



---

### 评论 #3 — PhilipDeegan (2017-07-02T19:20:44Z)

I'm still getting this error even after changing from "http://packages" to "http://repo"

---

### 评论 #4 — gstoner (2017-07-02T20:19:45Z)

We going to need to register our repo with Debian group.  

---
