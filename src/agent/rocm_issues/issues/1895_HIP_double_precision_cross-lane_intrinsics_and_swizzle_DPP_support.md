# HIP double precision cross-lane intrinsics and swizzle / DPP support

> **Issue #1895**
> **状态**: closed
> **创建时间**: 2023-01-21T09:09:28Z
> **更新时间**: 2024-05-12T22:00:24Z
> **关闭时间**: 2024-05-12T22:00:24Z
> **作者**: nschaeff
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1895

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

Hello,
Using HIP, I currently perform cross-lane reductions with `__shfl_xor()` instructions.
These seem to be a perfect match for the  ds_swizzle_b32 instruction [1], but when looking at the assembly generated, it seems only ds_(b)permute_b32 instructions are generated.
The performance is impacted: many instructions are used to generate the addressing of lanes, while ds_swizzle_b32 require none if I understand correctly.
Furthermore, ref [1] also says that cross-lane data exchange can be performed at full throughput using DPP modifiers.
Things like
      `x += __shfl_down(y, 1, 16);`
could be translated into a single instruction add with DPP modifier if I understand correctly.

But anyway, maybe the compiler can't do it due to some limitations. Could we then have intrinsics that do the job, including for double-precision values ? The intrinsics I've seen are limited to 32-bit words...
Has someone advice as to how to get decent performance for such cross-lane operations in HIP targeted at AMD CDNA ?
If possible, I would like to avoid inline asm, as it is said it disables many compiler optimizations.

Thanks a lot!

[1] https://gpuopen.com/learn/amd-gcn-assembly-cross-lane-operations/

---

## 评论 (3 条)

### 评论 #1 — nschaeff (2023-01-26T09:53:57Z)

As workaround, I have written the following shfl_* replacements that select the fastest cross-lane instructions (DPP if possible, then ds_swizzle_b32, and finally ds_bpermute_b32 if the previous two do not cover the required exchange pattern.
https://bitbucket.org/nschaeff/workspace/snippets/k74rab

Question remains: does fp64 instructions support DPP modifiers ? Contradictory informations can be fond in https://developer.amd.com/wp-content/resources/CDNA2_Shader_ISA_4February2022.pdf
Page 2, Feature Changes in MI200 devices says that MI200 "Supports DPP for 64-bit data types".
But later, section 13.3.9 says DPP modifier applies to VOP1, VOP2 or VOPC instructions, while v_add_f64 (for instance) is a VOP3 instruction... 

---

### 评论 #2 — jlgreathouse (2024-02-03T03:18:29Z)

Hi @nschaeff 

First, as for why we do not currently generate DS_SWIZZLE operations when using __shfl_xor(). The __shfl operations take in a per-lane variable as the laneMask argument. This means that the [functional implementation](https://github.com/ROCm/clr/blob/28743d8dbd47423ce5b97e7b6931e3db25f22d68/hipamd/include/hip/amd_detail/amd_warp_functions.h#L435) of this takes in a variable that is not known at compile time.

The DS_SWIZZLE instruction, however, requires the swizzle pattern to be known at compile time, because the pattern is encoded in the instruction itself (rather than coming in from a register holding a variable value). DPP has the same limitation.

We do include compiler builtins to directly access DPP operations, and I see you found at least one of them. Since I'm answering this in a way that others might see, I must warn everyone that compiler builtins like this are not a stable API and the Clang compiler may change them in the future. We also do not guarantee that these builtins will work on all AMD GPUs now or in the future. That said, the [__builtin_amdgcn_update_dpp()](https://github.com/llvm/llvm-project/blob/42d6eb54752c37c2583301158e30648cf09195a4/clang/include/clang/Basic/BuiltinsAMDGPU.def#L212) operation can be used to implement cross-lane operations; for example [see here](https://github.com/gromacs/gromacs/blob/373287336464811df7429ab6eea080b52290e970/src/gromacs/gpu_utils/sycl_kernel_utils.h#L347). I see that you used __builtin_amdgcn_mov_dpp(), but if I remember correctly, we tend to prefer that developers use the latter because it lets our compiler more aggressively try to combine the DPP movement operation with later math ops into a single DPP math op.

In the CDNA2 and CDNA3 ISAs, the following are the only F64-input instructions that support DPP:

- F64-input instructions in the VOP2 space with DPP support
  - V_FMAC_F64
- F64-input instructions in the VOP1 space with DPP support
  - V_CEIL_F64
  - V_CVT_F32_F64
  - V_CVT_I32_F64
  - V_CVT_U32_F64
  - V_FLOOR_F64
  - V_FRACT_F64
  - V_FREXP_EXP_I32_F64
  - V_FREXP_MANT_F64
  - V_TRUNC_F64

And the only DPP Control values that F64-input instructions support are DPP_ROW*, i.e. control values 0x150-0x15F. The encodings are incorrectly stated as 0x150-0x165 in the ISA guides. The 15 DPP_ROW encodings are actually 0x150-0x15F

---

### 评论 #3 — ppanchad-amd (2024-05-09T20:16:14Z)

@nschaeff Do you still need any additional assistance with this ticket? If not, please close this ticket. Thanks!

---
