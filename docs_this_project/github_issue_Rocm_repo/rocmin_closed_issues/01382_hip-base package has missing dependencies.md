# hip-base package has missing dependencies

- **Issue #:** 1382
- **State:** closed
- **Created:** 2021-02-15T09:01:42Z
- **Updated:** 2021-05-07T10:35:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/1382

```
# sudo apt install hip-base4.0.0 
...
# /opt/rocm-4.0.0/bin/hipconfig 
HIP version  : 4.0.20496-4f163c68

== hipconfig
HIP_PATH     : /opt/rocm-4.0.0/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : hcc
HIP_PLATFORM : hcc
HIP_RUNTIME  : HCC
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-4.0.0/hip/include -I/opt/rocm/hcc/include -I/opt/rocm/hsa/include

== hcc
HSA_PATH     : /opt/rocm/hsa
HCC_HOME     : /opt/rocm/hcc
Can't exec "/opt/rocm/hcc/bin/hcc": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 222.
Can't exec "/opt/rocm/hcc/bin/llc": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 223.
HCC-cxxflags : Can't exec "/opt/rocm/hcc/bin/hcc-config": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 225.

HCC-ldflags  : Can't exec "/opt/rocm/hcc/bin/hcc-config": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 228.


=== Environment Variables
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

== Linux Kernel
Hostname     : debian
Linux debian 5.10.0-2-amd64 #1 SMP Debian 5.10.9-1 (2021-01-20) x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux bullseye/sid
Release:	testing
Codename:	bullseye

#
```
