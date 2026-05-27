# clinfo failure

> **Issue #185**
> **状态**: closed
> **创建时间**: 2017-08-23T00:49:48Z
> **更新时间**: 2018-01-18T18:18:16Z
> **关闭时间**: 2017-08-24T21:07:42Z
> **作者**: kiritigowda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/185

## 描述

After successful installation of apt-get rocm-opencl-dev, clinfo fails with Vega and intel i7 on Ubuntu 16.04. 
./clinfo 
terminate called after throwing an instance of 'cl::Error'
what():  clGetPlatformIDs
Aborted (core dumped)

Any resolutions or did I miss any step?

Thanks!


---

## 评论 (15 条)

### 评论 #1 — gstoner (2017-08-24T01:44:39Z)

We just rolled out ROCm 1.6.3 can you try this. 

---

### 评论 #2 — kiritigowda (2017-08-24T16:34:40Z)

I installed the latest update using apt-get on a fresh ubuntu 16.04, but the clinfo fails. Attached is the stack trace; any thing I am not doing right?
![stack_trace](https://user-images.githubusercontent.com/16549273/29677278-71ffd9fc-88af-11e7-8171-6c7ec37a6651.png)
 

---

### 评论 #3 — gstoner (2017-08-24T17:04:34Z)

When you installed ROCm did you follow these instructions https://rocm.github.io/ROCmInstall.html

---

### 评论 #4 — gstoner (2017-08-24T17:04:54Z)

I can not tell from this is Kernel driver is loaded and running 

---

### 评论 #5 — kiritigowda (2017-08-24T17:12:10Z)

Yes, I followed all the instructions and here are my systems info and kfd.

lspci | grep -i AMD
01:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470 (rev c1)
02:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8

uname -m && cat /etc/*release
x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.3 LTS"
NAME="Ubuntu"
VERSION="16.04.3 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.3 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial

gcc --version 
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609

uname -r
4.11.0-kfd-compute-rocm-rel-1.6-127


---

### 评论 #6 — kiritigowda (2017-08-24T17:45:52Z)

Here is the error I get when I try to verify install

./vector_copy 
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent failed.


---

### 评论 #7 — gstoner (2017-08-24T17:55:09Z)

Do this first  
Uninstall the a Package
•	Ubuntu
•	sudo apt-get purge libhsakmt
•	sudo apt-get purge radeon-firmware
•	sudo apt-get purge $(dpkg -l | grep 'kfd\|rocm' | grep linux | grep -v libc | awk '{print $2}')


Then do this 

Ubuntu Install
Add the Repo Server

For Debian based systems, like Ubuntu, configure the Debian ROCm repository as follows:

wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'

The gpg key might change, so it may need to be updated when installing a new release. The current rocm.gpg.key is not avialable in a standard key ring distribution, but has the following sha1sum hash:
f0d739836a9094004b0a39058d046349aacc1178 rocm.gpg.key

Install or update ROCm

sudo apt-get update
sudo apt-get install rocm rocm-opencl-dev

Then, make the ROCm kernel your default kernel. If using grub2 as your bootloader, you can edit the GRUB_DEFAULT variable in the following file:

sudo nano /etc/default/grub

set the GRUB_Default Edit: GRUB_DEFAULT=”Advanced options for Ubuntu>Ubuntu, with Linux 4.11.0-kfd-compute-rocm-rel-1.6-148”
sudo update-grub

uname -r
4.11.0-kfd-compute-rocm-rel-1.6-148


---

### 评论 #8 — kiritigowda (2017-08-24T19:02:42Z)

Hi Greg, followed all the above steps and I still get this error
![clinfo-failure](https://user-images.githubusercontent.com/16549273/29683705-1e118de4-88c4-11e7-9198-d1d8ef25b339.png)


---

### 评论 #9 — gstoner (2017-08-24T19:28:49Z)

We have to see if we can replicate this,  we use Ubuntu 16.04.2 server primarily. With out issue. There maybe something in Ubuntu 16.04.3,  I am seeing it complaining about the libPCIe3, and libudev1

Also, can you just paste the text in the future not an image 

One thing can you open terminal go to /opt/rocm/opencl 

Also did you apt-get install clinfo.   We install clinfo part of the package install  You should not be doing this.   You will find it here /opt/rocm/opencl/bin/x86_64. run this version. 

You can also test the ROCm with compiling hipinfo in /opt/rocm/hip/samples/1_Utils/hipInfo

greg

---

### 评论 #10 — kiritigowda (2017-08-24T19:52:00Z)

I did not install apt-get install clinfo, I am using the clinfo in the bin folder from /opt/rocm/opencl/.

I tried compiling the example, it also gives the following error.
sudo make
[sudo] password for kiriti: 
/opt/rocm/hip/bin/hipcc hipInfo.cpp -o hipInfo
Can't exec "/usr/local/cuda/bin/nvcc": No such file or directory at /opt/rocm/hip/bin/hipcc line 474.
Died at /opt/rocm/hip/bin/hipcc line 474.
Makefile:12: recipe for target 'hipInfo' failed
make: *** [hipInfo] Error 2

Thanks for your help, and please let me know if you find any resolution for this issue.
  

---

### 评论 #11 — kiritigowda (2017-08-24T20:02:15Z)

Posting the stack trace for reference.
/opt/rocm/opencl/bin/x86_64$ valgrind --leak-check=full --track-origins=yes  ./clinfo 
==3163== Memcheck, a memory error detector
==3163== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==3163== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==3163== Command: ./clinfo
==3163== 
==3163== Syscall param ioctl(generic) points to uninitialised byte(s)
==3163==    at 0x5C85F07: ioctl (syscall-template.S:84)
==3163==    by 0x9B9B8A7: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.6)
==3163==    by 0x9B9F6CA: hsaKmtGetClockCounters (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.6)
==3163==    by 0x993282D: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==3163==    by 0x991E7F0: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==3163==    by 0x991E883: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==3163==    by 0x9930E7D: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==3163==    by 0x6787F0C: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x675B9C2: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x67786A6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x6744601: clIcdGetPlatformIDsKHR (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x555176D: ??? (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==3163==  Address 0xffeffe700 is on thread 1's stack
==3163==  in frame #2, created by hsaKmtGetClockCounters (???:)
==3163==  Uninitialised value was created by a stack allocation
==3163==    at 0x990A7B0: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==3163== 
==3163== Invalid read of size 8
==3163==    at 0x67884E6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x675B9C2: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x67786A6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x6744601: clIcdGetPlatformIDsKHR (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x555176D: ??? (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==3163==    by 0x5553646: ??? (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==3163==    by 0x597AA98: __pthread_once_slow (pthread_once.c:116)
==3163==    by 0x5551D30: clGetPlatformIDs (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==3163==    by 0x40F686: ??? (in /opt/rocm/opencl/bin/x86_64/clinfo)
==3163==    by 0x407C11: ??? (in /opt/rocm/opencl/bin/x86_64/clinfo)
==3163==    by 0x5BA982F: (below main) (libc-start.c:291)
==3163==  Address 0x8 is not stack'd, malloc'd or (recently) free'd
==3163== 
==3163== 
==3163== Process terminating with default action of signal 11 (SIGSEGV)
==3163==  Access not within mapped region at address 0x8
==3163==    at 0x67884E6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x675B9C2: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x67786A6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x6744601: clIcdGetPlatformIDsKHR (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==3163==    by 0x555176D: ??? (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==3163==    by 0x5553646: ??? (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==3163==    by 0x597AA98: __pthread_once_slow (pthread_once.c:116)
==3163==    by 0x5551D30: clGetPlatformIDs (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==3163==    by 0x40F686: ??? (in /opt/rocm/opencl/bin/x86_64/clinfo)
==3163==    by 0x407C11: ??? (in /opt/rocm/opencl/bin/x86_64/clinfo)
==3163==    by 0x5BA982F: (below main) (libc-start.c:291)
==3163==  If you believe this happened as a result of a stack
==3163==  overflow in your program's main thread (unlikely but
==3163==  possible), you can try to increase the size of the
==3163==  main thread stack using the --main-stacksize= flag.
==3163==  The main thread stack size used in this run was 8388608.
==3163== 
==3163== HEAP SUMMARY:
==3163==     in use at exit: 236,794 bytes in 1,076 blocks
==3163==   total heap usage: 1,414 allocs, 338 frees, 476,734 bytes allocated
==3163== 
==3163== LEAK SUMMARY:
==3163==    definitely lost: 0 bytes in 0 blocks
==3163==    indirectly lost: 0 bytes in 0 blocks
==3163==      possibly lost: 0 bytes in 0 blocks
==3163==    still reachable: 236,794 bytes in 1,076 blocks
==3163==                       of which reachable via heuristic:
==3163==                         stdstring          : 410 bytes in 10 blocks
==3163==         suppressed: 0 bytes in 0 blocks
==3163== Reachable blocks (those to which a pointer was found) are not shown.
==3163== To see them, rerun with: --leak-check=full --show-leak-kinds=all
==3163== 
==3163== For counts of detected and suppressed errors, rerun with: -v
==3163== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)

==2319== 1 errors in context 1 of 2:
==2319== Invalid read of size 8
==2319==    at 0x67884E6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==2319==    by 0x675B9C2: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==2319==    by 0x67786A6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==2319==    by 0x6744601: clIcdGetPlatformIDsKHR (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==2319==    by 0x555176D: ??? (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==2319==    by 0x5553646: ??? (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==2319==    by 0x597AA98: __pthread_once_slow (pthread_once.c:116)
==2319==    by 0x5551D30: clGetPlatformIDs (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==2319==    by 0x40F686: ??? (in /opt/rocm/opencl/bin/x86_64/clinfo)
==2319==    by 0x407C11: ??? (in /opt/rocm/opencl/bin/x86_64/clinfo)
==2319==    by 0x5BA982F: (below main) (libc-start.c:291)
==2319==  Address 0x8 is not stack'd, malloc'd or (recently) free'd
==2319== 
==2319== 
==2319== 1 errors in context 2 of 2:
**==2319== Syscall param ioctl(generic) points to uninitialised byte(s)
==2319==    at 0x5C85F07: ioctl (syscall-template.S:84)
==2319==    by 0x9B9B8A7: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.6)
==2319==    by 0x9B9F6CA: hsaKmtGetClockCounters (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.6)
==2319==    by 0x993282D: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==2319==    by 0x991E7F0: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==2319==    by 0x991E883: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==2319==    by 0x9930E7D: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.6)
==2319==    by 0x6787F0C: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==2319==    by 0x675B9C2: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==2319==    by 0x67786A6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==2319==    by 0x6744601: clIcdGetPlatformIDsKHR (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==2319==    by 0x555176D: ??? (in /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1)
==2319==  Address 0xffeffe700 is on thread 1's stack
==2319==  in frame #2, created by hsaKmtGetClockCounters (???:)**


Segmentation fault (core dumped)


---

### 评论 #12 — gstoner (2017-08-24T21:07:42Z)

I want to thank you for testing our release Ubuntu 16.04.3 this is unsupported distro release currently just like it is with AMDGPUpro driver.   The release was tested with 16.04.2 

---

### 评论 #13 — kiritigowda (2017-08-25T19:50:55Z)

Just to update on this issue, I got it running by updating the GPU BIOS.

---

### 评论 #14 — gstoner (2017-08-25T20:09:38Z)

Thanks.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: kiritigowda <notifications@github.com>
Sent: Friday, August 25, 2017 12:50:56 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; State change
Subject: Re: [RadeonOpenCompute/ROCm] clinfo failure (#185)


Just to update on this issue, I got it running by updating the GPU BIOS.

—
You are receiving this because you modified the open/close state.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/185#issuecomment-325019555>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuauAXHzf3wfJGK0NAA2xl1Vy0_ROks5sbyWggaJpZM4O_Wwy>.


---

### 评论 #15 — Yougmark (2018-01-18T18:18:16Z)

@kiritigowda  Could you post how did you update GPU BIOS and solve the problem? I'm having similar issues. Thanks!

---
