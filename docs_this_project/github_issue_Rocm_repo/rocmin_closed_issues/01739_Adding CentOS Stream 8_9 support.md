# Adding CentOS Stream 8/9 support

- **Issue #:** 1739
- **State:** closed
- **Created:** 2022-05-19T12:09:15Z
- **Updated:** 2024-01-26T05:24:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/1739

Currently amdgpu-install rpm failed to detect the version of CentOS Stream series as CentOS Stream versioning only use one number (8 or 9) which differs from RHEL's dual number.
As CentOS Stream has different updating model than RHEL it may be tricky to maintain upstream with amdgpu-dkms but rocm repo seems to work fine.
Please add support for CentOS Stream.