# Required to be root to list devices

> **Issue #1826**
> **状态**: closed
> **创建时间**: 2022-10-08T04:31:58Z
> **更新时间**: 2024-02-09T14:37:42Z
> **关闭时间**: 2024-02-09T14:37:41Z
> **作者**: illwieckz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1826

## 描述

Here I'm running ROCm 5.3 on Ubuntu 22.04

I can't list devices as user:

```
illwieckz@test:~$ clinfo --list
```
 
But I can do it as root:

```
illwieckz@test:~$ sudo -u root clinfo --list
Platform #0: AMD Accelerated Parallel Processing
 `-- Device #0: gfx1033
```

Note that this is a computer upgraded from an Ubuntu 20.04 that was the first install.

On another computer, I can list the devices without being root, but this other computer has more than a decade of Ubuntu upgrades so maybe it inherited some configuration from old Ubuntu versions:

```
illwieckz@other:~$ clinfo --list
Platform #0: AMD Accelerated Parallel Processing
 `-- Device #0: gfx701
```

Note: the user is already in the `video` group.

---

## 评论 (3 条)

### 评论 #1 — illwieckz (2022-10-08T04:36:21Z)

I had to add the user to the `render` group as well:

This is written to be only required for Ubuntu 20.04 on this page:
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

Anyway this page is obsolete it is said to be for ROCm 4.3 that predates Ubuntu 22.04 as far as I know.

---

### 评论 #2 — nartmada (2024-02-02T22:50:44Z)

Hi @illwieckz, do we still need this ticket to be opened? Please close it if your concern has been addressed.  Thanks. 

---

### 评论 #3 — nartmada (2024-02-09T14:37:41Z)

Closing the ticket.  @illwieckz, please re-open if you still see this issue in latest ROCm 6.0.2.  Thanks.

---
