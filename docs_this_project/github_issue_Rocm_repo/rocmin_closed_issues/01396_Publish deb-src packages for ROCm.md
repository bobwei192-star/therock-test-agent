# Publish deb-src packages for ROCm

- **Issue #:** 1396
- **State:** closed
- **Created:** 2021-03-01T11:29:00Z
- **Updated:** 2021-03-22T07:14:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1396

As per the subject. Currently, only the binary debs are available.

In cases like [issue 1236](https://github.com/RadeonOpenCompute/ROCm/issues/1236), working around dependencies that are not available (and not strictly required), it would be much easier to take a deb-src, tweak what is needed and then build one's own packages from that, rather than having to take apart a binary package or forcing installation and breaking the dependency tree.