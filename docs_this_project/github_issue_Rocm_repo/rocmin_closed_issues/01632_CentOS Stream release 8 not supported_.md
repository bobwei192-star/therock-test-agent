# CentOS Stream release 8 not supported?

- **Issue #:** 1632
- **State:** closed
- **Created:** 2021-12-04T08:59:07Z
- **Updated:** 2023-09-29T15:59:48Z
- **URL:** https://github.com/ROCm/ROCm/issues/1632

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


