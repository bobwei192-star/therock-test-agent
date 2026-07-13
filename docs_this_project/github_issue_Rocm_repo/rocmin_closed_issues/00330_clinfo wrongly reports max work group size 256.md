# clinfo wrongly reports max work group size 256

- **Issue #:** 330
- **State:** closed
- **Created:** 2018-02-08T11:18:12Z
- **Updated:** 2018-02-20T21:50:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/330

ROCm 1.7, Ubuntu 17.10, Vega 64:
clinfo reports:
 Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256

In particular the "max workgroup size" does not appear to be correct as I can execute workgroups with larger sizes just fine (tried 512).