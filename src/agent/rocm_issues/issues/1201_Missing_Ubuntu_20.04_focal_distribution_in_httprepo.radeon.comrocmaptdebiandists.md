# Missing Ubuntu 20.04 focal distribution in http://repo.radeon.com/rocm/apt/debian/dists

> **Issue #1201**
> **状态**: closed
> **创建时间**: 2020-08-24T06:08:10Z
> **更新时间**: 2020-12-15T11:37:46Z
> **关闭时间**: 2020-12-15T10:23:55Z
> **作者**: jmsjr
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1201

## 描述

As per #1074 and as per on-line documentation at https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html, both says that Ubuntu 20.04 is now officially supported.

However, both :
1) The on-line section at https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu 
2) And the repo at http://repo.radeon.com/rocm/apt/debian/dists/

... indicates that only Ubuntu Xenial ( 16.04 ) is supported.

Will there be a separate instructions or directory for Ubuntu 20.04 ( Focal Fossa ) ?





---

## 评论 (4 条)

### 评论 #1 — YifeiLu-1 (2020-08-24T09:36:03Z)

I used rocm-dkms package in the xenial folder for my ubuntu 20.04.1 and VEGA 64.
So far my hip code seems working fine

---

### 评论 #2 — rkothako (2020-08-25T06:03:09Z)

@jmsjr
This issue is already notified internally and will be fixed in ROCm 3.8.

xenial is the space name here which points to all packages in ROCm repo. Actually there is no issue w.r.to functionality front.
As ROCm dropped official support of Ubuntu 16.04, we have plans to change the space name to "focal" instead of "xenial".
Next release will have this change.

---

### 评论 #3 — rkothako (2020-08-25T06:04:50Z)

Yes @YifeiLuDublin, Its the same and name is only the difference.
We can use the same path for all supported versions of Ubuntu.

---

### 评论 #4 — ROCmSupport (2020-12-15T10:23:55Z)

Hi @jmsjr 
Only naming is the issue, but functionally its same only. We have plans to change the name from xenial to focal/bionic in future. But its low priority task and we are working on it too. 

---
