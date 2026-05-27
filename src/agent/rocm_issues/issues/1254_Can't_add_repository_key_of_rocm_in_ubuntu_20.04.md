# Can't add repository key of rocm in ubuntu 20.04

> **Issue #1254**
> **状态**: closed
> **创建时间**: 2020-10-07T04:22:14Z
> **更新时间**: 2020-11-05T09:01:07Z
> **关闭时间**: 2020-11-05T09:00:18Z
> **作者**: AtulPremNarayan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1254

## 描述

hello rocm team 
plz help, the terminal is showning 

`wget -q -O - http://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
gpg: invalid key resource URL '/tmp/apt-key-gpghome.KMH3OusvRn/home:manuelschneid3r.asc.gpg'
gpg: keyblock resource '(null)': General error
gpg: key 1488EB46E192A257: 1 signature not checked due to a missing key
gpg: key 1488EB46E192A257: 1 signature not checked due to a missing key
gpg: key 3B4FE6ACC0B21F32: 3 signatures not checked due to missing keys
gpg: key D94AA3F0EFE21092: 3 signatures not checked due to missing keys
gpg: key 871920D1991BC93C: 1 signature not checked due to a missing key
gpg: Total number processed: 7
gpg:       skipped new keys: 7
`

---

## 评论 (6 条)

### 评论 #1 — xuhuisheng (2020-10-07T05:03:09Z)

try `wget -q -O - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -`

---

### 评论 #2 — AtulPremNarayan (2020-10-07T06:33:10Z)

> try `wget -q -O - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -`

thanks, 
but its still same

---

### 评论 #3 — ableeker (2020-10-11T10:34:27Z)

That first wget should work, it uses the new location of the ROCm key. As a matter of fact, it does work on my computer. The error doesn't seem to point to an issue with the ROCm key, but to other keys. People have mentioned that the manuelschneid3r may have expired. That one may have to be updated. I wonder if the ROCm key hasn't been added after all. What does 'apt-key list' show? If it's showing the ROCm key, it most likely has added the key successfully, and it may be complaining about other keys.

---

### 评论 #4 — rkothako (2020-10-13T12:08:52Z)

Hi @AtulPremNarayan 

Looks like issue is specific to your system.
Can you please list out the keys in your machine as "sudo apt-key list", so that we will come to know whether ROCm key is successfully added or not.
Please share the latest observations if you have any.

---

### 评论 #5 — rkothako (2020-11-02T11:01:18Z)

Hi @AtulPremNarayan 
Request you to close this issue, if not reproduced.
Thank you.

---

### 评论 #6 — streamhsa (2020-11-05T09:01:07Z)

Closing this issue as there is no response from reporter for a long time.
Request @AtulPremNarayan to open a new issue if there is still a problem.

---
