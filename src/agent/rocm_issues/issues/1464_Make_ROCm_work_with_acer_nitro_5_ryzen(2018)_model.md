# Make ROCm work with acer nitro 5 ryzen(2018) model

> **Issue #1464**
> **状态**: closed
> **创建时间**: 2021-04-30T21:54:07Z
> **更新时间**: 2021-05-03T06:46:50Z
> **关闭时间**: 2021-05-03T06:46:49Z
> **作者**: Shreyashwaghe
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1464

## 描述

I am using a "acer nitro 5 ryzen 5 AN515-42" (2018 model) which has ryzen 2500u ( AMD Raven Ridge (Ryzen 2000 APU)
 series APU) + integrated Radeon RX Vega 8 + discrete radeon rx560x

I have a freshly installed ubuntu 20.04.2 with kernel 5.8.0-48, ( i also tried the base 5.4.0-26-generic kernel too, but no luck) and followed the installation of ROCm v4.1

opt/rocm/bin/rocminfo               
ROCk module is loaded
Unable to open /dev/kfd read-write: Operation not permitted
shreyash is member of render group

/opt/rocm/opencl/bin/clinfo        
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3241.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0

Other things, which may be helpful -

dmesg | grep kfd
[   19.344100] kfd kfd: Allocated 3969056 bytes on gart
[   19.344988] kfd kfd: added device 1002:67ef
[   19.813048] kfd kfd: Allocated 3969056 bytes on gart
[   19.813420] kfd kfd: added device 1002:15dd

Looks like rocm installation isnt detecting the gpu devices:
sudo lshw -c video
  *-display                 
       description: Display controller
       product: Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:01:00.0
       version: c0
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:59 memory:d0000000-dfffffff memory:e0000000-e01fffff ioport:3000(size=256) memory:e0a00000-e0a3ffff memory:e0a40000-e0a5ffff
  *-display
       description: VGA compatible controller
       product: Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:04:00.0
       version: c4
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi msix vga_controller bus_master cap_list
       configuration: driver=amdgpu latency=0
       resources: irq:63 memory:b0000000-bfffffff memory:c0000000-c01fffff ioport:1000(size=256) memory:e0800000-e087ffff




---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-05-03T06:46:49Z)

Thanks @Shreyashwaghe for reaching out.
We are not officially supporting gfx8 IP devices anymore.
We are also not supporting integrated GPUs with ROCm.
Request you to look at [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)
Hope this helps.
Thank you.

---
