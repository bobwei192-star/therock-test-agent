# OpenCL codegen: disable FP IEEE_mode on -cl-fast-relaxed-math

> **Issue #967**
> **状态**: closed
> **创建时间**: 2019-12-15T07:16:54Z
> **更新时间**: 2024-10-17T16:01:23Z
> **关闭时间**: 2024-10-17T16:01:23Z
> **作者**: preda
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/967

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

See #964 for context.
When OpenCL compilation is done with -cl-fast-relaxed-math (or maybe even just -cl-finite-math-only) disable FP IEEE_mode.

Why: this allows more efficient code to be generated, and that's exactly the intention of -cl-fast-relaxed-math. The generated code is potentially more efficient with IEEE_mode disabled because e.g. output-modifiers (mul:2) can be used, which are otherwise disabled in IEEE_mode.

Additionally, there is no other mecanism currently to control IEEE_mode in OpenCL.

---

## 评论 (6 条)

### 评论 #1 — tasso (2023-12-19T16:44:42Z)

Is this still an issue?  If not, can we please close it?  Thanks!

---

### 评论 #2 — tasso (2023-12-22T13:18:15Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks

---

### 评论 #3 — preda (2024-01-23T10:26:14Z)

Please reopen, this is still an issue and not fixed.

---

### 评论 #4 — nartmada (2024-01-23T12:47:30Z)

Reopening the ticket.  An internal ticket is created for investigation.

---

### 评论 #5 — sohaibnd (2024-10-16T17:59:02Z)

Hi @preda, thanks for waiting. Have you tried using the `-mno-amdgpu-ieee`  and `-fno-honor-nans` compiler options ([see clang doc](https://rocm.docs.amd.com/projects/llvm-project/en/latest/LLVM/clang/html/ClangCommandLineReference.html#cmdoption-clang-mamdgpu-ieee))? That should disable IEEE mode.

---

### 评论 #6 — jamesxu2 (2024-10-17T16:01:23Z)

Hi @preda , I think we will continue discussion of this issue here: https://github.com/ROCm/ROCm/issues/1405

Like @sohaibnd said, ```mno-amdgpu-ieee``` is a Clang flag that does work on latest ROCm clang-18, which allows control over FP IEEE mode. It must be combined with ```-fno-honor-nans```, and there is a pretty extended discussion of this in the [LLVM code review](https://reviews.llvm.org/D77013). However, like you mention in the other ticket, there is currently no way to pass these into the OpenCL runtime compiler.  

Regarding this request: 
> When OpenCL compilation is done with -cl-fast-relaxed-math (or maybe even just -cl-finite-math-only) disable FP IEEE_mode.

Changing the default fp mode register was considered an ABI break ([ref](https://clang.llvm.org/docs/ClangCommandLineReference.html#cmdoption-clang-mamdgpu-ieee)). This would've led to unexpected behaviour when combining different translation units with different fast math modes, had we decided to imply the FP IEEE mode as a part of the fast math flag. So, this setting can only be specified using -m[no]-amdgpu-ieee, to make this ABI break more explicit.

I'll continue investigating in the other ticket, as I'm trying to find out how much work needs to be done to pass this functionality through clBuildProgram. It's definitely not a valid option for that compiler at this time ([ref](https://github.com/ROCm/clr/blob/364dfb0ed16e110f43d13f73e05da00605989486/rocclr/compiler/lib/utils/OPTIONS.def#L21-L40)). 

So, we'll continue this discussion on the status of implementing this:
> [a] mecanism currently to control IEEE_mode in OpenCL

In the FR ticket you made here: https://github.com/ROCm/ROCm/issues/1405

---
