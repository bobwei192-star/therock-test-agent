# Broken repository url with amdgpu-install 5.5.50500-1 for Ubuntu

- **Issue #:** 2111
- **State:** closed
- **Created:** 2023-05-04T12:37:27Z
- **Updated:** 2024-05-13T16:08:33Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/2111

When installing `amdgpu-install_5.5.50500-1_all.deb` it writes a file named `/etc/apt/sources.list.d/amdgpu-proprietary.list` that contains this content:

```
# Enabling this repository requires acceptance of the following license:
# /usr/share/amdgpu-install/AMDGPUPROEULA
#deb https://repo.radeon.com/amdgpu/@AMDGPUVER@/ubuntu jammy proprietary
```

Notice the bad `@AMDGPUVER@` string (instead of `5.5` version string) that makes this file unusable.