# Unsuccessful installation on Ubuntu 20.04 RX 580

- **Issue #:** 1412
- **State:** closed
- **Created:** 2021-03-20T08:02:54Z
- **Updated:** 2021-03-22T08:34:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/1412

Followed the installation process: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu
When I run:
```
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
```
I get:
```
zsh: no such file or directory: /opt/rocm/bin/rocminfo
dlerror: libamd_comgr.so.1: cannot open shared object file: No such file or directory
ERROR: clGetPlatformIDs(-1001)
```

Kernel: 5.4.0-42-generic
