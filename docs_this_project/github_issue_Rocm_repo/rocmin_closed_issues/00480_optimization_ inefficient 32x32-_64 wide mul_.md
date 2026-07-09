# optimization: inefficient 32x32->64 wide mul?

- **Issue #:** 480
- **State:** closed
- **Created:** 2018-07-30T12:10:34Z
- **Updated:** 2023-12-12T21:48:52Z
- **Labels:** Under Investigation, Compiler Performance Issue
- **URL:** https://github.com/ROCm/ROCm/issues/480

uint a, b;
ulong x = a * (ulong) b;

When doing the wide integer multiplication 32x32 -> 64, such code is generated:

```
	v_mul_lo_u32 v0, v4, v3                                    // 000000003D58: D2850000 00020704
	v_mul_hi_u32 v1, v4, v3                                    // 000000003D60: D2860001 00020704
```

It seems to me it would be more efficient to generate a single v_mad_u64_u32 instead, e.g.
```
v_mad_u64_u32 v[0:1], vcc, v4, v3, 0
```