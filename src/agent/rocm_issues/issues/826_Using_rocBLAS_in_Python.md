# Using rocBLAS in Python

> **Issue #826**
> **状态**: closed
> **创建时间**: 2019-06-20T23:30:47Z
> **更新时间**: 2021-03-19T03:34:58Z
> **关闭时间**: 2021-03-19T03:34:58Z
> **作者**: SandboChang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/826

## 描述

Sorry if this is novice question, it will be great if I can have some guides as to where to start.

I want to utilize my GPUs (Vega and Radeon VII) mainly for matrix multiplications.
In Python with Tensorflow, I measured very good performance from the GPUs. However the variable initialization is slow with Tensorflow and I am not familiar with the graph nature of it for just numerical computations.

I used to use PyOpenCL but then most BLAS packages there are out-of-date and do not have optimization for Vega and later GPUs.

If I want to write some basic hipBLAS code and port them to Python 3, where should I start?
Thanks.
