# Repo issues for rocprofiler-dev and rocr_debug_agent

- **Issue #:** 914
- **State:** closed
- **Created:** 2019-10-21T07:50:08Z
- **Updated:** 2023-12-18T17:10:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/914

This is the output
```Get:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocprofiler-dev amd64 1.0.0 [217 kB]
Err:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocprofiler-dev amd64 1.0.0
  Hash Sum mismatch
Get:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocr_debug_agent amd64 1.0.0 [890 kB]
Err:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocr_debug_agent amd64 1.0.0
  Writing more data than expected (890180 > 890176)
Fetched 216 kB in 0s (2032 kB/s)         
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocprofiler-dev/rocprofiler-dev_1.0.0_amd64.deb  Hash Sum mismatch

E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocr_debug_agent/rocr_debug_agent_1.0.0_amd64.deb  Writing more data than expected (890180 > 890176)
```
The update of the deb-database is not done (correctly)?