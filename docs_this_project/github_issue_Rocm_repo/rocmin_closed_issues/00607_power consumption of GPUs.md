# power consumption of GPUs

- **Issue #:** 607
- **State:** closed
- **Created:** 2018-11-07T08:45:10Z
- **Updated:** 2021-01-07T10:59:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/607

With ROCm 1.9.211, kernel 4.19.0-rc7

The power consumption of one GPU (RX580) is ~30 Watts after boot, but does not return to ~30 Watts after stopping GPU computing program, it remains stuck at ~47 Watts.
Note that during the run of computing program the GPU power is ~144 Watts, it should return to ~30 Watts after stopping the program.

This issue was not present with kernel 4.17
