# PCIe Bus Error when running vector_copy sample

> **Issue #32**
> **状态**: closed
> **创建时间**: 2016-09-25T17:19:40Z
> **更新时间**: 2016-09-29T11:45:42Z
> **关闭时间**: 2016-09-27T15:01:51Z
> **作者**: Maratyszcza
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/32

## 描述

I followed the README to install ROCm driver. However, when I try to run `vector_copy` sample, the program hangs, and I see report about a PCIe error on `dmesg`.

Configuration:
- Intel Core i7 6700K on GIGABYTE GA-Z170-HD3 (rev. 1.0) motherboard with Intel Z170 chipset.
- AMD Radeon Fury Nano GPU in the PCIe x16 slot
- Ubuntu 16.04 on AMD64 architecture
- `uname -r`: `4.4.0-kfd-compute-rocm-rel-1.2-31`

Kernel log (`dmesg`) messages after running the `vector_copy` sample:

```
[  942.180230] pcieport 0000:00:1c.4: AER: Uncorrected (Fatal) error received: id=00e4
[  942.180239] pcieport 0000:00:1c.4: PCIe Bus Error: severity=Uncorrected (Fatal), type=Transaction Layer, id=00e4(Receiver ID)
[  942.180327] pcieport 0000:00:1c.4:   device [8086:a114] error status/mask=00040000/00000000
[  942.180392] pcieport 0000:00:1c.4:    [18] Malformed TLP          (First)
[  942.180444] pcieport 0000:00:1c.4:   TLP Header: 6c000002 06000000 0000000f b76e6008
[  942.180511] pcieport 0000:00:1c.4: broadcast error_detected message
[  942.180513] amdgpu 0000:06:00.0: device has no AER-aware driver
[  942.180514] snd_hda_intel 0000:06:00.1: device has no AER-aware driver
[  943.188998] pcieport 0000:00:1c.4: Root Port link has been reset
[  943.189001] pcieport 0000:00:1c.4: AER: Device recovery failed
```

`/opt/rocm/rocm-smi -a` output:

```
===================   ROCm System Management Interface   ===================
============================================================================
GPU[0]      : GPU ID: 0x7300
============================================================================
============================================================================
GPU[0]      : Temperature: 511.0c
============================================================================
============================================================================
GPU[0]      : Unable to determine current clocks. Check dmesg or GPU temperature
============================================================================
GPU[0]      : Fan Level: 255 (100.0)%
============================================================================
============================================================================
GPU[0]      : Current PowerPlay Level: auto
============================================================================
============================================================================
GPU[0]      : Current OverDrive value: 0%
============================================================================
============================================================================
GPU[0]      : Supported GPU clock frequencies on GPU0
GPU[0]      : 0: 300Mhz
GPU[0]      : 1: 508Mhz
GPU[0]      : 2: 717Mhz
GPU[0]      : 3: 874Mhz
GPU[0]      : 4: 911Mhz
GPU[0]      : 5: 944Mhz
GPU[0]      : 6: 974Mhz
GPU[0]      : 7: 1000Mhz
GPU[0]      :
GPU[0]      : Supported GPU Memory clock frequencies on GPU0
GPU[0]      : 0: 500Mhz
GPU[0]      :
============================================================================
===================          End of ROCm SMI Log         ===================
```


---

## 评论 (9 条)

### 评论 #1 — almson (2016-09-27T07:15:47Z)

Perhaps you aren't using the first motherboard slot? Looks like the second may be wired through the chipset.

How were you able to install ROCm on Ubuntu 16.04?


---

### 评论 #2 — gstoner (2016-09-27T11:42:08Z)

We found the issue,  it is system bios is not properly configuring the CPU correctly and enabling PCIe Platform Atomics.  Gigabyte has to fix the SBIOS.

greg

On Sep 27, 2016, at 2:15 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:

Perhaps you aren't using the first motherboard slot? Looks like the second may be wired through the chipset.

How were you able to install ROCm on Ubuntu 16.04?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/32#issuecomment-249785063, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuVCH7V-tmzC_NeYAzK89ggZQF_d6ks5quMKjgaJpZM4KF854.


---

### 评论 #3 — Maratyszcza (2016-09-27T12:57:10Z)

@gstoner Would you report it to Gigabyte?


---

### 评论 #4 — Maratyszcza (2016-09-27T15:01:51Z)

@gstoner @almson is right! The card was installed into the second PCIe slot (PCIe x16 slot running at x4 speed according to MB docs). After I switched it into the first slot, it seems to work fine.

However, a more user-friendly diagnostic message would certainly help!


---

### 评论 #5 — almson (2016-09-28T13:32:38Z)

@gstoner Will atomics work through the CPU->DMI->Chipset->PCIe path that's used for the 2nd slot of that motherboard?


---

### 评论 #6 — gstoner (2016-09-28T15:16:43Z)

PCIe Atomics only work with PCIe Gen 3

Here is what Atomic Operations do

Atomic Operations – Goal: Support SMP-type operations across a PCIe network to allow for things like offloading tasks between CPU cores and accelerators like a GPU. The spec says this enables advanced synchronization mechanisms that are particularly useful with multiple producers or consumers that need to be synchronized in a non-blocking fashion. Three new atomic non-posted requests were added, plus the corresponding completion (the address must be naturally aligned with the operand size or the TLP is malformed):
1. ```
   Fetch and Add – uses one operand as the “add” value. Reads the target location, adds the operand, and then writes the result back to the original location.
   ```
2. ```
   Unconditional Swap – uses one operand as the “swap” value. Reads the target location and then writes the swap value to it.
   ```
3. ```
   Compare and Swap – uses 2 operands: first data is compare value, second is swap value. Reads the target location, checks it against the compare value and, if equal, writes the swap value to the target location.
   ```
4. ```
   AtomicOpCompletion–newcompletiontogivetheresultsofanatomicrequestand indicate that the atomicity of the transaction has been maintained.
   ```

Since AtomicOps are not locked they don’t have the performance downsides of the PCI locked protocol. Compared to locked cycles, they provide “lower latency, higher scalability, advanced synchronization algorithms, and dramatically lower impact on other PCIe traffic.” The lock mechanism can still be used across a bridge to PCIe to achieve the desired operation.

AtomicOps can go from device to device, device to host, or host to device. Each completer indicates whether it supports this capability and guarantees atomic access if it does. The ability to route AtomicOps is also indicated in the registers for a given port.

On Sep 28, 2016, at 8:32 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:

@gstonerhttps://github.com/gstoner Will atomics work through the CPU->DMI->Chipset->PCIe path that's used for the 2nd slot of that motherboard?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/32#issuecomment-250167350, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuRTnGaigmHK63iPMFj-UDHhw3RGnks5qumx3gaJpZM4KF854.


---

### 评论 #7 — almson (2016-09-29T11:38:15Z)

Thank you for the background information. Can you tell us what hardware scenarios are or aren't supported? Here is an [illustration of the Z170 chipset](http://arstechnica.com/gadgets/2015/08/intels-100-series-chipsets-ddr4-pcie-3-0-ssds-and-other-skylake-supplements/) (first image in the article). As you can see, some PCIe slots may be connected through the Z170 PCH. It seems that atomics do not work in this case. Is this a hardware or a BIOS limitation? Do you plan to create a utility to analyze which slots are compatible, or a database of hardware that can be consulted prior to purchase? Do PCIe switches (such as those in the ASUS X99E-WS) always work?


---

### 评论 #8 — almson (2016-09-29T11:42:33Z)

To be clear, Z170 advertises PCIe 3.0.


---

### 评论 #9 — gstoner (2016-09-29T11:45:41Z)

The issue was it was in the wrong slot,   He had the device in x16 slot that was x4 which could be not comping off the main CPU.   Which could be Gen2 slot or BIOS is not configured correctly.   The CPU support PCIe Gen3 with Atomics

greg
On Sep 29, 2016, at 6:42 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:

To be clear, Z170 advertises PCIe 3.0.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/32#issuecomment-250443161, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuaccDnOoU8qjQa3MEynsn-4FEKn8ks5qu6QpgaJpZM4KF854.


---
