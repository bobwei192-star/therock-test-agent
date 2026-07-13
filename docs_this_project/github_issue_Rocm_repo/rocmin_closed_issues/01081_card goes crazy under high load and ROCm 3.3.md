# card goes crazy under high load and ROCm 3.3

- **Issue #:** 1081
- **State:** closed
- **Created:** 2020-04-13T08:27:58Z
- **Updated:** 2021-06-02T12:15:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1081

At the moment I'm running Folding@Home. I figured running two GPU slots on same card bringd higher efficiency but after some time Fan goes to 100% and I see the following non-sense from `rocm-smi`:
```
$ rocm-smi 
========================ROCm System Management Interface========================
================================================================================
GPU  Temp    AvgPwr        SCLK  MCLK  Fan     Perf  PwrCap  VRAM%  GPU%  
0    511.0c  1072.741824W  N/A   N/A   100.0%  auto  220.0W    2%   100%  
================================================================================
==============================End of ROCm SMI Log ==============================
```

To reproduce, one needs to run `FAHClient` first. Then using `FAHControl` add a second GPU slot and hardcode GPU and OpenCL index to `0`. btw there seems to be a configurator bug because FAHClient loses this configuration on restart.

While running 2 tasks on same GPU simultaneously for awhile the situation described above happens.

-- fahclient-7.5.1-1.x86_64 on Red Hat Enterprise Linux 7.7
-- Vega 10 XTX [Radeon Vega Frontier Edition] with ROCm 3.3 driver