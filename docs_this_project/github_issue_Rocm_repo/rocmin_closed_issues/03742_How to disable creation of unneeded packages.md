# How to disable creation of unneeded packages

- **Issue #:** 3742
- **State:** closed
- **Created:** 2024-09-18T02:01:46Z
- **Updated:** 2024-09-29T19:23:07Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3742

With the default build cmd:
make -f ROCm/tools/ROCm.mk  all
all variants of packages will be created, which I don't need respectively use, I only need DEB. How can I disable the creation of all other, espacially RPM, which fails due an outdated rpmbuild in Debian stable.

Thanks for helping.