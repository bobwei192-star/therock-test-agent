# Question: is membership in the 'video' group mandatory?

> **Issue #1622**
> **状态**: closed
> **创建时间**: 2021-11-19T12:20:08Z
> **更新时间**: 2024-01-02T18:56:36Z
> **关闭时间**: 2024-01-02T18:56:36Z
> **作者**: mtds
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1622

## 描述

As stated in the subject, I would like to know if it is an absolute requirement that every users that try to access and run
his/her workload on the AMD GPUs must be an explicit member of the `video` group.

With our current setup this would be quite complicated to implement:

* there is no direct login involved (nor via GDM/KDM or SSH), so the methods based on `pam_group.so` and `/etc/security/groups.conf` are not an option.
* modifications on our current centralized LDAP service are tricky to perform as well, since the `video` group is a system group and by internal policy we do not export them.
* list explicitly all the potential users under `/etc/group` on dozens of machines is somehow doable via configuration management but it is at best cumbersome and it is clear it does not scale when there are more than 15 users and many more may be added in the future.

Other than these three possibilities, there is no easy way to transparently add a supplementary group to every possible users as soon as  a job is started (not interactively but as batch) via our job management system (Slurm).

The solution provided in the official documentation:

https://rocmdocs.amd.com/en/latest/InstallGuide.html#setting-permissions-for-groups

is definitely not feasible for us.

Details of our configuration:
* AMD Radeon MI100
* ROCm framework version 4.3.1

In addition: we **do not** use Docker to run our GPU related workload, so its command line option like `--group-add video`
is definitely not a possibility for us.

Thanks in advance!

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-11-22T09:20:30Z)

Hi @mtds 
Thanks for reaching out.
Yes, user should be part of 'video' or 'render' group as part of DRM access for accessing file system.
Its mandatory.
Thank you.

---

### 评论 #2 — abhimeda (2024-01-02T15:37:50Z)

@mtds have we resolved your issue? Can we please close it?  Thanks!

---

### 评论 #3 — mtds (2024-01-02T18:56:36Z)

@abhimeda Sure I will close it, thanks.

---
