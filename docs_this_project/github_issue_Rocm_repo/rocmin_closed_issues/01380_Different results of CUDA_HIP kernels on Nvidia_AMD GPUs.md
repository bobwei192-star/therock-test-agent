# Different results of CUDA/HIP kernels on Nvidia/AMD GPUs

- **Issue #:** 1380
- **State:** closed
- **Created:** 2021-02-13T18:49:44Z
- **Updated:** 2022-03-19T18:26:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/1380

Hello,

I have a kernel, that uploads 4096 float2 numbers with 512 threads (each stores 8 numbers) and does some reordering using 32KB of statically allocated shared memory. CUDA version run on Nvidia 1660Ti GPU produces the correct result. HIP version (obtained with hipify) run on AMD MI100 and Radeon VII produces a different result. I attach both kernels and outputs. What can be the issue behind this behavior? Thank you.

[test.zip](https://github.com/RadeonOpenCompute/ROCm/files/5976267/test.zip)

Best regards,
Dmitrii Tolmachev