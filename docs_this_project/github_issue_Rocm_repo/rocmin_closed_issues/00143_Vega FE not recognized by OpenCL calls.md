# Vega FE not recognized by OpenCL calls

- **Issue #:** 143
- **State:** closed
- **Created:** 2017-07-01T23:03:58Z
- **Updated:** 2018-07-30T15:00:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/143

Hi, just got an Vega FE and trying to run some compute task on it. Installed 1.6 (ROCM OpenCL opencl-dev)and everything seems fine (Vega card is properly initialized on boot, and KFD shows device added properly), but OpenCL apps don't see the card. 

Also tried installing the 17.20 driver packages, and same thing there as well (Those drivers DO see the Polaris based cards though). Interestingly if I remove the polaris card and try to run clinfo on just the vega card it crashes. (I don't see clinfo installed with rocm). 