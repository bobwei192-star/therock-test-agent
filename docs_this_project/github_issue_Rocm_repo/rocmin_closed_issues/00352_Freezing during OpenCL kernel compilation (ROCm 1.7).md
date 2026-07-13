# Freezing during OpenCL kernel compilation (ROCm 1.7)

- **Issue #:** 352
- **State:** closed
- **Created:** 2018-03-03T16:13:18Z
- **Updated:** 2018-06-06T12:34:26Z
- **Labels:** Under Investigation, Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/352

I'm maintaining a μ-benchmark suite for GPU memories using OpenCL dubbed _gpumembench_. A particular benchmark (_shmembench-ocl_) freezes during compilation when using _int4_ data type. This even happens with ROCm v1.7.1 beta 4. It seems that the problem is triggered by using an unroll directive before the core loop:

```
#pragma unroll 32
for(...)
```

Removing the directive resolves the problem but there has to be a better solution.

The full source code is provided on [gpumembench page on github](https://github.com/ekondis/gpumembench)