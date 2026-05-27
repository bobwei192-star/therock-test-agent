# Missing info about how to install rocprof

> **Issue #549**
> **状态**: closed
> **创建时间**: 2018-09-18T13:54:34Z
> **更新时间**: 2018-09-20T15:30:39Z
> **关闭时间**: 2018-09-20T15:30:39Z
> **作者**: misos1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/549

## 描述

Rocprof is not installed with rocm-dkms. I was able to get it only after using:
```
sudo apt install rocprofiler-dev
```
And after that the location of rpl_run.sh was not `/opt/rocm/rocprofiler/bin/rpl_run.sh` but `/opt/rocm/bin/rpl_run.sh`.

Seems old rocm-profiler and rocm-gdb are not working anymore as is stated in readme.md (for rocm-profiler).


---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2018-09-20T15:30:39Z)

This information should be up to date in the README now. Thanks for pointing this out.

---
