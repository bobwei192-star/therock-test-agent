# rocminfo HSA_STATUS_ERROR_OUT_OF_RESOURCES in Ubuntu

- **Issue #:** 1758
- **State:** closed
- **Created:** 2022-06-22T01:04:58Z
- **Updated:** 2023-12-21T19:29:16Z
- **URL:** https://github.com/ROCm/ROCm/issues/1758

we are hitting this common issue, and have tried to add current user (root) to video and render group. It still doesn't help. Here are the details:

```
rocminfo
ROCk module is loaded
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1140
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

rocm-smi
======================= ROCm System Management Interface =======================
================================= Concise Info =================================
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
ERROR: 15 GPU[0]: power: Data (usually from reading a file) was not of the type that was expected
================================================================================
================================================================================
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
ERROR: 15 GPU[0]:Data (usually from reading a file) was not of the type that was expected
GPU  Temp  AvgPwr  SCLK  MCLK  Fan  Perf     PwrCap       VRAM%  GPU%
0    N/A   N/A     None  None  0%   unknown  Unsupported    0%   0%
================================================================================
============================= End of ROCm SMI Log ==============================
```

OS:
```
uname -m && cat /etc/*release
x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.4 LTS"
NAME="Ubuntu"
VERSION="20.04.4 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.4 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```

Kernel
```
uname -a
Linux molokai 5.8.0-63-generic #71~20.04.1-Ubuntu SMP Thu Jul 15 17:46:08 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

GPU
[Radeon RX 6950 XT 16GB GDDR6 ](https://www.newegg.com/asrock-radeon-rx-6950-xt-rx6950xt-ocf-16g/p/N82E16814930073?Item=N82E16814930073)
```
root@molokai:~/yue# lspci | grep AMD
ca:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Upstream Port of PCI Express Switch (rev c0)
cb:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Downstream Port of PCI Express Switch (rev ff)
cc:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 73a5 (rev ff)
cc:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device ab28 (rev ff)
```

CPU
```
lscpu
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 57 bits virtual
CPU(s):                          112
On-line CPU(s) list:             0-111
Thread(s) per core:              2
Core(s) per socket:              28
Socket(s):                       2
NUMA node(s):                    2
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           106
Model name:                      Intel(R) Xeon(R) Gold 6348 CPU @ 2.60GHz
Stepping:                        6
Frequency boost:                 enabled
CPU MHz:                         800.459
CPU max MHz:                     3500.0000
CPU min MHz:                     800.0000
BogoMIPS:                        5200.00
Virtualization:                  VT-x
L1d cache:                       2.6 MiB
L1i cache:                       1.8 MiB
L2 cache:                        70 MiB
L3 cache:                        84 MiB
NUMA node0 CPU(s):               0-27,56-83
NUMA node1 CPU(s):               28-55,84-111
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Enhanced IBRS, IBPB conditional, RSB filling
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi
                                  mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfm
                                 on pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 mo
                                 nitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic
                                  movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpu
                                 id_fault epb cat_l3 invpcid_single intel_ppin ssbd mba ibrs ibpb stibp ibrs_enhanced tpr
                                 _shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms i
                                 nvpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt av
                                 x512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm
                                 _mbm_total cqm_mbm_local split_lock_detect wbnoinvd dtherm ida arat pln pts avx512vbmi u
                                 mip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo
                                 pcntdq la57 rdpid fsrm md_clear pconfig flush_l1d arch_capabilities

```

dmsg contains some errors regarding drm, not sure those are related

```
[    0.000000] Linux version 5.8.0-63-generic (buildd@lgw01-amd64-035) (gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #71~20.04.1-Ubuntu SMP Thu Jul 15 17:46:08 UTC 2021 (Ubuntu 5.8.0-63.71~20.04.1-generic 5.8.18)
[    4.949205] amdkcl: loading out-of-tree module taints kernel.
[    4.955769] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    5.158645] [drm] amdgpu kernel modesetting enabled.
[    5.158649] [drm] amdgpu version: 5.13.20.22.10
[    5.158842] amdgpu: CRAT table not found
[    5.158845] amdgpu: Virtual CRAT table created for CPU
[    5.158858] amdgpu: Topology: Add CPU node
[    5.163810] amdkcl: is_firmware_framebuffer:enable the runtime pm
[    5.164024] amdgpu 0000:cc:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
[    5.166437] amdgpu 0000:cc:00.0: amdgpu: Fetched VBIOS from VFCT
[    5.166444] amdgpu: ATOM BIOS: 113-EXT800376-L04
[    5.166543] amdgpu 0000:cc:00.0: amdgpu: MEM ECC is not presented.
[    5.166547] amdgpu 0000:cc:00.0: amdgpu: SRAM ECC is not presented.
[    5.166582] amdgpu 0000:cc:00.0: BAR 2: releasing [mem 0x208ff0000000-0x208ff01fffff 64bit pref]
[    5.166589] amdgpu 0000:cc:00.0: BAR 0: releasing [mem 0x208fe0000000-0x208fefffffff 64bit pref]
[    5.166668] amdgpu 0000:cc:00.0: BAR 0: assigned [mem 0x208000000000-0x2083ffffffff 64bit pref]
[    5.166686] amdgpu 0000:cc:00.0: BAR 2: assigned [mem 0x208400000000-0x2084001fffff 64bit pref]
[    5.166823] amdgpu 0000:cc:00.0: amdgpu: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used)
[    5.166831] amdgpu 0000:cc:00.0: amdgpu: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[    5.166837] amdgpu 0000:cc:00.0: amdgpu: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF
[    5.166977] [drm] amdgpu: 16368M of VRAM memory ready
[    5.166985] [drm] amdgpu: 257544M of GTT memory ready.
[    6.289620] amdgpu 0000:cc:00.0: amdgpu: STB initialized to 2048 entries
[    6.345613] amdgpu 0000:cc:00.0: amdgpu: Will use PSP to load VCN firmware
[    6.561007] amdgpu 0000:cc:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[    6.562892] amdgpu 0000:cc:00.0: amdgpu: use vbios provided pptable
[    6.639350] amdgpu 0000:cc:00.0: amdgpu: SMU is initialized successfully!
[    6.658830] amdkcl: drm_connector_attach_dp_subconnector_property is not supported
[    6.688109] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    6.766087] amdgpu: HMM registered 16368MB device memory
[    6.767114] amdgpu: Virtual CRAT table created for GPU
[    6.768139] amdgpu: Topology: Add dGPU node [0x73a5:0x1002]
[    6.768661] kfd kfd: amdgpu: added device 1002:73a5
[    6.769203] amdgpu 0000:cc:00.0: amdgpu: SE 4, SH per SE 2, CU per SH 10, active_cu_number 80
[    6.769800] amdgpu 0000:cc:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[    6.770330] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[    6.770860] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[    6.771382] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[    6.771975] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[    6.772481] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[    6.772981] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[    6.773476] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[    6.773965] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[    6.774447] amdgpu 0000:cc:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[    6.774920] amdgpu 0000:cc:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[    6.775381] amdgpu 0000:cc:00.0: amdgpu: ring sdma1 uses VM inv eng 13 on hub 0
[    6.775889] amdgpu 0000:cc:00.0: amdgpu: ring sdma2 uses VM inv eng 14 on hub 0
[    6.776321] amdgpu 0000:cc:00.0: amdgpu: ring sdma3 uses VM inv eng 15 on hub 0
[    6.776737] amdgpu 0000:cc:00.0: amdgpu: ring vcn_dec_0 uses VM inv eng 0 on hub 1
[    6.777143] amdgpu 0000:cc:00.0: amdgpu: ring vcn_enc_0.0 uses VM inv eng 1 on hub 1
[    6.777541] amdgpu 0000:cc:00.0: amdgpu: ring vcn_enc_0.1 uses VM inv eng 4 on hub 1
[    6.777933] amdgpu 0000:cc:00.0: amdgpu: ring vcn_dec_1 uses VM inv eng 5 on hub 1
[    6.778321] amdgpu 0000:cc:00.0: amdgpu: ring vcn_enc_1.0 uses VM inv eng 6 on hub 1
[    6.778706] amdgpu 0000:cc:00.0: amdgpu: ring vcn_enc_1.1 uses VM inv eng 7 on hub 1
[    6.779077] amdgpu 0000:cc:00.0: amdgpu: ring jpeg_dec uses VM inv eng 8 on hub 1
[    6.780461] amdgpu 0000:cc:00.0: amdgpu: Using BACO for runtime pm
[    6.789520] [drm] Initialized amdgpu 3.45.0 20150101 for 0000:cc:00.0 on minor 1
[    6.821863] amdgpu 0000:cc:00.0: [drm] Cannot find any crtc or sizes
[   11.092796] snd_hda_intel 0000:cc:00.1: bound 0000:cc:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[  171.656524] amdgpu 0000:cc:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[  171.656533] amdgpu 0000:cc:00.0: amdgpu: SMU is resuming...
[  171.656561] amdgpu 0000:cc:00.0: amdgpu: dpm has been enabled
[  171.661406] amdgpu 0000:cc:00.0: amdgpu: SMU is resumed successfully!
[  171.712569] amdgpu 0000:cc:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[  171.712573] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[  171.712575] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[  171.712577] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[  171.712579] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[  171.712581] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[  171.712583] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[  171.712586] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[  171.712589] amdgpu 0000:cc:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[  171.712591] amdgpu 0000:cc:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[  171.712593] amdgpu 0000:cc:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[  171.712595] amdgpu 0000:cc:00.0: amdgpu: ring sdma1 uses VM inv eng 13 on hub 0
[  171.712597] amdgpu 0000:cc:00.0: amdgpu: ring sdma2 uses VM inv eng 14 on hub 0
[  171.712599] amdgpu 0000:cc:00.0: amdgpu: ring sdma3 uses VM inv eng 15 on hub 0
[  171.712601] amdgpu 0000:cc:00.0: amdgpu: ring vcn_dec_0 uses VM inv eng 0 on hub 1
[  171.712603] amdgpu 0000:cc:00.0: amdgpu: ring vcn_enc_0.0 uses VM inv eng 1 on hub 1
[  171.712605] amdgpu 0000:cc:00.0: amdgpu: ring vcn_enc_0.1 uses VM inv eng 4 on hub 1
[  171.712607] amdgpu 0000:cc:00.0: amdgpu: ring vcn_dec_1 uses VM inv eng 5 on hub 1
[  171.712609] amdgpu 0000:cc:00.0: amdgpu: ring vcn_enc_1.0 uses VM inv eng 6 on hub 1
[  171.712611] amdgpu 0000:cc:00.0: amdgpu: ring vcn_enc_1.1 uses VM inv eng 7 on hub 1
[  171.712613] amdgpu 0000:cc:00.0: amdgpu: ring jpeg_dec uses VM inv eng 8 on hub 1
[  171.724868] amdgpu 0000:cc:00.0: [drm] Cannot find any crtc or sizes
[  171.724881] amdgpu 0000:cc:00.0: [drm] Cannot find any crtc or sizes
[  186.744269] amdgpu 0000:cc:00.0: can't change power state from D3cold to D0 (config space inaccessible)
[  197.034042] [drm:gmc_v10_0_flush_vm_hub.constprop.0 [amdgpu]] *ERROR* Timeout waiting for VM flush hub: 0!
[  197.144364] [drm:gmc_v10_0_flush_vm_hub.constprop.0 [amdgpu]] *ERROR* Timeout waiting for sem acquire in VM flush!
[  197.254470] [drm:gmc_v10_0_flush_vm_hub.constprop.0 [amdgpu]] *ERROR* Timeout waiting for VM flush hub: 1!
[  197.364499] [drm:gmc_v10_0_flush_vm_hub.constprop.0 [amdgpu]] *ERROR* Timeout waiting for sem acquire in VM flush!
[  197.474512] [drm:gmc_v10_0_flush_vm_hub.constprop.0 [amdgpu]] *ERROR* Timeout waiting for VM flush hub: 1!
[  197.584777] [drm:gmc_v10_0_flush_vm_hub.constprop.0 [amdgpu]] *ERROR* Timeout waiting for VM flush hub: 0!
[  197.625363] amdgpu 0000:cc:00.0: amdgpu: RAS Init Status: 0xFFFFFFFF
[  197.625608] amdgpu 0000:cc:00.0: amdgpu: RAP TA initialize fail (0) status -1.
[  197.625611] amdgpu 0000:cc:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[  197.625616] amdgpu 0000:cc:00.0: amdgpu: SMU is resuming...
[  197.625623] amdgpu 0000:cc:00.0: amdgpu: dpm has been enabled
[  197.625627] amdgpu 0000:cc:00.0: amdgpu: SMU is resumed successfully!
[  201.747571] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  201.859117] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  201.970589] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  202.082050] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  202.193481] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  202.304905] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  202.416340] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  202.416717] WARNING: CPU: 0 PID: 1090 at /var/lib/dkms/amdgpu/5.13.20.22.10-1420322/build/amd/amdgpu/../display/dc/dcn20/dcn20_hubbub.c:570 hubbub2_get_dchub_ref_freq+0x9f/0xb0 [amdgpu]
[  202.416719] Modules linked in: nls_iso8859_1 dm_multipath scsi_dh_rdac scsi_dh_emc scsi_dh_alua intel_rapl_msr intel_rapl_common dax_pmem_compat device_dax nd_pmem dax_pmem_core nd_btt i10nm_edac ipmi_ssif x86_pkg_temp_thermal intel_powerclamp input_leds joydev coretemp kvm_intel kvm rapl rndis_host cdc_ether usbnet mii snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic ledtrig_audio efi_pstore snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event isst_if_mmio isst_if_mbox_pci isst_if_common snd_rawmidi snd_seq snd_seq_device snd_timer snd soundcore mei_me mei ioatdma acpi_ipmi ipmi_si acpi_pad nfit acpi_power_meter mac_hid sch_fq_codel ipmi_devintf ipmi_msghandler msr parport_pc ppdev lp parport ip_tables x_tables autofs4 btrfs blake2b_generic raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear hid_generic usbhid hid amdgpu(OE) iommu_v2 amdttm(OE)
[  202.416771]  amd_sched(OE) ast drm_vram_helper amdkcl(OE) drm_ttm_helper ttm i2c_algo_bit drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops crct10dif_pclmul cec crc32_pclmul nvme rc_core ghash_clmulni_intel ixgbe aesni_intel xfrm_algo crypto_simd ahci i2c_i801 xhci_pci cryptd dca nvme_core glue_helper drm mdio xhci_pci_renesas i2c_smbus libahci wmi
[  202.417090] RIP: 0010:hubbub2_get_dchub_ref_freq+0x9f/0xb0 [amdgpu]
[  202.417403]  dcn30_init_hw+0x4ea/0x7b0 [amdgpu]
[  202.417681]  ? amdgpu_dm_dmub_reg_read+0x23/0x30 [amdgpu]
[  202.417948]  dc_set_power_state+0x11b/0x160 [amdgpu]
[  202.418216]  dm_resume+0xd4/0x5c0 [amdgpu]
[  202.418368]  amdgpu_device_ip_resume_phase2+0x6b/0xd0 [amdgpu]
[  202.418518]  ? amdgpu_device_fw_loading+0xb9/0x140 [amdgpu]
[  202.418693]  amdgpu_device_resume+0xac/0x1f0 [amdgpu]
[  202.418868]  amdgpu_pmops_runtime_resume+0x83/0xe0 [amdgpu]
[  203.207965] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  203.319387] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  203.430816] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  203.542231] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  203.653718] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  203.765261] [drm:dc_dmub_srv_wait_idle [amdgpu]] *ERROR* Error waiting for DMUB idle: status=3
[  203.875624] amdgpu 0000:cc:00.0: amdgpu: rlc autoload: gc ucode autoload timeout
[  203.875805] [drm:amdgpu_device_ip_resume_phase2 [amdgpu]] *ERROR* resume of IP block <gfx_v10_0> failed -110
[  203.875810] amdgpu 0000:cc:00.0: amdgpu: amdgpu_device_ip_resume failed (-110).

```



