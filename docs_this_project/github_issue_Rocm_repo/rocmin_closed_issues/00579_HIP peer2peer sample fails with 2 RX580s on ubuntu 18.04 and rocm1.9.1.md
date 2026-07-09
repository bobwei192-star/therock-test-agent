# HIP peer2peer sample fails with 2 RX580s on ubuntu 18.04 and rocm1.9.1

- **Issue #:** 579
- **State:** closed
- **Created:** 2018-10-16T16:18:00Z
- **Updated:** 2019-02-08T17:49:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/579

I tried running the peer2peer application provided in with the hip installation found at the following location: "/opt/rocm/hip/samples/2_Cookbook/8_peer2peer".
However with 2 RX580s I got the following failure: 
"**peer2peer transfer not possible between the selected gpu devices**".

From the release notes of ROCm1.9.1 I see the following: "_Some ROCm features are not available in the upstream KFD: * More system memory available to ROCm applications * Interoperability between graphics and compute * RDMA * IPC_".

The statement would imply the RDMA should work with the latest amd rocm-dkms package. Is my understanding correct? 

If it is not supported is there a target version for this support?