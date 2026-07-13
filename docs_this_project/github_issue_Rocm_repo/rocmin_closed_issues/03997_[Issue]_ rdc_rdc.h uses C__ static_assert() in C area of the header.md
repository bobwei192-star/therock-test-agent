# [Issue]: rdc/rdc.h uses C++ static_assert() in C area of the header

- **Issue #:** 3997
- **State:** closed
- **Created:** 2024-11-06T00:42:09Z
- **Updated:** 2025-01-13T19:49:03Z
- **Labels:** Under Investigation, ROCm 6.2.1
- **URL:** https://github.com/ROCm/ROCm/issues/3997

### Problem Description

Building a C program that includes rdc/rdc.h from ROCm 6.2.1, I'm hitting this error:

```
In file included from conftest.c:28:
/opt/rocm-6.2.1/include/rdc/rdc.h:325:33: error: expected ')' before '%' token
 static_assert(RDC_FI_ECC_SDMA_CE % 2 == 0, "Correctable Error enum is not even");
```

It look like the header uses static_assert(), which I assume is only available in C++, in a C-exposed area of the header.


### Operating System

RHEL8

### CPU

Irrelevant

### GPU

Irrelevant

### ROCm Version

ROCm 6.2.1

### ROCm Component

rdc

### Steps to Reproduce

Compile any C program while including rdc/rdc.h.


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_