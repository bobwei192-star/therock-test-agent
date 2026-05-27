# Clarify default installation path

> **Issue #1568**
> **状态**: closed
> **创建时间**: 2021-09-01T07:53:28Z
> **更新时间**: 2021-09-13T07:46:26Z
> **关闭时间**: 2021-09-13T07:27:15Z
> **作者**: bgoglin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1568

## 描述

Hello
Can you clarify the documentation of the default install path? https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html talks about /opt/rocm and also about /opt/rocm-<version>/. All platforms I have access to use the latter. Some RPMs from your download area too.
Is /opt/rocm supposed to be a symlink to one of the /opt/rocm-<version>/ installations? Is one of your packages supposed to create that symlink? Or do you have 2 install strategies, one for single version under /opt/rocm, and one for multiversions under /opt/rocm-<version> but no /opt/rocm?
I am asking this because I'd the hwloc configure scripts to automatically look for ROCm SMI lib/headers under /opt/rocm but I couldn't find a single platform where it would work :/
Thanks

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-09-13T07:16:36Z)

Thanks @bgoglin for reaching out.
I will check this for you and get back with an update asap.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-09-13T07:27:14Z)

Hi @bgoglin 
Please find the responses here.

1. /opt/rocm is a soft link path to the actual installed rocm like /opt/rocm-4.3.1.
2. rocm-dev package creates that soft-link post installation.
3. At a time, only one way of installation is recommended, whether its single rocm(non-versioned rocm packages) or multi-rocm(versioned rocm packages).
Its not recommended to install single and multi rocm versions together, which makes installation breakages.

Eg: rocm-dev is non-versioned package for single rocm use, whereas rocm-dev4.3.1 is a multi-version package.
We can check whether we have installed single rocm or mutli-rocm using dpkg checks, eg: “dpkg -l | grep -i rocm-dev”.
If it prints “rocm-dev”, it means its a implies single rocm package. Else, if it prints “rocm-dev4.3.1”, it means its a versioned package.

Note: Two single rocm packages can not exist. At a time, only one single rocm version can be installed.
Two multi-version packages can co-exist but /opt/rocm softlink will point to latest installed multi-versioned rocm.

Hope this helps.
Thank you.

---

### 评论 #3 — bgoglin (2021-09-13T07:46:25Z)

Thanks!

---
