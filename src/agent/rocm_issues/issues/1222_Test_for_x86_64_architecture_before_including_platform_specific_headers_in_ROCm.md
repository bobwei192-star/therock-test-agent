# Test for x86_64 architecture before including platform specific headers in ROCm

> **Issue #1222**
> **状态**: closed
> **创建时间**: 2020-09-17T21:52:43Z
> **更新时间**: 2021-06-02T10:02:11Z
> **关闭时间**: 2021-06-02T10:02:11Z
> **作者**: sameershende
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1222

## 描述

amd64 platform is assumed in rocm_bandwidth_test/hsatimer.hpp and it includes a platform specific file without guards to check for the platform: 
#include <x86intrin.h>

It also uses __rtdscp and when an alternative timestamp function is used with guards elsewhere in the code. This check should be performed at other locations where __rtdscp is used. 
In rocm-smi, DEBIAN/control also hardcodes Architecture: amd64 in DEBIAN/control



---

## 评论 (8 条)

### 评论 #1 — baryluk (2020-09-22T22:51:41Z)

Yes, you are right.

I think personally, this code doesn't really need to use `rtdscp` at all. Using `gettimeofday(2)`, or `clock_gettime(2)` with `CLOCK_MONOTONIC` is going to be equally good and more portable across archs. Unless it is trying to measure latency of super low values (<500ns), there is no need for rtdscp. As the name suggest the test measures bandwidth.

I didn't test ROCm on non-amd64 arch, but I am definitively going to (aarch64, and possibly power9). I had enough issues on amd64 already.


---

### 评论 #2 — ROCmSupport (2020-12-16T05:41:10Z)

Thanks @sameershende for reaching out.
I will check and get back asap on this issue.
Thank you.

---

### 评论 #3 — rerrabolu (2021-01-29T17:40:10Z)

All the repo for rocm_bandwidth_test [](https://github.com/RadeonOpenCompute/rocm_bandwidth_test) has an update in this regard.

Implementation has moved away from using __rtdscp timers. You can find the change submitted a while ago - eae85ad52d2eb7c336a9198542a5.

For one or more reasons this change was not picked up by public release of ROCm stack.


---

### 评论 #4 — ROCmSupport (2021-02-01T05:38:29Z)

Thanks @rerrabolu for the update.
Can you please make sure that new change will be picked up for the next upcoming ROCm release?
Thank you.

---

### 评论 #5 — cfreehill (2021-02-01T18:15:26Z)

@sameershende Thanks for the feedback.

> In rocm-smi, DEBIAN/control also hardcodes Architecture: amd64 in DEBIAN/control

I had to do some research on this. Mainly, I'm looking at this: https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-architecture.  I'm not aware of and don't recall  any CPU architecture specific code in the rocm_smi library code. Therefore, I think "amd64" should be changed to "any". Let me know if you disagree.


---

### 评论 #6 — ROCmSupport (2021-04-08T11:07:23Z)

Hi @sameershende 
Can you please check this with the latest ROCm 4.1 and update.
Thank you.

---

### 评论 #7 — ROCmSupport (2021-05-07T09:58:15Z)

Hi @sameershende 
As the changes are merged, request you to check on the latest 4.2 code.
Thank you.

---

### 评论 #8 — ROCmSupport (2021-06-02T10:02:11Z)

As there is no response for more than a month, considering that issue is fixed.
Am closing this now as the changes are already pushed.
Thank you.

---
