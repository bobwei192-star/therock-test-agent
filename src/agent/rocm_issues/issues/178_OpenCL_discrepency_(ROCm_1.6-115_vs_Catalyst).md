# OpenCL discrepency (ROCm 1.6-115 vs Catalyst)

> **Issue #178**
> **状态**: closed
> **创建时间**: 2017-08-07T09:40:33Z
> **更新时间**: 2018-02-16T16:22:43Z
> **关闭时间**: 2018-02-16T16:22:42Z
> **作者**: newling
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/178

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

MIOpenGEMM generates OpenCL kernels based on ~20 hyper-parameters. Almost all of generated kernels compile and give correct results on ROCm. But occasionally a combination of hyper-parameters will give a  kernel which either

(1) gives incorrect results on ROCm, but correct on Catalyst. An example is here
https://github.com/ROCmSoftwarePlatform/MIOpenGEMM/blob/develop/rocm1/incorrect1.cpp

(2) hangs in clBuildProgram on ROCm, but compiles fine on Catalyst. An example is here 
https://github.com/ROCmSoftwarePlatform/MIOpenGEMM/blob/develop/rocm1/hangs1.cpp

I can't pinpoint the problem, it seems to arise from a complex interaction of hyper-parameters. 
Not sure what info I can provide? 

---

## 评论 (12 条)

### 评论 #1 — gstoner (2017-08-09T21:22:05Z)

Are you sure you do not have out of bounds memory references,  Catalyst would just let them though. 

---

### 评论 #2 — newling (2017-08-09T21:53:37Z)

i'm pretty certain there are no out of bound mem refs here. 

---

### 评论 #3 — searlmc1 (2017-08-22T00:31:45Z)

I can reproduce the issue:
$ /usr/bin/c++ -I/opt/rocm/opencl/include incorrect1.cpp -std=c++11 -L/opt/rocm/opencl/lib/x86_64/ -lOpenCL
$ a.out
clCreateCommandQueue..clCreateProgramWithSource..clBuildProgram..clSetKernelArg(s)..clEnqueueNDRangeKernel..clFinish..clEnqueueReadBuffer..clFinish..done.
sum of initial c = 154.0970916748046875
sum of final c  gpu = 132.538177490234375
sum of final on cpu = 20.899591445922851562
(cpu - gpu )/cpu = -111.638588
elapsed seconds : 0.004344373941

Passes with -cl-opt-disable:
$ export AMD_OCL_BUILD_OPTIONS_APPEND="-cl-opt-disable"
$ a.out
clCreateCommandQueue..clCreateProgramWithSource..clBuildProgram..clSetKernelArg(s)..clEnqueueNDRangeKernel..clFinish..clEnqueueReadBuffer..clFinish..done.
sum of initial c = 154.0970916748046875
sum of final c  gpu = 20.899591445922851562
sum of final on cpu = 20.899591445922851562
(cpu - gpu )/cpu = 0
elapsed seconds : 0.006285465788

I’ll continue investigating; thanks for reporting.


---

### 评论 #4 — dagamayank (2017-09-05T21:28:05Z)

@searlmc1 Any progress on this bug?

cc/ @acmeman925 

---

### 评论 #5 — searlmc1 (2017-09-05T21:48:22Z)

@dagamayank ,

Progress of sorts: I’ve been working with incorrect1.cpp; it appears to be a codegen issue triggered by loop unrolling; AMD_OCL_BUILD_OPTIONS_APPEND=”-Wf,-fno-unroll-loops" cures the bug; adding “#pragma unroll 1“ to the loops helped to narrow it to a particular loop, but it is a bit touchy. I.e., it looks like a combination of loops need to be unrolled to trigger the bad codegen. Still working to identify the root problem.

cc/ @acmeman925 

---

### 评论 #6 — dagamayank (2017-10-04T15:02:51Z)

@searlmc1 Any progress on this bug? We are seeing this issue crop up in a lot of other tests. We are spending a lot of time debugging them to ultimately figure out it is a compiler bug.

I checked the 1460579 build as well which is fairly recent and this bug persists there as well.

---

### 评论 #7 — searlmc1 (2017-10-04T15:11:42Z)

@dagamayank  - no additional progress; sorry for the delay; I'll spend more time on it.

---

### 评论 #8 — dagamayank (2017-11-21T22:44:46Z)

@searlmc1 Any update on this issue? We are now hitting the same bug on our RNN tests also.

---

### 评论 #9 — searlmc1 (2017-12-29T00:44:19Z)

Appears to be a problem in the load/store optimizer; possibly triggered by this commit:
commit 881e9f317759f2a1e32a01bad39eb08cdad91dc1
Author: Stanislav Mekhanoshin <Stanislav.Mekhanoshin@amd.com>
Date:   Thu Apr 13 17:53:07 2017 +0000

    [AMDGPU] Combine DS operations with offsets bigger than byte

    In many cases ds operations can be combined even if offsets do not
    fit into 8 bit encoding. What it takes is to adjust base address.

    Differential Revision: https://reviews.llvm.org/D31993

    git-svn-id: https://llvm.org/svn/llvm-project/llvm/trunk@300227 91177308-0d34-0410-b5e6-96231b3b80d8


---

### 评论 #10 — acmeman925 (2018-02-15T23:04:29Z)

@searlmc1  Could log this in Jira and assign to Stas

---

### 评论 #11 — searlmc1 (2018-02-15T23:10:19Z)

The issue was logged into jira and has been fixed ( https://reviews.llvm.org/rL323153 ).

---

### 评论 #12 — searlmc1 (2018-02-16T16:22:42Z)

This was a compiler issue and has been fixed, so closing.

---
