# The RPM signing key expired in August 2021

- **Issue #:** 1762
- **State:** closed
- **Created:** 2022-06-29T10:49:54Z
- **Updated:** 2022-10-13T22:03:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/1762

The signing key for http://repo.radeon.com/rocm/zyp/zypper/ expired last year in August:

```
Warning: The gpg key signing file 'repomd.xml' has expired.
  Repository:       Radeon Open Compute (ROCM)
  Key Fingerprint:  CA8B B472 7A47 B4D0 9B4E E896 9386 B48A 1A69 3C5C
  Key Name:         James Adrian Edwards (ROCm Release Manager) 
<JamesAdrian.Edwards@amd.com>
  Key Algorithm:    RSA 4096
  Key Created:      Fri Aug  2 02:51:30 2019
  Key Expires:      Sun Aug  1 02:51:18 2021 (EXPIRED)
  Subkey:           30C07AF01A6D36BA 2016-08-01 [expired: 2021-08-01]
  Rpm Name:         gpg-pubkey-1a693c5c-5d438912
```

The email address of the key doesn't exist: `The email address you entered couldn't be found.`