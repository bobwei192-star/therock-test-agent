# Large OpenCL performance regression in 3.8 for RX 470 card

- **Issue #:** 1241
- **State:** closed
- **Created:** 2020-09-24T12:22:37Z
- **Updated:** 2020-12-11T06:07:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1241

Ubuntu 18 w/ 5.4.0-48 kernel.
RX 470 GPU
Skylake CPU

Under 3.5, my kernels would take 13.8 ms to complete. With latest 3.8 upgrade, 
time increases to 17.8 ms. So, around 30% slower. 