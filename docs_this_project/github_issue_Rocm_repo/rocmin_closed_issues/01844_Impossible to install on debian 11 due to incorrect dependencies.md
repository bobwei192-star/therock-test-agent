# Impossible to install on debian 11 due to incorrect dependencies

- **Issue #:** 1844
- **State:** closed
- **Created:** 2022-10-25T15:56:04Z
- **Updated:** 2024-05-21T15:40:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/1844

Unfortunately, the dependency list for rocm-llvm includes these:

```
 rocm-llvm : Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable or
                      libstdc++-11-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable or
                      libgcc-11-dev but it is not installable
```

but not this:

```
root@hermes:~# dpkg -l | grep libgcc-10
ii  libgcc-10-dev:amd64                              10.2.1-6                                                         amd64        GCC support library (development files)
root@hermes:~# dpkg -l | grep libgcc-9
ii  libgcc-9-dev:amd64                               9.3.0-22                                                         amd64        GCC support library (development files)
```

Please update the dependencies to include debian's versions, or, remove this dependency check in the .deb, and put it in the `amdgpu-install` script, specifically to check to see that a version of libgcc-number-dev is installed.