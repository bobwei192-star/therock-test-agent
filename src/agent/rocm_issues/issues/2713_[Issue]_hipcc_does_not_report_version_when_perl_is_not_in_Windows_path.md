# [Issue]: hipcc does not report version when perl is not in Windows path

> **Issue #2713**
> **状态**: closed
> **创建时间**: 2023-12-14T19:48:12Z
> **更新时间**: 2025-03-24T18:36:41Z
> **关闭时间**: 2025-03-24T18:36:40Z
> **作者**: ghost
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/2713

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

### Problem Description

Documentation does not mention that perl is needed, documentation needs updating 🙏🏻 , or maybe HIP SDK for windows should bundle the perl executable and use it instead of relying on it being in path?

### Operating System

Windows 11 10.0.22621 Build 22621

### CPU

AMD Ryzen 7 5500U with Radeon Graphics

### GPU

AMD Ryzen 7 5500U with Radeon Graphics

### ROCm Version

5.5.0

### ROCm Component

hipcc

### Steps to Reproduce

1. Install the HIP SDK for Windows,
2. Run `hipcc --version`
3. Version is not reported correctly when perl is not in system or user path

### Output of /opt/rocm/bin/rocminfo --support

Could not find rocminfo on Windows
