# [Question]  remove/uninstalle old 3.5 dkms rock  pakage

> **Issue #1293**
> **状态**: closed
> **创建时间**: 2020-11-16T16:32:24Z
> **更新时间**: 2020-11-17T15:57:32Z
> **关闭时间**: 2020-11-17T15:57:32Z
> **作者**: arpu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1293

## 描述

Hello
after try to update to latest 3.9   i cannon update or remove amdgpu-3.5-30.el7 
amdgpu-3.5-30.el7 is not located in the DKMS tree.
system is fedora 33 using centos8 repo 3.9.1

---

## 评论 (3 条)

### 评论 #1 — rkothako (2020-11-17T07:03:18Z)

Hi @arpu 
Thanks for reaching out.
Can you please share the steps you followed in step by step manner.
Thank you.

---

### 评论 #2 — arpu (2020-11-17T15:53:05Z)

hi @rkothako 
i simple try to uninstalle the rock-dkms with 

```
udo dnf remove rock-dkms                                                                                                                                                                     1 ↵  10579  16:51:36
[sudo] password for arpu: 
Dependencies resolved.
==============================================================================================================================================================================================================================================================================================================================
 Package                                                                             Architecture                                                            Version                                                                          Repository                                                                 Size
==============================================================================================================================================================================================================================================================================================================================
Removing:
 rock-dkms                                                                           noarch                                                                  1:3.5-30.el7                                                                     @@System                                                                  169 M
 rock-dkms                                                                           noarch                                                                  1:3.9-17.el7                                                                     @@System                                                                  188 M
 rock-dkms                                                                           noarch                                                                  1:3.9-19.el7                                                                     @ROCm                                                                     188 M
Removing unused dependencies:
 rock-dkms-firmware                                                                  noarch                                                                  1:3.9-19.el7                                                                     @ROCm                                                                      42 M

Transaction Summary
==============================================================================================================================================================================================================================================================================================================================
Remove  4 Packages

Freed space: 587 M
Is this ok [y/N]: y
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                                                                                                                                                                                      1/1 
  Running scriptlet: rock-dkms-1:3.9-19.el7.noarch                                                                                                                                                                                                                                                                        1/4 

------------------------------
Deleting module version: 3.9-19.el7
completely from the DKMS tree.
------------------------------
Done.

  Erasing          : rock-dkms-1:3.9-19.el7.noarch                                                                                                                                                                                                                                                                        1/4 
  Erasing          : rock-dkms-firmware-1:3.9-19.el7.noarch                                                                                                                                                                                                                                                               2/4 
  Running scriptlet: rock-dkms-1:3.9-17.el7.noarch                                                                                                                                                                                                                                                                        3/4 
Error! The module/version combo: amdgpu-3.9-17.el7
is not located in the DKMS tree.
error: %preun(rock-dkms-1:3.9-17.el7.noarch) scriptlet failed, exit status 3

Error in PREUN scriptlet in rpm package rock-dkms
  Running scriptlet: rock-dkms-1:3.5-30.el7.noarch                                                                                                                                                                                                                                                                        4/4 
error: rock-dkms-1:3.9-17.el7.noarch: erase failed
Error! The module/version combo: amdgpu-3.5-30.el7
is not located in the DKMS tree.
error: %preun(rock-dkms-1:3.5-30.el7.noarch) scriptlet failed, exit status 3

Error in PREUN scriptlet in rpm package rock-dkms
  Verifying        : rock-dkms-1:3.5-30.el7.noarch                                                                                                                                                                                                                                                                        1/4 
  Verifying        : rock-dkms-1:3.9-17.el7.noarch                                                                                                                                                                                                                                                                        2/4 
  Verifying        : rock-dkms-1:3.9-19.el7.noarch                                                                                                                                                                                                                                                                        3/4 
  Verifying        : rock-dkms-firmware-1:3.9-19.el7.noarch                                                                                                                                                                                                                                                               4/4 

Removed:
  rock-dkms-1:3.9-19.el7.noarch                                                                                                                             rock-dkms-firmware-1:3.9-19.el7.noarch                                                                                                                            

Failed:
  rock-dkms-1:3.5-30.el7.noarch                                                                                                                                 rock-dkms-1:3.9-17.el7.noarch                                                                                                                                

Error: Transaction failed

```


---

### 评论 #3 — arpu (2020-11-17T15:57:32Z)

i think i found the solution 

```
sudo yum --setopt=tsflags=noscripts remove rock-dkms
```

---
