# ROCm available for Vega M / Kaby Lake G / NUC Hades Canyon?

- **Issue #:** 523
- **State:** closed
- **Created:** 2018-09-07T21:11:54Z
- **Updated:** 2018-10-04T06:04:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/523

Is there support for Vega M processors (Intel i7 with combined AMD GPU)? It's not clear where that model fits in under the [supported list of CPUs](https://github.com/RadeonOpenCompute/ROCm#supported-cpus).

AMDGPU support for Vega M is [said to be available with the 4.18 kernel](https://www.phoronix.com/scan.php?page=news_item&px=Linux-4.18-DRM-Features). I can get ROCm installed under the 4.18.5 kernel on Ubuntu 18.04.1 following the [Vega 56/64 guide](https://github.com/RadeonOpenCompute/ROCm/issues/463), but calling `rocminfo` gives the dreaded return of 

> hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

System information is available [here](https://pastebin.com/raw/AuHQ6Lds) if useful.