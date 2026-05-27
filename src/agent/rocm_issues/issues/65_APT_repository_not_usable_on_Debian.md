# APT repository not usable on Debian

> **Issue #65**
> **状态**: closed
> **创建时间**: 2016-12-31T23:20:33Z
> **更新时间**: 2017-02-23T02:45:32Z
> **关闭时间**: 2017-02-22T16:07:15Z
> **作者**: anewusername
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/65

## 描述

Followed the instructions in the readme, resulting in the following errors:
```
Get:76 http://packages.amd.com/rocm/apt/debian xenial InRelease [1,831 B]          
Err:76 http://packages.amd.com/rocm/apt/debian xenial InRelease                    
  The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
Reading package lists... Done                                                        
W: GPG error: http://packages.amd.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
E: The repository 'http://packages.amd.com/rocm/apt/debian xenial InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

---

## 评论 (2 条)

### 评论 #1 — jedwards-AMD (2017-02-22T16:07:11Z)

Please import the current key. You may have an old one.

---

### 评论 #2 — anewusername (2017-02-23T02:45:32Z)

The key is up to date as of 2017-02-22.
```
$ mv rocm.gpg.key rocm.gpg.key.old
$ wget -q http://packages.amd.com/rocm/apt/debian/rocm.gpg.key
$ md5sum rocm.gpg.key*
0de9302403f0e767f42c7ccaeb8fad0a  rocm.gpg.key
0de9302403f0e767f42c7ccaeb8fad0a  rocm.gpg.key.old
```

and still gives the same errors:
```
$ wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
OK

$ sudo apt update
Get:3 http://packages.amd.com/rocm/apt/debian xenial InRelease [1,831 B]
Hit:1 http://cdn-fastly.deb.debian.org/debian unstable InRelease
Err:3 http://packages.amd.com/rocm/apt/debian xenial InRelease
  The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
Hit:2 http://cdn-fastly.deb.debian.org/debian experimental InRelease
Reading package lists... Done                     
W: GPG error: http://packages.amd.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
E: The repository 'http://packages.amd.com/rocm/apt/debian xenial InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```


---
