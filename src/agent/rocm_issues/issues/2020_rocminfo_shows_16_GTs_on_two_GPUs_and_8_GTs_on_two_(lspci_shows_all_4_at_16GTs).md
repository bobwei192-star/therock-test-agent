# rocminfo shows 16 GT/s on two GPUs and 8 GT/s on two (lspci shows all 4 at 16GT/s)

> **Issue #2020**
> **状态**: closed
> **创建时间**: 2023-04-05T19:06:07Z
> **更新时间**: 2024-06-19T20:23:13Z
> **关闭时间**: 2024-06-19T20:23:12Z
> **作者**: jordan44665
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2020

## 描述

I am seeing something weird. I have 4 Radeon PRO W6800 cards and when I install two of them, I get 16 GT/s (see 2gpu-lspci.txt and 2gpu-rocmsmi.txt) but when I install all 4 of them then lspci gives me the "correct" transfer rates (16 GT/s) but rocminfo says only 2 of them have 16 GT/s and the other 2 have 8 GT/s. 

I wonder if this causes some issues with the driver being able to transfer data from host to GPUs and back? My program (I am doing a long running ML training session) crashes after 12 hours. 

[2gpu-rocmsmi.txt](https://github.com/RadeonOpenCompute/ROCm/files/11162222/2gpu-rocmsmi.txt)
[2gpu-lspci.txt](https://github.com/RadeonOpenCompute/ROCm/files/11162223/2gpu-lspci.txt)
[4gpu-lspci.txt](https://github.com/RadeonOpenCompute/ROCm/files/11162224/4gpu-lspci.txt)
[4gpu-rocmsmi.txt](https://github.com/RadeonOpenCompute/ROCm/files/11162225/4gpu-rocmsmi.txt)


---

## 评论 (3 条)

### 评论 #1 — preda (2023-04-11T06:36:29Z)

Most likely the difference between the 2-GPU and the 4-GPU situation results from the motherboard/CPU negociating different PCIe capabilities as the number of PCIe devices changes.

I suspect what you see in the lspci reflects the "capability" of the GPU (as all of them are capable of 16x Gen-4), while what you see in rocmsmi is the effective width and speed as negociated with the motherboard/CPU.

You may find more information in the motherboard manual, where usually there is a section about the number and speed of PCIe slots on the MB, and how that relates to the number of PCIe lanes of the CPU.

Anyway, the GPUs do run perfectly fine at either PCIe speed and PCIe width. The difference you see in PCIe config is not the reason for the crash.

(for the crash, do you see any relevant information in dmesg?  -- that's where the driver might log something)


---

### 评论 #2 — ppanchad-amd (2024-05-10T18:37:17Z)

@jordan44665 Has your issue been resolved? If so, please close the ticket. Thanks!

---

### 评论 #3 — harkgill-amd (2024-06-19T20:23:12Z)

Hi @jordan44665, as mentioned in the comment above, lspci will output the maximum data transfer rate of the PCIe link whereas rocmsmi reports the current transfer rate of the PCIe link. The link can downshift to a lower speed when the full bandwidth is not required, which can result in rocmsmi reporting a lower transfer rate than lspci. If you are still experiencing the crash with ROCm 6.1.2, please re-open this ticket. Thanks!

---
