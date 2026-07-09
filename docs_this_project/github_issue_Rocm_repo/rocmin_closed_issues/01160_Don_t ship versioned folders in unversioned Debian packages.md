# Don't ship versioned folders in unversioned Debian packages

- **Issue #:** 1160
- **State:** closed
- **Created:** 2020-06-22T17:00:29Z
- **Updated:** 2021-01-12T14:55:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1160

While it is understandable that support for side-by-side installs of different ROCm versions is intended, this is a concept that does not seem to be properly implemented for the ROCm Debian packages.

And since the 3.5.1 release now has shown that mixed versions are getting shipped on the package repository, the symlink-approach for providing a stable path should be dropped as too unreliable to provide any real benefit.

Instead, please either adjust the packaging to install to stable unversioned paths, so things stop breaking on every other update or actually introduce versioned packages (with the version number in their names), support installing multiple of those in parallel, utilize the powerful alternatives system that comes with Debian and Debian-based distributions: https://wiki.debian.org/DebianAlternatives and then provide unversioned meta-packages that depend on the then-current versioned package similar to how e.g. Linux Kernels are distributed.

Breaking user's setups on every single update and now even patch-release is not fun. Please let's find a solution to put an end to that.