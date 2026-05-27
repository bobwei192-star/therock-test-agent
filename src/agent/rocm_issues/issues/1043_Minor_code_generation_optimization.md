# Minor code generation optimization

> **Issue #1043**
> **状态**: closed
> **创建时间**: 2020-03-15T10:08:19Z
> **更新时间**: 2021-04-05T11:52:34Z
> **关闭时间**: 2021-04-05T11:52:34Z
> **作者**: gwoltman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1043

## 描述

I'm using rocm 2.10

Both
  int  f = (d & 0xFFF00FFF) | (e & 0x000FF000);
and
  int  f = (d & 0xFFF00FFF) + (e & 0x000FF000);

could generate a single V_BFI_B32 instruction rather than these 2 instructions:

	v_and_b32_e32 v3, 0xff000, v4
	v_and_or_b32 v2, v2, s4, v3




---

## 评论 (2 条)

### 评论 #1 — gwoltman (2020-03-15T10:16:19Z)


Also, I think

int f = (d & 0xFFF00FFF) | 0x000AB000;

could do a bit-field-insert as well


---

### 评论 #2 — ROCmSupport (2021-04-05T11:52:34Z)

Thanks @gwoltman for reaching out.
As you tried it on old ROCm version: 2.10, recommend you to try with the latest ROCm 4.1 and file a new issue, if any, for quick response.
Thank you.

---
