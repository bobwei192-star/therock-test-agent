# New system: Debian 9.8 with ROCm - rocm-smi works but not clinfo

> **Issue #723**
> **状态**: closed
> **创建时间**: 2019-03-04T09:59:25Z
> **更新时间**: 2019-03-05T19:46:13Z
> **关闭时间**: 2019-03-04T15:28:36Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/723

## 描述

The clinfo command returns error -1001.
rocm-smi works and shows gpu correctly.


---

## 评论 (8 条)

### 评论 #1 — valeriob01 (2019-03-04T15:28:34Z)

I have resolved this by installing mesa-opencl-icd and now clinfo works.
Depending on the kernel version I get varying results:
-kernel 4.19 : ... PCI device rejects atomics ...
-kernel 4.9 : ... GPU recognized, but program still fails with kernel panic on opencl compilation.


---

### 评论 #2 — jlgreathouse (2019-03-04T15:28:36Z)

Debian is not an AMD-supported distribution for ROCm. You are welcome to ask for community help in Debian forums or mailing lists, but I cannot walk you through bugtesting an unsupported distribution. "clinfo returning error" could be anything from:

- driver not installed correctly (does `dmesg | grep kfd` show your device is found?)
- ROCT and/or ROCR not installed correctly (does `rocminfo` work?)
- OpenCL runtime not installed correctly (our .deb files are built for Ubuntu, not Debian, and so they may not work with your distro)
- Unsupported hardware (have you tried with a supported distro?)

---

### 评论 #3 — jlgreathouse (2019-03-04T15:30:30Z)

If your device rejects PCI atomics, then it is not supported on ROCm even in supported distributions. It is an unsupported hardware configuration (so my 4th guess in my post above).

`mesa-opencl-icd` is a separate OpenCL runtime and is not the AMD OpenCL runtime, so by installing it you are by passing the entire ROCm stack.

---

### 评论 #4 — valeriob01 (2019-03-04T15:32:27Z)

> If your device rejects PCI atomics, then it is not supported on ROCm even in supported distributions. It is an unsupported hardware configuration (so my 4th guess in my post above).

I restate this: gpu rejects atomics based only with some kernel version.

> `mesa-opencl-icd` is a separate OpenCL runtime and is not the AMD OpenCL runtime, so by installing it you are by passing the entire ROCm stack.

so why clinfo is working ?


---

### 评论 #5 — jlgreathouse (2019-03-04T16:08:36Z)

Older kernel version (4.9) do not natively support ROCm software and do not have working KFD drivers in them. The KFD driver did not emit the "PCI rejects atomics" warning message until later versions. Whether or not PCI atomics work is a hardware issue, not a driver issue.

clinfo works because you have a working OpenCL installation. It's Mesa OpenCL, however, and not ROCm OpenCL.

---

### 评论 #6 — valeriob01 (2019-03-05T08:16:51Z)

It turns out that the main-board has Gen2 3.0 PCIe slots (full-width).
I am stumbled by the lack of platform support of ROCm, which only requires Gen3 slots. This forces me to switch back to amdgpu-pro for this machine.


---

### 评论 #7 — valeriob01 (2019-03-05T11:56:07Z)

> Whether or not PCI atomics work is a hardware issue, not a driver issue.

It has been clever to add the message "Device rejects atomics" at least we can do some minimal diagnostics.


---

### 评论 #8 — valeriob01 (2019-03-05T19:46:13Z)

> If your device rejects PCI atomics, then it is not supported on ROCm even in supported distributions. It is an unsupported hardware configuration (so my 4th guess in my post above).

The main-board is working perfectly with Ubuntu and amdgpu-pro.



---
