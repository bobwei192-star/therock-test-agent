# Missing dependency perl-URI-Encode not in CentOS PowerTools

> **Issue #1448**
> **状态**: closed
> **创建时间**: 2021-04-09T15:02:40Z
> **更新时间**: 2021-07-07T03:52:44Z
> **关闭时间**: 2021-07-07T03:52:44Z
> **作者**: pjgeorg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1448

## 描述

The ROCm 4.1.1 release notes mention new the the "hip-base package has a dependency on Perl modules that some operating systems may not have in their default package repositories."
According to the release notes it should be enough to enable the Power Tools repository for CentOS. (CoreReady Builder for RHEL). However the Power Tools repository does **not** contain the (all?) newly added dependencies.

In particular hip-base now requires `perl-URI-Encode`. This package is not part of Power Tools or any other official CentOS (or RHEL repository). It seems to be part of EPEL, but I hesitate to enable EPEL on all machines just for this dependency.

I hence ask you to please remove this depency again or contact Red Hat and ask them to include it in a future RHEL minor/major release. Of course you'd have to provide sufficient arguments why this particular package is required.

---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-04-12T07:07:21Z)

Thanks @pjgeorg for reaching out.
I will check this for you.

---

### 评论 #2 — ROCmSupport (2021-04-12T07:28:33Z)

Hi @pjgeorg 
Recommend to install epel-release, which serves many dependencies.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-05-07T11:55:48Z)

Solution provided and so closing this now.
Feel free to open a new issue, if any.
Thank you.

---

### 评论 #4 — pjgeorg (2021-05-07T12:07:15Z)

FYI: Actually no solution has been provided, nor has the reported documentation error been fixed.

Two possible solutions:
1. Remove the `perl-URI-Encode` dependency
2. At least fix the README and Installation Code: It currently states to enable the Power Tools repository for CentOS to fulfill the `perl-URI-Encode` dependency. This is simply wrong.

---

### 评论 #5 — ROCmSupport (2021-05-07T12:31:00Z)

Hi @pjgeorg 
Removing dependency is not possible now.
Only way is to install epel-release to proceed with all dependencies.
I will work with documentation team to have the fix.
Thank you.

---

### 评论 #6 — ROCmSupport (2021-07-07T03:52:44Z)

Latest update:
Docs updated with all information now.
Thank you.

---
