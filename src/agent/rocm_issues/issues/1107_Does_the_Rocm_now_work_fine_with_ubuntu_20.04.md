# Does the Rocm now work fine with ubuntu 20.04

> **Issue #1107**
> **状态**: closed
> **创建时间**: 2020-05-10T04:45:00Z
> **更新时间**: 2021-07-29T06:07:29Z
> **关闭时间**: 2021-03-03T11:16:47Z
> **作者**: chaoji90
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1107

## 描述

The tensorflow-rocm worked fine on 19.10.
When I updated to ubuntu 20.04 and used the tensorflow-rocm then I got this
2020-05-10 12:24:20.926812: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-05-10 12:24:20.982479: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:03:00.0 name: Vega 10 XL/XT [Radeon RX Vega 56/64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.59GHz coreCount: 56 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-05-10 12:24:21.020605: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-05-10 12:24:21.021757: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-05-10 12:24:21.024344: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-05-10 12:24:21.024556: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-05-10 12:24:21.024624: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-05-10 12:24:21.024894: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX
2020-05-10 12:24:21.031167: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 3411120000 Hz
2020-05-10 12:24:21.031533: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x86a0570 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-10 12:24:21.031555: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-05-10 12:24:21.032908: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x8708d60 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-05-10 12:24:21.032932: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Vega 10 XL/XT [Radeon RX Vega 56/64], AMDGPU ISA version: gfx900
2020-05-10 12:24:21.033075: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:03:00.0 name: Vega 10 XL/XT [Radeon RX Vega 56/64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.59GHz coreCount: 56 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-05-10 12:24:21.033109: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-05-10 12:24:21.033125: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-05-10 12:24:21.033140: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-05-10 12:24:21.033153: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-05-10 12:24:21.033188: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-05-10 12:24:21.033206: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-05-10 12:24:21.033214: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2020-05-10 12:24:21.033220: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2020-05-10 12:24:21.033282: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7444 MB memory) -> physical GPU (device: 0, name: Vega 10 XL/XT [Radeon RX Vega 56/64], pci bus id: 0000:03:00.0)
2020-05-10 12:24:27.770244: E tensorflow/stream_executor/rocm/rocm_event.cc:28] Error polling for event status: failed to query event: hipError_t(600)
2020-05-10 12:24:27.770282: F tensorflow/core/common_runtime/gpu/gpu_event_mgr.cc:273] Unexpected Event status: 1

Both rocminfo and clinfo work fine now so I have no idea what happened
I tried to reinstall all rocm-dkms and tensorflow-rocm but it didn't work.

---

## 评论 (45 条)

### 评论 #1 — chaoji90 (2020-05-10T10:08:46Z)

I tried to reinstall ubuntu 19.10 and setup the whole environment in a new disk and the tensorflow worked fine, so I guesss something wrong with rocm and ubuntu 20.04.

---

### 评论 #2 — c0d3st0rm (2020-05-10T13:01:27Z)

I have found it to install fine on 20.04 from the official ROCm repos (dkms modules install without error) with a Vega 56, clinfo "works" (but reports no platform for CL_DEVICE_TYPE_GPU), and the OpenCL target appears and looks to work, however I have been having issues specifically with sycl. I'll open up a new issue for that. I cant comment on anything but that, so I don't known if tensorflow works or not.

---

### 评论 #3 — alfabuster (2020-05-11T08:03:09Z)

No, it doesn't work fine with Ubuntu 20.04, even doesn't install.

```
sudo apt install rocm-dkms
...
Loading new amdgpu-3.3-19 DKMS files...
Building for 5.6.7-050607-generic
Building for architecture x86_64
Building initial module for 5.6.7-050607-generic
ERROR (dkms apport): kernel package linux-headers-5.6.7-050607-generic is not supported
Error! Bad return status for module build on kernel: 5.6.7-050607-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.3-19/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10
Setting up rocm-smi (1.0.0-199-rocm-rel-3.3-19-ga9d6426) ...
Setting up rocm-debug-agent (1.0.0) ...
dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
Setting up hip-doc (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
No apport report written because the error message indicates its a followup error from a previous failure.
     Setting up hsakmt-roct (1.0.9-330-gd84bc09) ...
Setting up hip-samples (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
Setting up hsa-rocr-dev (1.1.30300.0-rocm-rel-3.3-19-23fc088b) ...
Setting up rocm-opencl (2.0.0-rocm-rel-3.3-19-363509c8d) ...
Setting up hsakmt-roct-dev (1.0.9-330-gd84bc09) ...
Setting up hsa-ext-rocr-dev (1.1.30300.0-rocm-rel-3.3-19-23fc088b) ...
Setting up rocm-opencl-dev (2.0.0-rocm-rel-3.3-19-363509c8d) ...
Setting up rocprofiler-dev (1.0.0) ...
Setting up rocm-clang-ocl (0.5.0.48-rocm-rel-3.3-19-fa039e7) ...
Setting up rocm-utils (3.3.0-19) ...
Setting up hcc (3.1.20114) ...
Setting up hip-hcc (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
Setting up rocm-dev (3.3.0-19) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9) ...
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

But I have kernel 5.6.7.

I don't know maybe I should open a new issue and get information about system, but it seems many issues still open... Let me know please should I open new issue.

---

### 评论 #4 — chaoji90 (2020-05-11T10:46:43Z)

> No, it doesn't work fine with Ubuntu 20.04, even doesn't install.
> 
> ```
> sudo apt install rocm-dkms
> ...
> Loading new amdgpu-3.3-19 DKMS files...
> Building for 5.6.7-050607-generic
> Building for architecture x86_64
> Building initial module for 5.6.7-050607-generic
> ERROR (dkms apport): kernel package linux-headers-5.6.7-050607-generic is not supported
> Error! Bad return status for module build on kernel: 5.6.7-050607-generic (x86_64)
> Consult /var/lib/dkms/amdgpu/3.3-19/build/make.log for more information.
> dpkg: error processing package rock-dkms (--configure):
>  installed rock-dkms package post-installation script subprocess returned error exit status 10
> Setting up rocm-smi (1.0.0-199-rocm-rel-3.3-19-ga9d6426) ...
> Setting up rocm-debug-agent (1.0.0) ...
> dpkg: dependency problems prevent configuration of rocm-dkms:
>  rocm-dkms depends on rock-dkms; however:
>   Package rock-dkms is not configured yet.
> 
> dpkg: error processing package rocm-dkms (--configure):
>  dependency problems - leaving unconfigured
> Setting up hip-doc (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
> No apport report written because the error message indicates its a followup error from a previous failure.
>      Setting up hsakmt-roct (1.0.9-330-gd84bc09) ...
> Setting up hip-samples (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
> Setting up hsa-rocr-dev (1.1.30300.0-rocm-rel-3.3-19-23fc088b) ...
> Setting up rocm-opencl (2.0.0-rocm-rel-3.3-19-363509c8d) ...
> Setting up hsakmt-roct-dev (1.0.9-330-gd84bc09) ...
> Setting up hsa-ext-rocr-dev (1.1.30300.0-rocm-rel-3.3-19-23fc088b) ...
> Setting up rocm-opencl-dev (2.0.0-rocm-rel-3.3-19-363509c8d) ...
> Setting up rocprofiler-dev (1.0.0) ...
> Setting up rocm-clang-ocl (0.5.0.48-rocm-rel-3.3-19-fa039e7) ...
> Setting up rocm-utils (3.3.0-19) ...
> Setting up hcc (3.1.20114) ...
> Setting up hip-hcc (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
> Setting up rocm-dev (3.3.0-19) ...
> Processing triggers for man-db (2.9.1-1) ...
> Processing triggers for libc-bin (2.31-0ubuntu9) ...
> Errors were encountered while processing:
>  rock-dkms
>  rocm-dkms
> E: Sub-process /usr/bin/dpkg returned an error code (1)
> ```
> 
> But I have kernel 5.6.7.
> 
> I don't know maybe I should open a new issue and get information about system, but it seems many issues still open... Let me know please should I open new issue.

I have kernel version 5.4 in the 20.04 and 5.3 in the 19.10. 
It might be that some rocm functions are affected by the upgrade, but I am neither an expert in rocm nor in kernel, so it is difficult to say where is the problem. Maybe you can try rocm with 5.3 kernel in 20.04

---

### 评论 #5 — alfabuster (2020-05-11T10:52:53Z)

I'll check kernel 5.3 but later...

---

### 评论 #6 — c0d3st0rm (2020-05-11T14:34:41Z)

The module should build on 5.3 as that is what the 18.04 HWE stack is using (if I recall correctly). It seems to build on 5.4 (however that does not mean it will necessarily function as expected), but any newer releases of the kernel may introduce breaking ABI changes which means the module won't compile.

---

### 评论 #7 — jackyin68 (2020-05-11T16:22:08Z)

Actually, the support of ROCM is terrible bad. Very very confused users. How to use? OS version+Rocm version. Give right and directly guideline, please !!! 

---

### 评论 #8 — c0d3st0rm (2020-05-11T16:26:52Z)

There are installation instructions for supported distributions in the documentation: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

---

### 评论 #9 — Rmalavally (2020-05-11T16:34:34Z)

Thank you for providing the link to the AMD ROCm documentation. Please let us know if you are unable to find what you need in our documentation. Your feedback is important to us.

---

### 评论 #10 — ableeker (2020-05-11T17:51:12Z)

It does indeed install without problems. That's to say, as long as you don't try to install the DKMS bit. And because I only need OpenCL, I don't install rocm-kms, I install meta-package rocm-dev instead. This skips the DKMS bit, and install just fine. As far as I know, package rocm-dkms will only install on Ubuntu 18.04. Even without DKMS however, OpenCL will install, and run just fine on 20.04 this way.

---

### 评论 #11 — chaoji90 (2020-05-12T06:46:57Z)

> It does indeed install without problems. That's to say, as long as you don't try to install the DKMS bit. And because I only need OpenCL, I don't install rocm-kms, I install meta-package rocm-dev instead. This skips the DKMS bit, and install just fine. As far as I know, package rocm-dkms will only install on Ubuntu 18.04. Even without DKMS however, OpenCL will install, and run just fine on 20.04 this way.

Got it, thanks a lot.

---

### 评论 #12 — alfabuster (2020-05-13T07:42:37Z)

Kernel 5.3 doesn't solve problem, but the error not same...

```
sudo apt install rocm-dkms
...

Loading new amdgpu-3.3-19 DKMS files...
Building for 5.3.0-050300-generic 5.6.7-050607-generic
Building for architecture x86_64
Building initial module for 5.3.0-050300-generic
Secure Boot not enabled on this system.
Done.
Forcing installation of amdgpu

amdgpu.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.3.0-050300-generic/updates/dkms/

amdttm.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.3.0-050300-generic/updates/dkms/

amdkcl.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.3.0-050300-generic/updates/dkms/

amd-sched.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.3.0-050300-generic/updates/dkms/

Running the post_install script:
update-initramfs: Generating /boot/initrd.img-5.3.0-050300-generic
W: Possible missing firmware /lib/firmware/amdgpu/navi10_mes.bin for module amdgpu
I: The initramfs will attempt to resume from /dev/nvme0n1p3
I: (UUID=fcfce3f2-3d20-4779-981d-e970bb82b3f9)
I: Set the RESUME variable to override this.
Error 24 : Write error : cannot write compressed block 
E: mkinitramfs failure cpio 141 lz4 -9 -l 24
update-initramfs: failed for /boot/initrd.img-5.3.0-050300-generic with 1.

depmod....

Backing up initrd.img-5.3.0-050300-generic to /boot/initrd.img-5.3.0-050300-generic.old-dkms
cp: error writing '/boot/initrd.img-5.3.0-050300-generic.old-dkms': No space left on device
Making new initrd.img-5.3.0-050300-generic
(If next boot fails, revert to initrd.img-5.3.0-050300-generic.old-dkms image)
update-initramfs.......(bad exit status: 1)

-------- Uninstall Beginning --------
Module:  amdgpu
Version: 3.3-19
Kernel:  5.3.0-050300-generic (x86_64)
-------------------------------------

Status: Before uninstall, this module version was ACTIVE on this kernel.

amdgpu.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.3.0-050300-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdttm.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.3.0-050300-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdkcl.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.3.0-050300-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amd-sched.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.3.0-050300-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


Running the post_remove script:
depmod...

update-initramfs.......(bad exit status: 1)
Warning: There was a problem remaking your initrd.  You must manually remake it
before booting into this kernel.

DKMS: uninstall completed.
Error! Problems with mkinitrd detected.  Automatically uninstalling this module.
DKMS: Install Failed (mkinitrd problems).  Module rolled back to built state.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 7
Setting up rocm-smi (1.0.0-199-rocm-rel-3.3-19-ga9d6426) ...
Setting up rocm-debug-agent (1.0.0) ...
dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
No apport report written because the error message indicates its a followup error from a previous failure.
     Setting up hip-doc (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
Setting up hsakmt-roct (1.0.9-330-gd84bc09) ...
Setting up hip-samples (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
Setting up hsa-rocr-dev (1.1.30300.0-rocm-rel-3.3-19-23fc088b) ...
Setting up rocm-opencl (2.0.0-rocm-rel-3.3-19-363509c8d) ...
Setting up hsakmt-roct-dev (1.0.9-330-gd84bc09) ...
Setting up hsa-ext-rocr-dev (1.1.30300.0-rocm-rel-3.3-19-23fc088b) ...
Setting up rocm-opencl-dev (2.0.0-rocm-rel-3.3-19-363509c8d) ...
Setting up rocprofiler-dev (1.0.0) ...
Setting up rocm-clang-ocl (0.5.0.48-rocm-rel-3.3-19-fa039e7) ...
Setting up rocm-utils (3.3.0-19) ...
Setting up hcc (3.1.20114) ...
Setting up hip-hcc (3.3.20126.4629-rocm-rel-3.3-19-2dbba46b) ...
Setting up rocm-dev (3.3.0-19) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9) ...
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

But still fail install rocm on Ubuntu 20.04...

---

### 评论 #13 — c0d3st0rm (2020-05-13T21:43:45Z)

It looks like you ran out of space in `/boot` - see the error in the log from `cp`? This issue is unrelated to ROCm, and you'll need to either resize your `/boot` partition or get rid of some old kernels and initrd images to make room.

---

### 评论 #14 — alfabuster (2020-05-15T09:49:19Z)

You are right. I haven't enough space on /boot partition and now I can't use more then 2 kernels. Will try resize my /boot partition later...

---

### 评论 #15 — ableeker (2020-05-15T18:10:50Z)

Kernel 5.3 works indeed. After I'd switched to kernel 5.3, I was able to install and run rocm-dkms just fine, wheras it doesn't install with kernel 5.4 (or other versions I presume). However, all I need ROCm for is OpenCL actually. That's why I install rocm-dev, which skips DKMS. That's why it does install on stock 20.04. So if you don't need DKMS, just install rocm-dev, and you don't have to use any work-arounds.

---

### 评论 #16 — alfabuster (2020-05-17T11:33:05Z)

Solve problem with my /boot partition and now for kernel 5.3 rocm driver was installed, but if run 
```
/opt/rocm/bin/rocminfo
ROCk module is loaded
den is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

And here...

 /opt/rocm/opencl/bin/x86_64/clinfo                                               
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3098.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```
I don't understand how it works. I also will try rocm-dev, the last chance to get success.


---

### 评论 #17 — ableeker (2020-05-17T11:56:53Z)

For me the advantage of rocm-dev is that you don't have to switch to kernel 5.3. However, I've tried kernel 5.3, and rocm-dkms did work on my computer. So, when you're running kernel 5.3, rocm-dkms should work, and I have a feeling installing rocm-dev won't solve your problem.

But there's  another thing you could try. This error might be caused by a change in permissions for kfd in Ubuntu 20.04. Before 20.04 you have to give yourself the right permissions by adding yourself to the video group, because kfd is owned by video, if I understand correctly. However, in 20.04 this has cnaged, and kfd is now owned by render. I don't know if you still need to be a member of the video group, but to be safe I've made added myself to both the video, and the render group. It works for me.

---

### 评论 #18 — alfabuster (2020-05-17T14:31:14Z)

I installed rocm-dev. But errors the same like above...

```
/opt/rocm/bin/rocminfo
ROCk module is loaded
den is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

And here...

 /opt/rocm/opencl/bin/x86_64/clinfo                                               
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3098.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```

I think it is don't work properly. Cause when I use blender, I can't use opencl...
![Screenshot_20200517_172843](https://user-images.githubusercontent.com/18118824/82151398-31ed2c80-9864-11ea-9e31-9da34ecacd57.png)


---

### 评论 #19 — ableeker (2020-05-18T17:20:18Z)

Something isn't correct yet. Blender does recognise my GPU (it's an RX 64).

I had to install libtinfo5 to make clinfo work, and that's not in the installation guide unfortunately. Then you should add yourself to the video group, and possibly the render group. And if you're installing rocm-dev, you'll have to create file /etc/udev/rules.d/70-kfd.rules, that should contain the following:

`SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"`

But other than that, the OpenCL part from ROCm 3.3 is running fine on my computer with Ubuntu 20.04.

![Screenshot from 2020-05-18 19-01-37](https://user-images.githubusercontent.com/2095835/82240577-ee192680-993a-11ea-80d8-257e58229c12.png)


---

### 评论 #20 — rkothako (2020-05-19T07:02:47Z)

Hi All,
Ubuntu 20.04 support was not enabled officially for ROCm 3.3, but it might work.
So once we claim 20.04 officially with the upcoming ROCm releases, we will definitely make sure that all documentation things are taken care properly.

---

### 评论 #21 — advancingu (2020-05-30T23:52:52Z)

Blender doesn't recognize my Vega 56 on Ubuntu 20.04 with `rocm-dev` installed, `/etc/udev/rules.d/70-kfd.rules` correctly in place and user added to `video` group.

```
$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3098.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   
  clCreateContext(NULL, ...) [default]            No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.11
  ICD loader Profile                              OpenCL 2.1
```

```
$ /opt/rocm/bin/rocminfo
ROCk module is loaded
athlon is member of video group
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 1700X Eight-Core Processor
  Marketing Name:          AMD Ryzen 7 1700X Eight-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3400                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16388600(0xfa11f8) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16388600(0xfa11f8) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XL/XT [Radeon RX Vega 56/64]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26751(0x687f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1590                               
  BDFID:                   3328                               
  Internal Node ID:        1                                  
  Compute Unit:            56                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             
```

Any ideas on how to fix?

---

### 评论 #22 — eapenfold (2020-07-31T19:03:41Z)

@rkothako  What is the current status of Ubuntu 20.04 support? ROCm 3.5.1 is out but the release notes don't seem to mention Ubuntu 20.04.

---

### 评论 #23 — H-Ribeiro (2020-08-24T15:21:29Z)

No it doesn't, installation keeps failing as kernel 5.4 seems not to be supported.. Which does not make sense since Ubuntu 20.04 comes packed with kernel 5.4..

---

### 评论 #24 — ableeker (2020-08-25T21:32:37Z)

I've just tried to install ROCm on Ubuntu 20.04, and rocm-dkms installs, at least on this computer with kernel 5.4.0-42. Besides, the documentation explicitly states it supports 20.04. I admit this is the new ROCm 3.7.0, but I'm pretty sure I've installed 3.5 on 20.04 as well. So far rocminfo, rocm-smi, and clinfo all recognise my Vega 64, and OpenCL programs work.

---

### 评论 #25 — yaomtc (2020-11-29T02:41:15Z)

I'm trying to install on Ubuntu 20.10, but no dice. (Yes, I know it's not officially supported.)

```
$ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocm-dkms is already the newest version (3.9.0.30900-17).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
2 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] Y
Setting up rock-dkms (1:3.9-17) ...
Removing old amdgpu-3.9-17 DKMS files...

------------------------------
Deleting module version: 3.9-17
completely from the DKMS tree.
------------------------------
Done.
Loading new amdgpu-3.9-17 DKMS files...
Building for 5.8.0-29-generic
Building for architecture x86_64
Building initial module for 5.8.0-29-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms-firmw
are.0.crash'
Error! Bad return status for module build on kernel: 5.8.0-29-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.9-17/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error 
exit status 10
dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
No apport report written because the error message indicates its a followup erro
r from a previous failure.
                          Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

---

### 评论 #26 — xuhuisheng (2020-11-29T02:52:13Z)

Ubuntu 20.04 got offical supporting since ROCm-3.7.
<https://github.com/RadeonOpenCompute/ROCm/issues/1074#issuecomment-678805920>

And AMD confirmed they wont add non-LTS releasing on offcial supporting list. But I had test ROCm-3.9 on Ubuntu 20.10 with upstream kernel driver - only install rocm-dev and rocm-libs. it works.
<https://github.com/RadeonOpenCompute/ROCm/issues/1263#issuecomment-720264016>

---

### 评论 #27 — yaomtc (2020-11-29T16:33:59Z)

I had to update to 20.10 because the kernel used in 20.04 caused my Ethernet connection to disappear after resuming from standby. Does ROCm have any issue with updating the kernel in 20.04? Or does that make it not-really-LTS anymore?

---

### 评论 #28 — valeriob01 (2020-11-29T20:11:16Z)

I use ROCm 3.3 with Ubuntu 20.04 without problems. I did a minimal install and it works fine, and it is faster that version 3.5 and later versions.


---

### 评论 #29 — ROCmSupport (2020-11-30T04:52:44Z)

Hi @yaomtc 
ROCm works well with Ubuntu 20.04 official/default kernels. You can try with any different kernel on top of 20.04 but might or might not work. You can give a try.

---

### 评论 #30 — RoyPrather (2020-11-30T22:53:45Z)

Hi @ROCmSupport 
   Today I downloaded a fresh ubuntu 20.04 lts, installed it and then fallowed the instructions here https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html ... It failed at the 'apt install rocm-dkms' step with an error about rock-dkms. I have attached the error file.


[Crash.txt](https://github.com/RadeonOpenCompute/ROCm/files/5619191/Crash.txt)



---

### 评论 #31 — yaomtc (2020-12-01T05:02:46Z)

Turns out the issue I'm having doesn't occur in linux-oem (5.6) which ROCm does support. Nice.

---

### 评论 #32 — yaomtc (2020-12-01T05:30:30Z)

Unfortunately even with linux-oem on 20.04... I still can't install it.

```
Setting up dkms (2.8.1-5ubuntu1) ...
Setting up hip-rocclr (3.9.20412-6d111f85) ...
Setting up rock-dkms (1:3.9-17) ...
Loading new amdgpu-3.9-17 DKMS files...
Building for 5.8.0-29-generic
Building for architecture x86_64
Building initial module for 5.8.0-29-generic
Error! Bad return status for module build on kernel: 5.8.0-29-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.9-17/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error 
exit status 10
Setting up g++-9 (9.3.0-17ubuntu1~20.04) ...
Setting up g++ (4:9.3.0-1ubuntu2) ...
update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mo
de
Setting up build-essential (12.8ubuntu1.1) ...
dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
No apport report written because the error message indicates its a followup erro
r from a previous failure.
                          Setting up gcc-multilib (4:9.3.0-1ubuntu2) ...
Setting up g++-9-multilib (9.3.0-17ubuntu1~20.04) ...
Setting up g++-multilib (4:9.3.0-1ubuntu2) ...
Processing triggers for sgml-base (1.29.1) ...
Setting up x11proto-dev (2019.2-1ubuntu1) ...
Setting up libxau-dev:amd64 (1:1.0.9-0ubuntu1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.1) ...
Processing triggers for man-db (2.9.1-1) ...
Setting up libxdmcp-dev:amd64 (1:1.1.3-0ubuntu1) ...
Setting up x11proto-core-dev (2019.2-1ubuntu1) ...
Setting up libxcb1-dev:amd64 (1.14-2) ...
Setting up libx11-dev:amd64 (2:1.6.9-2ubuntu1.1) ...
Setting up libglx-dev:amd64 (1.3.1-1ubuntu0.20.04.1) ...
Setting up libgl-dev:amd64 (1.3.1-1ubuntu0.20.04.1) ...
Setting up mesa-common-dev:amd64 (20.0.8-0ubuntu1~20.04.1) ...
Setting up rocm-opencl-dev (3.6Beta-14-g0c40e05-rocm-rel-3.9-17) ...
Setting up rocm-clang-ocl (0.5.0.64-rocm-rel-3.9-17-50fb51a) ...
Setting up rocm-utils (3.9.0.30900-17) ...
Setting up rocm-dev (3.9.0.30900-17) ...
Processing triggers for libc-bin (2.31-0ubuntu9.1) ...
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)

```

---

### 评论 #33 — ROCmSupport (2020-12-01T08:17:12Z)

Hi @RoyPrather 
Looks like you are installing ROCm on 5.4.0-56. Found that 5.4.0-56 is not working for ROCm.
Recommend to install ROCm on 5.4.0-54 and it works.

---

### 评论 #34 — josarv (2020-12-02T05:32:33Z)

I got the exact same message as @yaomtc while trying to install rocm on both fresh Ubuntu and Pop os (practically the same). Upon opening the log at /var/lib/dkms/amdgpu/3.9-17/build/make.log it says that there is a gcc version mismatch (kernel 5.4.0-56 has gcc version 90303 instead of 90300) which I suspect could be the root of the problem. There have been similar problems to the unspoken Nvidia drivers as well, strengthening that suspicion. Problem could be solved by downgrading the kernel or gcc, testing right now. However, 20.04 is officially supported but it ships with kernel 5.4.0-56 which won't work with rocm. Moreover the legacy and pal stacks are deprecated and due to that not even amdgpu-pro drivers provide opencl support for 20.04. Could you please look into this? 

---

### 评论 #35 — ROCmSupport (2020-12-02T06:45:23Z)

Hi @josarv 
We are aware of this issue now and there are similar tickets logged: #1307 
We are working on the fix. 
Meanwhile recommend to proceed with 5.4.0-54 kernel
Thank you.

---

### 评论 #36 — rur0 (2020-12-02T08:06:55Z)

> Hi @josarv
> We are aware of this issue now and there are similar tickets logged: #1307
> We are working on the fix.
> Meanwhile recommend to proceed with 5.4.0-54 kernel
> Thank you.

ROCm does not work on Ubuntu 20.04 5.4.0-54 kernel with MI25 GPU

---

### 评论 #37 — ROCmSupport (2020-12-02T08:40:58Z)

Hi @rur0 
ROCm works well with 5.4.0-54 but not with 5.4.0-56. Hence am recommending 5.4.0-54.
I have Ubuntu 20.04.1 with 5.4.0-54 + MI25, its working well.

---

### 评论 #38 — josarv (2020-12-04T07:39:42Z)

The issue with rocm seems to be affecting amdgpu-drivers as well due to legacy and pal stacks having been phased out. It looks like until the issue is resolved there's no opencl support for 20.04 that I know of. The 20.45 amdgpu-pro driver looks broken judging from my failed attempts to install it on a fresh 20.04 Ubuntu/Pop and the blender people report a similar situation: https://devtalk.blender.org/t/guide-install-amd-opencl-on-pop-os-some-ubuntu-derivates/13458
Will there be a new amdgpu-pro driver following the fix?

---

### 评论 #39 — ROCmSupport (2020-12-04T08:20:09Z)

Hi @josarv 
This is the space for ROCm. 
Our kernel team is already working on patch for fixing installation issue on 5.4.0-56 kernel.
Until then, we recommend to use a working kernel like 5.4.0-54 or hwe kernels to proceed further with ROCm.

---

### 评论 #40 — RoyPrather (2020-12-04T18:26:42Z)

For people just landing here cus there stuff is broken. Kernel -56 doesn't isnt working, kernel -54 breaks my networking... but Ubuntu live media ships with kernel -42. I was able to boot into kernel -42,  apt remove all other kernel images/modules/headers , then amd's software instaled without issue. both ROCm and pro drivers. OpenCL working.

---

### 评论 #41 — ableeker (2020-12-05T14:14:13Z)

For me Ubuntu 20.04 with the original 5.4 kernel, and dkms kernel modules, did install, and work successfully.

But I only need OpenCL, so now I don't use dkms anymore, and only install package rocm-opencl. So far OpenCL installed this way is working fine for me (although there are some minor issues) on 20.04 with all kernels, and even on 20.10 with kernel 5.8.

---

### 评论 #42 — ROCmSupport (2021-03-03T11:16:47Z)

Hi @chaoji90 and all,
Now ROCm 4.0 works well on Ubuntu 20.04 and ROCm 4.1 is coming with the latest kernel support also.
The current issue is not observed anymore.
I am closing this now.
Feel free to open any new issue for quick responses.
Thank you.

---

### 评论 #43 — Gustavofaa (2021-07-29T02:56:37Z)

I still can not install it on Ubuntu 20.04.

Got the following:

Unpacking rock-dkms-firmware (1:4.2-21) ...
dpkg: error processing archive /var/cache/apt/archives/rock-dkms-firmware_1%3a4.2-21_all.deb (--unpack):
 trying to overwrite '/usr/share/doc/amdgpu-dkms-firmware/LICENSE', which is also in package amdgpu-dkms-firmware 1:5.9.20.104-
1247438
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/rock-dkms-firmware_1%3a4.2-21_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)



---

### 评论 #44 — Gustavofaa (2021-07-29T03:01:29Z)

For more information about GPU model, please see:

sudo lshw -C display
  *-display                 
       description: VGA compatible controller
       product: Hawaii XT / Grenada XT [Radeon R9 290X/390X]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:01:00.0
       version: 80
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:30 memory:d0000000-dfffffff memory:e0000000-e07fffff ioport:e000(size=256) memory:efe00000-efe3ffff memory:c0000-dffff


---

### 评论 #45 — ROCmSupport (2021-07-29T06:07:29Z)

Hi @Gustavofaa 
As the current issue is already closed, request you to file new tickets, for quick resolutions.

You are using Hawaii XT, which is not a supported rocm config and so can not comment on this.
And also from the above error messages, I found that you have already instaled amdgpu-pro initially and then trying to install rocm on top of that, which is incorrect. At a time, rocm or amdgpu-pro can be installed. Installing both cause installation breakages.
Hope this helps.
Thank you.

---
