# Error: close failed in file object destructor: sys.excepthook is missing

- **Issue #:** 885
- **State:** closed
- **Created:** 2019-09-12T08:58:31Z
- **Updated:** 2019-09-12T10:42:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/885

Hello, thank you for developing ROCm.

I am testing new environment on ROCm 2.4 September 12th, Ubuntu 18.04.3 LTS, Vega VII these days, and now testing to compile a simple program using HIP compiler that I can find in /opt/rocm/hip/bin/. 

The problem is that I cannot compile the below source using hipcc, with a command hipcc test.cpp where test.cpp denotes the file name of the source.

```
#include <iostream>

int main(){
    std::cout << "test is also a test\n";
}

```
After launching hipcc, it stops and does not reply to console. The error message I could obtain sending an exit signal using "Ctl + C" is as following,

```
close failed in file object destructor:
sys.excepthook is missing
lost sys.stderr
```

How can I solve this problem? please help me.