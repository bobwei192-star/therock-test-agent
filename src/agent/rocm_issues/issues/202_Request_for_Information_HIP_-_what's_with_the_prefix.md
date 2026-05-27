# Request for Information: HIP - what's with the prefix?

> **Issue #202**
> **状态**: closed
> **创建时间**: 2017-09-08T02:58:23Z
> **更新时间**: 2017-09-10T13:16:57Z
> **关闭时间**: 2017-09-09T21:02:24Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/202

## 描述

Or rather is there not a way to fuse and focus on better nvcc compatability?

What I'm getting at is I respect hip should be by default it's own thing and show that throughout code with the hip prefix.  But I wonder why, when it targets CUDA compatability, it cannot just work for code not relying on intrinsics/inline ptx or fancy features.  I don't know, maybe a sourcecompat flag. The issue is mainly around the runtime/hostside portion of things.

I'd like to gain some reasoning as to why compiling from a very clean and simple "plain-old-CUDA" sourcefile would always require a hipify pass.  It adds burden to the build process to generate sourcefiles and this is definitely a complex detail in any build system I've ever seen (make/cmake in mind specifically).  Should we expect that hipify will always be a required to compile hip-minded CUDA code with the ROCm ecosystem?

---

## 评论 (3 条)

### 评论 #1 — gstoner (2017-09-09T21:02:24Z)

You should really direct this rant at NVIDIA since there is not an open plan old Cuda.  You see they recently even pull NCCL 2 in to be a proprietary library.     cuBLAS, cuFFT, cuSPASE, cuRAND, cuDNN all proprietary.   There are no open standard interfaces people can use for this code.  But we also internal restrictions. 

Now a community project could start using the  Google Cuda Clang Front end in LLVM  and use it with HIP to build out this runtime.   

Again there is nothing stopping the community from building this out.   GCC tools happen this way on Linux so did LLVM in the beginning. 

I know we are the underdog.  It takes time to put the key foundation in place. 

---

### 评论 #2 — nevion (2017-09-09T23:03:09Z)

Not a rant. I wanted to know where things are going in tools and usage, what's in the works and how things came to be.  I know other people wonder as well - but rather than wonder and get faced with the question myself I want to be able to share why as it always comes up.  Technical, legal, all on the board. 

There is plain old cuda out there.  I write it often and I know other engineers who write it often across my career as for some people authoring inhouse kernels is the majority of work.  Sometimes 3rd party libraries such as CUB (as has been mentioned in the past) or host driven libraries like thrust or the examples you mention are pulled in, but in practice (or by SLOC) those are the exception, not the rule.  

I've also been wondering how the Clang front end would start playing in here but I figured the project distance was high.  It did spring the question though that if "they're doing it" why you can't as well, legally or technically speaking.

Say if I took the burden onto myself to streamline the hipify/hipcc process, would that be something you could merge?

Have a good weekend Greg.

---

### 评论 #3 — gstoner (2017-09-10T13:16:57Z)

I send you a pm.   All changes develop by the community are well, they will go through a review process for inclusion. 

---
