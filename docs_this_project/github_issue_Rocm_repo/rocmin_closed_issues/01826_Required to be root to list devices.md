# Required to be root to list devices

- **Issue #:** 1826
- **State:** closed
- **Created:** 2022-10-08T04:31:58Z
- **Updated:** 2024-02-09T14:37:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/1826

Here I'm running ROCm 5.3 on Ubuntu 22.04

I can't list devices as user:

```
illwieckz@test:~$ clinfo --list
```
 
But I can do it as root:

```
illwieckz@test:~$ sudo -u root clinfo --list
Platform #0: AMD Accelerated Parallel Processing
 `-- Device #0: gfx1033
```

Note that this is a computer upgraded from an Ubuntu 20.04 that was the first install.

On another computer, I can list the devices without being root, but this other computer has more than a decade of Ubuntu upgrades so maybe it inherited some configuration from old Ubuntu versions:

```
illwieckz@other:~$ clinfo --list
Platform #0: AMD Accelerated Parallel Processing
 `-- Device #0: gfx701
```

Note: the user is already in the `video` group.