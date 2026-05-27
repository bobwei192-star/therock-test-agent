# rx 580 Call returned 4104

> **Issue #719**
> **状态**: closed
> **创建时间**: 2019-02-26T17:48:14Z
> **更新时间**: 2019-05-01T22:15:43Z
> **关闭时间**: 2019-03-12T11:52:06Z
> **作者**: tu6ge
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/719

## 描述

help me , my problem is up
```
tu6ge@tu6ge-desktop:/opt/rocm/bin$ ./rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104
tu6ge@tu6ge-desktop:/opt/rocm/bin$ /opt/rocm/opencl/bin/x86_64/clinfo 
ERROR: clGetPlatformIDs(-1001)
```
my pc info:
```
tu6ge@tu6ge-desktop:~$ groups
tu6ge adm cdrom sudo dip video plugdev lpadmin sambashare
tu6ge@tu6ge-desktop:~$ uname -r
4.15.0-45-generic
tu6ge@tu6ge-desktop:~$ dkms status
amdgpu, 2.1-96, 4.15.0-45-generic, x86_64: installed
tu6ge@tu6ge-desktop:~$ modinfo amdgpu | grep filename
filename:       /lib/modules/4.15.0-45-generic/updates/dkms/amdgpu.ko
tu6ge@tu6ge-desktop:~$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-45-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[    1.130512] kfd kfd: DID 6fdf is missing in supported_devices
[    1.130513] kfd kfd: kgd2kfd_probe failed
tu6ge@tu6ge-desktop:~$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-45-generic (buildd@lgw01-amd64-031) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #48-Ubuntu SMP Tue Jan 29 16:28:13 UTC 2019 (Ubuntu 4.15.0-45.48-generic 4.15.18)
[    0.857513] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[    0.996854] amdkcl: loading out-of-tree module taints kernel.
[    0.996868] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    1.128409] [drm] amdgpu kernel modesetting enabled.
[    1.128410] [drm] amdgpu version: 19.10.7.418
[    1.129939] fb: switching to amdgpudrmfb from EFI VGA
[    1.130702] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.130773] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[    1.130774] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    1.130907] [drm] amdgpu: 8192M of VRAM memory ready
[    1.130907] [drm] amdgpu: 8192M of GTT memory ready.
[    1.365826] fbcon: amdgpudrmfb (fb0) is primary device
[    1.365900] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    1.391539] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:01:00.0 on minor 0
```
 My English is so poor ，sorry

---

## 评论 (23 条)

### 评论 #1 — jlgreathouse (2019-02-26T23:16:33Z)

Hm, looks like we're missing 0x6fdf in our KFD's device list. Thank you for the report, I will try to get this added into future ROCm releases.

In the mean time, could you do the following?

1. Open `/usr/src/amdgpu-2.1-96/amd/amdkfd/kfd_device.c` (you may need to open with `sudo`).
1. Add the following on line 357: `    { 0x6FDF, &polaris10_device_info }, /* Polaris10 */`
1. Run the following commands:
   1. `sudo dkms remove amdgpu/2.1-96 --all`
   1. `sudo dkms add amdgpu/2.1-96`
   1. `sudo dkms install amdgpu/2.1-96`
1. Reboot

After rebooting, what does `dmesg | grep kfd` say?

---

### 评论 #2 — tu6ge (2019-02-27T00:59:35Z)

thinks, I go home for a try in the evening( from china) ^_^

---

### 评论 #3 — tu6ge (2019-02-27T12:02:08Z)

```
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[    1.600048] kfd kfd: Allocated 3969056 bytes on gart
[    1.600681] kfd kfd: added device 1002:6fdf
```

---

### 评论 #4 — tu6ge (2019-02-27T12:02:45Z)

```
tu6ge@tu6ge-desktop:~$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104
tu6ge@tu6ge-desktop:~$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
```

---

### 评论 #5 — tu6ge (2019-02-27T17:40:14Z)

How long will it take to solve this problem？
thinks

---

### 评论 #6 — jlgreathouse (2019-02-27T18:03:14Z)

Officially? Perhaps by the next release of ROCm. It may take longer. I cannot give you any guarantees.

---

### 评论 #7 — jlgreathouse (2019-02-27T18:05:41Z)

It appears that you editing your post that tested `dmesg | grep kfd`. My email notification shows that you originally did not see any output messages from the kfd in your dmesg. You then immediately followed up with a post showing that the user-level software (e.g. `rocminfo` did not work).

You then updated your post to show that your KFD *does* work, but you did not go back and test `rocminfo`.

Could you please verify that, on your system where the KFD shows that it "added device 1002:6fdf", you still see `rocminfo` failing to work?

---

### 评论 #8 — tu6ge (2019-02-28T00:09:08Z)


I update with you.first reboot dmsg | grep kfd，result is nothing.but second reboot show 
'''
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[    1.600048] kfd kfd: Allocated 3969056 bytes on gart
[    1.600681] kfd kfd: added device 1002:6fdf
'''
but rocminfo is not work

---

### 评论 #9 — jlgreathouse (2019-02-28T00:31:06Z)

Looks like we would also need to make a patch to [the Thunk](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/roc-2.1.0/src/topology.c#L149) to add in this new PCI ID. It's probably best if you just wait until a new version of ROCm comes out, as it's non-trivial to rebuild the Thunk. If you're willing to wait a few days, I can give you directions on how to do this for ROCm 2.1 if you so desire, but I do not have the time to do so at this moment.

---

### 评论 #10 — tu6ge (2019-02-28T01:04:00Z)

thank you,tell me how to do this for ROCm

---

### 评论 #11 — tu6ge (2019-02-28T02:31:58Z)

after update that,I'm afraid there will be other problems.

---

### 评论 #12 — tu6ge (2019-03-04T14:35:45Z)

I'm looking forward to it.

---

### 评论 #13 — tu6ge (2019-03-09T01:24:54Z)

 The problem has been solved. 

---

### 评论 #14 — Djip007 (2019-03-09T03:03:12Z)

dmesg | grep kfd

```[    2.497777] kfd kfd: Allocated 3969056 bytes on gart
[    2.503387] kfd kfd: added device 1002:67ef
[    2.510806] kfd kfd: DID 15d8 is missing in supported_devices
[    2.510808] kfd kfd: kgd2kfd_probe failed
```


uname -a
```
Linux localhost.localdomain 4.20.13-200.fc29.x86_64 #1 SMP Wed Feb 27 19:42:55 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```

 lspci -tv
``` 
```-[0000:00]-+-00.0  Advanced Micro Devices, Inc. [AMD] Device 15d0
           +-00.2  Advanced Micro Devices, Inc. [AMD] Device 15d1
           +-01.0  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
           +-01.1-[01]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X]
           +-01.2-[02]----00.0  Kingston Technology Company, Inc. Device 5008
           +-01.3-[03]----00.0  Realtek Semiconductor Co., Ltd. RTL8821CE 802.11ac PCIe Wireless Network Adapter
           +-01.4-[04]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           +-08.0  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
           +-08.1-[05]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Picasso
           |            +-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller
           |            +-00.2  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
           |            +-00.3  Advanced Micro Devices, Inc. [AMD] Device 15e0
           |            +-00.4  Advanced Micro Devices, Inc. [AMD] Device 15e1
           |            \-00.6  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller
           +-08.2-[06]----00.0  Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode]
           +-14.0  Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller
           +-14.3  Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge
           +-18.0  Advanced Micro Devices, Inc. [AMD] Device 15e8
           +-18.1  Advanced Micro Devices, Inc. [AMD] Device 15e9
           +-18.2  Advanced Micro Devices, Inc. [AMD] Device 15ea
           +-18.3  Advanced Micro Devices, Inc. [AMD] Device 15eb
           +-18.4  Advanced Micro Devices, Inc. [AMD] Device 15ec
           +-18.5  Advanced Micro Devices, Inc. [AMD] Device 15ed
           +-18.6  Advanced Micro Devices, Inc. [AMD] Device 15ee
           \-18.7  Advanced Micro Devices, Inc. [AMD] Device 15ef
```
System Information
```  PROCESSOR:          AMD Ryzen 5 3550H @ 2.10GHz
    Core Count:       4                                        
    Thread Count:     8                                        
    Extensions:       SSE 4.2 + AVX2 + AVX + RDRAND + FSGSBASE 
    Cache Size:       512 KB                                   
    Microcode:        0x8108102                                
    Scaling Driver:   acpi-cpufreq ondemand                    

  GRAPHICS:           ASUS AMD Picasso 4GB
    Frequency:        1223/1750MHz                                                      
    OpenCL:           OpenCL 1.2 pocl RelWithDebInfo LLVM 7.0.1 SLEEF DISTRO POCL_DEBUG 
    Screen:           1920x1080                                                         
 
  MOTHERBOARD:        ASUS FX505DY v1.0
    BIOS Version:     FX505DY.304                                                 
    Chipset:          AMD Device 15d0                                             
    Audio:            AMD Raven/Raven2/Fenghuang                                  
    Network:          Realtek RTL8111/8168/8411 + Realtek RTL8821CE 802.11ac PCIe 

  MEMORY:             8192MB

  DISK:               128GB KINGSTON RBUSNS8154P3128GJ + 1000GB Seagate ST1000LM035-1RK1
    File-System:      ext4                 
    Mount Options:    relatime rw seclabel 
    Disk Scheduler:   CFQ                  

  OPERATING SYSTEM:   Fedora 29
    Kernel:           4.20.13-200.fc29.x86_64 (x86_64)                                   
    Desktop:          GNOME Shell 3.30.2                                                 
    Display Server:   X Server                                                           
    Compiler:         GCC 8.3.1 20190223 + Clang 8.0 + LLVM 4.0.0                        
    Security:         SELinux                                                            
                      + __user pointer sanitization                                      
                      + Full AMD retpoline IBPB: conditional STIBP: disabled RSB filling 
                      + SSB disabled via prctl and seccomp                               
```
Can you add this Raven card?

---

### 评论 #15 — Djip007 (2019-03-09T03:21:43Z)

and the RX560 may work... is it normal to have this:
```
rocminfo 
hsa api call failure at line 900, file: /data/jenkins_workspace/sandbox-centos/rocm-rel-2.1/rocm-2.1-96-20190201/centos/rocminfo/rocminfo.cc. Call returned 4104
```
rocm-smi
```
========================        ROCm System Management Interface        ========================
================================================================================================
GPU   Temp   AvgPwr   SCLK    MCLK    PCLK           Fan     Perf    PwrCap   SCLK OD   MCLK OD  GPU%
GPU[0] 		: WARNING: Unable to read /sys/class/hwmon/hwmon1/temp1_input
GPU[0] 		: WARNING: Unable to read /sys/class/hwmon/hwmon1/power1_average
0     N/A    N/A      N/A     N/A     N/A            0%      off     48.0W    0%        0%       0%       
GPU[1] 		: WARNING: Unable to read /sys/class/hwmon/hwmon2/power1_average
GPU[1] 		: WARNING: Empty SysFS value: pclk
GPU[1] 		: WARNING: Unable to read /sys/class/drm/card1/device/gpu_busy_percent
1     37.0c  N/A      300Mhz  933Mhz  N/A            0.0%    auto    N/A      0%        0%       N/A      
================================================================================================
========================               End of ROCm SMI Log              ========================
```

---

### 评论 #16 — kentrussell (2019-03-12T11:52:06Z)

@Djip007 We don't have official Fedora support, which is likely why you're hitting those issues. If you're having issues using the upstream kernel, you should raise a bug report with the upstream kernel (https://bugs.freedesktop.org/ under amdgfx)

From the README:
For example, Fedora may work but may not be compatible with the rock-dkms kernel driver. As such, users may want to skip the rocm-dkms and rock-dkms packages, as described above, and instead use the upstream kernel driver.


@tu6ge 
Glad to see that things are working now. I'll close the ticket since things are working for you

---

### 评论 #17 — Djip007 (2019-03-12T23:45:44Z)

I know for fedora... I will report it to kernel to. But after read your comment I look here:
https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/roc-2.1.0/src/topology.c#L203
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdkfd/kfd_device.c#L322
the device (Vega8..) DID 15d8 (Ryzen 5 3550H) is missing in the rocm part too.

For testing I made change in kernel 5.0.0... but not sur it is good... any advise welcome
```
diff --git a/drivers/gpu/drm/amd/amdkfd/kfd_device.c b/drivers/gpu/drm/amd/amdkfd/kfd_device.c
index 8be9677c0c07..73e722cc6ae2 100644
--- a/drivers/gpu/drm/amd/amdkfd/kfd_device.c
+++ b/drivers/gpu/drm/amd/amdkfd/kfd_device.c
@@ -319,6 +319,7 @@ static const struct kfd_deviceid supported_devices[] = {
        { 0x9875, &carrizo_device_info },       /* Carrizo */
        { 0x9876, &carrizo_device_info },       /* Carrizo */
        { 0x9877, &carrizo_device_info },       /* Carrizo */
+       { 0x15D8, &raven_device_info },         /* Raven */
        { 0x15DD, &raven_device_info },         /* Raven */
 #endif
        { 0x67A0, &hawaii_device_info },        /* Hawaii */
```

---

### 评论 #18 — JishinMaster (2019-03-18T16:26:37Z)

Hi,
I have had a similar issue with rocm2.2.
rocm-smi was working, but rocm-info was not.

I used some of the tips from this post to solve my problem.
You can read what I have done here : https://github.com/RadeonOpenCompute/ROCm/issues/731 


---

### 评论 #19 — tu6ge (2019-04-26T11:45:00Z)

There's something wrong with the new version.

```
tu6ge@tu6ge-desktop:~$ rocminfo 
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.3/rocminfo/rocminfo.cc. Call returned 4104
```
my computer`s info :
```
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   13.360582] kfd kfd: Allocated 3969056 bytes on gart
[   13.361135] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ uname -a
Linux tu6ge-desktop 4.15.0-041500-generic #201802011154 SMP Thu Feb 1 11:55:45 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
tu6ge@tu6ge-desktop:~$ groups
tu6ge adm cdrom sudo dip video plugdev lpadmin sambashare
tu6ge@tu6ge-desktop:~$ uname -r
4.15.0-041500-generic
tu6ge@tu6ge-desktop:~$ dkms status
amdgpu, 2.3-14, 4.15.0-041500-generic, x86_64: installed
virtualbox, 5.2.18, 4.15.0-041500-generic, x86_64: installed
tu6ge@tu6ge-desktop:~$ modinfo amdgpu | grep filename
filename:       /lib/modules/4.15.0-041500-generic/updates/dkms/amdgpu.ko
tu6ge@tu6ge-desktop:~$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-041500-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   13.360582] kfd kfd: Allocated 3969056 bytes on gart
[   13.361135] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ dmesg | grep amd
[   11.055816] amdkcl: loading out-of-tree module taints kernel.
[   11.055833] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   11.615325] [drm] amdgpu kernel modesetting enabled.
[   11.615326] [drm] amdgpu version: 5.0.19.20.6
[   12.320874] fb: switching to amdgpudrmfb from EFI VGA
[   12.321506] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[   12.772981] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[   12.772983] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   12.773139] [drm] amdgpu: 8192M of VRAM memory ready
[   12.773141] [drm] amdgpu: 8192M of GTT memory ready.
[   13.362648] fbcon: amdgpudrmfb (fb0) is primary device
[   13.401764] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[   13.432512] [drm] Initialized amdgpu 3.31.0 20150101 for 0000:01:00.0 on minor 0
```

---

### 评论 #20 — tu6ge (2019-04-26T11:46:06Z)

@jlgreathouse 

---

### 评论 #21 — tu6ge (2019-04-28T15:19:23Z)

help me ,how to do it, I waiting for it long time 

---

### 评论 #22 — tu6ge (2019-04-28T15:20:13Z)

 Maybe it's a mistake for me to buy an AMD GPU 

---

### 评论 #23 — Djip007 (2019-05-01T22:15:43Z)

the issus is close... try reopen it... 

---
