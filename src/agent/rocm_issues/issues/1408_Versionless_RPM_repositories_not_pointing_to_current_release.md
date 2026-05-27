# Versionless RPM repositories not pointing to current release

> **Issue #1408**
> **状态**: closed
> **创建时间**: 2021-03-19T11:06:46Z
> **更新时间**: 2021-08-04T10:03:32Z
> **关闭时间**: 2021-03-19T11:42:45Z
> **作者**: pjgeorg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1408

## 描述

Both https://repo.radeon.com/rocm/yum/rpm/ and https://repo.radeon.com/rocm/centos8/rpm/ point to version 4.0.0. However the current release is 4.0.1.

Users probably expect the versionless repository link to always point to the current release. This is actually not the first time this happened. The same happened with previous micro (x.x.1) releases. For major and minor releases the versionless repo has always been updated.

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-03-19T11:27:59Z)

Hi @pjgeorg 
Thanks for reaching out.
**Actually this is not an issue, is the new process.**
We do not wish to change/update repos with every point release as point release is with some specific changes and we do not expect all users to try for the same and its not required too. 

https://repo.radeon.com/rocm/yum/rpm/ --> Refers to the major release only
https://repo.radeon.com/rocm/yum/4.0.x/ --> Refers to the point releases
So when you wish to try with the latest point release, I recommend to check for https://repo.radeon.com/rocm/yum/ space and look for the latest point release. Map accordingly and you are able to install it.
Hope it helps.
Feel free me reach for any other query.
Thank you.



---

### 评论 #2 — pjgeorg (2021-03-19T11:42:45Z)

Thanks for your reply.

This actually makes no sense to me as users of https://repo.radeon.com/rocm/yum/rpm/ will be hit by unexpected major releases anyway. Hence users who do not want the version to be changed should rely on specifiying a particular version, e.g. https://repo.radeon.com/rocm/yum/4.0.0/
With your new process using https://repo.radeon.com/rocm/yum/rpm/ is now neither suitable for users that want to always have the current version nor for users who want to install a particular version.
I honestly can't think of any user who wants to get major release updates automatically but no point release updates.

Anyway it's the new process, fine for me. At least I now know what to do and what to expect.
However you should probably update https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#centos-rhel to reflect this new process.


---

### 评论 #3 — ROCmSupport (2021-03-19T12:01:20Z)

Thanks @pjgeorg for the feedback.
The concept of point releases are redefined now.
These point releases are only special builds, generated only in case of any specific issue/changes. So major release builds will serve all f the things mostly.
Anyways, I will make sure to update this point in our docs.
Thank you much.

---

### 评论 #4 — ROCmSupport (2021-08-04T10:03:32Z)

Docs updated with this information now.
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

ROCm Repositories
    For major releases - https://repo.radeon.com/rocm/yum/rpm/
    For point releases - https://repo.radeon.com/rocm/yum/4.3.x/

---
