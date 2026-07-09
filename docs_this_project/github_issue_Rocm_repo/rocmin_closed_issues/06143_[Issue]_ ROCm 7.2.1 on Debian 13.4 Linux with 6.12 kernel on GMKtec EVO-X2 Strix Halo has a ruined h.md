# [Issue]: ROCm 7.2.1 on Debian 13.4 Linux with 6.12 kernel on GMKtec EVO-X2 Strix Halo has a ruined hipallocator

- **Issue #:** 6143
- **State:** closed
- **Created:** 2026-04-12T18:27:23Z
- **Updated:** 2026-05-19T10:35:07Z
- **Labels:** status: assessed
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6143

### Problem Description

Having set the UMA buffer size to 96 GB in the BIOS and adjusted kernel parameters to 

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amdgpu.gttsize=98304 ttm.pages_limit=25000000 iommu=pt"

 the kernel crashes upon execution of the hip vectoradd test in :

(automatic1111) ai-service@GMKtec-EVO-X2:~/hip-examples/vectorAdd$ sudo dmesg -w | grep -iE "amdgpu|kfd|fault|ring"
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-6.12.74+deb13+1-amd64 root=UUID=cf6e5677-72ee-4993-97c8-635e9a091402 ro quiet splash amdgpu.gttsize=98304 ttm.pages_limit=25000000 iommu=pt
[    0.012587] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.12.74+deb13+1-amd64 root=UUID=cf6e5677-72ee-4993-97c8-635e9a091402 ro quiet splash amdgpu.gttsize=98304 ttm.pages_limit=25000000 iommu=pt
[    0.069755] pid_max: default: 32768 minimum: 301
[    0.072231] Yama: disabled by default; enable with sysctl kernel.yama.*
[    0.181675] smp: Bringing up secondary CPUs ...
[    0.207108] ACPI: PM: Registering ACPI NVS region [mem 0x0a200000-0x0a287fff] (557056 bytes)
[    0.207108] ACPI: PM: Registering ACPI NVS region [mem 0x7037f000-0x7137efff] (16777216 bytes)
[    0.429685] PCI: Ignoring E820 reservations for host bridge windows
[    0.460158] Low-power S0 idle used by default for system suspend
[    0.460249] iommu: Default domain type: Passthrough (set via kernel command line)
[    0.461999] NetLabel:  unlabeled traffic allowed by default
[    0.484903] PCI: CLS 64 bytes, default 64
[    0.486124] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.489309] Initialise system trusted keyrings
[    0.489520] integrity: Platform Keyring initialized
[    0.489522] integrity: Machine keyring initialized
[    0.632333] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    2.097755] resctrl: L3 monitoring detected
[    2.283340] nvme nvme0: 16/0/0 default/read/poll queues
[    2.292565] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.292871] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.293802] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.294492] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.295638] usb usb5: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.295894] usb usb6: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.296825] usb usb7: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.297050] usb usb8: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    3.526961] [drm] amdgpu kernel modesetting enabled.
[    3.526966] [drm] amdgpu version: 6.16.13
[    3.527876] amdgpu: Virtual CRAT table created for CPU
[    3.527882] amdgpu: Topology: Add CPU node
[    3.530770] amdgpu 0000:c5:00.0: enabling device (0006 -> 0007)
[    3.530830] amdgpu 0000:c5:00.0: amdgpu: initializing kernel modesetting (IP DISCOVERY 0x1002:0x1586 0x2014:0x801D 0xC1).
[    3.530851] amdgpu 0000:c5:00.0: amdgpu: register mmio base: 0xA0200000
[    3.530852] amdgpu 0000:c5:00.0: amdgpu: register mmio size: 1048576
[    3.533833] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 0 <common_v1_0_0> (soc21_common)
[    3.533835] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 1 <gmc_v11_0_0> (gmc_v11_0)
[    3.533836] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 2 <ih_v6_0_0> (ih_v6_1)
[    3.533837] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 3 <psp_v13_0_0> (psp)
[    3.533838] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 4 <smu_v14_0_0> (smu)
[    3.533839] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 5 <dce_v1_0_0> (dm)
[    3.533840] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 6 <gfx_v11_0_0> (gfx_v11_0)
[    3.533841] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 7 <sdma_v6_0_0> (sdma_v6_0)
[    3.533842] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 8 <vcn_v4_0_5> (vcn_v4_0_5)
[    3.533843] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 9 <jpeg_v4_0_5> (jpeg_v4_0_5)
[    3.533843] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 10 <mes_v11_0_0> (mes_v11_0)
[    3.533844] amdgpu 0000:c5:00.0: amdgpu: detected ip block number 11 <vpe_v6_1_0> (vpe_v6_1)
[    3.533866] amdgpu 0000:c5:00.0: amdgpu: Fetched VBIOS from VFCT
[    3.533867] amdgpu: ATOM BIOS: 113-STRXLGEN-001
[    3.539316] amdgpu 0000:c5:00.0: amdgpu: VPE: collaborate mode true
[    3.539319] amdgpu 0000:c5:00.0: amdgpu: Trusted Memory Zone (TMZ) feature disabled as experimental (default)
[    3.539366] amdgpu 0000:c5:00.0: amdgpu: vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[    3.539386] amdgpu 0000:c5:00.0: amdgpu: VRAM: 98304M 0x0000008000000000 - 0x00000097FFFFFFFF (98304M used)
[    3.539387] amdgpu 0000:c5:00.0: amdgpu: GART: 512M 0x00007FFF00000000 - 0x00007FFF1FFFFFFF
[    3.539802] amdgpu 0000:c5:00.0: amdgpu: amdgpu: 98304M of VRAM memory ready
[    3.539803] amdgpu 0000:c5:00.0: amdgpu: [drm] Configuring gttsize via module parameter is deprecated, please use ttm.pages_limit
[    3.539803] amdgpu 0000:c5:00.0: amdgpu: [drm] GTT size has been set as 103079215104 but TTM size has been set as 16638816256, this is unusual
[    3.539804] amdgpu 0000:c5:00.0: amdgpu: amdgpu: 98304M of GTT memory ready.
[    3.540839] amdgpu 0000:c5:00.0: amdgpu: [drm] Loading DMUB firmware via PSP: version=0x09003500
[    3.541207] amdgpu 0000:c5:00.0: amdgpu: [VCN instance 0] Found VCN firmware Version ENC: 1.24 DEC: 9 VEP: 0 Revision: 27
[    3.541247] amdgpu 0000:c5:00.0: amdgpu: [VCN instance 1] Found VCN firmware Version ENC: 1.24 DEC: 9 VEP: 0 Revision: 27
[    3.564978] amdgpu 0000:c5:00.0: amdgpu: reserve 0x8c00000 from 0x97e0000000 for PSP TMR
[    3.902695] amdgpu 0000:c5:00.0: amdgpu: RAS: optional ras ta ucode is not available
[    3.906615] amdgpu 0000:c5:00.0: amdgpu: RAP: optional rap ta ucode is not available
[    3.906617] amdgpu 0000:c5:00.0: amdgpu: SECUREDISPLAY: optional securedisplay ta ucode is not available
[    3.942098] amdgpu 0000:c5:00.0: amdgpu: SMU is initialized successfully!
[    3.943392] amdgpu 0000:c5:00.0: amdgpu: [drm] Display Core v3.2.359 initialized on DCN 3.5.1
[    3.943393] amdgpu 0000:c5:00.0: amdgpu: [drm] DP-HDMI FRL PCON supported
[    3.946146] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x09003500
[    3.949850] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.949938] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.950057] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.950170] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.950284] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.950333] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.950374] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.950415] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.950454] amdgpu 0000:c5:00.0: amdgpu: [drm] PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[    3.960319] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    3.960324] kfd kfd: amdgpu: Total number of KFD nodes to be created: 1
[    3.963144] amdgpu: Virtual CRAT table created for GPU
[    3.963938] amdgpu: Topology: Add dGPU node [0x1586:0x1002]
[    3.963939] kfd kfd: amdgpu: added device 1002:1586
[    3.963948] amdgpu 0000:c5:00.0: amdgpu: SE 2, SH per SE 2, CU per SH 10, active_cu_number 40
[    3.963952] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[    3.963953] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[    3.963953] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[    3.963953] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[    3.963954] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[    3.963954] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[    3.963955] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[    3.963955] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[    3.963955] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[    3.963956] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[    3.963956] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[    3.963957] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
[    3.963957] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_0 uses VM inv eng 4 on hub 8
[    3.963957] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_1 uses VM inv eng 6 on hub 8
[    3.963958] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[    3.963958] amdgpu 0000:c5:00.0: amdgpu: ring vpe uses VM inv eng 7 on hub 8
[    3.965096] amdgpu 0000:c5:00.0: amdgpu: Runtime PM not available
[    3.965457] [drm] Initialized amdgpu 3.64.0 for 0000:c5:00.0 on minor 0
[    3.987436] amdgpu 0000:c5:00.0: [drm] Cannot find any crtc or sizes
[    3.987486] amdgpu 0000:c5:00.0: [drm] Cannot find any crtc or sizes
[    3.987491] amdgpu 0000:c5:00.0: [drm] Cannot find any crtc or sizes
[    4.506008] systemd[1]: Queued start job for default target graphical.target.
[    4.761037] snd_hda_intel 0000:c5:00.1: bound 0000:c5:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[   10.882122] audit: type=1400 audit(1776016193.288:126): apparmor="STATUS" operation="profile_load" profile="unconfined" name="docker-default" pid=1942 comm="apparmor_parser"
[   11.099753] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[   11.287325] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:32770)
[   11.287341] amdgpu 0000:c5:00.0: amdgpu:  Process ollama pid 2231 thread ollama pid 2231
[   11.287345] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f1b61269000 from client 10
[   11.287349] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00800932
[   11.287351] amdgpu 0000:c5:00.0: amdgpu:      Faulty UTCL2 client ID: CPF (0x4)
[   11.287353] amdgpu 0000:c5:00.0: amdgpu:      MORE_FAULTS: 0x0
[   11.287354] amdgpu 0000:c5:00.0: amdgpu:      WALKER_ERROR: 0x1
[   11.287355] amdgpu 0000:c5:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[   11.287357] amdgpu 0000:c5:00.0: amdgpu:      MAPPING_ERROR: 0x1
[   11.287358] amdgpu 0000:c5:00.0: amdgpu:      RW: 0x0
[   11.772019] NFS: Registering the id_resolver key type
[   13.493502] traps: python[2327] general protection fault ip:7f63db8b09df sp:7f613e9fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f63db623000+481000]
[   28.693387] traps: python[2661] general protection fault ip:7fa6be2b09df sp:7fa4210fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fa6be023000+481000]
[   43.938164] traps: python[2803] general protection fault ip:7fdddb0b09df sp:7fdb3e1fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fdddae23000+481000]
[   59.199907] traps: python[2945] general protection fault ip:7fc142eb09df sp:7fbea5efa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fc142c23000+481000]
[   74.444098] traps: python[3097] general protection fault ip:7f00fdcb09df sp:7efe60cfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f00fda23000+481000]
[   89.722153] traps: python[3267] general protection fault ip:7f82e52b09df sp:7f80482fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f82e5023000+481000]
[  104.950990] traps: python[3411] general protection fault ip:7fec30cb09df sp:7fe9939fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fec30a23000+481000]
[  120.216485] traps: python[3559] general protection fault ip:7f72676b09df sp:7f6fca5fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f7267423000+481000]
[  135.446414] traps: python[3703] general protection fault ip:7f535dcb09df sp:7f50c0bfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f535da23000+481000]
[  150.693087] traps: python[3848] general protection fault ip:7f13924b09df sp:7f10f55fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f1392223000+481000]
[  165.956371] traps: python[3992] general protection fault ip:7f44ee4b09df sp:7f42513fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f44ee223000+481000]
[  181.216082] traps: python[4144] general protection fault ip:7fbdf08b09df sp:7fbb536fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fbdf0623000+481000]
[  196.454978] traps: python[4287] general protection fault ip:7f5778eb09df sp:7f54dbffa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f5778c23000+481000]
[  211.732271] traps: python[4424] general protection fault ip:7fcaa66b09df sp:7fc8095fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fcaa6423000+481000]
[  226.903041] traps: python[4570] general protection fault ip:7f40e8cb09df sp:7f3e4bcfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f40e8a23000+481000]
[  242.221886] traps: python[4712] general protection fault ip:7feafe2b09df sp:7fe8613fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7feafe023000+481000]
[  257.431337] traps: python[4858] general protection fault ip:7f55b50b09df sp:7f5317ffa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f55b4e23000+481000]
[  272.739417] traps: python[5010] general protection fault ip:7f3a6f6b09df sp:7f37d21fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f3a6f423000+481000]
[  287.948286] traps: python[5154] general protection fault ip:7f6e44eb09df sp:7f6ba7dfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f6e44c23000+481000]
[  303.215941] traps: python[5298] general protection fault ip:7fedd5cb09df sp:7feb389fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fedd5a23000+481000]
[  318.417424] traps: python[5699] general protection fault ip:7f3f5cab09df sp:7f3cbf9fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f3f5c823000+481000]
[  333.662547] traps: python[5844] general protection fault ip:7fb6e32b09df sp:7fb4461fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fb6e3023000+481000]
[  348.971308] traps: python[6072] general protection fault ip:7f1e2deb09df sp:7f1b90bfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f1e2dc23000+481000]
[  364.145845] traps: python[6217] general protection fault ip:7fb8e5ab09df sp:7fb6489fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fb8e5823000+481000]
[  379.204057] traps: python[6360] general protection fault ip:7fe97beb09df sp:7fe6dedfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fe97bc23000+481000]
[  394.421930] traps: python[6504] general protection fault ip:7fdd7d6b09df sp:7fdae05fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fdd7d423000+481000]
[  409.721996] traps: python[6648] general protection fault ip:7fbe9dcb09df sp:7fbc00bfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fbe9da23000+481000]
[  424.971988] traps: python[6805] general protection fault ip:7fcab7ab09df sp:7fc81aafa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fcab7823000+481000]
[  440.203222] traps: python[6948] general protection fault ip:7f2bc6cb09df sp:7f2929bfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f2bc6a23000+481000]
[  444.287684] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:32770)
[  444.287705] amdgpu 0000:c5:00.0: amdgpu:  Process rvs pid 6958 thread rvs pid 6958
[  444.287710] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f5c29dd8000 from client 10
[  444.287715] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00800B32
[  444.287719] amdgpu 0000:c5:00.0: amdgpu:      Faulty UTCL2 client ID: CPC (0x5)
[  444.287723] amdgpu 0000:c5:00.0: amdgpu:      MORE_FAULTS: 0x0
[  444.287725] amdgpu 0000:c5:00.0: amdgpu:      WALKER_ERROR: 0x1
[  444.287728] amdgpu 0000:c5:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[  444.287730] amdgpu 0000:c5:00.0: amdgpu:      MAPPING_ERROR: 0x1
[  444.287732] amdgpu 0000:c5:00.0: amdgpu:      RW: 0x0
[  455.488154] traps: python[7099] general protection fault ip:7f3beaab09df sp:7f394dbfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f3bea823000+481000]
[  470.715484] traps: python[7244] general protection fault ip:7faf102b09df sp:7fac732fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7faf10023000+481000]
[  485.927084] traps: python[7387] general protection fault ip:7f5fafcb09df sp:7f5d12dfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f5fafa23000+481000]
[  501.204396] traps: python[7529] general protection fault ip:7fb5600b09df sp:7fb2c30fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fb55fe23000+481000]
[  516.438004] traps: python[7669] general protection fault ip:7fbdcfab09df sp:7fbb32afa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fbdcf823000+481000]
[  519.732402] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:32770)
[  519.732427] amdgpu 0000:c5:00.0: amdgpu:  Process rvs pid 7679 thread rvs pid 7679
[  519.732434] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f8a30ff0000 from client 10
[  519.732440] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00800B32
[  519.732444] amdgpu 0000:c5:00.0: amdgpu:      Faulty UTCL2 client ID: CPC (0x5)
[  519.732448] amdgpu 0000:c5:00.0: amdgpu:      MORE_FAULTS: 0x0
[  519.732451] amdgpu 0000:c5:00.0: amdgpu:      WALKER_ERROR: 0x1
[  519.732454] amdgpu 0000:c5:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[  519.732456] amdgpu 0000:c5:00.0: amdgpu:      MAPPING_ERROR: 0x1
[  519.732459] amdgpu 0000:c5:00.0: amdgpu:      RW: 0x0
[  531.666641] traps: python[7820] general protection fault ip:7fc0288b09df sp:7fbd8b5fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fc028623000+481000]
[  546.888059] traps: python[7966] general protection fault ip:7f0eeeeb09df sp:7f0c51efa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f0eeec23000+481000]
[  561.977183] traps: python[8109] general protection fault ip:7f94c38b09df sp:7f92269fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f94c3623000+481000]
[  577.261114] traps: python[8258] general protection fault ip:7fda2d8b09df sp:7fd7907fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fda2d623000+481000]
[  592.461811] traps: python[8401] general protection fault ip:7faddb0b09df sp:7fab3defa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7faddae23000+481000]
[  604.815017] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:32770)
[  604.815043] amdgpu 0000:c5:00.0: amdgpu:  Process rvs pid 8500 thread rvs pid 8500
[  604.815049] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007fd5211f1000 from client 10
[  604.815056] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00800B32
[  604.815060] amdgpu 0000:c5:00.0: amdgpu:      Faulty UTCL2 client ID: CPC (0x5)
[  604.815064] amdgpu 0000:c5:00.0: amdgpu:      MORE_FAULTS: 0x0
[  604.815067] amdgpu 0000:c5:00.0: amdgpu:      WALKER_ERROR: 0x1
[  604.815070] amdgpu 0000:c5:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[  604.815072] amdgpu 0000:c5:00.0: amdgpu:      MAPPING_ERROR: 0x1
[  604.815075] amdgpu 0000:c5:00.0: amdgpu:      RW: 0x0
[  607.734015] traps: python[8554] general protection fault ip:7fb9856b09df sp:7fb6e85fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fb985423000+481000]
[  622.907110] traps: python[8704] general protection fault ip:7f93f2ab09df sp:7f9155afa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f93f2823000+481000]
[  637.925262] traps: python[8846] general protection fault ip:7f5400ab09df sp:7f51639fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f5400823000+481000]
[  653.211269] traps: python[8991] general protection fault ip:7f8fa3cb09df sp:7f8d06dfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f8fa3a23000+481000]
[  668.436999] traps: python[9130] general protection fault ip:7f133a4b09df sp:7f109d5fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f133a223000+481000]
[  683.425132] traps: python[9278] general protection fault ip:7fd859eb09df sp:7fd5bcdfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fd859c23000+481000]
[  698.726747] traps: python[9420] general protection fault ip:7fc1506b09df sp:7fbeb34fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fc150423000+481000]
[  713.931002] traps: python[9565] general protection fault ip:7fb7c26b09df sp:7fb5257fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fb7c2423000+481000]
[  729.328374] traps: python[9778] general protection fault ip:7fe48d0b09df sp:7fe1f00fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fe48ce23000+481000]
[  744.501655] traps: python[9921] general protection fault ip:7f5cdceb09df sp:7f5a3fefa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f5cdcc23000+481000]
[  759.707549] traps: python[10065] general protection fault ip:7fbaa7eb09df sp:7fb80adfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fbaa7c23000+481000]
[  774.973803] traps: python[10227] general protection fault ip:7fd746cb09df sp:7fd4a9dfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fd746a23000+481000]
[  790.211772] traps: python[10372] general protection fault ip:7f7e8a6b09df sp:7f7bed6fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f7e8a423000+481000]
[  794.299500] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:32770)
[  794.299524] amdgpu 0000:c5:00.0: amdgpu:  Process vectoradd_hip.e pid 10436 thread vectoradd_hip.e pid 10436
[  794.299530] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f7dd7eb4000 from client 10
[  794.299535] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00800932
[  794.299539] amdgpu 0000:c5:00.0: amdgpu:      Faulty UTCL2 client ID: CPF (0x4)
[  794.299542] amdgpu 0000:c5:00.0: amdgpu:      MORE_FAULTS: 0x0
[  794.299545] amdgpu 0000:c5:00.0: amdgpu:      WALKER_ERROR: 0x1
[  794.299547] amdgpu 0000:c5:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[  794.299549] amdgpu 0000:c5:00.0: amdgpu:      MAPPING_ERROR: 0x1
[  794.299552] amdgpu 0000:c5:00.0: amdgpu:      RW: 0x0
[  805.408776] traps: python[10575] general protection fault ip:7f5e84eb09df sp:7f5be7cfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f5e84c23000+481000]
[  820.453493] traps: python[10715] general protection fault ip:7f9c39ab09df sp:7f999c9fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f9c39823000+481000]
[  835.708765] traps: python[10867] general protection fault ip:7f0c2e2b09df sp:7f09911fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f0c2e023000+481000]
[  851.000253] traps: python[11012] general protection fault ip:7f2ac0eb09df sp:7f2823ffa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f2ac0c23000+481000]
[  866.230079] traps: python[11158] general protection fault ip:7f8699eb09df sp:7f83fcefa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f8699c23000+481000]
[  878.808351] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:32770)
[  878.808376] amdgpu 0000:c5:00.0: amdgpu:  Process vectoradd_hip.e pid 11295 thread vectoradd_hip.e pid 11295
[  878.808384] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f24ee711000 from client 10
[  878.808390] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00800932
[  878.808395] amdgpu 0000:c5:00.0: amdgpu:      Faulty UTCL2 client ID: CPF (0x4)
[  878.808399] amdgpu 0000:c5:00.0: amdgpu:      MORE_FAULTS: 0x0
[  878.808402] amdgpu 0000:c5:00.0: amdgpu:      WALKER_ERROR: 0x1
[  878.808405] amdgpu 0000:c5:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[  878.808408] amdgpu 0000:c5:00.0: amdgpu:      MAPPING_ERROR: 0x1
[  878.808410] amdgpu 0000:c5:00.0: amdgpu:      RW: 0x0
[  881.449186] traps: python[11309] general protection fault ip:7efe370b09df sp:7efb99ffa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7efe36e23000+481000]
[  896.813784] traps: python[11453] general protection fault ip:7fa23b6b09df sp:7f9f9e1fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fa23b423000+481000]
[  912.059073] traps: python[11615] general protection fault ip:7efe47ab09df sp:7efbaaafa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7efe47823000+481000]
[  927.305578] traps: python[11760] general protection fault ip:7f4df32b09df sp:7f4b561fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f4df3023000+481000]
[  942.617103] traps: python[11903] general protection fault ip:7f5c3c2b09df sp:7f599f0fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f5c3c023000+481000]
[  957.849415] traps: python[12047] general protection fault ip:7f9e8c4b09df sp:7f9bef3fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f9e8c223000+481000]
[  973.111781] traps: python[12184] general protection fault ip:7f2079cb09df sp:7f1ddccfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f2079a23000+481000]
[  988.319623] traps: python[12326] general protection fault ip:7f70d6cb09df sp:7f6e39bfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f70d6a23000+481000]
[ 1003.679048] traps: python[12474] general protection fault ip:7f6d5d2b09df sp:7f6ac00fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f6d5d023000+481000]
[ 1019.141086] traps: python[12616] general protection fault ip:7f52d0eb09df sp:7f5033efa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f52d0c23000+481000]
[ 1034.393702] traps: python[12767] general protection fault ip:7fc0190b09df sp:7fbd7c0fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fc018e23000+481000]
[ 1048.901249] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:32771)
[ 1048.901274] amdgpu 0000:c5:00.0: amdgpu:  Process vectoradd_hip.e pid 12935 thread vectoradd_hip.e pid 12935
[ 1048.901281] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f648ea76000 from client 10
[ 1048.901287] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00800932
[ 1048.901292] amdgpu 0000:c5:00.0: amdgpu:      Faulty UTCL2 client ID: CPF (0x4)
[ 1048.901296] amdgpu 0000:c5:00.0: amdgpu:      MORE_FAULTS: 0x0
[ 1048.901299] amdgpu 0000:c5:00.0: amdgpu:      WALKER_ERROR: 0x1
[ 1048.901302] amdgpu 0000:c5:00.0: amdgpu:      PERMISSION_FAULTS: 0x3
[ 1048.901305] amdgpu 0000:c5:00.0: amdgpu:      MAPPING_ERROR: 0x1
[ 1048.901307] amdgpu 0000:c5:00.0: amdgpu:      RW: 0x0
[ 1049.577357] traps: python[12934] general protection fault ip:7f9785cb09df sp:7f94e8bfa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f9785a23000+481000]
[ 1064.856302] traps: python[13085] general protection fault ip:7fb4edcb09df sp:7fb250efa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fb4eda23000+481000]
[ 1080.100060] traps: python[13230] general protection fault ip:7fc20a0b09df sp:7fbf6d1fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fc209e23000+481000]
[ 1095.347874] traps: python[13374] general protection fault ip:7f6d236b09df sp:7f6a866fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f6d23423000+481000]
[ 1110.605164] traps: python[13517] general protection fault ip:7fa061ab09df sp:7f9dc4afa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fa061823000+481000]
[ 1125.858144] traps: python[13660] general protection fault ip:7fe7fc2b09df sp:7fe55f1fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7fe7fc023000+481000]
[ 1141.135883] traps: python[13798] general protection fault ip:7f6c476b09df sp:7f69aa5fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f6c47423000+481000]
[ 1156.323801] traps: python[13943] general protection fault ip:7f4cc3ab09df sp:7f4a269fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f4cc3823000+481000]
[ 1171.509622] traps: python[14091] general protection fault ip:7f7730ab09df sp:7f74939fa850 error:0 in libamdhip64.so.7.2.70201[2b09df,7f7730823000+481000]

### Operating System

Debian 13.4 Trixie

### CPU

GMKtec EVO-X2 Ryzen Max 295+ 128 GB RAM, there is a problem with the BIOS. The 128 GB RAM are not recognized properly. The BIOS sees only 64 GB CPU RAM maximum. If one allocates less than 64 GB of RAM for the UMA buffer, then the CPU RAM caps at 64 GB RAM. That is why i have put the default UMA buffer size to the maximum of 96 GB VRAM allocation. A BIOS update would be proper here.

### GPU

Radeon 8060S, gfx1151

### ROCm Version

ROCm-7.2.1

### ROCm Component

HIP

### Steps to Reproduce

install AMD ROCm-7.2.1 for the 6.12 Debian 13 stock kernel. The backports 6.19 kernel yields compilation errors and breaks apt, thus it had to be discarded and only stock Debian 13.4 to be used. Trying to use the backports Debian 13 amdgpu for the backports 6.19 kernel supported the NPU, but had to be discarded on account of incompatiblity with amdgpu from the official AMD Ubuntu packages.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

rocminfo for the amdgpu-dkms for the 6.12 kernel disregards the NPU:

(automatic1111) ai-service@GMKtec-EVO-X2:~/hip-examples/vectorAdd$ rocminfo
ROCk module version 6.16.13 is loaded
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
  Max Clock Freq. (MHz):   5185                               
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
      Size:                    32497688(0x1efe018) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32497688(0x1efe018) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32497688(0x1efe018) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32497688(0x1efe018) KB             
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
    L3:                      32768(0x8000) KB                   
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 32                                 
  SDMA engine uCode::      17                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    100663296(0x6000000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    100663296(0x6000000) KB            
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
*** Done *** 

Inside the conda environment the gfx1103 is reported in a regular system-wide user account gfx1151 is reported. But the kernel errors are same for the vectoradd test.

### Additional Information

_No response_