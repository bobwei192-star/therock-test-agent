# [Issue]: Only sclk adjustable on mi210, high idle power

- **Issue #:** 5315
- **State:** open
- **Created:** 2025-09-16T00:39:14Z
- **Updated:** 2025-10-31T17:46:13Z
- **Labels:** Feature Request, status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5315

### Problem Description

mi210 cards have `mclk` locked at max even with low power. Kernel is `6.16.6`

```
[user@machine ~]$ rocm-smi -s


============================ ROCm System Management Interface ============================
============================== Supported clock frequencies ===============================
GPU[0]		: 
GPU[0]		: Supported fclk frequencies on GPU0
GPU[0]		: 0: 400Mhz *
GPU[0]		: 
GPU[0]		: Supported mclk frequencies on GPU0
GPU[0]		: 0: 400Mhz
GPU[0]		: 1: 700Mhz
GPU[0]		: 2: 1200Mhz
GPU[0]		: 3: 1600Mhz *
GPU[0]		: 
GPU[0]		: Supported sclk frequencies on GPU0
GPU[0]		: 0: 500Mhz *
GPU[0]		: 1: 500Mhz
GPU[0]		: 
GPU[0]		: Supported socclk frequencies on GPU0
GPU[0]		: 0: 666Mhz
GPU[0]		: 1: 857Mhz
GPU[0]		: 2: 1000Mhz
GPU[0]		: 3: 1090Mhz *
GPU[0]		: 4: 1333Mhz
GPU[0]		: 
GPU[0]		: 
------------------------------------------------------------------------------------------
GPU[1]		: 
GPU[1]		: Supported fclk frequencies on GPU1
GPU[1]		: 0: 400Mhz *
GPU[1]		: 
GPU[1]		: Supported mclk frequencies on GPU1
GPU[1]		: 0: 400Mhz
GPU[1]		: 1: 700Mhz
GPU[1]		: 2: 1200Mhz
GPU[1]		: 3: 1600Mhz *
GPU[1]		: 
GPU[1]		: Supported sclk frequencies on GPU1
GPU[1]		: 0: 500Mhz *
GPU[1]		: 1: 500Mhz
GPU[1]		: 
GPU[1]		: Supported socclk frequencies on GPU1
GPU[1]		: 0: 666Mhz
GPU[1]		: 1: 857Mhz
GPU[1]		: 2: 1000Mhz
GPU[1]		: 3: 1090Mhz *
GPU[1]		: 4: 1333Mhz
GPU[1]		: 
GPU[1]		: 
------------------------------------------------------------------------------------------
==========================================================================================
================================== End of ROCm SMI Log ===================================
```
Trying to set `mclk` to 0 and save power:
```
[user@machine ~]$ sudo rocm-smi --setclock mclk 0


============================ ROCm System Management Interface ============================
=================================== Set mclk Frequency ===================================
GPU[0]		: Performance level was set to manual
GPU[0]		: set_gpu_clk_freq_mclk, Permission denied
ERROR: GPU[0]	: Unable to set mclk bitmask to: 0x1
GPU[1]		: Performance level was set to manual
GPU[1]		: set_gpu_clk_freq_mclk, Permission denied
ERROR: GPU[1]	: Unable to set mclk bitmask to: 0x1
==========================================================================================
================================== End of ROCm SMI Log ===================================
```
Setting or unsetting overdrive bit doesn't seem to change this. Auto and low performance modes are also like this.

Idle power is 38-42W per card, I believe this is primarily because of the memory speed. It does not seem usual methods let me adjust the mclk or other card parameters than sclk. Please advise, as this uses much more power than expected because the card is not idling on linux.

Please advise if this should be filed elsewhere.

### Operating System

Linux

### CPU

Xeon 4th Generation

### GPU

2x Instinct Mi210

### ROCm Version

6.4.3

### ROCm Component

_No response_

### Steps to Reproduce

Install 2x Mi210, set power profile to low. Inspect power consumption with lm-sensors or other tool, inspect clock frequencies. Note that mclk is locked at highest value and does not reduce.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Enabling aspm in driver and kernel does not help. Enabling overdrive does not help (e.g. ppfeaturemask).