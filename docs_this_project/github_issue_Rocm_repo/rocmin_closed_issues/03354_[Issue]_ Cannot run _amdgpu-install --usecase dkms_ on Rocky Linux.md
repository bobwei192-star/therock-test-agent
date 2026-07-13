# [Issue]: Cannot run `amdgpu-install --usecase dkms` on Rocky Linux

- **Issue #:** 3354
- **State:** closed
- **Created:** 2024-06-24T13:54:52Z
- **Updated:** 2024-07-31T20:59:30Z
- **Labels:** AMD Instinct MI250X, AMD Instinct MI250, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3354

### Problem Description

I cannot get `amdgpu-install --usecase xxx` to work on Rocky Linux (at the moment I've only test 8). 
Granted, this could be a mess up on my side as It's been since the days of CentOS 6 that I last used anything RedHat based! However I thought I'd raise it as it looks a bit sucpicious either way that it's passing the flag down to dnf.

### Operating System

Rocky Linux 8.9

### CPU

AMD EPYC 7713 64-Core Processor

### GPU

AMD Instinct MI250X, AMD Instinct MI250

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

I'm using ROCm Version 6.1.2 at the moment but it's not available in the list above:

So, I'm running the following and it appears that the --usecase flag is being passed down to the dnf command. Other flags I've tried, such as `--list-usecase` work fine.

```
amdgpu-install --usecase=dkms
usage: dnf install [-c [config file]] [-q] [-v] [--version]
                   [--installroot [path]] [--nodocs] [--noplugins]
                   [--enableplugin [plugin]] [--disableplugin [plugin]]
                   [--releasever RELEASEVER] [--setopt SETOPTS]
                   [--skip-broken] [-h] [--allowerasing] [-b | --nobest] [-C]
                   [-R [minutes]] [-d [debug level]] [--debugsolver]
                   [--showduplicates] [-e ERRORLEVEL] [--obsoletes]
                   [--rpmverbosity [debug level name]] [-y] [--assumeno]
                   [--enablerepo [repo]] [--disablerepo [repo] | --repo
                   [repo]] [--enable | --disable] [-x [package]]
                   [--disableexcludes [repo]] [--repofrompath [repo,path]]
                   [--noautoremove] [--nogpgcheck] [--color COLOR] [--refresh]
                   [-4] [-6] [--destdir DESTDIR] [--downloadonly]
                   [--comment COMMENT] [--bugfix] [--enhancement]
                   [--newpackage] [--security] [--advisory ADVISORY]
                   [--bz BUGZILLA] [--cve CVES]
                   [--sec-severity {Critical,Important,Moderate,Low}]
                   [--forcearch ARCH]
                   PACKAGE [PACKAGE ...]
dnf install: error: unrecognized arguments: --usecase=dkms
```



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

This has worked fine on Ubuntu but only seems to affect my RockyLinux image builds. I'm just using a bit of Packer and Ansible to build the images and whilst this is all successful, when booting the image, I'm greeted with no `rocminfo` binary which lead me to try and manually run this, which resulted in these findings. 

Running it without the flag results in:
```
amdgpu-install
Last metadata expiration check: 0:04:41 ago on Mon Jun 24 13:52:47 2024.
All matches were filtered out by exclude filtering for argument: amdgpu-dkms
Error: Unable to find a match: amdgpu-dkms
```


It's also worth noting that my Ansible does a dnf upgrade at the end of the run, after the GPU section of Ansible passes. This upgrades it from 8.9 to 8.10 of Rocky Linux so I'm not sure if this is having an impact on functionality after the fact but as `rocminfo` isn't available, I suspect this isn't really of note. However the more information I can provide the better, right? 😄 