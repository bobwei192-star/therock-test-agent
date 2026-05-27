# 'apt update' failure due to gpg key expiration

> **Issue #487**
> **状态**: closed
> **创建时间**: 2018-08-02T04:16:08Z
> **更新时间**: 2019-08-02T20:47:18Z
> **关闭时间**: 2018-08-02T20:48:23Z
> **作者**: llseek
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/487

## 描述

Hi,

There's an 'apt update' failure due to gpg key expiration:

```
$ wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
$ sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
$ sudo apt update
Get:4 http://repo.radeon.com/rocm/apt/debian xenial InRelease [1,816 B]
Err:4 http://repo.radeon.com/rocm/apt/debian xenial InRelease
  The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360
```

```
$ sudo apt-key list
/etc/apt/trusted.gpg
--------------------
pub   4096R/1A693C5C 2016-08-01 [expired: 2018-08-01]
uid                  James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
```

Regards,

---

## 评论 (9 条)

### 评论 #1 — NEELMCW (2018-08-02T07:40:09Z)

Yep,

I get the same error too 

Err:4 http://repo.radeon.com/rocm/apt/debian xenial InRelease                        
  The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360
Hit:5 http://in.archive.ubuntu.com/ubuntu xenial-backports InRelease
Reading package lists... Done
W: GPG error: http://repo.radeon.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360


---

### 评论 #2 — nioroso-x3 (2018-08-02T19:23:17Z)

Same here, please update the gpg keys.

---

### 评论 #3 — sunway513 (2018-08-02T20:05:33Z)

We have just renewed the gpg keys, it should work fine now after update it:
`wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -`

---

### 评论 #4 — jlgreathouse (2018-08-02T20:48:23Z)

Just tested by following the directions given by @sunway513 . Can confirm the new keys work, so closing this ticket.

---

### 评论 #5 — mdPlusPlus (2018-08-04T17:55:06Z)

Please update your documentation (not only the README.md of this repository) to contain the hash of the new key instead of the old one.

---

### 评论 #6 — sunway513 (2018-08-04T18:31:15Z)

@mdPlusPlus , thanks for the heads up, we have updated the message in the follow two more docs:

https://github.com/RadeonOpenCompute/ROCm_Documentation/blob/master/InstallGuide.rst#debian-repository-apt-get

https://github.com/RadeonOpenCompute/ROCm/wiki#add-the-rocm-apt-repository

---

### 评论 #7 — mdPlusPlus (2018-08-05T06:23:27Z)

https://rocm.github.io/install.html still points to the old key.

---

### 评论 #8 — jlgreathouse (2018-08-10T19:44:35Z)

Hi @mdPlusPlus 

Thanks for pointing that out. I've updated the directions there as well.

---

### 评论 #9 — 3lt0nM0rais-zz (2019-08-02T20:47:18Z)

Hi guys,
The key has expired again, can you update please?
`
pub   rsa4096 2016-08-01 [SC] [expirado: 2019-08-02]
      CA8B B472 7A47 B4D0 9B4E  E896 9386 B48A 1A69 3C5C
uid           [ expirada] James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>

`
`Err:3 http://repo.radeon.com/rocm/apt/debian xenial InRelease
  As seguintes assinaturas eram inválidas: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
Atingido:8 http://archive.ubuntu.com/ubuntu bionic-updates InRelease
Atingido:10 http://archive.ubuntu.com/ubuntu bionic-backports InRelease
Lendo listas de pacotes... Pronto                         
W: Erro GPG: http://repo.radeon.com/rocm/apt/debian xenial InRelease: As seguintes assinaturas eram inválidas: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
`

Thank you.

---
