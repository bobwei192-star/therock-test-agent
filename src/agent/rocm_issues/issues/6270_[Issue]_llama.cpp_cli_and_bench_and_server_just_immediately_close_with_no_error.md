# [Issue]: llama.cpp cli and bench and server just immediately close with no error at all

> **Issue #6270**
> **状态**: closed
> **创建时间**: 2026-05-18T16:31:00Z
> **更新时间**: 2026-05-25T17:39:29Z
> **关闭时间**: 2026-05-25T17:39:29Z
> **作者**: PCAssistSoftware
> **标签**: status: triage
> **URL**: https://github.com/ROCm/ROCm/issues/6270

## 标签

- **status: triage** (颜色: #585dd7)

## 负责人

- darren-amd

## 描述

### Problem Description

Using this version - https://repo.radeon.com/rocm/llama.cpp/windows/rocm-rel-7.2.1/llama-b8407-windows-rocm-7.2.1-gfx110X-gfx115X-gfx120X-x64.zip

Running any command e.g. 

.\llama-bench `
  -m "D:\Models\lmstudio-community\Qwen3.6-35B-A3B-GGUF\Qwen3.6-35B-A3B-Q4_K_M.gguf" `
 -ngl 999 `
  -fa on `
  -p 8192 `
  -n 512 `
  -b 1024 `
  -r 3

just results in immediately exiting and returning to terminal prompt with no indication of error etc

### Operating System

Windows 11 10.0.26200

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

AMD Radeon(TM) 8060S Graphics

### ROCm Version

-

### ROCm Component

_No response_

### Steps to Reproduce

as above

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

---

## 评论 (4 条)

### 评论 #1 — darren-amd (2026-05-20T19:39:41Z)

Hi @PCAssistSoftware,

Thanks for reporting the issue, I was able to reproduce this on a clean system and it was due to missing `.dll` libraries. Could you please install the Visual C++ 2015-2022 Redistributables as suggested [here](https://rocm.docs.amd.com/projects/radeon-ryzen/en/docs-7.1.1/docs/limitations/limitationsryz.html#windows) as well as LLVM, and confirm if the issue persists?

On my system, `libomp140.x86_64.dll` wasn't being found properly so I had to copy and rename `libomp.dll` from the LLVM bin folder into the llama folder.

---

### 评论 #2 — PCAssistSoftware (2026-05-20T20:13:03Z)

Hi, thanks for testing. The computer I am using already had Visual C++ 2015-2022 redistributables installed, but I have reinstalled them just in case.  I also downloaded the latest archive from https://github.com/llvm/llvm-project/releases/tag/llvmorg-22.1.6 and copied the libomp.dll into the extracted llama folder e.g. \llama_cpp_binaries\llama-b8407-windows-rocm-7.2.1-gfx110X-gfx115X-gfx120X-x64, but it sill doesn't work, just exist immediately with no error or indication of the problem.

Have used multiple other versions of llama.cpp (e.g. CPU, Vulkan and HIP versions from https://github.com/ggml-org/llama.cpp/releases/tag/b9253) and the latest ROCm nightly from https://github.com/lemonade-sdk/llamacpp-rocm - and these all work without a problem.

Anything I can do to test / diagnose please let me know

---

### 评论 #3 — PCAssistSoftware (2026-05-20T20:54:33Z)

EDIT: I just re-read your response and noted that I had missed a step, I had copied the libomp.dll over but had not renamed it.  Now renamed it to libomp140.x86_64.dll and it has resolved the problem.

Will this file be included in the archive in future rather than having to manually copy it each time?

---

### 评论 #4 — darren-amd (2026-05-25T17:39:29Z)

Hi @PCAssistSoftware,

Thanks for confirming that it is working for you now. Had a chat with the team and we most likely will not be releasing pre-build binaries in the future, I'd suggest either using upstream llama.cpp builds or [lemonade-sdk](https://github.com/lemonade-sdk/llamacpp-rocm) in the future, thanks!

---
