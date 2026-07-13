# Installation fails on Ubuntu 24.04

- **Issue #:** 4565
- **State:** closed
- **Created:** 2025-04-06T05:13:50Z
- **Updated:** 2025-04-23T19:25:44Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4565

When trying to download rocm 6.3.3 (which I believe is the latest version) on Ubuntu 24.04 (fresh install from 2 days ago), all ways of installing fail when trying to install the `rocm` package with the following issues :
```
The following packages have unmet dependencies.
 libzstd-dev : Depends: libzstd1 (= 1.5.5+dfsg2-2build1) but 1.5.5+dfsg2-2build1.1 is to be installed
 mesa-common-dev : Depends: libdrm-dev (>= 2.4.95) but it is not installable
 python3-dev : Depends: python3 (= 3.12.3-0ubuntu1) but 3.12.3-0ubuntu2 is to be installed
 zlib1g-dev : Depends: zlib1g (= 1:1.3.dfsg-3.1ubuntu2) but 1:1.3.dfsg-3.1ubuntu2.1 is to be installed
```
Attached is the full output from the offline creator tool which is the last thing I tried.

[output.log](https://github.com/user-attachments/files/19619770/output.log)