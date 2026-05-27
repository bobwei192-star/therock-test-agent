# ROCk module is NOT loaded, possibly no GPU devices

> **Issue #1505**
> **状态**: closed
> **创建时间**: 2021-06-25T06:53:01Z
> **更新时间**: 2021-06-25T09:45:25Z
> **关闭时间**: 2021-06-25T09:45:25Z
> **作者**: zwl773993221
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1505

## 描述

1.
zwl@ubuntu:~$ cat /proc/version
Linux version 5.4.0-77-generic (buildd@lgw01-amd64-021) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #86~18.04.1-Ubuntu SMP Fri Jun 18 01:23:22 UTC 2021
2.
use TechPowerUp GPU-Z check result is AMD Radeon(TM) Graphics
3.
zwl@ubuntu:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.5 LTS
Release:	18.04
Codename:	bionic
4.I follow this link:https://rocmdocs.amd.com/en/latest/InstallGuide.html

my question: if my compute support ROCM ? what to do my next step ? please give me a directive, thanks






---

## 评论 (11 条)

### 评论 #1 — ROCmSupport (2021-06-25T08:23:17Z)

Hi @zwl773993221 
Thanks for reaching out.
Can you please help me with the GPU that you use, you can get that information from the below command.
**lspci -nn | grep AMD/ATI**

---

### 评论 #2 — zwl773993221 (2021-06-25T08:49:49Z)

HI @ROCmSupport  
Thanks for you reply.
the order I give nothing ,but I use other order get information, hope this message have useful

zwl@ubuntu:~$ lspci nn | grep AMD/ATI
Usage: lspci [<switches>]

Basic display modes:
-mm		Produce machine-readable output (single -m for an obsolete format)
-t		Show bus tree

Display options:
-v		Be verbose (-vv for very verbose)
-k		Show kernel drivers handling each device
-x		Show hex-dump of the standard part of the config space
-xxx		Show hex-dump of the whole config space (dangerous; root only)
-xxxx		Show hex-dump of the 4096-byte extended config space (root only)
-b		Bus-centric view (addresses and IRQ's as seen by the bus)
-D		Always show domain numbers

Resolving of device ID's to names:
-n		Show numeric ID's
-nn		Show both textual and numeric ID's (names & numbers)
-q		Query the PCI ID database for unknown ID's via DNS
-qq		As above, but re-query locally cached entries
-Q		Query the PCI ID database for all ID's via DNS

Selection of devices:
-s [[[[<domain>]:]<bus>]:][<slot>][.[<func>]]	Show only devices in selected slots
-d [<vendor>]:[<device>][:<class>]		Show only devices with specified ID's

Other options:
-i <file>	Use specified ID database instead of /usr/share/misc/pci.ids.gz
-p <file>	Look up kernel modules in a given file instead of default modules.pcimap
-M		Enable `bus mapping' mode (dangerous; root only)

PCI access options:
-A <method>	Use the specified PCI access method (see `-A help' for a list)
-O <par>=<val>	Set PCI access parameter (see `-O help' for a list)
-G		Enable PCI access debugging
-H <mode>	Use direct hardware access (<mode> = 1 or 2)
-F <file>	Read PCI configuration dump from a given file
zwl@ubuntu:~$ lspci nn
Usage: lspci [<switches>]

Basic display modes:
-mm		Produce machine-readable output (single -m for an obsolete format)
-t		Show bus tree

Display options:
-v		Be verbose (-vv for very verbose)
-k		Show kernel drivers handling each device
-x		Show hex-dump of the standard part of the config space
-xxx		Show hex-dump of the whole config space (dangerous; root only)
-xxxx		Show hex-dump of the 4096-byte extended config space (root only)
-b		Bus-centric view (addresses and IRQ's as seen by the bus)
-D		Always show domain numbers

Resolving of device ID's to names:
-n		Show numeric ID's
-nn		Show both textual and numeric ID's (names & numbers)
-q		Query the PCI ID database for unknown ID's via DNS
-qq		As above, but re-query locally cached entries
-Q		Query the PCI ID database for all ID's via DNS

Selection of devices:
-s [[[[<domain>]:]<bus>]:][<slot>][.[<func>]]	Show only devices in selected slots
-d [<vendor>]:[<device>][:<class>]		Show only devices with specified ID's

Other options:
-i <file>	Use specified ID database instead of /usr/share/misc/pci.ids.gz
-p <file>	Look up kernel modules in a given file instead of default modules.pcimap
-M		Enable `bus mapping' mode (dangerous; root only)

PCI access options:
-A <method>	Use the specified PCI access method (see `-A help' for a list)
-O <par>=<val>	Set PCI access parameter (see `-O help' for a list)
-G		Enable PCI access debugging
-H <mode>	Use direct hardware access (<mode> = 1 or 2)
-F <file>	Read PCI configuration dump from a given file
zwl@ubuntu:~$ lspci -nn | grep AMD/ATI
zwl@ubuntu:~$ sudo lshw -c video
[sudo] password for zwl: 
  *-display                 
       description: VGA compatible controller
       product: SVGA II Adapter
       vendor: VMware
       physical id: f
       bus info: pci@0000:00:0f.0
       version: 00
       width: 32 bits
       clock: 33MHz
       capabilities: vga_controller bus_master cap_list rom
       configuration: driver=vmwgfx latency=64
       resources: irq:16 ioport:1070(size=16) memory:e8000000-efffffff memory:fe000000-fe7fffff memory:c0000-dffff
zwl@ubuntu:~$ lspci | grep AMD/ATI
zwl@ubuntu:~$ lspci
00:00.0 Host bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge (rev 01)
00:01.0 PCI bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge (rev 01)
00:07.0 ISA bridge: Intel Corporation 82371AB/EB/MB PIIX4 ISA (rev 08)
00:07.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)
00:07.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08)
00:07.7 System peripheral: VMware Virtual Machine Communication Interface (rev 10)
00:0f.0 VGA compatible controller: VMware SVGA II Adapter
00:10.0 SCSI storage controller: LSI Logic / Symbios Logic 53c1030 PCI-X Fusion-MPT Dual Ultra320 SCSI (rev 01)
00:11.0 PCI bridge: VMware PCI bridge (rev 02)
00:15.0 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.1 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.2 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.3 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.4 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.5 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.6 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.7 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.0 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.1 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.2 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.3 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.4 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.5 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.6 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.7 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.0 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.1 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.2 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.3 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.4 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.5 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.6 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.7 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.0 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.1 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.2 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.3 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.4 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.5 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.6 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.7 PCI bridge: VMware PCI Express Root Port (rev 01)
02:00.0 USB controller: VMware USB1.1 UHCI Controller
02:01.0 Ethernet controller: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) (rev 01)
02:02.0 Ethernet controller: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) (rev 01)
02:03.0 Multimedia audio controller: Ensoniq ES1371/ES1373 / Creative Labs CT2518 (rev 02)
02:04.0 USB controller: VMware USB2 EHCI Controller
02:06.0 SATA controller: VMware SATA AHCI controller
zwl@ubuntu:~$ lspci -nn | grep AMD/ATI
zwl@ubuntu:~$ lspci nn | grep AMD/ATI
Usage: lspci [<switches>]

Basic display modes:
-mm		Produce machine-readable output (single -m for an obsolete format)
-t		Show bus tree

Display options:
-v		Be verbose (-vv for very verbose)
-k		Show kernel drivers handling each device
-x		Show hex-dump of the standard part of the config space
-xxx		Show hex-dump of the whole config space (dangerous; root only)
-xxxx		Show hex-dump of the 4096-byte extended config space (root only)
-b		Bus-centric view (addresses and IRQ's as seen by the bus)
-D		Always show domain numbers

Resolving of device ID's to names:
-n		Show numeric ID's
-nn		Show both textual and numeric ID's (names & numbers)
-q		Query the PCI ID database for unknown ID's via DNS
-qq		As above, but re-query locally cached entries
-Q		Query the PCI ID database for all ID's via DNS

Selection of devices:
-s [[[[<domain>]:]<bus>]:][<slot>][.[<func>]]	Show only devices in selected slots
-d [<vendor>]:[<device>][:<class>]		Show only devices with specified ID's

Other options:
-i <file>	Use specified ID database instead of /usr/share/misc/pci.ids.gz
-p <file>	Look up kernel modules in a given file instead of default modules.pcimap
-M		Enable `bus mapping' mode (dangerous; root only)

PCI access options:
-A <method>	Use the specified PCI access method (see `-A help' for a list)
-O <par>=<val>	Set PCI access parameter (see `-O help' for a list)
-G		Enable PCI access debugging
-H <mode>	Use direct hardware access (<mode> = 1 or 2)
-F <file>	Read PCI configuration dump from a given file
zwl@ubuntu:~$ lspci -mm | grep AMD/ATI
zwl@ubuntu:~$ lspci -v | grep AMD/ATI
zwl@ubuntu:~$ lspci -v
00:00.0 Host bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge (rev 01)
	Subsystem: VMware Virtual Machine Chipset
	Flags: bus master, medium devsel, latency 0
	Kernel driver in use: agpgart-intel

00:01.0 PCI bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, 66MHz, medium devsel, latency 0
	Bus: primary=00, secondary=01, subordinate=01, sec-latency=64

00:07.0 ISA bridge: Intel Corporation 82371AB/EB/MB PIIX4 ISA (rev 08)
	Subsystem: VMware Virtual Machine Chipset
	Flags: bus master, medium devsel, latency 0

00:07.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01) (prog-if 8a [ISA Compatibility mode controller, supports both channels switched to PCI native mode, supports bus mastering])
	Subsystem: VMware Virtual Machine Chipset
	Flags: bus master, medium devsel, latency 64
	[virtual] Memory at 000001f0 (32-bit, non-prefetchable) [size=8]
	[virtual] Memory at 000003f0 (type 3, non-prefetchable)
	[virtual] Memory at 00000170 (32-bit, non-prefetchable) [size=8]
	[virtual] Memory at 00000370 (type 3, non-prefetchable)
	I/O ports at 1060 [size=16]
	Kernel driver in use: ata_piix
	Kernel modules: pata_acpi

00:07.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08)
	Subsystem: VMware Virtual Machine Chipset
	Flags: medium devsel, IRQ 9
	Kernel modules: i2c_piix4

00:07.7 System peripheral: VMware Virtual Machine Communication Interface (rev 10)
	Subsystem: VMware Virtual Machine Communication Interface
	Flags: bus master, medium devsel, latency 64, IRQ 16
	I/O ports at 1080 [size=64]
	Memory at febfe000 (64-bit, non-prefetchable) [size=8K]
	Capabilities: <access denied>
	Kernel driver in use: vmw_vmci
	Kernel modules: vmw_vmci

00:0f.0 VGA compatible controller: VMware SVGA II Adapter (prog-if 00 [VGA controller])
	Subsystem: VMware SVGA II Adapter
	Flags: bus master, medium devsel, latency 64, IRQ 16
	I/O ports at 1070 [size=16]
	Memory at e8000000 (32-bit, prefetchable) [size=128M]
	Memory at fe000000 (32-bit, non-prefetchable) [size=8M]
	[virtual] Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: vmwgfx
	Kernel modules: vmwgfx

00:10.0 SCSI storage controller: LSI Logic / Symbios Logic 53c1030 PCI-X Fusion-MPT Dual Ultra320 SCSI (rev 01)
	Subsystem: VMware LSI Logic Parallel SCSI Controller
	Flags: bus master, medium devsel, latency 64, IRQ 17
	I/O ports at 1400 [size=256]
	Memory at feba0000 (64-bit, non-prefetchable) [size=128K]
	Memory at febc0000 (64-bit, non-prefetchable) [size=128K]
	[virtual] Expansion ROM at c0008000 [disabled] [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: mptspi
	Kernel modules: mptspi

00:11.0 PCI bridge: VMware PCI bridge (rev 02) (prog-if 01 [Subtractive decode])
	Flags: bus master, medium devsel, latency 64
	Bus: primary=00, secondary=02, subordinate=02, sec-latency=68
	I/O behind bridge: 00002000-00003fff
	Memory behind bridge: fd500000-fdffffff
	Prefetchable memory behind bridge: 00000000e7b00000-00000000e7ffffff
	Capabilities: <access denied>

00:15.0 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 24
	Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
	I/O behind bridge: 00004000-00004fff
	Memory behind bridge: fd400000-fd4fffff
	Prefetchable memory behind bridge: 00000000e7a00000-00000000e7afffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:15.1 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 25
	Bus: primary=00, secondary=04, subordinate=04, sec-latency=0
	I/O behind bridge: 00008000-00008fff
	Memory behind bridge: fd000000-fd0fffff
	Prefetchable memory behind bridge: 00000000e7600000-00000000e76fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:15.2 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 26
	Bus: primary=00, secondary=05, subordinate=05, sec-latency=0
	I/O behind bridge: 0000c000-0000cfff
	Memory behind bridge: fcc00000-fccfffff
	Prefetchable memory behind bridge: 00000000e7200000-00000000e72fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:15.3 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 27
	Bus: primary=00, secondary=06, subordinate=06, sec-latency=0
	Memory behind bridge: fc800000-fc8fffff
	Prefetchable memory behind bridge: 00000000e6e00000-00000000e6efffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:15.4 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 28
	Bus: primary=00, secondary=07, subordinate=07, sec-latency=0
	Memory behind bridge: fc400000-fc4fffff
	Prefetchable memory behind bridge: 00000000e6a00000-00000000e6afffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:15.5 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 29
	Bus: primary=00, secondary=08, subordinate=08, sec-latency=0
	Memory behind bridge: fc000000-fc0fffff
	Prefetchable memory behind bridge: 00000000e6600000-00000000e66fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:15.6 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 30
	Bus: primary=00, secondary=09, subordinate=09, sec-latency=0
	Memory behind bridge: fbc00000-fbcfffff
	Prefetchable memory behind bridge: 00000000e6200000-00000000e62fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:15.7 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 31
	Bus: primary=00, secondary=0a, subordinate=0a, sec-latency=0
	Memory behind bridge: fb800000-fb8fffff
	Prefetchable memory behind bridge: 00000000e5e00000-00000000e5efffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.0 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 32
	Bus: primary=00, secondary=0b, subordinate=0b, sec-latency=0
	I/O behind bridge: 00005000-00005fff
	Memory behind bridge: fd300000-fd3fffff
	Prefetchable memory behind bridge: 00000000e7900000-00000000e79fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.1 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 33
	Bus: primary=00, secondary=0c, subordinate=0c, sec-latency=0
	I/O behind bridge: 00009000-00009fff
	Memory behind bridge: fcf00000-fcffffff
	Prefetchable memory behind bridge: 00000000e7500000-00000000e75fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.2 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 34
	Bus: primary=00, secondary=0d, subordinate=0d, sec-latency=0
	I/O behind bridge: 0000d000-0000dfff
	Memory behind bridge: fcb00000-fcbfffff
	Prefetchable memory behind bridge: 00000000e7100000-00000000e71fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.3 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 35
	Bus: primary=00, secondary=0e, subordinate=0e, sec-latency=0
	Memory behind bridge: fc700000-fc7fffff
	Prefetchable memory behind bridge: 00000000e6d00000-00000000e6dfffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.4 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 36
	Bus: primary=00, secondary=0f, subordinate=0f, sec-latency=0
	Memory behind bridge: fc300000-fc3fffff
	Prefetchable memory behind bridge: 00000000e6900000-00000000e69fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.5 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 37
	Bus: primary=00, secondary=10, subordinate=10, sec-latency=0
	Memory behind bridge: fbf00000-fbffffff
	Prefetchable memory behind bridge: 00000000e6500000-00000000e65fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.6 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 38
	Bus: primary=00, secondary=11, subordinate=11, sec-latency=0
	Memory behind bridge: fbb00000-fbbfffff
	Prefetchable memory behind bridge: 00000000e6100000-00000000e61fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:16.7 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 39
	Bus: primary=00, secondary=12, subordinate=12, sec-latency=0
	Memory behind bridge: fb700000-fb7fffff
	Prefetchable memory behind bridge: 00000000e5d00000-00000000e5dfffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:17.0 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 40
	Bus: primary=00, secondary=13, subordinate=13, sec-latency=0
	I/O behind bridge: 00006000-00006fff
	Memory behind bridge: fd200000-fd2fffff
	Prefetchable memory behind bridge: 00000000e7800000-00000000e78fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:17.1 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 41
	Bus: primary=00, secondary=14, subordinate=14, sec-latency=0
	I/O behind bridge: 0000a000-0000afff
	Memory behind bridge: fce00000-fcefffff
	Prefetchable memory behind bridge: 00000000e7400000-00000000e74fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:17.2 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 42
	Bus: primary=00, secondary=15, subordinate=15, sec-latency=0
	I/O behind bridge: 0000e000-0000efff
	Memory behind bridge: fca00000-fcafffff
	Prefetchable memory behind bridge: 00000000e7000000-00000000e70fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:17.3 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 43
	Bus: primary=00, secondary=16, subordinate=16, sec-latency=0
	Memory behind bridge: fc600000-fc6fffff
	Prefetchable memory behind bridge: 00000000e6c00000-00000000e6cfffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:17.4 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 44
	Bus: primary=00, secondary=17, subordinate=17, sec-latency=0
	Memory behind bridge: fc200000-fc2fffff
	Prefetchable memory behind bridge: 00000000e6800000-00000000e68fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:17.5 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 45
	Bus: primary=00, secondary=18, subordinate=18, sec-latency=0
	Memory behind bridge: fbe00000-fbefffff
	Prefetchable memory behind bridge: 00000000e6400000-00000000e64fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:17.6 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 46
	Bus: primary=00, secondary=19, subordinate=19, sec-latency=0
	Memory behind bridge: fba00000-fbafffff
	Prefetchable memory behind bridge: 00000000e6000000-00000000e60fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:17.7 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 47
	Bus: primary=00, secondary=1a, subordinate=1a, sec-latency=0
	Memory behind bridge: fb600000-fb6fffff
	Prefetchable memory behind bridge: 00000000e5c00000-00000000e5cfffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:18.0 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 48
	Bus: primary=00, secondary=1b, subordinate=1b, sec-latency=0
	I/O behind bridge: 00007000-00007fff
	Memory behind bridge: fd100000-fd1fffff
	Prefetchable memory behind bridge: 00000000e7700000-00000000e77fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:18.1 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 49
	Bus: primary=00, secondary=1c, subordinate=1c, sec-latency=0
	I/O behind bridge: 0000b000-0000bfff
	Memory behind bridge: fcd00000-fcdfffff
	Prefetchable memory behind bridge: 00000000e7300000-00000000e73fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:18.2 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 50
	Bus: primary=00, secondary=1d, subordinate=1d, sec-latency=0
	Memory behind bridge: fc900000-fc9fffff
	Prefetchable memory behind bridge: 00000000e6f00000-00000000e6ffffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:18.3 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 51
	Bus: primary=00, secondary=1e, subordinate=1e, sec-latency=0
	Memory behind bridge: fc500000-fc5fffff
	Prefetchable memory behind bridge: 00000000e6b00000-00000000e6bfffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:18.4 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 52
	Bus: primary=00, secondary=1f, subordinate=1f, sec-latency=0
	Memory behind bridge: fc100000-fc1fffff
	Prefetchable memory behind bridge: 00000000e6700000-00000000e67fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:18.5 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 53
	Bus: primary=00, secondary=20, subordinate=20, sec-latency=0
	Memory behind bridge: fbd00000-fbdfffff
	Prefetchable memory behind bridge: 00000000e6300000-00000000e63fffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:18.6 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 54
	Bus: primary=00, secondary=21, subordinate=21, sec-latency=0
	Memory behind bridge: fb900000-fb9fffff
	Prefetchable memory behind bridge: 00000000e5f00000-00000000e5ffffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

00:18.7 PCI bridge: VMware PCI Express Root Port (rev 01) (prog-if 00 [Normal decode])
	Flags: bus master, fast devsel, latency 0, IRQ 55
	Bus: primary=00, secondary=22, subordinate=22, sec-latency=0
	Memory behind bridge: fb500000-fb5fffff
	Prefetchable memory behind bridge: 00000000e5b00000-00000000e5bfffff
	Capabilities: <access denied>
	Kernel driver in use: pcieport

02:00.0 USB controller: VMware USB1.1 UHCI Controller (prog-if 00 [UHCI])
	Subsystem: VMware USB1.1 UHCI Controller
	Physical Slot: 32
	Flags: bus master, medium devsel, latency 64, IRQ 18
	I/O ports at 20c0 [size=32]
	Capabilities: <access denied>
	Kernel driver in use: uhci_hcd

02:01.0 Ethernet controller: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) (rev 01)
	Subsystem: VMware PRO/1000 MT Single Port Adapter
	Physical Slot: 33
	Flags: bus master, 66MHz, medium devsel, latency 0, IRQ 19
	Memory at fd5c0000 (64-bit, non-prefetchable) [size=128K]
	Memory at fdff0000 (64-bit, non-prefetchable) [size=64K]
	I/O ports at 2000 [size=64]
	[virtual] Expansion ROM at fd500000 [disabled] [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: e1000
	Kernel modules: e1000

02:02.0 Ethernet controller: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) (rev 01)
	Subsystem: VMware PRO/1000 MT Single Port Adapter
	Physical Slot: 34
	Flags: bus master, 66MHz, medium devsel, latency 0, IRQ 16
	Memory at fd5a0000 (64-bit, non-prefetchable) [size=128K]
	Memory at fdfe0000 (64-bit, non-prefetchable) [size=64K]
	I/O ports at 2040 [size=64]
	[virtual] Expansion ROM at fd510000 [disabled] [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: e1000
	Kernel modules: e1000

02:03.0 Multimedia audio controller: Ensoniq ES1371/ES1373 / Creative Labs CT2518 (rev 02)
	Subsystem: Ensoniq Audio PCI 64V/128/5200 / Creative CT4810/CT5803/CT5806 [Sound Blaster PCI]
	Physical Slot: 35
	Flags: bus master, medium devsel, latency 64, IRQ 17
	I/O ports at 2080 [size=64]
	Capabilities: <access denied>
	Kernel driver in use: snd_ens1371
	Kernel modules: snd_ens1371

02:04.0 USB controller: VMware USB2 EHCI Controller (prog-if 20 [EHCI])
	Subsystem: VMware USB2 EHCI Controller
	Physical Slot: 36
	Flags: bus master, fast devsel, latency 64, IRQ 18
	Memory at fd59f000 (32-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: ehci-pci

02:06.0 SATA controller: VMware SATA AHCI controller (prog-if 01 [AHCI 1.0])
	Subsystem: VMware SATA AHCI controller
	Physical Slot: 38
	Flags: bus master, 66MHz, fast devsel, latency 64, IRQ 56
	Memory at fd59e000 (32-bit, non-prefetchable) [size=4K]
	[virtual] Expansion ROM at fd520000 [disabled] [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: ahci
	Kernel modules: ahci

zwl@ubuntu:~$ 




---

### 评论 #3 — zwl773993221 (2021-06-25T09:11:08Z)

Hi @ROCmSupport 
Thanks you

I find System -Details , this show:
Ubuntu 18.04.5 LTS
Memory:3.8GiB
Processor:AMD Ryzen 7 4800u with radeon graphics * 2
Graphics:SVGA3D;build;RELEASE;LLVM;

Does my machine not support ROCM?

---

### 评论 #4 — ROCmSupport (2021-06-25T09:14:25Z)

Thanks @zwl773993221 
Looks like you are using very old radeon graphics. I am still not sure about the graphic card name.
Can you please share the output of **lspci -nn | grep AMD/ATI**

---

### 评论 #5 — zwl773993221 (2021-06-25T09:18:06Z)

@ROCmSupport 
Thanks for you reply

It’s a pity, this is a new machine I bought this year, and there is no output from this command.

output nothins

 zwl@ubuntu:~$ lspci -nn | grep AMD/ATI
zwl@ubuntu:~$ 

If my machine doesn’t support it, please let me know, thank you very much

---

### 评论 #6 — ROCmSupport (2021-06-25T09:22:45Z)

In my case, its showing that my machine is holding Vega10 card.

taccuser@taccuser-X399-DESIGNARE-EX:~$ _lspci -nn | grep AMD/ATI_
43:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] **Vega 10 XL/XT [Radeon RX Vega 56/64]** [1002:687f] (rev c1)
43:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 HDMI Audio [Radeon Vega 56/64] [1002:aaf8]


---

### 评论 #7 — ROCmSupport (2021-06-25T09:23:19Z)

Atleast try to share **lspci -nn** output

---

### 评论 #8 — zwl773993221 (2021-06-25T09:24:06Z)

@ROCmSupport 

zwl@ubuntu:~$ lspci -nn
00:00.0 Host bridge [0600]: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge [8086:7190] (rev 01)
00:01.0 PCI bridge [0604]: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge [8086:7191] (rev 01)
00:07.0 ISA bridge [0601]: Intel Corporation 82371AB/EB/MB PIIX4 ISA [8086:7110] (rev 08)
00:07.1 IDE interface [0101]: Intel Corporation 82371AB/EB/MB PIIX4 IDE [8086:7111] (rev 01)
00:07.3 Bridge [0680]: Intel Corporation 82371AB/EB/MB PIIX4 ACPI [8086:7113] (rev 08)
00:07.7 System peripheral [0880]: VMware Virtual Machine Communication Interface [15ad:0740] (rev 10)
00:0f.0 VGA compatible controller [0300]: VMware SVGA II Adapter [15ad:0405]
00:10.0 SCSI storage controller [0100]: LSI Logic / Symbios Logic 53c1030 PCI-X Fusion-MPT Dual Ultra320 SCSI [1000:0030] (rev 01)
00:11.0 PCI bridge [0604]: VMware PCI bridge [15ad:0790] (rev 02)
00:15.0 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:15.1 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:15.2 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:15.3 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:15.4 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:15.5 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:15.6 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:15.7 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:16.0 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:16.1 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:16.2 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:16.3 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:16.4 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:16.5 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:16.6 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:16.7 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:17.0 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:17.1 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:17.2 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:17.3 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:17.4 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:17.5 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:17.6 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:17.7 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:18.0 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:18.1 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:18.2 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:18.3 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:18.4 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:18.5 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:18.6 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
00:18.7 PCI bridge [0604]: VMware PCI Express Root Port [15ad:07a0] (rev 01)
02:00.0 USB controller [0c03]: VMware USB1.1 UHCI Controller [15ad:0774]
02:01.0 Ethernet controller [0200]: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) [8086:100f] (rev 01)
02:02.0 Ethernet controller [0200]: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) [8086:100f] (rev 01)
02:03.0 Multimedia audio controller [0401]: Ensoniq ES1371/ES1373 / Creative Labs CT2518 [1274:1371] (rev 02)
02:04.0 USB controller [0c03]: VMware USB2 EHCI Controller [15ad:0770]
02:06.0 SATA controller [0106]: VMware SATA AHCI controller [15ad:07e0]
zwl@ubuntu:~$ 


---

### 评论 #9 — ROCmSupport (2021-06-25T09:26:26Z)

Looks like you do not have a physical GPU in the system(as per the lspci output).
Can you please check your system physically that it has a discrete GPU or not?
Thank you.


---

### 评论 #10 — zwl773993221 (2021-06-25T09:39:42Z)

Thank you very much, I just found some information on the Internet, saying that this machine is an integrated graphics card, CPU and GPU in one chip, AMD Ryzen 7 4800U, if this is the case, can my machine pass VMware+ubuntu18.04, come Complete the installation of ROCM for deep learning or machine learning

or how can i solve ROCm module is NOT loaded, possibly no GPU devices ？

---

### 评论 #11 — ROCmSupport (2021-06-25T09:45:25Z)

Yes, I got that you are using Ryzen. But I am worrying about discrete GPU.
Thanks for confirming that you do not have a discrete GPU in the system.
ROCm does not support integrated GPUs, it only supports discrete GPUs. Please check [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url) for more information
Thank you.

---
