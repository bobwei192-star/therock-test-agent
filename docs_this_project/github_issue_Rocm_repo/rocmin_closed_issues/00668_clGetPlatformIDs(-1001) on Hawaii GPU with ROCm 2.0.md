# clGetPlatformIDs(-1001) on Hawaii GPU with ROCm 2.0

- **Issue #:** 668
- **State:** closed
- **Created:** 2019-01-11T19:17:49Z
- **Updated:** 2019-01-25T21:50:57Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/668

Good evening

After updating my ROCm setup to v2.0 via apt my OpenCL setup is broken.
I managed to fix the issue with missing firmware files (#640),
but executing clinfo now runs into 
``ERROR: clGetPlatformIDs(-1001)``
Calling ``clinfo -v`` just shows the same error.

Do you have an idea where this could come from?

My system is a Ubuntu 18.04.1 (4.15.0-43-generic) with two R9 390 (Hawaii) GPUs
and two Xeon E5-2690 v0 CPUs.
The previous version of rocm (1.9.x), installed via Debian PPA as well,
worked fine on this machine.

Please let me know if you need further information.