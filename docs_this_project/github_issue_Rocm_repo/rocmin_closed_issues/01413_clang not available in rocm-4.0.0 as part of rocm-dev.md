# clang not available in rocm-4.0.0 as part of rocm-dev

- **Issue #:** 1413
- **State:** closed
- **Created:** 2021-03-21T08:51:31Z
- **Updated:** 2021-03-22T08:47:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/1413

Hello

I installed rocm-dev  as below:

_$ sudo yum install rocm-dev_

The install was successful. 
_[ec2-user@ip-172-31-35-60 llvm]$ sudo yum list installed | grep rocm-dev
rocm-dev.x86_64                 4.0.0.40000-23.el7             @ROCm            
rocm-device-libs.x86_64         1.0.0.637_rocm_rel_4.0_23_db8c0c3-1_

I want to build and run the veccopy example program.
However, clang which is required for this, is not available as part of the rocm-4.0.0 package.

_[ec2-user@ip-172-31-35-60 llvm]$ pwd
/opt/rocm-4.0.0/llvm
[ec2-user@ip-172-31-35-60 llvm]$ ls -l bin/
total 6120
-rwxr-xr-x 1 root root 4077712 Dec 14 11:19 flang1
-rwxr-xr-x 1 root root 2186696 Dec 14 11:19 flang2_

What do I need to do in order to install clang? 
This issue is not seen with rock-dkms or AOMP however, I can not install any of them since I want only the userspace code for rocm.

Thanks
Rajarshi Das