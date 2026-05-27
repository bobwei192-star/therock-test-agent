# rocm apt repo issues..

> **Issue #1169**
> **状态**: closed
> **创建时间**: 2020-06-29T19:00:10Z
> **更新时间**: 2020-12-17T04:25:16Z
> **关闭时间**: 2020-12-17T04:25:15Z
> **作者**: evilbulgarian
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1169

## 描述

getting a lot of these errors for rocm packages..
Get:25 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocprofiler-dev amd64 1.0.0 [239 kB]
Err:25 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocprofiler-dev amd64 1.0.0
  File has unexpected size (238830 != 238824). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:7c7569771dd406d0066d5e64cec6008f51bafc719508a8f8bf106f5768f8ad92
   - SHA1:97bd8c8b614070ecdf0d7461cb869837e3c4d82b [weak]
   - MD5Sum:cfd100215149f3e69da8f5d1938c28f2 [weak]
   - Filesize:238824 [weak]
Get:26 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 roctracer-dev amd64 1.0.0 [393 kB]


---

## 评论 (6 条)

### 评论 #1 — CarlPretorius (2020-07-01T14:34:29Z)

Same here. 
Get:1 http://deb.debian.org/debian buster/main amd64 libelf-dev amd64 0.176-1.1 [72.1 kB]
Err:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 comgr amd64 1.6.0.143-rocm-rel-3.5-34-e24e8c1
  404  Not Found [IP: 13.82.220.49 80]

Get:5 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct amd64 1.0.9-347-gd4b224f [67.2 kB]
Err:5 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct amd64 1.0.9-347-gd4b224f
  File has unexpected size (67202 != 67200). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:56e4d74289e1625aed9f22b897d4a542fa3a2aa17fda0cbcab80710fedb156e7
   - SHA1:1d65862a98de6f6e2109efcf346057c622e190f6 [weak]
   - MD5Sum:2e0ad38f7a419aab64f459a19609ad19 [weak]
   - Filesize:67200 [weak]


---

### 评论 #2 — leihaoda (2020-07-03T05:39:37Z)

I tried using "sudo apt dist-upgrade", and re-add the PPA & GPG KEY, still have the same problem

---

### 评论 #3 — ableeker (2020-07-04T18:48:41Z)

The current repo debian doesn't point to the latest 3.5.1, but to 3.5.0. However, if you look at the file sizes, and the version numbers of the packages, the installer seems to expect 3.5.1. I noticed this issue today, and was able to solve it by explicitly pointing the repo to 3.5.1, instead of debian.

---

### 评论 #4 — saiarcot895 (2020-07-05T06:34:19Z)

If you want to continue using the existing repo, and are hitting the errors, run `sudo rm /var/lib/apt/lists/repo.radeon.com_rocm_apt_debian_dists_xenial_*` to explicitly delete the locally-cached package information.

The problem appears to be that `debian` was pointing to 3.5.1 at some point of time, then got changed back to 3.5, and now the apt clients that updated to 3.5.1 version of the package info files won't download the 3.5 version because it's technically older.

Also, it looks like some of the packages in this repo need proper versioning. I noticed that some packages were "upgrading" from 1.0.0 to 1.0.0, even though the package sizes were different.

---

### 评论 #5 — seesturm (2020-07-05T11:03:58Z)

Seems they still have a lot to learn what it takes to properly maintain a debian repository.
Until this is improved it might be better to release the packages as separate download(s) instead of having a frequently broken repo server.

---

### 评论 #6 — ROCmSupport (2020-12-17T04:25:15Z)

Hi @evilbulgarian 
Thanks for reaching out.
The issue caused because of keeping pkgs of 3.5 in repo first, and then 3.5.1 and then reverted back to 3.5.
This is not going to happen anymore and we brought a process into picture.

Request to try with the latest released ROCm version 3.10 and file a new ticket, if any.
Thank you.

---
