# clinfo makes Ryzen 5 GPU reset and freeze X server

- **Issue #:** 1584
- **State:** closed
- **Created:** 2021-10-07T08:17:01Z
- **Updated:** 2021-11-04T00:42:16Z
- **URL:** https://github.com/ROCm/ROCm/issues/1584

## Environment
### ROCm information
* Version: 4.3.1 (latest)
* Installed packages: `rock-dkms`, `rocm-opencl`, `rocminfo`, `rocm-smi-lib`, `rocm-bandwidth-test`

### HW & Linux information
* PC: MSI Modern 14 B4MW
* CPU/GPU: Ryzen 4500U
* RAM: 16 GB
* OS: Ubuntu 20.04.3 LTS
* Linux Kernel (package name): 5.11.0-37-generic
* linux-firmware version: 1.187.17

## How to Reproduce Error
1. install `libncurses5` (Although #1067 says it was resolved...)
2. run `/opt/rocm-4.3.1/opencl/bin/clinfo`
3. GPU reset and failed to recover -> X server malfunctioning -> screen was blinking twice and was frozen
    - related log from `journalctl -b-1`
```
Oct 07 15:47:47 sanori-laptop kernel: amdgpu: qcm fence wait loop timeout expired
Oct 07 15:47:47 sanori-laptop kernel: amdgpu: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
Oct 07 15:47:47 sanori-laptop kernel: amdgpu: Failed to evict process queues
Oct 07 15:47:47 sanori-laptop kernel: amdgpu: Failed to quiesce KFD
Oct 07 15:47:47 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset begin!
Oct 07 15:47:47 sanori-laptop kernel: [drm] free PSP TMR buffer
Oct 07 15:47:47 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: MODE2 reset
Oct 07 15:47:47 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset succeeded, trying to resume
Oct 07 15:47:47 sanori-laptop kernel: [drm] PCIE GART of 1024M enabled.
Oct 07 15:47:47 sanori-laptop kernel: [drm] PTB located at 0x000000F400900000
Oct 07 15:47:47 sanori-laptop kernel: [drm] PSP is resuming...
Oct 07 15:47:47 sanori-laptop kernel: [drm] reserve 0x400000 from 0xf41f800000 for PSP TMR
Oct 07 15:47:47 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: RAS: optional ras ta ucode is not available
Oct 07 15:47:47 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: RAP: optional rap ta ucode is not available
Oct 07 15:47:47 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
Oct 07 15:47:47 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: SMU is resuming...
Oct 07 15:47:47 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: SMU is resumed successfully!
Oct 07 15:47:47 sanori-laptop kernel: [drm] kiq ring mec 2 pipe 1 q 0
Oct 07 15:47:47 sanori-laptop kernel: [drm] DMUB hardware initialized: version=0x01010016
Oct 07 15:47:48 sanori-laptop kernel: [drm] VCN decode and encode initialized successfully(under DPG Mode).
Oct 07 15:47:48 sanori-laptop kernel: [drm] JPEG decode initialized successfully.
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring gfx uses VM inv eng 0 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring sdma0 uses VM inv eng 0 on hub 1
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring vcn_dec uses VM inv eng 1 on hub 1
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring vcn_enc0 uses VM inv eng 4 on hub 1
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring vcn_enc1 uses VM inv eng 5 on hub 1
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring jpeg_dec uses VM inv eng 6 on hub 1
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: recover vram bo from shadow start
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: recover vram bo from shadow done
Oct 07 15:47:48 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset(1) succeeded!
Oct 07 15:47:57 sanori-laptop kernel: amdgpu: qcm fence wait loop timeout expired
Oct 07 15:47:57 sanori-laptop kernel: amdgpu: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
Oct 07 15:47:57 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset begin!
Oct 07 15:47:57 sanori-laptop kernel: [drm] free PSP TMR buffer
Oct 07 15:47:57 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: MODE2 reset
Oct 07 15:47:57 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset succeeded, trying to resume
Oct 07 15:47:57 sanori-laptop kernel: [drm] PCIE GART of 1024M enabled.
Oct 07 15:47:57 sanori-laptop kernel: [drm] PTB located at 0x000000F400900000
Oct 07 15:47:57 sanori-laptop kernel: [drm] PSP is resuming...
Oct 07 15:47:57 sanori-laptop kernel: [drm] reserve 0x400000 from 0xf41f800000 for PSP TMR
Oct 07 15:47:57 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: RAS: optional ras ta ucode is not available
Oct 07 15:47:57 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: RAP: optional rap ta ucode is not available
Oct 07 15:47:57 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
Oct 07 15:47:57 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: SMU is resuming...
Oct 07 15:47:57 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: SMU is resumed successfully!
Oct 07 15:47:57 sanori-laptop kernel: [drm] kiq ring mec 2 pipe 1 q 0
Oct 07 15:47:57 sanori-laptop kernel: [drm] DMUB hardware initialized: version=0x01010016
Oct 07 15:47:58 sanori-laptop kernel: [drm] VCN decode and encode initialized successfully(under DPG Mode).
Oct 07 15:47:58 sanori-laptop kernel: [drm] JPEG decode initialized successfully.
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring gfx uses VM inv eng 0 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring sdma0 uses VM inv eng 0 on hub 1
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring vcn_dec uses VM inv eng 1 on hub 1
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring vcn_enc0 uses VM inv eng 4 on hub 1
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring vcn_enc1 uses VM inv eng 5 on hub 1
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: ring jpeg_dec uses VM inv eng 6 on hub 1
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: recover vram bo from shadow start
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: recover vram bo from shadow done
Oct 07 15:47:58 sanori-laptop kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset(2) succeeded!
```
  - Output of clinfo (partial?)
```
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3305.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Renoir
  Device Topology:                               PCI[ B#3, D#0, F#0 ]
  Max compute units:                             26
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           1500Mhz
  Address bits:                                  64
  Max memory allocation:                         456340272
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            16384
  Max image 3D height:                           16384
  Max image 3D depth:                            8192
  Max samplers within kernel:                    5686
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            536870912
  Constant buffer size:                          456340272
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          456340272
  Max global variable size:                      456340272
  Max global variable preferred total size:      536870912
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7f61d7906e10
  Name:                                          gfx902:xnack+
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                3305.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program
```
  - Output of `modinfo amdgpu`
```
filename:       /lib/modules/5.11.0-37-generic/updates/dkms/amdgpu.ko
version:        5.11.14
license:        GPL and additional rights
description:    AMD GPU
author:         AMD linux driver team
firmware:       amdgpu/vangogh_gpu_info.bin
firmware:       amdgpu/navi12_gpu_info.bin
firmware:       amdgpu/navi14_gpu_info.bin
firmware:       amdgpu/navi10_gpu_info.bin
firmware:       amdgpu/renoir_gpu_info.bin
firmware:       amdgpu/arcturus_gpu_info.bin
firmware:       amdgpu/raven2_gpu_info.bin
firmware:       amdgpu/picasso_gpu_info.bin
firmware:       amdgpu/raven_gpu_info.bin
firmware:       amdgpu/vega12_gpu_info.bin
firmware:       amdgpu/vega10_gpu_info.bin
firmware:       amdgpu/mullins_mec.bin
firmware:       amdgpu/mullins_rlc.bin
firmware:       amdgpu/mullins_ce.bin
firmware:       amdgpu/mullins_me.bin
firmware:       amdgpu/mullins_pfp.bin
firmware:       amdgpu/kabini_mec.bin
firmware:       amdgpu/kabini_rlc.bin
firmware:       amdgpu/kabini_ce.bin
firmware:       amdgpu/kabini_me.bin
firmware:       amdgpu/kabini_pfp.bin
firmware:       amdgpu/kaveri_mec2.bin
firmware:       amdgpu/kaveri_mec.bin
firmware:       amdgpu/kaveri_rlc.bin
firmware:       amdgpu/kaveri_ce.bin
firmware:       amdgpu/kaveri_me.bin
firmware:       amdgpu/kaveri_pfp.bin
firmware:       amdgpu/hawaii_mec.bin
firmware:       amdgpu/hawaii_rlc.bin
firmware:       amdgpu/hawaii_ce.bin
firmware:       amdgpu/hawaii_me.bin
firmware:       amdgpu/hawaii_pfp.bin
firmware:       amdgpu/bonaire_mec.bin
firmware:       amdgpu/bonaire_rlc.bin
firmware:       amdgpu/bonaire_ce.bin
firmware:       amdgpu/bonaire_me.bin
firmware:       amdgpu/bonaire_pfp.bin
firmware:       amdgpu/mullins_sdma1.bin
firmware:       amdgpu/mullins_sdma.bin
firmware:       amdgpu/kabini_sdma1.bin
firmware:       amdgpu/kabini_sdma.bin
firmware:       amdgpu/kaveri_sdma1.bin
firmware:       amdgpu/kaveri_sdma.bin
firmware:       amdgpu/hawaii_sdma1.bin
firmware:       amdgpu/hawaii_sdma.bin
firmware:       amdgpu/bonaire_sdma1.bin
firmware:       amdgpu/bonaire_sdma.bin
firmware:       amdgpu/si58_mc.bin
firmware:       amdgpu/hainan_mc.bin
firmware:       amdgpu/oland_mc.bin
firmware:       amdgpu/verde_mc.bin
firmware:       amdgpu/pitcairn_mc.bin
firmware:       amdgpu/tahiti_mc.bin
firmware:       amdgpu/hainan_rlc.bin
firmware:       amdgpu/hainan_ce.bin
firmware:       amdgpu/hainan_me.bin
firmware:       amdgpu/hainan_pfp.bin
firmware:       amdgpu/oland_rlc.bin
firmware:       amdgpu/oland_ce.bin
firmware:       amdgpu/oland_me.bin
firmware:       amdgpu/oland_pfp.bin
firmware:       amdgpu/verde_rlc.bin
firmware:       amdgpu/verde_ce.bin
firmware:       amdgpu/verde_me.bin
firmware:       amdgpu/verde_pfp.bin
firmware:       amdgpu/pitcairn_rlc.bin
firmware:       amdgpu/pitcairn_ce.bin
firmware:       amdgpu/pitcairn_me.bin
firmware:       amdgpu/pitcairn_pfp.bin
firmware:       amdgpu/tahiti_rlc.bin
firmware:       amdgpu/tahiti_ce.bin
firmware:       amdgpu/tahiti_me.bin
firmware:       amdgpu/tahiti_pfp.bin
firmware:       amdgpu/topaz_mc.bin
firmware:       amdgpu/hawaii_mc.bin
firmware:       amdgpu/bonaire_mc.bin
firmware:       amdgpu/polaris12_k_mc.bin
firmware:       amdgpu/polaris10_k_mc.bin
firmware:       amdgpu/polaris11_k_mc.bin
firmware:       amdgpu/polaris12_32_mc.bin
firmware:       amdgpu/polaris12_mc.bin
firmware:       amdgpu/polaris10_mc.bin
firmware:       amdgpu/polaris11_mc.bin
firmware:       amdgpu/tonga_mc.bin
firmware:       amdgpu/vega12_asd.bin
firmware:       amdgpu/vega12_sos.bin
firmware:       amdgpu/vega10_asd.bin
firmware:       amdgpu/vega10_sos.bin
firmware:       amdgpu/raven_ta.bin
firmware:       amdgpu/raven2_ta.bin
firmware:       amdgpu/picasso_ta.bin
firmware:       amdgpu/raven2_asd.bin
firmware:       amdgpu/picasso_asd.bin
firmware:       amdgpu/raven_asd.bin
firmware:       amdgpu/dimgrey_cavefish_ta.bin
firmware:       amdgpu/dimgrey_cavefish_sos.bin
firmware:       amdgpu/vangogh_toc.bin
firmware:       amdgpu/vangogh_asd.bin
firmware:       amdgpu/navy_flounder_ta.bin
firmware:       amdgpu/navy_flounder_sos.bin
firmware:       amdgpu/sienna_cichlid_ta.bin
firmware:       amdgpu/sienna_cichlid_sos.bin
firmware:       amdgpu/arcturus_ta.bin
firmware:       amdgpu/arcturus_asd.bin
firmware:       amdgpu/arcturus_sos.bin
firmware:       amdgpu/navi12_ta.bin
firmware:       amdgpu/navi12_asd.bin
firmware:       amdgpu/navi12_sos.bin
firmware:       amdgpu/navi14_ta.bin
firmware:       amdgpu/navi14_asd.bin
firmware:       amdgpu/navi14_sos.bin
firmware:       amdgpu/navi10_ta.bin
firmware:       amdgpu/navi10_asd.bin
firmware:       amdgpu/navi10_sos.bin
firmware:       amdgpu/vega20_ta.bin
firmware:       amdgpu/vega20_asd.bin
firmware:       amdgpu/vega20_sos.bin
firmware:       amdgpu/green_sardine_ta.bin
firmware:       amdgpu/green_sardine_asd.bin
firmware:       amdgpu/renoir_ta.bin
firmware:       amdgpu/renoir_asd.bin
firmware:       amdgpu/aldebaran_ta.bin
firmware:       amdgpu/aldebaran_sos.bin
firmware:       amdgpu/vegam_rlc.bin
firmware:       amdgpu/vegam_mec2.bin
firmware:       amdgpu/vegam_mec.bin
firmware:       amdgpu/vegam_me.bin
firmware:       amdgpu/vegam_pfp.bin
firmware:       amdgpu/vegam_ce.bin
firmware:       amdgpu/polaris12_rlc.bin
firmware:       amdgpu/polaris12_mec2_2.bin
firmware:       amdgpu/polaris12_mec2.bin
firmware:       amdgpu/polaris12_mec_2.bin
firmware:       amdgpu/polaris12_mec.bin
firmware:       amdgpu/polaris12_me_2.bin
firmware:       amdgpu/polaris12_me.bin
firmware:       amdgpu/polaris12_pfp_2.bin
firmware:       amdgpu/polaris12_pfp.bin
firmware:       amdgpu/polaris12_ce_2.bin
firmware:       amdgpu/polaris12_ce.bin
firmware:       amdgpu/polaris11_rlc.bin
firmware:       amdgpu/polaris11_mec2_2.bin
firmware:       amdgpu/polaris11_mec2.bin
firmware:       amdgpu/polaris11_mec_2.bin
firmware:       amdgpu/polaris11_mec.bin
firmware:       amdgpu/polaris11_me_2.bin
firmware:       amdgpu/polaris11_me.bin
firmware:       amdgpu/polaris11_pfp_2.bin
firmware:       amdgpu/polaris11_pfp.bin
firmware:       amdgpu/polaris11_ce_2.bin
firmware:       amdgpu/polaris11_ce.bin
firmware:       amdgpu/polaris10_rlc.bin
firmware:       amdgpu/polaris10_mec2_2.bin
firmware:       amdgpu/polaris10_mec2.bin
firmware:       amdgpu/polaris10_mec_2.bin
firmware:       amdgpu/polaris10_mec.bin
firmware:       amdgpu/polaris10_me_2.bin
firmware:       amdgpu/polaris10_me.bin
firmware:       amdgpu/polaris10_pfp_2.bin
firmware:       amdgpu/polaris10_pfp.bin
firmware:       amdgpu/polaris10_ce_2.bin
firmware:       amdgpu/polaris10_ce.bin
firmware:       amdgpu/fiji_rlc.bin
firmware:       amdgpu/fiji_mec2.bin
firmware:       amdgpu/fiji_mec.bin
firmware:       amdgpu/fiji_me.bin
firmware:       amdgpu/fiji_pfp.bin
firmware:       amdgpu/fiji_ce.bin
firmware:       amdgpu/topaz_rlc.bin
firmware:       amdgpu/topaz_mec.bin
firmware:       amdgpu/topaz_me.bin
firmware:       amdgpu/topaz_pfp.bin
firmware:       amdgpu/topaz_ce.bin
firmware:       amdgpu/tonga_rlc.bin
firmware:       amdgpu/tonga_mec2.bin
firmware:       amdgpu/tonga_mec.bin
firmware:       amdgpu/tonga_me.bin
firmware:       amdgpu/tonga_pfp.bin
firmware:       amdgpu/tonga_ce.bin
firmware:       amdgpu/stoney_rlc.bin
firmware:       amdgpu/stoney_mec.bin
firmware:       amdgpu/stoney_me.bin
firmware:       amdgpu/stoney_pfp.bin
firmware:       amdgpu/stoney_ce.bin
firmware:       amdgpu/carrizo_rlc.bin
firmware:       amdgpu/carrizo_mec2.bin
firmware:       amdgpu/carrizo_mec.bin
firmware:       amdgpu/carrizo_me.bin
firmware:       amdgpu/carrizo_pfp.bin
firmware:       amdgpu/carrizo_ce.bin
firmware:       amdgpu/aldebaran_rlc.bin
firmware:       amdgpu/aldebaran_mec2.bin
firmware:       amdgpu/aldebaran_mec.bin
firmware:       amdgpu/green_sardine_rlc.bin
firmware:       amdgpu/green_sardine_mec2.bin
firmware:       amdgpu/green_sardine_mec.bin
firmware:       amdgpu/green_sardine_me.bin
firmware:       amdgpu/green_sardine_pfp.bin
firmware:       amdgpu/green_sardine_ce.bin
firmware:       amdgpu/renoir_rlc.bin
firmware:       amdgpu/renoir_mec.bin
firmware:       amdgpu/renoir_me.bin
firmware:       amdgpu/renoir_pfp.bin
firmware:       amdgpu/renoir_ce.bin
firmware:       amdgpu/arcturus_rlc.bin
firmware:       amdgpu/arcturus_mec.bin
firmware:       amdgpu/raven_kicker_rlc.bin
firmware:       amdgpu/raven2_rlc.bin
firmware:       amdgpu/raven2_mec2.bin
firmware:       amdgpu/raven2_mec.bin
firmware:       amdgpu/raven2_me.bin
firmware:       amdgpu/raven2_pfp.bin
firmware:       amdgpu/raven2_ce.bin
firmware:       amdgpu/picasso_rlc_am4.bin
firmware:       amdgpu/picasso_rlc.bin
firmware:       amdgpu/picasso_mec2.bin
firmware:       amdgpu/picasso_mec.bin
firmware:       amdgpu/picasso_me.bin
firmware:       amdgpu/picasso_pfp.bin
firmware:       amdgpu/picasso_ce.bin
firmware:       amdgpu/raven_rlc.bin
firmware:       amdgpu/raven_mec2.bin
firmware:       amdgpu/raven_mec.bin
firmware:       amdgpu/raven_me.bin
firmware:       amdgpu/raven_pfp.bin
firmware:       amdgpu/raven_ce.bin
firmware:       amdgpu/vega20_rlc.bin
firmware:       amdgpu/vega20_mec2.bin
firmware:       amdgpu/vega20_mec.bin
firmware:       amdgpu/vega20_me.bin
firmware:       amdgpu/vega20_pfp.bin
firmware:       amdgpu/vega20_ce.bin
firmware:       amdgpu/vega12_rlc.bin
firmware:       amdgpu/vega12_mec2.bin
firmware:       amdgpu/vega12_mec.bin
firmware:       amdgpu/vega12_me.bin
firmware:       amdgpu/vega12_pfp.bin
firmware:       amdgpu/vega12_ce.bin
firmware:       amdgpu/vega10_rlc.bin
firmware:       amdgpu/vega10_mec2.bin
firmware:       amdgpu/vega10_mec.bin
firmware:       amdgpu/vega10_me.bin
firmware:       amdgpu/vega10_pfp.bin
firmware:       amdgpu/vega10_ce.bin
firmware:       amdgpu/dimgrey_cavefish_rlc.bin
firmware:       amdgpu/dimgrey_cavefish_mec2.bin
firmware:       amdgpu/dimgrey_cavefish_mec.bin
firmware:       amdgpu/dimgrey_cavefish_me.bin
firmware:       amdgpu/dimgrey_cavefish_pfp.bin
firmware:       amdgpu/dimgrey_cavefish_ce.bin
firmware:       amdgpu/vangogh_rlc.bin
firmware:       amdgpu/vangogh_mec2.bin
firmware:       amdgpu/vangogh_mec.bin
firmware:       amdgpu/vangogh_me.bin
firmware:       amdgpu/vangogh_pfp.bin
firmware:       amdgpu/vangogh_ce.bin
firmware:       amdgpu/navy_flounder_rlc.bin
firmware:       amdgpu/navy_flounder_mec2.bin
firmware:       amdgpu/navy_flounder_mec.bin
firmware:       amdgpu/navy_flounder_me.bin
firmware:       amdgpu/navy_flounder_pfp.bin
firmware:       amdgpu/navy_flounder_ce.bin
firmware:       amdgpu/sienna_cichlid_rlc.bin
firmware:       amdgpu/sienna_cichlid_mec2.bin
firmware:       amdgpu/sienna_cichlid_mec.bin
firmware:       amdgpu/sienna_cichlid_me.bin
firmware:       amdgpu/sienna_cichlid_pfp.bin
firmware:       amdgpu/sienna_cichlid_ce.bin
firmware:       amdgpu/navi12_rlc.bin
firmware:       amdgpu/navi12_mec2.bin
firmware:       amdgpu/navi12_mec.bin
firmware:       amdgpu/navi12_me.bin
firmware:       amdgpu/navi12_pfp.bin
firmware:       amdgpu/navi12_ce.bin
firmware:       amdgpu/navi14_rlc.bin
firmware:       amdgpu/navi14_mec2.bin
firmware:       amdgpu/navi14_mec.bin
firmware:       amdgpu/navi14_me.bin
firmware:       amdgpu/navi14_pfp.bin
firmware:       amdgpu/navi14_ce.bin
firmware:       amdgpu/navi14_mec2_wks.bin
firmware:       amdgpu/navi14_mec_wks.bin
firmware:       amdgpu/navi14_me_wks.bin
firmware:       amdgpu/navi14_pfp_wks.bin
firmware:       amdgpu/navi14_ce_wks.bin
firmware:       amdgpu/navi10_rlc.bin
firmware:       amdgpu/navi10_mec2.bin
firmware:       amdgpu/navi10_mec.bin
firmware:       amdgpu/navi10_me.bin
firmware:       amdgpu/navi10_pfp.bin
firmware:       amdgpu/navi10_ce.bin
firmware:       amdgpu/topaz_sdma1.bin
firmware:       amdgpu/topaz_sdma.bin
firmware:       amdgpu/vegam_sdma1.bin
firmware:       amdgpu/vegam_sdma.bin
firmware:       amdgpu/polaris12_sdma1.bin
firmware:       amdgpu/polaris12_sdma.bin
firmware:       amdgpu/polaris11_sdma1.bin
firmware:       amdgpu/polaris11_sdma.bin
firmware:       amdgpu/polaris10_sdma1.bin
firmware:       amdgpu/polaris10_sdma.bin
firmware:       amdgpu/stoney_sdma.bin
firmware:       amdgpu/fiji_sdma1.bin
firmware:       amdgpu/fiji_sdma.bin
firmware:       amdgpu/carrizo_sdma1.bin
firmware:       amdgpu/carrizo_sdma.bin
firmware:       amdgpu/tonga_sdma1.bin
firmware:       amdgpu/tonga_sdma.bin
firmware:       amdgpu/aldebaran_sdma.bin
firmware:       amdgpu/green_sardine_sdma.bin
firmware:       amdgpu/renoir_sdma.bin
firmware:       amdgpu/arcturus_sdma.bin
firmware:       amdgpu/raven2_sdma.bin
firmware:       amdgpu/picasso_sdma.bin
firmware:       amdgpu/raven_sdma.bin
firmware:       amdgpu/vega20_sdma1.bin
firmware:       amdgpu/vega20_sdma.bin
firmware:       amdgpu/vega12_sdma1.bin
firmware:       amdgpu/vega12_sdma.bin
firmware:       amdgpu/vega10_sdma1.bin
firmware:       amdgpu/vega10_sdma.bin
firmware:       amdgpu/navi12_sdma1.bin
firmware:       amdgpu/navi12_sdma.bin
firmware:       amdgpu/navi14_sdma1.bin
firmware:       amdgpu/navi14_sdma.bin
firmware:       amdgpu/navi10_sdma1.bin
firmware:       amdgpu/navi10_sdma.bin
firmware:       amdgpu/vangogh_sdma.bin
firmware:       amdgpu/dimgrey_cavefish_sdma.bin
firmware:       amdgpu/navy_flounder_sdma.bin
firmware:       amdgpu/sienna_cichlid_sdma.bin
firmware:       amdgpu/sienna_cichlid_mes.bin
firmware:       amdgpu/navi10_mes.bin
firmware:       amdgpu/vega20_uvd.bin
firmware:       amdgpu/vega12_uvd.bin
firmware:       amdgpu/vega10_uvd.bin
firmware:       amdgpu/vegam_uvd.bin
firmware:       amdgpu/polaris12_uvd.bin
firmware:       amdgpu/polaris11_uvd.bin
firmware:       amdgpu/polaris10_uvd.bin
firmware:       amdgpu/stoney_uvd.bin
firmware:       amdgpu/fiji_uvd.bin
firmware:       amdgpu/carrizo_uvd.bin
firmware:       amdgpu/tonga_uvd.bin
firmware:       amdgpu/mullins_uvd.bin
firmware:       amdgpu/hawaii_uvd.bin
firmware:       amdgpu/kaveri_uvd.bin
firmware:       amdgpu/kabini_uvd.bin
firmware:       amdgpu/bonaire_uvd.bin
firmware:       amdgpu/oland_uvd.bin
firmware:       amdgpu/pitcairn_uvd.bin
firmware:       amdgpu/verde_uvd.bin
firmware:       amdgpu/tahiti_uvd.bin
firmware:       amdgpu/vega20_vce.bin
firmware:       amdgpu/vega12_vce.bin
firmware:       amdgpu/vega10_vce.bin
firmware:       amdgpu/vegam_vce.bin
firmware:       amdgpu/polaris12_vce.bin
firmware:       amdgpu/polaris11_vce.bin
firmware:       amdgpu/polaris10_vce.bin
firmware:       amdgpu/stoney_vce.bin
firmware:       amdgpu/fiji_vce.bin
firmware:       amdgpu/carrizo_vce.bin
firmware:       amdgpu/tonga_vce.bin
firmware:       amdgpu/mullins_vce.bin
firmware:       amdgpu/hawaii_vce.bin
firmware:       amdgpu/kaveri_vce.bin
firmware:       amdgpu/kabini_vce.bin
firmware:       amdgpu/bonaire_vce.bin
firmware:       amdgpu/dimgrey_cavefish_vcn.bin
firmware:       amdgpu/vangogh_vcn.bin
firmware:       amdgpu/navy_flounder_vcn.bin
firmware:       amdgpu/sienna_cichlid_vcn.bin
firmware:       amdgpu/navi12_vcn.bin
firmware:       amdgpu/navi14_vcn.bin
firmware:       amdgpu/navi10_vcn.bin
firmware:       amdgpu/aldebaran_vcn.bin
firmware:       amdgpu/green_sardine_vcn.bin
firmware:       amdgpu/renoir_vcn.bin
firmware:       amdgpu/arcturus_vcn.bin
firmware:       amdgpu/raven2_vcn.bin
firmware:       amdgpu/picasso_vcn.bin
firmware:       amdgpu/raven_vcn.bin
firmware:       amdgpu/dimgrey_cavefish_smc.bin
firmware:       amdgpu/navy_flounder_smc.bin
firmware:       amdgpu/sienna_cichlid_smc.bin
firmware:       amdgpu/navi12_smc.bin
firmware:       amdgpu/navi14_smc.bin
firmware:       amdgpu/navi10_smc.bin
firmware:       amdgpu/arcturus_smc.bin
firmware:       amdgpu/aldebaran_smc.bin
firmware:       amdgpu/vega20_smc.bin
firmware:       amdgpu/vega12_smc.bin
firmware:       amdgpu/vega10_acg_smc.bin
firmware:       amdgpu/vega10_smc.bin
firmware:       amdgpu/vegam_smc.bin
firmware:       amdgpu/polaris12_k_smc.bin
firmware:       amdgpu/polaris12_smc.bin
firmware:       amdgpu/polaris11_k2_smc.bin
firmware:       amdgpu/polaris11_k_smc.bin
firmware:       amdgpu/polaris11_smc_sk.bin
firmware:       amdgpu/polaris11_smc.bin
firmware:       amdgpu/polaris10_k2_smc.bin
firmware:       amdgpu/polaris10_k_smc.bin
firmware:       amdgpu/polaris10_smc_sk.bin
firmware:       amdgpu/polaris10_smc.bin
firmware:       amdgpu/fiji_smc.bin
firmware:       amdgpu/tonga_k_smc.bin
firmware:       amdgpu/tonga_smc.bin
firmware:       amdgpu/topaz_k_smc.bin
firmware:       amdgpu/topaz_smc.bin
firmware:       amdgpu/hawaii_k_smc.bin
firmware:       amdgpu/hawaii_smc.bin
firmware:       amdgpu/bonaire_k_smc.bin
firmware:       amdgpu/bonaire_smc.bin
firmware:       amdgpu/banks_k_2_smc.bin
firmware:       amdgpu/hainan_k_smc.bin
firmware:       amdgpu/hainan_smc.bin
firmware:       amdgpu/oland_k_smc.bin
firmware:       amdgpu/oland_smc.bin
firmware:       amdgpu/verde_k_smc.bin
firmware:       amdgpu/verde_smc.bin
firmware:       amdgpu/pitcairn_k_smc.bin
firmware:       amdgpu/pitcairn_smc.bin
firmware:       amdgpu/tahiti_smc.bin
firmware:       amdgpu/navi12_dmcu.bin
firmware:       amdgpu/raven_dmcu.bin
firmware:       amdgpu/dimgrey_cavefish_dmcub.bin
firmware:       amdgpu/vangogh_dmcub.bin
firmware:       amdgpu/green_sardine_dmcub.bin
firmware:       amdgpu/navy_flounder_dmcub.bin
firmware:       amdgpu/sienna_cichlid_dmcub.bin
firmware:       amdgpu/renoir_dmcub.bin
srcversion:     E958932D6313FD2C98B0D1C
alias:          pci:v00001002d00007410sv*sd*bc*sc*i*
alias:          pci:v00001002d0000740Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000740Csv*sd*bc*sc*i*
alias:          pci:v00001002d00007408sv*sd*bc*sc*i*
alias:          pci:v00001002d000073FFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073E2sv*sd*bc*sc*i*
alias:          pci:v00001002d000073E1sv*sd*bc*sc*i*
alias:          pci:v00001002d000073E0sv*sd*bc*sc*i*
alias:          pci:v00001002d000073DFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073C3sv*sd*bc*sc*i*
alias:          pci:v00001002d000073C1sv*sd*bc*sc*i*
alias:          pci:v00001002d000073C0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000163Fsv*sd*bc*sc*i*
alias:          pci:v00001002d000073BFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073AEsv*sd*bc*sc*i*
alias:          pci:v00001002d000073ABsv*sd*bc*sc*i*
alias:          pci:v00001002d000073A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A0sv*sd*bc*sc*i*
alias:          pci:v00001002d00007362sv*sd*bc*sc*i*
alias:          pci:v00001002d00007360sv*sd*bc*sc*i*
alias:          pci:v00001002d0000164Csv*sd*bc*sc*i*
alias:          pci:v00001002d00001638sv*sd*bc*sc*i*
alias:          pci:v00001002d00001636sv*sd*bc*sc*i*
alias:          pci:v00001002d0000734Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00007347sv*sd*bc*sc*i*
alias:          pci:v00001002d00007341sv*sd*bc*sc*i*
alias:          pci:v00001002d00007340sv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Asv*sd*bc*sc*i*
alias:          pci:v00001002d00007319sv*sd*bc*sc*i*
alias:          pci:v00001002d00007318sv*sd*bc*sc*i*
alias:          pci:v00001002d00007312sv*sd*bc*sc*i*
alias:          pci:v00001002d00007310sv*sd*bc*sc*i*
alias:          pci:v00001002d00007390sv*sd*bc*sc*i*
alias:          pci:v00001002d0000738Esv*sd*bc*sc*i*
alias:          pci:v00001002d00007388sv*sd*bc*sc*i*
alias:          pci:v00001002d0000738Csv*sd*bc*sc*i*
alias:          pci:v00001002d000015D8sv*sd*bc*sc*i*
alias:          pci:v00001002d000015DDsv*sd*bc*sc*i*
alias:          pci:v00001002d000066AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000066A7sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A4sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A0sv*sd*bc*sc*i*
alias:          pci:v00001002d000069AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000069A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000687Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006869sv*sd*bc*sc*i*
alias:          pci:v00001002d00006868sv*sd*bc*sc*i*
alias:          pci:v00001002d00006867sv*sd*bc*sc*i*
alias:          pci:v00001002d00006864sv*sd*bc*sc*i*
alias:          pci:v00001002d00006863sv*sd*bc*sc*i*
alias:          pci:v00001002d00006862sv*sd*bc*sc*i*
alias:          pci:v00001002d00006861sv*sd*bc*sc*i*
alias:          pci:v00001002d00006860sv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000699Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006997sv*sd*bc*sc*i*
alias:          pci:v00001002d00006995sv*sd*bc*sc*i*
alias:          pci:v00001002d00006987sv*sd*bc*sc*i*
alias:          pci:v00001002d00006986sv*sd*bc*sc*i*
alias:          pci:v00001002d00006985sv*sd*bc*sc*i*
alias:          pci:v00001002d00006981sv*sd*bc*sc*i*
alias:          pci:v00001002d00006980sv*sd*bc*sc*i*
alias:          pci:v00001002d00006FDFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CCsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067C9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067DFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067D0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C7sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C4sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C2sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E7sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067FFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067EFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067EBsv*sd*bc*sc*i*
alias:          pci:v00001002d000067E8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E3sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E0sv*sd*bc*sc*i*
alias:          pci:v00001002d000098E4sv*sd*bc*sc*i*
alias:          pci:v00001002d00009877sv*sd*bc*sc*i*
alias:          pci:v00001002d00009876sv*sd*bc*sc*i*
alias:          pci:v00001002d00009875sv*sd*bc*sc*i*
alias:          pci:v00001002d00009874sv*sd*bc*sc*i*
alias:          pci:v00001002d00009870sv*sd*bc*sc*i*
alias:          pci:v00001002d0000730Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00007300sv*sd*bc*sc*i*
alias:          pci:v00001002d00006939sv*sd*bc*sc*i*
alias:          pci:v00001002d00006938sv*sd*bc*sc*i*
alias:          pci:v00001002d00006930sv*sd*bc*sc*i*
alias:          pci:v00001002d0000692Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000692Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00006929sv*sd*bc*sc*i*
alias:          pci:v00001002d00006928sv*sd*bc*sc*i*
alias:          pci:v00001002d00006921sv*sd*bc*sc*i*
alias:          pci:v00001002d00006920sv*sd*bc*sc*i*
alias:          pci:v00001002d00006907sv*sd*bc*sc*i*
alias:          pci:v00001002d00006903sv*sd*bc*sc*i*
alias:          pci:v00001002d00006902sv*sd*bc*sc*i*
alias:          pci:v00001002d00006901sv*sd*bc*sc*i*
alias:          pci:v00001002d00006900sv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Asv*sd*bc*sc*i*
alias:          pci:v00001002d00009859sv*sd*bc*sc*i*
alias:          pci:v00001002d00009858sv*sd*bc*sc*i*
alias:          pci:v00001002d00009857sv*sd*bc*sc*i*
alias:          pci:v00001002d00009856sv*sd*bc*sc*i*
alias:          pci:v00001002d00009855sv*sd*bc*sc*i*
alias:          pci:v00001002d00009854sv*sd*bc*sc*i*
alias:          pci:v00001002d00009853sv*sd*bc*sc*i*
alias:          pci:v00001002d00009852sv*sd*bc*sc*i*
alias:          pci:v00001002d00009851sv*sd*bc*sc*i*
alias:          pci:v00001002d00009850sv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Asv*sd*bc*sc*i*
alias:          pci:v00001002d00009839sv*sd*bc*sc*i*
alias:          pci:v00001002d00009838sv*sd*bc*sc*i*
alias:          pci:v00001002d00009837sv*sd*bc*sc*i*
alias:          pci:v00001002d00009836sv*sd*bc*sc*i*
alias:          pci:v00001002d00009835sv*sd*bc*sc*i*
alias:          pci:v00001002d00009834sv*sd*bc*sc*i*
alias:          pci:v00001002d00009833sv*sd*bc*sc*i*
alias:          pci:v00001002d00009832sv*sd*bc*sc*i*
alias:          pci:v00001002d00009831sv*sd*bc*sc*i*
alias:          pci:v00001002d00009830sv*sd*bc*sc*i*
alias:          pci:v00001002d000067BEsv*sd*bc*sc*i*
alias:          pci:v00001002d000067BAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067B9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067AAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067A9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Csv*sd*bc*sc*i*
alias:          pci:v00001002d00006658sv*sd*bc*sc*i*
alias:          pci:v00001002d00006651sv*sd*bc*sc*i*
alias:          pci:v00001002d00006650sv*sd*bc*sc*i*
alias:          pci:v00001002d00006649sv*sd*bc*sc*i*
alias:          pci:v00001002d00006647sv*sd*bc*sc*i*
alias:          pci:v00001002d00006646sv*sd*bc*sc*i*
alias:          pci:v00001002d00006641sv*sd*bc*sc*i*
alias:          pci:v00001002d00006640sv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00001318sv*sd*bc*sc*i*
alias:          pci:v00001002d00001317sv*sd*bc*sc*i*
alias:          pci:v00001002d00001316sv*sd*bc*sc*i*
alias:          pci:v00001002d00001315sv*sd*bc*sc*i*
alias:          pci:v00001002d00001313sv*sd*bc*sc*i*
alias:          pci:v00001002d00001312sv*sd*bc*sc*i*
alias:          pci:v00001002d00001311sv*sd*bc*sc*i*
alias:          pci:v00001002d00001310sv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Asv*sd*bc*sc*i*
alias:          pci:v00001002d00001309sv*sd*bc*sc*i*
alias:          pci:v00001002d00001307sv*sd*bc*sc*i*
alias:          pci:v00001002d00001306sv*sd*bc*sc*i*
alias:          pci:v00001002d00001305sv*sd*bc*sc*i*
alias:          pci:v00001002d00001304sv*sd*bc*sc*i*
alias:          pci:v00001002d0000666Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006667sv*sd*bc*sc*i*
alias:          pci:v00001002d00006665sv*sd*bc*sc*i*
alias:          pci:v00001002d00006664sv*sd*bc*sc*i*
alias:          pci:v00001002d00006663sv*sd*bc*sc*i*
alias:          pci:v00001002d00006660sv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00006839sv*sd*bc*sc*i*
alias:          pci:v00001002d00006838sv*sd*bc*sc*i*
alias:          pci:v00001002d00006837sv*sd*bc*sc*i*
alias:          pci:v00001002d00006835sv*sd*bc*sc*i*
alias:          pci:v00001002d00006831sv*sd*bc*sc*i*
alias:          pci:v00001002d00006830sv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006829sv*sd*bc*sc*i*
alias:          pci:v00001002d00006828sv*sd*bc*sc*i*
alias:          pci:v00001002d00006827sv*sd*bc*sc*i*
alias:          pci:v00001002d00006826sv*sd*bc*sc*i*
alias:          pci:v00001002d00006825sv*sd*bc*sc*i*
alias:          pci:v00001002d00006824sv*sd*bc*sc*i*
alias:          pci:v00001002d00006823sv*sd*bc*sc*i*
alias:          pci:v00001002d00006822sv*sd*bc*sc*i*
alias:          pci:v00001002d00006821sv*sd*bc*sc*i*
alias:          pci:v00001002d00006820sv*sd*bc*sc*i*
alias:          pci:v00001002d00006631sv*sd*bc*sc*i*
alias:          pci:v00001002d00006623sv*sd*bc*sc*i*
alias:          pci:v00001002d00006621sv*sd*bc*sc*i*
alias:          pci:v00001002d00006620sv*sd*bc*sc*i*
alias:          pci:v00001002d00006617sv*sd*bc*sc*i*
alias:          pci:v00001002d00006613sv*sd*bc*sc*i*
alias:          pci:v00001002d00006611sv*sd*bc*sc*i*
alias:          pci:v00001002d00006610sv*sd*bc*sc*i*
alias:          pci:v00001002d00006608sv*sd*bc*sc*i*
alias:          pci:v00001002d00006607sv*sd*bc*sc*i*
alias:          pci:v00001002d00006606sv*sd*bc*sc*i*
alias:          pci:v00001002d00006605sv*sd*bc*sc*i*
alias:          pci:v00001002d00006604sv*sd*bc*sc*i*
alias:          pci:v00001002d00006603sv*sd*bc*sc*i*
alias:          pci:v00001002d00006602sv*sd*bc*sc*i*
alias:          pci:v00001002d00006601sv*sd*bc*sc*i*
alias:          pci:v00001002d00006600sv*sd*bc*sc*i*
alias:          pci:v00001002d00006819sv*sd*bc*sc*i*
alias:          pci:v00001002d00006818sv*sd*bc*sc*i*
alias:          pci:v00001002d00006817sv*sd*bc*sc*i*
alias:          pci:v00001002d00006816sv*sd*bc*sc*i*
alias:          pci:v00001002d00006811sv*sd*bc*sc*i*
alias:          pci:v00001002d00006810sv*sd*bc*sc*i*
alias:          pci:v00001002d00006809sv*sd*bc*sc*i*
alias:          pci:v00001002d00006808sv*sd*bc*sc*i*
alias:          pci:v00001002d00006806sv*sd*bc*sc*i*
alias:          pci:v00001002d00006802sv*sd*bc*sc*i*
alias:          pci:v00001002d00006801sv*sd*bc*sc*i*
alias:          pci:v00001002d00006800sv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006799sv*sd*bc*sc*i*
alias:          pci:v00001002d00006798sv*sd*bc*sc*i*
alias:          pci:v00001002d00006792sv*sd*bc*sc*i*
alias:          pci:v00001002d00006791sv*sd*bc*sc*i*
alias:          pci:v00001002d00006790sv*sd*bc*sc*i*
alias:          pci:v00001002d0000678Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006788sv*sd*bc*sc*i*
alias:          pci:v00001002d00006784sv*sd*bc*sc*i*
alias:          pci:v00001002d00006780sv*sd*bc*sc*i*
depends:        drm_kms_helper,drm,amdttm,amdkcl,iommu_v2,drm_ttm_helper,amd-sched,i2c-algo-bit
retpoline:      Y
name:           amdgpu
vermagic:       5.11.0-37-generic SMP mod_unload modversions 
sig_id:         PKCS#7
signer:         sanori-laptop Secure Boot Module Signature key
sig_key:        33:51:14:A8:23:47:89:F3:EC:A6:F4:E5:4B:F6:4C:6F:0A:5E:94:6E
sig_hashalgo:   sha512
signature:      46:7C:0E:2E:61:04:72:8F:8F:20:32:A5:E6:2D:88:4F:F1:AC:09:ED:
		06:DA:19:57:F4:45:BD:88:89:C3:FF:F8:9B:F0:46:E2:0F:8B:13:D5:
		63:5B:CA:63:82:4B:21:3D:5A:E2:02:82:ED:E3:36:7D:80:9B:26:54:
		6E:E1:8D:F5:D9:C7:18:4D:72:A5:F2:30:25:E6:4C:7D:69:42:C7:C9:
		87:B7:CB:40:5E:DF:E2:2D:B7:B0:AB:DB:30:62:75:9C:CC:FA:55:54:
		38:65:F8:B1:31:3A:33:A3:BF:0C:40:A5:74:0F:31:1C:57:63:C6:6E:
		37:32:B4:CF:CC:8A:9B:1A:60:A6:82:DB:BC:6B:4A:F5:54:79:76:71:
		42:02:1F:7E:0C:D3:E5:3B:2F:0F:E4:C9:3C:0D:86:BD:07:C6:DE:FE:
		79:2E:ED:0F:3E:A4:54:73:A5:6C:BC:D4:38:39:67:6D:EA:7A:0D:6A:
		57:93:1A:B3:99:40:EC:17:42:46:C3:9A:71:5A:A7:F0:D0:94:3B:04:
		A4:5B:E3:E8:40:D3:0C:C7:4F:BA:AD:FC:E4:F6:CA:F6:83:C1:85:18:
		6F:9D:C0:BB:B8:01:7B:19:7B:90:49:89:A6:4C:CC:2F:39:0F:D3:19:
		E9:95:D9:C9:F8:A2:E3:B1:BA:99:5E:B5:57:95:F2:9D
parm:           vramlimit:Restrict VRAM for testing, in megabytes (int)
parm:           vis_vramlimit:Restrict visible VRAM for testing, in megabytes (int)
parm:           gartsize:Size of GART to setup in megabytes (32, 64, etc., -1=auto) (uint)
parm:           gttsize:Size of the GTT domain in megabytes (-1 = auto) (int)
parm:           moverate:Maximum buffer migration rate in MB/s. (32, 64, etc., -1=auto, 0=1=disabled) (int)
parm:           benchmark:Run benchmark (int)
parm:           test:Run tests (int)
parm:           audio:Audio enable (-1 = auto, 0 = disable, 1 = enable) (int)
parm:           disp_priority:Display Priority (0 = auto, 1 = normal, 2 = high) (int)
parm:           hw_i2c:hw i2c engine enable (0 = disable) (int)
parm:           pcie_gen2:PCIE Gen2 mode (-1 = auto, 0 = disable, 1 = enable) (int)
parm:           msi:MSI support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           lockup_timeout:GPU lockup timeout in ms (default: for bare metal 10000 for non-compute jobs and 60000 for compute jobs; for passthrough or sriov, 10000 for all jobs. 0: keep default value. negative: infinity timeout), format: for bare metal [Non-Compute] or [GFX,Compute,SDMA,Video]; for passthrough or sriov [all jobs] or [GFX,Compute,SDMA,Video]. (string)
parm:           dpm:DPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           fw_load_type:firmware loading type (0 = direct, 1 = SMU, 2 = PSP, -1 = auto) (int)
parm:           aspm:ASPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           runpm:PX runtime pm (2 = force enable with BAMACO, 1 = force enable with BACO, 0 = disable, -1 = PX only default) (int)
parm:           ip_block_mask:IP Block Mask (all blocks enabled (default)) (uint)
parm:           bapm:BAPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           deep_color:Deep Color support (1 = enable, 0 = disable (default)) (int)
parm:           vm_size:VM address space size in gigabytes (default 64GB) (int)
parm:           vm_fragment_size:VM fragment size in bits (4, 5, etc. 4 = 64K (default), Max 9 = 2M) (int)
parm:           vm_block_size:VM page table size in bits (default depending on vm_size) (int)
parm:           vm_fault_stop:Stop on VM fault (0 = never (default), 1 = print first, 2 = always) (int)
parm:           vm_debug:Debug VM handling (0 = disabled (default), 1 = enabled) (int)
parm:           vm_update_mode:VM update using CPU (0 = never (default except for large BAR(LB)), 1 = Graphics only, 2 = Compute only (default for LB), 3 = Both (int)
parm:           exp_hw_support:experimental hw support (1 = enable, 0 = disable (default)) (int)
parm:           dc:Display Core driver (1 = enable, 0 = disable, -1 = auto (default)) (int)
parm:           sched_jobs:the max number of jobs supported in the sw queue (default 32) (int)
parm:           sched_hw_submission:the max number of HW submissions (default 2) (int)
parm:           ppfeaturemask:all power features enabled (default)) (hexint)
parm:           no_evict:Support pinning request from user space (1 = enable, 0 = disable (default)) (int)
parm:           direct_gma_size:Direct GMA size in megabytes (max 96MB) (int)
parm:           ssg:SSG support (1 = enable, 0 = disable (default)) (int)
parm:           forcelongtraining:force memory long training (uint)
parm:           pcie_gen_cap:PCIE Gen Caps (0: autodetect (default)) (uint)
parm:           pcie_lane_cap:PCIE Lane Caps (0: autodetect (default)) (uint)
parm:           cg_mask:Clockgating flags mask (0 = disable clock gating) (uint)
parm:           pg_mask:Powergating flags mask (0 = disable power gating) (uint)
parm:           sdma_phase_quantum:SDMA context switch phase quantum (x 1K GPU clock cycles, 0 = no change (default 32)) (uint)
parm:           disable_cu:Disable CUs (se.sh.cu,...) (charp)
parm:           virtual_display:Enable virtual display feature (the virtual_display will be set like xxxx:xx:xx.x,x;xxxx:xx:xx.x,x) (charp)
parm:           job_hang_limit:how much time allow a job hang and not drop it (default 0) (int)
parm:           lbpw:Load Balancing Per Watt (LBPW) support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           compute_multipipe:Force compute queues to be spread across pipes (1 = enable, 0 = disable, -1 = auto) (int)
parm:           gpu_recovery:Enable GPU recovery mechanism, (2 = advanced tdr mode, 1 = enable, 0 = disable, -1 = auto) (int)
parm:           emu_mode:Emulation mode, (1 = enable, 0 = disable) (int)
parm:           ras_enable:Enable RAS features on the GPU (0 = disable, 1 = enable, -1 = auto (default)) (int)
parm:           ras_mask:Mask of RAS features to enable (default 0xffffffff), only valid when ras_enable == 1 (uint)
parm:           timeout_fatal_disable:disable watchdog timeout fatal error (false = default) (bool)
parm:           timeout_period:watchdog timeout period (0 = timeout disabled, 1 ~ 0x23 = timeout maxcycles = (1 << period) (uint)
parm:           si_support:SI support (1 = enabled (default), 0 = disabled) (int)
parm:           cik_support:CIK support (1 = enabled (default), 0 = disabled) (int)
parm:           smu_memory_pool_size:reserve gtt for smu debug usage, 0 = disable,0x1 = 256Mbyte, 0x2 = 512Mbyte, 0x4 = 1 Gbyte, 0x8 = 2GByte (uint)
parm:           async_gfx_ring:Asynchronous GFX rings that could be configured with either different priorities (HP3D ring and LP3D ring), or equal priorities (0 = disabled, 1 = enabled (default)) (int)
parm:           mcbp:Enable Mid-command buffer preemption (0 = disabled (default), 1 = enabled) (int)
parm:           discovery:Allow driver to discover hardware IPs from IP Discovery table at the top of VRAM (int)
parm:           mes:Enable Micro Engine Scheduler (0 = disabled (default), 1 = enabled) (int)
parm:           noretry:Disable retry faults (0 = retry enabled, 1 = retry disabled, -1 auto (default)) (int)
parm:           force_asic_type:A non negative value used to specify the asic type for all supported GPUs (int)
parm:           sched_policy:Scheduling policy (0 = HWS (Default), 1 = HWS without over-subscription, 2 = Non-HWS (Used for debugging only) (int)
parm:           hws_max_conc_proc:Max # processes HWS can execute concurrently when sched_policy=0 (0 = no concurrency, #VMIDs for KFD = Maximum(default)) (int)
parm:           cwsr_enable:CWSR enable (0 = Off, 1 = On (Default)) (int)
parm:           max_num_of_queues_per_device:Maximum number of supported queues per device (1 = Minimum, 4096 = default) (int)
parm:           send_sigterm:Send sigterm to HSA process on unhandled exception (0 = disable, 1 = enable) (int)
parm:           debug_largebar:Debug large-bar flag used to simulate large-bar capability on non-large bar machine (0 = disable, 1 = enable) (int)
parm:           ignore_crat:Ignore CRAT table during KFD initialization (0 = auto (default), 1 = ignore CRAT) (int)
parm:           halt_if_hws_hang:Halt if HWS hang is detected (0 = off (default), 1 = on) (int)
parm:           hws_gws_support:Assume MEC2 FW supports GWS barriers (false = rely on FW version check (Default), true = force supported) (bool)
parm:           queue_preemption_timeout_ms:queue preemption timeout in ms (1 = Minimum, 9000 = default) (int)
parm:           debug_evictions:enable eviction debug messages (false = default) (bool)
parm:           no_system_mem_limit:disable system memory limit (false = default) (bool)
parm:           no_queue_eviction_on_vm_fault:No queue eviction on VM fault (0 = queue eviction, 1 = no queue eviction) (int)
parm:           priv_cp_queues:Enable privileged mode for CP queues (0 = off (default), 1 = on) (int)
parm:           keep_idle_process_evicted:Restore evicted process only if queues are active (N = off(default), Y = on) (bool)
parm:           pcie_p2p:Enable PCIe P2P (requires large-BAR). (N = off, Y = on(default)) (bool)
parm:           dcfeaturemask:all stable DC features enabled (default)) (uint)
parm:           dcdebugmask:all debug options disabled (default)) (uint)
parm:           abmlevel:ABM level (0 = off (default), 1-4 = backlight reduction level)  (uint)
parm:           backlight:Backlight control (0 = pwm, 1 = aux, -1 auto (default)) (bint)
parm:           tmz:Enable TMZ feature (-1 = auto (default), 0 = off, 1 = on) (int)
parm:           freesync_video:Enable freesync modesetting optimization feature (0 = off (default), 1 = on) (uint)
parm:           reset_method:GPU reset method (-1 = auto (default), 0 = legacy, 1 = mode0, 2 = mode1, 3 = mode2, 4 = baco/bamaco, 5 = pci) (int)
parm:           bad_page_threshold:Bad page threshold(-1 = auto(default value), 0 = disable bad page retirement) (int)
parm:           num_kcq:number of kernel compute queue user want to setup (8 if set to greater than 8 or less than 0, only affect gfx 8+) (int)
parm:           smu_pptable_id:specify pptable id to be used (-1 = auto(default) value, 0 = use pptable from vbios, > 0 = soft pptable id) (int)
```

### Additional information
1. `clinfo`'s output without libncurses5
```
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3305.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               0
```

2. `rocminfo`'s output
```
[37mROCk module is loaded[0m
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
  Name:                    AMD Ryzen 5 4500U with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 4500U with Radeon Graphics
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
  Max Clock Freq. (MHz):   2375                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            6                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    15773232(0xf0ae30) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    15773232(0xf0ae30) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    15773232(0xf0ae30) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Renoir                             
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
    L2:                      1024(0x400) KB                     
  Chip ID:                 5686(0x1636)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1500                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            26                                 
  SIMDs per CU:            4                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
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
      Size:                    524288(0x80000) KB                 
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
      Name:                    amdgcn-amd-amdhsa--gfx902:xnack+   
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

3. `clinfo`'s output without `rock-dkms` (= with Ubuntu bundled amdgpu.ko)
- GPU was resetted too.
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3305.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Renoir
  Device Topology:				 PCI[ B#3, D#0, F#0 ]
  Max compute units:				 26
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1500Mhz
  Address bits:					 64
  Max memory allocation:			 456340272
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 16384
  Max image 3D height:				 16384
  Max image 3D depth:				 8192
  Max samplers within kernel:			 5686
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 536870912
  Constant buffer size:				 456340272
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 456340272
  Max global variable size:			 456340272
  Max global variable preferred total size:	 536870912
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f3858229e10
  Name:						 gfx902:xnack-
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3305.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```

## Question
Is there a workaround to avoid this GPU panic?
I tried several ROCm version from 4.2 to 4.3.1, but I could not succeed.
 