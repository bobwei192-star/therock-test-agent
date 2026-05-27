# Radeon VII problem on ROCm 2.6

> **Issue #843**
> **状态**: closed
> **创建时间**: 2019-07-11T10:06:46Z
> **更新时间**: 2019-10-05T19:29:20Z
> **关闭时间**: 2019-09-12T08:33:53Z
> **作者**: heero-yuy
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/843

## 描述

Hi, 

Installed Ubuntu 18.04.2 with kernel 4.15.0-54 with ROCm 2.6 installed, found the computing feature can't be set successfully, what's problem going on?

test@test:~/rvs/build/bin$ sudo /opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2924.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
test@test:~/rvs/build/bin$ sudo /opt/rocm/bin/rocm-smi


========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK    MCLK    Fan   Perf  PwrCap  VRAM%  GPU%  
1    35.0c  17.0W   931Mhz  351Mhz  0.0%  auto  225.0W    0%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================
test@test:~/rvs/build/bin$ ./rvs -g

ROCm Validation Suite (version 0.0.32)

Supported GPUs available:
20:00.0 - GPU[ 2 -  2996] Vega 20 (Device 26273)
test@test-G481-HA0-00:~/rvs/build/bin$ ./rvs -d 5 -c conf/gst_1.conf 
[DEBUG ] [  1968.962527] property: [name]   val:[action_1]
[DEBUG ] [  1968.962549] property: [device]   val:[26273]
[DEBUG ] [  1968.962555] property: [module]   val:[gst]
[DEBUG ] [  1968.962559] property: [parallel]   val:[false]
[DEBUG ] [  1968.962563] property: [count]   val:[2]
[DEBUG ] [  1968.962567] property: [wait]   val:[100]
[DEBUG ] [  1968.962571] property: [duration]   val:[18000]
[DEBUG ] [  1968.962575] property: [ramp_interval]   val:[7000]
[DEBUG ] [  1968.962580] property: [log_interval]   val:[1000]
[DEBUG ] [  1968.962584] property: [max_violations]   val:[1]
[DEBUG ] [  1968.962590] property: [copy_matrix]   val:[false]
[DEBUG ] [  1968.962594] property: [target_stress]   val:[5000]
[DEBUG ] [  1968.962599] property: [tolerance]   val:[0.07]
[DEBUG ] [  1968.962605] property: [matrix_size]   val:[5760]
[DEBUG ] [  1968.962609] property: [cli.-c]   val:[conf/gst_1.conf]
[DEBUG ] [  1968.962612] property: [cli.-d]   val:[5]
[DEBUG ] [  1968.962614] property: [cli.pwd]   val:[/home/test/rvs/build/bin/]
GPU device 0 doesn't not exist

Aborted (core dumped)


---

## 评论 (10 条)

### 评论 #1 — smartbitcoin (2019-07-11T21:16:44Z)

do you put your user inside video group ? 

---

### 评论 #2 — heero-yuy (2019-07-12T01:04:38Z)

Thanks, I've checked as following:

test@test:~$ groups
test adm cdrom sudo dip video plugdev lpadmin sambashare
test@test~$ groups test
test : test adm cdrom sudo dip video plugdev lpadmin sambashare

I'll reinstall the Ubuntu 18.04.2 with default kernel to check, thanks!


---

### 评论 #3 — heero-yuy (2019-07-12T04:32:16Z)

Checked the CentOS 7.6.1810 (without updated Kernel) & Ubuntu 18.04.2 with kernel 4.15.0-45 has the same problem, I'll check the older version of ROCm can cause this.

---

### 评论 #4 — heero-yuy (2019-07-15T02:54:57Z)

Hi All,

After checked with some HW parts, found the newer generation of CPU cause this (I used Intel Xeon Silver 4214), the older generation of CPU (HSW-EP/BDW-EP) didn't cause this, need wait for fixed , thanks!

---

### 评论 #5 — yejunjin (2019-07-18T05:32:10Z)

AMD developers will not give you any help. It seems they almost give up ROCm.

---

### 评论 #6 — kentrussell (2019-07-25T15:09:41Z)

If you run rocrtst, does that pass, or does it fail like clinfo? Just trying to narrow down where the issue lies. The SMI indicates that the kernel and DPM are working. There is also kfdtest which tests kernel functionality, as part of the ROCT project. Figuring out if it's a ROCK or ROCT or ROCR or OpenCL issue will help to get it addressed

---

### 评论 #7 — heero-yuy (2019-07-26T09:42:39Z)

Hi  kentrussell,

Thanks,  both them has failed during testing, but rocm-smi is workable, the clinfo still fail.

But when I use older generation of CPU, the problem is gone...

[rsmitst.txt](https://github.com/RadeonOpenCompute/ROCm/files/3435177/rsmitst.txt)
[kfdtest.txt](https://github.com/RadeonOpenCompute/ROCm/files/3435179/kfdtest.txt)



---

### 评论 #8 — kentrussell (2019-08-21T13:57:50Z)

Peculiar. We've got RadeonVII working in our internal testing on an i7, but that's obviously a different arch. I wonder if we've got some issues with Cascade Lake that we haven't tried out yet. Though I don't know why the CPU would be causing issues. Can you get a full dmesg and attach it in here? Thanks!

---

### 评论 #9 — heero-yuy (2019-09-12T08:33:38Z)

Hi kentrussell,

After Checked ROCm 2.7.1 with Ubuntu 18.04.3 (kernel 4.15.0-60), checked that the Intel CascadeLake-SP CPU can be used with the openCL enabled, many thanks!

---

### 评论 #10 — PhilipDeegan (2019-10-05T19:29:20Z)

> do you put your user inside video group ?

for posterity, it may also require the "render" group.

depending on what shows up in /dev/dri

---
