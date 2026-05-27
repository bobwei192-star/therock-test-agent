# GCN disassembler tools

> **Issue #1258**
> **状态**: closed
> **创建时间**: 2020-10-13T05:27:17Z
> **更新时间**: 2020-10-14T14:39:32Z
> **关闭时间**: 2020-10-14T14:39:32Z
> **作者**: lscat11
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1258

## 描述

Hi, recently I wanted to disassemble a kernel binary file *.co into assembly code *.s. I have tried the tools listed in [https://rocmdocs.amd.com/en/latest/Programming_Guides/gcn-assembler.html](https://rocmdocs.amd.com/en/latest/Programming_Guides/gcn-assembler.html), but it seems that these tools could not generate a complete assembly code file. So, does ROCm provide such a disassembler tool?

---

## 评论 (1 条)

### 评论 #1 — seesturm (2020-10-13T06:31:19Z)

Don't know such a tool. llvm-objdump can show disassembly, but cannot produce source file for (re-)assembly.

Only known method for producing *.s files known to me is setting environment variables before running OpenCL/HIP application according to #726 
```
export KMDUMPISA=1
export AMD_OCL_BUILD_OPTIONS_APPEND="-save-temps -g"
```

---
