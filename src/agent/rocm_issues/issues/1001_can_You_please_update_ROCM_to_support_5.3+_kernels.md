# can You please update ROCM to support 5.3+ kernels?

> **Issue #1001**
> **状态**: closed
> **创建时间**: 2020-01-17T22:11:09Z
> **更新时间**: 2021-04-19T12:59:12Z
> **关闭时间**: 2021-04-19T12:59:11Z
> **作者**: witeko
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1001

## 描述

ubuntu 18.04 has started to update to 5.3

---

## 评论 (6 条)

### 评论 #1 — cryptomilk (2020-02-01T11:15:32Z)

Are you sure that this isn't a bug in Ubuntu?

I'm running

`Linux magrathea 5.4.14-1-default #1 SMP Thu Jan 23 08:54:47 UTC 2020 (fc4ea7a) x86_64 x86_64 x86_64 GNU/Linux`

and it works just fine with ROCm 2.10.0.

---

### 评论 #2 — witeko (2020-02-01T14:08:21Z)

Im talking about the DKMS driver, its currently restricted to kernels up to 5.0,
Your are probably using the "upstream kernel" driver which doesnt suit me.

---

### 评论 #3 — rkothako (2020-02-06T09:17:46Z)

We will have ROCm 3.1 which supports 5.3 kernel also.

---

### 评论 #4 — witeko (2020-02-06T20:45:52Z)

@rkothako thx :)

---

### 评论 #5 — ddobreff (2020-02-12T11:04:51Z)

> We will have ROCm 3.1 which supports 5.3 kernel also.

Latest LTS kernel is 5.4. Is it going to be supported too?

---

### 评论 #6 — ROCmSupport (2021-04-19T12:59:11Z)

Thanks for reaching out.
This issue is fixed and not observed with the latest ROCm 4.1.
Hence recommend you to try with the same.
Feel free to open a new issue, for any, for quick resolution.
Thank you.

---
