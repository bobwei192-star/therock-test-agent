# R390 clinfo fails with dmesg failed to register MMU notifier

- **Issue #:** 906
- **State:** closed
- **Created:** 2019-10-10T18:31:41Z
- **Updated:** 2021-01-07T05:26:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/906

```
uname -a
Linux xfer 5.3.4 #1 SMP Sat Oct 5 22:39:14 CEST 2019 x86_64 GNU/Linux

grep HSA /boot/config-5.3.4
CONFIG_HSA_AMD=y

sudo lsmod | grep amdgpu
amdgpu               4677632  3
gpu_sched              36864  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   118784  1 amdgpu
drm_kms_helper        212992  1 amdgpu
drm                   548864  7 gpu_sched,drm_kms_helper,amdgpu,ttm
mfd_core               16384  2 lpc_ich,amdgpu

rocm-smi


========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr   SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%
0    35.0c  15.201W  300Mhz  150Mhz  26.67%  auto  208.0W    0%   0%
1    30.0c  17.001W  300Mhz  150Mhz  26.67%  auto  208.0W    0%   0%
================================================================================
==============================End of ROCm SMI Log ==============================
```

I understand that atomics blocks the use of HCC, I dont' see why this extends to openCL tho

Please advise.

rocm-smi shows the GPUs correctly.