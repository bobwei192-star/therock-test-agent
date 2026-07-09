# Reduce RocM Image size

- **Issue #:** 3935
- **State:** closed
- **Created:** 2024-10-22T23:50:21Z
- **Updated:** 2024-11-13T22:45:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/3935

Note: If I am raising this issue at the wrong place, please forward it to the correct location

https://hub.docker.com/r/rocm/pytorch currently is a ~32 GB decompressed container size.
Most build systems, e.g. github actions only have 25/29GB of total disk space available for the build


