# Radeon ProRender for Blender 1.7.203 renders black on Vega FE

- **Issue #:** 503
- **State:** closed
- **Created:** 2018-08-19T07:13:41Z
- **Updated:** 2021-01-07T08:30:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/503

Hello,
I have had time to test ROCm 1.8.2 on my Ubuntu 18.04 machine again, and it looks like the dkms driver compiles fine on 4.15 this time around, thank you!

However when testing Radeon ProRender on Blender 2.79 I've found that it just renders black when picking the Vega card, and on CPU it does render correctly.

2x E5-2680v2 Xeons with a Vega Frontier Edition running headless, Nvidia Quadro k2000 for display, the CPU itself should have PCI-E 3.0 with atomic, but for double-checking I've also tried with ```export HSA_ENABLE_SDMA=0```

Stats: 
```
$ lsmod | grep amdgpu
amdgpu               2699264  2
amdchash               16384  1 amdgpu
amd_sched              24576  1 amdgpu
amdttm                110592  1 amdgpu
amdkcl                 28672  4 amdttm,amdgpu,amd_sched,amdkfd
i2c_algo_bit           16384  2 amdgpu,nouveau
drm_kms_helper        172032  2 amdgpu,nouveau
drm                   401408  18 amdttm,amdgpu,amdkcl,amd_sched,nouveau,ttm,drm_kms_helper
```
```
$ lsmod | grep amdkfd
amdkfd                274432  3
amd_iommu_v2           20480  1 amdkfd
amdkcl                 28672  4 amdttm,amdgpu,amd_sched,amdkfd
```
```
$ groups
alex adm cdrom sudo dip video plugdev lpadmin sambashare docker libvirt dockershared
```
```
$ lspci | grep VGA
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition]
07:00.0 VGA compatible controller: NVIDIA Corporation GK107GL [Quadro K2000] (rev a1)
```
```
$ lspci -vvv
00:00.0 Host bridge: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 DMI2 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 DMI2
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Interrupt: pin A routed to IRQ 0
        NUMA node: 0
        Capabilities: <access denied>

00:01.0 PCI bridge: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 1a (rev 04) (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 24
        NUMA node: 0
        Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
        I/O behind bridge: 0000f000-00000fff
        Memory behind bridge: fff00000-000fffff
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
        BridgeCtl: Parity+ SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>                                                                                                                                   
        Kernel driver in use: pcieport                                                                                                                                  
        Kernel modules: shpchp                                                                                                                                          
                                                                                                                                                                        
00:02.0 PCI bridge: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 2a (rev 04) (prog-if 00 [Normal decode])                                      
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B- DisINTx-                                                           
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-                                                            
        Latency: 0, Cache Line Size: 64 bytes                                                                                                                           
        Interrupt: pin A routed to IRQ 25                                                                                                                               
        NUMA node: 0                                                                                                                                                    
        Bus: primary=00, secondary=07, subordinate=07, sec-latency=0                                                                                                    
        I/O behind bridge: 0000a000-0000afff
        Memory behind bridge: ee000000-ef0fffff
        Prefetchable memory behind bridge: 00000000b0000000-00000000c1ffffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity+ SERR+ NoISA- VGA+ MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

00:03.0 PCI bridge: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 3a (rev 04) (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 26
        NUMA node: 0
        Bus: primary=00, secondary=04, subordinate=06, sec-latency=0
        I/O behind bridge: 0000b000-0000bfff
        Memory behind bridge: ef100000-ef2fffff
        Prefetchable memory behind bridge: 00000000d0000000-00000000e01fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity+ SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

00:04.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 0 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 0
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 43
        NUMA node: 0
        Region 0: Memory at ef63c000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

00:04.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 1 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 1
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 45
        NUMA node: 0
        Region 0: Memory at ef638000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

00:04.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 2 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 2
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin C routed to IRQ 43
        NUMA node: 0
        Region 0: Memory at ef634000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

00:04.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 3 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 3
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin D routed to IRQ 45
        NUMA node: 0
        Region 0: Memory at ef630000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

00:04.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 4 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 4
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 43
        NUMA node: 0
        Region 0: Memory at ef62c000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

00:04.5 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 5 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 5
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 45
        NUMA node: 0
        Region 0: Memory at ef628000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

00:04.6 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 6 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 6
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin C routed to IRQ 43
        NUMA node: 0
        Region 0: Memory at ef624000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

00:04.7 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 7 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 7
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin D routed to IRQ 45
        NUMA node: 0
        Region 0: Memory at ef620000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

00:05.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 VTd/Memory Map/Misc (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 VTd/Memory Map/Misc
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        NUMA node: 0
        Capabilities: <access denied>

00:05.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IIO RAS (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 IIO RAS
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        NUMA node: 0
        Capabilities: <access denied>

00:05.4 PIC: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IOAPIC (rev 04) (prog-if 20 [IO(X)-APIC])
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IOAPIC
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        NUMA node: 0
        Region 0: Memory at ef64a000 (32-bit, non-prefetchable) [size=4K]
        Capabilities: <access denied>

00:11.0 PCI bridge: Intel Corporation C600/X79 series chipset PCI Express Virtual Root Port (rev 05) (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 16
        NUMA node: 0
        Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
        I/O behind bridge: 0000c000-0000cfff
        Memory behind bridge: c2000000-c20fffff
        Prefetchable memory behind bridge: 00000000e0400000-00000000e08fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

00:16.0 Communication controller: Intel Corporation C600/X79 series chipset MEI Controller #1 (rev 05)
        Subsystem: Hewlett-Packard Company C600/X79 series chipset MEI Controller
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin A routed to IRQ 47
        NUMA node: 0
        Region 0: Memory at ef649000 (64-bit, non-prefetchable) [size=16]
        Capabilities: <access denied>
        Kernel driver in use: mei_me
        Kernel modules: mei_me

00:16.2 IDE interface: Intel Corporation C600/X79 series chipset IDE-r Controller (rev 05) (prog-if 85 [Master SecO PriO])
        Subsystem: Hewlett-Packard Company C600/X79 series chipset IDE-r Controller
        Control: I/O+ Mem- BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin C routed to IRQ 18
        NUMA node: 0
        Region 0: I/O ports at e0b0 [size=8]
        Region 1: I/O ports at e0a0 [size=4]
        Region 2: I/O ports at e090 [size=8]
        Region 3: I/O ports at e080 [size=4]
        Region 4: I/O ports at e070 [size=16]
        Capabilities: <access denied>
        Kernel driver in use: ata_generic
        Kernel modules: pata_acpi

00:16.3 Serial controller: Intel Corporation C600/X79 series chipset KT Controller (rev 05) (prog-if 02 [16550])
        Subsystem: Hewlett-Packard Company C600/X79 series chipset KT Controller
        Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Interrupt: pin B routed to IRQ 17
        NUMA node: 0
        Region 0: I/O ports at e060 [size=8]
        Region 1: Memory at ef647000 (32-bit, non-prefetchable) [size=4K]
        Capabilities: <access denied>
        Kernel driver in use: serial

00:19.0 Ethernet controller: Intel Corporation 82579LM Gigabit Network Connection (rev 05)
        Subsystem: Hewlett-Packard Company 82579LM Gigabit Network Connection (Lewisville)
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin A routed to IRQ 38
        NUMA node: 0
        Region 0: Memory at ef600000 (32-bit, non-prefetchable) [size=128K]
        Region 1: Memory at ef64d000 (32-bit, non-prefetchable) [size=4K]
        Region 2: I/O ports at e040 [size=32]
        Capabilities: <access denied>
        Kernel driver in use: e1000e
        Kernel modules: e1000e

00:1a.0 USB controller: Intel Corporation C600/X79 series chipset USB2 Enhanced Host Controller #2 (rev 05) (prog-if 20 [EHCI])
        Subsystem: Hewlett-Packard Company C600/X79 series chipset USB2 Enhanced Host Controller
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin A routed to IRQ 16
        NUMA node: 0
        Region 0: Memory at ef64f000 (32-bit, non-prefetchable) [size=1K]
        Capabilities: <access denied>
        Kernel driver in use: ehci-pci

00:1b.0 Audio device: Intel Corporation C600/X79 series chipset High Definition Audio Controller (rev 05)
        Subsystem: Hewlett-Packard Company C600/X79 series chipset High Definition Audio Controller
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 64
        NUMA node: 0
        Region 0: Memory at ef640000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

00:1c.0 PCI bridge: Intel Corporation C600/X79 series chipset PCI Express Root Port 2 (rev b5) (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 16
        NUMA node: 0
        Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
        I/O behind bridge: 0000d000-0000dfff
        Memory behind bridge: ef500000-ef5fffff
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity+ SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

00:1c.5 PCI bridge: Intel Corporation C600/X79 series chipset PCI Express Root Port 5 (rev b5) (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 17
        NUMA node: 0
        Bus: primary=00, secondary=08, subordinate=08, sec-latency=0
        I/O behind bridge: 0000f000-00000fff
        Memory behind bridge: fff00000-000fffff
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity+ SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

00:1c.6 PCI bridge: Intel Corporation C600/X79 series chipset PCI Express Root Port 3 (rev b5) (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin C routed to IRQ 18
        NUMA node: 0
        Bus: primary=00, secondary=09, subordinate=09, sec-latency=0
        I/O behind bridge: 0000f000-00000fff
        Memory behind bridge: fff00000-000fffff
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity+ SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

00:1c.7 PCI bridge: Intel Corporation C600/X79 series chipset PCI Express Root Port 4 (rev b5) (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin D routed to IRQ 19
        NUMA node: 0
        Bus: primary=00, secondary=0a, subordinate=0a, sec-latency=0
        I/O behind bridge: 0000f000-00000fff
        Memory behind bridge: ef400000-ef4fffff
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

00:1d.0 USB controller: Intel Corporation C600/X79 series chipset USB2 Enhanced Host Controller #1 (rev 05) (prog-if 20 [EHCI])
        Subsystem: Hewlett-Packard Company C600/X79 series chipset USB2 Enhanced Host Controller
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin A routed to IRQ 23
        NUMA node: 0
        Region 0: Memory at ef64e000 (32-bit, non-prefetchable) [size=1K]
        Capabilities: <access denied>
        Kernel driver in use: ehci-pci

00:1e.0 PCI bridge: Intel Corporation 82801 PCI Bridge (rev a5) (prog-if 01 [Subtractive decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        NUMA node: 0
        Bus: primary=00, secondary=0b, subordinate=0b, sec-latency=128
        I/O behind bridge: 0000f000-00000fff
        Memory behind bridge: ef300000-ef3fffff
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff
        Secondary status: 66MHz- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity+ SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>

00:1f.0 ISA bridge: Intel Corporation C600/X79 series chipset LPC Controller (rev 05)
        Subsystem: Hewlett-Packard Company C600/X79 series chipset LPC Controller
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        NUMA node: 0
        Capabilities: <access denied>
        Kernel driver in use: lpc_ich
        Kernel modules: lpc_ich

00:1f.2 SATA controller: Intel Corporation C600/X79 series chipset 6-Port SATA AHCI Controller (rev 05) (prog-if 01 [AHCI 1.0])
        Subsystem: Hewlett-Packard Company C600/X79 series chipset 6-Port SATA AHCI Controller
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin B routed to IRQ 35
        NUMA node: 0
        Region 0: I/O ports at e0f0 [size=8]
        Region 1: I/O ports at e0e0 [size=4]
        Region 2: I/O ports at e0d0 [size=8]
        Region 3: I/O ports at e0c0 [size=4]
        Region 4: I/O ports at e020 [size=32]
        Region 5: Memory at ef64c000 (32-bit, non-prefetchable) [size=2K]
        Capabilities: <access denied>
        Kernel driver in use: ahci
        Kernel modules: ahci

00:1f.3 SMBus: Intel Corporation C600/X79 series chipset SMBus Host Controller (rev 05)
        Subsystem: Hewlett-Packard Company C600/X79 series chipset SMBus Host Controller
        Control: I/O+ Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Interrupt: pin C routed to IRQ 11
        NUMA node: 0
        Region 0: Memory at ef64b000 (64-bit, non-prefetchable) [disabled] [size=256]
        Region 4: I/O ports at e000 [size=32]
        Kernel modules: i2c_i801

01:00.0 Ethernet controller: Intel Corporation 82574L Gigabit Network Connection
        Subsystem: Hewlett-Packard Company 82574L Gigabit Network Connection
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 17
        NUMA node: 0
        Region 0: Memory at ef500000 (32-bit, non-prefetchable) [size=128K]
        Region 2: I/O ports at d000 [size=32]
        Region 3: Memory at ef520000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: e1000e
        Kernel modules: e1000e

02:00.0 Serial Attached SCSI controller: Intel Corporation C602 chipset 4-Port SATA Storage Control Unit (rev 05)
        Subsystem: Hewlett-Packard Company C602 chipset 4-Port SATA Storage Control Unit
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 16
        NUMA node: 0
        Region 0: Memory at e0800000 (64-bit, prefetchable) [size=16K]
        Region 2: Memory at e0400000 (64-bit, prefetchable) [size=4M]
        Region 4: I/O ports at c000 [size=256]
        Capabilities: <access denied>
        Kernel driver in use: isci
        Kernel modules: isci

04:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470 (prog-if 00 [Normal decode])
        Physical Slot: 5
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 26
        NUMA node: 0
        Region 0: Memory at ef200000 (32-bit, non-prefetchable) [size=16K]
        Bus: primary=04, secondary=05, subordinate=06, sec-latency=0
        I/O behind bridge: 0000b000-0000bfff
        Memory behind bridge: ef100000-ef1fffff
        Prefetchable memory behind bridge: 00000000d0000000-00000000e01fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

05:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471 (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 26
        NUMA node: 0
        Bus: primary=05, secondary=06, subordinate=06, sec-latency=0
        I/O behind bridge: 0000b000-0000bfff
        Memory behind bridge: ef100000-ef1fffff
        Prefetchable memory behind bridge: 00000000d0000000-00000000e01fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: <access denied>
        Kernel driver in use: pcieport
        Kernel modules: shpchp

06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition] (prog-if 00 [VGA controller])
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition]
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 42
        NUMA node: 0
        Region 0: Memory at d0000000 (64-bit, prefetchable) [size=256M]
        Region 2: Memory at e0000000 (64-bit, prefetchable) [size=2M]
        Region 4: I/O ports at b000 [size=256]
        Region 5: Memory at ef100000 (32-bit, non-prefetchable) [size=512K]
        Expansion ROM at ef180000 [disabled] [size=128K]
        Capabilities: <access denied>
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu

06:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 67
        NUMA node: 0
        Region 0: Memory at ef1a0000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

07:00.0 VGA compatible controller: NVIDIA Corporation GK107GL [Quadro K2000] (rev a1) (prog-if 00 [VGA controller])
        Subsystem: Hewlett-Packard Company GK107GL [Quadro K2000]
        Physical Slot: 2
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 68
        NUMA node: 0
        Region 0: Memory at ee000000 (32-bit, non-prefetchable) [size=16M]
        Region 1: Memory at b0000000 (64-bit, prefetchable) [size=256M]
        Region 3: Memory at c0000000 (64-bit, prefetchable) [size=32M]
        Region 5: I/O ports at a000 [size=128]
        Expansion ROM at ef000000 [disabled] [size=512K]
        Capabilities: <access denied>
        Kernel driver in use: nouveau
        Kernel modules: nvidiafb, nouveau, nvidia_drm, nvidia

07:00.1 Audio device: NVIDIA Corporation GK107 HDMI Audio Controller (rev a1)
        Subsystem: Hewlett-Packard Company GK107 HDMI Audio Controller
        Physical Slot: 2
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 65
        NUMA node: 0
        Region 0: Memory at ef080000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

0a:00.0 USB controller: Texas Instruments TUSB73x0 SuperSpeed USB 3.0 xHCI Host Controller (rev 02) (prog-if 30 [XHCI])
        Subsystem: Hewlett-Packard Company TUSB73x0 SuperSpeed USB 3.0 xHCI Host Controller
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 19
        NUMA node: 0
        Region 0: Memory at ef400000 (64-bit, non-prefetchable) [size=64K]
        Region 2: Memory at ef410000 (64-bit, non-prefetchable) [size=8K]
        Capabilities: <access denied>
        Kernel driver in use: xhci_hcd

0b:05.0 FireWire (IEEE 1394): LSI Corporation FW322/323 [TrueFire] 1394a Controller (rev 70) (prog-if 10 [OHCI])
        Subsystem: Hewlett-Packard Company FW322/323 [TrueFire] 1394a Controller
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 128 (3000ns min, 6000ns max), Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 19
        NUMA node: 0
        Region 0: Memory at ef300000 (32-bit, non-prefetchable) [size=4K]
        Capabilities: <access denied>
        Kernel driver in use: firewire_ohci
        Kernel modules: firewire_ohci

3f:08.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 0 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 0
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:09.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 1 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 1
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0a.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 0 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 0
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0a.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 1 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 1
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0a.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 2 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 2
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0a.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 3 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 3
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0b.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0b.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0c.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0c.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0c.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0c.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0c.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0d.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0d.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0d.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0d.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0d.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0e.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Home Agent 0 (rev 04)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:0e.1 Performance counters: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Home Agent 0 (rev 04)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Kernel driver in use: ivbep_uncore

3f:0f.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Target Address/Thermal Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Target Address/Thermal Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:0f.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 RAS Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 RAS Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:0f.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:0f.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:0f.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:0f.5 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:10.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 0 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 0
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>
        Kernel driver in use: ivbep_uncore

3f:10.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 1 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 1
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>
        Kernel driver in use: ivbep_uncore

3f:10.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 0 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 0
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:10.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 1 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 1
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:10.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 2 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 2
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>
        Kernel driver in use: ivbep_uncore

3f:10.5 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 3 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 3
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>
        Kernel driver in use: ivbep_uncore

3f:10.6 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 2 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 2
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:10.7 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 3 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 3
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

3f:13.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:13.1 Performance counters: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Kernel driver in use: ivbep_uncore

3f:13.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:13.5 Performance counters: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Performance Ring Monitoring (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Performance Ring Monitoring
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Kernel driver in use: ivbep_uncore

3f:16.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 System Address Decoder (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 System Address Decoder
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:16.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

3f:16.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

40:04.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 0 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 0
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 54
        NUMA node: 1
        Region 0: Memory at fbf1c000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

40:04.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 1 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 1
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 56
        NUMA node: 1
        Region 0: Memory at fbf18000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

40:04.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 2 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 2
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin C routed to IRQ 54
        NUMA node: 1
        Region 0: Memory at fbf14000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

40:04.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 3 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 3
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin D routed to IRQ 56
        NUMA node: 1
        Region 0: Memory at fbf10000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

40:04.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 4 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 4
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 54
        NUMA node: 1
        Region 0: Memory at fbf0c000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

40:04.5 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 5 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 5
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 56
        NUMA node: 1
        Region 0: Memory at fbf08000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

40:04.6 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 6 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 6
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin C routed to IRQ 54
        NUMA node: 1
        Region 0: Memory at fbf04000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

40:04.7 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 7 (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 7
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin D routed to IRQ 56
        NUMA node: 1
        Region 0: Memory at fbf00000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: ioatdma
        Kernel modules: ioatdma

40:05.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 VTd/Memory Map/Misc (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 VTd/Memory Map/Misc
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        NUMA node: 1
        Capabilities: <access denied>

40:05.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IIO RAS (rev 04)
        Subsystem: Hewlett-Packard Company Xeon E7 v2/Xeon E5 v2/Core i7 IIO RAS
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        NUMA node: 1
        Capabilities: <access denied>

40:05.4 PIC: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IOAPIC (rev 04) (prog-if 20 [IO(X)-APIC])
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IOAPIC
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        NUMA node: 1
        Region 0: Memory at fbf22000 (32-bit, non-prefetchable) [size=4K]
        Capabilities: <access denied>

7f:08.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 0 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 0
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:09.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 1 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 1
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0a.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 0 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 0
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0a.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 1 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 1
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0a.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 2 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 2
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0a.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 3 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 3
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0b.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0b.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0c.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0c.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0c.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0c.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0c.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0d.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0d.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0d.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0d.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0d.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0e.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Home Agent 0 (rev 04)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:0e.1 Performance counters: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Home Agent 0 (rev 04)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Kernel driver in use: ivbep_uncore

7f:0f.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Target Address/Thermal Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Target Address/Thermal Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:0f.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 RAS Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 RAS Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:0f.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:0f.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:0f.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:0f.5 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:10.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 0 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 0
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>
        Kernel driver in use: ivbep_uncore

7f:10.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 1 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 1
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>
        Kernel driver in use: ivbep_uncore

7f:10.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 0 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 0
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:10.3 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 1 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 1
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:10.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 2 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 2
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>
        Kernel driver in use: ivbep_uncore

7f:10.5 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 3 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 3
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>
        Kernel driver in use: ivbep_uncore

7f:10.6 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 2 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 2
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:10.7 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 3 (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 3
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Capabilities: <access denied>

7f:13.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:13.1 Performance counters: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Kernel driver in use: ivbep_uncore

7f:13.4 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:13.5 Performance counters: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Performance Ring Monitoring (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Performance Ring Monitoring
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Kernel driver in use: ivbep_uncore

7f:16.0 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 System Address Decoder (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 System Address Decoder
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:16.1 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

7f:16.2 System peripheral: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers (rev 04)
        Subsystem: Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
```
```
$ lspci -tv
-+-[0000:7f]-+-08.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 0
 |           +-09.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 1
 |           +-0a.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 0
 |           +-0a.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 1
 |           +-0a.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 2
 |           +-0a.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 3
 |           +-0b.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers
 |           +-0b.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers
 |           +-0c.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0c.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0c.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0c.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0c.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0e.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Home Agent 0
 |           +-0e.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Home Agent 0
 |           +-0f.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Target Address/Thermal Registers
 |           +-0f.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 RAS Registers
 |           +-0f.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
 |           +-0f.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
 |           +-0f.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
 |           +-0f.5  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
 |           +-10.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 0
 |           +-10.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 1
 |           +-10.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 0
 |           +-10.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 1
 |           +-10.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 2
 |           +-10.5  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 3
 |           +-10.6  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 2
 |           +-10.7  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 3
 |           +-13.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe
 |           +-13.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe
 |           +-13.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Registers
 |           +-13.5  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Performance Ring Monitoring
 |           +-16.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 System Address Decoder
 |           +-16.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers
 |           \-16.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers
 +-[0000:40]-+-04.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 0
 |           +-04.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 1
 |           +-04.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 2
 |           +-04.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 3
 |           +-04.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 4
 |           +-04.5  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 5
 |           +-04.6  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 6
 |           +-04.7  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 7
 |           +-05.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 VTd/Memory Map/Misc
 |           +-05.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IIO RAS
 |           \-05.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IOAPIC
 +-[0000:3f]-+-08.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 0
 |           +-09.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Link 1
 |           +-0a.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 0
 |           +-0a.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 1
 |           +-0a.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 2
 |           +-0a.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Power Control Unit 3
 |           +-0b.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers
 |           +-0b.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 UBOX Registers
 |           +-0c.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0c.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0c.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0c.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0c.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0d.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Unicast Registers
 |           +-0e.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Home Agent 0
 |           +-0e.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Home Agent 0
 |           +-0f.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Target Address/Thermal Registers
 |           +-0f.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 RAS Registers
 |           +-0f.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
 |           +-0f.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
 |           +-0f.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
 |           +-0f.5  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder Registers
 |           +-10.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 0
 |           +-10.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 1
 |           +-10.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 0
 |           +-10.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 1
 |           +-10.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 2
 |           +-10.5  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 Thermal Control 3
 |           +-10.6  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 2
 |           +-10.7  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Integrated Memory Controller 1 Channel 0-3 ERROR Registers 3
 |           +-13.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe
 |           +-13.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 R2PCIe
 |           +-13.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Registers
 |           +-13.5  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 QPI Ring Performance Ring Monitoring
 |           +-16.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 System Address Decoder
 |           +-16.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers
 |           \-16.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Broadcast Registers
 \-[0000:00]-+-00.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 DMI2
             +-01.0-[03]--
             +-02.0-[07]--+-00.0  NVIDIA Corporation GK107GL [Quadro K2000]
             |            \-00.1  NVIDIA Corporation GK107 HDMI Audio Controller
             +-03.0-[04-06]----00.0-[05-06]----00.0-[06]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition]
             |                                            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
             +-04.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 0
             +-04.1  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 1
             +-04.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 2
             +-04.3  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 3
             +-04.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 4
             +-04.5  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 5
             +-04.6  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 6
             +-04.7  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 7
             +-05.0  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 VTd/Memory Map/Misc
             +-05.2  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IIO RAS
             +-05.4  Intel Corporation Xeon E7 v2/Xeon E5 v2/Core i7 IOAPIC
             +-11.0-[02]----00.0  Intel Corporation C602 chipset 4-Port SATA Storage Control Unit
             +-16.0  Intel Corporation C600/X79 series chipset MEI Controller #1
             +-16.2  Intel Corporation C600/X79 series chipset IDE-r Controller
             +-16.3  Intel Corporation C600/X79 series chipset KT Controller
             +-19.0  Intel Corporation 82579LM Gigabit Network Connection
             +-1a.0  Intel Corporation C600/X79 series chipset USB2 Enhanced Host Controller #2
             +-1b.0  Intel Corporation C600/X79 series chipset High Definition Audio Controller
             +-1c.0-[01]----00.0  Intel Corporation 82574L Gigabit Network Connection
             +-1c.5-[08]--
             +-1c.6-[09]--
             +-1c.7-[0a]----00.0  Texas Instruments TUSB73x0 SuperSpeed USB 3.0 xHCI Host Controller
             +-1d.0  Intel Corporation C600/X79 series chipset USB2 Enhanced Host Controller #1
             +-1e.0-[0b]----05.0  LSI Corporation FW322/323 [TrueFire] 1394a Controller
             +-1f.0  Intel Corporation C600/X79 series chipset LPC Controller
             +-1f.2  Intel Corporation C600/X79 series chipset 6-Port SATA AHCI Controller
             \-1f.3  Intel Corporation C600/X79 series chipset SMBus Host Controller
```
```
$ dmesg
[    0.000000] microcode: microcode updated early to revision 0x42c, date = 2018-01-25
[    0.000000] Linux version 4.15.0-30-generic (buildd@lgw01-amd64-060) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #32-Ubuntu SMP Thu Jul 26 17:42:43 UTC 2018 (Ubuntu 4.15.0-30.32-generic 4.15.18)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-30-generic root=UUID=7cc57c85-4008-465f-ade9-dffcb3a2a5c0 ro quiet splash vt.handoff=1
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'standard' format.
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009ffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000ab3c6fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000ab3c7000-0x00000000ab6c6fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ab6c7000-0x00000000ab7eefff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000ab7ef000-0x00000000ab9e4fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000ab9e5000-0x00000000ababbfff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ababc000-0x00000000abb0efff] type 20
[    0.000000] BIOS-e820: [mem 0x00000000abb0f000-0x00000000abb0ffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000abb10000-0x00000000abb95fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000abb96000-0x00000000abffffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000f0000000-0x00000000f7ffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed1c000-0x00000000fed3ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000104fffffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] efi: EFI v2.31 by American Megatrends
[    0.000000] efi:  ACPI 2.0=0xab702000  ACPI=0xab702000  SMBIOS=0xababab98  MPS=0xf4a20 
[    0.000000] secureboot: Secure boot could not be determined (mode 0)
[    0.000000] SMBIOS 2.7 present.
[    0.000000] DMI: Hewlett-Packard HP Z620 Workstation/158A, BIOS J61 v03.91 10/17/2016
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x1050000 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: write-back
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF uncachable
[    0.000000]   C0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 0000AC000000 mask 3FFFFC000000 uncachable
[    0.000000]   1 base 0000B0000000 mask 3FFFF0000000 uncachable
[    0.000000]   2 base 0000C0000000 mask 3FFFC0000000 uncachable
[    0.000000]   3 base 001050000000 mask 3FFFF0000000 uncachable
[    0.000000]   4 base 380000000000 mask 3FE000000000 uncachable
[    0.000000]   5 disabled
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000]   8 disabled
[    0.000000]   9 disabled
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000000] e820: last_pfn = 0xac000 max_arch_pfn = 0x400000000
[    0.000000] found SMP MP-table at [mem 0x000f4a10-0x000f4a1f] mapped at [        (ptrval)]
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [        (ptrval)] 99000 size 24576
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x46733f000, 0x46733ffff] PGTABLE
[    0.000000] BRK [0x467340000, 0x467340fff] PGTABLE
[    0.000000] BRK [0x467341000, 0x467341fff] PGTABLE
[    0.000000] BRK [0x467342000, 0x467342fff] PGTABLE
[    0.000000] BRK [0x467343000, 0x467343fff] PGTABLE
[    0.000000] BRK [0x467344000, 0x467344fff] PGTABLE
[    0.000000] BRK [0x467345000, 0x467345fff] PGTABLE
[    0.000000] BRK [0x467346000, 0x467346fff] PGTABLE
[    0.000000] RAMDISK: [mem 0x3047d000-0x34235fff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x00000000AB702000 000024 (v02 HPQOEM)
[    0.000000] ACPI: XSDT 0x00000000AB702098 0000B4 (v01 HPQOEM SLIC-WKS 01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x00000000AB709D70 00010C (v05 HPQOEM SLIC-WKS 01072009 AMI  00010013)
[    0.000000] ACPI: DSDT 0x00000000AB7021E0 007B8D (v02 HPQOEM SLIC-WKS 00000391 INTL 20051117)
[    0.000000] ACPI: FACS 0x00000000AB9DC080 000040
[    0.000000] ACPI: APIC 0x00000000AB709E80 000294 (v03 HPQOEM SLIC-WKS 01072009 AMI  00010013)
[    0.000000] ACPI: FPDT 0x00000000AB70A118 000044 (v01 HPQOEM SLIC-WKS 01072009 AMI  00010013)
[    0.000000] ACPI: MCFG 0x00000000AB70A160 00003C (v01 HPQOEM OEMMCFG. 01072009 MSFT 00000097)
[    0.000000] ACPI: SRAT 0x00000000AB70A1A0 000530 (v01 A M I  AMI SRAT 00000001 AMI. 00000000)
[    0.000000] ACPI: SLIT 0x00000000AB70A6D0 000030 (v01 A M I  AMI SLIT 00000000 AMI. 00000000)
[    0.000000] ACPI: HPET 0x00000000AB70A700 000038 (v01 HPQOEM SLIC-WKS 01072009 AMI. 00000005)
[    0.000000] ACPI: UEFI 0x00000000AB70A738 00012A (v01 INTEL  RstScuO  00000000      00000000)
[    0.000000] ACPI: SSDT 0x00000000AB70A868 005913 (v01 COMPAQ WMI      00000001 MSFT 03000001)
[    0.000000] ACPI: SLIC 0x00000000AB710180 000176 (v01 HPQOEM SLIC-WKS 00000001      00000000)
[    0.000000] ACPI: SSDT 0x00000000AB7102F8 002A71 (v02 HPQOEM CpuDef   00004000 INTL 20051117)
[    0.000000] ACPI: SSDT 0x00000000AB712D70 0CD380 (v02 INTEL  CpuPm    00004000 INTL 20051117)
[    0.000000] ACPI: ASF! 0x00000000AB7E00F0 0000A5 (v32 INTEL   HCG     00000001 TFSM 000F4240)
[    0.000000] ACPI: TCPA 0x00000000AB7E0198 000032 (v02 APTIO4 NAPAASF  00000001 MSFT 01000013)
[    0.000000] ACPI: UEFI 0x00000000AB7E01D0 000042 (v01 HPQOEM SLIC-WKS 01072009      00000000)
[    0.000000] ACPI: UEFI 0x00000000AB7E0218 00005C (v01 INTEL  RstScuV  00000000      00000000)
[    0.000000] ACPI: VFCT 0x00000000AB7E0278 00E884 (v01 HPQOEM SLIC-WKS 00000001 AMD  31504F47)
[    0.000000] ACPI: DMAR 0x00000000AB7EEB00 000100 (v01 A M I  OEMDMAR  00000001 INTL 00000001)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] SRAT: PXM 0 -> APIC 0x00 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x01 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x02 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x03 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x04 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x05 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x06 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x07 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x08 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x09 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x10 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x11 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x12 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x13 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x14 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x15 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x16 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x17 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x18 -> Node 0
[    0.000000] SRAT: PXM 0 -> APIC 0x19 -> Node 0
[    0.000000] SRAT: PXM 1 -> APIC 0x20 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x21 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x22 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x23 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x24 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x25 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x26 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x27 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x28 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x29 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x30 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x31 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x32 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x33 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x34 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x35 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x36 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x37 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x38 -> Node 1
[    0.000000] SRAT: PXM 1 -> APIC 0x39 -> Node 1
[    0.000000] ACPI: SRAT: Node 0 PXM 0 [mem 0x00000000-0xafffffff]
[    0.000000] ACPI: SRAT: Node 0 PXM 0 [mem 0x100000000-0x84fffffff]
[    0.000000] ACPI: SRAT: Node 1 PXM 1 [mem 0x850000000-0x104fffffff]
[    0.000000] NUMA: Initialized distance table, cnt=2
[    0.000000] NUMA: Node 0 [mem 0x00000000-0xafffffff] + [mem 0x100000000-0x84fffffff] -> [mem 0x00000000-0x84fffffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x84ffd5000-0x84fffffff]
[    0.000000] NODE_DATA(1) allocated [mem 0x104ffd4000-0x104fffefff]
[    0.000000] tsc: Fast TSC calibration using PIT
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000104fffffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x000000000009ffff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x00000000ab3c6fff]
[    0.000000]   node   0: [mem 0x00000000abb0f000-0x00000000abb0ffff]
[    0.000000]   node   0: [mem 0x00000000abb96000-0x00000000abffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000084fffffff]
[    0.000000]   node   1: [mem 0x0000000850000000-0x000000104fffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x000000084fffffff]
[    0.000000] On node 0 totalpages: 8370129
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 40 pages reserved
[    0.000000]   DMA zone: 3999 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 10913 pages used for memmap
[    0.000000]   DMA32 zone: 698418 pages, LIFO batch:31
[    0.000000]   Normal zone: 119808 pages used for memmap
[    0.000000]   Normal zone: 7667712 pages, LIFO batch:31
[    0.000000] Initmem setup node 1 [mem 0x0000000850000000-0x000000104fffffff]
[    0.000000] On node 1 totalpages: 8388608
[    0.000000]   Normal zone: 131072 pages used for memmap
[    0.000000]   Normal zone: 8388608 pages, LIFO batch:31
[    0.000000] Reserved but unavailable: 97 pages
[    0.000000] ACPI: PM-Timer IO Port: 0x408
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x00] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x06] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x08] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0a] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0c] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0e] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x10] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x12] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x14] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x16] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x18] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x1a] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x1c] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x1e] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x20] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x22] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x24] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x26] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x05] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x07] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x09] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0b] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0d] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x0f] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x11] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x13] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x15] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x17] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x19] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x1b] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x1d] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x1f] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x21] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x23] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x25] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x27] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 0, version 32, address 0xfec00000, GSI 0-23
[    0.000000] IOAPIC[1]: apic_id 2, version 32, address 0xfec01000, GSI 24-47
[    0.000000] IOAPIC[2]: apic_id 3, version 32, address 0xfec40000, GSI 48-71
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x8086a701 base: 0xfed00000
[    0.000000] smpboot: Allowing 40 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xab3c7000-0xab6c6fff]
[    0.000000] PM: Registered nosave memory: [mem 0xab6c7000-0xab7eefff]
[    0.000000] PM: Registered nosave memory: [mem 0xab7ef000-0xab9e4fff]
[    0.000000] PM: Registered nosave memory: [mem 0xab9e5000-0xababbfff]
[    0.000000] PM: Registered nosave memory: [mem 0xababc000-0xabb0efff]
[    0.000000] PM: Registered nosave memory: [mem 0xabb10000-0xabb95fff]
[    0.000000] PM: Registered nosave memory: [mem 0xac000000-0xefffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf0000000-0xf7ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf8000000-0xfed1bfff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed1c000-0xfed3ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed40000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] e820: [mem 0xac000000-0xefffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] random: get_random_bytes called from start_kernel+0x99/0x4fd with crng_init=0
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:40 nr_cpu_ids:40 nr_node_ids:2
[    0.000000] percpu: Embedded 46 pages/cpu @        (ptrval) s151552 r8192 d28672 u262144
[    0.000000] pcpu-alloc: s151552 r8192 d28672 u262144 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 00 01 02 03 04 05 06 07 [0] 08 09 20 21 22 23 24 25 
[    0.000000] pcpu-alloc: [0] 26 27 28 29 -- -- -- -- [1] 10 11 12 13 14 15 16 17 
[    0.000000] pcpu-alloc: [1] 18 19 30 31 32 33 34 35 [1] 36 37 38 39 -- -- -- -- 
[    0.000000] Built 2 zonelists, mobility grouping on.  Total pages: 16496840
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-30-generic root=UUID=7cc57c85-4008-465f-ade9-dffcb3a2a5c0 ro quiet splash vt.handoff=1
[    0.000000] log_buf_len individual max cpu contribution: 4096 bytes
[    0.000000] log_buf_len total cpu_extra contributions: 159744 bytes
[    0.000000] log_buf_len min size: 262144 bytes
[    0.000000] log_buf_len: 524288 bytes
[    0.000000] early log buf free: 245280(93%)
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 65729824K/67034948K available (12300K kernel code, 2470K rwdata, 4240K rodata, 2408K init, 2416K bss, 1305124K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=40, Nodes=2
[    0.000000] Kernel/User page tables isolation: enabled
[    0.000000] ftrace: allocating 39093 entries in 153 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000]  RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=40.
[    0.000000]  Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=40
[    0.000000] NR_IRQS: 524544, nr_irqs: 1560, preallocated irqs: 16
[    0.000000] vt handoff: transparent VT on vt#1
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] mempolicy: Enabling automatic NUMA balancing. Configure with numa_balancing= or the kernel.numa_balancing sysctl
[    0.000000] ACPI: Core revision 20170831
[    0.000000] ACPI: 4 ACPI AML tables successfully acquired and loaded
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484882848 ns
[    0.000000] hpet clockevent registered
[    0.000000] APIC: Switch to symmetric I/O mode setup
[    0.000000] DMAR: Host address width 46
[    0.000000] DMAR: DRHD base: 0x000000fbf20000 flags: 0x0
[    0.000000] DMAR: dmar0: reg_base_addr fbf20000 ver 1:0 cap d2078c106f0466 ecap f020df
[    0.000000] DMAR: DRHD base: 0x000000ef644000 flags: 0x1
[    0.000000] DMAR: dmar1: reg_base_addr ef644000 ver 1:0 cap d2078c106f0466 ecap f020df
[    0.000000] DMAR: RMRR base: 0x000000ab694000 end: 0x000000ab6c2fff
[    0.000000] DMAR: ATSR flags: 0x0
[    0.000000] DMAR-IR: IOAPIC id 3 under DRHD base  0xfbf20000 IOMMU 0
[    0.000000] DMAR-IR: IOAPIC id 0 under DRHD base  0xef644000 IOMMU 1
[    0.000000] DMAR-IR: IOAPIC id 2 under DRHD base  0xef644000 IOMMU 1
[    0.000000] DMAR-IR: HPET id 0 under DRHD base 0xef644000
[    0.000000] DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
[    0.000000] DMAR-IR: Enabled IRQ remapping in x2apic mode
[    0.000000] x2apic enabled
[    0.000000] Switched APIC routing to cluster x2apic.
[    0.000000] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.020000] tsc: Fast TSC calibration using PIT
[    0.024000] tsc: Detected 2793.145 MHz processor
[    0.024000] Calibrating delay loop (skipped), value calculated using timer frequency.. 5586.29 BogoMIPS (lpj=11172580)
[    0.024000] pid_max: default: 40960 minimum: 320
[    0.024000] Security Framework initialized
[    0.024000] Yama: becoming mindful.
[    0.024000] AppArmor: AppArmor initialized
[    0.041164] Dentry cache hash table entries: 8388608 (order: 14, 67108864 bytes)
[    0.047979] Inode-cache hash table entries: 4194304 (order: 13, 33554432 bytes)
[    0.048227] Mount-cache hash table entries: 131072 (order: 8, 1048576 bytes)
[    0.048437] Mountpoint-cache hash table entries: 131072 (order: 8, 1048576 bytes)
[    0.048793] CPU: Physical Processor ID: 0
[    0.048793] CPU: Processor Core ID: 0
[    0.048799] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.048799] ENERGY_PERF_BIAS: View and update with x86_energy_perf_policy(8)
[    0.048804] mce: CPU supports 27 MCE banks
[    0.048829] CPU0: Thermal monitoring enabled (TM1)
[    0.048873] process: using mwait in idle threads
[    0.048875] Last level iTLB entries: 4KB 512, 2MB 8, 4MB 8
[    0.048876] Last level dTLB entries: 4KB 512, 2MB 0, 4MB 0, 1GB 4
[    0.048878] Spectre V2 : Mitigation: Full generic retpoline
[    0.048878] Spectre V2 : Spectre v2 mitigation: Enabling Indirect Branch Prediction Barrier
[    0.048879] Spectre V2 : Enabling Restricted Speculation for firmware calls
[    0.048880] Speculative Store Bypass: Vulnerable
[    0.049454] Freeing SMP alternatives memory: 36K
[    0.054175] TSC deadline timer enabled
[    0.054180] smpboot: CPU0: Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz (family: 0x6, model: 0x3e, stepping: 0x4)
[    0.054318] Performance Events: PEBS fmt1+, IvyBridge events, 16-deep LBR, full-width counters, Intel PMU driver.
[    0.054340] ... version:                3
[    0.054340] ... bit width:              48
[    0.054341] ... generic registers:      4
[    0.054342] ... value mask:             0000ffffffffffff
[    0.054342] ... max period:             00007fffffffffff
[    0.054343] ... fixed-purpose events:   3
[    0.054343] ... event mask:             000000070000000f
[    0.054407] Hierarchical SRCU implementation.
[    0.056000] smp: Bringing up secondary CPUs ...
[    0.056000] x86: Booting SMP configuration:
[    0.056000] .... node  #0, CPUs:        #1
[    0.064256] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.064279]   #2  #3  #4  #5  #6  #7  #8  #9
[    0.096191] .... node  #1, CPUs:   #10 #11 #12 #13 #14 #15 #16 #17 #18 #19
[    0.216151] .... node  #0, CPUs:   #20 #21 #22 #23 #24 #25 #26 #27 #28 #29
[    0.243046] .... node  #1, CPUs:   #30 #31 #32 #33 #34 #35 #36 #37 #38 #39
[    0.284149] smp: Brought up 2 nodes, 40 CPUs
[    0.284149] smpboot: Max logical packages: 2
[    0.284149] smpboot: Total of 40 processors activated (223490.92 BogoMIPS)
[    0.291302] devtmpfs: initialized
[    0.291302] x86/mm: Memory block size: 2048MB
[    0.292038] evm: security.selinux
[    0.292039] evm: security.SMACK64
[    0.292039] evm: security.SMACK64EXEC
[    0.292040] evm: security.SMACK64TRANSMUTE
[    0.292040] evm: security.SMACK64MMAP
[    0.292041] evm: security.apparmor
[    0.292042] evm: security.ima
[    0.292042] evm: security.capability
[    0.292079] PM: Registering ACPI NVS region [mem 0xab7ef000-0xab9e4fff] (2056192 bytes)
[    0.292079] PM: Registering ACPI NVS region [mem 0xabb10000-0xabb95fff] (548864 bytes)
[    0.292221] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.292221] futex hash table entries: 16384 (order: 8, 1048576 bytes)
[    0.292532] pinctrl core: initialized pinctrl subsystem
[    0.292654] RTC time:  6:23:27, date: 08/19/18
[    0.295024] NET: Registered protocol family 16
[    0.295139] audit: initializing netlink subsys (disabled)
[    0.295145] audit: type=2000 audit(1534659807.292:1): state=initialized audit_enabled=0 res=1
[    0.295145] cpuidle: using governor ladder
[    0.295145] cpuidle: using governor menu
[    0.295145] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.295145] ACPI: bus type PCI registered
[    0.295145] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.295145] PCI: MMCONFIG for domain 0000 [bus 00-7f] at [mem 0xf0000000-0xf7ffffff] (base 0xf0000000)
[    0.295145] PCI: MMCONFIG at [mem 0xf0000000-0xf7ffffff] reserved in E820
[    0.295145] PCI: Using configuration type 1 for base access
[    0.296029] core: PMU erratum BJ122, BV98, HSD29 worked around, HT is on
[    0.300087] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.300087] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.300243] ACPI: Added _OSI(Module Device)
[    0.300244] ACPI: Added _OSI(Processor Device)
[    0.300244] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.300245] ACPI: Added _OSI(Processor Aggregator Device)
[    0.300246] ACPI: Added _OSI(Linux-Dell-Video)
[    0.300452] ACPI: Executed 1 blocks of module-level executable AML code
[    0.549094] ACPI: Interpreter enabled
[    0.549111] ACPI: (supports S0 S3 S4 S5)
[    0.549113] ACPI: Using IOAPIC for interrupt routing
[    0.549146] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.549476] ACPI: Enabled 5 GPEs in block 00 to 3F
[    0.571041] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-3f])
[    0.571046] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.571241] acpi PNP0A08:00: _OSC: platform does not support [PCIeCapability]
[    0.571333] acpi PNP0A08:00: _OSC: not requesting control; platform does not support [PCIeCapability]
[    0.571336] acpi PNP0A08:00: _OSC: OS requested [PCIeHotplug PME AER PCIeCapability]
[    0.571337] acpi PNP0A08:00: _OSC: platform willing to grant [PCIeHotplug PME AER]
[    0.571339] acpi PNP0A08:00: _OSC failed (AE_SUPPORT); disabling ASPM
[    0.571838] PCI host bridge to bus 0000:00
[    0.571840] pci_bus 0000:00: root bus resource [io  0x0000-0x03af window]
[    0.571841] pci_bus 0000:00: root bus resource [io  0x03e0-0x0cf7 window]
[    0.571843] pci_bus 0000:00: root bus resource [io  0x03b0-0x03df window]
[    0.571845] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.571847] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.571849] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000dffff window]
[    0.571850] pci_bus 0000:00: root bus resource [mem 0xb0000000-0xefffffff window]
[    0.571851] pci_bus 0000:00: root bus resource [mem 0x380000000000-0x38007fffffff window]
[    0.571853] pci_bus 0000:00: root bus resource [bus 00-3f]
[    0.571865] pci 0000:00:00.0: [8086:0e00] type 00 class 0x060000
[    0.571939] pci 0000:00:00.0: PME# supported from D0 D3hot D3cold
[    0.572027] pci 0000:00:01.0: [8086:0e02] type 01 class 0x060400
[    0.572115] pci 0000:00:01.0: PME# supported from D0 D3hot D3cold
[    0.572215] pci 0000:00:02.0: [8086:0e04] type 01 class 0x060400
[    0.572295] pci 0000:00:02.0: PME# supported from D0 D3hot D3cold
[    0.572391] pci 0000:00:03.0: [8086:0e08] type 01 class 0x060400
[    0.572429] pci 0000:00:03.0: enabling Extended Tags
[    0.572477] pci 0000:00:03.0: PME# supported from D0 D3hot D3cold
[    0.572572] pci 0000:00:04.0: [8086:0e20] type 00 class 0x088000
[    0.572591] pci 0000:00:04.0: reg 0x10: [mem 0xef63c000-0xef63ffff 64bit]
[    0.572717] pci 0000:00:04.1: [8086:0e21] type 00 class 0x088000
[    0.572734] pci 0000:00:04.1: reg 0x10: [mem 0xef638000-0xef63bfff 64bit]
[    0.572859] pci 0000:00:04.2: [8086:0e22] type 00 class 0x088000
[    0.572877] pci 0000:00:04.2: reg 0x10: [mem 0xef634000-0xef637fff 64bit]
[    0.573008] pci 0000:00:04.3: [8086:0e23] type 00 class 0x088000
[    0.573026] pci 0000:00:04.3: reg 0x10: [mem 0xef630000-0xef633fff 64bit]
[    0.573151] pci 0000:00:04.4: [8086:0e24] type 00 class 0x088000
[    0.573168] pci 0000:00:04.4: reg 0x10: [mem 0xef62c000-0xef62ffff 64bit]
[    0.573298] pci 0000:00:04.5: [8086:0e25] type 00 class 0x088000
[    0.573316] pci 0000:00:04.5: reg 0x10: [mem 0xef628000-0xef62bfff 64bit]
[    0.573445] pci 0000:00:04.6: [8086:0e26] type 00 class 0x088000
[    0.573463] pci 0000:00:04.6: reg 0x10: [mem 0xef624000-0xef627fff 64bit]
[    0.573592] pci 0000:00:04.7: [8086:0e27] type 00 class 0x088000
[    0.573610] pci 0000:00:04.7: reg 0x10: [mem 0xef620000-0xef623fff 64bit]
[    0.573733] pci 0000:00:05.0: [8086:0e28] type 00 class 0x088000
[    0.573861] pci 0000:00:05.2: [8086:0e2a] type 00 class 0x088000
[    0.573986] pci 0000:00:05.4: [8086:0e2c] type 00 class 0x080020
[    0.573999] pci 0000:00:05.4: reg 0x10: [mem 0xef64a000-0xef64afff]
[    0.574134] pci 0000:00:11.0: [8086:1d3e] type 01 class 0x060400
[    0.574235] pci 0000:00:11.0: PME# supported from D0 D3hot D3cold
[    0.574336] pci 0000:00:16.0: [8086:1d3a] type 00 class 0x078000
[    0.574360] pci 0000:00:16.0: reg 0x10: [mem 0xef649000-0xef64900f 64bit]
[    0.574433] pci 0000:00:16.0: PME# supported from D0 D3hot D3cold
[    0.574505] pci 0000:00:16.2: [8086:1d3c] type 00 class 0x010185
[    0.574524] pci 0000:00:16.2: reg 0x10: [io  0xe0b0-0xe0b7]
[    0.574534] pci 0000:00:16.2: reg 0x14: [io  0xe0a0-0xe0a3]
[    0.574543] pci 0000:00:16.2: reg 0x18: [io  0xe090-0xe097]
[    0.574552] pci 0000:00:16.2: reg 0x1c: [io  0xe080-0xe083]
[    0.574560] pci 0000:00:16.2: reg 0x20: [io  0xe070-0xe07f]
[    0.574673] pci 0000:00:16.3: [8086:1d3d] type 00 class 0x070002
[    0.574691] pci 0000:00:16.3: reg 0x10: [io  0xe060-0xe067]
[    0.574698] pci 0000:00:16.3: reg 0x14: [mem 0xef647000-0xef647fff]
[    0.574833] pci 0000:00:19.0: [8086:1502] type 00 class 0x020000
[    0.574851] pci 0000:00:19.0: reg 0x10: [mem 0xef600000-0xef61ffff]
[    0.574859] pci 0000:00:19.0: reg 0x14: [mem 0xef64d000-0xef64dfff]
[    0.574867] pci 0000:00:19.0: reg 0x18: [io  0xe040-0xe05f]
[    0.574925] pci 0000:00:19.0: PME# supported from D0 D3hot D3cold
[    0.575001] pci 0000:00:1a.0: [8086:1d2d] type 00 class 0x0c0320
[    0.575022] pci 0000:00:1a.0: reg 0x10: [mem 0xef64f000-0xef64f3ff]
[    0.575103] pci 0000:00:1a.0: PME# supported from D0 D3hot D3cold
[    0.575183] pci 0000:00:1b.0: [8086:1d20] type 00 class 0x040300
[    0.575202] pci 0000:00:1b.0: reg 0x10: [mem 0xef640000-0xef643fff 64bit]
[    0.575264] pci 0000:00:1b.0: PME# supported from D0 D3hot D3cold
[    0.575340] pci 0000:00:1c.0: [8086:1d12] type 01 class 0x060400
[    0.575421] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.575515] pci 0000:00:1c.5: [8086:1d18] type 01 class 0x060400
[    0.575597] pci 0000:00:1c.5: PME# supported from D0 D3hot D3cold
[    0.575691] pci 0000:00:1c.6: [8086:1d14] type 01 class 0x060400
[    0.575773] pci 0000:00:1c.6: PME# supported from D0 D3hot D3cold
[    0.575858] pci 0000:00:1c.7: [8086:1d16] type 01 class 0x060400
[    0.575939] pci 0000:00:1c.7: PME# supported from D0 D3hot D3cold
[    0.576032] pci 0000:00:1d.0: [8086:1d26] type 00 class 0x0c0320
[    0.576053] pci 0000:00:1d.0: reg 0x10: [mem 0xef64e000-0xef64e3ff]
[    0.576136] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
[    0.576214] pci 0000:00:1e.0: [8086:244e] type 01 class 0x060401
[    0.576332] pci 0000:00:1f.0: [8086:1d41] type 00 class 0x060100
[    0.576508] pci 0000:00:1f.2: [8086:1d02] type 00 class 0x010601
[    0.576525] pci 0000:00:1f.2: reg 0x10: [io  0xe0f0-0xe0f7]
[    0.576533] pci 0000:00:1f.2: reg 0x14: [io  0xe0e0-0xe0e3]
[    0.576541] pci 0000:00:1f.2: reg 0x18: [io  0xe0d0-0xe0d7]
[    0.576548] pci 0000:00:1f.2: reg 0x1c: [io  0xe0c0-0xe0c3]
[    0.576555] pci 0000:00:1f.2: reg 0x20: [io  0xe020-0xe03f]
[    0.576562] pci 0000:00:1f.2: reg 0x24: [mem 0xef64c000-0xef64c7ff]
[    0.576601] pci 0000:00:1f.2: PME# supported from D3hot
[    0.576672] pci 0000:00:1f.3: [8086:1d22] type 00 class 0x0c0500
[    0.576689] pci 0000:00:1f.3: reg 0x10: [mem 0xef64b000-0xef64b0ff 64bit]
[    0.576708] pci 0000:00:1f.3: reg 0x20: [io  0xe000-0xe01f]
[    0.576848] pci 0000:00:01.0: PCI bridge to [bus 03]
[    0.576915] pci 0000:07:00.0: [10de:0ffe] type 00 class 0x030000
[    0.576931] pci 0000:07:00.0: reg 0x10: [mem 0xee000000-0xeeffffff]
[    0.576940] pci 0000:07:00.0: reg 0x14: [mem 0xb0000000-0xbfffffff 64bit pref]
[    0.576949] pci 0000:07:00.0: reg 0x1c: [mem 0xc0000000-0xc1ffffff 64bit pref]
[    0.576955] pci 0000:07:00.0: reg 0x24: [io  0xa000-0xa07f]
[    0.576961] pci 0000:07:00.0: reg 0x30: [mem 0xef000000-0xef07ffff pref]
[    0.576967] pci 0000:07:00.0: enabling Extended Tags
[    0.576976] pci 0000:07:00.0: BAR 1: assigned to efifb
[    0.577064] pci 0000:07:00.1: [10de:0e1b] type 00 class 0x040300
[    0.577076] pci 0000:07:00.1: reg 0x10: [mem 0xef080000-0xef083fff]
[    0.577102] pci 0000:07:00.1: enabling Extended Tags
[    0.577183] pci 0000:00:02.0: PCI bridge to [bus 07]
[    0.577186] pci 0000:00:02.0:   bridge window [io  0xa000-0xafff]
[    0.577189] pci 0000:00:02.0:   bridge window [mem 0xee000000-0xef0fffff]
[    0.577195] pci 0000:00:02.0:   bridge window [mem 0xb0000000-0xc1ffffff 64bit pref]
[    0.577258] pci 0000:04:00.0: [1022:1470] type 01 class 0x060400
[    0.577274] pci 0000:04:00.0: reg 0x10: [mem 0xef200000-0xef203fff]
[    0.577292] pci 0000:04:00.0: enabling Extended Tags
[    0.577333] pci 0000:04:00.0: PME# supported from D0 D3hot D3cold
[    0.577402] pci 0000:00:03.0: PCI bridge to [bus 04-06]
[    0.577405] pci 0000:00:03.0:   bridge window [io  0xb000-0xbfff]
[    0.577408] pci 0000:00:03.0:   bridge window [mem 0xef100000-0xef2fffff]
[    0.577413] pci 0000:00:03.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.577452] pci 0000:05:00.0: [1022:1471] type 01 class 0x060400
[    0.577484] pci 0000:05:00.0: enabling Extended Tags
[    0.577522] pci 0000:05:00.0: PME# supported from D0 D3hot D3cold
[    0.577580] pci 0000:04:00.0: PCI bridge to [bus 05-06]
[    0.577584] pci 0000:04:00.0:   bridge window [io  0xb000-0xbfff]
[    0.577587] pci 0000:04:00.0:   bridge window [mem 0xef100000-0xef1fffff]
[    0.577591] pci 0000:04:00.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.577629] pci 0000:06:00.0: [1002:6863] type 00 class 0x030000
[    0.577649] pci 0000:06:00.0: reg 0x10: [mem 0xd0000000-0xdfffffff 64bit pref]
[    0.577658] pci 0000:06:00.0: reg 0x18: [mem 0xe0000000-0xe01fffff 64bit pref]
[    0.577665] pci 0000:06:00.0: reg 0x20: [io  0xb000-0xb0ff]
[    0.577671] pci 0000:06:00.0: reg 0x24: [mem 0xef100000-0xef17ffff]
[    0.577678] pci 0000:06:00.0: reg 0x30: [mem 0xef180000-0xef19ffff pref]
[    0.577682] pci 0000:06:00.0: enabling Extended Tags
[    0.577728] pci 0000:06:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.577785] pci 0000:06:00.1: [1002:aaf8] type 00 class 0x040300
[    0.577797] pci 0000:06:00.1: reg 0x10: [mem 0xef1a0000-0xef1a3fff]
[    0.577822] pci 0000:06:00.1: enabling Extended Tags
[    0.577859] pci 0000:06:00.1: PME# supported from D1 D2 D3hot D3cold
[    0.577926] pci 0000:05:00.0: PCI bridge to [bus 06]
[    0.577930] pci 0000:05:00.0:   bridge window [io  0xb000-0xbfff]
[    0.577934] pci 0000:05:00.0:   bridge window [mem 0xef100000-0xef1fffff]
[    0.577938] pci 0000:05:00.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.578015] pci 0000:02:00.0: [8086:1d6b] type 00 class 0x010700
[    0.578045] pci 0000:02:00.0: reg 0x10: [mem 0xe0800000-0xe0803fff 64bit pref]
[    0.578059] pci 0000:02:00.0: reg 0x18: [mem 0xe0400000-0xe07fffff 64bit pref]
[    0.578069] pci 0000:02:00.0: reg 0x20: [io  0xc000-0xc0ff]
[    0.578093] pci 0000:02:00.0: enabling Extended Tags
[    0.578183] pci 0000:02:00.0: reg 0x164: [mem 0x380000000000-0x380000003fff 64bit pref]
[    0.578186] pci 0000:02:00.0: VF(n) BAR0 space: [mem 0x380000000000-0x38000007bfff 64bit pref] (contains BAR0 for 31 VFs)
[    0.578389] pci 0000:00:11.0: PCI bridge to [bus 02]
[    0.578393] pci 0000:00:11.0:   bridge window [io  0xc000-0xcfff]
[    0.578402] pci 0000:00:11.0:   bridge window [mem 0xe0400000-0xe08fffff 64bit pref]
[    0.578485] pci 0000:01:00.0: [8086:10d3] type 00 class 0x020000
[    0.578533] pci 0000:01:00.0: reg 0x10: [mem 0xef500000-0xef51ffff]
[    0.578570] pci 0000:01:00.0: reg 0x18: [io  0xd000-0xd01f]
[    0.578589] pci 0000:01:00.0: reg 0x1c: [mem 0xef520000-0xef523fff]
[    0.578768] pci 0000:01:00.0: PME# supported from D0 D3hot D3cold
[    0.588025] pci 0000:00:1c.0: PCI bridge to [bus 01]
[    0.588029] pci 0000:00:1c.0:   bridge window [io  0xd000-0xdfff]
[    0.588033] pci 0000:00:1c.0:   bridge window [mem 0xef500000-0xef5fffff]
[    0.588099] pci 0000:00:1c.5: PCI bridge to [bus 08]
[    0.588164] pci 0000:00:1c.6: PCI bridge to [bus 09]
[    0.588243] pci 0000:0a:00.0: [104c:8241] type 00 class 0x0c0330
[    0.588281] pci 0000:0a:00.0: reg 0x10: [mem 0xef400000-0xef40ffff 64bit]
[    0.588300] pci 0000:0a:00.0: reg 0x18: [mem 0xef410000-0xef411fff 64bit]
[    0.588417] pci 0000:0a:00.0: supports D1 D2
[    0.588419] pci 0000:0a:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.600021] pci 0000:00:1c.7: PCI bridge to [bus 0a]
[    0.600027] pci 0000:00:1c.7:   bridge window [mem 0xef400000-0xef4fffff]
[    0.600086] pci 0000:0b:05.0: [11c1:5811] type 00 class 0x0c0010
[    0.600103] pci 0000:0b:05.0: reg 0x10: [mem 0xef300000-0xef300fff]
[    0.600163] pci 0000:0b:05.0: supports D1 D2
[    0.600165] pci 0000:0b:05.0: PME# supported from D0 D1 D2 D3hot
[    0.600243] pci 0000:00:1e.0: PCI bridge to [bus 0b] (subtractive decode)
[    0.600248] pci 0000:00:1e.0:   bridge window [mem 0xef300000-0xef3fffff]
[    0.600255] pci 0000:00:1e.0:   bridge window [io  0x0000-0x03af window] (subtractive decode)
[    0.600257] pci 0000:00:1e.0:   bridge window [io  0x03e0-0x0cf7 window] (subtractive decode)
[    0.600258] pci 0000:00:1e.0:   bridge window [io  0x03b0-0x03df window] (subtractive decode)
[    0.600260] pci 0000:00:1e.0:   bridge window [io  0x0d00-0xffff window] (subtractive decode)
[    0.600261] pci 0000:00:1e.0:   bridge window [mem 0x000a0000-0x000bffff window] (subtractive decode)
[    0.600262] pci 0000:00:1e.0:   bridge window [mem 0x000c0000-0x000dffff window] (subtractive decode)
[    0.600264] pci 0000:00:1e.0:   bridge window [mem 0xb0000000-0xefffffff window] (subtractive decode)
[    0.600265] pci 0000:00:1e.0:   bridge window [mem 0x380000000000-0x38007fffffff window] (subtractive decode)
[    0.600314] pci_bus 0000:00: on NUMA node 0
[    0.601094] ACPI: PCI Root Bridge [PCI1] (domain 0000 [bus 40-7f])
[    0.601098] acpi PNP0A08:01: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.601290] acpi PNP0A08:01: _OSC: platform does not support [PCIeCapability]
[    0.601382] acpi PNP0A08:01: _OSC: not requesting control; platform does not support [PCIeCapability]
[    0.601384] acpi PNP0A08:01: _OSC: OS requested [PCIeHotplug PME AER PCIeCapability]
[    0.601386] acpi PNP0A08:01: _OSC: platform willing to grant [PCIeHotplug PME AER]
[    0.601387] acpi PNP0A08:01: _OSC failed (AE_SUPPORT); disabling ASPM
[    0.601691] PCI host bridge to bus 0000:40
[    0.601693] pci_bus 0000:40: root bus resource [io  0x0000-0x03af window]
[    0.601694] pci_bus 0000:40: root bus resource [io  0x03e0-0x0cf7 window]
[    0.601696] pci_bus 0000:40: root bus resource [mem 0x000c0000-0x000dffff window]
[    0.601697] pci_bus 0000:40: root bus resource [mem 0xf8000000-0xfbffffff window]
[    0.601698] pci_bus 0000:40: root bus resource [mem 0x381000000000-0x38107fffffff window]
[    0.601700] pci_bus 0000:40: root bus resource [bus 40-7f]
[    0.601713] pci 0000:40:04.0: [8086:0e20] type 00 class 0x088000
[    0.601733] pci 0000:40:04.0: reg 0x10: [mem 0xfbf1c000-0xfbf1ffff 64bit]
[    0.601845] pci 0000:40:04.1: [8086:0e21] type 00 class 0x088000
[    0.601865] pci 0000:40:04.1: reg 0x10: [mem 0xfbf18000-0xfbf1bfff 64bit]
[    0.601975] pci 0000:40:04.2: [8086:0e22] type 00 class 0x088000
[    0.601995] pci 0000:40:04.2: reg 0x10: [mem 0xfbf14000-0xfbf17fff 64bit]
[    0.602108] pci 0000:40:04.3: [8086:0e23] type 00 class 0x088000
[    0.602128] pci 0000:40:04.3: reg 0x10: [mem 0xfbf10000-0xfbf13fff 64bit]
[    0.602236] pci 0000:40:04.4: [8086:0e24] type 00 class 0x088000
[    0.602255] pci 0000:40:04.4: reg 0x10: [mem 0xfbf0c000-0xfbf0ffff 64bit]
[    0.602364] pci 0000:40:04.5: [8086:0e25] type 00 class 0x088000
[    0.602383] pci 0000:40:04.5: reg 0x10: [mem 0xfbf08000-0xfbf0bfff 64bit]
[    0.602495] pci 0000:40:04.6: [8086:0e26] type 00 class 0x088000
[    0.602515] pci 0000:40:04.6: reg 0x10: [mem 0xfbf04000-0xfbf07fff 64bit]
[    0.602631] pci 0000:40:04.7: [8086:0e27] type 00 class 0x088000
[    0.602651] pci 0000:40:04.7: reg 0x10: [mem 0xfbf00000-0xfbf03fff 64bit]
[    0.602759] pci 0000:40:05.0: [8086:0e28] type 00 class 0x088000
[    0.602863] pci 0000:40:05.2: [8086:0e2a] type 00 class 0x088000
[    0.602972] pci 0000:40:05.4: [8086:0e2c] type 00 class 0x080020
[    0.602987] pci 0000:40:05.4: reg 0x10: [mem 0xfbf22000-0xfbf22fff]
[    0.603108] pci_bus 0000:40: on NUMA node 1
[    0.603222] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 7 10 *11 12 14 15)
[    0.603288] ACPI: PCI Interrupt Link [LNKB] (IRQs *3 4 5 6 7 10 11 12 14 15)
[    0.603351] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.603414] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 *4 5 6 10 11 12 14 15)
[    0.603476] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 *5 6 7 10 11 12 14 15)
[    0.603539] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 7 10 11 12 14 15) *0
[    0.603603] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 *7 10 11 12 14 15)
[    0.603667] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 7 *10 11 12 14 15)
[    0.607639] SCSI subsystem initialized
[    0.607705] libata version 3.00 loaded.
[    0.607705] pci 0000:07:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    0.607705] pci 0000:06:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    0.607705] pci 0000:06:00.0: vgaarb: bridge control possible
[    0.607705] pci 0000:07:00.0: vgaarb: bridge control possible
[    0.607705] pci 0000:07:00.0: vgaarb: setting as boot device
[    0.607705] vgaarb: loaded
[    0.607705] ACPI: bus type USB registered
[    0.607705] usbcore: registered new interface driver usbfs
[    0.607705] usbcore: registered new interface driver hub
[    0.607705] usbcore: registered new device driver usb
[    0.608064] EDAC MC: Ver: 3.0.0
[    0.608207] Registered efivars operations
[    0.618479] PCI: Using ACPI for IRQ routing
[    0.618479] PCI: Discovered peer bus 3f
[    0.618479] PCI: root bus 3f: using default resources
[    0.618479] PCI: Probing PCI hardware (bus 3f)
[    0.618479] PCI host bridge to bus 0000:3f
[    0.618479] pci_bus 0000:3f: root bus resource [io  0x0000-0xffff]
[    0.618479] pci_bus 0000:3f: root bus resource [mem 0x00000000-0x3fffffffffff]
[    0.618479] pci_bus 0000:3f: No busn resource found for root bus, will use [bus 3f-ff]
[    0.618479] pci_bus 0000:3f: busn_res: can not insert [bus 3f-ff] under domain [bus 00-ff] (conflicts with (null) [bus 00-3f])
[    0.618479] pci 0000:3f:08.0: [8086:0e80] type 00 class 0x088000
[    0.618479] pci 0000:3f:09.0: [8086:0e90] type 00 class 0x088000
[    0.618479] pci 0000:3f:0a.0: [8086:0ec0] type 00 class 0x088000
[    0.620036] pci 0000:3f:0a.1: [8086:0ec1] type 00 class 0x088000
[    0.620077] pci 0000:3f:0a.2: [8086:0ec2] type 00 class 0x088000
[    0.620127] pci 0000:3f:0a.3: [8086:0ec3] type 00 class 0x088000
[    0.620170] pci 0000:3f:0b.0: [8086:0e1e] type 00 class 0x088000
[    0.620209] pci 0000:3f:0b.3: [8086:0e1f] type 00 class 0x088000
[    0.620253] pci 0000:3f:0c.0: [8086:0ee0] type 00 class 0x088000
[    0.620292] pci 0000:3f:0c.1: [8086:0ee2] type 00 class 0x088000
[    0.620331] pci 0000:3f:0c.2: [8086:0ee4] type 00 class 0x088000
[    0.620372] pci 0000:3f:0c.3: [8086:0ee6] type 00 class 0x088000
[    0.620411] pci 0000:3f:0c.4: [8086:0ee8] type 00 class 0x088000
[    0.620450] pci 0000:3f:0d.0: [8086:0ee1] type 00 class 0x088000
[    0.620492] pci 0000:3f:0d.1: [8086:0ee3] type 00 class 0x088000
[    0.620531] pci 0000:3f:0d.2: [8086:0ee5] type 00 class 0x088000
[    0.620569] pci 0000:3f:0d.3: [8086:0ee7] type 00 class 0x088000
[    0.620609] pci 0000:3f:0d.4: [8086:0ee9] type 00 class 0x088000
[    0.620649] pci 0000:3f:0e.0: [8086:0ea0] type 00 class 0x088000
[    0.620692] pci 0000:3f:0e.1: [8086:0e30] type 00 class 0x110100
[    0.620750] pci 0000:3f:0f.0: [8086:0ea8] type 00 class 0x088000
[    0.620809] pci 0000:3f:0f.1: [8086:0e71] type 00 class 0x088000
[    0.620862] pci 0000:3f:0f.2: [8086:0eaa] type 00 class 0x088000
[    0.620920] pci 0000:3f:0f.3: [8086:0eab] type 00 class 0x088000
[    0.620976] pci 0000:3f:0f.4: [8086:0eac] type 00 class 0x088000
[    0.621029] pci 0000:3f:0f.5: [8086:0ead] type 00 class 0x088000
[    0.621084] pci 0000:3f:10.0: [8086:0eb0] type 00 class 0x088000
[    0.621141] pci 0000:3f:10.1: [8086:0eb1] type 00 class 0x088000
[    0.621194] pci 0000:3f:10.2: [8086:0eb2] type 00 class 0x088000
[    0.621248] pci 0000:3f:10.3: [8086:0eb3] type 00 class 0x088000
[    0.621305] pci 0000:3f:10.4: [8086:0eb4] type 00 class 0x088000
[    0.621359] pci 0000:3f:10.5: [8086:0eb5] type 00 class 0x088000
[    0.621411] pci 0000:3f:10.6: [8086:0eb6] type 00 class 0x088000
[    0.621464] pci 0000:3f:10.7: [8086:0eb7] type 00 class 0x088000
[    0.621520] pci 0000:3f:13.0: [8086:0e1d] type 00 class 0x088000
[    0.621562] pci 0000:3f:13.1: [8086:0e34] type 00 class 0x110100
[    0.621604] pci 0000:3f:13.4: [8086:0e81] type 00 class 0x088000
[    0.621644] pci 0000:3f:13.5: [8086:0e36] type 00 class 0x110100
[    0.621687] pci 0000:3f:16.0: [8086:0ec8] type 00 class 0x088000
[    0.621729] pci 0000:3f:16.1: [8086:0ec9] type 00 class 0x088000
[    0.621769] pci 0000:3f:16.2: [8086:0eca] type 00 class 0x088000
[    0.621817] pci_bus 0000:3f: busn_res: [bus 3f-ff] end is updated to 3f
[    0.621819] pci_bus 0000:3f: busn_res: can not insert [bus 3f] under domain [bus 00-ff] (conflicts with (null) [bus 00-3f])
[    0.622544] PCI: Discovered peer bus 7f
[    0.622545] PCI: root bus 7f: using default resources
[    0.622546] PCI: Probing PCI hardware (bus 7f)
[    0.622567] PCI host bridge to bus 0000:7f
[    0.622569] pci_bus 0000:7f: root bus resource [io  0x0000-0xffff]
[    0.622570] pci_bus 0000:7f: root bus resource [mem 0x00000000-0x3fffffffffff]
[    0.622572] pci_bus 0000:7f: No busn resource found for root bus, will use [bus 7f-ff]
[    0.622575] pci_bus 0000:7f: busn_res: can not insert [bus 7f-ff] under domain [bus 00-ff] (conflicts with (null) [bus 40-7f])
[    0.622583] pci 0000:7f:08.0: [8086:0e80] type 00 class 0x088000
[    0.622635] pci 0000:7f:09.0: [8086:0e90] type 00 class 0x088000
[    0.622689] pci 0000:7f:0a.0: [8086:0ec0] type 00 class 0x088000
[    0.622738] pci 0000:7f:0a.1: [8086:0ec1] type 00 class 0x088000
[    0.622791] pci 0000:7f:0a.2: [8086:0ec2] type 00 class 0x088000
[    0.622840] pci 0000:7f:0a.3: [8086:0ec3] type 00 class 0x088000
[    0.622892] pci 0000:7f:0b.0: [8086:0e1e] type 00 class 0x088000
[    0.622939] pci 0000:7f:0b.3: [8086:0e1f] type 00 class 0x088000
[    0.622988] pci 0000:7f:0c.0: [8086:0ee0] type 00 class 0x088000
[    0.623037] pci 0000:7f:0c.1: [8086:0ee2] type 00 class 0x088000
[    0.623091] pci 0000:7f:0c.2: [8086:0ee4] type 00 class 0x088000
[    0.623141] pci 0000:7f:0c.3: [8086:0ee6] type 00 class 0x088000
[    0.623190] pci 0000:7f:0c.4: [8086:0ee8] type 00 class 0x088000
[    0.623242] pci 0000:7f:0d.0: [8086:0ee1] type 00 class 0x088000
[    0.623289] pci 0000:7f:0d.1: [8086:0ee3] type 00 class 0x088000
[    0.623336] pci 0000:7f:0d.2: [8086:0ee5] type 00 class 0x088000
[    0.623389] pci 0000:7f:0d.3: [8086:0ee7] type 00 class 0x088000
[    0.623438] pci 0000:7f:0d.4: [8086:0ee9] type 00 class 0x088000
[    0.623491] pci 0000:7f:0e.0: [8086:0ea0] type 00 class 0x088000
[    0.623557] pci 0000:7f:0e.1: [8086:0e30] type 00 class 0x110100
[    0.623624] pci 0000:7f:0f.0: [8086:0ea8] type 00 class 0x088000
[    0.623697] pci 0000:7f:0f.1: [8086:0e71] type 00 class 0x088000
[    0.623766] pci 0000:7f:0f.2: [8086:0eaa] type 00 class 0x088000
[    0.623836] pci 0000:7f:0f.3: [8086:0eab] type 00 class 0x088000
[    0.623904] pci 0000:7f:0f.4: [8086:0eac] type 00 class 0x088000
[    0.623974] pci 0000:7f:0f.5: [8086:0ead] type 00 class 0x088000
[    0.624048] pci 0000:7f:10.0: [8086:0eb0] type 00 class 0x088000
[    0.624125] pci 0000:7f:10.1: [8086:0eb1] type 00 class 0x088000
[    0.624202] pci 0000:7f:10.2: [8086:0eb2] type 00 class 0x088000
[    0.624277] pci 0000:7f:10.3: [8086:0eb3] type 00 class 0x088000
[    0.624343] pci 0000:7f:10.4: [8086:0eb4] type 00 class 0x088000
[    0.624413] pci 0000:7f:10.5: [8086:0eb5] type 00 class 0x088000
[    0.624481] pci 0000:7f:10.6: [8086:0eb6] type 00 class 0x088000
[    0.624546] pci 0000:7f:10.7: [8086:0eb7] type 00 class 0x088000
[    0.624612] pci 0000:7f:13.0: [8086:0e1d] type 00 class 0x088000
[    0.624663] pci 0000:7f:13.1: [8086:0e34] type 00 class 0x110100
[    0.624711] pci 0000:7f:13.4: [8086:0e81] type 00 class 0x088000
[    0.624758] pci 0000:7f:13.5: [8086:0e36] type 00 class 0x110100
[    0.624809] pci 0000:7f:16.0: [8086:0ec8] type 00 class 0x088000
[    0.624854] pci 0000:7f:16.1: [8086:0ec9] type 00 class 0x088000
[    0.624900] pci 0000:7f:16.2: [8086:0eca] type 00 class 0x088000
[    0.624959] pci_bus 0000:7f: busn_res: [bus 7f-ff] end is updated to 7f
[    0.624961] pci_bus 0000:7f: busn_res: can not insert [bus 7f] under domain [bus 00-ff] (conflicts with (null) [bus 40-7f])
[    0.624971] PCI: pci_cache_line_size set to 64 bytes
[    0.624998] pci 0000:02:00.0: can't claim BAR 7 [mem 0x380000000000-0x38000007bfff 64bit pref]: no compatible bridge window
[    0.625159] e820: reserve RAM buffer [mem 0xab3c7000-0xabffffff]
[    0.625161] e820: reserve RAM buffer [mem 0xabb10000-0xabffffff]
[    0.625272] NetLabel: Initializing
[    0.625273] NetLabel:  domain hash size = 128
[    0.625273] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.625294] NetLabel:  unlabeled traffic allowed by default
[    0.625311] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    0.625311] hpet0: 8 comparators, 64-bit 14.318180 MHz counter
[    0.626169] clocksource: Switched to clocksource hpet
[    0.637996] VFS: Disk quotas dquot_6.6.0
[    0.638027] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.638218] AppArmor: AppArmor Filesystem Enabled
[    0.638237] pnp: PnP ACPI init
[    0.638377] system 00:00: [mem 0xfc000000-0xfcffffff window] has been reserved
[    0.638379] system 00:00: [mem 0xfd000000-0xfdffffff window] has been reserved
[    0.638380] system 00:00: [mem 0xfe000000-0xfeafffff window] has been reserved
[    0.638382] system 00:00: [mem 0xfeb00000-0xfebfffff window] has been reserved
[    0.638384] system 00:00: [mem 0xfed00400-0xfed3ffff window] could not be reserved
[    0.638386] system 00:00: [mem 0xfed45000-0xfedfffff window] has been reserved
[    0.638387] system 00:00: [mem 0xef646000-0xef646fff window] has been reserved
[    0.638392] system 00:00: Plug and Play ACPI device, IDs PNP0c01 (active)
[    0.638512] system 00:01: [mem 0xef644000-0xef645fff] could not be reserved
[    0.638516] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.638715] system 00:02: [io  0x0620-0x063f] has been reserved
[    0.638717] system 00:02: [io  0x0610-0x061f] has been reserved
[    0.638721] system 00:02: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.638776] pnp 00:03: Plug and Play ACPI device, IDs PNP0303 PNP030b (active)
[    0.638828] pnp 00:04: Plug and Play ACPI device, IDs PNP0f03 PNP0f13 (active)
[    0.638873] pnp 00:05: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.638976] system 00:06: [io  0x04d0-0x04d1] has been reserved
[    0.638980] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.639146] pnp 00:07: Plug and Play ACPI device, IDs IFX0102 PNP0c31 (active)
[    0.639400] system 00:08: [io  0x0400-0x0453] has been reserved
[    0.639402] system 00:08: [io  0x0458-0x047f] has been reserved
[    0.639404] system 00:08: [io  0x1180-0x119f] has been reserved
[    0.639405] system 00:08: [io  0x0500-0x057f] has been reserved
[    0.639407] system 00:08: [mem 0xfed1c000-0xfed1ffff] has been reserved
[    0.639409] system 00:08: [mem 0xfec00000-0xfecfffff] could not be reserved
[    0.639411] system 00:08: [mem 0xfed08000-0xfed08fff] has been reserved
[    0.639412] system 00:08: [mem 0xff000000-0xffffffff] has been reserved
[    0.639416] system 00:08: Plug and Play ACPI device, IDs PNP0c01 (active)
[    0.639525] system 00:09: [io  0x0454-0x0457] has been reserved
[    0.639529] system 00:09: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    0.639746] system 00:0a: [mem 0xfbf20000-0xfbf21fff] could not be reserved
[    0.639750] system 00:0a: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.640155] pnp: PnP ACPI: found 11 devices
[    0.646540] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.646548] pci_bus 0000:00: max bus depth: 3 pci_try_num: 4
[    0.646619] pci 0000:00:11.0: BAR 14: assigned [mem 0xc2000000-0xc20fffff]
[    0.646621] pci 0000:00:01.0: PCI bridge to [bus 03]
[    0.646630] pci 0000:00:02.0: PCI bridge to [bus 07]
[    0.646632] pci 0000:00:02.0:   bridge window [io  0xa000-0xafff]
[    0.646636] pci 0000:00:02.0:   bridge window [mem 0xee000000-0xef0fffff]
[    0.646639] pci 0000:00:02.0:   bridge window [mem 0xb0000000-0xc1ffffff 64bit pref]
[    0.646644] pci 0000:05:00.0: PCI bridge to [bus 06]
[    0.646646] pci 0000:05:00.0:   bridge window [io  0xb000-0xbfff]
[    0.646649] pci 0000:05:00.0:   bridge window [mem 0xef100000-0xef1fffff]
[    0.646652] pci 0000:05:00.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.646656] pci 0000:04:00.0: PCI bridge to [bus 05-06]
[    0.646658] pci 0000:04:00.0:   bridge window [io  0xb000-0xbfff]
[    0.646661] pci 0000:04:00.0:   bridge window [mem 0xef100000-0xef1fffff]
[    0.646664] pci 0000:04:00.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.646668] pci 0000:00:03.0: PCI bridge to [bus 04-06]
[    0.646670] pci 0000:00:03.0:   bridge window [io  0xb000-0xbfff]
[    0.646673] pci 0000:00:03.0:   bridge window [mem 0xef100000-0xef2fffff]
[    0.646676] pci 0000:00:03.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.646682] pci 0000:02:00.0: BAR 7: assigned [mem 0xe0804000-0xe087ffff 64bit pref]
[    0.646686] pci 0000:00:11.0: PCI bridge to [bus 02]
[    0.646689] pci 0000:00:11.0:   bridge window [io  0xc000-0xcfff]
[    0.646693] pci 0000:00:11.0:   bridge window [mem 0xc2000000-0xc20fffff]
[    0.646697] pci 0000:00:11.0:   bridge window [mem 0xe0400000-0xe08fffff 64bit pref]
[    0.646703] pci 0000:00:1c.0: PCI bridge to [bus 01]
[    0.646705] pci 0000:00:1c.0:   bridge window [io  0xd000-0xdfff]
[    0.646709] pci 0000:00:1c.0:   bridge window [mem 0xef500000-0xef5fffff]
[    0.646717] pci 0000:00:1c.5: PCI bridge to [bus 08]
[    0.646726] pci 0000:00:1c.6: PCI bridge to [bus 09]
[    0.646736] pci 0000:00:1c.7: PCI bridge to [bus 0a]
[    0.646740] pci 0000:00:1c.7:   bridge window [mem 0xef400000-0xef4fffff]
[    0.646747] pci 0000:00:1e.0: PCI bridge to [bus 0b]
[    0.646751] pci 0000:00:1e.0:   bridge window [mem 0xef300000-0xef3fffff]
[    0.646758] pci_bus 0000:00: resource 4 [io  0x0000-0x03af window]
[    0.646759] pci_bus 0000:00: resource 5 [io  0x03e0-0x0cf7 window]
[    0.646761] pci_bus 0000:00: resource 6 [io  0x03b0-0x03df window]
[    0.646762] pci_bus 0000:00: resource 7 [io  0x0d00-0xffff window]
[    0.646763] pci_bus 0000:00: resource 8 [mem 0x000a0000-0x000bffff window]
[    0.646764] pci_bus 0000:00: resource 9 [mem 0x000c0000-0x000dffff window]
[    0.646766] pci_bus 0000:00: resource 10 [mem 0xb0000000-0xefffffff window]
[    0.646767] pci_bus 0000:00: resource 11 [mem 0x380000000000-0x38007fffffff window]
[    0.646768] pci_bus 0000:07: resource 0 [io  0xa000-0xafff]
[    0.646770] pci_bus 0000:07: resource 1 [mem 0xee000000-0xef0fffff]
[    0.646771] pci_bus 0000:07: resource 2 [mem 0xb0000000-0xc1ffffff 64bit pref]
[    0.646772] pci_bus 0000:04: resource 0 [io  0xb000-0xbfff]
[    0.646773] pci_bus 0000:04: resource 1 [mem 0xef100000-0xef2fffff]
[    0.646774] pci_bus 0000:04: resource 2 [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.646776] pci_bus 0000:05: resource 0 [io  0xb000-0xbfff]
[    0.646777] pci_bus 0000:05: resource 1 [mem 0xef100000-0xef1fffff]
[    0.646778] pci_bus 0000:05: resource 2 [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.646779] pci_bus 0000:06: resource 0 [io  0xb000-0xbfff]
[    0.646780] pci_bus 0000:06: resource 1 [mem 0xef100000-0xef1fffff]
[    0.646782] pci_bus 0000:06: resource 2 [mem 0xd0000000-0xe01fffff 64bit pref]
[    0.646783] pci_bus 0000:02: resource 0 [io  0xc000-0xcfff]
[    0.646784] pci_bus 0000:02: resource 1 [mem 0xc2000000-0xc20fffff]
[    0.646785] pci_bus 0000:02: resource 2 [mem 0xe0400000-0xe08fffff 64bit pref]
[    0.646787] pci_bus 0000:01: resource 0 [io  0xd000-0xdfff]
[    0.646788] pci_bus 0000:01: resource 1 [mem 0xef500000-0xef5fffff]
[    0.646789] pci_bus 0000:0a: resource 1 [mem 0xef400000-0xef4fffff]
[    0.646790] pci_bus 0000:0b: resource 1 [mem 0xef300000-0xef3fffff]
[    0.646792] pci_bus 0000:0b: resource 4 [io  0x0000-0x03af window]
[    0.646793] pci_bus 0000:0b: resource 5 [io  0x03e0-0x0cf7 window]
[    0.646794] pci_bus 0000:0b: resource 6 [io  0x03b0-0x03df window]
[    0.646795] pci_bus 0000:0b: resource 7 [io  0x0d00-0xffff window]
[    0.646797] pci_bus 0000:0b: resource 8 [mem 0x000a0000-0x000bffff window]
[    0.646798] pci_bus 0000:0b: resource 9 [mem 0x000c0000-0x000dffff window]
[    0.646800] pci_bus 0000:0b: resource 10 [mem 0xb0000000-0xefffffff window]
[    0.646801] pci_bus 0000:0b: resource 11 [mem 0x380000000000-0x38007fffffff window]
[    0.646862] pci_bus 0000:40: resource 4 [io  0x0000-0x03af window]
[    0.646864] pci_bus 0000:40: resource 5 [io  0x03e0-0x0cf7 window]
[    0.646866] pci_bus 0000:40: resource 6 [mem 0x000c0000-0x000dffff window]
[    0.646867] pci_bus 0000:40: resource 7 [mem 0xf8000000-0xfbffffff window]
[    0.646869] pci_bus 0000:40: resource 8 [mem 0x381000000000-0x38107fffffff window]
[    0.646877] pci_bus 0000:3f: resource 4 [io  0x0000-0xffff]
[    0.646878] pci_bus 0000:3f: resource 5 [mem 0x00000000-0x3fffffffffff]
[    0.646884] pci_bus 0000:7f: resource 4 [io  0x0000-0xffff]
[    0.646885] pci_bus 0000:7f: resource 5 [mem 0x00000000-0x3fffffffffff]
[    0.646945] NET: Registered protocol family 2
[    0.647356] TCP established hash table entries: 524288 (order: 10, 4194304 bytes)
[    0.648043] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.648205] TCP: Hash tables configured (established 524288 bind 65536)
[    0.648364] UDP hash table entries: 32768 (order: 8, 1048576 bytes)
[    0.648549] UDP-Lite hash table entries: 32768 (order: 8, 1048576 bytes)
[    0.648953] NET: Registered protocol family 1
[    0.696419] PCI: CLS 64 bytes, default 64
[    0.696455] Unpacking initramfs...
[    1.524038] Freeing initrd memory: 63204K
[    1.524124] DMAR: [Firmware Bug]: RMRR entry for device 0a:00.0 is broken - applying workaround
[    1.524183] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    1.524186] software IO TLB [mem 0xa496d000-0xa896d000] (64MB) mapped at [        (ptrval)-        (ptrval)]
[    1.526842] Scanning for low memory corruption every 60 seconds
[    1.528314] Initialise system trusted keyrings
[    1.528323] Key type blacklist registered
[    1.528404] workingset: timestamp_bits=36 max_order=24 bucket_order=0
[    1.529741] zbud: loaded
[    1.530454] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    1.530635] fuse init (API version 7.26)
[    1.533398] Key type asymmetric registered
[    1.533399] Asymmetric key parser 'x509' registered
[    1.533429] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    1.533562] io scheduler noop registered
[    1.533564] io scheduler deadline registered
[    1.533649] io scheduler cfq registered (default)
[    1.535784] efifb: probing for efifb
[    1.535796] efifb: framebuffer at 0xb0000000, using 2432k, total 2432k
[    1.535797] efifb: mode is 800x600x32, linelength=4096, pages=1
[    1.535798] efifb: scrolling: redraw
[    1.535799] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    1.535901] Console: switching to colour frame buffer device 100x37
[    1.535913] fb0: EFI VGA frame buffer device
[    1.535920] intel_idle: MWAIT substates: 0x1120
[    1.535921] intel_idle: v0.4.1 model 0x3E
[    1.537554] intel_idle: lapic_timer_reliable_states 0xffffffff
[    1.537686] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
[    1.537731] ACPI: Power Button [PWRB]
[    1.537777] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input1
[    1.537796] ACPI: Power Button [PWRF]
[    1.593716] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    1.595457] serial 0000:00:16.3: enabling device (0000 -> 0003)
[    1.615891] 0000:00:16.3: ttyS4 at I/O 0xe060 (irq = 17, base_baud = 115200) is a 16550A
[    1.616313] Linux agpgart interface v0.103
[    1.643263] tpm_tis 00:07: 1.2 TPM (device-id 0xB, rev-id 16)
[    1.780971] loop: module loaded
[    1.781704] scsi host0: ata_generic
[    1.781823] scsi host1: ata_generic
[    1.781858] ata1: PATA max UDMA/100 cmd 0xe0b0 ctl 0xe0a0 bmdma 0xe070 irq 18
[    1.781860] ata2: PATA max UDMA/100 cmd 0xe090 ctl 0xe080 bmdma 0xe078 irq 18
[    1.781937] libphy: Fixed MDIO Bus: probed
[    1.781938] tun: Universal TUN/TAP device driver, 1.6
[    1.781981] PPP generic driver version 2.4.2
[    1.782021] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    1.782023] ehci-pci: EHCI PCI platform driver
[    1.782165] ehci-pci 0000:00:1a.0: EHCI Host Controller
[    1.782179] ehci-pci 0000:00:1a.0: new USB bus registered, assigned bus number 1
[    1.782192] ehci-pci 0000:00:1a.0: debug port 2
[    1.786094] ehci-pci 0000:00:1a.0: cache line size of 64 is not supported
[    1.786105] ehci-pci 0000:00:1a.0: irq 16, io mem 0xef64f000
[    1.800023] ehci-pci 0000:00:1a.0: USB 2.0 started, EHCI 1.00
[    1.800069] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    1.800070] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.800072] usb usb1: Product: EHCI Host Controller
[    1.800073] usb usb1: Manufacturer: Linux 4.15.0-30-generic ehci_hcd
[    1.800074] usb usb1: SerialNumber: 0000:00:1a.0
[    1.800200] hub 1-0:1.0: USB hub found
[    1.800206] hub 1-0:1.0: 2 ports detected
[    1.800452] ehci-pci 0000:00:1d.0: EHCI Host Controller
[    1.800456] ehci-pci 0000:00:1d.0: new USB bus registered, assigned bus number 2
[    1.800468] ehci-pci 0000:00:1d.0: debug port 2
[    1.804375] ehci-pci 0000:00:1d.0: cache line size of 64 is not supported
[    1.804387] ehci-pci 0000:00:1d.0: irq 23, io mem 0xef64e000
[    1.820015] ehci-pci 0000:00:1d.0: USB 2.0 started, EHCI 1.00
[    1.820048] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002
[    1.820050] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.820051] usb usb2: Product: EHCI Host Controller
[    1.820052] usb usb2: Manufacturer: Linux 4.15.0-30-generic ehci_hcd
[    1.820054] usb usb2: SerialNumber: 0000:00:1d.0
[    1.820180] hub 2-0:1.0: USB hub found
[    1.820186] hub 2-0:1.0: 2 ports detected
[    1.820309] ehci-platform: EHCI generic platform driver
[    1.820316] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    1.820318] ohci-pci: OHCI PCI platform driver
[    1.820333] ohci-platform: OHCI generic platform driver
[    1.820344] uhci_hcd: USB Universal Host Controller Interface driver
[    1.820433] xhci_hcd 0000:0a:00.0: xHCI Host Controller
[    1.820438] xhci_hcd 0000:0a:00.0: new USB bus registered, assigned bus number 3
[    1.820605] xhci_hcd 0000:0a:00.0: hcc params 0x0270f06d hci version 0x96 quirks 0x04004000
[    1.820922] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002
[    1.820923] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.820925] usb usb3: Product: xHCI Host Controller
[    1.820926] usb usb3: Manufacturer: Linux 4.15.0-30-generic xhci-hcd
[    1.820928] usb usb3: SerialNumber: 0000:0a:00.0
[    1.821040] hub 3-0:1.0: USB hub found
[    1.821051] hub 3-0:1.0: 4 ports detected
[    1.821176] xhci_hcd 0000:0a:00.0: xHCI Host Controller
[    1.821179] xhci_hcd 0000:0a:00.0: new USB bus registered, assigned bus number 4
[    1.821195] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
[    1.821214] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003
[    1.821215] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.821217] usb usb4: Product: xHCI Host Controller
[    1.821219] usb usb4: Manufacturer: Linux 4.15.0-30-generic xhci-hcd
[    1.821221] usb usb4: SerialNumber: 0000:0a:00.0
[    1.821326] hub 4-0:1.0: USB hub found
[    1.821336] hub 4-0:1.0: 4 ports detected
[    1.821526] i8042: PNP: PS/2 Controller [PNP0303:PS2K,PNP0f03:PS2M] at 0x60,0x64 irq 1,12
[    1.824629] serio: i8042 KBD port at 0x60,0x64 irq 1
[    1.824634] serio: i8042 AUX port at 0x60,0x64 irq 12
[    1.824746] mousedev: PS/2 mouse device common for all mice
[    1.824893] rtc_cmos 00:05: RTC can wake from S4
[    1.825026] rtc_cmos 00:05: rtc core: registered rtc_cmos as rtc0
[    1.825055] rtc_cmos 00:05: alarms up to one month, y3k, 114 bytes nvram, hpet irqs
[    1.825063] i2c /dev entries driver
[    1.825123] device-mapper: uevent: version 1.0.3
[    1.825192] device-mapper: ioctl: 4.37.0-ioctl (2017-09-20) initialised: dm-devel@redhat.com
[    1.825199] intel_pstate: Intel P-state driver initializing
[    1.828274] ledtrig-cpu: registered to indicate activity on CPUs
[    1.828279] EFI Variables Facility v0.08 2004-May-17
[    1.840110] NET: Registered protocol family 10
[    1.844537] Segment Routing with IPv6
[    1.844554] NET: Registered protocol family 17
[    1.844600] Key type dns_resolver registered
[    1.848024] RAS: Correctable Errors collector initialized.
[    1.848056] microcode: sig=0x306e4, pf=0x1, revision=0x42c
[    1.849066] microcode: Microcode Update Driver: v2.2.
[    1.849075] sched_clock: Marking stable (1849060812, 0)->(1937943514, -88882702)
[    1.849487] registered taskstats version 1
[    1.849494] Loading compiled-in X.509 certificates
[    1.851875] Loaded X.509 cert 'Build time autogenerated kernel key: 83a24b0453c1c7015e385f44153c9d4e483baefd'
[    1.852176] Loaded UEFI:db cert 'Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4' linked to secondary sys keyring
[    1.852196] Loaded UEFI:db cert 'Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53' linked to secondary sys keyring
[    1.852220] Loaded UEFI:db cert 'Hewlett-Packard UEFI Secure Boot DB Key: e7203ac28b848d3c03432f6a485dd1f4c7b8e529' linked to secondary sys keyring
[    1.854234] Loaded UEFI:MokListRT cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63' linked to secondary sys keyring
[    1.854516] zswap: loaded using pool lzo/zbud
[    1.857913] Key type big_key registered
[    1.857916] Key type trusted registered
[    1.859469] Key type encrypted registered
[    1.859471] AppArmor: AppArmor sha1 policy hashing enabled
[    2.136033] usb 1-1: new high-speed USB device number 2 using ehci-pci
[    2.147576] evm: HMAC attrs: 0x1
[    2.148336]   Magic number: 14:895:367
[    2.148337]   hash matches /build/linux-I4R9hO/linux-4.15.0/drivers/base/power/main.c:757
[    2.148535] rtc_cmos 00:05: setting system clock to 2018-08-19 06:23:29 UTC (1534659809)
[    2.148582] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    2.148583] EDD information not available.
[    2.151370] Freeing unused kernel memory: 2408K
[    2.156034] usb 2-1: new high-speed USB device number 2 using ehci-pci
[    2.164033] Write protecting the kernel read-only data: 20480k
[    2.164762] Freeing unused kernel memory: 2008K
[    2.168727] Freeing unused kernel memory: 1904K
[    2.175458] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    2.175459] x86/mm: Checking user space page tables
[    2.181877] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    2.284249] ipmi message handler version 39.2
[    2.285893] ipmi device interface
[    2.286331] pps_core: LinuxPPS API ver. 1 registered
[    2.286332] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    2.287597] PTP clock support registered
[    2.291780] isci: Intel(R) C600 SAS Controller Driver - version 1.2.0
[    2.291823] isci 0000:02:00.0: driver configured for rev: 5 silicon
[    2.291913] isci 0000:02:00.0: OEM SAS parameters (version: 1.1) loaded (platform)
[    2.292117] isci 0000:02:00.0: SCU controller 0: phy 3-0 cables: {short, short, short, short}
[    2.294410] scsi host2: isci
[    2.294494] ahci 0000:00:1f.2: version 3.0
[    2.294840] usb 1-1: New USB device found, idVendor=8087, idProduct=0024
[    2.294842] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    2.294965] e1000e: Intel(R) PRO/1000 Network Driver - 3.2.6-k
[    2.294966] e1000e: Copyright(c) 1999 - 2015 Intel Corporation.
[    2.295113] firewire_ohci 0000:0b:05.0: enabling device (0100 -> 0102)
[    2.295237] hub 1-1:1.0: USB hub found
[    2.295325] hub 1-1:1.0: 6 ports detected
[    2.302503] PKCS#7 signature not signed with a trusted key
[    2.302510] amdkcl: loading out-of-tree module taints kernel.
[    2.302529] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    2.304762] ahci 0000:00:1f.2: AHCI 0001.0300 32 slots 6 ports 6 Gbps 0xd impl SATA mode
[    2.304765] ahci 0000:00:1f.2: flags: 64bit ncq sntf pm led clo pio slum part ems apst 
[    2.312417] usb 2-1: New USB device found, idVendor=8087, idProduct=0024
[    2.312419] usb 2-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    2.312565] hub 2-1:1.0: USB hub found
[    2.312664] hub 2-1:1.0: 8 ports detected
[    2.328510] scsi host3: ahci
[    2.328670] scsi host4: ahci
[    2.328762] scsi host5: ahci
[    2.328893] scsi host6: ahci
[    2.328988] scsi host7: ahci
[    2.329212] scsi host8: ahci
[    2.329248] ata3: SATA max UDMA/133 abar m2048@0xef64c000 port 0xef64c100 irq 35
[    2.329249] ata4: DUMMY
[    2.329251] ata5: SATA max UDMA/133 abar m2048@0xef64c000 port 0xef64c200 irq 35
[    2.329252] ata6: SATA max UDMA/133 abar m2048@0xef64c000 port 0xef64c280 irq 35
[    2.329253] ata7: DUMMY
[    2.329254] ata8: DUMMY
[    2.329541] e1000e 0000:00:19.0: Interrupt Throttling Rate (ints/sec) set to dynamic conservative mode
[    2.352071] firewire_ohci 0000:0b:05.0: added OHCI v1.0 device as card 0, 8 IR + 8 IT contexts, quirks 0x0
[    2.358340] Warning: fail to get symbol drm_fb_helper_release_fbi, replace it with kcl stub
[    2.387349] PKCS#7 signature not signed with a trusted key
[    2.388575] PKCS#7 signature not signed with a trusted key
[    2.389023] PKCS#7 signature not signed with a trusted key
[    2.389623] PKCS#7 signature not signed with a trusted key
[    2.389638] nvidia: module license 'NVIDIA' taints kernel.
[    2.389638] Disabling lock debugging due to kernel taint
[    2.398319] module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc         (ptrval), val ffffffffc0d224c0
[    2.406999] PKCS#7 signature not signed with a trusted key
[    2.419823] e1000e 0000:00:19.0 0000:00:19.0 (uninitialized): registered PHC clock
[    2.507336] e1000e 0000:00:19.0 eth0: (PCI Express:2.5GT/s:Width x1) a0:d3:c1:34:1f:38
[    2.507338] e1000e 0000:00:19.0 eth0: Intel(R) PRO/1000 Network Connection
[    2.507379] e1000e 0000:00:19.0 eth0: MAC: 10, PHY: 11, PBA No: 0100FF-0FF
[    2.507617] e1000e 0000:01:00.0: Interrupt Throttling Rate (ints/sec) set to dynamic conservative mode
[    2.527179] PKCS#7 signature not signed with a trusted key
[    2.540127] module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc         (ptrval), val ffffffffc1f214c0
[    2.556053] tsc: Refined TSC clocksource calibration: 2793.268 MHz
[    2.556077] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x28436928c28, max_idle_ns: 440795267499 ns
[    2.558968] e1000e 0000:01:00.0 0000:01:00.0 (uninitialized): registered PHC clock
[    2.564727] [drm] amdgpu kernel modesetting enabled.
[    2.566967] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    2.566968] AMD IOMMUv2 functionality not available on this system
[    2.569293] PKCS#7 signature not signed with a trusted key
[    2.570412] CRAT table not found
[    2.570414] Virtual CRAT table created for CPU
[    2.570415] Parsing CRAT table with 2 nodes
[    2.570417] Creating topology SYSFS entries
[    2.570438] Topology: Add CPU node
[    2.570438] Finished initializing topology
[    2.572427] kfd kfd: Initialized module
[    2.572616] checking generic (b0000000 260000) vs hw (d0000000 10000000)
[    2.572658] amdgpu 0000:06:00.0: enabling device (0106 -> 0107)
[    2.572831] [drm] initializing kernel modesetting (VEGA10 0x1002:0x6863 0x1002:0x6B76 0x00).
[    2.572838] [drm] register mmio base: 0xEF100000
[    2.572839] [drm] register mmio size: 524288
[    2.572844] [drm] add ip block number 0 <soc15_common>
[    2.572846] [drm] add ip block number 1 <gmc_v9_0>
[    2.572846] [drm] add ip block number 2 <vega10_ih>
[    2.572847] [drm] add ip block number 3 <psp>
[    2.572848] [drm] add ip block number 4 <amdgpu_powerplay>
[    2.572849] [drm] add ip block number 5 <dm>
[    2.572850] [drm] add ip block number 6 <gfx_v9_0>
[    2.572851] [drm] add ip block number 7 <sdma_v4_0>
[    2.572852] [drm] add ip block number 8 <uvd_v7_0>
[    2.572853] [drm] add ip block number 9 <vce_v4_0>
[    2.572891] [drm] probing gen 2 caps for device 1022:1471 = 700d03/e
[    2.572892] [drm] probing mlw for device 1022:1471 = 700d03
[    2.572898] [drm] UVD is enabled in VM mode
[    2.572899] [drm] UVD ENC is enabled in VM mode
[    2.572900] [drm] VCE enabled in VM mode
[    2.572939] ATOM BIOS: 113-D0501100-109
[    2.572970] [drm] vm size is 256 GB, 3 levels, block size is 9-bit, fragment size is 9-bit
[    2.572980] amdgpu 0000:06:00.0: BAR 2: releasing [mem 0xe0000000-0xe01fffff 64bit pref]
[    2.572982] amdgpu 0000:06:00.0: BAR 0: releasing [mem 0xd0000000-0xdfffffff 64bit pref]
[    2.572993] pcieport 0000:05:00.0: BAR 15: releasing [mem 0xd0000000-0xe01fffff 64bit pref]
[    2.572995] pcieport 0000:04:00.0: BAR 15: releasing [mem 0xd0000000-0xe01fffff 64bit pref]
[    2.572996] pcieport 0000:00:03.0: BAR 15: releasing [mem 0xd0000000-0xe01fffff 64bit pref]
[    2.573020] pcieport 0000:00:03.0: BAR 15: no space for [mem size 0x600000000 64bit pref]
[    2.573021] pcieport 0000:00:03.0: BAR 15: failed to assign [mem size 0x600000000 64bit pref]
[    2.573024] pcieport 0000:04:00.0: BAR 15: no space for [mem size 0x600000000 64bit pref]
[    2.573026] pcieport 0000:04:00.0: BAR 15: failed to assign [mem size 0x600000000 64bit pref]
[    2.573028] pcieport 0000:05:00.0: BAR 15: no space for [mem size 0x600000000 64bit pref]
[    2.573029] pcieport 0000:05:00.0: BAR 15: failed to assign [mem size 0x600000000 64bit pref]
[    2.573032] amdgpu 0000:06:00.0: BAR 0: no space for [mem size 0x400000000 64bit pref]
[    2.573033] amdgpu 0000:06:00.0: BAR 0: failed to assign [mem size 0x400000000 64bit pref]
[    2.573038] amdgpu 0000:06:00.0: BAR 2: no space for [mem size 0x00200000 64bit pref]
[    2.573039] amdgpu 0000:06:00.0: BAR 2: failed to assign [mem size 0x00200000 64bit pref]
[    2.573042] pcieport 0000:00:03.0: PCI bridge to [bus 04-06]
[    2.573044] pcieport 0000:00:03.0:   bridge window [io  0xb000-0xbfff]
[    2.573047] pcieport 0000:00:03.0:   bridge window [mem 0xef100000-0xef2fffff]
[    2.573054] pcieport 0000:00:03.0: PCI bridge to [bus 04-06]
[    2.573056] pcieport 0000:00:03.0:   bridge window [io  0xb000-0xbfff]
[    2.573060] pcieport 0000:00:03.0:   bridge window [mem 0xef100000-0xef2fffff]
[    2.573062] pcieport 0000:00:03.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    2.573067] pcieport 0000:04:00.0: PCI bridge to [bus 05-06]
[    2.573068] pcieport 0000:04:00.0:   bridge window [io  0xb000-0xbfff]
[    2.573072] pcieport 0000:04:00.0:   bridge window [mem 0xef100000-0xef1fffff]
[    2.573074] pcieport 0000:04:00.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    2.573078] pcieport 0000:05:00.0: PCI bridge to [bus 06]
[    2.573080] pcieport 0000:05:00.0:   bridge window [io  0xb000-0xbfff]
[    2.573083] pcieport 0000:05:00.0:   bridge window [mem 0xef100000-0xef1fffff]
[    2.573086] pcieport 0000:05:00.0:   bridge window [mem 0xd0000000-0xe01fffff 64bit pref]
[    2.573092] [drm] Not enough PCI address space for a large BAR.
[    2.573095] amdgpu 0000:06:00.0: BAR 0: assigned [mem 0xd0000000-0xdfffffff 64bit pref]
[    2.573102] amdgpu 0000:06:00.0: BAR 2: assigned [mem 0xe0000000-0xe01fffff 64bit pref]
[    2.573113] amdgpu 0000:06:00.0: VRAM: 16368M 0x000000F400000000 - 0x000000F7FEFFFFFF (16368M used)
[    2.573115] amdgpu 0000:06:00.0: GTT: 256M 0x000000F800000000 - 0x000000F80FFFFFFF
[    2.573118] [drm] Detected VRAM RAM=16368M, BAR=256M
[    2.573119] [drm] RAM width 2048bits HBM
[    2.573172] [TTM] Zone  kernel: Available graphics memory: 61772268 kiB
[    2.573173] [TTM] Initializing pool allocator
[    2.573177] [TTM] Initializing DMA pool allocator
[    2.573210] [drm] amdgpu: 16368M of VRAM memory ready
[    2.573212] [drm] amdgpu: 64346M of GTT memory ready.
[    2.573223] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    2.573294] [drm] PCIE GART of 256M enabled (table at 0x000000F400800000).
[    2.574662] [drm] use_doorbell being set to: [true]
[    2.574701] [drm] use_doorbell being set to: [true]
[    2.574860] [drm] Found UVD firmware Version: 1.50 Family ID: 17
[    2.574865] [drm] PSP loading UVD firmware
[    2.575155] [drm] Found VCE firmware Version: 53.19 Binary ID: 4
[    2.575161] [drm] PSP loading VCE firmware
[    2.642267] ata3: SATA link down (SStatus 0 SControl 300)
[    2.642316] ata6: SATA link up 3.0 Gbps (SStatus 123 SControl 300)
[    2.642362] ata5: SATA link up 3.0 Gbps (SStatus 123 SControl 300)
[    2.642947] ata6.00: ATA-9: ST1000DM003-1ER162, CC45, max UDMA/133
[    2.642949] ata6.00: 1953525168 sectors, multi 16: LBA48 NCQ (depth 31/32), AA
[    2.643533] ata6.00: configured for UDMA/133
[    2.645059] ata5.00: supports DRM functions and may not be fully accessible
[    2.645878] ata5.00: ATA-11: Samsung SSD 860 EVO 500GB, RVT01B6Q, max UDMA/133
[    2.645879] ata5.00: 976773168 sectors, multi 1: LBA48 NCQ (depth 31/32), AA
[    2.648189] ata5.00: supports DRM functions and may not be fully accessible
[    2.650919] ata5.00: configured for UDMA/133
[    2.728245] scsi 5:0:0:0: Direct-Access     ATA      Samsung SSD 860  1B6Q PQ: 0 ANSI: 5
[    2.728429] sd 5:0:0:0: Attached scsi generic sg0 type 0
[    2.728438] ata5.00: Enabling discard_zeroes_data
[    2.728536] e1000e 0000:01:00.0 eth1: (PCI Express:2.5GT/s:Width x1) a0:d3:c1:34:1f:39
[    2.728538] e1000e 0000:01:00.0 eth1: Intel(R) PRO/1000 Network Connection
[    2.728627] sd 5:0:0:0: [sda] 976773168 512-byte logical blocks: (500 GB/466 GiB)
[    2.728628] scsi 6:0:0:0: Direct-Access     ATA      ST1000DM003-1ER1 CC45 PQ: 0 ANSI: 5
[    2.728629] e1000e 0000:01:00.0 eth1: MAC: 3, PHY: 8, PBA No: FFFFFF-0FF
[    2.728656] sd 5:0:0:0: [sda] Write Protect is off
[    2.728658] sd 5:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    2.728699] sd 5:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    2.728820] sd 6:0:0:0: [sdb] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    2.728822] sd 6:0:0:0: [sdb] 4096-byte physical blocks
[    2.728829] sd 6:0:0:0: [sdb] Write Protect is off
[    2.728830] sd 6:0:0:0: [sdb] Mode Sense: 00 3a 00 00
[    2.728841] sd 6:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    2.728860] sd 6:0:0:0: Attached scsi generic sg1 type 0
[    2.728917] ata5.00: Enabling discard_zeroes_data
[    2.729905] e1000e 0000:00:19.0 eno1: renamed from eth0
[    2.730479]  sda: sda1 sda2
[    2.730693] ata5.00: Enabling discard_zeroes_data
[    2.731997] sd 5:0:0:0: [sda] supports TCG Opal
[    2.731999] sd 5:0:0:0: [sda] Attached SCSI disk
[    2.738555]  sdb: sdb1 sdb2
[    2.738861] sd 6:0:0:0: [sdb] Attached SCSI disk
[    2.752207] e1000e 0000:01:00.0 enp1s0: renamed from eth1
[    2.876198] firewire_core 0000:0b:05.0: created device fw0: GUID 0060b00000a09671, S400
[    3.013594] [drm] Display Core initialized with v3.1.32!
[    3.014142] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    3.014143] [drm] Driver supports precise vblank timestamp query.
[    3.037224] [drm] UVD and UVD ENC initialized successfully.
[    3.136716] [drm] VCE initialized successfully.
[    3.147136] kfd kfd: Allocated 3969056 bytes on gart
[    3.147151] Virtual CRAT table created for GPU
[    3.147152] Parsing CRAT table with 1 nodes
[    3.147168] Creating topology SYSFS entries
[    3.147300] Topology: Add dGPU node [0x6863:0x1002]
[    3.147377] kfd kfd: added device 1002:6863
[    3.150567] [drm] Cannot find any crtc or sizes
[    3.150652] amdgpu 0000:06:00.0: ring 0(gfx) uses VM inv eng 4 on hub 0
[    3.150653] amdgpu 0000:06:00.0: ring 1(comp_1.0.0) uses VM inv eng 5 on hub 0
[    3.150655] amdgpu 0000:06:00.0: ring 2(comp_1.1.0) uses VM inv eng 6 on hub 0
[    3.150656] amdgpu 0000:06:00.0: ring 3(comp_1.2.0) uses VM inv eng 7 on hub 0
[    3.150657] amdgpu 0000:06:00.0: ring 4(comp_1.3.0) uses VM inv eng 8 on hub 0
[    3.150658] amdgpu 0000:06:00.0: ring 5(comp_1.0.1) uses VM inv eng 9 on hub 0
[    3.150660] amdgpu 0000:06:00.0: ring 6(comp_1.1.1) uses VM inv eng 10 on hub 0
[    3.150661] amdgpu 0000:06:00.0: ring 7(comp_1.2.1) uses VM inv eng 11 on hub 0
[    3.150662] amdgpu 0000:06:00.0: ring 8(comp_1.3.1) uses VM inv eng 12 on hub 0
[    3.150663] amdgpu 0000:06:00.0: ring 9(kiq_2.1.0) uses VM inv eng 13 on hub 0
[    3.150664] amdgpu 0000:06:00.0: ring 10(sdma0) uses VM inv eng 4 on hub 1
[    3.150665] amdgpu 0000:06:00.0: ring 11(sdma1) uses VM inv eng 5 on hub 1
[    3.150667] amdgpu 0000:06:00.0: ring 12(uvd) uses VM inv eng 6 on hub 1
[    3.150668] amdgpu 0000:06:00.0: ring 13(uvd_enc0) uses VM inv eng 7 on hub 1
[    3.150669] amdgpu 0000:06:00.0: ring 14(uvd_enc1) uses VM inv eng 8 on hub 1
[    3.150670] amdgpu 0000:06:00.0: ring 15(vce0) uses VM inv eng 9 on hub 1
[    3.150671] amdgpu 0000:06:00.0: ring 16(vce1) uses VM inv eng 10 on hub 1
[    3.150672] amdgpu 0000:06:00.0: ring 17(vce2) uses VM inv eng 11 on hub 1
[    3.150701] [drm] ECC is not present.
[    3.151525] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:06:00.0 on minor 0
[    3.257849] random: fast init done
[    3.262168] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    3.262179] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    3.262182] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    3.262856] EXT4-fs (sda2): mounted filesystem with ordered data mode. Opts: (null)
[    3.418602] ip_tables: (C) 2000-2006 Netfilter Core Team
[    3.445586] random: systemd: uninitialized urandom read (16 bytes read)
[    3.447609] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    3.464939] systemd[1]: Detected architecture x86-64.
[    3.464976] random: systemd: uninitialized urandom read (16 bytes read)
[    3.464984] random: systemd: uninitialized urandom read (16 bytes read)
[    3.469123] systemd[1]: Set hostname to <alex-HP-Z620-Workstation>.
[    3.480621] random: (sd-executor): uninitialized urandom read (16 bytes read)
[    3.481576] random: (sd-executor): uninitialized urandom read (16 bytes read)
[    3.482920] random: (sd-executor): uninitialized urandom read (16 bytes read)
[    3.484187] random: (sd-executor): uninitialized urandom read (16 bytes read)
[    3.579098] systemd[1]: Reached target Remote File Systems.
[    3.579202] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    3.579220] systemd[1]: Reached target Libvirt guests shutdown.
[    3.579388] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[    3.580165] clocksource: Switched to clocksource tsc
[    3.581148] systemd[1]: Created slice User and Session Slice.
[    3.581160] systemd[1]: Reached target User and Group Name Lookups.
[    3.581520] systemd[1]: Created slice System Slice.
[    3.683618] lp: driver loaded but no devices found
[    3.705650] ppdev: user-space parallel port driver
[    3.821548] EXT4-fs (sda2): re-mounted. Opts: errors=remount-ro
[    3.936157] systemd-journald[636]: Received request to flush runtime journal from PID 1
[    3.944842] Adding 2097148k swap on /swapfile.  Priority:-2 extents:6 across:2260988k SSFS
[    4.123807] dca service started, version 1.12.1
[    4.127642] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    4.128848] ioatdma: Intel(R) QuickData Technology Driver 4.00
[    4.351271] PKCS#7 signature not signed with a trusted key
[    4.351295] snd_hda_intel 0000:00:1b.0: enabling device (0100 -> 0102)
[    4.352297] RAPL PMU: API unit is 2^-32 Joules, 3 fixed counters, 163840 ms ovfl timer
[    4.352298] RAPL PMU: hw unit of domain pp0-core 2^-16 Joules
[    4.352299] RAPL PMU: hw unit of domain package 2^-16 Joules
[    4.352300] RAPL PMU: hw unit of domain dram 2^-16 Joules
[    4.352459] snd_hda_intel 0000:07:00.1: enabling device (0100 -> 0102)
[    4.355113] snd_hda_intel 0000:07:00.1: Disabling MSI
[    4.355124] snd_hda_intel 0000:07:00.1: Handle vga_switcheroo audio client
[    4.355203] snd_hda_intel 0000:06:00.1: enabling device (0100 -> 0102)
[    4.360734] snd_hda_intel 0000:06:00.1: Handle vga_switcheroo audio client
[    4.364337] input: HP WMI hotkeys as /devices/virtual/input/input5
[    4.389456] input: HD-Audio Generic HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:03.0/0000:04:00.0/0000:05:00.0/0000:06:00.1/sound/card2/input6
[    4.389537] module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc         (ptrval), val ffffffffc1ebf4c0
[    4.389582] input: HD-Audio Generic HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:03.0/0000:04:00.0/0000:05:00.0/0000:06:00.1/sound/card2/input7
[    4.389654] input: HD-Audio Generic HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:03.0/0000:04:00.0/0000:05:00.0/0000:06:00.1/sound/card2/input8
[    4.389802] input: HD-Audio Generic HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:03.0/0000:04:00.0/0000:05:00.0/0000:06:00.1/sound/card2/input9
[    4.389935] input: HD-Audio Generic HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:03.0/0000:04:00.0/0000:05:00.0/0000:06:00.1/sound/card2/input10
[    4.390100] input: HD-Audio Generic HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:03.0/0000:04:00.0/0000:05:00.0/0000:06:00.1/sound/card2/input11
[    4.429618] snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALC262: line_outs=1 (0x15/0x0/0x0/0x0/0x0) type:line
[    4.429620] snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=1 (0x16/0x0/0x0/0x0/0x0)
[    4.429621] snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
[    4.429622] snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
[    4.429623] snd_hda_codec_realtek hdaudioC0D0:    inputs:
[    4.429625] snd_hda_codec_realtek hdaudioC0D0:      Front Mic=0x19
[    4.429626] snd_hda_codec_realtek hdaudioC0D0:      Rear Mic=0x18
[    4.429627] snd_hda_codec_realtek hdaudioC0D0:      Line=0x1a
[    4.439635] input: HDA Intel PCH Front Mic as /devices/pci0000:00/0000:00:1b.0/sound/card0/input12
[    4.439702] input: HDA Intel PCH Rear Mic as /devices/pci0000:00/0000:00:1b.0/sound/card0/input13
[    4.439750] input: HDA Intel PCH Line as /devices/pci0000:00/0000:00:1b.0/sound/card0/input14
[    4.439808] input: HDA Intel PCH Line Out as /devices/pci0000:00/0000:00:1b.0/sound/card0/input15
[    4.439861] input: HDA Intel PCH Front Headphone as /devices/pci0000:00/0000:00:1b.0/sound/card0/input16
[    4.443506] AVX version of gcm_enc/dec engaged.
[    4.443506] AES CTR mode by8 optimization enabled
[    4.526062] PKCS#7 signature not signed with a trusted key
[    4.535899] module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc         (ptrval), val ffffffffc1ebf4c0
[    4.592553] EDAC sbridge: Seeking for: PCI ID 8086:0ea0
[    4.592573] EDAC sbridge: Seeking for: PCI ID 8086:0ea0
[    4.592581] EDAC sbridge: Seeking for: PCI ID 8086:0ea0
[    4.592584] EDAC sbridge: Seeking for: PCI ID 8086:0e60
[    4.592588] EDAC sbridge: Seeking for: PCI ID 8086:0ea8
[    4.592592] EDAC sbridge: Seeking for: PCI ID 8086:0ea8
[    4.592595] EDAC sbridge: Seeking for: PCI ID 8086:0ea8
[    4.592597] EDAC sbridge: Seeking for: PCI ID 8086:0e71
[    4.592601] EDAC sbridge: Seeking for: PCI ID 8086:0e71
[    4.592604] EDAC sbridge: Seeking for: PCI ID 8086:0e71
[    4.592605] EDAC sbridge: Seeking for: PCI ID 8086:0eaa
[    4.592609] EDAC sbridge: Seeking for: PCI ID 8086:0eaa
[    4.592612] EDAC sbridge: Seeking for: PCI ID 8086:0eaa
[    4.592613] EDAC sbridge: Seeking for: PCI ID 8086:0eab
[    4.592617] EDAC sbridge: Seeking for: PCI ID 8086:0eab
[    4.592620] EDAC sbridge: Seeking for: PCI ID 8086:0eab
[    4.592621] EDAC sbridge: Seeking for: PCI ID 8086:0eac
[    4.592625] EDAC sbridge: Seeking for: PCI ID 8086:0eac
[    4.592628] EDAC sbridge: Seeking for: PCI ID 8086:0eac
[    4.592629] EDAC sbridge: Seeking for: PCI ID 8086:0ead
[    4.592633] EDAC sbridge: Seeking for: PCI ID 8086:0ead
[    4.592636] EDAC sbridge: Seeking for: PCI ID 8086:0ead
[    4.592637] EDAC sbridge: Seeking for: PCI ID 8086:0e68
[    4.592641] EDAC sbridge: Seeking for: PCI ID 8086:0e79
[    4.592645] EDAC sbridge: Seeking for: PCI ID 8086:0e6a
[    4.592650] EDAC sbridge: Seeking for: PCI ID 8086:0e6b
[    4.592654] EDAC sbridge: Seeking for: PCI ID 8086:0e6c
[    4.592658] EDAC sbridge: Seeking for: PCI ID 8086:0e6d
[    4.592663] EDAC sbridge: Seeking for: PCI ID 8086:0eb8
[    4.592667] EDAC sbridge: Seeking for: PCI ID 8086:0ebc
[    4.592671] EDAC sbridge: Seeking for: PCI ID 8086:0ec8
[    4.592676] EDAC sbridge: Seeking for: PCI ID 8086:0ec8
[    4.592679] EDAC sbridge: Seeking for: PCI ID 8086:0ec8
[    4.592679] EDAC sbridge: Seeking for: PCI ID 8086:0ec9
[    4.592684] EDAC sbridge: Seeking for: PCI ID 8086:0ec9
[    4.592687] EDAC sbridge: Seeking for: PCI ID 8086:0ec9
[    4.592687] EDAC sbridge: Seeking for: PCI ID 8086:0eca
[    4.592692] EDAC sbridge: Seeking for: PCI ID 8086:0eca
[    4.592695] EDAC sbridge: Seeking for: PCI ID 8086:0eca
[    4.592819] EDAC MC0: Giving out device to module sb_edac controller Ivy Bridge SrcID#0_Ha#0: DEV 0000:3f:0e.0 (INTERRUPT)
[    4.592919] EDAC MC1: Giving out device to module sb_edac controller Ivy Bridge SrcID#1_Ha#0: DEV 0000:7f:0e.0 (INTERRUPT)
[    4.592920] EDAC sbridge:  Ver: 1.1.2 
[    4.595487] intel_rapl: Found RAPL domain package
[    4.595489] intel_rapl: Found RAPL domain core
[    4.595492] intel_rapl: Found RAPL domain dram
[    4.595496] intel_rapl: RAPL package 0 domain package locked by BIOS
[    4.595836] intel_rapl: Found RAPL domain package
[    4.595837] intel_rapl: Found RAPL domain core
[    4.595840] intel_rapl: Found RAPL domain dram
[    4.595844] intel_rapl: RAPL package 1 domain package locked by BIOS
[    4.782519] audit: type=1400 audit(1534659812.127:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=1185 comm="apparmor_parser"
[    4.782522] audit: type=1400 audit(1534659812.127:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=1185 comm="apparmor_parser"
[    4.782524] audit: type=1400 audit(1534659812.127:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=1185 comm="apparmor_parser"
[    4.783651] audit: type=1400 audit(1534659812.127:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=1192 comm="apparmor_parser"
[    4.783791] audit: type=1400 audit(1534659812.127:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="virt-aa-helper" pid=1190 comm="apparmor_parser"
[    4.785524] audit: type=1400 audit(1534659812.131:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=1191 comm="apparmor_parser"
[    4.785527] audit: type=1400 audit(1534659812.131:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=1191 comm="apparmor_parser"
[    4.786276] audit: type=1400 audit(1534659812.131:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/ippusbxd" pid=1194 comm="apparmor_parser"
[    4.787492] audit: type=1400 audit(1534659812.131:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=1183 comm="apparmor_parser"
[    5.124300] input: HDA NVidia HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:02.0/0000:07:00.1/sound/card1/input17
[    5.124361] input: HDA NVidia HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:02.0/0000:07:00.1/sound/card1/input18
[    5.124408] input: HDA NVidia HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:02.0/0000:07:00.1/sound/card1/input19
[    5.144608] checking generic (b0000000 260000) vs hw (b0000000 10000000)
[    5.144609] fb: switching to nouveaufb from EFI VGA
[    5.144675] Console: switching to colour dummy device 80x25
[    5.144771] nouveau 0000:07:00.0: NVIDIA GK107 (0e73e0a2)
[    5.270196] nouveau 0000:07:00.0: bios: version 80.07.dd.00.0b
[    5.477270] nouveau 0000:07:00.0: fb: 2048 MiB GDDR5
[    6.784528] [TTM] Zone  kernel: Available graphics memory: 32945210 kiB
[    6.784529] [TTM] Zone   dma32: Available graphics memory: 2097152 kiB
[    6.784530] [TTM] Initializing pool allocator
[    6.784535] [TTM] Initializing DMA pool allocator
[    6.784549] nouveau 0000:07:00.0: DRM: VRAM: 2048 MiB
[    6.784550] nouveau 0000:07:00.0: DRM: GART: 1048576 MiB
[    6.784554] nouveau 0000:07:00.0: DRM: TMDS table version 2.0
[    6.784556] nouveau 0000:07:00.0: DRM: DCB version 4.0
[    6.784558] nouveau 0000:07:00.0: DRM: DCB outp 00: 01000f02 00020030
[    6.784560] nouveau 0000:07:00.0: DRM: DCB outp 01: 02000f00 00000000
[    6.784562] nouveau 0000:07:00.0: DRM: DCB outp 02: 08811fc6 0f420010
[    6.784563] nouveau 0000:07:00.0: DRM: DCB outp 03: 08011f82 00020010
[    6.784564] nouveau 0000:07:00.0: DRM: DCB outp 04: 02822fa6 0f420010
[    6.784566] nouveau 0000:07:00.0: DRM: DCB outp 05: 02022f62 00020010
[    6.784567] nouveau 0000:07:00.0: DRM: DCB conn 00: 00001030
[    6.784568] nouveau 0000:07:00.0: DRM: DCB conn 01: 00010146
[    6.784569] nouveau 0000:07:00.0: DRM: DCB conn 02: 00002246
[    6.850955] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    6.850956] [drm] Driver supports precise vblank timestamp query.
[    6.852637] nouveau 0000:07:00.0: DRM: MM: using COPY for buffer copies
[    6.900243] IPv6: ADDRCONF(NETDEV_UP): eno1: link is not ready
[    7.074944] nouveau 0000:07:00.0: DRM: allocated 1920x1200 fb: 0x60000, bo         (ptrval)
[    7.115953] fbcon: nouveaufb (fb0) is primary device
[    7.116092] Console: switching to colour frame buffer device 240x75
[    7.116119] nouveau 0000:07:00.0: fb0: nouveaufb frame buffer device
[    7.116287] IPv6: ADDRCONF(NETDEV_UP): eno1: link is not ready
[    7.118801] IPv6: ADDRCONF(NETDEV_UP): enp1s0: link is not ready
[    7.176093] [drm] Initialized nouveau 1.3.1 20120801 for 0000:07:00.0 on minor 1
[    7.182244] IPv6: ADDRCONF(NETDEV_UP): enp1s0: link is not ready
[    7.350189] ip6_tables: (C) 2000-2006 Netfilter Core Team
[    7.623792] Ebtables v2.0 registered
[    7.861971] amdgpu 0000:06:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    7.861974] nouveau 0000:07:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    8.407399] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[    8.408001] virbr0: port 1(virbr0-nic) entered blocking state
[    8.408003] virbr0: port 1(virbr0-nic) entered disabled state
[    8.408065] device virbr0-nic entered promiscuous mode
[    8.531688] nf_conntrack version 0.5.0 (65536 buckets, 262144 max)
[    8.561315] PKCS#7 signature not signed with a trusted key
[    8.570072] module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc         (ptrval), val ffffffffc1ebf4c0
[    8.682232] PKCS#7 signature not signed with a trusted key
[    8.691027] module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc         (ptrval), val ffffffffc30144c0
[    9.198859] virbr0: port 1(virbr0-nic) entered blocking state
[    9.198861] virbr0: port 1(virbr0-nic) entered listening state
[    9.280713] virbr0: port 1(virbr0-nic) entered disabled state
[   11.651901] PKCS#7 signature not signed with a trusted key
[   11.662297] module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc         (ptrval), val ffffffffc1ebf4c0
[   11.805017] PKCS#7 signature not signed with a trusted key
[   11.815055] module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc         (ptrval), val ffffffffc30144c0
[   12.348149] random: crng init done
[   13.981579] kauditd_printk_skb: 11 callbacks suppressed
[   13.981580] audit: type=1400 audit(1534659821.327:22): apparmor="STATUS" operation="profile_load" profile="unconfined" name="docker-default" pid=3354 comm="apparmor_parser"
[   14.014219] aufs 4.15-20180219
[   15.494808] Bridge firewalling registered
[   15.598049] Initializing XFRM netlink socket
[   15.629709] Netfilter messages via NETLINK v0.30.
[   15.631912] ctnetlink v0.93: registering with nfnetlink.
[   15.656662] IPv6: ADDRCONF(NETDEV_UP): docker0: link is not ready
[   16.622474] aufs au_opts_verify:1623:dockerd[3382]: dirperm1 breaks the protection by the permission bits on the lower branch
[   16.801685] docker0: port 1(veth9612c34) entered blocking state
[   16.801687] docker0: port 1(veth9612c34) entered disabled state
[   16.801750] device veth9612c34 entered promiscuous mode
[   16.801883] IPv6: ADDRCONF(NETDEV_UP): veth9612c34: link is not ready
[   16.801885] docker0: port 1(veth9612c34) entered blocking state
[   16.801886] docker0: port 1(veth9612c34) entered forwarding state
[   16.802275] docker0: port 1(veth9612c34) entered disabled state
[   16.828231] docker0: port 2(veth37fe111) entered blocking state
[   16.828232] docker0: port 2(veth37fe111) entered disabled state
[   16.828294] device veth37fe111 entered promiscuous mode
[   16.828371] IPv6: ADDRCONF(NETDEV_UP): veth37fe111: link is not ready
[   16.828373] docker0: port 2(veth37fe111) entered blocking state
[   16.828374] docker0: port 2(veth37fe111) entered forwarding state
[   16.828506] docker0: port 2(veth37fe111) entered disabled state
[   17.484658] eth0: renamed from vethba8caa9
[   17.500437] IPv6: ADDRCONF(NETDEV_CHANGE): veth37fe111: link becomes ready
[   17.500483] docker0: port 2(veth37fe111) entered blocking state
[   17.500484] docker0: port 2(veth37fe111) entered forwarding state
[   17.500555] IPv6: ADDRCONF(NETDEV_CHANGE): docker0: link becomes ready
[   17.640438] eth0: renamed from veth985bc90
[   17.672342] IPv6: ADDRCONF(NETDEV_CHANGE): veth9612c34: link becomes ready
[   17.672398] docker0: port 1(veth9612c34) entered blocking state
[   17.672402] docker0: port 1(veth9612c34) entered forwarding state
[   24.565097] e1000e: enp1s0 NIC Link is Up 100 Mbps Full Duplex, Flow Control: Rx/Tx
[   24.565217] e1000e 0000:01:00.0 enp1s0: Link Speed was downgraded by SmartSpeed
[   24.565219] e1000e 0000:01:00.0 enp1s0: 10/100 speed: disabling TSO
[   24.565437] IPv6: ADDRCONF(NETDEV_CHANGE): enp1s0: link becomes ready
[   33.783314] traps: tracker-miner-f[2659] trap int3 ip:7f72934c0c41 sp:7ffe213e88e0 error:0 in libglib-2.0.so.0.5600.1[7f729346f000+113000]
```
```
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
  Name:                    Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz
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
  Max Clock Frequency (MHz):3600                               
  BDFID:                   0                                  
  Compute Unit:            20                                 
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32865096KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32865096KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):3600                               
  BDFID:                   0                                  
  Compute Unit:            20                                 
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    33025324KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    33025324KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 3                  
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
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 26723                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1600                               
  BDFID:                   1536                               
  Compute Unit:            64                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  100664320                          
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
```
```
$ /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP.internal (2574.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Vega 10 XTX [Radeon Vega Frontier Edition]
  Device Topology:                               PCI[ B#6, D#0, F#0 ]
  Max compute units:                             64
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           1600Mhz
  Address bits:                                  64
  Max memory allocation:                         14588628172
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26723
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            17163091968
  Constant buffer size:                          14588628172
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          1703726284
  Max global variable size:                      14588628172
  Max global variable preferred total size:      17163091968
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
  SVM capabilities:                              
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:                                
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:                              
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:                            
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7f6c8d7a4270
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0 
  Driver version:                                2574.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2 
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program
```