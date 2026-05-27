# ROCm clang adds own LLVM installation to include search path when OpenMP is enabled

> **Issue #1709**
> **状态**: closed
> **创建时间**: 2022-03-18T09:58:17Z
> **更新时间**: 2024-02-14T04:27:33Z
> **关闭时间**: 2024-02-14T04:27:32Z
> **作者**: chrgod
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1709

## 描述

We are compiling a project which utilizes LLVM using ROCm. When we add OpenMP support to our project using the `-fopenmp=libomp` flag (which is what CMake does), clang adds an include search path with top priority to it's own LLVM installation.
We are using our own LLVM package though and the one shipped with ROCm is not compatible as it is newer.

To reproduce it you can run

```
$ /opt/rocm/llvm/bin/clang++ -I /opt/myllvm -v test.cpp 
AMD clang version 14.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.0.2 22065 030a405a181176f1a7749819092f4ef8ea5f0758)
...
#include "..." search starts here:
#include <...> search starts here:
 /opt/myllvm
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7
...
```

and compare to

```
$ /opt/rocm/llvm/bin/clang++ -I /opt/myllvm -v -fopenmp=omp test.cpp 
AMD clang version 14.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.0.2 22065 030a405a181176f1a7749819092f4ef8ea5f0758)
...
#include "..." search starts here:
#include <...> search starts here:
 /opt/rocm-5.0.2/llvm/bin/../include
 /opt/myllvm
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7
...
```

interestingly

```
$ /opt/rocm/llvm/bin/clang++ -I /opt/myllvm -v -fopenmp test.cpp 
AMD clang version 14.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.0.2 22065 030a405a181176f1a7749819092f4ef8ea5f0758)
...
#include "..." search starts here:
#include <...> search starts here:
 /opt/myllvm
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7
 ...
```

We did not see this behavior with our own installation of clang 11 or ROCm 4.

---

## 评论 (2 条)

### 评论 #1 — abhimeda (2024-01-25T03:28:04Z)

@chrgod  Hi, is your issue resolved in the latest ROCm? If so can we close this ticket?

---

### 评论 #2 — nartmada (2024-02-14T04:27:32Z)

Closing the ticket as no response from @chrgod.  Please re-open if issue still exists in latest ROCm 6.0.2.

---
