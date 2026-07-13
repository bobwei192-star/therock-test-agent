# ROCm SMI uninstallation issue on RHEL and SLES

- **Issue #:** 4767
- **State:** open
- **Created:** 2025-05-21T18:38:35Z
- **Updated:** 2025-07-21T21:54:14Z
- **Labels:** Verified Issue, ROCm 6.4.1
- **URL:** https://github.com/ROCm/ROCm/issues/4767


`rocm-smi-lib` does not get uninstalled and remains orphaned on RHEL and SLES systems when:

* [Uninstalling ROCm using the AMDGPU installer](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.1/install/amdgpu-install.html#uninstalling-rocm) with `amdgpu-install --uninstall`

* [Uninstalling via package manager](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager/package-manager-rhel.html#uninstall-rocm-packages)
  with `dnf remove rocm-core` on RHEL or `zypper remove rocm-core` on SLES.

As a workaround, manually remove the `rocm-smi-lib` package using `sudo dnf remove rocm-smi-lib` or `sudo zypper remove rocm-smi-lib`.