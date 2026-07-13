# OpenCL runtime returns improper values for max work items per dimension

- **Issue #:** 58
- **State:** closed
- **Created:** 2016-12-18T21:05:13Z
- **Updated:** 2017-07-02T17:16:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/58

I'm experimenting with the ROCm v1.4 OpenCL preview runtime on a R9-Nano GPU.

clinfo returns for the GPU:
```
...
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
...
```

I think it would be proper for "Max work items[x]"(CL_DEVICE_MAX_WORK_ITEM_SIZES) to be 256 instead of 1024. That's the case for the Windows driver on the same system, btw.
