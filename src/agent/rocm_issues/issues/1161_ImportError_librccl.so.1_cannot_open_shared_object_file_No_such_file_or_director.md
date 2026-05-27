# ImportError: librccl.so.1: cannot open shared object file: No such file or directory

> **Issue #1161**
> **状态**: closed
> **创建时间**: 2020-06-23T12:12:57Z
> **更新时间**: 2021-08-10T13:48:55Z
> **关闭时间**: 2020-12-17T04:51:04Z
> **作者**: vuquocan1987
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1161

## 描述

Hello, I am trying to install rocm but got the above error when trying to import tensorflow
" ImportError: librccl.so.1: cannot open shared object file: No such file or directory "
My set up is:

ubuntu 20.04
rocm 3.5
tensorflow-rocm 2.2.0
gpu rx580
cpu intel 9100f
( using anaconda, if that matter )

I saw some other guys has same error he fix it with:
`yum install rccl`
I used 
`sudo apt install rccl`
installing was successful but I still got same error.
What should I do?


---

## 评论 (7 条)

### 评论 #1 — xuhuisheng (2020-06-24T16:07:37Z)

It's said that rocm cannot support ubuntu-20.04 right now.
https://github.com/RadeonOpenCompute/ROCm/issues/1112

I just install rocm-3.5.1 on ubunt-18.04, with sudo apt install rccl.

Ubuntu 18.04.04
ROCm 3.5.1-34
Python 3.6.10 with anaconda
tensorflow-rocm 2.2.0
cpu I7 4770
gpu RX 580

---

### 评论 #2 — xuhuisheng (2020-06-25T11:48:51Z)

It seems the `reboot` wont refresh ld cache, we must run `sudo ldconfig`.

---

### 评论 #3 — Bengt (2020-10-06T21:52:41Z)

I already had an old version of rccl installed:

    $ sudo apt install rccl
    [...]
    rccl is already the newest version (2.10.0-311-g1d2aa4e-rocm-rel-3.3-19).

I tried reinstalling it, anyways:

    $ sudo apt install --reinstall rccl
    [...]
    Reinstallation of rccl is not possible, it cannot be downloaded.

Uninstalling and installing RCCL got me the ROCm 3.8 version:

```
$ sudo apt remove rccl
[...]
Removing rccl (2.10.0-311-g1d2aa4e-rocm-rel-3.3-19) ...
$ sudo apt install rccl
[...]
Preparing to unpack .../rccl_2.7.8.467-rocm-rel-3.8-30-391bbf3_amd64.deb ...
Unpacking rccl (2.7.8.467-rocm-rel-3.8-30-391bbf3) Setting up rccl (2.7.8.467-rocm-rel-3.8-30-391bbf3)
```

So for your convenience:

    sudo apt remove --yes rccl && sudo apt install --yes rccl


---

### 评论 #4 — ROCmSupport (2020-12-17T04:51:04Z)

Hi @vuquocan1987 
Thanks for reaching out.
As tensorflow needs rccl and other math libraries along with rocm, always recommend to try the below way.
sudo apt install rocm-dkms rocm-libs rccl.

Recommend to try with the latest ROCm 3.10 and all packging/installation issues are resolved.

---

### 评论 #5 — den-run-ai (2021-08-09T18:33:54Z)

Same error with tensorflow-rocm binary wheel/package from PYPI:

ImportError: librccl.so.1: cannot open shared object file: No such file or directory


---

### 评论 #6 — ROCmSupport (2021-08-10T12:53:57Z)

As this issue is already closed, recommend to open a new issue with all supported details.
Thank you.

---

### 评论 #7 — den-run-ai (2021-08-10T13:48:55Z)

Installing rccl package and adding it to LD_LIBRARY_PATH resolved the issue.
Having RCCL wheel from PYPI would resolve this issue without sudo access.

On Tue, Aug 10, 2021 at 7:54 AM ROCmSupport ***@***.***>
wrote:

> As this issue is already closed, recommend to open a new issue with all
> supported details.
> Thank you.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1161#issuecomment-896002650>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AB4BTZM7JBQM7OZWQGICQSDT4EOPBANCNFSM4OFTJXVQ>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email>
> .
>


---
