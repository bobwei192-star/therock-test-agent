# Error during installation of rock-dkms 4.0 on 5.4 kernel

> **Issue #1367**
> **状态**: closed
> **创建时间**: 2021-01-24T17:06:27Z
> **更新时间**: 2021-05-31T17:53:17Z
> **关闭时间**: 2021-02-01T06:03:58Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1367

## 描述

I tried on several machines, guest VM or bare-metal, and installation is failing on Ubuntu 20.04.1 with 5.4 kernel which should be supported after going through all the previous steps. There appears to be a build error which informs to look at log file:
I will attach the log file if necessary: 

----------
apt install rocm-dkms -y
----------

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...

....

 - Installation
   - Installing to /lib/modules/5.4.0-42-generic/updates/dkms/

depmod....

DKMS: install completed.
Building initial module for 5.8.0-40-generic
Error! Bad return status for module build on kernel: 5.8.0-40-generic (x86_64)
Consult /var/lib/dkms/amdgpu/4.0-23/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10
Setting up rocm-smi (1.0.0-206-rocm-rel-4.0-23-ge39c0e2) ...
Setting up xtrans-dev (1.4.0-1) ...

....


Setting up rocm-clang-ocl (0.5.0.64-rocm-rel-4.0-23-50fb51a) ...
Setting up rocm-utils (4.0.0.40000-23) ...
Setting up rocm-dev (4.0.0.40000-23) ...
Processing triggers for libc-bin (2.31-0ubuntu9.1) ...
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)


---

## 评论 (19 条)

### 评论 #1 — fwinter (2021-01-24T19:27:48Z)

I had the same problem. Purging the linux image 5.8 solved it for me. It seems the installer tries to build a kernel module for every installed kernel image and for kernel 5.8 it fails to do so.

---

### 评论 #2 — xuhuisheng (2021-01-25T00:19:18Z)

rock-dkms cannot support linux-5.8.0 now, please refer here https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/107

---

### 评论 #3 — ROCmSupport (2021-01-25T06:11:36Z)

Hi @fwinter, 
     Yes, as pointed out by @xuhuisheng , we are not supporting 5.8 currently.  As per your log :

```
Building initial module for 5.8.0-40-generic
Error! Bad return status for module build on kernel: 5.8.0-40-generic (x86_64)
Consult /var/lib/dkms/amdgpu/4.0-23/build/make.log for more information.

```

 your analysis is correct it shall build for each kernel & 5.8 is not supported.  
 Since this has been resolved,  I am closing this. 

Thanks!!

---

### 评论 #4 — patvdleer (2021-01-25T11:54:22Z)

So I looked into the apt history, `/var/log/apt/history.log`, and found:

* rock-dkms:amd64 (1:3.10-29, 1:4.0-23)
* rock-dkms-firmware:amd64 (1:3.10-29, 1:4.0-23)

So looking at the available version it wasn't listed added it manually in `/etc/apt/sources.list.d/rocm.list`
And added the specific version: `deb [arch=amd64] https://repo.radeon.com/rocm/apt/3.10/ xenial main`

Install my previous version:
`sudo apt install rock-dkms=1:3.10-29 rock-dkms-firmware=1:3.10-29`

```
...
Unpacking rock-dkms (1:3.10-29) ...
Setting up rock-dkms (1:3.10-29) ...
Loading new amdgpu-3.10-29 DKMS files...
Building for 5.8.0-38-generic 5.8.0-40-generic
Building for architecture x86_64
Building initial module for 5.8.0-38-generic
Error! Bad return status for module build on kernel: 5.8.0-38-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.10-29/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 rock-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

Which also runs into compiler issues... so now what? This used to work 

---

### 评论 #5 — patvdleer (2021-01-25T12:14:16Z)

Ok so... installed 5.6 via https://kernel.ubuntu.com/~kernel-ppa/mainline/

removed all my 5.8 kernels
`sudo apt remove linux-headers-5.8.0-36-generic linux-headers-5.8.0-38-generic linux-headers-5.8.0-40-generic`

booted the 5.6 kernel, installed 3.10 which now does complete since it doesn't get stuck on 5.8 compiling anymore, reboot and got my screens again...

So from what I gather Ubuntu is pushing kernel 5.8 with rock-dkms which doesn't support it?


---

### 评论 #6 — xuhuisheng (2021-01-25T12:51:12Z)

AMD said they are working on linux-5.8. Maybe ROCm-4.1.

---

### 评论 #7 — gggh000 (2021-01-25T19:08:14Z)

why are you closingthis without resolving this issue?

---

### 评论 #8 — kentrussell (2021-01-26T12:54:53Z)

In the error log in your original message, there is this line:
Consult /var/lib/dkms/amdgpu/4.0-23/build/make.log for more information.
Can you check that file to see where compilation failed? During DKMS installation, the ROCm kernel is compiled and then installed. That failure indicates a build failure. If you look to the bottom of the log, you should see "Error 1" with the actual error (missing header, bad define, etc). That can help us to identify the cause of your installation issue

---

### 评论 #9 — patvdleer (2021-01-26T17:07:22Z)

My issue was with kernel 5.8, not 5.4, currently running 5.6 with ROCm 3.10

---

### 评论 #10 — ROCmSupport (2021-01-27T12:00:36Z)

Hi @gggh000 
Can you please confirm whether you are still observing the issue with 5.4 kernel. If yes, can you please share more details on it.
From your log, it says that its compiling for 5.8 kernel.
_DKMS: install completed.
Building initial module for 5.8.0-40-generic
Error! Bad return status for module build on kernel: 5.8.0-40-generic (x86_64)
Consult /var/lib/dkms/amdgpu/4.0-23/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
installed rock-dkms package post-installation script subprocess returned error exit status 10_

As we are not officially supporting 5.8 for now with ROCm 4.0 and below, request to not to use.
Thank you.

---

### 评论 #11 — gggh000 (2021-01-30T21:26:49Z)

I noticed as @patvdleer mentioned, I had to remove all of 5.8 artifacts, tricky process, after that it works. However the installation is tricky as 5.8 comes inbox with 20.04 version.

---

### 评论 #12 — ROCmSupport (2021-02-01T05:18:53Z)

Thanks @gggh000 for the confirmation.
Yes, as of today, installation is little tricky as Ubuntu 20.04 with 5.8 kernel + ROCm does not work.
ROCm with 5.8 kernel support is very near by, means it will be part of next ROCm release.
Please stay tuned for the updates.
Thank you.

---

### 评论 #13 — vegabook (2021-02-18T12:48:42Z)

It is unacceptable that 4.01s failure to install on the most widely deployed Linux configuration (Ubuntu LTS 20.04), is not VERY CLEARLY STATED in your i[nstallation documentation](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html). 

This is the kind of Rocm documentation slapdash attitude which happens constantly, and is why Cuda is miles ahead. I really do NOT want to have to trade in my FP64-crunching Radeon VII (for which I paid good money, and for which I _expect_ reliable software support), or a the very least, single-location canonical documentation without having to trawl the internet for obscure error messages. 

Virgin Ubuntu 20.04. AMD Ryzen 2700x. AMD Radeon VII. Follow the installation instructions to the letter. And it fails. Without being told right up front "doesn't work yet on kernel 5.8". No no no no no. And especially after your marketing department has made a[ big song and dance about it](https://www.phoronix.com/scan.php?page=article&item=amd-mi100-rocm4&num=1), the average Joe would surely expect it to work. 

With apologies to the devs. This is not a rant at them. It's a rant at making a big noise about "Rocm 4 is here!!" but it doesn't actually work! Make it work first before announcing it! And make the documentation _accurate_ if it doesn't. 

---

### 评论 #14 — Rmalavally (2021-02-18T17:47:16Z)

Thank you for your feedback about ROCm documentation. We are sorry for your experience with our documentation, and we are actively working with the QA and Support teams to resolve the issue. 

AMD ROCm Documentation Team

---

### 评论 #15 — jleni (2021-05-20T19:03:15Z)

any news on this? Are you going to support ubuntu 20.04?

---

### 评论 #16 — ROCmSupport (2021-05-31T09:52:42Z)

Hi @jleni 
ROCm supports Ubuntu 20.04 now so you can start using it
Thank you

---

### 评论 #17 — jleni (2021-05-31T10:22:54Z)

The information in the documentation indicates that:

> The AMD ROCm platform is designed to support the following operating systems:
>
> Ubuntu 20.04.2 HWE (5.4 and 5.6-oem) and 18.04.5 (Kernel 5.4)

Reference: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#prerequisites

Unless this has not been updated, it seems that rocm still does not support a standard Ubuntu 20.04 LTS deployment without having to downgrade the kernel to something that is not standard.

Has this changed? Are you planning to support the default kernel in 20.04 LTS?

---

### 评论 #18 — xuhuisheng (2021-05-31T10:52:54Z)

The kernel-5.8.0-53 on ubuntu-20.04.2 could support ROCm-4.1 properly.
The document needs update.

---

### 评论 #19 — Rmalavally (2021-05-31T17:53:17Z)

Thank you for reaching out. We are working with our internal teams to resolve the documentation issue. 

Please continue to send us your feedback.

AMD ROCm Documentation Team

---
