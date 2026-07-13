# The Ubuntu 24.04 quick-start install instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) simply don't work, yielding:

- **Issue #:** 4042
- **State:** closed
- **Created:** 2024-11-20T00:18:10Z
- **Updated:** 2024-11-25T15:02:36Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4042

              The Ubuntu 24.04 quick-start install instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) simply don't work, yielding:
```
The following packages have unmet dependencies:
 hipsolver : Depends: libcholmod3 but it is not installable
             Depends: libsuitesparseconfig5 but it is not installable
 rocm-gdb : Depends: libpython3.10 (>= 3.10.0) but it is not installable
 ```
I guess documentation was copied and pasted with only version number updates, assuming the steps would work about being tested.  No doubt testing these steps takes significant effort - but it's either once at source, or every poor user :-(

The detailed instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/native-install/ubuntu.html) **do work**, I guess because it's vital to register the AMD repo's.

_Originally posted by @chris-hatton in https://github.com/ROCm/ROCm/issues/2993#issuecomment-2480859340_
            