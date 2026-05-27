# Vega 56 strange behaviour with OpenCL

> **Issue #689**
> **状态**: closed
> **创建时间**: 2019-01-25T23:18:30Z
> **更新时间**: 2019-02-18T21:58:08Z
> **关闭时间**: 2019-02-18T21:58:08Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/689

## 描述

Hi ROCm team
My newly installed RX Vega 56 shows quite a strange behaviour when I run OpenCL apps on it:

- nothing is executed, but no errors appear anyway
I run a short benchmark with some crypto mining software.
The GPU is recognized and the OpenCL compute kernel is compiled for the Vega.
According to the app, the compute kernel is loaded properly and the benchmark starts.
In the end, the benchmark results are zero however (see [benchmark.txt](https://github.com/RadeonOpenCompute/ROCm/files/2798246/benchmark.txt)).

- in the same time, the GPU does not change any clocks nor voltages and shows GPU% as 0%
As rocm-smi shows, no values have changed since starting the benchmark.
It also shows 9W average power consumption... (see [rocm-smi.txt](https://github.com/RadeonOpenCompute/ROCm/files/2798226/rocm-smi.txt))

- after a reset, the Vega suddenly is heating up
When I reset the GPU via ```sudo cat /sys/kernel/debug/dri/1/amdgpu_gpu_recover```,
it still does nothing, but it suddenly starts heating up (see [rocm-smi_temperature.txt](https://github.com/RadeonOpenCompute/ROCm/files/2798224/rocm-smi_temperature.txt)).
I did the reset minutes after the benchmark has finished.

The GPU is initialized properly, appears in [clinfo](https://github.com/RadeonOpenCompute/ROCm/files/2798228/clinfo.txt)/[rocminfo](https://github.com/RadeonOpenCompute/ROCm/files/2798227/rocminfo.txt) and can be controlled via rocm-smi.
Even setting memoryoverdrive to 10% works.
But as I said, it does nothing but heating up when I want to run OpenCL apps on it.

I tested this GPU in a testing machine at home, with a simple board and an old i5 560 on it.
It worked perfectly with ROCm 2.0, so I decided to place it in my production machine.
Only there it behaves like this.

One thing to mention:
The board has an enabled onboard GPU (AST2300), which I use to configure the machine.
It also appears on the syslog at boot (see [bootlog.txt](https://github.com/RadeonOpenCompute/ROCm/files/2798229/bootlog.txt)).
This exact setup worked fine with two R9 390 before, together with ROCm 1.9 (until 2.0 came out which broke the Hawaii setup #668 )

Do you have any idea where this could come from?
Please let me know, if you need more information.

EDIT: I also tried to do a rollback to ROCm 1.9.2 via ROCM_Experimental, but the Vega behaved the same.

---

## 评论 (1 条)

### 评论 #1 — ghost (2019-02-18T21:58:08Z)

Everything works fine with amdgpu-pro 18.50 and the additional package libdrm-amdgpu1, installed via
```
sudo apt install libdrm-amdgpu1
```
I have no idea, why this package is necessary though...

Anyway, it works now.

Thank you

---
