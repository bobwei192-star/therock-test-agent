# Segmentation Fault Pytorch  RX 6700xt

> **Issue #1931**
> **状态**: closed
> **创建时间**: 2023-03-12T18:32:59Z
> **更新时间**: 2024-05-27T18:57:42Z
> **关闭时间**: 2024-05-27T18:57:42Z
> **作者**: mpourasa
> **标签**: application:pytorch
> **URL**: https://github.com/ROCm/ROCm/issues/1931

## 标签

- **application:pytorch** (颜色: #bfdadc)

## 描述

Hi,

I am trying to run a test for my RX 6700xt but I  face many problems.
I tried issue#1686 and 1687 but I was not able to fix them.

I get an error of segmentation faul when I am trying to do run a test inside a docker image:

https://www.youtube.com/watch?v=HwGgzaz7ipQ

The other problem is that after having installed rocm and pytorch terminal returns cuda available = false. ( in docker image returns true)

I have used both Ubuntu 22 and 20 but still have the same proble. Is pytorch compatible only with 5.2 rocm?

Also, in the docker image it returns cuda available but does not run the test.

Can anybody help?

---

## 评论 (5 条)

### 评论 #1 — tedtroxell (2023-03-20T17:43:05Z)

Do you know if that version supports the 6700 xt? I have a 7900 xtx, which isn't supported and I can't use the gpu without it segfaulting, I would guess that it's a driver mismatch.

---

### 评论 #2 — mpourasa (2023-03-25T13:24:11Z)

I followed the example below closely and got the same error again:


https://www.youtube.com/watch?v=IQSvz6jBCis&t=1072s

RX6700xt is compatible with the versions of the example

---

### 评论 #3 — hongxiayang (2023-12-05T20:48:12Z)

Looks like your gpu type is not in the official supported list:
https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html

Can you run 
```
rocminfo | grep gfx
```


---

### 评论 #4 — mpourasa (2023-12-20T19:00:08Z)

> Looks like your gpu type is not in the official supported list: https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html
> 
> Can you run
> 
> ```
> rocminfo | grep gfx
> ```

According to the following guide RX 6700 XT should be suffecient.

https://www.videogames.ai/2022/09/01/RX-6700s-Machine-Learning-ROCm.html

---

### 评论 #5 — ppanchad-amd (2024-05-10T18:00:33Z)

@mpourasa RX6700 XT is not officially supported in our latest ROCm 6.1.1. Thanks!

---
