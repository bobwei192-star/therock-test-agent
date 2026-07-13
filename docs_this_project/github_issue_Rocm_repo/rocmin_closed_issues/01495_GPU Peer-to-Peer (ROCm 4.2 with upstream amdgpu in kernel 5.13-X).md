# GPU Peer-to-Peer (ROCm 4.2 with upstream amdgpu in kernel 5.13-X)

- **Issue #:** 1495
- **State:** closed
- **Created:** 2021-06-19T13:11:36Z
- **Updated:** 2022-02-08T10:17:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/1495

ROCm 4.2 reports P2P as available for my machine with RX Vega 64 and Radeon VII in it. `rocm-bandwidth-test` therefore tries to measure the bandwidth between the GPUs, which causes immediate display corruption due to page faults and following GPU reset (see system log below).

Is P2P supposed to function in this configuration? Is any special configuration necessary to make it work?

While I hope P2P is (or can be) supported in this configuration, ROCm probably should avoid advertising it in situations where it can render the machine unusable.

> Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma0] address:0x0000000000048000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma0] address:0x00000000004d0000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma0] address:0x0000000000958000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma0] address:0x0000000000de0000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma0] address:0x0000000001268000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma0] address:0x00000000016f0000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x0000000000048000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x00000000004d0000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x0000000000958000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x0000000000de0000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x0000000001268000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma0] address:0x0000000001b78000 src_id:247 ring:3 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x00000000016f0000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x0000000001b78000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x0000000002000000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x0000000002488000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma1] address:0x0000000002910000 src_id:247 ring:2 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Jun 19 14:47:52 Machine kernel: amdgpu 0000:10:00.0: amdgpu: [sdma0] address:0x0000000002000000 src_id:247 ring:3 vmid:8 pasid:32786, for process rocm-bandwidth- pid 4905 thread rocm-bandwidth- pid 4905
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:157 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x0000000000664000 from IH client 0x12 (VMC)
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x0000013B
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: MP0 (0x0)
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x1
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x5
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0x3
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x1
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:157 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x0000000000664000 from IH client 0x12 (VMC)
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: MP0 (0x0)
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:221 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x0000000000480000 from IH client 0x1b (UTCL2)
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x000009BA
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: CPF (0x4)
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x0
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x5
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0xb
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x1
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: wait for kiq fence error: 0.
Jun 19 14:48:03 Machine kernel: [drm:amdgpu_job_timedout [amdgpu]] *ERROR* ring page1 timeout, signaled seq=48225, emitted seq=48227
Jun 19 14:48:03 Machine kernel: [drm:amdgpu_job_timedout [amdgpu]] *ERROR* Process information: process  pid 0 thread  pid 0
Jun 19 14:48:03 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: GPU reset begin!
Jun 19 14:48:03 Machine kernel: amdgpu 0000:0d:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring kiq_2.1.0 test failed (-110)
Jun 19 14:48:03 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: BACO reset
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: GPU reset succeeded, trying to resume
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring gfx uses VM inv eng 0 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring sdma0 uses VM inv eng 0 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring page0 uses VM inv eng 1 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring sdma1 uses VM inv eng 4 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring page1 uses VM inv eng 5 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring uvd_0 uses VM inv eng 6 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring vce0 uses VM inv eng 9 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring vce1 uses VM inv eng 10 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: ring vce2 uses VM inv eng 11 on hub 1
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: recover vram bo from shadow start
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: recover vram bo from shadow done
Jun 19 14:48:04 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: GPU reset(1) succeeded!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Jun 19 14:48:04 Machine kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!