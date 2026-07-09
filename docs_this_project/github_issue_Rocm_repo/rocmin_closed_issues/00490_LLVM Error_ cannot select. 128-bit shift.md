# LLVM Error: cannot select. 128-bit shift

- **Issue #:** 490
- **State:** closed
- **Created:** 2018-08-05T14:21:35Z
- **Updated:** 2019-05-29T21:32:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/490

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