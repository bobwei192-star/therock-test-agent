# The xnack feature of gfx90a of different roc* libs are inconsistent

> **Issue #2358**
> **状态**: closed
> **创建时间**: 2023-07-31T06:26:25Z
> **更新时间**: 2026-03-06T20:36:46Z
> **关闭时间**: 2026-03-06T20:36:45Z
> **作者**: littlewu2508
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/2358

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- lamikr
- cgmb
- Naraenda

## 描述

I'm maintainer of Gentoo ROCm packages, and I'm confused about the xnack feature of gfx90a.

By grepping strings from binary packages hosted on https://repo.radeon.com/rocm/apt/debian/pool/main/, it seems that some libs (like rocBLAS, rocRAND, rocSOLVER, rocSPARSE) ships with `gfx90a:xnack-` and `gfx90a:xnack+` kernels; while rocFFT only ships `gfx90a` without specifying xnack feature. What's more, the Tensile library of rocBLAS contains both `gfx90a`, `gfx90a:xnack-`, and `gfx90a:xnack+` ! While `gfx908` seems to be only xnack disabled.

On a MI210 PCIe card, I also found out that it's always xnack- in `rocminfo`, despite setting `HSA_XNACK=1` and `amdgpu.noretry=0`

According to https://docs.olcf.ornl.gov/systems/crusher_quick_start_guide.html#compiling-hip-kernels-for-specific-xnack-modes, it seems that there's performance difference. So is there detailed documents and guides on xnack feature?
