# Cannot install HCC deb package on ASROCK

> **Issue #541**
> **状态**: closed
> **创建时间**: 2018-09-16T22:56:26Z
> **更新时间**: 2018-09-17T02:08:24Z
> **关闭时间**: 2018-09-17T00:27:16Z
> **作者**: shimmervoid
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/541

## 描述

I updated to 18.10 and encountered the following error while installing rocm.

Get:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hcc amd64 1.2.18354 [304 MB]
58% [1 hcc 220 MB/304 MB 72%]                                                                                                                                         727 kB/s 1min 55s^Fetched 304 MB in 5min 15s (965 kB/s)
(Reading database ... 132208 files and directories currently installed.)
Preparing to unpack .../hcc_1.2.18354_amd64.deb ...
Unpacking hcc (1.2.18354) ...
dpkg-deb (subprocess): decompressing archive member: internal gzip read error: '<fd:4>: incorrect data check'
dpkg-deb: error: <decompress> subprocess returned error exit status 2
dpkg: error processing archive /var/cache/apt/archives/hcc_1.2.18354_amd64.deb (--unpack):
 cannot copy extracted data for './opt/rocm/hcc/share/scan-view/ScanView.py' to '/opt/rocm/hcc/share/scan-view/ScanView.py.dpkg-new': unexpected end of file or stream
Errors were encountered while processing:
 /var/cache/apt/archives/hcc_1.2.18354_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)

I've tried the following:

apt --fix-broken install 
apt install -f
apt-get clean and reinstalling but i encounter the same error.

System specs:
ASRock x399 | 1950x | Vega Frontier | 4.18.0-7-generic

The same packages were just installed sucessfully on an MSI  x399 rig. 

---

## 评论 (4 条)

### 评论 #1 — jlgreathouse (2018-09-16T23:53:58Z)

I'm unable to reproduce this issue, so I'm wondering if this is a one-time error where the download was corrupted and it has been cached.

Could you show me the output of the following command?
`apt-cache show hcc`

In addition, could you show me:
`ls -alh /var/cache/apt/archives/hcc_1.2.18354_amd64.deb`

If that file is still there, could you run the following and show the output?
`md5sum /var/cache/apt/archives/hcc_1.2.18354_amd64.deb`

---

### 评论 #2 — shimmervoid (2018-09-17T00:27:16Z)

Hello jlgreathouse,

I since purged hip_hcc and rocm-dev and complied hcc from source and copied it to /opt/rocm/
and everything seems to be just dandy.

Here is the output you requested:
root@cr-4:~# apt-cache show hcc
Package: hcc
Version: 1.2.18354
Architecture: amd64
Depends: g++-multilib, gcc-multilib, findutils, libelf1, libpci3, file , hsa-rocr-dev, hsa-ext-rocr-dev, rocm-utils
Installed-Size: 1603732
Maintainer: Siu Chi Chan <siuchi.chan@amd.com>
Priority: optional
Section: devel
Filename: pool/main/h/hcc/hcc_1.2.18354_amd64.deb
Size: 304038538
SHA256: d9cfd6be9b64dd77493d33de553c56236b4848691d44d851990ca0ad094c6c9a
SHA1: 7e7b114ffd6a54c27b4e2b9078537ca7aac1f248
MD5sum: c78f01a145607b5019abe87f1e482959
Description: HCC: An Open Source, Optimizing C++ Compiler for Heterogeneous Compute
Description-md5: 21e1eb128cebd5f6fed1f460126737b5

root@cr-4:~# ls -alh /var/cache/apt/archives/hcc_1.2.18354_amd64.deb
-rw-r--r-- 1 root root 290M Sep 14 16:49 /var/cache/apt/archives/hcc_1.2.18354_amd64.deb

root@cr-4:~# md5sum /var/cache/apt/archives/hcc_1.2.18354_amd64.deb
5c3cd24b19d337432c9275cc8326d823  /var/cache/apt/archives/hcc_1.2.18354_amd64.deb

Maybe it's just this unit.

Thanks.

---

### 评论 #3 — jlgreathouse (2018-09-17T01:01:04Z)

Hi @shimmervoid 

It looks like the .deb file in your apt cache is corrupted. The md5sum for hcc_1.2.18354_amd64.deb should be `c78f01a145607b5019abe87f1e482959`. If you want to still install from .deb, you could try deleting that file and attemping to `apt install` hcc again.

---

### 评论 #4 — shimmervoid (2018-09-17T02:08:24Z)

Good tip to know. Thanks much!

---
