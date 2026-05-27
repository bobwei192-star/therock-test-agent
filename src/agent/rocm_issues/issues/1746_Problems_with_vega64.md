# Problems with vega64

> **Issue #1746**
> **状态**: closed
> **创建时间**: 2022-05-30T16:22:53Z
> **更新时间**: 2023-12-27T17:55:17Z
> **关闭时间**: 2023-12-27T17:55:17Z
> **作者**: sinix-del
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1746

## 描述

Hello, a install ROCM 4.5.2 on 20.04, when i add second GPU i have a problem because they dont read fan on that card. Can you help and point me somewhere, and what to look. Both cards are the same.

Here is the rocm-smi
> ======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK    MCLK     Fan    Perf    PwrCap  VRAM%  GPU%
0    57.0c  119.0W  900Mhz  1050Mhz  0%     manual  264.0W   83%   100%
1    56.0c  130.0W  900Mhz  1050Mhz  80.0%  manual  264.0W   83%   100%
================================================================================
============================= End of ROCm SMI Log ==============================

and rocm-smi -a

> 

======================= ROCm System Management Interface =======================
========================= Version of System Component ==========================
Driver version: 5.11.32.21.40
================================================================================
====================================== ID ======================================
GPU[0]		: GPU ID: 0x687f

GPU[1]		: GPU ID: 0x687f

================================================================================
================================== Unique ID ===================================
GPU[0]		: Unique ID: 0x215084616963084

GPU[1]		: Unique ID: 0x2150654c1aa5144

================================================================================
==================================== VBIOS =====================================
GPU[0]		: VBIOS version: 113-D0500100-O08

GPU[1]		: VBIOS version: 113-D0500100-O08

================================================================================
================================= Temperature ==================================
GPU[0]		: Temperature (Sensor edge) (C): 58.0

GPU[0]		: Temperature (Sensor junction) (C): 63.0

GPU[0]		: Temperature (Sensor memory) (C): 79.0

GPU[0]		: Temperature (Sensor HBM 0) (C): N/A

GPU[0]		: Temperature (Sensor HBM 1) (C): N/A

GPU[0]		: Temperature (Sensor HBM 2) (C): N/A

GPU[0]		: Temperature (Sensor HBM 3) (C): N/A

GPU[1]		: Temperature (Sensor edge) (C): 57.0

GPU[1]		: Temperature (Sensor junction) (C): 69.0

GPU[1]		: Temperature (Sensor memory) (C): 90.0

GPU[1]		: Temperature (Sensor HBM 0) (C): N/A

GPU[1]		: Temperature (Sensor HBM 1) (C): N/A

GPU[1]		: Temperature (Sensor HBM 2) (C): N/A

GPU[1]		: Temperature (Sensor HBM 3) (C): N/A

================================================================================
========================== Current clock frequencies ===========================
GPU[0]		: pcie clock level: 1 (5.0GT/s x1)

GPU[1]		: dcefclk clock level: 0: (600Mhz)

GPU[1]		: mclk clock level: 3: (1050Mhz)

GPU[1]		: sclk clock level: 7: (900Mhz)

GPU[1]		: socclk clock level: 7: (1107Mhz)

GPU[1]		: pcie clock level: 1 (5.0GT/s x1)

================================================================================
============================== Current Fan Metric ==============================
GPU[0]		: Unable to detect fan speed for GPU 0

GPU[1]		: Fan Level: 204 (80%)

GPU[1]		: Fan RPM: 2645

================================================================================
============================ Show Performance Level ============================
GPU[0]		: Performance Level: manual

GPU[1]		: Performance Level: manual

================================================================================
=============================== OverDrive Level ================================
GPU[0]		: GPU OverDrive value (%): 0

GPU[1]		: GPU OverDrive value (%): 0

================================================================================
=============================== OverDrive Level ================================
================================== Power Cap ===================================
GPU[0]		: Max Graphics Package Power (W): 264.0

GPU[1]		: Max Graphics Package Power (W): 264.0

================================================================================
============================= Show Power Profiles ==============================
GPU[0]		: 1. Available power profile (#1 of 7): CUSTOM

GPU[0]		: 2. Available power profile (#2 of 7): VIDEO

GPU[0]		: 3. Available power profile (#3 of 7): POWER SAVING

GPU[0]		: 4. Available power profile (#4 of 7): COMPUTE*

GPU[0]		: 5. Available power profile (#5 of 7): VR

GPU[0]		: 6. Available power profile (#6 of 7): 3D FULL SCREEN

GPU[0]		: 7. Available power profile (#7 of 7): BOOTUP DEFAULT

GPU[1]		: 1. Available power profile (#1 of 7): CUSTOM

GPU[1]		: 2. Available power profile (#2 of 7): VIDEO

GPU[1]		: 3. Available power profile (#3 of 7): POWER SAVING

GPU[1]		: 4. Available power profile (#4 of 7): COMPUTE*

GPU[1]		: 5. Available power profile (#5 of 7): VR

GPU[1]		: 6. Available power profile (#6 of 7): 3D FULL SCREEN

GPU[1]		: 7. Available power profile (#7 of 7): BOOTUP DEFAULT

================================================================================
============================== Power Consumption ===============================
GPU[0]		: Average Graphics Package Power (W): 119.0

GPU[1]		: Average Graphics Package Power (W): 129.0

================================================================================
========================= Supported clock frequencies ==========================
GPU[0]		: Supported PCIe frequencies on GPU0

GPU[0]		: 0: 5.0GT/s x1

GPU[0]		: 1: 5.0GT/s x1 *

GPU[0]		: 

--------------------------------------------------------------------------------
GPU[1]		: Supported dcefclk frequencies on GPU1

GPU[1]		: 0: 600Mhz *

GPU[1]		: 1: 720Mhz

GPU[1]		: 2: 800Mhz

GPU[1]		: 3: 847Mhz

GPU[1]		: 4: 900Mhz

GPU[1]		: 

GPU[1]		: Supported mclk frequencies on GPU1

GPU[1]		: 0: 167Mhz

GPU[1]		: 1: 500Mhz

GPU[1]		: 2: 850Mhz

GPU[1]		: 3: 1050Mhz *

GPU[1]		: 

GPU[1]		: Supported sclk frequencies on GPU1

GPU[1]		: 0: 852Mhz

GPU[1]		: 1: 1175Mhz

GPU[1]		: 2: 1105Mhz

GPU[1]		: 3: 1110Mhz

GPU[1]		: 4: 1115Mhz

GPU[1]		: 5: 1120Mhz

GPU[1]		: 6: 1125Mhz

GPU[1]		: 7: 900Mhz *

GPU[1]		: 

GPU[1]		: Supported socclk frequencies on GPU1

GPU[1]		: 0: 600Mhz

GPU[1]		: 1: 720Mhz

GPU[1]		: 2: 800Mhz

GPU[1]		: 3: 847Mhz

GPU[1]		: 4: 900Mhz

GPU[1]		: 5: 960Mhz

GPU[1]		: 6: 1028Mhz

GPU[1]		: 7: 1107Mhz *

GPU[1]		: 

GPU[1]		: Supported PCIe frequencies on GPU1

GPU[1]		: 0: 5.0GT/s x1

GPU[1]		: 1: 5.0GT/s x1 *

GPU[1]		: 

--------------------------------------------------------------------------------
================================================================================
============================== % time GPU is busy ==============================
GPU[0]		: GPU use (%): 100

GPU[1]		: GPU use (%): 100

================================================================================
============================== Current Memory Use ==============================
================================================================================
================================ Memory Vendor =================================
GPU[0]		: GPU memory vendor: samsung

GPU[1]		: GPU memory vendor: samsung

================================================================================
============================= PCIe Replay Counter ==============================
GPU[0]		: PCIe Replay Count: 0

GPU[1]		: PCIe Replay Count: 0

================================================================================
================================ Serial Number =================================
GPU[0]		: Serial Number: N/A

GPU[1]		: Serial Number: N/A

================================================================================
================================ KFD Processes =================================
KFD process information:

PID 	PROCESS NAME	GPU(s)	VRAM USED  	SDMA USED	CU OCCUPANCY	

1319	teamredminer	2     	14147411968	0        	20          	

================================================================================
============================= GPUs Indexed by PID ==============================
PID 1319 is using 2 DRM device(s):
0 1 
================================================================================
================== GPU Memory clock frequencies and voltages ===================
================================================================================
=============================== Current voltage ================================
GPU[0]		: Voltage (mV): 900

GPU[1]		: Voltage (mV): 900

================================================================================
================================== PCI Bus ID ==================================
GPU[0]		: PCI Bus: 0000:04:00.0

GPU[1]		: PCI Bus: 0000:07:00.0

================================================================================
============================= Firmware Information =============================
GPU[0]		: ASD firmware version: 	553648226

GPU[0]		: CE firmware version: 		79

GPU[0]		: DMCU firmware version: 	0

GPU[0]		: MC firmware version: 		0

GPU[0]		: ME firmware version: 		166

GPU[0]		: MEC firmware version: 	33230

GPU[0]		: MEC2 firmware version: 	33230

GPU[0]		: PFP firmware version: 	191

GPU[0]		: RLC firmware version: 	96

GPU[0]		: RLC SRLC firmware version: 	0

GPU[0]		: RLC SRLG firmware version: 	0

GPU[0]		: RLC SRLS firmware version: 	0

GPU[0]		: SDMA firmware version: 	434

GPU[0]		: SDMA2 firmware version: 	434

GPU[0]		: SMC firmware version: 	05.28.19.00

GPU[0]		: SOS firmware version: 	0x0008025d

GPU[0]		: TA RAS firmware version: 	00.00.00.00

GPU[0]		: TA XGMI firmware version: 	00.00.00.00

GPU[0]		: UVD firmware version: 	0x422b1100

GPU[0]		: VCE firmware version: 	0x39060400

GPU[0]		: VCN firmware version: 	0x00000000

GPU[1]		: ASD firmware version: 	553648226

GPU[1]		: CE firmware version: 		79

GPU[1]		: DMCU firmware version: 	0

GPU[1]		: MC firmware version: 		0

GPU[1]		: ME firmware version: 		166

GPU[1]		: MEC firmware version: 	33230

GPU[1]		: MEC2 firmware version: 	33230

GPU[1]		: PFP firmware version: 	191

GPU[1]		: RLC firmware version: 	96

GPU[1]		: RLC SRLC firmware version: 	0

GPU[1]		: RLC SRLG firmware version: 	0

GPU[1]		: RLC SRLS firmware version: 	0

GPU[1]		: SDMA firmware version: 	434

GPU[1]		: SDMA2 firmware version: 	434

GPU[1]		: SMC firmware version: 	05.28.19.00

GPU[1]		: SOS firmware version: 	0x0008025d

GPU[1]		: TA RAS firmware version: 	00.00.00.00

GPU[1]		: TA XGMI firmware version: 	00.00.00.00

GPU[1]		: UVD firmware version: 	0x422b1100

GPU[1]		: VCE firmware version: 	0x39060400

GPU[1]		: VCN firmware version: 	0x00000000

================================================================================
================================= Product Info =================================
GPU[0]		: Card series: 		Vega 10 XL/XT [Radeon RX Vega 56/64]

GPU[0]		: Card model: 		0xe37f

GPU[0]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]

GPU[0]		: Card SKU: 		D05001

GPU[1]		: Card series: 		Vega 10 XL/XT [Radeon RX Vega 56/64]

GPU[1]		: Card model: 		0xe37f

GPU[1]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]

GPU[1]		: Card SKU: 		D05001

================================================================================
================================== Pages Info ==================================
============================ Show Valid sclk Range =============================
GPU[0]		: Unable to display sclk range

GPU[1]		: Unable to display sclk range

================================================================================
============================ Show Valid mclk Range =============================
GPU[0]		: Unable to display mclk range

GPU[1]		: Unable to display mclk range

================================================================================
=========================== Show Valid voltage Range ===========================
GPU[0]		: Unable to display voltage range

GPU[1]		: Unable to display voltage range

================================================================================
============================= Voltage Curve Points =============================
GPU[0]		: Voltage Curve is not supported

GPU[1]		: Voltage Curve is not supported

================================================================================
=============================== Consumed Energy ================================
================================================================================
============================= End of ROCm SMI Log ==============================

Thx



---

## 评论 (2 条)

### 评论 #1 — nartmada (2023-12-19T04:20:09Z)

Hi @sinix-del, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.


---

### 评论 #2 — nartmada (2023-12-27T17:55:17Z)

Closing the ticket as there was no response from the ticket reporter.  @sinix-del, please re-open the ticket if your issue is still not resolved with ROCm 6.0.0.  Thank you.

---
