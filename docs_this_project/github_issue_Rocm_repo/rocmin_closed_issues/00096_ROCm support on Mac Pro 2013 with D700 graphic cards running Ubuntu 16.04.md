# ROCm support on Mac Pro 2013 with D700 graphic cards running Ubuntu 16.04

- **Issue #:** 96
- **State:** closed
- **Created:** 2017-03-12T04:33:46Z
- **Updated:** 2023-11-03T22:45:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/96

Hi:
  Not sure if this is an issue because D700 graphic cards were customized by Apple and was not officially listed on the supported hardware.  Anyway, I tried to install ROCm 1.4 on Mac Pro 2013 with two D700 cards.  Got some progress but not had the luck to connect to GPU.  Here are the outputs from the verification sample program, 

**vector_copy**:

CPU Node [0] has no GPU connected
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent failed.

and here are excerpts of **dmesg dump related to radeon**:
.
.
[    2.616360] [drm] radeon kernel modesetting enabled.
.
.
[    2.622914] fb: switching to radeondrmfb from EFI VGA
.
.
[    2.623184] radeon 0000:06:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0x0000
[    2.623194] radeon 0000:06:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0x0000
[    2.623223] [drm:radeon_get_bios [radeon]] *ERROR* Unable to locate a BIOS ROM
[    2.623225] radeon 0000:06:00.0: Fatal error during GPU init
[    2.623227] [drm] radeon: finishing device.
[    2.623228] [TTM] Memory type 2 has not been initialized
[    2.630407] radeon: probe of 0000:06:00.0 failed with error -22
.
.
[   13.075063] radeon 0000:02:00.0: enabling device (0006 -> 0007)
.
.
[   13.075287] radeon 0000:02:00.0: VRAM: 6144M 0x0000000000000000 - 0x000000017FFFFFFF (6144M used)
[   13.075289] radeon 0000:02:00.0: GTT: 2048M 0x0000000180000000 - 0x00000001FFFFFFFF
[   13.075289] [drm] Detected VRAM RAM=6144M, BAR=256M
[   13.075290] [drm] RAM width 384bits DDR
[   13.075317] [TTM] Zone  kernel: Available graphics memory: 49459887 kiB
[   13.075319] [TTM] Initializing pool allocator
[   13.075322] [TTM] Initializing DMA pool allocator
[   13.075334] [drm] radeon: 6144M of VRAM memory ready
[   13.075335] [drm] radeon: 2048M of GTT memory ready.
.
.
[   15.400942] [drm] radeon: dpm initialized
.
.
[   15.654753] radeon 0000:02:00.0: WB enabled
[   15.654755] radeon 0000:02:00.0: fence driver on ring 0 use gpu addr 0x0000000180000c00 and cpu addr 0xffff881032f07c00
[   15.654756] radeon 0000:02:00.0: fence driver on ring 1 use gpu addr 0x0000000180000c04 and cpu addr 0xffff881032f07c04
[   15.654757] radeon 0000:02:00.0: fence driver on ring 2 use gpu addr 0x0000000180000c08 and cpu addr 0xffff881032f07c08
[   15.654758] radeon 0000:02:00.0: fence driver on ring 3 use gpu addr 0x0000000180000c0c and cpu addr 0xffff881032f07c0c
[   15.654759] radeon 0000:02:00.0: fence driver on ring 4 use gpu addr 0x0000000180000c10 and cpu addr 0xffff881032f07c10
[   15.654907] radeon 0000:02:00.0: fence driver on ring 5 use gpu addr 0x0000000000075a18 and cpu addr 0xffffc90007635a18
[   15.670313] snd_hda_codec_cirrus hdaudioC0D0: autoconfig for CS4208: line_outs=1 (0x13/0x0/0x0/0x0/0x0) type:line
[   15.670316] snd_hda_codec_cirrus hdaudioC0D0:    speaker_outs=1 (0x12/0x0/0x0/0x0/0x0)
[   15.670317] snd_hda_codec_cirrus hdaudioC0D0:    hp_outs=1 (0x10/0x0/0x0/0x0/0x0)
[   15.670318] snd_hda_codec_cirrus hdaudioC0D0:    mono: mono_out=0x0
[   15.670319] snd_hda_codec_cirrus hdaudioC0D0:    dig-out=0x21/0x0
[   15.670319] snd_hda_codec_cirrus hdaudioC0D0:    inputs:
[   15.670321] snd_hda_codec_cirrus hdaudioC0D0:      Mic=0x18
[   15.674915] radeon 0000:02:00.0: fence driver on ring 6 use gpu addr 0x0000000180000c18 and cpu addr 0xffff881032f07c18
[   15.674917] radeon 0000:02:00.0: fence driver on ring 7 use gpu addr 0x0000000180000c1c and cpu addr 0xffff881032f07c1c
[   15.674923] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   15.674923] [drm] Driver supports precise vblank timestamp query.
[   15.674924] radeon 0000:02:00.0: radeon: MSI limited to 32-bit
[   15.674944] radeon 0000:02:00.0: radeon: using MSI.
[   15.674965] [drm] radeon: irq initialized.
.
.
[   17.875995] radeon 0000:02:00.0: No connectors reported connected with modes
[   17.876000] [drm] Cannot find any crtc or sizes - going 1024x768
[   17.876442] [drm] fb mappable at 0x805D8000
[   17.876444] [drm] vram apper at 0x80000000
[   17.876444] [drm] size 3145728
[   17.876445] [drm] fb depth is 24
[   17.876446] [drm]    pitch is 4096
[   17.876750] Console: switching to colour frame buffer device 128x48
[   17.878442] radeon 0000:02:00.0: fb0: radeondrmfb frame buffer device
[   17.912425] wlan0: Broadcom BCM43a0 802.11 Hybrid Wireless Controller 6.30.223.271 (r587334)
[   17.927436] [drm] Initialized radeon 2.46.0 20080528 for 0000:02:00.0 on minor 0
.
.
Here are from **lspci**:

02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Tahiti XT [Radeon HD 7970/8970 OEM / R9 280X] (prog-if 00 [VGA controller])
        Subsystem: Apple Inc. Tahiti XT [Radeon HD 7970/8970 OEM / R9 280X]
        Physical Slot: 3-3
        Flags: bus master, fast devsel, latency 0, IRQ 85
        Memory at 80000000 (64-bit, prefetchable) [size=256M]
        Memory at a0700000 (64-bit, non-prefetchable) [size=256K]
        I/O ports at 3000 [size=256]
        Expansion ROM at a0740000 [disabled] [size=128K]
        Capabilities: <access denied>
        Kernel driver in use: radeon
        Kernel modules: radeon

02:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Tahiti XT HDMI Audio [Radeon HD 7970 Series]
        Subsystem: Apple Inc. Tahiti XT HDMI Audio [Radeon HD 7970 Series]
        Physical Slot: 3-3
        Flags: bus master, fast devsel, latency 0, IRQ 82
        Memory at a0760000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Tahiti XT [Radeon HD 7970/8970 OEM / R9 280X] (prog-if 00 [VGA controller])
        Subsystem: Apple Inc. Tahiti XT [Radeon HD 7970/8970 OEM / R9 280X]
        Physical Slot: 5-3
        Flags: fast devsel, IRQ 65
        Memory at 90000000 (64-bit, prefetchable) [size=256M]
        Memory at a0600000 (64-bit, non-prefetchable) [size=256K]
        I/O ports at 2000 [size=256]
        Expansion ROM at a0640000 [disabled] [size=128K]
        Capabilities: <access denied>
        Kernel modules: radeon

06:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Tahiti XT HDMI Audio [Radeon HD 7970 Series]
        Subsystem: Apple Inc. Tahiti XT HDMI Audio [Radeon HD 7970 Series]
        Physical Slot: 5-3
        Flags: bus master, fast devsel, latency 0, IRQ 84
        Memory at a0660000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

Any possibilities to make my Mac Pro ROCk?  Thanks!