# Support Ubuntu 22.04 LTS (Jammy Jellyfish)

> **Issue #1730**
> **状态**: closed
> **创建时间**: 2022-04-23T00:47:49Z
> **更新时间**: 2022-11-29T18:30:32Z
> **关闭时间**: 2022-11-17T17:13:17Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1730

## 描述

Ubuntu 22.04 LTS (Jammy Jellyfish) is the current LTS version of Ubuntu.

https://ubuntu.com/blog/ubuntu-22-04-lts-released

@ROCmSupport repeatedly promised support it once it is out:

https://github.com/RadeonOpenCompute/ROCm/issues/1590#issuecomment-942093569
https://github.com/RadeonOpenCompute/ROCm/issues/1612#issuecomment-965049119

Please fulfill that promise by stating official support in documentation, and also by providing an official release of ROCm that works with this version of Ubuntu.

The absence of a working release is already leading to issues:

https://github.com/RadeonOpenCompute/ROCm/issues/1713


---

## 评论 (62 条)

### 评论 #1 — moultonsa (2022-04-25T18:17:54Z)

Agreed.    I have researchers waiting on this.

---

### 评论 #2 — Bengt (2022-04-25T18:43:10Z)

I am such a researcher, stuck with an outdated OS. :/

---

### 评论 #3 — BloodyIron (2022-05-05T17:34:52Z)

Does AMD even care about OpenCL on consumer GPUs on Linux? You know, the feature that is literally sold on the box? Because I have seen zero evidence that AMD has interest in providing OpenCL working on Linux for consumer GPUs since like ROCm v3.3 for RX 580-era GPUs.

As I have said again in the past, this is why I'm buying nVidia. AMD seems literally unwilling to provide a means to run the AMDGPU (NON PRO) driver on Linux with a means to have OpenCL on consumer GPUs (whether it's ROCm or otherwise). Why even bother spending money for features they advertise but don't deliver on? It's been... 2 years now?

---

### 评论 #4 — keryell (2022-05-06T06:08:01Z)

@BloodyIron I will ask internally.

---

### 评论 #5 — BloodyIron (2022-05-07T03:59:58Z)

@keryell I really hope that AMD takes it seriously :/ Thanks for asking internally :)

---

### 评论 #6 — lionelchauvin (2022-05-12T09:57:26Z)

@ROCmSupport can you share AMD plans about Ubuntu support ?

Today nvidia published their kernel driver as open-source and they adjusted their closed-source CUDA driver to make it work with it. I am sure it will soon be packaged for Ubuntu LTS, Non LTS indifferently.


---

### 评论 #7 — Bengt (2022-05-12T21:25:27Z)

For future reference:

https://developer.nvidia.com/blog/nvidia-releases-open-source-gpu-kernel-modules/

The situation on the Nvidia side is quite complex, with closed-source firmware and user-space software. However, by releasing the kernel module as open source software, they enabled lots of possible improvements, like the already-activated DMA-BUF. Note that Nvidia did not release their compute component CUDA as open source, which is equivalent to AMD's ROCm, we are concerned about here. So technically, AMD is still ahead in terms of open-source support, which is, of course, the best way of being ahead. Still, in order for them to stay relevant, AMD urgently needs to release their ROCm packages in a version that is compatible with relevant operating systems. Every day that goes by without proper support is an incentive to turn the back on AMD products and in parallel Nvidia is ramping support for theirs.

---

### 评论 #8 — Laitaps (2022-05-18T13:45:50Z)

First and foremost, things need to work.  I am all in favor of open source and the AMD strategy here to be sure.  However, presently it is of little utility for me as I do not have functional AMD hardware upon which to develop my software.  I could revert to 20.04 as well, but that isn't really my point.  It is not unreasonable to expect support upon the launch of each new Ubuntu LTS.  Some of the arguments I have read elsewhere are becoming a little long in the tooth.

While some are arguing in support of AMD by saying that it is not "fair" because AMD is open source is a bit disingenuous.  This is not a small group of hackers reverse engineering a driver for an RGB keyboard here.  Open source or not, this is largely the effort of a multi-billion-dollar multinational corporation.  If insufficient resources are being committed by AMD, that is an AMD problem.  I want to see more competition in this space and better product offerings among multiple vendors.  However, for that to happen, AMD is going to have to step up and start supporting their hardware much better.  In a few months, Ada will launch, and if this issue is not resolved by then, I and many others will simply opt for less of a headache and migrate to Nvidia hardware.  At the end of the day, we need to get things done and this situation is deeply unhelpful.

---

### 评论 #9 — DrBlackross (2022-05-19T11:02:41Z)

Kinda, beating a dead horse kinda question....

But, how do you jump over 22.04 to 22.10 on https://repo.radeon.com/amdgpu-install/ ? Was reading the pdf from the rocm 5.11 tarball release, been trying to fix opencl with rocm (since i updated to 22.04, lol, decades later still same issues with linux and graphic cards).

Sidenote: It wants to install on 22.04 with amdgpu-install, just can't find amdgpu-lib, amdgpu-lib32, rocm-opencl-runtime, rocm-hip-runtime... just don't want to reinstall or downgrade. Like i said before, decades of this, make menuconfig and compile it in the kernel would be nice.

---

### 评论 #10 — Bengt (2022-05-19T12:30:14Z)

@DrBlackross Your request for ROCm to support Ubuntu 22.10 is off-topic in this issue about supporting Ubuntu 22.04. Please open a separate issue about that.

---

### 评论 #11 — lionelchauvin (2022-05-19T16:16:18Z)

@Bengt DrBlackross talks about Radeon™ Software for Linux® 22.10 on Ubuntu 22.04, not Ubuntu 22.10
Yes, this number version is confusing.
 

---

### 评论 #12 — Bengt (2022-05-19T17:59:31Z)

@lionelchauvin, ah, I see. Thanks for the clarification. Is this repository the right place to report issues about AMD/Radeon Software for Linux?

---

### 评论 #13 — lionelchauvin (2022-05-20T08:01:11Z)

@Bengt Perhaps I misunderstood too and he was talking about amdgpu 22.10.

Anyway I don't understand why Radeon™ Software for Linux® 22.10.2 (that contains rocm) has been released without the support of the most popular linux distribution. (https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-22-10-2)



---

### 评论 #14 — keryell (2022-05-20T14:55:42Z)

> Anyway I don't understand why Radeon™ Software for Linux® 22.10.2 (that contains rocm) has been released without the support of the most popular linux distribution.

@lionelchauvin I guess because it targets only the HPC  and datacenter ML niches?

---

### 评论 #15 — keryell (2022-05-20T15:07:03Z)

> I really hope that AMD takes it seriously :/ Thanks for asking internally :)

@BloodyIron following the recent GitHub discussions, a meeting was organized last week with 19 AMD employees attending. So, some people care and I can see more activity on GitHub now.
Let's see how far this flies... :-)

---

### 评论 #16 — BloodyIron (2022-05-20T16:04:04Z)

> > I really hope that AMD takes it seriously :/ Thanks for asking internally :)
> 
> @BloodyIron following the recent GitHub discussions, a meeting was organized last week with 19 AMD employees attending. So, some people care and I can see more activity on GitHub now. Let's see how far this flies... :-)

Thanks for letting me know! :D 

---

### 评论 #17 — lionelchauvin (2022-05-20T16:36:27Z)

> > Anyway I don't understand why Radeon™ Software for Linux® 22.10.2 (that contains rocm) has been released without the support of the most popular linux distribution.
> 
> @lionelchauvin I guess because it targets only the HPC and datacenter ML niches?

I doubt it is the unique reason because Amdvlk is supposed to target customers and has the same treatment.

---

### 评论 #18 — keryell (2022-05-20T17:20:30Z)

> I doubt it is the unique reason because Amdvlk is supposed to target customers and has the same treatment.

@lionelchauvin Just looking at the description of https://github.com/RadeonOpenCompute/ROCm it says *ROCm - Open Source Platform for HPC and Ultrascale GPU Computing*. But I hope it should be updated to work also on machines cheaper than $10M. ;-)


---

### 评论 #19 — BloodyIron (2022-05-20T18:54:43Z)

Yes, and ROCm is the only way to get OpenCL for consumer GPUs while using the AMDGPU driver, which is the preferred driver for gaming, as AMDGPU-Pro has worse performance for gaming. So while that may be what it says _now_, the ROCm suite has been the way to get OpenCL for years now for consumer GPUs when using AMDGPU. So I don't frankly care that it says it's for "HPC and Ultrascale GPU" without mentioning consumer usage. If AMD is not going to expose OpenCL in a way that works with AMDGPU drivers then they should frankly fully remove the declaration of OpenCL on the box for consumer GPUs considering Linux (and gaming on Linux) is a supported platform and use, supposedly.

---

### 评论 #20 — roblem (2022-05-23T06:20:59Z)

Another researcher (not gamer) that is waiting for 22.04 support.  I have 2 Radeon VII's that [**will not work**](https://github.com/RadeonOpenCompute/ROCm/issues/1431) with upstream radeon driver and Rocm unless the kernel/upstream kmods is fairly recent.  This more recent kernel is not available under 20.04.  It is available for 22.04.  So this support is required for operability of hardware, and downgrading to 20.04 won't solve the issue.

---

### 评论 #21 — Laitaps (2022-05-29T18:00:06Z)

I feel your pain.  Unfortunately, it appears that support for the most recent Ubuntu LTS is not a priority.  

---

### 评论 #22 — BloodyIron (2022-05-30T21:17:51Z)

I guess delivering on what is advertised on the box is not a priority...

---

### 评论 #23 — Bengt (2022-05-30T22:05:31Z)

Are GPUs sold with Ubuntu LTS support advertised on the box? Can you please share?

---

### 评论 #24 — Laitaps (2022-05-31T15:07:00Z)

@Bengt Wouldn't that be amazing!  AMD claims support (on their website) for certain Ubuntu LTS releases and makes no specific claims regarding future support for new releases (to be clear).  Though one would conclude that if you are intent on supporting Linux, it may be a good idea to get ahead of the curve with respect to what is probably the most widely used Linux Distro (if you include flavors).

This is not an issue of some sort of false advertising as some seem to be claiming.  Just a lack of desire to commit adequate resources.  When your competitor dominates the field (for AI) it is probably most profitable to invest more resources in design wins for large deployments that use specialized environments.  Unless more funds are allocated, this necessarily results in fewer resources assigned to supporting the newer OS releases used by a less profitable group of researchers and enthusiasts.  Oh... and crypto miners, but for obvious reasons, I feel no sympathy for them whatsoever.

Regardless of the reasons, if you dont like AMD's support and are unhappy with it, there is an obvious solution and alternative.

---

### 评论 #25 — BloodyIron (2022-05-31T19:38:10Z)

1. OpenCL 2.1 is on the Wikipedia page talking about capabilities (somehow not found on AMD's website it seems) : https://en.wikipedia.org/wiki/Radeon_RX_6000_series
2. AMD's website for RX 6600, for example, lists "OS Support Windows 11 - 64-Bit Edition Windows 10 - 64-Bit Edition Linux x86_64" : https://www.amd.com/en/products/graphics/amd-radeon-rx-6600

It's a reasonable thing to expect OpenCL to work on the most popular Linux distro for a device that is marketed and designed for gaming + productivity.

---

### 评论 #26 — Laitaps (2022-05-31T19:41:49Z)

> 1. OpenCL 2.1 is on the Wikipedia page talking about capabilities (somehow not found on AMD's website it seems) : https://en.wikipedia.org/wiki/Radeon_RX_6000_series
> 2. AMD's website for RX 6600, for example, lists "OS Support Windows 11 - 64-Bit Edition Windows 10 - 64-Bit Edition Linux x86_64" : https://www.amd.com/en/products/graphics/amd-radeon-rx-6600
> 
> It's a reasonable thing to expect OpenCL to work on the most popular Linux distro for a device that is marketed and designed for gaming + productivity.

Agreed, but that is not what is happening and AMD has made no public commitment to do so for the latest LTS release.

---

### 评论 #27 — Bengt (2022-05-31T19:53:40Z)

I would even take any current Linux distro. I mean, Ubuntu isn't my personal choice, but AMD's anyways. I run it, because there has been support for my GPU and would even switch distros to get it back. However, no current distro exists, leaving me running on fumes for security updates and bug fixes. I am one missing feature for TensorFlow away from not being able to run the code of my colleagues and one security issue away from not being able to process confidential data. Not that any of this applies to me, but this state of things still feels very unprofessional.

---

### 评论 #28 — cgmb (2022-05-31T21:48:15Z)

We need to make some adjustments to the packaging to support Ubuntu 22.04. Debian has begun packaging ROCm itself and there are now some package name conflicts between the rocm repo and the jamming repo. That's my fault. I was volunteering with Debian to help get proper OS packages for ROCm and I failed to notice that conflict when it was introduced.

---

### 评论 #29 — BloodyIron (2022-06-02T16:50:29Z)

Thanks for your efforts @cgmb ! Here's hoping this all gets sorted please!

---

### 评论 #30 — Espionage724 (2022-06-08T18:27:43Z)

I was holding off a bit on 22.04 due to waiting on activity in this thread, but nothing happened in about a week. I have a RX 6600 XT and want OpenCL 2.0 support, and Clover/Mesa wasn't usable. AMDGPU-PRO was a pain to install on other distros, so I've been using ROCm when possible.

This will get ROCm OpenCL up on Ubuntu 22.04:

Add repo key:
```
wget -O '/tmp/rocm.gpg.key' 'https://repo.radeon.com/rocm/rocm.gpg.key' && sudo mv '/tmp/rocm.gpg.key' '/etc/apt/trusted.gpg.d/rocm.asc' && sync
```

Add repo:
```
echo 'deb https://repo.radeon.com/rocm/apt/latest/ ubuntu main' | sudo tee '/etc/apt/sources.list.d/rocm.list' > '/dev/null' && cat '/etc/apt/sources.list.d/rocm.list'
```

Install:
```
sudo apt update && sudo apt install rocm-opencl
```

Permissions (if `$LOGNAME` doesn't work for some reason, change it to your username; [reference](https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.1.3/page/Prerequisite_Actions.html#d3019e640)):
```
sudo usermod --append --groups 'render,video' $LOGNAME
```

And after a reboot, the OpenCL app I wanted to use works fine!

---

### 评论 #31 — DrBlackross (2022-06-09T01:15:11Z)

Might want to tell people to put their username in the  '  ' (instead of yours lol)

> Permissions (change username)

(people just copy paste anymore)

ALSO, add sudo apt update before install step... for me i just ran full-upgrade, then sudo aptitude install rocm-opencl 


~$ sudo apt install rocm-opencl
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.15.0-36 linux-headers-5.15.0-36-generic linux-image-5.15.0-36-generic linux-image-5.17.0-12.2-liquorix-amd64 linux-modules-5.15.0-36-generic linux-modules-extra-5.15.0-36-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  comgr hsa-rocr hsakmt-roct-dev libtinfo5 rocm-core rocm-ocl-icd
Recommended packages:
  libdrm-amdgpu-amdgpu1
The following NEW packages will be installed:
  comgr hsa-rocr hsakmt-roct-dev libtinfo5 rocm-core rocm-ocl-icd rocm-opencl
0 upgraded, 7 newly installed, 0 to remove and 0 not upgraded.
Need to get 46.5 MB of archives.
After this operation, 385 MB of additional disk space will be used.
Do you want to continue? [Y/n]

---

### 评论 #32 — DrBlackross (2022-06-09T01:35:25Z)

Ok, i rebooted.... downloaded lolminer as a lark (just because i know it'll pull the opencl devices)

~/Desktop/1.51a$ sudo ./lolMiner --list-devices
OpenCL driver detected. Number of OpenCL supported GPUs: 0 
No Cuda driver or GPUs detected. 

hmmm, didn't work, BUT, it installed rocm.

now, mmpos usb bootable miner (i boot to it when im out of country) will detect and load the opencl drivers without a problem and mine whatever i want with opencl

(god only knows what linux distro is in there)

i know its probably me, i'm missing something

---

### 评论 #33 — DrBlackross (2022-06-09T02:55:10Z)

oops, forgot to add this

~/Desktop/xmrig$ ./xmrig --print-platforms
Number of platforms:        1

  Index:                    0
  Profile:                  FULL_PROFILE
  Version:                  OpenCL 2.1 AMD-APP (3423.0)
  Name:                     AMD Accelerated Parallel Processing
  Vendor:                   Advanced Micro Devices, Inc.
  Extensions:               cl_khr_icd cl_amd_event_callback

and from mmpos...

 v3.0.16
Agent version
5.10.83-mmp / 20.04
Kernel version
5.13.18 / 21.50.2
AMD driver versions
1.0.29
Addin version
510.73.05
Nvidia driver version
stable / 3.0.4 - (castle)
System version

---

### 评论 #34 — Espionage724 (2022-06-09T03:30:54Z)

> Ok, i rebooted.... downloaded lolminer as a lark (just because i know it'll pull the opencl devices)

I use [nsfminer](https://github.com/no-fee-ethereum-mining/nsfminer) (specifically [nsfminer_1.3.14-ubuntu_20.04-opencl.tgz](https://github.com/no-fee-ethereum-mining/nsfminer/releases/download/v1.3.14/nsfminer_1.3.14-ubuntu_20.04-opencl.tgz)) and it seems to work fine with ROCm OpenCL. I tried `lolminer --list-devices` but it does a Segmentation fault (may be unrelated to ROCm).

---

### 评论 #35 — DrBlackross (2022-06-09T04:36:47Z)

00:35:51 miner nsfminer 1.3.14 (No stinkin' fees edition)
00:35:51 miner Copyright 2021 Jean M. Cyr, Licensed under the terms
00:35:51 miner  of the GNU General Public License Version 3
00:35:51 miner https://github.com/no-fee-ethereum-mining/nsfminer
00:35:51 miner Build: linux/release/gnu
00:35:51 miner 3rd Party: GCC 10.2.0, Boost 1.76.0
00:35:51 miner 3rd Party: OpenSSL 1.1.1j  16 Feb 2021
00:35:51 miner Running as user: drblackross

Error: No usable mining devices found
even as 'root'.... nope

---

### 评论 #36 — Laitaps (2022-06-09T14:43:56Z)

I suspect this is unrelated to the topic at hand and should probably be moved to another thread.

---

### 评论 #37 — DrBlackross (2022-06-12T17:27:53Z)

k

---

### 评论 #38 — SciPyPanda (2022-06-20T17:57:32Z)

Is this issue being solved?

---

### 评论 #39 — cgmb (2022-07-01T18:07:19Z)

@SciPyPanda, yes. There was a solution found. It's a work in progress.

---

### 评论 #40 — rajhlinux (2022-07-05T04:16:18Z)

I have AMD Radeon RX580 GPU, how can I install "amdgpu-pro" drivers to encode H.264 using FFMPEG using hardware acceleration from AMD AMF on Ubuntu 22.04?

Thanks.

---

### 评论 #41 — My1 (2022-07-15T09:41:50Z)

> Does AMD even care about OpenCL on consumer GPUs on Linux? You know, the feature that is literally sold on the box? Because I have seen zero evidence that AMD has interest in providing OpenCL working on Linux for consumer GPUs since like ROCm v3.3 for RX 580-era GPUs.

even if not the amdgpu-install script currently depends on rocm so that kinda sux

---

### 评论 #42 — ableeker (2022-07-23T12:45:42Z)

The Ubuntu versions of amdgpu-install 22.20, and 22.20.1 come in a folder jammy, so you may assume these will support Ubuntu 2204.

I then actually try to use it to install HIP like so:

`amdgpu-install --usecase=hip,hiplibsdk`

This (still) fails with the following error:
```
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-llvm : Depends: python but it is not installable
             Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable
E: Unable to correct problems, you have held broken packages.
```
Ubuntu 2204 doesn't offer these packages anymore, only later versions. For HIP anyway, they're not even used. I install dummy packages just to satisfy the dependencies, and HIP install and runs fine. This workaround could of course cause other ROCm parts to fail if they need the packages. libgcc-dev, and libstdc++-dev may well be fine with later versions, but I think that Python refers to Python 2, and if that's correct, some parts will most likely fail if they try to use Python 3 instead.

---

### 评论 #43 — jlublin (2022-08-04T11:08:34Z)

It seems the driver packages does not actually need python, libstdc++-7-dev or libgcc-7-dev if appropriate newer packages are available. Here is a fairly simple workaround by creating a dummy package:

1. Install "equivs"
2. Run "equivs-control amdgpu-driver-fixes"
3. Edit the new amdgpu-fixes file, you may use the following lines

```
Package: amdgpu-driver-fixes
Provides: python,libstdc++-7-dev,libgcc-7-dev
Architecture: all
Description: Fixes the AMD GPU driver installation on Ubuntu 22.04
```
4. Run "equivs-build amdgpu-driver-fixes"
5. Install the new amdgpu-driver-fixes_1.0_all.deb

If you have python-is-python3 then you need to uninstall it since it will create a conflict.
I have not tested all functionallity but HIP in Blender works fine now.

---

### 评论 #44 — Fuzzillogic (2022-08-06T20:32:09Z)

@ableeker @jlublin THANK YOU! I bought an RX 6800XT in September 2021, expecting I could use it soon with Blender, which would be my main use case. I've been using AMD GPUs since Matrox quit the market, and I am Ubuntu user since 2012. Thus far AMD had been a good to excellent choice. So, I'm a bit miffed, to say the least, about the current situation with HIP on Ubuntu 22.04 LTS.

But thanks to you, almost a year later, it now *finally* works in Blender. A scene I made earlier took 6 minutes on CPU (Ryzen 2700X. Yes, that's AMD as well). It now takes 38 SECONDS on GPU, including some CPU-time for denoising. 

And still the hardware ray tracing capabilities are unused :(

I guess as mere enthusiast / hobbyist I'm not the prime market target for AMD. Still, letting us dangle for so long doesn't sit well with me.

---

### 评论 #45 — mrkapqa (2022-08-11T21:12:32Z)



what was helping in my case was to use this here

https://amdgpu-install.readthedocs.io/en/latest/install-installing.html#installing-the-all-open-use-case

**amdgpu-install -y --usecase=graphics
**

so it would install, when all other options failed on Ubuntu 22.04 with newer Amdgpu 22.20 repository for legacy graphics card Radeon RX 550X (Polaris)

---

### 评论 #46 — sosheskaz (2022-08-20T01:47:51Z)

I'm not too knowledgeable about the subject matter, but I arrived here because I wanted to play video games after updating to 22.04.

I tried the above, but still had performance issues. After also installing the `opencl` and `workstation` usecases, I am seeing good performance. I am not sure which one did the trick.

---

### 评论 #47 — rajkhand (2022-08-24T01:19:02Z)

I used this method to install the AMD driver
[https://askubuntu.com/questions/1417418/unmet-dependencies-ubuntu-22-04-amdgpu-hip-support](url)
There were no errors but not sure if this is correct

---

### 评论 #48 — Bengt (2022-09-27T14:25:59Z)

Building upon the answer by @jlublin, here is my procedure:

0. Make sure you do not have `python-is-python3` installed:  
   ```sudo apt remove --yes python-is-python3```
1. Make sure python, libstdc++-7-dev or libgcc-7-dev are installed:  
    ```sudo apt install --yes python3 libgcc-11-dev libstdc++-11-dev```
2. Install the "equivs" package using APT:  
    ```sudo apt install --yes equivs```
3. Create a file named `amdgpu-dependencies` containing the package metadata:  
   ```printf "Package: amdgpu-dependencies\nProvides: python,libstdc++-7-dev,libgcc-7-dev\nArchitecture: all\nDescription: Fixes the AMD GPU installation on Ubuntu 22.04\n" > amdgpu-dependencies```
4. Create a Debian package from the package metadata:
    ```equivs-build amdgpu-dependencies```
5. Install the package providing the dependencies:
    ```sudo dpkg -i amdgpu-dependencies_1.0_all.deb```
6. Cleanup leftover files:  
   ```rm amdgpu-dependencies*```

To verify this has worked, install and run the ```amdgpu``` installation script:

0. Add yourself to the `render` user group:  
   ```sudo usermod -a -G render $LOGNAME```
1. Download the installation script package:  
   ```wget https://repo.radeon.com/amdgpu-install/22.20.3/ubuntu/jammy/amdgpu-install_22.20.50203-1_all.deb```
2. Install the installation script package:  
   ```sudo apt-get install --yes ./amdgpu-install_22.20.50203-1_all.deb```
3. Clean up the left-over package file:
   ```rm ./amdgpu-install_22.20.50203-1_all.deb```
4. Run the installation script:  
    ```amdgpu-install --help```

To make my workstation capable to run machine learning using PyTorch, I installed the `rocm`, `dkms`, and `hip` packages.

0. Install the usecases required for machine learning with PyTorch:  
   ```yes | amdgpu-install --usecase=rocm,dkms,hip```

To test ROCm's availability to PyTorch:

0. Install the virtual environment package for Python 3.10:
   ```sudo apt install --yes python3.10-venv```
1. Create a virtual environment:
   ```python3.10 -m venv venv```
2. Install PyTorch:
   ```venv/bin/python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/rocm5.1.1```
3. Create a main Python file:
   ```printf "import torch\nprint('ROCm is ' + 'available.' if torch.cuda.is_available() else 'unavailable.')" > main.py```
4. Run it to test the availability of ROCm to PyTorch:
   ```venv/bin/python main.py```
5. Clean up leftover files and directories:
   ```rm -rf main.py venv```

---

### 评论 #49 — zzyjsjcom (2022-09-28T02:58:09Z)

**Add focal source to sources.list can fix libstdc++-7-dev issue**

Add the following line to the file: /etc/apt/sources.list
deb [arch=amd64] http://archive.ubuntu.com/ubuntu focal main universe

**Test pass on AMD Radeon RX 6500 XT, using the following instruction.**
# for ubuntu-22.04
// AMD Radeon RX 6500 XT
wget -c https://repo.radeon.com/amdgpu-install/22.20.3/ubuntu/jammy/amdgpu-install_22.20.50203-1_all.deb
sudo apt-get install ./amdgpu-install_22.20.50203-1_all.deb
sudo apt-get update
amdgpu-install --opencl=rocr

My full sources.list:

deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
\# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
\# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
\# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
\# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse

\# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
\# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse

deb [arch=amd64] http://archive.ubuntu.com/ubuntu focal main universe

Logs:
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.1 LTS
Release:        22.04
Codename:       jammy
$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3452.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback
  Platform Extensions function suffix             AMD
  Platform Host timer resolution                  1ns

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx1034
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0
  Driver Version                                  3452.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     GPU
  Device Board Name (AMD)                         AMD Radeon RX 6500 XT
  Device PCI-e ID (AMD)                           0x743f
  Device Topology (AMD)                           PCI-E, 0000:03:00.0
  Device Profile                                  FULL_PROFILE

After fix this issue, you can remove the following line from sources.list file:
deb [arch=amd64] http://archive.ubuntu.com/ubuntu focal main universe

---

### 评论 #50 — xuhuisheng (2022-10-01T01:18:03Z)

ROCm-5.3 provided official support for Ubuntu-22.04 (jammy).
<https://docs.amd.com/bundle/ROCm-Release-Notes-v5.3/page/About_This_Document.html>

---

### 评论 #51 — AbelVM (2022-10-01T09:45:41Z)

> ROCm-5.3 provided official support for Ubuntu-22.04 (jammy). https://docs.amd.com/bundle/ROCm-Release-Notes-v5.3/page/About_This_Document.html

IT'S WORKING FLAWLESSLY! :tada: 

(but you should run `apt update && apt full-upgrade` afterwards, as they have published newer packages of almost everything right after the release)




---

### 评论 #52 — Chase-san (2022-10-01T22:42:58Z)

@AbelVM So how did you install it? There is no release for v5.3 yet.

---

### 评论 #53 — mrplow (2022-10-01T22:46:30Z)

> @AbelVM So how did you install it? There is no release for v5.3 yet.

Sure there is, did you follow the link?

Finally I can unsub from this thread!

---

### 评论 #54 — Chase-san (2022-10-01T22:52:06Z)

It's release notes, which are great, but it does not provide a direct link to the downloads or installation guide. If anyone else sees this, go here instead https://docs.amd.com/bundle/ROCm-Downloads-Guide-v5.3/page/Introduction_to_AMD_ROCm_Installation_Downloads_Guide_for_Linux.html

---

### 评论 #55 — Rmalavally (2022-10-02T18:05:33Z)

@Chase-san 

Thank you for your feedback. The ROCm Release Notes document for the ROCm v5.3 release is now updated with a link to the ROCm Downloads Guide. You can access the latest version at:

https://docs.amd.com/bundle/ROCm-Release-Notes-v5.3/page/About_This_Document.html

ROCm Documentation Team



---

### 评论 #56 — keryell (2022-10-04T09:03:23Z)

Cool! Keep the momentum and get ready for Ubuntu 22.10 for the end of the month.

---

### 评论 #57 — xuhuisheng (2022-10-04T09:27:46Z)

@keryell 
I am afraid rocm wont want to support non-lts version.
And ubuntu-22.10 upgraded kernel from 5.15 to 5.19, the amdgpu-dkms may not support this new version of linux kernel.

In my opinion, lts is enough.

---

### 评论 #58 — achede22 (2022-11-17T17:00:36Z)

@Bengt Please close the issue, this is SOLVED!

https://docs.amd.com/bundle/ROCm-Release-Notes-v5.3/page/About_This_Document.html 

---

### 评论 #59 — Bengt (2022-11-17T17:13:14Z)

Closing this issue due to recent releases now supporting Ubuntu 22.04.

---

### 评论 #60 — flowluap (2022-11-29T16:18:04Z)

> It's release notes, which are great, but it does not provide a direct link to the downloads or installation guide. If anyone else sees this, go here instead https://docs.amd.com/bundle/ROCm-Downloads-Guide-v5.3/page/Introduction_to_AMD_ROCm_Installation_Downloads_Guide_for_Linux.html

Link is down, this should be the correct link:

https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.3/page/Introduction_to_ROCm_Installation_Guide_for_Linux.html

## How to install:
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.3/page/How_to_Install_ROCm.html#_How_to_Install



---

### 评论 #61 — Rmalavally (2022-11-29T16:37:39Z)

@flowluap Thank you for letting us know. You can access the active link for the ROCm Downloads Guide at:

https://docs.amd.com/bundle/ROCm-Downloads-Guide-v5.3/page/Introduction_to_ROCm_Installation_Downloads_Guide_for_Linux.html

Here are some recommended ways to access the release documentation:
- Click Release Documentation for a consolidated list of all ROCm releases and available documentation
- Click the ROCm v5.x link for 5.x release documentation

Please let us know if you cannot access the ROCm Downloads Guide, and I can send you a PDF version (download from the docs portal). 

ROCm Documentation Team

---

### 评论 #62 — flowluap (2022-11-29T18:30:31Z)

> @flowluap Thank you for letting us know. You can access the active link for the ROCm Downloads Guide at:
> 
> https://docs.amd.com/bundle/ROCm-Downloads-Guide-v5.3/page/Introduction_to_ROCm_Installation_Downloads_Guide_for_Linux.html
> 
> Here are some recommended ways to access the release documentation:
> 
> * Click Release Documentation for a consolidated list of all ROCm releases and available documentation
> * Click the ROCm v5.x link for 5.x release documentation
> 
> Please let us know if you cannot access the ROCm Downloads Guide, and I can send you a PDF version (download from the docs portal).
> 
> ROCm Documentation Team

@Rmalavally the link you sent works fine, thanks!
@Chase-san 's Link was down...

---
