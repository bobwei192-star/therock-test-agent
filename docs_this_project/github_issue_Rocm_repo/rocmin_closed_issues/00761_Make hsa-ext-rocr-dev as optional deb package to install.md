# Make hsa-ext-rocr-dev as optional deb package to install

- **Issue #:** 761
- **State:** closed
- **Created:** 2019-04-12T13:44:13Z
- **Updated:** 2021-11-15T07:50:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/761

Hi everybody,

thanks a lot for all the efforts to keep this suite as open as possible to the community. I have read in several places (https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/33, https://github.com/RadeonOpenCompute/ROCm/issues/267#issuecomment-422172140) that the only remaining package not open source is `hsa-ext-rocr-dev`, that IIUC, should be optional. The main issue is that in several rocm deb packages it is listed as dependency:
```
apt-cache rdepends hsa-ext-rocr-dev
hsa-ext-rocr-dev
Reverse Depends:
  hsa-rocr-dev
  rocm-dev
  hcc
```

It would be extremely useful if that dependency was removed, so whoever wants to stick with open-source only could deploy rocm without having to mess with dependencies to remove `hsa-ext-rocr-dev`. A quick update of the documentation would resolve any doubt from whoever wants to keep closed sources binaries.

Thanks in advance!

Luca