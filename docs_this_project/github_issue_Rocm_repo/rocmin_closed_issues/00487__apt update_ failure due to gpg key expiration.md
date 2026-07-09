# 'apt update' failure due to gpg key expiration

- **Issue #:** 487
- **State:** closed
- **Created:** 2018-08-02T04:16:08Z
- **Updated:** 2019-08-02T20:47:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/487

Hi,

There's an 'apt update' failure due to gpg key expiration:

```
$ wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
$ sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
$ sudo apt update
Get:4 http://repo.radeon.com/rocm/apt/debian xenial InRelease [1,816 B]
Err:4 http://repo.radeon.com/rocm/apt/debian xenial InRelease
  The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360
```

```
$ sudo apt-key list
/etc/apt/trusted.gpg
--------------------
pub   4096R/1A693C5C 2016-08-01 [expired: 2018-08-01]
uid                  James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
```

Regards,