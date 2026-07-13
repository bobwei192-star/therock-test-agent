# OpenCL "slow" performance on ethminer (ethereum)

- **Issue #:** 132
- **State:** closed
- **Created:** 2017-06-21T10:27:24Z
- **Updated:** 2025-01-14T15:33:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/132

The good news is that you can use "ROCm driver" for cpp-ethminer. Which does fail on amdgpu-pro 17.10. (at least on RX 480). I am posting this here, since I couldn't find anyone using ROCm for mining.

_I do not know what are differences between amdgpu-pro and ROCm version of OpenCL (AMD-APP), if someone explain it would be nice_

The "problem" is performance. The performance on RX 480 using amdgpu-pro should be ~ 22MH/s [*], but the max I can get is ~19MH/s. The more interesting thing is, if I manually underclock to 900MHz [**] (level 2 in `pp_dpm_sclk`) the speed stays the same, but there is much reduction of noise heat and power consumption.

Is there any known reason for slower mining speed and not scaling on higher frequencises?

[*] http://www.phoronix.com/scan.php?page=article&item=ethminer-linux-gpus&num=2
[**]
```
sudo su
echo manual > /sys/class/drm/card0/device/power_dpm_force_performance_level
echo 2 > /sys/class/drm/card0/device/pp_dpm_sclk
cat /sys/class/drm/card0/device/pp_dpm_sclk
```