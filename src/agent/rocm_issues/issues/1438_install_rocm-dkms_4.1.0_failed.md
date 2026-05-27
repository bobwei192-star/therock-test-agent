# install rocm-dkms 4.1.0 failed

> **Issue #1438**
> **状态**: closed
> **创建时间**: 2021-04-02T03:35:29Z
> **更新时间**: 2021-04-16T11:10:25Z
> **关闭时间**: 2021-04-16T11:10:25Z
> **作者**: SomnusMistletoe
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1438

## 描述

My Os is Ubuntu18.04, and old-verison is rocm-4.0.0,
I have removed rock-dkms before the upgrade, and install rock-dkms as https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html, howerver, when I execute

`sudo apt install rocm-dkms`

I encountered the following errors：

```
depmod.....

DKMS: install completed.
update-initramfs: Generating /boot/initrd.img-4.15.0-140-generic
find: ‘/lib/firmware/updates/amdgpu’: No such file or directory
W: Possible missing firmware /lib/firmware/amdgpu/dimgrey_cavefish_ta.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/green_sardine_ta.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/navi10_mes.bin for module amdgpu
Setting up rocm-opencl-dev (2.0.0.40100-26) ...
Setting up rocm-clang-ocl (0.5.0.40100-26) ...
Setting up rocm-dbgapi (0.42.0.40100-26) ...
Setting up rocm-smi-lib (3.0.0.40100-26) ...
Setting up hip-samples (4.1.21072.5776.40100-26) ...
Setting up libpython3.8-stdlib:amd64 (3.8.0-3~18.04.1) ...
Setting up hsa-amd-aqlprofile (1.0.0.40100-26) ...
Setting up libpython3.8:amd64 (3.8.0-3~18.04.1) ...
Setting up openmp-extras (12.41.0.40100-26) ...
Setting up rocm-utils (4.1.0.40100-26) ...
Setting up rocm-gdb (10.1.40100-26) ...
Setting up rocm-dev (4.1.0.40100-26) ...
/opt/rocm-4.1.0/bin/ca not found
update-alternatives: using /opt/rocm-4.1.0/bin/clang-ocl to provide /usr/bin/clang-ocl (clang-ocl) in auto mode
/opt/rocm-4.1.0/bin/extractkernel not found
/opt/rocm-4.1.0/bin/findcode.sh not found
/opt/rocm-4.1.0/bin/finduncodep.sh not found
/opt/rocm-4.1.0/bin/hipcc not found
/opt/rocm-4.1.0/bin/hipcc_cmake_linker_helper not found
/opt/rocm-4.1.0/bin/hipconfig not found
/opt/rocm-4.1.0/bin/hipconvertinplace-perl.sh not found
/opt/rocm-4.1.0/bin/hipconvertinplace.sh not found
/opt/rocm-4.1.0/bin/hipdemangleatp not found
/opt/rocm-4.1.0/bin/hipexamine-perl.sh not found
/opt/rocm-4.1.0/bin/hipexamine.sh not found
/opt/rocm-4.1.0/bin/hipify-cmakefile not found
/opt/rocm-4.1.0/bin/hipify-perl not found
/opt/rocm-4.1.0/bin/lpl not found
update-alternatives: using /opt/rocm-4.1.0/bin/rocgdb to provide /usr/bin/rocgdb (rocgdb) in auto mode
/opt/rocm-4.1.0/bin/rocm_agent_enumerator not found
/opt/rocm-4.1.0/bin/rocminfo not found
update-alternatives: using /opt/rocm-4.1.0/bin/rocm-smi to provide /usr/bin/rocm-smi (rocm-smi) in auto mode
update-alternatives: using /opt/rocm-4.1.0/bin/rocprof to provide /usr/bin/rocprof (rocprof) in auto mode
update-alternatives: using /opt/rocm-4.1.0 to provide /opt/rocm (rocm) in auto mode
Setting up rocm-dkms (4.1.0.40100-26) ...
Processing triggers for libc-bin (2.27-3ubuntu1.4) ...
```

when I execute /opt/rocm/bin/rocminfo, an error is prompted：
`-bash: /opt/rocm/bin/rocminfo: No such file or directory`

when I execute /opt/rocm/opencl/bin/clinfo, an error is prompted：
```
dlerror: libhsakmt.so.1: cannot open shared object file: No such file or directory
/opt/rocm/opencl/bin/clinfo: Relink `/usr/lib/x86_64-linux-gnu/libnvidia-opencl.so.1' with `/lib/x86_64-linux-gnu/librt.so.1' for IFUNC symbol `clock_gettime'
Segmentation fault (core dumped)
```
 I have reboot, and reexecute sudo apt install rocm-dkms, it prompt:
```
Reading package lists... Done
Building dependency tree
Reading state information... Done
rocm-dkms is already the newest version (4.1.0.40100-26).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```
but, execeute /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo, still the same error.

May I ask why, thank you.


---

## 评论 (16 条)

### 评论 #1 — xuhuisheng (2021-04-02T05:08:57Z)

The rocm-dkms and rock-dkms is different packages.

The rock-dkms is only a linux drm driver. The rocm-dkms is a meta package which includes rock-dkms and rocm-dev. And the error messages seems about opencl cannot find roct-thunk-interface.

My advise is re-install rocm-dkms from a clear enironment.


---

### 评论 #2 — SomnusMistletoe (2021-04-02T05:48:21Z)

I would like to ask if it is possible that my amd architecture is gfx803. It seems that ROCM 4.0 will not provide support for gfx803.

---

### 评论 #3 — xuhuisheng (2021-04-02T05:56:34Z)

For gfx803, installing is fine. But GEMM had broken since ROCm-3.7, we will get random wrong results when run tensorflow/pytorch.
https://github.com/xuhuisheng/rocm-build/tree/master/gfx803

---

### 评论 #4 — ROCmSupport (2021-04-05T08:03:56Z)

Hi @SomnusMistletoe 
Thanks for reaching out.
Looks like installation did not go well and so many things are missed.
Recommend to uninstall everything related to ROCm and try to do a fresh/clean install.
Thank you.

---

### 评论 #5 — SomnusMistletoe (2021-04-06T06:23:21Z)

> Hi @SomnusMistletoe
> Thanks for reaching out.
> Looks like installation did not go well and so many things are missed.
> Recommend to uninstall everything related to ROCm and try to do a fresh/clean install.
> Thank you.

@ROCmSupport 
Hi，I see this sentence in the document:

> You must use either ROCm or the amdgpu-pro driver

Should I uninstall amdgpu and what should I do to uninstall it?

In addition, if I want to go back to ROCM 4.0，it seems that executing the following statement doesn't work.

`sudo apt install rocm-dkms=4.0`

So what should I do? Thank you.



---

### 评论 #6 — ROCmSupport (2021-04-06T07:04:26Z)

Hi @SomnusMistletoe 
Yes, at a time, you should have amdgpu-pro driver or ROCm.
So I recommend to uninstall rocm and amdgpu-pro both once and install rocm and then check whether things are working or now.
Do a reboot after every uninstall or install.

Command for uninstaling amdgpu-pro driver: 
_amdgpu-pro-uninstall_

or _sudo apt autoremove amdgpu-core_

---

### 评论 #7 — SomnusMistletoe (2021-04-06T12:20:57Z)

Hi @ROCmSupport
I have uninstall amdgpu-core, and reinstall rocm, but it doesn't seem to work.
I have an urgent project to use ROCM environment, and I need to go back to ROCM 4.0, what should I do?
Best regards,
Thank you.



---

### 评论 #8 — ROCmSupport (2021-04-06T12:28:05Z)

Hi @SomnusMistletoe 
Looks like your uninstallation did not go well or some parts are still left.
OK, just uninstall everything now and reboot once.
You can install ROCm 4.0 from [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu](url)
But instead of _https://repo.radeon.com/rocm/apt/debian/_, you need to map to https://repo.radeon.com/rocm/apt/4.0
Thank you.

---

### 评论 #9 — SomnusMistletoe (2021-04-06T12:57:23Z)

Hi @ROCmSupport
Do you mean 
```
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.0 xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
```
instead of
```
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
```
I do as the first way, and uninstall, and reinstall, but get the following error:
```
# sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-dkms : Depends: rocm-dev but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```
Best regards,
Thank you.


---

### 评论 #10 — ROCmSupport (2021-04-06T13:22:40Z)

Yes @SomnusMistletoe 
I did not see any problem with ROCm 4.0 installation. 
I tried just now and its working perfect for me.
Please check the steps below.

Before mapping, I installed gnupg2 as _**apt install gnupg2**_

root@taccuser-X399-DESIGNARE-EX:/# **wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -**
OK
root@taccuser-X399-DESIGNARE-EX:/# **echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.0 xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list**
deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.0 xenial main
root@taccuser-X399-DESIGNARE-EX:/# **apt update**
Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease
Hit:2 http://archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:3 http://security.ubuntu.com/ubuntu focal-security InRelease
Hit:4 http://archive.ubuntu.com/ubuntu focal-backports InRelease
Get:5 https://repo.radeon.com/rocm/apt/4.0 xenial InRelease [1817 B]
Get:6 https://repo.radeon.com/rocm/apt/4.0 xenial/main amd64 Packages [17.6 kB]
Fetched 19.4 kB in 2s (12.7 kB/s)
Reading package lists... Done
Building dependency tree
Reading state information... Done
4 packages can be upgraded. Run 'apt list --upgradable' to see them.

root@taccuser-X399-DESIGNARE-EX:/# **sudo apt install rocm-dkms**
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential comgr cpp cpp-9 dctrl-tools distro-info-data dkms dpkg-dev fakeroot file g++ g++-9
  g++-9-multilib g++-multilib gcc gcc-7-base gcc-8-base gcc-9 gcc-9-base gcc-9-multilib gcc-multilib hip-base hip-doc hip-rocclr hip-samples
  hsa-amd-aqlprofile hsa-rocr-dev hsakmt-roct hsakmt-roct-dev kmod lib32asan5 lib32atomic1 lib32gcc-9-dev lib32gcc-s1 lib32gomp1 lib32itm1 lib32quadmath0
  lib32stdc++-9-dev lib32stdc++6 lib32ubsan1 libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan4 libasan5 libatomic1
  libbabeltrace-ctf1 libbabeltrace1 libbinutils libbsd0 libc-dev-bin libc6-dev libc6-dev-i386 libc6-dev-x32 libc6-i386 libc6-x32 libcc1-0 libcilkrts5
  libcrypt-dev libctf-nobfd0 libctf0 libdpkg-perl libdrm-amdgpu1 libdrm-common libdrm-dev libdrm-intel1 libdrm-nouveau2 libdrm-radeon1 libdrm2 libdw1
  libedit2 libelf-dev libelf1 libexpat1 libfakeroot libfile-fcntllock-perl libfile-which-perl libgcc-7-dev libgcc-9-dev libgdbm-compat4 libgdbm6 libgl-dev
  libgl1 libgl1-mesa-dri libglapi-mesa libglib2.0-0 libglib2.0-data libglvnd0 libglx-dev libglx-mesa0 libglx0 libgomp1 libgpm2 libicu66 libisl22 libitm1
  libkmod2 libllvm11 liblocale-gettext-perl liblsan0 libmagic-mgc libmagic1 libmpc3 libmpdec2 libmpfr6 libmpx2 libncurses5 libnuma1 libpciaccess0 libperl5.30
  libpthread-stubs0-dev libpython3-stdlib libpython3.8 libpython3.8-minimal libpython3.8-stdlib libquadmath0 libsensors-config libsensors5 libstdc++-7-dev
  libstdc++-9-dev libtinfo5 libtsan0 libubsan0 libubsan1 libvulkan1 libwayland-client0 libx11-6 libx11-data libx11-dev libx11-xcb1 libx32asan5 libx32atomic1
  libx32gcc-9-dev libx32gcc-s1 libx32gomp1 libx32itm1 libx32quadmath0 libx32stdc++-9-dev libx32stdc++6 libx32ubsan1 libxau-dev libxau6 libxcb-dri2-0
  libxcb-dri3-0 libxcb-glx0 libxcb-present0 libxcb-randr0 libxcb-sync1 libxcb-xfixes0 libxcb1 libxcb1-dev libxdamage1 libxdmcp-dev libxdmcp6 libxext6
  libxfixes3 libxml2 libxshmfence1 libxxf86vm1 linux-headers-5.4.0-70 linux-headers-5.4.0-70-generic linux-headers-generic linux-libc-dev llvm-amdgpu
  lsb-release make manpages manpages-dev mesa-common-dev mesa-vulkan-drivers mime-support netbase openmp-extras patch perl perl-modules-5.30 python3
  python3-minimal python3.8 python3.8-minimal rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake rocm-dbgapi rocm-dev rocm-device-libs rocm-gdb
  rocm-opencl rocm-opencl-dev rocm-smi rocm-smi-lib64 rocm-utils rocminfo rocprofiler-dev roctracer-dev shared-mime-info tzdata x11proto-core-dev
  x11proto-dev xdg-user-dirs xorg-sgml-doctools xtrans-dev xz-utils zlib1g-dev
Suggested packages:
  binutils-doc cpp-doc gcc-9-locales debtags menu debian-keyring gcc-9-doc lib32stdc++6-9-dbg libx32stdc++6-9-dbg autoconf automake libtool flex bison gdb
  gcc-doc glibc-doc git bzr gdbm-l10n gpm pciutils lm-sensors libstdc++-7-doc libstdc++-9-doc libx11-doc libxcb-doc make-doc man-browser ed diffutils-doc
  perl-doc libterm-readline-gnu-perl | libterm-readline-perl-perl libb-debug-perl liblocale-codes-perl python3-doc python3-tk python3-venv python3.8-venv
  python3.8-doc binfmt-support
The following NEW packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential comgr cpp cpp-9 dctrl-tools distro-info-data dkms dpkg-dev fakeroot file g++ g++-9
  g++-9-multilib g++-multilib gcc gcc-7-base gcc-8-base gcc-9 gcc-9-base gcc-9-multilib gcc-multilib hip-base hip-doc hip-rocclr hip-samples
  hsa-amd-aqlprofile hsa-rocr-dev hsakmt-roct hsakmt-roct-dev kmod lib32asan5 lib32atomic1 lib32gcc-9-dev lib32gcc-s1 lib32gomp1 lib32itm1 lib32quadmath0
  lib32stdc++-9-dev lib32stdc++6 lib32ubsan1 libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan4 libasan5 libatomic1
  libbabeltrace-ctf1 libbabeltrace1 libbinutils libbsd0 libc-dev-bin libc6-dev libc6-dev-i386 libc6-dev-x32 libc6-i386 libc6-x32 libcc1-0 libcilkrts5
  libcrypt-dev libctf-nobfd0 libctf0 libdpkg-perl libdrm-amdgpu1 libdrm-common libdrm-dev libdrm-intel1 libdrm-nouveau2 libdrm-radeon1 libdrm2 libdw1
  libedit2 libelf-dev libelf1 libexpat1 libfakeroot libfile-fcntllock-perl libfile-which-perl libgcc-7-dev libgcc-9-dev libgdbm-compat4 libgdbm6 libgl-dev
  libgl1 libgl1-mesa-dri libglapi-mesa libglib2.0-0 libglib2.0-data libglvnd0 libglx-dev libglx-mesa0 libglx0 libgomp1 libgpm2 libicu66 libisl22 libitm1
  libkmod2 libllvm11 liblocale-gettext-perl liblsan0 libmagic-mgc libmagic1 libmpc3 libmpdec2 libmpfr6 libmpx2 libncurses5 libnuma1 libpciaccess0 libperl5.30
  libpthread-stubs0-dev libpython3-stdlib libpython3.8 libpython3.8-minimal libpython3.8-stdlib libquadmath0 libsensors-config libsensors5 libstdc++-7-dev
  libstdc++-9-dev libtinfo5 libtsan0 libubsan0 libubsan1 libvulkan1 libwayland-client0 libx11-6 libx11-data libx11-dev libx11-xcb1 libx32asan5 libx32atomic1
  libx32gcc-9-dev libx32gcc-s1 libx32gomp1 libx32itm1 libx32quadmath0 libx32stdc++-9-dev libx32stdc++6 libx32ubsan1 libxau-dev libxau6 libxcb-dri2-0
  libxcb-dri3-0 libxcb-glx0 libxcb-present0 libxcb-randr0 libxcb-sync1 libxcb-xfixes0 libxcb1 libxcb1-dev libxdamage1 libxdmcp-dev libxdmcp6 libxext6
  libxfixes3 libxml2 libxshmfence1 libxxf86vm1 linux-headers-5.4.0-70 linux-headers-5.4.0-70-generic linux-headers-generic linux-libc-dev llvm-amdgpu
  lsb-release make manpages manpages-dev mesa-common-dev mesa-vulkan-drivers mime-support netbase openmp-extras patch perl perl-modules-5.30 python3
  python3-minimal python3.8 python3.8-minimal rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake rocm-dbgapi rocm-dev rocm-device-libs rocm-dkms rocm-gdb
  rocm-opencl rocm-opencl-dev rocm-smi rocm-smi-lib64 rocm-utils rocminfo rocprofiler-dev roctracer-dev shared-mime-info tzdata x11proto-core-dev
  x11proto-dev xdg-user-dirs xorg-sgml-doctools xtrans-dev xz-utils zlib1g-dev
0 upgraded, 209 newly installed, 0 to remove and 4 not upgraded.
Need to get 777 MB of archives.
After this operation, 1665 MB of additional disk space will be used.
Do you want to continue? [Y/n] y

---

### 评论 #11 — SomnusMistletoe (2021-04-06T13:57:01Z)

Hi @ROCmSupport 
it doesn't seem to work.
Is it possible that my kernel version is too low? 
```
# uname -r
4.15.0-140-generic
```
but, I have successfully installed rocm4.0 before.

---

### 评论 #12 — sunway513 (2021-04-06T14:46:28Z)

@SomnusMistletoe Yes, you'll need minimum 4.18 in order to install ROCm4.1 kernel driver.. The following instructions would do:
```
sudo apt update
sudo apt install linux-headers-4.18.0-25-generic linux-image-4.18.0-25-generic  linux-modules-4.18.0-25-generic linux-modules-extra-4.18.0-25-generic -y
sudo reboot
```


---

### 评论 #13 — ROCmSupport (2021-04-07T06:27:48Z)

Hi @SomnusMistletoe 
4.15 kernel is very old, recommend to use the latest kernels, atleast 4.18 and above.
In our documentation also, we clearly mentioned to use 5.4 and 5.6 kernels as recommended ones.
Thank you.

---

### 评论 #14 — ROCmSupport (2021-04-09T09:51:48Z)

Hi @SomnusMistletoe 
Please share an update or else close the issue, if the issue is resolved.
So that we can work for you and will update with resolution.
Thank you.

---

### 评论 #15 — SomnusMistletoe (2021-04-15T09:26:04Z)

Hi @ROCmSupport
I reinstalled the os, and install rocm-dkms 4.1.0 and llvm-project, ROCm-Device-Libs, ROCclr successfully.
when I 
`git clone -b rocm-4.1.x https://github.com/ROCm-Developer-Tools/HIP.git`
and continue to make HIP, I get the following error:
```
# make -j
Scanning dependencies of target gen-prof-api-str-header
[  0%] Generating profiling primitives: /usr/local/HIP/build/include/hip/hcc_detail/hip_prof_str.h
api: hip_init - hip_impl
api: hipInit
api: hipDriverGetVersion
api: hipRuntimeGetVersion
api: hipDeviceGet
api: hipDeviceComputeCapability
api: hipDeviceGetName
api: hipDeviceGetP2PAttribute
api: hipDeviceGetPCIBusId
api: hipDeviceGetByPCIBusId
api: hipDeviceTotalMem
api: hipDeviceSynchronize
api: hipDeviceReset
api: hipSetDevice
api: hipGetDevice
api: hipGetDeviceCount
api: hipDeviceGetAttribute
api: hipGetDeviceProperties
api: hipDeviceSetCacheConfig
api: hipDeviceGetCacheConfig
api: hipDeviceGetLimit
api: hipDeviceGetSharedMemConfig
api: hipGetDeviceFlags
api: hipDeviceSetSharedMemConfig
api: hipSetDeviceFlags
api: hipChooseDevice
api: hipExtGetLinkTypeAndHopCount
api: hipIpcGetMemHandle
api: hipIpcOpenMemHandle
api: hipIpcCloseMemHandle
api: hipIpcGetEventHandle
api: hipIpcOpenEventHandle
api: hipFuncSetAttribute
api: hipFuncSetCacheConfig
api: hipFuncSetSharedMemConfig
api: hipGetLastError
api: hipPeekAtLastError
api: hipGetErrorName
api: hipGetErrorString
api: hipStreamCreate
api: hipStreamCreateWithFlags
api: hipStreamCreateWithPriority
api: hipDeviceGetStreamPriorityRange
api: hipStreamDestroy
api: hipStreamQuery
api: hipStreamSynchronize
api: hipStreamWaitEvent
api: hipStreamGetFlags
api: hipStreamGetPriority
api: hipExtStreamCreateWithCUMask
api: hipExtStreamGetCUMask
api: hipStreamAddCallback
api: hipEventCreateWithFlags
api: hipEventCreate
api: hipEventRecord
api: hipEventRecord
api: hipEventDestroy
api: hipEventSynchronize
api: hipEventElapsedTime
api: hipEventQuery
api: hipPointerGetAttributes
api: hipMalloc
api: hipExtMallocWithFlags
api: hipMallocHost
api: hipMemAllocHost
api: hipHostMalloc
api: hipMallocManaged
api: hipMemPrefetchAsync
api: hipMemAdvise
api: hipMemRangeGetAttribute
api: hipMemRangeGetAttributes
api: hipStreamAttachMemAsync
api: hipHostAlloc
api: hipHostGetDevicePointer
api: hipHostGetFlags
api: hipHostRegister
api: hipHostUnregister
api: hipMallocPitch
api: hipMemAllocPitch
api: hipFree
api: hipFreeHost
api: hipHostFree
api: hipMemcpy
api: hipMemcpyWithStream
api: hipMemcpyHtoD
api: hipMemcpyDtoH
api: hipMemcpyDtoD
api: hipMemcpyHtoDAsync
api: hipMemcpyDtoHAsync
api: hipMemcpyDtoDAsync
api: hipModuleGetGlobal
api: hipGetSymbolAddress
api: hipGetSymbolSize
api: hipMemcpyToSymbol
api: hipMemcpyToSymbolAsync
api: hipMemcpyFromSymbol
api: hipMemcpyFromSymbolAsync
api: hipModuleGetGlobal
api: read_agent_global_from_process - hidden
api: hipGetSymbolAddress - hidden
api: hipGetSymbolSize - hidden
api: hipMemcpyToSymbol - hip_impl
api: hipMemcpyToSymbol - hidden
api: hipMemcpyToSymbolAsync - hip_impl
api: hipMemcpyFromSymbol - hip_impl
api: hipMemcpyFromSymbolAsync - hip_impl
api: hipMemcpyToSymbolAsync - hidden
api: hipMemcpyFromSymbol - hidden
api: hipMemcpyFromSymbolAsync - hidden
api: hipMemcpyAsync
api: hipMemset
api: hipMemsetD8
api: hipMemsetD8Async
api: hipMemsetD16
api: hipMemsetD16Async
api: hipMemsetD32
api: hipMemsetAsync
api: hipMemsetD32Async
api: hipMemset2D
api: hipMemset2DAsync
api: hipMemset3D
api: hipMemset3DAsync
api: hipMemGetInfo
api: hipMemPtrGetInfo
api: hipMallocArray
api: hipArrayCreate
api: hipArray3DCreate
api: hipMalloc3D
api: hipFreeArray
api: hipFreeMipmappedArray
api: hipMalloc3DArray
api: hipMallocMipmappedArray
api: hipGetMipmappedArrayLevel
api: hipMemcpy2D
api: hipMemcpyParam2D
api: hipMemcpyParam2DAsync
api: hipMemcpy2DAsync
api: hipMemcpy2DToArray
api: hipMemcpyToArray
api: hipMemcpyFromArray
api: hipMemcpy2DFromArray
api: hipMemcpy2DFromArrayAsync
api: hipMemcpyAtoH
api: hipMemcpyHtoA
api: hipMemcpy3D
api: hipMemcpy3DAsync
api: hipDrvMemcpy3D
api: hipDrvMemcpy3DAsync
api: hipDeviceCanAccessPeer
api: hipDeviceEnablePeerAccess
api: hipDeviceDisablePeerAccess
api: hipMemGetAddressRange
api: hipMemcpyPeer
api: hipMemcpyPeerAsync
api: hipCtxCreate
api: hipCtxDestroy
api: hipCtxPopCurrent
api: hipCtxPushCurrent
api: hipCtxSetCurrent
api: hipCtxGetCurrent
api: hipCtxGetDevice
api: hipCtxGetApiVersion
api: hipCtxGetCacheConfig
api: hipCtxSetCacheConfig
api: hipCtxSetSharedMemConfig
api: hipCtxGetSharedMemConfig
api: hipCtxSynchronize
api: hipCtxGetFlags
api: hipCtxEnablePeerAccess
api: hipCtxDisablePeerAccess
api: hipDevicePrimaryCtxGetState
api: hipDevicePrimaryCtxRelease
api: hipDevicePrimaryCtxRetain
api: hipDevicePrimaryCtxReset
api: hipDevicePrimaryCtxSetFlags
api: hipModuleLoad
api: hipModuleUnload
api: hipModuleGetFunction
api: hipFuncGetAttributes
api: hipFuncGetAttribute
api: hipModuleGetGlobal
api: hipModuleGetTexRef
api: hipModuleLoadData
api: hipModuleLoadDataEx
api: hipModuleLaunchKernel
api: hipLaunchCooperativeKernel
api: hipLaunchCooperativeKernelMultiDevice
api: hipExtLaunchMultiKernelMultiDevice
api: hipModuleOccupancyMaxPotentialBlockSize
api: hipModuleOccupancyMaxPotentialBlockSizeWithFlags
api: hipModuleOccupancyMaxActiveBlocksPerMultiprocessor
api: hipModuleOccupancyMaxActiveBlocksPerMultiprocessorWithFlags
api: hipOccupancyMaxActiveBlocksPerMultiprocessor
api: hipOccupancyMaxActiveBlocksPerMultiprocessorWithFlags
api: hipOccupancyMaxPotentialBlockSize
api: hipProfilerStart
api: hipProfilerStop
api: hipConfigureCall
api: hipSetupArgument
api: hipLaunchByPtr
api: __hipPushCallConfiguration
api: __hipPopCallConfiguration
api: hipLaunchKernel
api: hipExtLaunchKernel
api: hipBindTexture
Parsing /usr/local/HIP/rocclr for '\.cpp$'
/usr/local/HIP/rocclr/hip_stream.cpp
	hipStreamCreateWithFlags
	hipStreamCreate
	hipStreamCreateWithPriority
	hipDeviceGetStreamPriorityRange
	hipStreamGetFlags
	hipStreamSynchronize
	hipStreamDestroy
	hipStreamWaitEvent
	hipStreamQuery
	hipStreamAddCallback
	hipExtStreamCreateWithCUMask
	hipStreamGetPriority
	hipExtStreamGetCUMask
/usr/local/HIP/rocclr/cl_lqdflash_amd.cpp
/usr/local/HIP/rocclr/hip_error.cpp
	hipGetLastError
	hipPeekAtLastError
/usr/local/HIP/rocclr/fixme.cpp
/usr/local/HIP/rocclr/hip_texture.cpp
/usr/local/HIP/rocclr/hip_intercept.cpp
/usr/local/HIP/rocclr/hip_global.cpp
/usr/local/HIP/rocclr/hip_event.cpp
	hipEventCreateWithFlags
	hipEventCreate
	hipEventDestroy
	hipEventElapsedTime
	hipEventRecord
	hipEventSynchronize
	hipEventQuery
/usr/local/HIP/rocclr/hip_activity.cpp
/usr/local/HIP/rocclr/hip_rtc.cpp
/usr/local/HIP/rocclr/hip_device.cpp
	hipDeviceGet
	hipDeviceTotalMem
	hipDeviceComputeCapability
	hipDeviceGetName
	hipGetDeviceProperties
/usr/local/HIP/rocclr/hip_module.cpp
	hipModuleUnload
	hipModuleLoad
	hipModuleLoadData
	hipModuleLoadDataEx
	hipModuleGetFunction
	hipModuleGetGlobal
	hipFuncGetAttribute
	hipFuncGetAttributes
	hipFuncSetAttribute
	hipFuncSetCacheConfig
	hipFuncSetSharedMemConfig
	hipModuleLaunchKernel
	hipExtModuleLaunchKernel
	hipHccModuleLaunchKernel
	hipLaunchKernel
	hipExtLaunchKernel
	hipLaunchCooperativeKernel
	hipLaunchCooperativeKernelMultiDevice
	hipExtLaunchMultiKernelMultiDevice
	hipModuleGetTexRef
/usr/local/HIP/rocclr/hip_context.cpp
	hipInit
	hipCtxCreate
	hipCtxSetCurrent
	hipCtxGetCurrent
	hipCtxGetSharedMemConfig
	hipRuntimeGetVersion
	hipCtxDestroy
	hipCtxPopCurrent
	hipCtxPushCurrent
	hipDriverGetVersion
	hipCtxGetDevice
	hipCtxGetApiVersion
	hipCtxGetCacheConfig
	hipCtxSetCacheConfig
	hipCtxSetSharedMemConfig
	hipCtxSynchronize
	hipCtxGetFlags
	hipDevicePrimaryCtxGetState
	hipDevicePrimaryCtxRelease
	hipDevicePrimaryCtxRetain
	hipDevicePrimaryCtxReset
	hipDevicePrimaryCtxSetFlags
/usr/local/HIP/rocclr/hip_code_object.cpp
/usr/local/HIP/rocclr/hip_device_runtime.cpp
	hipChooseDevice
	hipDeviceGetAttribute
	hipDeviceGetByPCIBusId
	hipDeviceGetCacheConfig
	hipDeviceGetLimit
	hipDeviceGetPCIBusId
	hipDeviceGetSharedMemConfig
	hipDeviceReset
	hipDeviceSetCacheConfig
	hipDeviceSetSharedMemConfig
	hipDeviceSynchronize
	hipGetDevice
	hipGetDeviceCount
	hipGetDeviceFlags
	hipIpcGetEventHandle
	hipIpcOpenEventHandle
	hipSetDevice
	hipSetDeviceFlags
/usr/local/HIP/rocclr/hip_fatbin.cpp
/usr/local/HIP/rocclr/cl_gl.cpp
/usr/local/HIP/rocclr/hip_platform.cpp
	hipConfigureCall
	__hipPushCallConfiguration
	__hipPopCallConfiguration
	hipSetupArgument
	hipLaunchByPtr
	hipGetSymbolAddress
	hipGetSymbolSize
	hipOccupancyMaxPotentialBlockSize
	hipModuleOccupancyMaxPotentialBlockSize
	hipModuleOccupancyMaxPotentialBlockSizeWithFlags
	hipModuleOccupancyMaxActiveBlocksPerMultiprocessor
	hipModuleOccupancyMaxActiveBlocksPerMultiprocessorWithFlags
	hipOccupancyMaxActiveBlocksPerMultiprocessor
	hipOccupancyMaxActiveBlocksPerMultiprocessorWithFlags
/usr/local/HIP/rocclr/hip_peer.cpp
	hipDeviceCanAccessPeer args mismatch:
		/usr/local/HIP/rocclr/hip_peer.cpp line(24)
		api: int*, hipCtx_t, hipCtx_t, 
		eta: int*, int, int, 

	hipMemcpyPeer args mismatch:
		/usr/local/HIP/rocclr/hip_peer.cpp line(33)
		api: void*, hipCtx_t, const void*, hipCtx_t, size_t, 
		eta: void*, int, const void*, int, size_t, 

	hipMemcpyPeerAsync args mismatch:
		/usr/local/HIP/rocclr/hip_peer.cpp line(42)
		api: void*, hipCtx_t, const void*, hipCtx_t, size_t, hipStream_t, 
		eta: void*, int, const void*, int, size_t, hipStream_t, 

	hipExtGetLinkTypeAndHopCount
	hipDeviceGetP2PAttribute
	hipDeviceCanAccessPeer
	hipDeviceDisablePeerAccess
	hipDeviceEnablePeerAccess
	hipMemcpyPeer
	hipMemcpyPeerAsync
	hipCtxEnablePeerAccess
	hipCtxDisablePeerAccess
/usr/local/HIP/rocclr/hip_surface.cpp
/usr/local/HIP/rocclr/hip_hmm.cpp
	hipMallocManaged
	hipMemPrefetchAsync
	hipMemAdvise
	hipMemRangeGetAttribute
	hipMemRangeGetAttributes
	hipStreamAttachMemAsync
/usr/local/HIP/rocclr/hip_memory.cpp
	hipExtMallocWithFlags
	hipMalloc
	hipHostMalloc
	hipFree
	hipMemcpy
	hipMemcpyWithStream
	hipMemPtrGetInfo
	hipHostFree
	hipFreeArray
	hipMemGetAddressRange
	hipMemGetInfo
	hipMallocPitch
	hipMalloc3D
	hipArrayCreate
	hipMallocArray
	hipArray3DCreate
	hipMalloc3DArray
	hipHostGetFlags
	hipHostRegister
	hipHostUnregister
	hipHostAlloc
	hipMemcpyToSymbol
	hipMemcpyFromSymbol
	hipMemcpyToSymbolAsync
	hipMemcpyFromSymbolAsync
	hipMemcpyHtoD
	hipMemcpyDtoH
	hipMemcpyDtoD
	hipMemcpyAsync
	hipMemcpyHtoDAsync
	hipMemcpyDtoDAsync
	hipMemcpyDtoHAsync
	hipMemcpyParam2D
	hipMemcpy2D
	hipMemcpy2DAsync
	hipMemcpy2DToArray
	hipMemcpyToArray
	hipMemcpyFromArray
	hipMemcpyHtoA
	hipMemcpyAtoH
	hipMemcpy3D
	hipMemcpy3DAsync
	hipDrvMemcpy3D
	hipDrvMemcpy3DAsync
	hipMemset
	hipMemsetAsync
	hipMemsetD8
	hipMemsetD8Async
	hipMemsetD16
	hipMemsetD16Async
	hipMemsetD32
	hipMemsetD32Async
	hipMemset2D
	hipMemset2DAsync
	hipMemset3D
	hipMemset3DAsync
	hipMemAllocPitch
	hipMemAllocHost
	hipIpcGetMemHandle
	hipIpcOpenMemHandle
	hipIpcCloseMemHandle
	hipHostGetDevicePointer
	hipPointerGetAttributes
	hipMemcpyParam2DAsync
	hipMemcpy2DFromArray
	hipMemcpy2DFromArrayAsync
	hipMallocMipmappedArray
	hipFreeMipmappedArray
	hipGetMipmappedArrayLevel
	hipMallocHost
	hipFreeHost
/usr/local/HIP/rocclr/hip_profile.cpp
	hipProfilerStart
	hipProfilerStop
Init missing: hipKernelNameRef
 Warning: implementation not found: hipGetErrorName
/usr/local/HIP/rocclr/hip_prof_gen.py Warning: implementation not found: hipGetErrorName
 Warning: implementation not found: hipGetErrorString
/usr/local/HIP/rocclr/hip_prof_gen.py Warning: implementation not found: hipGetErrorString
 Warning: 2 API calls missing in interception layer
/usr/local/HIP/rocclr/hip_prof_gen.py Warning: 2 API calls missing in interception layer
Private: hipCreateTextureObject
Private: hipDestroyTextureObject
Private: hipGetTextureObjectResourceDesc
Private: hipGetTextureObjectResourceViewDesc
Private: hipGetTextureObjectTextureDesc
Private: hipBindTexture2D
Private: hipBindTextureToArray
Private: hipBindTextureToMipmappedArray
Private: hipUnbindTexture
Private: hipBindTexture
Private: hipGetChannelDesc
Private: hipGetTextureAlignmentOffset
Private: hipGetTextureReference
Private: hipTexRefSetFormat
Private: hipTexRefSetFlags
Private: hipTexRefSetFilterMode
Private: hipTexRefGetAddressMode
Private: hipTexRefSetAddressMode
Private: hipTexRefGetArray
Private: hipTexRefSetArray
Private: hipTexRefGetAddress
Private: hipTexRefSetAddress
Private: hipTexRefSetAddress2D
Private: hipTexRefGetBorderColor
Private: hipTexRefGetFilterMode
Private: hipTexRefGetFlags
Private: hipTexRefGetFormat
Private: hipTexRefGetMaxAnisotropy
Private: hipTexRefGetMipmapFilterMode
Private: hipTexRefGetMipmapLevelBias
Private: hipTexRefGetMipmapLevelClamp
Private: hipTexRefGetMipmappedArray
Private: hipTexRefSetBorderColor
Private: hipTexRefSetMaxAnisotropy
Private: hipTexRefSetMipmapFilterMode
Private: hipTexRefSetMipmapLevelBias
Private: hipTexRefSetMipmapLevelClamp
Private: hipTexRefSetMipmappedArray
Private: hipTexObjectCreate
Private: hipTexObjectDestroy
Private: hipTexObjectGetResourceDesc
Private: hipTexObjectGetResourceViewDesc
Private: hipTexObjectGetTextureDesc
Private: hipDeviceGetCount
Private: ihipModuleLaunchKernel
Private: hipModuleLaunchKernelExt
Private: hipSetValidDevices
Private: hipCreateSurfaceObject
Private: hipDestroySurfaceObject
Private: hipArrayDestroy
Private: hipArray3DGetDescriptor
Private: hipArrayGetDescriptor
Private: hipMemcpy2DArrayToArray
Private: hipMemcpyArrayToArray
Private: hipMemcpyFromArrayAsync
Private: hipMemcpy2DToArrayAsync
Private: hipMemcpyToArrayAsync
Private: hipMemcpyAtoA
Private: hipMemcpyAtoD
Private: hipMemcpyAtoHAsync
Private: hipMemcpyDtoA
Private: hipMemcpyHtoAAsync
Private: hipMipmappedArrayCreate
Private: hipMipmappedArrayDestroy
Private: hipMipmappedArrayGetLevel
[  0%] Built target gen-prof-api-str-header
Scanning dependencies of target hip64
[  0%] Building CXX object rocclr/CMakeFiles/hip64.dir/hip_context.cpp.o
In file included from /usr/local/HIP/rocclr/hip_platform.hpp:23,
                 from /usr/local/HIP/rocclr/hip_context.cpp:23:
/usr/local/HIP/rocclr/hip_fatbin.hpp:49:61: error: macro "guarantee" passed 2 arguments, but takes just 1
   49 |     guarantee(device_id >= 0, "Invalid DeviceId less than 0");
      |                                                             ^
In file included from /usr/local/ROCclr/include/top.hpp:101,
                 from /usr/local/ROCclr/include/vdi_common.hpp:24,
                 from /usr/local/HIP/rocclr/hip_internal.hpp:24,
                 from /usr/local/HIP/rocclr/hip_context.cpp:22:
/usr/local/ROCclr/utils/debug.hpp:93: note: macro "guarantee" defined here
   93 | #define guarantee(cond)                                                                            \
      | 
In file included from /usr/local/HIP/rocclr/hip_platform.hpp:23,
                 from /usr/local/HIP/rocclr/hip_context.cpp:23:
/usr/local/HIP/rocclr/hip_fatbin.hpp:50:131: error: macro "guarantee" passed 2 arguments, but takes just 1
   50 |  "Invalid DeviceId, greater than no of fatbin device info!");
      |                                                            ^

In file included from /usr/local/ROCclr/include/top.hpp:101,
                 from /usr/local/ROCclr/include/vdi_common.hpp:24,
                 from /usr/local/HIP/rocclr/hip_internal.hpp:24,
                 from /usr/local/HIP/rocclr/hip_context.cpp:22:
/usr/local/ROCclr/utils/debug.hpp:93: note: macro "guarantee" defined here
   93 | #define guarantee(cond)                                                                            \
      | 
In file included from /usr/local/HIP/rocclr/hip_platform.hpp:25,
                 from /usr/local/HIP/rocclr/hip_context.cpp:23:
/usr/local/HIP/rocclr/hip_code_object.hpp:98:74: error: macro "guarantee" passed 2 arguments, but takes just 1
   98 |       guarantee(false, "Device mismatch from where this module is loaded");
      |                                                                          ^
In file included from /usr/local/ROCclr/include/top.hpp:101,
                 from /usr/local/ROCclr/include/vdi_common.hpp:24,
                 from /usr/local/HIP/rocclr/hip_internal.hpp:24,
                 from /usr/local/HIP/rocclr/hip_context.cpp:22:
/usr/local/ROCclr/utils/debug.hpp:93: note: macro "guarantee" defined here
   93 | #define guarantee(cond)                                                                            \
      | 
In file included from /usr/local/HIP/rocclr/hip_internal.hpp:25,
                 from /usr/local/HIP/rocclr/hip_context.cpp:22:
/usr/local/HIP/rocclr/hip_prof_api.h: In constructor ‘api_callbacks_table_t::api_callbacks_table_t()’:
/usr/local/HIP/rocclr/hip_prof_api.h:72:59: warning: ‘void* memset(void*, int, size_t)’ clearing an object of type ‘struct api_callbacks_table_t::hip_cb_table_t’ with no trivial copy-assignment; use value-initialization instead [-Wclass-memaccess]
   72 |      memset(&callbacks_table_, 0, sizeof(callbacks_table_));
      |                                                           ^
/usr/local/HIP/rocclr/hip_prof_api.h:67:10: note: ‘struct api_callbacks_table_t::hip_cb_table_t’ declared here
   67 |   struct hip_cb_table_t {
      |          ^~~~~~~~~~~~~~
In file included from /usr/local/HIP/rocclr/hip_platform.hpp:23,
                 from /usr/local/HIP/rocclr/hip_context.cpp:23:
/usr/local/HIP/rocclr/hip_fatbin.hpp: In member function ‘void hip::FatBinaryInfo::DeviceIdCheck(int) const’:
/usr/local/HIP/rocclr/hip_fatbin.hpp:49:5: error: ‘guarantee’ was not declared in this scope
   49 |     guarantee(device_id >= 0, "Invalid DeviceId less than 0");
      |     ^~~~~~~~~
In file included from /usr/local/HIP/rocclr/hip_platform.hpp:25,
                 from /usr/local/HIP/rocclr/hip_context.cpp:23:
/usr/local/HIP/rocclr/hip_code_object.hpp: In member function ‘void hip::DynCO::CheckDeviceIdMatch()’:
/usr/local/HIP/rocclr/hip_code_object.hpp:98:7: error: ‘guarantee’ was not declared in this scope
   98 |       guarantee(false, "Device mismatch from where this module is loaded");
      |       ^~~~~~~~~
make[2]: *** [rocclr/CMakeFiles/hip64.dir/build.make:63: rocclr/CMakeFiles/hip64.dir/hip_context.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:9439: rocclr/CMakeFiles/hip64.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
```
Best regards,
Thank you.

---

### 评论 #16 — ROCmSupport (2021-04-16T11:10:25Z)

Hi @SomnusMistletoe 
Looks like your installation went well after clean installation. Thanks for the update
Hence I am closing this ticket now.

Request you to open a new issue for HIP installation with all exact steps you followed.
Thank you.

---
