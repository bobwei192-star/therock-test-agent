# need asm instruction set for AMD

> **Issue #1209**
> **状态**: closed
> **创建时间**: 2020-09-01T11:06:12Z
> **更新时间**: 2024-10-06T08:04:19Z
> **关闭时间**: 2020-09-09T22:51:31Z
> **作者**: srinivaskakarla
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/1209

## 标签

- **Question** (颜色: #cc317c)

## 描述

Hi  ,

Here is the asm example for  Nvidia .

_device__ inline void load_streaming_double2(double2 &a, const double2* addr)
  {   
    // double x, y;
    asm("ld.cs.global.v2.f64 {%0, %1}, [%2+0];" : "=d"(x), "=d"(y) : __PTR(addr));
    // a.x = x;  a.y = y;
  }
 I could find any asm instruction set for AMD,
 Can you please help me reference documents or  asm instruction set for  AMD .


Regards,
Srinivas


---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2020-09-09T22:51:31Z)

ISA documents for various generations of our GPUs:

- gfx7: http://developer.amd.com/wordpress/media/2013/07/AMD_Sea_Islands_Instruction_Set_Architecture.pdf
- gfx8: https://32ipi028l5q82yhj72224m8j-wpengine.netdna-ssl.com/wp-content/uploads/2016/08/AMD_GCN3_Instruction_Set_Architecture_rev1.1.pdf
- gfx900: https://developer.amd.com/wordpress/media/2017/08/Vega_Shader_ISA_28July2017.pdf
- gfx906: https://gpuopen.com/wp-content/uploads/2019/11/Vega_7nm_Shader_ISA_26November2019.pdf
- gfx908: https://developer.amd.com/wp-content/resources/CDNA1_Shader_ISA_14December2020.pdf
- gfx10.1: https://developer.amd.com/wp-content/resources/RDNA_Shader_ISA.pdf
- gfx10.3: https://developer.amd.com/wp-content/resources/RDNA2_Shader_ISA_November2020.pdf

We support inline assembly code in our HIP and OpenCL kernels, an example of using inline ASM in HIP can be found here: https://github.com/ROCm-Developer-Tools/HIP/blob/master/samples/2_Cookbook/10_inline_asm/inline_asm.cpp#L41. Inline assembly in our LLVM-based compilers uses [normal LLVM inline asm syntax](https://llvm.org/docs/LangRef.html#supported-constraint-code-list). There are some extensions (such as how to target scalar vs. vector registers) that can be found [here](http://llvm.org/docs/AMDGPUOperandSyntax.html) and [here](https://github.com/llvm-mirror/llvm/blob/master/docs/AMDGPUModifierSyntax.rst).

However, it's strongly recommended that you use compiler buildtins/intrinsics instead of inline assembly if possible. Inline ASM blocks defeat many of our compiler optimization passes, and are fraught with potential corner-case bugs. You can find our LLVM-based compilers' lists of supported builtin operations [here](https://github.com/llvm-mirror/clang/blob/master/include/clang/Basic/BuiltinsAMDGPU.def). Deeper details [here](https://github.com/llvm-mirror/llvm/blob/master/include/llvm/IR/IntrinsicsAMDGPU.td).

We also support writing kernels entirely in assembly and loading them directly in your application. See [our MIOpen library](https://github.com/ROCmSoftwarePlatform/MIOpen/tree/develop/src/kernels) as an example of this.

See also:
- https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/43#issuecomment-423001693
- https://github.com/RadeonOpenCompute/ROCm/issues/405#issuecomment-387446365

---

### 评论 #2 — yiakwy-xpu-ml-framework-team (2024-09-29T10:12:50Z)

@jlgreathouse Great anwser.

@srinivaskakarla As for v_mfma instruction I also recommend AMD research notes : https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-matrix-cores-readme/

Unfortunately, the post only provides anlaysis of few v_mfma instructions:

- [V_MFMA_F32_16x16x4F32](https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-matrix-cores-readme/#example-1-v-mfma-f32-16x16x4f32)
- [V_MFMA_F32_16x16x1F32](https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-matrix-cores-readme/#example-2-v-mfma-f32-16x16x1f32)
- [V_MFMA_F64_4x4x4F64](https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-matrix-cores-readme/#example-3-v-mfma-f64-4x4x4f64)

Recently I am analyzing the fragment layout of **v_mfma_fp32_16x16x16_fp16**, add single warp execution example for demonstration:

- V_MFMA_F32_16x16x16_FP16 :  https://github.com/ROCm/rocWMMA/issues/444

I am also interested in equivalent ldmatirx (with swizzle effects, see PTX 8.5 threads configuration of fragments and its memory layout) in AMD. If you know any examples about, simply ping me @jlgreathouse 

---
