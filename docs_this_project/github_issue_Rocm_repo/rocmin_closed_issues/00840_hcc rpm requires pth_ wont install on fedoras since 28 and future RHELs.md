# hcc rpm requires pth, wont install on fedoras since 28 and future RHELs

- **Issue #:** 840
- **State:** closed
- **Created:** 2019-07-10T00:31:05Z
- **Updated:** 2024-05-07T19:53:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/840

`pth` is gone in fedora and will be gone on next RHEL releases. the `npth` package is the replacement.

since the hcc rpm has a hard dependency on pth it wont install at all.
`  - nothing provides pth needed by hcc-1.3.19242-1.x86_64`

forcing installation, it does work, as npth is the intended replacement for pth.

[(more details)](https://github.com/RadeonOpenCompute/ROCm/issues/567#issuecomment-430500573)