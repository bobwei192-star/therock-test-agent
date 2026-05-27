# Unable to install rocm-dkms on Ubuntu 18.04

> **Issue #551**
> **状态**: closed
> **创建时间**: 2018-09-19T09:30:21Z
> **更新时间**: 2019-12-03T09:58:24Z
> **关闭时间**: 2018-09-19T14:13:02Z
> **作者**: Mnkach
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/551

## 描述

After installing amdgpu-pro 18.30-641594 on fresh Ubuntu 18.04 get
```
dpkg: error processing archive /tmp/apt-dpkg-install-cYzW7T/17-rock-dkms_1.9-211_all.deb (--unpack):
trying to overwrite '/usr/share/dkms/modules_to_force_install/amdgpu', which is also in package amdgpu-dkms 18.30-641594
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
```

on `apt install rocm-dkms`

---

## 评论 (7 条)

### 评论 #1 — preda (2018-09-19T13:04:57Z)

You should not install amdgpu-pro together with ROCm. Choose one or the other.

If you want to install ROCm, start by de-installing amdgpu-pro with "amdgpu-uninstall", next uninstall any old ROCm if there's any, then proceed to install ROCm 1.9.

To see what's installed from ROCm, I use
"apt list --installed | grep -i roc"

---

### 评论 #2 — jlgreathouse (2018-09-19T14:13:02Z)

Agreed with @preda 

The `rocm-dkms` package includes updated kernel driver modules for amdgpu and amdkfd. amdgpu-pro comes with its own version of at least amdgpu. I don't work much with amdgpu-pro, so it might come with its own amdkfd -- I seem to remember that amdgpu-pro worked with some of the older versions of our ROCm user-level tools in the past. You can find more information about that [here](https://github.com/RadeonOpenCompute/ROCm/issues/188).

---

### 评论 #3 — mk2016a (2019-12-03T01:02:27Z)

~$ sudo apt --fix-broken install
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Correcting dependencies... Done
The following packages were automatically installed and are no longer required:
  ca-certificates-java default-jre default-jre-headless fonts-dejavu-extra
  fonts-liberation2 fonts-opensymbol gir1.2-geocodeglib-1.0 gir1.2-gudev-1.0
  gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 java-common
  libatk-wrapper-java libatk-wrapper-java-jni libboost-date-time1.65.1
  libboost-filesystem1.65.1 libboost-iostreams1.65.1 libboost-locale1.65.1
  libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5
  libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libfreerdp-client2-2
  libfreerdp2-2 libgc1c2 libgif7 libgom-1.0-0 libgpgmepp6 liblangtag-common
  liblangtag1 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libodfgen-0.1-1
  libpoppler-qt5-1 libqqwing2v5 libqt5qevercloud3 librevenge-0.0-0 libssh-4
  libsuitesparseconfig5 libtidy5 libvncclient1 libwinpr2-2 libxmlsec1
  libxmlsec1-nss lp-solve mimetex openjdk-11-jre openjdk-11-jre-headless
  syslinux syslinux-common syslinux-legacy tidy usb-creator-common
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  rock-dkms
The following NEW packages will be installed:
  rock-dkms
0 upgraded, 1 newly installed, 0 to remove and 5 not upgraded.
1 not fully installed or removed.
Need to get 0 B/7,627 kB of archives.
After this operation, 197 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
(Reading database ... 233018 files and directories currently installed.)
Preparing to unpack .../rock-dkms_2.10-14_all.deb ...
Unpacking rock-dkms (2.10-14) ...
dpkg: error processing archive /var/cache/apt/archives/rock-dkms_2.10-14_all.deb (--unpack):
 trying to overwrite '/usr/share/dkms/modules_to_force_install/amdgpu', which is also in package amdgpu-dkms 19.30-934563
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/rock-dkms_2.10-14_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)


---

### 评论 #4 — mk2016a (2019-12-03T01:02:50Z)

~$ sudo amdgpu-pro-uninstall 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 amdgpu-dkms : Depends: amdgpu-core but it is not going to be installed
 amdgpu-lib-hwe : Depends: amdgpu-core (= 19.30-934563) but it is not going to be installed
 amdgpu-pro-core : Depends: amdgpu-core but it is not going to be installed
 gst-omx-amdgpu : Depends: amdgpu-core but it is not going to be installed
 libdrm-amdgpu-common : Depends: amdgpu-core but it is not going to be installed
 libdrm2-amdgpu:i386 : Depends: amdgpu-core:i386
 libdrm2-amdgpu : Depends: amdgpu-core but it is not going to be installed
 libegl1-amdgpu-mesa:i386 : Depends: amdgpu-core:i386
 libegl1-amdgpu-mesa : Depends: amdgpu-core but it is not going to be installed
 libgbm1-amdgpu:i386 : Depends: amdgpu-core:i386
 libgbm1-amdgpu : Depends: amdgpu-core but it is not going to be installed
 libgl1-amdgpu-mesa-dri:i386 : Depends: amdgpu-core:i386
                               Recommends: libtxc-dxtn-s2tc0:i386 but it is not installable or
                                           libtxc-dxtn0:i386 but it is not installable
 libgl1-amdgpu-mesa-dri : Depends: amdgpu-core but it is not going to be installed
                          Recommends: libtxc-dxtn-s2tc0 but it is not installable or
                                      libtxc-dxtn0 but it is not installable
 libglapi-amdgpu-mesa:i386 : Depends: amdgpu-core:i386
 libglapi-amdgpu-mesa : Depends: amdgpu-core but it is not going to be installed
 libllvm9.0-amdgpu:i386 : Depends: amdgpu-core:i386
 libllvm9.0-amdgpu : Depends: amdgpu-core but it is not going to be installed
 libwayland-amdgpu-client0:i386 : Depends: amdgpu-core:i386
 libwayland-amdgpu-client0 : Depends: amdgpu-core but it is not going to be installed
 libwayland-amdgpu-egl1:i386 : Depends: amdgpu-core:i386
 libwayland-amdgpu-egl1 : Depends: amdgpu-core but it is not going to be installed
 libwayland-amdgpu-server0:i386 : Depends: amdgpu-core:i386
 libwayland-amdgpu-server0 : Depends: amdgpu-core but it is not going to be installed
 mesa-amdgpu-va-drivers:i386 : Depends: amdgpu-core:i386
 mesa-amdgpu-va-drivers : Depends: amdgpu-core but it is not going to be installed
 mesa-amdgpu-vdpau-drivers:i386 : Depends: amdgpu-core:i386
 mesa-amdgpu-vdpau-drivers : Depends: amdgpu-core but it is not going to be installed
 rocm-dkms : Depends: rock-dkms but it is not going to be installed
 xserver-xorg-hwe-amdgpu-video-amdgpu : Depends: amdgpu-core but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).


---

### 评论 #5 — mk2016a (2019-12-03T01:04:21Z)

> Agreed with @preda
> 
> The `rocm-dkms` package includes updated kernel driver modules for amdgpu and amdkfd. amdgpu-pro comes with its own version of at least amdgpu. I don't work much with amdgpu-pro, so it might come with its own amdkfd -- I seem to remember that amdgpu-pro worked with some of the older versions of our ROCm user-level tools in the past. You can find more information about that [here](https://github.com/RadeonOpenCompute/ROCm/issues/188).

Can not uninstall amdgpu pro. What to do now?

---

### 评论 #6 — Justinikus (2019-12-03T03:23:14Z)

Similar problem here, now what?

---

### 评论 #7 — mk2016a (2019-12-03T09:58:24Z)

> Similar problem here, now what?

sudo dpkg -i --force-overwrite /var/cache/apt/archives/rock-dkms_2.10-14_all.deb

---
