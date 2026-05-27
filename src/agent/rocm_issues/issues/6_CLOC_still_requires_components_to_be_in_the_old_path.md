# CLOC still requires components to be in the old path

> **Issue #6**
> **状态**: closed
> **创建时间**: 2016-04-23T20:30:06Z
> **更新时间**: 2016-05-01T20:34:38Z
> **关闭时间**: 2016-05-01T20:34:38Z
> **作者**: syifan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/6

## 描述

I had just installed the ROCm using apt-get a few days ago. I saw the cloc is integrated into the package. However, in cloc.sh and snack.sh, the default path is still pointing to /opt/amd/llvm and /opt/amd/hsa. Should these default paths be updated? Is there a way that we can configure the tools to still make them usable? I did not see a clang in the llvm path, so which clang we can use for now? Can the one in /opt/rocm/hcc-hsail/bin work together with cloc?


---

## 评论 (1 条)

### 评论 #1 — jedwards-AMD (2016-05-01T20:34:38Z)

New packages for CLOC have been added to the Debian and RPM repositories. These versions of the tools should correct your problems.


---
