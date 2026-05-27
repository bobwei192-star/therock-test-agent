# how to build from source

> **Issue #29**
> **状态**: closed
> **创建时间**: 2016-09-02T00:51:25Z
> **更新时间**: 2017-01-03T19:17:56Z
> **关闭时间**: 2017-01-03T19:17:56Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/29

## 描述

Maybe I missed something out of the documentation spread across the repositories - but how does one build this hydra's toolchain?


---

## 评论 (9 条)

### 评论 #1 — gstoner (2016-09-02T02:03:50Z)

You find all the document in one place now,  that links you out .

https://radeonopencompute.github.io/documentation.html

On Sep 1, 2016, at 5:51 PM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

Maybe I missed something out of the documentation spread across the repository - but how does one build this hydra's toolchain?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/29, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DudSwncN7W96fbEXcFOWGbGYKrxXLks5ql3MOgaJpZM4JzRUN.


---

### 评论 #2 — nevion (2016-09-02T02:09:50Z)

Hey Greg,

Yes, I'm aware of that site but I didn't spot any instructions beyond repo checkout for building from source from the install page (most applicable, here: https://radeonopencompute.github.io/install.html) or the documentation pages


---

### 评论 #3 — gstoner (2016-09-02T02:14:31Z)

What are you trying to build HCC with LLVM.

greg
On Sep 1, 2016, at 7:09 PM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

Hey Greg,

Yes, I'm aware of that site but I didn't spot any instructions beyond repo checkout for building from source from the install page (most applicable, here: https://radeonopencompute.github.io/install.html) or the documentation pages

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/29#issuecomment-244265163, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DufhfGzO2GsTJdZotw8CyiWunZqi7ks5ql4VugaJpZM4JzRUN.


---

### 评论 #4 — nevion (2016-09-02T02:20:10Z)

The whole ROCm distribution, kernel land and userland alike.


---

### 评论 #5 — nevion (2016-09-02T20:00:42Z)

Just to illuminate the issue a little better, I don't expect a super indepth guide for something like configuring the kernel but working commands for cmake/build/install, in the correct order of installation to a ROCm prefix'd install location would be apt.


---

### 评论 #6 — almson (2016-09-06T18:25:23Z)

I'd like to point out that a _normal_ open-source project that is hosted on GitHub typically contains _only source code_ and inside the README.md there is instructions on how to build it. There may also be instructions on how to install binaries from a binary repository. Binaries normally live in other repository systems (linux distributions' repositores, Maven, etc.). Primarily, projects on GitHub are source code + build instructions. Binary-only or documentation-only repositories are atypical to GitHub.

It would be nice to see AMD's GitHub repositories cleaned up and reduced in number. They should also be under a single account.


---

### 评论 #7 — ghost (2016-09-06T22:19:37Z)

Hey almson,

Our projects are actually currently organized as you described (source only + build instructions). Inside each of the repositories there is a README or README.md that describes how to build that project. For example, for instructions on how to build the kernel you can look at ROCK-Kernel-Driver/README or for HIP you can look at HIP/README.md, and similar for all the other projects.

If a specific project is lacking build instructions (or they are inadequate), please feel free to open an issue in the specific project in order to get the attention of the correct maintainer.

This project (RadeonOpenCompute/ROCm) is meant to address your second concern. Finding the correct repositories to checkout by providing a repo manifest.xml that can be used to checkout all the ROCm repositories at the correct revision for a specific release.

We realize our current setup is far from perfect. For example, we are lacking an over-arching build system that produces artifacts from our public repo checkout from a simple 'make deb' or 'make rpm'. And that is something that bugs me a lot. But that is something we intend to address in the future as we shift more and more of our dev process to be public facing.


---

### 评论 #8 — nevion (2016-09-06T22:26:37Z)

@arodrigx7 I can deal with separate/distributed per project documentation but I'm not sure (without checking through each of them) that I'm going to install in the optimum order for dealing with dependencies.

I'd rather not lose maybe a day or something trying to sort that out if you guys already know and could simply list it.


---

### 评论 #9 — ghost (2016-09-06T22:49:01Z)

The README's usually state this information, as you will require the dependencies in order to perform link time validation during build. And you'll also need to provide the location of the include directory of the dependencies.

However, if you want a condensed/quick and easy way to get this info, it can be extracted from our apt repository.

After setting up the repo you can use 'debtree' to generate a dependency graph. E.g.
debtree --with-suggests rocm > rocm-dependencies.dot

Example attached as PNG
![out](https://cloud.githubusercontent.com/assets/14790944/18293698/8edc6bce-7462-11e6-8b1b-edd4e1aa6a5c.png)


---
