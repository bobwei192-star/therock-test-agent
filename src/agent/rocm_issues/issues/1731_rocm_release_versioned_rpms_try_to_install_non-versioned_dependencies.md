# rocm release versioned rpms try to install non-versioned dependencies

> **Issue #1731**
> **状态**: closed
> **创建时间**: 2022-04-25T20:21:40Z
> **更新时间**: 2024-02-17T15:41:37Z
> **关闭时间**: 2024-02-16T20:16:12Z
> **作者**: bigtrak
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1731

## 描述

When I say "release versioned" I mean rpms such as rocm-core4.5.0 vs the non-versioned rocm-core-4.5.0.

Switching our system over from 4.5.0 to a split 4.5.0 + 5.0.0 set of packages, as a test case, I found that
trying to add random rocm packages in would try to "drag in" non-versioned packages instead of the matching
versioned packages.    

I worked around this by installing dependencies by hand, or trying a group install (a package which
brings in many other packages) ... and checking the list to make sure all the dependencies were
versioned dependencies.   Needless to say this was quite time consuming to track down something
which allowed a proper install due to this issue.

I've added details about the last thing our researcher needed, and used it as an example here, after
everything else was installed.

I don't have the time to track this down, but it was definitely quite repeatable.  You might try a centos-8
container to repeat it in.   I removed all the non-versioned rocm software before migrating to the
versioned software.     I may try to repeat this in a container, as time permits, but it is low on my
priority list.

If you try to install the "versioned" rocm-gdb, you will find out that it tries to install non-versioned dependencies,
such as comgr, rocm-core, and rocm-dbgapi.    Those dependencies are incorrect, and it should be calling
for versioned dependency, such as comgr4.5.0, rocm-core4.5.0, and rocm-dbgapi4.5.0.

However, if I install versioned dependency, rocm-dbgapi4.5.0, for example, then it looks like
it has a side-effect of remedying this issue with rocm-gdb.    

rocm-gdb is not the only package that has this issue; I've had to install most of the rocm stack by hand
(aka package by package by hand to find ones that have complete versioned dependencies, instead
of some versioned and then reverting to un-versioned  due to this same issue with almost any versioned package.  

This occurred on centos-8 with rocm versions 4.5.0 and 5.0.0.

Once I validate our dual-version install, I'll add in the latest rocm version, to see if the behavior
persists with it.   I am using the rpm / yum based install.

---

## 评论 (6 条)

### 评论 #1 — bigtrak (2022-04-26T17:17:19Z)

This is repeatable if you create a centos-8 docker container, enable the necessary repos, install  a typical
minimum software base, add the ROCm repo, install rocm-core5.0.0, rocminfo5.0.0 then attempt to install
rocm-gdb5.0.0.    You'll see the dependency failure.  Then if you install rocm-dbgapi5.0.0 -- it grabs the
versioned names by itself correctly, and then rocm-gdb5.0.0 installs correctly.   

nB: You'll need to switch the .repo files from using the mirrorlist to baseurl configuration
pointing at vault.centos.org to be able to grab the latest centos-8.5 rpms.


---

### 评论 #2 — bigtrak (2022-04-27T19:17:28Z)

This also happens with rocm-5.1.1.

The package which seems to cause the most problems is the rocm-gdb package and the
rocm-dbgapi package as mentioned above.  However, the same type of "non-versioned install"
can happen with any install path -- this was just the easiest to make a repeater for.

If I install rocm-dbgapi early in the install process, it has so far fixed all the mis-matched
attempt to try and install "non versioned" packages with the remainder of the install.

Appended is an example of what yum reports about using "unversioned packages" 
as dependencies -- for example, you can see it tries installing
comgr
rocm-core
rocm-dbgapi

Instead of the correctly named versioned 
comgr5.1.1
rocm-core5.1.1
rocm-dbgapi5.1.1

------------------------------------------------------------------------------------

 yum install rocm-gdb5.1.1
Last metadata expiration check: 0:01:14 ago on Wed Apr 27 12:29:02 2022.
Dependencies resolved.
================================================================================
 Package            Arch        Version                   Repository       Size
================================================================================
Installing:
 rocm-gdb5.1.1      x86_64      11.2.50101-48.el8         ROCm-5.1.1       52 M
Installing dependencies:
 comgr              x86_64      2.4.0.50101-48.el8        ROCm-5.1.1       36 M
 rocm-core          x86_64      5.1.1.50101-48.el8        ROCm-5.1.1       15 k
 rocm-dbgapi        x86_64      0.64.0.50101-48.el8       ROCm-5.1.1      1.4 M

Transaction Summary
================================================================================
Install  4 Packages

Total download size: 89 M
Installed size: 323 M
Is this ok [y/N]: n
Operation aborted.


---

### 评论 #3 — saadrahim (2022-05-17T02:00:31Z)

Thanks for creating the issue. @frepaul  may be able to help with your inquiry.

---

### 评论 #4 — nartmada (2024-02-02T22:44:51Z)

Hi @bigtrak, please check latest ROCm6.0.2 to see if your issue still exists.  Please close the ticket if your issue has been fixed.  Thanks.

---

### 评论 #5 — nartmada (2024-02-16T20:16:12Z)

Closing the ticket as it is stale.  @bigtrak, please re-open if you still need AMD's attention on this issue.  Thanks.

---

### 评论 #6 — bigtrak (2024-02-17T15:41:36Z)

With later ROCm releases from 2023 and the ROCm-6.0.0 release, this has become
a non-issue.  We also changed to just doing the non-versioned ROCm setup, as that
removed these issues.   To duplicate it -- well I would tar up the existing rocm-last.version
installation, let the upgrade happen (into a new versioned directory) and then untar
the old version into it's old version directory.  Far easier to maintain, and updates have
become non-problematic.   That happened in early 2023 to work around the issue, and
still have multiple versions available.

---
