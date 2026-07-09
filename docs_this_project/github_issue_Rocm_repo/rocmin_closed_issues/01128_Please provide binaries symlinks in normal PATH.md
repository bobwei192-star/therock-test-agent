# Please provide binaries symlinks in normal PATH

- **Issue #:** 1128
- **State:** closed
- **Created:** 2020-06-04T13:52:54Z
- **Updated:** 2022-02-08T10:52:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/1128

Please provide versioned symlinks to `/opt/rocm-V/bin/X` in `/usr/bin/X-V` owned by packages, and also provide a relatrive symlink from `/usr/bin/X` to `/usr/bin/X-V`  managed using `update-alternatives(1)` ( https://manpages.debian.org/buster/dpkg/update-alternatives.1.en.html ) mechanism. https://wiki.debian.org/DebianAlternatives 

It is a real pain to use rocm right now.