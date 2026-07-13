# Report issues for OpenMP within the ROCm compiler

- **Issue #:** 1308
- **State:** closed
- **Created:** 2020-11-27T11:58:08Z
- **Updated:** 2022-02-22T12:49:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1308

Could you reproduce the following issues for offloading to an AMD GPU using OpenMP within the ROCm compiler ? When you can run any of the applications in my report successfully using your OpenMP within the ROCm compiler, please list them here. Then there may be some issues with my installation and/or build commands for these applications.

In each program with the suffix "-omp", there is a "Makefile.aomp". Please take a look at the file, and modify it for your environment. To build and run a program, go to a directory (e.g. all-pairs-distance-omp) and type

```
make -f Makefile.aomp run
```

Thanks.

The GPU results don't match the CPU results for the following OpenMP programs. 

https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/all-pairs-distance-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/compute-score-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/fft-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/amgmk-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/scan-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/axhelm-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/fpc-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/knn-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/lud-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/myoctye-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/nw-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/particlefilter-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/ccsd-trpdrv-omp

https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/crc64-omp
```
./main 10 5 33554432
Running 10 tests with seed 5
Loading global '_ZL11crc64_table' (Failed)
Libomptarget fatal error 1: failure of target construct while offloading is mandatory
make: *** [Makefile.aomp:65: run] Aborted (core dumped)
```
