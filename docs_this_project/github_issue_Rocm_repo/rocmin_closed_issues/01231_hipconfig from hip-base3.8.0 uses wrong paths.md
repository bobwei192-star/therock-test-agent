# hipconfig from hip-base3.8.0 uses wrong paths

- **Issue #:** 1231
- **State:** closed
- **Created:** 2020-09-22T21:18:46Z
- **Updated:** 2020-12-04T10:03:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1231

hip-base3.8.0  version 3.8.20371-d1886b0b


```
root@debian:~# /opt/rocm-3.8.0/bin/hipconfig 
Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/bin/hipconfig line 145.
HIP version  : 3.8.20371-d1886b0b

== hipconfig
HIP_PATH     : /opt/rocm-3.8.0/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : clang
HIP_PLATFORM : hcc
HIP_RUNTIME  : ROCclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-3.8.0/hip/include -I/opt/rocm/llvm/bin/../lib/clang/ -I/opt/rocm/hsa/include -D__HIP_ROCclr__

== hip-clang
HSA_PATH         : /opt/rocm/hsa
HIP_CLANG_PATH   : /opt/rocm/llvm/bin
Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/bin/hipconfig line 236.
Can't exec "/opt/rocm/llvm/bin/llc": No such file or directory at /opt/rocm-3.8.0/bin/hipconfig line 237.
hip-clang-cxxflags : Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm/llvm/bin/clang": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipcc line 203.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipcc line 204.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipcc line 208.
Use of uninitialized value $HIP_CLANG_INCLUDE_PATH in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipcc line 233.
Use of uninitialized value $HIP_CLANG_INCLUDE_PATH in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipcc line 234.
Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipcc line 724.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/rocm-3.8.0/hip/bin/hipcc line 725.
Use of uninitialized value $targetsStr in split at /opt/rocm-3.8.0/hip/bin/hipcc line 731.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipcc line 848.
-D__HIP_ROCclr__ -std=c++11 -isystem /.. -isystem /opt/rocm/hsa/include -D__HIP_ROCclr__ -isystem /opt/rocm-3.8.0/hip/include -O3
hip-clang-ldflags  : Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm/llvm/bin/clang": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipcc line 203.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.8.0/hip/bin/hipcc line 204.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipcc line 208.
Use of uninitialized value $HIP_CLANG_INCLUDE_PATH in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipcc line 233.
Use of uninitialized value $HIP_CLANG_INCLUDE_PATH in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipcc line 234.
Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/rocm-3.8.0/hip/bin/hipcc line 724.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/rocm-3.8.0/hip/bin/hipcc line 725.
Use of uninitialized value $targetsStr in split at /opt/rocm-3.8.0/hip/bin/hipcc line 731.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.8.0/hip/bin/hipcc line 848.
--driver-mode=g++ -L/opt/rocm-3.8.0/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm

=== Environment Variables
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

== Linux Kernel
Hostname     : debian
Linux debian 5.7.0-1-amd64 #1 SMP Debian 5.7.6-1 (2020-06-24) x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux bullseye/sid
Release:	unstable
Codename:	sid

```