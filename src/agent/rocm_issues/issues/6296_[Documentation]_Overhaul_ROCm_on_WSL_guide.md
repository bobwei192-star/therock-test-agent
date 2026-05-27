# [Documentation]: Overhaul ROCm on WSL guide

> **Issue #6296**
> **状态**: open
> **创建时间**: 2026-05-24T01:09:55Z
> **更新时间**: 2026-05-24T01:10:15Z
> **作者**: benrichard-amd
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/6296

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

### Description of errors

https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/wsl/howto_wsl.html

**User:** How do I install ROCm on WSL?

**This how-to guide:** HAVE YOU HEARD OF ROCDXG? LET ME TELL YOU ABOUT HOW GREAT ROCDXG IS AND NOT TELL YOU HOW TO INSTALL ROCM ON WSL!!!!

This page does not at all tell the user how to install ROCm on WSL.  It has an entire section about ROCDXG and then points the user to the build instructions on the librocdxg github page. And then directs them to another page with general ROCm Linux setup instructions.

<img width="805" height="274" alt="Image" src="https://github.com/user-attachments/assets/cbde528c-e548-473f-8bc4-2ab9dbd45f09" />

This is confusing and frustrating. Users expect a step-by-step guide to install ROCm on WSL. 

If librocdxg is required, why are we pointing the user to build instructions instead of the [librocdxg releases page](https://github.com/ROCm/librocdxg/releases) ? 



This is roughly the actual way to set up ROCm on WSL:

1. Install latest Radeon Windows driver
2. Install WSL + Ubuntu (Point to the Microsoft page for this)
4. Inside WSL install the librocdxg `.deb` package from the releases page
5. If using < 7.13, add this to your `~/.bashrc`: `export HSA_ENABLE_DXG_DETECTION=1`
6. Follow the Ubuntu ROCm install instructions (e.g. `amdgpu-install --no-dkms --usecase=rocm`)
7. Run `rocminfo` to verify the device is detected

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_
