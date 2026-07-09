# sometimes missed vcc-to-carry optimization

- **Issue #:** 478
- **State:** closed
- **Created:** 2018-07-29T15:46:19Z
- **Updated:** 2021-04-26T17:10:14Z
- **Labels:** Under Investigation, Compiler Performance Issue
- **URL:** https://github.com/ROCm/ROCm/issues/478

ROCm 1.9.2, OpenCL, I see such code generated:

```
        v_cndmask_b32_e64 v3, 0, 1, vcc                            // 000000003D8C: D1000003 01A90280
	v_add_co_u32_e32 v12, vcc, v0, v3                          // 000000003D94: 32180700
	v_addc_co_u32_e32 v13, vcc, 0, v1, vcc                     // 000000003D98: 381A0280
	v_mad_u64_u32 v[8:9], s[0:1], v4, v4, v[12:13]             // 000000003D9C: D1E80008 04320904
	v_mov_b32_e32 v1, v9                                       // 000000003DA4: 7E020309
	v_mad_u64_u32 v[3:4], s[0:1], v14, v4, v[1:2]              // 000000003DA8: D1E80003 0406090E
	v_cmp_lt_u64_e32 vcc, v[8:9], v[12:13]                     // 000000003DB0: 7DD21908
	v_addc_co_u32_e32 v1, vcc, 0, v4, vcc                      // 000000003DB4: 38020880
```
You see in the first line VCC is turned into a vector register "v3", to be added to the v_add on the second line. Instead, VCC could have been added directly using v_addc and skipping the v_cndmask. As you see done on the last two lines.

Apparently the problem manifests when the add is done to a 64-bit value on the lines of:
long a;
uint VCC;
long b = a + VCC;
