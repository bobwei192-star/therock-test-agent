# FR: generate MUL:2, MUL:4, DIV:2  for VOP3 instructions (OpenCL performance)

> **Issue #1405**
> **状态**: open
> **创建时间**: 2021-03-13T08:11:20Z
> **更新时间**: 2024-10-22T21:13:19Z
> **作者**: preda
> **标签**: Feature Request, Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1405

## 标签

- **Feature Request** (颜色: #fbca04)
- **Under Investigation** (颜色: #0052cc)

## 描述

A function such as:
double sum2(double x, double y) { return 2 * (x + y); }
could be compiled to a single VOP3 GCN instructions such as:
```
v_add_f64 %0, %1, %2 MUL:2
```

But this efficient code is not generated because MUL:2 and the like only function correctly with denormals disabled and non-IEEE mode. (denormals and IEEE mode can be set thus:
```
// turn IEEE mode and denormals off so that mul:2 and div:2 work
#define ENABLE_MUL2() { \
    __asm volatile ("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 9, 1), 0");\
    __asm volatile ("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 4, 4), 7");\
}
```

Feature request: please provide an OpenCL compilation flag that enables MUL:2 and the like, at the same time disabling denormals and IEEE mode as required. This would allow a developer to choose between the two good things: denormals on one side, and more performance on the other side (by making better use of the power of VOP3 instructions).


---

## 评论 (9 条)

### 评论 #1 — ROCmSupport (2021-03-15T09:02:04Z)

Thanks @preda for reaching out.
I will pass this information to compiler team and reach them for the inputs.
Thank you.

---

### 评论 #2 — b-sumner (2021-05-04T17:26:44Z)

clang/LLVM changes to enable this are now upstream.  The compiler options -mno-amdgpu-ieee and -fno-honor-nans are both required to enable such folding.

---

### 评论 #3 — preda (2021-05-04T20:53:10Z)

> clang/LLVM changes to enable this are now upstream. The compiler options -mno-amdgpu-ieee and -fno-honor-nans are both required to enable such folding.

@b-sumner This is great news, thank you. What is the way to enable this with OpenCL? -- will OpenCL accept those flags directly, or some other OpenCL flags that will be translated to clang -mno-amdgpu-ieee and -fno-honor-nans?


---

### 评论 #4 — preda (2021-05-09T20:05:30Z)

see also #967 related.

---

### 评论 #5 — preda (2023-04-11T07:02:49Z)

I'm coming back with this request:

Offer a way to enable the GCN Output Modifiers ("OMOD") such as MUL:2 in OpenCL.

Now that LLVM supports generating GCN OMODs (as per @b-sumner 's comment above), how can we make use of that in OpenCL?


---

### 评论 #6 — abhimeda (2024-01-22T22:36:08Z)

@preda Hi, is this issue still persisting on the latest version of ROCm? If not can we close this ticket?

---

### 评论 #7 — preda (2024-01-23T10:24:13Z)

I'm using OpenCL, and AFAIK there is still no way to take advantage of VOP3 modifiers such as MUL:2 in the OpenCL compilation.

OTOH according to @b-sumner 's comment above, the issue should be fixed for clang/llvm by using -mno-amdgpu-ieee and -fno-honor-nans .

But there does not seem to be a way to pass those compiler flags from OpenCL, so as far as this issue is concerned (note "OpenCL performance" in the issue title), this is not fixed.


---

### 评论 #8 — ppanchad-amd (2024-07-03T18:44:22Z)

@preda I will check with the internal team and get back to you. Thanks!

---

### 评论 #9 — jamesxu2 (2024-10-22T21:13:18Z)

Hi @preda, 

Thanks for your patience. 

> But there does not seem to be a way to pass those compiler flags from OpenCL, so as far as this issue is concerned (note "OpenCL performance" in the issue title), this is not fixed.

You could in theory pass these flags to the OpenCL compiler using -Wf,<option> to pass them to the Clang frontend prior to runtime compilation. However, there is a **known issue** in which these flags are not correctly forwarded to the compiler, that only occurs during OCL runtime compilation. 

Example invocation (that currently does not work):
```
[Code]
program.build({default_device}, "-Wf,-mno-amdgpu-ieee -Wf,-fno-honor-nans")




[result, if you run your executable with AMD_COMGR_EMIT_VERBOSE_LOGS=1]
error: invalid argument '-mno-amdgpu-ieee' only allowed with relaxed NaN handling
        ReturnStatus: AMD_COMGR_STATUS_ERROR

```

I'll keep you updated on the internal state of this ticket.

---
