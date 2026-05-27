# Problems with installation on 16.04 (toshiba sat with r7 260)

> **Issue #493**
> **状态**: closed
> **创建时间**: 2018-08-07T07:34:31Z
> **更新时间**: 2021-06-21T15:54:28Z
> **关闭时间**: 2018-08-23T16:13:46Z
> **作者**: mosheliv
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/493

## 描述

I have followed the installation instructions several times, from scratch, but still the end result is the same:
1. installed 16.04
`m@dl1:~$ uname -a
Linux dl1 4.4.0-116-generic #140-Ubuntu SMP Mon Feb 12 21:23:04 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```
`m@dl1:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.4 LTS
Release:	16.04
Codename:	xenial
```

2. did the next part (not including the log, nothing special)
```
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot
```
3. added the repo, still not very interesting
```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
sudo apt update
```
4. installed rocm-dkms, still uneventfull
```
sudo apt install rocm-dkms
```
5.  added video group
`sudo usermod -a -G video $LOGNAME `
and rebooted

6. Now things start to squeak...
```
m@dl1:~$ rocminfo
rocminfo: command not found
```
ok, no big deal, lets find it:
```
m@dl1:~$ sudo /opt/rocm/bin/rocminfo 
[sudo] password for m: 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
m@dl1:~$ 
```
and:
```
m@dl1:~$ clinfo
The program 'clinfo' is currently not installed. You can install it by typing:
sudo apt install clinfo
```
no big deal, lets install it
```
m@dl1:~$ sudo clinfo
Number of platforms                               0
```

read the faq:
```
m@dl1:~$ dmesg | grep kfd
[    1.231543] kfd kfd: Initialized module
m@dl1:~$ sudo apt-get autoremove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
m@dl1:~$ dmesg | grep amdgpu
[    1.226981] [drm] amdgpu kernel modesetting enabled.
[    1.231685] amdgpu 0000:09:00.0: enabling device (0100 -> 0103)
[    2.153698] [drm] add ip block number 3 <amdgpu_powerplay>
[    2.161257] amdgpu 0000:09:00.0: VRAM: 2048M 0x000000F400000000 - 0x000000F47FFFFFFF (2048M used)
[    2.161259] amdgpu 0000:09:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    2.161340] [drm] amdgpu: 2048M of VRAM memory ready
[    2.161341] [drm] amdgpu: 7902M of GTT memory ready.
[    2.165592] amdgpu: [powerplay] can't get the mac of 5
[    2.167168] amdgpu: [powerplay] VBIOS did not find boot engine clock value in dependency table. Using Memory DPM level 0!
[    7.818082] amdgpu: [powerplay] VI should always have 2 performance levels
[    7.864713] amdgpu 0000:09:00.0: GPU pci config reset
```

So, I really don't know what to do now. this is a fresh install, ,and I followed the readme to the letter.
Any help will be greatly appreciated

---

## 评论 (16 条)

### 评论 #1 — jlgreathouse (2018-08-07T16:05:38Z)

Hello @mosheliv 

Could you give me a bit more information about your hardware setup? There are hundreds of Toshiba Satellite models, so I'm not exactly sure what hardware you're using.

That said, if you're using a Radeon R7 260, I believe that is a "Bonaire" GPU. Unfortunately, the ROCm software stack does not offer support for Bonaire GPUs. Bonaire is a "Sea Islands" class GPU, which is often categorized in our Linux utilites as 'gfx7'. Unfortunately, the only 'gfx7' GPU that ROCm supports is Hawaii, and it only supports this in an experimental capacity.

You may want to explore using the amdgpu-pro software stack for using your GPU for compute under Linux.

---

### 评论 #2 — mosheliv (2018-08-07T22:17:42Z)

Thank you for your prompt reply. it is Toshiba satellite L50-B
I actually tried to understand from the readme if the r7 260 is supported or not. It seems to focus on what cpus are supported and there is actually little to no information about the gpus, which is... strange.
I am looking to use tensorflow 1.8 with gpu acceleration (as detailed https://gpuopen.com/rocm-tensorflow-1-8-release). I don't think the amdgpu-pro stack will allow the installation of this, right?
There is also some patches of information about installing tensorflow 1.8 over opencl but it is very unclear if this works or stable. Any pointers will be greatly appreciated.
Thanks

---

### 评论 #3 — jlgreathouse (2018-08-08T00:28:42Z)

Hi @mosheliv 

Unfortunately, the Radeon R7 260 is not on our supported list of GPUs for ROCm. (You can find a slightly out of date list [here](https://rocm.github.io/hardware.html). I will try to update this when I get a spare moment). The R7 260 is an older model GPU that, as shipped, does not support all of the features we need for the ROCm software stack to work. We were able to make enough changes to get "Hawaii" GPUs from that generation working, but these "Bonaire" GPUs currently will not run in ROCm.

I do not believe the amdgpu-pro software stack will work with our MIOpen version of TensorFlow. MIOpen relies on the HIP programming language, which currently does not run on amdgpu-pro.

I can't speak towards any OpenCL ports of TensorFlow.

---

### 评论 #4 — marwenmessaoud (2018-08-09T23:21:49Z)

Hi @jlgreathouse 
Can you tell me please if the AMD FirePro M4150 is supported or not. 

---

### 评论 #5 — jlgreathouse (2018-08-09T23:26:32Z)

Hello @marwenmessaoud 

The AMD FirePro M4150 is unfortunately not supported by the ROCm software stack. The GPU chip in this product is a variant of our "Oland" GPU, which is from our gfx6 generation of GPUs. This was also known as "Southern Islands". ROCm is primarily supported on gfx8 and above, though we offer support for a single gfx7 GPU ("Hawaii", as described above). Oland is older than this, however, so we are unable to support it.

---

### 评论 #6 — gshashank84 (2018-08-19T13:59:03Z)

I am also having the same problem and i followed the same steps as above stated. My hardware config are-- 
Intel i5 8th gen
AMD Graphics 550
Ubuntu
Python 3.5.0

when i entered clinfo in command line then
~~~
Number of platforms                               1
  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 18.0.5
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   Clover
Number of devices                                 1
  Device Name                                     AMD ICELAND (DRM 3.25.0 / 4.15.0-32-generic, LLVM 6.0.0)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 18.0.5
  Driver Version                                  18.0.5
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               6
  Max clock frequency                             1024MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2       
    half                                                 8 / 8        (cl_khr_fp16)
    float                                                4 / 4       
    double                                               2 / 2        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              7725101872 (7.195GiB)
  Error Correction support                        No
  Max memory allocation                           1931275468 (1.799GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       32768 bits (4096 bytes)
  Global Memory cache type                        None
  Image support                                   No
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Max number of constant args                     16
  Max constant buffer size                        1931275468 (1.799GiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Profiling timer resolution                      0ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_fp16

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [MESA]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD ICELAND (DRM 3.25.0 / 4.15.0-32-generic, LLVM 6.0.0)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD ICELAND (DRM 3.25.0 / 4.15.0-32-generic, LLVM 6.0.0)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD ICELAND (DRM 3.25.0 / 4.15.0-32-generic, LLVM 6.0.0)
~~~

And when i entered rocminfo on command line then
~~~
rocminfo: command not found
~~~

---

### 评论 #7 — jlgreathouse (2018-08-19T18:30:10Z)

I don't recognize the "Iceland" name, as I don't think we officially named any parts that (this may have be a result of whatever version of open source runtime you're using taking some pre-release codename and applying it another part).

Could you run the following commands and show me their output?
```shell
sudo lspci
sudo lspci -n
```

Based on some googling, I strongly suspect that ROCm does not support your GPU.

---

### 评论 #8 — gstoner (2018-08-19T18:36:08Z)

Double check the driver is seeing the GPU remember Laptop shut off the discreet GPU by default and use the iGPU in Linux.  

---

### 评论 #9 — gshashank84 (2018-08-19T18:39:23Z)

i ran the following commands 
~~~
sudo lspci
sudo lspci -n
~~~
Output of first command-
~~~
 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 08)
00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620 (rev 07)
00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 08)
00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 (rev 21)
00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
00:17.0 RAID bus controller: Intel Corporation 82801 Mobile SATA Controller [RAID mode] (rev 21)
00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1)
00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
00:1c.5 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #6 (rev f1)
00:1f.0 ISA bridge: Intel Corporation Intel(R) 100 Series Chipset Family LPC Controller/eSPI Controller - 9D4E (rev 21)
00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Topaz XT [Radeon R7 M260/M265 / M340/M360 / M440/M445] (rev c1)
02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL810xE PCI Express Fast Ethernet controller (rev 07)
03:00.0 Network controller: Qualcomm Atheros QCA9377 802.11ac Wireless Network Adapter (rev 31)
~~~
Output of 2nd command--
~~~
0600: 8086:5914 (rev 08)
00:02.0 0300: 8086:5917 (rev 07)
00:04.0 1180: 8086:1903 (rev 08)
00:14.0 0c03: 8086:9d2f (rev 21)
00:14.2 1180: 8086:9d31 (rev 21)
00:15.0 1180: 8086:9d60 (rev 21)
00:16.0 0780: 8086:9d3a (rev 21)
00:17.0 0104: 8086:282a (rev 21)
00:1c.0 0604: 8086:9d10 (rev f1)
00:1c.4 0604: 8086:9d14 (rev f1)
00:1c.5 0604: 8086:9d15 (rev f1)
00:1f.0 0601: 8086:9d4e (rev 21)
00:1f.2 0580: 8086:9d21 (rev 21)
00:1f.3 0403: 8086:9d71 (rev 21)
00:1f.4 0c05: 8086:9d23 (rev 21)
01:00.0 0380: 1002:6900 (rev c1)
02:00.0 0200: 10ec:8136 (rev 07)
03:00.0 0280: 168c:0042 (rev 31)
~~~

---

### 评论 #10 — jlgreathouse (2018-08-19T22:58:51Z)

Thank you, @gshashank84 ,

Could you please run the following commands and show me the output? Thanks.

- `lsmod | grep amdgpu`
- `lsmod | grep amdkfd`
- `groups`
- `lspci -tv`
- After a reboot: `dmesg`
- `/opt/rocm/bin/rocminfo`
- `/opt/rocm/opencl/bin/x86_64/clinfo`

---

### 评论 #11 — jlgreathouse (2018-08-23T16:13:46Z)

Actually, sorry @gshashank84 

I see now that your GPU's PCIe device ID ix 0x6900. Unfortunately, that device is not in our [list of supported GPUs in the amdkfd driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.8.x/drivers/gpu/drm/amd/amdkfd/kfd_device.c#L226). As such, I'm sorry to say that ROCm is not supported on your GPU.

---

### 评论 #12 — moriel5 (2021-06-13T20:41:53Z)

Are there any thoughts on expanding the experimental support to Bonaire? Or are there blockers to that which do not exist on Hawaii?

---

### 评论 #13 — ROCmSupport (2021-06-14T05:39:18Z)

Hi @moriel5 
We do not have plans right now to support cards specific to gfx8 and below.
Thank you.

---

### 评论 #14 — moriel5 (2021-06-14T05:49:42Z)

@ROCmSupport Pretty much as expected.
I was just wondering whether there are any technical hurdles for Bonaire in addition to what was required for Hawaii. 

---

### 评论 #15 — jlgreathouse (2021-06-21T14:28:27Z)

There is technical tasks required to get ROCm reliably running on Bonaire that AMD does not plan on working on at this time, yes.

---

### 评论 #16 — moriel5 (2021-06-21T15:54:27Z)

Thanks, while slightly disappointing, this certainly makes sense.
I guess the only recourse is searching for something that only has a UEFI, which means I'll have to wait until I have the budget to do so (and then something from the RX 400 or RX 500 series will make more sense).

---
