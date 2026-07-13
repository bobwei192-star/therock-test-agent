# Question about ROCm

- **Issue #:** 44
- **State:** closed
- **Created:** 2016-10-30T15:29:44Z
- **Updated:** 2016-10-31T01:56:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/44

I have a GPU-accelerated video compression application - very memory intensive.

I use OpenCL 1.2.  There is no need for device side enqueue, or to have different
GPUs communicate with each other.

Is there an advantage to using ROCm over regular OpenCL runtime, for my application?

I have heard that performance is better due to lower host-side overhead.

Thanks so much,
Aaron
