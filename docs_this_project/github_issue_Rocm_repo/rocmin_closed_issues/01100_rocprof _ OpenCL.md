# rocprof & OpenCL

- **Issue #:** 1100
- **State:** closed
- **Created:** 2020-05-07T21:35:47Z
- **Updated:** 2021-02-09T09:47:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/1100

We have ported a large project from CUDA to OpenCL, but CUDA is currently about 4x faster on equivalent hardware.  We want to tune the code for OpenCL.  
We used to tune with rcprof on ROCm 2.x, 
but we do not have an OpenCL profiling tool for ROCm 3.3.0.

rcprof used to report OCCUPANCY & register usage for OpenCL.
rocprof has replaced rcprof, and while it can profile ROCm, HIP, HSA, it does NOT profile OpenCL.

The problem is that there is no documentation about configuring rocprof to profile OpenCL.
We can get some diagnostics from rocprof on our code, but nothing on OpenCL. Here is our input.text file with several rocprof profiling features enabled:
```
# Perf counters group 1
pmc : Wavefronts 
# Perf counters group 2
pmc : VALUInsts SALUInsts SFetchInsts FlatVMemInsts LDSInsts
# Perf counters group 3
pmc : GDSInsts VALUUtilization FetchSize
# Perf counters group 4
pmc : WriteSize L2CacheHit
# supported range formats: "3:9", "3:", "3"
range: 1
gpu: 0 
kernel: MedianFilterKernel
```
What flags do we need to profile OpenCL with rocprof in ROCm 3.3.0?
Specifically, we want to monitor occupancy, shared memory & register usage.

