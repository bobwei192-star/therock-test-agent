# xUbuntu 18.04 - desktop session logout

> **Issue #1099**
> **状态**: closed
> **创建时间**: 2020-05-06T17:05:24Z
> **更新时间**: 2020-05-08T00:40:42Z
> **关闭时间**: 2020-05-08T00:40:42Z
> **作者**: alphaaurigae
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1099

## 描述

ive just installed rocm from the xenial apt repo as described in the documentation on my xubuntu 18.04 setup - (`5.3.0-51-generic 44~18.04.2-Ubuntu`).

previously i had amdgpu-pro installed and the system running smoothly without errors.

after i removed amdgpu-pro and replaced it with the rocm i experience various desktop session logouts!

for some reason - every-time the session logout occurs i run "`pidgin`" - i get logged out directly.
In other cases the source of error was less recognizable..

EDIT:
```
Package: rocm-libs
Version: 3.3.0-19
Priority: optional
Section: devel
```


---

## 评论 (6 条)

### 评论 #1 — Rmalavally (2020-05-06T17:15:37Z)

Thank you for reaching out. 

Can you, please, provide a link to the documentation you are using to install AMD ROCm? 

---

### 评论 #2 — alphaaurigae (2020-05-06T17:19:59Z)

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

was yest, as i recall it was this link..





---

### 评论 #3 — Rmalavally (2020-05-06T17:27:46Z)

The link is correct. Thank you for confirming. Let me check with our QA team and get back to you.

---

### 评论 #4 — alphaaurigae (2020-05-06T18:46:57Z)

meanwhile got logged out a couple more times.

**this only occurs when apps / windows are opened and closed. Never "randomly" without button clicks.**

last it occurred when i closed a terminal window.

---

### 评论 #5 — Rmalavally (2020-05-07T18:43:16Z)

I checked with our team and they said the documentation is accurate. They believe the issue is not related to AMD ROCm. 

The team recommends you try the following options:

- Uninstall ROCm, reboot, and check for the behavior

- Install ROCm, reboot, and check again


---

### 评论 #6 — alphaaurigae (2020-05-08T00:40:33Z)

Confirm error persists after `rocm` removal and  `linux-firmware` re-installation.

This error started to occur when i removed the `amd-gpu pro` and installed the `rocm dkms`.

Currently i have no driver installed and the error still  keeps on coming back. 

The system wants to report some crash on every reboot:
- went to the /var/log/crash folder and found a `xfsettingsd` & `xorg` crash report.

when googling up the `xfsettingsd` error i found it similarly occurred in another place when mixing up ubuntu version dpkg packages
https://askubuntu.com/questions/546061/xfce-settings-manager-crashing

i close the error report here as i have no means to research further and just setup a new box instead and see if anything the like occurs again .

---
