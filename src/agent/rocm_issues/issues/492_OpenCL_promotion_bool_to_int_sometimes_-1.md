# OpenCL promotion bool to int: sometimes -1

> **Issue #492**
> **状态**: closed
> **创建时间**: 2018-08-06T11:05:06Z
> **更新时间**: 2018-08-08T23:37:08Z
> **关闭时间**: 2018-08-08T23:37:08Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/492

## 描述

ROCm 1.8.2, Ubuntu 18.04, Vega64.
```
KERNEL(256) test(global ulong2 *data) {
  data[get_global_id(0)] = true;
 }
```
```
KERNEL(256) test(global ulong2 *data) {
  data[get_global_id(0)] = (true == 1);
 }
```
Consider the two above kernels. I think OpenCL dictates that bool true is promoted to int 1. This is confirmed by (true == 1) evaluating to true. Yet: the first kernel fills the buffer with the int value -1(!) while the second fills it with 1. This is confirmed in ISA diff:
```
<       v_mov_b32_e32 v1, -1                                       // 000000003D18: 7E0202C1
<       v_mov_b32_e32 v4, v1                                       // 000000003D1C: 7E080301
---
>       v_mov_b32_e32 v1, 1                                        // 000000003D18: 7E020281
>       v_mov_b32_e32 v2, 0                                        // 000000003D1C: 7E040280
```


---

## 评论 (2 条)

### 评论 #1 — b-sumner (2018-08-08T20:51:14Z)

Apparently, true == 1 is an int not a bool.  Assigning a bool to a vector, or comparing vectors results in a same sized integer vector whose bits are all set or all not set.  Assigning a scalar int 1 to a vector results in a vector whose elements are all 1.   This explains your observations I believe.

---

### 评论 #2 — preda (2018-08-08T23:37:08Z)

Thanks. Indeed the OpenCL spec seems to say:
1. scalar "==" produces an int "1" when true.
2. boolean "true" conversion to a vector must set all bits to 1 (i.e. -1).
So this seems to be the expected behavior according to the spec.

---
