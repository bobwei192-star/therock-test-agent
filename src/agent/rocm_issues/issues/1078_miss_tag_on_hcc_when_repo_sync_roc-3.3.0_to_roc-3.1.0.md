# miss tag on hcc when repo sync roc-3.3.0 to roc-3.1.0

> **Issue #1078**
> **状态**: closed
> **创建时间**: 2020-04-08T03:04:53Z
> **更新时间**: 2021-03-17T08:03:31Z
> **关闭时间**: 2021-03-17T08:03:31Z
> **作者**: wormwang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1078

## 描述

I meet a error , when I run repo sync 
#error: in `sync`: revision refs/tags/rocm-3.3.0 in hcc not found

root@k8snode:~/rocm3# ~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-3.3.0
.repo/manifests/: discarding 1 commits

If you want to change this, please re-run 'repo init' with --config-name

Testing colorized output (for 'repo diff', 'repo status'):
  black    red      green    yellow   blue     magenta   cyan     white 
  bold     dim      ul       reverse 
Enable color display in this user account (y/N)? 

repo has been initialized in /home/motech/rocm3

root@k8snode:~/rocm3# ~/bin/repo sync
error: in `sync`: revision refs/tags/rocm-3.3.0 in hcc not found


---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-03-17T08:03:31Z)

Hi @wormwang 
Thanks for reaching out.
As hcc is removed from ROCm 3.3 onwards, and as it was there before and in ROCm 3.1, repo sync might have thrown this error.
Recommend to clean your system and sync with the latest ROCm 4.0, issue will be gone.
Hope this helps.
Thank you.

---
