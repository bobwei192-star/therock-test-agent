# README.md lists the wrong kernel versions for Ubuntu

> **Issue #1707**
> **状态**: closed
> **创建时间**: 2022-03-17T23:35:55Z
> **更新时间**: 2024-01-23T21:50:11Z
> **关闭时间**: 2024-01-23T21:50:11Z
> **作者**: earlruby
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1707

## 描述

Ubuntu 18.04.4 LTS shipped with a 5.3 kernel. A 5.4 kernel is available in the HWE package. See https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes#Updated_Packages

Ubuntu 20.04 LTS shipped with a 5.4 kernel. A 5.8 kernel is available in the HWE package. See https://wiki.ubuntu.com/FocalFossa/ReleaseNotes#Linux_Kernel

I created a branch with the correction:

```
-| Ubuntu 20.04.3 | 5.8.0 LTS / 5.11 HWE |
-| Ubuntu 18.04.5 [5.4 HWE kernel] | 5.4.0-71-generic |
+| Ubuntu 20.04 | 5.4 LTS / 5.8 HWE |
+| Ubuntu 18.04.4 | 5.3 LTS / 5.4 HWE |
```

... but the repo won't allow me to submit a branch for an MR.

---

## 评论 (2 条)

### 评论 #1 — Rmalavally (2022-03-17T23:40:31Z)

Thank you for the feedback, @earlruby. We will have our QA and Deployment teams review your recommended changes and update our documentation accordingly. 

AMD ROCm Documentation Team

---

### 评论 #2 — abhimeda (2024-01-23T21:50:08Z)

@earlruby Hi, it seems that this has been solved a long time ago. Closing this now.

---
