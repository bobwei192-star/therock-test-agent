# ROCm programs hangs with Vega 20 (MI 50)

> **Issue #1386**
> **状态**: closed
> **创建时间**: 2021-02-19T15:00:45Z
> **更新时间**: 2021-03-11T19:59:37Z
> **关闭时间**: 2021-03-01T06:05:29Z
> **作者**: arfio
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1386

## 描述

Hi,

I have recently installed ROCm v4.0.0 on a server running 2 Vega 20 GPUs (MI 50).

The clinfo command locks up like the issues #484 #1326. The difference is I have to force the restart of the server to have access to the agents after the program locks. The bug.tar.gz locks also and the output is in the output.txt file. I thought it was only with OpenCL programs but it happens also with Tensorflow scripts.

The two GPUs are not connected with XGMi. The motherboard uses the latest BIOS available. The issue happened with Ubuntu 18.04 (Linux kernel 4.15) and 20.04 (Linux kernel 5.4.0-65).

[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6010742/rocminfo.txt)
[bug.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/6010743/bug.tar.gz)
[output.txt](https://github.com/RadeonOpenCompute/ROCm/files/6010744/output.txt)
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6010745/clinfo.txt)
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/6010746/dmesg.txt)


---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-02-22T06:16:12Z)

Thanks @arfio for reaching us.

From the dmesg, looks like severe hardware error observed. Might be hardware problem.
_[ 1358.996458] amdgpu 0000:83:00.0: uncorrectable hardware error(ERREVENT_ATHUB_INTERRUPT) detected!_

I will get more information for you.
Thank you.

---

### 评论 #2 — kentrussell (2021-02-23T15:34:06Z)

I wonder if there might be a hardware failure in there. The dmesg shows that the HW is hanging during GPU reset, the SMU can't be stopped successfully, PowerPlay IP block can't be shut down cleanly, and then getting things restarted again just craps out. Is this isolated to one of the GPUs, or can it be seen on both? And how consistent is it? 
Normally, a UE (Uncorrectable Error) is not going to take the whole thing down, but it is possible in some extreme cases. First, I'd suggest trying to reproduce it with a single GPU in there. If you can reproduce it, swap the GPU and try again. If it only happens on one, it's more likely to be a HW failure, but if it's occurring on both, then there's some deeper digging required. Thanks!

---

### 评论 #3 — ROCmSupport (2021-02-26T05:02:15Z)

Hi @arfio 
Most likely its an hardware issue.
As suggested by Kent, recommend to try plugging one card every time and share an update.
Thank you.

---

### 评论 #4 — arfio (2021-02-27T02:50:45Z)

Hi @ROCmSupport @kentrussell 
After verification by running a sample program on each GPU, we identified that one of the GPU installed was not working correctly, so we will remove and replace the board.
Thank you for your time.

---

### 评论 #5 — ROCmSupport (2021-03-01T06:05:29Z)

Thank you very much @arfio 
I am closing it now then.

---

### 评论 #6 — arfio (2021-03-11T15:08:45Z)

Hi @ROCmSupport 

Previously I thought that it was a hardware issue, but I tested each GPU separately, and they all work. We have the latest BIOS update, latest ROCm installation. We have also tested different slots, but they are all working correctly when we only have one GPU.

We keep having the same issue with two different servers in the same configuration. Here is the dmidecode output if it can help.

Thank you.
[dmidecode.txt](https://github.com/RadeonOpenCompute/ROCm/files/6125667/dmidecode.txt)


---
