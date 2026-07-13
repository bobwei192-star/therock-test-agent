# Versionless RPM repositories not pointing to current release

- **Issue #:** 1408
- **State:** closed
- **Created:** 2021-03-19T11:06:46Z
- **Updated:** 2021-08-04T10:03:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/1408

Both https://repo.radeon.com/rocm/yum/rpm/ and https://repo.radeon.com/rocm/centos8/rpm/ point to version 4.0.0. However the current release is 4.0.1.

Users probably expect the versionless repository link to always point to the current release. This is actually not the first time this happened. The same happened with previous micro (x.x.1) releases. For major and minor releases the versionless repo has always been updated.