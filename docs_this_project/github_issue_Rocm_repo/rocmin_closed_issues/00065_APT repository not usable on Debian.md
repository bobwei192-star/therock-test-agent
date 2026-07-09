# APT repository not usable on Debian

- **Issue #:** 65
- **State:** closed
- **Created:** 2016-12-31T23:20:33Z
- **Updated:** 2017-02-23T02:45:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/65

Followed the instructions in the readme, resulting in the following errors:
```
Get:76 http://packages.amd.com/rocm/apt/debian xenial InRelease [1,831 B]          
Err:76 http://packages.amd.com/rocm/apt/debian xenial InRelease                    
  The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
Reading package lists... Done                                                        
W: GPG error: http://packages.amd.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
E: The repository 'http://packages.amd.com/rocm/apt/debian xenial InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```