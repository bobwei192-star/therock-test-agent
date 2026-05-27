# DNF repository: miopen-hip-1.0.0-1.x86_64 tries to pull nonexistent rocm-opencl-dev

> **Issue #165**
> **状态**: closed
> **创建时间**: 2017-07-19T16:29:32Z
> **更新时间**: 2018-06-03T14:49:40Z
> **关闭时间**: 2018-06-03T14:49:40Z
> **作者**: mmxgn
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/165

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 负责人

- pfultz2
- dagamayank

## 描述

Hello,

```
~> sudo dnf install miopen-hip
Last metadata expiration check: 3:48:39 ago on Wed 19 Jul 2017 13:34:36 BST.
Error: 
 Problem: conflicting requests
  - nothing provides rocm-opencl-dev needed by miopen-hip-1.0.0-1.x86_64

```
But rocm-opencl-devel exists instead:

```
mmxgn@emerdesktop:~> dnf search rocm-opencl-dev
Last metadata expiration check: 2:03:19 ago on Wed 19 Jul 2017 15:22:47 BST.
===================================================================================== 
Name Matched: rocm-opencl-dev
=====================================================================================
rocm-opencl-devel.x86_64 : OpenCL/ROCm
```

My rocm.repo

```
mmxgn@emerdesktop:~> cat /etc/yum.repos.d/rocm.repo 
[remote]

name=ROCm Repo

baseurl=http://repo.radeon.com/rocm/yum/rpm/

enabled=1

gpgcheck=0

```

Regards,
