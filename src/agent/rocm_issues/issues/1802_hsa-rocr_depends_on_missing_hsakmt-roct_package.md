# hsa-rocr depends on missing hsakmt-roct package

> **Issue #1802**
> **状态**: closed
> **创建时间**: 2022-08-30T00:42:28Z
> **更新时间**: 2023-02-24T21:55:30Z
> **关闭时间**: 2023-02-24T21:55:29Z
> **作者**: JoniSt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1802

## 负责人

- frepaul

## 描述

Hi,

The `hsa-rocr` DEB package that ships in the 5.2.3 apt repository lists `hsakmt-roct` as one of its dependencies; however, the latter package doesn't exist in the 5.2.3 repo. (The last repo that contains it is 4.3.1)

This seems a little broken to me. Is the dependency list of `hsa-rocr` wrong, maybe?

Thanks,
Jonathan

---

## 评论 (5 条)

### 评论 #1 — saadrahim (2022-09-16T17:49:33Z)

@frepaul will be able to comment on this issue.

---

### 评论 #2 — frepaul (2022-09-16T18:01:16Z)

@JoniSt . We are take care of this in our next release. 

Thanks for reporting.

---

### 评论 #3 — frepaul (2022-09-16T18:31:29Z)

Wanted to clarify one more detail here. Since we were transitioning hsakmt-roct to hsakmt-roct-dev, currently hsakmt-roct-dev provides both and hence installation of hsa-rocr should not have any issues.

---

### 评论 #4 — JoniSt (2022-09-16T18:37:08Z)

Oh, I just checked again and you're right, that is indeed the case! I'm not sure why exactly APT insists on installing the missing hsakmt-roct package on my system... When I install hsakmt-roct-dev manually before the rest of the packages, it works just fine.

Thank you very much!

I'll leave it up to you if you want to close this issue immediately or after the next release.

---

### 评论 #5 — kentrussell (2023-02-24T21:55:29Z)

Closing as fixed

---
