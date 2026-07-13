# binary  compiled with hipcc uses 100% cpu forever

- **Issue #:** 694
- **State:** closed
- **Created:** 2019-01-30T15:32:44Z
- **Updated:** 2021-01-07T05:25:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/694

I have an Ubuntu18.04 System.
 Hardware : Xeon e5 1630-v3 with AMD Firepro W9100.
I installed ROCM according to this guide: https://github.com/ROCm/ROCm.github.io/blob/master/ROCmInstall.md
As all of the example applications would hang indefinitely, and there and the current version seems to be broken for Hawaii GPUS,  uninstalled it and installed the 1.92 version with the distro install script.
Unfortunately this does not work either:
I have a simple hello world.
[hallo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2813197/hallo.txt)
compiled with clang it  works fine, and prints "Hello world".
Compiled with hipcc the resulting binary uses 100% CPU, and seems to never complete.  I have left it overnight and didn't see any output.
rocminfo gives me
[roc.txt](https://github.com/RadeonOpenCompute/ROCm/files/2813229/roc.txt)
and hipconfig --full:
[hipconf.txt](https://github.com/RadeonOpenCompute/ROCm/files/2813232/hipconf.txt)

Any sugesstions?


