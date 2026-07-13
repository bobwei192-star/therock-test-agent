# rocm-smi 3.9 & 3.10 returns error

- **Issue #:** 1274
- **State:** closed
- **Created:** 2020-11-01T14:19:48Z
- **Updated:** 2024-06-01T15:28:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1274

I updated my Ubuntu 20.04 container to ROCm 3.9 from 3.8, and rocm-smi now produces the following error:
`ERROR:root:ROCm SMI returned 8 (the expected value is 0)`

Running rocm_smi.py produces the same error, but rocm_smi_deprecated.py seems to work as expected with the following output:
```
========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK     MCLK    Fan   Perf  PwrCap  VRAM%  GPU%  
1    31.0c  7.0W    1269Mhz  945Mhz  0.0%  auto  220.0W    0%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================
```

I have tried completely uninstalling ROCm and reinstalling but the error persists.

**rocm-smi Version:** 3.9.0
**Kernel version:** 5.4.65-1-pve (container host is running ProxMox)
**GPU:** Radeon Instinct MI25