# Distinguish ROCm LLVM from upstream in plugin

> **Issue #1680**
> **状态**: open
> **创建时间**: 2022-02-16T14:25:41Z
> **更新时间**: 2024-10-24T19:36:57Z
> **作者**: fodinabor
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1680

## 标签

- **Under Investigation** (颜色: #0052cc)

## 负责人

- searlmc1

## 描述

Hi,
hipSYCL builds a Clang and LLVM plugin to support SYCL on top of HIP but also upstream Clang.
We currently have multiple issues where providing compatibility with both, upstream and ROCm Clang releases, results in having to specify explicit workaround macros while building the plugin for ROCm Clang (https://github.com/illuhad/hipSYCL/pull/702, https://github.com/illuhad/hipSYCL/issues/709).

This is due to ROCm Clang providing the `LLVM_VERSION_MAJOR` (and friends) value of upstream Clang at the time of the last pull, which usually is the version of the next release already. It is however not (easily) possible to determine at buildtime at which point this was and which APIs have already or not been changed in ROCm Clang, that are changed in the corresponding released LLVM version.

E.g. LLVM 14 is not yet released, ROCm 5.0 is released, but already provides `LLVM_VERSION_MAJOR==14` and thus building the Clang plugin expects the `release/14.x` branch's API state. But ROCm 5.0's LLVM still provides comparatively old APIs (e.g. https://github.com/llvm/llvm-project/commit/1d8750c3dad432bf01f708eb2e67a6e18757c379 is not included yet).

So is there any version macro defined in the ROCm LLVM headers that we can use to add another bunch of compatibility `#ifdef`s explicitly for ROCm versions? I.e. is there a `ROCM_LLVM_VERSION_MAJOR 5` (and friends) that we haven't found yet, but could use? Do you have any other recommended way of detecting ROCm LLVM's exact version at plugin compile time?

Apart from the issue-related work-around macros, another worst-case option for us would be either requiring the user to set a `-DROCM_LLVM_VERSION=050000` macro or similar at build time or detecting that ourselves using CMake.

I hope you can help us find better ways to deal with this and if not fix this for the future.
Thanks!

cc @illuhad

---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2022-02-22T13:51:03Z)

Hi @fodinabor 
Thanks for reaching out. I understood the query.
I have assigned this to compiler developers. Request to wait for the update.
Thank you.

---

### 评论 #2 — illuhad (2022-08-03T16:12:15Z)

@ROCmSupport Can you kindly provide us with an update?

---

### 评论 #3 — nartmada (2024-02-01T01:37:22Z)

Hi @fodinabor, does this issue still exists?  Please close the ticket if the issue has been fixed.  Thanks.

---

### 评论 #4 — fodinabor (2024-02-03T19:28:57Z)

Afaict, there's no change on the ROCm side of things (otherwise, please point me to it).

We found workarounds, but I find them non-optimal, as they try to deduce the version from `clang --version` or similar parsing... so, I'd still vote to get an LLVM header-built-in variant that is more stable and makes our workarounds obsolete.


---

### 评论 #5 — searlmc1 (2024-05-08T23:15:11Z)

Hi @fodinabor ,

"This is due to ROCm Clang providing the LLVM_VERSION_MAJOR (and friends) value of upstream Clang at the time of the last pull"

That statement remains true, however, starting with ROCm 6.1, our intent is to align the llvm upstream content within a ROCm release branch with the content within a LLVM release branch when first created. So, the window for ROCM Clang's definition of the llvm major version to differ from upstream's will be much smaller. 

E.g., ROCm 6.1 llvm ( major version 17 ) contains upstream llvm as of ~July 20, 2023; llvm upstream created LLVM 17 release branch a few days later.
E.g., ROCm 6.2 llvm ( major version 18 )  will contain upstream llvm as of ~January 19, 2024; llvm upstream created LLVM 18 release branch a few days.

Also, we added LLVM_MAIN_REVISION into AMD's fork of llvm-project: llvm-config.h.cmake ( https://github.com/ROCm/llvm-project/blob/amd-staging/llvm/include/llvm/Config/llvm-config.h.cmake#L17
 ) . It gives finer granularity on the "upstream revision" ; it's a count of the number of upstream commits that have landed in AMD's fork. Arguably a work-around, but you can ifdef based on LLVM_MAIN_REVISION ; LLVM_MAIN_REVISION does not exist in 6.1; it will exist in an upcoming release.

#if LLVM_MAIN_REVISION && LLVM_MAIN_REVISION < 376217
  // Old version of the code
#else
  // New version of the code (also handles unknown version, which we treat as latest)
#endif

Lemme know if this helps you


---

### 评论 #6 — ppanchad-amd (2024-08-01T14:36:35Z)

@fodinabor Do you still need assistance with this ticket? If not, please close the ticket. Thanks!

---

### 评论 #7 — fodinabor (2024-08-01T17:55:18Z)

Hi, sorry for remaining without a comment.
I appreciate the added macro, as it should be a relatively good measure to distinguish which LLVM version indeed is the base of a ROCm LLVM version.

However, I do have a number of concerns with this and am wondering if it still would be possible to also add a ROCm version macro to the LLVM config?

The revision count reminds me strongly of SVN times and for me comes with a number of related concerns:
- do we really have a guarantee that the commit count is strictly monotonously growing? (What happens if it is decided at some point that MLIR is bloating LLVM monorepo too much and the directory, including its commit history is purged? probably unlikely, just illustrating the point that commit count is not as inherently stable as it might sound)
- in LLVM upstream we have a number of release branches, I assume you ROCm will always base their LLVM on main? Still there's quite simply ambiguity between commit 400001 on `main` and `release/19.x`
- do you guarantee, that you're not porting changes from upstream LLVM to ROCm LLVM after that commit id update that might change APIs?
- do you guarantee to not change APIs downstream? So just using the commit count as a reference, would be helpful to identify the LLVM+ROCm version, sure, but it probably isn't updated between 6.1.2 and 6.1.3, where there miiight be an ever so slight change you had to do downstream?
- using commit count is not very intuitive, one has to cross reference which LLVM version & ROCm this actually was, ... when I get a bug report ROCm 6.2 is broken, how do I find out the relevant commit count range for the ROCm specific version? Is it the same for all 6.x releases? How can I easily map commit counts back to ROCm versions for bug chasing purposes? (I guess we can have `ROCM_6_1_COMMIT_MAIN_REVISION` defines or sth like this, but this still doesn't really improve the situation over just having a ROCm version macro in the LLVM config.

So, to me it seems that having a stable correlation between ROCm version and LLVM base commit is not entirely enough, but instead I'd really be interested in what ROCm version we're dealing with.

So far, I do not know of any AdaptiveCpp (hipSYCL) users that would use self-built ROCm versions that lie somewhere in-between ROCm versions - and this is certainly not something we intend to support. So the ROCm release identification should be enough for our purposes.

CC @illuhad 

---
