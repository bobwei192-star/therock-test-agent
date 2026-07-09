# OpenCL missing libhsa-ext-finalize64.so.1

- **Issue #:** 537
- **State:** closed
- **Created:** 2018-09-15T14:12:57Z
- **Updated:** 2018-12-05T01:44:59Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/537

After installing the OpenCL path for ROCm 1.9, and following the [HelloWorld test](https://github.com/RadeonOpenCompute/ROCm#upon-restart-to-test-your-opencl-instance). 

I'm unable to run `HelloWorld` as I get the error:
```
[user@host test]$ ./HelloWorld
LoadLib(libhsa-ext-finalize64.so.1) failed: libhsa-ext-finalize64.so.1: cannot open shared object file: No such file or directory
Segmentation fault (core dumped)
```

I've tried on Ubuntu and Fedora and both of them have the same issue. This library `libhsa-ext-finalize64.so.1` is not found in any package in the repo.