# Fails to download source for 3.8.x

> **Issue #1225**
> **状态**: closed
> **创建时间**: 2020-09-21T20:38:38Z
> **更新时间**: 2020-10-08T05:42:43Z
> **关闭时间**: 2020-10-08T05:42:43Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1225

## 描述

The following url claims, to download the 3.8.x but it does not work:

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#getting-the-rocm-source-code
...
Downloading the ROCm Source Code
The following example shows how to use the repo binary to download the ROCm source code. If you choose a directory other than ~/bin/ to install the repo, you must use that chosen directory in the code as shown below:

mkdir -p ~/ROCm/
cd ~/ROCm/
~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-3.8.x
repo sync
...

run from linux terminal failed:
Downloading manifest from https://github.com/RadeonOpenCompute/ROCm.git
fatal: Couldn't find remote ref refs/heads/roc-3.8.x
manifests:
fatal: Couldn't find remote ref refs/heads/roc-3.8.x

fatal: Couldn't find remote ref refs/heads/roc-3.8.x
manifests:
fatal: Couldn't find remote ref refs/heads/roc-3.8.x



---

## 评论 (5 条)

### 评论 #1 — Rmalavally (2020-09-21T23:40:55Z)

Thank you for reaching out. 

Refresh the browser and try again.

 If you are unable to find the information you need, please contact us.

AMD ROCm Documentation Team



---

### 评论 #2 — gggh000 (2020-09-22T23:17:57Z)

not sure waht changed as a browser refresh but it is appearing to work. thx., 

---

### 评论 #3 — Rmalavally (2020-09-22T23:19:35Z)

Thank you for the positive feedback. We are glad it worked!!

AMD ROCm Documentation Team

---

### 评论 #4 — baryluk (2020-09-26T21:04:07Z)

Works for me. Maybe github was down for a moment?


---

### 评论 #5 — gggh000 (2020-10-08T05:42:43Z)

thx, i think this can be closed.

---
