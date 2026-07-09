# RX Vega56 - opencl not working on 16.04

- **Issue #:** 389
- **State:** closed
- **Created:** 2018-04-19T18:26:20Z
- **Updated:** 2018-04-20T08:42:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/389

I thought a lot how to properly submit this issue but couldn't find suitable way of doing it.

My issue is ...probably due to using 4.16 but I managed to patch it to support kfd init.
First this is dmesg output: http://paste.ubuntu.com/p/RbxPFvcdF9/
amdkfd is properly loaded and successfully initialized GPU node.
amdgpu successfully recognizes my Vega56 but when I type:

> /opt/rocm/opencl/bin/x86_64/clinfo
> terminate called after throwing an instance of 'cl::Error'
>   what():  clGetPlatformIDs
> Aborted (core dumped)

Here is what happens.
When preloading amdocl64 lib it shows this:

> LD_PRELOAD=/opt/rocm/opencl/lib/x86_64/libamdocl64.so /opt/rocm/opencl/bin/x86_64/clinfo
> Number of platforms:                             1
>   Platform Profile:                              FULL_PROFILE
>   Platform Version:                              OpenCL 2.1 AMD-APP.internal (2576.0)
>   Platform Name:                                 AMD Accelerated Parallel Processing
>   Platform Vendor:                               Advanced Micro Devices, Inc.
>   Platform Extensions:                           cl_khr_icd cl_amd_object_metadata cl_amd_event_callback
> 
> 
>   Platform Name:                                 AMD Accelerated Parallel Processing
> ERROR: clGetDeviceIDs(-1)
> 

Here are kfd nodes:

> root@vega56:/sys/devices/virtual/kfd/kfd/topology/nodes# ls
> 0  1
> root@vega56:/sys/devices/virtual/kfd/kfd/topology/nodes#
> 

First one is obviously CPU a.k.a node/0
Second is GPU node a.k.a node/1

> root@vega56:/sys/devices/virtual/kfd/kfd/topology/nodes# cat 0/gpu_id
> 0
> root@vega56:/sys/devices/virtual/kfd/kfd/topology/nodes# cat 1/gpu_id
> 44526
> root@vega56:/sys/devices/virtual/kfd/kfd/topology/nodes#

I have been struggling to find a way for rocm-opencl to recognize it for a few days.
Any help is appreciated.
Thank you