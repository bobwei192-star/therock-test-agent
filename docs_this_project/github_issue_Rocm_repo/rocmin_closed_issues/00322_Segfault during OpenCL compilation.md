# Segfault during OpenCL compilation

- **Issue #:** 322
- **State:** closed
- **Created:** 2018-02-02T12:15:01Z
- **Updated:** 2019-01-03T20:51:39Z
- **Labels:** Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/322

I've been running into occasional segfaults during compilation of kernels with large amounts of inline assembly.  I managed to reproduce this in a small(ish) example while trying to reproduce a var/register leak problem that I am also observing in kernels with inline assembly.  I've attached the example that is reproducing the segfault.  Changing the macro SEGFAULT between 0 and 1 will respectively exclude or include the code that seems to be triggering the problem.

I am running on rocm 1.7 and targeting Vega.

[segfault.txt](https://github.com/RadeonOpenCompute/ROCm/files/1689245/segfault.txt)

Let me know if there is anything else I can do to help hunt down this bug.