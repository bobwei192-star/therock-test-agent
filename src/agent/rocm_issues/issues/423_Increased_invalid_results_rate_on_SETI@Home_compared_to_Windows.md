# Increased invalid results rate on SETI@Home compared to Windows

> **Issue #423**
> **状态**: closed
> **创建时间**: 2018-05-22T12:28:14Z
> **更新时间**: 2021-01-05T10:56:54Z
> **关闭时间**: 2021-01-05T10:56:54Z
> **作者**: ghost
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/423

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

A user on the SETI@Home forums has reported an increased a significantly higher rate of inconclusive and invalid SETI@Home workunits on their system using an RX Vega 64 when running Linux + ROCm 1.8 compared to the same hardware on Windows (to be honest, that system has 0 invalids on Windows compared to quite a few on Linux).

[Link to thread](https://setiathome.berkeley.edu/forum_thread.php?id=82949)

The host using Linux + ROCm [Link](https://setiathome.berkeley.edu/show_host_detail.php?hostid=8365846) (Oddly enough, here the GPU is identified as AMD Device 687f instead of AMD Radeon RX Vega)
The host using Windows [Link](https://setiathome.berkeley.edu/show_host_detail.php?hostid=8507353)

Don't really have much diagnostic info, but something seems to be messing with the computation compared to Windows - I think this might be worth looking at.




---

## 评论 (6 条)

### 评论 #1 — gstoner (2018-06-03T13:35:21Z)

I having some look into this 

---

### 评论 #2 — benjaminjscott (2019-01-04T21:44:57Z)

I am having the same problem, but maybe worse, with ROCm 2.0. With version 1.9 I have only occasional invalid work units, but with 2.0 I am flooded with inconclusives  and have many invalids. This happened under both Debian and Ubuntu.

---

### 评论 #3 — Ricks-Lab (2019-01-04T23:08:28Z)

> I am having the same problem, but maybe worse, with ROCm 2.0. With version 1.9 I have only occasional invalid work units, but with 2.0 I am flooded with inconclusives and have many invalids. This happened under both Debian and Ubuntu.

Hi Ben,  I had been able to reproduce this problem consistently with specific work units when I first reported the problem.  It would be interesting to see if the short WUs included in the latest benchmark script I released would also reproduce the problem.  You can verify this by running benchMT --std_signals.  I don't currently have a system configured with ROCm.

---

### 评论 #4 — Ricks-Lab (2019-03-26T06:54:37Z)

I just installed ROCm 2.2 and found that this is still an issue.  It produces invalid results for all reference work units.  I tried with a full install and openCL only install.

---

### 评论 #5 — Ricks-Lab (2019-10-19T03:32:54Z)

I have installed ROCm 2.9.6 on a new build which is a Epyc 7702p and a Radeon VII GPU on Ubuntu with Kernel 5.0.0-31 and still gives invalid results for SETI, where the standard amdgpu package gives appropriate results.

---

### 评论 #6 — ROCmSupport (2021-01-05T10:56:53Z)

Hi @corecodeshredder 
As its very old (its around ~2 years old), closing this issue.
Request you to try with ROCm 4.0 and open a new issue, if any, for quick response.
Thank you.

---
