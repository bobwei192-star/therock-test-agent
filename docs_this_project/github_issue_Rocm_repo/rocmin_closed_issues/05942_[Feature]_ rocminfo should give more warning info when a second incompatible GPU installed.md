# [Feature]: rocminfo should give more warning info when a second incompatible GPU installed

- **Issue #:** 5942
- **State:** closed
- **Created:** 2026-02-07T12:17:36Z
- **Updated:** 2026-04-14T16:31:50Z
- **Labels:** Feature Request, status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5942

### Problem Description

I installed an older GPU as a secondary GPU (in the hopes of playing around with multi GPU running LLMs).

Doing more research, it seems unlikely getting this to work (I find various reports from "should work, and use lower-complexity upper layers on the smaller GPU, deeper higher-complexity-layers on the bigger GPU" to "RX580/gfx803 support has been abandoned or completely removed")...

But at least `rocminfo` should either detect and show both cards, or at least only the primary (RX 7800 XT).

Instead, I get this message:

```
# rocminfo
ROCk module version 6.16.13 is loaded
hsa api call failure at: /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/rocm-systems/projects/rocminfo/rocminfo.cc:1329
Call returned HSA_STATUS_ERROR: A generic error has occurred.
```

### Operating System

Debian 13

### CPU

Ryzen 7 2700X

### GPU

Primary: RX 7800 XT, Secondary: RX 580

### ROCm Version

7.2.0

### ROCm Component

rocminfo

### Steps to Reproduce

* Install two GPUs, one of them old and likely unsupported by ROCm?
* Install ROCm 7.2.0
* Run `rocminfo`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

same output as without `--support`

### Additional Information

Both cards are present:
# lspci | grep VGA
0c:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 32 [Radeon RX 7700 XT / 7800 XT] (rev c8)
0d:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] (rev e7)

Mainboard: Gigabyte Aorus X370 Ultra Gaming

They are in the (according to the motherboard) correct PCIe-Slots, both directly connected to the CPU.
Primary:
```
  LnkSta: Speed 16GT/s, Width x16
                        TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
```
Secondary:
```
LnkSta: Speed 2.5GT/s (downgraded), Width x8 (downgraded)
                        TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
```