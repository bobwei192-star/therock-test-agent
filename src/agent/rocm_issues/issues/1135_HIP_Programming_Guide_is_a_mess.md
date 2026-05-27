# HIP Programming Guide is a mess

> **Issue #1135**
> **状态**: closed
> **创建时间**: 2020-06-06T19:02:17Z
> **更新时间**: 2025-01-27T18:08:37Z
> **关闭时间**: 2025-01-27T17:57:34Z
> **作者**: baryluk
> **标签**: Under Investigation, Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1135

## 标签

- **Under Investigation** (颜色: #0052cc)
- **Documentation** (颜色: #5319e7)

## 负责人

- Maetveis
- MathiasMagnus
- Naraenda
- saadrahim

## 描述

https://rocmdocs.amd.com/en/latest/Programming_Guides/Programming-Guides.html

is unusable.

I have 20 years of programming experience with C, C++, D, and many other languages, and HPC programming, but I can't parse this document at all.

1) It has a number of references to non-HIP stuff, like HCC, and OpenCL. And even Anaconda, where two paragraphs later reader is notified that it actually doesn't work yet.

2) Formatting is all over the place, and many `code` stuff are not formatted or formatted in a broken way.

3) There are no full examples provided or instructions to how to compile and execute simple HIP codes.

4a) It contains stuff that is totally unrelated to Programming Guide purpose. Things like versioning scheme and git tags. It is extremely niche and inconsequential, and shouldn't be there.

4b) The document starts with FAQ of random stuff, instead of providing relevant information first.

4c) There is a link to "HIP Programming Guide" from inside the "HIP programming guide" . I am not sure if this is a joke.

5a) Finding how to even install HIP in this document is hard, there is a link, but it is buried in the middle of the text, plus the link that it leads to shows how to install `hip_hcc` which is supposedly deprecated, or I am confused.

5b) There is a section about HIP-clang, in pre-build binaries, but actually there are no instructions how to install them and verify they work.

6) Document assumes familiarity with CUDA, but why assume that?


Document should be totally reworked, or written from scratch. It should have:

1) Premise (max 3 paragraphs what HIP is).

2) Installation and how to check it is installed. (max 4-5 paragraphs). Don't link to other documents, tell which package to install and how to test it. Assume basic ROCm stuff is already installed. The package dependencies should do the rest anyway.

3) Minimal example (initialization, memory allocation, launching kernel, some minimal synchronization) sample C++ code in a single file (max 25 lines), and exact command line to compile, link and run it. No references to external github directories, Makefiles or other complex build mechanisms. I should just copy paste it, and run.

4) More advanced topics overview (i.e. debugging, compiling for multiple GPUs, link to a reference manual with all hip library constructs).

5) Link to separate article on porting tools and porting methods for CUDA code to HIP.

Please give this task to a good technical writer, because right now I don't know what this document is even trying to achieve. It feels more like a marketing material, than actual something that an engineer or software developer would use.


---

## 评论 (18 条)

### 评论 #1 — Rmalavally (2020-06-06T19:29:25Z)

Thank you for your detailed feedback. It is much appreciated. 

AMD ROCm documentation is continually evolving and making improvements to enhance the AMD ROCm user experience. The newly-formed AMD ROCm Documentation team will review the recommended changes and incorporate your suggestions as applicable. 

---

### 评论 #2 — Degerz (2020-06-10T20:57:17Z)

The HIP documentation is indeed a mess. CUDA familiarity is ideal because ~90% of it's documentation can be applied to HIP so that you can pretty much use CUDA docs as the reference. 

That being said the intended audience for HIP are mainly CUDA developers.

---

### 评论 #3 — ROCmSupport (2021-02-15T13:49:15Z)

Thanks @baryluk for your detailed information.
I will work with Documentation and HIP teams and will make sure that docs are updated accordingly.
Request you to allow us little more time for all changes to be replicated.
Thank you.

---

### 评论 #4 — Rmalavally (2021-02-15T16:00:34Z)

Thank you @baryluk for your feedback. We noticed that this ticket was opened in June 2020. The HIP Programming Guide has since been updated for ROCm v4.0 and is now available in PDF format. Please refer to more details on the ROCm documentation website at:

https://rocmdocs.amd.com/en/latest/Programming_Guides/Programming-Guides.html

We will appreciate your feedback on the latest and updated HIP Programming Guide and the HIP API Guide for ROCm v4.0.

AMD ROCm Documentation Team


---

### 评论 #5 — baryluk (2021-02-15T17:37:38Z)

> Thank you @baryluk for your feedback. We noticed that this ticket was opened in June 2020. The HIP Programming Guide has since been updated for ROCm v4.0 and is now available in PDF format. Please refer to more details on the ROCm documentation website at:
> 
> https://rocmdocs.amd.com/en/latest/Programming_Guides/Programming-Guides.html
> 
> We will appreciate your feedback on the latest and updated HIP Programming Guide and the HIP API Guide for ROCm v4.0.
> 
> AMD ROCm Documentation Team

@Rmalavally  The link to the Guide doesn't work. It just bring me to this repo.

---

### 评论 #6 — Rmalavally (2021-02-15T17:41:40Z)

@baryluk 

That's correct. The PDFs for ROCm v4.0 documentation are available in this repository. Please click the link to the HIP Programming Guide v4.0, and you will access the following page:

https://github.com/RadeonOpenCompute/ROCm/blob/master/HIP_Programming_Guide_v4.0.pdf

You can choose to review the content on the webpage or download the PDF document. 


---

### 评论 #7 — baryluk (2021-02-15T18:35:55Z)

@baryluk Fix the link please. The link says "Download HIP Programming Guide v4.0 PDF" but it doesn't do that.

I done an initial review of the `HIP_Programming_Guide_v4.0.pdf` , and it is something, and a bit better than where we started from, but unfortunately far from reasonable or acceptable.

The commands, code and instructions there are clearly untested, contains semantic and syntactic errors, are impossible to use, doesn't provide instruction how to use them, or simply give errors, plus there is a lot of formatting and stylistic issues all over the document on almost every page, changes in purpose or scope, introduce concepts out of order, link to non-existing pages, etc. :( It is extremely disappointing.

Sections 2.3, 2.7, 3.2, 3.3, 3.4 are completely unusable and lacking in countless ways.

Given the current state of HIP, the only way to learn it is to reverse engineer it. That is not a good approach.

---

### 评论 #8 — Rmalavally (2021-02-15T18:50:31Z)

Thanks, @baryluk, for your feedback. We are continuing to work on it, and it is an evolving document. Please continue to share specific feedback with us, and we are happy to provide the information you need. 



---

### 评论 #9 — ROCmSupport (2021-05-07T10:44:01Z)

Hi @baryluk 
Got an update on this.
We have updated HIP programming guide to a better level now.
Still working more and more and more changes will be pushed slowly. Please stay tuned for more and more updates.
Thank you.

---

### 评论 #10 — keryell (2022-04-05T20:52:12Z)

@baryluk any update?

---

### 评论 #11 — saadrahim (2023-06-14T20:01:59Z)

Please take a look at the redone HIP documentation.

https://rocm.docs.amd.com/projects/HIP/en/latest/index.html


---

### 评论 #12 — keryell (2023-06-14T22:34:04Z)

I have the feeling there is still the point "6 Document assumes familiarity with CUDA, but why assume that?" which could be explained.

---

### 评论 #13 — saadrahim (2023-06-14T22:41:49Z)

> I have the feeling there is still the point "6 Document assumes familiarity with CUDA, but why assume that?" which could be explained.

Feedback accepted. I have added it to a backlog and will assign in the future.

---

### 评论 #14 — baryluk (2023-06-15T00:07:38Z)

I do not even know where to start.

3, 4b, 5a, 6 are not addressed.

FAQ is horrendous and huge. Half of it should be removed, because I doubt any real person (or more than one) asked them, to actually be "Frequently asked question". Actually, lets remove 75% of it.

Site formatting is not great.

"Content" on the right, with scrolling should be removed. It is redundant with content already on page, big distraction, jumps multiple sections at the time, and when clicked, scrolls to the wrong entry. It is broken in too many ways, and even if fixed, it will still be bad UX. Just remove it. (But make sure sections can still be linked directly using an anchor)

Ordering of sections could be better, it feels random. I have spent 30 minutes trying to do something, and I could not. Maybe I am stupid. So, I went to SYCL and CUDA documentation. It took me less than 1 minute to find what I need.

"HIP Logging Tips" is absolutely comical. Please remove, because it is insulting.

The rest of "Developer Guide": 1) Contributor Guidlines - move to git repo as Markdown file (and maybe remove half of the content in it), its existence in HIP Programming Guide is not justified IMHO  2) "Logging mechanism" - remove, it is so trivial, 1 minute of developing of HIP will make you know it, so it is redundant. Maybe leave the environment variables documentation for reference (and users of HIP), but make it shorter.

"Terms used in HIP Documentation" - remove, does not provide any useful information.

"HIP Runtime API Reference" - is a chaos too. Half of the pages is broken, empty, have wrong formatting, scroll incorrectly, do now show up on left, have broken navigation, etc. More than half. It is clear that it was done quickly with automated tools.

There is a lot poor wording, and inaccurate descriptions all over the place. It causes confusion, and when you click hoping to find X, you find Y.

For example "Kernel Language Syntax". I do not think you know what "Syntax" means. 90% of what is in "Kernel Language Syntax" does not belong to that document.

Another example, repeatedly mixing up function and macro, even in same section - no, they are not the same thing.

Another one: not understanding a difference between language and library. In multiple places.

Inconsistencies: On some pages, functions are marked `__device__`, and on some others they are not (despite that they are surely `__device__`).

Redundant information: "Kernel Language Syntax" is filled with filler, that can be found on other pages, or should be split.

Inefficient formatting: "HIP MATH APIs Documentation" is a great example. The same information could be easily fitted in 10% of current length of this document.

These are just examples.

In current form, this is not a "Documentation" or "Guide". More like a bag of tricks and hacks.


For some comparison, here is a list of guides that actually does the job, and does it very well (structure, clarity, intent, effectiveness, UX).

- https://registry.khronos.org/SYCL/specs/sycl-2020/html/sycl-2020.html
- https://developer.codeplay.com/products/computecpp/ce/2.11.0/guides/getting-started-with-computecpp
- https://docs.nvidia.com/cuda/cuda-c-programming-guide/contents.html
- https://intel.github.io/llvm-docs/GetStartedGuide.html
- https://www.intel.com/content/www/us/en/docs/dpcpp-cpp-compiler/get-started-guide/2023-1/overview.html (that one is a bit messy, but still better than HIP Programming Guide)



And, yes, I think https://github.com/RadeonOpenCompute/ROCm/issues/1760 is critical, and should be given VERY high priority.

---

### 评论 #15 — saadrahim (2023-06-15T19:24:13Z)

@baryluk Thank you for your thorough feedback. I will prioritize this ticket and #1760.  HIP documentation will be completely rewritten.



---

### 评论 #16 — hliuca (2023-09-14T20:43:29Z)

Strongly agree with this, "Content" on the right, with scrolling should be removed. It is redundant with content already on page, big distraction, jumps multiple sections at the time, and when clicked, scrolls to the wrong entry. It is broken in too many ways, and even if fixed, it will still be bad UX. Just remove it. (But make sure sections can still be linked directly using an anchor)". 

@saadrahim I was thinking of creating a JIRA ticket for this. The current documentation uses 3 columns, two of them are "contents". Only one column for documentation itself. The right column should merge into the left "contents", and leave more space for documentation.

Also, some manuals have section number in "contents", such as rocsolver, "2, 2.1, 2.2", and some manuals have no section number, such as rocblas. Not consistent.

---

### 评论 #17 — harkgill-amd (2025-01-23T19:04:45Z)

Hi @baryluk, the HIP Programming Guide has been completely rewritten and addresses the concerns raised in this thread. You can find the updated guide [here](https://rocm.docs.amd.com/projects/HIP/en/latest/programming_guide.html). Different points may have been addressed in staggered updates of the documentation, however; this rework aims at tackling all the concerns brought up and more. Going through some of the issues brought up at the beginning of this thread

> 1. It has a number of references to non-HIP stuff, like HCC, and OpenCL. And even Anaconda, where two paragraphs later reader is notified that it actually doesn't work yet.

All unnecessary references have been removed.

>  2. Formatting is all over the place, and many code stuff are not formatted or formatted in a broken way.

There were discrepancies in the formatting of code and of the docs in general. Formatting has been unified with the rework.

> 3. There are no full examples provided or instructions to how to compile and execute simple HIP codes.

Multiple tutorials and examples have been added throughout the documentation such as 
- https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/saxpy.html
- https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/reduction.html
- https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/error_handling.html#complete-example

> 4a) It contains stuff that is totally unrelated to Programming Guide purpose. Things like versioning scheme and git tags. It is extremely niche and inconsequential, and shouldn't be there.

We agree and took this into account when updating the guide.

> 4b) The document starts with FAQ of random stuff, instead of providing relevant information first.

The FAQ section has been reworked and is no longer at the start of the programming guide.

> 4c) There is a link to "HIP Programming Guide" from inside the "HIP programming guide" . I am not sure if this is a joke.

The content of the "HIP Programming Guide" page had been split up, extended, and rewritten. Now multiple pages represent the Programming Guide. The introduction page link can be found [here](https://rocm.docs.amd.com/projects/HIP/en/latest/programming_guide.html)

> 5a) Finding how to even install HIP in this document is hard, there is a link, but it is buried in the middle of the text, plus the link that it leads to shows how to install hip_hcc which is supposedly deprecated, or I am confused.

HIP is an interface, while ROCm is the software stack. This relationship is now better defined in the HIP documentation under the [What is HIP?](https://rocm.docs.amd.com/projects/HIP/en/latest/what_is_hip.html) and [Installing HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/install/install.html) pages.

> 5b) There is a section about HIP-clang, in pre-build binaries, but actually there are no instructions how to install them and verify they work.

In the [SAXPY tutorial](https://rocmdocs.amd.com/projects/HIP/en/latest/tutorial/saxpy.html#compiling-on-the-command-line), we introduce the amdclang compiler and how to verify it's usage. We will be updated the programming guide to include more documentation on this as well to avoid any confusion.

> 6. Document assumes familiarity with CUDA, but why assume that?

During the rework, we avoided making this assumption as much as possible.

In regards to the documentation you noted that should be added or reworked.

1. Premise: https://rocm.docs.amd.com/projects/HIP/en/latest/what_is_hip.html
2. Installation: https://rocm.docs.amd.com/projects/HIP/en/latest/install/install.html 
3. Minimal Examples: In each section of the guide, we've added as my examples as possible. We've also expanded on the examples listed under the "Tutorials" section of the documentation.
4. More advanced topics overview: We are currently working to improve this area of the documentation.
5. Link to separate article on porting tools/methods: The [HIP Porting Guide](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_porting_guide.html) and [Porting CUDA driver API](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_porting_driver_api.html) pages address this.

The issues listed in https://github.com/ROCm/ROCm/issues/1135#issuecomment-1592146810 were also taken into account when rewriting the programming guide and the other pieces of relevant documentation. Please take a moment to review the new guide and share any feedback you have. Thanks!

---

### 评论 #18 — baryluk (2025-01-27T17:57:34Z)

@harkgill-amd Wow. Thank you for addressing almost all issues.

I must commend this. I did look briefly in new HIP docs, and it is actually very good now. Both high level structure, and some details. I didn't dive deep, but I think it looks good, and I am no longer lost.

It is also amazing that there are clean installation instructions, including building from source.

I will tests some of the guide later. But I am not sure if my Radeon 6900 XT (atm I only have Radeon 6900 XT (RDNA2) and Radeon R9 Fury X (Fiji XT, GCN3)  will work fully.


I also see ROCm installation and docs were updated few months ago, and are in general cleaner and more usable.

Thank you.

The content and right column with sub-naviation is better, but probably still can be improved to address some of the comments from me and Hui Liu in this issue.

Closing for now.


---
