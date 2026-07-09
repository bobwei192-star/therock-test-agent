# Why Rocm can't install on Ubuntu 18.04 LTS

- **Issue #:** 646
- **State:** closed
- **Created:** 2018-12-24T07:20:52Z
- **Updated:** 2019-01-15T19:05:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/646

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

