# Training model results in SIGSEGV, stuck at epoch 1 (comgr)

- **Issue #:** 1768
- **State:** closed
- **Created:** 2022-07-09T18:12:34Z
- **Updated:** 2024-05-10T22:06:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1768

Hello, I've just recently installed ROCm on arch with the [rocm-arch](https://github.com/rocm-arch/rocm-arch) repository. Everything has worked up to this point (no initial errors, `clinfo`, `rocm-smi`, and `rocminfo` produce outputs). 

When trying to train a network, python stops at epoch 1 for a few minutes before ending with:
`Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)`

The specific output when running the program (before segfault):
```
2022-07-09 13:12:25.368489: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.562609: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.562657: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.563104: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-07-09 13:12:25.563884: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.563989: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.564035: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.564674: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.564710: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.564743: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-07-09 13:12:25.564898: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 15868 MB memory:  -> device: 0, name: AMD Radeon RX 6950 XT, pci bus id: 0000:03:00.0
2022-07-09 13:12:26.111186: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-07-09 13:12:26.114009: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-07-09 13:12:26.116080: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
Epoch 1/20
2022-07-09 13:12:26.378430: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
```

dmesg error that reems to be related to comgr:
```
python[3108]: segfault at 7f0dffff4008 ip 00007f143b971838 sp 00007f0e32ff88a0 error 4 in libamd_comgr.so.2.4[7f1438d46000+4d8a000]
Code: 40 00 f3 0f 6f 68 10 f3 0f 6f 00 48 83 e8 80 48 83 c7 10 f3 0f 6f 48 a0 f3 0f 6f 70 b0 0f c6 c5 88 66 0f 6f d0 f3 0f 6f 78 d0 <f3> 0f 6f 68 f0 0f c6 ce 88 66 0f 61 c1 66 0f 69 d1 66 0f 6f c8 66
```

possibly associated dmesg stacktrace: 
```
[  419.962259] ------------[ cut here ]------------
[  419.962261] WARNING: CPU: 6 PID: 264 at drivers/gpu/drm/ttm/ttm_bo.c:409 ttm_bo_release+0x2e9/0x310 [ttm]
[  419.962267] Modules linked in: rfcomm snd_seq_dummy snd_hrtimer snd_seq snd_seq_device cmac algif_hash algif_skcipher af_alg ccm xt_CHECKSUM xt_MASQUERADE xt_conntrack ipt_REJECT nf_reject_ipv4 xt_tcpudp nft_compat snd_sof_pci_intel_cnl snd_sof_intel_hda_common soundwire_intel intel_rapl_msr nft_chain_nat intel_rapl_common soundwire_generic_allocation bnep nf_nat soundwire_cadence snd_sof_intel_hda nf_conntrack snd_sof_pci btusb snd_sof_xtensa_dsp btrtl snd_sof btbcm nf_defrag_ipv6 btintel nf_defrag_ipv4 soundwire_bus bluetooth snd_soc_skl snd_soc_hdac_hda snd_hda_ext_core snd_soc_sst_ipc nft_counter ecdh_generic iwlmvm snd_soc_sst_dsp snd_soc_acpi_intel_match snd_soc_acpi snd_soc_core snd_hda_codec_realtek intel_tcc_cooling x86_pkg_temp_thermal intel_powerclamp snd_hda_codec_generic snd_compress coretemp ac97_bus ledtrig_audio snd_hda_codec_hdmi snd_pcm_dmaengine kvm_intel snd_hda_intel mousedev joydev nf_tables mac80211 iTCO_wdt libcrc32c snd_intel_dspcfg snd_intel_sdw_acpi
[  419.962290]  intel_pmc_bxt mei_hdcp ee1004 kvm amdgpu iTCO_vendor_support snd_hda_codec libarc4 nfnetlink crct10dif_pclmul intel_wmi_thunderbolt mxm_wmi wmi_bmof bridge squashfs snd_hda_core crc32_pclmul stp qrtr ghash_clmulni_intel llc ns loop iwlwifi i915 aesni_intel snd_hwdep intel_spi_pci snd_pcm crypto_simd cryptd r8169 ucsi_ccg intel_spi rapl realtek gpu_sched spi_nor snd_timer typec_ucsi mei_me vfat intel_cstate mdio_devres drm_ttm_helper cfg80211 fat snd typec i2c_i801 intel_uncore pcspkr libphy mtd mei i2c_smbus rfkill roles ttm soundcore intel_pch_thermal intel_gtt wmi video acpi_tad acpi_pad mac_hid dm_multipath dm_mod ipmi_devintf ipmi_msghandler sg fuse crypto_user ip_tables x_tables ext4 crc32c_generic crc16 mbcache jbd2 usbhid crc32c_intel xhci_pci vfio_pci vfio_pci_core irqbypass vfio_virqfd vfio_iommu_type1 vfio
[  419.962319] CPU: 6 PID: 264 Comm: kworker/6:1 Not tainted 5.15.50-1-MANJARO #1 fffffd25ed6fe5b8459d1f2fe9b1fccc660ede08
[  419.962321] Hardware name: Micro-Star International Co., Ltd. MS-7C75/Z490-A PRO (MS-7C75), BIOS 2.80 01/30/2021
[  419.962322] Workqueue: kfd_process_wq kfd_process_wq_release [amdgpu]
[  419.962494] RIP: 0010:ttm_bo_release+0x2e9/0x310 [ttm]
[  419.962498] Code: e8 dc ff 39 fb e9 b2 fd ff ff 49 8b 7e 98 b9 28 23 00 00 31 d2 be 01 00 00 00 e8 22 22 3a fb 49 8b 46 e8 eb 9e 48 89 e8 eb 99 <0f> 0b e9 38 fd ff ff e8 7b fd 39 fb e9 ef fe ff ff be 03 00 00 00
[  419.962499] RSP: 0018:ffffbbbcc076bcc8 EFLAGS: 00010202
[  419.962500] RAX: 0000000000000001 RBX: ffffbbbcc076bd10 RCX: 0000000000000001
[  419.962501] RDX: ffffa011d3f531b8 RSI: 0000000000000000 RDI: ffffa011d3f531b8
[  419.962501] RBP: ffffa0116e965270 R08: 0000000000000000 R09: 0000000000000000
[  419.962502] R10: 0000000000000000 R11: 0000000000000000 R12: ffffa011d3f53000
[  419.962502] R13: ffffa011d3f53058 R14: ffffa011d3f531b8 R15: ffffa01160618630
[  419.962503] FS:  0000000000000000(0000) GS:ffffa0187e180000(0000) knlGS:0000000000000000
[  419.962504] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  419.962505] CR2: 00007fdc809b4000 CR3: 000000017aabe004 CR4: 00000000007706e0
[  419.962505] PKRU: 55555554
[  419.962506] Call Trace:
[  419.962507]  <TASK>
[  419.962509]  amdgpu_bo_unref+0x1a/0x30 [amdgpu 4e9ddf1f39fdbedfe96056dc66601a4b2d649f8a]
[  419.962598]  amdgpu_gem_object_free+0x30/0x50 [amdgpu 4e9ddf1f39fdbedfe96056dc66601a4b2d649f8a]
[  419.962687]  amdgpu_amdkfd_gpuvm_free_memory_of_gpu+0x35e/0x3c0 [amdgpu 4e9ddf1f39fdbedfe96056dc66601a4b2d649f8a]
[  419.962797]  kfd_process_device_free_bos+0xa1/0xf0 [amdgpu 4e9ddf1f39fdbedfe96056dc66601a4b2d649f8a]
[  419.962903]  kfd_process_wq_release+0x20d/0x2e0 [amdgpu 4e9ddf1f39fdbedfe96056dc66601a4b2d649f8a]
[  419.963008]  process_one_work+0x1c7/0x390
[  419.963011]  worker_thread+0x4d/0x3a0
[  419.963012]  ? process_one_work+0x390/0x390
[  419.963013]  kthread+0x120/0x150
[  419.963015]  ? set_kthread_struct+0x50/0x50
[  419.963016]  ret_from_fork+0x1f/0x30
[  419.963018]  </TASK>
[  419.963019] ---[ end trace 6a8afef99fdf3d07 ]---
```

gdb bt:
```
#0  0x00007f525f7dd860 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
[Current thread is 1 (Thread 0x7f4b637fe640 (LWP 3650))]
(gdb) bt
#0  0x00007f525f7dd860 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#1  0x00007f525f80adc6 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#2  0x00007f525f80c696 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#3  0x00007f525f80c751 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#4  0x00007f525f8119da in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#5  0x00007f525f8131ed in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#6  0x00007f525f84f187 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#7  0x00007f525f3d11d7 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#8  0x00007f525f3d182f in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#9  0x00007f525f45e135 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#10 0x00007f525f3d537c in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#11 0x00007f525d6acfdf in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#12 0x00007f525cc69b22 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#13 0x00007f525cc6ac2f in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#14 0x00007f525cc6b2f0 in ?? () from /opt/rocm/lib/libamd_comgr.so.2
#15 0x00007f525cc768a8 in amd_comgr_do_action () from /opt/rocm/lib/libamd_comgr.so.2
#16 0x00007f512a8924d7 in ?? () from /opt/rocm/lib/libMIOpen.so
#17 0x00007f512a8868b6 in miopen::comgr::BuildHip(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, miopen::TargetProperties const&, std::vector<char, std::allocator<char> >&) () from /opt/rocm/lib/libMIOpen.so
#18 0x00007f512a883ef4 in miopen::HIPOCProgramImpl::BuildCodeObjectInMemory(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) () from /opt/rocm/lib/libMIOpen.so
#19 0x00007f512a883caf in miopen::HIPOCProgramImpl::BuildCodeObject(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) () from /opt/rocm/lib/libMIOpen.so
#20 0x00007f512a8835a2 in miopen::HIPOCProgramImpl::HIPOCProgramImpl(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, miopen::TargetProperties const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) () from /opt/rocm/lib/libMIOpen.so
#21 0x00007f512a884e20 in ?? () from /opt/rocm/lib/libMIOpen.so
#22 0x00007f512a8841ee in miopen::HIPOCProgram::HIPOCProgram(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, miopen::TargetProperties const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) () from /opt/rocm/lib/libMIOpen.so
#23 0x00007f512a8809db in miopen::Handle::LoadProgram(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::ba
```

Please tell me if there's any other diagnostic information I can provide.