# CentOS Stream release 8 not supported?

> **Issue #1632**
> **状态**: closed
> **创建时间**: 2021-12-04T08:59:07Z
> **更新时间**: 2023-09-29T15:59:48Z
> **关闭时间**: 2022-02-09T09:29:45Z
> **作者**: VinInn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1632

## 描述

Hope this is the correct place where to report about this issue.

on
```
uname -m && cat /etc/*release
x86_64
CentOS Stream release 8
NAME="CentOS Stream"
VERSION="8"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="8"
PLATFORM_ID="platform:el8"
PRETTY_NAME="CentOS Stream 8"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:8"
HOME_URL="https://centos.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_SUPPORT_PRODUCT="Red Hat Enterprise Linux 8"
REDHAT_SUPPORT_PRODUCT_VERSION="CentOS Stream"
CentOS Stream release 8
CentOS Stream release 8
```


i get
```
sudo yum install https://repo.radeon.com/amdgpu-install/21.40/rhel/8.4/amdgpu-install-21.40.40500-1.noarch.rpm
AMDGPU 21.40 repository                                                                                                                                                                                                                                                            267  B/s | 178  B     00:00
Errors during downloading metadata for repository 'amdgpu':
  - Status code: 404 for https://repo.radeon.com/amdgpu/21.40/rhel//main/x86_64/repodata/repomd.xml (IP: 13.82.220.49)
Error: Failed to download metadata for repo 'amdgpu': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
```

notice the missing ```8.4```  in the hyperlink after error 404
same with 8.5

Is there any solution/workaround?




---

## 评论 (11 条)

### 评论 #1 — ROCmSupport (2021-12-14T08:42:56Z)

Thanks @VinInn for reaching out.
We will take a look and update asap.

---

### 评论 #2 — ROCmSupport (2021-12-20T08:38:42Z)

Hi @VinInn 
I am not able to reproduce the problem.
Can you please try again and if you still see the issue, please share the exact steps(step by step) to reproduce the problem.
Thank you.

---

### 评论 #3 — VinInn (2021-12-20T09:26:51Z)

Just this 

```
[localadmin@patatrack03 ~]$ sudo yum clean all
[sudo] password for localadmin:
36 files removed
[localadmin@patatrack03 ~]$ sudo yum update
CentOS Stream 8 - CERN                                                                                                                                                                                                 754 kB/s |  48 kB     00:00
CVMFS yum repository for el8                                                                                                                                                                                           465 kB/s |  24 kB     00:00
CentOS Stream 8 - AppStream                                                                                                                                                                                             13 MB/s |  18 MB     00:01
CentOS Stream 8 - BaseOS                                                                                                                                                                                                11 MB/s |  15 MB     00:01
CentOS Stream 8 - Extras                                                                                                                                                                                               607 kB/s |  16 kB     00:00
CentOS Stream 8 - PowerTools                                                                                                                                                                                            85 MB/s | 3.7 MB     00:00
AMDGPU 21.40 repository                                                                                                                                                                                                265  B/s | 178  B     00:00
Errors during downloading metadata for repository 'amdgpu':
  - Status code: 404 for https://repo.radeon.com/amdgpu/21.40/rhel//main/x86_64/repodata/repomd.xml (IP: 13.82.220.49)
Error: Failed to download metadata for repo 'amdgpu': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
```
also
```
[localadmin@patatrack03 ~]$ amdgpu-install
AMDGPU 21.40 repository                                                                                                                                                                                                266  B/s | 178  B     00:00
Errors during downloading metadata for repository 'amdgpu':
  - Status code: 404 for https://repo.radeon.com/amdgpu/21.40/rhel//main/x86_64/repodata/repomd.xml (IP: 13.82.220.49)
Error: Failed to download metadata for repo 'amdgpu': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
```


uname -a
Linux patatrack03 4.18.0-348.2.1.el8_5.x86_64 #1 SMP Tue Nov 16 14:42:35 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux


---

### 评论 #4 — coinserv (2021-12-25T18:10:05Z)

I have the same issue, See below:

[root@Coinserv21]# dnf install https://repo.radeon.com/amdgpu-install/21.40/rhel/8.4/amdgpu-install-21.40.40500-1.noarch.rpm
Last metadata expiration check: 0:01:51 ago on Sat 25 Dec 2021 12:59:53 PM EST.
amdgpu-install-21.40.40500-1.noarch.rpm                                                                                           89 kB/s |  20 kB     00:00
Dependencies resolved.
=================================================================================================================================================================
 Package                               Architecture                  Version                                           Repository                           Size
=================================================================================================================================================================
Installing:
 amdgpu-install                        noarch                        21.40.40500-1334189.el8                           @commandline                         20 k

Transaction Summary
=================================================================================================================================================================
Install  1 Package

Total size: 20 k
Installed size: 30 k
Is this ok [y/N]: y
Downloading Packages:
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                         1/1
  Installing       : amdgpu-install-21.40.40500-1334189.el8.noarch                                                                                           1/1
  Running scriptlet: amdgpu-install-21.40.40500-1334189.el8.noarch                                                                                           1/1
  Verifying        : amdgpu-install-21.40.40500-1334189.el8.noarch                                                                                           1/1
Installed products updated.

Installed:
  amdgpu-install-21.40.40500-1334189.el8.noarch

Complete!
[root@Coinserv21]# dnf clean all
57 files removed
[root@Coinserv21]# dnf update
CentOS Stream 8 - AppStream                                                                                                      3.4 MB/s |  18 MB     00:05
CentOS Stream 8 - BaseOS                                                                                                         5.5 MB/s |  16 MB     00:02
CentOS Stream 8 - Extras                                                                                                          29 kB/s |  16 kB     00:00
AMDGPU 21.40 repository                                                                                                          1.5 kB/s | 178  B     00:00
Errors during downloading metadata for repository 'amdgpu':
  - Status code: 404 for https://repo.radeon.com/amdgpu/21.40/rhel//main/x86_64/repodata/repomd.xml (IP: 13.82.220.49)
Error: Failed to download metadata for repo 'amdgpu': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried


---

### 评论 #5 — brubash (2021-12-31T04:21:16Z)

Me too:
- Status code: 404 for https://repo.radeon.com/amdgpu/21.40.2/rhel//main/x86_64/repodata/repomd.xml (IP: 13.82.220.49)
Error: Failed to download metadata for repo 'amdgpu': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried

---

### 评论 #6 — ROCmSupport (2022-02-09T09:29:45Z)

Hi @VinInn 
I got clarity that you are asking about CentOS Stream 8, not CentOS 8.
Sorry for the confusion.
Currently we are not supporting CentOS stream 8 with ROCm. Please keep track of our documentation for the latest updates.
Thank you.


---

### 评论 #7 — fwyzard (2022-02-16T11:30:12Z)

Hi, here are the instructions to fix the `amdgpu-install` for CentOS 8 Stream, using the RHEL 8.5 repository:
```bash
sudo yum install -y https://repo.radeon.com/amdgpu-install/21.50/rhel/8.5/amdgpu-install-21.50.50000-1.el8.noarch.rpm
sudo sed -e's/$amdgpudistro/8.5/g' -i /etc/yum.repos.d/amdgpu*.repo
```

ROCm and HIP can then be installed as usual:
```bash
sudo amdgpu-install -y --usecase=dkms,rocm,hiplibsdk
```
_or_
```bash
sudo yum install -y amdgpu-dkms rocm-dev rocm-hip-sdk
```

---

### 评论 #8 — fwyzard (2022-02-16T11:32:32Z)

@ROCmSupport

> Currently we are not supporting CentOS stream 8 with ROCm. Please keep track of our documentation for the latest updates.

Maybe you should instead improve the support for your users, while you still have any.


---

### 评论 #9 — Yujif1Aero (2023-05-20T03:42:24Z)

I tried this and $ sudo amdgpu-install --usecase=hiplibsdk,rocm.
After installing finished, I did $rocm-smi but I is not woriking well.
I found an error during $ sudo amdgpu-install --usecase=hiplibsdk,rocm.
The error shows 
Loading new amdgpu-5.18.13-1538762.el8 DKMS files...

Building for 4.18.0-490.el8.x86_64

Building initial module for 4.18.0-490.el8.x86_64

Error! Bad return status for module build on kernel: 4.18.0-490.el8.x86_64 (x86_64)

Consult /var/lib/dkms/amdgpu/5.18.13-1538762.el8/build/make.log for more information.

And I check the make.log
$ cat /var/lib/dkms/amdgpu/5.18.13-1538762.el8/build/make.log

DKMS make.log for amdgpu-5.18.13-1538762.el8 for kernel 4.18.0-490.el8.x86_64 (x86_64) 2023年 5月 19日 金曜日 15:50:29 JST

make: ディレクトリ '/usr/src/kernels/4.18.0-490.el8.x86_64'　に入ります /var/lib/dkms/amdgpu/5.18.13-1538762.el8/build/Makefile:16: *** dma_resv->seq is missing., exit.... 中止.

make: *** [Makefile:1616: _module_/var/lib/dkms/amdgpu/5.18.13-1538762.el8/build] エラー 2 make: ディレクトリ '/usr/src/kernels/4.18.0-490.el8.x86_64' から出ます

Now I am using CentOS8stream and kernel is $ uname -r 4.18.0-490.el8.x86_64


Could you teach me how to fix it?

---

### 评论 #10 — Yujif1Aero (2023-05-20T03:54:49Z)

And when I try installing $sudo amdgpu-install --usecase=dkms, I get a WARNING: amdgpu dkms failed for running kernel

---

### 评论 #11 — VasMan (2023-09-29T15:59:48Z)

> And when I try installing $sudo amdgpu-install --usecase=dkms, I get a WARNING: amdgpu dkms failed for running kernel

I am having the same issue with my CentOS Stream 8 running kernel 4.18.0-514.el8.x86_64 and my Radeon XT550. I get a black screen and can only SSH or remote desktop.

Did you manage to find a way around this or should I send the card back and try to find a different card that works for CentOS Stream 8?

Thank you!
 

---
