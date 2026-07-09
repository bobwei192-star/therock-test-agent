# GCN ISA: document impact of FP IEEE_mode on VOP3 output modifiers

- **Issue #:** 968
- **State:** closed
- **Created:** 2019-12-15T07:45:54Z
- **Updated:** 2023-12-18T15:56:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/968

It seems that "output modifiers" on VOP3 instructions (e.g. mul:2 on v_mul_f64) are ignored when IEEE_mode is set. Please add this information in the GCN ISA document. This is important because by default OpenCL code is generated with IEEE_mode set, and inline __asm() is supported, which can be used to take advantage of output modifiers.

Context: see #964