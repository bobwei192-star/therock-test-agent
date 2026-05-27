# Missing information for 1.2 source?

> **Issue #26**
> **状态**: closed
> **创建时间**: 2016-08-25T10:59:13Z
> **更新时间**: 2017-01-03T19:17:23Z
> **关闭时间**: 2017-01-03T19:17:23Z
> **作者**: chrisaj
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/26

## 描述

Using the given command to download the RoCM 1.2 source does not work:

$ repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-1.2.0

curl: (22) The requested URL returned error: 404 Not Found
Server does not provide clone.bundle; ignoring.
fatal: Couldn't find remote ref refs/heads/roc-1.2.0
Unexpected end of command stream


---

## 评论 (17 条)

### 评论 #1 — almson (2016-08-25T12:35:36Z)

There is no `roc-1.2.0` branch, and this repo doesn't contain anything interesting. Maybe someone could answer where to get all of the sources.


---

### 评论 #2 — chrisaj (2016-08-25T14:07:55Z)

The command I posted is taken directly from the readme


---

### 评论 #3 — chrisaj (2016-08-25T14:10:39Z)

https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md

On Thu, 25 Aug 2016 at 15:09, almson notifications@github.com wrote:

> Which readme?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> https://github.com/RadeonOpenCompute/ROCm/issues/26#issuecomment-242400028,
> or mute the thread
> https://github.com/notifications/unsubscribe-auth/AEMf7P8rIuDdlnuI5W30dhocXJBj7FJcks5qjaIggaJpZM4Js8gt
> .


---

### 评论 #4 — almson (2016-08-25T14:13:07Z)

Ah, yes. Someone from AMD will have to fix that. Looks like they meant to make the other repos as submodules of this repository.


---

### 评论 #5 — jedwards-AMD (2016-08-25T15:27:53Z)

This has been corrected. A ROCm 1.2.0 branch is now available for use with the repo command.


---

### 评论 #6 — chrisaj (2016-08-25T15:32:54Z)

Thanks!

On Thu, 25 Aug 2016 at 16:27, James Edwards notifications@github.com
wrote:

> This has been corrected. A ROCm 1.2.0 branch is now available for use with
> the repo command.
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> https://github.com/RadeonOpenCompute/ROCm/issues/26#issuecomment-242429248,
> or mute the thread
> https://github.com/notifications/unsubscribe-auth/AEMf7NPLR9WlfXqaYQP-U9g9KimSdqGpks5qjbR6gaJpZM4Js8gt
> .


---

### 评论 #7 — chrisaj (2016-08-25T20:46:30Z)

Hmmm. Still no clean checkout:

$ repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-1.2.0
Get https://gerrit.googlesource.com/git-repo/clone.bundle
Get https://gerrit.googlesource.com/git-repo
remote: Counting objects: 1, done
remote: Finding sources: 100% (54/54)
remote: Total 54 (delta 15), reused 54 (delta 15)
Unpacking objects: 100% (54/54), done.
From https://gerrit.googlesource.com/git-repo
   f97e72e..39252ba  master     -> origin/master
   203153e..39252ba  stable     -> origin/stable
- [new tag]         v1.12.34   -> v1.12.34
  Get https://github.com/RadeonOpenCompute/ROCm.git
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  curl: (22) The requested URL returned error: 404 Not Found
  Server does not provide clone.bundle; ignoring.
  remote: Counting objects: 138, done.
  remote: Compressing objects: 100% (3/3), done.
  remote: Total 138 (delta 0), reused 0 (delta 0), pack-reused 135
  Receiving objects: 100% (138/138), 48.29 KiB | 0 bytes/s, done.
  Resolving deltas: 100% (37/37), done.
  From https://github.com/RadeonOpenCompute/ROCm
- [new branch]      from-andres -> origin/from-andres
- [new branch]      gh-pages   -> origin/gh-pages
- [new branch]      master     -> origin/master
- [new branch]      roc-1.0.0  -> origin/roc-1.0.0
- [new branch]      roc-1.1.0  -> origin/roc-1.1.0
- [new branch]      roc-1.1.1  -> origin/roc-1.1.1
- [new branch]      roc-1.2.0  -> origin/roc-1.2.0
- [new tag]         roc-1.0.0  -> roc-1.0.0

Doing a repo sync then fails in various ways:
$ repo sync
Fetching project rdma-perftest
Fetching project HIP-Examples
Fetching project HIP
Fetching project clang
fatal: Invalid refspec '+refs/heads//refs/tags/roc-1.2.0:refs/remotes/pctools-github//refs/tags/roc-1.2.0'
fatal: Invalid refspec '+refs/heads//refs/tags/roc-1.2.0:refs/remotes/roc-github//refs/tags/roc-1.2.0'
fatal: Invalid refspec '+refs/heads//refs/tags/roc-1.2.0:refs/remotes/roc-github//refs/tags/roc-1.2.0'
fatal: Invalid refspec '+refs/heads//refs/tags/roc-1.2.0:refs/remotes/pctools-github//refs/tags/roc-1.2.0'
.....


---

### 评论 #8 — ghost (2016-08-25T20:52:11Z)

There is an extra '/' in the refspec, I'll get it fix in a sec.


---

### 评论 #9 — ghost (2016-08-25T20:54:21Z)

Seems like Adrian beat me to it.


---

### 评论 #10 — jedwards-AMD (2016-08-25T21:09:27Z)

Yes this has been fixed.


---

### 评论 #11 — chrisaj (2016-08-25T21:13:04Z)

There is still a problem with the repo init:

repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-1.2.0
Get https://gerrit.googlesource.com/git-repo/clone.bundle
Get https://gerrit.googlesource.com/git-repo
remote: Counting objects: 1, done
remote: Finding sources: 100% (54/54)
remote: Total 54 (delta 15), reused 54 (delta 15)
Unpacking objects: 100% (54/54), done.
From https://gerrit.googlesource.com/git-repo
   f97e72e..39252ba  master     -> origin/master
   203153e..39252ba  stable     -> origin/stable
- [new tag]         v1.12.34   -> v1.12.34
  Get https://github.com/RadeonOpenCompute/ROCm.git
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  curl: (22) The requested URL returned error: 404 Not Found
  Server does not provide clone.bundle; ignoring.


---

### 评论 #12 — chrisaj (2016-08-25T21:13:36Z)

(Please let me know if there's a better way to report this kind of problem)


---

### 评论 #13 — ghost (2016-08-25T21:23:26Z)

Hey chisaj,

Can I trouble you to create gist with your full console log for this command:
https://gist.github.com/

If that is an error fetching clone.bundle it should be benign. The clone.bundle is used to optimize downloads of very large projects like the Android source code.

In this case you will see repo init has an exit code of 0 (success).


---

### 评论 #14 — ghost (2016-08-25T21:23:51Z)

For a bit more reference:
http://stackoverflow.com/questions/23300245/what-to-do-about-curl-clone-bundle-error-on-aosp-repo-sync


---

### 评论 #15 — chrisaj (2016-08-25T21:27:05Z)

gist here: https://gist.github.com/chrisaj/e3a77e3b7145faf68413733db362c829


---

### 评论 #16 — ghost (2016-08-25T21:30:35Z)

That is the case I described above. Repo init actually completed successfully and the exit code status should be '0'.

You can proceed to run 'repo sync' to fetch all the code. 


---

### 评论 #17 — chrisaj (2016-08-25T21:42:11Z)

Thanks. I'm running the sync now. Seems to be working so far.


---
