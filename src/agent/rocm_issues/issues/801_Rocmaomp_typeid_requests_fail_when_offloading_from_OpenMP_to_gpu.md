# Rocm/aomp: typeid requests fail when offloading from OpenMP to gpu

> **Issue #801**
> **状态**: closed
> **创建时间**: 2019-05-20T13:13:01Z
> **更新时间**: 2023-12-21T14:32:59Z
> **关闭时间**: 2023-12-21T14:32:58Z
> **作者**: D-Dirk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/801

## 描述

I am using rocm 2.4 on Ubuntu 18.04 with the rocm aomp tools and compilers based on clang 8 for offloading from OpenMP to AMD GPUs: 

[link to rocm/aomp project](https://github.com/ROCm-Developer-Tools/aomp)

The code works fine as long as I offload to the CPUs. However, once I offload to my GPU it only compiles and works when I remove all typeid requests. But I need these requests to pass the results and data from and to Rcpp (at least I get 18 errors if I don't have them all concerning typeid). The aomp compiler based on clang 8 suggests to compile with option -frtti but if I recompile my program with that option, the compilation still fails with the same error message. 

I provide a minimal example by simply adding a single typeid request  and the required header to one of the working examples from aomp, namely reduction.c: 

[link to aomp example "reduction"](https://github.com/ROCm-Developer-Tools/aomp/tree/master/examples/openmp/reduction)

`#include <stdio.h>
 #define N   1000000ll
 #define SUM (N * (N-1)/2)

int main (void)
{
  long long a, i;

//std::cout << typeid(a).name() << std::endl;

  #pragma omp target parallel shared(a) private(i)
  {
    #pragma omp master
    a = 0;

    #pragma omp barrier

    #pragma omp for reduction(+:a)
    for (i = 0; i < N; i++) {
        a += i;
    }

    // The Sum shall be sum:[0:N]
    #pragma omp single
    {
      if (a != SUM)
        printf ("Incorrect result = %lld, expected = %lld!\n", a, SUM);
      else
        printf ("The result is correct = %lld!\n", a);
    }
  }

  return 0;
}`

This works fine when compiled unchanged with the following options:

`$ /opt/rocm/aomp/bin/clang++ -frtti -target x86_64-pc-linux-gnu -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx906 reduction.c`

However, when I uncomment the single typeid request in the code above and add the required headers at the very top:

`#include <typeinfo>
#include <iostream>`

the compilation fails with the error:

`reduction.c:12:14: error: use of typeid requires -frtti`

which is however already used. Once I compile with CPU options only, it works again:

`$ /opt/rocm/aomp/bin/clang++ -target x86_64-pc-linux-gnu -fopenmp  reduction.c`

Does anybody know the reason for this problem and how it can be solved? Any hint would be greatly appreciated!




---

## 评论 (2 条)

### 评论 #1 — tasso (2023-12-18T18:58:49Z)

Is this still reproducible?  If not, can we please close it?  Thanks!

---

### 评论 #2 — tasso (2023-12-21T14:32:58Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will happy to investigate it.  Thanks!

---
