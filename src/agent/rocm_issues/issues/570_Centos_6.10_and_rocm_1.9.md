# Centos 6.10 and rocm 1.9

> **Issue #570**
> **状态**: closed
> **创建时间**: 2018-10-03T18:18:12Z
> **更新时间**: 2018-10-04T23:21:19Z
> **关闭时间**: 2018-10-04T14:14:38Z
> **作者**: asteroids1
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/570

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

With a modest amount of effort, it can be made to work. This opens up rocm to traditional linux distributions.

---

## 评论 (12 条)

### 评论 #1 — rumatadest (2018-10-04T08:48:09Z)

What for? Support for this version ended in 2017

---

### 评论 #2 — jlgreathouse (2018-10-04T14:14:38Z)

Adding support for CentOS 6 is not on our roadmap in the foreseeable future. That said, all of our software is open sourced. If someone in the community would like to take on this "modest" amount of effort, there may be folks interested in the results.

---

### 评论 #3 — asteroids1 (2018-10-04T14:31:58Z)

I'd be happy to publish my notes. The process was straight forward. Build the compilation environment, pull down the latest rocm , followup with the missing bits. As an aside, I'm at a university. I prefer environments that don't have systemd. Open source is good. Truly portable tools are even better. rocm is getting there.

---

### 评论 #4 — asteroids1 (2018-10-04T14:32:59Z)

Centos 6 is supported into 2020.

---

### 评论 #5 — gstoner (2018-10-04T14:34:01Z)

yes ROCm is evolution,  with step jumps along the way.  

---

### 评论 #6 — gstoner (2018-10-04T14:39:05Z)

The issue we had was C++ 17 support with GCC in 4.8 which 6.x uses.   HCC is tracking the ISO standard.   We are move to new front end for HIP that is upstream CLANG based, with OpenCL we been looking how we can do support across older distro again.  But we can not have all the tools run with an older version of GCC especially to meet the requirements for C++ as you know.  It fun puzzle to deal with since we have customers on both sides,    those who trail on distro support those on bleeding edge.    REHL 8.x is just around the corner. 

---

### 评论 #7 — jlgreathouse (2018-10-04T14:50:31Z)

Hi @asteroids1 

If there are folks in the community with the same desire (to run ROCm on CentOS 6), then I'm sure your notes would be appreciated. I should warn anyone using them, however, that AMD does not guarantee to support such a setup.

What I mean by that is: there are dozens (hundreds? :) ) of Linux distros, each with their own idiosyncrasies. The ROCm organization is somewhat small, and we are focusing our efforts on bringing up useful features and new hardware on a fixed set of distros that are of interest to the server and datacenter users that we work with. @gstoner raises the point that much of our user-level software support relies on newer tools because we are taking advantage of (and driving) new standards.

That's not to say that we do not desire to have wider software support. Our goal is to attempt to _enable_ as many distros on as much hardware as possible. But since AMD doesn't have the resources to fix every problem that comes along during such a process, we are hoping to get help from the community for things like broader distro support. This can include help packaging, pull requests to fix problems that we do not see on our supported distros, notes on how to go about installing ROCm on these platforms, etc.

However, because AMD may not be involved in each step of that process, AMD engineers would not necessarily be able to provide tech support when something goes wrong on one of these "unsupported" distros. If a user has a problem on these setups, we can't guarantee to spend time researching the root cause or making a patch. That's not to say we would never accept patches, etc. to fix known issues found and debugged by the community. Rather, this is just a statement on what kind of "support" AMD would offer for "unsupported" platforms. :)

I know this sounds like splitting hairs, but I think it's important to make the distinction between platforms where ROCm _may_ work (where we have enabled it) and platforms where ROCm is _supported_ by AMD.

---

### 评论 #8 — asteroids1 (2018-10-04T16:44:44Z)

With respect, open source + true portability , is a good thing. Conformance to ISO and IEEE standards is a good thing. We get into trouble were areas are not covered by standards (eg kernel drivers.)

The current ROCm is tied to packaging somewhat. I wish it wasn't .

I wish folks had gone OpenCL instead of relying on CUDA. 

Dependence on specific compilers to build things is unfortunate.

As gstoner said, it is an evolution.

---

### 评论 #9 — asteroids1 (2018-10-04T17:57:24Z)

My original intent of the post was to simply post a positive result running ROCm in a different environment, not to generate a long conversation. I apologize for any meandering.

---

### 评论 #10 — gstoner (2018-10-04T18:16:22Z)

I love it that we have a community working on this, I am Joe Boss,  also CTO of RTG for ROCm and Machine learning 

---

### 评论 #11 — jlgreathouse (2018-10-04T18:23:08Z)

If the boss likes it, I like it. ;)

Seriously though, if you have directions that show how to get ROCm working on CentOS 6, we'd love to see them.

---

### 评论 #12 — asteroids1 (2018-10-04T23:21:19Z)

If the boss is happy, then we are doing something right. Drop me a note. Thanks, Tom. tg@cs.toronto.edu

---
