# Debian bullseye and libgcc deps

> **Issue #1230**
> **状态**: closed
> **创建时间**: 2020-09-22T20:05:51Z
> **更新时间**: 2020-11-18T11:14:03Z
> **关闭时间**: 2020-11-18T11:14:03Z
> **作者**: piodag
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1230

## 描述

Hi,

is there a way to circumvent the deps on libgcc-7 and to be able to run at least the rocm-dev version on Bullseye/Sid?

Is an hard world. For the best R support I need testing or Sid. For the best tensorflow  and keras some stable (but way older) Ubuntu. I'd say that keeping an up to date Debian Sid version would give you two birds with a single stone.

Regards

gfwp

---

## 评论 (2 条)

### 评论 #1 — baryluk (2020-09-22T20:13:27Z)

Yes, there is a workaround.

Download the deb package for llvm-amdgpu or llvm-amdgpu3.7.0. Unpack it, edit control file, and change / remove dependency on libgcc-7. Then repack using `dpkg-buildpackage`, and install using `dpkg -i`. It did work for me, and I didn't spotted any actual binary having issues.

See https://github.com/RadeonOpenCompute/ROCm/issues/1125


---

### 评论 #2 — rkothako (2020-11-03T11:41:32Z)

Hi @gfwp 
Can you please close this ticket if the above workaround helps you.
Please share an update. Thank you.

---
