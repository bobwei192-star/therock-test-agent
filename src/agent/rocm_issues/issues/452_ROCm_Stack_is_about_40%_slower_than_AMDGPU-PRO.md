# ROCm Stack is about 40% slower than AMDGPU-PRO 

> **Issue #452**
> **状态**: closed
> **创建时间**: 2018-07-07T13:31:18Z
> **更新时间**: 2018-07-07T14:59:05Z
> **关闭时间**: 2018-07-07T14:59:05Z
> **作者**: robinchrist
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/452

## 描述

Hi,

Well... The ROCm stack is a nice thing, but it's so horribly slow!

For a Boundary Element Method solver, I utilize the GPU via OpenCL.
The application I developed has a small benchmark tool, which calculates the number of integrals calculated per second.

WIth AMDGPU-PRO 18.20-606296 (Ubuntu 16.04.4, Kernel 4.15) I get around 5.1GInt/s (Gigaintegrals per second) at n = 22000. With ROCm (Ubuntu 16.04.4, Kernel 4.13), I get around 3.18GInt/s.
GPU is Radeon Vega Frontier

The only problem with AMDGPU-PRO is that I cannot allocate Buffers larger than 4GByte... With ROCm I can.

//EDIT:
When adding ` -cl-denorms-are-zero` to the OpenCL kernel compilation parameters with ROCm, the performance is identical. Flags are `-O3 -cl-no-signed-zeros`

Does the AMDGPU-PRO driver automatically add this flag?

---

## 评论 (2 条)

### 评论 #1 — briansp2020 (2018-07-07T14:12:04Z)

I think you figured out the problem yourself.

https://github.com/RadeonOpenCompute/ROCm/issues/421

---

### 评论 #2 — gstoner (2018-07-07T14:59:05Z)

@robinchrist   The default behavior AMDGPU pro is with denorms off.   Note as i said before the AMDGPUpro is using a different compiler. LLVM to HSAIl - > HSAIL -SC ( Shader Compiler - It is not Open Source).

ROCm compiler is based on fulll LLVM compiler flow ( all three stages FE, Optimizer, Code Generator ). This is no Intermediate IL ( Like  HSAIL or PTX)  in the code generation path.  

Yes we had with   ROCm LLVM compiler denorm on by default.    As you can see you set flag to shut them off 

You can find out more about the new compiler at https://llvm.org/docs/AMDGPUUsage.html  

---
