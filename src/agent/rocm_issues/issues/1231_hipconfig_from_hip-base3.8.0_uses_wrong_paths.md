# hipconfig from hip-base3.8.0 uses wrong paths

> **Issue #1231**
> **状态**: closed
> **创建时间**: 2020-09-22T21:18:46Z
> **更新时间**: 2020-12-04T10:03:58Z
> **关闭时间**: 2020-12-03T08:19:30Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1231

## 描述

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

---

## 评论 (13 条)

### 评论 #1 — baryluk (2020-09-22T21:19:59Z)

Overriding environment variable (to `ROCM_PATH=/opt/rocm-3.8.0`) or providing a symlink in `/opt/rocm -> /opt/rocm-3.8.0`, seems to workaround issue.


---

### 评论 #2 — rrawther (2020-10-01T18:22:01Z)

I am still getting this error even after setting the ROCM_PATH as suggested above.
How to fix this?

---

### 评论 #3 — baryluk (2020-10-02T04:52:18Z)

@rrawther Try: `sudo ln -n -s /opt/rocm-3.8.0 /opt/rocm`

It is very ugly workaround, but can get you going.


---

### 评论 #4 — rkothako (2020-11-03T11:52:04Z)

Hi @baryluk 
This might be fixed with the removal of ldconfig entries in 3.9.
Can you please check with 3.9 and update please.
If not reproduced, request you to close this issue.

---

### 评论 #5 — baryluk (2020-11-03T20:24:48Z)

@rkothako Same with `hip-base3.9.0`. This is fresh installation, with no rocm ever installed on the system.

---

### 评论 #6 — rkothako (2020-11-04T07:54:06Z)

Thanks @baryluk for the information.
I am able to reproduce this issue locally, I will share an update very soon.

---

### 评论 #7 — rkothako (2020-11-04T08:09:53Z)

Hi @baryluk 
The fix for this issue is ready and it will be part of next release.
Thank you.

---

### 评论 #8 — Dan-RAI (2020-11-16T18:27:16Z)

Fresh rocm-3.9.1 install on ubuntu:

Can't exec "/opt/rocm/llvm/bin/clang++": No such file or directory at /opt/rocm/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm/bin/hipconfig line 145.
HIP version  : 3.9.20412-6d111f85

== hipconfig
HIP_PATH     : /opt/rocm-3.9.1/hip



---

### 评论 #9 — ROCmSupport (2020-11-17T13:55:24Z)

Hi @Dan-RAI 
This will be part of 3.10, which will be available very soon.

---

### 评论 #10 — ROCmSupport (2020-12-03T07:57:43Z)

Hi @baryluk and @Dan-RAI 
As promised, this issue is fixed in 3.10 and its working good now.
Thank you.

taccuser@taccuser-All-Series:/# /opt/rocm/hip/bin/hipconfig
HIP version  : 3.10.20465-f9876b8d

== hipconfig
HIP_PATH     : /opt/rocm-3.10.0/hip
ROCM_PATH    : /opt/rocm-3.10.0
HIP_COMPILER : clang
HIP_PLATFORM : hcc
HIP_RUNTIME  : ROCclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-3.10.0/hip/include -I/opt/rocm-3.10.0/llvm/bin/../lib/clang/12.0.0 -I/opt/rocm-3.10.0/hsa/include -D__HIP_ROCclr__

== hip-clang
HSA_PATH         : /opt/rocm-3.10.0/hsa
HIP_CLANG_PATH   : /opt/rocm-3.10.0/llvm/bin
clang version 12.0.0 (/src/external/llvm-project/clang 60f39e2924d51c1e8606f2135f95e9047fb1da5d)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-3.10.0/llvm/bin
LLVM (http://llvm.org/):
  LLVM version 12.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: haswell

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : -D__HIP_ROCclr__ -std=c++11 -isystem /opt/rocm-3.10.0/llvm/lib/clang/12.0.0/include/.. -isystem /opt/rocm-3.10.0/hsa/include -D__HIP_ROCclr__ -isystem /opt/rocm-3.10.0/hip/include -O3
hip-clang-ldflags  :  -L/opt/rocm-3.10.0/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm

=== Environment Variables
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

== Linux Kernel
Hostname     : taccuser-All-Series
Linux taccuser-All-Series 5.4.0-56-generic #62~18.04.1-Ubuntu SMP Tue Nov 24 10:07:50 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.1 LTS
Release:        20.04
Codename:       focal


---

### 评论 #11 — baryluk (2020-12-03T09:39:23Z)

I will test this shortly and response back with results.


---

### 评论 #12 — baryluk (2020-12-03T22:00:07Z)

@streamhsa Yes. It is now fixed. Thank you.

This is will make so many people happy, with things now working really out of the box after installing `rocm-dev`.

---

### 评论 #13 — ROCmSupport (2020-12-04T10:03:58Z)

Thanks @baryluk for your energetic feedback.
Thank you.

---
