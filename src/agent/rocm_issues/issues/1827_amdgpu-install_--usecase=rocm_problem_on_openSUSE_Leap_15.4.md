# amdgpu-install --usecase=rocm problem on openSUSE Leap 15.4

> **Issue #1827**
> **状态**: closed
> **创建时间**: 2022-10-08T19:52:08Z
> **更新时间**: 2024-02-25T15:07:17Z
> **关闭时间**: 2024-02-25T15:07:16Z
> **作者**: jvmf1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1827

## 描述

```
$ sudo zypper --no-gpg-checks install https://repo.radeon.com/amdgpu-install/5.3/sle/15.4/amdgpu-install-5.3.50300-1.noarch.rpm 
$ amdgpu-install --usecase=rocm
Loading repository data...
Reading installed packages...
Resolving package dependencies...

Problem: nothing provides 'perl-URI-Encode' needed by the to be installed hip-devel-5.3.22061.50300-sles153.63.x86_64
 Solution 1: do not install rocm-dev-5.3.0.50300-sles153.63.x86_64
 Solution 2: break hip-devel-5.3.22061.50300-sles153.63.x86_64 by ignoring some of its dependencies
```

---

## 评论 (3 条)

### 评论 #1 — pramenku (2022-11-17T12:25:45Z)

@jvmf1 you can try below

sudo zypper addrepo https://download.opensuse.org/repositories/devel:languages:perl/SLE_15/devel:languages:perl.repo
sudo zypper ref
amdgpu-install --usecase=rocm


---

### 评论 #2 — nartmada (2024-02-22T02:55:25Z)

Hi @jvmf1, just checking if you are still seeing this issue?  Thanks.

---

### 评论 #3 — nartmada (2024-02-25T15:07:16Z)

Closing the ticket as there is no response from @jvmf1.  Please re-open the ticket if you are still experiencing this issue.  Thanks.

---
