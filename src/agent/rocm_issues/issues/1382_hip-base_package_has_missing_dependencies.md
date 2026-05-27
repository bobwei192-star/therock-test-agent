# hip-base package has missing dependencies

> **Issue #1382**
> **状态**: closed
> **创建时间**: 2021-02-15T09:01:42Z
> **更新时间**: 2021-05-07T10:35:31Z
> **关闭时间**: 2021-05-07T10:35:30Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1382

## 描述

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


---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-02-15T09:40:02Z)

Thanks @baryluk for reaching us.
I will get an update for you.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-02-15T09:53:03Z)

Analyzed more and issue is caused as only hip-base package is installed.
As per HIP documentation, need to install hip-rocclr or hip-nvcc to actually get a complete working hip.
hip-base is common package alone it cannot detect which HIP_PLATFORM.
So I can say that its user error.




---

### 评论 #3 — ROCmSupport (2021-02-15T09:54:35Z)

All hcc code is removed in our HIP staging/internal builds.
The expectation is that the changes are going to merged into release branches soon and so we can expect all hcc based code will be removed and so expect this issue will be not observed anymore from ROCm 4.2/4.3
Request you to stay tuned for the updates.
Thank you.

---

### 评论 #4 — baryluk (2021-02-15T10:17:33Z)

> Analyzed more and issue is caused as only hip-base package is installed.
> As per HIP documentation, need to install hip-rocclr or hip-nvcc to actually get a complete working hip.
> hip-base is common package alone it cannot detect which HIP_PLATFORM.
> So I can say that its user error.

No, it is a packaging error.


---

### 评论 #5 — ROCmSupport (2021-03-17T06:19:06Z)

All hcc code is removed in our HIP staging/internal builds.
The expectation is that the changes are going to merged into release branches soon and so we can expect all hcc based code will be removed and so expect this issue will be not observed anymore from ROCm 4.2/4.3.
Request you to stay tuned for the updates.
Thank you.

---

### 评论 #6 — ROCmSupport (2021-05-07T10:35:30Z)

Hi @baryluk 
got an update.
The issue is resolved now as the cleaning of hcc is done and all hcc content is erased now.
I verified with the internal 4.2 code and issue is fixed now. 4.2 will be released in a day or two and so you can also try the same.

master@prj47-rack-43:/opt/rocm-4.2.0$ /opt/rocm-4.2.0/bin/hipconfig
HIP version  : 4.2.21155-37cb3a34

== hipconfig
HIP_PATH     : /opt/rocm-4.2.0/hip
ROCM_PATH    : /opt/rocm-4.2.0
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I"/opt/rocm-4.2.0/hip/include" -I"/opt/rocm-4.2.0/llvm/bin/../lib/clang/12.0.0" -I/opt/rocm-4.2.0/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm-4.2.0/hsa
HIP_CLANG_PATH   : /opt/rocm-4.2.0/llvm/bin
clang version 12.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-4.2.0 21161 b204d7f0cae65b6cd4446eec50fc1fb675d582af)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-4.2.0/llvm/bin
LLVM (http://llvm.org/):
  LLVM version 12.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver1

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags :  -std=c++11 -isystem "/opt/rocm-4.2.0/llvm/lib/clang/12.0.0/include/.." -isystem /opt/rocm-4.2.0/hsa/include -isystem "/opt/rocm-4.2.0/hip/include" -O3
hip-clang-ldflags  : --driver-mode=g++ -L"/opt/rocm-4.2.0/hip/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/home/master/.local/bin:/home/master/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

== Linux Kernel
Hostname     : prj47-rack-43
Linux prj47-rack-43 5.4.0-72-generic #80~18.04.1-Ubuntu SMP Mon Apr 12 23:26:25 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.5 LTS
Release:        18.04
Codename:       bionic


---
