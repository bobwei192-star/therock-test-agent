# Document that latest release does not track point releases.

> **Issue #1967**
> **状态**: closed
> **创建时间**: 2023-03-17T06:24:23Z
> **更新时间**: 2024-04-21T14:08:18Z
> **关闭时间**: 2024-04-21T14:08:18Z
> **作者**: Maetveis
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1967

## 描述

The "latest" urls on https://repo.radeon.com/rocm (e.g. https://repo.radeon.com/rocm/apt/latest for Ubuntu) is not the latest release (5.4.3 at the time of writing, the "latest" url contains 5.4.0).

This applies to the other supported distributions as well.

Is the latest repository no longer supported or is it tracking only minor releases and doesn't include bugfix releases?

---

## 评论 (4 条)

### 评论 #1 — saadrahim (2023-03-17T13:26:32Z)

Latest does not track point releases. This should be documented. 

---

### 评论 #2 — Maetveis (2023-03-17T14:00:10Z)

> Latest does not track point releases. This should be documented.

Sure, I updated the issue title. With that in mind should the quick start and installation guides use this latest url or should they point to the latest point release like on docs.amd.com? Currently they use the former and as such aren't the very latest, but if they need to track the point releases then that can easily get out of date.

Would it make sense to have a "bleeding-edge" url  that always tracks the very latest, including point releases?

---

### 评论 #3 — saadrahim (2023-03-17T14:38:24Z)

People should use latest for now. That's the best we can recommend to end users. "bleeding-edge" is needed.

---

### 评论 #4 — nartmada (2024-04-21T14:08:18Z)

Issue has been fixed with ROCm 6.1.0.

https://repo.radeon.com/rocm/apt/
![image](https://github.com/ROCm/ROCm/assets/144284448/bf43506d-443f-476d-b22d-e50670963e05)


---
