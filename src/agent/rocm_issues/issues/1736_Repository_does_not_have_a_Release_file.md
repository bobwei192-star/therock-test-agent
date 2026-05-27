# Repository does not have a Release file 

> **Issue #1736**
> **状态**: closed
> **创建时间**: 2022-05-13T09:26:44Z
> **更新时间**: 2025-07-23T18:53:43Z
> **关闭时间**: 2022-05-16T10:37:58Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1736

## 描述

Since today, I get the following error:

```
$ sudo apt update
[...]
Ign:9 http://repo.radeon.com/rocm/apt/debian xenial InRelease
Err:10 http://repo.radeon.com/rocm/apt/debian xenial Release
  404  Not Found [IP: 13.82.220.49 80]
Reading package lists... Done
E: The repository 'http://repo.radeon.com/rocm/apt/debian xenial Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

---

## 评论 (9 条)

### 评论 #1 — Bengt (2022-05-13T16:04:57Z)

Switching to HTTPS does not help.

---

### 评论 #2 — Bengt (2022-05-13T23:08:03Z)

I had to deactivate the AMD repository to make my other updates work.

---

### 评论 #3 — Bengt (2022-05-15T22:01:50Z)

This issue causes security vulnerabilities of running outdated and potentially dangerous software versions of other packages.

---

### 评论 #4 — xuhuisheng (2022-05-16T03:47:21Z)

try this:
`deb [arh=amd64] https://repo.radeon.com/rocm/apt/debian ubuntu release`

---

### 评论 #5 — Bengt (2022-05-16T10:37:05Z)

Thanks for the idea, however, your line is slightly incorrect. For me, this worked:

    echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian ubuntu main' | \
        sudo tee /etc/apt/sources.list.d/rocm.list

I also had to add the new public key to my keyring:

    wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -


---

### 评论 #6 — Bengt (2022-05-16T10:37:58Z)

Thanks for helping me, @xuhuisheng. This resolves the issue for me. I will therefore close it.

---

### 评论 #7 — tvandraren (2022-12-20T17:02:14Z)

> Thanks for the idea, however, your line is slightly incorrect. For me, this worked:
> 
> ```
> echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian ubuntu main' | \
>     sudo tee /etc/apt/sources.list.d/rocm.list
> ```
> 
> I also had to add the new public key to my keyring:
> 
> ```
> wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
> ```

thanks for your response. I have no idea what I'm doing here and this helped.

---

### 评论 #8 — skipdashu (2025-01-16T17:09:33Z)

ditto on not knowing what I'm doing but replacing "ubuntu" with "focal" on the "echo" line seems to have resolved it for me.

---

### 评论 #9 — srohit0 (2025-07-23T18:53:43Z)

The command didn't work on Ubuntu 18.04.5 LTS

`wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -`
-k or -r can be used together with -O only if outputting to a regular file.
gpg: no valid OpenPGP data found.


---
