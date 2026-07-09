# Using rocBLAS in Python

- **Issue #:** 826
- **State:** closed
- **Created:** 2019-06-20T23:30:47Z
- **Updated:** 2021-03-19T03:34:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/826

Sorry if this is novice question, it will be great if I can have some guides as to where to start.

I want to utilize my GPUs (Vega and Radeon VII) mainly for matrix multiplications.
In Python with Tensorflow, I measured very good performance from the GPUs. However the variable initialization is slow with Tensorflow and I am not familiar with the graph nature of it for just numerical computations.

I used to use PyOpenCL but then most BLAS packages there are out-of-date and do not have optimization for Vega and later GPUs.

If I want to write some basic hipBLAS code and port them to Python 3, where should I start?
Thanks.