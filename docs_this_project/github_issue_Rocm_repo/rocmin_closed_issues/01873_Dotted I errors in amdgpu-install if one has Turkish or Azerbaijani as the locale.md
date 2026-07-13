# Dotted I errors in amdgpu-install if one has Turkish or Azerbaijani as the locale

- **Issue #:** 1873
- **State:** closed
- **Created:** 2022-12-12T10:24:52Z
- **Updated:** 2024-03-22T17:08:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1873

Steps to reproduce: 
Run `sudo amdgpu-install`

Expected:
Everything goes normally

Actual:
`/usr/bin/amdgpu-install: satır 436: ${USECASE_GRAPHİCS_PACKAGES[*]}: hatalı ikame`