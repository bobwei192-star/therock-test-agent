# Problem with ubuntu xenial repository

> **Issue #394**
> **状态**: closed
> **创建时间**: 2018-04-25T21:33:29Z
> **更新时间**: 2018-04-25T21:40:49Z
> **关闭时间**: 2018-04-25T21:40:49Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/394

## 描述

    E: The repository 'http://repo.radeon.com/rocm/apt/debian xenial Release' does not have a Release file.
    N: Updating from such a repository can't be done securely, and is therefore disabled by default.
    N: See apt-secure(8) manpage for repository creation and user configuration details.



---

## 评论 (1 条)

### 评论 #1 — boxerab (2018-04-25T21:40:48Z)

Problem was:  

`http://repo.radeon.com/rocm/apt/debian` should be replaced by 
`http://repo.radeon.com/rocm/apt/debian/debian`


---
