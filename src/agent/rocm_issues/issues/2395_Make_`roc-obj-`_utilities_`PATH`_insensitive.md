# Make `roc-obj-*` utilities `PATH` insensitive

> **Issue #2395**
> **状态**: closed
> **创建时间**: 2023-08-22T10:48:42Z
> **更新时间**: 2024-03-09T01:48:54Z
> **关闭时间**: 2024-03-09T01:48:54Z
> **作者**: MathiasMagnus
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2395

## 负责人

- david-salinas
- kzhuravl

## 描述

These utilities (when calling one another) expect that all of them are on the PATH. This is problematic if the user doesn't add `/opt/rocm/bin` to the PATH (as the APT packages don't by default) and is also problematic in multi-version scenarios.

Please make them PATH insensitive.
