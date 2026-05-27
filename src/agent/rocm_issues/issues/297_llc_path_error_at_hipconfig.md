# llc path error at hipconfig

> **Issue #297**
> **状态**: closed
> **创建时间**: 2018-01-04T10:01:42Z
> **更新时间**: 2018-06-03T15:42:12Z
> **关闭时间**: 2018-06-03T15:42:12Z
> **作者**: greatken999
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/297

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

rocm1.7
hipconfig line 132 :system("$HCC_HOME/compiler/bin/llc --version");
need change to : system("$HCC_HOME/bin/llc --version");

---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-03-02T23:09:01Z)

@greatken999   Can you try the beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2  It supports 4.13 Linux kernel 

---

### 评论 #2 — davclark (2018-04-18T03:43:20Z)

I'm having the same trouble, which led me to wonder if there's also a way to check the rocm version on the command line? I've installed them via apt, which reports version 1.7.137 for many of the packages.

---
