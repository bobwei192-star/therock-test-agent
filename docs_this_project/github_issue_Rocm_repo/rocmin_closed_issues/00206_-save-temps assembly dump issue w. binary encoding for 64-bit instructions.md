# -save-temps assembly dump issue w. binary encoding for 64-bit instructions

- **Issue #:** 206
- **State:** closed
- **Created:** 2017-09-13T08:34:46Z
- **Updated:** 2017-11-15T22:47:18Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/206

On AMDGPU-pro 17.30, RX Vega 64, Linux.
Passing -save-temps when compiling the OpenCL kernel dumps assembly in a file like _0_gfx900.s, e.g.
```
flat_load_dwordx4 v[19:22], v[2:3]                   // 00000000C0EC: DC5C0000 DC5C0000
flat_load_dwordx4 v[35:38], v[10:11]                 // 00000000C0F4: DC5C0000 DC5C0000
```
In the comment is the address and the binary encoding of the instruction. For 64 bits instructions, the binary encoding is wrong, being one word written twice (DC5C0000 DC5C0000) instead of the correct encoding.
