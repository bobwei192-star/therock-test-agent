# OpenCL GPU-resident memory swapped out?

- **Issue #:** 673
- **State:** closed
- **Created:** 2019-01-16T19:23:28Z
- **Updated:** 2019-03-15T20:00:37Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/673

ROCm 2.0 OpenCL, Vega64, Ubuntu 18.10 w linux 4.20.

In OpenCL I'm trying to allocate the maximum amount of GPU memory, by doing a repeated creation of a buffer of size 36MB. This buffer is allocated with CL_MEM_READ_WRITE | CL_MEM_HOST_NO_ACCESS to clCreateBuffer(). Just to make sure that the buffer is actually allocated, I also do a clEnqueueFillBuffer() for the full size of the newly created buffer with zeros and wait on it with clFinish().

My GPU has 8GB of physical GPU memory. I expect the buffers to reside on the GPU (because CL_MEM_HOST_NO_ACCESS). Yet somehow I can allocate without error (and write to as indicated above) 374 buffers (of 36MB each), for a total of about 13GB (after the 374 buffers I get CL_MEM_OBJECT_ALLOCATION_FAILURE on buffer creation).

How is this possible -- that I can allocate and write to 13GB of GPU resident buffers on a 8GB Vega64?

To investigate I started to query CL_DEVICE_GLOBAL_FREE_MEMORY_AMD after each allocation, and what I see is this: initially the free memory is decreasing at the expected rate of 36MB per allocation. But later on, the allocations continue to proceed successfully while the free memory remains constant at 53MB. Another observation, once the 53MB point is reached, the allocations become slower.

2019-01-17 06:01:15 vega0 GPU free mem 7937 MB
2019-01-17 06:01:15 vega0 GPU free mem 7901 MB
2019-01-17 06:01:15 vega0 GPU free mem 7865 MB
[...]
2019-01-17 06:01:16 vega0 GPU free mem 197 MB
2019-01-17 06:01:16 vega0 GPU free mem 161 MB
2019-01-17 06:01:16 vega0 GPU free mem 125 MB
2019-01-17 06:01:16 vega0 GPU free mem 89 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:17 vega0 GPU free mem 53 MB
2019-01-17 06:01:17 vega0 GPU free mem 53 MB

What is happening? is GPU memory evicted to host memory? something else? can the behavior be controlled? (what I want to achieve is "fast GPU-resident memory" without any over-allocation)
