# [Issue]: Change the version of libxml2 the rocm use.

- **Issue #:** 6046
- **State:** closed
- **Created:** 2026-03-19T01:46:50Z
- **Updated:** 2026-04-09T18:24:06Z
- **Labels:** status: assessed
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6046

### Problem Description

The ubuntu now use libxml2.so.16 but ROCm only use libxml2.so.2. Should upgrade the shared library ROCm use?

```bash 
$ ldd /opt/rocm-7.2.0/lib/llvm/bin/lld | grep libxml2
        libxml2.so.2 => not found
```
```bash
$ ldconfig -p | grep libxml2
        libxml2.so.16 (libc6,x86-64) => /lib/x86_64-linux-gnu/libxml2.so.16
        libxml2.so.16 (libc6) => /lib/i386-linux-gnu/libxml2.so.16
        libxml2.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libxml2.so
```

### Operating System

Ubuntu 25.10 (Questing Quokka)

### CPU

AMD Ryzen 9 9950X 16-Core Processor

### GPU

Radeon RX 7900 XTX 

### ROCm Version

ROCm 7.2.0

### ROCm Component

llvm-project

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_