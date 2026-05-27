# hipconfig doesn't work out of the box. missing some package dependency

> **Issue #1140**
> **状态**: closed
> **创建时间**: 2020-06-06T19:51:18Z
> **更新时间**: 2021-02-15T09:32:22Z
> **关闭时间**: 2021-01-12T09:16:16Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1140

## 描述

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


---

## 评论 (16 条)

### 评论 #1 — baryluk (2020-08-25T02:31:42Z)

Still the same issue in 3.7

---

### 评论 #2 — xuhuisheng (2020-08-25T02:54:31Z)

Maybe you should try remove rocm 3.5.0 and reinstall rocm 3.7.0.
I can run hipconfig successly on rocm-3.7.0.
```
$ /opt/rocm/bin/hipconfig
HIP version  : 3.7.20315-077bcfa0

== hipconfig
HIP_PATH     : /opt/rocm-3.7.0/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : clang
HIP_PLATFORM : hcc
HIP_RUNTIME  : ROCclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-3.7.0/hip/include -I/opt/rocm/llvm/bin/../lib/clang/11.0.0 -I/opt/rocm/hsa/include -D__HIP_ROCclr__

== hip-clang
HSA_PATH         : /opt/rocm/hsa
HIP_CLANG_PATH   : /opt/rocm/llvm/bin
clang version 11.0.0 (/src/external/llvm-project/clang ee4e4ebbadcc8ea14ce99e34ed31ab31e94827ac)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
LLVM (http://llvm.org/):
  LLVM version 11.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: haswell

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : -D__HIP_ROCclr__ -std=c++11 -isystem /opt/rocm-3.7.0/llvm/lib/clang/11.0.0/include/.. -isystem /opt/rocm/hsa/include -D__HIP_ROCclr__ -isystem /opt/rocm-3.7.0/hip/include -D__HIP_ARCH_GFX803__=1  -O3
hip-clang-ldflags  : 


 -L/opt/rocm-3.7.0/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm

=== Environment Variables
PATH=/home/work/anaconda3/bin:/home/work/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

== Linux Kernel
Hostname     : 31d2ed49d9f3
Linux 31d2ed49d9f3 5.4.0-42-generic #46~18.04.1-Ubuntu SMP Fri Jul 10 07:21:24 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

---

### 评论 #3 — baryluk (2020-08-25T03:16:37Z)

I never had 3.5 installed on this machine before. I never had any rocm / hip stuff on this machine. It is freshly installed OS.

---

### 评论 #4 — baryluk (2020-08-25T03:17:19Z)

The issue is because `hipconfig` has wrong dependencies. The package it is in (`hip-base3.7.0`) should depend on `llvm-amdgpu`, but it isn't.

---

### 评论 #5 — baryluk (2020-09-22T21:16:18Z)

Still broken in ROCm 3.8:

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



rocminfo, clinfo do all work just fine.


---

### 评论 #6 — crtrott (2020-10-14T22:14:08Z)

Same issue here. 

---

### 评论 #7 — ROCmSupport (2021-01-12T09:16:16Z)

Hi @baryluk and others, thanks for reaching out.
Mentioned issue is no more observed with ROCm 4.0.

taccuser@taccuser-X399-DESIGNARE-EX:/opt/rocm-4.0.0$ /opt/rocm-4.0.0/hip/bin/hipconfig
HIP version  : 4.0.20496-4f163c68

== hipconfig
HIP_PATH     : /opt/rocm-4.0.0/hip
ROCM_PATH    : /opt/rocm-4.0.0
HIP_COMPILER : clang
HIP_PLATFORM : hcc
HIP_RUNTIME  : ROCclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-4.0.0/hip/include -I/opt/rocm-4.0.0/llvm/bin/../lib/clang/12.0.0 -I/opt/rocm-4.0.0/hsa/include -D__HIP_ROCclr__

== hip-clang
HSA_PATH         : /opt/rocm-4.0.0/hsa
HIP_CLANG_PATH   : /opt/rocm-4.0.0/llvm/bin
clang version 12.0.0 (/src/external/llvm-project/clang dac2bfceaa8d4a90257dc8a6d58f268e172ce00e)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-4.0.0/llvm/bin
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
hip-clang-cxxflags : -D__HIP_ROCclr__ -std=c++11 -isystem /opt/rocm-4.0.0/llvm/lib/clang/12.0.0/include/.. -isystem /opt/rocm-4.0.0/hsa/include -D__HIP_ROCclr__ -isystem /opt/rocm-4.0.0/hip/include -O3
hip-clang-ldflags  :  -L/opt/rocm-4.0.0/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm

=== Environment Variables
PATH=/home/taccuser/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

== Linux Kernel
Hostname     : taccuser-X399-DESIGNARE-EX
Linux taccuser-X399-DESIGNARE-EX 5.4.0-59-generic #65-Ubuntu SMP Thu Dec 10 12:01:51 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.1 LTS
Release:        20.04
Codename:       focal

Request to open issues, for any new.
Thank you.

---

### 评论 #8 — baryluk (2021-01-12T14:52:19Z)

@ROCmSupport Issue is still in 4.0. Not fixed.

```
$ /opt/rocm-4.0.0/bin/hipconfig 
HIP version  : 4.0.20496-4f163c68

== hipconfig
HIP_PATH     : /opt/rocm-4.0.0/hip
ROCM_PATH    : /opt/rocm-4.0.0
HIP_COMPILER : hcc
HIP_PLATFORM : hcc
HIP_RUNTIME  : HCC
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-4.0.0/hip/include -I/opt/rocm-4.0.0/hcc/include -I/opt/rocm-4.0.0/hsa/include

== hcc
HSA_PATH     : /opt/rocm-4.0.0/hsa
HCC_HOME     : /opt/rocm-4.0.0/hcc
Can't exec "/opt/rocm-4.0.0/hcc/bin/hcc": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 222.
Can't exec "/opt/rocm-4.0.0/hcc/bin/llc": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 223.
HCC-cxxflags : Can't exec "/opt/rocm-4.0.0/hcc/bin/hcc-config": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 225.

HCC-ldflags  : Can't exec "/opt/rocm-4.0.0/hcc/bin/hcc-config": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 228.


=== Environment Variables
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games

== Linux Kernel
Hostname     : debian
Linux debian 5.9.0-4-amd64 #1 SMP Debian 5.9.11-1 (2020-11-27) x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux bullseye/sid
Release:	unstable
Codename:	sid
```

I did gave explanation what is the issue in my previous comment https://github.com/RadeonOpenCompute/ROCm/issues/1140#issuecomment-679501786

The `/opt/rocm-4.0.0/hcc/bin/llc` is in `llvm-amdgpu` package. So adding `llvm-amdgpu` dependency to `hip-base` should probably help.

It also looks for `/opt/rocm-4.0.0/hcc/bin/hcc`, as it defaults to `HIP_COMPILER` `hcc` (as can be seen above). This is because it also should probably depend on `hip-rocclr` package, which provides `/opt/rocm-4.0.0/hip/lib/.hipInfo` that makes it switch to `clang`.


---

### 评论 #9 — ROCmSupport (2021-01-29T04:54:54Z)

Hi @baryluk 
In your machine, HIP_COMPILER is showing as hcc but it should be clang instead.
I tried on a clean system and it always says clang. So I request you to try on a clean or a different system.

No need to worry about HIP_PLATFORM=hcc in both of our cases as no problem with this for now, but slowly it will also be changes as per the information shared by HIP/compiler team.

Thank you.

---

### 评论 #10 — baryluk (2021-01-29T18:37:56Z)

@ROCmSupport That test was on a clean computer, with no ROCm ever installed.

Here is an example on fresh system:

```
# apt install hip-base4.0.0
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  hip-base4.0.0
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 250 kB of archives.
After this operation, 2,239 kB of additional disk space will be used.
Get:1 https://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-base4.0.0 amd64 4.0.20496.5685.40000-23 [250 kB]
Fetched 250 kB in 1s (321 kB/s)       
Selecting previously unselected package hip-base4.0.0.
(Reading database ... 753192 files and directories currently installed.)
Preparing to unpack .../hip-base4.0.0_4.0.20496.5685.40000-23_amd64.deb ...
Unpacking hip-base4.0.0 (4.0.20496.5685.40000-23) ...
Setting up hip-base4.0.0 (4.0.20496.5685.40000-23) ...
```

```
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
Linux debian 5.10.0-1-amd64 #1 SMP Debian 5.10.4-1 (2020-12-31) x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux bullseye/sid
Release:	unstable
Codename:	sid
#
```


The dependencies are just wrong / missing on `hip-base`.


---

### 评论 #11 — Badasper (2021-02-14T05:45:44Z)

``` lambda-tensorflow-benchmark git:(master) ✗ /opt/rocm-4.0.0/bin/hipconfig 
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/bin/hipconfig line 145.
HIP version  : 4.0.20496-4f163c68

== hipconfig
HIP_PATH     : /opt/rocm-4.0.0/hip
ROCM_PATH    : /opt/rocm-4.0.0
HIP_COMPILER : clang
HIP_PLATFORM : hcc
HIP_RUNTIME  : ROCclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-4.0.0/hip/include -I/opt/rocm-4.0.0/llvm/bin/../lib/clang/ -I/opt/rocm-4.0.0/hsa/include -D__HIP_ROCclr__

== hip-clang
HSA_PATH         : /opt/rocm-4.0.0/hsa
HIP_CLANG_PATH   : /opt/rocm-4.0.0/llvm/bin
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 236.
Can't exec "/opt/rocm-4.0.0/llvm/bin/llc": No such file or directory at /opt/rocm-4.0.0/bin/hipconfig line 237.
hip-clang-cxxflags : Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipcc line 203.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipcc line 204.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipcc line 208.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipcc line 846.
-D__HIP_ROCclr__ -std=c++11 -isystem /opt/rocm-4.0.0/llvm/lib/clang/include/.. -isystem /opt/rocm-4.0.0/hsa/include -D__HIP_ROCclr__ -isystem /opt/rocm-4.0.0/hip/include -O3
hip-clang-ldflags  : Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang++": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-4.0.0/llvm/bin/clang": No such file or directory at /opt/rocm-4.0.0/hip/bin/hipcc line 203.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-4.0.0/hip/bin/hipcc line 204.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipcc line 208.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-4.0.0/hip/bin/hipcc line 846.
--driver-mode=g++ -L/opt/rocm-4.0.0/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm

=== Environment Variables
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/rocm/bin:/opt/rocm/rocprofiler/bin:/opt/rocm/opencl/bin

== Linux Kernel
Hostname     : pc
Linux pc 5.4.0-65-generic #73-Ubuntu SMP Mon Jan 18 17:25:17 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.2 LTS
Release:        20.04
Codename:       focal
```

The dependencies are just wrong 

---

### 评论 #12 — ROCmSupport (2021-02-15T05:20:54Z)

Hi all, as the issue is already in closed state, request to open a new issue for better progress.
Thank you.

---

### 评论 #13 — baryluk (2021-02-15T06:41:31Z)

@ROCmSupport Just reopen this issue please.

---

### 评论 #14 — ROCmSupport (2021-02-15T08:03:24Z)

Hi @baryluk 
This issue does not occur when we install complete rocm as rocm-dkms or rocm-dev(versioned/unversioned).
This issue occurs only when you install hip-base package alone, which is not a recommend way of running hipconfig from there.
Because hip-base needs hip-rocclr as dependency so its not a real issue.
Though its not a real issue, I can ask for possible fix, if any, so request you to log a separate ticket to track this.

Reg this ticket, as the initial issue is taken care, we have closed this ticket.



---

### 评论 #15 — baryluk (2021-02-15T09:02:24Z)

Filled new issue: https://github.com/RadeonOpenCompute/ROCm/issues/1382

---

### 评论 #16 — ROCmSupport (2021-02-15T09:32:22Z)

Thanks @baryluk 
I will take it forward, thank you.

---
