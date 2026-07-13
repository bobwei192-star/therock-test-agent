# **rocm-smi --showbw displays as 0**

- **Issue #:** 2469
- **State:** closed
- **Created:** 2023-09-15T17:31:09Z
- **Updated:** 2024-03-10T05:05:48Z
- **Labels:** Verified Issue, 5.7.0, Resolved
- **URL:** https://github.com/ROCm/ROCm/issues/2469

When ROCm is installed and a workload is run in a console, checking the bandwidth using the _rocm-smi –showbw_ instruction results in a 0.

 
**Expected behavior**

If _showbw_ is supported in AMD Instinct™ MI200, the result appears as follows, 

_taccuser@TCT-ML-MI210-1:~$ rocm-smi –showbw_


**Current behavior**

_--showbw_ appears as 0 even if a workload runs in the background. 

This known issue is expected to be fixed in a future release. 