# Unable to get ROCm working with 16.04

> **Issue #522**
> **状态**: closed
> **创建时间**: 2018-09-07T17:01:26Z
> **更新时间**: 2020-01-04T05:53:56Z
> **关闭时间**: 2018-09-07T21:32:12Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/522

## 描述

*(无描述)*

---

## 评论 (6 条)

### 评论 #1 — jlgreathouse (2018-09-07T17:22:42Z)

Could you run `dkms status`, please? I would guess that your "manually installed kernel 4.13 and headers" then movement to linux-generic-hwe has resulted in the correct versions of amdgpu and/or amdkfd not being properly built or installed for your current kernel.

Another few things to try if you have the time:
`sudo update-initramfs -u -k all`, reboot and see if you get a different KFD dmesg.

If the above doesn't work, reboot into 4.15.0-33 and do:
`sudo apt autoremove rocm-dkms; sudo apt -y install rocm-dkms`, then reboot and check this stuff again.

---

### 评论 #2 — computingdolas (2018-09-07T17:52:15Z)

same issue here on EPYC + MI25 server 

calling dmesg | grep -I kfd gives 
[    2.178948] kfd kfd: Initialized module
[    3.212256] amdgpu 0000:06:00.0: kfd not supported on this ASIC
[    5.116217] amdgpu 0000:23:00.0: kfd not supported on this ASIC
[    6.128280] amdgpu 0000:44:00.0: kfd not supported on this ASIC
[    8.031433] amdgpu 0000:63:00.0: kfd not supported on this ASIC

Is it generic problem with the update ?

Although 
dkms status:
amdgpu, 1.8-192, 4.15.0-29-generic, x86_64: installed
amdgpu, 1.8-192, 4.15.0-30-generic, x86_64: installed
amdgpu, 1.8-192, 4.15.0-32-generic, x86_64: installed

uname -a
Linux P47-01 4.15.0-33-generic #36~16.04.1-Ubuntu 

---

### 评论 #3 — jlgreathouse (2018-09-07T17:55:33Z)

Hi @computingdolas 

1.8-192 is ROCm 1.8.2. ROCm 1.8.2 is incompatible with 4.15.0-33, so you will need to update to ROCm 1.8.3.

In addition, it looks like your ROCm installation has not built a DKMS module for your existing kernel, so you are likely falling back to the generic amdgpu driver in 4.15 which is not ROCm-compatible.

What happens if you do `sudo apt update; sudo apt dist-upgrade` ?

---

### 评论 #4 — computingdolas (2018-09-07T18:16:34Z)

Thanks 👍 .. Let's solve this 

Problem not solved : How do I update rocm-kernel to 1.8.3

sudo apt update : gives 
```
sudo apt update
[sudo] password for surf:
Sorry, try again.
[sudo] password for surf:
Get:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [107 kB]
Hit:2 http://de.archive.ubuntu.com/ubuntu xenial InRelease
Get:3 http://repo.radeon.com/rocm/apt/debian xenial InRelease [1816 B]
Get:4 http://de.archive.ubuntu.com/ubuntu xenial-updates InRelease [109 kB]
Get:5 http://de.archive.ubuntu.com/ubuntu xenial-backports InRelease [107 kB]
Get:6 http://security.ubuntu.com/ubuntu xenial-security/main amd64 DEP-11 Metadata [67.7 kB]
Get:7 http://security.ubuntu.com/ubuntu xenial-security/main DEP-11 64x64 Icons [68.0 kB]
Get:8 http://security.ubuntu.com/ubuntu xenial-security/universe amd64 DEP-11 Metadata [107 kB]
Get:9 http://security.ubuntu.com/ubuntu xenial-security/universe DEP-11 64x64 Icons [142 kB]
Hit:10 https://download.docker.com/linux/ubuntu xenial InRelease
Err:3 http://repo.radeon.com/rocm/apt/debian xenial InRelease
  The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360
Get:11 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [842 kB]
Get:12 http://de.archive.ubuntu.com/ubuntu xenial-updates/main i386 Packages [759 kB]
Get:13 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 DEP-11 Metadata [320 kB]
Get:14 http://de.archive.ubuntu.com/ubuntu xenial-updates/main DEP-11 64x64 Icons [225 kB]
Get:15 http://de.archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [682 kB]
Get:16 http://de.archive.ubuntu.com/ubuntu xenial-updates/universe i386 Packages [624 kB]
Get:17 http://de.archive.ubuntu.com/ubuntu xenial-updates/universe amd64 DEP-11 Metadata [247 kB]
Get:18 http://de.archive.ubuntu.com/ubuntu xenial-updates/universe DEP-11 64x64 Icons [333 kB]
Get:19 http://de.archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 DEP-11 Metadata [5960 B]
Get:20 http://de.archive.ubuntu.com/ubuntu xenial-updates/multiverse DEP-11 64x64 Icons [14.3 kB]
Get:21 http://de.archive.ubuntu.com/ubuntu xenial-backports/main amd64 DEP-11 Metadata [3328 B]
Get:22 http://de.archive.ubuntu.com/ubuntu xenial-backports/universe amd64 DEP-11 Metadata [5100 B]
Fetched 4769 kB in 1s (3311 kB/s)
AppStream cache update completed, but some metadata was ignored due to errors.
Reading package lists... Done
Building dependency tree
Reading state information... Done
89 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://repo.radeon.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360
W: Failed to fetch http://repo.radeon.com/rocm/apt/debian/dists/xenial/InRelease  The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360
W: Some index files failed to download. They have been ignored, or old ones used instead.
```
and 

```
sudo apt dist-upgrade
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following packages were automatically installed and are no longer required:
  libllvm5.0 linux-headers-4.13.0-45 linux-headers-4.13.0-45-generic linux-headers-4.15.0-30 linux-headers-4.15.0-30-generic linux-image-4.13.0-45-generic
  linux-image-4.15.0-30-generic linux-image-extra-4.13.0-45-generic linux-modules-4.15.0-30-generic linux-signed-image-4.13.0-45-generic
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  libllvm6.0
The following packages will be upgraded:
  amd64-microcode appstream apt apt-transport-https apt-utils base-files bsdutils docker-ce fonts-opensymbol fwupd gir1.2-gdkpixbuf-2.0 gir1.2-packagekitglib-1.0 guile-2.0-libs
  hicolor-icon-theme libappstream-glib8 libappstream3 libapt-inst2.0 libapt-pkg5.0 libblkid1 libdfu1 libegl1-mesa libfdisk1 libfwupd1 libgbm1 libgdk-pixbuf2.0-0
  libgdk-pixbuf2.0-common libgl1-mesa-dri libgl1-mesa-glx libglapi-mesa libglib2.0-0 libglib2.0-bin libglib2.0-data libmount1 libnux-4.0-0 libnux-4.0-common
  libpackagekit-glib2-16 libpam-systemd libreoffice-avmedia-backend-gstreamer libreoffice-base-core libreoffice-calc libreoffice-common libreoffice-core libreoffice-draw
  libreoffice-gnome libreoffice-gtk libreoffice-impress libreoffice-math libreoffice-ogltrans libreoffice-pdfimport libreoffice-style-breeze libreoffice-style-galaxy
  libreoffice-writer libslang2 libsmartcols1 libsmbclient libsystemd0 libudev1 libuuid1 libwayland-egl1-mesa libwbclient0 libxatracker2 linux-firmware mount nux-tools
  python-apt-common python3-apt python3-uno python3-urllib3 samba-libs shared-mime-info snapd squashfs-tools systemd systemd-sysv ubuntu-core-launcher udev uno-libs3 ure
  util-linux uuid-runtime x11-common xorg xserver-common xserver-xorg-core-hwe-16.04 xserver-xorg-legacy-hwe-16.04 xserver-xorg-video-amdgpu-hwe-16.04
  xserver-xorg-video-ati-hwe-16.04 xserver-xorg-video-intel-hwe-16.04 xserver-xorg-video-radeon-hwe-16.04
89 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 222 MB of archives.
After this operation, 87.0 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 base-files amd64 9.4ubuntu4.7 [65.9 kB]
Get:2 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 bsdutils amd64 1:2.27.1-6ubuntu3.6 [51.2 kB]
Get:3 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 util-linux amd64 2.27.1-6ubuntu3.6 [848 kB]
Get:4 https://download.docker.com/linux/ubuntu xenial/stable amd64 docker-ce amd64 18.06.1~ce~3-0~ubuntu [40.0 MB]
Get:5 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 mount amd64 2.27.1-6ubuntu3.6 [121 kB]
Get:6 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libapt-pkg5.0 amd64 1.2.27 [706 kB]
Get:7 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libapt-inst2.0 amd64 1.2.27 [55.4 kB]
Get:8 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 apt amd64 1.2.27 [1042 kB]
Get:9 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 apt-utils amd64 1.2.27 [196 kB]
Get:10 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 systemd-sysv amd64 229-4ubuntu21.4 [11.6 kB]
Get:11 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpam-systemd amd64 229-4ubuntu21.4 [115 kB]
Get:12 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgl1-mesa-glx amd64 18.0.5-0ubuntu0~16.04.1 [132 kB]
Get:13 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglapi-mesa amd64 18.0.5-0ubuntu0~16.04.1 [23.4 kB]
Get:14 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libllvm6.0 amd64 1:6.0-1ubuntu2~16.04.1 [14.3 MB]
Get:15 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libwayland-egl1-mesa amd64 18.0.5-0ubuntu0~16.04.1 [5778 B]
Get:16 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libegl1-mesa amd64 18.0.5-0ubuntu0~16.04.1 [87.0 kB]
Get:17 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgbm1 amd64 18.0.5-0ubuntu0~16.04.1 [24.0 kB]
Get:18 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgl1-mesa-dri amd64 18.0.5-0ubuntu0~16.04.1 [6080 kB]
Get:19 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 nux-tools amd64 4.0.8+16.04.20180622.2-0ubuntu1 [10.2 kB]
Get:20 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 xserver-xorg-legacy-hwe-16.04 amd64 2:1.19.6-1ubuntu4~16.04.1 [35.5 kB]
Get:21 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 x11-common all 1:7.7+13ubuntu3.1 [22.9 kB]
Get:22 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 xserver-common all 2:1.18.4-0ubuntu0.8 [27.7 kB]
Get:23 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsystemd0 amd64 229-4ubuntu21.4 [204 kB]
Get:24 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 xserver-xorg-core-hwe-16.04 amd64 2:1.19.6-1ubuntu4~16.04.1 [1346 kB]
Get:25 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 systemd amd64 229-4ubuntu21.4 [3615 kB]
Get:26 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 udev amd64 229-4ubuntu21.4 [993 kB]
Get:27 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libudev1 amd64 229-4ubuntu21.4 [54.1 kB]
Get:28 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libuuid1 amd64 2.27.1-6ubuntu3.6 [15.1 kB]
Get:29 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libblkid1 amd64 2.27.1-6ubuntu3.6 [107 kB]
Get:30 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libmount1 amd64 2.27.1-6ubuntu3.6 [114 kB]
Get:31 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglib2.0-data all 2.48.2-0ubuntu4 [132 kB]
Get:32 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglib2.0-bin amd64 2.48.2-0ubuntu4 [39.4 kB]
Get:33 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglib2.0-0 amd64 2.48.2-0ubuntu4 [1119 kB]
Get:34 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 uuid-runtime amd64 2.27.1-6ubuntu3.6 [25.9 kB]
Get:35 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-ogltrans amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [73.3 kB]
Get:36 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 ure amd64 5.1.6~rc2-0ubuntu1~xenial4 [1532 kB]
Get:37 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 uno-libs3 amd64 5.1.6~rc2-0ubuntu1~xenial4 [704 kB]
Get:38 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-calc amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [6463 kB]
Get:39 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-impress amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [969 kB]
Get:40 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-draw amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [2410 kB]
Get:41 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-gnome amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [60.7 kB]
Get:42 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-gtk amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [207 kB]
Get:43 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3-uno amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [137 kB]
Get:44 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-style-galaxy all 1:5.1.6~rc2-0ubuntu1~xenial4 [1523 kB]
Get:45 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-style-breeze all 1:5.1.6~rc2-0ubuntu1~xenial4 [470 kB]
Get:46 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-common all 1:5.1.6~rc2-0ubuntu1~xenial4 [22.4 MB]
Get:47 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-pdfimport amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [182 kB]
Get:48 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-math amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [374 kB]
Get:49 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-base-core amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [714 kB]
Get:50 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-avmedia-backend-gstreamer amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [24.3 kB]
Get:51 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-writer amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [7581 kB]
Get:52 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-core amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [28.2 MB]
Get:53 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgdk-pixbuf2.0-0 amd64 2.32.2-1ubuntu1.5 [159 kB]
Get:54 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgdk-pixbuf2.0-common all 2.32.2-1ubuntu1.5 [10.3 kB]
Get:55 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 fonts-opensymbol all 2:102.7+LibO5.1.6~rc2-0ubuntu1~xenial4 [104 kB]
Get:56 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 samba-libs amd64 2:4.3.11+dfsg-0ubuntu0.16.04.16 [5161 kB]
Get:57 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libwbclient0 amd64 2:4.3.11+dfsg-0ubuntu0.16.04.16 [30.2 kB]
Get:58 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsmbclient amd64 2:4.3.11+dfsg-0ubuntu0.16.04.16 [53.5 kB]
Get:59 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 squashfs-tools amd64 1:4.3-3ubuntu2.16.04.3 [105 kB]
Get:60 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 ubuntu-core-launcher amd64 2.34.2 [1560 B]
Get:61 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 snapd amd64 2.34.2 [14.2 MB]
Get:62 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libfdisk1 amd64 2.27.1-6ubuntu3.6 [138 kB]
Get:63 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsmartcols1 amd64 2.27.1-6ubuntu3.6 [62.7 kB]
Get:64 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libslang2 amd64 2.3.0-2ubuntu1.1 [415 kB]
Get:65 http://de.archive.ubuntu.com/ubuntu xenial-updates/main amd64 apt-transport-https amd64 1.2.27 [26.1 kB]
Setting up libnux-4.0-common (4.0.8+16.04.20180622.2-0ubuntu1) ...
Setting up libnux-4.0-0 (4.0.8+16.04.20180622.2-0ubuntu1) ...
Setting up libxatracker2:amd64 (18.0.5-0ubuntu0~16.04.1) ...
Setting up linux-firmware (1.157.20) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-33-generic
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
update-initramfs: Generating /boot/initrd.img-4.15.0-32-generic
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
update-initramfs: Generating /boot/initrd.img-4.15.0-30-generic
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
update-initramfs: Generating /boot/initrd.img-4.15.0-29-generic
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
update-initramfs: Generating /boot/initrd.img-4.13.0-45-generic
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
Setting up python3-urllib3 (1.13.1-2ubuntu0.16.04.2) ...
Setting up xorg (1:7.7+13ubuntu3.1) ...
Setting up xserver-xorg-video-amdgpu-hwe-16.04 (18.0.1-1~16.04.1) ...
Setting up xserver-xorg-video-radeon-hwe-16.04 (1:18.0.1-1~16.04.1) ...
Setting up xserver-xorg-video-ati-hwe-16.04 (1:18.0.1-1~16.04.1) ...
Setting up xserver-xorg-video-intel-hwe-16.04 (2:2.99.917+git20171229-1~16.04.1) ...
Setting up amd64-microcode (3.20180524.1~ubuntu0.16.04.2) ...
update-initramfs: deferring update (trigger activated)
amd64-microcode: microcode will be updated at next boot
Setting up libreoffice-common (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Installing new version of config file /etc/bash_completion.d/libreoffice.sh ...
Setting up libreoffice-style-galaxy (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-style-breeze (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-core (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-draw (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-impress (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-ogltrans (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-base-core (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-calc (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-gtk (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-gnome (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up python3-uno (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-pdfimport (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-math (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-avmedia-backend-gstreamer (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-writer (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Processing triggers for desktop-file-utils (0.22-1ubuntu5.2) ...
Processing triggers for bamfdaemon (0.5.3~bzr0+16.04.20180209-0ubuntu1) ...
Rebuilding /usr/share/applications/bamf-2.index...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for initramfs-tools (0.122ubuntu8.11) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-33-generic
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
```
```
dmesg | grep -I kfd
[    2.178948] kfd kfd: Initialized module
[    3.212256] amdgpu 0000:06:00.0: kfd not supported on this ASIC
[    5.116217] amdgpu 0000:23:00.0: kfd not supported on this ASIC
[    6.128280] amdgpu 0000:44:00.0: kfd not supported on this ASIC
[    8.031433] amdgpu 0000:63:00.0: kfd not supported on this ASIC
```

---

### 评论 #5 — jlgreathouse (2018-09-07T18:27:41Z)

Your ROCm install is not being updated because we updated our package signing key last month and you still have the old key cached (#496)

See the error at the bottom of the `apt update` output:
```
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://repo.radeon.com/rocm/apt/debian xenial InRelease: The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360
W: Failed to fetch http://repo.radeon.com/rocm/apt/debian/dists/xenial/InRelease  The following signatures were invalid: KEYEXPIRED 1533155360  KEYEXPIRED 1533155360  KEYEXPIRED 1533155360
W: Some index files failed to download. They have been ignored, or old ones used instead.
```

Please run the following commands to get the new key:
```shell
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
```

Then re-run `sudo apt update; sudo apt dist-upgrade`

---

### 评论 #6 — computingdolas (2018-09-08T10:54:00Z)

It works 👍 

---
