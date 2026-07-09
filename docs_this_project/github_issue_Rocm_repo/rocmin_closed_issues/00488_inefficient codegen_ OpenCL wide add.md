# inefficient codegen: OpenCL wide add

- **Issue #:** 488
- **State:** closed
- **Created:** 2018-08-02T12:09:14Z
- **Updated:** 2023-12-18T18:41:44Z
- **Labels:** Under Investigation, Compiler Performance Issue
- **URL:** https://github.com/ROCm/ROCm/issues/488

This is a 3-word-wide add-with-carry in OpenCL:
```
uint3 add(uint3 a, uint3 b) {
  ulong x = a.x + (ulong) b.x;
  ulong y = a.y + (ulong) b.y + (x >> 32);
  uint  z = a.z + b.z + (y >> 32);
  return (uint3) (x, y, z);
}
```
This code can be compiled to 3 v_add instructions (with carry-in/carry-out as appropriate). But this is what is generated:
```
	v_add_co_u32_e32 v2, vcc, v7, v4                           // 000000003D74: 32040907
	v_addc_co_u32_e64 v0, s[0:1], 0, 0, vcc                    // 000000003D78: D11C0000 01A90080
	s_waitcnt vmcnt(1)                                         // 000000003D80: BF8C0F71
	v_add_co_u32_e32 v3, vcc, v8, v5                           // 000000003D84: 32060B08
	v_addc_co_u32_e64 v5, s[0:1], 0, 0, vcc                    // 000000003D88: D11C0005 01A90080
	v_add_co_u32_e32 v3, vcc, v3, v0                           // 000000003D90: 32060103
	v_addc_co_u32_e32 v0, vcc, 0, v5, vcc                      // 000000003D94: 38000A80
	v_add_u32_e32 v4, v9, v6                                   // 000000003D98: 68080D09
	v_add_u32_e32 v4, v4, v0
```
Which is 8 adds.

Apparently the compiler does not understand the carry expressed in OpenCL as widening add.

Below is the expected ISA snippet:
```
	v_add_co_u32_e32 v2, vcc, v4, v7                           // 000000003D74: 32040F04
	v_addc_co_u32_e32 v3, vcc, v5, v8, vcc                     // 000000003D78: 38061105
	v_addc_co_u32_e32 v4, vcc, v6, v9, vcc                     // 000000003D7C: 38081306
```