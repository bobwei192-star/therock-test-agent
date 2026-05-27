# GPG key is served insecurely

> **Issue #64**
> **状态**: closed
> **创建时间**: 2016-12-31T23:18:26Z
> **更新时间**: 2017-12-17T19:05:31Z
> **关闭时间**: 2017-04-19T11:22:22Z
> **作者**: anewusername
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/64

## 描述

The GPG key for the debian repository is served over an insecure connection (HTTP) and can be trivially changed using a man-in-the-middle attack.

---

## 评论 (6 条)

### 评论 #1 — victoredwardocallaghan (2017-04-19T11:01:25Z)

hehe, I was about to post the same issue but figured it would be a duplicate as surely someone noticed this too! ;)

---

### 评论 #2 — victoredwardocallaghan (2017-04-19T11:02:22Z)

@johnbridgman 

---

### 评论 #3 — gstoner (2017-04-19T11:22:22Z)

We are moving off this server supplied AMD IT,  and will be fixxing this issue. 

---

### 评论 #4 — victoredwardocallaghan (2017-05-04T00:56:27Z)

@gstoner can you please reopen this until it is actually resolved.

---

### 评论 #5 — victoredwardocallaghan (2017-09-09T10:41:10Z)

@gstoner @johnbridgman  this is seriously egregious that this bug was closed and things were never fixed.
https://instinct.radeon.com/en-us/amd-deep-learning-stack-using-docker/

---

### 评论 #6 — anoother (2017-12-17T19:05:18Z)

This is probably worth reopening... The key is not yet available over HTTPS that I can see.



---
