# V_MAD_U64_U32 and V_MAD_I64_I32 Documentation: VOP3B but undocumented SDST

> **Issue #752**
> **状态**: closed
> **创建时间**: 2019-03-28T20:05:40Z
> **更新时间**: 2023-08-07T23:43:54Z
> **关闭时间**: 2023-08-07T23:42:03Z
> **作者**: dragontamer
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/752

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

In the Vega ISA, V_MAD_U64_U32  and V_MAD_I64_I32 are documented as follows:

    {vcc_out,D.u64} = S0.u32 * S1.u32 + S2.u64.

However, the VOP3B opcodes touch 5 registers: S0, S1, S2 (3 source registers), VDST (destination), and SDST (a 5th register, "scalar" destination). 

This seems to me to be a documentation error. Perhaps "VCC_OUT" is really sent to SDST? (If so, it should be specified that SDST represents two registers / a register pair) I haven't really tested it one way or the other yet, but its clear to me that something is documented wrong. Page 149 of the PDF, but printed as page "141 of 239".

---

## 评论 (3 条)

### 评论 #1 — preda (2019-03-30T20:59:28Z)

https://developer.amd.com/wp-content/resources/Vega_Shader_ISA_28July2017.pdf
https://github.com/CLRX/CLRX-mirror/blob/master/doc/GcnInstrsVop3.md#v_mad_u64_u32

vcc_out is a scalar destination (64 bit)

Maybe AMD's documentation is a bit lacking in clarity or detail, but what specifically do you see wrong in this case?


---

### 评论 #2 — dragontamer (2019-03-31T05:20:01Z)

@preda 

If I **really** needed to know how this instruction worked specifically... it wouldn't take me very long to experiment with the GPU and figure out the details myself.

I dunno what the state of the Radeon VII documentation is, but I figure that its helpful if I bring up minor documentation issues like this. In the worst case, maybe the documentation fix won't help by the Radeon VII ISA guide, but at least this issue would be documented and maybe fixed by Navi's ISA documentation.

I think the documentation in the CLRX assembler page is more clear than what is in the Vega ISA. But the CLRX Assembler doesn't document the V_MAD_I64_I32 instruction very well: https://github.com/CLRX/CLRX-mirror/blob/master/doc/GcnInstrsVop3.md#v_mad_i64_i32

> Description: Multiply 32-bit signed integer value from SRC0 by 32-bit signed value from SRC1 and add 64-bit unsigned value to this result, and store final result into VDST and store some value of bits to SDST (unknown behavior).

---

### 评论 #3 — jlgreathouse (2023-08-07T23:42:02Z)

Hi @dragontamer 

I'm sorry for the long delay in getting back to you. Your ticket came in right about the time that I was running out of extra time to work on github issues like this.

You're absolutely correct, this is a minor typo in our existing documentation. [As of gfx9](https://www.amd.com/system/files/TechDocs/vega-shader-instruction-set-architecture.pdf), when they were moved into the VOP3B encoding ([VOP3SD in gfx11](https://www.amd.com/system/files/TechDocs/rdna3-shader-instruction-set-architecture-feb-2023_0.pdf)) the V_MAD_U64_U32 and V_MAD_I64_I32 instructions can be encoded to output their carryout into any SGPR targeted by the SDST field. The common encoding is to set that to VCC, but it is not required.

This instruction definition was meant to say "The VCC destination may be an arbitrary SGPR-pair.", much like e.g. V_ADD_CO_U32

Please note, however, that the V_DIV_SCALE_F32 and V_DIV_SCALE_F64 operations (despite their encoding) should still use VCC as described in the manuals.

---
