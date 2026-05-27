# roc-obj-extract consumes stdin even when arguments are specified.

> **Issue #1755**
> **状态**: closed
> **创建时间**: 2022-06-16T21:20:32Z
> **更新时间**: 2024-01-25T02:42:57Z
> **关闭时间**: 2024-01-25T02:42:57Z
> **作者**: bigtrak
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1755

## 描述

roc-obj-extract consumes stdin due to a coding error.    While it works interactively, if you 
script roc-object-extract, it  will try consuming stdin, and be confused by the input.

The fix to this is to check for argv having arguments, and NOT push stdin before argv in 
this case.     This is the patch I used to not read stdin when arguments are present after 
option parsing.   If you pipe roc-obj-ls to the modified roc-obj-extract with a  awk '{print $3;}' 
to select the URI, it works in that mode as well.

[roc-obj-extract.patch.txt](https://github.com/RadeonOpenCompute/ROCm/files/8922431/roc-obj-extract.patch.txt)


---

## 评论 (3 条)

### 评论 #1 — nartmada (2023-12-19T04:06:42Z)

Hi @bigtrak, thanks for your input.  Please close the ticket if no further action is needed.  Thanks.

---

### 评论 #2 — nartmada (2023-12-19T04:07:55Z)

Also please check latest ROCm 6.0 to see if your issue has been fixed.  Thanks.

---

### 评论 #3 — nartmada (2024-01-25T02:42:57Z)

Closing the ticket.  @bigtrak, please re-open if the issue still exists with latest ROCm.  Thanks.

---
