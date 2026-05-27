# Installation goes fine, but clinfo hangs forever and OpenCL doesn't work

> **Issue #482**
> **状态**: closed
> **创建时间**: 2018-07-30T17:30:38Z
> **更新时间**: 2019-12-26T13:49:32Z
> **关闭时间**: 2018-10-10T19:18:48Z
> **作者**: qolii
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/482

## 描述

I am filing this as an upstream version of https://github.com/nixos-rocm/nixos-rocm/issues/7

In short, I am using the 1.8.2 versions of everything here (with NixOS Linux – but in a configuration exactly matching that of another NixOS user, for whom it is working perfectly), and while the installation appears to succeed just fine, OpenCL is not working for me at runtime.

Note, this is a Radeon Vega FE card in an older (Ivy Bridge) system, with a Z77 Express chipset which, although is advertised to have PCIe Gen3 in the link below, I believe either has PCIe Gen2 in my configuration, or at least does not support atomics, given I got the ~`This system does not support atomics` error from ROCm in the 1.7.x series).

My system:
CPU: Intel Core-i5 3570
Motherboard: [Gigabyte Z77N-WIFI](https://www.gigabyte.com/Motherboard/GA-Z77N-WIFI-rev-10#sp)
GPU: Radeon Vega FE 16GB

My primary symptoms are:
1) if I run `clinfo`, it hangs forever. A truncated `strace` output is [here](https://github.com/nixos-rocm/nixos-rocm/files/2233563/cldebug_trunc.txt); it just repeats the last `sched_yield()` lines forever.

2) If I run XMR-stak. it sits forever at the line: `Compiling code and initializing GPUs. This will take a while...`. My CPU usage goes up to 100% (of one core), but it never progresses to actually mining anything.

Please let me know if there is anything I can try, to collect useful info, or if you there's a chance I have something configured wrong. As mentioned in the other thread, I have just replaced my PSU with an 850W Seasonic, which should have about 3x the power this system needs, and I get the same result... so I don't think power is the problem!


```
# lspci
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor DRAM Controller (rev 09)
00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port (rev 09)
00:02.0 Display controller: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor Graphics Controller (rev 09)
00:14.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller (rev 04)
00:16.0 Communication controller: Intel Corporation 7 Series/C216 Chipset Family MEI Controller #1 (rev 04)
00:1a.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #2 (rev 04)
00:1c.0 PCI bridge: Intel Corporation 7 Series/C216 Chipset Family PCI Express Root Port 1 (rev c4)
00:1c.4 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 5 (rev c4)
00:1c.5 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 6 (rev c4)
00:1c.6 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 7 (rev c4)
00:1d.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #1 (rev 04)
00:1f.0 ISA bridge: Intel Corporation Z77 Express Chipset LPC Controller (rev 04)
00:1f.2 SATA controller: Intel Corporation 7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode] (rev 04)
00:1f.3 SMBus: Intel Corporation 7 Series/C216 Chipset Family SMBus Controller (rev 04)
01:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470
02:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition]
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
05:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)
06:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)
07:00.0 Network controller: Intel Corporation Centrino Wireless-N 2230 (rev c4)
```


```
# rocminfo
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Core(TM) i5-3570 CPU @ 3.40GHz
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):3800                               
  BDFID:                   0                                  
  Compute Unit:            4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16322420KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16322420KB                         
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
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 26723                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1600                               
  BDFID:                   768                                
  Compute Unit:            64                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size per Dimension:
    x                        1024                               
    y                        1024                               
    z                        1024                               
  Waves Per CU:            40                                 
  Max Work-item Per CU:    2560                               
  Grid Max Size:           4294967295                         
  Grid Max Size per Dimension:
    x                        4294967295                         
    y                        4294967295                         
    z                        4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64KB                               
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
      Workgroup Max Size:      1024                               
      Workgroup Max Size per Dimension:
        x                        1024                               
        y                        1024                               
        z                        1024                               
      Grid Max Size:           4294967295                         
      Grid Max Size per Dimension:
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      FBarrier Max Size:       32                                 
*** Done ***             
```

---

## 评论 (18 条)

### 评论 #1 — jlgreathouse (2018-07-30T17:37:02Z)

What happens if you set the environment variable `HSA_ENABLE_SDMA=0`

For example:
```
export HSA_ENABLE_SDMA=0
clinfo
```


---

### 评论 #2 — gstoner (2018-07-30T18:13:05Z)

Do you have an icd

Get Outlook for iOS<https://aka.ms/o0ukef>

________________________________
From: qolii <notifications@github.com>
Sent: Monday, July 30, 2018 12:31 PM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: [RadeonOpenCompute/ROCm] Installation goes fine, but clinfo hangs forever and OpenCL doesn't work (#482)


I am filing this as an upstream version of nixos-rocm/nixos-rocm#7<https://github.com/nixos-rocm/nixos-rocm/issues/7>

In short, I am using the 1.8.2 versions of everything here (with NixOS Linux – but in a configuration exactly matching that of another NixOS user, for whom it is working perfectly), and while the installation appears to succeed just fine, OpenCL is not working for me at runtime.

Note, this is a Radeon Vega FE card in an older (Ivy Bridge) system, with a Z77 Express chipset which, although is advertised to have PCIe Gen3 in the link below, I believe either has PCIe Gen2 in my configuration, or at least does not support atomics, given I got the ~This system does not support atomics error from ROCm in the 1.7.x series).

My system:
CPU: Intel Core-i5 3570
Motherboard: Gigabyte Z77N-WIFI<https://www.gigabyte.com/Motherboard/GA-Z77N-WIFI-rev-10#sp>
GPU: Radeon Vega FE 16GB

My primary symptoms are:

  1.  if I run clinfo, it hangs forever. A truncated strace output is here<https://github.com/nixos-rocm/nixos-rocm/files/2233563/cldebug_trunc.txt>; it just repeats the last sched_yield() lines forever.

  2.  If I run XMR-stak. it sits forever at the line: Compiling code and initializing GPUs. This will take a while.... My CPU usage goes up to 100% (of one core), but it never progresses to actually mining anything.

Please let me know if there is anything I can try, to collect useful info, or if you there's a chance I have something configured wrong. As mentioned in the other thread, I have just replaced my PSU with an 850W Seasonic, which should have about 3x the power this system needs, and I get the same result... so I don't think power is the problem!

# lspci
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor DRAM Controller (rev 09)
00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port (rev 09)
00:02.0 Display controller: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor Graphics Controller (rev 09)
00:14.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller (rev 04)
00:16.0 Communication controller: Intel Corporation 7 Series/C216 Chipset Family MEI Controller #1 (rev 04)
00:1a.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #2 (rev 04)
00:1c.0 PCI bridge: Intel Corporation 7 Series/C216 Chipset Family PCI Express Root Port 1 (rev c4)
00:1c.4 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 5 (rev c4)
00:1c.5 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 6 (rev c4)
00:1c.6 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 7 (rev c4)
00:1d.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #1 (rev 04)
00:1f.0 ISA bridge: Intel Corporation Z77 Express Chipset LPC Controller (rev 04)
00:1f.2 SATA controller: Intel Corporation 7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode] (rev 04)
00:1f.3 SMBus: Intel Corporation 7 Series/C216 Chipset Family SMBus Controller (rev 04)
01:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470
02:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition]
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
05:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)
06:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)
07:00.0 Network controller: Intel Corporation Centrino Wireless-N 2230 (rev c4)


# rocminfo
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Core(TM) i5-3570 CPU @ 3.40GHz
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0
  Queue Min Size:          0
  Queue Max Size:          0
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768KB
  Chip ID:                 0
  Cacheline Size:          64
  Max Clock Frequency (MHz):3800
  BDFID:                   0
  Compute Unit:            4
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16322420KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16322420KB
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
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26723
  Cacheline Size:          64
  Max Clock Frequency (MHz):1600
  BDFID:                   768
  Compute Unit:            64
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size per Dimension:
    x                        1024
    y                        1024
    z                        1024
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size:           4294967295
  Grid Max Size per Dimension:
    x                        4294967295
    y                        4294967295
    z                        4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16760832KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
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
      Workgroup Max Size:      1024
      Workgroup Max Size per Dimension:
        x                        1024
        y                        1024
        z                        1024
      Grid Max Size:           4294967295
      Grid Max Size per Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      FBarrier Max Size:       32
*** Done ***


—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/482>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuVXo8XE6ywae9En9dYBqe23G9Qwvks5uL0LYgaJpZM4Vm1nQ>.


---

### 评论 #3 — qolii (2018-07-30T18:20:02Z)

@jlgreathouse, Hm, that doesn't seem to help. It still hangs forever. I can get another strace output with that in place if that's useful?

@gstoner, I do! It's at `/run/opengl-driver/etc/OpenCL/vendors/amdocl64.icd` (the exact path is unusual because it's NixOS, but it's legit), and we see at line 126 of the strace output:
```
openat(AT_FDCWD, "/run/opengl-driver/etc/OpenCL/vendors/amdocl64.icd", O_RDONLY) = 4
```
so it seems like it's being found, right?

Also, just to be clear:
```
# cat /run/opengl-driver/etc/OpenCL/vendors/amdocl64.icd
/nix/store/8lrqhf2nx6nyca4l0wi5inlrvahwap6r-rocm-opencl-runtime-1.8.2/lib/libamdocl64.so
```
so it's pointing somewhere, and:
```
# ls /nix/store/8lrqhf2nx6nyca4l0wi5inlrvahwap6r-rocm-opencl-runtime-1.8.2/lib/libamdocl64.so
/nix/store/8lrqhf2nx6nyca4l0wi5inlrvahwap6r-rocm-opencl-runtime-1.8.2/lib/libamdocl64.so
```
so that somewhere definitely exists.

---

### 评论 #4 — jlgreathouse (2018-07-30T21:00:05Z)

I know this is going to be kind of a pain for you, but is there any chance you could attempt installing ROCm on your system with Ubuntu 16.04.4 LTS, as per the directions in the README file in the [ROCm github](https://github.com/RadeonOpenCompute/ROCm).

This is not to say "don't try installing ROCm on NixOS". Rather, I think this would help us figure out if the problem is a hardware or a configuration problem. Right now, I'm unsure if your hardware is properly configured, and we may simultaneously be debugging cross-distribution configuration issues.

---

### 评论 #5 — qolii (2018-07-31T17:02:08Z)

> is there any chance you could attempt installing ROCm on your system with Ubuntu 16.04.4 LTS

Yeeeeeah, that sounds like the most appropriate thing to try. I just noticed there was a newer firmware for my motherboard, with the change note of "improves compatbility" and got all excited, but it doesn't fix the problem. So yes, installing via the most supported path sounds like the best option. It'll take me a few days to get to that, I expect. I'll keep you posted!

FWIW, I also got another `strace` with `HSA_ENABLE_SDMA=0` in place, but it looks the same to me. Certainly, the overall problem of endless `sched_yield` remains.

In the mean time, is there any low hanging fruit you might look at to debug a PCIe/atomics corner case like I think this system might be? I can run whatever.

---

### 评论 #6 — jlgreathouse (2018-07-31T17:11:25Z)

If you've tried with `HSA_ENABLE_SDMA=0` and it didn't improve, and if you've seen `rocminfo` properly work, then I suspect PCIe/atomics aren't the problem. My gut feeling is that this is something in the OpenCL runtime, perhaps because it's looking for files in the wrong location. However, I'd like to verify before digging too deeply into that, because the OpenCL runtime can be pretty convoluted. I'd like to verify that this isn't a low-hanging-fruit problem (like something wrong with your hardware) before going down that path.

Towards that end, there are two other requests:
1. Could you try running one of the non-OpenCL test applications that come with ROCm to see if they work? For instance, could I see the output of the following commands on your NixOS build?
```
$ cp -R /opt/rocm/hip/samples/0_Intro/square .
$ cd square
$ make
$ ./square.out
```

2. Could you write up a list of directions that show exactly how you're installing NixOS? I've never worked with this distribution before, so doing any kind of debugging on my end would be predicated on setting up such a system. I suspect that if I don't have a configuration very similar to yours, I could spend a long time just getting things working in such a way that I see your problem.

---

### 评论 #7 — blueberry (2018-07-31T18:54:41Z)

@jlgreathouse as for configuration, you'll find it relatively easy to replicate, since NixOS uses declarative configuration for everything. You'd need qolii's nix file(s) and simply run nixos update with it.

---

### 评论 #8 — qolii (2018-08-05T22:00:46Z)

Hi @jlgreathouse, I'm trying Ubuntu:

I got [this 16.04.5 server image](http://releases.ubuntu.com/xenial/ubuntu-16.04.5-server-amd64.iso), linked to from [this page](http://releases.ubuntu.com/xenial/) and installed. I then followed [the directions](https://github.com/RadeonOpenCompute/ROCm), running:
```
$ sudo apt update
$ sudo apt dist-upgrade
$ sudo apt install libnuma-dev
$ sudo reboot

$ wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
$ sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'

$ sudo apt update
$ sudo apt install rocm-dkms

$ sudo usermod -a -G video $LOGNAME
$ sudo reboot
```
Now, the directions say, after rebooting, to run `rocminfo` and `clinfo`, but I get:
```
$ rocminfo
rocminfo: command not found

$ clinfo
The program 'clinfo' is currently not installed. You can install it by typing:
sudo apt install clinfo
```
Installing `clinfo` like that works, but with `rocminfo` it's a little confusing:
```
$ sudo apt install rocminfo
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocminfo is already the newest version (1.0.0).
rocminfo set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```
Not sure what the deal is with that, it sounds like it knows of the package and that it is already installed. But just typing `rocminfo` does not work for sure. So, maybe a fix for the documentation here or so...

Anyway, the moment of truth!
```
$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP.internal (2574.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  2574.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         Device 6863
  Device Topology (AMD)                           PCI-E, 03:00.0
  Max compute units                               64
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1600MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              17163091968 (15.98GiB)
  Global free memory (AMD)                        16758784 (15.98GiB)
  Global memory channels (AMD)                    64
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           14588628172 (13.59GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26723
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        14588628172 (13.59GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 16:00:00 1969)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.8
  ICD loader Profile                              OpenCL 1.2
	NOTE:	your OpenCL library declares to support OpenCL 1.2,
		but it seems to support up to OpenCL 2.1 too.
```
So, like, yay... I guess? :/

Following your instructions above:
```
$ cp -R /opt/rocm/hip/samples/0_Intro/square .
$ cd square
$ make
$ ./square.out
info: running on device Device 6863
info: allocate host mem (  7.63 MB)
info: allocate device mem (  7.63 MB)
info: copy Host2Device
info: launch 'vector_square' kernel
info: copy Device2Host
info: check result
PASSED!
```

So, it seems like my hardware really is ok. Happy to try `rocm-bandwidth` here (can you advise me? I have literally zero Ubuntu knowledge), but I can also imagine there's no real need to at this point.

Blargh. This is kind've not the outcome I was hoping for. Debugging NixOS is hard to justify from your end, I'm sure. I am of course happy to write up instructions for you to reproduce my system if the idea is palatable to you, though?

Given that @acowley has an identical software configuration to me, but is using an RX550 instead of a Vega – and *his system works* – perhaps that narrows the scope a little bit...

---

### 评论 #9 — acowley (2018-08-06T01:24:42Z)

I have an RX580, but I'm not the only user of nixos-rocm (the README actually still says it has only been tested with a Vega Frontier Edition, so there's a second data point). If we really can't debug that hang in `rocm_bandwidth_test`, I don't know what else to do other than wait for ROCm-1.9 that should work with a mainline kernel. At least then we won't be using an AMD kernel with the nixpkgs software stack, so if the problem persists it might be possible to get debugging help from kernel experts in the broader NixOS community.

---

### 评论 #10 — qolii (2018-08-06T16:56:25Z)

> I have an RX580

Oops, sorry for the mistype.

> the README actually still says it has only been tested with a Vega Frontier Edition

Oh, so it does! Huh. Now I'm extra confused.

One thing I'll do is try to pare down my `configuration.nix` to the point that it might be something other people can rebuild to on their systems. It would be weird, because I don't think my config is that interesting, but maybe something specific to my configuration is causing the breakage.

> ...wait for ROCm-1.9...

Yeah, that might be the necessary thing.

---

### 评论 #11 — jlgreathouse (2018-08-06T17:09:21Z)

Hi @qolii ,

Thank you for running the tests under Ubuntu and verifying that this most likely is not a hardware configuration issue. For reference, `rocminfo` and `clinfo` should both be contained, by default, within the `/opt/rocm/` directory. For instance:
```
$ which rocminfo
/opt/rocm/bin/rocminfo
```
```
$ which clinfo
/opt/rocm/opencl/bin/x86_64/clinfo
```

I don't know why this wasn't automatically added to your PATH environment variable -- I thought we automatically did this, but I don't have a fresh system install to try at the moment.

That said, the fact that the `square` example worked implies, to me anyway, that your hardware is properly configured and does, in fact, support ROCm on supported platforms.

I suppose the next step would be to try to show what you're doing to configure NixOS. If others have NixOS working with a similar hardware setup, there may be something in your configuration.

---

### 评论 #12 — jlgreathouse (2018-09-14T22:44:14Z)

Hi @qolii 

We just release ROCm 1.9.0. This version of ROCm should work even with upstream kernels. Could you and the NixOS folks see if this does anything for you?

---

### 评论 #13 — qolii (2018-09-14T23:35:09Z)

Yay! I was waiting for this, to hopefully spare you the effort of setting up a new system from your end.

I will try this out ASAP and get back to you.

Thanks!

---

### 评论 #14 — jlgreathouse (2018-10-09T22:03:53Z)

Hi @qolii 

Any luck?

---

### 评论 #15 — qolii (2018-10-10T16:22:05Z)

Hi @jlgreathouse,

Sorry this took so long.

Eventually, I needed to move the card to another (new, AMD EPYC) machine, so I haven't been able to fully test ROCm 1.9 against that existing configuration. However, I did eventually get to try it on the new machine, and everything is working as it should! And with the same configuration, too. Given this, I think I'm happy to put my problems down to some vagary of that motherboard. What do you guys think?

---

### 评论 #16 — jlgreathouse (2018-10-10T16:24:21Z)

Sounds good to me. If things work out of the box otherwise with the ROCm-NixOS, and your GPUs work in the systems they're in now, I'm fine not continuing to chase after ghosts. :)

---

### 评论 #17 — qolii (2018-10-11T16:20:58Z)

I agree :)

Thanks so much for all your help! I really appreciate it, and especially for a niche distro.

---

### 评论 #18 — pqyptixa (2019-12-26T01:24:49Z)

Right now I'm testing rocm-dkms 2.10-14 on Ubuntu 18.04 (kernel 5.3.0-24-generic, hardware is Ryzen 5 3550H with Vega 8 + RX 560), and clinfo hangs every time I run it (as does rocminfo). There seems to be a couple of similar bugs here: https://bugs.freedesktop.org/show_bug.cgi?id=108879 https://bugs.freedesktop.org/show_bug.cgi?id=111877  Could be related?

**Update**: adding amdgpu.runpm=0 to the kernel command line helped.

---
