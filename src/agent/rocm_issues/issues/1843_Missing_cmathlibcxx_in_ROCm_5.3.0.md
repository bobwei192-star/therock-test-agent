# Missing cmath/libcxx in ROCm 5.3.0

> **Issue #1843**
> **状态**: closed
> **创建时间**: 2022-10-24T20:24:41Z
> **更新时间**: 2025-11-04T18:45:17Z
> **关闭时间**: 2024-05-09T16:33:02Z
> **作者**: joelandman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1843

## 描述

From the HIP examples [repo](https://github.com/ROCm-Developer-Tools/HIP-Examples)  

Machine is a zen2 Ryzen 7 4800H, 64 GB ram, running Linux Mint (Ubuntu derivative).  

```
joe@zap:~/build/HIP-Examples$ ./test_all.sh 

==== vectorAdd ====
rm -f ./vectoradd_hip.exe
rm -f vectoradd_hip.o
rm -f /opt/rocm-5.3.0//hip/src/*.o
/opt/rocm-5.3.0//hip/bin/hipcc -g   -c -o vectoradd_hip.o vectoradd_hip.cpp
In file included from <built-in>:1:
/opt/rocm-5.3.0/llvm/lib/clang/15.0.0/include/__clang_hip_runtime_wrapper.h:50:10: fatal error: 'cmath' file not found
#include <cmath>
         ^~~~~~~
1 error generated when compiling for gfx90c.
make: *** [<builtin>: vectoradd_hip.o] Error 1
...
```

Seems to be missing `cmath` which is usually in a clang `libcxx/include` directory.  I copied the missing headers to a local path, pointed added an include path, and then it complains about a configuration file missing.

```
rm -f ./vectoradd_hip.exe
rm -f vectoradd_hip.o
rm -f /opt/rocm-5.3.0//hip/src/*.o
joe@zap:~/build/HIP-Examples/vectorAdd$ make
/opt/rocm-5.3.0//hip/bin/hipcc -g -I/home/joe/nlytiq/dev/nlytiq-base/llvm-project-15.0.3.src/libcxx/include   -c -o vectoradd_hip.o vectoradd_hip.cpp
In file included from <built-in>:1:
In file included from /opt/rocm-5.3.0/llvm/lib/clang/15.0.0/include/__clang_hip_runtime_wrapper.h:50:
In file included from /home/joe/nlytiq/dev/nlytiq-base/llvm-project-15.0.3.src/libcxx/include/cmath:307:
In file included from /home/joe/nlytiq/dev/nlytiq-base/llvm-project-15.0.3.src/libcxx/include/__assert:13:
/home/joe/nlytiq/dev/nlytiq-base/llvm-project-15.0.3.src/libcxx/include/__config:13:10: fatal error: '__config_site' file not found
#include <__config_site>
         ^~~~~~~~~~~~~~~
1 error generated when compiling for gfx90c.
make: *** [<builtin>: vectoradd_hip.o] Error 1

```

---

## 评论 (18 条)

### 评论 #1 — elbriggs (2022-11-29T21:45:33Z)

I ran into this same issue on Ubuntu 22.04.1 with rocm 5.3.3 installed using the package manger. Worked around it by building llvm from the github release.

---

### 评论 #2 — elliottbinder (2022-12-06T15:26:06Z)

I'm having the same issue w/ 5.4 on 22.04.1. Did you follow the instructions [here](https://github.com/RadeonOpenCompute/llvm-project), @elbriggs?
I did that, followed by build install but hipcc is still not able to find cmath.

---

### 评论 #3 — elbriggs (2022-12-06T16:15:32Z)

I did but I found a better way. Installing libstdc++-12-dev fixes the issue on 22.04.1 with 5.4 without requiring llvm.

---

### 评论 #4 — elliottbinder (2022-12-06T16:42:19Z)

Fixed it for me too, thanks @elbriggs!

---

### 评论 #5 — zilverberg (2022-12-06T19:31:47Z)

Fixed it for me too.
Much appreciated @elbriggs!


---

### 评论 #6 — neoblizz (2023-02-05T20:29:20Z)

Ran into the same issue when I upgraded my Ubuntu 20.04 to 22.04, system information:
```
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.1 LTS
Release:        22.04
Codename:       jammy
```
hipcc information:
```
HIP version: 5.4.22801-aaa1e3d8
AMD clang version 15.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.4.0 22465 d6f0fe8b22e3d8ce0f2cbd657ea14b16043018a5)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
```

The above fix of `sudo apt-get install libstdc++-12-dev` worked for me as well. The error initially showed up as "Failed to find a default HIP architecture", so that might be related. Now it finds the correct architecture being compiled for and not the `gfx000`.

---

### 评论 #7 — ByThisBeard (2023-04-08T00:40:55Z)

> I did but I found a better way. Installing libstdc++-12-dev fixes the issue on 22.04.1 with 5.4 without requiring llvm.

I don't know what this is, or what it did - but the error is gone. Praise!

---

### 评论 #8 — letttop (2023-06-21T15:10:27Z)

> I did but I found a better way. Installing libstdc++-12-dev fixes the issue on 22.04.1 with 5.4 without requiring llvm.

It work! Thanks!

---

### 评论 #9 — trisweb (2023-07-01T22:05:35Z)

It's insane that to get ROCm compilation working you need a secret incantation from a random github issue... but thanks!

---

### 评论 #10 — rraulison (2023-09-19T11:53:55Z)

works for me too!!! rocm 5.6.1 , 5600g apu. thanks!

---

### 评论 #11 — tas71 (2023-10-10T04:19:03Z)

> I did but I found a better way. Installing libstdc++-12-dev fixes the issue on 22.04.1 with 5.4 without requiring llvm.

How did you find this?

---

### 评论 #12 — elbriggs (2023-10-10T17:00:20Z)

Compared my initial fix (building with llvm) with the packages and saw the discrepancy.

---

### 评论 #13 — splasky (2023-10-23T07:09:13Z)

ubutnu 23.04 work. Thanks!

---

### 评论 #14 — torehl (2023-11-01T12:09:23Z)

Hit this issue compiling OpenUCC 1.2.0 with Cuda and ROCm support. Installing libstdc++-12-dev fixed issue.

---

### 评论 #15 — BKitor (2023-11-16T00:56:07Z)

```
In file included from /opt/rocm-5.7.0/llvm/lib/clang/17.0.0/include/__clang_hip_runtime_wrapper.h:50:
/opt/rocm-5.7.0/llvm/lib/clang/17.0.0/include/cuda_wrappers/cmath:27:15: fatal error: 'cmath' file not found
#include_next <cmath>
              ^~~~~~~
27:15: fatal error: 'cmath' file not found
#include_next <cmath>
              ^~~~~~~
```

Error is still present in rocm-5.7.0 on Ubuntu 22.04, but libstdc++-12-dev doesn't work anymore. 
New fix is to install libstdc++-13-dev, 
`sudo apt install libstdc++-13-dev`

---

### 评论 #16 — yxsamliu (2023-11-16T03:49:24Z)

execute `hipcc -v` will show detected gcc and selected gcc, e.g:

Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/11
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/12
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/7
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/7.5.0
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/8
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/9
Selected GCC installation: /usr/lib/gcc/x86_64-linux-gnu/12

Usually it selects the highest gcc version installed. If you installed gcc-13, it will select gcc-13, then you need to have libstdc++-13 installed to work.

---

### 评论 #17 — agreppin (2024-11-12T11:13:30Z)

thanks for the info, here is one more fix for ROCm/hipcc 6.2.4 about cmath header not found:
- install libstdc++-14-dev (Ubuntu 24.04.1)

maintainers: please add this dependency on the hipcc deb package

---

### 评论 #18 — a1ix2 (2025-11-04T18:39:57Z)

Nov 2025, Ubuntu 24.04, trying to compile llama.cpp on ROCm 6.3.4 (last version to properly support Mi50/gfx906 target without work-around) suddenly stopped working for some unknown reason complaining about missing cmath. It was working before, but I think I ran an `apt autoremove` recently and libstdc++-14-dev probably got uninstalled since it's not specified as a dep.

So thank you, `sudo apt install libstdc++-14-dev` fixed it right away.

---
