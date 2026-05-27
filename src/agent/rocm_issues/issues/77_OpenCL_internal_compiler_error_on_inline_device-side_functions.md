# OpenCL internal compiler error on inline device-side functions

> **Issue #77**
> **状态**: closed
> **创建时间**: 2017-01-15T10:51:53Z
> **更新时间**: 2017-07-09T03:21:37Z
> **关闭时间**: 2017-07-02T17:19:14Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/77

## 描述

The error: <unknown>:0:0: in function generate void (float addrspace(1)*, i32, i32, i32, i32): unsupported call to function philox\n\nError: Creating the executable failed: Compiling LLVM IRs to exe.

The kernel sourcecode: https://github.com/arrayfire/arrayfire/blob/devel/src/backend/opencl/kernel/random_engine_philox.cl

The build options:
-cl-std=CL2.0  -D dim_t=long  -D T=float -D THREADS=256 -D RAND_DIST=0 -D ELEMENTS_PER_BLOCK=1024

Simply s/inline //g and the error mysteriously disappears.

---

## 评论 (9 条)

### 评论 #1 — jrprice (2017-03-06T14:12:41Z)

This sounds like misuse of the `inline` keyword. Clang conforms to C99 for `inline`, which gives different semantics to either GNU C89 or C++. See [here](http://clang.llvm.org/compatibility.html#inline) for more information.

You should just be able to use `static inline` instead of `inline`.


---

### 评论 #2 — nevion (2017-03-21T02:02:35Z)

@jrprice weird but I don't recall ever reading about static inline with any OpenCL standard.  As such, still a bug.  Interested to try it though to see but I'm afraid still a bug in the end.  Also, since such optimizations for inlining should be enabled by default and can only be explicitly disabled... well, you know - still a bug. I'll let you know if I can compile with ```static inline``` if I find the time.

---

### 评论 #3 — nevion (2017-07-08T13:29:50Z)

Hey @gstoner are you sure this should be closed? opencv/opencv#8185 has the issue too in addition to my report of it above.  It looks like a compiler error...  I don't have access to a rocm enabled computer right now to test against 1.6, however.

---

### 评论 #4 — boxerab (2017-07-08T13:36:33Z)

Can confirm that this error still happens on rocm 1.6

---

### 评论 #5 — gstoner (2017-07-08T14:16:45Z)

Remember OpenCL C language is based on C99, so it uses the C99 semantics (which are different than the c89 or c++ semantics) for the inline keyword. For C99 “static inline” is the proper declaration for functions that should be inlined in the current translation unit.

---

### 评论 #6 — nevion (2017-07-08T14:36:36Z)

@gstoner alright, I'm a believer, but not a fan of this C99 feature - even as an occational language lawyer I had a hard time digesting that and this summary was of great aid  : https://stackoverflow.com/questions/216510/extern-inline/216546#216546

In the C++ kernel language coming, will that as I expect be C++ rules on inlining?  What's the status of C++ kernelside support these days?

Also, I think rocm is the first OpenCL platform to do the C99 rules on inlining correctly... which means all the code out in the wild is wrong and they don't know it - and will result in compiler errors.  Perhaps this needs some faq entry that google will pick up somewhere?  To make matters worse, for those unlucky few supporting multiple opencl platforms, this is going to be ugly to support.  I'm not sure it's as simple as a macro decorating the front of a function since per my reading one needs to make sure external function definitions are always available in many of the contexts developers are used to using inline with.

---

### 评论 #7 — jrprice (2017-07-08T14:49:30Z)

> To make matters worse, for those unlucky few supporting multiple opencl platforms, this is going to be ugly to support. I'm not sure it's as simple as a macro decorating the front of a function since per my reading one needs to make sure external function definitions are always available...

Just use `static inline` as Greg suggested - this works with all platforms, both those that conform to C99 like ROCm, and those that don't like NVIDIA/Intel etc.

---

### 评论 #8 — nevion (2017-07-08T14:51:03Z)

@jrprice can one do that in a header file and get the right behavior?  I guess it would although it seems more apt to produce bloated binaries since it doesn't follow the one definition rule...  leaves a bitter taste... and rightly so - it does create problems afterall: https://stackoverflow.com/questions/23699719/inline-vs-static-inline-in-header-file

Note to future visitors: if you want to achieve the same inline semantics as C prior to C99 or C++, that thread shows you - do not haphazardly use `static inline` as many have suggested and expect true equivalence, especially if you are using header files.  Good luck managing whatever scenario brings you, especially if macro based.

---

### 评论 #9 — jrprice (2017-07-08T15:04:19Z)

> @jrprice can one do that in a header file and get the right behavior?

If you have the full function definition in the header, the yes, `static inline` should work fine (though I can't say I've tried this). If it's just a declaration in the header with the definition in some other translation unit that you'll later link against, I assume you want `extern inline` on the definition.

---
