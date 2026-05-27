# amdflang not workable because of broken package dependencies

> **Issue #1808**
> **状态**: closed
> **创建时间**: 2022-09-16T15:48:05Z
> **更新时间**: 2024-07-03T16:34:03Z
> **关闭时间**: 2024-07-03T16:34:03Z
> **作者**: bertwesarg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1808

## 负责人

- frepaul

## 描述

when installing just the `rocm-llvm` Debian package for 5.2.3, the provided `amdflang` binary is not workable:

```console
$ amdflang -o conftest    conftest.f  -lz >&5
clang-14: error: unable to execute command: Executable "flang1" doesn't exist!
```

Because `flang1` is only provided in the (badly generic named) package `openmp-extras`:

```console
$ dpkg -S /opt/rocm-5.2.3/llvm/bin/amdflang 
rocm-llvm: /opt/rocm-5.2.3/llvm/bin/amdflang
$ dpkg -S /opt/rocm-5.2.3/llvm/bin/flang1
openmp-extras: /opt/rocm-5.2.3/llvm/bin/flang1
$ apt-cache depends openmp-extras
openmp-extras
  Depends: rocm-llvm
  Depends: rocm-device-libs
  Depends: rocm-core
```


---

## 评论 (8 条)

### 评论 #1 — saadrahim (2022-09-16T17:46:12Z)

Thank you for reporting the issue. @frepaul will be able to help resolve this issue.

---

### 评论 #2 — frepaul (2022-09-16T18:37:52Z)

@bertwesarg  Once again thanks for reporting.
I hope you are able to continue with the usage once openmp-extras is installed.

Discussing internally on how to correct this issue by packaging flang related files in one and same package. 


---

### 评论 #3 — bertwesarg (2022-09-16T20:25:06Z)

It would be great, if the [ROCm docker images](https://github.com/RadeonOpenCompute/ROCm-docker/tree/master/dev) already install the `rocm-llvm` and `openmp-extras` packages.

---

### 评论 #4 — bertwesarg (2022-09-17T20:45:48Z)

…and the while you are at it, `hip-runtime-amd` package would be great too.

---

### 评论 #5 — bertwesarg (2022-09-19T12:54:58Z)

nevermind my last two comments, installing `python-is-python3` triggered the removal of these packages

---

### 评论 #6 — bertwesarg (2022-09-19T13:56:37Z)

See [#112](/RadeonOpenCompute/rocm_smi_lib/issues/112)

---

### 评论 #7 — MathiasMagnus (2023-08-17T11:15:05Z)

This issue was reported in 2022 September. I ran into it on 2023 August. I'd have thought that installing a defunct toolchain was something that would be prioritized higher. I understand that `rocm-terminal` and similar docker images install `openmp-extras`, but it's still a major bug for a package to install an executable that practically can't compile an empty main function.

---

### 评论 #8 — harkgill-amd (2024-07-03T16:34:03Z)

Hi @bertwesarg, this issue was resolved in an earlier release of ROCm. If you are still seeing issues with `amdflang`, please open a new issue. Thanks!

---
