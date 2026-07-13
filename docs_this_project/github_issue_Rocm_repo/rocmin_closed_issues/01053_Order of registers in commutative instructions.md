# Order of registers in commutative instructions

- **Issue #:** 1053
- **State:** closed
- **Created:** 2020-03-19T15:20:42Z
- **Updated:** 2021-04-05T10:20:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/1053

I'm looking at the ISA generated for some OpenCL kernel (ROCm 3.1, Vega20), and I see this as a diff between two compilations of slightly different (but equivalent) source code:
```
4122c4122
<       v_add_u32_e32 v7, v7, v8
---
>       v_add_u32_e32 v7, v8, v7
4141c4141
<       v_add_u32_e32 v9, v20, v9
---
>       v_add_u32_e32 v9, v9, v20
4154c4154
<       v_add_u32_e32 v21, v21, v9
---
>       v_add_u32_e32 v21, v9, v21
4179c4179
<       v_add_u32_e32 v13, v28, v13
---
>       v_add_u32_e32 v13, v13, v28
```

As you see, the difference consists only in the order of the two VGPRs into an add. I'd like to know, is there any difference *at all* between e.g. v_add_u32 v0, v0, v1 and v_add_u32_e32 v0, v1, v0 ? If there isn't any, then the compiler could canonicalize them (by chosing a consistent order when the order doesn't matter).
