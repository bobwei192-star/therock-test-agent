# Docker image `rocm/dev-ubuntu-20.04:4.2-complete` stops working

- **Issue #:** 1551
- **State:** closed
- **Created:** 2021-08-07T18:05:20Z
- **Updated:** 2021-08-16T05:38:16Z
- **URL:** https://github.com/ROCm/ROCm/issues/1551

I have been using the docker image `rocm/dev-ubuntu-20.04:4.2-complete` as my development and testing environment. However, it stopped working after when 4.3 is released. To recreate the error, one can simply run `apt update` in the docker image and the following error will appear. 

```
W: GPG error: https://repo.radeon.com/rocm/apt/4.2 ubuntu InRelease: The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
E: The repository 'https://repo.radeon.com/rocm/apt/4.2 ubuntu InRelease' is not signed.
```

Here is the error in my testing environment. 

https://gitlab.com/akita/rhipo/-/jobs/1485844044#L52