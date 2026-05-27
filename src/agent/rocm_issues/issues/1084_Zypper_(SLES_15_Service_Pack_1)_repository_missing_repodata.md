# Zypper (SLES 15 Service Pack 1) repository missing "repodata"

> **Issue #1084**
> **状态**: closed
> **创建时间**: 2020-04-20T12:47:00Z
> **更新时间**: 2021-03-17T07:23:24Z
> **关闭时间**: 2021-03-17T07:23:24Z
> **作者**: FilipVaverka
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1084

## 描述

ROCm SLES 15 Service Pack 1 repository (zypper) at [http://repo.radeon.com/rocm/zyp/zypper/](http://repo.radeon.com/rocm/zyp/zypper/) seems to be missing repository metadata "[repodata](http://repo.radeon.com/rocm/zyp/zypper/repodata/)" used by zypper. This results in following error when update is attempted:

> An error occurred during repository initialization. [zypper|http://repo.radeon.com/rocm/zyp/zypper/] Repository type can't be determined.

The "repodata" are present in version [3.1.1](http://repo.radeon.com/rocm/zyp/3.1.1/repodata/) but not in [3.3](http://repo.radeon.com/rocm/zyp/3.3/repodata/).

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-03-17T07:23:24Z)

Hi @FilipVaverka 
Thanks for reaching out.
This issue is fixed and no more observed with the latest ROCm 4.0 and so request you to try the same.
Thank you.


---
