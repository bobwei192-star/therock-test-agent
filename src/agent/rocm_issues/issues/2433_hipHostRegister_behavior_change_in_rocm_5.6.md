# hipHostRegister behavior change in rocm 5.6

> **Issue #2433**
> **状态**: closed
> **创建时间**: 2023-09-04T22:12:25Z
> **更新时间**: 2024-06-24T19:15:21Z
> **关闭时间**: 2024-06-24T19:15:21Z
> **作者**: ye-luo
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/2433

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Noticed significant slow down of hipHostRegister which seems due to underlying implementation change to SVM in hsa in rocm 5.6.
There is an undocumented environment variable `HSA_USE_SVM` after digging into ROCr.

[many_transfers.zip](https://github.com/RadeonOpenCompute/ROCm/files/12516910/many_transfers.zip)

All the timings reported here are from runs on a RadeonVII gfx906 but newer GPUs like MI250x shows the same issue.
```
#threaded OMP case
hipcc -fopenmp -g -DCUDA2HIP many_transfer.omp.cpp -o many_transfer.omp.x
```

Using rocm-5.6.0, default setting HSA_USE_SVM=1
```
yeluo@epyc-server:~/temp/many_transfers$ OMP_NUM_THREADS=8 ./many_transfer.omp.x
Function many_transfer.omp HostRegistering takes 5.37867e+07 us # very very slow, a huge regression.
Function many_transfer.omp thread 0 takes 42616.2 us
Function many_transfer.omp thread 2 takes 26110.7 us
Function many_transfer.omp thread 7 takes 28389.9 us
Function many_transfer.omp thread 4 takes 72282.9 us
Function many_transfer.omp thread 3 takes 85687.2 us
Function many_transfer.omp thread 5 takes 87175.1 us
Function many_transfer.omp thread 1 takes 93498.1 us
Function many_transfer.omp thread 6 takes 99937.7 us
```
Usually slower hipHostRegister is not a bit deal since reasonable codes just need to register once. However, in this case, the slowdown is so huge that reasonable codes got noticeable slowdown.
If changing `#define N 16384` to `32768` in the source code, at least 10^8 us is needed in the initialization.

Using rocm-5.6.0, turning off SVM and got back rocm 5.5 behavior in hipHostRegister
```
yeluo@epyc-server:~/temp/many_transfers$ OMP_NUM_THREADS=8 HSA_USE_SVM=0 ./many_transfer.omp.x
Function many_transfer.omp HostRegistering takes 708273 us
Function many_transfer.omp thread 0 takes 49525.1 us
Function many_transfer.omp thread 5 takes 41510.6 us
Function many_transfer.omp thread 7 takes 28397.9 us
Function many_transfer.omp thread 1 takes 28777.3 us
Function many_transfer.omp thread 4 takes 5.62431e+06 us # drunk?
Function many_transfer.omp thread 6 takes 27235.2 us
Function many_transfer.omp thread 2 takes 5.63835e+06 us # drunk?
Function many_transfer.omp thread 3 takes 26933.6 us
```
Some threads seem stranded. Very concerning behavior for codes using multiple streams from host threads.

Using rocm-5.5.0
```
yeluo@epyc-server:~/temp/many_transfers$ OMP_NUM_THREADS=8 ./many_transfer.omp.x
Function many_transfer.omp HostRegistering takes 709061 us
Function many_transfer.omp thread 0 takes 85138.3 us
Function many_transfer.omp thread 5 takes 62581.4 us
Function many_transfer.omp thread 7 takes 34131.3 us
Function many_transfer.omp thread 3 takes 98494.9 us
Function many_transfer.omp thread 6 takes 118628 us
Function many_transfer.omp thread 4 takes 112630 us
Function many_transfer.omp thread 2 takes 127532 us
Function many_transfer.omp thread 1 takes 115938 us
```

Clearly, switching to SVM makes code initialization much longer.
If not using SVM, rocm 5.6 improved hipMemcpyAsync on some threads in a threaded scenario compared to rocm-5.5.0 but still the huge imbalance is also extremely concerning.
