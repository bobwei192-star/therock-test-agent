# HIP equivalent to CUDA int_as_float and float_as_int device functions.

- **Issue #:** 1479
- **State:** closed
- **Created:** 2021-05-23T01:11:23Z
- **Updated:** 2021-05-24T19:21:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1479

Hello, I am working on porting my CUDA code to HIP and ran into an issue with porting over two device functions: int_as_float and float_as_int. The Hipify tools state that they are unsupported. If this is the case, is there any way to implement these functions?

Specifically, they are used in a trick to implement floating point atomicMax using atomicCAS.

Any help is appreciated and thank you.