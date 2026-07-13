# Installing ROCM on Ubuntu - hsa api call failure

- **Issue #:** 1064
- **State:** closed
- **Created:** 2020-03-28T16:18:24Z
- **Updated:** 2021-04-05T10:12:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/1064

So I am trying to install ROCm on Ubuntu 18.04.3 which is supposedly supported. I have tried reinstalling ubuntu twice and spent quite a few hours trying to get it working. I sticked completely to the official instructions on this github page. One thing that might be relevant is that I ticked `Install third-party software for graphics and Wi-Fi hardware and additional media formats`. When I run `rocminfo` I get the following hsa api call failure:

<pre><code>bauermax@backbone:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
bauermax is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-3.1/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.</code></pre>

Now I could find this issue online and a lot of people seem to have it also, but I could not find any solution.

When I run `clinfo` everything seems to be working exept it says `ERROR: clGetDeviceIDs(-1)` at the end:

<pre><code>bauermax@backbone:~$ /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3084.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
</code></pre>

My current kernel is `5.3.0-42-generic` and in the instruction they say 5.3 is supported, so I think the kernel is right:
<pre><code>bauermax@backbone:~$ uname -r
5.3.0-42-generic
</code></pre>

I downloaded and installed `Ubuntu 18.04.3` however having followed the official instructions my version is now `Ubuntu 18.04.4 LTS` . I suppose that is because of the `sudo apt update` and `sudo apt dist-upgrade` command which however is in the official instructions. In the supported operating systems section it says that only `18.04.3` is supported, so I am not sure if this is a problem:

<pre><code>bauermax@backbone:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.4 LTS
Release:        18.04
Codename:       bionic
</code></pre>

`lshw` shows that my GPU is using the `amdgpu` driver which I think is the open source one:
<pre><code>bauermax@backbone:~$ sudo lshw -c video
[sudo] password for bauermax: 
  *-display                 
       description: VGA compatible controller
       product: Ellesmere [Radeon RX 470/480/570/570X/580/580X]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:01:00.0
       version: e7
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:32 memory:e0000000-efffffff memory:f0000000-f01fffff ioport:e000(size=256) memory:f7e00000-f7e3ffff memory:c0000-dffff
</code></pre>

My specs:
Motherboard: Gigabyte Z77-DS3H
CPU: i7 3770k
GPU: Sapphire RX580 Pulse 4GB

<pre><code>bauermax@backbone:~$ sudo lshw -short
H/W path       Device      Class          Description
=====================================================
                           system         To be filled by O.E.M. (To be filled by O.E.M.)
/0                         bus            Z77-DS3H
/0/0                       memory         64KiB BIOS
/0/4                       memory         128KiB L1 cache
/0/5                       memory         1MiB L2 cache
/0/6                       memory         8MiB L3 cache
/0/7                       memory         32GiB System Memory
/0/7/0                     memory         8GiB DIMM DDR3 Synchronous 1600 MHz (0.6 ns)
/0/7/1                     memory         8GiB DIMM DDR3 Synchronous 1600 MHz (0.6 ns)
/0/7/2                     memory         8GiB DIMM DDR3 Synchronous 1600 MHz (0.6 ns)
/0/7/3                     memory         8GiB DIMM DDR3 Synchronous 1600 MHz (0.6 ns)
/0/43                      processor      Intel(R) Core(TM) i7-3770K CPU @ 3.50GHz
/0/100                     bridge         Xeon E3-1200 v2/3rd Gen Core processor DRAM Controller
/0/100/1                   bridge         Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port
/0/100/1/0                 display        Ellesmere [Radeon RX 470/480/570/570X/580/580X]
/0/100/1/0.1               multimedia     Ellesmere [Radeon RX 580]
/0/100/14                  bus            7 Series/C210 Series Chipset Family USB xHCI Host Controller
/0/100/14/0    usb3        bus            xHCI Host Controller
/0/100/14/0/1              input          USB Receiver
/0/100/14/0/3              communication  Broadcom Bluetooth 3.0 Device
/0/100/14/1    usb4        bus            xHCI Host Controller
/0/100/16                  communication  7 Series/C216 Chipset Family MEI Controller #1
/0/100/1a                  bus            7 Series/C216 Chipset Family USB Enhanced Host Controller #2
/0/100/1a/1    usb1        bus            EHCI Host Controller
/0/100/1a/1/1              bus            Integrated Rate Matching Hub
/0/100/1b                  multimedia     7 Series/C216 Chipset Family High Definition Audio Controller
/0/100/1c                  bridge         7 Series/C216 Chipset Family PCI Express Root Port 1
/0/100/1c.2                bridge         7 Series/C210 Series Chipset Family PCI Express Root Port 3
/0/100/1c.2/0  enp3s0      network        AR8161 Gigabit Ethernet
/0/100/1c.3                bridge         82801 PCI Bridge
/0/100/1c.3/0              bridge         82801 PCI Bridge
/0/100/1c.4                bridge         7 Series/C210 Series Chipset Family PCI Express Root Port 5
/0/100/1c.4/0  wlp6s0      network        BCM4360 802.11ac Wireless Network Adapter
/0/100/1d                  bus            7 Series/C216 Chipset Family USB Enhanced Host Controller #1
/0/100/1d/1    usb2        bus            EHCI Host Controller
/0/100/1d/1/1              bus            Integrated Rate Matching Hub
/0/100/1f                  bridge         Z77 Express Chipset LPC Controller
/0/100/1f.2                storage        7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode]
/0/100/1f.3                bus            7 Series/C216 Chipset Family SMBus Controller
/0/1           scsi0       storage        
/0/1/0.0.0     /dev/sda    disk           256GB SAMSUNG SSD 830
/0/1/0.0.0/1               volume         511MiB Windows FAT volume
/0/1/0.0.0/2   /dev/sda2   volume         237GiB EXT4 volume
/0/2           scsi1       storage        
/0/2/0.0.0     /dev/sdb    disk           256GB Samsung SSD 840
/0/2/0.0.0/1   /dev/sdb1   volume         528MiB Windows NTFS volume
/0/2/0.0.0/2   /dev/sdb2   volume         98MiB Windows FAT volume
/0/2/0.0.0/3   /dev/sdb3   volume         15MiB reserved partition
/0/2/0.0.0/4   /dev/sdb4   volume         237GiB Windows NTFS volume
/0/3           scsi4       storage        
/0/3/0.0.0     /dev/cdrom  disk           DVDRAM GH24NS95
/1                         power          To Be Filled By O.E.M.
</code></pre>

Hope this is enough information, if you need any more just write. I would be grateful for any kind of help