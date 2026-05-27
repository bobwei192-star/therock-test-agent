# Is it possible to use llvm/clang-8.0.0 to build ROCm?

> **Issue #749**
> **状态**: closed
> **创建时间**: 2019-03-20T20:32:09Z
> **更新时间**: 2019-03-21T15:49:03Z
> **关闭时间**: 2019-03-21T15:49:02Z
> **作者**: justxi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/749

## 描述

Is it possible to use llvm/clang-8.0.0 from llvm.org to build ROCm?

---

## 评论 (8 条)

### 评论 #1 — jlgreathouse (2019-03-20T21:12:08Z)

Could you define what you mean by "build ROCm"? Which parts of ROCm are you looking to build, precisely? Is there a particular problem you're running into if you try to do this?

---

### 评论 #2 — justxi (2019-03-20T21:25:23Z)

There is currently no problem. At least I want to build ROCt-Thunk-Interface, ROCR-Runtime and ROCm-OpenCL-Runtime. Other parts/packages should follow.  
If it is possbile to use llvm/clang from llvm.org, it would not be necessary to install llvm/clang from ROCm additionally (I am trying to help package ROCm for Gentoo Linux). 
So my question is, if it is known to work or if there are changes which are not upstreamed yet, but necessary for building?

---

### 评论 #3 — jlgreathouse (2019-03-20T21:57:50Z)

So your question is that you want to _build_ ROCm using upstream LLVM, or you want to _use_ upstream LLVM in parts of ROCm (such as for the back-end device compiler for our OpenCL runtime)?

---

### 评论 #4 — justxi (2019-03-21T06:11:43Z)

The second, I would like to use upstream LLVM in parts of ROCM. The idea is, to split the build process, maybe it is not necessary to build the compiler backend every time, when ROCm libraries change(?).

---

### 评论 #5 — scchan (2019-03-21T15:25:49Z)

Most of our compute libraries depend on custom changes that currently only exist in our own branches.  Also, our toolchain and libraries evolve pretty quickly together so it would require the entire stack to be upgraded for every new release.

---

### 评论 #6 — justxi (2019-03-21T15:44:31Z)

Ok, thank you, that clarifies my question. 
Is it planned to upstream all changes in the long term?

---

### 评论 #7 — scchan (2019-03-21T15:45:29Z)

yes

---

### 评论 #8 — justxi (2019-03-21T15:49:02Z)

Ok, then I will wait and postpone splitting the build process.
In the meantime I will use all the software from the ROC repsositories.
Thanks. 

---
