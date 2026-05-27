# Tahiti GCN1.0/GFX6 card support

> **Issue #374**
> **状态**: closed
> **创建时间**: 2018-03-26T18:13:11Z
> **更新时间**: 2020-01-04T17:22:42Z
> **关闭时间**: 2018-05-02T01:51:50Z
> **作者**: talentoscope
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/374

## 描述

Is there any way to get ROCm working on my R9 280X card, either through ROCm directly or via some other OpenCL "thing"?
I want to use TensorFlow on the GPU I have, and it is still a decent card, I'm surprised that there's not anything more about support for older cards in any documentation. Is that because they're not supported *at all* and I'm supposed to buy a new one ( :( ), or has it just not been tested, or something else?

I know this isn't an issue per se, but if these Southern Island cards (or even just the 280X) are supported, it would be helpful to have something about it in the documentation, or even just some caveats to get it working.

Thank you :)

---

## 评论 (5 条)

### 评论 #1 — pmc01 (2018-03-27T01:24:09Z)

According to [gstoner](https://github.com/RadeonOpenCompute/ROCm/issues/353#issuecomment-372121101) it will only work on W9100 or newer. I mentioned some boot settings for Southern Islands in that thread, but after reviewing the ROCm amdkfd driver, it does not include support for GCN1.0 cards. If you want to add support for TAHITI then amdkfd is a good place to start.

---

### 评论 #2 — Mandrewoid (2018-03-28T22:52:37Z)

@xteejx Have you seen Hugh Perkins' tf-coriander? https://github.com/hughperkins/tf-coriander
or https://github.com/plaidml/plaidml
Might be worth a look.
I never tried coriander, but plaidml ran on my radeon HD 7950

---

### 评论 #3 — talentoscope (2018-03-29T09:28:08Z)

Will have a look at those, thanks!


---

### 评论 #4 — l29ah (2020-01-04T16:28:20Z)

Do GFX6 cards lack some necessary hardware features for amdkfd support?

---

### 评论 #5 — talentoscope (2020-01-04T17:22:42Z)

This report is closed. Ask a question in a forum or on IRC or something 

---
