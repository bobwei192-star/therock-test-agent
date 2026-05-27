# The RPM signing key expired in August 2021

> **Issue #1762**
> **状态**: closed
> **创建时间**: 2022-06-29T10:49:54Z
> **更新时间**: 2022-10-13T22:03:26Z
> **关闭时间**: 2022-10-13T22:03:26Z
> **作者**: cryptomilk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1762

## 描述

The signing key for http://repo.radeon.com/rocm/zyp/zypper/ expired last year in August:

```
Warning: The gpg key signing file 'repomd.xml' has expired.
  Repository:       Radeon Open Compute (ROCM)
  Key Fingerprint:  CA8B B472 7A47 B4D0 9B4E E896 9386 B48A 1A69 3C5C
  Key Name:         James Adrian Edwards (ROCm Release Manager) 
<JamesAdrian.Edwards@amd.com>
  Key Algorithm:    RSA 4096
  Key Created:      Fri Aug  2 02:51:30 2019
  Key Expires:      Sun Aug  1 02:51:18 2021 (EXPIRED)
  Subkey:           30C07AF01A6D36BA 2016-08-01 [expired: 2021-08-01]
  Rpm Name:         gpg-pubkey-1a693c5c-5d438912
```

The email address of the key doesn't exist: `The email address you entered couldn't be found.`

---

## 评论 (2 条)

### 评论 #1 — saadrahim (2022-07-22T12:59:06Z)

@amd-aakash and @zhang2amd can you please confirm if the issue reported is valid? 

---

### 评论 #2 — zhang2amd (2022-07-22T15:05:37Z)

You probably have a very old key and didn't update for some time. Can you please re-import (update) your key?
rpm --import http://repo.radeon.com/rocm/rocm.gpg.key

---
