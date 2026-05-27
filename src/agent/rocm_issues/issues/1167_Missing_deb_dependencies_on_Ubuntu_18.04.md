# Missing deb dependencies on Ubuntu 18.04

> **Issue #1167**
> **状态**: closed
> **创建时间**: 2020-06-25T21:43:38Z
> **更新时间**: 2020-06-26T16:19:46Z
> **关闭时间**: 2020-06-26T16:19:46Z
> **作者**: rbberger
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1167

## 描述

During linking the following error message is written out:

```
Can't exec "file": No such file or directory at /opt/rocm/bin/hipcc line 584.
Use of uninitialized value $fileType in pattern match (m//) at /opt/rocm/bin/hipcc line 585.
Use of uninitialized value $fileType in pattern match (m//) at /opt/rocm/bin/hipcc line 585.
Use of uninitialized value $fileType in pattern match (m//) at /opt/rocm/bin/hipcc line 586.
```
This eventually ends with a linking failure.

Apparently, the `hipcc` wrapper uses the `file` command, which wasn't installed as a dependency.

Also: doing an `apt-get upgrade` on the `rocm/dev-ubuntu-18.04:3.5` Docker container completely messes up the install due to missing reinstalls of dependent packages, since some packages will update to 3.5.1. Only a completely fresh install based on Ubuntu 18.04 seems to produce a usable environment (apart from missing dependencies like `file`).

---

## 评论 (5 条)

### 评论 #1 — skyreflectedinmirrors (2020-06-25T22:45:16Z)

@rbberger -- any chance you have the full list of dependencies missing from the image? (not the broken install part, but things like `file`)

Thanks!

---

### 评论 #2 — rbberger (2020-06-25T23:17:28Z)

@arghdos I gave up chasing them and just did a fresh install.

Essentially, avoid the upgrade from 3.5.0 to 3.5.1, do a fresh install of 3.5.1 on the base `ubuntu:18.04` image, and install the `file` package. `hipcc` now completes my compilation and links the binary.

Here is what I did for our Singularity container https://github.com/lammps/lammps/pull/2167/commits/e6b3611c2d33cda5fc3f5336a9fada3d287db30a. 

---

### 评论 #3 — sunway513 (2020-06-26T01:11:32Z)

Hi @rbberger , I’ll update the Ubuntu18.04 base dockerfile with `file` and refresh the public docker containers. Thanks for bringing up this issue. 

---

### 评论 #4 — sunway513 (2020-06-26T04:31:49Z)

I've refreshed the docker containers, please check and see if that works, thanks:
https://hub.docker.com/r/rocm/dev-ubuntu-18.04/tags

---

### 评论 #5 — rbberger (2020-06-26T16:19:46Z)

That works. Thanks.

---
