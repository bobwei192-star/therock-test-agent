# Zypper (SLES 15 Service Pack 1) repository missing "repodata"

- **Issue #:** 1084
- **State:** closed
- **Created:** 2020-04-20T12:47:00Z
- **Updated:** 2021-03-17T07:23:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/1084

ROCm SLES 15 Service Pack 1 repository (zypper) at [http://repo.radeon.com/rocm/zyp/zypper/](http://repo.radeon.com/rocm/zyp/zypper/) seems to be missing repository metadata "[repodata](http://repo.radeon.com/rocm/zyp/zypper/repodata/)" used by zypper. This results in following error when update is attempted:

> An error occurred during repository initialization. [zypper|http://repo.radeon.com/rocm/zyp/zypper/] Repository type can't be determined.

The "repodata" are present in version [3.1.1](http://repo.radeon.com/rocm/zyp/3.1.1/repodata/) but not in [3.3](http://repo.radeon.com/rocm/zyp/3.3/repodata/).