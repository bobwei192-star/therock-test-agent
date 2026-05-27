# HIP peer2peer sample fails with 2 RX580s on ubuntu 18.04 and rocm1.9.1

> **Issue #579**
> **状态**: closed
> **创建时间**: 2018-10-16T16:18:00Z
> **更新时间**: 2019-02-08T17:49:39Z
> **关闭时间**: 2019-02-08T17:49:38Z
> **作者**: x3ccd4828
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/579

## 描述

I tried running the peer2peer application provided in with the hip installation found at the following location: "/opt/rocm/hip/samples/2_Cookbook/8_peer2peer".
However with 2 RX580s I got the following failure: 
"**peer2peer transfer not possible between the selected gpu devices**".

From the release notes of ROCm1.9.1 I see the following: "_Some ROCm features are not available in the upstream KFD: * More system memory available to ROCm applications * Interoperability between graphics and compute * RDMA * IPC_".

The statement would imply the RDMA should work with the latest amd rocm-dkms package. Is my understanding correct? 

If it is not supported is there a target version for this support?

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-02-08T17:49:38Z)

Hi @x3ccd4828 

Peer to peer communication between GPUs in the ROCm software stack requires that your GPUs and system support [PCIe large BAR](https://rocm.github.io/ROCmPCIeFeatures.html). If this is not enabled on your CPU/motherboard/BIOS, then even supported GPUs will not be able to talk to one another. The [ROCm bandwidth test application](https://github.com/RadeonOpenCompute/rocm_bandwidth_test) can also verify if your GPUs can talk to one another over peer-to-peer communication.

Note also that your *GPUs* must also support large PCIe BAR space for peer to peer. We do not enable this on our consumer class GPUs (Radeon-branded). This is usually a feature found in our workstation Radeon Pro or server Radeon Instinct GPUs.

---
