# [Issue]: GPU hang on AMD AI+ 395pro(gfx1151 + ubuntu24.04 + linux Kenerl 6.14)

- **Issue #:** 5151
- **State:** open
- **Created:** 2025-08-05T04:02:03Z
- **Updated:** 2025-11-08T17:39:08Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5151

### Problem Description

OS:
NAME="Ubuntu"
VERSION="24.04.2 LTS (Noble Numbat)"
CPU: 
model name      : AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
GPU:
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Name:                    gfx1151                            
  Marketing Name:          AMD Radeon Graphics                
      Name:                    amdgcn-amd-amdhsa--gfx1151         
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
  Name:                    aie2                               
  Marketing Name:          AIE-ML  

VRAM=64G by BIOS.

Using ollama to run the large model qwen3:30b, and continuously calling to keep the large model running, after running for a period of time, it was found that the GPU would reset. The GPU reset was not fixed. Kernel log:
```
Aug 05 08:56:22.546687 my-server kernel: amdgpu: Freeing queue vital buffer 0x78d1fa200000, queue evicted
Aug 05 08:56:22.546749 my-server kernel: amdgpu: Freeing queue vital buffer 0x78d206000000, queue evicted
Aug 05 08:56:22.546848 my-server kernel: amdgpu: Freeing queue vital buffer 0x78d37c200000, queue evicted
Aug 05 08:56:22.546867 my-server kernel: amdgpu: Freeing queue vital buffer 0x78d37e200000, queue evicted
Aug 05 08:56:22.546876 my-server kernel: amdgpu: Freeing queue vital buffer 0x78d384400000, queue evicted
Aug 05 08:56:24.669800 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
Aug 05 08:56:24.670058 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1806
Aug 05 08:56:24.670111 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
Aug 05 08:56:24.670186 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 4
Aug 05 08:56:24.670225 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!
Aug 05 08:56:24.670267 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 2
Aug 05 08:56:24.670660 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
Aug 05 08:56:24.670702 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 0
Aug 05 08:56:24.671654 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
Aug 05 08:56:24.671716 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
Aug 05 08:56:24.677663 my-server kernel: amdgpu: Freeing queue vital buffer 0x7bd139400000, queue evicted
Aug 05 08:56:24.677688 my-server kernel: amdgpu: Freeing queue vital buffer 0x7bd200200000, queue evicted
Aug 05 08:56:24.677696 my-server kernel: amdgpu: Freeing queue vital buffer 0x7bd201600000, queue evicted
Aug 05 08:56:24.677704 my-server kernel: amdgpu: Freeing queue vital buffer 0x7bd202400000, queue evicted
Aug 05 08:56:24.677712 my-server kernel: amdgpu: Freeing queue vital buffer 0x7bd203200000, queue evicted
Aug 05 08:56:25.714779 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:169 vmid:0 pasid:0)
Aug 05 08:56:25.714945 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:25.715008 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00040B53
Aug 05 08:56:25.715060 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          Faulty UTCL2 client ID: CPC (0x5)
Aug 05 08:56:25.715105 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          MORE_FAULTS: 0x1
Aug 05 08:56:25.715142 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          WALKER_ERROR: 0x1
Aug 05 08:56:25.715180 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          PERMISSION_FAULTS: 0x5
Aug 05 08:56:25.715222 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          MAPPING_ERROR: 0x1
Aug 05 08:56:25.715265 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          RW: 0x1
Aug 05 08:56:25.715302 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0)
Aug 05 08:56:25.715341 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:25.715378 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:169 vmid:0 pasid:0)
Aug 05 08:56:25.715413 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:25.715448 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0)
Aug 05 08:56:25.715484 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:25.715519 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:169 vmid:0 pasid:0)
Aug 05 08:56:25.715554 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:25.715589 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0)
Aug 05 08:56:25.715625 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:25.715668 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:169 vmid:0 pasid:0)
Aug 05 08:56:25.715703 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:25.715737 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0)
Aug 05 08:56:25.715771 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:27.428131 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=SUSPEND
Aug 05 08:56:27.428631 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: suspend of IP block <mes_v11_0> failed -110
Aug 05 08:56:27.714174 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:169 vmid:0 pasid:0)
Aug 05 08:56:27.714699 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:27.714868 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00040B53
Aug 05 08:56:27.715001 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          Faulty UTCL2 client ID: CPC (0x5)
Aug 05 08:56:27.715126 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          MORE_FAULTS: 0x1
Aug 05 08:56:27.715248 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          WALKER_ERROR: 0x1
Aug 05 08:56:27.715368 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          PERMISSION_FAULTS: 0x5
Aug 05 08:56:27.715488 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          MAPPING_ERROR: 0x1
Aug 05 08:56:27.715606 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          RW: 0x1
Aug 05 08:56:27.715749 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0)
Aug 05 08:56:27.715870 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x0000000000000000 from client 10
Aug 05 08:56:27.715987 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
Aug 05 08:56:27.747675 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
Aug 05 08:56:27.748110 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
Aug 05 08:56:27.754663 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
Aug 05 08:56:27.797668 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
Aug 05 08:56:27.797822 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Aug 05 08:56:27.797869 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Aug 05 08:56:27.797912 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
Aug 05 08:56:27.797950 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
Aug 05 08:56:27.797986 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
Aug 05 08:56:27.798022 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
Aug 05 08:56:27.798057 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
Aug 05 08:56:27.798092 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
Aug 05 08:56:27.798127 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
Aug 05 08:56:27.798164 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
Aug 05 08:56:27.798202 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
Aug 05 08:56:27.798236 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_0 uses VM inv eng 4 on hub 8
Aug 05 08:56:27.798271 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_1 uses VM inv eng 6 on hub 8
Aug 05 08:56:27.798311 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
Aug 05 08:56:27.798347 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vpe uses VM inv eng 7 on hub 8
Aug 05 08:56:27.838664 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset(6) succeeded!
Aug 05 09:01:42.326886 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.327198 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.327313 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58f7f000 from client 10
Aug 05 09:01:42.327410 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00901031
Aug 05 09:01:42.327516 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          Faulty UTCL2 client ID: TCP (0x8)
Aug 05 09:01:42.327610 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          MORE_FAULTS: 0x1
Aug 05 09:01:42.327720 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          WALKER_ERROR: 0x0
Aug 05 09:01:42.327812 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          PERMISSION_FAULTS: 0x3
Aug 05 09:01:42.327904 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          MAPPING_ERROR: 0x0
Aug 05 09:01:42.327995 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          RW: 0x0
Aug 05 09:01:42.328084 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.328173 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.328262 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58fda000 from client 10
Aug 05 09:01:42.328354 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00901030
Aug 05 09:01:42.328447 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          Faulty UTCL2 client ID: TCP (0x8)
Aug 05 09:01:42.328535 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          MORE_FAULTS: 0x0
Aug 05 09:01:42.328629 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          WALKER_ERROR: 0x0
Aug 05 09:01:42.328723 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          PERMISSION_FAULTS: 0x3
Aug 05 09:01:42.328813 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          MAPPING_ERROR: 0x0
Aug 05 09:01:42.328900 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:          RW: 0x0
Aug 05 09:01:42.328988 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.329075 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.329163 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58fad000 from client 10
Aug 05 09:01:42.329253 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.329341 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.329426 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58f67000 from client 10
Aug 05 09:01:42.329519 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.329605 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.329698 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58f62000 from client 10
Aug 05 09:01:42.330217 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.330394 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.330553 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58f76000 from client 10
Aug 05 09:01:42.330713 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.330841 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.330959 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58fd1000 from client 10
Aug 05 09:01:42.331078 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.331192 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.331307 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58fc2000 from client 10
Aug 05 09:01:42.331426 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.331541 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.331709 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58fc7000 from client 10
Aug 05 09:01:42.331876 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:9 pasid:32771)
Aug 05 09:01:42.332038 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:  in process ollama pid 3678233 thread ollama pid 3678241)
Aug 05 09:01:42.332206 my-server kernel: amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f3a58fbd000 from client 10
Aug 05 09:01:44.313823 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
Aug 05 09:01:44.314116 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1804
Aug 05 09:01:44.314183 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
Aug 05 09:01:44.314238 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 2
Aug 05 09:01:44.314280 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!
Aug 05 09:01:44.314318 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 0
Aug 05 09:01:44.315668 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 6
Aug 05 09:01:44.315995 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 5
Aug 05 09:01:44.316129 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 4
Aug 05 09:01:44.316351 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 3
Aug 05 09:01:44.316729 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 2
Aug 05 09:01:44.316808 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
Aug 05 09:01:44.316851 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 0
Aug 05 09:01:44.316893 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 6, simd_id 0, wgp_id 0
Aug 05 09:01:44.316901 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 8, simd_id 0, wgp_id 0
Aug 05 09:01:44.316907 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 6, simd_id 0, wgp_id 0
Aug 05 09:01:44.316922 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 9, simd_id 0, wgp_id 0
Aug 05 09:01:44.316928 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
Aug 05 09:01:44.316966 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 9, simd_id 0, wgp_id 0
Aug 05 09:01:44.316975 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 8, simd_id 0, wgp_id 0
Aug 05 09:01:44.316981 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 6, simd_id 0, wgp_id 0
Aug 05 09:01:44.316986 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 7, simd_id 0, wgp_id 0
Aug 05 09:01:44.316994 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 7, simd_id 0, wgp_id 0
Aug 05 09:01:44.316998 my-server kernel: amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 7, simd_id 0, wgp_id 0
Aug 05 09:01:44.317661 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
Aug 05 09:01:47.281746 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=SUSPEND
Aug 05 09:01:47.282276 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: suspend of IP block <mes_v11_0> failed -110
Aug 05 09:01:50.350694 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
Aug 05 09:01:50.380672 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
Aug 05 09:01:50.381696 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
Aug 05 09:01:50.390681 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
Aug 05 09:01:50.430680 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
Aug 05 09:01:50.430979 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Aug 05 09:01:50.431123 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Aug 05 09:01:50.431244 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
Aug 05 09:01:50.431361 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
Aug 05 09:01:50.431476 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
Aug 05 09:01:50.431589 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
Aug 05 09:01:50.431804 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
Aug 05 09:01:50.431891 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
Aug 05 09:01:50.431955 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
Aug 05 09:01:50.432012 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
Aug 05 09:01:50.432066 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
Aug 05 09:01:50.432124 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_0 uses VM inv eng 4 on hub 8
Aug 05 09:01:50.432175 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_1 uses VM inv eng 6 on hub 8
Aug 05 09:01:50.432227 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
Aug 05 09:01:50.432280 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vpe uses VM inv eng 7 on hub 8
Aug 05 09:01:50.473714 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset(7) succeeded!
Aug 05 09:01:51.339669 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f39cd400000, queue evicted
Aug 05 09:01:51.339748 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f3a41e00000, queue evicted
Aug 05 09:01:51.339757 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f3a58200000, queue evicted
Aug 05 09:01:51.339763 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f3bc6a00000, queue evicted
Aug 05 09:01:51.339770 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f3d90400000, queue evicted
Aug 05 09:01:52.078678 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d26d1000000, queue evicted
Aug 05 09:01:52.078761 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d2798600000, queue evicted
Aug 05 09:01:52.078776 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d2799c00000, queue evicted
Aug 05 09:01:52.078782 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d279aa00000, queue evicted
Aug 05 09:01:52.078787 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d293c400000, queue evicted
Aug 05 09:03:18.738736 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
Aug 05 09:03:18.739153 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1804
Aug 05 09:03:18.739296 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
Aug 05 09:03:18.739413 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 2
Aug 05 09:03:18.739524 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!
Aug 05 09:03:18.739634 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 0
Aug 05 09:03:18.739768 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 6
Aug 05 09:03:18.739821 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 5
Aug 05 09:03:18.740698 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 4
Aug 05 09:03:18.740788 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 3
Aug 05 09:03:18.740849 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 2
Aug 05 09:03:18.741657 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
Aug 05 09:03:18.741745 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 0
Aug 05 09:03:18.741782 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
Aug 05 09:03:18.742661 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
Aug 05 09:03:21.858692 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=SUSPEND
Aug 05 09:03:21.859146 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: suspend of IP block <mes_v11_0> failed -110
Aug 05 09:03:24.773689 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
Aug 05 09:03:24.804673 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
Aug 05 09:03:24.805667 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
Aug 05 09:03:24.810659 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
Aug 05 09:03:24.851669 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
Aug 05 09:03:24.851886 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Aug 05 09:03:24.852006 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Aug 05 09:03:24.852104 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
Aug 05 09:03:24.852198 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
Aug 05 09:03:24.852295 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
Aug 05 09:03:24.852372 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
Aug 05 09:03:24.852451 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
Aug 05 09:03:24.852550 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
Aug 05 09:03:24.852650 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
Aug 05 09:03:24.852961 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
Aug 05 09:03:24.853140 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
Aug 05 09:03:24.853271 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_0 uses VM inv eng 4 on hub 8
Aug 05 09:03:24.853393 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_1 uses VM inv eng 6 on hub 8
Aug 05 09:03:24.853511 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
Aug 05 09:03:24.853633 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: ring vpe uses VM inv eng 7 on hub 8
Aug 05 09:03:24.888683 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: GPU reset(8) succeeded!
Aug 05 09:03:25.394693 my-server kernel: amdgpu: Freeing queue vital buffer 0x7e8d40e00000, queue evicted
Aug 05 09:03:25.394803 my-server kernel: amdgpu: Freeing queue vital buffer 0x7e8d41c00000, queue evicted
Aug 05 09:03:25.394823 my-server kernel: amdgpu: Freeing queue vital buffer 0x7e9520800000, queue evicted
Aug 05 09:03:25.394838 my-server kernel: amdgpu: Freeing queue vital buffer 0x7e9568400000, queue evicted
Aug 05 09:03:25.394851 my-server kernel: amdgpu: Freeing queue vital buffer 0x7e95e8600000, queue evicted
Aug 05 09:03:26.470702 my-server kernel: amdgpu: Freeing queue vital buffer 0x6fff6c200000, queue evicted
Aug 05 09:03:26.470837 my-server kernel: amdgpu: Freeing queue vital buffer 0x6fff88a00000, queue evicted
Aug 05 09:03:26.470855 my-server kernel: amdgpu: Freeing queue vital buffer 0x6fff8aa00000, queue evicted
Aug 05 09:03:26.470870 my-server kernel: amdgpu: Freeing queue vital buffer 0x700112800000, queue evicted
Aug 05 09:03:26.470893 my-server kernel: amdgpu: Freeing queue vital buffer 0x700218800000, queue evicted
Aug 05 09:06:22.628671 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d09f0600000, queue evicted
Aug 05 09:06:22.628876 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d09f1400000, queue evicted
Aug 05 09:06:22.628944 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d11cb200000, queue evicted
Aug 05 09:06:22.628966 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d1218400000, queue evicted
Aug 05 09:06:22.628985 my-server kernel: amdgpu: Freeing queue vital buffer 0x7d1454200000, queue evicted
Aug 05 09:06:22.662673 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f1c48400000, queue evicted
Aug 05 09:06:22.662724 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f1cb9600000, queue evicted
Aug 05 09:06:22.662736 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f1cbda00000, queue evicted
Aug 05 09:06:22.662746 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f1e3e200000, queue evicted
Aug 05 09:06:22.662754 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f1e44200000, queue evicted
Aug 05 10:12:04.048989 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: No more SDMA queue to allocate
Aug 05 10:12:04.049457 my-server kernel: amdgpu: process pid 3929525 DQM create queue type 1 failed. ret -12
Aug 05 10:22:07.785676 my-server kernel: amdgpu: Freeing queue vital buffer 0x7bd795c00000, queue evicted
Aug 05 10:22:07.785822 my-server kernel: amdgpu: Freeing queue vital buffer 0x7bdf6ce00000, queue evicted
Aug 05 10:22:07.785837 my-server kernel: amdgpu: Freeing queue vital buffer 0x7bdfbc400000, queue evicted
Aug 05 10:22:07.785848 my-server kernel: amdgpu: Freeing queue vital buffer 0x7be03c600000, queue evicted
Aug 05 10:22:07.785855 my-server kernel: amdgpu: Freeing queue vital buffer 0x7be03d400000, queue evicted
Aug 05 10:22:08.262724 my-server kernel: amdgpu: Freeing queue vital buffer 0x700af9400000, queue evicted
Aug 05 10:22:08.262898 my-server kernel: amdgpu: Freeing queue vital buffer 0x700b6f200000, queue evicted
Aug 05 10:22:08.262916 my-server kernel: amdgpu: Freeing queue vital buffer 0x700cecc00000, queue evicted
Aug 05 10:22:08.262930 my-server kernel: amdgpu: Freeing queue vital buffer 0x700cef200000, queue evicted
Aug 05 10:22:08.262961 my-server kernel: amdgpu: Freeing queue vital buffer 0x700cf4200000, queue evicted
Aug 05 10:22:08.541720 my-server kernel: amdgpu: Freeing queue vital buffer 0x76fe13200000, queue evicted
Aug 05 10:22:08.541766 my-server kernel: amdgpu: Freeing queue vital buffer 0x76fe23200000, queue evicted
Aug 05 10:22:08.541782 my-server kernel: amdgpu: Freeing queue vital buffer 0x76fe3ea00000, queue evicted
Aug 05 10:22:08.541798 my-server kernel: amdgpu: Freeing queue vital buffer 0x76fe44400000, queue evicted
Aug 05 10:22:08.541814 my-server kernel: amdgpu: Freeing queue vital buffer 0x76fe45200000, queue evicted
Aug 05 10:22:08.900682 my-server kernel: amdgpu: Freeing queue vital buffer 0x7b39abe00000, queue evicted
Aug 05 10:22:08.900803 my-server kernel: amdgpu: Freeing queue vital buffer 0x7b39af200000, queue evicted
Aug 05 10:22:08.900817 my-server kernel: amdgpu: Freeing queue vital buffer 0x7b39b0800000, queue evicted
Aug 05 10:22:08.900826 my-server kernel: amdgpu: Freeing queue vital buffer 0x7b39d8200000, queue evicted
Aug 05 10:22:08.900836 my-server kernel: amdgpu: Freeing queue vital buffer 0x7b39d9000000, queue evicted
Aug 05 10:28:24.811915 my-server kernel: amdgpu 0000:c5:00.0: amdgpu: No more SDMA queue to allocate
Aug 05 10:28:24.812377 my-server kernel: amdgpu: process pid 3972722 DQM create queue type 1 failed. ret -12
Aug 05 10:38:31.154667 my-server kernel: amdgpu: Freeing queue vital buffer 0x7ef356600000, queue evicted
Aug 05 10:38:31.154810 my-server kernel: amdgpu: Freeing queue vital buffer 0x7ef378800000, queue evicted
Aug 05 10:38:31.154841 my-server kernel: amdgpu: Freeing queue vital buffer 0x7ef379600000, queue evicted
Aug 05 10:38:31.154866 my-server kernel: amdgpu: Freeing queue vital buffer 0x7ef37a400000, queue evicted
Aug 05 10:38:31.154900 my-server kernel: amdgpu: Freeing queue vital buffer 0x7ef37b200000, queue evicted
Aug 05 10:38:31.583679 my-server kernel: amdgpu: Freeing queue vital buffer 0x766ff9c00000, queue evicted
Aug 05 10:38:31.583823 my-server kernel: amdgpu: Freeing queue vital buffer 0x767042e00000, queue evicted
Aug 05 10:38:31.583843 my-server kernel: amdgpu: Freeing queue vital buffer 0x767048200000, queue evicted
Aug 05 10:38:31.583865 my-server kernel: amdgpu: Freeing queue vital buffer 0x767075600000, queue evicted
Aug 05 10:38:31.583884 my-server kernel: amdgpu: Freeing queue vital buffer 0x767076c00000, queue evicted
Aug 05 10:49:33.170710 my-server kernel: amdgpu: Freeing queue vital buffer 0x7ede95a00000, queue evicted
Aug 05 10:49:33.170879 my-server kernel: amdgpu: Freeing queue vital buffer 0x7edea8200000, queue evicted
Aug 05 10:49:33.170896 my-server kernel: amdgpu: Freeing queue vital buffer 0x7edeaa200000, queue evicted
Aug 05 10:49:33.170910 my-server kernel: amdgpu: Freeing queue vital buffer 0x7ee01c600000, queue evicted
Aug 05 10:49:33.170935 my-server kernel: amdgpu: Freeing queue vital buffer 0x7ee01d400000, queue evicted
Aug 05 10:49:46.725779 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f0c78e00000, queue evicted
Aug 05 10:49:46.725929 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f0c79c00000, queue evicted
Aug 05 10:49:46.725948 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f1459000000, queue evicted
Aug 05 10:49:46.725965 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f14a0400000, queue evicted
Aug 05 10:49:46.725977 my-server kernel: amdgpu: Freeing queue vital buffer 0x7f1524200000, queue evicted

```

### Operating System

ubuntu24.04

### CPU

 AMD RYZEN AI MAX+ 395

### GPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### ROCm Version

ROCm 6.4.2

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module version 6.12.12 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.15
Runtime Ext Version:     1.7
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
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
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
    L1:                      49152(0xc000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5187                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    65465664(0x3e6ed40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65465664(0x3e6ed40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65465664(0x3e6ed40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65465664(0x3e6ed40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1151                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon Graphics                
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
    L3:                      16384(0x4000) KB                   
  Chip ID:                 5510(0x1586)                       
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2900                               
  BDFID:                   50432                              
  Internal Node ID:        1                                  
  Compute Unit:            40                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
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
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 26                                 
  SDMA engine uCode::      14                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    67108864(0x4000000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    67108864(0x4000000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx1151         
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
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*******                  
Agent 3                  
*******                  
  Name:                    aie2                               
  Uuid:                    AIE-XX                             
  Marketing Name:          AIE-ML                             
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
    L3:                      16384(0x4000) KB                   
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
      Size:                    65465664(0x3e6ed40) KB             
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
      Size:                    65465664(0x3e6ed40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***   

### Additional Information

_No response_