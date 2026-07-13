# [Documentation]: Debian 12 installation

- **Issue #:** 4330
- **State:** closed
- **Created:** 2025-02-03T14:25:46Z
- **Updated:** 2025-02-28T15:41:35Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/4330

### Description of errors

* `amdgpu-dkms` fails while building kernel module
* wrong `environment-modules` directions

### Suggestions

* remove the need for`amdgpu-dkms`: kernel 6.1 with its amdgpu (and firmware?) is enough. your dkms version of the module will fail to build on current debian stable. you can get it work on debian unstable but that's out of this issue scope.
* documentation for `environment-modules` doesn't seem accurate for Debian's version. as a replacement, `export ROCM_PATH=/opt/rocm` works.