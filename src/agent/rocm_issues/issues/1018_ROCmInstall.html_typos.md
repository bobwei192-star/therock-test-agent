# ROCmInstall.html typos

> **Issue #1018**
> **状态**: closed
> **创建时间**: 2020-02-21T12:28:56Z
> **更新时间**: 2020-12-01T17:46:44Z
> **关闭时间**: 2020-12-01T17:46:31Z
> **作者**: PhilipDeegan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1018

## 描述

not sure what happened over at https://rocm.github.io/ROCmInstall.html
but it looks like some "|" pipe characters are not there, or rendering anymore

```
	echo 'ADD_EXTRA_GROUPS=1' 		
 sudo tee -a /etc/adduser.conf   
	echo 'EXTRA_GROUPS=video' 		
 sudo tee -a /etc/adduser.conf
```

this doesn't make sense as it's missing the pipe before "sudo"

---

## 评论 (5 条)

### 评论 #1 — valeriob01 (2020-02-21T16:19:17Z)

On Debian sudo is not installed by default I think. The command should be:

su -c 'tee -a /etc/adduser.conf'

---

### 评论 #2 — seesturm (2020-02-21T17:34:54Z)

The instructions got broken with [this commit](https://github.com/RadeonOpenCompute/ROCm/commit/f0d15004a0c7fa61c87e014da347c9765f7cdcd9#diff-04c6e90faac2675aa89e2176d2eec7d8) and have not been really fixed since. The last good version (maybe a bit outdated) of README.md is [this](https://github.com/RadeonOpenCompute/ROCm/tree/a899984e4e46f81bf0b5aedb32c538579da4651e).

Wrt Debian: The instructions are actually for Ubuntu. I doubt that ROCm will work on Debian.

---

### 评论 #3 — valeriob01 (2020-02-21T17:51:49Z)

> The instructions got broken with [this commit](https://github.com/RadeonOpenCompute/ROCm/commit/f0d15004a0c7fa61c87e014da347c9765f7cdcd9#diff-04c6e90faac2675aa89e2176d2eec7d8) and have not been really fixed since. The last good version (maybe a bit outdated) of README.md is [this](https://github.com/RadeonOpenCompute/ROCm/tree/a899984e4e46f81bf0b5aedb32c538579da4651e).
> 
> Wrt Debian: The instructions are actually for Ubuntu. I doubt that ROCm will work on Debian.

Obviously it work on Debian I use it all the time. All my machines are Debian with ROCm.


---

### 评论 #4 — valeriob01 (2020-02-21T17:53:05Z)

> > The instructions got broken with [this commit](https://github.com/RadeonOpenCompute/ROCm/commit/f0d15004a0c7fa61c87e014da347c9765f7cdcd9#diff-04c6e90faac2675aa89e2176d2eec7d8) and have not been really fixed since. The last good version (maybe a bit outdated) of README.md is [this](https://github.com/RadeonOpenCompute/ROCm/tree/a899984e4e46f81bf0b5aedb32c538579da4651e).
> > Wrt Debian: The instructions are actually for Ubuntu. I doubt that ROCm will work on Debian.
> 
> Obviously it work on Debian I use it all the time. All my machines are Debian with ROCm.

PS: Just needs to modify the install procedure a bit and it works.


---

### 评论 #5 — jlgreathouse (2020-12-01T17:46:31Z)

This should be fixed in https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html, which has replaced our rocm.github.io documentation. Thanks!

---
