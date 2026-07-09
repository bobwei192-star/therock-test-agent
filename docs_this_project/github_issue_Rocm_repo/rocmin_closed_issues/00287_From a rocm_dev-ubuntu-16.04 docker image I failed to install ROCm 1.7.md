# From a rocm/dev-ubuntu-16.04 docker image I failed to install ROCm 1.7

- **Issue #:** 287
- **State:** closed
- **Created:** 2017-12-27T00:31:19Z
- **Updated:** 2017-12-27T15:36:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/287

Trying to install according to [ROCm install page](https://rocm.github.io/ROCmInstall.html). I'm using docker with "rocm/dev-ubuntu-16.04" image. 

Getting errors at command "apt dist-upgrade" from "Pre Install Directions" section:

root@ef7acb3e674d:/# apt update
Get:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
Get:3 http://repo.radeon.com/rocm/apt/debian xenial InRelease [1814 B]
Get:4 http://security.ubuntu.com/ubuntu xenial-security/universe Sources [56.7 kB]
Get:5 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages [5765 B]
Get:6 http://archive.ubuntu.com/ubuntu xenial-updates InRelease [102 kB]
Get:7 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [521 kB]
Get:8 http://archive.ubuntu.com/ubuntu xenial-backports InRelease [102 kB]
Get:9 http://archive.ubuntu.com/ubuntu xenial/universe Sources [9802 kB]
Get:10 http://security.ubuntu.com/ubuntu xenial-security/restricted amd64 Packages [12.9 kB]
Get:11 http://security.ubuntu.com/ubuntu xenial-security/universe amd64 Packages [239 kB]
Get:12 http://security.ubuntu.com/ubuntu xenial-security/multiverse amd64 Packages [3481 B]
Get:13 http://archive.ubuntu.com/ubuntu xenial/main amd64 Packages [1558 kB]
Get:14 http://archive.ubuntu.com/ubuntu xenial/restricted amd64 Packages [14.1 kB]
Get:15 http://archive.ubuntu.com/ubuntu xenial/universe amd64 Packages [9827 kB]
Get:16 http://archive.ubuntu.com/ubuntu xenial/multiverse amd64 Packages [176 kB]
Get:17 http://archive.ubuntu.com/ubuntu xenial-updates/universe Sources [233 kB]
Get:18 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [882 kB]
Get:19 http://archive.ubuntu.com/ubuntu xenial-updates/restricted amd64 Packages [13.7 kB]
Get:20 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [726 kB]
Get:21 http://archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 Packages [18.5 kB]
Get:22 http://archive.ubuntu.com/ubuntu xenial-backports/main amd64 Packages [5162 B]
Get:23 http://archive.ubuntu.com/ubuntu xenial-backports/universe amd64 Packages [7146 B]
Fetched 24.7 MB in 24s (1023 kB/s)
Reading package lists... Done
Building dependency tree
Reading state information... Done
27 packages can be upgraded. Run 'apt list --upgradable' to see them.
**root@ef7acb3e674d:/# apt dist-upgrade**
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following packages were automatically installed and are no longer required:
  cxlactivitylogger rocm-profiler
Use 'apt autoremove' to remove them.
The following NEW packages will be installed:
  hsa-amd-aqlprofile hsakmt-roct rocm-clang-ocl rocm-opencl rocm-opencl-dev rocminfo
The following packages will be upgraded:
  curl cxlactivitylogger dpkg hcc hip_base hip_doc hip_hcc hip_samples hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct-dev
  libcurl3-gnutls libdb5.3 libperl5.22 libsystemd0 libudev1 linux-libc-dev perl perl-base perl-modules-5.22 rocm-dev
  rocm-device-libs rocm-profiler rocm-smi rocm-utils systemd systemd-sysv
27 upgraded, 6 newly installed, 0 to remove and 0 not upgraded.
Need to get 372 MB of archives.
After this operation, 344 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 dpkg amd64 1.18.4ubuntu1.3 [2084 kB]
Selecting previously unselected package rocm-clang-ocl.
Preparing to unpack .../rocm-clang-ocl_0.2.0-83527dd_amd64.deb ...
Unpacking rocm-clang-ocl (0.2.0-83527dd) ...
dpkg: error processing archive /var/cache/apt/archives/rocm-clang-ocl_0.2.0-83527dd_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm/bin/clang-ocl', which is also in package rocm-utils 1.0.0
Preparing to unpack .../rocm-utils_1.7.60_amd64.deb ...
Unpacking rocm-utils (1.7.60) over (1.0.0) ...
Preparing to unpack .../hip%5fdoc_1.4.17494_amd64.deb ...
Unpacking hip_doc (1.4.17494) over (1.3.17385) ...
Preparing to unpack .../hip%5fhcc_1.4.17494_amd64.deb ...
Unpacking hip_hcc (1.4.17494) over (1.3.17385) ...
Preparing to unpack .../hip%5fsamples_1.4.17494_amd64.deb ...
Unpacking hip_samples (1.4.17494) over (1.3.17385) ...
Preparing to unpack .../hip%5fbase_1.4.17494_amd64.deb ...
Unpacking hip_base (1.4.17494) over (1.3.17385) ...
Preparing to unpack .../rocm-smi_1.0.0-34-g23012d0_amd64.deb ...
Unpacking rocm-smi (1.0.0-34-g23012d0) over (1.0.0-25-gbdb99b4) ...
Selecting previously unselected package hsa-amd-aqlprofile.
Preparing to unpack .../hsa-amd-aqlprofile_1.0.0_amd64.deb ...
Unpacking hsa-amd-aqlprofile (1.0.0) ...
Preparing to unpack .../hcc_1.1.17493_amd64.deb ...
Unpacking hcc (1.1.17493) over (1.0.17412) ...
Preparing to unpack .../linux-libc-dev_4.4.0-104.127_amd64.deb ...
Unpacking linux-libc-dev:amd64 (4.4.0-104.127) over (4.4.0-98.121) ...
Preparing to unpack .../cxlactivitylogger_5.3.6652_amd64.deb ...
Unpacking cxlactivitylogger (5.3.6652) over (5.3.6544) ...
Preparing to unpack .../rocm-profiler_5.3.6652_amd64.deb ...
Unpacking rocm-profiler (5.3.6652) over (5.2.6552) ...
Processing triggers for libc-bin (2.23-0ubuntu9) ...
Errors were encountered while processing:
 /var/cache/apt/archives/hsakmt-roct_1.0.7-3-g19be283_amd64.deb
 /var/cache/apt/archives/rocminfo_1.0.7_amd64.deb
 /var/cache/apt/archives/rocm-clang-ocl_0.2.0-83527dd_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)

 /var/cache/apt/archives/rocm-clang-ocl_0.2.0-83527dd_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)

