# Launch day support for future OS releases

> **Issue #1761**
> **状态**: closed
> **创建时间**: 2022-06-29T09:07:25Z
> **更新时间**: 2023-12-20T13:20:54Z
> **关闭时间**: 2023-12-19T03:38:11Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1761

## 描述

[ROCm did not plan support for the current Ubuntu 22.04 release.](https://github.com/RadeonOpenCompute/ROCm/issues/1590#issuecomment-1167625353) This is problematic, because by default the software updater of Ubuntu suggests upgrading as soon as the release drops:

![image](https://user-images.githubusercontent.com/11575/176397752-6ef448df-7a68-4fff-b6bc-37ddb027976c.png)

Users who followed the suggestion of upgrading to new LTS releases have found themselves with dysfunctional ROCm installations. See #1590 for the current collection of problems regarding the unavailability of a ROCm release for Ubuntu 22.04. This here issue is requesting to avoid these kinds of problems by ROCm providing launch day support for Ubuntu in particular, but also for all officially supported operating systems. Note that for this purpose there are extensive prerelease phases, at least in the Ubuntu release cycle:

https://discourse.ubuntu.com/t/jammy-jellyfish-release-schedule/23906

---

## 评论 (14 条)

### 评论 #1 — nyanmisaka (2022-06-29T14:03:25Z)

ROCm 5.2 and Linux driver 22.20 will arrive soon.
https://www.phoronix.com/scan.php?page=news_item&px=Radeon-Software-22.20-Coming

---

### 评论 #2 — Sfinx (2022-07-06T12:03:53Z)

> ROCm 5.2 and Linux driver 22.20 will arrive soon. https://www.phoronix.com/scan.php?page=news_item&px=Radeon-Software-22.20-Coming

No luck - python (aka python2) is obsolete in 22.04

```
The following packages have unmet dependencies:
 rocm-llvm5.2.0 : Depends: python but it is not installable
E: Unable to correct problems, you have held broken packages.
```


---

### 评论 #3 — Bengt (2022-07-06T12:15:30Z)

@Sfinx there seems to be no easy fix for that issue, as 22.04 does not include a python-is-python2 package anymore:

<https://packages.ubuntu.com/search?keywords=python-is-python2&searchon=names>

---

### 评论 #4 — Sfinx (2022-07-06T12:41:26Z)

> @Sfinx there seems to be no easy fix for that issue, as 22.04 does not include a python-is-python2 package anymore:
> 
> https://packages.ubuntu.com/search?keywords=python-is-python2&searchon=names

Easiest fix is to repackage rocm-llvm5.2.0 manually replacing 'python' dep with 'python3'. The llvm-14 which is used inside rocm-llvm5.2.0 is python3 aware already. Seems like AMD never do test installs of their own packages ;)

---

### 评论 #5 — Sfinx (2022-07-06T13:39:03Z)

I think this was needed by AMD when making rocm-llvm5.2.0 but not blindly setting the obsolete python as dep:

```
diff -ur patched/opt/rocm-5.2.0/llvm/bin/analyze-build /opt/rocm-5.2.0/llvm/bin/analyze-build
--- patched/opt/rocm-5.2.0/llvm/bin/analyze-build       2022-06-28 06:01:41.000000000 +0300
+++ /opt/rocm-5.2.0/llvm/bin/analyze-build      2022-07-06 16:33:19.280464923 +0300
@@ -1,4 +1,4 @@
-#!/usr/bin/env python
+#!/usr/bin/env python3
 # -*- coding: utf-8 -*-
 # Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
 # See https://llvm.org/LICENSE.txt for license information.
diff -ur patched/opt/rocm-5.2.0/llvm/bin/git-clang-format /opt/rocm-5.2.0/llvm/bin/git-clang-format
--- patched/opt/rocm-5.2.0/llvm/bin/git-clang-format    2022-06-28 06:01:41.000000000 +0300
+++ /opt/rocm-5.2.0/llvm/bin/git-clang-format   2022-07-06 16:33:39.236733030 +0300
@@ -1,4 +1,4 @@
-#!/usr/bin/env python
+#!/usr/bin/env python3
 #
 #===- git-clang-format - ClangFormat Git Integration ---------*- python -*--===#
 #
diff -ur patched/opt/rocm-5.2.0/llvm/bin/intercept-build /opt/rocm-5.2.0/llvm/bin/intercept-build
--- patched/opt/rocm-5.2.0/llvm/bin/intercept-build     2022-06-28 06:01:41.000000000 +0300
+++ /opt/rocm-5.2.0/llvm/bin/intercept-build    2022-07-06 16:33:45.244813823 +0300
@@ -1,4 +1,4 @@
-#!/usr/bin/env python
+#!/usr/bin/env python3
 # -*- coding: utf-8 -*-
 # Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
 # See https://llvm.org/LICENSE.txt for license information.
diff -ur patched/opt/rocm-5.2.0/llvm/bin/run-clang-tidy /opt/rocm-5.2.0/llvm/bin/run-clang-tidy
--- patched/opt/rocm-5.2.0/llvm/bin/run-clang-tidy      2022-06-28 06:01:41.000000000 +0300
+++ /opt/rocm-5.2.0/llvm/bin/run-clang-tidy     2022-07-06 16:33:33.324653562 +0300
@@ -1,4 +1,4 @@
-#!/usr/bin/env python
+#!/usr/bin/env python3
 #
 #===- run-clang-tidy.py - Parallel clang-tidy runner --------*- python -*--===#
 #
diff -ur patched/opt/rocm-5.2.0/llvm/bin/scan-build-py /opt/rocm-5.2.0/llvm/bin/scan-build-py
--- patched/opt/rocm-5.2.0/llvm/bin/scan-build-py       2022-06-28 06:01:41.000000000 +0300
+++ /opt/rocm-5.2.0/llvm/bin/scan-build-py      2022-07-06 16:33:53.296922157 +0300
@@ -1,4 +1,4 @@
-#!/usr/bin/env python
+#!/usr/bin/env python3
 # -*- coding: utf-8 -*-
 # Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
 # See https://llvm.org/LICENSE.txt for license information.
diff -ur patched/opt/rocm-5.2.0/llvm/bin/scan-view /opt/rocm-5.2.0/llvm/bin/scan-view
--- patched/opt/rocm-5.2.0/llvm/bin/scan-view   2022-06-28 06:01:41.000000000 +0300
+++ /opt/rocm-5.2.0/llvm/bin/scan-view  2022-07-06 16:33:26.512562039 +0300
@@ -1,4 +1,4 @@
-#!/usr/bin/env python
+#!/usr/bin/env python3
 
 from __future__ import print_function
 
diff -ur patched/opt/rocm-5.2.0/llvm/lib/clang/14.0.0/bin/hwasan_symbolize /opt/rocm-5.2.0/llvm/lib/clang/14.0.0/bin/hwasan_symbolize
--- patched/opt/rocm-5.2.0/llvm/lib/clang/14.0.0/bin/hwasan_symbolize   2022-06-28 06:01:43.000000000 +0300
+++ /opt/rocm-5.2.0/llvm/lib/clang/14.0.0/bin/hwasan_symbolize  2022-07-06 16:33:12.896379240 +0300
@@ -1,4 +1,4 @@
-#!/usr/bin/env python
+#!/usr/bin/env python3
 #===- lib/hwasan/scripts/hwasan_symbolize ----------------------------------===#
 #
 # Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
```

Edit: Wrong diff direction

---

### 评论 #6 — keryell (2022-07-08T10:09:12Z)

Curious to see Python2 in this discussion, as it was sunset in 01/01/2020 and announced basically a decade earlier... :-/

---

### 评论 #7 — Bengt (2022-07-08T10:25:32Z)

@keryell Yes, Python 2 is very much dead. I turned that thought into an issue.

---

### 评论 #8 — Sfinx (2022-07-08T13:15:09Z)

Yep, there is no 'python' package in 22.04 as it means 'python2'. So 'python' dep for rocm-llvm5.2.0 must be replaced by 'python3'. But rocm-llvm5.2.0 still will be buggy until above posted patch will be applied.

---

### 评论 #9 — My1 (2022-07-14T13:36:53Z)

> No luck - python (aka python2) is obsolete in 22.04

why is python2 even still used nowadays, when was EOL again?

---

### 评论 #10 — FCLC (2022-07-26T14:41:50Z)

this still seems to be an issue unfortunately

for those needing ROCm: an option is to build from source, using this repo seems wise: https://github.com/xuhuisheng/rocm-build/

---

### 评论 #11 — Sfinx (2022-07-27T06:13:28Z)

> this still seems to be an issue unfortunately
> 
> for those needing ROCm: an option is to build from source, using this repo seems wise: https://github.com/xuhuisheng/rocm-build/

No need to compile all this stuff - you can repackage the broken package by yourself:

```
apt-get download rocm-llvm5.2.0
dpkg-deb -x rocm-llvm5.2.0*deb rocm-llvm5.2.0
dpkg-deb --control rocm-llvm5.2.0*deb rocm-llvm5.2.0/DEBIAN
vi rocm-llvm5.2.0/DEBIAN/control
# change python dep to python3, save file exit
# apply patch I've posted above
dpkg -b rocm-llvm5.2.0 rocm-llvm5.2.0.deb
apt-get install rocm-llvm5.2.0.deb
```



---

### 评论 #12 — saadrahim (2022-10-13T22:02:19Z)

This is a discussion, not an issue. Please move to the discussions section. I will be closing discussions that are using issues. 

---

### 评论 #13 — nartmada (2023-12-19T03:38:11Z)

Closing this ticket as it is a discussion, not an issue.  

---

### 评论 #14 — My1 (2023-12-20T13:20:54Z)

I think discussions weren't a thing back then.
but since the issue was not moved into a discussion, I opened one.
#2760

---
