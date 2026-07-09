# amdgpu kworker CPU usage growing in time

- **Issue #:** 1059
- **State:** closed
- **Created:** 2020-03-26T11:44:08Z
- **Updated:** 2020-04-25T07:21:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/1059

With RadeonVII (but likely independent of the specific GPU model)
With Linux 2.4.x, 2.5.x, 2.6.x, with ROCm 2.10 and 3.1 (and likely earlier versions too),
when running an OpenCL process for a long time (tens of hours, days),

there are visible (e.g. in "top") root threads "kworker" that take up an amount of CPU that slowly increases over time until reaching 100% (i.e. one core) per kworker. The number of kworker threads is equal to the number of GPUs. Stopping all of the OpenCL apps (on *all* the GPUs) resets these kworkers to 0, from where they start climbing up again.

```
  973 root      20   0       0      0      0 I  35.9   0.0   4:15.28 kworker/1:0-events                                                                                                        
 2477 root      20   0       0      0      0 I  34.9   0.0   0:33.77 kworker/5:34-events
```

After stopping *all* opencl apps and re-starting all again:

```
  650 root      20   0       0      0      0 I   2.3   0.0   8:19.30 kworker/3:3-events                                                                                                        
 3148 root      20   0       0      0      0 I   2.3   0.0   0:01.40 kworker/6:1-events 
```

It appears to me that these "kworker" are related to the amdgpu kernel driver. If so, this may be an amdgpu issue instead of a ROCm one.

One way to repro is to run gpuowl for a long time (many hours), ideally two instances on a system with 2 GPUs, and you should see the kworker average CPU usage growing in time.
