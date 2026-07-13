# Incorrect reported voltage after --gpureset

- **Issue #:** 1116
- **State:** closed
- **Created:** 2020-05-23T16:40:59Z
- **Updated:** 2021-08-04T10:09:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1116

ROCm v3.3.0
Ubuntu 18.04
Radeon VII

:~$ rocm-smi --showvoltage

GPU[0] 		: Voltage (mV): 737

:~$ rocm-smi -d0 --gpureset

GPU[0] 		: GPU reset was successful

:~$ rocm-smi --showvoltage

GPU[0] 		: Voltage (mV): 1550

Power consumption is also misreported. Any quick fix?