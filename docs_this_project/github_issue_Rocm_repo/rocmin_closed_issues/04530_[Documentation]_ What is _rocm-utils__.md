# [Documentation]: What is `rocm-utils`?

- **Issue #:** 4530
- **State:** closed
- **Created:** 2025-03-26T01:27:18Z
- **Updated:** 2025-05-26T15:07:57Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/4530

### Description of errors

When using `dnf`/`apt` to install ROCm, `rocm-utils` is a package installed from `repo.radeon.com` ([e.g., `.deb` here](https://repo.radeon.com/rocm/apt/6.3.3/pool/main/r/rocm-utils/)) but is not mentioned anywhere in the ROCm documentation. The closest thing to documentation relating to this is [this GitHub Pages page of ROCm 4.1 documentation](https://cgmb-rocm-docs.readthedocs.io/en/latest/Installation_Guide/Software-Stack-for-AMD-GPU.html) that was cloned by Cory.

It seems that the only file it adds is a text file (`/opt/rocm/.info/version-utils` ) that contains a single line that specifies the ROCm version. (E.g., `6.3.3-74`.)

Is this an artifact from older versions of ROCm, or is this still used somewhere?

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_