# Test for x86_64 architecture before including platform specific headers in ROCm

- **Issue #:** 1222
- **State:** closed
- **Created:** 2020-09-17T21:52:43Z
- **Updated:** 2021-06-02T10:02:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/1222

amd64 platform is assumed in rocm_bandwidth_test/hsatimer.hpp and it includes a platform specific file without guards to check for the platform: 
#include <x86intrin.h>

It also uses __rtdscp and when an alternative timestamp function is used with guards elsewhere in the code. This check should be performed at other locations where __rtdscp is used. 
In rocm-smi, DEBIAN/control also hardcodes Architecture: amd64 in DEBIAN/control

