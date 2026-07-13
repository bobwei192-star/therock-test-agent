# OpenCL codegen: make use of the GCN VOP3 output modifiers

- **Issue #:** 1021
- **State:** closed
- **Created:** 2020-02-24T10:35:49Z
- **Updated:** 2021-05-09T19:54:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/1021

The GCN VOP3 instructions offer an output modifier which is a multiplication by 0.5, 2, or 4 *for free*. OTOH the generated code for OpenCL never uses these output modifiers. This is a pity -- the generated code does not use GCN to its full power.

Please enable OMOD (output modifiers) in the generated code, at least when compiling with -cl-fast-relaxed-math.
