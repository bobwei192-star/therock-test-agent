# Can't install rocm-dev on Debian Bullseye

- **Issue #:** 1125
- **State:** closed
- **Created:** 2020-06-03T03:26:16Z
- **Updated:** 2023-02-01T19:31:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/1125

Trying to install rocm-dev on Debian Bullseye (Testing) fails due to unmet dependencies.
```
$ sudo apt install rocm-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 llvm-amdgpu : Depends: libstdc++-5-dev but it is not installable or
                        libstdc++-7-dev but it is not installable
               Depends: libgcc-5-dev but it is not installable or
                        libgcc-7-dev but it is not installable
E: Unable to correct problems, you have held broken packages.
```
Neither libstdc++-5-dev, libstdc++-7-dev, libgcc-5-dev nor libgcc-7-dev are available for Bullseye anymore