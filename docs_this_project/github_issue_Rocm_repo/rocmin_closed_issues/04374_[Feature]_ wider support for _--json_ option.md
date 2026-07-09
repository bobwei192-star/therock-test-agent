# [Feature]: wider support for '--json' option

- **Issue #:** 4374
- **State:** closed
- **Created:** 2025-02-14T08:25:36Z
- **Updated:** 2025-03-11T19:45:45Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/4374

### Suggestion Description

Our node monitoring scripts call `rocm-smi -a --json` and briefly cache its output in order to make a number of health checks on each compute node. We would like to add a new check for uncorrectable SDMA/GFX/MMHUB errors, but ...
```
[root@vipa1278 ~]# rocm-smi --json --showrasinfo 
WARNING: No JSON data to report
[root@vipa1278 ~]# rocm-smi --json --showrasinfo SDMA GFX MMHUB 
WARNING: No JSON data to report
[root@vipa1278 ~]# 
```
Please could you add support for the `--json` option to all `--show*` options. 

### Operating System

SUSE SLES 15SP*

### GPU

MI300A

### ROCm Component

_No response_