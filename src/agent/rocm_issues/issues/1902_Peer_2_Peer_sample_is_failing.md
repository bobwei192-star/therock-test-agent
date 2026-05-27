# Peer 2 Peer sample is failing

> **Issue #1902**
> **状态**: closed
> **创建时间**: 2023-02-07T20:25:52Z
> **更新时间**: 2024-02-03T23:00:29Z
> **关闭时间**: 2024-02-03T23:00:28Z
> **作者**: ramin-raeisi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1902

## 描述

Peer to peer sample from HIP's git repository(https://github.com/ROCm-Developer-Tools/HIP/tree/develop/samples/2_Cookbook/8_peer2peer) is failing on my server with this log: [Peer2PeerLog.txt](https://github.com/RadeonOpenCompute/ROCm/files/10680119/Peer2PeerLog.txt).

**My Server Specification:**
- [Motherboard](https://www.supermicro.com/en/products/motherboard/X12DPG-OA6)
- [Cpu](https://ark.intel.com/content/www/us/en/ark/products/215277/intel-xeon-silver-4310-processor-18m-cache-2-10-ghz.html)
- 10 x Instinct MI50 GPUs
- PCI Peer-to-Peer enabled in BIOS
- IOMMU disabled, in BIOS and grub

**Here is a little background on how I reached this point:**

I stumbled upon the `Memory access fault by GPU node-1 on address "(nil)." Reason: Page not present or supervisor privilege` error while executing the training sample code of [PaLM-RLHF-Pytorch](https://github.com/lucidrains/PaLM-rlhf-pytorch) and that led me to [https://github.com/RadeonOpenCompute/ROCm/issues/1339](https://github.com/RadeonOpenCompute/ROCm/issues/1339#issuecomment-756090300) which eventually convinced me to run the peer to peer sample.

Here is the output of dmesg, I can see page faults, [dmesg output.txt](https://github.com/RadeonOpenCompute/ROCm/files/10685859/dmesg.output.txt).



My thoughts are going towards the driver which might be the issue, but I am not sure. I have ROCm 5.4.1 installed with all usecases.

I do appreciate if you could help me on this.

---

## 评论 (4 条)

### 评论 #1 — IMbackK (2023-10-21T12:31:33Z)

I can confirm that this issue still exists as of rocm 5.7 and that it is specific to gfx906. gfx900, gfx908, gfx1030 are unaffected

---

### 评论 #2 — nartmada (2024-02-02T23:03:57Z)

Hi @ramin-raeisi, please check latest ROCm6.0.2 to see if your issue has been fixed.  If fixed, please close the ticket.  Thanks.

---

### 评论 #3 — IMbackK (2024-02-03T11:18:25Z)

the issue appears fixed by updated kernel not rocm but yes, fixed

---

### 评论 #4 — nartmada (2024-02-03T23:00:28Z)

Closing the ticket as issue is fixed.

---
