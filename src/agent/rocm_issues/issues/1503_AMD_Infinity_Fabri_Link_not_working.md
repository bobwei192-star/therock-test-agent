# AMD Infinity Fabri Link not working 

> **Issue #1503**
> **状态**: closed
> **创建时间**: 2021-06-24T10:28:45Z
> **更新时间**: 2021-06-24T14:57:42Z
> **关闭时间**: 2021-06-24T14:57:42Z
> **作者**: question12345
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1503

## 描述

Hi everybody, 

here is my problem:

I have 2 gpu MI100 in my server and they are seen by the system:

========================== Link Type between two GPUs ==========================
GPU0 GPU1
GPU0 0 PCIE
GPU1 PCIE 0

*******************************

Instead, If I connect them with through a bridge (AMD Infinity Fabri Link) then the system doesn't see them anymore at all.

The bridge is a 4 slots bridge, but I have only 2 MI100, so, is it possible that having a 4 slots bridge for only 2 MI100 then it does not work?

regards

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-06-24T14:57:42Z)

Hi @question12345 
Thanks for reaching out.

Its not architect-ed to work like that.
The bridge tells the firmware that its a 4p hive.

The routing on the bridge is static. It expects to find a GPU in every slot. The PSP firmwares of all GPUs need to coordinate during boot-up. There is some HW topology ID that the firmwares get from the bridge. If you have a 4P bridge, they expect to fine 3 peer GPUs to synchronize with.

Hope this helps.
Thank you.

---
