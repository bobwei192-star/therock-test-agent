# Versioned deb packages should use `Conflicts` with non-versioned ones. Or `Provides`.

- **Issue #:** 1134
- **State:** closed
- **Created:** 2020-06-06T18:12:48Z
- **Updated:** 2023-12-23T18:07:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/1134

```
root@debian:~# apt install rocm-opencl3.5.0 -V
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
   comgr3.5.0 (1.6.0.143-rocm-rel-3.5-30-e24e8c1)
   hsa-ext-rocr-dev3.5.0 (1.1.30500.0-rocm-rel-3.5-30-def83d8)
   hsa-rocr-dev3.5.0 (1.1.30500.0-rocm-rel-3.5-30-def83d8)
   hsakmt-roct3.5.0 (1.0.9-347-gd4b224f)
The following NEW packages will be installed:
   comgr3.5.0 (1.6.0.143-rocm-rel-3.5-30-e24e8c1)
   hsa-ext-rocr-dev3.5.0 (1.1.30500.0-rocm-rel-3.5-30-def83d8)
   hsa-rocr-dev3.5.0 (1.1.30500.0-rocm-rel-3.5-30-def83d8)
   hsakmt-roct3.5.0 (1.0.9-347-gd4b224f)
   rocm-opencl3.5.0 (2.0.20191)
0 upgraded, 5 newly installed, 0 to remove and 40 not upgraded.
Need to get 30.5 MB of archives.
After this operation, 359 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
Get:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 comgr3.5.0 amd64 1.6.0.143-rocm-rel-3.5-30-e24e8c1 [29.5 MB]
Get:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct3.5.0 amd64 1.0.9-347-gd4b224f [55.8 kB]  
Get:3 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-rocr-dev3.5.0 amd64 1.1.30500.0-rocm-rel-3.5-30-def83d8 [337 kB]
Get:4 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-ext-rocr-dev3.5.0 amd64 1.1.30500.0-rocm-rel-3.5-30-def83d8 [174 kB]
Get:5 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl3.5.0 amd64 2.0.20191 [414 kB]            
Fetched 30.5 MB in 49s (627 kB/s)                                                                                   
Selecting previously unselected package comgr3.5.0.
(Reading database ... 484153 files and directories currently installed.)
Preparing to unpack .../comgr3.5.0_1.6.0.143-rocm-rel-3.5-30-e24e8c1_amd64.deb ...
Unpacking comgr3.5.0 (1.6.0.143-rocm-rel-3.5-30-e24e8c1) ...
dpkg: error processing archive /var/cache/apt/archives/comgr3.5.0_1.6.0.143-rocm-rel-3.5-30-e24e8c1_amd64.deb (--unpa
ck):
 trying to overwrite '/opt/rocm-3.5.0/include/amd_comgr.h', which is also in package comgr 1.6.0.143-rocm-rel-3.5-30-
e24e8c1
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Selecting previously unselected package hsakmt-roct3.5.0.
Preparing to unpack .../hsakmt-roct3.5.0_1.0.9-347-gd4b224f_amd64.deb ...
Unpacking hsakmt-roct3.5.0 (1.0.9-347-gd4b224f) ...
dpkg: error processing archive /var/cache/apt/archives/hsakmt-roct3.5.0_1.0.9-347-gd4b224f_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm-3.5.0/lib/libhsakmt.so.1.0.30500', which is also in package hsakmt-roct 1.0.9-347-gd4
b224f
Selecting previously unselected package hsa-rocr-dev3.5.0.
Preparing to unpack .../hsa-rocr-dev3.5.0_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd64.deb ...
Unpacking hsa-rocr-dev3.5.0 (1.1.30500.0-rocm-rel-3.5-30-def83d8) ...
dpkg: error processing archive /var/cache/apt/archives/hsa-rocr-dev3.5.0_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd64.de
b (--unpack):
 trying to overwrite '/opt/rocm-3.5.0/hsa/include/hsa/Brig.h', which is also in package hsa-rocr-dev 1.1.30500.0-rocm
-rel-3.5-30-def83d8
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Selecting previously unselected package hsa-ext-rocr-dev3.5.0.
Preparing to unpack .../hsa-ext-rocr-dev3.5.0_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd64.deb ...
Unpacking hsa-ext-rocr-dev3.5.0 (1.1.30500.0-rocm-rel-3.5-30-def83d8) ...
dpkg: error processing archive /var/cache/apt/archives/hsa-ext-rocr-dev3.5.0_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd6
4.deb (--unpack):
 trying to overwrite '/opt/rocm-3.5.0/hsa/lib/libhsa-ext-image64.so.1.1.30500', which is also in package hsa-ext-rocr
-dev 1.1.30500.0-rocm-rel-3.5-30-def83d8
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Selecting previously unselected package rocm-opencl3.5.0.
Preparing to unpack .../rocm-opencl3.5.0_2.0.20191_amd64.deb ...
Unpacking rocm-opencl3.5.0 (2.0.20191) ...
dpkg: error processing archive /var/cache/apt/archives/rocm-opencl3.5.0_2.0.20191_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm-3.5.0/opencl/bin/clinfo', which is also in package rocm-opencl 2.0.20191
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/comgr3.5.0_1.6.0.143-rocm-rel-3.5-30-e24e8c1_amd64.deb
 /var/cache/apt/archives/hsakmt-roct3.5.0_1.0.9-347-gd4b224f_amd64.deb
 /var/cache/apt/archives/hsa-rocr-dev3.5.0_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd64.deb
 /var/cache/apt/archives/hsa-ext-rocr-dev3.5.0_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd64.deb
 /var/cache/apt/archives/rocm-opencl3.5.0_2.0.20191_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
root@debian:~# 

```


This is simply wrong.

The proper solution is to make:

1) Make them conflict with non-versioned packages.

Or EVEN BETTER:

2) Non-versioned package, should just be metapackages, that depend on the latest stable version of versioned-package. This way there is no way to conflict, and updats + preserving of old version on updates is guranteed. This is a recommended methods, and is used in Debian and Ubuntu extensivly for things like versioned GCC compilers and libraries, versioned LLVM libraries, linux kernel images, linux-perf, golang compilers, php environment, and many more. This is usually done using Metapackage that depend on the latest version, and each version using `Provide` fields, so they can be also installed individually.

Examples:

```
# apt-cache show g++ | egrep 'Package|Depends'
Package: g++
Depends: cpp (= 4:10-1), gcc (= 4:10-1), g++-10 (>= 10-20191205-1~), gcc-10 (>= 10-20191205-1~)
Package: g++
Depends: cpp (= 4:9.2.1-3.1), gcc (= 4:9.2.1-3.1), g++-9 (>= 9.2.1-1~), gcc-9 (>= 9.2.1-1~)
# apt-cache show g++-10 | egrep 'Package|Depends|Provides'
Package: g++-10
Provides: c++-compiler, c++abi2-dev
Depends: gcc-10-base (= 10.1.0-3), gcc-10 (= 10.1.0-3), libstdc++-10-dev (= 10.1.0-3), libc6 (>= 2.14), libgmp10 (>= 2:5.0.1~), libisl22 (>= 0.15), libmpc3, libmpfr6 (>= 3.1.3), libzstd1 (>= 1.3.2), zlib1g (>= 1:1.1.4)
# 
```


```
# apt-cache show php | egrep 'Package|Depends'
Package: php
Depends: php7.4
# apt-cache show php7.4 | egrep 'Package|Depends|Provides'
Package: php7.4
Provides: php
Depends: libapache2-mod-php7.4 | php7.4-fpm | php7.4-cgi, php7.4-common
#
```

```
# apt-cache show nvidia-driver | egrep 'Provides|Depends|Pre-Depends|Suggests|Recommends'
Provides: nvidia-driver-any, nvidia-glx-any
Depends: nvidia-driver-libs (= 440.82-2), nvidia-driver-bin (= 440.82-2), xserver-xorg-video-nvidia (= 440.82-2), nvidia-vdpau-driver (= 440.82-2), nvidia-alternative (= 440.82-2), nvidia-kernel-dkms (= 440.82-2) | nvidia-kernel-440.82, nvidia-support
Pre-Depends: nvidia-installer-cleanup, nvidia-legacy-check (>= 396)
Recommends: nvidia-settings (>= 440), libnvidia-cfg1 (= 440.82-2), nvidia-persistenced
Suggests: nvidia-kernel-dkms (>= 440.82) | nvidia-kernel-source (>= 440.82)
# apt-cache show nvidia-driver-bin | egrep 'Provides|Depends|Pre-Depends|Suggests|Recommends'
Provides: nvidia-driver-bin-440.82
Depends: nvidia-alternative (= 440.82-2), libc6 (>= 2.2.5), libnvidia-ml1 (>= 319) | libnvidia-ml.so.1 (>= 319)
Recommends: nvidia-driver
#
```

Please see sections 7.2, 7.4 and 7.5 of Debian Policy Manual.


Implementing meta-package and `Provides` is definitively better long term. To implement it and make upgrades from existing (broken) packages painless, you would also need to use `Replaces` with proper version inequality, to make this work nice. See sections 7.3 and 7.6 of Debian Policy Manual.