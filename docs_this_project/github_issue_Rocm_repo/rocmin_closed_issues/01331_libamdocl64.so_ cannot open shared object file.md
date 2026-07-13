# libamdocl64.so: cannot open shared object file

- **Issue #:** 1331
- **State:** closed
- **Created:** 2020-12-11T19:45:59Z
- **Updated:** 2021-09-24T20:37:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/1331

apt update send rocm 3.9 to 3.10. 

manually removed via apt remove rocm* and hsa* .

reinstalled rocm via apt. (3.10).

calling clinfo yields

clinfo
dlerror: /opt/rocm-3.1.0/opencl/lib/x86_64/libamdocl64.so: cannot open shared object file: No such file or directory
Number of platforms:				 1




