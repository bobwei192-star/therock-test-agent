# Missing deb dependencies on Ubuntu 18.04

- **Issue #:** 1167
- **State:** closed
- **Created:** 2020-06-25T21:43:38Z
- **Updated:** 2020-06-26T16:19:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/1167

During linking the following error message is written out:

```
Can't exec "file": No such file or directory at /opt/rocm/bin/hipcc line 584.
Use of uninitialized value $fileType in pattern match (m//) at /opt/rocm/bin/hipcc line 585.
Use of uninitialized value $fileType in pattern match (m//) at /opt/rocm/bin/hipcc line 585.
Use of uninitialized value $fileType in pattern match (m//) at /opt/rocm/bin/hipcc line 586.
```
This eventually ends with a linking failure.

Apparently, the `hipcc` wrapper uses the `file` command, which wasn't installed as a dependency.

Also: doing an `apt-get upgrade` on the `rocm/dev-ubuntu-18.04:3.5` Docker container completely messes up the install due to missing reinstalls of dependent packages, since some packages will update to 3.5.1. Only a completely fresh install based on Ubuntu 18.04 seems to produce a usable environment (apart from missing dependencies like `file`).