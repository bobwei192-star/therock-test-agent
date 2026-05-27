# Cannot detect OpenCL platform for both amdgpu-pro and rocm-dkms

> **Issue #692**
> **状态**: closed
> **创建时间**: 2019-01-29T09:59:51Z
> **更新时间**: 2019-01-29T17:26:17Z
> **关闭时间**: 2019-01-29T17:26:16Z
> **作者**: ghostplant
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/692

## 描述

Hi,

I have a metal equipped with `Raven Ridge Ryzen 5 2400G` and seems like it is not supporting ROCM at the moment officially. Then I tried to install amdgpu-pro drivers to enable the OpenCL platform for this APU but also reported failure. However, this model should support OpenCL, right?

```sh
$ uname -a
Linux ubuntu 4.18.0-10-generic #11-Ubuntu SMP Thu Oct 11 15:13:55 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
$ /opt/amdgpu-pro/bin/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
$ ./a.out
OpenCL error: clGetPlatformIDs(-1001)

```

My OS is Ubuntu 18.10 with latest Linux image driver 4.18.

Any root cause to lead to the failure? Thanks!


---

## 评论 (2 条)

### 评论 #1 — ghostplant (2019-01-29T10:03:54Z)

More messages:
```sh
$ dmesg | grep kfd
[    1.238024] kfd kfd: Initialized module
[    1.239801] kfd kfd: DID 15dd is missing in supported_devices
[    1.239803] kfd kfd: kgd2kfd_probe failed

$ inxi
CPU: Quad Core AMD Ryzen 5 2400G with Radeon Vega Graphics (-MT MCP-) speed/min/max: 1424/1600/3600 MHz
Kernel: 4.18.0-10-generic x86_64 Up: 41m Mem: 260.4/15041.6 MiB (1.7%) Storage: 223.57 GiB (2.5% used)
Procs: 189 Shell: bash 4.4.19 inxi: 3.0.24
```

---

### 评论 #2 — jlgreathouse (2019-01-29T17:26:16Z)

Support for Raven Ridge [wasn't added to the upstream kfd until 4.19](https://elixir.bootlin.com/linux/v4.19/source/drivers/gpu/drm/amd/amdkfd/kfd_device.c#L277).

---
