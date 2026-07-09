# Q: OpenCL: perf impact of SVM vs. cl_mem buffers

- **Issue #:** 655
- **State:** closed
- **Created:** 2019-01-02T01:28:33Z
- **Updated:** 2021-05-09T20:07:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/655

I would like to ask: what is the expected performance impact of using SVM (clSVMAlloc) memory vs. "classic" OpenCL buffers (clCreateBuffer).

In particular in this scenario: two GPUs, accessing (read+write) disjoint regions of the same SVM buffer.

In the "high performance" scenario, I'd expect a memory page (4KB?) to be migrated locally to the GPU that's accessing it, and provide high local speed.

In the "low performance" scenario, I imagine the physical memory residing in one place (host or one GPU), and the access being done through PCIe, and that'd be slow.

So, do SVM buffers offer the same performance as "classic" buffers, or should I expect SVM to be slower?
thanks