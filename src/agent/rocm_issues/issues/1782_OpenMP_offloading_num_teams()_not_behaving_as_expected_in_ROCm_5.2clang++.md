# OpenMP offloading num_teams() not behaving as expected in ROCm 5.2/clang++

> **Issue #1782**
> **状态**: closed
> **创建时间**: 2022-08-07T09:40:35Z
> **更新时间**: 2022-08-11T20:49:45Z
> **关闭时间**: 2022-08-11T20:49:45Z
> **作者**: vincentadamthefirst
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1782

## 描述

I am currently working with OpenMP offloading to AMD GPUs and found a strange bug while benchmarking my code.
I utilize the clause `num_teams` in my application but as far as I can tell it seems to have no effect when executing the code.

To illustrate the problem I use this simple C++ program:
```c++
#include <iostream>
#include <omp.h>

#define SIZE 16777216 // 2^24
#define THREADS_PER_TEAM 512
#define NUM_TEAMS 32768 // = SIZE / THREADS_PER_TEAM

void copy(double* A, double* B) {
#pragma omp target data map(to:A[0:SIZE]) map(tofrom:B[0:SIZE])
    {
        size_t i, j;
#pragma omp target teams distribute num_teams(NUM_TEAMS) thread_limit(THREADS_PER_TEAM)
        for (i = 0; i < SIZE; i += THREADS_PER_TEAM) {
#pragma omp parallel for num_threads(THREADS_PER_TEAM)
            for (j = i; j < i + THREADS_PER_TEAM; j++) {
                B[j] = A[j];
            }
        }
    }
}

int main() {
    double* A = (double*) malloc(SIZE * sizeof(double));
    double* B = (double*) malloc(SIZE * sizeof(double));

    std::cout << "SIZE        = " << SIZE << std::endl;
    std::cout << "NUM_TEAMS   = " << NUM_TEAMS << std::endl;
    std::cout << "NUM_THREADS = " << THREADS_PER_TEAM << std::endl;

    for (uint64_t i = 0; i < SIZE; i++) {
        A[i] = i;
    }

    copy(A, B);
}
```

It copies elements from one array to another and uses blocking to split the workload onto multiple teams (each team handles THREADS_PER_TEAM copies). This code is not very efficient and is only meant to illustrate the problem.

To compile this code I used `AMD clang version 14.0.0 (... roc-5.2.0 ...)` using these flags:
```shell
amdclang++ -std=c++11 -O3 -g -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx90a example.cpp -o rocm_example
```

I compiled the code both for a MI50 (gfx906) and MI250 (gfx90a) and profiled it via `rocprof` to read the kernel grid size and work group size. The results of the profiling can be seen here:

MI50:
```csv
Index,KernelName,gpu-id,queue-id,queue-index,pid,tid,                   grd,      wgr, lds,scr,vgpr,sgpr,fbar
0,"__omp_offloading_2a_d4ce97d__Z4copyPdS__l13.kd",0,0,0,136496,136496, 16777216, 512, 512,0,40,48,0
```

MI250:
```csv
Index,KernelName,gpu-id,queue-id,queue-index,pid,tid,               grd,      wgr, lds,scr,vgpr,sgpr,fbar
0,"__omp_offloading_29_d4ce97d__Z4copyPdS__l13.kd",0,0,0,8741,8741, 16777216, 512, 512,0,20,48,0
```

It can be seen, that the grid sizes are 16777216 (the upper limit of the associated for loop) where they should be at most 32768.
I think this is a bug with the current compiler or am I missing something?


---

## 评论 (2 条)

### 评论 #1 — Lynd98 (2022-08-10T19:45:03Z)

Hi vincentadamthefirst,

The grid size is not the same as the number of teams.  Try running with “export LIBOMPTARGET_KERNEL_TRACE=1”, which shows the number of teams and number of threads in parenthesis.  The numbers in parenthesis for “reqd” are the requested (number of teams, number of threads) and the numbers in parenthesis for “teamsXthrds” are the actual (number of teams, number of threads). 

Here is my execution of rocm.cpp with LIBOMPTARGET_KERNEL_TRACE=1.

   $ export LIBOMPTARGET_KERNEL_TRACE=1
   $ clang++ -std=c++11 -O2 -g -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx90a rocm.cpp -o rocm_exampl
   $ ./rocm_exampl
   SIZE        = 16777216
   NUM_TEAMS   = 32768
   NUM_THREADS = 512
   DEVID: 0 SGN:3 ConstWGSize:513  args: 2 teamsXthrds:(32768X 512) reqd:(32768X 512) lds_usage:9808B sgpr_count:108 vgpr_count:57 sgpr_spill_count:27 vgpr_spill_count:0 tripcount:32768 rpc:1 n:__omp_offloading_fd00_19e4120__Z4copyPdS__l12

I see one kernel invocation and it is correct for both grid size (32768 * 512), number of teams (32768), and number of threads (512).  You set num_teams and num_threads in the source code and they were set to the correct values in execution.

Lynd

---

### 评论 #2 — vincentadamthefirst (2022-08-11T20:49:45Z)

Hi @Lynd98,

thank you very much for that explanation.
Everything works as intended as you said, I just made a huge mistake by thinking grid size = number of teams.
I think this comes from working with `NSight Compute` which reports the 32768 teams as the grid size.

Thanks again for the clarification,

Vincent



---
