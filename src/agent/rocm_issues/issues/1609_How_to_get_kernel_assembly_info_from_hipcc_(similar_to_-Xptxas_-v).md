# How to get kernel assembly info from hipcc (similar to -Xptxas -v)?

> **Issue #1609**
> **状态**: closed
> **创建时间**: 2021-11-03T19:15:46Z
> **更新时间**: 2024-03-12T23:54:01Z
> **关闭时间**: 2021-11-15T08:01:22Z
> **作者**: ravil-mobile
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1609

## 描述

Hi everyone, 

I am trying to find a compiler flag (similar to -Xptxas -v in nvcc) to print out kernel information e.g., num. registers per thread, register spills, shared memory usage, etc. Does anybody know which flag I should use?

I am using HIP version 4.2.21155-37cb3a34 and compiling for gfx908 architecture. 

Thanks in advance!

---

## 评论 (5 条)

### 评论 #1 — ex-rzr (2021-11-05T10:32:25Z)

`hipcc -save-temps ...` creates `*gfx*.s` files, there is a block after each kernel with the number of registers (scalar, vector), a size of scratch memory (i.e. spilling), occupancy.


---

### 评论 #2 — ROCmSupport (2021-11-10T10:06:13Z)

Thanks @ravil-mobile for reaching out. I understood the problem.
Let me talk to Compiler/HIP team for better information. Thank you.

---

### 评论 #3 — ravil-mobile (2021-11-12T16:17:28Z)

@ex-rzr, many thanks! it was exactly was I was looking for

---

### 评论 #4 — ROCmSupport (2021-11-15T08:01:22Z)

Hi @ravil-mobile 
Yes, You can compile with -save-temps, then check the dumped .s file.
Thanks @ex-rzr for helping in parallel.
Hope you are satisfied with the resolution. I am closing it.
Feel free to open a new issue, if any, for quick resolution.
Thank you.

---

### 评论 #5 — ravil-mobile (2024-03-12T23:54:00Z)

Now, `amdclang` compiler has `-Rpass-analysis=kernel-resource-usage` backend-flag which generates kernel resource usage to the standard output. 

```bash
main.cpp:9:1: remark: Function Name: _Z10helloworldPcS_ [-Rpass-analysis=kernel-resource-usage]
    9 | __global__ void helloworld(char* in, char* out) {
      | ^
main.cpp:9:1: remark:     SGPRs: 36 [-Rpass-analysis=kernel-resource-usage]
main.cpp:9:1: remark:     VGPRs: 32 [-Rpass-analysis=kernel-resource-usage]
main.cpp:9:1: remark:     ScratchSize [bytes/lane]: 196 [-Rpass-analysis=kernel-resource-usage]
main.cpp:9:1: remark:     Dynamic Stack: False [-Rpass-analysis=kernel-resource-usage]
main.cpp:9:1: remark:     Occupancy [waves/SIMD]: 16 [-Rpass-analysis=kernel-resource-usage]
main.cpp:9:1: remark:     SGPRs Spill: 9 [-Rpass-analysis=kernel-resource-usage]
main.cpp:9:1: remark:     VGPRs Spill: 7 [-Rpass-analysis=kernel-resource-usage]
main.cpp:9:1: remark:     LDS Size [bytes/block]: 0 [-Rpass-analysis=kernel-resource-usage]
```

---
