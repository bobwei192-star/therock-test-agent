# About cl_amd_copy_buffer_p2p seen in ROCM 1.6 OpenCL..

> **Issue #140**
> **状态**: closed
> **创建时间**: 2017-06-30T22:41:47Z
> **更新时间**: 2019-01-05T23:35:19Z
> **关闭时间**: 2017-07-01T21:29:38Z
> **作者**: oscarbg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/140

## 描述

Just searching in the binary I see new cl_amd_copy_buffer_p2p extensión..
info coming soon?

---

## 评论 (10 条)

### 评论 #1 — gstoner (2017-06-30T23:24:00Z)

It is a new P2P API for OpenCL on large BAR system  which we have been working on that not DirectGMA based.  It will also deal with the copy across the QPI link on Intel Xeon 2p Systems.



On Jun 30, 2017, at 5:41 PM, Oscar Barenys <notifications@github.com<mailto:notifications@github.com>> wrote:


Just searching in the binary I see new cl_amd_copy_buffer_p2p extensión..
info coming soon?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/140>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuW3vJ6wPxGn0jli5oPagYc_972VTks5sJXmsgaJpZM4OLHiH>.



---

### 评论 #2 — oscarbg (2017-07-28T03:40:23Z)

thanks.. 
seems this has made the way to Windows driver 17.7.2..


---

### 评论 #3 — preda (2018-12-29T23:08:37Z)

Where may I find a bit of information, or a sample, about how to use cl_amd_copy_buffer_p2p? (the API methods that are enabled by this extension). Thanks.


---

### 评论 #4 — jlgreathouse (2019-01-05T04:30:07Z)

Hi @preda 

The only function enabled by this extension is `clEnqueueCopyBufferP2PAMD()`, and `clGetDeviceInfo()` is extended with two new parameters that tell you which "P2P neighbors" a target device could use with this function.

I have created a toy application that demonstrates how to use this function to move data between buffers in two separate GPUs. You can find it at https://github.com/jlgreathouse/test_cl_amd_copy_buffer_p2p

---

### 评论 #5 — preda (2019-01-05T11:22:12Z)

@jlgreathouse thank you, this is useful! Unfortunately my system with two Vega64 GPUs apparently doesn't support p2p transfer:

Searching for platforms...
    Using platform: AMD Accelerated Parallel Processing
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #0: 0
PCIe Topology of device 0: 19:0.0
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #1: 0
PCIe Topology of device 1: 67:0.0
Device 0 and device 1 are not P2P neighbors
They cannot be used to test P2P transfers.


---

### 评论 #6 — jlgreathouse (2019-01-05T20:04:30Z)

Looking at the PCIe IDs, I suspect that your devices are on different sockets in a multi-socket system. If this is an Intel system, I'll note that I don't believe this P2P mechanism supports crossing QPI fabric at this time.

If your Vga 64 GPUs are not Large BAR enabled, this will also not work.

---

### 评论 #7 — seesturm (2019-01-05T20:30:30Z)

This issue is already closed, but I'm curious about P2P copy.
Talking about "Large BAR", my BIOS does map the GPU below 4GB. But on boot with 4.20.0 kernel, a remapping by amdgpu can be observed:
```
[    1.395069] ATOM BIOS: 113-BAFFIN_PRO_160513_D5_2G_HY_0_SF_W83
[    1.395093] [drm] vm size is 256 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[    1.395136] amdgpu 0000:41:00.0: BAR 2: releasing [mem 0x90000000-0x901fffff 64bit pref]
[    1.395139] amdgpu 0000:41:00.0: BAR 0: releasing [mem 0x80000000-0x8fffffff 64bit pref]
[    1.395155] pcieport 0000:40:03.1: BAR 15: releasing [mem 0x80000000-0x901fffff 64bit pref]
[    1.395164] pcieport 0000:40:03.1: BAR 15: assigned [mem 0x47e80000000-0x47f3fffffff 64bit pref]
[    1.395167] amdgpu 0000:41:00.0: BAR 0: assigned [mem 0x47e80000000-0x47effffffff 64bit pref]
[    1.395175] amdgpu 0000:41:00.0: BAR 2: assigned [mem 0x47f00000000-0x47f001fffff 64bit pref]
```
Would this allow P2P?
The 4.20 kernel now also provides the CONFIG_PCI_P2PDMA option. Is this needed to allow P2P between the GPUs?

Currently this is all theoretical since there is only a single GPU in my system.

---

### 评论 #8 — preda (2019-01-05T22:18:10Z)

My system is a single-socket, single-CPU, [asrock x299 taichi motherboard](https://www.asrock.com/MB/Intel/X299%20Taichi/index.asp) with  i7-7820X (28 PCIe lanes on the CPU). The 2 Vega64 GPUs are located in the "best" slots on the motherboard which I think are PCIe slots 1 & 3. These are both Gen3, but one runs at 16x and the other at 8x (because of limited PCIe lanes offered by the CPU).

Is it expected for the p2p copy to not work in such a setup?

About large BAR, I do have in BIOS enabled "above 4G decoding". Do I need to do something else to enable "large BAR" -- or is there a way to check the BAR status.

---

### 评论 #9 — preda (2019-01-05T22:25:23Z)

Maybe the "large BAR" is the issue in my case? I see "[drm] Not enough PCI address space for a large BAR".

dmesg | grep BAR
[    4.730144] amdgpu 0000:19:00.0: BAR 2: releasing [mem 0x90000000-0x901fffff 64bit pref]
[    4.730146] amdgpu 0000:19:00.0: BAR 0: releasing [mem 0x80000000-0x8fffffff 64bit pref]
[    4.730157] pcieport 0000:18:00.0: BAR 15: releasing [mem 0x80000000-0x901fffff 64bit pref]
[    4.730159] pcieport 0000:17:00.0: BAR 15: releasing [mem 0x80000000-0x901fffff 64bit pref]
[    4.730160] pcieport 0000:16:00.0: BAR 15: releasing [mem 0x80000000-0x901fffff 64bit pref]
[    4.730174] pcieport 0000:16:00.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[    4.730175] pcieport 0000:16:00.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[    4.730176] pcieport 0000:17:00.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[    4.730177] pcieport 0000:17:00.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[    4.730178] pcieport 0000:18:00.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[    4.730179] pcieport 0000:18:00.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[    4.730180] amdgpu 0000:19:00.0: BAR 0: no space for [mem size 0x200000000 64bit pref]
[    4.730181] amdgpu 0000:19:00.0: BAR 0: failed to assign [mem size 0x200000000 64bit pref]
[    4.730182] amdgpu 0000:19:00.0: BAR 2: no space for [mem size 0x00200000 64bit pref]
[    4.730183] amdgpu 0000:19:00.0: BAR 2: failed to assign [mem size 0x00200000 64bit pref]
[    4.730217] [drm] Not enough PCI address space for a large BAR.
[    4.730219] amdgpu 0000:19:00.0: BAR 0: assigned [mem 0x80000000-0x8fffffff 64bit pref]
[    4.730224] amdgpu 0000:19:00.0: BAR 2: assigned [mem 0x90000000-0x901fffff 64bit pref]
[    4.730257] [drm] Detected VRAM RAM=8176M, BAR=256M
[    5.284007] caller pci_map_rom+0x71/0x1c0 mapping multiple BARs
[    5.284056] amdgpu 0000:67:00.0: BAR 2: releasing [mem 0xd0000000-0xd01fffff 64bit pref]
[    5.284057] amdgpu 0000:67:00.0: BAR 0: releasing [mem 0xc0000000-0xcfffffff 64bit pref]
[    5.284069] pcieport 0000:66:00.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[    5.284071] pcieport 0000:65:00.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[    5.284072] pcieport 0000:64:00.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[    5.284087] pcieport 0000:64:00.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[    5.284088] pcieport 0000:64:00.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[    5.284090] pcieport 0000:65:00.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[    5.284090] pcieport 0000:65:00.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[    5.284092] pcieport 0000:66:00.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[    5.284093] pcieport 0000:66:00.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[    5.284094] amdgpu 0000:67:00.0: BAR 0: no space for [mem size 0x200000000 64bit pref]
[    5.284095] amdgpu 0000:67:00.0: BAR 0: failed to assign [mem size 0x200000000 64bit pref]
[    5.284096] amdgpu 0000:67:00.0: BAR 2: no space for [mem size 0x00200000 64bit pref]
[    5.284097] amdgpu 0000:67:00.0: BAR 2: failed to assign [mem size 0x00200000 64bit pref]
[    5.284133] [drm] Not enough PCI address space for a large BAR.
[    5.284134] amdgpu 0000:67:00.0: BAR 0: assigned [mem 0xc0000000-0xcfffffff 64bit pref]
[    5.284140] amdgpu 0000:67:00.0: BAR 2: assigned [mem 0xd0000000-0xd01fffff 64bit pref]
[    5.284155] [drm] Detected VRAM RAM=8176M, BAR=256M

---

### 评论 #10 — preda (2019-01-05T23:35:19Z)

It seems I fixed the large BAR problem, but still no success with the p2p copy (see below)

~$ dmesg | grep BAR
[    4.801949] amdgpu 0000:19:00.0: BAR 2: releasing [mem 0xb0000000-0xb01fffff 64bit pref]
[    4.801950] amdgpu 0000:19:00.0: BAR 0: releasing [mem 0xa0000000-0xafffffff 64bit pref]
[    4.801962] pcieport 0000:18:00.0: BAR 15: releasing [mem 0xa0000000-0xb01fffff 64bit pref]
[    4.801964] pcieport 0000:17:00.0: BAR 15: releasing [mem 0xa0000000-0xb01fffff 64bit pref]
[    4.801965] pcieport 0000:16:00.0: BAR 15: releasing [mem 0xa0000000-0xb01fffff 64bit pref]
[    4.801980] pcieport 0000:16:00.0: BAR 15: assigned [mem 0x381000000000-0x3812ffffffff 64bit pref]
[    4.801981] pcieport 0000:17:00.0: BAR 15: assigned [mem 0x381000000000-0x3812ffffffff 64bit pref]
[    4.801982] pcieport 0000:18:00.0: BAR 15: assigned [mem 0x381000000000-0x3812ffffffff 64bit pref]
[    4.801984] amdgpu 0000:19:00.0: BAR 0: assigned [mem 0x381000000000-0x3811ffffffff 64bit pref]
[    4.801989] amdgpu 0000:19:00.0: BAR 2: assigned [mem 0x381200000000-0x3812001fffff 64bit pref]
[    4.802048] [drm] Detected VRAM RAM=8176M, BAR=8192M
[    5.367624] caller pci_map_rom+0x71/0x1c0 mapping multiple BARs
[    5.367677] amdgpu 0000:67:00.0: BAR 2: releasing [mem 0xd0000000-0xd01fffff 64bit pref]
[    5.367678] amdgpu 0000:67:00.0: BAR 0: releasing [mem 0xc0000000-0xcfffffff 64bit pref]
[    5.367690] pcieport 0000:66:00.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[    5.367691] pcieport 0000:65:00.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[    5.367692] pcieport 0000:64:00.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[    5.367707] pcieport 0000:64:00.0: BAR 15: assigned [mem 0x382000000000-0x3822ffffffff 64bit pref]
[    5.367709] pcieport 0000:65:00.0: BAR 15: assigned [mem 0x382000000000-0x3822ffffffff 64bit pref]
[    5.367710] pcieport 0000:66:00.0: BAR 15: assigned [mem 0x382000000000-0x3822ffffffff 64bit pref]
[    5.367711] amdgpu 0000:67:00.0: BAR 0: assigned [mem 0x382000000000-0x3821ffffffff 64bit pref]
[    5.367717] amdgpu 0000:67:00.0: BAR 2: assigned [mem 0x382200000000-0x3822001fffff 64bit pref]
[    5.367765] [drm] Detected VRAM RAM=8176M, BAR=8192M

~$ ./test_cl_amd_copy_buffer_p2p/test_p2p 
Searching for platforms...
    Using platform: AMD Accelerated Parallel Processing
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #0: 0
PCIe Topology of device 0: 19:0.0
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #1: 0
PCIe Topology of device 1: 67:0.0
Device 0 and device 1 are not P2P neighbors
They cannot be used to test P2P transfers.
Exiting!

---
