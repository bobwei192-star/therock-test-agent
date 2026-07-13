# amdgpu-install --usecase=rocm problem on openSUSE Leap 15.4

- **Issue #:** 1827
- **State:** closed
- **Created:** 2022-10-08T19:52:08Z
- **Updated:** 2024-02-25T15:07:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1827

```
$ sudo zypper --no-gpg-checks install https://repo.radeon.com/amdgpu-install/5.3/sle/15.4/amdgpu-install-5.3.50300-1.noarch.rpm 
$ amdgpu-install --usecase=rocm
Loading repository data...
Reading installed packages...
Resolving package dependencies...

Problem: nothing provides 'perl-URI-Encode' needed by the to be installed hip-devel-5.3.22061.50300-sles153.63.x86_64
 Solution 1: do not install rocm-dev-5.3.0.50300-sles153.63.x86_64
 Solution 2: break hip-devel-5.3.22061.50300-sles153.63.x86_64 by ignoring some of its dependencies
```