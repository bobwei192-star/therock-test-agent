# Readme formatting

> **Issue #953**
> **状态**: closed
> **创建时间**: 2019-11-28T19:36:53Z
> **更新时间**: 2020-12-02T03:27:38Z
> **关闭时间**: 2020-12-02T03:27:38Z
> **作者**: atamazov
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/953

## 负责人

- amd-aakash
- Rmalavally

## 描述

Formatting of readme looks incorrect. For example, see point 2 [there](https://github.com/RadeonOpenCompute/ROCm#installing-a-rocm-package-from-a-debian-repository) -- the users who would copy-paste this onto their command line will be surprised.

This came from #945

---

## 评论 (6 条)

### 评论 #1 — zhang2amd (2019-12-19T23:28:11Z)

Thanks for raising the issue. The typo has been fixed.

---

### 评论 #2 — WalterPiTheScienceGuy (2020-01-03T17:04:00Z)

Very similar issue with point 2 in different iteration (install instructions for ROCm v3.0), so using same thread.
https://rocm.github.io/ROCmInstall.html

The resulting rocm.list file looks more like a manual for gpg then anything meaningful, and it produces the error on next step (sudo apt update):

"""
waltp@waltp-HP-Pavilion-Laptop-15z-cw100:~$ sudo apt update
E: Type 'gpg' is not known on line 1 in source list /etc/apt/sources.list.d/rocm.list
E: The list of sources could not be read.
"""

More detailed explanation (including rocm.list file) in text: 
[ROCm_install_difficulty.txt](https://github.com/RadeonOpenCompute/ROCm/files/4020034/ROCm_install_difficulty.txt)





---

### 评论 #3 — WalterPiTheScienceGuy (2020-01-03T17:25:17Z)

Oh, I see.  The typo was fixed for the GitHub Readme text but not the website-style presentation at https://rocm.github.io/ROCmInstall.html
I deleted rocm.list and then followed the corrected Readme text, and now it's fine. :)

---

### 评论 #4 — jithunnair-amd (2020-02-06T18:13:47Z)

Actually, I think the https://rocm.github.io/ROCmInstall.html page still needs some finessing. In the "Ubuntu" section, the "|" pipe command is formatted into a table for whatever reason, so it isn't evident that the two commands are to be given on the same line. Also, a copy paste of the command provided (`echo ‘deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main’`) (ie. with single quotes) put those quotes into rocm.list as well, which obviously doesn't work. Replacing them with single or double quotes retyped in the terminal worked. (It could also have to do with the unicode character for the single quote on the website being different than the single quote on an Ubuntu terminal, since they look different: `‘` (doesn't work) vs `'` (works)). My system details are:
```
NAME="Ubuntu"
VERSION="18.04.3 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.3 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

---

### 评论 #5 — jithunnair-amd (2020-02-06T18:59:43Z)

More nits:
https://rocm.github.io/ROCmInstall.html:
1. The below needs to be separated out into two commands:
`sudo apt update sudo apt install rocm-dkms`
2. The commands in the `By default, add any future users to the video group` section are missing the "|" operator again. This also needs to be corrected in the [wiki doc](https://github.com/RadeonOpenCompute/ROCm#installing-a-rocm-package-from-a-debian-repository).

---

### 评论 #6 — jlgreathouse (2020-12-02T03:27:38Z)

In the intervening months, our installation directions have been centralized in [the readthedocs site](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html). I believe the issues raised here are all fixed in the current documentation. Thanks!

---
