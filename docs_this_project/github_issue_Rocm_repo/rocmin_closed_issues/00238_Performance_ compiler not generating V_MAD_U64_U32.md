# Performance: compiler not generating V_MAD_U64_U32

- **Issue #:** 238
- **State:** closed
- **Created:** 2017-10-26T23:44:22Z
- **Updated:** 2019-06-03T10:05:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/238

ROCm 1.6-180, Ubuntu 16.04, R9-Nano.

I prepared a small kernel which should be the ideal case for V_MAD_U64_U32:
```
KERNEL(256) test(global ulong *io) {
  uint p = get_global_id(0);
  ulong ab = io[p];
  uint a = ab >> 32;
  uint b = ab & 0xffffffff; 
  io[p] = ab + ((ulong ) a) * b;
}
```

Yet what is generated is:
```
	v_mul_lo_u32 v4, v3, v2                                    // 000000023054: D2850004 D2850004
	v_mul_hi_u32 v5, v3, v2                                    // 00000002305C: D2860005 D2860005
	v_add_i32_e32 v2, vcc, v2, v4                              // 000000023064: 32040902
	v_addc_u32_e32 v3, vcc, v5, v3, vcc
```

The generated code is inefficient. Apparently the code generator is not aware of the (powerful) instruction V_MAD_U64_U32. This is penalizing large integer arithmetic.
