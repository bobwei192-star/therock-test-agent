# [Issue]: 780M  MES failed to response frequently which cause GPU reset frequently with doorbell 0x1002,0x1000

- **Issue #:** 6018
- **State:** closed
- **Created:** 2026-03-04T15:20:44Z
- **Updated:** 2026-06-25T17:55:15Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6018

### Problem Description

Run ollama with translategemma 12b for local translate, MES failed to response frequently which cause GPU reset frequently, check following log.

### Operating System

Arch linux

### CPU

7840hs

### GPU

780M

### ROCm Version

7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

```
[73314.889668] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[73314.889675] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[73314.889677] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[73314.889681] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
[73314.889682] amdgpu 0000:c5:00.0: amdgpu: Failed to evict process queues
[73314.889684] amdgpu: Failed to quiesce KFD
[73314.889701] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[73314.891684] amdgpu 0000:c5:00.0: amdgpu: remove_all_kfd_queues_mes: Failed to remove queue 0 for dev 49700
[73314.891708] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[73314.893432] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[73316.994500] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[73316.994507] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[73318.998481] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[73318.998487] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[73318.999856] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[73319.031470] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[73319.031938] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[73319.032193] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[73319.032198] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[73319.032202] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[73319.033702] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[73319.039404] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[73319.185138] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[73319.185150] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[73319.185153] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[73319.185155] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[73319.185157] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[73319.185158] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[73319.185160] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[73319.185162] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[73319.185163] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[73319.185165] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[73319.185167] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[73319.185169] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[73319.185171] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[73319.187263] amdgpu 0000:c5:00.0: amdgpu: GPU reset(1) succeeded!
[73319.187276] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[73327.541061] amdgpu: Freeing queue vital buffer 0x7f2e27400000, queue evicted
[73327.541067] amdgpu: Freeing queue vital buffer 0x7f3041200000, queue evicted
[73327.541070] amdgpu: Freeing queue vital buffer 0x7f3047400000, queue evicted
[73327.541071] amdgpu: Freeing queue vital buffer 0x7f3047a00000, queue evicted
[73327.541075] amdgpu: Freeing queue vital buffer 0x7f3196600000, queue evicted
[73327.649199] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[73327.649205] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1000
[73327.649207] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[73327.649211] amdgpu 0000:c5:00.0: amdgpu: Failed to remove queue 0
[73327.649212] amdgpu: Resetting wave fronts (cpsch) on dev 0000000058c303b6
[73327.649214] amdgpu 0000:c5:00.0: amdgpu: no vmid pasid mapping supported
[73327.649214] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[73327.649312] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[73327.652804] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[73327.758867] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[73327.793270] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[73327.793923] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[73327.793983] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[73327.793985] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[73327.793988] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[73327.796093] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[73327.803519] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[73328.541797] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[73328.541804] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[73328.541807] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[73328.541808] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[73328.541810] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[73328.541811] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[73328.541813] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[73328.541814] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[73328.541815] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[73328.541817] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[73328.541819] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[73328.541820] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[73328.541822] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[73328.543914] amdgpu 0000:c5:00.0: amdgpu: GPU reset(2) succeeded!
[73328.543927] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[73819.930091] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[73819.930100] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[73819.930102] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[73819.930107] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
[73819.930111] amdgpu 0000:c5:00.0: amdgpu: Failed to evict process queues
[73819.930135] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[73819.933292] amdgpu 0000:c5:00.0: amdgpu: remove_all_kfd_queues_mes: Failed to remove queue 0 for dev 49700
[73819.933323] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[73819.934978] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[73822.026089] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[73822.026096] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[73824.030060] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[73824.030066] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[73824.031435] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[73824.063114] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[73824.063599] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[73824.063826] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[73824.063832] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[73824.063839] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[73824.065380] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[73824.071356] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[73824.193078] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[73824.193087] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[73824.193090] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[73824.193092] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[73824.193094] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[73824.193095] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[73824.193097] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[73824.193099] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[73824.193101] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[73824.193103] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[73824.193105] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[73824.193107] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[73824.193109] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[73824.195332] amdgpu 0000:c5:00.0: amdgpu: GPU reset(3) succeeded!
[73824.195345] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[73838.829061] amdgpu: Freeing queue vital buffer 0x7fe58f200000, queue evicted
[73838.829068] amdgpu: Freeing queue vital buffer 0x7fe59fc00000, queue evicted
[73838.829070] amdgpu: Freeing queue vital buffer 0x7fe5a0000000, queue evicted
[73838.829071] amdgpu: Freeing queue vital buffer 0x7fe909c00000, queue evicted
[73838.829073] amdgpu: Freeing queue vital buffer 0x7fe90a200000, queue evicted
[73838.829080] amdgpu: Freeing queue vital buffer 0x7fe99a200000, queue evicted
[73838.921111] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[73838.921122] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1000
[73838.921124] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[73838.921129] amdgpu 0000:c5:00.0: amdgpu: Failed to remove queue 0
[73838.921132] amdgpu: Resetting wave fronts (cpsch) on dev 0000000058c303b6
[73838.921135] amdgpu 0000:c5:00.0: amdgpu: no vmid pasid mapping supported
[73838.921148] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[73838.921240] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[73838.925110] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[73839.018046] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[73839.051567] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[73839.052262] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[73839.052325] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[73839.052328] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[73839.052332] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[73839.053887] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[73839.060470] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[73839.816239] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[73839.816247] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[73839.816250] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[73839.816251] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[73839.816253] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[73839.816254] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[73839.816255] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[73839.816257] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[73839.816258] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[73839.816260] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[73839.816262] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[73839.816263] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[73839.816265] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[73839.818312] amdgpu 0000:c5:00.0: amdgpu: GPU reset(4) succeeded!
[73839.818325] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[74121.237443] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74121.237451] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[74121.237453] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[74121.237457] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
[74121.237459] amdgpu 0000:c5:00.0: amdgpu: Failed to evict process queues
[74121.237480] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[74121.241693] amdgpu 0000:c5:00.0: amdgpu: Failed to restore queue 5
[74121.241696] amdgpu 0000:c5:00.0: amdgpu: Failed to restore process queues
[74121.242215] amdgpu 0000:c5:00.0: amdgpu: remove_all_kfd_queues_mes: Failed to remove queue 5 for dev 49700
[74121.242244] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[74121.243864] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[74123.339950] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74123.339957] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[74125.343943] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74125.343950] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[74125.345332] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[74125.375969] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[74125.376466] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[74125.376550] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[74125.376562] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[74125.376576] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[74125.378181] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[74125.383901] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[74125.505881] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[74125.505890] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[74125.505893] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[74125.505895] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[74125.505897] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[74125.505898] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[74125.505900] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[74125.505901] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[74125.505903] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[74125.505911] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[74125.505913] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[74125.505914] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[74125.505916] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[74125.508081] amdgpu 0000:c5:00.0: amdgpu: GPU reset(5) succeeded!
[74125.508096] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[74127.209515] amdgpu: Freeing queue vital buffer 0x7f5407400000, queue evicted
[74127.209521] amdgpu: Freeing queue vital buffer 0x7f5621800000, queue evicted
[74127.209524] amdgpu: Freeing queue vital buffer 0x7f5634400000, queue evicted
[74127.209525] amdgpu: Freeing queue vital buffer 0x7f5634a00000, queue evicted
[74127.209529] amdgpu: Freeing queue vital buffer 0x7f5776600000, queue evicted
[74127.261547] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74127.261554] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1008
[74127.261557] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[74127.261560] amdgpu 0000:c5:00.0: amdgpu: Failed to remove queue 5
[74127.261564] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[74127.261614] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74127.261617] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1000
[74127.261619] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[74127.261621] amdgpu 0000:c5:00.0: amdgpu: Failed to remove queue 0
[74127.261647] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[74127.264687] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[74127.362731] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[74127.396007] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[74127.396641] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[74127.396721] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[74127.396724] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[74127.396727] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[74127.397656] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[74127.404264] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[74128.026595] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[74128.026603] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[74128.026606] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[74128.026607] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[74128.026609] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[74128.026610] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[74128.026611] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[74128.026613] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[74128.026614] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[74128.026616] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[74128.026617] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[74128.026619] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[74128.026621] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[74128.028737] amdgpu 0000:c5:00.0: amdgpu: GPU reset(6) succeeded!
[74128.028751] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[74147.033117] amdgpu: Freeing queue vital buffer 0x7fb3bac00000, queue evicted
[74154.953981] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74154.953988] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[74154.953990] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[74154.953994] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
[74154.953996] amdgpu 0000:c5:00.0: amdgpu: Failed to evict process queues
[74154.953998] amdgpu: Failed to quiesce KFD
[74154.954014] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[74154.954766] amdgpu 0000:c5:00.0: amdgpu: remove_all_kfd_queues_mes: Failed to remove queue 0 for dev 49700
[74154.954795] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[74154.956754] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[74157.055311] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74157.055318] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[74159.059304] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74159.059311] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[74159.060798] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[74159.092363] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[74159.092883] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[74159.093096] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[74159.093098] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[74159.093101] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[74159.094614] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[74159.100208] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[74159.222235] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[74159.222243] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[74159.222246] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[74159.222247] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[74159.222249] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[74159.222250] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[74159.222252] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[74159.222253] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[74159.222255] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[74159.222257] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[74159.222258] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[74159.222260] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[74159.222262] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[74159.224396] amdgpu 0000:c5:00.0: amdgpu: GPU reset(7) succeeded!
[74159.224410] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[74159.900878] amdgpu: Freeing queue vital buffer 0x7f5a35a00000, queue evicted
[74159.900886] amdgpu: Freeing queue vital buffer 0x7f5a46000000, queue evicted
[74159.900890] amdgpu: Freeing queue vital buffer 0x7f5c6ca00000, queue evicted
[74159.900891] amdgpu: Freeing queue vital buffer 0x7f5da4600000, queue evicted
[74159.900896] amdgpu: Freeing queue vital buffer 0x7f5dae600000, queue evicted
[74159.940895] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74159.940908] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1000
[74159.940912] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[74159.940920] amdgpu 0000:c5:00.0: amdgpu: Failed to remove queue 0
[74159.940924] amdgpu: Resetting wave fronts (cpsch) on dev 0000000058c303b6
[74159.940927] amdgpu 0000:c5:00.0: amdgpu: no vmid pasid mapping supported
[74159.940927] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[74159.941031] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[74159.944284] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[74160.044686] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[74160.079198] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[74160.079924] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[74160.079969] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[74160.079971] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[74160.079974] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[74160.080853] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[74160.088019] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[74160.709700] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[74160.709708] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[74160.709710] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[74160.709712] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[74160.709713] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[74160.709715] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[74160.709716] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[74160.709717] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[74160.709719] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[74160.709721] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[74160.709722] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[74160.709724] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[74160.709725] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[74160.711825] amdgpu 0000:c5:00.0: amdgpu: GPU reset(8) succeeded!
[74160.711837] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[74243.815136] amdgpu: Freeing queue vital buffer 0x7f8741400000, queue evicted
[74257.667205] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74257.667212] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[74257.667214] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[74257.667217] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
[74257.667219] amdgpu 0000:c5:00.0: amdgpu: Failed to evict process queues
[74257.667221] amdgpu: Failed to quiesce KFD
[74257.667239] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[74257.667254] amdgpu 0000:c5:00.0: amdgpu: remove_all_kfd_queues_mes: Failed to remove queue 0 for dev 49700
[74257.667278] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[74257.669273] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[74259.772206] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74259.772214] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[74261.776183] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74261.776191] amdgpu 0000:c5:00.0: amdgpu: failed to unmap legacy queue
[74261.777671] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[74261.808782] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[74261.809266] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[74261.809349] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[74261.809360] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[74261.809373] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[74261.811030] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[74261.816743] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[74261.938533] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[74261.938541] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[74261.938543] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[74261.938545] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[74261.938546] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[74261.938548] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[74261.938549] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[74261.938551] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[74261.938552] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[74261.938554] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[74261.938555] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[74261.938557] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[74261.938558] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[74261.940336] amdgpu 0000:c5:00.0: amdgpu: GPU reset(9) succeeded!
[74261.940348] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[74262.586736] amdgpu: Freeing queue vital buffer 0x7f526d400000, queue evicted
[74262.586744] amdgpu: Freeing queue vital buffer 0x7f527d800000, queue evicted
[74262.586747] amdgpu: Freeing queue vital buffer 0x7f55d4200000, queue evicted
[74262.586749] amdgpu: Freeing queue vital buffer 0x7f55d4800000, queue evicted
[74262.586752] amdgpu: Freeing queue vital buffer 0x7f55dd600000, queue evicted
[74262.630844] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[74262.630850] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1000
[74262.630852] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[74262.630855] amdgpu 0000:c5:00.0: amdgpu: Failed to remove queue 0
[74262.630857] amdgpu: Resetting wave fronts (cpsch) on dev 0000000058c303b6
[74262.630859] amdgpu 0000:c5:00.0: amdgpu: no vmid pasid mapping supported
[74262.630859] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[74262.630938] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[74262.634581] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[74262.726752] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[74262.761776] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[74262.762445] [drm] PCIE GART of 512M enabled (table at 0x00000083FFD00000).
[74262.762517] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[74262.762521] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[74262.762525] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[74262.764668] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[74262.771408] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x08005700
[74263.510407] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[74263.510415] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[74263.510417] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[74263.510419] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[74263.510421] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[74263.510422] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[74263.510423] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[74263.510425] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[74263.510426] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[74263.510428] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[74263.510430] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[74263.510431] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[74263.510433] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[74263.512637] amdgpu 0000:c5:00.0: amdgpu: GPU reset(10) succeeded!
[74263.512650] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
```

```
$: cat /proc/cmdline
root=LABEL=ArchLinux rw initrd=boot\amd-ucode.img resume=LABEL=swap zswap.enabled=0 sysrq_always_enabled=1 amdgpu.gpu_recovery=1 initrd=\boot\initramfs-linux-xanmod.img
```

```
 ╰──➤ $ pacman -Q |grep -E 'rocm|amd'
amd-ucode 20260221-1
amdgpu_top 0.11.2-1
hip-runtime-amd 7.2.0-1
lib32-vulkan-amdgpu-pro 25.10_2202160-1
linux-amd-drm-fixes 6.19.2026.02.05-1
linux-amd-drm-fixes-headers 6.19.2026.02.05-1
linux-firmware-amdgpu 20260221-1
ollama-rocm 0.17.0-1
python-pytorch-rocm 2.10.0-2
python-torchaudio-rocm 2.10.0-3
rocm-cmake 7.2.0-1
rocm-core 7.2.0-2
rocm-device-libs 2:7.2.0-1
rocm-hip-libraries 7.2.0-1
rocm-hip-runtime 7.2.0-1
rocm-hip-sdk 7.2.0-1
rocm-language-runtime 7.2.0-1
rocm-llvm 2:7.2.0-1
rocm-opencl-runtime 7.2.0-1
rocm-opencl-sdk 7.2.0-1
rocm-smi-lib 7.2.0-1
rocminfo 7.2.0-1
vulkan-amdgpu-pro 25.10_2202160-1
xf86-video-amdgpu 25.0.0-1
```

```
 ╰──➤ $ uname -a
Linux mingfan 6.18.13-x64v3-xanmod1-1 #1 SMP PREEMPT_DYNAMIC Fri, 20 Feb 2026 05:25:15 +0000 x86_64 GNU/Linux
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.15
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 7840HS w/ Radeon 780M Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 7840HS w/ Radeon 780M Graphics
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
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5137                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    49116096(0x2ed73c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    49116096(0x2ed73c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    49116096(0x2ed73c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    49116096(0x2ed73c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1103                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon 780M Graphics           
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      2048(0x800) KB                     
  Chip ID:                 5567(0x15bf)                       
  ASIC Revision:           7(0x7)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2700                               
  BDFID:                   50432                              
  Internal Node ID:        1                                  
  Compute Unit:            12                                 
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       APU
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 67                                 
  SDMA engine uCode::      23                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    24558048(0x176b9e0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    24558048(0x176b9e0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1103         
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*******                  
Agent 3                  
*******                  
  Name:                    aie2                               
  Uuid:                    AIE-XX                             
  Marketing Name:          RyzenAI-npu1                       
  Vendor Name:             AMD                                
  Feature:                 AGENT_DISPATCH                     
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        1(0x1)                             
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          64(0x40)                           
  Queue Type:              SINGLE                             
  Node:                    0                                  
  Device Type:             DSP                                
  Cache Info:              
    L2:                      2048(0x800) KB                     
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          0(0x0)                             
  Max Clock Freq. (MHz):   0                                  
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            0                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:0                                  
  Memory Properties:       
  Features:                AGENT_DISPATCH
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, COARSE GRAINED
      Size:                    49116096(0x2ed73c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65536(0x10000) KB                  
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    49116096(0x2ed73c0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***
```


### Additional Information

_No response_