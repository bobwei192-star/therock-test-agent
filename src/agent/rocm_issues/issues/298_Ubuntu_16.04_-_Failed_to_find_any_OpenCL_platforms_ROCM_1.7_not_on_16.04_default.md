# Ubuntu 16.04 - Failed to find any OpenCL platforms ROCM 1.7 not on 16.04 default Linux,  on 4.13.0-21-generic 

> **Issue #298**
> **状态**: closed
> **创建时间**: 2018-01-08T17:58:10Z
> **更新时间**: 2018-08-24T00:54:15Z
> **关闭时间**: 2018-08-24T00:54:15Z
> **作者**: thagrisu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/298

## 描述

Hey,

i'm not able to get opencl running on my Ubuntu 16.04 system. 
System is running 9 AMD RX470 GPUs

Error with clinfo:
```
~$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
what():  clGetPlatformIDs
Aborted (core dumped)
```

Error with Hello World example:
```
~$ ./HelloWorld
Failed to find any OpenCL platforms.
Failed to create OpenCL context.

```

Error with rocm-smi

```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  5   24.0c   13.216W  300Mhz   300Mhz   43.92%   auto      0%
  3   21.0c   13.216W  300Mhz   300Mhz   43.92%   auto      0%
Traceback (most recent call last):
  File "/opt/rocm/bin/rocm-smi", line 1058, in <module>
    showAllConcise(deviceList)
  File "/opt/rocm/bin/rocm-smi", line 728, in showAllConcise
    fan = str(getFanSpeed(device))
  File "/opt/rocm/bin/rocm-smi", line 358, in getFanSpeed
    fanLevel = int(getSysfsValue(device, 'fan'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
```


Systeminfo:

Distributor ID: Ubuntu
Description:    Ubuntu 16.04.3 LTS
Release:        16.04
Codename:       xenial
Kernel:  4.13.0-21-generic

lspci output:

```
00:00.0 Host bridge: Intel Corporation Device 5904 (rev 02)
00:02.0 VGA compatible controller: Intel Corporation Device 5906 (rev 02)
00:08.0 System peripheral: Intel Corporation Sky Lake Gaussian Mixture Model
00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI (rev 21)
00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21)
00:1c.0 PCI bridge: Intel Corporation Device 9d12 (rev f1)
00:1c.3 PCI bridge: Intel Corporation Device 9d13 (rev f1)
00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port (rev f1)
00:1c.5 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port (rev f1)
00:1f.0 ISA bridge: Intel Corporation Device 9d50 (rev 21)
00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
00:1f.3 Audio device: Intel Corporation Device 9d71 (rev 21)
00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
01:00.0 PCI bridge: ASMedia Technology Inc. Device 1184
02:01.0 PCI bridge: ASMedia Technology Inc. Device 1184
02:03.0 PCI bridge: ASMedia Technology Inc. Device 1184
02:05.0 PCI bridge: ASMedia Technology Inc. Device 1184
02:07.0 PCI bridge: ASMedia Technology Inc. Device 1184
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
05:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
06:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
07:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
08:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 07)
09:00.0 PCI bridge: ASMedia Technology Inc. Device 1184
0a:01.0 PCI bridge: ASMedia Technology Inc. Device 1184
0a:03.0 PCI bridge: ASMedia Technology Inc. Device 1184
0a:05.0 PCI bridge: ASMedia Technology Inc. Device 1184
0a:07.0 PCI bridge: ASMedia Technology Inc. Device 1184
0b:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
0b:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
0c:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
0c:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
0d:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
0d:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
0e:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
0e:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
```

I guess the link to opencl info is missing somewhere on filesystem or systemvariable ? 
Please can someone advice me on how to troubleshoot this problem ? 

Thanks ! 
regards


---

## 评论 (52 条)

### 评论 #1 — gstoner (2018-01-08T18:24:54Z)

Did you remove the special kernels for ROCm 1.6, make sure the default kernels are installed and reinstall ROCm 1.7?

# Search all old ROCm-enabled kernels, as these cannot be used for the DKMS'ed ROCM 1.7
apt-cache search compute-rocm

# when for example 1.6-148 and 1.6-180 were found:
apt remove linux-image-4.11.0-kfd-compute-rocm-rel-1.6-180 linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-180
apt remove linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148 linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148

# Make sure the default kernels are installed
apt-get install linux-headers-generic linux-image-generic

# Be sure you update Grub the right way - depending on your distribution and version it is quite different.
# Grub method 1
update-grub
# Grub method 2
grub-mkconfig -o /boot/grub/grub.cfg

# remove ROCm completely. 
apt-get autoremove rocm-profiler rocm-opencl-dev rocm-dev rocm-dkms
# Double check if all is gone
apt-cache search rocm
apt-cache search hsa

# install the new ROCm.
sudo apt-get install libnuma-dev rocm-dkms rocm-opencl-dev

---

### 评论 #2 — thagrisu (2018-01-08T19:01:24Z)

yes no special kernel in use. 
As stated in Systeminfo i'm running 4.13.0-21-generic installed with apt-get install linux-image-generic-hwe-16.04-edge

---

### 评论 #3 — gstoner (2018-01-08T19:17:48Z)

Are you running GPU on PCIe Gen2 slots if so you have an issue seeing the GPU due to lack of PCIe Atomics. 

---

### 评论 #4 — thagrisu (2018-01-08T19:27:48Z)

Hm any tip on how to find out PCIe Gen on linux ?  Is it the devoce  "PCI bridge: ASMedia Technology Inc. Device 1184" lspci output ?

---

### 评论 #5 — thagrisu (2018-01-08T19:46:16Z)

According to http://www.asmedia.com.tw/eng/e_show_products.php?item=135&cate_index=112 it seems that my PCIe slots are Gen2 .
That means that rocm 1.7 is not usable for me right ?

---

### 评论 #6 — streamhsa (2018-01-09T08:32:08Z)

Can you please run clinfo after doing sudo chmod 777 /dev/dri/*
  

---

### 评论 #7 — thagrisu (2018-01-09T08:50:59Z)

@streamhsa  no change. Same errors.  Whats the system entry point for applications to opencl ? Is it /usr/include/CL ? Should this link to  /opt/rocm/opencl/include/CL/ ?

---

### 评论 #8 — spozi (2018-01-10T05:08:40Z)

Try to disable secureboot

---

### 评论 #9 — gstoner (2018-01-10T11:36:02Z)

This is the issue your using Generic Kernel  aka 4.13.0-21-generic    you need to use 16.04 specific kernel.   

---

### 评论 #10 — thagrisu (2018-01-10T11:59:11Z)

4.13.0-21-generic is the kernel i get from rolling HWE stack .. via  linux-generic-hwe-16.04-edge . So i think this is a 16.04 specific kernel ?  I've the same error with 4.10.0-42-generic which comes with 16.04.3 LTS
 

---

### 评论 #11 — pacxx (2018-01-10T12:02:17Z)

We are successfully running ROCm 1.7 on linux-generic-hwe-16.04-edge and linux-generic-hwe-16.04. Is your linux user in the video group?

---

### 评论 #12 — thagrisu (2018-01-10T12:56:46Z)

@spozi secure boot is disabled
@pacxx  yes is in video group 

but as gstoner already mentioned ROCm 1.7 seems to need gen3.0 PCIe .
Is this "just good to have" or is ROCm 1.7 not functional without gen3.0 PCIe ? 

---

### 评论 #13 — gstoner (2018-01-10T12:57:41Z)

You need to run 16.04 based kernel how the current dkms kcl is configured.   Note the last bits for ROCm DGPu support went up to the Linux kernel maintainer so in the future you be able to use generic kernel more easily

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: pacxx <notifications@github.com>
Sent: Wednesday, January 10, 2018 6:02:18 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] Ubuntu 16.04 - Failed to find any OpenCL platforms ROCM 1.7 (#298)


We are successfully running ROCm 1.7 on linux-generic-hwe-16.04-edge and linux-generic-hwe-16.04. Is your linux user in the video group?

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/298#issuecomment-356582808>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuT8dguHsWM6ndCaLe1vTgpppWn09ks5tJKbKgaJpZM4RWu9W>.


---

### 评论 #14 — chinf (2018-01-11T02:41:47Z)

Note that 16.04 HWE has moved from kernel 4.10 to 4.13 early as per the note at the end of [the Ubuntu Spectre/Meltdown advisory](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/SpectreAndMeltdown).

---

### 评论 #15 — thagrisu (2018-01-11T08:57:13Z)

@gstoner  i went back to ROCm 1.6-148 since i can't get ROCm 1.7 running.. maybe because of the lack of gen3.0 PCIe .
4.11.0-kfd-compute-rocm-rel-1.6-148 was running fine with 8 AMD RX470 Cards. When i attach one card more ( 9 in total ) i see the follwing random crash on boot. 

> Dec 12 16:49:28 14-5-5 kernel: [    4.921338] [drm:gfx_v8_0_kiq_resume [amdgpu]] *ERROR* KCQ enable failed (scratch(0xC040)=0xCAFEDEAD)

u can find kern.log here: https://pastebin.com/1P8jk0SF 

Is there a known issue with 8+ cards ? 

---

### 评论 #16 — thagrisu (2018-01-11T13:21:36Z)

According to :  https://bugs.freedesktop.org/show_bug.cgi?id=99851 these CAFEDEAD issue was introduced somewhere in 4.11.x kernel. I can confirm that my cards are working with 4.10 kernel. I've tried all kernel from 4.10 upwards.
Unfortunately 4.10 kernel  can't handle fragment_size which i need . 

So the question is, can i patch the **amdgpu_vm_adjust_size** feature into 4.10 kernel ? 

---

### 评论 #17 — gsedej (2018-01-15T09:04:04Z)

@gstoner 

```
Make sure the default kernels are installed
apt-get install linux-headers-generic linux-image-generic
```
the default 16.04 kernel is 4.4. 
rocm is probably not running well on 4.4?

edit:
it starts working when you install "hwe" kernel (4.13). 
```
sudo apt install linux-generic-hwe-16.04 linux-headers-generic-hwe-16.04 linux-image-generic-hwe-16.04
```
It should be mentioned in manuals, both here[1] and here[2]

[1] https://github.com/RadeonOpenCompute/ROCm

[2] https://rocm.github.io/install.html

edit2:
@thagrisu 
the `amdgpu.vm_fragment_size=9` does work for me

---

### 评论 #18 — BryceLuminary (2018-01-15T09:17:00Z)

@gstoner 

I encountered the same problem. After installing the driver with the official apt-get installation on a freshly installed ubuntu 16.04.3, the kernel is updated to 4.13.0-21-generic (instead of 4.11.0, mentioned in the installation guide). I can use rocm-smi to find the video card, but a similar segment error in @thagrisu 's issue occurred while the program was running. I tried the ubuntu desktop version and server version, no effect.

---

### 评论 #19 — gstoner (2018-01-15T15:26:55Z)

What would be helpful to understand is what issue are you trying to solve with moving off the base 4.4 kernel used in Ununtu 16.04 that  ROCm 1.7 was testing with for the DKMS install.   

I know in the past we bootlegged to newer kernel,  but many of you asked for DKMS, but it does have its downsides   yes you need to  install linux-headers since you are going to recompile the kernel 

I think I need the get the Core Linux driver team to do a write up on KCL + DKMS 

We have ROCm 1.7.1 in the works, targeting before the end of the month. 

---

### 评论 #20 — gsedej (2018-01-15T19:42:51Z)

@gstoner I don't have knowledge what rocm does to the kernel, but 4.4 was first (or one of the first) kernerls to support polaris, and it was quite buggy (there were also some firmware issues).

With rocm 1.7, I was able to use much newer kernel 4.13, which was very nice feature. It might even resolve my kernel memory issue due to DC and/or audio over hdmi. I will report

---

### 评论 #21 — gstoner (2018-01-15T20:01:59Z)

Yep, the benefit of the old bootleg method. DKMS has it own fun attached to it. 

---

### 评论 #22 — gstoner (2018-01-15T20:41:50Z)

You what happen is we bring the current most driver but it attaches to the older kernel via DKMS the only issue is you have all the old CPU stuff and driver for everything else. 

---

### 评论 #23 — BryceLuminary (2018-01-16T03:30:48Z)

@gstoner 

All I did was download the 16.04.3 LTS operating system from Ubuntu's website (which itself contains the 4.10.0-28-generic kernel of 16.04.3 LTS, instead of the 4.4 version of older 16.04 LTS) and follow the instructions to download ROCm using the apt-get command. I did not explicitly change the kernel version.

```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'

sudo apt-get update
sudo apt-get install libnuma-dev
sudo apt-get install rocm-dkms rocm-opencl-dev
```

After the apt-get command has finished running and restarted the computer, the kernel has been upgraded to the 4.13.0-26-generic version, not version 4.11 specified in the [installation guideline](https://rocm.github.io/ROCmInstall.html).

At this point, I run the HelloWorld test program and the program prints "Can not find OpenCL device." I am in the process of troubleshooting problems, such as paragraph errors occurred.

---

### 评论 #24 — ghost (2018-01-16T04:10:44Z)

I am having the same issue. Fresh install of Ubuntu Server 16.04.3, then update, upgrade, add ROCm repo, update, install ROCm, reboot. The `amdgpu` driver seems to be loaded just fine (the console gets a nice resolution boost), but I have no luck running `clinfo`. It just crashes with `cl::Error` exception. I have also experimented with downgrading to ROCm version 1.6 and using that + kernel that comes with it, but no avail. I am pretty sure that I have also tried 4.11 kernel with the same result (although I may need to repeat that exercise just to be sure).

---

### 评论 #25 — gstoner (2018-01-16T04:17:44Z)

When you installed driver did you install Linux kernel header for the kernel you were using.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Krzysztof Woś <notifications@github.com>
Sent: Monday, January 15, 2018 10:10:46 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Ubuntu 16.04 - Failed to find any OpenCL platforms ROCM 1.7 not on 16.04 default Linux, on 4.13.0-21-generic (#298)


I am having the same issue. Fresh install of Ubuntu Server 16.04.3, then update, upgrade, add ROCm repo, update, install ROCm, reboot. The amdgpu driver seems to be loaded just fine (the console gets a nice resolution boost), but I have no luck running clinfo. It just crashes with cl::Error exception. I have also experimented with downgrading to ROCm version 1.6 and using that + kernel that comes with it, but no avail. I am pretty sure that I have also tried 4.11 kernel with the same result (although I may need to repeat that exercise just to be sure).

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/298#issuecomment-357848935>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuW3A-uRaaLbm6MzDOpd7etL4ggcdks5tLCFFgaJpZM4RWu9W>.


---

### 评论 #26 — ghost (2018-01-16T04:20:21Z)

Yes, of course. Both kernel image and headers. I'll have more time to work on this over the weekend, I'll have another go at it and then post an exact transcript of all commands from a fresh install.

---

### 评论 #27 — Yougmark (2018-01-18T21:10:16Z)

Could you check if hsa runtime is installed? Either by looking at /opt/rocm/hsa/ directory or search libhsa-runtime64.so.  I missed hsa installation for unknown reasons when installing rocm-dkms.

I don't know how to install one for rocm-dkms.  So please reply if anyone knows.

However, current hsa-runtime doesn't seem to work with Raven Ridge APU (Ryzen+Vega), so I kept getting invalid pointer error thrown from free() function. When will hsa-runtime support Raven Ridge?

---

### 评论 #28 — gstoner (2018-01-18T21:18:45Z)

Raven Ridge support is still in development, you bit ahead of our support with this request I being worked on. 

---

### 评论 #29 — Yougmark (2018-01-18T23:48:05Z)

@gstoner Thanks for letting us know.  I thought it's supported as in the ROCm installation page, it's said to be tested in the mid 2017.  

When would Raven Ridge be supported? Any possibility to use AMDOVX (OpenVX) on Raven Ridge now?  Are people outside AMD/HSA encouraged to contribute? How?

Thanks!

---

### 评论 #30 — gstoner (2018-01-19T01:13:41Z)

We working on bring it into next major release of ROCm.   

On ROCm contributions,  we love to get more community support, we need help in lots of areas, testing documentation and more.      We want to grow the community and make open and collaborative.     I would be happy even if you bought the userland of ROCm to NVIDIA, Intel, Qualcomm and ARM hardware. 

---

### 评论 #31 — ghost (2018-02-18T07:09:30Z)

470 2g users 480 and vega, You might want to try a few simple things. First remove all the i386 packs,
put a hold on the kernel before even think about upgrading. Install the low-latency. Then umm well toss the amd installer in just use dpkg hold the kernel and headers and then like this  `rm *i386* ; ls > installamd ; sed  -i s/^/dpkg\ -i\ --force-all/g installamd ; chmod 755 ./installamd ; ./installamd ;apt-get -f install` . Then throw on the rocm and make sure to disable the hdm audio on the cards. If you want that nice with a bit quicker bootup throw the whole baby out because it basicly needs to be and dump systemd and use sysvinit.  Please keep in mind picking hardware is and can be a issue too. You can get a nice multi pci board to handle 18 gpus for about 100 bucks. While a expensive one is alot more. Alot of the 8pin powered cards are only that way because of the wire guage where you can an they do work on only 6pins and as long as you do not have a floating ground but a good back plane its one switch and 18 cards are fine since the kick on power is only about 650w @ 250. 

---

### 评论 #32 — ghost (2018-02-18T07:14:57Z)

Rocm, Need to like tell people hey the packages for cmake gcc and libs includes are over here :+1:  There are alot of hardware configurations and so its going to be umm Interesting. I think with the amount of firmware, sqcuse me fuckups(Experiment Computer Science). That a wiki like openwrt would be nice.  ROCM works great on intel but require both a bit of alchemy and right hardware, Crazy Can't be too good can't be too bad. Worst then the freaking goldylox zone.

---

### 评论 #33 — gstoner (2018-02-18T16:24:22Z)

@tekcomm 

My team develops the userland components,  We are now trying to break down the DKMS build process so it is better documented, we get your pain we need this as well in our team.   The base Linux driver is developed in a separate team from ROCm userland team we work on everything from ROCr System library upward.   

You see we trying to get better documentation in place especially around the base Linux driver, we are still a small team that was a startup in AMD for the last two year.  I personally put the ROCm website up and new documentation site.  

Have you looked at this install guide since it tells you which tool we need for release? 
- https://rocm.github.io/ROCmInstall.html

Also, we have been driving all new documentation to here. 
- https://rocm.github.io it all evolving to here http://rocm-documentation.readthedocs.io/en/latest/index.html 

You see we even documented all of our system level debug flags 
-  http://rocm-documentation.readthedocs.io/en/latest/Other_Solutions/Other-Solutions.html 

Also, we very explicit what GPU we support with ROCm,  You can get even more understand of core compiler technology, code object format etc  here   https://llvm.org/docs/AMDGPUUsage.html

On the Linux driver in the past, ROCm was using a  bootleg kernel driver where it was totally controlled what we needed for ROCm Userland stack, understand we using newer PCIe feature older hardware did not support ( PCIe Gen3 Atomic Completion/PCIe Atomics example)  because ROCm was targeted at Intel Xeon E5 server hardware and every system  in this space has to go through system-level validation at AMD and the OEM/ODM.   Note Ryzen, Threadripper, and EPYC support all the capabilities that Xeon E5 v3 does which we use. 

On the base Linux driver,  we made four changes from early days of the project,  

- First, we moved to DKMS style install for base Linux kernels install for the binary product starting with 1.7. This was critical for us to support more distros ( REHL/CENTOS, SUSE) with new hardware that is not upstream.   This transition was not smooth and we are working on remedying this.  

- The second thing we have been working with Linux team upstream all the core ROCm Linux driver changes so when you pull a base Linux kernel ROCm userland just works except for our existing shipping GPU that documented to work with ROCm.  This right now looks to be complete with 1.7 or 1.8 Linux kernel release. 

- Third from lesson learn on ROCm 1.0 to 1.6.4 we diving into the core Linux team improved the testing program,  at the ROCm level we are growing our Test data center, we rolled on 30 new servers since December and another 20 will be in by end of March.     One thing, we are building out is a Customer Validation Test Suite to validate there install, this should be complete by June.  We will also make more of our  ROCm Validation Tests to simplify customer driver development. 

- Fourth we are working with Linux team to improve documentation of the based driver, this will take time. 

I want to ask for patience as we work on improving the project,  I personally started the ROCm project at AMD with Ben Sander since we knew we had to change how we approached GPU Computing.   We are working hard to make the adjustment to drive this to a solid product.   Also, we working to get in place key foundation so we all can chase down issue 

I want the group to see we working hard to address the 1.7 release issue.     To help you and us I am giving you early access to  1.7.1 Beta this has been tested with 4.13 Generic Linux kernel.  http://repo.radeon.com/misc/archive/beta/rocm-1.7.1-beta.tar.gz  

best regards, 

Greg 
CTO RTG - Systems Engineering 



---

### 评论 #34 — ghost (2018-02-18T23:35:51Z)

Great, So you already probably know as I type I am trying it on the http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.15/ :P

---

### 评论 #35 — gstoner (2018-02-18T23:37:30Z)

Yep,  we working with the Linux team to clean up KCL for 4.15.  

---

### 评论 #36 — ghost (2018-02-19T18:01:29Z)

The kthread kcl patch is here btw :)

http://www.ozlabs.org/~akpm/mmotm/broken-out/linux-next.patch

On Mon, Feb 19, 2018 at 6:37 AM, Gregory Stoner <notifications@github.com>
wrote:

> Yep, we working with the Linux team to clean up KCL for 4.15.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/298#issuecomment-366558765>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w49GgV7FLgWGadbax-rs1fcv18sjks5tWLQ9gaJpZM4RWu9W>
> .
>


---

### 评论 #37 — ghost (2018-02-19T20:11:19Z)

4.15 kthread problem 
4.11.0.13-14-lowlatency  problem
linux-image-lowlatency-hwe-16.04-edge gold
Works with beta rocm 
Currently testing on 3 rx 500 series with FAH for 24hrs

---

### 评论 #38 — brian-maher (2018-02-19T23:22:18Z)

First off - thank you very much for your efforts here! I've personally been struggling with rocm as I need a kernel version which is new enough to behave with thunderbolt 3 devices (if you think graphics drivers are tricky!)

I've had a play with 1.7.1 beta on 4.14.8 - and I cannot, for the life of me, get it working. I get the same issue as above - not finding any OpenCL platforms.

lshw output:
`  *-display               
       description: VGA compatible controller
       product: Advanced Micro Devices, Inc. [AMD/ATI]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:01:00.0
       version: c0
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:35 memory:c0000000-cfffffff memory:d0000000-d01fffff ioport:4000(size=256) memory:92600000-9263ffff memory:92640000-9265ffff
  *-display UNCLAIMED
       description: VGA compatible controller
       product: Advanced Micro Devices, Inc. [AMD/ATI]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:46:00.0
       version: 00
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller cap_list
       configuration: latency=0
       resources: memory:99a00000-99a7ffff memory:99a80000-99a9ffff`

This system has 2 GPUs, an internal RP 580, and a Frontier Edition in a TB3 enclosure. As you can see above, the 580 seems to get the amdgpu driver, whilst the FE doesn't.

clinfo just says `Number of platforms                               0`

If I try to run rocm-smi I get an error I have not seen on any rocm build previously:


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
Traceback (most recent call last):
  File "/opt/rocm/bin/rocm-smi", line 1076, in <module>
    showAllConcise(deviceList)
  File "/opt/rocm/bin/rocm-smi", line 714, in showAllConcise
    fan = str(getFanSpeed(device))
  File "/opt/rocm/bin/rocm-smi", line 354, in getFanSpeed
    fanLevel = getSysfsValue(device, 'fan')
  File "/opt/rocm/bin/rocm-smi", line 116, in getSysfsValue
    fileValue = fileContents.read().rstrip('\n')
OSError: [Errno 19] No such device

If there's anything I can do to help/test, please do let me know! I imagine I'm not the only person eager to use rocm with TB3 gpus - at the moment we're restricted to using metal under OS X - which is, shall we say, hard work.

---

### 评论 #39 — brian-maher (2018-02-20T00:27:46Z)

Just tried with the edge kernel. I get further than before - no errors, but any OpenCL commands just hang indefinitely. Machine also hangs on shutdown - so something is really not happy. It's half past midnight so I won't have a chance to debug this kernel tonight, but will do some fiddling after work tomorrow.

Edit: looks like it is indeed the driver - here's the crashlog for `clinfo` running edge.

[crash.log](https://github.com/RadeonOpenCompute/ROCm/files/1738592/crash.log)

@tekcomm are you using 1.7.1 on edge?


---

### 评论 #40 — gstoner (2018-02-20T04:16:46Z)

This just tell you who built it on jenkins,  I see if there is an issue 
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104

---

### 评论 #41 — gstoner (2018-02-20T04:17:45Z)

Here is the source for ROCminfo https://github.com/RadeonOpenCompute/rocminfo 

---

### 评论 #42 — jedwards-AMD (2018-02-20T04:17:55Z)

What do you need?

---

### 评论 #43 — jedwards-AMD (2018-02-20T04:20:00Z)

That was zed, and zeds dead baby, zeds dead.

---

### 评论 #44 — gstoner (2018-02-20T04:20:04Z)

Now your talking my nick name  is?   Nice Coffee you have 5. minutes 

// Print out all static information known to HSA about the target system.
// Throughout this program, the Acquire-type functions make HSA calls to
// interate through HSA objects and then perform HSA get_info calls to
// acccumulate information about those objects. Corresponding to each
// Acquire-type function is a Display* function which display the
// accumulated data in a formatted way.
int main(int argc, char* argv[]) {
  hsa_status_t err;

  err = hsa_init(); <-- line 900
  RET_IF_HSA_ERR(err);


---

### 评论 #45 — jedwards-AMD (2018-02-20T04:22:02Z)

Is this a permission issue on the /dev/kfd device? Have you been able to run other apps?

---

### 评论 #46 — gstoner (2018-02-20T19:44:59Z)

Place them here https://github.com/RadeonOpenCompute/KFD_Patchset I gave you write permissions 

---

### 评论 #47 — ghost (2018-02-22T10:01:20Z)

I am uploading my dev testing flash now.
AMD-rocm-rippa-1.7.1
unzip the file and just 
dd if=AMD-rocm-ripper of=/dev/sd? 
to your flash drive
You can use a 16 gig flash with 9 gigs room to spare
4.13 latest lowlatency hwe kernel
Ripped systemd out and replaced it with sysvinit
refind efi boot loader
installer for any version of ubuntu
ethminer & fah client installed
wircd-ncurses for network config
ls ~
1.7.1 rocm beta & DKMS Modules
amdgpu-pro-17.50-511655 & DKMS modules
All current updates for 16.04 / dkms
 and all the opencl compiler dev tools.
Installers for all flavors of ubuntu are in the guru home directory

username: guru or eth or root
password : rocm

The source to attempt this feat of sleep derpervation requires at least a few cups of coffee.
Here is the stub code. It is really stubby. The main system works good. The stub code is not really alpha.
Its more like the apt-gets of a sleep deprived madman :) The usb Is like a bella, dd and bam
https://github.com/tekcomm/AMD-rocm-rippa/tree/master
There ya go its up version .1 :+1:  Feel free to test it
A full rocm/amd-gpu-pro prebuilt headless horsemen. 7 gigs for the base system with installers for any 
derivative systems and on a 16 gig storage it leaves 9 for dev.
The entire system only uses 113288 megs of ram.
wicd-curses are available apon login for network configuration and the logs are auto trimmed on boot.
Various speed mods have been put in place. A text mode installer is included if you wish to install it.

Total RAM = 15930 MiB, Used RAM = 111 MiB; UEFI;   
UEFI and grub compatible and also includes a front end shim to bypass the 64 bit limitation on efi systems that are older 32bit efi with 64 bit processors :)

Im off to look at the KFC problem.
Here ya go :)
https://drive.google.com/open?id=126D3TLvs7IvZyrGPcEkVk1pcuGub42QM


Enjoy: Use of the system is accompanied by the standardized end user agreement.
https://www.youtube.com/watch?v=_3Cl43FZvZc&feature=youtu.be

---

### 评论 #48 — ghost (2018-02-22T13:05:35Z)

Zed's dead wheres jeb? Hey thanks for fixing the oh umm rocm-info :+1: 

---

### 评论 #49 — kruftindustries (2018-07-20T23:53:45Z)

So how do I get a cl platform back after ubuntu updates the kernel?

---

### 评论 #50 — kruftindustries (2018-07-20T23:58:52Z)

Looks like booting 4.13.0-43-generic  after it updated to 4.15 gets cl platform back

---

### 评论 #51 — ghost (2018-07-21T10:33:06Z)

To install
dpkg -i linux-imagewhatever version.

To remove
apt-get purge linux-*4.15*
.... Thus it also will remove the kernel and headers and source if
installed. You should have pinned it to the working version if you did not
know how to remove it or refer to the distro's main documentation. Or the
oracle of google.
http://ubuntuhandbook.org/index.php/2016/05/remove-old-kernels-ubuntu-16-04/



On Fri, Jul 20, 2018 at 11:58 PM, kruftindustries <notifications@github.com>
wrote:

> Looks like booting 4.13.0-43-generic after it updated to 4.15 gets cl
> platform back
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/298#issuecomment-406753909>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w-nx6TXOtCcDx70jRRJDcsI8Ttryks5uIm7AgaJpZM4RWu9W>
> .
>


---

### 评论 #52 — Angel996 (2018-07-22T20:31:50Z)

I have the same problem. Kernel 4.4.0-130-generic, amdgpu 18.20-606296.
OpenCL platform is not available. Can't find any fix so far. ((

---
