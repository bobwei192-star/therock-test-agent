# OpenCL: -cl-denorms-are-zero affects SP but not DP

> **Issue #966**
> **状态**: closed
> **创建时间**: 2019-12-15T06:40:33Z
> **更新时间**: 2019-12-15T20:31:43Z
> **关闭时间**: 2019-12-15T20:31:43Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/966

## 描述

With ROCm 2.10, specifying -cl-denorms-are-zero at the OpenCL compilation changes the float_mode of the generated kernel from 240 (0xF0) to 192 (0xC0), so it seems that -cl-denorms-are-zero only affects the denorms flag of single precision but not that of double precision. Is this the intended behavior?

To repro: compile any OpenCL kernel with/without -cl-denorms-are-zero, and dump the generated ISA, looking for float_mode in kernel header.

---

## 评论 (4 条)

### 评论 #1 — preda (2019-12-15T06:59:50Z)

This is with ROCm 2.10:
```
                .amdhsa_float_round_mode_32 0
		.amdhsa_float_round_mode_16_64 0
		.amdhsa_float_denorm_mode_32 0
		.amdhsa_float_denorm_mode_16_64 3
		.amdhsa_dx10_clamp 1
		.amdhsa_ieee_mode 1
```
("float_mode" mentioned before was printed by ROCm 2.5)
the situation is the same though, denorm_mode_32 is 0 but denorm_16_64 is 3 (i.e. unaffected by -cl-denorms-are-zero)

---

### 评论 #2 — b-sumner (2019-12-15T17:13:22Z)

That is indeed the intended behavior.  From the start, OpenCL intended double precision computation to be as accurate, and as similar to CPU behavior as possible.

Also note that -cl-denorms-are-zero is an optimization option which implementations are free to handle as they chose.

Older GPUs and certain current embeddd GPUs save power at the expense of accuracy by not supporting f32 denorms and not supporting f64 at all.  But most modern compute GPUs support deorms, and most users want CPU matching results.

---

### 评论 #3 — preda (2019-12-15T20:19:40Z)

OK thank you, feel free to close the issue.

This is the OpenCL wording on this:
https://www.khronos.org/registry/OpenCL/sdk/2.1/docs/man/xhtml/

-cl-denorms-are-zero
    This option controls how single precision and double precision denormalized numbers are handled. If specified as a build option, the single precision denormalized numbers may be flushed to zero; double precision denormalized numbers may also be flushed to zero if the optional extension for double precsion is supported. This is intended to be a performance hint and the OpenCL compiler can choose not to flush denorms to zero if the device supports single precision (or double precision) denormalized numbers.
    This option is ignored for single precision numbers if the device does not support single precision denormalized numbers i.e. CL_FP_DENORM bit is not set in CL_DEVICE_SINGLE_FP_CONFIG.
    This option is ignored for double precision numbers if the device does not support double precision or if it does support double precison but not double precision denormalized numbers i.e. CL_FP_DENORM bit is not set in CL_DEVICE_DOUBLE_FP_CONFIG.
    This flag only applies for scalar and vector single precision floating-point variables and computations on these floating-point variables inside a program. It does not apply to reading from or writing to image objects.


---

### 评论 #4 — b-sumner (2019-12-15T20:31:43Z)

Thanks @preda .  Closing.

---
