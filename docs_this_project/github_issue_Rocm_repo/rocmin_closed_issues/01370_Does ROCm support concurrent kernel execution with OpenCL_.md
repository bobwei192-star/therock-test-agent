# Does ROCm support concurrent kernel execution with OpenCL?

- **Issue #:** 1370
- **State:** closed
- **Created:** 2021-02-04T07:41:28Z
- **Updated:** 2021-02-09T07:30:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/1370

Let's suppose there are multiple command queues with single device.
If multiple cl_kernel with very small global work item size are enqueued to each queues, are they executed concurrently?

I'm using RX 5700 XT, ubuntu 20.04 and ROCm 3.10.0.