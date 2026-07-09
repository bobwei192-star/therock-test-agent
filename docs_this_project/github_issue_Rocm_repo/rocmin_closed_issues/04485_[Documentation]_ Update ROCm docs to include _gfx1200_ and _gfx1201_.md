# [Documentation]: Update ROCm docs to include `gfx1200` and `gfx1201`

- **Issue #:** 4485
- **State:** closed
- **Created:** 2025-03-12T16:37:46Z
- **Updated:** 2025-05-26T15:16:37Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/4485

### Description of errors

It seems that as of #4162, `gfx1200` and `gfx1201` have been added to the ROCm build scripts.

Documentation (mainly support matrices) should be updated to reflect these supported architectures and corresponding hardware, namely Radeon 9070 and Radeon 9070 XT.

Here are some pages which require updates, though this is likely not an exhaustive list:
- https://rocm.docs.amd.com/en/docs-6.3.3/compatibility/compatibility-matrix.html
- https://rocm.docs.amd.com/projects/radeon/en/docs-6.3/docs/compatibility/native_linux/native_linux_compatibility.html
- https://rocm.docs.amd.com/projects/radeon/en/docs-6.3/docs/compatibility/wsl/wsl_compatibility.html

This also addresses some of the questions posed in #4443.

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_