# Disable P2P and large BAR support for mining machines

- **Issue #:** 678
- **State:** closed
- **Created:** 2019-01-18T02:30:51Z
- **Updated:** 2023-12-12T21:53:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/678

Hi, I'm having an issue with Intel consumer platform motherboards (Z270 and Z370), where the driver is unable to allocate large BARs for more than four rx vega 56/64.
This causes crashes and hangs when mining with ROCM using all GPUs, but no problems if using the PAL opencl libraries or when using ROCM selecting only the GPUS that had large BAR enabled.

Attachment is for dmesg output of a machine with 7 vega 64 cards.
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/2771383/dmesg.txt)
