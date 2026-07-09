# OpenCL app lock-up on R9 390x

- **Issue #:** 484
- **State:** closed
- **Created:** 2018-08-01T00:26:35Z
- **Updated:** 2021-11-22T21:55:24Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/484

Ubuntu 18.04, Linux kernel 4.15, ROCm 1.8.2, on a system that was running fine with amdgpu-pro 18.20, and the app is also running fine on different GPUs (vega, fuji) with ROCm 1.8.2.

When running on R9 390x, the apps runs a bit (seconds) and then locks up. I see this in dmesg:
[   99.996641] Evicting PASID 32768 queues
[  100.004263] Restoring PASID 32768 queues
[  700.349797] Evicting PASID 32768 queues
[  700.357341] Restoring PASID 32768 queues

The process appears in "Sl+" state
~$ ps auxw | grep openowl
preda     3020  1.0  0.1 271070972 81644 pts/3 Sl+  10:17   0:04 ./openowl -user preda -cpu 390 -block 100

The GPU uses low power (is not busy) after the lock up.

The system is still responding including graphics on this GPU. I can kill the app with "kill -9" and restart it (and the same lockup repeats).