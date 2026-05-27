# uname -a reports non-kfd driver

> **Issue #290**
> **状态**: closed
> **创建时间**: 2017-12-28T05:10:23Z
> **更新时间**: 2017-12-28T18:50:45Z
> **关闭时间**: 2017-12-28T18:50:45Z
> **作者**: amansinha-sw
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/290

## 描述

I have recently installed rocm-1.7. I tried the HelloWorld sample after that and the run was successful. I have updated the GRUB_DEFAULT variable too and have run update-grub. But when I do uname -a, I am getting the below:
dnnroot@ubuntu:~$ uname -a
Linux ubuntu 4.4.0-104-generic #127-Ubuntu SMP Mon Dec 11 12:16:42 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

The above issue is not allowing me to run tests on HipCaffe Docker image, where the output while trying to train AlexNet is as below:
root@7eaaf0c1a5a0:/home/rocm-user# script -c "caffe train -solver=/Netinfo/AlexNet/solver.prototxt -gpu 0" /Data/Testing/HPE_P100_1.txt
Script started, file is /Data/Testing/HPE_P100_1.txt
I1228 04:53:44.488523    29 caffe.cpp:217] Using GPUs 0
There is no device can be used to do the computation
Script done, file is /Data/Testing/HPE_P100_1.txt

But when I run rocm-smi, I get the following output:
root@7eaaf0c1a5a0:/opt/rocm/bin# ./rocm-smi


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  0   687f   52.0c    N/A      852Mhz   500Mhz   12.94%   auto      0%       N/A
  1   67ef   42.0c    N/A      214Mhz   1750Mhz  13.73%   auto      0%       N/A
================================================================================
====================           End of ROCm SMI Log          ====================

Please suggest why "uname -a" is not reporting "4.11.0-kfd-compute-rocm-rel" as it used to report on rocm-1.6. This issue is not allowing me to run HipCaffe properly.

---

## 评论 (4 条)

### 评论 #1 — gstoner (2017-12-28T05:16:27Z)

With 1.7 we moved to DKMS install not  replacing the linux kernel with the 4.11 linux kernel like with 1.6.4.   So we us the standard  Ubuntu Linux kernel for 16.04 aka ubuntu 4.4.0-104-generic to install the driver, so this  correct.   






---

### 评论 #2 — gstoner (2017-12-28T05:18:27Z)

One thing you need to intstall the base kernel driver before running Docker,  also all docker container using 1.7 need  ROCT aka thunk update. With the current ROCr runtime API and tools 





---

### 评论 #3 — amansinha-sw (2017-12-28T08:46:53Z)

I am sorry, I am not sure if you refer to the AMPGPU-PRO drivers for "base kernel driver". Please confirm.

---

### 评论 #4 — gstoner (2017-12-28T18:46:44Z)

NO we do not support the AMDGPU pro driver in this repository.  This is only for the ROCm opensource driver 

---
