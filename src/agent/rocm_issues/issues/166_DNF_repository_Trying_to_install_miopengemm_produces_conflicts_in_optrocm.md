# DNF repository: Trying to install miopengemm produces conflicts in /opt/rocm

> **Issue #166**
> **状态**: closed
> **创建时间**: 2017-07-19T16:32:23Z
> **更新时间**: 2018-06-03T14:59:53Z
> **关闭时间**: 2018-06-03T14:59:53Z
> **作者**: mmxgn
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/166

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 负责人

- pfultz2
- dagamayank

## 描述

Hello again,

```
mmxgn@emerdesktop:~> sudo dnf install miopengemm
[sudo] password for mmxgn: 
Last metadata expiration check: 3:55:37 ago on Wed 19 Jul 2017 13:34:36 BST.
Dependencies resolved.
=========================================================================================================================================================================================================
 Package                                            Arch                                           Version                                          Repository                                      Size
=========================================================================================================================================================================================================
Installing:
 miopengemm                                         x86_64                                         1.0.1-1                                          remote                                         613 k

Transaction Summary
=========================================================================================================================================================================================================
Install  1 Package

Total size: 613 k
Installed size: 2.5 M
Is this ok [y/N]: y
Downloading Packages:
[SKIPPED] miopengemm-1.0.1-Linux.rpm: Already downloaded                                                                                                                                                
Running transaction check
Transaction check succeeded.
Running transaction test
The downloaded packages were saved in cache until the next successful transaction.
You can remove cached packages by executing 'dnf clean packages'.
Error: Transaction check error:
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hip_base-1.2.17263-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsakmt-roct-dev-1.0.6_3_gd13b4e2-1.x86_64
  file /opt/rocm/include from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsakmt-roct-dev-1.0.6_3_gd13b4e2-1.x86_64
  file /opt/rocm/lib from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsakmt-roct-dev-1.0.6_3_gd13b4e2-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsa-rocr-dev-1.1.6_21_g171a2d4-1.x86_64
  file /opt/rocm/include from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsa-rocr-dev-1.1.6_21_g171a2d4-1.x86_64
  file /opt/rocm/lib from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsa-rocr-dev-1.1.6_21_g171a2d4-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsa-ext-rocr-dev-1.1.6_21_g171a2d4-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-utils-1.0.0-1.x86_64
  file /opt/rocm/lib from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-profiler-5.1.6386-gbaddcc9.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hip_doc-1.2.17263-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hip_samples-1.2.17263-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hip_hcc-1.2.17263-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-device-libs-0.0.1-1.x86_64
  file /opt/rocm/include from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-device-libs-0.0.1-1.x86_64
  file /opt/rocm/lib from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-device-libs-0.0.1-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-dev-1.6.77-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-1.6.77-1.x86_64

Error Summary
-------------

```

My rocm.repo:

```
Error Summary
-------------

mmxgn@emerdesktop:~> cat /etc/yum.repos.d/rocm.repo 
[remote]

name=ROCm Repo

baseurl=http://repo.radeon.com/rocm/yum/rpm/

enabled=1

gpgcheck=0


```

Kind regards,

---

## 评论 (1 条)

### 评论 #1 — mmxgn (2017-08-12T10:07:44Z)

Hello, 

Do we have any updates on that issue? Are there any work arounds in the meanwhile?

Kind regards,

---
