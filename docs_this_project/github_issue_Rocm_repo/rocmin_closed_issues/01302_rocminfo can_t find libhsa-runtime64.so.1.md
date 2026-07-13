# rocminfo can't find libhsa-runtime64.so.1

- **Issue #:** 1302
- **State:** closed
- **Created:** 2020-11-23T17:58:14Z
- **Updated:** 2021-05-03T13:59:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/1302

$rocminfo
>rocminfo: error while loading shared libraries: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory


$/opt/rocm/opencl/bin/clinfo
dlerror: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory
dlerror: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory
ERROR: clGetPlatformIDs(-1001)

$/opt/rocm/bin/rocminfo
/opt/rocm/bin/rocminfo: error while loading shared libraries: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory

lib-hsa-runtime64.so.1 is already exist /opt/rocm/hsa-amd-aqlprofile/ but can't use.