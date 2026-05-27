# Repo GPG key expired

> **Issue #854**
> **状态**: closed
> **创建时间**: 2019-08-02T18:48:09Z
> **更新时间**: 2019-08-03T15:17:54Z
> **关闭时间**: 2019-08-03T15:17:54Z
> **作者**: Jenot
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/854

## 描述

pub   rsa4096 2016-08-01 [SC] [expired: 2019-08-02]
      CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
uid           James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
sub   rsa4096 2016-08-01 [E] [expired: 2019-08-02]


---

## 评论 (1 条)

### 评论 #1 — zhang2amd (2019-08-02T22:16:14Z)

The public key file has been updated as well as the checksum in the readme. Please re-import the key and try again.
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo apt update

---
