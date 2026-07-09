# Compiler erroneously generates (OR 0x1) instead of (OR 0x80000001) assembly

- **Issue #:** 656
- **State:** closed
- **Created:** 2019-01-02T08:54:56Z
- **Updated:** 2019-01-25T23:28:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/656

Consider the following line: https://github.com/949f45ac/xmrig-HIP/blob/476c50d7aa449bee8cef77168d5f3b9a121a10c1/src/nvidia/fast_int_math_v2.hpp#L79

If I use either `__uint2float_rn(a & 0xFF)` or `(float)(a & 0xFF)` here, the compiler will generate a `v_cvt_f32_ubyte0_e32` instruction. Seems fair enough – however, it produces incorrect results.
Somehow if I force the same instruction without `_e32`, it works. Another solution is to just use `V_CVT_F32_U32_E32` and pass in `(a & 0xFF)` already calculated.

If I compile for an NVidia card, I get correct results with `__uint2float_rn`, so I think that this function should be the correct one to use in this case, and the ROCm/HIP implementation slightly off.
Tried on both gfx900 and gfx803.

Cheers!