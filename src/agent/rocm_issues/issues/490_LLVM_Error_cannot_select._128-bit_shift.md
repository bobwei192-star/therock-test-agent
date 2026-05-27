# LLVM Error: cannot select. 128-bit shift

> **Issue #490**
> **状态**: closed
> **创建时间**: 2018-08-05T14:21:35Z
> **更新时间**: 2019-05-29T21:32:58Z
> **关闭时间**: 2019-05-29T21:32:57Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/490

## 描述

This is outside of the OpenCL spec, yet it may be useful to be aware of it.
Apparently this is triggered by doing a shift on a 128-bit value, like this:

((unsigned long long)1) << ((uint) x);
```
LLVM ERROR: Cannot select: 0x556e0677e280: i64,i64 = shl_parts Constant:i64<1>, Constant:i64<0>, 0x556e067ca5c0
  0x556e067ca0e0: i64 = Constant<1>
  0x556e0682d5b0: i64 = Constant<0>
  0x556e067ca5c0: i32 = and 0x556e067c7668, Constant:i32<127>
    0x556e067c7668: i32 = extract_vector_elt 0x556e067c78d8, Constant:i32<0>
      0x556e067c78d8: v4i32,ch = load<(load 16 from %ir.19, addrspace 1)> 0x556e06d16918, 0x556e0682db60, undef:i64
        0x556e0682db60: i64 = add 0x556e06987210, 0x556e06849480
          0x556e06987210: i64 = bitcast 0x556e069856d0
            0x556e069856d0: v2i32,ch = load<(dereferenceable invariant load 8 from `i64 addrspace(4)* undef`, addrspace 4)> 0x556e06d16918, 0x556e0682cf30, undef:i64
              0x556e0682cf30: i64,ch = CopyFromReg 0x556e06d16918, Register:i64 %3
                0x556e0682d6e8: i64 = Register %3
              0x556e068298b0: i64 = undef
          0x556e06849480: i64 = shl 0x556e06d091a8, Constant:i32<4>
            0x556e06d091a8: i64 = zero_extend 0x556e06986b28
              0x556e06986b28: i32 = add 0x556e0682cd90, 0x556e06d097c0
                0x556e0682cd90: i32,ch = load<(load 4 from %ir.14, align 8, !tbaa !16, addrspace 4)> 0x556e06d16918, 0x556e069870d8, undef:i64
                  0x556e069870d8: i64 = add 0x556e0682cf30, Constant:i64<8>


                  0x556e068298b0: i64 = undef
                0x556e06d097c0: i32 = add 0x556e067c6f18, 0x556e067c7738
                  0x556e067c6f18: i32 = mul 0x556e067c7a10, 0x556e06d09278


                  0x556e067c7738: i32 = AssertZext 0x556e068df190, ValueType:ch:i8

            0x556e068451d0: i32 = Constant<4>
        0x556e068298b0: i64 = undef
      0x556e06987890: i32 = Constant<0>
    0x556e06d080c8: i32 = Constant<127>
```

---

## 评论 (8 条)

### 评论 #1 — preda (2018-08-05T14:24:38Z)

This was with ROCm 1.8.2, Ubuntu 18.04 4.15, Vega64, OpenCL 2.0

---

### 评论 #2 — preda (2018-08-05T14:49:36Z)

And another, which may be the same or not:
```
LLVM ERROR: Cannot select: 0x55c889a6d658: i64,i64 = srl_parts 0x55c889a6e940, 0x55c889a5e8d0, 0x55c889a5ece0
  0x55c889a6e940: i64 = or 0x55c889e8a6e8, 0x55c889e45638
    0x55c889e8a6e8: i64 = bitcast 0x55c889a6d998
      0x55c889a6d998: v2i32 = BUILD_VECTOR Constant:i32<0>, 0x55c889b36228
        0x55c889f5f9e8: i32 = Constant<0>
        0x55c889b36228: i32 = truncate 0x55c889e8ac98
          0x55c889e8ac98: i64,i1 = MAD_U64_U32 0x55c889b35ee8, 0x55c889a6eae0, 0x55c889b36088
            0x55c889b35ee8: i32 = shl 0x55c889e8a2d8, Constant:i32<1>
              0x55c889e8a2d8: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<2>
                0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
                  0x55c889b34750: v4i32 = Register %14
                0x55c8899159c0: i32 = Constant<2>
              0x55c889f5ece8: i32 = Constant<1>
            0x55c889a6eae0: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<1>
              0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
                0x55c889b34750: v4i32 = Register %14
              0x55c889f5ece8: i32 = Constant<1>
            0x55c889b36088: i64 = bitcast 0x55c889b31890
              0x55c889b31890: v2i32 = BUILD_VECTOR 0x55c889f67608, Constant:i32<0>
                0x55c889f67608: i32 = extract_vector_elt 0x55c889b31ca0, Constant:i32<1>
                  0x55c889b31ca0: v2i32 = bitcast 0x55c889a851f8

                  0x55c889f5ece8: i32 = Constant<1>
                0x55c889f5f9e8: i32 = Constant<0>
    0x55c889e45638: i64 = bitcast 0x55c889b365d0
      0x55c889b365d0: v2i32 = BUILD_VECTOR 0x55c889b31ea8, Constant:i32<0>
        0x55c889b31ea8: i32 = truncate 0x55c889a851f8
          0x55c889a851f8: i64,i1 = MAD_U64_U32 0x55c889a6eae0, 0x55c889a6eae0, 0x55c889e47840
            0x55c889a6eae0: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<1>
              0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
                0x55c889b34750: v4i32 = Register %14
              0x55c889f5ece8: i32 = Constant<1>
            0x55c889a6eae0: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<1>
              0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
                0x55c889b34750: v4i32 = Register %14
              0x55c889f5ece8: i32 = Constant<1>
            0x55c889e47840: i64 = add 0x55c889f67cf0, 0x55c889e478a8
              0x55c889f67cf0: i64,i1 = MAD_U64_U32 0x55c889b35ee8, 0x55c889b32388, 0x55c8899155b0
                0x55c889b35ee8: i32 = shl 0x55c889e8a2d8, Constant:i32<1>
                  0x55c889e8a2d8: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<2>


                  0x55c889f5ece8: i32 = Constant<1>
                0x55c889b32388: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<0>
                  0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14

                  0x55c889f5f9e8: i32 = Constant<0>
                0x55c8899155b0: i64 = srl 0x55c889f677a8, Constant:i32<31>
                  0x55c889f677a8: i64 = bitcast 0x55c889b33918

                  0x55c889e8a000: i32 = Constant<31>
              0x55c889e478a8: i64 = zero_extend 0x55c889a5e9a0
                0x55c889a5e9a0: i1 = setcc 0x55c889a85670, 0x55c889a5eb40, setult:ch
                  0x55c889a85670: i64,i1 = MAD_U64_U32 0x55c889b32388, 0x55c889b32388, 0x55c889a5eb40



                  0x55c889a5eb40: i64 = bitcast 0x55c889e89f30

        0x55c889f5f9e8: i32 = Constant<0>
  0x55c889a5e8d0: i64,i1 = MAD_U64_U32 0x55c889e8a2d8, 0x55c889e8a2d8, 0x55c889f682a0
    0x55c889e8a2d8: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<2>
      0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
        0x55c889b34750: v4i32 = Register %14
      0x55c8899159c0: i32 = Constant<2>
    0x55c889e8a2d8: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<2>
      0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
        0x55c889b34750: v4i32 = Register %14
      0x55c8899159c0: i32 = Constant<2>
    0x55c889f682a0: i64 = zero_extend 0x55c889a89148
      0x55c889a89148: i32,i1 = addcarry 0x55c889a5e730, Constant:i32<0>, 0x55c889913e80
        0x55c889a5e730: i32 = extract_vector_elt 0x55c889b36498, Constant:i32<1>
          0x55c889b36498: v2i32 = bitcast 0x55c889e8ac98
            0x55c889e8ac98: i64,i1 = MAD_U64_U32 0x55c889b35ee8, 0x55c889a6eae0, 0x55c889b36088
              0x55c889b35ee8: i32 = shl 0x55c889e8a2d8, Constant:i32<1>
                0x55c889e8a2d8: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<2>
                  0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14

                  0x55c8899159c0: i32 = Constant<2>
                0x55c889f5ece8: i32 = Constant<1>
              0x55c889a6eae0: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<1>
                0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
                  0x55c889b34750: v4i32 = Register %14
                0x55c889f5ece8: i32 = Constant<1>
              0x55c889b36088: i64 = bitcast 0x55c889b31890
                0x55c889b31890: v2i32 = BUILD_VECTOR 0x55c889f67608, Constant:i32<0>
                  0x55c889f67608: i32 = extract_vector_elt 0x55c889b31ca0, Constant:i32<1>


                  0x55c889f5f9e8: i32 = Constant<0>
          0x55c889f5ece8: i32 = Constant<1>
        0x55c889f5f9e8: i32 = Constant<0>
        0x55c889913e80: i1 = setcc 0x55c889a851f8, 0x55c889e47840, setult:ch
          0x55c889a851f8: i64,i1 = MAD_U64_U32 0x55c889a6eae0, 0x55c889a6eae0, 0x55c889e47840
            0x55c889a6eae0: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<1>
              0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
                0x55c889b34750: v4i32 = Register %14
              0x55c889f5ece8: i32 = Constant<1>
            0x55c889a6eae0: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<1>
              0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
                0x55c889b34750: v4i32 = Register %14
              0x55c889f5ece8: i32 = Constant<1>
            0x55c889e47840: i64 = add 0x55c889f67cf0, 0x55c889e478a8
              0x55c889f67cf0: i64,i1 = MAD_U64_U32 0x55c889b35ee8, 0x55c889b32388, 0x55c8899155b0
                0x55c889b35ee8: i32 = shl 0x55c889e8a2d8, Constant:i32<1>
                  0x55c889e8a2d8: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<2>


                  0x55c889f5ece8: i32 = Constant<1>
                0x55c889b32388: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<0>
                  0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14

                  0x55c889f5f9e8: i32 = Constant<0>
                0x55c8899155b0: i64 = srl 0x55c889f677a8, Constant:i32<31>
                  0x55c889f677a8: i64 = bitcast 0x55c889b33918

                  0x55c889e8a000: i32 = Constant<31>
              0x55c889e478a8: i64 = zero_extend 0x55c889a5e9a0
                0x55c889a5e9a0: i1 = setcc 0x55c889a85670, 0x55c889a5eb40, setult:ch
                  0x55c889a85670: i64,i1 = MAD_U64_U32 0x55c889b32388, 0x55c889b32388, 0x55c889a5eb40



                  0x55c889a5eb40: i64 = bitcast 0x55c889e89f30

          0x55c889e47840: i64 = add 0x55c889f67cf0, 0x55c889e478a8
            0x55c889f67cf0: i64,i1 = MAD_U64_U32 0x55c889b35ee8, 0x55c889b32388, 0x55c8899155b0
              0x55c889b35ee8: i32 = shl 0x55c889e8a2d8, Constant:i32<1>
                0x55c889e8a2d8: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<2>
                  0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14

                  0x55c8899159c0: i32 = Constant<2>
                0x55c889f5ece8: i32 = Constant<1>
              0x55c889b32388: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<0>
                0x55c889a5efb8: v4i32,ch = CopyFromReg 0x55c889f42488, Register:v4i32 %14
                  0x55c889b34750: v4i32 = Register %14
                0x55c889f5f9e8: i32 = Constant<0>
              0x55c8899155b0: i64 = srl 0x55c889f677a8, Constant:i32<31>
                0x55c889f677a8: i64 = bitcast 0x55c889b33918
                  0x55c889b33918: v2i32 = BUILD_VECTOR 0x55c889f67c20, 0x55c889bfd7e0


                0x55c889e8a000: i32 = Constant<31>
            0x55c889e478a8: i64 = zero_extend 0x55c889a5e9a0
              0x55c889a5e9a0: i1 = setcc 0x55c889a85670, 0x55c889a5eb40, setult:ch
                0x55c889a85670: i64,i1 = MAD_U64_U32 0x55c889b32388, 0x55c889b32388, 0x55c889a5eb40
                  0x55c889b32388: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<0>


                  0x55c889b32388: i32 = extract_vector_elt 0x55c889a5efb8, Constant:i32<0>


                  0x55c889a5eb40: i64 = bitcast 0x55c889e89f30

                0x55c889a5eb40: i64 = bitcast 0x55c889e89f30
                  0x55c889e89f30: v2i32 = BUILD_VECTOR Constant:i32<0>, 0x55c889e48540


  0x55c889a5ece0: i32 = AssertSext 0x55c889a85c20, ValueType:ch:i8
    0x55c889a85c20: i32,ch = CopyFromReg 0x55c889f42488, Register:i32 %6
      0x55c889a6d5f0: i32 = Register %6
In function: square

```

---

### 评论 #3 — b-sumner (2018-08-05T17:07:18Z)

Can you provide some means to reproduce these? 

There is no 128-bit scalar integer type in OpenCL.  Is clang treating "unsigned long long" as a 128-bit type?  It should be treating it the same as "unsigned long".

---

### 评论 #4 — preda (2018-08-05T23:00:36Z)

Repro for the first one:
```
KERNEL(256) test(global ulong2 *data) {
  uint p = get_global_id(0);
  ulong2 d = data[p];
  data[p].x = (1ull << (uint) (d.x));
}
```
clang's "extension" of providing 128-bit in OpenCL is incredibly useful. It may be viewed as similar to "__asm" which also isn't part of OpenCL, but is part of ROCm/clang and very useful as well.

```
LLVM ERROR: Cannot select: 0x559516beb120: i64,i64 = shl_parts Constant:i64<1>, Constant:i64<0>, 0x559516bd2990
  0x559516bd24b0: i64 = Constant<1>
  0x55951689a750: i64 = Constant<0>
  0x559516bd2990: i32 = and 0x559516bcfa38, Constant:i32<127>
    0x559516bcfa38: i32 = extract_vector_elt 0x559516bcfca8, Constant:i32<0>
      0x559516bcfca8: v4i32,ch = load<(load 16 from %ir.19, !tbaa !27, addrspace 1)> 0x5595166f7618, 0x55951689ad00, undef:i64
        0x55951689ad00: i64 = add 0x559516bcc8d0, 0x5595166ede70
          0x559516bcc8d0: i64 = bitcast 0x559516c0a780
            0x559516c0a780: v2i32,ch = load<(dereferenceable invariant load 8 from `i64 addrspace(4)* undef`, addrspace 4)> 0x5595166f7618, 0x55951689a0d0, undef:i64
              0x55951689a0d0: i64,ch = CopyFromReg 0x5595166f7618, Register:i64 %3
                0x55951689a888: i64 = Register %3
              0x559516beef00: i64 = undef
          0x5595166ede70: i64 = shl 0x559516c866a8, Constant:i32<4>
            0x559516c866a8: i64 = zero_extend 0x559516bcc1e8
              0x559516bcc1e8: i32 = add 0x559516899f30, 0x559516c86cc0
                0x559516899f30: i32,ch = load<(load 4 from %ir.14, align 8, !tbaa !16, addrspace 4)> 0x5595166f7618, 0x559516bcc798, undef:i64
                  0x559516bcc798: i64 = add 0x55951689a0d0, Constant:i64<8>


                  0x559516beef00: i64 = undef
                0x559516c86cc0: i32 = add 0x559516bcf2e8, 0x559516bcfb08
                  0x559516bcf2e8: i32 = mul 0x559516bcfde0, 0x559516c86778


                  0x559516bcfb08: i32 = AssertZext 0x559516772fe0, ValueType:ch:i8

            0x5595166e9bc0: i32 = Constant<4>
        0x559516beef00: i64 = undef
      0x559516bccf50: i32 = Constant<0>
    0x559516c63cc8: i32 = Constant<127>
In function: test
```

---

### 评论 #5 — b-sumner (2018-08-07T18:46:02Z)

This will be fixed in a future release.    However note that AMD is not officially supporting 128-bit integral types so you cannot count on everything to work, e.g. 128-bit division.

---

### 评论 #6 — preda (2018-08-07T21:09:46Z)

@b-sumner Yes I understand. It's fair, any amount of 128-bit is useful, and it's your choice how much to implement.

Now that you mention 128-bit division, I don't need it now. I imagine it would be a terribly slow operation, and with huge codegen. But I think it *could* be emulated using just normal underlying operations, such as 64-bit multiplication and division (64-bit division being itself emulated). I imagine existing compilers that offer emulated 128-bit have that code already.

Anyway it would be nice if the not-available operations were documented as not-available, and the compiler behaved elegantly on them (not crash). (In particular I consider the "cannot select" above a good behavior for a not-implemented, please make sure the other not-available ops are not worse).


---

### 评论 #7 — TCS-S1 (2019-05-29T09:33:22Z)

I could see no LLVM error even though I used 128-bit shift, would like to know whether this issue is resolved or not


My Kernel Source :
const char *kernelSource =                                       "\n" \
"#pragma OPENCL EXTENSION cl_khr_fp64 : enable                    \n" \
"__kernel void shift_128( __global unsigned int *a)               \n" \
"{                                                               \n" \
"     *a =  ((unsigned long long)1) << ((unsigned int) *a);      \n" \
"}                                                               \n" \
                                                                "\n" ;                                                     

System details:                                                                
Ubuntu 16.04.6 LTS                                                               
Rocm version : 2.4.25
opencl version : 
1. Device: gfx803
 1.1 Hardware version: OpenCL 1.2 
 1.2 Software version: 2874.0 (HSA1.1,LC)
 1.3 OpenCL C version: OpenCL C 2.0 
 1.4 Parallel compute units: 64
2. Device: gfx803
 2.1 Hardware version: OpenCL 1.2 
 2.2 Software version: 2874.0 (HSA1.1,LC)
 2.3 OpenCL C version: OpenCL C 2.0 
 2.4 Parallel compute units: 64

---

### 评论 #8 — preda (2019-05-29T21:32:57Z)

Yes, this seems fixed in ROCm 2.2!


---
