# ROCm installation flummoxed -Radeon VII, Ubuntu 18.04 - cancel

> **Issue #860**
> **状态**: closed
> **创建时间**: 2019-08-10T18:59:11Z
> **更新时间**: 2019-08-15T22:00:30Z
> **关闭时间**: 2019-08-15T22:00:16Z
> **作者**: cfshelor
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/860

## 描述

I bungled my amdgpu and rocm installation with a Radeon VII trying to get OpenCL installed and dug a hole deep enough that I cannot uninstall the packages.

First I installed the AMDGPU drivers for the Radeon VII using "./amdgpu-pro-install -y --opencl=pal" thinking that was the way to get OpenCL installed.  An earlier suggestion was to use ROCm, so I followed those installation instructions, but got some errors:

Selecting previously unselected package rock-dkms.
Preparing to unpack .../49-rock-dkms_2.6-22_all.deb ...
Unpacking rock-dkms (2.6-22) ...
dpkg: error processing archive /tmp/apt-dpkg-install-Ewk3Sx/49-rock-dkms_2.6-22_all.deb (--unpack):
 trying to overwrite '/usr/share/dkms/modules_to_force_install/amdgpu', which is also in package amdgpu-dkms 19.20-812932
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Selecting previously unselected package rocm-device-libs.
Preparing to unpack .../50-rocm-device-libs_0.0.1_amd64.deb ...
Unpacking rocm-device-libs (0.0.1) ...
Selecting previously unselected package rocm-smi.
Preparing to unpack .../51-rocm-smi_1.0.0-157-g8d290c1_amd64.deb ...
Unpacking rocm-smi (1.0.0-157-g8d290c1) ...
Selecting previously unselected package rocr_debug_agent.
Preparing to unpack .../52-rocr%5fdebug%5fagent_1.0.0_amd64.deb ...
Unpacking rocr_debug_agent (1.0.0) ...
Selecting previously unselected package rocm-dev.
Preparing to unpack .../53-rocm-dev_2.6.22_amd64.deb ...
Unpacking rocm-dev (2.6.22) ...
Selecting previously unselected package rocm-dkms.
Preparing to unpack .../54-rocm-dkms_2.6.22_amd64.deb ...
Unpacking rocm-dkms (2.6.22) ...
Errors were encountered while processing:
 /tmp/apt-dpkg-install-Ewk3Sx/49-rock-dkms_2.6-22_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)

So I figured I needed to uninstall the amdgpu-pro packages which produced:
cfs0042@alveo-cse:~/downloads$ sudo amdgpu-pro-uninstall
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 amdgpu-dkms : Depends: amdgpu-core but it is not going to be installed
 amdgpu-lib-hwe : Depends: amdgpu-core (= 19.20-812932) but it is not going to be installed
 amdgpu-pro-core : Depends: amdgpu-core but it is not going to be installed
 gst-omx-amdgpu : Depends: amdgpu-core but it is not going to be installed
 libdrm-amdgpu-common : Depends: amdgpu-core but it is not going to be installed
 libdrm2-amdgpu : Depends: amdgpu-core but it is not going to be installed
 libdrm2-amdgpu:i386 : Depends: amdgpu-core:i386
 libegl1-amdgpu-mesa : Depends: amdgpu-core but it is not going to be installed
 libegl1-amdgpu-mesa:i386 : Depends: amdgpu-core:i386
 libgbm1-amdgpu : Depends: amdgpu-core but it is not going to be installed
 libgbm1-amdgpu:i386 : Depends: amdgpu-core:i386
...
 xserver-xorg-hwe-amdgpu-video-amdgpu : Depends: amdgpu-core but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).

So I tried the --fix-broken install as suggested:
cfs0042@alveo-cse:~/downloads$ sudo apt --fix-broken install
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Correcting dependencies... Done
The following additional packages will be installed:
  rock-dkms
The following NEW packages will be installed:
  rock-dkms
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
54 not fully installed or removed.
Need to get 0 B/6,223 kB of archives.
After this operation, 140 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
(Reading database ... 269123 files and directories currently installed.)
Preparing to unpack .../rock-dkms_2.6-22_all.deb ...
Unpacking rock-dkms (2.6-22) ...
dpkg: error processing archive /var/cache/apt/archives/rock-dkms_2.6-22_all.deb (--unpack):
 trying to overwrite '/usr/share/dkms/modules_to_force_install/amdgpu', which is also in package amdgpu-dkms 19.20-812932
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/rock-dkms_2.6-22_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)

The following rocm packages are shown to be installed:
cfs0042@alveo-cse:~/downloads$ apt list --installed | grep -i rocm
rocm-clang-ocl/Ubuntu 16.04,now 0.4.0-7ce124f amd64 [installed,automatic]
rocm-dev/Ubuntu 16.04,now 2.6.22 amd64 [installed,automatic]
rocm-device-libs/Ubuntu 16.04,now 0.0.1 amd64 [installed,automatic]
rocm-dkms/Ubuntu 16.04,now 2.6.22 amd64 [installed]
rocm-opencl/Ubuntu 16.04,now 1.2.0-2019070446 amd64 [installed,automatic]
rocm-opencl-dev/Ubuntu 16.04,now 1.2.0-2019070446 amd64 [installed,automatic]
rocm-smi/Ubuntu 16.04,now 1.0.0-157-g8d290c1 amd64 [installed,automatic]
rocm-utils/Ubuntu 16.04,now 2.6.22 amd64 [installed,automatic]
rocminfo/Ubuntu 16.04,now 1.0.0 amd64 [installed,automatic]

and the following amdgpu packages are installed:
amdgpu-core/unknown,now 19.20-812932 all [installed,automatic]
amdgpu-dkms/unknown,now 19.20-812932 all [installed]
amdgpu-hwe/unknown,now 19.20-812932 amd64 [installed]
amdgpu-lib-hwe/unknown,now 19.20-812932 amd64 [installed,automatic]
amdgpu-lib32/unknown,now 19.20-812932 amd64 [installed]
amdgpu-pro-core/unknown,now 19.20-812932 all [installed,automatic]
amdgpu-pro-hwe/unknown,now 19.20-812932 amd64 [installed]
amdgpu-pro-lib32/unknown,now 19.20-812932 amd64 [installed]
amdgpu-pro-pin/unknown,now 19.20-812932 all [installed]
gst-omx-amdgpu/unknown,now 1.0.0.1-812932 amd64 [installed,automatic]
libdrm-amdgpu-amdgpu1/unknown,now 1:2.4.97-812932 amd64 [installed,automatic]
libdrm-amdgpu-common/unknown,now 1.0.0-812932 all [installed,automatic]
libdrm-amdgpu1/bionic-updates,now 2.4.97-1ubuntu1~18.04.1 amd64 [installed]
libdrm2-amdgpu/unknown,now 1:2.4.97-812932 amd64 [installed,automatic]
libegl1-amdgpu-mesa/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libegl1-amdgpu-mesa-drivers/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libegl1-amdgpu-pro/unknown,now 19.20-812932 i386 [installed,automatic]
libgbm1-amdgpu/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libgbm1-amdgpu-pro/unknown,now 19.20-812932 i386 [installed,automatic]
libgbm1-amdgpu-pro-base/unknown,now 19.20-812932 all [installed,automatic]
libgl1-amdgpu-mesa-dri/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libgl1-amdgpu-mesa-glx/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libgl1-amdgpu-pro-appprofiles/unknown,now 19.20-812932 all [installed,automatic]
libgl1-amdgpu-pro-dri/unknown,now 19.20-812932 i386 [installed,automatic]
libgl1-amdgpu-pro-ext-hwe/unknown,now 19.20-812932 amd64 [installed,automatic]
libgl1-amdgpu-pro-glx/unknown,now 19.20-812932 i386 [installed,automatic]
libglapi-amdgpu-mesa/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libglapi1-amdgpu-pro/unknown,now 19.20-812932 i386 [installed,automatic]
libgles1-amdgpu-mesa/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libgles2-amdgpu-mesa/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libgles2-amdgpu-pro/unknown,now 19.20-812932 i386 [installed,automatic]
libllvm7.1-amdgpu/unknown,now 1:7.1-812932 amd64 [installed,automatic]
libosmesa6-amdgpu/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
libwayland-amdgpu-client0/unknown,now 1.15.0-812932 amd64 [installed,automatic]
libwayland-amdgpu-egl1/unknown,now 1.15.0-812932 amd64 [installed,automatic]
libwayland-amdgpu-server0/unknown,now 1.15.0-812932 amd64 [installed,automatic]
libxatracker2-amdgpu/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
mesa-amdgpu-omx-drivers/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
mesa-amdgpu-va-drivers/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
mesa-amdgpu-vdpau-drivers/unknown,now 1:18.3.0-812932 amd64 [installed,automatic]
vulkan-amdgpu-pro/unknown,now 19.20-812932 amd64 [installed]
wsa-amdgpu/unknown,now 19.20-812932 amd64 [installed,automatic]
xserver-xorg-hwe-amdgpu-video-amdgpu/unknown,now 1:19.0.1-812932 amd64 [installed,automatic]
xserver-xorg-video-amdgpu-hwe-18.04/bionic-updates,now 19.0.1-1~18.04.1 amd64 [installed,automatic]

I am open to any and all suggestions for the best way to recover and get an operational OpenCL running on the Radeon VII.  I also have a Xilinx Alveo FPGA accelerator installed with OpenCL.  Is it possible that the OpenCL runtime is getting confused between two different platforms?  I'm not a sys-admin type, know just enough to get myself in trouble, obviously.

Thank you to any who can help me out,

Charles
 



---

## 评论 (1 条)

### 评论 #1 — cfshelor (2019-08-15T22:00:16Z)

We decided having two OpenCL vendors on the same system was going to be troublesome, so we are buying a second box to host the Radeon VII.  We are installing the OS from scratch on the existing box to ensure all Radeon VII software has been eliminated.  After many hours of searching here and the AMD community forums, I have formed the opinion that for my application of primarily using the Radeon VII for OpenCL I should install the ROCm package and not mess with the AMDGPU-Pro drivers.  If anyone disagrees with this statement, please respond with some rationale indicating why that is the incorrect procedure.

---
