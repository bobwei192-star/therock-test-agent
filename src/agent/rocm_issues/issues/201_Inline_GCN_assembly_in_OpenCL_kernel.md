# Inline GCN assembly in OpenCL kernel ?

> **Issue #201**
> **状态**: closed
> **创建时间**: 2017-09-07T23:40:20Z
> **更新时间**: 2018-05-12T14:24:46Z
> **关闭时间**: 2018-05-12T14:24:46Z
> **作者**: boxerab
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/201

## 标签

- **Question** (颜色: #cc317c)

## 描述

Is this possible on ROCm ? I would like to use the new cross-lane functionality.

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-09-08T03:36:08Z)

Yes

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Aaron Boxer <notifications@github.com>
Sent: Thursday, September 7, 2017 6:40:23 PM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: [RadeonOpenCompute/ROCm] Inline GCN assembly in OpenCL kernel ? (#201)


Is this possible on ROCm ? I would like to use the new cross-lane functionality.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/201>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuWpDIJ_ve4ipAn8335NhLbQ0rRlFks5sgH7lgaJpZM4PQhYp>.


---

### 评论 #2 — boxerab (2017-09-08T04:18:27Z)

Thanks. Is there any documentation on how to do this? I would like to write a custom inclusive scan
method using cross-lane commands - currently I do this with LDS, but registers would be better.

---

### 评论 #3 — boxerab (2017-09-08T04:20:01Z)

Instead of scan across entire work group (there is OpenCL 2.0 method for this) I would like to scan over each quarter wave.

---

### 评论 #4 — preda (2017-09-18T13:11:02Z)

Here you may find an example:
https://github.com/zawawawa/gatelessgate/blob/master/Core/binary-kernel/equihash.cl
(not tested though)

---

### 评论 #5 — boxerab (2017-09-18T13:26:51Z)

Thanks, Mihai. It would also be nice for AMD to provide some examples as well.

---
