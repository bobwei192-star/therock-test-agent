# RDMA support

- **Issue #:** 744
- **State:** closed
- **Created:** 2019-03-19T18:30:17Z
- **Updated:** 2023-12-09T01:53:26Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/744

Is there documentation somewhere or an example of how to use RDMA/Peer Direct with OpenCL or HIP? The page at https://rocm-documentation.readthedocs.io/en/latest/Remote_Device_Programming/Remote-Device-Programming.html seems to describe details about the underlying implementation, but I am not clear how to use it in practice.

My current goal is to transfer data between two Radeon Pro WX 8200 cards on different machines over an infiniband interconnect. I'm not sure how I would initiate a transfer of an OpenCL buffer, perhaps I need to be using HIP instead?