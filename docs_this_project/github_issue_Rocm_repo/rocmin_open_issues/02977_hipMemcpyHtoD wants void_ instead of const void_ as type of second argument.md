# hipMemcpyHtoD wants void* instead of const void* as type of second argument

- **Issue #:** 2977
- **State:** open
- **Created:** 2024-03-25T15:18:16Z
- **Updated:** 2025-03-26T11:00:24Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon Pro W6800
- **URL:** https://github.com/ROCm/ROCm/issues/2977

### Problem Description

Calling `hipMemcpyHtoD(dst, src, size)` with the same types of arguments as a succesful call to `cuMemcpyHtoD` gives
```
error: invalid conversion from 'const void*' to 'void*' [-fpermissive]
   48 |   .....(hipMemcpyHtoD(dst, src, size));
      |                            ^~~
      |                            |
      |                            const void*
```

So the problem is with the second argument, i.e. `src` with is of type `const void*` and not `void*`, which `hipMemcpyHtoD` needs, contrary to `cuMemcpyHtoD` .

This means that just running `hipconvertinplace-perl.sh` is insufficient.

### Operating System

NAME="Rocky Linux" VERSION="8.9 (Green Obsidian)"

### CPU

AMD EPYC 7282 16-Core Processor

### GPU

AMD Radeon Pro W6800

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

Call `hipMemcpyHtoDAsync` with a `const void*` type second argument while not using `-fpermissive`.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_