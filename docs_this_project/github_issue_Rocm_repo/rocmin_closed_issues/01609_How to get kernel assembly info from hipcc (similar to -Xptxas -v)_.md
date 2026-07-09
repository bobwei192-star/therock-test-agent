# How to get kernel assembly info from hipcc (similar to -Xptxas -v)?

- **Issue #:** 1609
- **State:** closed
- **Created:** 2021-11-03T19:15:46Z
- **Updated:** 2024-03-12T23:54:01Z
- **URL:** https://github.com/ROCm/ROCm/issues/1609

Hi everyone, 

I am trying to find a compiler flag (similar to -Xptxas -v in nvcc) to print out kernel information e.g., num. registers per thread, register spills, shared memory usage, etc. Does anybody know which flag I should use?

I am using HIP version 4.2.21155-37cb3a34 and compiling for gfx908 architecture. 

Thanks in advance!