# Repository does not have a Release file 

- **Issue #:** 1736
- **State:** closed
- **Created:** 2022-05-13T09:26:44Z
- **Updated:** 2025-07-23T18:53:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/1736

Since today, I get the following error:

```
$ sudo apt update
[...]
Ign:9 http://repo.radeon.com/rocm/apt/debian xenial InRelease
Err:10 http://repo.radeon.com/rocm/apt/debian xenial Release
  404  Not Found [IP: 13.82.220.49 80]
Reading package lists... Done
E: The repository 'http://repo.radeon.com/rocm/apt/debian xenial Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```