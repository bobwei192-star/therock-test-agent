# /opt/rocm/opencl/bin/clinfo runs but not  /opt/rocm/bin/rocminfo , Ubuntu20.04 on azure

> **Issue #1807**
> **状态**: closed
> **创建时间**: 2022-09-14T09:11:17Z
> **更新时间**: 2022-10-13T23:08:43Z
> **关闭时间**: 2022-10-13T23:08:43Z
> **作者**: maxmanus96
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1807

## 描述

Hi,
I installed ROCm using official guide on Ubuntu 20.04 on Azure from [here](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#rocm-installation-guide-v5-0)
However, when I run rocminfo it shows `ROCk module is NOT loaded, possibly no GPU devices`. However, I am SURE we have graphic card it is AMD Vega 10. `VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon Instinct MI25 MxGPU] (prog-if 00 [VGA controller])` and Kernel is successfully installed when I run the command `sudo dkms status` I have the output `amdgpu, 5.16.9.22.20-1438746~20.04, 5.15.0-1017-azure, x86_64: installed`, 
also clinfo runs successfully;
```
opt/rocm/opencl/bin/clinfo
Number of platforms: 2
  Platform Profile: FULL_PROFILE
  Platform Version: OpenCL 1.1 Mesa 21.2.6
  Platform Name: Clover
  Platform Vendor: Mesa
  Platform Extensions: cl_khr_icd
  Platform Profile: FULL_PROFILE
  Platform Version: OpenCL 2.1 AMD-APP (3452.0)
  Platform Name: AMD Accelerated Parallel Processing
  Platform Vendor: Advanced Micro Devices, Inc.
  Platform Extensions: cl_khr_icd cl_amd_event_callback 


  Platform Name: Clover
Number of devices: 0
  Platform Name: AMD Accelerated Parallel Processing
Number of devices: 0
```

Eventually, since `rocminfo ` does show above error, I think installation is not successful. Therefore. I am looking for your help. Best Regards,

---

## 评论 (1 条)

### 评论 #1 — maxmanus96 (2022-09-14T10:17:31Z)

It turns out Kernel version was not right. On Ubuntu 20.04 Kernel 5.11 HWE is supported. I had version 5.15 kernel, doing downgrade to my Kernel version now.

---
