# Documentation for OpenCL-only ROCm install

> **Issue #474**
> **状态**: closed
> **创建时间**: 2018-07-27T10:13:57Z
> **更新时间**: 2020-02-10T15:57:00Z
> **关闭时间**: 2018-09-14T22:41:58Z
> **作者**: preda
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/474

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Looking at this page https://github.com/RadeonOpenCompute/ROCm for installation instructions,
I install rocm-dkms. But this package install many other dependencies:
dkms hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs rocm-smi rocm-utils rocminfo

I would like instructions for installing a minimal OpenCL-only ROCm. For example, is "hcc" needed for an OpenCL-only install?


---

## 评论 (40 条)

### 评论 #1 — BryantLam (2018-07-27T22:57:13Z)

Try installing only `rocm-opencl-dev` or `rocm-opencl-devel`. It should also install `rocm-opencl` as a dependency.

---

### 评论 #2 — preda (2018-07-28T00:13:03Z)

I tried rocm-opencl only, and that was not enough (clinfo didn't detect any platform). I expected that -dev installs additionally only include headers (relative to rocm-opencl); if that's so then it's not enough. But I'll try next time I do a ROCm install.

---

### 评论 #3 — preda (2018-07-28T09:51:23Z)

Yep I confirm, installing rocm-opencl-dev (which pulls rocm-opencl too) does not do it. It installs the libOpenCL library, but OpenCL is not functional.

---

### 评论 #4 — Angel996 (2018-07-29T20:57:46Z)

How can we have OpenCL functional with ROCM 1.8.192?

---

### 评论 #5 — preda (2018-07-29T22:41:25Z)

Installing "rocm-dkms" pulls in everything OpenCL needs (and presumably more), and produces a working OpenCL installation.

---

### 评论 #6 — Angel996 (2018-07-29T23:01:10Z)

No, in fact it does not. After 1.8.192 installation `lspci -vv` yields supposedly working driver installation (kernel driver in use: amdgpu), however clinfo reports 

> Number of OpenCL platforms: 0

No legacy OpenCL application can actually see the GPUs. Tried kernels 4.4.0-112/116/131.

---

### 评论 #7 — preda (2018-07-29T23:50:44Z)

What OS / Linux kernel are you installing on? in my case it worked with Ubuntu 18.04 and kernel 4.15.


---

### 评论 #8 — jlgreathouse (2018-07-30T05:20:42Z)

The problem @Angel996 is seeing is most likely related to what is being discussed in #479 . @Angel996 is unable to see any OpenCL devices because there are no working GPU devices in the system.

I suspect that issue and this issue are unrelated, as it is not an OpenCL problem in particular.

---

### 评论 #9 — Angel996 (2018-07-30T12:12:25Z)

No, it is not related to #479. The #479 is about 4.13 kernel problem, not even ROCM, however, it is referenced in ROCM manual, that's why I mentioned it here.

This one is about not being able to use legacy OpenCL devices. The amdgpu-pro package has a command line option  `--opencl=legacy,pal --headless` that adds support for legacy OpenCL. If this command line option is not used, amdgpu-pro yields the same result: _Kernel driver in use: amdgpu_  reported by _lspci_, yet 0 OpenCL devices reported by _clinfo_.

ROCM needs something like that `--opencl=legacy` thing too, I guess.

---

### 评论 #10 — jlgreathouse (2018-07-30T19:24:58Z)

@Angel996 , if you have a working ROCm installation, OpenCL should work for you. Simply having amdgpu loaded for your graphics card is not enough, as ROCm requires a slightly modified amdgpu (this will be fixed in upcoming kernel releases, as we are upstreaming our changes), as well as the amdkfd driver, ROCt thunk layer, etc.

In addition, just because these drivers are loaded does not mean that ROCm is successfully running. For instance, as I mentioned in #479, if your hardware does not properly meet some requirements (such as PCIe gen 3 with atomics support), then you may not be able to successfully communicate with the GPU.

If, after installing ROCm, you try to run `/opt/rocm/bin/rocminfo` and it fails (please make sure you are in the 'video' group before doing this), then you do not have a successfully working ROCm installation and, yes, OpenCL will not work.

I believe this issue is specifically asking for a way to install ROCm but avoid installing packages such as HCC, HIP, ROCm-SMI, etc. I'm currently looking into that question, but I think conflating a non-working ROCm installation, or OpenCL not working on top of a working ROCm installation, with this issue will end up confusing things. That, in my opinion, should be a separate ticket.

---

### 评论 #11 — jlgreathouse (2018-07-30T20:51:30Z)

@preda I just tried a fresh installation of ROCm on Ubuntu 16.04.4 LTS using the follow commands and was able to get some OpenCL test applications working:
```
sudo apt-get -y update; sudo apt-get -y upgrade
sudo apt-get -y install libnuma-dev
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add 
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
sudo apt update
sudo apt-get install dkms rock-dkms rocm-clang-ocl rocm-opencl rocm-opencl-dev
sudo usermod -a -G video ${LOGNAME}
sudo reboot
```
Note that this won't install `clinfo`, but if you have a copy sitting around (or if you get it our [OpenCL runtime GitHub](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime)) you should be able to see your GPU devices. I was able to run some separate OpenCL test applications after running the above commands.

(You might be able to get away with skipping the install of `rocm-clang-ocl`. I didn't want to go back and start from scratch just to test that. :)  )

---

### 评论 #12 — preda (2018-07-31T05:58:59Z)

Yes, thanks; I can install ROCm with OpenCL with just "sudo apt install rocm-dkms" which seems to pull as dependencies all the OpenCL stuff.

But I think that right now rocm-dkms may install too much for somebody interested in OpenCL only. E.g. it installs "hcc", which is a big package (~ 400MB), and which I don't know whether is needed for OpenCL at all.

So I was thinking to mention somewhere in the docs, the *minimal* set of packages to install if one wants OpenCL *only*.

---

### 评论 #13 — jlgreathouse (2018-07-31T15:41:47Z)

Hello @preda,

Note that the commands I included above are not installing roc**m**-dkmos, but roc**k**-dkms. As such, I was attempting to give yo ua minimal set of packages to install if one wants OpenCL only.

The list I show above does not install e.g. hcc, and so it should significantly decrease the amount of software installed. It should, however, successfully run OpenCL applications.

Could you try that set of commands and tell me if it works for your needs?

---

### 评论 #14 — preda (2018-07-31T21:21:40Z)

@jlgreathouse sorry my bad reading. Yes I'll try this and report back.

---

### 评论 #15 — preda (2018-08-01T00:14:09Z)

sudo apt install rock-dkms rocm-clang-ocl
worked for me. rocm-clang-ocl pulls as dependencies rocm-opencl and rocm-opencl-dev. Next time I'll try without rocm-clang-ocl and see how it goes.


---

### 评论 #16 — rkothako (2018-08-01T03:28:49Z)

@preda 
ROCm is a full compute stack, in which every top layer depends on ROCk(KFD driver), ROCr(Base HSA Runtime) and ROCt(thunk interface).

So if you need only OpenCL only ROCm means, need to install ROCk, ROCr, ROCt before installing OpenCL.
So need to run as below, which covers everything needed for OpenCL.
sudo apt install rock-dkms rocm-opencl-dev

---

### 评论 #17 — cryptomilk (2018-08-03T08:06:38Z)

If I strace clinfo I get:

```
openat(AT_FDCWD, "/lib64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
munmap(0x7f8953b6c000, 272408)          = 0
openat(AT_FDCWD, "./libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "./libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
```

It tries to load libamdoclcl64.so which doesn't exist.

`Number of platforms                               0`

---

### 评论 #18 — rkothako (2018-08-03T10:10:50Z)

@cryptomilk 
How did you install? What are all commands you followed?
Please provide. Thank you.


---

### 评论 #19 — cryptomilk (2018-08-03T10:39:31Z)

```dnf install /home/asn/Downloads/rocm/rocm-clang-ocl-0.3.0-7997136-Linux.rpm /home/asn/Downloads/rocm/rocm-opencl-devel-1.2.0-2018071635.x86_64.rpm /home/asn/Downloads/rocm/rocm-opencl-1.2.0-2018071635.x86_64.rpm /home/asn/Downloads/rocm/hsakmt-roct-1.0.8-1-ge3dd067-Linux.rpm /home/asn/Downloads/rocm/hsa-rocr-dev-1.1.8-15-ge851b7a-Linux.rpm```

The following code seems to try to load the library:

https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/master/runtime/device/rocm/rocdevice.cpp#L196

It looks like the RPMs got build with: WITH_COMPILER_LIB


libamdocl64.so tries to load libamdoclcl64.so

---

### 评论 #20 — preda (2018-08-24T00:39:37Z)

"sudo apt install rock-dkms rocm-opencl" is the answer to the original question ("minimal OpenCL install"), and should get a working clinfo. Maybe this info could be added to the install page, and this issue closed.

---

### 评论 #21 — jlgreathouse (2018-08-24T00:43:33Z)

I'm currently leaving this open because I need to wrap back around and figure out how to do the same "minimal" installation for RHEL/CentOS. I have the "minimal OpenCL" directions in the main README.md of the ROCm repo, but I also need to get it into all our other various installation direction pages.

---

### 评论 #22 — rkothako (2018-08-24T13:59:59Z)

Hi @jlgreathouse 

I have already mentioned https://github.com/RadeonOpenCompute/ROCm/issues/474#issuecomment-409437703
**We have verified and its working for both Ubuntu and CentOS.**

For Ubuntu: sudo apt install rock-dkms rocm-opencl-dev --> does OpenCL only ROCm
For CentOS: sudo yum install rock-dkms rocm-opencl-devel --> does OpenCL only ROCm

You can close this.

---

### 评论 #23 — cryptomilk (2018-08-28T09:53:36Z)

I didn't install rock-dkms, but with Linux Kernel 4.18 it works just fine if you install rocm-opencl-devel.

---

### 评论 #24 — rkothako (2018-08-28T10:09:27Z)

Hi @cryptomilk 
sudo apt install rocm-opencl-dev will not install rock-dkms on its own. It installs OpenCL and its dependent ROCr(hsa) runtime files.
We need to explicitly install rock-dkms along with rocm-opencl-dev.

---

### 评论 #25 — cryptomilk (2018-08-28T10:13:58Z)

I'm just saying that if you run Kernel 4.18 you don't have to install rock-dkms. The driver will offer the required features.

---

### 评论 #26 — rkothako (2018-08-28T12:26:57Z)

@cryptomilk 
My Ubuntu has 4.15 kernel, how to switch to 4.18.?

---

### 评论 #27 — cryptomilk (2018-08-28T13:20:17Z)

If you don't have Kernel 4.18 you need to install the rock-dkms package which provides a newer amdgpu driver for the kernel.

---

### 评论 #28 — rkothako (2018-08-28T13:54:26Z)

Thanks @cryptomilk 
Can you please let know what are all steps you followed, so that I will also follow the same to replicate here for 4.18 kernel

---

### 评论 #29 — cryptomilk (2018-08-28T15:13:35Z)

I'm sorry, I can't help you I don't use Ubuntu.

---

### 评论 #30 — Srinivasuluch (2018-08-29T12:16:38Z)

Hi @cryptomilk  - Can you check whether kfd node enabled ? the libamdoclcl64.so should not be the root cause
`#cd /sys/devices/virtual/kfd/kfd/topology/nodes`

You should see more than "0" node.

> 0 for CPU
> 1, 2, .... for GPUs


---

### 评论 #31 — cryptomilk (2018-08-29T12:27:11Z)

`/sys/devices/virtual/kfd/kfd/topology/nodes` has two nodes 0 and 1.

---

### 评论 #32 — Srinivasuluch (2018-08-29T12:37:59Z)

@cryptomilk  : Go to node "1" and check the properties.
`#cat properties`
can you give the console output?

---

### 评论 #33 — cryptomilk (2018-08-29T12:39:24Z)

@Srinivasuluch  here you go:

```
$ cat 1/properties 
cpu_cores_count 0
simd_count 128
mem_banks_count 1
caches_count 50
io_links_count 1
cpu_core_id_base 0
simd_id_base 2147487744
max_waves_per_simd 10
lds_size_in_kb 64
gds_size_in_kb 0
wave_front_size 64
array_count 4
simd_arrays_per_engine 1
cu_per_simd_array 9
simd_per_cu 4
max_slots_scratch_cu 32
vendor_id 4098
device_id 26591
location_id 256
drm_render_minor 128
max_engine_clk_fcompute 1260
local_mem_size 0
fw_version 723
capability 4736
max_engine_clk_ccompute 4000
```

---

### 评论 #34 — Srinivasuluch (2018-08-29T13:05:11Z)

@cryptomilk  : Can you give following output aswell ? Suspecting device_id 26591
`lspci | grep VGA`

---

### 评论 #35 — cryptomilk (2018-08-29T13:27:00Z)

The GPU is a RX 470

```
magrathea:~ # lspci | grep VGA
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X] (rev cf)
```

---

### 评论 #36 — jlgreathouse (2018-08-30T20:08:21Z)

@rkothako I can verify that your directions for an OpenCL-only installation on CentOS 7.5 work for me. I'll add them to the ROCm README.

@cryptomilk are you still running into the issue you mentioned [above](https://github.com/RadeonOpenCompute/ROCm/issues/474#issuecomment-410178531)? It appears that in that install line, you did not install the ROCK kernel driver package.

I was able to manually install ROCm on CentOS 7.5 with the following commands. Note that this obviously isn't the most efficient way of doing it, but it handles installing things in the right order and shows each step. Note that I had to [manually install DNF](https://www.ostechnix.com/install-dnf-centos-7/) because it's not included in CentOS 7.x, I believe you should be able to do this with yum instead, but I was trying to match your use of `dnf`.
```shell
# Using DNF version 0.6.4 on CentOS 7.5
# This should be done after installing Devtoolset-7, dkms, and your kernel headers.
# Download RPMs
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/o/ocl-icd-2.2.12-1.el7.x86_64.rpm
wget http://repo.radeon.com/rocm/yum/rpm/hsakmt-roct-1.0.8-2-g2076b0c-Linux.rpm
wget http://repo.radeon.com/rocm/yum/rpm/hsa-rocr-dev-1.1.8-15-ge851b7a-Linux.rpm
wget http://mirror.centos.org/centos/7/updates/x86_64/Packages/kernel-devel-3.10.0-862.11.6.el7.x86_64.rpm
wget http://repo.radeon.com/rocm/yum/rpm/rock-dkms-1.8-199.el7.noarch.rpm
wget http://repo.radeon.com/rocm/yum/rpm/rocm-opencl-1.2.0-2018082827.x86_64.rpm
# Install RPMs one by one
sudo dnf install ./ocl-icd-2.2.12-1.el7.x86_64.rpm
sudo dnf install ./hsakmt-roct-1.0.8-2-g2076b0c-Linux.rpm
sudo dnf install ./hsa-rocr-dev-1.1.8-15-ge851b7a-Linux.rpm
sudo dnf install ./kernel-devel-3.10.0-862.11.6.el7.x86_64.rpm
sudo dnf install ./rock-dkms-1.8-199.el7.noarch.rpm
sudo dnf install ./rocm-opencl-1.2.0-2018082827.x86_64.rpm
# Add user to video group
sudo add user -a -G video $LOGNAME
sudo reboot
```

After rebooting, I was able to properly see the device when checking `/opt/rocm/opencl/bin/x86_64/clinfo`.

As such, I would like to close this ticket.

---

### 评论 #37 — rkothako (2018-08-31T03:32:20Z)

Thanks 

---

### 评论 #38 — valeriob01 (2019-08-26T18:25:56Z)

> "sudo apt install rock-dkms rocm-opencl" is the answer to the original question ("minimal OpenCL install"), and should get a working clinfo. Maybe this info could be added to the install page, and this issue closed.

On Debian 10 I have attempted this install procedure, I also needed to pull rocm-opencl-dev and rocm-smi by hand.


---

### 评论 #39 — jboero (2020-02-10T15:29:39Z)

> If I strace clinfo I get:
> 
> ```
> openat(AT_FDCWD, "/lib64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
> openat(AT_FDCWD, "/usr/lib64/libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
> munmap(0x7f8953b6c000, 272408)          = 0
> openat(AT_FDCWD, "./libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
> openat(AT_FDCWD, "./libamdoclcl64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
> ```
> 
> It tries to load libamdoclcl64.so which doesn't exist.
> 
> `Number of platforms 0`

@cryptomilk
Hi I know this is an older thread but this has been driving me nuts too for days and I figured I'd put the workaround in here for record.  The fix is painfully pathetic.  There is a typo - it should be looking for "libamdocl64.so" but someone fat fingered "libamdoclcl64.so" which is redundant. I managed to supress it working by symlinking my rocm "libamdocl64.so" to "/usr/lib64/libamdoclcl.so" which fixes the errors (warnings as the original libamdocl64.so is actually loaded anyway) and I can finally use ROCm for OpenCL.  (ROCm 3.0 with LD_LIBRARY_PATH set to '/opt/rocm/lib64;/opt/rocm/lib')

```
$  clinfo -l
Platform #0: AMD Accelerated Parallel Processing
 `-- Device #0: gfx803
Platform #1: NVIDIA CUDA
 `-- Device #0: Quadro RTX 4000
```

---

### 评论 #40 — cryptomilk (2020-02-10T15:57:00Z)

Normally you don't need need libamdoclcl64.so. This shipped with the proprietary driver. However there seems to be a bug in ROCm 3.0 and it looks like one fix is symlinking to libamdoclcl64.so

See also https://github.com/RadeonOpenCompute/ROCm/issues/977

---
