# compute-firmware fails to install

- **Issue #:** 3
- **State:** closed
- **Created:** 2016-04-20T19:52:40Z
- **Updated:** 2016-04-20T20:28:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/3

When I tried to install rocm through apt-get, compute-firmware fails to install properly:

```
Errors were encountered while processing:
 /var/cache/apt/archives/compute-firmware_1.0-fdd910a_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

When I tried to force the installation through `sudo apt-get -f install` I get the following:

```
The following extra packages will be installed:
  compute-firmware
The following NEW packages will be installed:
  compute-firmware
0 upgraded, 1 newly installed, 0 to remove and 92 not upgraded.
21 not fully installed or removed.
Need to get 0 B/1,349 kB of archives.
After this operation, 21.0 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
(Reading database ... 250969 files and directories currently installed.)
Preparing to unpack .../compute-firmware_1.0-fdd910a_all.deb ...
Unpacking compute-firmware (1.0-fdd910a) ...
Replacing files in old package linux-firmware (1.127.20) ...
dpkg: error processing archive /var/cache/apt/archives/compute-firmware_1.0-fdd910a_all.deb (--unpack):
 trying to overwrite '/lib/firmware/radeon/tonga_sdma1.bin', which is also in package radeon-firmware 410-604
dpkg-deb: error: subprocess paste was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/compute-firmware_1.0-fdd910a_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
