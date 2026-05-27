# Inline assembly Mul:2 Div:2 modifiers ignored

> **Issue #964**
> **状态**: closed
> **创建时间**: 2019-12-14T05:06:08Z
> **更新时间**: 2023-12-18T19:33:53Z
> **关闭时间**: 2023-12-18T19:33:53Z
> **作者**: gwoltman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/964

## 描述

Take any working code with inline assembly.  Add mul:2 or div:2 modifiers to the assembly and your code will still work!

This is the assembly code I wrote to calculate tmp = 2 * a.x * a.y:
              __asm( "v_mul_f64 %0, %1, %2 mul:2\n" : "=v" (tmp) : "v" (a.x), "v" (a.y)); 


---

## 评论 (9 条)

### 评论 #1 — b-sumner (2019-12-14T16:52:44Z)

Unfortunately, the documentation doesn't really spell out the fact that output modifiers are not compatible with denorms enabled, nor are they compatible with IEEE mode, and you are likely using both.

---

### 评论 #2 — preda (2019-12-14T20:32:43Z)

How can IEEE mode be controlled in OpenCL? (or controlled at all). What would disabling IEEE mode entail?

The app is already using -cl-fast-relaxed-math with should disable denorms, so no denorms are not enabled.


---

### 评论 #3 — b-sumner (2019-12-14T21:41:15Z)

There is a whole section on the MODE register in the ISA document.  (Latest vega 7nm guide here: https://gpuopen.com/wp-content/uploads/2019/11/Vega_7nm_Shader_ISA_26November2019.pdf )

There are no compiler options to directly manipulate any MODE register fields.  I need to check on whether we turn off IEEE when flushing denorms.  Can you comment on why you're flushing denorms?

---

### 评论 #4 — preda (2019-12-15T05:36:38Z)

I see in the kernel ISA dump that the float_mode is always 240 (0xF0). This is for a compilation done with -cl-fast-relaxed-math.

```
	.amd_kernel_code_t
		amd_code_version_major = 1
		amd_code_version_minor = 2
		amd_machine_kind = 1
		amd_machine_version_major = 9
		amd_machine_version_minor = 0
		amd_machine_version_stepping = 6
		kernel_code_entry_byte_offset = 256
		kernel_code_prefetch_byte_size = 0
		granulated_workitem_vgpr_count = 3
		granulated_wavefront_sgpr_count = 3
		priority = 0
		float_mode = 240
                priv = 0
		enable_dx10_clamp = 1
		debug_mode = 0
		enable_ieee_mode = 1
```

According to the OpenCL docs https://www.khronos.org/registry/OpenCL/sdk/2.0/docs/man/xhtml/clBuildProgram.html

-cl-fast-relaxed-math:
Sets the optimization options -cl-finite-math-only and -cl-unsafe-math-optimizations. This allows optimizations for floating-point arithmetic that may violate the IEEE 754 standard and the OpenCL numerical compliance requirements defined in the specification in section 7.4 for single-precision and double precision floating-point, and edge case behavior in section 7.5. This option also relaxes the precision of commonly used math functions (refer to table 7.2 defined in section 7.4). This option causes the preprocessor macro __FAST_RELAXED_MATH__ to be defined in the OpenCL program. 

-cl-unsafe-math-optimizations:
    Allow optimizations for floating-point arithmetic that (a) assume that arguments and results are valid, (b) may violate IEEE 754 standard and (c) may violate the OpenCL numerical compliance requirements as defined in section 7.4 for single precision and double precision floating-point, and edge case behavior in section 7.5. This option includes the -cl-no-signed-zeros and -cl-mad-enable options. 

-cl-finite-math-only:
    Allow optimizations for floating-point arithmetic that assume that arguments and results are not NaNs or ±∞. This option may violate the OpenCL numerical compliance requirements defined in section 7.4 for single precision and double precision floating point, and edge case behavior in section 7.5. 

So the OpenCL doc seems to suggest that IEEE_MODE should be disabled when -cl-fast-relaxed-math is requested. This becomes more important as there is no other way to disable IEEE_MODE in OpenCL.


---

### 评论 #5 — preda (2019-12-15T05:42:13Z)

I would associate IEEE_MODE with -cl-finite-math-only (vs. flushing of denormals), as IEEE_MODE in my reading from the ISA doc seems to be concerned with the handling of NaNs and maybe INFs.


---

### 评论 #6 — preda (2019-12-15T06:23:24Z)

After more careful consideration, I see that  *float_mode = 240* indicates that denorms aren't flushed (top 4 bits), and there is a separate enable_ieee_mode which is set. So the question becomes, is this the intended behavior of -cl-fast-relaxed-math ?

---

### 评论 #7 — gwoltman (2019-12-17T01:10:51Z)

I can confirm that adding these two lines to the start of the kernel fixes the problem.  I'll leave it to others to work out whether the OpenCL -cl-fast-relaxed-math switch is setting bits properly.

 

`__asm("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 9, 1), 0\n");
 __asm("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 4, 4), 5\n"); `

---

### 评论 #8 — nartmada (2023-12-13T22:40:52Z)

Hi @gwoltman, please close this ticket if your issue has been resolved.  Thanks.

---

### 评论 #9 — gwoltman (2023-12-18T19:33:53Z)

Closing ticket.  I'm no longer doing Radeon VII development work.

---
