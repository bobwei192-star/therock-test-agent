# C++ OpenMP offloading example fails to compile on Centos7

> **Issue #1440**
> **状态**: closed
> **创建时间**: 2021-04-05T13:32:33Z
> **更新时间**: 2022-02-08T11:01:00Z
> **关闭时间**: 2022-02-08T11:00:59Z
> **作者**: nolta
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1440

## 描述

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

---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2021-04-06T07:06:59Z)

Thanks @nolta for reaching out.
I will check this for you and get back with an update.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-04-06T13:25:47Z)

Can you please share the exact steps you followed, to reproduce the problem.
Thank you.

---

### 评论 #3 — nolta (2021-04-06T14:31:47Z)

```
$ scl enable devtoolset-7 bash
$ /opt/rocm-4.1.0/llvm/bin/clang++ -O3 \
  -fopenmp \
  -fopenmp-targets=amdgcn-amd-amdhsa \
  -Xopenmp-target=amdgcn-amd-amdhsa \
  -march=gfx906 \
  -o vmul_template \
  /opt/rocm-4.1.0/llvm/examples/openmp/vmul_template/vmul_template.cpp
```

---

### 评论 #4 — ROCmSupport (2021-04-07T12:31:24Z)

Hi @nolta
I tried the same sample and am able to see output executable like "vmul_template".
I tried just now on CentOS 8. Let me check with CentOS 7 and update you asap.

/opt/rocm-4.1.0/llvm/bin/clang++ -O3   -fopenmp   -fopenmp-targets=amdgcn-amd-amdhsa   -Xopenmp-target=amdgcn-amd-amdhsa   -march=gfx906   -o vmul_template   /opt/rocm-4.1.0/llvm/examples/openmp/vmul_template/vmul_template.cpp

[taccuser@z-MI50-1804-Triage ~]$ ./vmul_template
Success

Thank you.

---

### 评论 #5 — ROCmSupport (2021-04-08T10:07:58Z)

Hi @nolta 
I am able to reproduce the problem with CentOS 7 docker.
Strange that test compiler and PASSED with ROCm 4.1 + CentOS 8.2.
But compilation failed with ROCm 4.1 + CentOS 7 docker.
Trying to find out the difference. Will keep you posted.


---

### 评论 #6 — ROCmSupport (2021-12-13T05:46:03Z)

Hi @nolta 
Good news. This issue is fixed with our internal builds and so the fix will be part of ROCm 5.0. Hope it helps.
Thank you.

---

### 评论 #7 — ROCmSupport (2022-02-08T11:00:59Z)

Verified with 5.0 internal builds and issue is fixed. Fixes are in 5.0.

---
