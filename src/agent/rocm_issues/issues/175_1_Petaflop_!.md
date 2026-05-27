# 1 Petaflop !

> **Issue #175**
> **状态**: closed
> **创建时间**: 2017-08-02T01:44:47Z
> **更新时间**: 2017-08-23T03:53:05Z
> **关闭时间**: 2017-08-23T03:53:05Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/175

## 描述

http://wccftech.com/amd-manages-to-pack-a-1-petaflop-super-computer-in-a-rack-with-project-47/

---

## 评论 (7 条)

### 评论 #1 — gstoner (2017-08-02T03:19:37Z)

yep..  it was fun to work on 



---

### 评论 #2 — nevion (2017-08-02T03:35:08Z)

@gstoner any slides detailing system architecture and device/network topology?  Does the mellanox card have localized access to GPU memory?  Curious to see how you guys are trying to answer nvlink besides more pcie gen3 lines.

---

### 评论 #3 — gstoner (2017-08-02T03:58:55Z)

NVLINK  is great for P2P but HOST I/O performance you are blocked by the PLX switch.    4 GPU into 1 x16 is not idea state.    Also EPYC supports 256b packet on PCIe for P2P..  You have 128 lanes of PCIe exposed on an EPYC.    Rember you need to talk across PCIe to work with Mellonox NIC today. 

---

### 评论 #4 — nevion (2017-08-02T05:00:45Z)

Certainly, I'm looking at it in terms of P2P capabilities as well as host IO capabilities.  By system architecture, I mean something like [this](https://www.microway.com/wp-content/uploads/NumberSmasher_1U_Tesla_GPU_Server_with_NVLink_Block_Diagram.png)

~Is it an 8-GPU system with a mellanox card in there?   If so, Is there a single root complex in this system's architecture to multiplex host/device IO to the mellanox or something else?~ A diagram like that would be the best answer though.

Looks like 4 GPUs / system.  Did you guys choose to do anything with the remaining slots/pcie lanes?

---

### 评论 #5 — psteinb (2017-08-02T07:19:55Z)

30 GFlops/Watt?! is that number correct? What an achievement if so.

that would double the efficiency of the the top1 in the 
[green500.org](https://www.top500.org/green500/lists/2017/06/).


---

### 评论 #6 — oscarbg (2017-08-02T17:15:16Z)

"Also EPYC supports 256b packet on PCIe for P2P.."
so threadripper will also?

---

### 评论 #7 — gstoner (2017-08-02T17:24:08Z)

Yep….  You have to use SDMA transfer P2P.   The Root I/O Zen has some nice properties.  Also, GMI and xGMI does not block P2P transfers.   

EPYC ( 128 Lanes of PCIe)  and Threadripper ( 64 lanes of PCIe ) 





---
