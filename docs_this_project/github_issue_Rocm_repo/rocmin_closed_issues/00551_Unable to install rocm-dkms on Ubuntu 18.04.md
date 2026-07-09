# Unable to install rocm-dkms on Ubuntu 18.04

- **Issue #:** 551
- **State:** closed
- **Created:** 2018-09-19T09:30:21Z
- **Updated:** 2019-12-03T09:58:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/551

After installing amdgpu-pro 18.30-641594 on fresh Ubuntu 18.04 get
```
dpkg: error processing archive /tmp/apt-dpkg-install-cYzW7T/17-rock-dkms_1.9-211_all.deb (--unpack):
trying to overwrite '/usr/share/dkms/modules_to_force_install/amdgpu', which is also in package amdgpu-dkms 18.30-641594
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
```

on `apt install rocm-dkms`