# [Question] Is AMD Renoir supported ?

> **Issue #1648**
> **状态**: closed
> **创建时间**: 2021-12-26T13:32:34Z
> **更新时间**: 2021-12-28T05:27:28Z
> **关闭时间**: 2021-12-28T05:27:27Z
> **作者**: sviscapi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1648

## 描述

Dear all,

After reading the documentation I'm a little unsure whether my APU will be supported by ROCm, once it becomes available for my distribution of choice (Debian):

https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support

My system sports an AMD Ryzen 7 4800H CPU (Zen 2 / Renoir) with Radeon Graphics. So far I've been unable to run any OpenCL jobs on it because the libclc-amdgcn package lacks support for this model:

https://packages.debian.org/bullseye/libclc-amdgcn

Could you please shed some light on this issue ?

Best regards,

Samuel

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-12-28T05:27:27Z)

Hi @sviscapi 
Thanks for reaching out.
APUs are not supported with ROCm. Thank you.

---
