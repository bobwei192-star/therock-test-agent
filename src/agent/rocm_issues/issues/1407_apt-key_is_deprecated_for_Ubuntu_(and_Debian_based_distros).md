# apt-key is deprecated for Ubuntu (and Debian based distros)

> **Issue #1407**
> **状态**: closed
> **创建时间**: 2021-03-16T13:25:42Z
> **更新时间**: 2021-03-22T11:18:04Z
> **关闭时间**: 2021-03-22T11:18:04Z
> **作者**: staticdev
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1407

## 描述

When you follow the installation instructions you get:

```sh
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
OK
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
```

Helpful documentation:
https://www.linuxuprising.com/2021/01/apt-key-is-deprecated-how-to-add.html

Instructions should be changed to something like:

```sh
wget -O- https://repo.radeon.com/rocm/rocm.gpg.key | gpg --dearmor > rocm.gpg
sudo mv rocm.gpg /usr/share/keyrings/
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/debian/ xenial main' |\
  sudo tee -a /etc/apt/sources.list.d/rocm.list
```

---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2021-03-17T05:04:59Z)

Thanks @staticdev for reaching out.
I have not seen this issue(below error) anytime before.
_Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8))._

Can you please share your configuration details and steps you followed for better understanding.
Thank you.


---

### 评论 #2 — staticdev (2021-03-17T08:49:11Z)

@ROCmSupport it will happen in all Debian based OS from now on: https://manpages.debian.org/testing/apt/apt-key.8.en.html

I am not sure I understood what you want me to do? I tested this on up-to-date Ubuntu 20.04 (supported) and also on 20.10 (not officially-supported).

---

### 评论 #3 — ROCmSupport (2021-03-22T03:52:37Z)

Hi @staticdev 
We are not able to reproduce this issue anytime with Ubuntu 18.04.x and 20.04.x configs(which are ROCm supported OSes as of today) and so we wish to know the exact OS or config to reproduce this problem.
Request you to share your config details for better understanding.

---

### 评论 #4 — staticdev (2021-03-22T10:50:26Z)

@ROCmSupport you are correct this comes in 20.10+, but you can make the instructions "future proof" with that change, since that works also on the versions you mentioned.

---

### 评论 #5 — ROCmSupport (2021-03-22T11:18:04Z)

Hi @staticdev 
ROCm does not support any non LTS versions like 20.10 officially and so we are not going to make changes for now.
If the same issue comes with any upcoming LTS version like 22.04, we will take care accordingly, but its more than a year to go.
Hope this helps.
Thank you.

---
