# Multicard training error with rocm5.7

- **Issue #:** 2494
- **State:** closed
- **Created:** 2023-09-21T18:42:16Z
- **Updated:** 2024-10-02T15:41:59Z
- **Labels:** hardware:Radeon, application:pytorch, model:transformer
- **Assignees:** hongxiayang
- **URL:** https://github.com/ROCm/ROCm/issues/2494

GPU Model: 
7900XTX

OS and other system details:
CPU:
amd epyc 7542
MotherBoard:
H12SSL-i
RAM:
8*32G 
OS:
debian12  with kernel 6.1.0.11
kernel params :
amd_iommu=off
amdgpu version:
 [amdgpu_5.7.50700-1652687.22.04_amd64.deb]


Describe your Problem Provide sufficient information to reproduce your problem. Explain why the current behavior is a concern.

When i use 2 gpu run a Transformer Model with pytorch 2.0.1 it'crash and more the graphic card are not usable else the kernel dmesg show large amount of errors  and first reboot the system cannot detect the graphics card it need reset bios and redetect

command is 
`torchrun --nnodes=1 --nproc_per_node=2 --rdzv_id=100 --rdzv_backend=c10d --rdzv_endpoint=localhost:29400 task/asr/train.py`
Output:

```
Memory access fault by GPU node-2 (Agent handle: 0x5561f711dfd0) on address 0x7fb7a0d67000. Reason: Page not present or supervisor privilege.
Memory access fault by GPU node-1 (Agent handle: 0x560b9370e950) on address 0x6efcab62f000. Reason: Page not present or supervisor privilege
```




dmesg output
```
[22340.105480] amdgpu 0000:03:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32776, for process python3 pid 172866 thread python3 pid 172866)
[22340.105491] amdgpu 0000:03:00.0: amdgpu:   in page starting at address 0x00000002e4cd2000 from client 10
[22340.105496] amdgpu 0000:03:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
[22340.105499] amdgpu 0000:03:00.0: amdgpu:      Faulty UTCL2 client ID: TCP (0x8)
[22340.105502] amdgpu 0000:03:00.0: amdgpu:      MORE_FAULTS: 0x1
[22340.105504] amdgpu 0000:03:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.105507] amdgpu 0000:03:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[22340.105509] amdgpu 0000:03:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.105512] amdgpu 0000:03:00.0: amdgpu:      RW: 0x0
[22340.105597] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.105601] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.105620] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00006efcab62b000 from client 10
[22340.105632] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
[22340.105640] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: TCP (0x8)
[22340.105648] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x1
[22340.105654] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.105660] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[22340.105665] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.105671] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.105683] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.105694] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00006efcab62f000 from client 10
[22340.105702] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[22340.105708] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[22340.105715] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[22340.105720] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.105726] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[22340.105732] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.105738] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.105753] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.105763] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x000000e200002000 from client 10
[22340.105770] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[22340.105776] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[22340.105782] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[22340.105788] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.105793] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[22340.105799] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.105805] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.105817] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.105827] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x000000e300002000 from client 10
[22340.105834] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[22340.105840] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[22340.105846] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[22340.105852] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.105857] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[22340.105863] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.105869] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.105880] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.105889] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x000000e400002000 from client 10
[22340.105896] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[22340.105902] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[22340.105908] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[22340.105914] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.105920] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[22340.105925] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.105931] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.105945] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.105954] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x000000e500002000 from client 10
[22340.105961] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[22340.105967] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[22340.105973] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[22340.105979] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.105985] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[22340.105990] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.105996] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.106010] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.106019] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x000000e600002000 from client 10
[22340.106026] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[22340.106032] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[22340.106038] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[22340.106044] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.106050] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[22340.106055] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.106061] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.106076] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.106085] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x000000e700002000 from client 10
[22340.106092] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[22340.106098] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[22340.106104] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[22340.106109] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.106115] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[22340.106121] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.106127] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.106141] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32775, for process python3 pid 172865 thread python3 pid 172865)
[22340.106150] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x000000e800002000 from client 10
[22340.106157] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[22340.106163] amdgpu 0000:83:00.0: amdgpu:      Faulty UTCL2 client ID: CB/DB (0x0)
[22340.106169] amdgpu 0000:83:00.0: amdgpu:      MORE_FAULTS: 0x0
[22340.106175] amdgpu 0000:83:00.0: amdgpu:      WALKER_ERROR: 0x0
[22340.106180] amdgpu 0000:83:00.0: amdgpu:      PERMISSION_FAULTS: 0x0
[22340.106186] amdgpu 0000:83:00.0: amdgpu:      MAPPING_ERROR: 0x0
[22340.106192] amdgpu 0000:83:00.0: amdgpu:      RW: 0x0
[22340.211851] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22340.212137] amdgpu: failed to remove hardware queue from MES, doorbell=0x1216
[22340.212140] amdgpu: MES might be in unrecoverable state, issue a GPU reset
[22340.212148] amdgpu: Failed to evict queue 10
[22340.212171] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212187] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212204] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212220] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 0, simd_id 0, wgp_id 0
[22340.212234] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212250] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[22340.212270] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 0, simd_id 0, wgp_id 0
[22340.212288] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212302] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212323] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[22340.212337] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212353] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212388] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.212467] amdgpu 0000:03:00.0: amdgpu: GPU reset begin!
[22340.220197] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22340.220408] amdgpu: failed to remove hardware queue from MES, doorbell=0x1216
[22340.220411] amdgpu: MES might be in unrecoverable state, issue a GPU reset
[22340.220416] amdgpu: Failed to evict queue 10
[22340.220424] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220438] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220451] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.220464] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 5, simd_id 0, wgp_id 0
[22340.220477] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220490] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 4, simd_id 0, wgp_id 0
[22340.220504] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220518] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.220532] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220555] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 5, simd_id 0, wgp_id 0
[22340.220568] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 6, simd_id 0, wgp_id 0
[22340.220581] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220605] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220617] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220630] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.220643] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220657] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[22340.220670] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 5, simd_id 0, wgp_id 0
[22340.220683] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.220696] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.220708] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220721] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 6, simd_id 0, wgp_id 0
[22340.220735] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 6, simd_id 0, wgp_id 0
[22340.220748] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220760] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220773] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.220786] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220798] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.220813] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 4, simd_id 0, wgp_id 0
[22340.220825] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220838] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 5, simd_id 0, wgp_id 0
[22340.220851] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220863] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 5, simd_id 0, wgp_id 0
[22340.220876] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220890] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.220903] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220916] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 0, simd_id 0, wgp_id 0
[22340.220928] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 2, simd_id 0, wgp_id 0
[22340.220941] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220954] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 5, simd_id 0, wgp_id 0
[22340.220978] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 3, simd_id 0, wgp_id 0
[22340.220991] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 1, priv 1, wave_id 4, simd_id 0, wgp_id 0
[22340.221003] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 5, simd_id 0, wgp_id 0
[22340.221016] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 4, simd_id 0, wgp_id 0
[22340.221029] amdgpu: sq_intr: error, detail 0x00000000, type 1, sh 0, priv 1, wave_id 7, simd_id 0, wgp_id 0
[22340.221061] amdgpu 0000:83:00.0: amdgpu: GPU reset begin!
[22341.235735] amdgpu 0000:83:00.0: amdgpu: IP block:gfx_v11_0 is hung!
[22341.235795] amdgpu 0000:03:00.0: amdgpu: IP block:gfx_v11_0 is hung!
[22342.259763] [drm:sdma_v6_0_ring_test_ib [amdgpu]] *ERROR* amdgpu: IB test timed out
[22342.260203] amdgpu 0000:03:00.0: amdgpu: IP block:sdma_v6_0 is hung!
[22342.263690] [drm:sdma_v6_0_ring_test_ib [amdgpu]] *ERROR* amdgpu: IB test timed out
[22342.264010] amdgpu 0000:83:00.0: amdgpu: IP block:sdma_v6_0 is hung!
[22342.633518] Failed to wait all pipes clean
[22342.633568] amdgpu 0000:83:00.0: amdgpu: soft reset failed, will fallback to full reset!
[22342.675604] Failed to wait all pipes clean
[22342.675612] amdgpu 0000:03:00.0: amdgpu: soft reset failed, will fallback to full reset!
[22342.834411] amdgpu 0000:83:00.0: amdgpu: SMU: response:0xFFFFFFFF for index:59 param:0x00000000 message:DFCstateControl?
[22342.834418] amdgpu 0000:83:00.0: amdgpu: [SetDfCstate] failed!
[22342.834421] amdgpu 0000:83:00.0: amdgpu: Failed to disallow df cstate
[22342.834432] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=5
[22342.877202] amdgpu 0000:03:00.0: amdgpu: SMU: response:0xFFFFFFFF for index:59 param:0x00000000 message:DFCstateControl?
[22342.877209] amdgpu 0000:03:00.0: amdgpu: [SetDfCstate] failed!
[22342.877212] amdgpu 0000:03:00.0: amdgpu: Failed to disallow df cstate
[22342.877224] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=5
[22342.964952] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22342.965137] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.007776] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.007966] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.075161] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.075338] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.117935] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.118111] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.185372] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.185547] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.228075] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.228250] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.295587] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.295766] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.338200] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.338375] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.405795] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.405969] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.448344] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.448517] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.515985] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.516159] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.558464] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.558637] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.626170] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.626342] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.668606] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.668781] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.736379] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.736557] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.778715] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.778893] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.846554] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.846728] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22343.888824] [drm:mes_v11_0_submit_pkt_and_poll_completion.constprop.0 [amdgpu]] *ERROR* MES failed to response msg=3
[22343.888997] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[22344.249704] [drm:gfx_v11_0_hw_fini [amdgpu]] *ERROR* failed to halt cp gfx
[22344.249947] [drm:psp_ring_cmd_submit [amdgpu]] *ERROR* ring_buffer_start = 000000008f2b9fb6; ring_buffer_end = 000000006e89c2b3; write_frame = 00000000d8de01da
[22344.250121] [drm:psp_ring_cmd_submit [amdgpu]] *ERROR* write_frame is pointing to address out of bounds
[22344.250291] [drm:psp_suspend [amdgpu]] *ERROR* Failed to terminate ras ta
[22344.250459] [drm:amdgpu_device_ip_suspend_phase2 [amdgpu]] *ERROR* suspend of IP block <psp> failed -22
[22344.251655] amdgpu 0000:83:00.0: amdgpu: MODE1 reset
[22344.251660] amdgpu 0000:83:00.0: amdgpu: GPU mode1 reset
[22344.252662] amdgpu 0000:83:00.0: amdgpu: GPU smu mode1 reset
[22344.252666] amdgpu 0000:83:00.0: amdgpu: SMU: response:0xFFFFFFFF for index:47 param:0x00000000 message:Mode1Reset?
[22344.252670] amdgpu 0000:83:00.0: amdgpu: GPU mode1 reset failed
[22344.292232] [drm:gfx_v11_0_hw_fini [amdgpu]] *ERROR* failed to halt cp gfx
[22344.292471] [drm:psp_ring_cmd_submit [amdgpu]] *ERROR* ring_buffer_start = 000000008d2bdb3a; ring_buffer_end = 00000000ff4eb044; write_frame = 000000005abb7a30
[22344.292645] [drm:psp_ring_cmd_submit [amdgpu]] *ERROR* write_frame is pointing to address out of bounds
[22344.292814] [drm:psp_suspend [amdgpu]] *ERROR* Failed to terminate ras ta
[22344.292984] [drm:amdgpu_device_ip_suspend_phase2 [amdgpu]] *ERROR* suspend of IP block <psp> failed -22
[22344.294178] amdgpu 0000:03:00.0: amdgpu: MODE1 reset
[22344.294183] amdgpu 0000:03:00.0: amdgpu: GPU mode1 reset
[22344.295186] amdgpu 0000:03:00.0: amdgpu: GPU smu mode1 reset
[22344.295190] amdgpu 0000:03:00.0: amdgpu: SMU: response:0xFFFFFFFF for index:47 param:0x00000000 message:Mode1Reset?
[22344.295194] amdgpu 0000:03:00.0: amdgpu: GPU mode1 reset failed
[22344.456139] amdgpu 0000:83:00.0: amdgpu: ASIC reset failed with error, -121 for drm dev, 0000:83:00.0
[22344.498996] amdgpu 0000:03:00.0: amdgpu: ASIC reset failed with error, -121 for drm dev, 0000:03:00.0
[22348.746284] amdgpu 0000:83:00.0: amdgpu: GPU reset succeeded, trying to resume
[22348.746435] [drm] PCIE GART of 512M enabled (table at 0x00000085FEB00000).
[22348.746525] [drm] VRAM is lost due to GPU reset!
[22348.746528] [drm] PSP is resuming...
[22348.790706] amdgpu 0000:03:00.0: amdgpu: GPU reset succeeded, trying to resume
[22348.790900] [drm] PCIE GART of 512M enabled (table at 0x00000085FEB00000).
[22348.791038] [drm] VRAM is lost due to GPU reset!
[22348.791042] [drm] PSP is resuming...
[22348.967420] [drm:psp_hw_start [amdgpu]] *ERROR* PSP create ring failed!
[22348.967631] [drm:psp_resume [amdgpu]] *ERROR* PSP resume failed
[22348.967851] [drm:amdgpu_device_fw_loading [amdgpu]] *ERROR* resume of IP block <psp> failed -62
[22348.999763] [drm:psp_hw_start [amdgpu]] *ERROR* PSP create ring failed!
[22349.000013] [drm:psp_resume [amdgpu]] *ERROR* PSP resume failed
[22349.000293] [drm:amdgpu_device_fw_loading [amdgpu]] *ERROR* resume of IP block <psp> failed -62
[22383.942807] amdgpu: Failed to remove queue 9
[22383.942814] amdgpu: Failed to remove queue 8
[22383.942817] amdgpu: Failed to remove queue 7
[22383.942819] amdgpu: Failed to remove queue 6
[22383.942821] amdgpu: Failed to remove queue 5
[22383.942823] amdgpu: Failed to remove queue 4
[22383.942825] amdgpu: Failed to remove queue 3
[22383.942827] amdgpu: Failed to remove queue 2
[22383.942829] amdgpu: Failed to remove queue 1
[22383.942830] amdgpu: Failed to remove queue 0
[22387.880405] amdgpu: Failed to remove queue 9
[22387.880412] amdgpu: Failed to remove queue 8
[22387.880415] amdgpu: Failed to remove queue 7
[22387.880417] amdgpu: Failed to remove queue 6
[22387.880419] amdgpu: Failed to remove queue 5
[22387.880421] amdgpu: Failed to remove queue 4
[22387.880423] amdgpu: Failed to remove queue 3
[22387.880425] amdgpu: Failed to remove queue 2
[22387.880427] amdgpu: Failed to remove queue 1
[22387.880429] amdgpu: Failed to remove queue 0
[22475.343793] INFO: task kworker/u128:3:153651 blocked for more than 120 seconds.
[22475.343810]       Tainted: P           OE      6.1.0-11-amd64 #1 Debian 6.1.38-4
[22475.343819] "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
[22475.343824] task:kworker/u128:3  state:D stack:0     pid:153651 ppid:2      flags:0x00004000
[22475.343840] Workqueue: amdgpu-reset-dev amdgpu_amdkfd_reset_work [amdgpu]
[22475.344281] Call Trace:
[22475.344287]  <TASK>
[22475.344298]  __schedule+0x351/0xa20
[22475.344318]  schedule+0x5d/0xe0
[22475.344327]  schedule_timeout+0x118/0x150
[22475.344343]  dma_fence_default_wait+0x1a5/0x260
[22475.344356]  ? __bpf_trace_dma_fence+0x10/0x10
[22475.344369]  dma_fence_wait_timeout+0x108/0x130
[22475.344381]  amdgpu_sync_wait+0x75/0x110 [amdgpu]
[22475.344819]  amdgpu_mes_ctx_map_meta_data+0x1f0/0x2c0 [amdgpu]
[22475.345299]  amdgpu_mes_self_test+0x102/0x480 [amdgpu]
[22475.345701]  ? amdgpu_device_fw_loading+0x13e/0x150 [amdgpu]
[22475.346068]  ? __x86_return_thunk+0x5/0x6
[22475.346081]  ? __drm_err+0x7b/0xa0 [drm]
[22475.346162]  amdgpu_device_gpu_recover.cold+0x47a/0xb3f [amdgpu]
[22475.346672]  ? __ret+0x40/0x7e
[22475.346689]  amdgpu_amdkfd_reset_work+0x5e/0x80 [amdgpu]
[22475.347134]  process_one_work+0x1c7/0x380
[22475.347152]  worker_thread+0x4d/0x380
[22475.347165]  ? rescuer_thread+0x3a0/0x3a0
[22475.347174]  kthread+0xe9/0x110
[22475.347184]  ? kthread_complete_and_exit+0x20/0x20
[22475.347195]  ret_from_fork+0x22/0x30
[22475.347218]  </TASK>
[22475.347224] INFO: task kworker/u128:2:167646 blocked for more than 120 seconds.
[22475.347230]       Tainted: P           OE      6.1.0-11-amd64 #1 Debian 6.1.38-4
[22475.347236] "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
[22475.347240] task:kworker/u128:2  state:D stack:0     pid:167646 ppid:2      flags:0x00004000
[22475.347252] Workqueue: amdgpu-reset-dev amdgpu_amdkfd_reset_work [amdgpu]
[22475.347702] Call Trace:
[22475.347708]  <TASK>
[22475.347717]  __schedule+0x351/0xa20
[22475.347734]  schedule+0x5d/0xe0
[22475.347745]  schedule_timeout+0x118/0x150
[22475.347761]  dma_fence_default_wait+0x1a5/0x260
[22475.347774]  ? __bpf_trace_dma_fence+0x10/0x10
[22475.347789]  dma_fence_wait_timeout+0x108/0x130
[22475.347802]  amdgpu_sync_wait+0x75/0x110 [amdgpu]
[22475.348234]  amdgpu_mes_ctx_map_meta_data+0x1f0/0x2c0 [amdgpu]
[22475.348665]  amdgpu_mes_self_test+0x102/0x480 [amdgpu]
[22475.349062]  ? amdgpu_device_fw_loading+0x13e/0x150 [amdgpu]
[22475.349432]  ? __x86_return_thunk+0x5/0x6
[22475.349440]  ? __drm_err+0x7b/0xa0 [drm]
[22475.349519]  amdgpu_device_gpu_recover.cold+0x47a/0xb3f [amdgpu]
[22475.350052]  amdgpu_amdkfd_reset_work+0x5e/0x80 [amdgpu]
[22475.350474]  process_one_work+0x1c7/0x380
[22475.350489]  worker_thread+0x4d/0x380
[22475.350501]  ? rescuer_thread+0x3a0/0x3a0
[22475.350510]  kthread+0xe9/0x110
[22475.350518]  ? kthread_complete_and_exit+0x20/0x20
[22475.350530]  ret_from_fork+0x22/0x30
[22475.350552]  </TASK>
```
