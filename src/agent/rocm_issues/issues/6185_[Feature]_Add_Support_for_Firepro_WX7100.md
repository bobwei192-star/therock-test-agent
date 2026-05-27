# [Feature]: Add Support for Firepro WX7100

> **Issue #6185**
> **状态**: open
> **创建时间**: 2026-04-27T04:56:36Z
> **更新时间**: 2026-05-22T09:13:51Z
> **作者**: alter-affe
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/6185

## 标签

- **Feature Request** (颜色: #fbca04)

## 负责人

- schung-amd

## 描述

### Suggestion Description

Ich have a Firepro WX7100 graphics card which worked nicely for OpenCL-Usage with the proprietary amdgpu-pro drivers. However those have meanwhile been superseeded by the rocm-Drivers and the distros have reaches EOL. Installing rocm-drivers on Debian Trixie does not make OpenCL work with the Firepro WX7100.
Since exept this the card is doing fine I would not like to throw it (Usaecases: Libreoffice, Darktable, Blender).

Thanks in advance.

### Operating System

Debian

### GPU

_No response_

### ROCm Component

_No response_

---

## 评论 (1 条)

### 评论 #1 — Kinetic-Labs-GT (2026-05-22T09:13:51Z)

This feature request is fundamentally un-actionable within this repository's codebase. The FirePro WX7100 is built on the Polaris 10 architecture (`gfx803`), which reached formal end-of-life (EOL) status within the ROCm ecosystem during the ROCm 4.0 release sequence.

### Technical Limitations

1. **Compiler Infrastructure Pruning:** Mainline ROCm runtimes and their underlying LLVM-based back-ends have long since stripped the target code-generation codebases for `gfx803`. Restoring support is not a matter of a configuration change; it would require back-porting millions of lines of hardware-specific compiler structures and testing frameworks into the modern compiler tree.
2. **Hardware Atomic Requirements:** Modern ROCm components assume native PCIe 3.0/4.0/5.0 atomic operation support from the host platform and GPU firmware. Legacy GCN 4th Gen hardware lacks reliable support for these hardware-enforced primitives within current unified memory and HSA driver architectures.
3. **Driver Evolution:** The driver path requested by the poster (older `amdgpu-pro` packages) has been replaced by the modern upstream kernel `amdgpu` interface, which does not map memory objects or command submissions in a way that allows the modern user-space `ROCR-Runtime` to interoperate with legacy silicon.

### Recommended Community Solutions
For users seeking to keep `gfx803` hardware operational for open-source compute workloads, mainline tracking here is closed. You must look toward independent enthusiast efforts, such as the [xuhuisheng/rocm-gfx803](https://github.com/xuhuisheng/rocm-gfx803) or [robertrosenbusch/gfx803_rocm](https://github.com/robertrosenbusch/gfx803_rocm) containerized/patched compilation trees, which compile older iterations of the software stack to bypass upstream architectural blocks.

---
