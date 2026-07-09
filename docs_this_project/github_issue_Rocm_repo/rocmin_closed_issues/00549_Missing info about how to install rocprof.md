# Missing info about how to install rocprof

- **Issue #:** 549
- **State:** closed
- **Created:** 2018-09-18T13:54:34Z
- **Updated:** 2018-09-20T15:30:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/549

Rocprof is not installed with rocm-dkms. I was able to get it only after using:
```
sudo apt install rocprofiler-dev
```
And after that the location of rpl_run.sh was not `/opt/rocm/rocprofiler/bin/rpl_run.sh` but `/opt/rocm/bin/rpl_run.sh`.

Seems old rocm-profiler and rocm-gdb are not working anymore as is stated in readme.md (for rocm-profiler).
