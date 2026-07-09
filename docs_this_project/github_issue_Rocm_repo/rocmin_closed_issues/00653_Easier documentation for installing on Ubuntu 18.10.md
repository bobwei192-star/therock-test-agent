# Easier documentation for installing on Ubuntu 18.10

- **Issue #:** 653
- **State:** closed
- **Created:** 2018-12-31T02:07:35Z
- **Updated:** 2019-01-07T23:53:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/653

I understand that you only support up to Ubuntu 18.04, but Ubuntu 18.10 is the latest version and thus there should be a lot of users. It would be helpful to a lot of users if you just provide some a concise installation note for this specific distribution of Linux.

The current README.md is too complicated and long because it tries to cover lots of versions of lots of distributions. If one has a simple goal of enabling OpenCL on Ubuntu 18.10, the commands that need to be executed should be the same for all Ubuntu 18.10 users.

I have tried to follow the README, but installling rock-dkms caused "Error! Bad return status for module build on kernel: 4.18.0-13-generic (x86_64)" I assumed that this is because this kernel is not supped. So, I have tried the "upstream" way, whatever it is, but when I executed rocminfo, I got "hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104", and for "clinfo", I got, "ERROR: clGetPlatformIDs(-1001)".

As I said before, the instruction is scattered throughout the page so it is not really easy to follow for an average user. I mean, not all users are Linux experts. Could you add some concise, easy-to-follow set of commands for popular OS like Ubuntu 18.10?