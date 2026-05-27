# retired... 

> **Issue #457**
> **状态**: closed
> **创建时间**: 2018-07-12T10:58:15Z
> **更新时间**: 2018-08-19T16:38:57Z
> **关闭时间**: 2018-08-19T16:38:57Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/457

## 描述

*(无描述)*

---

## 评论 (20 条)

### 评论 #1 — Johnreidsilver (2018-07-12T11:05:51Z)

Vega including APU Vega  (Raven Ridge) ? 

---

### 评论 #2 — avfedorov (2018-07-12T12:46:52Z)

4.19 but inside deb's is 4.18.0-041800rc4. 
is it ok?

---

### 评论 #3 — securitizones (2018-07-12T15:33:21Z)

Hi tekcomm
I will test on vega 64. 
but a couple of questions:
1. does the https://github.com/tekcomm/linux-image-4.19-wip-generic have the rocm 1.8.2 beta patch already in the deb file.
2. which order to install the deb files to make sure nothing goes wrong.

---

### 评论 #4 — rhlug (2018-07-14T20:02:29Z)

put it on a rig where i test shit, dont have ethernet there.   the wifi on my asrock didnt work out of the gate, so i didnt get too far.   going to build my own drm-next-4.19-wip with a copy of my working kernel .config first.

i probably just need to load a iwlwifi module, but didnt check if that was even in linux-modules.  did you modularize everything?

---

### 评论 #5 — avfedorov (2018-07-14T20:54:29Z)

Is this kernel compatible with rocm-dkms?
Or some patching is required?

---

### 评论 #6 — rhlug (2018-07-15T03:51:57Z)

Havent tested vega yet, but Pro Duo doesnt like latest drm-next-4.19-wip.   That card works fine with 4.17.0-rc2-180424-fkxamd.

Kernel: 4.18.0-rc3-drm-next-wip-4.19-20180714
GPU: Radeon Pro Duo (polaris)

```
[   57.056204] [drm:amdgpu_job_timedout [amdgpu]] *ERROR* ring sdma1 timeout, last signaled seq=331, last emitted seq=333
[   57.056209] [drm] GPU recovery disabled.
[   57.056332] [drm:amdgpu_job_timedout [amdgpu]] *ERROR* ring sdma0 timeout, last signaled seq=573, last emitted seq=574
[   57.056335] [drm] GPU recovery disabled.
```





---

### 评论 #7 — avfedorov (2018-07-16T16:14:04Z)

Build and install drm-next-4.19-wip kernel
Boot with VEGA56
```
# dmesg | egrep "(amd|drm|kfd)"
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.18.0-rc3+ root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb amdgpu.ppfeaturemask=0xffffffff spectre_v1=off selinux=0 security=off audit=0 nmi_watchdog=0 amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 spectre_v2=off nopti pti=off
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.18.0-rc3+ root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb amdgpu.ppfeaturemask=0xffffffff spectre_v1=off selinux=0 security=off audit=0 nmi_watchdog=0 amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 spectre_v2=off nopti pti=off
[    1.061496] [drm] Replacing VGA console driver
[    1.063959] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.063963] [drm] Driver supports precise vblank timestamp query.
[    1.064658] [drm] Finished loading DMC firmware i915/skl_dmc_ver1_27.bin (v1.27)
[    1.071195] [drm] Initialized i915 1.6.0 20180620 for 0000:00:02.0 on minor 0
[    1.100233] fbcon: inteldrmfb (fb0) is primary device
[    1.144731] i915 0000:00:02.0: fb0: inteldrmfb frame buffer device
[    3.562892] [drm] amdgpu kernel modesetting enabled.
[    3.650796] kfd kfd: Initialized module
[    3.651697] amdgpu 0000:03:00.0: enabling device (0000 -> 0003)
[    3.652479] [drm] initializing kernel modesetting (VEGA10 0x1002:0x687F 0x1002:0x6B76 0xC3).
[    3.653148] [drm] register mmio base: 0xDFC00000
[    3.653791] [drm] register mmio size: 524288
[    3.654453] [drm] add ip block number 0 <soc15_common>
[    3.655090] [drm] add ip block number 1 <gmc_v9_0>
[    3.655733] [drm] add ip block number 2 <vega10_ih>
[    3.656349] [drm] add ip block number 3 <psp>
[    3.656947] [drm] add ip block number 4 <powerplay>
[    3.657565] [drm] add ip block number 5 <dm>
[    3.658155] [drm] add ip block number 6 <gfx_v9_0>
[    3.658751] [drm] add ip block number 7 <sdma_v4_0>
[    3.659326] [drm] add ip block number 8 <uvd_v7_0>
[    3.660474] [drm] add ip block number 9 <vce_v4_0>
[    3.666124] [drm] UVD(0) is enabled in VM mode
[    3.666704] [drm] UVD(0) ENC is enabled in VM mode
[    3.667263] [drm] VCE enabled in VM mode
[    4.930800] [drm] GPU posting now...
[    5.030381] [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[    5.030974] amdgpu 0000:03:00.0: BAR 2: releasing [mem 0x2ff0000000-0x2ff01fffff 64bit pref]
[    5.031552] amdgpu 0000:03:00.0: BAR 0: releasing [mem 0x2fe0000000-0x2fefffffff 64bit pref]
[    5.035527] amdgpu 0000:03:00.0: BAR 0: assigned [mem 0x2000000000-0x21ffffffff 64bit pref]
[    5.036049] amdgpu 0000:03:00.0: BAR 2: assigned [mem 0x2200000000-0x22001fffff 64bit pref]
[    5.042479] amdgpu 0000:03:00.0: VRAM: 8176M 0x000000F400000000 - 0x000000F5FEFFFFFF (8176M used)
[    5.042968] amdgpu 0000:03:00.0: GART: 512M 0x000000F600000000 - 0x000000F61FFFFFFF
[    5.043459] [drm] Detected VRAM RAM=8176M, BAR=8192M
[    5.043959] [drm] RAM width 2048bits HBM
[    5.046035] [drm] amdgpu: 8176M of VRAM memory ready
[    5.046538] [drm] amdgpu: 2550M of GTT memory ready.
[    5.047070] [drm] GART: num cpu pages 131072, num gpu pages 131072
[    5.047653] [drm] PCIE GART of 512M enabled (table at 0x000000F400900000).
[    5.065578] [drm] use_doorbell being set to: [true]
[    5.066288] [drm] use_doorbell being set to: [true]
[    5.071481] [drm] Found UVD firmware Version: 1.87 Family ID: 17
[    5.073083] [drm] PSP loading UVD firmware
[    5.079429] [drm] Found VCE firmware Version: 53.45 Binary ID: 4
[    5.081041] [drm] PSP loading VCE firmware
[    5.408097] [drm] Display Core initialized with v3.1.55!
[    5.409059] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    5.409596] [drm] Driver supports precise vblank timestamp query.
[    5.433451] [drm] UVD and UVD ENC initialized successfully.
[    5.534544] [drm] VCE initialized successfully.
[    5.536010] kfd kfd: Allocated 3969056 bytes on gart
[    5.538745] kfd kfd: added device 1002:687f
[    5.539366] [drm] Cannot find any crtc or sizes
[    5.539976] amdgpu 0000:03:00.0: ring 0(gfx) uses VM inv eng 4 on hub 0
[    5.540504] amdgpu 0000:03:00.0: ring 1(comp_1.0.0) uses VM inv eng 5 on hub 0
[    5.541034] amdgpu 0000:03:00.0: ring 2(comp_1.1.0) uses VM inv eng 6 on hub 0
[    5.541557] amdgpu 0000:03:00.0: ring 3(comp_1.2.0) uses VM inv eng 7 on hub 0
[    5.542099] amdgpu 0000:03:00.0: ring 4(comp_1.3.0) uses VM inv eng 8 on hub 0
[    5.542610] amdgpu 0000:03:00.0: ring 5(comp_1.0.1) uses VM inv eng 9 on hub 0
[    5.543120] amdgpu 0000:03:00.0: ring 6(comp_1.1.1) uses VM inv eng 10 on hub 0
[    5.543617] amdgpu 0000:03:00.0: ring 7(comp_1.2.1) uses VM inv eng 11 on hub 0
[    5.544129] amdgpu 0000:03:00.0: ring 8(comp_1.3.1) uses VM inv eng 12 on hub 0
[    5.544616] amdgpu 0000:03:00.0: ring 9(kiq_2.1.0) uses VM inv eng 13 on hub 0
[    5.545107] amdgpu 0000:03:00.0: ring 10(sdma0) uses VM inv eng 4 on hub 1
[    5.545610] amdgpu 0000:03:00.0: ring 11(sdma1) uses VM inv eng 5 on hub 1
[    5.546090] amdgpu 0000:03:00.0: ring 12(uvd<0>) uses VM inv eng 6 on hub 1
[    5.546570] amdgpu 0000:03:00.0: ring 13(uvd_enc0<0>) uses VM inv eng 7 on hub 1
[    5.547076] amdgpu 0000:03:00.0: ring 14(uvd_enc1<0>) uses VM inv eng 8 on hub 1
[    5.547550] amdgpu 0000:03:00.0: ring 15(vce0) uses VM inv eng 9 on hub 1
[    5.548024] amdgpu 0000:03:00.0: ring 16(vce1) uses VM inv eng 10 on hub 1
[    5.548497] amdgpu 0000:03:00.0: ring 17(vce2) uses VM inv eng 11 on hub 1
[    5.549018] [drm] ECC is not present.
[    5.758931] [drm] Initialized amdgpu 3.26.0 20150101 for 0000:03:00.0 on minor 1
```

Extract and install all from rocm 1.8.2, except dkms.

No opencl found:
```
# /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted

# /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/root/git/rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

```

from strace ./clinfo:
```
open("/dev/kfd", O_RDWR|O_CLOEXEC)      = 5
[skip]
ioctl(5, _IOC(_IOC_READ|_IOC_WRITE, 0x4b, 0x19, 0x10), 0x7ffda3ad8330) = -1 EINVAL (Invalid argument)
ioctl(5, AMDKFD_IOC_GET_PROCESS_APERTURES, 0x7ffda3ad84b0) = 0
ioctl(5, _IOC(_IOC_WRITE, 0x4b, 0x21, 0x08), 0x7ffda3ad84b0) = -1 EINVAL (Invalid argument)
close(5)                                = 0
```


---

### 评论 #8 — rhlug (2018-07-16T21:17:45Z)

>That is great news. This is a bug that has crept in and out I already and a
few dozen other people have it open on the freedesktop. I created on the
advice of another dev a regression branch at the end of the 4.16 to use as
a stable its in my github. Can you please use that one.
Here is the latest patches from the 4.19-wip with the stable kernel

The 4.17.0-rc2-180424-fkxamd kernel does everything I need it to do right now.  I was just going to test the ppfeaturemask to see how much more convenient it would be as opposed to building out custom pp_table files.    But I'll just carry on with modified pp_table for the time being.   

Hopefully I'll find some time to test the vegas soon enough.

---

### 评论 #9 — rhlug (2018-07-16T21:21:47Z)

> lspci -n | grep 1002: | egrep -v ".1"| awk '{print "find /sys | grep ""$1"/rescan" -| tac -;"}' | sh - | sed s/^/echo\ 1\ >\ "&/g | sed s/$/"/g

You need to escape the .1 with \\.1  

Otherwise..
```
# lspci -n | grep 1002: | egrep -v ".1" | wc -l
0
# lspci -n | grep 1002: | egrep -v "\.1" | wc -l
6
```

---

### 评论 #10 — rhlug (2018-07-16T21:39:25Z)

ah, that makes sense.  can it not be simplified into

```
find /sys/class/drm/card*/device/rescan -exec echo 1 > {} \;
```

(assuming all cards are vega)

---

### 评论 #11 — avfedorov (2018-07-16T22:19:51Z)

tekcomm, my setup is on CentOS 7, not on beaver.
I try to install your lyra-xmr-support.tgz
Now:
```
# ./clinfo | egrep "Board|Num"
Number of platforms:				 1
Number of devices:				 1
  Board name:					 Radeon RX Vega
```
xmr-stak is start, but hashrate is zero and in dmesg:
```
[ 1147.176302] amdgpu 0000:03:00.0: [gfxhub] VMC page fault (src_id:0 ring:158 vmid:6 pasid:32768, for process xmr-stak pid 1571 thread xmr-stak pid 1573
)
[ 1147.176436] amdgpu 0000:03:00.0:   at page 0x00000003049e7000 from 27
[ 1147.176493] amdgpu 0000:03:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x0060113C
```

---

### 评论 #12 — KeironO (2018-07-17T20:37:05Z)

This is incredible, I'll have to give this a go tonigh!

---

### 评论 #13 — gstoner (2018-07-20T14:54:06Z)

@tekcomm    I thought you like to see this https://github.com/ROCmSoftwarePlatform/rocprofiler   Lower level profiler and trace for ROCm stack.  It will allow you to get a lot deeper into the GPU then CodeXL. 

---

### 评论 #14 — gstoner (2018-07-20T14:55:28Z)

We soon also have ROCm Tracer Callback/Activity Library for Performance tracing AMD GPU's that leverage this. 

---

### 评论 #15 — securitizones (2018-07-21T13:14:33Z)

When will rocm 1.9 be out

---

### 评论 #16 — gstoner (2018-07-22T15:12:12Z)

Also working the team to get the debugger out.  Trying hard to have the core of it in place by 1.9. 

On the question, I talk to new VP of Eng.  I am now the CTO. 

---

### 评论 #17 — triosphere (2018-07-25T16:25:46Z)

Can you provide any tips on installing your latest AMDGPU stuff on Debian 9?  Specifically, is there a particular order wip, headers, (ROCm, OpenCL) etc. should be installed?  Forgive me if the presumption that this stuff will work on Debian is incorrect.  I see .deb files, but I also think I understand you created these for Ubuntu.  Thanks in advance, Not-exactly-a-novice-but-definitely-not-a-career-programmer.  I am starting with a fresh Debian install because I polluted my system with so many OpenCL files my head is spinning.

---

### 评论 #18 — triosphere (2018-07-26T11:55:39Z)

For what it's worth, the linux-kernel-amdgpu-binaries install on the latest stable Stretch, and booted just fine (I wasn't sure just how interchangeable those files would be between Debian and Ubuntu).  No noticeable change in hardware recognition though (update-pciids produces the exact same Radeon Vega 64 card listing, pretty much as I expected as I don't think Debian ever had trouble recognizing the card).  I did notice that clinfo now shows 1 platform, but still no devices attached.  Before your kernel binaries, it was 0 platforms.  So, I'm back to suspecting it's a problem with opencl or a related dependency or library.  I really don't want to capitulate with Windows 10, but I'd like to get some return on my Vega investment with xmr-stak, which not-surprisingly still doesn't see my AMD GPU.  Let me know if you would like me to test anything further (GA-B250-FinTech mainboard, Pentium G4400T, 8 GB RAM, HDD + Gigabyte Radeon Vega 64s).  I'm currently testing the Vega on a riser, as this is my intended configuration.

---

### 评论 #19 — triosphere (2018-07-26T13:33:40Z)

Thanks Doc.  I did see the live Ubuntu system, but I'm trying to get Debian to work, or apply some of your updates/fixes to my own build.  That may be too much to ask at my level of experience, so I'll check out your complete build.  Not sure what you mean by "49 mins left", but I'll download now just in case.    ; )

---

### 评论 #20 — triosphere (2018-07-26T14:10:27Z)

Sorry Doc, one more Q.  I have Rippa V3 and v5, and I see that V2 can be downloaded "by request" and it was designed for mining.  May I get a V2 download link?

---
