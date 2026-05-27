# Problem installing rocm-dkms on different Linux distributes and PCs. 

> **Issue #902**
> **状态**: closed
> **创建时间**: 2019-10-05T05:58:21Z
> **更新时间**: 2019-10-06T08:45:17Z
> **关闭时间**: 2019-10-05T19:00:03Z
> **作者**: 1234bpv
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/902

## 描述

Greetings.
I have unsuccessfully tried to install ROCm on different Linux distributives (Ubuntu 16.04, 18.04, CentOS 7.4, 7.6, 7.7). 
My PC hardware is AMD RX580, FX8300, Asus m5a99x Evo, 16gb ddr3.
Notebook: Dell 7375 (Ryzen 2500U, Vega8, 32gb ddr4).
I have tried using both rocm-dkms packages and using upstream kernel driver (uname –r shows, that kernel did not change after installation), that both led to the same error.
On versions 2.2, 2.3, 2.5 error is:

```
pavlo@pavlo-desktop:~$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
pavlo@pavlo-desktop:~$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104
```

On versions 2.7.2, 2.8 error is:

```
pavlo@pavlo-desktop:~$ /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2973.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
pavlo@pavlo-desktop:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
pavlo is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.8@2/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

```

I`ve used a tutorial from https://rocm.github.io/ROCmInstall.html.
Thank you for your help.


---

## 评论 (5 条)

### 评论 #1 — JMadgwick (2019-10-05T14:14:16Z)

> My PC hardware is AMD RX580, FX8300

Unfortunately that isn't a supported configuration. RX 580 is a GFX8 GPU, [it requires PCIe 3.0 with atomics](https://github.com/RadeonOpenCompute/ROCm#supported-cpus). Your CPU and motherboard do not support that, ROCm will not work with this configuration.

You will need to replace your Motherboard and CPU with something Newer. AMD Ryzen CPUs or Intel Haswell or newer and anything newer will work.

---

### 评论 #2 — 1234bpv (2019-10-05T18:03:48Z)

Thank you for reply.
I also tried to use my notebook with Ryzen 2500U and Radeon Vega 8 iGPU, but I get the same errors. Can you help me to set up rocm-dkms on notebook? Or maybe there is another way to run tensorfow-rocm on my pc?

---

### 评论 #3 — JMadgwick (2019-10-05T18:28:04Z)

>  Ryzen 2500U and Radeon Vega 8 iGPU

This is an APU, [Please see the comments here.](https://github.com/RadeonOpenCompute/ROCm#supported-gpus) Primarily this section further down:

> AMD "Raven Ridge" APUs are enabled to run OpenCL, but do not yet support HCC, HIP, or our libraries built on top of these compilers and runtimes.

Your Vega 8 is Raven Ridge and so is also not supported for what you want to do. For OpenCL is would probably be better to install AMDGPU-PRO.
Primarily only recent Mid to High end AMD Desktop GPUs are supported by ROCm. The only Laptops will full support are those with an RX 5XX series GPU and certain PCIe configurations.

---

### 评论 #4 — 1234bpv (2019-10-05T19:00:02Z)

Thank you for help and quick response. Probably upgrade my pc to new Ryzen 3000.

---

### 评论 #5 — seesturm (2019-10-06T08:45:17Z)

> > Ryzen 2500U and Radeon Vega 8 iGPU
> 
> This is an APU, [Please see the comments here.](https://github.com/RadeonOpenCompute/ROCm#supported-gpus) Primarily this section further down:
> 
> > AMD "Raven Ridge" APUs are enabled to run OpenCL, but do not yet support HCC, HIP, or our libraries built on top of these compilers and runtimes.

Couldn't this statement be interpreted as "ROCm backend supports Raven Ridge, but out of the three frontends (OpenCL, HCC, HIP) only OpenCL is supported" ? This is at least my interpretation when reading another statement "... and "Raven Ridge" APUs are enabled in our upstream drivers and the ROCm OpenCL runtime".

Nevertheless, the page also says that one "requires the use of upstream kernel drivers" (this probably means that a recent linux 5.x kernel needs to be compiled instead of rocm-dkms) and that there are known issues with many notebook manufactures omitting crucial information from the BIOS.

I'm writing this also because I don't have an APU and am curious if anyone ever got ROCm OpenCL running with an APU.

---
