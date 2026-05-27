# Voltage in PowerTable not being respected - Vega 64 FF - ROCm 3.0

> **Issue #1015**
> **状态**: closed
> **创建时间**: 2020-02-20T11:04:57Z
> **更新时间**: 2020-02-21T09:24:27Z
> **关闭时间**: 2020-02-20T14:13:02Z
> **作者**: theRTLmaker
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1015

## 描述

I'm trying to characterize how does the GPU power and performance changes in undervoltage scenarios, but when I change the voltage in the PowerTables and select the desired performance level for the GPU Core, the voltage is the same as for the default settings.

I'm running **CentOS 7.5** with **ROCm 3.0**.

I've followed the instalation instructions from [git/ROCm](https://github.com/RadeonOpenCompute/ROCm#CentOS-RHEL) and [issue](https://github.com/RadeonOpenCompute/ROCm/issues/463) (with the necessary changes for CentOS not ubunto) and configured the PowerTables accordingly with [issue](https://github.com/RadeonOpenCompute/ROCm/issues/463#issuecomment-450698247)

I've written a script that performs this procedure:
1. scl enable devtoolset-7 bash
2. rocm-smi -r
3. rocm-smi --setfan 255
4. rocm-smi --setperflevel manual
5. rocm-smi --setslevel <level> <frequency> <voltage> with the following values
Level | Freq | Volt
0  852    810
1  991    822
2  1138  834
3  1269  846
4  1348  858
5  1440  860
6  1528  872
7  1600  1000
6. rocm-smi --setsclk 7 
7. rocm-smi --showvoltage

What I see is that independently of the voltage that I select for the level 7, the output of --showvoltage is always
```
========================ROCm System Management Interface========================
================================================================================
GPU[1]          : Voltage (mV): 1187
================================================================================
==============================End of ROCm SMI Log ==============================

```
What can I be doing wrong?


---

## 评论 (2 条)

### 评论 #1 — nikAizuddin (2020-02-20T16:46:05Z)

@TheEmbbededCoder Hi, did you solved the problem?

---

### 评论 #2 — theRTLmaker (2020-02-21T09:24:27Z)

> @TheEmbbededCoder Hi, did you solved the problem?

I just noticed that if I'm using the default frequency (in this case 1600 MHz for the level 7), the voltage does not respect what I wrote for that level, the GPU uses the default 1200 mV. However, If I put any other frequency (for example 1601 MHz or 1599 Mhz), the voltage that I write to that level starts to be respected by the GPU. 
I don't understand this behaviour, I don't see it written anywhere...

Do you have any idea why is this the case?

---
