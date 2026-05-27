# Debian buster Upgrgade from 3.7 -> 3.8 fail : rocm-gdb : Depends: libpython3.8 but it is not installable

> **Issue #1236**
> **状态**: closed
> **创建时间**: 2020-09-22T23:48:57Z
> **更新时间**: 2021-04-24T16:33:59Z
> **关闭时间**: 2020-09-30T12:53:15Z
> **作者**: minzak
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1236

## 描述

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

---

## 评论 (8 条)

### 评论 #1 — rkothako (2020-09-23T08:07:44Z)

Hi @bizlevel 
As we do not support Ubuntu 16.04 officially, we recommend to try with Ubuntu 18.04.x or Ubuntu 20.04.x and comeback with your observations.

---

### 评论 #2 — minzak (2020-09-23T09:03:11Z)

I use Debian 10, it is like Ubuntu 18 on some drivers. 

---

### 评论 #3 — niso (2020-09-23T13:32:58Z)

I have the same problem. Also using Debian 10.
Is there any way to downgrade to 3.7?
Why do you need python 3.8? Which features are not available in python 3.7?

---

### 评论 #4 — baryluk (2020-09-23T22:30:08Z)

@bizlevel

Debian is not officially supported. You are on your own.

I use rocm 3.8 on Debian testing with success tho.

But it is unsupported.

Claiming Debian testing, Debian 10, or Debian sid, "are like" Ubuntu X, is not accurate. Ubuntu usually snapshot their releases at some version of Debian testing, with packages, which might be long gone from Debian. So the incompatibilities are to be expected.


---

### 评论 #5 — rkothako (2020-09-24T04:35:19Z)

Hi @bizlevel 
Yes, we are not supporting debian OS officially.

---

### 评论 #6 — minzak (2020-09-30T12:53:15Z)

As I see, only several ways are possible to resolve it:
- just wait some times for new libs.
- roll back to 3.7
- build owl libpython3.8
- forget about ROCM and go to AMD way driver (and some miner prefer AMD support)

---

### 评论 #7 — baryluk (2020-10-02T06:44:06Z)

@minzak You can build rocm from source. Or do a workaround as I said (that is modify packages to remove this dependency, and force to install it anyway). I agree it is not user friendly, but again, Debian is not supported (regrettably).

Or update to Debian testing. It is not end of the world :)

---

### 评论 #8 — fluidnumericsJoe (2021-04-24T16:22:10Z)

Late to the game, but since the dependency in Debian 10 that causes the break is libpython3.8, you can the people.debian.org unofficial backports to expose libpython3.8 to apt. To install rocm-dev on Debian 10, run the following as a root user
```
apt-get install -y lsb-release
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.1/ xenial main' | tee /etc/apt/sources.list.d/rocm.list
wget https://people.debian.org/~paravoid/python-all/unofficial-python-all.asc
mv unofficial-python-all.asc /etc/apt/trusted.gpg.d
echo "deb http://people.debian.org/~paravoid/python-all $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/python-all.list
apt-get update -y
apt-get install -y rocm-dev rocm-libs
```
[Gist](https://gist.github.com/schoonovernumerics/bcee99cad3e0575539e2507eb62374ca)

---
