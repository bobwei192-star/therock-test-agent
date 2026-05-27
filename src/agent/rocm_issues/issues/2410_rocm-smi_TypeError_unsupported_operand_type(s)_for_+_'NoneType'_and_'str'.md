# rocm-smi TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

> **Issue #2410**
> **状态**: closed
> **创建时间**: 2023-08-28T15:01:02Z
> **更新时间**: 2024-03-22T23:25:32Z
> **关闭时间**: 2024-03-22T23:25:32Z
> **作者**: grigio
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2410

## 描述

I'm using your dev rocm container with `ubuntu:22:04`

```
rocm-smi -a


========================= ROCm System Management Interface =========================
=========================== Version of System Component ============================
Driver version: 6.1.5
====================================================================================
======================================== ID ========================================
GPU[0]		: GPU ID: 0x164e
====================================================================================
==================================== Unique ID =====================================
GPU[0]		: Unique ID: N/A
====================================================================================
====================================== VBIOS =======================================
GPU[0]		: VBIOS version: 102-RAPHAEL-008
====================================================================================
=================================== Temperature ====================================
GPU[0]		: Temperature (Sensor edge) (C): 47.0
====================================================================================
============================ Current clock frequencies =============================
GPU[0]		: mclk clock level: 0: (2600Mhz)
GPU[0]		: sclk clock level: 1: (600Mhz)
GPU[0]		: socclk clock level: 1: (1200Mhz)
====================================================================================
================================ Current Fan Metric ================================
GPU[0]		: Unable to detect fan speed for GPU 0
====================================================================================
============================== Show Performance Level ==============================
GPU[0]		: Performance Level: auto
====================================================================================
================================= OverDrive Level ==================================
GPU[0]		: GPU OverDrive value (%): 0
====================================================================================
================================= OverDrive Level ==================================
GPU[0]		: GPU Memory OverDrive value (%): 0
====================================================================================
==================================== Power Cap =====================================
GPU[0]		: get_power_cap, Not supported on the given system
GPU[0]		: Max Graphics Package Power Unsupported
====================================================================================
=============================== Show Power Profiles ================================
GPU[0]		: get_power_profiles, Not supported on the given system
====================================================================================
================================ Power Consumption =================================
Traceback (most recent call last):
  File "/usr/bin/rocm-smi", line 3586, in <module>
    showPower(deviceList)
  File "/usr/bin/rocm-smi", line 2190, in showPower
    if checkIfSecondaryDie(device):
  File "/usr/bin/rocm-smi", line 715, in checkIfSecondaryDie
    if not (rsmi_ret_ok(ret, None, None, False) and power_cap.value == 0):
  File "/usr/bin/rocm-smi", line 3227, in rsmi_ret_ok
    printLog(device, metric + ", " + rsmi_status_verbose_err_out[my_ret], None)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

```

```
rocm_agent_enumerator -a
gfx000
gfx1036

```
