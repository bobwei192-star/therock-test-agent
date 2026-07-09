# luxmark 3.1 doesn't work with RX Vega on pcie 2.0 platform

- **Issue #:** 501
- **State:** closed
- **Created:** 2018-08-17T23:09:01Z
- **Updated:** 2018-08-28T07:06:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/501

I'm testing ROCM on a 990FX+AMD FX 8320 platform. The computer has two MSI Vega 56 Airboost in the x16 slots.
Luxmark just shows a black picture as output, and hangs after the 120 second benchmark finishes.

Setting LD_LIBRARY_PROFILE to use the amdgpu-pro 18.20 OpenCL stack works fine.

I can run more tests if needed.