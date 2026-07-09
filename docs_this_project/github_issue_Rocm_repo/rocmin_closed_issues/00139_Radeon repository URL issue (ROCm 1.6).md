# Radeon repository URL issue (ROCm 1.6)

- **Issue #:** 139
- **State:** closed
- **Created:** 2017-06-30T17:27:45Z
- **Updated:** 2017-06-30T17:35:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/139

According to the documentation the repository URL is not correct. For instance, the GPG key in the wget command should be available at:

`http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key`

However, the actual URL seems to be:

`http://repo.radeon.com/rocm/apt/debian/debian/rocm.gpg.key`

So, one has to add the "debian/" suffix to all URLs for the commands to work.
