# Native support for ROCm in Hadoop Yarn

> **Issue #1391**
> **状态**: closed
> **创建时间**: 2021-02-22T10:38:19Z
> **更新时间**: 2023-04-26T10:08:38Z
> **关闭时间**: 2023-04-26T10:08:38Z
> **作者**: elukey
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1391

## 描述

Hi everybody,

In the Hadoop 3.x ecosystem there seems to be space for a native non-Nvidia GPU support, see:

https://issues.apache.org/jira/browse/YARN-10225
https://issues.apache.org/jira/browse/YARN-8891

From Hadoop 3.3.0 (still not released) it will be possible to create custom jars to support various devices, like new GPUs, something that for the moment is limited to Nvidia cards. I think that it would be great to have an official Hadoop plugin maintained by ROCm devs, that eventually may end up in Hadoop's main repo?

Hadoop users can still target ROCm GPUs via solutions like https://github.com/criteo/tf-yarn, but the Yarn scheduler will still be unware of GPUs as resources, so not really a fine grained solution. I'd be happy to help in case needed, this seems to be a very interesting project to reduce the monopoly from Nvidia :)

Thanks in advance!

---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2021-02-23T13:00:30Z)

Thanks @elukey for reaching us.
I will get some information on this and update you asap.

---

### 评论 #2 — elukey (2021-03-08T11:55:56Z)

Hi @ROCmSupport, any news? :)

---

### 评论 #3 — ROCmSupport (2021-03-08T15:19:32Z)

Hi @elukey 
We are going to discuss on this today, I hope I will share an update on this soon.
Thank you.

---

### 评论 #4 — elukey (2021-03-21T18:00:34Z)

@ROCmSupport gentle ping :)

---

### 评论 #5 — ROCmSupport (2021-03-22T06:36:25Z)

Thanks @elukey for the ping.
As per out last discussion, this will be seen as a P2 item. Anyway I am going to get some update by today/tomorrow, will reach you asap.
Thank you.

---

### 评论 #6 — elukey (2021-10-07T12:38:44Z)

@ROCmSupport any news :)

---

### 评论 #7 — ROCmSupport (2021-10-11T08:59:59Z)

Hi @elukey 
No update so far.
We are internally discussing on this feasibility and etc.
I will update this thread once I get some information. Thank you.

---
