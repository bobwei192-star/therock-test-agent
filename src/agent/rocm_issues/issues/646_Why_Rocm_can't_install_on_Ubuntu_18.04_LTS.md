# Why Rocm can't install on Ubuntu 18.04 LTS

> **Issue #646**
> **状态**: closed
> **创建时间**: 2018-12-24T07:20:52Z
> **更新时间**: 2019-01-15T19:05:10Z
> **关闭时间**: 2019-01-15T19:04:55Z
> **作者**: nano1900
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/646

## 描述

After i installed ROCm on my computer.after i reboot the system the desktop do not show up.
kernel 
$ uname -a
Linux nano-System-Product-Name 4.15.0-29-generic #31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux


$ lspci -tv
-[0000:00]-+-00.0  Intel Corporation Skylake Host Bridge/DRAM Registers
           +-01.0-[01]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Hawaii PRO [Radeon R9 290/390]
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Hawaii HDMI Audio [Radeon R9 290/290X / 390/390X]
           +-01.1-[02]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Tahiti XT [Radeon HD 7970/8970 OEM / R9 280X]
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Tahiti HDMI Audio [Radeon HD 7870 XT / 7950/7970]
           +-02.0  Intel Corporation HD Graphics 530
           +-14.0  Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller
           +-16.0  Intel Corporation Sunrise Point-H CSME HECI #1
           +-17.0  Intel Corporation Sunrise Point-H SATA controller [AHCI mode]
           +-1b.0-[03]--
           +-1c.0-[04]----00.0  ASMedia Technology Inc. ASM1142 USB 3.1 Host Controller
           +-1c.2-[05-06]----00.0-[06]--
           +-1d.0-[07]--
           +-1f.0  Intel Corporation Sunrise Point-H LPC Controller
           +-1f.2  Intel Corporation Sunrise Point-H PMC
           +-1f.3  Intel Corporation Sunrise Point-H HD Audio
           +-1f.4  Intel Corporation Sunrise Point-H SMBus
           \-1f.6  Intel Corporation Ethernet Connection (2) I219-V

$ sudo lshw -numeric -class video

  *-display UNCLAIMED       
       description: VGA compatible controller
       product: Hawaii PRO [Radeon R9 290/390] [1002:67B1]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI] [1002]
       physical id: 0
       bus info: pci@0000:01:00.0
       version: 00
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list
       configuration: latency=0
       resources: memory:a0000000-afffffff memory:b0000000-b07fffff ioport:e000(size=256) memory:df200000-df23ffff memory:c0000-dffff
  *-display UNCLAIMED
       description: VGA compatible controller
       product: Tahiti XT [Radeon HD 7970/8970 OEM / R9 280X] [1002:6798]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI] [1002]
       physical id: 0
       bus info: pci@0000:02:00.0
       version: 00
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller cap_list
       configuration: latency=0
       resources: memory:c0000000-cfffffff memory:df100000-df13ffff ioport:d000(size=256) memory:df140000-df15ffff
  *-display UNCLAIMED
       description: Display controller
       product: HD Graphics 530 [8086:1912]
       vendor: Intel Corporation [8086]
       physical id: 2
       bus info: pci@0000:00:02.0
       version: 06
       width: 64 bits
       clock: 33MHz
       capabilities: pciexpress msi pm bus_master cap_list
       configuration: latency=0
       resources: memory:de000000-deffffff memory:90000000-9fffffff ioport:f000(size=64)

CPU  ntel 6700k
GPU1  R9 290
GPU2  R9 280x

The Rocm installing steps  just the same as here[https://github.com/RadeonOpenCompute/ROCm](url)



---

## 评论 (13 条)

### 评论 #1 — nano1900 (2018-12-24T12:21:36Z)

now after i remove the R9 280x ,and reinstall the Rocm .at this time the desktop show up.but the Rocm still not working 

and now i just updated the Kernel to 4.15.0-43-generic

$ /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104

$ /opt/rocm/opencl/bin/x86_64/clinfo 
ERROR: clGetPlatformIDs(-1001)


Is that the GPU drivers cause this problm?

---

### 评论 #2 — JMadgwick (2018-12-24T15:26:06Z)

I think this is related to https://github.com/RadeonOpenCompute/ROCm/issues/640#issuecomment-449402749. I had the same problem the R9 290. It appears to be related to some changes made to firmware locations in the kernel. Might want to check dmesg and see if you have the same firmware problem as that issue. Upgrading to 4.19 might help but I didn't try that. There doesn't seem to be any solution to this yet, hopefully we will know more in the new year.

---

### 评论 #3 — nano1900 (2018-12-25T01:17:56Z)

@JMadgwick  
Thank you I will check that out
if i made any progress ,i will let you know


---

### 评论 #4 — nano1900 (2018-12-25T03:01:04Z)

$ dmesg | grep amdgpu


[    1.314396] [drm] amdgpu kernel modesetting enabled.
[    1.314396] [drm] amdgpu version: 19.10.0.418
[    1.315467] fb: switching to amdgpudrmfb from VESA VGA
[    1.315790] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.315838] amdgpu 0000:01:00.0: Direct firmware load for amdgpu/hawaii_mc.bin failed with error -2
[    1.315838] cik_mc: Failed to load firmware "amdgpu/hawaii_mc.bin"
[    1.315871] [drm:gmc_v7_0_sw_init [amdgpu]] *ERROR* Failed to load mc firmware!
[    1.315894] [drm:amdgpu_device_init [amdgpu]] *ERROR* sw_init of IP block <gmc_v7_0> failed -2
[    1.315895] amdgpu 0000:01:00.0: amdgpu_device_ip_init failed
[    1.315896] amdgpu 0000:01:00.0: Fatal error during GPU init
[    1.315897] [drm] amdgpu: finishing device.
[    1.316041] amdgpu: probe of 0000:01:00.0 failed with error -2


---

### 评论 #5 — nano1900 (2018-12-25T04:16:15Z)

now updated kernel to 4.19.0
and reinstall the ROCm 

$ uname -a
Linux nano-System-Product-Name 4.19.0-041900-generic #201810221809 SMP Mon Oct 22 22:11:45 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

dmesg | grep amdgpu
[    1.644371] [drm] amdgpu kernel modesetting enabled.
[    1.647589] fb: switching to amdgpudrmfb from VESA VGA
[    1.647760] amdgpu 0000:01:00.0: CIK support provided by radeon.
[    1.647761] amdgpu 0000:01:00.0: Use radeon.cik_support=0 amdgpu.cik_support=1 to override.

$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104

$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)

still not working

---

### 评论 #6 — nano1900 (2018-12-25T05:07:12Z)

try again reinstall the ubuntu 18.4 LTS and update the kernel to 4.19.11

$ sudo dpkg -i *.deb

(正在读取数据库 ... 系统当前共安装有 139059 个文件和目录。)
正准备解包 linux-headers-4.19.11-041911_4.19.11-041911.201812191931_all.deb  ...
正在解包 linux-headers-4.19.11-041911 (4.19.11-041911.201812191931) ...
正准备解包 linux-headers-4.19.11-041911-generic_4.19.11-041911.201812191931_amd64.deb  ...
正在将 linux-headers-4.19.11-041911-generic (4.19.11-041911.201812191931) 解包到 (4.19.11-041911.201812191931) 上 ...
正准备解包 linux-image-unsigned-4.19.11-041911-generic_4.19.11-041911.201812191931_amd64.deb  ...
正在将 linux-image-unsigned-4.19.11-041911-generic (4.19.11-041911.201812191931) 解包到 (4.19.11-041911.201812191931) 上 ...
正准备解包 linux-modules-4.19.11-041911-generic_4.19.11-041911.201812191931_amd64.deb  ...
正在将 linux-modules-4.19.11-041911-generic (4.19.11-041911.201812191931) 解包到 (4.19.11-041911.201812191931) 上 ...
正在设置 linux-headers-4.19.11-041911 (4.19.11-041911.201812191931) ...
正在设置 linux-headers-4.19.11-041911-generic (4.19.11-041911.201812191931) ...
正在设置 linux-modules-4.19.11-041911-generic (4.19.11-041911.201812191931) ...
正在设置 linux-image-unsigned-4.19.11-041911-generic (4.19.11-041911.201812191931) ...
I: /vmlinuz.old is now a symlink to boot/vmlinuz-4.19.11-041911-generic
I: /initrd.img.old is now a symlink to boot/initrd.img-4.19.11-041911-generic
正在处理用于 linux-image-unsigned-4.19.11-041911-generic (4.19.11-041911.201812191931) 的触发器 ...
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-4.19.11-041911-generic
W: Possible missing firmware /lib/firmware/amdgpu/vega12_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/si58_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/banks_k_2_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/polaris12_k_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/polaris10_k_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/polaris11_k_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_asd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_sos.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_asd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sos.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega20_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/polaris12_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/polaris11_k2_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/polaris10_k2_smc.bin for module amdgpu
/etc/kernel/postinst.d/zz-update-grub:
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.19.11-041911-generic
Found initrd image: /boot/initrd.img-4.19.11-041911-generic
Found linux image: /boot/vmlinuz-4.15.0-29-generic
Found initrd image: /boot/initrd.img-4.15.0-29-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
done






---

### 评论 #7 — nano1900 (2018-12-25T06:23:08Z)


kernel 4.19.11
installed ROCm and reboot


$ dmesg | grep amdgpu
[    2.586188] [drm] amdgpu kernel modesetting enabled.

 /opt/rocm/opencl/bin/x86_64/clinfo 
ERROR: clGetPlatformIDs(-1001)

/opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104

---

### 评论 #8 — JMadgwick (2018-12-25T09:38:00Z)

You have a long list of missing firmware. This problem is mentioned in https://github.com/RadeonOpenCompute/ROCm/issues/640#issuecomment-449118988. Without the hawaii firmware rocm nor amdgpu will work. The firmware location changed in 4.19 and this causes it to be missing. You could try downloading the [latest firmware from here](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/) and placing it in the /lib/firmware/amdgpu folder. I don't know if this will help. This was attempted in the other issue and progressed the issue slightly.
Might make things easier to close this as duplicate, it seems to be the same as #640 

---

### 评论 #9 — nano1900 (2018-12-25T10:15:00Z)

I did that too

sudo cp /lib/firmware/radeon/hawaii_* /lib/firmware/amdgpu/
sudo modprobe -r amdgpu
sudo modprobe amdgpu

---

### 评论 #10 — nano1900 (2018-12-25T10:24:45Z)

but i not sure the the hawaii drivers in the radeon folder do any help

---

### 评论 #11 — nano1900 (2018-12-26T00:18:28Z)

@JMadgwick 
now after i replace firmware then reinstall the kernel (4.15.0-43-generic) and Rocm
it seems working


$ /opt/rocm/bin/rocminfo
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
  Name:                    Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz
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
  Max Clock Frequency (MHz):4200                               
  BDFID:                   0                                  
  Compute Unit:            8                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16338776KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16338776KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx701                             
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
  Chip ID:                 26545                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1000                               
  BDFID:                   256                                
  Compute Unit:            40                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  16778240                           
    Dim[2]:                  0                                  
  Grid Max Size:           4294967295                         
  Waves Per CU:            40                                 
  Max Work-item Per CU:    2560                               
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                         
    Dim[1]:                  4294967295                         
    Dim[2]:                  4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    4194304KB                          
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
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    4194304KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
      Workgroup Max Dimension: 
        Dim[0]:                  67109888                           
        Dim[1]:                  1024                               
        Dim[2]:                  16777217                           
      Workgroup Max Size:      1024                               
      Grid Max Dimension:      
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      Grid Max Size:           4294967295                         
      FBarrier Max Size:       32                                 
*** Done *** 



---

### 评论 #12 — nano1900 (2018-12-26T00:20:09Z)

but the opencl still  not working


$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)

------------------------------------------------------------------------------------------------------------

$ dmesg | grep amdgpu


[    1.340479] [drm] amdgpu kernel modesetting enabled.
[    1.340480] [drm] amdgpu version: 19.10.0.418
[    1.341644] fb: switching to amdgpudrmfb from VESA VGA
[    1.341938] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.342003] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    1.342003] amdgpu 0000:01:00.0: GART: 1024M 0x000000FF00000000 - 0x000000FF3FFFFFFF
[    1.342054] [drm] amdgpu: 4096M of VRAM memory ready
[    1.342054] [drm] amdgpu: 15955M of GTT memory ready.
[    1.566115] fbcon: amdgpudrmfb (fb0) is primary device
[    1.566155] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    1.602006] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:01:00.0 on minor 0





---

### 评论 #13 — jlgreathouse (2019-01-15T19:04:55Z)

Hi @nano1900 

Please see [this post](https://github.com/RadeonOpenCompute/ROCm/issues/640#issuecomment-454264790) for steps on how you can get ROCm 2.0 working with Hawaii. I'm going to close this issue since it is the same underlying problem(s) as describe in the linked post.

---
