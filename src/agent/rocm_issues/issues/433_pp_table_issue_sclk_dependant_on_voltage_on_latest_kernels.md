# pp_table issue: sclk dependant on voltage on latest kernels

> **Issue #433**
> **状态**: closed
> **创建时间**: 2018-06-13T19:41:01Z
> **更新时间**: 2019-01-08T01:06:09Z
> **关闭时间**: 2019-01-08T01:06:08Z
> **作者**: rhlug
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/433

## 描述

There may be a new issue around pp_table on latest kernels.   I wanted to record it here in case it flows through to amdgpu-pro or rocm via dkms being loaded.

I was testing powerplay in kernel drm-next-4.19-wip.

I setup a pp_table on a couple vega64 cards for 1390mhz/1090mhz/900mv

Both cards say they are running those clocks (via /sys/class/drm/*)

```
# clocks
3: 1090Mhz *
7: 1390Mhz *
3: 1090Mhz *
7: 1390Mhz *
```

However, getting data from  /sys/kernel/debug/dri/*/amdgpu_pm_info,  its different.

```
1390/1090/900mv (4.17.0-rc5-20180610-drm-next-4.19-wip)

 ID       Name  Sclk  Mclk mVolt Watts  Temp   Fan
============================================================
  0   rxvega64  1334  1090   937   115    62   40%
  1   rxvega64  1316  1090   900   102    60   26%
============================================================
```

I dont have any idea where gpu #0 gets 937mv.  Not from pp_table, thats for sure.

I cant get to 1390mhz core unless I up voltage over 975mv.   Here is 925mv, 950mv, 975mv

```
============================================================
  1   rxvega64  1334  1090   925   117    63   37%
  1   rxvega64  1356  1090   950   129    62   48%
  1   rxvega64  1388  1090   975   137    62   37%
============================================================
```

Reverting back to 4.17.0-rc2-180424-fkxamd, what I set in pp_table is really happening

```
1390/1090/900mv (4.17.0-rc2-180424-fkxamd)

 ID       Name  Sclk  Mclk mVolt Watts  Temp   Fan
============================================================
  0   rxvega64  1390  1090   900   113    61   26%
  1   rxvega64  1390  1090   900   114    62   26%
============================================================
```





---

## 评论 (16 条)

### 评论 #1 — heavyarms2112 (2018-06-29T13:26:51Z)

and i am assuming we cant change the power limit as well?

---

### 评论 #2 — rhlug (2018-07-01T00:49:58Z)

In pp_table, you can set power limit, wattage limit, or even target temp if you want to reduce power.   Refer to the spreadsheet for location of those items.

https://docs.google.com/spreadsheets/d/1-rhYsaRXO1ahk3PyrEgT9gXzs7ImAzh-sbqtgwy8HQg/edit#gid=964538665

---

### 评论 #3 — sayyiditow (2018-07-03T10:41:15Z)

@rhlug were you able to control the power limit/voltgage for your vegas? Any instructions/steps you can direct me to? I want to reduce the power usage on my vega 56. I am running ubuntu 16.04, rocm 1.8.1.

---

### 评论 #4 — rhlug (2018-07-04T03:49:24Z)

Oh yea.   I have a couple small test rigs running Cryptonight-heavy.   Vega56 runs ~1225 h/s @ ~100w (not TDP) and Vega64 runs 1325h/s @ ~105w (not TDP).     I dont have any Cryptonightv7 rates to share.

```
# rates
MINING xhv
GPU #0
Totals (ALL):   1232.8 1233.0 1233.1 H/s
GPU #1
Totals (ALL):   1220.9 1221.0 1220.9 H/s
GPU #2
Totals (ALL):   1232.1 1231.3 1232.1 H/s
GPU #3
Totals (ALL):   1220.6 1220.6 1221.3 H/s
Speed (ALL GPU): 4906.4 
```

```
# gfx
 ID       Name  Sclk  Mclk Volts Watts  Temp   Fan
============================================================
  0   rxvega56  1365   925   900   104    60   58%
  1   rxvega56  1365   925   900    98    62   56%
  2   rxvega56  1365   925   900   105    60   70%
  3   rxvega56  1365   895   900    90    63   57%
============================================================
  4                                397
```

```
# gfx
 ID       Name  Sclk  Mclk mVolt Watts  Temp   Fan
============================================================
  0   rxvega64  1390  1090   893   108    61   26%
  1   rxvega64  1390  1090   893   106    62   40%
============================================================
  2                                214
```

```
# rates
MINING xhv
GPU #0
Totals (ALL):   1335.9 1336.2 1335.9 H/s
GPU #1
Totals (ALL):   1321.3 1321.8 1322.2 H/s
Speed (ALL GPU): 2657.2  Shares (ALL GPU): 
```


I run Ubuntu 18.04 with 4.17.0-rc2-180424-fkxamd  kernel built from fxkamd/drm-next-wip ROCT-Thunk.

I apply pp_tables that set them at 1365mhz core (900mv) and 925mhz memory.    My last card is XFX reference, and doesnt like 925mhz.

```
# ls -la mining/ppt/rxvega56/cryptonight/[0-3]
lrwxrwxrwx 1 root root 23 Jun 26 19:15 mining/ppt/rxvega56/cryptonight/0 -> pp_table.1365.925.900mv
lrwxrwxrwx 1 root root 23 Jun 26 19:15 mining/ppt/rxvega56/cryptonight/1 -> pp_table.1365.925.900mv
lrwxrwxrwx 1 root root 23 Jun 12 04:37 mining/ppt/rxvega56/cryptonight/2 -> pp_table.1365.925.900mv
lrwxrwxrwx 1 root root 23 Jun 12 04:56 mining/ppt/rxvega56/cryptonight/3 -> pp_table.1365.895.900mv
```

I have 64 bios on these ref 56's also, and I can push them all at 1095mhz memory no problem, so not sure why it doesnt like 900+mhz on 56 timings.  I can push the first 3 at 945mhz no issue.

I find there is no speed benefit to running 64 bios on my vega56 in terms of cryptonight*.   If I were mining eth, I'd be flipping to 64 bios, and running 1095mhz for sure.  They can actually go higher if I up the SoC.   But I dont like heat in the summer, so not mining ethash.



---

### 评论 #5 — TheKnightCoder (2018-07-05T21:30:01Z)

@rhlug do you mind giving me some pointers on how to build a 4.17.0-rc2-180424-fkxamd kernel with ROCT-Thunk

---

### 评论 #6 — rhlug (2018-07-06T21:26:45Z)

something like this..   (editing, sorry but i realized i gave wrong url for kernel)

```
# git clone --depth 1 https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver -b fxkamd/drm-next-wip
# cd ROCK-Kernel-Driver 
# cp /boot/config-`uname -r` .config
# yes '' | make oldconfig
# make -j `getconf _NPROCESSORS_ONLN` deb-pkg LOCALVERSION=-fxkamd
# dpkg -i *deb
```
Thats the kernel part of it.   The Thunk

```
# git clone --depth 1 https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface -b fxkamd/drm-next-wip
# cd ROCT-Thunk-Interface
# make
# cp -a /opt/rocm/libhsakmt/lib/ /opt/rocm/libhsakmt/lib.bak
# cp build/lnx64a/libhsakmt.so* /opt/rocm/libhsakmt/lib
(and fix any symlinks...)
```


---

### 评论 #7 — TheKnightCoder (2018-07-07T16:15:15Z)

@rhulg thanks that helps a lot. I read a post where you mention you have amdgpu-pro 18.20-579836 without DKMS, how did you add this?
Do you have amdgpu-pro and ROCm 1.8.x in your kernel?

---

### 评论 #8 — gstoner (2018-07-07T16:39:41Z)

@TheKnightCoder   When you look at how stack is build you have Set of Language Runtimes, Usermode Driver and Kernel mode driver.     For AMD all driver start on linux with AMDGPU  base kernel mode driver which is what is upstreamed in the linux kernel.     

The each driver can have different UMD layer. AMDGPUpro use PAL + LLVM to HSAIl -> HSAIL Finalizer -> Shader Compiler aka SC.   

ROCm user mode is ROCr ( HSA System Runtime  based ) with THUNK layer 

OpenCL as core language library is the same for ROCm and AMDGPUpro what different is  VDI layer mappings.  AMDGPUpro goes to PAL and ROCm goes to ROCr.    

Second change is they run on two different Compilers   But use a common Frontend.  AMDGPUpro still used proprietary Shader Compiler which is also used for OpenGL.  ROCm uses native LLVM code generator. 

When you see performance delta it can be optimization flag you need to set like shutting off DENORMS, or they could be need to address optimization maturity issue native LLVM compiler.  It newer.  But you also have all the source to it so you can see what going on. 


KCL in DKMS is issue right now we discussing with Linux team way to fix it,  also make sure they have compatibily of what they upstream with the ROCm thunk.  This is the current issue. 

---

### 评论 #9 — TheKnightCoder (2018-07-07T18:50:47Z)

@gstoner thanks for the explanation it's making a lot of sense now.

But if ROCm and AMDGPUpro are two different usermode drivers then why does some AMDGPUpro mention they include ROCm 1.6?

Specifically the page says:
Package Contents
AMDGPU-Pro Driver
ROCm Platform 1.6 in supported distributions

---

### 评论 #10 — gstoner (2018-07-07T18:54:11Z)

Which version of AMDGPUpro.. 18.xx series is when the switch happened, Older AMDGPUpro used ROCm aka ROCr OpenCL runtime in 17.50 with the LLVM to HSAIL compiler.

On Jul 7, 2018, at 1:50 PM, TheKnightCoder <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> thanks for the explanation it's making a lot of sense now.

But if ROCm and AMDGPUpro are two different usermode drivers then why does some AMDGPUpro mention they include ROCm 1.6?

Specifically the page says:
Package Contents
AMDGPU-Pro Driver
ROCm Platform 1.6 in supported distributions

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/433#issuecomment-403235980>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSzcXmLPBaEvzTf23NBb8BBqrIIGks5uEQMIgaJpZM4Um0ET>.



---

### 评论 #11 — rhlug (2018-07-11T14:11:32Z)

> @rhulg thanks that helps a lot. I read a post where you mention you have amdgpu-pro
> 18.20-579836 without DKMS, how did you add this?

With the fkxamd kernel, the amdgpu-dkms package will install, it will just fail to install the dkms module.   But thats okay, because you dont need it.  All the kfd is in the kernel.

> Do you have amdgpu-pro and ROCm 1.8.x in your kernel?

Right now, just amdgpu-pro 18.20-606296.  I'll probably be switching to rocm 1.9 when its out.


---

### 评论 #12 — securitizones (2018-07-19T17:51:53Z)

So a question . If you are starting from base 18.04 with 4.17rc2 say. With no rocm or amdgpupro installed. Are you saying you can just build and install the 2 drivers and it will work with opencl etc. Or do you have to add anything before or after. Really really appreciate a full list of things on base system just installed and kernel updated. With exactly what you have to build and install to get opencl rocm interface working

---

### 评论 #13 — rhlug (2018-07-20T14:12:01Z)

```
# uname -a
Linux rig30 4.17.0-rc2-180424-fkxamd #1 SMP PREEMPT Wed Apr 25 17:53:26 CDT 2018 x86_64 x86_64 x86_64 GNU/Linux

# dpkg -l | grep amdgpu
ii  amdgpu-core                              18.20-606296                        all          Core meta package for unified amdgpu driver.
ii  amdgpu-dkms                              18.20-606296                        all          amdgpu driver in DKMS format.
ii  amdgpu-pro-core                          18.20-606296                        all          Core meta package for Pro components of the unified amdgpu driver.
ii  clinfo-amdgpu-pro                        18.20-606296                        amd64        AMD OpenCL info utility
ii  ids-amdgpu                               1.0.0-606296                        all          List of AMD/ATI cards' device IDs, revision IDs and marketing names
ii  libdrm-amdgpu-amdgpu1:amd64              1:2.4.91-606296                     amd64        Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm2-amdgpu:amd64                     1:2.4.91-606296                     amd64        Userspace interface to kernel DRM services -- runtime
ii  libopencl1-amdgpu-pro:amd64              18.20-606296                        amd64        AMD OpenCL ICD Loader library
ii  opencl-amdgpu-pro                        18.20-606296                        amd64        AMD OpenCL
ii  opencl-amdgpu-pro-dev                    18.20-606296                        amd64        AMD OpenCL SDK
ii  opencl-amdgpu-pro-icd                    18.20-606296                        amd64        non-free AMD OpenCL ICD Loaders
ii  opencl-orca-amdgpu-pro-icd:amd64         18.20-606296                        amd64        non-free AMD OpenCL ICD Loaders

# clinfo | grep "Device Board"
  Device Board Name (AMD)                         Radeon RX Vega
  Device Board Name (AMD)                         Radeon RX Vega
  Device Board Name (AMD)                         Radeon RX Vega
  Device Board Name (AMD)                         Radeon RX Vega
  Device Board Name (AMD)                         Radeon RX Vega
  Device Board Name (AMD)                         Radeon RX Vega
```



---

### 评论 #14 — gstoner (2018-07-20T14:41:20Z)

 
This is only for GFX8. and older GPU's, it is not used for Vega10 
opencl-orca-amdgpu-pro-icd:amd64         18.20-606296                        amd64        non-free AMD OpenCL ICD Loaders


---

### 评论 #15 — securitizones (2018-07-20T15:14:42Z)

i am so confused.

I just want to install a kernel and be able to run tdxminer which is dependent upon rocm and also undervolt  my vega64's

Is there any way i can do that?



---

### 评论 #16 — jlgreathouse (2019-01-08T01:06:08Z)

Hi @securitizones 

If you are using 18.04, but you want to use a kernel newer than the 4.15 that comes with current versions of Ubuntu 18.04, then you should look into using ROCm with our [upstream Linux driver support](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#rocm-support-in-upstream-linux-kernels). To do this, you can follow these directions:

1. [Update your system](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#first-make-sure-your-system-is-up-to-date)
2. [Add the ROCm repository](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#add-the-rocm-apt-repository)
3. Run `apt update`
4. [Install ROCm without installing the `rock-dkms` kernel driver](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#using-rocm-with-upstream-kernel-drivers)
5. [Set up permissions](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#next-set-your-permissions)

Note that if you do not want to follow these directions manually, you should also be able to run the Ubuntu 18.10 installation scripts in the [Experimental ROC](https://github.com/RadeonOpenCompute/Experimental_ROC/tree/roc-2.0.0) project to automatically perform these steps. The Ubuntu 18.10 installation directions use the upstream kernel driver, and basically every other step is the same as installing Ubuntu 18.04. So they should work if you're using a post-4.15 kernel on Ubuntu 18.04.

Note that if you are using a Vega 10 GPU, you will need a [post-4.17 kernel](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#rocm-support-in-upstream-linux-kernels) to have the required software support.

If you want to try overclocking, undervolting, etc. on your GPU, you can look into using [new versions of `rocm-smi`](https://github.com/RadeonOpenCompute/ROC-smi/blob/roc-2.0.0/README.md). Boot your kernel [with OverDrive enabled](https://github.com/RadeonOpenCompute/ROCm/issues/458#issuecomment-449775522) in the `amdgpu.ppfeaturemask`, and you can then use `rocm-smi --setslevel` and `rocm-smi --setmlevel` [to set the clocks and voltages for the various DPM states in your GPU](https://github.com/RadeonOpenCompute/ROCm/issues/463#issuecomment-450698247). In this manner, you shouldn't need to directly edit the `pp_table` or flash a custom BIOS on to set voltages and frequencies. Hopefully this will be easier than these other options.

You can also use these tools to [potentially set a higher maximum power cap on your GPU](https://github.com/RadeonOpenCompute/ROCm/issues/458#issuecomment-449775522), as requested here by @heavyarms2112 and @Sayyiditow. This can be done with `rocm-smi --setpoweroverdrive`.

@TheKnightCoder if you are interested in building custom versions of any of the ROCm software stack, please check out the [Experimental ROC project](https://github.com/RadeonOpenCompute/Experimental_ROC), where we now have build scripts for various Linux distributions for all of the software projects in ROCm.

---
