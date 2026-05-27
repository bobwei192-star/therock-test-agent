# compute-firmware fails to install

> **Issue #3**
> **状态**: closed
> **创建时间**: 2016-04-20T19:52:40Z
> **更新时间**: 2016-04-20T20:28:51Z
> **关闭时间**: 2016-04-20T20:16:47Z
> **作者**: kwu91
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/3

## 描述

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


---

## 评论 (3 条)

### 评论 #1 — jedwards-AMD (2016-04-20T19:59:32Z)

The radeon-firmware package is the old HSA firmware package, and contains a lot of duplicate files with compute-firmware. You would have trouble installing compute-firmware on top of this packages without apt-get. You can remove radeon-firmware with 'dpkg -r radeon-firmware'. On our end we should add a "Replaces" directive in the compute-firmware package, but for now just remove the radeon-firmware package manually.


---

### 评论 #2 — ghost (2016-04-20T20:16:36Z)

Thanks for pointing that out Kevin. I had completely forgotten about the old radeon-firmware package.

I've updated the "pre-release package cleanup" section of the readme to address this case as well.

For reference, what you need to do is:
sudo apt-get purge radeon-firmware


---

### 评论 #3 — kwu91 (2016-04-20T20:28:51Z)

Removing the radeon-firmware package helped fixed the issue. Thanks all. 


---
