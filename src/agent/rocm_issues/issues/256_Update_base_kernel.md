# Update base kernel?

> **Issue #256**
> **状态**: closed
> **创建时间**: 2017-11-17T09:20:35Z
> **更新时间**: 2018-09-16T20:28:07Z
> **关闭时间**: 2018-09-16T20:28:07Z
> **作者**: madscientist159
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/256

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Would it be possible to get the ROCK kernel updated to use Linux 4.13 as its base?  We need to use POWER9 with ROCm due to the PCIe atomic support, but Linux 4.11 is unusable on our POWER9 boxes.

Thanks!

---

## 评论 (9 条)

### 评论 #1 — gstoner (2017-11-17T19:52:14Z)

Next release moves to 4.13 Linux Kernel 

---

### 评论 #2 — madscientist159 (2017-11-17T22:52:26Z)

@gstoner Excellent!  We had to put the Vega card into an old Windows PC to get OpenCL, and it is overall a very poor experience compared to our normal Linux systems (bad enough that without this pending Linux support we'd give up on Vega entirely for the time being).

Any idea of when the initial revup to 4.13 might be up here on GitHub (alpha quality is fine, need to run POWER9 tests)?

---

### 评论 #3 — briansp2020 (2017-11-17T23:12:44Z)

@gstoner 
When will ROCm 1.7 come out...
Give it to me now...

BTW, will you release TensorFlow 1.4 along with ROCm 1.7? If not when do you think you will have 1.4?

---

### 评论 #4 — delbabrour (2017-12-16T16:42:26Z)

+1
Update to at **least linux kernel 4.14 or 4.15 rc1** to fix the issue with most Mobo like MSI z270-A Pro or H110 or even h81 i got all errors when booting with custom vBios GPUs RX570 :(

it is identified as bug in linux kernel and need quick update 

**Kernel bug**  here https://bugs.freedesktop.org/show_bug.cgi?id=100443

---

### 评论 #5 — blisskidd (2018-01-05T19:47:12Z)

Can we get something for *CURRENT* kernels please?
I'm on 4.14.11.
I can do 4.15 if that helps.
4.13 = dead now.

---

### 评论 #6 — Cyclic3 (2018-03-10T12:36:41Z)

Has there been any movement on this?

---

### 评论 #7 — shimmervoid (2018-04-02T04:30:17Z)

Kernel 4.16 is here, maybe some movement here?

---

### 评论 #8 — kentrussell (2018-09-14T12:42:43Z)

The 1.9 release is based on 4.15, so this should help. Let us know (code available on github, apt repo should be updated later today)

---

### 评论 #9 — jlgreathouse (2018-09-16T20:28:07Z)

ROCm 1.9.0 should with upstream kernels now, so I'm going to close this particular issue. If other problems arise, please start an issue for them specifically. Thanks.

---
