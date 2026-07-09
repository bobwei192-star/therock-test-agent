# GPU stuck on lowest power state with ppfeaturemask

- **Issue #:** 504
- **State:** closed
- **Created:** 2018-08-19T14:39:36Z
- **Updated:** 2018-09-19T09:18:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/504

Ubuntu 18.04 4.15.0-32, ROCm 1.8.2, GPU FuryX, CPU AMD Ryzen 1700X.
The GPU was working fine with amdgpu-pro 18.20.
I installed ROCm 1.8.2, and clinfo works correctly.
I tried to run gpuowl https://github.com/preda/gpuowl ,
it runs correctly but very slowly (about 4 times slower than normal).

I see with rocm-smi that the GPU is stuck in the lowest power state, and it draws only 50W (while normally under load draws 220W).

I tried to manually set the power state higher with rocm-smi --setsclk 7, but it has no effect (or the state is immediately reset back to 0).

Seems a similar situation with what's reported here:
https://github.com/RadeonOpenCompute/ROCm/issues/491

Attached output of lshw
[lshw.txt](https://github.com/RadeonOpenCompute/ROCm/files/2300386/lshw.txt)

