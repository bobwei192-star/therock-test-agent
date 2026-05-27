# OpenCL compile failure with inline assembly for Polaris

> **Issue #392**
> **状态**: closed
> **创建时间**: 2018-04-23T10:20:01Z
> **更新时间**: 2018-10-24T04:34:07Z
> **关闭时间**: 2018-10-24T04:34:07Z
> **作者**: todxx
> **标签**: Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/392

## 标签

- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

Below is a kernel that fails to compile for Polaris (mcpu=gfx803).  This kernel compiles and functions correctly for Vega (mcpu=gfx900).  Attempting to compile for Polaris produces the following error: `error: couldn't allocate output register for constraint 'v' at line 104`  I believe all instructions/features used in the assembly are GCN 1.2 compatible and should compile for Polaris.

```
inline short2 mad_short2(short2 a, short2 b, short2 c)
{
    short2 result;
     __asm (
            "v_mul_lo_u16_sdwa  %[result], %[a],        %[b] dst_sel:WORD_0 dst_unused:UNUSED_PRESERVE src0_sel:WORD_0 src1_sel:WORD_0\n"
            "v_mul_lo_u16_sdwa  %[result], %[a],        %[b] dst_sel:WORD_1 dst_unused:UNUSED_PRESERVE src0_sel:WORD_1 src1_sel:WORD_1\n"
            "v_add_u16_sdwa     %[result], %[result],   %[c] dst_sel:WORD_0 dst_unused:UNUSED_PRESERVE src0_sel:WORD_0 src1_sel:WORD_0\n"
            "v_add_u16_sdwa     %[result], %[result],   %[c] dst_sel:WORD_1 dst_unused:UNUSED_PRESERVE src0_sel:WORD_1 src1_sel:WORD_1\n"
            : [result] "=&v" (result)
            : [a] "v" (a), [b] "v" (b), [c] "v" (c)
            );
    
    return result; 
}   
    
__kernel 
void mad_test(__global uint4 *data)
{   
    short2 a = {-1235,-7};
    short2 b = {-15,20000};
    short2 c = {-34,-41};
    short2 result = mad_short2(a,b,c);

    printf("result : %x\n", as_uint(result));
    printf("ref    : %x\n", as_uint(a * b + c));
}
```

---

## 评论 (4 条)

### 评论 #1 — gstoner (2018-05-05T14:50:09Z)

Team is looking at this 

---

### 评论 #2 — gstoner (2018-05-12T13:04:11Z)

@todxx the team found the issue now we working on getting through the testing phase 

---

### 评论 #3 — todxx (2018-05-13T03:30:16Z)

Awesome! Thanks for looking into this bug.

When you guys push the fix, if possible, could you link the upstream commit if it is relatively contained?  I'd like to back-port it to my 1.7 local llvm build.  I've yet to figure out how to get upstream build to work correctly with devlibs, etc.

---

### 评论 #4 — jlgreathouse (2018-10-09T18:13:28Z)

Hi @todxx 

I just tested this with the ROCm 1.9.1 we released last week. `clinfo` reports ` Driver version:                                2679.0 (HSA1.1,LC)`, which I believe is also the version we had in 1.9.0.

I just tested your kernel on a Fiji and a Polaris 10 (both gfx803). It appears to work now. Could you grab the latest ROCm 1.9.1 and verify if things work for you now?

---
