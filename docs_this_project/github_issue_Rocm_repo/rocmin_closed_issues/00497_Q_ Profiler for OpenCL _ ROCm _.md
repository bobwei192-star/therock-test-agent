# Q: Profiler for OpenCL / ROCm ?

- **Issue #:** 497
- **State:** closed
- **Created:** 2018-08-10T14:55:54Z
- **Updated:** 2019-02-08T17:16:52Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/497

I would like to obtain insight into the performance of an OpenCL app running on ROCm. Is there a GPU profiler that I could use? (that works with ROCm 1.8.2, and OpenCL).

I'm thinking about information such as:
- occupancy problems
- slow or stalled instructions
- cache L1/L2 hit rate etc
- bank conflicts (global or LDS)
etc