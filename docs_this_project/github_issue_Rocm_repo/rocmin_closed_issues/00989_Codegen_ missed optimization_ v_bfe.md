# Codegen: missed optimization: v_bfe

- **Issue #:** 989
- **State:** closed
- **Created:** 2020-01-02T09:51:13Z
- **Updated:** 2023-12-18T15:47:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/989

Using ROCm 2.10, RadeonVII, OpenCL
```
int lowBits(int u, unsigned bits) { return ((u << (32 - bits)) >> (32 - bits)); }
```

Is compiled to
```
        v_sub_u32_e32 v3, 0, v3
	v_and_b32_e32 v3, 31, v3
	v_lshlrev_b32_e32 v2, v3, v2
	v_ashrrev_i32_e32 v2, v3, v2
```

While it could be compiled to a single fast instruction:
```
	v_bfe_i32 v2, v2, 0, v3
```

There should be a way to get the compiler to use the v_bfe without having to use assembly.
