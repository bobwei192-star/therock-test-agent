# [Driver] *ERROR* MES failed to response msg=2

- **Issue #:** 2196
- **State:** open
- **Created:** 2023-05-30T23:40:56Z
- **Updated:** 2025-10-15T11:04:01Z
- **Labels:** 5.5.0
- **URL:** https://github.com/ROCm/ROCm/issues/2196

Triggered by running https://github.com/RadeonOpenCompute/rocm_bandwidth_test in a loop while running https://github.com/ROCm-Developer-Tools/HIP-Examples/tree/master/gpu-burn in a loop.

1x 7900XTX
ASROCK ROMED8-2T
EPYC 7662
Ubuntu 22.04, Kernel 6.2.14-060214-generic, ROCm 5.5

`sudo cat /sys/kernel/debug/dri/1/amdgpu_gpu_recover` will recover the GPU.

```
[  111.406216] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:10 pasid:32769, for process rocm-bandwidth- pid 3286 thread rocm-bandwidth- pid 3286)
[  111.406237] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00007f0000000000 from client 10
[  111.406246] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00A01A30
[  111.406253] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: SDMA0 (0xd)
[  111.406259] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[  111.406265] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[  111.406270] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[  111.406275] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[  111.406280] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[  114.188710] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:10 pasid:32769, for process rocm-bandwidth- pid 3286 thread rocm-bandwidth- pid 3286)
[  114.188729] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00007f0000000000 from client 10
[  114.188738] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00A01A30
[  114.188746] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: SDMA0 (0xd)
[  114.188754] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[  114.188759] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[  114.188765] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[  114.188770] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[  114.188776] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[  114.302856] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=2
[  114.303173] amdgpu: failed to add hardware queue to MES, doorbell=0x1202
[  114.303176] amdgpu: MES might be in unrecoverable state, issue a GPU reset
[  114.303179] amdgpu: Failed to restore queue 0
[  114.303182] amdgpu: Failed to restore process queues
[  114.303184] amdgpu: Failed to restore queues of pasid 0x8001
[  114.303450] amdgpu 0000:83:00.0: amdgpu: GPU reset begin!
[  114.303477] amdgpu: Failed to evict queue 1
[  114.303483] amdgpu: Failed to suspend process 0x8002
[  114.309700] amdgpu 0000:83:00.0: amdgpu: recover vram bo from shadow start
[  114.309705] amdgpu 0000:83:00.0: amdgpu: recover vram bo from shadow done
[  114.412749] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=14
[  114.413073] [drm:amdgpu_mes_reg_write_reg_wait [amdgpu]] *ERROR* failed to reg_write_reg_wait
[  114.420094] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=14
[  114.420379] [drm:amdgpu_mes_reg_write_reg_wait [amdgpu]] *ERROR* failed to reg_write_reg_wait
[  114.523222] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=14
[  114.523499] [drm:amdgpu_mes_reg_write_reg_wait [amdgpu]] *ERROR* failed to reg_write_reg_wait
[  114.530476] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=14
[  114.530750] [drm:amdgpu_mes_reg_write_reg_wait [amdgpu]] *ERROR* failed to reg_write_reg_wait
[  114.634108] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=14
[  114.634391] [drm:amdgpu_mes_reg_write_reg_wait [amdgpu]] *ERROR* failed to reg_write_reg_wait
...
[  117.293167] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=2
[  117.293439] [drm:amdgpu_mes_add_hw_queue [amdgpu]] *ERROR* failed to add hardware queue to MES, doorbell=0x2200
[  117.293712] [drm:amdgpu_mes_self_test [amdgpu]] *ERROR* failed to add ring
[  117.294161] amdgpu 0000:83:00.0: amdgpu: GPU reset(1) succeeded!
```