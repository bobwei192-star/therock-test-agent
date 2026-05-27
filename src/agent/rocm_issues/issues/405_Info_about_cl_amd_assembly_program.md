# Info about cl_amd_assembly_program?

> **Issue #405**
> **状态**: closed
> **创建时间**: 2018-05-08T05:22:39Z
> **更新时间**: 2018-05-09T04:13:40Z
> **关闭时间**: 2018-05-09T04:13:40Z
> **作者**: oscarbg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/405

## 描述

Hi,
finally installed ROCM 1.7.2 on Ubuntu 18.04 via kernel 4.13 from PPA..
now seeing clinfo I see:
version  2576.0 (HSA1.1,LC)
and a new extension  cl_amd_assembly_program ..
searching seems it has clCreateProgramWithAssemblyAMD but quick inspection 
on api/opencl/amdocl/cl_program.cpp doesn't reveal many details..

that allows inline assembly?
also there is some sample of using it?

thanks..


---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2018-05-08T15:39:23Z)

Hello @oscarbg ,

This extension allows the creation of kernels from full assembly source code. In other words, rather than writing OpenCL device-side code in [OpenCL C](https://www.khronos.org/registry/OpenCL/specs/opencl-2.0-openclc.pdf), you would instead write the kernels purely in GCN assembly. Examples of kernels written purely in assembly can be found, for example, in [our MIOpen library](https://github.com/ROCmSoftwarePlatform/MIOpen/tree/master/src/kernels). (See the .s files).

You would pass this kernel assembly text into `clCreateProgramWithAssemblyAMD()` instead of passing OpenCL text, both of which are passed to their respective functions as strings. The result would return a `cl_program` as if you had called `clCreateProgramWithSource()`. You would later need to call `clBuildProgram()` on this object.

At the moment, we don't have a public example in e.g. MIOpen about doing this -- MIOpen builds its kernels directly using the Clang OpenCL compiler and then brings those objects into the program. However, `clCreateProgramWithAssemblyAMD()` essentially does the same thing without needing to manually fork off a separate process.


If you are, instead, looking for *inline* assembly, that has been available for quite a while and is easier to use. See, for example, our [inline assembly examples for HIP](https://github.com/ROCm-Developer-Tools/HIP/tree/master/samples/2_Cookbook/10_inline_asm). While these examples are used in HIP kernels, the same mechanism is available in our OpenCL kernels. Essentially, you can add in an `__asm__ __volatile__("asm_goes_here" : output_constraints : input_constraints : clobber_list);` statement directly into your OpenCL C kernel code. So long as your AMD-provided OpenCL runtime is using Clang as its compiler (e.g. ROCm does this, I believe newer versions of AMDGPU-Pro also do this), it will insert this assembly directly into your kernel.

The following links may be helpful if you plan on doing this:
- [The ISA manual for our Vega GPUs](https://developer.amd.com/wordpress/media/2017/08/Vega_Shader_ISA_28July2017.pdf)
- [How to define constraints for GCN assembly](http://llvm.org/docs/AMDGPUOperandSyntax.html)
- [An example of inline assembly in an old version of an MIOpen kernel](https://github.com/AMDComputeLibraries/MLOpen/blob/448b648cc670d781c3089a9ecd935a86a13229c3/src/kernels/MIOpenBatchNormFwdTrainSpatial.cl)

---

### 评论 #2 — oscarbg (2018-05-09T04:13:20Z)

thanks for fast and very informative answer..
will give a test shortly..


2018-05-08 17:39 GMT+02:00 Joseph Greathouse <notifications@github.com>:

> Hello @oscarbg <https://github.com/oscarbg> ,
>
> This extension allows the creation of kernels from full assembly source
> code. In other words, rather than writing OpenCL device-side code in OpenCL
> C <https://www.khronos.org/registry/OpenCL/specs/opencl-2.0-openclc.pdf>,
> you would instead write the kernels purely in GCN assembly. Examples of
> kernels written purely in assembly can be found, for example, in our
> MIOpen library
> <https://github.com/ROCmSoftwarePlatform/MIOpen/tree/master/src/kernels>.
> (See the .s files).
>
> You would pass this kernel assembly text into
> clCreateProgramWithAssemblyAMD() instead of passing OpenCL text, both of
> which are passed to their respective functions as strings. The result would
> return a cl_program as if you had called clCreateProgramWithSource(). You
> would later need to call clBuildProgram() on this object.
>
> At the moment, we don't have a public example in e.g. MIOpen about doing
> this -- MIOpen builds its kernels directly using the Clang OpenCL compiler
> and then brings those objects into the program. However,
> clCreateProgramWithAssemblyAMD() essentially does the same thing without
> needing to manually fork off a separate process.
>
> If you are, instead, looking for *inline* assembly, that has been
> available for quite a while and is easier to use. See, for example, our inline
> assembly examples for HIP
> <https://github.com/ROCm-Developer-Tools/HIP/tree/master/samples/2_Cookbook/10_inline_asm>.
> While these examples are used in HIP kernels, the same mechanism is
> available in our OpenCL kernels. Essentially, you can add in an __asm__
> __volatile__("asm_goes_here" : output_constraints : input_constraints :
> clobber_list); statement directly into your OpenCL C kernel code. So long
> as your AMD-provided OpenCL runtime is using Clang as its compiler (e.g.
> ROCm does this, I believe newer versions of AMDGPU-Pro also do this), it
> will insert this assembly directly into your kernel.
>
> The following links may be helpful if you plan on doing this:
>
>    - The ISA manual for our Vega GPUs
>    <https://developer.amd.com/wordpress/media/2017/08/Vega_Shader_ISA_28July2017.pdf>
>    - How to define constraints for GCN assembly
>    <http://llvm.org/docs/AMDGPUOperandSyntax.html>
>    - An example of inline assembly in an old version of an MIOpen kernel
>    <https://github.com/AMDComputeLibraries/MLOpen/blob/448b648cc670d781c3089a9ecd935a86a13229c3/src/kernels/MIOpenBatchNormFwdTrainSpatial.cl>
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/405#issuecomment-387446365>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAo2eZQ-Hl61oY2wjMuZCfm9Ln26meilks5twbwvgaJpZM4T2CBp>
> .
>


---
