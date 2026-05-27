# I need help understanding the argument format for the "ip_block_mask" kernel option

> **Issue #759**
> **状态**: closed
> **创建时间**: 2019-04-11T04:21:58Z
> **更新时间**: 2023-12-18T18:52:57Z
> **关闭时间**: 2023-12-18T18:52:57Z
> **作者**: lsimplify
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/759

## 描述

My GPU is crashing during mining with ROC version 2.2, and I would like to disable the IP block that appears to be interfering with the recovery by using this kernel module parm: `ip_block_mask:IP Block Mask (all blocks enabled (default)) (uint)`

I'm assuming that disabling the UVD Block will prevent the RX 580 from crashing.

I need help understanding the argument format for this kernel option for the purpose of disabling some of the blocks.

Btw, I've noticed the IP block layout is different between this RX580 and the Vega 64. Is it possible to disable blocks on a individual device basis?

Here is some bug information:
```
$ uname -rv
5.0.1-050001-generic #201903100732 SMP Sun Mar 10 07:33:53 UTC 2019
```

```
$ lspci -s 0000:20:00.0
20:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X] (rev e7)
```

```dmesg
$ dmseg -e
...
[Apr10 21:21] gmc_v8_0_process_interrupt: 2 callbacks suppressed
[  +0.000006] amdgpu 0000:20:00.0: GPU fault detected: 147 0x00004801 for process  pid 0 thread  pid 0
[  +0.000005] amdgpu 0000:20:00.0:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x0C500000
[  +0.000002] amdgpu 0000:20:00.0:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x12048001
[  +0.000002] amdgpu 0000:20:00.0: VM fault (0x01, vmid 9, pasid 32780) at page 206569472, read from 'TC4' (0x54433400) (72)
[  +0.001018] Evicting PASID 32780 queues
[  +9.002235] qcm fence wait loop timeout expired
[  +0.000005] The cp might be in an unrecoverable state due to an unsuccessful queues preemption
[  +0.000012] amdgpu 0000:20:00.0: GPU reset begin!
[  +0.000004] Evicting PASID 32781 queues
[  +0.000001] Failed to evict process queues
[  +0.000002] Failed to suspend process 32781
[  +0.000002] Evicting PASID 32780 queues
[  +0.000861] Evicting PASID 32780 queues
[  +0.006300] Evicting PASID 32782 queues
[  +0.000002] Failed to evict process queues
[  +0.000002] Failed to suspend process 32782
[  +0.437877] amdgpu 0000:20:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring kiq_2.1.0 test failed (-110)
[  +0.000050] [drm:gfx_v8_0_hw_fini [amdgpu]] *ERROR* KCQ disable failed
[  +0.244698] cp is busy, skip halt cp
[  +0.244410] rlc is busy, skip halt rlc
[  +0.001026] amdgpu 0000:20:00.0: GPU pci config reset
[  +0.108658] amdgpu 0000:20:00.0: GPU reset succeeded, trying to resume
[  +0.001605] [drm] PCIE GART of 256M enabled (table at 0x000000F4001D5000).
[  +0.000056] [drm:amdgpu_device_gpu_recover [amdgpu]] *ERROR* VRAM is lost!
[  +1.040532] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012513] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012519] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012513] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012500] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012505] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012512] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012504] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012515] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +1.012489] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, trying to reset the VCPU!!!
[  +0.019906] [drm:uvd_v6_0_start [amdgpu]] *ERROR* UVD not responding, giving up!!!
[  +0.000042] [drm:amdgpu_device_ip_set_powergating_state [amdgpu]] *ERROR* set_powergating_state of IP block <uvd_v6_0> failed -1
[  +0.264129] amdgpu 0000:20:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring uvd test failed (-110)
[  +0.000040] [drm:amdgpu_device_ip_resume_phase2 [amdgpu]] *ERROR* resume of IP block <uvd_v6_0> failed -110
[  +0.000046] amdgpu 0000:20:00.0: GPU reset(1) failed
[  +0.000205] amdgpu 0000:20:00.0: GPU reset end with ret = -110
[  +0.540503] [drm] Fence fallback timer expired on ring sdma0
[  +0.511980] [drm] Fence fallback timer expired on ring sdma0
[  +0.512367] [drm] Fence fallback timer expired on ring sdma0
[Apr10 21:26] [drm] Fence fallback timer expired on ring sdma1
[  +2.847887] [drm] Fence fallback timer expired on ring sdma1
[Apr10 21:27] [drm] Fence fallback timer expired on ring sdma1
[  +1.951911] [drm] Fence fallback timer expired on ring sdma1
...
```

---

## 评论 (4 条)

### 评论 #1 — magikfingerz (2019-09-03T01:35:21Z)

amdgpu.ip_block_mask is a number representing a mask of 16 bits, each bit allows activate(1) or deactivate(0) certain feature of the GPU. You need to figure out what is the bit controlling the UVD, I will thell you what I did to find it:
1.- check the output of the following command: sudo dmesg | grep block

look for a block of messages like this:

[drm] add ip block number 0 <vi_common>
[drm] add ip block number 1 <gmc_v8_0>
[drm] add ip block number 2 <cz_ih>
... etc.

2.- Look for the number of the feature you need to disable (in my case uvd_v6_0 was the problem)
DO NOT COPY the number from another computer, because numbers vary even with same hardware, so, this must be done in your computer.

3.- Once you have the number you want to disable  (for example 6) then write down a binary number of 16 digits, like this:
1111111111111111

4.- Now, counting from right to left locate the digit of the feature you want to disable and change it for a zero(the first digit is for feature number 0, the next for feature number 1, the next for feature number 2 and so on) so, if you want to disable a feature with the number six your binary number changes to:
1111111110111111.

5.- You're almost done, now this number needs to be converted to an hex number, you can do it with any scientific calculator or you can install one in your linux (for example galculator), with binary mode enabled enter the binary number in the calc and change mode to hex numbers, in this example, the result is FFFFFFBF, so this is the mask you need to enter in your kernel with the following format(using lowercases):

amdgpu.ip_block_mask=0xffffffbf

and that's it, hope this solve your problem :)


---

### 评论 #2 — nottux (2019-09-11T19:38:35Z)

`*ERROR* resume of IP block <uvd_v6_0> failed` this error has been resolved with kernel `5.3.0-rc1` and onwards, at least for my RX 540 gpu

---

### 评论 #3 — tasso (2023-12-12T20:12:33Z)

Is this still an issue?  If not, can we please close it?  Thanks!

---

### 评论 #4 — tasso (2023-12-18T18:52:57Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request. If this is still an issue, please file a new ticket and we will be more than happy to investigate it. Thanks!

---
