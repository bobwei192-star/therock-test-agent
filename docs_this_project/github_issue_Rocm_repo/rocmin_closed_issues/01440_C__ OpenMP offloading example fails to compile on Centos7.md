# C++ OpenMP offloading example fails to compile on Centos7

- **Issue #:** 1440
- **State:** closed
- **Created:** 2021-04-05T13:32:33Z
- **Updated:** 2022-02-08T11:01:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/1440

I'm trying to compile and run all of the examples in `/opt/rocm-4.1.0/llvm/examples` on our new AMD GPU cluster. The OS is Centos7.

All of the C & Fortran examples work, but the sole C++ example fails:

```
clang++ -O3 \
  -fopenmp \
  -fopenmp-targets=amdgcn-amd-amdhsa \
  -Xopenmp-target=amdgcn-amd-amdhsa \
  -march=gfx906 \
  -o vmul_template \
  /opt/rocm-4.1.0/llvm/examples/openmp/vmul_template/vmul_template.cpp
```

```
In file included from /opt/rocm-4.1.0/llvm/examples/openmp/vmul_template/vmul_template.cpp:2:
In file included from /opt/rocm-4.1.0/llvm/lib/clang/12.0.0/include/openmp_wrappers/math.h:20:
In file included from /opt/rocm-4.1.0/llvm/lib/clang/12.0.0/include/openmp_wrappers/cmath:86:
/opt/rocm-4.1.0/llvm/lib/clang/12.0.0/include/__clang_hip_cmath.h:70:17: error: static declaration of 'isinf' follows non-static declaration
__DEVICE__ bool isinf(double __x) { return ::__isinf(__x); }
                ^
/usr/include/bits/mathcalls.h:202:19: note: previous declaration is here
__MATHDECL_1 (int,isinf,, (_Mdouble_ __value)) __attribute__ ((__const__));
                  ^
In file included from /opt/rocm-4.1.0/llvm/examples/openmp/vmul_template/vmul_template.cpp:2:
In file included from /opt/rocm-4.1.0/llvm/lib/clang/12.0.0/include/openmp_wrappers/math.h:20:
In file included from /opt/rocm-4.1.0/llvm/lib/clang/12.0.0/include/openmp_wrappers/cmath:86:
/opt/rocm-4.1.0/llvm/lib/clang/12.0.0/include/__clang_hip_cmath.h:90:17: error: static declaration of 'isnan' follows non-static declaration
__DEVICE__ bool isnan(double __x) { return ::__isnan(__x); }
                ^
/usr/include/bits/mathcalls.h:235:19: note: previous declaration is here
__MATHDECL_1 (int,isnan,, (_Mdouble_ __value)) __attribute__ ((__const__));
                  ^
2 errors generated.
```