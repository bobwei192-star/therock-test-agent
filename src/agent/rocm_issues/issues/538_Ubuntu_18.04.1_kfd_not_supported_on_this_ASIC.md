# Ubuntu 18.04.1: kfd not supported on this ASIC

> **Issue #538**
> **状态**: closed
> **创建时间**: 2018-09-16T13:19:34Z
> **更新时间**: 2018-09-18T10:01:11Z
> **关闭时间**: 2018-09-16T20:02:02Z
> **作者**: littlelailo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/538

## 描述

Hey,

I tried to get ROCm working, but while kfd shows up under /dev, rocminfo is still failing with:
```
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104
```
Operation system is Ubuntu 18.04.1 (clean installation):
```
Linux littlelailo-ubuntu 4.15.0-34-generic #37-Ubuntu SMP Mon Aug 27 15:21:48 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```
The card is a radeon r9 270X:
```
littlelailo@littlelailo-ubuntu:~$ sudo lshw -C display
  *-display                 
       Beschreibung: VGA compatible controller
       Produkt: Curacao XT / Trinidad XT [Radeon R7 370 / R9 270X/370X]
       Hersteller: Advanced Micro Devices, Inc. [AMD/ATI]
       Physische ID: 0
       Bus-Informationen: pci@0000:01:00.0
       Version: 00
       Breite: 64 bits
       Takt: 33MHz
       Fähigkeiten: pm pciexpress msi vga_controller bus_master cap_list rom
       Konfiguration: driver=amdgpu latency=0
       Ressourcen: irq:34 memory:e0000000-efffffff memory:f7d00000-f7d3ffff ioport:e000(Größe=256) memory:c0000-dffff
```

The whole dmesg output: https://ghostbin.com/paste/c6k2a
and the important parts:
```
littlelailo@littlelailo-ubuntu:~$ dmesg | grep kfd
[    1.171875] kfd kfd: Initialized module
[    1.172206] kfd2kgd: kfd not supported on this ASIC
littlelailo@littlelailo-ubuntu:~$ dmesg | grep amdgpu
[    1.168794] [drm] amdgpu kernel modesetting enabled.
[    1.168795] [drm] amdgpu version: 18.30.2.15
[    1.171979] fb: switching to amdgpudrmfb from VESA VGA
[    1.179287] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.179574] amdgpu 0000:01:00.0: VRAM: 2048M 0x000000F400000000 - 0x000000F47FFFFFFF (2048M used)
[    1.179575] amdgpu 0000:01:00.0: GTT: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
[    1.179789] [drm] amdgpu: 2048M of VRAM memory ready
[    1.179790] [drm] amdgpu: 23997M of GTT memory ready.
[    1.180429] amdgpu 0000:01:00.0: PCIE GART of 1024M enabled (table at 0x000000F4007E9000).
[    1.180523] [drm] amdgpu: dpm initialized
[    1.455181] fbcon: amdgpudrmfb (fb1) is primary device
[    1.684839] amdgpu 0000:01:00.0: fb1: amdgpudrmfb frame buffer device
[    1.684935] [drm] Initialized amdgpu 3.26.0 20150101 for 0000:01:00.0 on minor 1
```

I've also tried running it under root (also added root to the video group) and with HSA_ENABLE_SDMA=0, I'm in the video group, boot args are the default ones:
```
littlelailo@littlelailo-ubuntu:~$ groups
littlelailo adm cdrom sudo dip video plugdev lpadmin sambashare
littlelailo@littlelailo-ubuntu:~$ export  HSA_ENABLE_SDMA=0
littlelailo@littlelailo-ubuntu:~$ /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104
littlelailo@littlelailo-ubuntu:~$ sudo -s
root@littlelailo-ubuntu:~# unset HSA_ENABLE_SDMA
root@littlelailo-ubuntu:~# /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104
root@littlelailo-ubuntu:~# export  HSA_ENABLE_SDMA=0
root@littlelailo-ubuntu:~# /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104
root@littlelailo-ubuntu:~# groups
root video
root@littlelailo-ubuntu:~# ls /dev | grep kfd
kfd
root@littlelailo-ubuntu:~# cat /proc/cmdline 
BOOT_IMAGE=/boot/vmlinuz-4.15.0-34-generic root=UUID=cea500e5-9e1b-4659-bad9-d26d216b495f ro quiet splash vt.handoff=1
```
System was also updated & rebooted before I installed the driver and rebooted after installation

I also looked at other issues and in 522 it was suggested to run `sudo update-initramfs -u -k all` and then retrying but that  resulted in the same error.

As a side note: I've no problem with reinstalling Ubuntu or any other linux OS, if that's necessary.

Thank you in advanced, 
littlelailo


---

## 评论 (3 条)

### 评论 #1 — mdPlusPlus (2018-09-16T13:42:11Z)

I've just opened the same issue for a RX ~~560~~ 550: #539.  
Guess we started the post at around the same time, as your issue wasn't there when I started mine.

---

### 评论 #2 — ms178 (2018-09-16T16:57:31Z)

@littlelailo  Your GPU is not supported by ROCm as it is based on GFX6 (Southern Islands), see https://github.com/RadeonOpenCompute/ROCm#supported-gpus 

---

### 评论 #3 — jlgreathouse (2018-09-16T20:02:02Z)

@ms178 is correct. Your GPU is a "Southern Islands" GPU (PItcairn). This is [not in our list of supported GPUs](https://rocm.github.io/hardware.html). As such, ROCm will not work with your device.

---
