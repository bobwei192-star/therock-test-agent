# A clean install of rocm-opencl on debian unstable does not work because of missing libtinfo5

- **Issue #:** 1477
- **State:** closed
- **Created:** 2021-05-20T03:20:26Z
- **Updated:** 2021-11-16T10:11:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/1477

libamd_comgr.so depends on libtinfo.so.5 but the package "comgr" does not list "libtinfo5" as a dependency. 