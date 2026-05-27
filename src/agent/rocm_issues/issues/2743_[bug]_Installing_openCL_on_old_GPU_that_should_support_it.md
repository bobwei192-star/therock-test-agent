# [bug]: Installing openCL on old GPU that should support it

> **Issue #2743**
> **状态**: closed
> **创建时间**: 2023-12-18T00:07:41Z
> **更新时间**: 2024-11-06T15:22:03Z
> **关闭时间**: 2024-11-06T15:22:03Z
> **作者**: BarbzYHOOL
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/2743

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

### Suggestion Description

Hello, I have an AMD Radeon HD 7870 and it should support opencl

I'm on POPOS 22.04 and I managed to install these:
amdgpu-install_5.4.50401-1_all.deb  amdgpu-install_5.7.50702-1_all.deb    amdgpu-install_5.5.50503-1_all.deb 

Install with 5.7 == impossible to work, it doesn't find some packages (spent 1h on google and no one has any solution)

For both below, I had to install in top of that mesa-opencl-icd
Install with 5.4 == i didn't notice errors but it doesn't work in the end
Install with 5.5 == several errors, and it doesn't work either

"clinfo" gives me 2 platforms but always 0 devices

I cannot find any solution, everybody just say to retry reinstalling with different options, it makes no sense
I installed with --use-case=opencl (or without this) and --opencl=legacy

### Operating System

pop os 22.04

### GPU

Radeon HD 7870 

### ROCm Component

_No response_
