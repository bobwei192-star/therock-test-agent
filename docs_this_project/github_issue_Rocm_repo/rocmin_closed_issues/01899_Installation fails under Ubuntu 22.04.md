# Installation fails under Ubuntu 22.04

- **Issue #:** 1899
- **State:** closed
- **Created:** 2023-02-01T10:41:10Z
- **Updated:** 2023-11-10T16:41:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/1899

Running
```bash
echo "deb [arch=amd64] http://repo.radeon.com/rocm/apt/5.4 jammy main" > /etc/apt/sources.list.d/rocm.list
curl https://repo.radeon.com/rocm/rocm.gpg.key > /etc/apt/trusted.gpg.d/repo.radeon.com.asc
apt-get update
apt-get install -y rocm-hip-sdk
```
in a Ubuntu 22.04 docker image leads to the following error
```
The following packages have unmet dependencies:
 rocm-hip-runtime : Depends: rocminfo (= 1.0.0.50400-72~22.04) but 5.0.0-1 is to be installed
 rocm-hip-runtime-dev : Depends: rocm-device-libs (= 1.0.0.50400-72~22.04) but 5.0.0-1 is to be installed
                        Depends: rocm-cmake (= 0.8.0.50400-72~22.04) but 5.0.0-1 is to be installe
```