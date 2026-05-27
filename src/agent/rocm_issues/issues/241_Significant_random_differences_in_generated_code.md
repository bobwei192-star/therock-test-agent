# Significant random differences in generated code.

> **Issue #241**
> **状态**: closed
> **创建时间**: 2017-10-29T09:44:02Z
> **更新时间**: 2018-02-13T19:19:08Z
> **关闭时间**: 2018-02-13T19:19:08Z
> **作者**: preda
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/241

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

ROCm 1.6-180, Ubuntu 16.04, R9-Nano.

Compiling the exact same OpenCL source in identical conditions, produces two significantly different outputs. The two outputs seem to alternate in a random manner. I attach the two ISA files for comparison. Note, they are output from exactly identical input/args. (!)

The outputs were compiled from GpuOwl  at commit 28c127f.

Note, the two variants have different performance. The differences are not 'neutral'. E.g.
```
3953c3953
<               workitem_private_segment_byte_size = 100
---
>               workitem_private_segment_byte_size = 220
```

[DP_4M_0_fiji-A.txt](https://github.com/RadeonOpenCompute/ROCm/files/1424909/DP_4M_0_fiji-A.txt)
[DP_4M_0_fiji-B.txt](https://github.com/RadeonOpenCompute/ROCm/files/1424910/DP_4M_0_fiji-B.txt)


---

## 评论 (10 条)

### 评论 #1 — preda (2017-10-29T13:34:26Z)

To add a bit more detail: it appears only one kernel is affected by this random two-choice (the "tail" kernel). In the "bad" variant, this kernel is 16% slower. In practice, when I hit the "bad" compilation, I re-try the compilation until I hit on the good one. Interesting..

---

### 评论 #2 — acmeman925 (2017-10-30T20:32:55Z)

Have you observed the same behavior from the compiler before  GpuOwl at commit 28c127f?

---

### 评论 #3 — preda (2017-10-30T21:20:25Z)

I'm not sure, but I think yes it was present before. It looks like
https://github.com/RadeonOpenCompute/ROCm/issues/204
may be the same issue.


---

### 评论 #4 — preda (2017-10-31T06:14:59Z)

No, I'm using ROCm 1.6-180, as I said in the bug report.

On 31 October 2017 at 09:30, Iyad Natour <notifications@github.com> wrote:

> Are you still using for #241
> <https://github.com/RadeonOpenCompute/ROCm/issues/241> AMDGPU-pro 17.30 ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/241#issuecomment-340604482>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AArHehV6Zp07AqQ7gACARqW78FPE8troks5sxk4ZgaJpZM4QKQDO>
> .
>


---

### 评论 #5 — preda (2017-11-15T23:15:06Z)

With ROCm 1.6-180, Ubuntu 16.04.3, I clearly reproduced this bug on these hardware:

Rx Vega 64,
R9-Fury X, R9-Nano,
390x

on the 390x I can't dump ISA (ROCm doesn't support that on 390x yet), but even so the performance difference between the "good" and the "bad" compilation is radical. The "bad" compilation seems to function correctly, it's only the performance that's severely affected.


---

### 评论 #6 — preda (2018-02-08T03:17:12Z)

I can confirm this bug is still active on ROCm 1.7:
(Ubuntu 17.10, Vega 64).

Repro: build this version of GpuOwl:
https://github.com/preda/gpuowl/tree/6ab41b28bc77fb8b487419fe34c82ca2f4575a15

And execute it with -dump to get kernel disassembly.

What is happening: from exactly same OpenCL source, compiled in the same conditions, two different kernel ISAs are generated *randomly*. Just by successive invocation, you get one or the other.

One compilation has significant slower performance than the other.
good: workitem_private_segment_byte_size = 228
bad: workitem_private_segment_byte_size = 396

I attach the two ISAs generated for the same kernel, same everything.
[bad-1.7.txt](https://github.com/RadeonOpenCompute/ROCm/files/1705603/bad-1.7.txt)
[good-1.7.txt](https://github.com/RadeonOpenCompute/ROCm/files/1705604/good-1.7.txt)


---

### 评论 #7 — acmeman925 (2018-02-12T14:23:21Z)

We worked on it, and we are not observing the issue internally.  If you are able to build our opencl compiler from the truck,  I expect you will not be seeing the issue.  We are exploring the possibility of making publicly  available, on a regular basis, our internal nightly build of OpenCL.

---

### 评论 #8 — preda (2018-02-12T17:21:56Z)

I can try to build. Would you care to point me to some starting instructions? (for building the opencl compiler? llvm? and how to integrate the build into the existing ROCm installation). thanks!

(a nightly build would be useful, of course!)


---

### 评论 #9 — kzhuravl (2018-02-12T20:47:54Z)

Hi @preda,

You can build the OpenCL stack (including the compiler) by following the instructions from here:
https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/master/README.md

Here are also step by step instructions:
- Make sure you have rocm installed
- You can leave the existing rocm-opencl* packages installed
- Get the OpenCL source (including the compiler)
  - repo init -u https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git -b master -m opencl.xml
  - repo sync -j 4
- Build OpenCL:
  - mkdir opencl/build
  - cmake -DLLVM_TARGETS_TO_BUILD="AMDGPU;X86" -DCMAKE_BUILD_TYPE=Release ..
  - make -j
  - You can select additional LLVM targets to build by passing them into "-DLLVM_TARGETS_TO_BUILD"
  - You can select other build types (i.e. Release, Debug, RelWithDebInfo, MinSizeRel)
  - You can build additional compiler tools by specifying "-DLLVM_BUILD_TOOLS=ON"
- You might need to install additional dependencies, for example, mesa-common-dev, libpci-dev, libpci3

After you build it, set LD_LIBRARY_PATH environment variable to opencl/build/lib. When you run your OpenCL program with LD_LIBRARY_PATH set to opencl/build/lib, it will use your newly built OpenCL runtime.

Let me know if you encounter any issues!


---

### 评论 #10 — preda (2018-02-12T23:50:47Z)

Thank you for the build instructions! I did build successfully.

I can no longer reproduce the issue, either with stock ROCm 1.7 (strange!) or with the manual head build. So as far as I'm concerned, this bug can be closed.

(I'll keep an eye on the generated code in the future, and report back anything strange I see).


---
