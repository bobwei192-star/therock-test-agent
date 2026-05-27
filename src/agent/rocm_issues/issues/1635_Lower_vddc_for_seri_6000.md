# Lower vddc for seri 6000

> **Issue #1635**
> **状态**: closed
> **创建时间**: 2021-12-10T18:09:12Z
> **更新时间**: 2022-01-28T11:43:54Z
> **关闭时间**: 2021-12-20T09:18:24Z
> **作者**: phucvinh52
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1635

## 描述

Hi team,
I have a problem when use voltoffset for 6600xt.
I set VDDC_OFFSET: -150 (or -200 or -400) but when I cat file `/sys/class/drm/card1device/hwmon/hwmon*/in0_input` seem it stable min at 737(mV).
Could i set lower vddc for my gpu.
Thanks 

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-12-20T09:18:24Z)

Hi @phucvinh52 
Thanks for reaching out.
We are not supporting Navi23 with ROCm, so can not comment on this.
Thank you.

---

### 评论 #2 — masahi (2022-01-21T18:14:05Z)

> We are not supporting Navi23 with ROCm

@ROCmSupport 
Do you mean "currently", or navi23 support will never come even in future release? I've seen that RDNA2 cards would get support soon.

---

### 评论 #3 — ROCmSupport (2022-01-28T11:43:54Z)

Hi @masahi 
I am not sure about future plans right now.
If we have some support plans in future, we will update via our documentation. Thank you.

---
