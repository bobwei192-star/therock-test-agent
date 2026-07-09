# ROCm Release Manager signature invalid

- **Issue #:** 859
- **State:** closed
- **Created:** 2019-08-10T08:30:57Z
- **Updated:** 2024-01-29T02:51:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/859

I get this error related to the signature of the release manager being invalid:

```
$ sudo apt update
[...]
Err:20 http://repo.radeon.com/rocm/apt/debian xenial InRelease                                         
  The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
Reading package lists... Done 
Building dependency tree       
Reading state information... Done
All packages are up to date.
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://repo.radeon.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
W: Failed to fetch http://repo.radeon.com/rocm/apt/debian/dists/xenial/InRelease  The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
W: Some index files failed to download. They have been ignored, or old ones used instead.
```