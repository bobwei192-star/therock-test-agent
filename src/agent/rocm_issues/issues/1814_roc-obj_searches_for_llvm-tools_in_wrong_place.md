# roc-obj searches for llvm-tools in wrong place

> **Issue #1814**
> **状态**: closed
> **创建时间**: 2022-09-29T13:27:26Z
> **更新时间**: 2024-02-09T15:22:59Z
> **关闭时间**: 2024-02-09T15:22:59Z
> **作者**: Melirius
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1814

## 描述

Using roc-obj in current 5.2.3 gives an error
``` shell
~/$ /opt/rocm/bin/roc-obj -d test
error: could not find llvm-objdump in /opt/rocm-5.2.3/bin /opt/rocm-5.2.3/bin/../../llvm/bin or PATH
```

Inspection shows that the search path is wrong, it should be `/opt/rocm-5.2.3/bin/../llvm/bin`. Line 140
``` shell
  for dir in "$BASE_DIR" "${HIP_CLANG_PATH:-"$BASE_DIR/../../llvm/bin"}"; do
```
of `roc-obj` script should be fixed to 
``` shell
  for dir in "$BASE_DIR" "${HIP_CLANG_PATH:-"$BASE_DIR/../llvm/bin"}"; do
```
After such a change it runs smoothly.


---

## 评论 (2 条)

### 评论 #1 — nartmada (2024-02-02T22:53:52Z)

Hi @Melirius, please check latest ROCm6.0.2 to see if your issue still exists.  Please close the ticket if your issue has been fixed.  Thanks.

---

### 评论 #2 — nartmada (2024-02-09T15:22:59Z)

Closing the ticket as no response from @Melirius.  Please re-open the ticket if your issue still exists with latest ROCm 6.0.2.  Thanks.

---
