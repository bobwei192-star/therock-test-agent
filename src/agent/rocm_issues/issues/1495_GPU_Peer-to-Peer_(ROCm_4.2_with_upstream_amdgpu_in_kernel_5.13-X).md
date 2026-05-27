# GPU Peer-to-Peer (ROCm 4.2 with upstream amdgpu in kernel 5.13-X)

> **Issue #1495**
> **状态**: closed
> **创建时间**: 2021-06-19T13:11:36Z
> **更新时间**: 2022-02-08T10:17:40Z
> **关闭时间**: 2022-02-08T10:17:39Z
> **作者**: FilipVaverka
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1495

## 描述

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

---

## 评论 (24 条)

### 评论 #1 — ROCmSupport (2021-06-23T04:59:08Z)

Thanks @FilipVaverka for reaching out.
Let me take a look at this.

---

### 评论 #2 — ROCmSupport (2021-07-09T03:23:50Z)

Hi @FilipVaverka 
Can you please share below logs for better understanding of the problem.

--> Collect cosole log from following run
<shell-prompt> /opt/rocm/bin/rocminfo

--> Collect cosole log from following run
<shell-prompt> /opt/rocm/bin/rocm-bandwidth-test  -t
(if rocm-bandwidth-test is not available in the system, you can install it by "sudo apt install rocm-bandwidth-test")

---

### 评论 #3 — FilipVaverka (2021-07-09T07:55:34Z)

Here are requested logs:
- [rocminfo_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/6789730/rocminfo_log.txt)
- [rocm_bandwidth_test_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/6789731/rocm_bandwidth_test_log.txt)
- [clinfo_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/6789733/clinfo_log.txt)


---

### 评论 #4 — ROCmSupport (2021-07-09T10:08:38Z)

Thanks for the logs.
I have shared to developer. Thank you.

---

### 评论 #5 — seesturm (2021-07-09T20:36:33Z)

https://github.com/ROCm-Developer-Tools/HIP/issues/2214 is related to this.

---

### 评论 #6 — ROCmSupport (2021-07-12T05:14:24Z)

Hi @FilipVaverka 
Looking at the logs of RBT I don't see a reason as to why RBT run should fail. 
One thing to try is to run RBT in node-to-node scheme for following scenarios:

    RBT -s 0 -d 1
    RBT -s 0 -d 2
    RBT -s 1 -d 2
    RBT -s 1 -d 1
    RBT -s 2 -d 2

If my hunch is correct, one of the intra-device runs should fail (RBT -s 1 -d 1 or RBT -s 2 -d 2). Please update ticket with your observations including logs.
Thank you.

---

### 评论 #7 — FilipVaverka (2021-07-12T07:07:52Z)

Neither of intra-device runs fail. It is Device-to-Device communication that causes issues:
- [rbt_s_2_d_1_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/6799189/rbt_s_2_d_1_log.txt) - while this run causes bunch of SDMA messages in the system log [rbt_s_2_d_1_sys_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/6799242/rbt_s_2_d_1_sys_log.txt)
- [rbt_s_1_d_2_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/6799196/rbt_s_1_d_2_log.txt) - causes similar messages, but also causes range of error in system log and restarts the GPU on which graphics environment is running. [rbt_s_1_d_2_sys_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/6799262/rbt_s_1_d_2_sys_log.txt) (here I first ran 2->1 and then 1->2 with errors)

---

### 评论 #8 — FilipVaverka (2021-08-20T18:27:45Z)

So I swapped my RX Vega 64 for RX 6900 XT. The good news is this new configuration can successfully run through RBT! However I still see load of AMDGPU messages:

> Aug 20 20:13:56 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
Aug 20 20:13:56 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: [sdma0] address:0x0000000000048000 src_id:247 ring:2 vmid:8 pasid:32795, for process rocm-bandwidth- pid 6692 thread rocm-bandwidth- pid 6692

However, there are no page fault errors (I assume) which I did get with RX Vega 64 (and which I suspect led to GPU reset):

> Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: in page starting at address 0x0000000000664000 from IH client 0x12 (VMC)
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: Faulty UTCL2 client ID: MP0 (0x0)
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: MORE_FAULTS: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: WALKER_ERROR: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: PERMISSION_FAULTS: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: MAPPING_ERROR: 0x0
Jun 19 14:47:52 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: RW: 0x0
Jun 19 14:47:53 Machine kernel: amdgpu 0000:0d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:221 vmid:0 pasid:0, for process pid 0 thread pid 0)

While there are number of differences between RX Vega 64 and RX 6900 XT... is it possible that there are issues with asymemtric P2P, where one GPU has different amount of VRAM? Former configuration had 8GB Vega and 16GB R7, whereas now both GPUs have 16GB of VRAM.

I don't think we should mark this as resolved yet as this is not solution, rather observation.

EDIT 1: While I'm yet to test whether transferred data are actually valid (assuming RBT doesn't check that), here are RBT results:

> RocmBandwidthTest Version: 2.5.1

          Launch Command is: rocm-bandwidth-test (rocm_bandwidth -a + rocm_bandwidth -A)


          Device: 0,  AMD Ryzen 9 3950X 16-Core Processor
          Device: 1,  Vega 20 [Radeon VII],  GPU-9f50716172fd5d40,  0d:0.0
          Device: 2,  Navi 21 [Radeon RX 6800/6800 XT / 6900 XT],  GPU-XX,  10:0.0

          Inter-Device Access

          D/D       0         1         2         

          0         1         1         1         

          1         1         1         1         

          2         1         1         1         


          Inter-Device Numa Distance

          D/D       0         1         2         

          0         0         20        20        

          1         20        0         40        

          2         20        40        0         


          Unidirectional copy peak bandwidth GB/s

          D/D       0           1           2           

          0         N/A         7.177       14.106      

          1         7.151       594.097     47.080      

          2         14.277      81.621      1302.073    


          Bidirectional copy peak bandwidth GB/s

          D/D       0           1           2           

          0         N/A         13.053      25.833      

          1         13.053      N/A         86.108      

          2         25.833      86.108      N/A

EDIT 2: Thought these numbers was "tad" high and indeed `RBT -v` fails for both P2P directions... well, at least it doesn't take whole graphics subsystem down with it.

---

### 评论 #9 — seesturm (2021-08-21T10:14:55Z)

To my best knowledge the P2P patches did not make it into the upstream kernel yet. If you want to use P2P either rocm-dkms or manual patching of kernel is needed.
I've modified the patch for kernel 5.10.5. It can be downloaded here: [p2p-5.10.5-github.diff.txt](https://github.com/ROCm-Developer-Tools/HIP/files/5792508/p2p-5.10.5-github.diff.txt). You could try to modify for your kernel.

---

### 评论 #10 — FilipVaverka (2021-08-21T15:05:06Z)

I'm running 5.13.8 right now. Is there any way to track this kind of differences between ROCm-dkms and upstream? I would like to keep track of things that are (not) supposed to work in upstream and also when to expect them to land.

---

### 评论 #11 — AgenttiX (2021-10-27T13:02:56Z)

I have a similar issue with Radeon VII and ROCm 4.0.1 on Kubuntu 21.10 with kernel 5.13.0-20 using the upstream kernel driver. When cryptomining with Ethminer, the dmesg log gets filled by the following errors:
```
amdgpu 0000:03:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
amdgpu 0000:03:00.0: amdgpu: [sdma0] address:0x0000000005310000 src_id:247 ring:3 vmid:8 pasid:32784, for process ethminer pid 9613 thread ethminer pid 9613
```

<details>
<summary>rocminfo output</summary>

```
$ rocminfo
ROCk module is loaded
Able to open /dev/kfd read-write
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen Threadripper 3970X 32-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen Threadripper 3970X 32-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3700                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            64                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131756716(0x7da72ac) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131756716(0x7da72ac) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx906                             
  Uuid:                    GPU-38dc192172fd5d74               
  Marketing Name:          Vega 20 [Radeon VII]               
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26287(0x66af)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1801                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            60                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx906          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***
```

</details>

<details>
<summary>clinfo output</summary>

```
$ clinfo
Number of platforms                               3
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (3212.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD

  Platform Name                                   Portable Computing Language
  Platform Vendor                                 The pocl project
  Platform Version                                OpenCL 1.2 pocl 1.6, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             POCL

  Platform Name                                   NVIDIA CUDA
  Platform Vendor                                 NVIDIA Corporation
  Platform Version                                OpenCL 3.0 CUDA 11.4.136
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_fp64 cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing cl_nv_compiler_options cl_nv_device_attribute_query cl_nv_pragma_unroll cl_nv_copy_opts cl_khr_gl_event cl_nv_create_buffer cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_device_uuid cl_khr_pci_bus_info
  Platform Extensions with Version                cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_fp64                                                      0x400000 (1.0.0)
                                                  cl_khr_3d_image_writes                                           0x400000 (1.0.0)
                                                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_icd                                                       0x400000 (1.0.0)
                                                  cl_khr_gl_sharing                                                0x400000 (1.0.0)
                                                  cl_nv_compiler_options                                           0x400000 (1.0.0)
                                                  cl_nv_device_attribute_query                                     0x400000 (1.0.0)
                                                  cl_nv_pragma_unroll                                              0x400000 (1.0.0)
                                                  cl_nv_copy_opts                                                  0x400000 (1.0.0)
                                                  cl_khr_gl_event                                                  0x400000 (1.0.0)
                                                  cl_nv_create_buffer                                              0x400000 (1.0.0)
                                                  cl_khr_int64_base_atomics                                        0x400000 (1.0.0)
                                                  cl_khr_int64_extended_atomics                                    0x400000 (1.0.0)
                                                  cl_khr_device_uuid                                               0x400000 (1.0.0)
                                                  cl_khr_pci_bus_info                                              0x400000 (1.0.0)
  Platform Numeric Version                        0xc00000 (3.0.0)
  Platform Extensions function suffix             NV
  Platform Host timer resolution                  0ns

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx906
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0 
  Driver Version                                  3212.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Vega 20 [Radeon VII]
  Device PCI-e ID (AMD)                           0x66af
  Device Topology (AMD)                           PCI-E, 0000:03:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               60
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1801MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     60
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple (kernel)     64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              17163091968 (15.98GiB)
  Global free memory (AMD)                        16760832 (15.98GiB) 16760832 (15.98GiB)
  Global memory channels (AMD)                    128
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           14588628168 (13.59GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    14588628168 (13.59GiB)
  Preferred total size of global vars             17163091968 (15.98GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26287
    Max size for 1D images from buffer            4294967295 pixels
    Max 1D or 2D image array size                 8192 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             16384x16384x8192 pixels
    Max number of read image args                 128
    Max number of write image args                8
    Max number of read/write image args           64
  Max number of pipe args                         16
  Max active pipe reservations                    16
  Max pipe packet size                            1703726280 (1.587GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory size per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        14588628168 (13.59GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties (on host)                      
    Out-of-order execution                        No
    Profiling                                     Yes
  Queue properties (on device)                    
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                262144 (256KiB)
    Max size                                      8388608 (8MiB)
  Max queues on device                            1
  Max events on device                            1024
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Thu Jan  1 02:00:00 1970)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             60
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

  Platform Name                                   Portable Computing Language
Number of devices                                 1
  Device Name                                     pthread-AMD Ryzen Threadripper 3970X 32-Core Processor
  Device Vendor                                   AuthenticAMD
  Device Vendor ID                                0x1022
  Device Version                                  OpenCL 1.2 pocl HSTR: pthread-x86_64-pc-linux-gnu-znver2
  Driver Version                                  1.6
  Device OpenCL C Version                         OpenCL C 1.2 pocl
  Device Type                                     CPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               64
  Max clock frequency                             4549MHz
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     equally, by counts
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             4096x4096x4096
  Max work group size                             4096
  Preferred work group size multiple (kernel)     8
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                               16 / 16      
    int                                                  8 / 8       
    long                                                 4 / 4       
    half                                                 0 / 0        (n/a)
    float                                                8 / 8       
    double                                               4 / 4        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              132771393536 (123.7GiB)
  Error Correction support                        No
  Max memory allocation                           34359738368 (32GiB)
  Unified memory for Host and Device              Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16777216 (16MiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            2147483648 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             32768x32768 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                128
  Local memory type                               Global
  Local memory size                               524288 (512KiB)
  Max number of constant args                     8
  Max constant buffer size                        524288 (512KiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        Yes
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            Yes
  printf() buffer size                            16777216 (16MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_3d_image_writes cl_khr_fp64 cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64

  Platform Name                                   NVIDIA CUDA
Number of devices                                 1
  Device Name                                     NVIDIA GeForce GTX TITAN
  Device Vendor                                   NVIDIA Corporation
  Device Vendor ID                                0x10de
  Device Version                                  OpenCL 3.0 CUDA
  Device UUID                                     341bf311-d1d1-048f-8484-ddb89ef89b7d
  Driver UUID                                     341bf311-d1d1-048f-8484-ddb89ef89b7d
  Valid Device LUID                               No
  Device LUID                                     6d69-637300000000
  Device Node Mask                                0
  Device Numeric Version                          0xc00000 (3.0.0)
  Driver Version                                  470.74
  Device OpenCL C Version                         OpenCL C 1.2 
  Device OpenCL C all versions                    OpenCL C                                                         0x400000 (1.0.0)
                                                  OpenCL C                                                         0x401000 (1.1.0)
                                                  OpenCL C                                                         0x402000 (1.2.0)
                                                  OpenCL C                                                         0xc00000 (3.0.0)
  Device OpenCL C features                        __opencl_c_fp64                                                  0xc00000 (3.0.0)
                                                  __opencl_c_images                                                0xc00000 (3.0.0)
                                                  __opencl_c_int64                                                 0xc00000 (3.0.0)
                                                  __opencl_c_3d_image_writes                                       0xc00000 (3.0.0)
  Latest comfornace test passed                   v2021-02-01-00
  Device Type                                     GPU
  Device Topology (NV)                            PCI-E, 0000:4c:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               14
  Max clock frequency                             875MHz
  Compute Capability (NV)                         3.5
  Device Partition                                (core)
    Max number of sub-devices                     1
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x64
  Max work group size                             1024
  Preferred work group size multiple (device)     32
  Preferred work group size multiple (kernel)     32
  Warp size (NV)                                  32
  Max sub-groups per work group                   0
  Preferred / native vector sizes                 
    char                                                 1 / 1       
    short                                                1 / 1       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 0 / 0        (n/a)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              6379208704 (5.941GiB)
  Error Correction support                        No
  Max memory allocation                           1594802176 (1.485GiB)
  Unified memory for Host and Device              No
  Integrated memory (NV)                          No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   No
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       4096 bits (512 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Atomic memory capabilities                      relaxed, work-group scope
  Atomic fence capabilities                       relaxed, acquire/release, work-group scope
  Max size for global variable                    0
  Preferred total size of global vars             0
  Global Memory cache type                        Read/Write
  Global Memory cache size                        229376 (224KiB)
  Global Memory cache line size                   128 bytes
  Image support                                   Yes
    Max number of samplers per kernel             32
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             4096x4096x4096 pixels
    Max number of read image args                 256
    Max number of write image args                16
    Max number of read/write image args           0
  Pipe support                                    No
  Max number of pipe args                         0
  Max active pipe reservations                    0
  Max pipe packet size                            0
  Local memory type                               Local
  Local memory size                               49152 (48KiB)
  Registers per block (NV)                        65536
  Max number of constant args                     9
  Max constant buffer size                        65536 (64KiB)
  Generic address space support                   No
  Max size of kernel argument                     4352 (4.25KiB)
  Queue properties (on host)                      
    Out-of-order execution                        Yes
    Profiling                                     Yes
  Device enqueue capabilities                     (n/a)
  Queue properties (on device)                    
    Out-of-order execution                        No
    Profiling                                     No
    Preferred size                                0
    Max size                                      0
  Max queues on device                            0
  Max events on device                            0
  Prefer user sync for interop                    No
  Profiling timer resolution                      1000ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Non-uniform work-groups                       No
    Work-group collective functions               No
    Sub-group independent forward progress        No
    Kernel execution timeout (NV)                 No
  Concurrent copy and kernel execution (NV)       Yes
    Number of async copy engines                  1
    IL version                                    (n/a)
    ILs with version                              <printDeviceInfo:186: get CL_DEVICE_ILS_WITH_VERSION : error -30>
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                (n/a)
  Built-in kernels with version                   <printDeviceInfo:190: get CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION : error -30>
  Device Extensions                               cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_fp64 cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing cl_nv_compiler_options cl_nv_device_attribute_query cl_nv_pragma_unroll cl_nv_copy_opts cl_khr_gl_event cl_nv_create_buffer cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_device_uuid cl_khr_pci_bus_info
  Device Extensions with Version                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_fp64                                                      0x400000 (1.0.0)
                                                  cl_khr_3d_image_writes                                           0x400000 (1.0.0)
                                                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_icd                                                       0x400000 (1.0.0)
                                                  cl_khr_gl_sharing                                                0x400000 (1.0.0)
                                                  cl_nv_compiler_options                                           0x400000 (1.0.0)
                                                  cl_nv_device_attribute_query                                     0x400000 (1.0.0)
                                                  cl_nv_pragma_unroll                                              0x400000 (1.0.0)
                                                  cl_nv_copy_opts                                                  0x400000 (1.0.0)
                                                  cl_khr_gl_event                                                  0x400000 (1.0.0)
                                                  cl_nv_create_buffer                                              0x400000 (1.0.0)
                                                  cl_khr_int64_base_atomics                                        0x400000 (1.0.0)
                                                  cl_khr_int64_extended_atomics                                    0x400000 (1.0.0)
                                                  cl_khr_device_uuid                                               0x400000 (1.0.0)
                                                  cl_khr_pci_bus_info                                              0x400000 (1.0.0)


NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx906
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx906
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx906
        NOTE:   your OpenCL library only supports OpenCL 2.2,
                but some installed platforms support OpenCL 3.0.
                Programs using 3.0 features may crash
                or behave unexpectedly
```

</details>

---

### 评论 #12 — FilipVaverka (2021-10-27T18:45:48Z)

I've just quickly tested the behavior of `RBT -a -v` with kernel 5.14.11 and ROCm 4.3.1 and P2P transfers still don't work (validation fails). Will be patch posted by @seesturm ever upstreamed? Or will P2P be only possible with custom kernels?

---

### 评论 #13 — ROCmSupport (2021-11-09T06:06:08Z)

Hi @FilipVaverka 
As ROCm 4.5 released recently a couple of days ago, can you please verify with ROCm 4.5 and update here.
Thank you.

---

### 评论 #14 — FilipVaverka (2021-11-09T10:02:43Z)

Yes, the issue is still present with **ROCm 4.5** and kernel **5.14.14-1-default** (from OpenSUSE distribution). `RBT -a -v` still fails in Device-to-Device P2P transfers:

> rocm-bandwidth-test -a -v

          RocmBandwidthTest Version: 2.6.0

          Launch Command is: rocm-bandwidth-test -a -v


          Device: 0,  AMD Ryzen 9 3950X 16-Core Processor
          Device: 1,  AMD Radeon VII,  GPU-9f50716172fd5d40,  0d:0.0
          Device: 2,  AMD Radeon RX 6900 XT,  GPU-XX,  10:0.0

          Inter-Device Access

          D/D       0         1         2         

          0         1         1         1         

          1         1         1         1         

          2         1         1         1         


          Data Path Validation

          D/D       0           1           2           

          0         N/A         PASS        PASS        

          1         PASS        PASS        FAIL        

          2         PASS        FAIL        PASS

---

### 评论 #15 — rerrabolu (2022-01-07T19:07:18Z)

Hi @FilipVaverka going by the comments, if I am reading them correctly, your system has amdgpu module built on upstream branch (not the dkms branch used by ROCm releases). Could you confirm this including the branch name used by you.

As @seesturm noted support for P2P is not yet part of non-dkms branches. There are discussions underway to enable P2P on upstream branch. I don't have a date yet as to when this will be part of it. 

Lastly on your system, do you have P2P issues if you were to load the amdgpu module built from the dkms branch i.e. one from ROCm release. Please let me know .

P.S.  FilipVaverka you may want to review the discussion on this thread as well which talks about aspects affecting your experience - https://github.com/ROCm-Developer-Tools/HIP/issues/2214


---

### 评论 #16 — FilipVaverka (2022-01-08T11:36:50Z)

Yes, I'm running latest kernel distributed with OpenSUSE Tumbleweed. Which right now is:

> Linux 5.15.12-1-default #1 SMP Wed Dec 29 14:50:16 UTC 2021 (375fcb8) x86_64 x86_64 x86_64 GNU/Linux

I haven't tested DKMS at all as it seems to support only rather old kernels and I don't know how it would interact with kernel that already has amdgpu built into it. If its possible to use DKMS with kernel I'm running right now, I could try it out.

---

### 评论 #17 — rerrabolu (2022-01-09T00:35:31Z)

@FilipVaverka thanks for confirming the setup you are using (5.15.12-1 with builtin amdgpu module). This explains why you are not able to do P2P. As indicated by @seesturm P2P support is absent in amdgpu code base that is part of upstream.

If you really wish to try/test P2P my suggestion would be step down to kernels supported by ROCm release. I would say the procedure to remove builtin modules is same as any other. Let us know if you have any surprises.

I will pass on you original observation of GPU reset so that on setups such as your system does not advertise P2P being enabled.


---

### 评论 #18 — rerrabolu (2022-01-10T17:05:57Z)

@FilipVaverka could update the issue with log from "sudo lspci -vv" command. Want to know if the GPUs are reporting small or large BAR.

---

### 评论 #19 — FilipVaverka (2022-01-10T18:05:40Z)

Here: [lspci_vv.txt](https://github.com/RadeonOpenCompute/ROCm/files/7840974/lspci_vv.txt). Both devices are reporting BAR 0 as 16GB and BAR 2 as 256MB, I believe. The system is Ryzen 9 3950X on ASUS Crosshair VIII Hero (X570 chipset).


---

### 评论 #20 — rerrabolu (2022-01-10T20:14:18Z)

@FilipVaverka thanks for providing the lspci logs. I see that both devices report BAR-0 as having 16 GB.

- Device @ 0d:00.0 - Region 0: Memory at 7800000000 (64-bit, prefetchable) [size=16G]
- Device @ 10:00.0 - Region 0: Memory at 7000000000 (64-bit, prefetchable) [size=16G]

One question I have is where did you get these GPU's. Were these purchased in the open market or provided by AMD in some partnership program. The reason I ask is vBIOSes supporting large BAR is not common unless the devices are targeted for ROCm platforms.



---

### 评论 #21 — FilipVaverka (2022-01-10T20:24:24Z)

Both GPUs are bought from local retailer the 6900XT has original vBIOS, while I had to flash Radeon VII vBIOS as it didn't support UEFI out of the box (I believe the new vBIOS was from official AMD site).
I thought the gaming GPUs have to support resizable BAR since AMD introduced Smart Memory Access (I believe its Windows equivalent to resizable BAR on Linux).

---

### 评论 #22 — rerrabolu (2022-01-10T21:21:41Z)

Thanks for the update. Your experience (GPU reset) was compounded because the vBIOS was reporting large BAR giving false green signal.

Amdgpu modules, ones based on upstream branches, should consult large BAR status only when other elements of P2P support are in place. This will avoid experiences such as yours.


---

### 评论 #23 — FilipVaverka (2022-01-10T21:31:58Z)

I should just clarify that the GPU reset issue disappeared when I swapped RX Vega 64 for 6900XT.
I opened the issue with RX Vega 64 + Radeon VII and later swapped the Vega out.
Either way, thanks for some insight its very appreciated. Hopefully P2P support makes its way into upstream rather sooner than later.


---

### 评论 #24 — ROCmSupport (2022-02-08T10:17:39Z)

Thanks for the suggestions and help @rerrabolu 
I am closing this now. Thank you.

---
