# Ubuntu / Debian packages do not update /opt/rocm symlink

- **Issue #:** 1157
- **State:** closed
- **Created:** 2020-06-22T07:21:58Z
- **Updated:** 2021-01-12T08:10:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/1157

The Debian / Ubuntu packages will not update the `/opt/rocm` symlink when upgrading to a new releases. This leaves everything in a broken state after upgrading.