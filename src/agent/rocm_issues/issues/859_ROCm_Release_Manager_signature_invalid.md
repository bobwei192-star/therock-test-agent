# ROCm Release Manager signature invalid

> **Issue #859**
> **状态**: closed
> **创建时间**: 2019-08-10T08:30:57Z
> **更新时间**: 2024-01-29T02:51:35Z
> **关闭时间**: 2019-08-10T08:34:22Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/859

## 描述

I get this error related to the signature of the release manager being invalid:

```
$ sudo apt update
[...]
Err:20 http://repo.radeon.com/rocm/apt/debian xenial InRelease                                         
  The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
Reading package lists... Done 
Building dependency tree       
Reading state information... Done
All packages are up to date.
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://repo.radeon.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
W: Failed to fetch http://repo.radeon.com/rocm/apt/debian/dists/xenial/InRelease  The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
W: Some index files failed to download. They have been ignored, or old ones used instead.
```

---

## 评论 (3 条)

### 评论 #1 — Bengt (2019-08-10T08:34:12Z)

[As suggested before](https://github.com/RadeonOpenCompute/ROCm/issues/854#issuecomment-517859522), updating the signature helped:

```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
```

---

### 评论 #2 — bankh (2023-02-09T01:35:14Z)

If one needs to use an older repository, the following will work by the date of this post:
```
$ wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
```

Then the following will work and the following example is for rocm3.5.1:
```
$ echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/3.5.1/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
$ sudo apt update
```

---

### 评论 #3 — Artem-B (2024-01-29T02:51:34Z)

This should probably be mentioned somewhere in the ROCm installation instructions. I've just ran into the same issue trying to isntall ROCm 6.0 on Ubuntu 20.04 following the official "quick start" instructions here: https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html#rocm-install-quick

---
