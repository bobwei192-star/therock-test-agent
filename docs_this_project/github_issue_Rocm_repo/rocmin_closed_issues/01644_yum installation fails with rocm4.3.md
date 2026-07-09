# yum installation fails with rocm4.3

- **Issue #:** 1644
- **State:** closed
- **Created:** 2021-12-18T08:55:00Z
- **Updated:** 2022-01-25T13:05:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/1644

after satisfying all requirements, yum installation gives out error aboutsome dependency but  problem  is this happens with is ROCm4.3 installation instruction : 

ROCm                                            202 kB/s | 168 kB     00:00
(try to add '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
Error:
 Problem: package rocm-dkms-4.2.0.40200-21.el7.x86_64 requires rocm-dev, but none of the providers can be installed
  - package rocm-dev-4.2.0.40200-21.el7.x86_64 requires hip-base, but none of the providers can be installed
  - conflicting requests
  - nothing provides perl-File-BaseDir needed by hip-base-4.2.21155.5900.40200-21.el7.x86_64
