# is there any way to install previous version of rocm with apt install?

> **Issue #284**
> **状态**: closed
> **创建时间**: 2017-12-23T14:58:33Z
> **更新时间**: 2019-10-07T16:59:02Z
> **关闭时间**: 2018-01-22T05:46:43Z
> **作者**: smithakihide
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/284

## 描述

because rocm1.7 still have many issues and actually my codes dose not work on rocm1.7.  I want to use rocm 1.6.
please tell me how to install rocm 1.6 with apt.

---

## 评论 (29 条)

### 评论 #1 — gstoner (2017-12-23T15:16:30Z)

first can you try to use this command 

```shell
sudo usermod -a -G video <username>
```

Then reboot.  

Also what CPU are you on.   

---

### 评论 #2 — smithakihide (2017-12-23T15:20:05Z)

thank you for answering.
sorry, I missed that instruction because it was a little hard to understand. now I will try it.

here is my cpu information.
```
~$ cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 94
model name      : Intel(R) Core(TM) i5-6400 CPU @ 2.70GHz
stepping        : 3
microcode       : 0x33
cpu MHz         : 899.945
cache size      : 6144 KB
```

---

### 评论 #3 — smithakihide (2017-12-23T15:27:08Z)

I do `sudo usermod -a -G video <username>`. 
but my environment generates still incorrect result.

here is the result of `group`
```
nico@nico:~$ groups
nico adm cdrom sudo dip video plugdev lpadmin sambashare
```

note that I am not a beginner of rocm and hcc. I have been able to compile hcc programs and execute it on rocm 1.6.

---

### 评论 #4 — gstoner (2017-12-23T15:39:46Z)

 Use this command,  
sudo usermod -a -G video $LOGNAME

You were to replace <username> with your real username it is a place holder.   

Greg

---

### 评论 #5 — gstoner (2017-12-23T15:40:00Z)

Note you need to reboot

---

### 评论 #6 — gstoner (2017-12-23T15:40:31Z)

or log out log in if you have rebooted since the install 

---

### 评论 #7 — smithakihide (2017-12-23T15:43:40Z)

I am sorry to give you mislead. and thank you for answering.

the actual command I executed is the below. my user name is nico.
`sudo usermod -a -G video nico`
then I rebooted my system.

after the system waked up, I executed the below command and got the output.
```
nico@nico:~$ groups
nico adm cdrom sudo dip video plugdev lpadmin sambashare
```
is this output correct?



---

### 评论 #8 — gstoner (2017-12-23T15:59:37Z)

This is correct you now have the video group added to your username


---

### 评论 #9 — smithakihide (2017-12-23T16:04:32Z)

thank you.

but still I could not find the RX 580s on my system when I executed some hcc program. here is an example output.
`There is no device can be used to do the computation`
could you give me any suggestion?


---

### 评论 #10 — gstoner (2017-12-23T16:16:41Z)

I just looked in the KFD Source to double check  if your RX580 is support,  you look for the  DeviceID  is supported 

kfd_device.c   
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdkfd/kfd_device.c   

{ 0x67DF, &polaris10_device_info },	/* Polaris10 */

Also in to make sure it was there in the key setup files for AMDGPU base driver 
amdgpu_cgs.c
{ 0x67DF, &polaris10_device_info },	/* Polaris10 */ 
amdgpu_drv.c. 
{0x1002, 0x67DF, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_POLARIS10},

It not driver support issue 

Still seams like permision issue.     Can you run rocminfo it is in /opt/rocm/bin 

Also can you run clinfo 


---

### 评论 #11 — smithakihide (2017-12-23T16:20:39Z)

yes. here are the results
```
nico@nico:~$ sudo /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104
```

```
nico@nico:~$ sudo /opt/rocm/opencl/bin/x86_64/clinfo 
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```

---

### 评论 #12 — smithakihide (2017-12-23T16:22:51Z)

I will do the same instructions with more carefully from fresh Ubuntu environment.

---

### 评论 #13 — gstoner (2017-12-23T16:36:45Z)

Hey are the GPU on X16 links in your motherboard 

run this 
 lspci -tv

When debugging PCIe issue I wrote this up as guide to the tools we use 
http://rocm-documentation.readthedocs.io/en/latest/Other_Solutions/PCIe-Debug.html#pcie-debug

---

### 评论 #14 — gstoner (2017-12-23T19:03:34Z)

Sorry I found it in the 0x67df in the Polaris 11 section.    I think I need to send you low level rocr level test 

---

### 评论 #15 — smithakihide (2017-12-25T03:08:54Z)

here is the output of `lspci -tv` and note that my mother board consists of Z170 chip set.

```
nico@nico:~$ lspci -tv
-[0000:00]-+-00.0  Intel Corporation Sky Lake Host Bridge/DRAM Registers
           +-01.0-[01]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-08.0  Intel Corporation Sky Lake Gaussian Mixture Model
           +-14.0  Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller
           +-14.2  Intel Corporation Sunrise Point-H Thermal subsystem
           +-15.0  Intel Corporation Sunrise Point-H LPSS I2C Controller #0
           +-15.1  Intel Corporation Sunrise Point-H LPSS I2C Controller #1
           +-16.0  Intel Corporation Sunrise Point-H CSME HECI #1
           +-17.0  Intel Corporation Sunrise Point-H SATA controller [AHCI mode]
           +-1c.0-[02]--
           +-1c.4-[03]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-1d.0-[04]--
           +-1d.3-[05]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           +-1e.0  Intel Corporation Sunrise Point-H LPSS UART #0
           +-1f.0  Intel Corporation Sunrise Point-H LPC Controller
           +-1f.2  Intel Corporation Sunrise Point-H PMC
           +-1f.3  Intel Corporation Sunrise Point-H HD Audio
           \-1f.4  Intel Corporation Sunrise Point-H SMBus
```

---

### 评论 #16 — smithakihide (2017-12-25T03:14:11Z)

Although I can help you to investigate the bugs in ROCm 1.7, but now I have a important project with ROCm.
So I want you to prepare the way install ROCm 1.6. it will be needed also in the future .


---

### 评论 #17 — extraymond (2017-12-25T05:46:18Z)

@smithakihide 

What's the version of kernel you're using?
I've had trouble using it with 4.15rc5. Rolling back to ubuntu 16.04 default make it work again.

---

### 评论 #18 — smithakihide (2017-12-25T06:20:49Z)

I am using  the kernel presented below.
```
$ uname -sr
Linux 4.10.0-40-generic
```
note that my OS is Ubuntu 16.04.3
did ROCm 1.7 really work even if it is a little? Although I tried it on the both environments with R9 390X on Core i5 4670 and RX580 on core i5 6400, it did not work.
if you could, tell me your environments.

---

### 评论 #19 — extraymond (2017-12-25T11:28:44Z)

```
Ubuntu 16.04.03
Linux 4.10.0-43-generic
```

I have a RX 480, haven't done anything serious, but afaik opencl works and rocminfo works too.

---

### 评论 #20 — smithakihide (2017-12-25T12:32:03Z)

@extraymond 
really? thank you for that information.
then it might have a worth to try again more carefully.

could you tell me your hardware information such as CPU and chipset?

---

### 评论 #21 — extraymond (2017-12-25T12:35:42Z)

CPU:   xeon e3-1231-v3. 
Mobo: is H97M.

---

### 评论 #22 — smithakihide (2017-12-25T13:52:14Z)

thank you. I will try when I go back to my country.
but I found that our kernels a little different.

mine is `Linux 4.10.0-40-generic.`
and your is `Linux 4.10.0-43-generic`

my Mo.bo. is H97-Pro. it's strange. I have to investigate more...

---

### 评论 #23 — gstoner (2017-12-27T15:40:09Z)

I noticed your using R9 390x aka Hawaii,  We will need to role you back to 1.6.4,  I have seen a few issue with  Hawaii.    @smithakihide  is this school project?   

---

### 评论 #24 — gstoner (2017-12-27T15:45:41Z)

For now  Try the AMDGPUpro driver 17.50 http://support.amd.com/en-us/kb-articles/Pages/Installation-Instructions-for-amdgpu-Graphics-Stacks.aspx

---

### 评论 #25 — smithakihide (2017-12-27T16:20:02Z)

@gstoner 
thank you for answering. but now I have not been able to make also RX 580 works yet.
yes, but a little different. this is the collaborative project with a company as well as a school project mainly on W8100 (I also wandering why ROCm are recognizing R9 390 and W8100 as the same).

can I use HCC on the AMDGPUpro driver 17.50 ?
I have to use C++ AMP compatible environment.... for the future of this world.
And I have already launched this project, so I really want you to help me by rolling back or remove issues from ROCm 1.7 as soon as possible.

---

### 评论 #26 — VincentSC (2018-01-04T16:42:30Z)

Could you please put older versions on http://repo.radeon.com/rocm/apt/debian/ ? These files have been removed.
With i.e. `apt install rocm-dev=1.6.180` the 1.6.180-version should get installed, but it gives "_E: Version '1.6.180' for 'rocm-dev' was not found_".

---

### 评论 #27 — VincentSC (2018-01-05T10:29:37Z)

If you have problems installing, see https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-355328679 for how to update to 1.7 correctly.

Solved the downgrade-problem by creating a local repo using the archives at http://repo.radeon.com/rocm/archive/
Our `/etc/apt/sources.list.d/rocm.list` now looks like this:
````
deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main
deb [arch=amd64] file:///opt/apt/rocm_1.6.3/ xenial main
deb [arch=amd64] file:///opt/apt/rocm_1.6.4/ xenial main
````
This makes it possible to install version 1.6.3, 1.6.4 and 1.7.0 using _apt_.

This is the result:
````
$ apt-cache madison rocm-dev
  rocm-dev |     1.7.60 | http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
  rocm-dev |    1.6.180 | file:/opt/apt/rocm_1.6.4 xenial/main amd64 Packages
  rocm-dev |    1.6.148 | file:/opt/apt/rocm_1.6.3 xenial/main amd64 Packages
````
If you're not familiar with installing a specific version, just remove ROCm, comment out and install again. Don't forget to update /boot/grub/grub.cfg with the specific default (update x, use `apt-cache search):
````
set default="Advanced options for Ubuntu>Ubuntu, with Linux 4.x.x-kfd-compute-rocm-rel-1.6-xxx"
````
See for the most recent 1.6 installation instructions: https://github.com/RadeonOpenCompute/ROCm/wiki/Home/196ace6906cea5f6c99119ff0934aee25eb71de6

---

### 评论 #28 — smithakihide (2018-01-22T05:46:43Z)

thank you for many reply.
I tried to reinstall Ubuntu after I came back to my country, and follow the current instructions of rocm carefully, I could successfully establish the environment.   

I am really glad so many people take care of me. thank you.

---

### 评论 #29 — iszotic (2019-10-07T16:29:11Z)

The easiest way is configure the debian repository like this:
`wget -qO - http://repo.radeon.com/rocm/apt/x.x.x/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/x.x.x/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list`
in the `x.x.x` put the version you want, you can check in http://repo.radeon.com/rocm/apt/ the versions available, uninstall your current version, update and install with the version you want. And if you want the latest again change the `x.x.x` with `debian`

---
