# Unable to run with 7900 xtx

> **Issue #2746**
> **状态**: closed
> **创建时间**: 2023-12-18T08:58:53Z
> **更新时间**: 2024-03-31T15:10:44Z
> **关闭时间**: 2024-03-31T15:10:44Z
> **作者**: AlfredTallMountain
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2746

## 描述

Hi I've tried every combination possible of rocm and pytorch
(with docker, without, from sources, 5.6, 5.7, with env variables, ...)
but all that I get is 100% CPU forever of immediate segfault.

This is on fresh ubuntu 22.04.

amdgpu-install has all the 'usecases', rocminfo and rocm-smi do work,
steam is able to run 3d accelerated games
and on windows the card works (tried stable diffusion, shark ai, directml)

Did anyone here have more luck ?

