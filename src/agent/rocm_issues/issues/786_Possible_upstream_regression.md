# Possible upstream regression

> **Issue #786**
> **状态**: closed
> **创建时间**: 2019-05-04T14:19:56Z
> **更新时间**: 2019-05-14T11:15:05Z
> **关闭时间**: 2019-05-14T11:15:05Z
> **作者**: PhilipDeegan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/786

## 描述

Hey there folks,

I was using ROCM on kernel 5.0.7. Recently did a usual apt update/upgrade and now only "rocm-smi" appears to work.

This occurs on two machines with Debian Kernel 5+
One has dual vega fe, the other has liquid vega 64.

I would have thought I hadn't configured the kernel correctly when building, if it hadn't worked previously.

```
lshw -C video
  *-display
       description: VGA compatible controller
       product: Advanced Micro Devices, Inc. [AMD/ATI]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:03:00.0
       version: 00
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:82 memory:c0000000-cfffffff memory:d0000000-d01fffff ioport:e000(size=256) memory:fba00000-fba7ffff memory:c0000-dffff
  *-display
       description: VGA compatible controller
       product: Advanced Micro Devices, Inc. [AMD/ATI]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:0c:00.0
       version: 00
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:83 memory:a0000000-afffffff memory:b0000000-b01fffff ioport:d000(size=256) memory:fb800000-fb87ffff memory:fb880000-fb89ffff
```


```
/opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.3/rocminfo/rocminfo.cc. Call returned 4104
```

```
/opt/rocm/bin/rocm-smi 


========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK    MCLK    Fan   Perf  PwrCap  SCLK OD  MCLK OD  GPU%  
0    26.0c  3.0W    852Mhz  167Mhz  0.0%  auto  220.0W  0%       0%       0%    
1    21.0c  3.0W    852Mhz  167Mhz  0.0%  auto  220.0W  0%       0%       0%    
================================================================================
==============================End of ROCm SMI Log ==============================
```

```
dmesg | grep amdgpu
[   10.332554] [drm] amdgpu kernel modesetting enabled.
[   10.332700] fb0: switching to amdgpudrmfb from EFI VGA
[   10.336587] amdgpu 0000:03:00.0: No more image in the PCI ROM
[   10.336632] amdgpu 0000:03:00.0: VRAM: 16368M 0x000000F400000000 - 0x000000F7FEFFFFFF (16368M used)
[   10.336633] amdgpu 0000:03:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[   10.336634] amdgpu 0000:03:00.0: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
[   10.337672] [drm] amdgpu: 16368M of VRAM memory ready
[   10.337673] [drm] amdgpu: 16368M of GTT memory ready.
[   10.840798] amdgpu 0000:03:00.0: ring gfx uses VM inv eng 0 on hub 0
[   10.840798] amdgpu 0000:03:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[   10.840799] amdgpu 0000:03:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[   10.840799] amdgpu 0000:03:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[   10.840800] amdgpu 0000:03:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[   10.840801] amdgpu 0000:03:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[   10.840801] amdgpu 0000:03:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[   10.840802] amdgpu 0000:03:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[   10.840802] amdgpu 0000:03:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[   10.840803] amdgpu 0000:03:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[   10.840803] amdgpu 0000:03:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[   10.840804] amdgpu 0000:03:00.0: ring sdma1 uses VM inv eng 1 on hub 1
[   10.840804] amdgpu 0000:03:00.0: ring uvd_0 uses VM inv eng 4 on hub 1
[   10.840805] amdgpu 0000:03:00.0: ring uvd_enc_0.0 uses VM inv eng 5 on hub 1
[   10.840805] amdgpu 0000:03:00.0: ring uvd_enc_0.1 uses VM inv eng 6 on hub 1
[   10.840806] amdgpu 0000:03:00.0: ring vce0 uses VM inv eng 7 on hub 1
[   10.840806] amdgpu 0000:03:00.0: ring vce1 uses VM inv eng 8 on hub 1
[   10.840807] amdgpu 0000:03:00.0: ring vce2 uses VM inv eng 9 on hub 1
[   10.841561] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:03:00.0 on minor 0
[   10.841653] amdgpu 0000:0c:00.0: enabling device (0000 -> 0003)
[   11.249592] amdgpu 0000:0c:00.0: VRAM: 16368M 0x000000F400000000 - 0x000000F7FEFFFFFF (16368M used)
[   11.249593] amdgpu 0000:0c:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[   11.249594] amdgpu 0000:0c:00.0: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
[   11.249841] [drm] amdgpu: 16368M of VRAM memory ready
[   11.249842] [drm] amdgpu: 16368M of GTT memory ready.
[   11.713998] amdgpu 0000:0c:00.0: ring gfx uses VM inv eng 0 on hub 0
[   11.713998] amdgpu 0000:0c:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[   11.713999] amdgpu 0000:0c:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[   11.713999] amdgpu 0000:0c:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[   11.714000] amdgpu 0000:0c:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[   11.714000] amdgpu 0000:0c:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[   11.714001] amdgpu 0000:0c:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[   11.714001] amdgpu 0000:0c:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[   11.714002] amdgpu 0000:0c:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[   11.714002] amdgpu 0000:0c:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[   11.714003] amdgpu 0000:0c:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[   11.714003] amdgpu 0000:0c:00.0: ring sdma1 uses VM inv eng 1 on hub 1
[   11.714004] amdgpu 0000:0c:00.0: ring uvd_0 uses VM inv eng 4 on hub 1
[   11.714004] amdgpu 0000:0c:00.0: ring uvd_enc_0.0 uses VM inv eng 5 on hub 1
[   11.714005] amdgpu 0000:0c:00.0: ring uvd_enc_0.1 uses VM inv eng 6 on hub 1
[   11.714005] amdgpu 0000:0c:00.0: ring vce0 uses VM inv eng 7 on hub 1
[   11.714006] amdgpu 0000:0c:00.0: ring vce1 uses VM inv eng 8 on hub 1
[   11.714006] amdgpu 0000:0c:00.0: ring vce2 uses VM inv eng 9 on hub 1
[   11.714731] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:0c:00.0 on minor 1
[   11.907564] amdgpu 0000:03:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=io+mem
[   11.907565] amdgpu 0000:0c:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
```

```
dmesg | grep kfd
[   10.840466] kfd kfd: Allocated 3969056 bytes on gart
[   10.840599] kfd kfd: added device 1002:6863
[   11.713572] kfd kfd: Allocated 3969056 bytes on gart
[   11.713799] kfd kfd: added device 1002:6863
```

```
lsmod | grep amd
amdgpu               3969024  2
chash                  20480  1 amdgpu
gpu_sched              36864  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   114688  1 amdgpu
drm_kms_helper        204800  1 amdgpu
drm                   491520  7 gpu_sched,drm_kms_helper,amdgpu,ttm
```

---

## 评论 (10 条)

### 评论 #1 — PhilipDeegan (2019-05-06T12:34:51Z)

Ok, so it seems that the VEGA 64 machine works now (no idea why)

And the DUAL VEGA FE works with sudo only

---

### 评论 #2 — valeriob01 (2019-05-11T12:33:33Z)

> Ok, so it seems that the VEGA 64 machine works now (no idea why)
> 
> And the DUAL VEGA FE works with sudo only

That problem is not new. OpenCL programs run only under root account. It is like that from ROCm version 2.0


---

### 评论 #3 — seesturm (2019-05-11T16:00:58Z)

I'm using ROCm with vanilla kernel since 4.20. Currently on kernel 5.1. For me OpenCL programs run successfully non-root. At the moment using ROCm 2.4.

- What are the permissions of /dev/kfd and /dev/dri/* ?
- Is your user in the video group?
 

---

### 评论 #4 — valeriob01 (2019-05-12T07:38:10Z)

> I'm using ROCm with vanilla kernel since 4.20. Currently on kernel 5.1. For me OpenCL programs run successfully non-root. At the moment using ROCm 2.4.
> 
>     * What are the permissions of /dev/kfd and /dev/dri/* ?

I did not change any permission, not working outside root account, that means some permission is wrong *by default*


>     * Is your user in the video group?

Yes, in the video group already


---

### 评论 #5 — seesturm (2019-05-12T08:46:25Z)

@valeriob01 
> I did not change any permission, not working outside root account, that means some permission is wrong _by default_

Ok, you didn't change the permission. But that is not the point here. The _default_ setup is Ubuntu 18.04.2 with its kernel (I guess this is 4.18) and the rocm-dkms package installed. This should take care of the permissions. Don't know about your setup, but the issue was opened by @Dekken who isn't running on the default setup, but on kernel 5.0.7.

When you install a non-default kernel (like I did) rocm-dkms will fail (due to its dependency on rock-dkms) and therefore should be omitted. But when omitted, you have to take care of the permissions yourself. For the permissions rocm-dkms creates an udev rule file in **/etc/udev/rules.d/kfd.rules** with following content:
```KERNEL=="kfd", MODE="0666"```

But I didn't want to let users blindly edit config files without checking the actual situation. Because if the permissions are already correct and a different problem exists creating/creating random config files might make things even worse.


---

### 评论 #6 — valeriob01 (2019-05-12T09:01:20Z)

That file is present and contains exactly what you wrote.


---

### 评论 #7 — PhilipDeegan (2019-05-13T07:17:06Z)

Yes to video group

```
ls -l /dev/kfd /dev/dri/*
crw-rw---- 1 root video  226,   0 May 13 09:13 /dev/dri/card0
crw-rw---- 1 root video  226,   1 May 13 09:13 /dev/dri/card1
crw-rw---- 1 root render 226, 128 May 13 09:13 /dev/dri/renderD128
crw-rw---- 1 root render 226, 129 May 13 09:13 /dev/dri/renderD129
crw-rw---- 1 root video  243,   0 May 13 09:13 /dev/kfd

/dev/dri/by-path:
total 0
lrwxrwxrwx 1 root root  8 May 13 09:13 pci-0000:03:00.0-card -> ../card0
lrwxrwxrwx 1 root root 13 May 13 09:13 pci-0000:03:00.0-render -> ../renderD128
lrwxrwxrwx 1 root root  8 May 13 09:13 pci-0000:0c:00.0-card -> ../card1
lrwxrwxrwx 1 root root 13 May 13 09:13 pci-0000:0c:00.0-render -> ../renderD129
```



---

### 评论 #8 — PhilipDeegan (2019-05-13T07:50:56Z)

It would appear that to be able to run without root, one requires an active monitor and to be logged in to an active DM

this is very odd - and I find it quite needless



---

### 评论 #9 — seesturm (2019-05-13T20:08:34Z)

@Dekken: interesting, it appears that your dri/render devices are in the render group. Maybe it helps to add yourself also to the render group.

For me all nodes are in the video group:
```
$ ls -l /dev/dri
total 0
drwxr-xr-x  2 root root       120 Mai 13 20:55 by-path
crw-rw----+ 1 root video 226,   0 Mai 13 20:55 card0
crw-rw----+ 1 root video 226,   1 Mai 13 20:55 card1
crw-rw----+ 1 root video 226, 128 Mai 13 20:55 renderD128
crw-rw----+ 1 root video 226, 129 Mai 13 20:55 renderD129```

---

### 评论 #10 — PhilipDeegan (2019-05-14T11:15:03Z)

That seemed to do the trick!

---
