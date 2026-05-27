# Inconsistent information by rocminfo and Vega FE

> **Issue #454**
> **状态**: closed
> **创建时间**: 2018-07-08T04:46:04Z
> **更新时间**: 2023-12-18T18:19:07Z
> **关闭时间**: 2023-12-18T18:19:07Z
> **作者**: robinchrist
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/454

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

Hi,

rocminfo reports:
```
 Name:                    gfx900                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
[...]                   
  Max Clock Frequency (MHz):1600                               
  BDFID:                   2816                               
  Compute Unit:            64                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE    
```
in Agent section, but

```
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE          
```

in ISA section.

Shouldn't rocm report `Fast F16 Operation: TRUE`?

I believe the issue was already reported as #274 about 6 months ago.

---

## 评论 (7 条)

### 评论 #1 — kentrussell (2018-09-14T13:48:04Z)

Can you try it out with the 1.9 release? If it's still happening, we can try to get someone to figure out what's going on.

---

### 评论 #2 — jlgreathouse (2018-09-15T00:41:41Z)

I can confirm still I see this issue on ROCm 1.9.0 with a Vega 56.

```
*******
Agent 2
*******
  Name:                    gfx900
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
...
  Max Clock Frequency (MHz):1622
  BDFID:                   2560
  Compute Unit:            56
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
...
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx900
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
```

The is caused by ROCr [always returning false](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-1.9.x/src/core/runtime/amd_gpu_agent.cpp#L694) for the Agent query on fast f16.

I have sent this issue to the ROCr team, and they are now tracking it.

---

### 评论 #3 — ROCmSupport (2021-01-06T12:56:33Z)

Thanks for reaching out.
We are working on it and will share progress on this.
Thank you.

---

### 评论 #4 — tasso (2023-12-08T17:04:50Z)

If there is a solution, can we please close this issue?

---

### 评论 #5 — tasso (2023-12-12T21:50:10Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---

### 评论 #6 — robinchrist (2023-12-12T21:57:02Z)

> Original ticket is more than a year old and the person that originally opened ticket has not responded to the latest request. If this is still an issue, please file a new ticket and we will be happy to investigate it. Thanks!

Ah yes, this nicely lines up with what we know from AMD.

Last reply from AMD was: 

> Thanks for reaching out.
> We are working on it and will share progress on this.
> Thank you.


...no progress was ever shared :)

---

### 评论 #7 — tasso (2023-12-13T13:29:19Z)

Robin is the issue still reproducible with the latest ROCM?

---
