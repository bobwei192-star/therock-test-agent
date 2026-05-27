# rocm.gpg.key sha1sum doesn't match.

> **Issue #498**
> **状态**: closed
> **创建时间**: 2018-08-10T18:31:39Z
> **更新时间**: 2018-08-10T21:33:25Z
> **关闭时间**: 2018-08-10T21:33:25Z
> **作者**: soulhunter
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/498

## 描述

Hello,

As I was installing updates I got a message about expired key.  Decided to fetch the new key:

wget http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key

But sha1sum doesn't match with that document:

f7f8147431c75e505c58a6f3a3548510869357a6  rocm.gpg.key

Documented sha1sum is:

f0d739836a9094004b0a39058d046349aacc1178 rocm.gpg.key

So, either documents are outdated (most likely), or the key is not the one it should be.

Thanks!


---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2018-08-10T19:58:06Z)

As documented on the [main ROCm README page](https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md), the correct sha1sum is `f7f8147431c75e505c58a6f3a3548510869357a6 rocm.gpg.key`.

If you were looking at the listing on the [rocm.github.io installation page](https://rocm.github.io/install.html) or on [the readthedocs site](http://rocm-documentation.readthedocs.io/en/latest/Installation_Guide/Installation-Guide.html#debian-repository-apt), I have updated both of those to include the new, correct, key.

Were you able to find the old key anywhere else? Thanks, and sorry for the difficulties this caused.

---

### 评论 #2 — soulhunter (2018-08-10T21:33:25Z)

No, just those sites (and I could've sworn it was the old one on the README page as well, but anyway).  Thanks for updating that!



---
