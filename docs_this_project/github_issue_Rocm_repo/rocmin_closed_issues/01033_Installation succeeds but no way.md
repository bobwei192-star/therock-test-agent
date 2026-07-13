# Installation succeeds but no way

- **Issue #:** 1033
- **State:** closed
- **Created:** 2020-03-01T13:57:11Z
- **Updated:** 2020-12-01T19:16:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1033

# apt upgrade
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
4 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] y
Setting up linux-headers-4.19.0-8-amd64 (4.19.98-1) ...
/etc/kernel/header_postinst.d/dkms:
Error! Could not locate dkms.conf file.
File: /var/lib/dkms/amdgpu/2.7-27/source/dkms.conf does not exist.
run-parts: /etc/kernel/header_postinst.d/dkms exited with return code 4
Failed to process /etc/kernel/header_postinst.d at /var/lib/dpkg/info/linux-headers-4.19.0-8-amd64.postinst line 11.
dpkg: error processing package linux-headers-4.19.0-8-amd64 (--configure):
 installed linux-headers-4.19.0-8-amd64 package post-installation script subprocess returned error exit status 1
Setting up linux-image-4.19.0-8-amd64 (4.19.98-1) ...
/etc/kernel/postinst.d/dkms:
Error! Could not locate dkms.conf file.
File: /var/lib/dkms/amdgpu/2.7-27/source/dkms.conf does not exist.
run-parts: /etc/kernel/postinst.d/dkms exited with return code 4
dpkg: error processing package linux-image-4.19.0-8-amd64 (--configure):
 installed linux-image-4.19.0-8-amd64 package post-installation script subprocess returned error exit status 1
dpkg: dependency problems prevent configuration of linux-headers-amd64:
 linux-headers-amd64 depends on linux-headers-4.19.0-8-amd64; however:
  Package linux-headers-4.19.0-8-amd64 is not configured yet.

dpkg: error processing package linux-headers-amd64 (--configure):
 dependency problems - leaving unconfigured
dpkg: dependency problems prevent configuration of linux-image-amd64:
 linux-image-amd64 depends on linux-image-4.19.0-8-amd64; however:
  Package linux-image-4.19.0-8-amd64 is not configured yet.

dpkg: error processing package linux-image-amd64 (--configure):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 linux-headers-4.19.0-8-amd64
 linux-image-4.19.0-8-amd64
 linux-headers-amd64
 linux-image-amd64
E: Sub-process /usr/bin/dpkg returned an error code (1)
