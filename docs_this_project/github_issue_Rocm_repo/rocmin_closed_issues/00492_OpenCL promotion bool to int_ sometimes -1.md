# OpenCL promotion bool to int: sometimes -1

- **Issue #:** 492
- **State:** closed
- **Created:** 2018-08-06T11:05:06Z
- **Updated:** 2018-08-08T23:37:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/492

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
