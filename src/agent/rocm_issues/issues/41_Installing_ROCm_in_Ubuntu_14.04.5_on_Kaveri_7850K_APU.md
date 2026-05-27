# Installing ROCm in Ubuntu 14.04.5 on Kaveri 7850K APU

> **Issue #41**
> **状态**: closed
> **创建时间**: 2016-10-25T05:44:39Z
> **更新时间**: 2017-01-03T19:16:38Z
> **关闭时间**: 2017-01-03T19:16:38Z
> **作者**: tqta
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/41

## 描述

Hi, 

I'm having trouble in installing ROCm in Ubuntu 14.04.5. I did a fresh installation of Ubuntu. I turned off the lightdm to make sure there was no conflict with the driver to be installed. 

I got the error message 'The system is running in low-graphics mode. Your screen, graphics card and input device settings could not be detected correctly'. It seems the driver is not detected. 

I also got a warning "[AMD VI] unable to write to IOMMU perf counter" although I turned on the IOMMU in my bios which is Asus A88X-Pro. 

Has anyone had the same problem before? 

Thank you!


---

## 评论 (6 条)

### 评论 #1 — briansp2020 (2016-10-26T00:53:12Z)

What version of BIOS are you using?


---

### 评论 #2 — tqta (2016-10-26T14:13:44Z)

Hi Brian, 

The BIOS version I'm using is 2603 that is the latest version on Asus website. 


---

### 评论 #3 — briansp2020 (2016-10-26T18:10:30Z)

I used to use 7850K APU + Asus A88X-Pro with ROCm 1.2. But now I'm using Intel + Fiji setup. Not sure what the problem maybe.


---

### 评论 #4 — ghost (2016-10-26T18:30:51Z)

What are the actual symptoms of your issue? I.e. what happens when you try to run the vector_copy sample?

Also what is on your full dmesg?

Btw, we are not going out of our way to break Kaveri support, but it is technically an unsupported platform for the current ROCm version. For more info on supported hardware you can look here:
https://radeonopencompute.github.io/hardware.html


---

### 评论 #5 — tqta (2016-10-26T19:26:26Z)

I couldn't get into the log-in window, and the Ubuntu warned "The system is running in low-graphics mode". I suspect the OS didn't detect the driver correctly. 

Andres, the list does not include APU. Will ROCm support future APUs (Carizzo and later)? 


---

### 评论 #6 — ghost (2016-12-06T20:50:24Z)

@tqta - you are describing a problem almost certainly resulting from not having the AMD video driver loaded, and that's not a ROCm problem. 

If you are installing ROCm from repo using instructions on page https://github.com/RadeonOpenCompute/ROCm, then just do a new clean Ubuntu install and do not disable stuff, and follow the instructions. Reboot after doing the install.

Compiling/linking like so should work:

hcc `hcc-config --cxxflags` foo.cpp -c -o  foo.o
hcc `hcc-config --ldflags` foo.o --amdgpu-target=AMD:AMDGPU:7:0:0

"[AMD VI] unable to write to IOMMU perf counter" -- I get that too, not 100% why, but it does not seem to cause problems.

---
