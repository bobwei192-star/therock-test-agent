# OpenCL internal compiler error on inline device-side functions

- **Issue #:** 77
- **State:** closed
- **Created:** 2017-01-15T10:51:53Z
- **Updated:** 2017-07-09T03:21:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/77

The error: <unknown>:0:0: in function generate void (float addrspace(1)*, i32, i32, i32, i32): unsupported call to function philox\n\nError: Creating the executable failed: Compiling LLVM IRs to exe.

The kernel sourcecode: https://github.com/arrayfire/arrayfire/blob/devel/src/backend/opencl/kernel/random_engine_philox.cl

The build options:
-cl-std=CL2.0  -D dim_t=long  -D T=float -D THREADS=256 -D RAND_DIST=0 -D ELEMENTS_PER_BLOCK=1024

Simply s/inline //g and the error mysteriously disappears.