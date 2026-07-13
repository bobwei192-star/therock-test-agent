# I need help understanding the argument format for the "ip_block_mask" kernel option

- **Issue #:** 759
- **State:** closed
- **Created:** 2019-04-11T04:21:58Z
- **Updated:** 2023-12-18T18:52:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/759

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