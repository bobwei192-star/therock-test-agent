# OpenCL rapid packed math support for Vega

> **Issue #219**
> **状态**: closed
> **创建时间**: 2017-09-29T12:33:34Z
> **更新时间**: 2017-11-14T13:43:16Z
> **关闭时间**: 2017-10-17T12:44:34Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/219

## 描述

Any time frame for when this will be available ?

---

## 评论 (19 条)

### 评论 #1 — jamilbk (2017-10-07T20:58:52Z)

I'm curious about this too. But we should already be able to utilize the RPM instructions from the Vega ISA using inline GCN assembly, no?

---

### 评论 #2 — oscarbg (2017-10-09T14:42:21Z)

+1

---

### 评论 #3 — gstoner (2017-10-15T15:02:36Z)

It will be in ROCm 1.6.4 for OpenCL.  HIP and HCC support it today 

---

### 评论 #4 — gstoner (2017-10-15T15:14:24Z)

I just ran Mixbench this week on MI25,  not he has a couple of issue in his code.    But MI25 is hitting Float 16 22.5 TFLOPS at peak.  Float 32 11.2 at peak 

He @ekondis has few spot where is need to clean up  like so we can build mixbench. 

- mix_kernels_ocl.cpp:28:25: error: conflicting declaration ‘typedef short int cl_half2 [2]’
- /opt/rocm/opencl/include/CL/cl_platform.h:869:2: note: previous declaration as ‘typedef union cl_half2 cl_half2’

---

### 评论 #5 — boxerab (2017-10-15T16:42:52Z)

Sounds good. Can you please update us on ETA for 1.6.4 ? 

---

### 评论 #6 — gstoner (2017-10-15T17:27:04Z)

When I am happy with it, right now looks like next week. 

---

### 评论 #7 — boxerab (2017-10-15T17:41:55Z)

OK, thanks for the update. Looking forward to it.

---

### 评论 #8 — gstoner (2017-10-16T23:48:06Z)

@boxerab @ekondis Hey we loaded a new version of ROCm 1.6.4 at repo.radeon.com can you test it. 

---

### 评论 #9 — boxerab (2017-10-17T01:08:05Z)

Cool! I tested it - all functionality looks good. In particular, OpenCL image support looks complete.

Very happy with this release. Unfortunately, performance for my application is still almost twice as slow as windows version. I understand that this is still beta release..... I will open a separate issue for this.  

---

### 评论 #10 — boxerab (2017-10-17T01:11:06Z)

Will CodeXL work with ROCm ?

---

### 评论 #11 — boxerab (2017-10-17T01:12:14Z)

What's the best way of troubleshooting performance difference between windows and ROCm drivers for OpenCL ?

---

### 评论 #12 — nevion (2017-10-17T02:38:57Z)

@boxerab I asked this question a short while ago.  See #186 , it's now https://github.com/GPUOpen-Tools/RCP - but it is also included in the ubuntu install as  /opt/rocm/bin/rocm-profiler per @chesik-amd 's comment



---

### 评论 #13 — gstoner (2017-10-17T12:07:30Z)

Yes use RCP to get the data, then you process it on CodeXL 

---

### 评论 #14 — gstoner (2017-10-17T12:16:06Z)

Remember we decided to build out fully open source compiler we are now working on addressing key shortcomings of the historical AMDGPU LLVM compiler code generator.    
- Improved Scheduler
- Put in place a New ILP scheduler.
- Scalarization/uniformity improvements 
- Better load/store vectorization.  – this is a Longer project
- Improved Peephole optimization for SDWA ( just went in the trunk) 
- We have more work on loop unrolling and optimizations 
- Function call support 

We are also working on new foundation for perf counter and tracing support, plus went back to address the debugger. 

---

### 评论 #15 — ekondis (2017-10-17T14:53:47Z)

@gstoner I've removed the type redefinition in mixbench so it compiles flawlessly on the new ROCm release.

---

### 评论 #16 — gstoner (2017-10-17T15:16:43Z)

Perfect.   both Alt and RO now work 

---

### 评论 #17 — jamilbk (2017-10-23T17:25:48Z)

@boxerab FYI looks like [PlaidML](https://github.com/plaidml/plaidml/issues/29) will be the first ML framework to support this :thumbsup:

---

### 评论 #18 — boxerab (2017-10-23T17:51:19Z)

@jamilbk my question was regarding driver support for packed math. Once support is there, then anyone 
can use it, including PlaidML.

---

### 评论 #19 — tugrul512bit (2017-11-14T13:43:16Z)

So this will boost performance as if passing from 486 to pentium? Cool.

---
