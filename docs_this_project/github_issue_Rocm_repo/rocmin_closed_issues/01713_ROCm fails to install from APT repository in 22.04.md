# ROCm fails to install from APT repository in 22.04

- **Issue #:** 1713
- **State:** closed
- **Created:** 2022-03-24T05:27:25Z
- **Updated:** 2024-05-20T16:53:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/1713

Ubuntu 22.04's feature freeze has already passed and the version in the APT repository is not installable due to missing dependencies (in APT-based distributions, feature freeze is also the minor version freeze).

Main issues being:

- python 3.8, whereas the earliest version available is 3.9
- libstdc++ and libgcc symbol version 5 but the earliest version available is 9