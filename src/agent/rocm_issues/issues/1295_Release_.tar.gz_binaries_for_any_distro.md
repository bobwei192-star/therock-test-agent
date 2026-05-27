# Release .tar.gz binaries for any distro

> **Issue #1295**
> **状态**: closed
> **创建时间**: 2020-11-18T12:01:38Z
> **更新时间**: 2021-01-07T05:20:05Z
> **关闭时间**: 2021-01-07T05:20:04Z
> **作者**: 0x0f0f0f
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1295

## 描述

Me and other distros users are having trouble building the stack. Having to build a custom clang and a custom LLVM is quite time intensive. Could you please release a tarball with the binaries?

---

## 评论 (13 条)

### 评论 #1 — jpsamaroo (2020-11-18T13:42:13Z)

To add to this, it would be ideal if such a tarball had binaries linked against LLVM statically. This would be necessary for languages/projects that package their own LLVM (Julia in my case), since multiple dynamically-loaded libLLVMs conflict with each other.

---

### 评论 #2 — baryluk (2020-11-18T19:37:50Z)

@jpsamaroo I really doubt you will be able to load multiple versions of LLVM at the same time into single process. I could be wrong tho.

I also just feel linking entire LLVM statically might be an overkill, even if this LLVM only supports amdgcn targets. It is a very big library.

As of tarballs. You can build things yourself from git. Technically. I still struggle to make it work.


---

### 评论 #3 — ROCmSupport (2020-11-19T06:15:31Z)

Thanks @0x0f0f0f for reaching out.
We will check and get back to you asap.

---

### 评论 #4 — searlmc1 (2020-11-19T22:11:29Z)

Hi @baryluk ,

You mentioned that you have troubles building from git. Can you expand on what problems you are having?

Thanks

---

### 评论 #5 — 0x0f0f0f (2020-11-20T00:13:26Z)

I think that a "git pipeline"/github actions is what @baryluk meant. A travis CI/github actions build pipeline would really help understanding how to build, replicating a standard build locally and mostly, giving us downloadable binary archives. 

If talking about cloned git repositories, is not very clear to understand how to build for ROCm newcomers like me. My ROCm dir is 9.9GBs.... 
Which ROCm packages do depend on each other? Each package has it's own README format, some packages lack an INSTALL file with instructions, some packages require configuration steps that are not explained in the README. It's also not very clear which custom forks of LLVM/clang should be used to build. Is aomp even needed at all when building ROCm?

I really think that apart from distro agnostic binaries, a "global" build script letting you choose which components of ROCm you need, and doing the dirty building job on its own would be very helpful. 

---

### 评论 #6 — baryluk (2020-11-20T15:01:25Z)

@searlmc1 I tried building ROCm 3.8 few weeks ago. It was very hard to figure out all the repos that are required (only the required ones, not all the "extras"), order in which to build them, and flags to pass, especially if one wants to build a relocatable installation (i.e. not in /opt/rocm), especially without root. I managed to figure this out eventually after a lot of trail and error, but still one of the crucial components was failing cmake configuration, despite me trying all the possible cmake flags (I tried like 20 different path flags) and options to point it into the correct directory. After few days of fighting with cmake, I gave up. I believe it was `HIP` that was failing cmake. All the other things like `rocm-cmake`, (ROCm's) `llvm-project`, `ROCT-Thunk-Interface`, `ROCm-Device-Libs`, `ROCR-Runtime`, `ROCm-CompilerSupport`, `ROCclr` (ROCm-OpenCL-Runtime), compiled in that order, built fine. But then `HIP` was a failure. It probably was possible to fix it, but I just don't know cmake enough to make it work.

I don't want a script, I want a documentation that explains the process, a graph of dependencies what requires what. I find scripts to be too ridgid, follow poor practices or coding style, are overly complex / verbose, have hard coded paths, are not adaptable, pull non-required dependencies from who knows where, and break on various distros or future versions. Documentation how to build a MINIMAL build, would be better.

See https://github.com/RadeonOpenCompute/ROCm/issues/1188


---

### 评论 #7 — 0x0f0f0f (2020-11-20T19:24:47Z)

@baryluk is on point!

---

### 评论 #8 — saitam757 (2020-11-23T16:52:47Z)

@ROCmSupport: Better than releasing tar.bz binaries would be using a build system. A viable way would be e.g. the [OpenSUSE Build System](https://openbuildservice.org/) where distribution packages not only for OpenSUSE but several other distributions could be build (ubuntu, fedora, ...). 

---

### 评论 #9 — baryluk (2020-11-23T17:02:02Z)

> @ROCmSupport: Better than releasing tar.bz binaries would be using a build system. A viable way would be e.g. the [OpenSUSE Build System](https://openbuildservice.org/) where distribution packages not only for OpenSUSE but several other distributions could be build (ubuntu, fedora, ...).

It is impossible for AMD to support all distributions and releases.

The best is to provide the build instructions (in up to date text), and distros and people can pick it up from there easily to support everything. Not scripts or build system.

It is just my opinion.

---

### 评论 #10 — saitam757 (2020-11-23T17:29:51Z)

@baryluk I admit, a build system would be the nicest thing to have. But up to date information and correct use of Cmake would be great. I tried building the stuff for Solus and I gave up.  

---

### 评论 #11 — rkothako (2020-11-24T04:58:44Z)

Hi @saitam757 and @baryluk 
We are working internally to update the docs with proper build instructions.
We will get back asap, please stay tuned.

---

### 评论 #12 — ROCmSupport (2020-12-11T05:20:01Z)

Hi All,
We need some more time to get the proper build instructions and documentation updated.
Will keep you posted.
Thank you.

---

### 评论 #13 — ROCmSupport (2021-01-07T05:20:04Z)

Hi All,
Reg: "Releasing ROCm in the form of .tar.bz" --> We do not plan to do such releases
Reg: Building ROCm from source with proper instructions --> Please track #1188 ticket.
Thank you.

 


---
