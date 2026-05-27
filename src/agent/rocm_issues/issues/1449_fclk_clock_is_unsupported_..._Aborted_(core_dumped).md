# fclk clock is unsupported ... Aborted (core dumped)

> **Issue #1449**
> **状态**: closed
> **创建时间**: 2021-04-09T23:43:46Z
> **更新时间**: 2021-04-16T10:49:47Z
> **关闭时间**: 2021-04-14T05:53:06Z
> **作者**: perestoronin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1449

## 描述

```
rocm-smi -a
========================== Current clock frequencies ===========================
GPU[0]		: dcefclk clock level: 0: (600Mhz)
ERROR: GPU[0] 		: fclk clock is unsupported
GPU[0]		: mclk clock level: 0: (167Mhz)
GPU[0]		: sclk clock level: 0: (852Mhz)
GPU[0]		: socclk clock level: 0: (600Mhz)
python3: /var/tmp/portage/dev-libs/rocm-smi-lib-4.1.0/work/rocm_smi_lib-rocm-4.1.0/src/rocm_smi.cc:898: rsmi_status_t get_frequencies(amd::smi::DevInfoTypes, uint32_t, rsmi_frequencies_t*, uint32_t*): Assertion `f->current == RSMI_MAX_NUM_FREQUENCIES + 1' failed.
Aborted (core dumped)
```

same text error on other case: https://github.com/RadeonOpenCompute/rocm_smi_lib/issues/81

may be reason this case: pp_dpm_fclk interface is only available for Vega20 and later ASICs.

but I have case with this error on GPU Vega 10 Frontier Edition Air

---

## 评论 (12 条)

### 评论 #1 — perestoronin (2021-04-09T23:55:15Z)

uname -a
Linux rst 5.10.28-gentoo-rt36 #1 SMP PREEMPT_RT  

---

### 评论 #2 — ROCmSupport (2021-04-12T08:02:30Z)

Thanks @perestoronin for reaching out.
Can you please help me with few details like ROCm version, OS, /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-04-12T09:11:53Z)

I am not able to reproduce the issue locally with vega10 + ROCm 4.1

taccuser@taccuser-X399-DESIGNARE-EX:~$ /opt/rocm-4.1.0/bin/rocm-smi -a


======================= ROCm System Management Interface =======================
========================= Version of System Component ==========================
Driver version: 5.9.15
================================================================================
====================================== ID ======================================
GPU[0]          : GPU ID: 0x687f
================================================================================
================================== Unique ID ===================================
GPU[0]          : Unique ID: 0x21508ad07d44184
================================================================================
==================================== VBIOS =====================================
GPU[0]          : VBIOS version: 113-D0500100_104
================================================================================
================================= Temperature ==================================
GPU[0]          : Temperature (Sensor edge) (C): 40.0
GPU[0]          : Temperature (Sensor junction) (C): 41.0
GPU[0]          : Temperature (Sensor memory) (C): 41.0
================================================================================
========================== Current clock frequencies ===========================
GPU[0]          : dcefclk clock level: 0: (600Mhz)
ERROR: GPU[0]           : fclk clock is unsupported
GPU[0]          : mclk clock level: 2: (800Mhz)
GPU[0]          : sclk clock level: 3: (1138Mhz)
GPU[0]          : socclk clock level: 3: (847Mhz)
GPU[0]          : pcie clock level: 1 (8.0GT/s x16)
================================================================================
============================== Current Fan Metric ==============================
GPU[0]          : Fan Level: 73 (29%)
GPU[0]          : Fan RPM: 1024
================================================================================
============================ Show Performance Level ============================
GPU[0]          : Performance Level: auto
================================================================================
=============================== OverDrive Level ================================
GPU[0]          : GPU OverDrive value (%): 0
================================================================================
=============================== OverDrive Level ================================
GPU[0]          : GPU Memory OverDrive value (%): 0
================================================================================
================================== Power Cap ===================================
GPU[0]          : Max Graphics Package Power (W): 260.0
================================================================================
============================= Show Power Profiles ==============================
GPU[0]          : 1. Available power profile (#1 of 7): CUSTOM
GPU[0]          : 2. Available power profile (#2 of 7): VIDEO
GPU[0]          : 3. Available power profile (#3 of 7): POWER SAVING
GPU[0]          : 4. Available power profile (#4 of 7): COMPUTE
GPU[0]          : 5. Available power profile (#5 of 7): VR
GPU[0]          : 6. Available power profile (#6 of 7): 3D FULL SCREEN
GPU[0]          : 7. Available power profile (#7 of 7): BOOTUP DEFAULT*
================================================================================
============================== Power Consumption ===============================
GPU[0]          : Average Graphics Package Power (W): 16.0
================================================================================
========================= Supported clock frequencies ==========================
GPU[0]          : Supported dcefclk frequencies on GPU0
GPU[0]          : 0: 600Mhz *
GPU[0]          : 1: 720Mhz
GPU[0]          : 2: 800Mhz
GPU[0]          : 3: 847Mhz
GPU[0]          : 4: 900Mhz
GPU[0]          :
ERROR: GPU[0]           : fclk frequency is unsupported
GPU[0]          :
GPU[0]          : Supported mclk frequencies on GPU0
GPU[0]          : 0: 167Mhz
GPU[0]          : 1: 500Mhz
GPU[0]          : 2: 800Mhz *
GPU[0]          : 3: 945Mhz
GPU[0]          :
GPU[0]          : Supported sclk frequencies on GPU0
GPU[0]          : 0: 852Mhz
GPU[0]          : 1: 991Mhz
GPU[0]          : 2: 1084Mhz
GPU[0]          : 3: 1138Mhz *
GPU[0]          : 4: 1200Mhz
GPU[0]          : 5: 1401Mhz
GPU[0]          : 6: 1536Mhz
GPU[0]          : 7: 1630Mhz
GPU[0]          :
GPU[0]          : Supported socclk frequencies on GPU0
GPU[0]          : 0: 600Mhz
GPU[0]          : 1: 720Mhz
GPU[0]          : 2: 800Mhz
GPU[0]          : 3: 847Mhz *
GPU[0]          : 4: 900Mhz
GPU[0]          : 5: 960Mhz
GPU[0]          : 6: 1028Mhz
GPU[0]          : 7: 1107Mhz
GPU[0]          :
GPU[0]          : Supported PCIe frequencies on GPU0
GPU[0]          : 0: 8.0GT/s x16
GPU[0]          : 1: 8.0GT/s x16 *
GPU[0]          :
--------------------------------------------------------------------------------
================================================================================
============================== % time GPU is busy ==============================
GPU[0]          : GPU use (%): 0
================================================================================
============================== Current Memory Use ==============================
ERROR: 2 GPU[0]: % memory use: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
================================================================================
================================ Memory Vendor =================================
GPU[0]          : GPU memory vendor: samsung
================================================================================
============================= PCIe Replay Counter ==============================
GPU[0]          : PCIe Replay Count: 0
================================================================================
================================ Serial Number =================================
GPU[0]          : Serial Number: N/A
================================================================================
================================ KFD Processes =================================
No KFD PIDs currently running
================================================================================
============================= GPUs Indexed by PID ==============================
No KFD PIDs currently running
================================================================================
================== GPU Memory clock frequencies and voltages ===================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
================================================================================
=============================== Current voltage ================================
GPU[0]          : Voltage (mV): 825
================================================================================
================================== PCI Bus ID ==================================
GPU[0]          : PCI Bus: 0000:43:00.0
================================================================================
============================= Firmware Information =============================
GPU[0]          : ASD firmware version:         553648198
GPU[0]          : CE firmware version:          79
GPU[0]          : DMCU firmware version:        0
GPU[0]          : MC firmware version:          0
GPU[0]          : ME firmware version:          164
GPU[0]          : MEC firmware version:         33216
GPU[0]          : MEC2 firmware version:        33216
GPU[0]          : PFP firmware version:         188
GPU[0]          : RLC firmware version:         96
GPU[0]          : RLC SRLC firmware version:    0
GPU[0]          : RLC SRLG firmware version:    0
GPU[0]          : RLC SRLS firmware version:    0
GPU[0]          : SDMA firmware version:        432
GPU[0]          : SDMA2 firmware version:       432
GPU[0]          : SMC firmware version:         05.28.19.00
GPU[0]          : SOS firmware version:         0x0008025d
GPU[0]          : TA RAS firmware version:      00.00.00.00
GPU[0]          : TA XGMI firmware version:     00.00.00.00
GPU[0]          : UVD firmware version:         0x422b1100
GPU[0]          : VCE firmware version:         0x39060400
GPU[0]          : VCN firmware version:         0x00000000
================================================================================
================================= Product Info =================================
GPU[0]          : Card model:           0x2387
GPU[0]          : Card vendor:          Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]          : Card SKU:             D05001
================================================================================
================================== Pages Info ==================================
ERROR: 2 GPU[0]: ras: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
============================ Show Valid sclk Range =============================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
GPU[0]          : Unable to display sclk range
================================================================================
============================ Show Valid mclk Range =============================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
GPU[0]          : Unable to display mclk range
================================================================================
=========================== Show Valid voltage Range ===========================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
GPU[0]          : Unable to display voltage range
================================================================================
============================= Voltage Curve Points =============================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
GPU[0]          : Voltage Curve is not supported
================================================================================
WARNING:                 One or more commands failed
============================= End of ROCm SMI Log ==============================


---

### 评论 #4 — perestoronin (2021-04-13T02:35:51Z)

Rocm-smi (deprecated) 4.0 work excellent with rocm stack 4.1
Thank you, i will retry with rocm-smi 4.1, may by my troubles in ld.so.conf.d for rsmi libs...

---

### 评论 #5 — perestoronin (2021-04-13T19:26:42Z)

@ROCmSupport  I added more logs
deprecated old rocm-smi work without errors and asserts
/opt/rocm/bin/rocm-smi -a
https://gist.github.com/raw/136a1fdb2bee8bec1ea5fe8de76dbadf

but new rocm-smi raised assert and output errors
rocm-smi -a
https://gist.github.com/raw/7e21367dd82557c343f4601ed8049334

In my case error in this results:
```
i=0
f->frequency[i]=2500000000
f->current=33
RSMI_MAX_NUM_FREQUENCIES=32
current=1
i=1
f->frequency[i]=2500000000
f->current=0
RSMI_MAX_NUM_FREQUENCIES=32
current=1
python3: /var/tmp/portage/dev-libs/rocm-smi-lib-4.1.0/work/rocm_smi_lib-rocm-4.1.0/src/rocm_smi.cc:905: rsmi_status_t get_frequencies(amd::smi::DevInfoTypes, uint32_t, rsmi_frequencies_t*, uint32_t*): Assertion `f->current == RSMI_MAX_NUM_FREQUENCIES + 1' failed.
```


---

### 评论 #6 — perestoronin (2021-04-13T20:07:27Z)

error on type 13 = kDevPCIEClk

---

### 评论 #7 — perestoronin (2021-04-13T20:28:37Z)

On these data new rocm-smi failed:
```
/sys/class/drm/card0/device # cat pp_dpm_pcie 
0: 2.5GT/s, x16 *
1: 2.5GT/s, x16 *
```

---

### 评论 #8 — perestoronin (2021-04-13T20:31:09Z)

error in driver amdgpu, but rocm-smi as I expected 
1. not must asserted on this illegal data from driver
2. not nessary type ERROR on non exists for card new types of fclk and so on.

 

---

### 评论 #9 — perestoronin (2021-04-14T04:58:50Z)

about logick in rocm-kernel-driver and logick in kernel drivers 5.10 https://i.imgur.com/yMiQxZi.png

---

### 评论 #10 — perestoronin (2021-04-14T05:18:15Z)

this new commit to new kernel linux will raise failed to work rocm-smi  http://git.yoctoproject.org/cgit/cgit.cgi/linux-yocto-dev/commit/?id=040afa09ef066fa9b525b790f05ae03022ed7954 https://cdn.kernel.org/pub/linux/kernel/v5.x/patch-5.10.27.xz after removing logic based on PPSMC_MSG_GetCurrentLinkIndex

@ROCmSupport  Please sync with kernel command to fix this.

---

### 评论 #11 — perestoronin (2021-04-14T05:52:57Z)

solution to new kernel mainline driver  vega10_hwmgr.c.patch  https://gist.github.com/raw/32685450353b72f99ec11acba4e6b9bc

---

### 评论 #12 — ROCmSupport (2021-04-16T10:49:47Z)

Hi @perestoronin 
Request to open a new task for the latest issue as a separate ticket so that I will work with kernel team for the fixes.
Thank you.

---
