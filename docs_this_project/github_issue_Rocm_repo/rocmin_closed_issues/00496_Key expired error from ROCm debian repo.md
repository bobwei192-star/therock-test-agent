# Key expired error from ROCm debian repo

- **Issue #:** 496
- **State:** closed
- **Created:** 2018-08-10T06:41:26Z
- **Updated:** 2018-08-10T07:12:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/496

I am getting the following error while doing `apt update`
        W: An error occurred during the signature verification. The repository is not updated and the previous 
        index files will be used. GPG error: http://repo.radeon.com/rocm/apt/debian xenial InRelease: The             following signatures were invalid: KEYEXPIRED [key]  KEYEXPIRED [key]      KEYEXPIRED [key]
        W: Failed to fetch http://repo.radeon.com/rocm/apt/debian/dists/xenial/InRelease  The following     signatures were invalid: KEYEXPIRED [key]  KEYEXPIRED [key]  KEYEXPIRED [key]

Is there any solution to that?