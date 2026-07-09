# ROCm clang adds own LLVM installation to include search path when OpenMP is enabled

- **Issue #:** 1709
- **State:** closed
- **Created:** 2022-03-18T09:58:17Z
- **Updated:** 2024-02-14T04:27:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/1709

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