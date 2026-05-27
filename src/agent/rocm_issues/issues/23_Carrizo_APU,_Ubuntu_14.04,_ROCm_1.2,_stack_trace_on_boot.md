# Carrizo APU, Ubuntu 14.04, ROCm 1.2, stack trace on boot

> **Issue #23**
> **状态**: closed
> **创建时间**: 2016-08-17T18:34:51Z
> **更新时间**: 2016-08-22T17:55:06Z
> **关闭时间**: 2016-08-22T17:55:06Z
> **作者**: pelarejo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/23

## 描述

Hello,

I updated ROCm from 1.1.1 to version 1.2 and upon reboot I get a stack trace which hangs the boot sequence.
A fresh install of Ubuntu did nothing to solve this so it should easily be reproducible, at least on a Aspire E15 with a FX-8800P processor.

I would love to be able to paste the stack trace in this thread but kern.log doesn't show anything related to the 4.4.0-kfd-compute-rocm-rel-1.2-31 kernel and would gladly follow any directions as to provide any additional information. I do have a picture of it below which hopefully will get the idea across.

Would it be possible, as a fast recovery option, to provide ROCm version 1.1 through the apt-get server ?

![img_1211](https://cloud.githubusercontent.com/assets/4035760/17748327/bf54c04c-64b0-11e6-8e87-0b633a3dac20.JPG)


---

## 评论 (12 条)

### 评论 #1 — jedwards-AMD (2016-08-17T18:58:52Z)

The old kernel should still be installed on the system; it isn't removed by default and is compatible with the new 1.2 runtime components. I think the easiest solution would be to boot using the 1.1.1-10 kernel. This can be accomplished by holding down the shift key while booting, selecting accessing "Advanced options for Ubuntu" and the selecting the 4.4.0-kfd-compute-rocm-rel-1.1.1-10 kernel.


---

### 评论 #2 — fxkamd (2016-08-17T20:45:59Z)

There are at least two backtraces here, maybe more that are cut off. Can you get a complete kernel log from /var/log/kern.log? To make sure the log is as complete as possible, remount the root partition (assuming you don't have /var on its own partition) synchronously before rebooting:
    sudo mount -o remount,sync /

Then reboot, wait for it to get stuck, reset the system and grab /var/log/kern.log

If you still don't see anything useful in kern.log, the rsyslog daemon probably gets killed too early during shutdown. You could try commenting out the following line from /etc/init/rsyslog.conf to keep it running as long as possible:
    stop on runlevel [06]

I'm assuming that you're running Ubuntu 14.04 with upstart. If you're on Ubuntu 16.04 with systemd, I'm not as familiar with that.


---

### 评论 #3 — streamhsa (2016-08-18T07:47:24Z)

Could you try following steps to clean up your old kernel/package completely then install 1.2?

# uninstall steps:

sudo apt-get purge $(dpkg -l | grep 'kfd|rocm' | grep linux | grep -v libc | awk '{print $2}')
sudo apt-get purge hcc_lc
sudo apt-get purge hsakmt-rocm-dev
sudo dpkg -r hsakmt-roct-dev
sudo apt-get purge hcc_hsail
sudo apt-get purge llvm-amdgpu
sudo apt-get purge rocm
sudo apt-get autoremove rocm
sudo dpkg -r compute-firmware
sudo dpkg -r hcblas
sudo rm -rf rocm 
sudo update-grub

# Install steps:

sudo apt-get clean all
sudo apt-get update
sudo apt-get install rocm


---

### 评论 #4 — pelarejo (2016-08-18T15:27:45Z)

Great will try uninstalling once I get back from work. Else I'll remount the root partition.

I doubt the uninstall process will solve the problem tho as I already tried to reinstall the whole system but it might show logs in keen.log again. 


---

### 评论 #5 — pelarejo (2016-08-19T16:51:10Z)

After reinstalling the whole ROCm suite, Ubuntu's boot animation did appeared this time but hanged up. It did however had the effect of logging properly in the kern.log which you can find here:
[kern.log.txt](https://github.com/RadeonOpenCompute/ROCm/files/427470/kern.log.txt)

As we can see line 0.773282, the first call trace happens and triggers **AMD-Vi: Unable to write to IOMMU perf counter.**
However this message used to happen in version 1.1.1 and did not affect the execution of vector_copy.

Scrolling down to line 20.736147 is where I believe is the real problem as we get **amdgpu 0000:03:00.0: amdgpu_init failed** message which triggers a series of call trace.

Edit: I've just notice the mention of using the previous kernel, I do not have it any more since I've cleaned the system. However, I did tried to boot the previous 1.1.1 kernel when crashing for the first time and it did not managed to boot up. If the problem is related to amdgpu package it would make sense.

Since the GPU might be at fault, my machine also possess an AMD Radeon R8 M365DX dGPU but running the command bellow on the default kernel does show that the Carrizo GPU is selected.
`lspci -vnnn | perl -lne 'print if /^\d+\:.+(\[\S+\:\S+\])/' | grep VGA`

Finally, the default kernel seems to run the amdgpu without trouble as the below command shows driver=amdgpu for the VGA compatible controller Product: Carrizo.
`sudo lshw -c video`


---

### 评论 #6 — fxkamd (2016-08-19T19:32:57Z)

Looks like Iceland GPU support is broken in our kernel. It fails to initialize and the error handling code seems to have some trouble and printing some warnings including backtraces. The actual protection faults that probably take down the system are later, in unrelated kernel functions. It's possible that faulty error handling in amdgpu is corrupting unrelated kernel data structures and causing problems later on.

Is there a way you can disable the dGPU in your BIOS setup as a workaround?


---

### 评论 #7 — pelarejo (2016-08-19T20:00:03Z)

Unfortunately, Acer BIOS is very limited and barely has any option regarding anything so I can't disable the dGPU.
Is there anyway I could be provided with the latest version of a deb package of ROCm 1.1 suite as a work around ? It seems I am to wait for a patch for HSA to work again and I unfortunately don't have that time as I have to present a working project relatively soon.


---

### 评论 #8 — jedwards-AMD (2016-08-19T20:25:56Z)

Did you try booting to older kernel, or did you completely remove it?


---

### 评论 #9 — pelarejo (2016-08-19T20:28:46Z)

It is now completely removed. When I tried it before deleting the whole ROCm 1.1 suite it also wouldn't get past initialisation. 


---

### 评论 #10 — jedwards-AMD (2016-08-19T21:39:59Z)

Unfortunately our repo server doesn't archive older versions of the ROCm packages. We are considering enhancing the repo to support that, but it isn't implemented at this time.


---

### 评论 #11 — pelarejo (2016-08-19T21:50:14Z)

Yes I've noticed that which is unfortunate. Wouldn't it be possible to have them sent by mail ?
Or can I expect an update before the end of the month ?

Disabling the dGPU seems impossible on this machine and the sources are incomplete as the README seems to imply.


---

### 评论 #12 — jedwards-AMD (2016-08-22T17:54:59Z)

I have placed the kernel debian packages for ROCm 1.1.1 on the package server in a gzip file. You can download it with this command:
wget http://packages.amd.com/rocm/gz/linux-4.4.0-kfd-compute-rocm-rel_1.1.1.tar.gz
.
The ROCm 1.1.1 user-mode debians will not be provided.


---
