# Missing cmath/libcxx in ROCm 5.3.0

- **Issue #:** 1843
- **State:** closed
- **Created:** 2022-10-24T20:24:41Z
- **Updated:** 2025-11-04T18:45:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1843

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