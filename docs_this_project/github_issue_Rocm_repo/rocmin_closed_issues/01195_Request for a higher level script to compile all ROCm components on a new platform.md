# Request for a higher level script to compile all ROCm components on a new platform

- **Issue #:** 1195
- **State:** closed
- **Created:** 2020-08-21T03:51:56Z
- **Updated:** 2020-12-16T11:00:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1195

It would help to have a script that configures, builds, and installs all the components from source code in a  given target directory with an architecture. I am compiling ROCm on ppc64le (Ubuntu 20.04) and I see several places where architecture specific parameters are hard-coded. For e.g., a Linux kernel version 3.6.0 is assumed instead of querying uname to retrieve the current value. This is set in ROCK-Kernel-Driver/include/config/kernel.release and  in ROCK-Kernel-Driver/include/config/auto.conf.cmd. The platform is assumed as amd64 in rocm_bandwidth_test/hsatimer.hpp where #include <x86intrin.h> and __rtdscp are used, rocminfo hard-codes NBIT and NBITSTR based on checks for x86_64 only. In rocm-smi, DEBIAN/control also hardcodes Architecture: amd64 in DEBIAN/control. These issues and the complex dependency graph of some of the other packages such as rocprofiler, make it difficult to build the entire tree from the source code. If a higher-level script can be developed, it would help port us ROCm to other platforms (e.g., ppc64le with Ubuntu 20.04). 