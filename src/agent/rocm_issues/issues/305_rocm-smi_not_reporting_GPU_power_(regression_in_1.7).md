# rocm-smi: not reporting GPU power (regression in 1.7)

> **Issue #305**
> **状态**: closed
> **创建时间**: 2018-01-21T12:02:48Z
> **更新时间**: 2018-06-03T15:30:51Z
> **关闭时间**: 2018-06-03T15:30:51Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/305

## 描述

With ROCm 1.7, Ubuntu 16.04.3, Vega64:

The rocm-smi that comes with 1.7 (located at /opt/rocm/bin/rocm-smi ) does not report GPU power when invoked with "rocm-smi -a". It says:
GPU[0] 		: Cannot get GPU power Consumption: Average GPU Power not supported

But, some old rocm-smi script (from 1.6 era) did detect and report correctly the power on "rocm-smi -a".

What's more, the new (1.7) rocm-smi does detect GPU power when invoked without arguments:
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  0   50.0c   8.0W     852Mhz   500Mhz   12.94%   auto      0%

So this seems to be a simple regression in the script itself.

---

## 评论 (4 条)

### 评论 #1 — kentrussell (2018-01-22T11:52:29Z)

Can you post the full output from the 1.7 script of rocm-smi -a ? Thanks!

---

### 评论 #2 — preda (2018-01-22T16:57:24Z)

[rocm-smi-1.7.txt](https://github.com/RadeonOpenCompute/ROCm/files/1652829/rocm-smi-1.7.txt)


---

### 评论 #3 — bananajamma (2018-05-12T19:12:03Z)

Same issue here with rocm 1.6 in the [AMD 18.10 unified drivers](https://support.amd.com/en-us/kb-articles/Pages/Radeon-Software-for-Linux-Release-Notes.aspx)

```
====================    ROCm System Management Interface    ====================
================================================================================
GPU[0]          : GPU ID: 0x687f
================================================================================
================================================================================
GPU[0]          : Temperature: 78.0c
================================================================================
================================================================================
GPU[0]          : GPU Clock Level: 7 (1590Mhz)
GPU[0]          : GPU Memory Clock Level: 3 (800Mhz)
================================================================================
================================================================================
GPU[0]          : Fan Level: 107 (41.96)%
================================================================================
================================================================================
GPU[0]          : Current PowerPlay Level: auto
================================================================================
================================================================================
GPU[0]          : Current OverDrive value: 0%
================================================================================
================================================================================
GPU[0]          : Minimum SCLK: 1538MHz
GPU[0]          : Minimum MCLK: 0MHz
GPU[0]          : Activity threshold: 0%
GPU[0]          : Hysteresis Up: 0ms
GPU[0]          : Hysteresis Down: 0ms
================================================================================
================================================================================
GPU[0]          : Cannot get GPU power Consumption: Average GPU Power not supported
================================================================================
================================================================================
GPU[0]          : Supported GPU clock frequencies on GPU0
GPU[0]          : 0: 852Mhz 
GPU[0]          : 1: 991Mhz 
GPU[0]          : 2: 1138Mhz 
GPU[0]          : 3: 1269Mhz 
GPU[0]          : 4: 1312Mhz 
GPU[0]          : 5: 1474Mhz 
GPU[0]          : 6: 1538Mhz 
GPU[0]          : 7: 1590Mhz *
GPU[0]          : 
GPU[0]          : Supported GPU Memory clock frequencies on GPU0
GPU[0]          : 0: 167Mhz 
GPU[0]          : 1: 500Mhz 
GPU[0]          : 2: 700Mhz 
GPU[0]          : 3: 800Mhz *
GPU[0]          : 
================================================================================
====================           End of ROCm SMI Log          ====================
```

---

### 评论 #4 — kentrussell (2018-05-14T13:19:38Z)

It was a known issue in previous releases due to some assumptions made regarding the DRM device enumeration. 1.8 has been released, can you try it there? The fix is in there and should address your concerns. If it still occurs, please paste the output of this command:
sudo cat /sys/kernel/debug/dri/0/amdgpu_pm_info
(If that fails, try dri/1 instead, depends on the enumeration of the DRM devices and if you have an on-board device or not)
See https://github.com/RadeonOpenCompute/ROC-smi/issues/16 for more

---
