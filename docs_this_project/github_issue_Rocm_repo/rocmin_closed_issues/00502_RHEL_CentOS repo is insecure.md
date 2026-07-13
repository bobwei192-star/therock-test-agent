# RHEL/CentOS repo is insecure

- **Issue #:** 502
- **State:** closed
- **Created:** 2018-08-18T16:11:05Z
- **Updated:** 2021-01-07T08:43:12Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/502

The installation http://repo.radeon.com/rocm/yum/rpm/ is insecure and vulnerable to man-in-the-middle attacks that could install trojanized software because: 1. It uses http, not https, and 2. gpgcheck is disabled in the .repo file, presumably because the packages are not signed. 
