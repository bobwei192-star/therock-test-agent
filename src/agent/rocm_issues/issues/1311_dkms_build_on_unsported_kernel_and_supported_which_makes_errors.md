# dkms build on unsported kernel and supported which makes errors 

> **Issue #1311**
> **状态**: closed
> **创建时间**: 2020-11-30T18:45:16Z
> **更新时间**: 2021-05-12T09:44:20Z
> **关闭时间**: 2020-12-09T16:56:16Z
> **作者**: Yahia-Ghadiry
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1311

## 描述

I have to kernels 5.8 which came with the os and 5.4 which I installed manually when I try to download using the official guide it tries to build dkms for both kernels which will cause errors due to incompatibility is there a way that I can make the dkms only build for certain kernel(5.4) not 5.8? I know this can be implemented by adding BUILD_EXCLUSIVE_KERNEL="^(5\.[0-6]\.)" to dkms.conf but I don't know how to do that with apt-get

---

## 评论 (18 条)

### 评论 #1 — ROCmSupport (2020-12-01T10:28:18Z)

Hi @yahia20 
Thanks for reaching out.
Can you please update us with OS version and kernel version etc.,. for better understanding of the problem.
Also update the GPU that you are using.

---

### 评论 #2 — Yahia-Ghadiry (2020-12-01T13:54:05Z)

Pop OS 20.10 kernel 5.4 and 5.8 
My GPU is rx 5500xt 

---

### 评论 #3 — ROCmSupport (2020-12-02T07:07:39Z)

Hi @yahia20 
I recommend to boot into 5.4 kernel(through /etc/default/grub or some other way).
Then install rock-dkms which will build and install dkms for 5.4 kernel and it works.
Currently 5.4.0-56 has some issues and so recommend to go with 5.4.0-54 kernel.
Thank you.


---

### 评论 #4 — Yahia-Ghadiry (2020-12-03T15:35:46Z)

okay but when I try to install even when booting into 5.4 it tries to build dkms for both kernels(5.4 and 5.8) which causes it to fail since it's incompatible with 5.8 kernel I can't uninstall 5.8 so how can I make it so that it only builds dkms for 5.4 kernel

---

### 评论 #5 — ROCmSupport (2020-12-04T10:48:23Z)

Can you please share the output of below commands.
_uname -r
dkms status_


---

### 评论 #6 — ROCmSupport (2020-12-04T10:52:06Z)

Can you please try the following in your machine loaded with 5.4 kernel.
Make a note that, ROCm installation fails on 5.4.0-56 kernel, which is a known problem. See #1307 and #1315 

If your machine does not have above kernel, recommend to try the below.
_sudo dkms remove amdgpu/3.10-27 --all
sudo dkms add amdgpu/3.10-27
sudo dkms install amdgpu/3.10-27_

---

### 评论 #7 — Yahia-Ghadiry (2020-12-05T13:01:34Z)

uname -r
5.4.0-54-generic

dkms status
amdgpu, 3.9-19, 5.4.0-54-generic, x86_64: installed (original_module exists)
 
sudo dkms remove amdgpu/3.10-27 --all
Error! The module/version combo: amdgpu-3.10-27
is not located in the DKMS tree.

 sudo dkms add amdgpu/3.10-27
Error! Could not find module source directory.
Directory: /usr/src/amdgpu-3.10-27 does not exist.

 sudo dkms install amdgpu/3.10-27
Error! Could not find module source directory.
Directory: /usr/src/amdgpu-3.10-27 does not exist.

but when I try installing rocm-dkms I get this:

`......
Loading new amdgpu-3.9-19 DKMS files...
Building for 5.4.0-54-generic 5.8.0-7630-generic
Building for architecture x86_64
Building initial module for 5.4.0-54-generic
Done.
Forcing installation of amdgpu

amdgpu.ko:
Running module version sanity check.
 - Original module
   - Found /lib/modules/5.4.0-54-generic/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko
   - Storing in /var/lib/dkms/amdgpu/original_module/5.4.0-54-generic/x86_64/
   - Archiving for uninstallation purposes
 - Installation
   - Installing to /lib/modules/5.4.0-54-generic/updates/

amdttm.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/5.4.0-54-generic/updates/

amdkcl.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/5.4.0-54-generic/updates/

amd-sched.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/5.4.0-54-generic/updates/

depmod...

DKMS: install completed.
Building initial module for 5.8.0-7630-generic
ERROR (dkms apport): kernel package linux-headers-5.8.0-7630-generic is not supported
Error! Bad return status for module build on kernel: 5.8.0-7630-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.9-19/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10
Setting up rocm-smi (1.0.0-206-rocm-rel-3.9-19-ge39c0e2) ...
Setting up rocm-dbgapi (0.36.0-rocm-rel-3.9-19) ...
Setting up libelf-dev:amd64 (0.181-1) ...
Setting up amdgpu-core (20.45-1164792) ...
Setting up libbabeltrace1:amd64 (1.5.8-1build1) ...
dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
No apport report written because the error message indicates its a followup error from a previous failure.
                                                                                                          Setting up hip-doc (3.9.20412-
6d111f85) ...
Setting up hsakmt-roct (20200924.0.55-mainline-20200924-0-gcd55f1f) ...
Setting up libtinfo5:amd64 (6.2-1) ...
Setting up hip-samples (3.9.20412-6d111f85) ...
Setting up libbabeltrace-ctf1 (1.5.8-1build1) ...
Setting up hsa-rocr-dev (1.2.30901.0-rocm-rel-3.9-19-75f9b74a) ...
Setting up libncurses5:amd64 (6.2-1) ...
Setting up libllvm10.0-amdgpu:amd64 (1:10.0-1164792) ...
Setting up rocm-gdb (9.2-rocm-rel-3.9-19) ...
Setting up rocm-opencl (3.6Beta-14-g0c40e05-rocm-rel-3.9-19) ...
Setting up llvm-amdgpu-10.0-runtime (1:10.0-1164792) ...
Setting up hsakmt-roct-dev (20200924.0.55-mainline-20200924-0-gcd55f1f) ...
Setting up llvm-amdgpu-10.0 (1:10.0-1164792) ...
Setting up llvm-amdgpu-runtime (1:10.0-1164792) ...
Setting up llvm-amdgpu-10.0-dev (1:10.0-1164792) ...
Setting up rocm-opencl-dev (3.6Beta-14-g0c40e05-rocm-rel-3.9-19) ...
Setting up rocprofiler-dev (1.0.0) ...
Setting up llvm-amdgpu (1:10.0-1164792) ...
Setting up rocm-clang-ocl (0.5.0.64-rocm-rel-3.9-19-50fb51a) ...
Setting up openmp-extras (12.9-0) ...
Setting up rocm-utils (3.9.1.30901-19) ...
Setting up hip-rocclr (3.9.20412-6d111f85) ...
Setting up rocm-dev (3.9.1.30901-19) ...
Processing triggers for man-db (2.9.3-2) ...
Processing triggers for libc-bin (2.32-0ubuntu3) ...
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)`

---

### 评论 #8 — fgnm (2020-12-06T11:59:52Z)

Using 5.6.0 Kernel fixed the compiling issue, I had to update because even switching to 5.4.0-54 compiling fails.

---

### 评论 #9 — Yahia-Ghadiry (2020-12-06T14:58:18Z)

I did once try 5.6 but it would still try to build for 5.8 which I can't delete because a lot of system packages depends on it 

---

### 评论 #10 — ROCmSupport (2020-12-07T08:57:55Z)

Hi @yahia20 
I will gather more information.
Thank you.

---

### 评论 #11 — Yahia-Ghadiry (2020-12-07T19:50:45Z)

ok thanks

---

### 评论 #12 — ROCmSupport (2020-12-08T04:54:42Z)

Hi @yahia20 
Request you to do the below way.

If required kernel is available in the repository you'll need to pre-install it with matching linux-headers package, 
for example: **apt install linux-image-5.4.0-53-generic linux-headers-5.4.0-53**
Boot into that kernel and install rock-dkms. 
Dkms simply skips the build for 5.4 and builds only for that kernel that has headers installed.

---

### 评论 #13 — Yahia-Ghadiry (2020-12-08T15:06:54Z)

I have used the following packages to install kernel 5.4:
linux-headers-5.4.0-54_5.4.0-54.60_all.deb            
linux-modules-5.4.0-54-generic_5.4.0-54.60~18.04.1_amd64.deb
linux-headers-5.4.0-54-generic_5.4.0-54.60_amd64.deb  
linux-modules-extra-5.4.0-54-generic_5.4.0-54.60_amd64.deb
linux-image-5.4.0-54-generic_5.4.0-54.60_amd64.deb 

I got them from ubuntu archive (because I can't get them with apt)when I boot into the kernel and try to install but the problem persists I have both 5.4 and 5.8 headers installed due to some packages are depend on  5.8 

I had the same issue when I tried to install amdgpu-pro drivers the solution is that I unpacked the dkms deb package and added  BUILD_EXCLUSIVE_KERNEL="^(5.[0-6].)" line to dkms.conf but I want to use rocm 

Is there a way that I can download all the deb packages and install them manually so that I can try the same fix?

---

### 评论 #14 — kentrussell (2020-12-09T12:58:30Z)

In general, the DKMS install (and any DKMS install via apt) will use these criteria to determine what kernel to install onto:
1) Try install it on the currently booted kernel
    a) If linux-headers-$(uname -r) are present, install it on that kernel
    b) If linux-headers-$(uname -r) aren't present, don't install

Since you've got the 5.8 headers installed, you'd need to downgrade or remove them, and install the 5.4 ones. We're using the same packaging as amdgpu-pro, so you'll be stuck with that method there, at least for the initial installation.

Once you have the rock-dkms installed on one kernel, you can use "dkms build amdgpu/<version> -k `uname -r`/x86_64" and then "dkms install  amdgpu/<version> -k `uname -r`/x86_64" to install it on that kernel, or "dkms remove amdgpu<version> -k <kernelversion>" to remove it from a specific kernel version.

By default, apt only installs it on the booted kernel. To try to install it on a different kernel, you either need to modify dkms as you did there, or manually add/remove it for the desired kernels using the dkms application. It's sub-optimal, but unfortunately it leaves us at the mercy of apt, and it doesn't allow for choosing the kernel for DKMS packages, you've got to get around it by using the dkms functionality. Sorry I don't have better news in that regard, but at least you have one workaround available there.

---

### 评论 #15 — Yahia-Ghadiry (2020-12-09T16:56:16Z)

I ended up fixing the issue by: getting the dkms deb from https://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms_3.10-27_all.deb and then unpacking it using:   dpkg-deb -R rock-dkms_3.10-27_all.deb.deb tmp
then edited tmp/usr/src/amdgpu-3.10-27/dkms.conf 
added line : BUILD_EXCLUSIVE_KERNEL="^(5.[0-6].)"
then repacked it using : dpkg-deb -b tmp rock-dkms_3.10-27_all.deb.deb
and installed it using: sudo dpkg -i rock-dkms_3.10-27_all.deb.deb
then installed rocm-dkms using the default sudo apt-get install rocm-dkms and I am in the process of completing the install but so far no errors

---

### 评论 #16 — ROCmSupport (2020-12-10T04:06:31Z)

Thanks @yahia20 for the closure.
Thank you.

---

### 评论 #17 — cloudishBenne (2021-05-10T22:50:39Z)

@yahia20 can this solution be permanent for limiting the package to a specific kernel? so when i run `apt update && apt upgrade` this will only install to the kernel versions i want? and when there is a new version of rocm which has support for a newer kernel i can simply edit the dkms.conf file to match this new condition? is it possible to store the dkms.conf file in a nice place where it will be read when updating? i think this would be a nice solution for this problem. i think there are more people out there having multiple kernel versions for multiple usecases that don't want to have a second system.

---

### 评论 #18 — Yahia-Ghadiry (2021-05-12T09:44:20Z)

@cloudishBenne probably not but I have given up on it as it caused me more bugs the more I try to make resolve work.

---
