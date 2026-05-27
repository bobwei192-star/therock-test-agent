# new rocm-smi reports an error when trying to find fan of QXL video device (libvirt-qemu/kvm)

> **Issue #282**
> **状态**: closed
> **创建时间**: 2017-12-21T23:05:11Z
> **更新时间**: 2018-06-03T15:28:18Z
> **关闭时间**: 2018-06-03T15:28:18Z
> **作者**: GiordanoBruno69
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/282

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Hi,

I have been using rocm for a while now inside a qemu/kvm VM using PCI-passthrough for the AMD GPUs.  There is also a QXL video device for the VM (GPU 0).

After a recent update, `rocm-smi` now has a messy error when it tries to get info about the QXL device fans on GPU 0.

`rocm-smi` version: `1.0.0-34-g23012d0`
kernel:  `Linux 4.11.0-kfd-compute-rocm-rel-1.6-180`
error:
```
root@ubuntu:/home/tux# rocm-smi 
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  5   47.0c   120.210W 1000Mhz  500Mhz   71.76%   auto      0%       
  3   44.0c   81.170W  1266Mhz  2088Mhz  100.0%   auto      0%       
  1   43.0c   76.33W   1185Mhz  2088Mhz  100.0%   manual    2%       
  4   42.0c   73.255W  1185Mhz  2088Mhz  100.0%   manual    2%       
  2   41.0c   81.253W  1266Mhz  2088Mhz  100.0%   manual    0%       
Traceback (most recent call last):
  File "/usr/bin/rocm-smi", line 1058, in <module>
    showAllConcise(deviceList)
  File "/usr/bin/rocm-smi", line 728, in showAllConcise
    fan = str(getFanSpeed(device))
  File "/usr/bin/rocm-smi", line 358, in getFanSpeed
    fanLevel = int(getSysfsValue(device, 'fan'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
root@ubuntu:/home/tux# 
```
it seems to normally detect no powerplay on `GPU 0` with the rest of the fields when invoking `roc-smi -a`, but has the same messy error with the fans:

```
root@ubuntu:/home/tux# rocm-smi -a
====================    ROCm System Management Interface    ====================
================================================================================
GPU[5] 		: GPU ID: 0x7300
GPU[3] 		: GPU ID: 0x67df
GPU[1] 		: GPU ID: 0x67df
GPU[4] 		: GPU ID: 0x67df
GPU[2] 		: GPU ID: 0x67df
GPU[0] 		: GPU ID: 0x0100
================================================================================
================================================================================
GPU[5] 		: Temperature: 53.0c
GPU[3] 		: Temperature: 48.0c
GPU[1] 		: Temperature: 48.0c
GPU[4] 		: Temperature: 47.0c
GPU[2] 		: Temperature: 46.0c
GPU[0] 		: Unable to display temperature
================================================================================
================================================================================
GPU[5] 		: GPU Clock Level: 7 (1000Mhz)
GPU[5] 		: GPU Memory Clock Level: 0 (500Mhz)
GPU[3] 		: GPU Clock Level: 4 (1266Mhz)
GPU[3] 		: GPU Memory Clock Level: 2 (2088Mhz)
GPU[1] 		: GPU Clock Level: 3 (1185Mhz)
GPU[1] 		: GPU Memory Clock Level: 2 (2088Mhz)
GPU[4] 		: GPU Clock Level: 3 (1185Mhz)
GPU[4] 		: GPU Memory Clock Level: 2 (2088Mhz)
GPU[2] 		: GPU Clock Level: 4 (1266Mhz)
GPU[2] 		: GPU Memory Clock Level: 2 (2088Mhz)
GPU[0] 		: PowerPlay not enabled - Cannot display clocks
================================================================================
================================================================================
GPU[5] 		: Fan Level: 183 (71.76)%
GPU[3] 		: Fan Level: 255 (100.0)%
GPU[1] 		: Fan Level: 255 (100.0)%
GPU[4] 		: Fan Level: 255 (100.0)%
GPU[2] 		: Fan Level: 255 (100.0)%
Traceback (most recent call last):
  File "/usr/bin/rocm-smi", line 1074, in <module>
    showCurrentFans(deviceList)
  File "/usr/bin/rocm-smi", line 563, in showCurrentFans
    fanspeed = getFanSpeed(device)
  File "/usr/bin/rocm-smi", line 358, in getFanSpeed
    fanLevel = int(getSysfsValue(device, 'fan'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
root@ubuntu:/home/tux# 
```

It does not seem to affect usability and performance so far.

---

## 评论 (7 条)

### 评论 #1 — gstoner (2017-12-21T23:10:40Z)

We pushing update right now can you double check. After donning update to the driver.

One thing KVM may not be passing the PPLIB lnfo vis SYSfs interface
Greg



---

### 评论 #2 — GiordanoBruno69 (2017-12-22T02:55:44Z)

@gstoner FYI that was after upgrading the whole `rocm` suite from the prior version hosted at the github/radeon repo

I have just done a fresh install of the rocm packages on another VM to test it (as per the official guide), and i get this error with rocm-smi, it seems the default installation is broken ...
```
root@ubuntu:/home/tux# /opt/rocm/bin/rocm-smi 
Traceback (most recent call last):
  File "/opt/rocm/bin/rocm-smi", line 8, in <module>
    import json
ImportError: No module named 'json'
root@ubuntu:/home/tux# 
```

also `rocminfo`:
```
root@ubuntu:/home/tux# /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104
```
for now, is there a way to install the old set of `rocm`packages, for stability of my setup?  (the rocm kfd-compute kernel, etc) ... this seems a big change from what I was running, and it is broken when doing a fresh install ...

I am afraid that when I reboot my other VM (the one with the upgraded rocm-smi, etc), that it may be broken ... 

---

### 评论 #3 — gstoner (2017-12-22T04:25:33Z)

repo.radeon.com is where you get the binary packages 

---

### 评论 #4 — GiordanoBruno69 (2017-12-22T05:04:00Z)

@gstoner

Any suggestions on how to fix the broken fresh installation?

(edit:  regarding the rollback, I just found the old archives, will see if they work for now: 
 http://repo.radeon.com/rocm/archive/apt_1.6.4.tar.bz2)

---

### 评论 #5 — GiordanoBruno69 (2017-12-22T07:13:29Z)

@gstoner I have the fresh installation more functional now 

The problem I think was that it was too fresh, I had it so minimal that some packages were missing that were not installed as an explicit dependency (python json module or something)

though, `roc-smi` is behaving the same with regards to the QXL video device of the qemu/kvm VM:
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
Traceback (most recent call last):
  File "/opt/rocm/bin/rocm-smi", line 1058, in <module>
    showAllConcise(deviceList)
  File "/opt/rocm/bin/rocm-smi", line 728, in showAllConcise
    fan = str(getFanSpeed(device))
  File "/opt/rocm/bin/rocm-smi", line 358, in getFanSpeed
    fanLevel = int(getSysfsValue(device, 'fan'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
```

You mentioned an update is being pushed, where can I grab it?

---

### 评论 #6 — gstoner (2017-12-22T14:44:05Z)


The  ROCm-SMI source code lives here for the release  https://github.com/RadeonOpenCompute/ROC-smi/tree/roc-1.7.x.  This still looks like we can not get the data we need via SYSFS in a virtualized environment.






---

### 评论 #7 — GiordanoBruno69 (2018-01-18T09:46:27Z)

@gstoner some more information that may be useful to you:

The **roc-smi** version that I am using which works cleaner is from ROCm 1.6 debian/ubuntu repository:

**guest roc-smi version:**  `1.0.0-25-gbdb99b4 amd64`
**guest kernel version:**  `Linux 4.11.0-kfd-compute-rocm-rel-1.6-180`

version of kernel and virtualisation packages of the host:

**host kernel version:** `Linux 4.13.0-26-generic`
**host qemu-kvm version:** `1:2.5+dfsg-5ubuntu10.16 amd64`
**host libvirt-bin / libvirt0 version:** `1.3.1-1ubuntu10.15 amd64`
**host ovmf version:** `0~20160408.ffea0a2c-2 all`

I use this in the **same environment** (libvirt qemu/kvm virtual machine with QXL video device as GPU 0, all AMD GPUs are via PCI-passthrough)

**lspci VGA output:**

```
# lspci | grep VGA
00:02.0 VGA compatible controller: Red Hat, Inc. QXL paravirtual graphic card (rev 04)
00:07.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
00:09.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
00:0b.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
00:0d.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
00:0f.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
00:11.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
00:13.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
```

**with this version of `rocm-smi`, i get this cleaner output (`PowerPlay not enabled`):**

```
# rocm-smi

====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  5   67df   53.0c    61.49W   1162Mhz  2000Mhz  100.0%   auto      0%       N/A      
  3   67df   61.0c    85.44W   1310Mhz  2075Mhz  100.0%   auto      0%       N/A      
  1   67df   59.0c    89.197W  1310Mhz  2075Mhz  100.0%   auto      0%       N/A      
  6   67df   57.0c    115.113W 1162Mhz  2000Mhz  100.0%   auto      0%       N/A      
  4   67df   59.0c    94.61W   1350Mhz  2000Mhz  100.0%   auto      0%       N/A      
  2   67df   63.0c    96.99W   1310Mhz  2075Mhz  100.0%   auto      0%       N/A      
GPU[0] 		: PowerPlay not enabled - Cannot get supported clocks
GPU[0] 		: PowerPlay not enabled - Cannot get supported clocks
  0   0100   N/A      N/A      N/A      N/A      None%              N/A      N/A      
  7   67df   68.0c    118.255W 1162Mhz  2000Mhz  100.0%   auto      0%       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================
```

**the full output of `-a` option:**

```
# rocm-smi -a

====================    ROCm System Management Interface    ====================
================================================================================
GPU[5] 		: GPU ID: 0x67df
GPU[3] 		: GPU ID: 0x67df
GPU[1] 		: GPU ID: 0x67df
GPU[6] 		: GPU ID: 0x67df
GPU[4] 		: GPU ID: 0x67df
GPU[2] 		: GPU ID: 0x67df
GPU[0] 		: GPU ID: 0x0100
GPU[7] 		: GPU ID: 0x67df
================================================================================
================================================================================
GPU[5] 		: Temperature: 57.0c
GPU[3] 		: Temperature: 61.0c
GPU[1] 		: Temperature: 58.0c
GPU[6] 		: Temperature: 59.0c
GPU[4] 		: Temperature: 61.0c
GPU[2] 		: Temperature: 62.0c
GPU[0] 		: Unable to display temperature
GPU[7] 		: Temperature: 71.0c
================================================================================
================================================================================
GPU[5] 		: GPU Clock Level: 3 (1162Mhz)
GPU[5] 		: GPU Memory Clock Level: 2 (2000Mhz)
GPU[3] 		: GPU Clock Level: 6 (1310Mhz)
GPU[3] 		: GPU Memory Clock Level: 2 (2075Mhz)
GPU[1] 		: GPU Clock Level: 3 (1154Mhz)
GPU[1] 		: GPU Memory Clock Level: 2 (2075Mhz)
GPU[6] 		: GPU Clock Level: 1 (900Mhz)
GPU[6] 		: GPU Memory Clock Level: 2 (2000Mhz)
GPU[4] 		: GPU Clock Level: 7 (1350Mhz)
GPU[4] 		: GPU Memory Clock Level: 2 (2000Mhz)
GPU[2] 		: GPU Clock Level: 6 (1310Mhz)
GPU[2] 		: GPU Memory Clock Level: 2 (2075Mhz)
GPU[0] 		: PowerPlay not enabled - Cannot display clocks
GPU[7] 		: GPU Clock Level: 3 (1162Mhz)
GPU[7] 		: GPU Memory Clock Level: 2 (2000Mhz)
================================================================================
================================================================================
GPU[5] 		: Fan Level: 255 (100.0)%
GPU[3] 		: Fan Level: 255 (100.0)%
GPU[1] 		: Fan Level: 255 (100.0)%
GPU[6] 		: Fan Level: 255 (100.0)%
GPU[4] 		: Fan Level: 255 (100.0)%
GPU[2] 		: Fan Level: 255 (100.0)%
GPU[0] 		: Unable to determine current fan speed
GPU[7] 		: Fan Level: 255 (100.0)%
================================================================================
================================================================================
GPU[5] 		: Current PowerPlay Level: auto
GPU[3] 		: Current PowerPlay Level: auto
GPU[1] 		: Current PowerPlay Level: auto
GPU[6] 		: Current PowerPlay Level: auto
GPU[4] 		: Current PowerPlay Level: auto
GPU[2] 		: Current PowerPlay Level: auto
GPU[0] 		: Cannot get Performance Level: Performance Level not supported
GPU[7] 		: Current PowerPlay Level: auto
================================================================================
================================================================================
GPU[5] 		: Current OverDrive value: 0%
GPU[3] 		: Current OverDrive value: 0%
GPU[1] 		: Current OverDrive value: 0%
GPU[6] 		: Current OverDrive value: 0%
GPU[4] 		: Current OverDrive value: 0%
GPU[2] 		: Current OverDrive value: 0%
GPU[0] 		: Cannot get OverDrive value: OverDrive not supported
GPU[7] 		: Current OverDrive value: 0%
================================================================================
================================================================================
GPU[5] 		: Minimum SCLK: 900MHz
GPU[5] 		: Minimum MCLK: 0MHz
GPU[5] 		: Activity threshold: 50%
GPU[5] 		: Hysteresis Up: 0ms
GPU[5] 		: Hysteresis Down: 5ms
GPU[3] 		: Minimum SCLK: 1266MHz
GPU[3] 		: Minimum MCLK: 0MHz
GPU[3] 		: Activity threshold: 50%
GPU[3] 		: Hysteresis Up: 0ms
GPU[3] 		: Hysteresis Down: 5ms
GPU[1] 		: Minimum SCLK: 1266MHz
GPU[1] 		: Minimum MCLK: 0MHz
GPU[1] 		: Activity threshold: 50%
GPU[1] 		: Hysteresis Up: 0ms
GPU[1] 		: Hysteresis Down: 5ms
GPU[6] 		: Minimum SCLK: 900MHz
GPU[6] 		: Minimum MCLK: 0MHz
GPU[6] 		: Activity threshold: 50%
GPU[6] 		: Hysteresis Up: 0ms
GPU[6] 		: Hysteresis Down: 5ms
GPU[4] 		: Minimum SCLK: 1310MHz
GPU[4] 		: Minimum MCLK: 0MHz
GPU[4] 		: Activity threshold: 50%
GPU[4] 		: Hysteresis Up: 0ms
GPU[4] 		: Hysteresis Down: 5ms
GPU[2] 		: Minimum SCLK: 1266MHz
GPU[2] 		: Minimum MCLK: 0MHz
GPU[2] 		: Activity threshold: 50%
GPU[2] 		: Hysteresis Up: 0ms
GPU[2] 		: Hysteresis Down: 5ms
GPU[0] 		: PowerPlay not enabled - Compute Power Profile not supported
GPU[7] 		: Minimum SCLK: 900MHz
GPU[7] 		: Minimum MCLK: 0MHz
GPU[7] 		: Activity threshold: 50%
GPU[7] 		: Hysteresis Up: 0ms
GPU[7] 		: Hysteresis Down: 5ms
================================================================================
================================================================================
GPU[5] 		: Average GPU Power: 	115.251 W
GPU[3] 		: Average GPU Power: 	90.62 W
GPU[1] 		: Average GPU Power: 	89.197 W
GPU[6] 		: Average GPU Power: 	86.75 W
GPU[4] 		: Average GPU Power: 	94.248 W
GPU[2] 		: Average GPU Power: 	96.15 W
GPU[0] 		: Cannot get GPU power Consumption: Average GPU Power not supported
GPU[7] 		: Average GPU Power: 	120.7 W
================================================================================
================================================================================
GPU[5] 		: Supported GPU clock frequencies on GPU5
GPU[5] 		: 0: 300Mhz 
GPU[5] 		: 1: 600Mhz 
GPU[5] 		: 2: 900Mhz 
GPU[5] 		: 3: 1162Mhz *
GPU[5] 		: 
GPU[5] 		: Supported GPU Memory clock frequencies on GPU5
GPU[5] 		: 0: 300Mhz 
GPU[5] 		: 1: 1000Mhz 
GPU[5] 		: 2: 2000Mhz *
GPU[5] 		: 
GPU[3] 		: Supported GPU clock frequencies on GPU3
GPU[3] 		: 0: 300Mhz 
GPU[3] 		: 1: 600Mhz 
GPU[3] 		: 2: 900Mhz 
GPU[3] 		: 3: 1154Mhz 
GPU[3] 		: 4: 1224Mhz 
GPU[3] 		: 5: 1266Mhz 
GPU[3] 		: 6: 1310Mhz *
GPU[3] 		: 
GPU[3] 		: Supported GPU Memory clock frequencies on GPU3
GPU[3] 		: 0: 300Mhz 
GPU[3] 		: 1: 1000Mhz 
GPU[3] 		: 2: 2075Mhz *
GPU[3] 		: 
GPU[1] 		: Supported GPU clock frequencies on GPU1
GPU[1] 		: 0: 300Mhz 
GPU[1] 		: 1: 600Mhz 
GPU[1] 		: 2: 900Mhz 
GPU[1] 		: 3: 1154Mhz 
GPU[1] 		: 4: 1224Mhz 
GPU[1] 		: 5: 1266Mhz 
GPU[1] 		: 6: 1310Mhz *
GPU[1] 		: 
GPU[1] 		: Supported GPU Memory clock frequencies on GPU1
GPU[1] 		: 0: 300Mhz 
GPU[1] 		: 1: 1000Mhz 
GPU[1] 		: 2: 2075Mhz *
GPU[1] 		: 
GPU[6] 		: Supported GPU clock frequencies on GPU6
GPU[6] 		: 0: 300Mhz 
GPU[6] 		: 1: 600Mhz 
GPU[6] 		: 2: 900Mhz *
GPU[6] 		: 3: 1162Mhz 
GPU[6] 		: 
GPU[6] 		: Supported GPU Memory clock frequencies on GPU6
GPU[6] 		: 0: 300Mhz 
GPU[6] 		: 1: 1000Mhz 
GPU[6] 		: 2: 2000Mhz *
GPU[6] 		: 
GPU[4] 		: Supported GPU clock frequencies on GPU4
GPU[4] 		: 0: 300Mhz 
GPU[4] 		: 1: 600Mhz 
GPU[4] 		: 2: 900Mhz 
GPU[4] 		: 3: 1154Mhz 
GPU[4] 		: 4: 1224Mhz 
GPU[4] 		: 5: 1266Mhz 
GPU[4] 		: 6: 1310Mhz 
GPU[4] 		: 7: 1350Mhz *
GPU[4] 		: 
GPU[4] 		: Supported GPU Memory clock frequencies on GPU4
GPU[4] 		: 0: 300Mhz 
GPU[4] 		: 1: 1000Mhz 
GPU[4] 		: 2: 2000Mhz *
GPU[4] 		: 
GPU[2] 		: Supported GPU clock frequencies on GPU2
GPU[2] 		: 0: 300Mhz 
GPU[2] 		: 1: 600Mhz 
GPU[2] 		: 2: 900Mhz 
GPU[2] 		: 3: 1154Mhz 
GPU[2] 		: 4: 1224Mhz 
GPU[2] 		: 5: 1266Mhz 
GPU[2] 		: 6: 1310Mhz *
GPU[2] 		: 
GPU[2] 		: Supported GPU Memory clock frequencies on GPU2
GPU[2] 		: 0: 300Mhz 
GPU[2] 		: 1: 1000Mhz 
GPU[2] 		: 2: 2075Mhz *
GPU[2] 		: 
GPU[0] 		: PowerPlay not enabled - Cannot display clocks
GPU[7] 		: Supported GPU clock frequencies on GPU7
GPU[7] 		: 0: 300Mhz 
GPU[7] 		: 1: 600Mhz 
GPU[7] 		: 2: 900Mhz 
GPU[7] 		: 3: 1162Mhz *
GPU[7] 		: 
GPU[7] 		: Supported GPU Memory clock frequencies on GPU7
GPU[7] 		: 0: 300Mhz 
GPU[7] 		: 1: 1000Mhz 
GPU[7] 		: 2: 2000Mhz *
GPU[7] 		: 
================================================================================
====================           End of ROCm SMI Log          ====================
```

As you can see, with this version it cleanly reports `GPU[0] 		: Unable to determine current fan speed` instead of throwing the error which the more recent version gives.

I will continue to use 1.6 for stability but let me know if you want me to test any updates on the 1.7+ versions.

cheers

---
