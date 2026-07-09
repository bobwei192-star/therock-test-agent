# memory bandwidth of HBM1 drops with more than 2GB to consume

- **Issue #:** 102
- **State:** closed
- **Created:** 2017-03-28T21:18:49Z
- **Updated:** 2018-06-03T14:46:37Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/102

Hi, I ran a series of GPU-stream instances on a R9 Fiji Nano with rocm 1.4 on a E5 haswell box. I looked at the OpenCL and HIP implementations available in [GPU-Stream 3.1](https://github.com/UoB-HPC/GPU-STREAM). 

I am wondering why the bandwidth drops off by 2x after a total of 2GB of data is consumed on the device. I attached the plot here.

![gpu_stream_add_bandwidth_rocm](https://cloud.githubusercontent.com/assets/1465603/24427876/c69581e6-140c-11e7-903f-4e8a88110e62.png)
