# Install ROCm on Ubuntu without affecting display

> **Issue #1010**
> **状态**: closed
> **创建时间**: 2020-02-05T17:04:43Z
> **更新时间**: 2025-02-19T20:12:04Z
> **关闭时间**: 2020-07-07T17:32:41Z
> **作者**: Ian-Mint
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1010

## 描述

I am running Ubuntu 18.04, and I have tried two different strategies to install ROCm.

[1] following the instructions here: https://github.com/RadeonOpenCompute/ROCm#Ubuntu

This does work, but when I reboot, I am limited to very low resolution.

[2] install rocm with amdgpu-pro following these instructions: https://www.amd.com/en/support/kb/faq/gpu-635

And the installation fails with the error:

nomodeset detected in kernel parameters. amdgpu requires KMS
I have verified that nomodeset is not present in /etc/default/grub

So, is there a good solution to either the first or the second problem?

OS: Ubuntu 18.04.4 LTS | GPU: Radeon HD 8830M / R7 M465X

---

## 评论 (3 条)

### 评论 #1 — 7allom (2025-02-19T00:02:25Z)

Hi, I got the same problem as you.
Were you able to solve it?

---

### 评论 #2 — Ian-Mint (2025-02-19T19:44:04Z)

> Hi, I got the same problem as you. Were you able to solve it?

Nope, sorry @7allom. Maybe re-open the issue and add your details. I'm pretty sure I closed this to after just giving up on ROCm entirely.

---

### 评论 #3 — 7allom (2025-02-19T20:12:02Z)

> > Hi, I got the same problem as you. Were you able to solve it?
> 
> Nope, sorry @7allom. Maybe re-open the issue and add your details. I'm pretty sure I closed this to after just giving up on ROCm entirely.

Okay thank you.
I am trying now to install now I hope it works 

---
