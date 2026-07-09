# hipconfig doesn't work out of the box. missing some package dependency

- **Issue #:** 1140
- **State:** closed
- **Created:** 2020-06-06T19:51:18Z
- **Updated:** 2021-02-15T09:32:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/1140

```
# /opt/rocm-3.5.0/hip/bin/hipconfig 
HIP version  : 3.5.20214-a2917cd

== hipconfig
HIP_PATH     : /opt/rocm-3.5.0/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : hcc
HIP_PLATFORM : hcc
HIP_RUNTIME  : HCC
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-3.5.0/hip/include -I/opt/rocm/hcc/include -I/opt/rocm/hsa/include

== hcc
HSA_PATH     : /opt/rocm/hsa
HCC_HOME     : /opt/rocm/hcc
Can't exec "/opt/rocm/hcc/bin/hcc": No such file or directory at /opt/rocm-3.5.0/hip/bin/hipconfig line 216.
Can't exec "/opt/rocm/hcc/bin/llc": No such file or directory at /opt/rocm-3.5.0/hip/bin/hipconfig line 217.
HCC-cxxflags : Can't exec "/opt/rocm/hcc/bin/hcc-config": No such file or directory at /opt/rocm-3.5.0/hip/bin/hipconfig line 219.

HCC-ldflags  : Can't exec "/opt/rocm/hcc/bin/hcc-config": No such file or directory at /opt/rocm-3.5.0/hip/bin/hipconfig line 222.
```

It also incorrectly reports some paths with `/opt/rocm/`. Such directory doesn't exist.
