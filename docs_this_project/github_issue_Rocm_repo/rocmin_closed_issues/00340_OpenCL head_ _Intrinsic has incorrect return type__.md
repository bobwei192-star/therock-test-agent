# OpenCL head: "Intrinsic has incorrect return type!"

- **Issue #:** 340
- **State:** closed
- **Created:** 2018-02-20T02:40:19Z
- **Updated:** 2018-12-30T03:17:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/340

Ubuntu 17.10, Vega 64.
With freshly built opencl, I get this on clGetPlatformIDs() invocation, e.g.:

$ LD_LIBRARY_PATH=/home/preda/rocm/opencl/build/lib clinfo
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.dispatch.ptr
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.implicitarg.ptr
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.implicitarg.ptr
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.implicitarg.ptr
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.dispatch.ptr
Number of platforms                               0
