# is rocm gpg file expired

> **Issue #1511**
> **状态**: closed
> **创建时间**: 2021-07-04T13:20:25Z
> **更新时间**: 2021-07-06T03:41:08Z
> **关闭时间**: 2021-07-05T12:10:27Z
> **作者**: poohzaza166
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1511

## 描述

 ~ wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
gpg: invalid key resource URL '/tmp/apt-key-gpghome.cxQTQYrmSe/home:manuelschneid3r.asc.gpg'
gpg: keyblock resource '(null)': General error
gpg: key 1488EB46E192A257: 1 signature not checked due to a missing key
gpg: key 1488EB46E192A257: 1 signature not checked due to a missing key
gpg: key D94AA3F0EFE21092: 3 signatures not checked due to missing keys
gpg: key 871920D1991BC93C: 1 signature not checked due to a missing key
gpg: Total number processed: 7
gpg:       skipped new keys: 7

pop os 21.04


---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-07-06T02:53:12Z)

Thanks @poohzaza166 for closing this issue.
Hope issue is resolved for you.
More information on this: ROCm supports LTS versions of OS officially right now, pop os is not supported.
Thank you.

---

### 评论 #2 — poohzaza166 (2021-07-06T03:41:07Z)

yea it turn out that there is a another gpg key that is causing the trouble 

---
