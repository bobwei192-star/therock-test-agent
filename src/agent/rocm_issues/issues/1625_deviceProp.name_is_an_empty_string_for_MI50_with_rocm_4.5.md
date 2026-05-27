# deviceProp.name is an empty string for MI50 with rocm 4.5 

> **Issue #1625**
> **状态**: closed
> **创建时间**: 2021-11-22T22:07:50Z
> **更新时间**: 2024-02-09T04:36:25Z
> **关闭时间**: 2024-02-09T04:36:25Z
> **作者**: sbalint98
> **标签**: Verified Issue, 4.5.0
> **URL**: https://github.com/ROCm/ROCm/issues/1625

## 标签

- **Verified Issue** (颜色: #0052cc)
- **4.5.0** (颜色: #500CDC)

## 负责人

- gargrahul

## 描述

In the case of using rocm 4.5 the `deviceProp.name` string does not contain the expected device name. 

The following code can reproduce the issue:

```
#include<iostream>
#include <hip/hip_runtime.h>
int main(){
  hipDeviceProp_t deviceProp;
  hipGetDeviceProperties(&deviceProp, 0);
  std::cout << deviceProp.name << std::endl;
}
```
This behaviour has been observed on a system with an MI50 accelerator

---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2021-11-23T05:14:57Z)

Thanks @sbalint98 for reaching out.
I certainly understood the problem.
We already found this issue internally, tracking it and fix is in progress. I will share further update soon.
Thank you.


---

### 评论 #2 — lanwatch (2022-05-09T13:51:31Z)

Same issue here on MI100 rocm 5.1.1

---

### 评论 #3 — awehrfritz (2022-05-11T14:30:21Z)

I observed this issue as well on my local system with a Radeon Vega card. Any update on this @ROCmSupport?

---

### 评论 #4 — wyphan (2022-07-15T16:53:54Z)

Same issue still happens with ROCm 5.2.0 with MI50, MI100, and MI210.

---

### 评论 #5 — doit-op (2022-10-21T01:06:03Z)

This is still an issue with MI210's on 5.2.3.

---

### 评论 #6 — keryell (2022-11-30T01:47:26Z)

Is this still an issue with the latest ROCm 5.3.3?

---

### 评论 #7 — nartmada (2024-02-09T04:36:25Z)

Closing this ticket as it is stale.  Furthermore, an internal developer has confirmed issue has been fixed for MI250 and MI300 in ROCm6.0.0.  @sbalint98, please re-open the ticket if you are still seeing empty string.  Thanks.

---
