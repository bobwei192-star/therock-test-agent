# ROCm OpenCL support/plans

> **Issue #31**
> **状态**: closed
> **创建时间**: 2016-09-23T14:01:32Z
> **更新时间**: 2016-09-25T18:31:49Z
> **关闭时间**: 2016-09-24T23:14:44Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/31

## 描述

Please clarify plans for and status of the OpenCL compiler/runtime support in ROCm!

Not being able to use OpenCL applications on the compute-oriented stack nor having any official plan for when/if this will happen creates an awkward situation where many compute projects with compatible/tuned OpenCL code -- that some may call "loyal" -- are left behind without clear path for progress. Possibly even worse, these are the people likely most interested in testing/using/helping develop the compute stack and not involving them seems like a bad idea.


---

## 评论 (2 条)

### 评论 #1 — gstoner (2016-09-24T23:14:44Z)

We have stated OpenCL will be comming to ROCm.    We had few thing to do first in the new compiler and runtime to support OpenCL. We have stated post 1.3 which is our next release we will be bring out Developer release of OpenCL.  It currently looking like mid November.  But understand we are still working on it so this subject to change. 

If you need a solution on Linux right now for OpenCL we are shipping AMDGPU Hybrid Driver on Linux that will solve your current need to support OpenCL.    

I really recomend you check out this Video on ROCm where we publicly talk about OpenCL comminig to ROCm http://insidehpc.com/2016/09/rocm/


---

### 评论 #2 — gstoner (2016-09-25T18:31:49Z)

I figured it be good to give you little more info with our transistion from proprietry code to Opensource, we had number of new component we need to put in place since not all of our exsting code would be usefull on the new platform.  Also we had to remove number of historical foundation componets and replace them with new solutions. 

First big update is we moving to  our new native GCN ISA compiler. We holding to our promise we make the stack opensource. .It is big shift for us since we are no longer leveraging the our historical two stage compiler architecture.
    - First Pass was a high level LLVM based Compiler which did code generation to an IL( AMDIL or HSAIL).
    - Second pass was we took binary of this IL then compiled it via our propritary shader compiler.

The LLVM native GCN ISA code generator has already been upstreamed http://llvm.org/docs/AMDGPUUsage.html. Also we now have released the Device libs for https://github.com/RadeonOpenCompute/ROCm-Device-Libs where you find the math intrinsics for OpenCL already.

Next we had  work to do on the upstream version CLANG OpenCL Frontend  to bring it up to capbility of our internal front end.  You see we have been active here. 

We also want to make sure what we bring out passes OpenCL conformance 

So there are lots of sub componets we had to pull back togther and make them clean for comunity.


---
