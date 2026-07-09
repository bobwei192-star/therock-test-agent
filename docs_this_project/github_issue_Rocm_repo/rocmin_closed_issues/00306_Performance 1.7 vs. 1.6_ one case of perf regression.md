# Performance 1.7 vs. 1.6, one case of perf regression

- **Issue #:** 306
- **State:** closed
- **Created:** 2018-01-21T13:07:27Z
- **Updated:** 2018-06-06T12:33:28Z
- **Labels:** Compiler Performance Issue
- **URL:** https://github.com/ROCm/ROCm/issues/306

Ubuntu 16.04.3, Vega 64, ROCm 1.7 vs. 1.6

Using GpuOwl https://github.com/preda/gpuowl/tree/9fc4b1c0b1a9769bf29688e9ad0cc3c36dc606be

For most of the kernels, performance of 1.7 is "same or better" than 1.6, mostly small increases, nice.

But for one problem kernel (the kernel "tail"), there is a significant performance drop in 1.7.

This seems to be related to https://github.com/RadeonOpenCompute/ROCm/issues/241
In that issue, this same kernel "tail", in 1.6 was compiled to either a fast or a slow variant with about equal chances. It seems that 1.7 is generating only the "slow" variant for that kernel.

I attach the ISA dumps of this kernel, as compiled by 1.6 in the "fast" variant, and as compiled by 1.7.
A diff of the two ISA shows a hint to the cause of the problem: while 1.6 uses workitem_private_segment_byte_size = 100, 1.7 uses workitem_private_segment_byte_size = 152.

For this kernel, the performance drop in 1.7 vs. 1.6 is 16%.

What is interesting, is that exactly the same problem was present in 1.6 in the form of the fast/slow compilation https://github.com/RadeonOpenCompute/ROCm/issues/241 , if that may help pin it down.
[tail-1.6.txt](https://github.com/RadeonOpenCompute/ROCm/files/1649758/tail-1.6.txt)
[tail-1.7.txt](https://github.com/RadeonOpenCompute/ROCm/files/1649759/tail-1.7.txt)

