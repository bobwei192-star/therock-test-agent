# cross-lane operation intrinsics in OpenCL

- **Issue #:** 189
- **State:** closed
- **Created:** 2017-08-29T14:56:30Z
- **Updated:** 2018-06-03T15:03:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/189

In particular exposing the `ds_permute`, `ds_swizzle` would be useful, but given that hcc defines shfl ops too, why not add those too via some OpenCL extensions.

In addition, the wavefront voting instrinsics `__any`, `__all`, `__ballot` would also be valuable.

As an intermediate solution, is it possible to somehow write in-line ASM equivalent of these or somehow use hc along OpenCL in kernels?