# Memory access fault on ROCm 2.0, but code works fine on Windows

> **Issue #664**
> **状态**: closed
> **创建时间**: 2019-01-06T14:20:33Z
> **更新时间**: 2019-01-07T23:02:05Z
> **关闭时间**: 2019-01-07T23:02:05Z
> **作者**: arakan94
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/664

## 描述

My platform:
Ubuntu 18.04
ROCm 2.0
Radeon RX 580

Error message:
Memory access fault by GPU node-1 (Agent handle: 0x561756df8460) on address 0x501006000. Reason: Page not present or supervisor privilege.

Code:
[rocm_crash.zip](https://github.com/RadeonOpenCompute/ROCm/files/2730523/rocm_crash.zip)

Description:
Same code works fine on Windows 10, Visual Studio 2017 and this SDK [https://github.com/GPUOpen-LibrariesAndSDKs/OCL-SDK/releases](url).

I am not sure what to do next to determine cause of this error or what it even means. Perhaps it's problem in ROCm itself, which is why I post it here - feel free to try the code or instruct me what to do to debug this.

Note:
Tried running it as root without change.

---

## 评论 (2 条)

### 评论 #1 — Moading (2019-01-06T19:23:28Z)

Hi,
in my experience, this error is caused by an out of bounds memory access in one of your kernels. I have encountered similar messages when running my code in ROCm. After fixing the out of bounds memory access, the message disapeared. However, the search for this type of error is tiresome :)
I guess ROCm is less tolerant when out of bounds memory access occurs.

---

### 评论 #2 — jlgreathouse (2019-01-07T23:02:05Z)


Hi @arakan94 

I agree with @Moading. ROCm is slightly more stringent with its memory access policies than many other OpenCL implementations. In particular, ROCm can create buffers using 4 KiB virtual memory pages, while many other implementations use 64 KiB pages. If you overflow one of the 4 KiB pages, it may cause a page fault on your GPU, leading to the error you see. If, however, your kernel would not overflow a 64 KiB page, you might not see the error on a different platform.

You may want to try running your kernel with [clARMOR](https://github.com/ROCm-Developer-Tools/clARMOR) to see if it detects an overflow within your kernels. Whenever I run your test zip file within the current of clARMOR ([19.01](https://github.com/ROCm-Developer-Tools/clARMOR/tree/19.01)), I see that by the 8th iteration (after "Global size 2048"), multiple iterations of the the `bitonic_sort` kernel starts causing write overflows on the buffer `input`. As such, this problem is appearing in kernels before it starts causing crashes.

However, by the iteration after "Global size 65536", this overflow is eventually reaching beyond the allocated pages and causing a segfault.

Because I'm able to observe buffer overflows in your kernels, at this time I do not believe the error to be a ROCm problem. As such, I'm going to close this ticket. If you fix these problems and your program causes ROCm software to crash in some way, please feel free to open a new ticket or potentially reopen this one.

---
