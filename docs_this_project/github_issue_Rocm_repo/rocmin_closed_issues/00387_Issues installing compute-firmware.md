# Issues installing compute-firmware

- **Issue #:** 387
- **State:** closed
- **Created:** 2018-04-15T19:42:52Z
- **Updated:** 2018-05-02T01:48:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/387

`machinehum@wlkr:~/Downloads$ sudo apt --fix-broken install
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Correcting dependencies... Done
The following additional packages will be installed:
  compute-firmware
The following NEW packages will be installed:
  compute-firmware
0 upgraded, 1 newly installed, 0 to remove and 92 not upgraded.
55 not fully installed or removed.
Need to get 0 B/3,259 kB of archives.
After this operation, 36.6 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
(Reading database ... 333728 files and directories currently installed.)
Preparing to unpack .../compute-firmware_1.7.17_all.deb ...
Unpacking compute-firmware (1.7.17) ...
dpkg: error processing archive /var/cache/apt/archives/compute-firmware_1.7.17_all.deb (--unpack):
 trying to overwrite '/lib/firmware/radeon/tahiti_k_smc.bin', which is also in package firmware-amd-graphics 20161130-3
dpkg-deb: error: subprocess paste was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/compute-firmware_1.7.17_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
`

Is there a workaround? Or should I just remove firmware-amd-graphics? This is a dep for firmware-linux-nonfree which I don't really want to remove.