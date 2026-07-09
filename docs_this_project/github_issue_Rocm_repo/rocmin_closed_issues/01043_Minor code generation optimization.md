# Minor code generation optimization

- **Issue #:** 1043
- **State:** closed
- **Created:** 2020-03-15T10:08:19Z
- **Updated:** 2021-04-05T11:52:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/1043

I'm using rocm 2.10

Both
  int  f = (d & 0xFFF00FFF) | (e & 0x000FF000);
and
  int  f = (d & 0xFFF00FFF) + (e & 0x000FF000);

could generate a single V_BFI_B32 instruction rather than these 2 instructions:

	v_and_b32_e32 v3, 0xff000, v4
	v_and_or_b32 v2, v2, s4, v3


