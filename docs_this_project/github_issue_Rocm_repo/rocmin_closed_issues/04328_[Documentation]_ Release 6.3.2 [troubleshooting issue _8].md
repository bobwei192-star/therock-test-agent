# [Documentation]: Release 6.3.2 [troubleshooting issue #8]

- **Issue #:** 4328
- **State:** closed
- **Created:** 2025-02-02T05:46:46Z
- **Updated:** 2025-05-28T15:01:34Z
- **Labels:** Under Investigation, Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/4328

### Description of errors

Description:

Everything was fine during the installation process, and I was able to load the amdgpu module twice. However, after restarting my system, I faced multiple issues trying to make my kernel (6.11.0-14-generic) load the graphics module. It became impossible to load the amdgpu module, and tools like rocminfo and clinfo indicated that the graphics were not loaded.

The cause was related to Secure Boot, which was preventing the kernel from loading the amdgpu module. This issue was not mentioned in the installation prerequisites or the [Installation troubleshooting section](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.3.2/reference/install-faq.html#issue-8-the-amdgpu-driver-is-not-loaded-after-installation) in the documentation.

Recommendation:

It would be helpful to include a note in the installation prerequisites or troubleshooting section of the documentation to inform users that Secure Boot must be disabled in order for the amdgpu driver to load properly.

    Kernel version: 6.11.0-14-generic 
    Dist: Ubuntu 24.10
    Issue: Secure Boot blocking the loading of the amdgpu module
    Suggested fix: Disable Secure Boot in BIOS/UEFI
    Observations: Not mentioned in the installation prerequisites or the Installation troubleshooting issue#8
