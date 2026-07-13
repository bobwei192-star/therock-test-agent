# Debian buster Upgrgade from 3.7 -> 3.8 fail : rocm-gdb : Depends: libpython3.8 but it is not installable

- **Issue #:** 1236
- **State:** closed
- **Created:** 2020-09-22T23:48:57Z
- **Updated:** 2021-04-24T16:33:59Z
- **URL:** https://github.com/ROCm/ROCm/issues/1236

On Debian Buster not exist libpython3.8 yet!

```
root@z820 ~ # apt list --upgradable -a
Listing... Done
rocm-gdb/Ubuntu 16.04 9.2-rocm-rel-3.8-30 amd64 [upgradable from: 9.2-rocm-rel-3.7-20]
rocm-gdb/now 9.2-rocm-rel-3.7-20 amd64 [installed,upgradable to: 9.2-rocm-rel-3.8-30]
```
```
root@z820 ~ # apt purge rocm-gdb
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  rocalution* rocm-dev* rocm-dkms* rocm-gdb* rocm-libs*
0 upgraded, 0 newly installed, 5 to remove and 0 not upgraded.
After this operation, 93.1 MB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 247106 files and directories currently installed.)
Removing rocm-libs (3.8.0-30) ...
Removing rocalution (1.9.3.515-rocm-rel-3.8-30-2d9fe47) ...
Removing rocm-dkms (3.8.0-30) ...
Removing rocm-dev (3.8.0-30) ...
Removing rocm-gdb (9.2-rocm-rel-3.7-20) ...
```
```
root@z820 /opt # apt install rocm-gdb
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-gdb : Depends: libpython3.8 but it is not installable
E: Unable to correct problems, you have held broken packages.
```
If add repo from sid and try install libpython3.8 we got:
```
root@z820 /etc/apt # apt install libpython3.8
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 libc6-dev : Breaks: libgcc-8-dev (< 8.4.0-2~) but 8.3.0-6 is to be installed
E: Error, pkgProblemResolver::Resolve generated breaks, this may be caused by held packages.
```
P.S. At this moment impossible to install rocm-gdb v3.8
How to fix it?
Or how to install / build libpython3.8 ?