# Ubuntu / Debian packages do not update /opt/rocm symlink

> **Issue #1157**
> **状态**: closed
> **创建时间**: 2020-06-22T07:21:58Z
> **更新时间**: 2021-01-12T08:10:32Z
> **关闭时间**: 2021-01-12T08:10:32Z
> **作者**: Dantali0n
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1157

## 描述

The Debian / Ubuntu packages will not update the `/opt/rocm` symlink when upgrading to a new releases. This leaves everything in a broken state after upgrading.

---

## 评论 (5 条)

### 评论 #1 — YifeiLu-1 (2020-06-22T12:05:20Z)

Maybe try uninstall the previous rocm version and reinstall 3.5.1 following the [installation guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html)?
This fixed my 3.5.0 and 3.5.1 mix.

---

### 评论 #2 — Dantali0n (2020-06-22T12:52:35Z)

> Maybe try uninstall the previous rocm version and reinstall 3.5.1 following the [installation guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html)?
> This fixed my 3.5.0 and 3.5.1 mix.

Yes that would be a workaround but not a fix, deb packages should be self isolated packages that make all necessary changes. Any dependency or transition required to update from one package to the next should be made by simply upgrading to the newer version of the package.

---

### 评论 #3 — bd4 (2020-06-22T23:43:55Z)

Related to #1160. Having to uninstall first or force re-install on every minor version update is a very unexpected extra requirement for those used to ubuntu/debian systems.

---

### 评论 #4 — ye-luo (2020-06-24T14:28:12Z)

This caused a lot of pain to reinstall many packages manually via trial and error.

---

### 评论 #5 — ROCmSupport (2021-01-12T08:10:32Z)

Hi @Dantali0n and others,
ROCm upgrade is not upto mark and so recommend all to go with uninstall and install for now.
Solved most of the issues specific to ROCm Upgrade now, we will share an official note once all checks are done. Please stay tuned for the updates.
Thank you.


---
