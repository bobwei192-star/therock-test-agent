# E: Unable to locate package rocm-dkms on Ubuntu 18.04

> **Issue #836**
> **状态**: closed
> **创建时间**: 2019-07-09T00:18:01Z
> **更新时间**: 2023-07-29T20:30:39Z
> **关闭时间**: 2019-07-09T00:32:29Z
> **作者**: TobiasJu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/836

## 描述

So i followed the offical how-to, but failed already during installation:
```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
OK
```
```
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
```
```
sudo apt update
Hit:1 http://de.archive.ubuntu.com/ubuntu bionic InRelease
Hit:2 http://de.archive.ubuntu.com/ubuntu bionic-updates InRelease                                                               
Hit:3 http://de.archive.ubuntu.com/ubuntu bionic-backports InRelease                                                             
Hit:4 http://security.ubuntu.com/ubuntu bionic-security InRelease                                                              
Ign:5 http://repo.radeon.com/rocm/apt/debian xenial InRelease           
Ign:6 http://dl.google.com/linux/chrome/deb stable InRelease                                      
Err:7 http://repo.radeon.com/rocm/apt/debian xenial Release                                       
  404  Not Found [IP: 13.82.220.49 80]
Hit:8 http://dl.google.com/linux/chrome/deb stable Release
Reading package lists... Done                      
N: Ignoring file 'rocm' in directory '/etc/apt/sources.list.d/' as it has no filename extension
E: The repository 'http://repo.radeon.com/rocm/apt/debian xenial Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```
```
sudo apt-get install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
N: Ignoring file 'rocm' in directory '/etc/apt/sources.list.d/' as it has no filename extension
E: Unable to locate package rocm-dkms
```
I have new clean installation of Ubuntu 18.04.


---

## 评论 (9 条)

### 评论 #1 — amd-aakash (2019-07-09T00:24:05Z)

Hi,
 Can you try again ? I just tried it on my 18.04 system and am able to download rocm without any issues.

---

### 评论 #2 — TobiasJu (2019-07-09T00:32:10Z)

Hi aaksud,

well your answer worked, thanks. 
I did exactly the same steps, 3 times. Then reported here, than again a 4th time and then it worked. The more I learn, the less I seem to know about Ubuntu.

---

### 评论 #3 — massimotamos (2020-04-12T21:30:23Z)

This ROCm project is a mega disaster. Nothing works despite trying out all the info on blogs and documentation. AMD website and documentation is not at the expected quality level.

---

### 评论 #4 — edhemphill (2020-08-17T04:47:44Z)

So:

```
Need to get 756 B of archives.
After this operation, 0 B of additional disk space will be used.
Err:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dkms amd64 3.5.1-34
  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dkms/rocm-dkms_3.5.1-34_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
```

But here is the thing - there is no `rocm-dkms_3.5.1-34_amd64.deb` at the given path at repo.radeon.com. The latest version there is 3.5.0-30

http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dkms/

So what's up AMD? The issue is not closed. Whoever is supposed to be maintaining the repo is not doing their job. Get it together. Seriously.  CUDA stuff just works.

---

### 评论 #5 — xuhuisheng (2020-08-17T05:21:09Z)

please try http://repo.radeon.com/rocm/apt/3.5.1, The http://repo.radeon.com/rocm/apt/debian seems forward to the http://repo.radeon.com/rocm/apt/3.5

```
1.9.3/                                             13-Dec-2018 08:30                   -
2.0/                                               18-Dec-2018 07:11                   -
2.1/                                               02-Feb-2019 04:50                   -
2.10.0/                                            20-Nov-2019 04:06                   -
2.10.0-hipclang/                                   14-Mar-2020 01:36                   -
2.2/                                               08-Mar-2019 07:10                   -
2.3/                                               17-Apr-2019 21:36                   -
2.4/                                               03-May-2019 03:33                   -
2.5/                                               07-Jun-2019 20:11                   -
2.6/                                               09-Jul-2019 00:11                   -
2.7/                                               10-Aug-2019 10:00                   -
2.7.1/                                             10-Sep-2019 23:30                   -
2.7.2/                                             29-Aug-2019 19:17                   -
2.8.0/                                             20-Sep-2019 17:34                   -
2.9.0/                                             02-Oct-2019 04:21                   -
3.0/                                               17-Dec-2019 07:23                   -
3.1/                                               25-Feb-2020 08:19                   -
3.1.1/                                             13-Mar-2020 17:22                   -
3.3/                                               18-Apr-2020 01:44                   -
3.5/                                               02-Jun-2020 23:32                   -
3.5.1/                                             17-Jun-2020 19:37                   -
debian/                                            02-Jun-2020 23:32                   -
```

---

### 评论 #6 — cia05rf (2021-09-20T09:29:39Z)

If it helps anyone later on searhcing this i found my solution was that i'd missed out `apt` from the path

it was:
`deb [arch=amd64] https://repo.radeon.com/rocm/debian/ xenial main`

it SHOULD have been:
`deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main`

---

### 评论 #7 — kleyton67 (2022-09-11T17:05:04Z)

The link to gpg key is: http://repo.radeon.com/rocm/rocm.gpg.key

---

### 评论 #8 — De-Been-Tech-Solutions (2023-07-25T11:33:03Z)

Yeah..... I am having the same exact problems as everyone above.

And the reason is WSL in general, cannot see the GPU and therefore ignores it, which is why WSL based distro's do not install amdgpu nor its -dkms package.

---

### 评论 #9 — De-Been-Tech-Solutions (2023-07-29T20:30:09Z)

Huh, ROCm appears to not support consumer GPU's other then a Radeon Vega VII.

https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html

---
