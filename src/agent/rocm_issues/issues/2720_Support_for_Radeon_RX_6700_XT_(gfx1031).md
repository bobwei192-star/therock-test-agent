# Support for Radeon RX 6700 XT (gfx1031)

> **Issue #2720**
> **状态**: closed
> **创建时间**: 2023-12-15T04:04:10Z
> **更新时间**: 2024-11-13T07:40:53Z
> **关闭时间**: 2024-02-14T02:33:30Z
> **作者**: paralin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2720

## 描述

There is no TensileLibrary_lazy_gfx1031.dat which causes an error when trying to use rocBLAS with a RX 6700 XT.

How can I get this working with this GPU, or is this currently not supported? If it's not supported, will it be in the near future? Is it just HIP that's not working, or also the opencl integration?

I was able to get the opencl / clBLAST support to work with an older revision of rocm, fwiw.

### Operating System

Ubuntu 22.04.3 LTS

### ROCm Component

rocBLAS
