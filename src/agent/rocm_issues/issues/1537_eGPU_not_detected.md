# eGPU not detected

> **Issue #1537**
> **状态**: closed
> **创建时间**: 2021-07-30T12:18:30Z
> **更新时间**: 2021-07-31T09:10:09Z
> **关闭时间**: 2021-07-31T09:10:09Z
> **作者**: JeremieMary
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1537

## 描述

Hello, I have a Thinkpad X1 extreme and I want to accelerate pytorch thanks to a 6900XT enclosed in a Razer Core X eGPU box. 

I'm under Ubuntu 20.04 - fresh install-, the eGPU is detected and authorized by Ubuntu. The system works fine under windows. I followed to the letter the  install instructions of [the guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html) without any error message. 

Thought `/opt/rocm/bin/rocinfo` still claims that the ROCm Module is not loaded.

According to this repo: _Thunderbolt 1, 2, and 3 enabled breakout boxes should now be able to work with ROCm. Thunderbolt 1 and 2 are PCIe 2.0 based, and thus are only supported with GPUs that do not require PCIe 3.1.0 atomics (e.g. Vega 10). However, we have done no testing on this configuration and would need community support due to limited access to this type of equipment._

Is there something I can do to help there?

edit: 
```
jeremie@ThinkPad-X1:~$ lspci | grep -i thunder 
04:00.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 4C 2018] (rev 06)
05:00.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 4C 2018] (rev 06)
05:01.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 4C 2018] (rev 06)
05:02.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 4C 2018] (rev 06)
05:04.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 4C 2018] (rev 06)
06:00.0 System peripheral: Intel Corporation JHL7540 Thunderbolt 3 NHI [Titan Ridge 4C 2018] (rev 06)
07:00.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
08:01.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
3a:00.0 USB controller: Intel Corporation JHL7540 Thunderbolt 3 USB Controller [Titan Ridge 4C 2018] (rev 06)

jeremie@ThinkPad-X1:~/Desktop$ lspci | grep -i AMD 
09:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Upstream Port of PCI Express Switch (rev c0)
0a:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Downstream Port of PCI Express Switch
0b:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 73bf (rev c0)
0b:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device ab28
0b:00.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 73a6
0b:00.3 Serial bus controller [0c80]: Advanced Micro Devices, Inc. [AMD/ATI] Device 73a4
```


---

## 评论 (1 条)

### 评论 #1 — JeremieMary (2021-07-31T09:10:09Z)

The issue was that the driver is not signed so it is necessary to disable Secure Boot in the BIOS

---
