# Please remove Recommends: gcc-multilib, g++-multilib from openmp-extras package

> **Issue #1319**
> **状态**: closed
> **创建时间**: 2020-12-04T01:50:36Z
> **更新时间**: 2020-12-09T09:24:15Z
> **关闭时间**: 2020-12-09T09:24:15Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1319

## 描述

ROCm 3.10

```
$ apt-cache show openmp-extras3.10.0 | grep Recommends
Recommends: gcc, g++, gcc-multilib, g++-multilib
$
```

This is unnecessary. And AFAIK doesn't enhance the package in anyway.

Use instead:

```
Suggests: gcc, g++
```


that is without `gcc-multilib` (which does for example conflict with `gcc-10-i686-linux-gnu` for cross-compiling), and downgrade to `Suggests`.

There is nothing in this package that interact with GCC in anyway, nor is GCC interacting with anything in this package.



---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2020-12-04T09:15:10Z)

Thanks @baryluk for reaching out.
I am working with OMP team on this, will keep you posted.
Thank you.

---

### 评论 #2 — ROCmSupport (2020-12-09T08:55:40Z)

Update on this:
Fix is ready and will be pushed soon. Most likely it will be part of ROCm 4.1.
Thank you.

---

### 评论 #3 — baryluk (2020-12-09T09:24:15Z)

Thank you for addressing even small issues like that!

It is appreciated.

---
