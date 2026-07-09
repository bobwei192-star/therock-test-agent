# [Documentation]: Build requires library not specified in instructions nor called out when failure occurs

- **Issue #:** 2949
- **State:** closed
- **Created:** 2024-03-06T17:37:40Z
- **Updated:** 2025-07-21T15:09:55Z
- **Labels:** Under Investigation, Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/2949

### Description of errors

https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/native-install/ubuntu.html

The current version requires an additional C++ library which is used when building the dynamic library locally:

add:  "sudo apt-get install libstdc++-12-dev" to instructions

Found at:  https://github.com/ROCm/ROCm/issues/2031

### Attach any links, screenshots, or additional evidence you think will be helpful.

https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/native-install/ubuntu.html

https://github.com/ROCm/ROCm/issues/2031