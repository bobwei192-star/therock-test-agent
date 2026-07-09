# [Issue]: rdc/rdc.h is missing #include <stdbool.h>

- **Issue #:** 5061
- **State:** closed
- **Created:** 2025-07-16T19:52:25Z
- **Updated:** 2025-08-14T13:43:43Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5061

### Problem Description

In ROCM 6.4.1, rdc/rdc.h introduces the use of the "bool" type, but it fails to include stdbool.h. It needs to add:

```
#include <stdbool.h>
```

It would be also be great if you could add a simple C build test for this header. This is the second time that rdc.h has failed to compile under C in recent history.

Here's what happens without stdbool.h included:

```
In file included from conftest.c:30:
/opt/rocm-6.4.1/include/rdc/rdc.h:659:3: error: unknown type name 'bool'
   bool is_p2p_accessible;
   ^~~~
/opt/rocm-6.4.1/include/rdc/rdc.h:1739:1: error: unknown type name 'bool'; did you mean '_Bool'?
 bool rdc_is_partition_string(const char* s);
 ^~~~
 _Bool
/opt/rocm-6.4.1/include/rdc/rdc.h:1750:1: error: unknown type name 'bool'; did you mean '_Bool'?
 bool rdc_parse_partition_string(const char* s, uint32_t* physicalGpu, uint32_t* partition);
 ^~~~
 _Bool

```

### Operating System

Any

### CPU

N/A

### GPU

N/A

### ROCm Version

ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_