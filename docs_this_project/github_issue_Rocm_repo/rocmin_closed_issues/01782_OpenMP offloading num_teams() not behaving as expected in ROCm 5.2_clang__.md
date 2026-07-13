# OpenMP offloading num_teams() not behaving as expected in ROCm 5.2/clang++

- **Issue #:** 1782
- **State:** closed
- **Created:** 2022-08-07T09:40:35Z
- **Updated:** 2022-08-11T20:49:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/1782

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
