# Not possible to build ROCm from source code

> **Issue #1238**
> **状态**: closed
> **创建时间**: 2020-09-23T15:49:08Z
> **更新时间**: 2020-10-14T12:31:58Z
> **关闭时间**: 2020-10-14T12:31:58Z
> **作者**: niso
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1238

## 描述

System information

    OS Platform and Distribution (e.g., Linux Ubuntu 16.04): Debian buster
    Python version: 3.7
    ROCm/MIOpen version: 3.8
    GPU model and memory: Vega 64

Describe the problem
Core components nor metapackages are not present when using the instructions below:
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#downloading-the-rocm-source-code

Since the new deb packages depend on python 3.8, you have blocked the possibility to all Debian buster users.
Since you don't have older versions in your repository, we can't downgrade to 3.7.
Since your instructions to build the library from source are not working we are totally stuck.

    Do we have any way (apart from reinstall a new OS) to have a working system?


---

## 评论 (4 条)

### 评论 #1 — Rmalavally (2020-09-23T16:06:36Z)

Thank you for reaching out and bringing the issue to our attention.

We have passed on the relevant information you have shared to our team and will keep you updated once we hear from them.

AMD ROCm Documentation Team

---

### 评论 #2 — baryluk (2020-09-26T21:00:35Z)

You can modify the control files to use python3.7 libraries. It should work. Or update to Debian testing (bullseye).

Debian is not officially supported, but another possibility is to add `python3.7 | python3.8` instead of just `python3.8` where required. And when using `python3 >= xx", use `python3 >= 3.7.0`. I don't guarantee it will work with python3.7, as there are some syntax and ABI extensions present in 3.8 that are not available in 3.7. But I expect no code in ROCm repos really use these new syntax features (like assignment expressions, positional-only parameters, vectorcall ABI, final methods, typed dicts, etc), so there is high chance of this working.


---

### 评论 #3 — niso (2020-10-07T08:23:15Z)

Hi @baryluk , thanks for the answer.
I ended up installing Ubuntu in the testing box.

I consider the issue is still open but it does not affect me anymore.

---

### 评论 #4 — rkothako (2020-10-14T08:57:20Z)

Hi @niso 
As ROCm does not support Ubuntu 16.xx anymore as per documentation mentioned @ https://github.com/RadeonOpenCompute/ROCm#list-of-supported-operating-systems, can you please close this ticket, if its not relevant anymore.
Thank you.


---
