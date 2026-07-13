# ROCm upgrades itself without explicit request

- **Issue #:** 1198
- **State:** closed
- **Created:** 2020-08-22T13:41:01Z
- **Updated:** 2022-02-27T19:31:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1198

Just doing normal ubuntu updates causes ROCm to upgrade itself. With normal debian repositories this would not be a problem. But ROCm is different: The [Release Notes](https://github.com/RadeonOpenCompute/ROCm#fresh-installation-of-amd-rocm-v37-recommended) of ROCM 3.7 state that "fresh and clean installation of AMD ROCm v3.7 is recommended".

The reason for this statement becomes obvious after such an involuntary upgrade: the whole ROCm installation is broken and must be fixed by manually executing the steps described in the installation guide. Several issues reported in this project already document this behavior.

While it is can be reasonable to have a manual upgrade process for ROCm software it is not reasonable to expect users to disable all updates for ubuntu. Updates are needed in order to keep the installation secure and to have bugs in other software packages fixed.