# Flags used for building ROCm packages for Ubuntu/CentOS?

> **Issue #1348**
> **状态**: closed
> **创建时间**: 2020-12-23T00:16:18Z
> **更新时间**: 2021-03-09T08:13:38Z
> **关闭时间**: 2021-03-09T08:07:28Z
> **作者**: DarjanKrijan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1348

## 描述

As I can't find source packages on http://repo.radeon.com/rocm, could you disclose which flags you use for building ROCm packages for Ubuntu/CentOS.

Given the hardware requirements being essentially AMD Zen and newer or Intel Haswell and newer, I'd expect something like
```-march=haswell``` or ```-march=core-avx2``` which are both compatible with AMD Zen.
Most importantly the ```-march``` flag as well as the ```-O``` optimization level used for the repo packages would be of interest.
Any more flags that are used would be appreciated as well.

I'd propose to the package maintainers for Arch Linux over at https://github.com/rocm-arch/rocm-arch to use these flags to be in line with the upstream built packages so they achieve comparable CPU features and performance.


---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-01-04T07:55:33Z)

Thanks @darjankrijan for reaching out.
Will reach respective team and help you out

---

### 评论 #2 — ROCmSupport (2021-03-09T08:07:28Z)

Hi @darjankrijan 
We can not fulfill this requirement as we are not owning/making rocm on arch, hence I cannot comment on "seeking all the flags for building rocm-arch".
Hope it clarifies.
Thank you.

---

### 评论 #3 — DarjanKrijan (2021-03-09T08:13:37Z)

Uhm, I asked about flags used for building rocm for Ubuntu/CentOS (AMD provides repositories for these) so these can be synchronized with the community build for Arch Linux.

---
