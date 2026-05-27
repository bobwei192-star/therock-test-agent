# confirm incompatibility APU raven ridge A12 

> **Issue #686**
> **状态**: closed
> **创建时间**: 2019-01-24T11:33:47Z
> **更新时间**: 2019-01-29T21:37:22Z
> **关闭时间**: 2019-01-29T21:37:21Z
> **作者**: Payback80
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/686

## 描述

Hello,
i have a notebook with this apu, i can run DL with plaidml, but i'd like to run tensorflow
target system is Ubuntu 18.10 (i tried 18.04 too), tried both rocm-dkms and the upstream driver, but i still get the infamous message: 

`hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104
`
and
`/opt/rocm/opencl/bin/x86_64/clinfo `

dmesg | grep kfd   returns: 

`andrea@andrea-HP-15-bw0xx:~$ dmesg | grep kfd
[   16.014377] kfd kfd: Initialized module
[   16.496547] kfd kfd: Allocated 3969056 bytes on gart
[   16.496593] kfd kfd: error getting iommu info. is the iommu enabled?
[   16.496598] kfd kfd: Error initializing iommuv2
[   16.496728] kfd kfd: device 1002:9874 NOT added due to errors
[   16.523031] amdgpu 0000:05:00.0: kfd not supported on this ASIC
`

So is there a way to install and use tensorflow or shall we wait for support? Also is there any plan to make it kernel version agnostic? 

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-01-29T21:37:21Z)

Hi @Payback80 

A few things:

1. It does not appear that your IOMMU is enabled. This may be a system BIOS misconfiguration or a lack of IOMMU enablement in your system BIOS.
2. It appears that your APU is a Carrizo or Bristol Ridge, not a Raven Ridge. This is based on KFD detecting PCIe device `1002:9874`, which is the GPU for a Carrizo part.
3. Neither Carrizo nor Raven Ridge are currently supported in TensorFlow at this time.

---
