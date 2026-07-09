# Determine to which NUMA node a GPU belongs from an OpenCL device ID

- **Issue #:** 563
- **State:** closed
- **Created:** 2018-09-27T20:32:40Z
- **Updated:** 2018-10-08T19:07:53Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/563

Hi everybody,

first of all, this a feature request, not a bug report.
Dual socket mainboards contain two or more NUMA nodes. There are systems out there that allow connecting multiple GPUs to each GPU, for example via a PCIe witch. See this machine for example: 
[https://www.supermicro.com/products/system/4U/4028/SYS-4028GR-TR.cfm](url)

When a system with two or more NUMA nodes is used, it is important to bind processes to NUMA nodes and to allocate memory locally, i.e. on the NUMA node that the process was bound to. Otherwise, the performance will decrease due to remote memory access. I have not tested this but I am 100% sure, that the same logic applies to programs using GPUs as well. For example, let's consider a system with 2 NUMA nodes where each node contains a single GPU. If a program runs on NUMA node 0 and uses the GPU that is connected to NUMA node 1, the performance will be less compared to a program running on NUMA node 0 and uses the GPU that is connected to NUMA node 0. When I say performance, I mean host<->device memory transfers in OpenCL.

So here is my question or feature request: When I used clGetDeviceID to get the device IDs for the GPUs, how can I tell to which NUMA node the GPU belongs? Is it possible to extract the PCIe bus ID from the device ID? Are the device IDs returned by clGetDeviceID ordered in some way?

After a short google search it seems that others had similar question years ago but I found no satisfying answer.

This is not super urgent but it is relevant in a HPC context.

Greetings!