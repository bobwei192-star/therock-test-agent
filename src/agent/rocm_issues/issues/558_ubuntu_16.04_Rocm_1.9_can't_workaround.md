# ubuntu 16.04 Rocm 1.9 can't workaround

> **Issue #558**
> **状态**: closed
> **创建时间**: 2018-09-26T07:20:38Z
> **更新时间**: 2018-09-27T17:19:45Z
> **关闭时间**: 2018-09-27T16:34:54Z
> **作者**: tom21tom21
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/558

## 描述

CPU:E5 2670 v2
GPU:RX580
System:Ubuntu 16.04
Kernel:4.15.0-34-generic 

I tried two days and referenced many issue. But the problem is the same.

PS. The OS reinstall.
```
$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104
```
```
$ /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (2671.3)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Radeon RX 580 Series
  Device Topology:                               PCI[ B#2, D#0, F#0 ]
  Max compute units:                             36
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
  Max clock frequency:                           1360Mhz
  Address bits:                                  64
  Max memory allocation:                         4244635648
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    16
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              2048
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     No
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            8200589312
  Constant buffer size:                          4244635648
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             32768
  Max pipe arguments:                            0
  Max pipe active reservations:                  0
  Max pipe packet size:                          0
  Max global variable size:                      0
  Max global variable preferred total size:      0
  Max read/write image args:                     0
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
  SVM capabilities:
    Coarse grain buffer:                         No
    Fine grain buffer:                           No
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7ff074545190
  Name:                                          Ellesmere
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 1.2
  Driver version:                                2671.3
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2 AMD-APP (2671.3)
  Extensions:                                    cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event
```
```
 python /opt/rocm/bin/rocm_smi.py


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  0   37c     29.225W  300Mhz   300Mhz   42.75%   auto      0%         0%
================================================================================
====================           End of ROCm SMI Log          ====================
```

```
python /opt/rocm/bin/rocm_smi.py -p


====================    ROCm System Management Interface    ====================
================================================================================
GPU[0]          : Current PowerPlay Level: auto
================================================================================
====================           End of ROCm SMI Log          ====================
```

```
lspci -tv
-+-[0000:ff]-+-08.0  Intel Corporation Xeon E5/Core i7 QPI Link 0
 |           +-08.3  Intel Corporation Xeon E5/Core i7 QPI Link Reut 0
 |           +-08.4  Intel Corporation Xeon E5/Core i7 QPI Link Reut 0
 |           +-09.0  Intel Corporation Xeon E5/Core i7 QPI Link 1
 |           +-09.3  Intel Corporation Xeon E5/Core i7 QPI Link Reut 1
 |           +-09.4  Intel Corporation Xeon E5/Core i7 QPI Link Reut 1
 |           +-0a.0  Intel Corporation Xeon E5/Core i7 Power Control Unit 0
 |           +-0a.1  Intel Corporation Xeon E5/Core i7 Power Control Unit 1
 |           +-0a.2  Intel Corporation Xeon E5/Core i7 Power Control Unit 2
 |           +-0a.3  Intel Corporation Xeon E5/Core i7 Power Control Unit 3
 |           +-0b.0  Intel Corporation Xeon E5/Core i7 Interrupt Control Registers
 |           +-0b.3  Intel Corporation Xeon E5/Core i7 Semaphore and Scratchpad Configuration Registers
 |           +-0c.0  Intel Corporation Xeon E5/Core i7 Unicast Register 0
 |           +-0c.1  Intel Corporation Xeon E5/Core i7 Unicast Register 0
 |           +-0c.2  Intel Corporation Xeon E5/Core i7 Unicast Register 0
 |           +-0c.3  Intel Corporation Xeon E5/Core i7 Unicast Register 0
 |           +-0c.6  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller System Address Decoder 0
 |           +-0c.7  Intel Corporation Xeon E5/Core i7 System Address Decoder
 |           +-0d.0  Intel Corporation Xeon E5/Core i7 Unicast Register 0
 |           +-0d.1  Intel Corporation Xeon E5/Core i7 Unicast Register 0
 |           +-0d.2  Intel Corporation Xeon E5/Core i7 Unicast Register 0
 |           +-0d.3  Intel Corporation Xeon E5/Core i7 Unicast Register 0
 |           +-0d.6  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller System Address Decoder 1
 |           +-0e.0  Intel Corporation Xeon E5/Core i7 Processor Home Agent
 |           +-0e.1  Intel Corporation Xeon E5/Core i7 Processor Home Agent Performance Monitoring
 |           +-0f.0  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Registers
 |           +-0f.1  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller RAS Registers
 |           +-0f.2  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Target Address Decoder 0
 |           +-0f.3  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Target Address Decoder 1
 |           +-0f.4  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Target Address Decoder 2
 |           +-0f.5  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Target Address Decoder 3
 |           +-0f.6  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Target Address Decoder 4
 |           +-10.0  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Channel 0-3 Thermal Control 0
 |           +-10.1  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Channel 0-3 Thermal Control 1
 |           +-10.2  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller ERROR Registers 0
 |           +-10.3  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller ERROR Registers 1
 |           +-10.4  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Channel 0-3 Thermal Control 2
 |           +-10.5  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller Channel 0-3 Thermal Control 3
 |           +-10.6  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller ERROR Registers 2
 |           +-10.7  Intel Corporation Xeon E5/Core i7 Integrated Memory Controller ERROR Registers 3
 |           +-11.0  Intel Corporation Xeon E5/Core i7 DDRIO
 |           +-13.0  Intel Corporation Xeon E5/Core i7 R2PCIe
 |           +-13.1  Intel Corporation Xeon E5/Core i7 Ring to PCI Express Performance Monitor
 |           +-13.4  Intel Corporation Xeon E5/Core i7 QuickPath Interconnect Agent Ring Registers
 |           +-13.5  Intel Corporation Xeon E5/Core i7 Ring to QuickPath Interconnect Link 0 Performance Monitor
 |           \-13.6  Intel Corporation Xeon E5/Core i7 Ring to QuickPath Interconnect Link 1 Performance Monitor
 \-[0000:00]-+-00.0  Intel Corporation Xeon E5/Core i7 DMI2
             +-02.0-[01]--
             +-03.0-[02]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
             |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
             +-05.0  Intel Corporation Xeon E5/Core i7 Address Map, VTd_Misc, System Management
             +-05.2  Intel Corporation Xeon E5/Core i7 Control Status and Global Errors
             +-05.4  Intel Corporation Xeon E5/Core i7 I/O APIC
             +-11.0-[03]--
             +-16.0  Intel Corporation C600/X79 series chipset MEI Controller #1
             +-1a.0  Intel Corporation C600/X79 series chipset USB2 Enhanced Host Controller #2
             +-1b.0  Intel Corporation C600/X79 series chipset High Definition Audio Controller
             +-1c.0-[04]--
             +-1c.2-[05]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
             +-1c.3-[06]----00.0  VIA Technologies, Inc. VL805 USB 3.0 Host Controller
             +-1d.0  Intel Corporation C600/X79 series chipset USB2 Enhanced Host Controller #1
             +-1e.0-[07]--
             +-1f.0  Intel Corporation C600/X79 series chipset LPC Controller
             +-1f.2  Intel Corporation C600/X79 series chipset 6-Port SATA AHCI Controller
             \-1f.3  Intel Corporation C600/X79 series chipset SMBus Host Controller
```

```
lspci -n
00:00.0 0600: 8086:3c00 (rev 07)
00:02.0 0604: 8086:3c04 (rev 07)
00:03.0 0604: 8086:3c08 (rev 07)
00:05.0 0880: 8086:3c28 (rev 07)
00:05.2 0880: 8086:3c2a (rev 07)
00:05.4 0800: 8086:3c2c (rev 07)
00:11.0 0604: 8086:1d3e (rev 06)
00:16.0 0780: 8086:1d3a (rev 05)
00:1a.0 0c03: 8086:1d2d (rev 06)
00:1b.0 0403: 8086:1d20 (rev 06)
00:1c.0 0604: 8086:1d10 (rev b6)
00:1c.2 0604: 8086:1d14 (rev b6)
00:1c.3 0604: 8086:1d16 (rev b6)
00:1d.0 0c03: 8086:1d26 (rev 06)
00:1e.0 0604: 8086:244e (rev a6)
00:1f.0 0601: 8086:1d41 (rev 06)
00:1f.2 0106: 8086:1d02 (rev 06)
00:1f.3 0c05: 8086:1d22 (rev 06)
02:00.0 0300: 1002:67df (rev e7)
02:00.1 0403: 1002:aaf0
05:00.0 0200: 10ec:8168 (rev 07)
06:00.0 0c03: 1106:3483 (rev 01)
ff:08.0 0880: 8086:3c80 (rev 07)
ff:08.3 0880: 8086:3c83 (rev 07)
ff:08.4 0880: 8086:3c84 (rev 07)
ff:09.0 0880: 8086:3c90 (rev 07)
ff:09.3 0880: 8086:3c93 (rev 07)
ff:09.4 0880: 8086:3c94 (rev 07)
ff:0a.0 0880: 8086:3cc0 (rev 07)
ff:0a.1 0880: 8086:3cc1 (rev 07)
ff:0a.2 0880: 8086:3cc2 (rev 07)
ff:0a.3 0880: 8086:3cd0 (rev 07)
ff:0b.0 0880: 8086:3ce0 (rev 07)
ff:0b.3 0880: 8086:3ce3 (rev 07)
ff:0c.0 0880: 8086:3ce8 (rev 07)
ff:0c.1 0880: 8086:3ce8 (rev 07)
ff:0c.2 0880: 8086:3ce8 (rev 07)
ff:0c.3 0880: 8086:3ce8 (rev 07)
ff:0c.6 0880: 8086:3cf4 (rev 07)
ff:0c.7 0880: 8086:3cf6 (rev 07)
ff:0d.0 0880: 8086:3ce8 (rev 07)
ff:0d.1 0880: 8086:3ce8 (rev 07)
ff:0d.2 0880: 8086:3ce8 (rev 07)
ff:0d.3 0880: 8086:3ce8 (rev 07)
ff:0d.6 0880: 8086:3cf5 (rev 07)
ff:0e.0 0880: 8086:3ca0 (rev 07)
ff:0e.1 1101: 8086:3c46 (rev 07)
ff:0f.0 0880: 8086:3ca8 (rev 07)
ff:0f.1 0880: 8086:3c71 (rev 07)
ff:0f.2 0880: 8086:3caa (rev 07)
ff:0f.3 0880: 8086:3cab (rev 07)
ff:0f.4 0880: 8086:3cac (rev 07)
ff:0f.5 0880: 8086:3cad (rev 07)
ff:0f.6 0880: 8086:3cae (rev 07)
ff:10.0 0880: 8086:3cb0 (rev 07)
ff:10.1 0880: 8086:3cb1 (rev 07)
ff:10.2 0880: 8086:3cb2 (rev 07)
ff:10.3 0880: 8086:3cb3 (rev 07)
ff:10.4 0880: 8086:3cb4 (rev 07)
ff:10.5 0880: 8086:3cb5 (rev 07)
ff:10.6 0880: 8086:3cb6 (rev 07)
ff:10.7 0880: 8086:3cb7 (rev 07)
ff:11.0 0880: 8086:3cb8 (rev 07)
ff:13.0 0880: 8086:3ce4 (rev 07)
ff:13.1 1101: 8086:3c43 (rev 07)
ff:13.4 1101: 8086:3ce6 (rev 07)
ff:13.5 1101: 8086:3c44 (rev 07)
ff:13.6 0880: 8086:3c45 (rev 07)
```
```
$lsmod
Module                  Size  Used by
nls_iso8859_1          16384  2
intel_rapl             20480  0
sb_edac                24576  0
x86_pkg_temp_thermal    16384  0
intel_powerclamp       16384  0
coretemp               16384  0
snd_hda_codec_realtek   106496  1
snd_hda_codec_hdmi     49152  1
snd_hda_codec_generic    73728  1 snd_hda_codec_realtek
kvm_intel             212992  0
kvm                   598016  1 kvm_intel
snd_hda_intel          40960  5
snd_hda_codec         126976  4 snd_hda_intel,snd_hda_codec_hdmi,snd_hda_codec_generic,snd_hda_codec_realtek
irqbypass              16384  1 kvm
snd_hda_core           81920  5 snd_hda_intel,snd_hda_codec,snd_hda_codec_hdmi,snd_hda_codec_generic,snd_hda_codec_realtek
crct10dif_pclmul       16384  0
crc32_pclmul           16384  0
snd_hwdep              20480  1 snd_hda_codec
ghash_clmulni_intel    16384  0
pcbc                   16384  0
snd_pcm                98304  4 snd_hda_intel,snd_hda_codec,snd_hda_core,snd_hda_codec_hdmi
snd_seq_midi           16384  0
snd_seq_midi_event     16384  1 snd_seq_midi
joydev                 24576  0
input_leds             16384  0
snd_rawmidi            32768  1 snd_seq_midi
aesni_intel           188416  0
aes_x86_64             20480  1 aesni_intel
crypto_simd            16384  1 aesni_intel
glue_helper            16384  1 aesni_intel
cryptd                 24576  3 crypto_simd,ghash_clmulni_intel,aesni_intel
snd_seq                65536  2 snd_seq_midi_event,snd_seq_midi
intel_cstate           20480  0
intel_rapl_perf        16384  0
snd_seq_device         16384  3 snd_seq,snd_rawmidi,snd_seq_midi
snd_timer              32768  2 snd_seq,snd_pcm
serio_raw              16384  0
snd                    81920  21 snd_hda_intel,snd_hwdep,snd_seq,snd_hda_codec,snd_timer,snd_rawmidi,snd_hda_codec_hdmi,snd_hda_codec_generic,snd_seq_device,snd_hda_codec_realtek,snd_pcm
mei_me                 40960  0
lpc_ich                24576  0
mei                    90112  1 mei_me
soundcore              16384  1 snd
shpchp                 36864  0
mac_hid                16384  0
parport_pc             36864  1
ppdev                  20480  0
lp                     20480  0
parport                49152  3 lp,parport_pc,ppdev
autofs4                40960  2
uas                    24576  0
usb_storage            69632  2 uas
hid_logitech_hidpp     32768  0
hid_logitech_dj        20480  0
hid_generic            16384  0
usbhid                 49152  0
hid                   118784  6 hid_generic,usbhid,hid_logitech_dj,hid_logitech_hidpp
amdkfd                180224  1
amd_iommu_v2           20480  1 amdkfd
amdgpu               2732032  53
chash                  16384  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   106496  1 amdgpu
drm_kms_helper        172032  1 amdgpu
syscopyarea            16384  1 drm_kms_helper
sysfillrect            16384  1 drm_kms_helper
psmouse               147456  0
sysimgblt              16384  1 drm_kms_helper
fb_sys_fops            16384  1 drm_kms_helper
ahci                   36864  3
drm                   401408  9 amdgpu,ttm,drm_kms_helper
libahci                32768  1 ahci
r8169                  86016  0
mii                    16384  1 r8169
```

```
$dkms status
amdgpu, 18.30-641594, 4.15.0-34-generic, x86_64: built
amdgpu, 1.9-211, 4.15.0-34-generic, x86_64: built
```

```
$lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.5 LTS
Release:        16.04
```

```
$uname -a
Linux horry-desktop 4.15.0-34-generic #37~16.04.1-Ubuntu SMP Tue Aug 28 10:44:06 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

```
$dmesg | grep kfd
[    1.949412] kfd kfd: Initialized module
[    2.705392] amdgpu 0000:02:00.0: kfd not supported on this ASIC
```

```
$dmesg | grep amd
[    0.000000] Linux version 4.15.0-34-generic (buildd@lgw01-amd64-037) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)) #37~16.04.1-Ubuntu SMP Tue Aug 28 10:44:06 UTC 2018 (Ubuntu 4.15.0-34.37~16.04.1-generic 4.15.18)
[    1.944271] [drm] amdgpu kernel modesetting enabled.
[    1.949564] fb: switching to amdgpudrmfb from EFI VGA
[    1.950089] amdgpu 0000:02:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.950182] amdgpu 0000:02:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[    1.950185] amdgpu 0000:02:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    1.950268] [drm] amdgpu: 8192M of VRAM memory ready
[    1.950269] [drm] amdgpu: 8192M of GTT memory ready.
[    1.950376] amdgpu 0000:02:00.0: amdgpu: using MSI.
[    1.950391] [drm] amdgpu: irq initialized.
[    1.950408] amdgpu: [powerplay] amdgpu: powerplay sw initialized
[    1.950619] amdgpu 0000:02:00.0: fence driver on ring 0 use gpu addr 0x0000000000400040, cpu addr 0x        (ptrval)
[    1.950656] amdgpu 0000:02:00.0: fence driver on ring 1 use gpu addr 0x00000000004000c0, cpu addr 0x        (ptrval)
[    1.950688] amdgpu 0000:02:00.0: fence driver on ring 2 use gpu addr 0x0000000000400140, cpu addr 0x        (ptrval)
[    1.950725] amdgpu 0000:02:00.0: fence driver on ring 3 use gpu addr 0x00000000004001c0, cpu addr 0x        (ptrval)
[    1.950757] amdgpu 0000:02:00.0: fence driver on ring 4 use gpu addr 0x0000000000400240, cpu addr 0x        (ptrval)
[    1.950789] amdgpu 0000:02:00.0: fence driver on ring 5 use gpu addr 0x00000000004002c0, cpu addr 0x        (ptrval)
[    1.950820] amdgpu 0000:02:00.0: fence driver on ring 6 use gpu addr 0x0000000000400340, cpu addr 0x        (ptrval)
[    1.950852] amdgpu 0000:02:00.0: fence driver on ring 7 use gpu addr 0x00000000004003c0, cpu addr 0x        (ptrval)
[    1.950884] amdgpu 0000:02:00.0: fence driver on ring 8 use gpu addr 0x0000000000400440, cpu addr 0x        (ptrval)
[    1.950902] amdgpu 0000:02:00.0: fence driver on ring 9 use gpu addr 0x00000000004004e0, cpu addr 0x        (ptrval)
[    1.951397] amdgpu 0000:02:00.0: fence driver on ring 10 use gpu addr 0x0000000000400560, cpu addr 0x        (ptrval)
[    1.951434] amdgpu 0000:02:00.0: fence driver on ring 11 use gpu addr 0x00000000004005e0, cpu addr 0x        (ptrval)
[    1.951761] amdgpu 0000:02:00.0: fence driver on ring 12 use gpu addr 0x000000f4001e6420, cpu addr 0x        (ptrval)
[    1.951790] amdgpu 0000:02:00.0: fence driver on ring 13 use gpu addr 0x00000000004006e0, cpu addr 0x        (ptrval)
[    1.951817] amdgpu 0000:02:00.0: fence driver on ring 14 use gpu addr 0x0000000000400760, cpu addr 0x        (ptrval)
[    1.951945] amdgpu 0000:02:00.0: fence driver on ring 15 use gpu addr 0x00000000004007e0, cpu addr 0x        (ptrval)
[    1.951975] amdgpu 0000:02:00.0: fence driver on ring 16 use gpu addr 0x0000000000400860, cpu addr 0x        (ptrval)
[    2.687456] fbcon: amdgpudrmfb (fb0) is primary device
[    2.687525] amdgpu 0000:02:00.0: fb0: amdgpudrmfb frame buffer device
[    2.705392] amdgpu 0000:02:00.0: kfd not supported on this ASIC
[    2.705402] [drm] Initialized amdgpu 3.23.0 20150101 for 0000:02:00.0 on minor 0
```
```
$ groups
horry adm cdrom sudo dip plugdev lpadmin sambashare
```

---

## 评论 (15 条)

### 评论 #1 — jlgreathouse (2018-09-26T14:36:35Z)

I see a few problems with the current output you're showing.

1. Based on your DKMS output, you have amdgpu-pro installed. I would recommend uninstalling this with `amdgpu-pro-uninstall`.
2. Based on your DKMS output, the ROCm driver is not fully installed for your kernel. It is built, but not installed. You can fix this by running `sudo dkms install amdgpu/1.9-211`.
3. Your user is not in the 'video' group. You can fix this `sudo usermod -a -G video $LOGNAME`
4. I'm not 100% sure if your CPU [is on our support list for your GPU](https://rocm.github.io/hardware.html). It appears that the Xeon E5-2600 V2 series _does_ [support PCIe atomics](https://software.intel.com/en-us/articles/intel-xeon-processor-e5-2600-v2-product-family-technical-overview). However, I haven't tested this processor specifically.

---

### 评论 #2 — tom21tom21 (2018-09-26T14:43:56Z)

@jlgreathouse  Thank you to your answer.
I will try tomorrow. 
BTW,  I will tell the result asap.


---

### 评论 #3 — tom21tom21 (2018-09-26T15:51:43Z)

> @jlgreathouse Thank you to your answer.
> I will try tomorrow.
> BTW, I will tell the result asap.

Sorry The problem can't solve, even I used above method.

---

### 评论 #4 — jlgreathouse (2018-09-26T17:44:45Z)

Could you rerun the following test after a reboot?

- `groups`
- `uname -r`
- `dkms status`
- `modinfo amdgpu | grep filename`
- `modinfo amdkfd | grep filename`
- `dmesg | grep kfd`
- `dmesg | grep amd`

And could you define what you mean by "the problem" in your latest message? What have you tested to verify that this problem still exists? Thanks.

---

### 评论 #5 — tom21tom21 (2018-09-27T02:25:31Z)

I re-install OS and ROCM.
Under the script.

I define the problem :
```
$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104
```

```
$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```

Please help me. Thank you
```
sudo apt update
Hit:1 http://tw.archive.ubuntu.com/ubuntu xenial InRelease
Hit:2 http://tw.archive.ubuntu.com/ubuntu xenial-updates InRelease
Hit:3 http://tw.archive.ubuntu.com/ubuntu xenial-backports InRelease
Get:4 http://security.ubuntu.com/ubuntu xenial-security InRelease [107 kB]
Fetched 107 kB in 1s (78.0 kB/s)
Reading package lists... Done
Building dependency tree
Reading state information... Done

$sudo apt dist-upgrade
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  bind9-host binutils dnsutils firefox fonts-opensymbol fwupd ghostscript ghostscript-x gir1.2-javascriptcoregtk-4.0
  gir1.2-webkit2-4.0 gnupg gpgv initramfs-tools initramfs-tools-bin initramfs-tools-core intel-microcode libappstream-glib8
  libarchive13 libbind9-140 libcapnp-0.5.3 libcurl3 libcurl3-gnutls libdfu1 libdns-export162 libdns162 libfwupd1 libgd3
  libglib2.0-0 libglib2.0-bin libglib2.0-data libgs9 libgs9-common libisc-export160 libisc160 libisccc140 libisccfg140
  libjavascriptcoregtk-4.0-18 liblcms2-2 liblcms2-utils liblwres141 libnux-4.0-0 libnux-4.0-common libpoppler-glib8 libpoppler58
  libreoffice-avmedia-backend-gstreamer libreoffice-base-core libreoffice-calc libreoffice-common libreoffice-core
  libreoffice-draw libreoffice-gnome libreoffice-gtk libreoffice-impress libreoffice-math libreoffice-ogltrans
  libreoffice-pdfimport libreoffice-style-breeze libreoffice-style-galaxy libreoffice-writer libsmbclient libwbclient0
  libwebkit2gtk-4.0-37 libwebkit2gtk-4.0-37-gtk2 libx11-6 libx11-data libx11-xcb1 libxcursor1 libxml2 linux-libc-dev nux-tools
  poppler-utils python3-uno python3-urllib3 samba-libs squashfs-tools uno-libs3 ure wpasupplicant x11-common xorg xserver-common
81 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 168 MB of archives.
After this operation, 4034 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglib2.0-data all 2.48.2-0ubuntu4.1 [132 kB]
Get:2 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglib2.0-bin amd64 2.48.2-0ubuntu4.1 [39.4 kB]
Get:3 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglib2.0-0 amd64 2.48.2-0ubuntu4.1 [1120 kB]
Get:4 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-ogltrans amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [73.3 kB]
Get:5 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 ure amd64 5.1.6~rc2-0ubuntu1~xenial4 [1532 kB]
Get:6 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 uno-libs3 amd64 5.1.6~rc2-0ubuntu1~xenial4 [704 kB]
Get:7 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libxml2 amd64 2.9.3+dfsg1-1ubuntu0.6 [697 kB]
Get:8 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-calc amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [6463 kB]
Get:9 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-impress amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [969 kB]
Get:10 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-draw amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [2410 kB]
Get:11 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-gnome amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [60.7 kB]
Get:12 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-gtk amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [207 kB]
Get:13 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3-uno amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [137 kB]
Get:14 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-style-galaxy all 1:5.1.6~rc2-0ubuntu1~xenial4 [1523 kB]
Get:15 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-style-breeze all 1:5.1.6~rc2-0ubuntu1~xenial4 [470 kB]
Get:16 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-common all 1:5.1.6~rc2-0ubuntu1~xenial4 [22.4 MB]
Get:17 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-pdfimport amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [182 kB]
Get:18 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-math amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [374 kB]
Get:19 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-base-core amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [714 kB]
Get:20 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-avmedia-backend-gstreamer amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [24.3 kB]
Get:21 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-writer amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [7581 kB]
Get:22 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libreoffice-core amd64 1:5.1.6~rc2-0ubuntu1~xenial4 [28.2 MB]
Get:23 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx11-data all 2:1.6.3-1ubuntu2.1 [113 kB]
Get:24 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx11-6 amd64 2:1.6.3-1ubuntu2.1 [570 kB]
Get:25 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 liblcms2-2 amd64 2.6-3ubuntu2.1 [136 kB]
Get:26 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpoppler58 amd64 0.41.0-0ubuntu1.8 [756 kB]
Get:27 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 fonts-opensymbol all 2:102.7+LibO5.1.6~rc2-0ubuntu1~xenial4 [104 kB]
Get:28 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libcurl3-gnutls amd64 7.47.0-1ubuntu2.9 [184 kB]
Get:29 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 samba-libs amd64 2:4.3.11+dfsg-0ubuntu0.16.04.16 [5161 kB]
Get:30 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libwbclient0 amd64 2:4.3.11+dfsg-0ubuntu0.16.04.16 [30.2 kB]
Get:31 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsmbclient amd64 2:4.3.11+dfsg-0ubuntu0.16.04.16 [53.5 kB]
Get:32 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 gpgv amd64 1.4.20-1ubuntu3.3 [165 kB]
Get:33 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 gnupg amd64 1.4.20-1ubuntu3.3 [626 kB]
Get:34 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 initramfs-tools all 0.122ubuntu8.12 [8628 B]
Get:35 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 initramfs-tools-core all 0.122ubuntu8.12 [44.9 kB]
Get:36 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 initramfs-tools-bin amd64 0.122ubuntu8.12 [9726 B]
Get:37 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libisc-export160 amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [153 kB]
Get:38 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdns-export162 amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [667 kB]
Get:39 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 bind9-host amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [38.4 kB]
Get:40 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 dnsutils amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [89.2 kB]
Get:41 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libisc160 amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [215 kB]
Get:42 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdns162 amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [881 kB]
Get:43 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libisccc140 amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [16.3 kB]
Get:44 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libisccfg140 amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [40.4 kB]
Get:45 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 liblwres141 amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [33.7 kB]
Get:46 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libbind9-140 amd64 1:9.10.3.dfsg.P4-8ubuntu1.11 [23.6 kB]
Get:47 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 binutils amd64 2.26.1-1ubuntu1~16.04.7 [2309 kB]
Get:48 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx11-xcb1 amd64 2:1.6.3-1ubuntu2.1 [9044 B]
Get:49 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 firefox amd64 62.0+build2-0ubuntu0.16.04.5 [44.6 MB]
Get:50 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libarchive13 amd64 3.1.2-11ubuntu0.16.04.4 [262 kB]
Get:51 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libappstream-glib8 amd64 0.5.13-1ubuntu6 [101 kB]
Get:52 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdfu1 amd64 0.8.3-0ubuntu4 [48.3 kB]
Get:53 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libfwupd1 amd64 0.8.3-0ubuntu4 [32.8 kB]
Get:54 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 fwupd amd64 0.8.3-0ubuntu4 [120 kB]
Get:55 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 ghostscript amd64 9.18~dfsg~0-0ubuntu2.9 [40.8 kB]
Get:56 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 ghostscript-x amd64 9.18~dfsg~0-0ubuntu2.9 [34.4 kB]
Get:57 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgs9-common all 9.18~dfsg~0-0ubuntu2.9 [2981 kB]
Get:58 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgs9 amd64 9.18~dfsg~0-0ubuntu2.9 [2060 kB]
Get:59 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libwebkit2gtk-4.0-37-gtk2 amd64 2.20.5-0ubuntu0.16.04.1 [9128 kB]
Get:60 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libwebkit2gtk-4.0-37 amd64 2.20.5-0ubuntu0.16.04.1 [10.5 MB]
Get:61 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libjavascriptcoregtk-4.0-18 amd64 2.20.5-0ubuntu0.16.04.1 [4256 kB]
Get:62 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 gir1.2-webkit2-4.0 amd64 2.20.5-0ubuntu0.16.04.1 [69.0 kB]
Get:63 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 gir1.2-javascriptcoregtk-4.0 amd64 2.20.5-0ubuntu0.16.04.1 [21.4 kB]
Get:64 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libcapnp-0.5.3 amd64 0.5.3-2ubuntu1.1 [580 kB]
Get:65 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libcurl3 amd64 7.47.0-1ubuntu2.9 [186 kB]
Get:66 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgd3 amd64 2.1.1-4ubuntu0.16.04.10 [126 kB]
Get:67 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 liblcms2-utils amd64 2.6-3ubuntu2.1 [40.3 kB]
Get:68 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libnux-4.0-0 amd64 4.0.8+16.04.20180622.2-0ubuntu1 [698 kB]
Get:69 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libnux-4.0-common all 4.0.8+16.04.20180622.2-0ubuntu1 [41.9 kB]
Get:70 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpoppler-glib8 amd64 0.41.0-0ubuntu1.8 [104 kB]
Get:71 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libxcursor1 amd64 1:1.1.14-1ubuntu0.16.04.2 [19.9 kB]
Get:72 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 linux-libc-dev amd64 4.4.0-135.161 [868 kB]
Get:73 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 nux-tools amd64 4.0.8+16.04.20180622.2-0ubuntu1 [10.2 kB]
Get:74 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 poppler-utils amd64 0.41.0-0ubuntu1.8 [131 kB]
Get:75 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3-urllib3 all 1.13.1-2ubuntu0.16.04.2 [58.1 kB]
Get:76 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 squashfs-tools amd64 1:4.3-3ubuntu2.16.04.3 [105 kB]
Get:77 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 wpasupplicant amd64 2.4-0ubuntu6.3 [902 kB]
Get:78 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 x11-common all 1:7.7+13ubuntu3.1 [22.9 kB]
Get:79 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 xorg amd64 1:7.7+13ubuntu3.1 [2978 B]
Get:80 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 xserver-common all 2:1.18.4-0ubuntu0.8 [27.7 kB]
Get:81 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 intel-microcode amd64 3.20180807a.0ubuntu0.16.04.1 [1275 kB]
Fetched 168 MB in 15s (10.7 MB/s)
Extracting templates from packages: 100%
(Reading database ... 215464 files and directories currently installed.)
Preparing to unpack .../libglib2.0-data_2.48.2-0ubuntu4.1_all.deb ...
Unpacking libglib2.0-data (2.48.2-0ubuntu4.1) over (2.48.2-0ubuntu3) ...
Preparing to unpack .../libglib2.0-bin_2.48.2-0ubuntu4.1_amd64.deb ...
Unpacking libglib2.0-bin (2.48.2-0ubuntu4.1) over (2.48.2-0ubuntu3) ...
Preparing to unpack .../libglib2.0-0_2.48.2-0ubuntu4.1_amd64.deb ...
Unpacking libglib2.0-0:amd64 (2.48.2-0ubuntu4.1) over (2.48.2-0ubuntu3) ...
Preparing to unpack .../libreoffice-ogltrans_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-ogltrans (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../ure_5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking ure (5.1.6~rc2-0ubuntu1~xenial4) over (5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../uno-libs3_5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking uno-libs3 (5.1.6~rc2-0ubuntu1~xenial4) over (5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libxml2_2.9.3+dfsg1-1ubuntu0.6_amd64.deb ...
Unpacking libxml2:amd64 (2.9.3+dfsg1-1ubuntu0.6) over (2.9.3+dfsg1-1ubuntu0.5) ...
Preparing to unpack .../libreoffice-calc_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-calc (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-impress_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-impress (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-draw_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-draw (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-gnome_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-gnome (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-gtk_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-gtk (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../python3-uno_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking python3-uno (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-style-galaxy_1%3a5.1.6~rc2-0ubuntu1~xenial4_all.deb ...
Unpacking libreoffice-style-galaxy (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-style-breeze_1%3a5.1.6~rc2-0ubuntu1~xenial4_all.deb ...
Unpacking libreoffice-style-breeze (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-common_1%3a5.1.6~rc2-0ubuntu1~xenial4_all.deb ...
Unpacking libreoffice-common (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-pdfimport_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-pdfimport (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-math_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-math (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-base-core_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-base-core (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-avmedia-backend-gstreamer_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-avmedia-backend-gstreamer (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-writer_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-writer (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libreoffice-core_1%3a5.1.6~rc2-0ubuntu1~xenial4_amd64.deb ...
Unpacking libreoffice-core (1:5.1.6~rc2-0ubuntu1~xenial4) over (1:5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libx11-data_2%3a1.6.3-1ubuntu2.1_all.deb ...
Unpacking libx11-data (2:1.6.3-1ubuntu2.1) over (2:1.6.3-1ubuntu2) ...
Preparing to unpack .../libx11-6_2%3a1.6.3-1ubuntu2.1_amd64.deb ...
Unpacking libx11-6:amd64 (2:1.6.3-1ubuntu2.1) over (2:1.6.3-1ubuntu2) ...
Preparing to unpack .../liblcms2-2_2.6-3ubuntu2.1_amd64.deb ...
Unpacking liblcms2-2:amd64 (2.6-3ubuntu2.1) over (2.6-3ubuntu2) ...
Preparing to unpack .../libpoppler58_0.41.0-0ubuntu1.8_amd64.deb ...
Unpacking libpoppler58:amd64 (0.41.0-0ubuntu1.8) over (0.41.0-0ubuntu1.7) ...
Preparing to unpack .../fonts-opensymbol_2%3a102.7+LibO5.1.6~rc2-0ubuntu1~xenial4_all.deb ...
Unpacking fonts-opensymbol (2:102.7+LibO5.1.6~rc2-0ubuntu1~xenial4) over (2:102.7+LibO5.1.6~rc2-0ubuntu1~xenial3) ...
Preparing to unpack .../libcurl3-gnutls_7.47.0-1ubuntu2.9_amd64.deb ...
Unpacking libcurl3-gnutls:amd64 (7.47.0-1ubuntu2.9) over (7.47.0-1ubuntu2.8) ...
Preparing to unpack .../samba-libs_2%3a4.3.11+dfsg-0ubuntu0.16.04.16_amd64.deb ...
Unpacking samba-libs:amd64 (2:4.3.11+dfsg-0ubuntu0.16.04.16) over (2:4.3.11+dfsg-0ubuntu0.16.04.13) ...
Preparing to unpack .../libwbclient0_2%3a4.3.11+dfsg-0ubuntu0.16.04.16_amd64.deb ...
Unpacking libwbclient0:amd64 (2:4.3.11+dfsg-0ubuntu0.16.04.16) over (2:4.3.11+dfsg-0ubuntu0.16.04.13) ...
Preparing to unpack .../libsmbclient_2%3a4.3.11+dfsg-0ubuntu0.16.04.16_amd64.deb ...
Unpacking libsmbclient:amd64 (2:4.3.11+dfsg-0ubuntu0.16.04.16) over (2:4.3.11+dfsg-0ubuntu0.16.04.13) ...
Preparing to unpack .../gpgv_1.4.20-1ubuntu3.3_amd64.deb ...
Unpacking gpgv (1.4.20-1ubuntu3.3) over (1.4.20-1ubuntu3.2) ...
Processing triggers for man-db (2.7.5-1) ...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for mime-support (3.59ubuntu1) ...
Processing triggers for gnome-menus (3.13.3-6ubuntu3.1) ...
Processing triggers for hicolor-icon-theme (0.15-0ubuntu1.1) ...
Processing triggers for fontconfig (2.11.94-0ubuntu1.1) ...
Setting up gpgv (1.4.20-1ubuntu3.3) ...
(Reading database ... 215464 files and directories currently installed.)
Preparing to unpack .../gnupg_1.4.20-1ubuntu3.3_amd64.deb ...
Unpacking gnupg (1.4.20-1ubuntu3.3) over (1.4.20-1ubuntu3.2) ...
Processing triggers for man-db (2.7.5-1) ...
Processing triggers for install-info (6.1.0.dfsg.1-5) ...
Setting up gnupg (1.4.20-1ubuntu3.3) ...
(Reading database ... 215464 files and directories currently installed.)
Preparing to unpack .../initramfs-tools_0.122ubuntu8.12_all.deb ...
Unpacking initramfs-tools (0.122ubuntu8.12) over (0.122ubuntu8.11) ...
Preparing to unpack .../initramfs-tools-core_0.122ubuntu8.12_all.deb ...
Unpacking initramfs-tools-core (0.122ubuntu8.12) over (0.122ubuntu8.11) ...
Preparing to unpack .../initramfs-tools-bin_0.122ubuntu8.12_amd64.deb ...
Unpacking initramfs-tools-bin (0.122ubuntu8.12) over (0.122ubuntu8.11) ...
Preparing to unpack .../libisc-export160_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking libisc-export160 (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../libdns-export162_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking libdns-export162 (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../bind9-host_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking bind9-host (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../dnsutils_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking dnsutils (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../libisc160_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking libisc160:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../libdns162_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking libdns162:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../libisccc140_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking libisccc140:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../libisccfg140_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking libisccfg140:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../liblwres141_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking liblwres141:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../libbind9-140_1%3a9.10.3.dfsg.P4-8ubuntu1.11_amd64.deb ...
Unpacking libbind9-140:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) over (1:9.10.3.dfsg.P4-8ubuntu1.10) ...
Preparing to unpack .../binutils_2.26.1-1ubuntu1~16.04.7_amd64.deb ...
Unpacking binutils (2.26.1-1ubuntu1~16.04.7) over (2.26.1-1ubuntu1~16.04.6) ...
Preparing to unpack .../libx11-xcb1_2%3a1.6.3-1ubuntu2.1_amd64.deb ...
Unpacking libx11-xcb1:amd64 (2:1.6.3-1ubuntu2.1) over (2:1.6.3-1ubuntu2) ...
Preparing to unpack .../firefox_62.0+build2-0ubuntu0.16.04.5_amd64.deb ...
Unpacking firefox (62.0+build2-0ubuntu0.16.04.5) over (61.0.1+build1-0ubuntu0.16.04.1) ...
Preparing to unpack .../libarchive13_3.1.2-11ubuntu0.16.04.4_amd64.deb ...
Unpacking libarchive13:amd64 (3.1.2-11ubuntu0.16.04.4) over (3.1.2-11ubuntu0.16.04.3) ...
Preparing to unpack .../libappstream-glib8_0.5.13-1ubuntu6_amd64.deb ...
Unpacking libappstream-glib8:amd64 (0.5.13-1ubuntu6) over (0.5.13-1ubuntu5) ...
Preparing to unpack .../libdfu1_0.8.3-0ubuntu4_amd64.deb ...
Unpacking libdfu1:amd64 (0.8.3-0ubuntu4) over (0.8.3-0ubuntu3) ...
Preparing to unpack .../libfwupd1_0.8.3-0ubuntu4_amd64.deb ...
Unpacking libfwupd1:amd64 (0.8.3-0ubuntu4) over (0.8.3-0ubuntu3) ...
Preparing to unpack .../fwupd_0.8.3-0ubuntu4_amd64.deb ...
Unpacking fwupd (0.8.3-0ubuntu4) over (0.8.3-0ubuntu3) ...
Preparing to unpack .../ghostscript_9.18~dfsg~0-0ubuntu2.9_amd64.deb ...
Unpacking ghostscript (9.18~dfsg~0-0ubuntu2.9) over (9.18~dfsg~0-0ubuntu2.8) ...
Preparing to unpack .../ghostscript-x_9.18~dfsg~0-0ubuntu2.9_amd64.deb ...
Unpacking ghostscript-x (9.18~dfsg~0-0ubuntu2.9) over (9.18~dfsg~0-0ubuntu2.8) ...
Preparing to unpack .../libgs9-common_9.18~dfsg~0-0ubuntu2.9_all.deb ...
Unpacking libgs9-common (9.18~dfsg~0-0ubuntu2.9) over (9.18~dfsg~0-0ubuntu2.8) ...
Preparing to unpack .../libgs9_9.18~dfsg~0-0ubuntu2.9_amd64.deb ...
Unpacking libgs9:amd64 (9.18~dfsg~0-0ubuntu2.9) over (9.18~dfsg~0-0ubuntu2.8) ...
Preparing to unpack .../libwebkit2gtk-4.0-37-gtk2_2.20.5-0ubuntu0.16.04.1_amd64.deb ...
Unpacking libwebkit2gtk-4.0-37-gtk2:amd64 (2.20.5-0ubuntu0.16.04.1) over (2.20.3-0ubuntu0.16.04.1) ...
Preparing to unpack .../libwebkit2gtk-4.0-37_2.20.5-0ubuntu0.16.04.1_amd64.deb ...
Unpacking libwebkit2gtk-4.0-37:amd64 (2.20.5-0ubuntu0.16.04.1) over (2.20.3-0ubuntu0.16.04.1) ...
Preparing to unpack .../libjavascriptcoregtk-4.0-18_2.20.5-0ubuntu0.16.04.1_amd64.deb ...
Unpacking libjavascriptcoregtk-4.0-18:amd64 (2.20.5-0ubuntu0.16.04.1) over (2.20.3-0ubuntu0.16.04.1) ...
Preparing to unpack .../gir1.2-webkit2-4.0_2.20.5-0ubuntu0.16.04.1_amd64.deb ...
Unpacking gir1.2-webkit2-4.0:amd64 (2.20.5-0ubuntu0.16.04.1) over (2.20.3-0ubuntu0.16.04.1) ...
Preparing to unpack .../gir1.2-javascriptcoregtk-4.0_2.20.5-0ubuntu0.16.04.1_amd64.deb ...
Unpacking gir1.2-javascriptcoregtk-4.0:amd64 (2.20.5-0ubuntu0.16.04.1) over (2.20.3-0ubuntu0.16.04.1) ...
Preparing to unpack .../libcapnp-0.5.3_0.5.3-2ubuntu1.1_amd64.deb ...
Unpacking libcapnp-0.5.3:amd64 (0.5.3-2ubuntu1.1) over (0.5.3-2ubuntu1) ...
Preparing to unpack .../libcurl3_7.47.0-1ubuntu2.9_amd64.deb ...
Unpacking libcurl3:amd64 (7.47.0-1ubuntu2.9) over (7.47.0-1ubuntu2.8) ...
Preparing to unpack .../libgd3_2.1.1-4ubuntu0.16.04.10_amd64.deb ...
Unpacking libgd3:amd64 (2.1.1-4ubuntu0.16.04.10) over (2.1.1-4ubuntu0.16.04.8) ...
Preparing to unpack .../liblcms2-utils_2.6-3ubuntu2.1_amd64.deb ...
Unpacking liblcms2-utils (2.6-3ubuntu2.1) over (2.6-3ubuntu2) ...
Preparing to unpack .../libnux-4.0-0_4.0.8+16.04.20180622.2-0ubuntu1_amd64.deb ...
Unpacking libnux-4.0-0 (4.0.8+16.04.20180622.2-0ubuntu1) over (4.0.8+16.04.20170816-0ubuntu1) ...
Preparing to unpack .../libnux-4.0-common_4.0.8+16.04.20180622.2-0ubuntu1_all.deb ...
Unpacking libnux-4.0-common (4.0.8+16.04.20180622.2-0ubuntu1) over (4.0.8+16.04.20170816-0ubuntu1) ...
Preparing to unpack .../libpoppler-glib8_0.41.0-0ubuntu1.8_amd64.deb ...
Unpacking libpoppler-glib8:amd64 (0.41.0-0ubuntu1.8) over (0.41.0-0ubuntu1.7) ...
Preparing to unpack .../libxcursor1_1%3a1.1.14-1ubuntu0.16.04.2_amd64.deb ...
Unpacking libxcursor1:amd64 (1:1.1.14-1ubuntu0.16.04.2) over (1:1.1.14-1ubuntu0.16.04.1) ...
Preparing to unpack .../linux-libc-dev_4.4.0-135.161_amd64.deb ...
Unpacking linux-libc-dev:amd64 (4.4.0-135.161) over (4.4.0-131.157) ...
Preparing to unpack .../nux-tools_4.0.8+16.04.20180622.2-0ubuntu1_amd64.deb ...
Unpacking nux-tools (4.0.8+16.04.20180622.2-0ubuntu1) over (4.0.8+16.04.20170816-0ubuntu1) ...
Preparing to unpack .../poppler-utils_0.41.0-0ubuntu1.8_amd64.deb ...
Unpacking poppler-utils (0.41.0-0ubuntu1.8) over (0.41.0-0ubuntu1.7) ...
Preparing to unpack .../python3-urllib3_1.13.1-2ubuntu0.16.04.2_all.deb ...
Unpacking python3-urllib3 (1.13.1-2ubuntu0.16.04.2) over (1.13.1-2ubuntu0.16.04.1) ...
Preparing to unpack .../squashfs-tools_1%3a4.3-3ubuntu2.16.04.3_amd64.deb ...
Unpacking squashfs-tools (1:4.3-3ubuntu2.16.04.3) over (1:4.3-3ubuntu2.16.04.2) ...
Preparing to unpack .../wpasupplicant_2.4-0ubuntu6.3_amd64.deb ...
Unpacking wpasupplicant (2.4-0ubuntu6.3) over (2.4-0ubuntu6.2) ...
Preparing to unpack .../x11-common_1%3a7.7+13ubuntu3.1_all.deb ...
Unpacking x11-common (1:7.7+13ubuntu3.1) over (1:7.7+13ubuntu3) ...
Preparing to unpack .../xorg_1%3a7.7+13ubuntu3.1_amd64.deb ...
Unpacking xorg (1:7.7+13ubuntu3.1) over (1:7.7+13ubuntu3) ...
Preparing to unpack .../xserver-common_2%3a1.18.4-0ubuntu0.8_all.deb ...
Unpacking xserver-common (2:1.18.4-0ubuntu0.8) over (2:1.18.4-0ubuntu0.7) ...
Preparing to unpack .../intel-microcode_3.20180807a.0ubuntu0.16.04.1_amd64.deb ...
Unpacking intel-microcode (3.20180807a.0ubuntu0.16.04.1) over (3.20180425.1~ubuntu0.16.04.2) ...
Processing triggers for man-db (2.7.5-1) ...
Processing triggers for doc-base (0.10.7) ...
Processing 1 changed doc-base file...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for gnome-menus (3.13.3-6ubuntu3.1) ...
Processing triggers for mime-support (3.59ubuntu1) ...
Processing triggers for hicolor-icon-theme (0.15-0ubuntu1.1) ...
Processing triggers for dbus (1.10.6-1ubuntu3.3) ...
Processing triggers for systemd (229-4ubuntu21.4) ...
Processing triggers for ureadahead (0.100.0-19) ...
ureadahead will be reprofiled on next reboot
Setting up libglib2.0-data (2.48.2-0ubuntu4.1) ...
Setting up libglib2.0-0:amd64 (2.48.2-0ubuntu4.1) ...
Setting up libglib2.0-bin (2.48.2-0ubuntu4.1) ...
Setting up uno-libs3 (5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libxml2:amd64 (2.9.3+dfsg1-1ubuntu0.6) ...
Setting up ure (5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up fonts-opensymbol (2:102.7+LibO5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libcurl3-gnutls:amd64 (7.47.0-1ubuntu2.9) ...
Setting up liblcms2-2:amd64 (2.6-3ubuntu2.1) ...
Setting up libx11-data (2:1.6.3-1ubuntu2.1) ...
Setting up libx11-6:amd64 (2:1.6.3-1ubuntu2.1) ...
Setting up libpoppler58:amd64 (0.41.0-0ubuntu1.8) ...
Setting up libwbclient0:amd64 (2:4.3.11+dfsg-0ubuntu0.16.04.16) ...
Setting up samba-libs:amd64 (2:4.3.11+dfsg-0ubuntu0.16.04.16) ...
Setting up libsmbclient:amd64 (2:4.3.11+dfsg-0ubuntu0.16.04.16) ...
Setting up initramfs-tools-bin (0.122ubuntu8.12) ...
Setting up initramfs-tools-core (0.122ubuntu8.12) ...
Setting up initramfs-tools (0.122ubuntu8.12) ...
update-initramfs: deferring update (trigger activated)
Setting up libisc-export160 (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up libdns-export162 (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up libisc160:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up libdns162:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up libisccc140:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up libisccfg140:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up libbind9-140:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up liblwres141:amd64 (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up bind9-host (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up dnsutils (1:9.10.3.dfsg.P4-8ubuntu1.11) ...
Setting up binutils (2.26.1-1ubuntu1~16.04.7) ...
Setting up libx11-xcb1:amd64 (2:1.6.3-1ubuntu2.1) ...
Setting up firefox (62.0+build2-0ubuntu0.16.04.5) ...
Please restart all running instances of firefox, or you will experience problems.
Setting up libarchive13:amd64 (3.1.2-11ubuntu0.16.04.4) ...
Setting up libappstream-glib8:amd64 (0.5.13-1ubuntu6) ...
Setting up libdfu1:amd64 (0.8.3-0ubuntu4) ...
Setting up libfwupd1:amd64 (0.8.3-0ubuntu4) ...
Setting up fwupd (0.8.3-0ubuntu4) ...
Setting up libgs9-common (9.18~dfsg~0-0ubuntu2.9) ...
Setting up libgs9:amd64 (9.18~dfsg~0-0ubuntu2.9) ...
Setting up ghostscript (9.18~dfsg~0-0ubuntu2.9) ...
Setting up ghostscript-x (9.18~dfsg~0-0ubuntu2.9) ...
Setting up libjavascriptcoregtk-4.0-18:amd64 (2.20.5-0ubuntu0.16.04.1) ...
Setting up libwebkit2gtk-4.0-37:amd64 (2.20.5-0ubuntu0.16.04.1) ...
Setting up libwebkit2gtk-4.0-37-gtk2:amd64 (2.20.5-0ubuntu0.16.04.1) ...
Setting up gir1.2-javascriptcoregtk-4.0:amd64 (2.20.5-0ubuntu0.16.04.1) ...
Setting up gir1.2-webkit2-4.0:amd64 (2.20.5-0ubuntu0.16.04.1) ...
Setting up libcapnp-0.5.3:amd64 (0.5.3-2ubuntu1.1) ...
Setting up libcurl3:amd64 (7.47.0-1ubuntu2.9) ...
Setting up libgd3:amd64 (2.1.1-4ubuntu0.16.04.10) ...
Setting up liblcms2-utils (2.6-3ubuntu2.1) ...
Setting up libnux-4.0-common (4.0.8+16.04.20180622.2-0ubuntu1) ...
Setting up libnux-4.0-0 (4.0.8+16.04.20180622.2-0ubuntu1) ...
Setting up libpoppler-glib8:amd64 (0.41.0-0ubuntu1.8) ...
Setting up libxcursor1:amd64 (1:1.1.14-1ubuntu0.16.04.2) ...
Setting up linux-libc-dev:amd64 (4.4.0-135.161) ...
Setting up nux-tools (4.0.8+16.04.20180622.2-0ubuntu1) ...
Installing new version of config file /etc/X11/Xsession.d/50_check_unity_support ...
Setting up poppler-utils (0.41.0-0ubuntu1.8) ...
Setting up python3-urllib3 (1.13.1-2ubuntu0.16.04.2) ...
Setting up squashfs-tools (1:4.3-3ubuntu2.16.04.3) ...
Setting up wpasupplicant (2.4-0ubuntu6.3) ...
Setting up x11-common (1:7.7+13ubuntu3.1) ...
update-rc.d: warning: start and stop actions are no longer supported; falling back to defaults
Setting up xorg (1:7.7+13ubuntu3.1) ...
Setting up xserver-common (2:1.18.4-0ubuntu0.8) ...
Setting up intel-microcode (3.20180807a.0ubuntu0.16.04.1) ...
update-initramfs: deferring update (trigger activated)
intel-microcode: microcode will be updated at next boot
Setting up libreoffice-common (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Installing new version of config file /etc/bash_completion.d/libreoffice.sh ...
Setting up libreoffice-style-galaxy (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-style-breeze (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-core (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-draw (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-impress (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-ogltrans (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-base-core (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-calc (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-gtk (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-gnome (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up python3-uno (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-pdfimport (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-math (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-avmedia-backend-gstreamer (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Setting up libreoffice-writer (1:5.1.6~rc2-0ubuntu1~xenial4) ...
Processing triggers for desktop-file-utils (0.22-1ubuntu5.2) ...
Processing triggers for bamfdaemon (0.5.3~bzr0+16.04.20180209-0ubuntu1) ...
Rebuilding /usr/share/applications/bamf-2.index...
Processing triggers for shared-mime-info (1.5-2ubuntu0.2) ...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for initramfs-tools (0.122ubuntu8.12) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-34-generic
horry@horry-desktop:~$ sudo apt install libnuma-dev -y
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
  libnuma-dev
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 31.5 kB of archives.
After this operation, 164 kB of additional disk space will be used.
Get:1 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libnuma-dev amd64 2.0.11-1ubuntu1.1 [31.5 kB]
Fetched 31.5 kB in 0s (259 kB/s)
Selecting previously unselected package libnuma-dev:amd64.
(Reading database ... 215466 files and directories currently installed.)
Preparing to unpack .../libnuma-dev_2.0.11-1ubuntu1.1_amd64.deb ...
Unpacking libnuma-dev:amd64 (2.0.11-1ubuntu1.1) ...
Processing triggers for man-db (2.7.5-1) ...
Setting up libnuma-dev:amd64 (2.0.11-1ubuntu1.1) ...


$ wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
OK

$ echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list

$ sudo apt update
Hit:1 http://tw.archive.ubuntu.com/ubuntu xenial InRelease
Hit:2 http://tw.archive.ubuntu.com/ubuntu xenial-updates InRelease
Hit:3 http://tw.archive.ubuntu.com/ubuntu xenial-backports InRelease
Get:4 http://security.ubuntu.com/ubuntu xenial-security InRelease [107 kB]
Get:5 http://repo.radeon.com/rocm/apt/debian xenial InRelease [1816 B]
Get:6 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages [6348 B]
Fetched 115 kB in 1s (67.2 kB/s)
AppStream cache update completed, but some metadata was ignored due to errors.
Reading package lists... Done
Building dependency tree
Reading state information... Done
All packages are up to date.


$ sudo apt install rocm-dkms -y
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  comgr dkms g++-5-multilib g++-multilib gcc-5-multilib gcc-multilib hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile
  hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev lib32asan2 lib32atomic1 lib32cilkrts5 lib32gcc-5-dev lib32gcc1
  lib32gomp1 lib32itm1 lib32mpx0 lib32quadmath0 lib32stdc++-5-dev lib32stdc++6 lib32ubsan0 libc6-dev-i386 libc6-dev-x32 libc6-i386
  libc6-x32 libx32asan2 libx32atomic1 libx32cilkrts5 libx32gcc-5-dev libx32gcc1 libx32gomp1 libx32itm1 libx32quadmath0
  libx32stdc++-5-dev libx32stdc++6 libx32ubsan0 rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs rocm-opencl rocm-opencl-dev
  rocm-smi rocm-utils rocminfo rocr_debug_agent
Suggested packages:
  lib32stdc++6-5-dbg libx32stdc++6-5-dbg
The following NEW packages will be installed:
  comgr dkms g++-5-multilib g++-multilib gcc-5-multilib gcc-multilib hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile
  hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev lib32asan2 lib32atomic1 lib32cilkrts5 lib32gcc-5-dev lib32gcc1
  lib32gomp1 lib32itm1 lib32mpx0 lib32quadmath0 lib32stdc++-5-dev lib32stdc++6 lib32ubsan0 libc6-dev-i386 libc6-dev-x32 libc6-i386
  libc6-x32 libx32asan2 libx32atomic1 libx32cilkrts5 libx32gcc-5-dev libx32gcc1 libx32gomp1 libx32itm1 libx32quadmath0
  libx32stdc++-5-dev libx32stdc++6 libx32ubsan0 rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs rocm-dkms rocm-opencl
  rocm-opencl-dev rocm-smi rocm-utils rocminfo rocr_debug_agent
0 upgraded, 54 newly installed, 0 to remove and 0 not upgraded.
Need to get 422 MB of archives.
After this operation, 1976 MB of additional disk space will be used.
Get:1 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 dkms all 2.2.0.3-2ubuntu11.5 [66.3 kB]
Get:2 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libc6-i386 amd64 2.23-0ubuntu10 [2336 kB]
Get:3 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libc6-dev-i386 amd64 2.23-0ubuntu10 [1262 kB]
Get:4 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libc6-x32 amd64 2.23-0ubuntu10 [2559 kB]
Get:5 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libc6-dev-x32 amd64 2.23-0ubuntu10 [1559 kB]
Get:6 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 comgr amd64 0.0.0 [28.9 MB]
Get:7 http://tw.archive.ubuntu.com/ubuntu xenial/main amd64 lib32gcc1 amd64 1:6.0.1-0ubuntu1 [46.6 kB]
Get:8 http://tw.archive.ubuntu.com/ubuntu xenial/main amd64 libx32gcc1 amd64 1:6.0.1-0ubuntu1 [38.7 kB]
Get:9 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32gomp1 amd64 5.4.0-6ubuntu1~16.04.10 [59.7 kB]
Get:10 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32gomp1 amd64 5.4.0-6ubuntu1~16.04.10 [55.4 kB]
Get:11 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32itm1 amd64 5.4.0-6ubuntu1~16.04.10 [29.6 kB]
Get:12 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32itm1 amd64 5.4.0-6ubuntu1~16.04.10 [27.7 kB]
Get:13 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32atomic1 amd64 5.4.0-6ubuntu1~16.04.10 [8640 B]
Get:14 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32atomic1 amd64 5.4.0-6ubuntu1~16.04.10 [8904 B]
Get:15 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32asan2 amd64 5.4.0-6ubuntu1~16.04.10 [260 kB]
Get:16 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32asan2 amd64 5.4.0-6ubuntu1~16.04.10 [253 kB]
Get:17 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32stdc++6 amd64 5.4.0-6ubuntu1~16.04.10 [404 kB]
Get:18 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32ubsan0 amd64 5.4.0-6ubuntu1~16.04.10 [105 kB]
Get:19 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32stdc++6 amd64 5.4.0-6ubuntu1~16.04.10 [384 kB]
Get:20 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32ubsan0 amd64 5.4.0-6ubuntu1~16.04.10 [97.0 kB]
Get:21 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32cilkrts5 amd64 5.4.0-6ubuntu1~16.04.10 [44.8 kB]
Get:22 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32cilkrts5 amd64 5.4.0-6ubuntu1~16.04.10 [40.8 kB]
Get:23 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32mpx0 amd64 5.4.0-6ubuntu1~16.04.10 [11.1 kB]
Get:24 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32quadmath0 amd64 5.4.0-6ubuntu1~16.04.10 [203 kB]
Get:25 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32quadmath0 amd64 5.4.0-6ubuntu1~16.04.10 [134 kB]
Get:26 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32gcc-5-dev amd64 5.4.0-6ubuntu1~16.04.10 [2050 kB]
Get:27 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32gcc-5-dev amd64 5.4.0-6ubuntu1~16.04.10 [1867 kB]
Get:28 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 gcc-5-multilib amd64 5.4.0-6ubuntu1~16.04.10 [968 B]
Get:29 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 lib32stdc++-5-dev amd64 5.4.0-6ubuntu1~16.04.10 [637 kB]
Get:30 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx32stdc++-5-dev amd64 5.4.0-6ubuntu1~16.04.10 [609 kB]
Get:31 http://tw.archive.ubuntu.com/ubuntu xenial-updates/main amd64 g++-5-multilib amd64 5.4.0-6ubuntu1~16.04.10 [992 B]
Get:32 http://tw.archive.ubuntu.com/ubuntu xenial/main amd64 gcc-multilib amd64 4:5.3.1-1ubuntu1 [1212 B]
Get:33 http://tw.archive.ubuntu.com/ubuntu xenial/main amd64 g++-multilib amd64 4:5.3.1-1ubuntu1 [940 B]
Get:34 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-ext-rocr-dev amd64 1.1.9-8-g51c00c2 [1058 kB]
Get:35 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct amd64 1.0.9-8-g238782c [49.8 kB]
Get:36 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct-dev amd64 1.0.9-8-g238782c [23.6 kB]
Get:37 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-rocr-dev amd64 1.1.9-8-g51c00c2 [380 kB]
Get:38 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocminfo amd64 1.0.0 [18.4 kB]
Get:39 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl amd64 1.2.0-2018090737 [41.2 MB]
Get:40 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl-dev amd64 1.2.0-2018090737 [17.2 MB]
Get:41 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-clang-ocl amd64 0.3.0-7997136 [1554 B]
Get:42 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-utils amd64 1.9.211 [766 B]
Get:43 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hcc amd64 1.2.18354 [304 MB]
Get:44 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip_base amd64 1.5.18353 [260 kB]
Get:45 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip_doc amd64 1.5.18353 [679 kB]
Get:46 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip_hcc amd64 1.5.18353 [5337 kB]
Get:47 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip_samples amd64 1.5.18353 [64.6 kB]
Get:48 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-amd-aqlprofile amd64 1.0.0 [57.7 kB]
Get:49 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rock-dkms all 1.9-211 [5685 kB]
Get:50 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-device-libs amd64 0.0.1 [725 kB]
Get:51 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-smi amd64 1.0.0-72-gec1da05 [9852 B]
Get:52 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocr_debug_agent amd64 1.0.0 [716 kB]
Get:53 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dev amd64 1.9.211 [840 B]
Get:54 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dkms amd64 1.9.211 [1002 B]
Fetched 422 MB in 1min 9s (6049 kB/s)
Extracting templates from packages: 100%
Selecting previously unselected package comgr.
(Reading database ... 215510 files and directories currently installed.)
Preparing to unpack .../archives/comgr_0.0.0_amd64.deb ...
Unpacking comgr (0.0.0) ...
Selecting previously unselected package dkms.
Preparing to unpack .../dkms_2.2.0.3-2ubuntu11.5_all.deb ...
Unpacking dkms (2.2.0.3-2ubuntu11.5) ...
Selecting previously unselected package libc6-i386.
Preparing to unpack .../libc6-i386_2.23-0ubuntu10_amd64.deb ...
Unpacking libc6-i386 (2.23-0ubuntu10) ...
Selecting previously unselected package libc6-dev-i386.
Preparing to unpack .../libc6-dev-i386_2.23-0ubuntu10_amd64.deb ...
Unpacking libc6-dev-i386 (2.23-0ubuntu10) ...
Selecting previously unselected package libc6-x32.
Preparing to unpack .../libc6-x32_2.23-0ubuntu10_amd64.deb ...
Unpacking libc6-x32 (2.23-0ubuntu10) ...
Selecting previously unselected package libc6-dev-x32.
Preparing to unpack .../libc6-dev-x32_2.23-0ubuntu10_amd64.deb ...
Unpacking libc6-dev-x32 (2.23-0ubuntu10) ...
Selecting previously unselected package lib32gcc1.
Preparing to unpack .../lib32gcc1_1%3a6.0.1-0ubuntu1_amd64.deb ...
Unpacking lib32gcc1 (1:6.0.1-0ubuntu1) ...
Selecting previously unselected package libx32gcc1.
Preparing to unpack .../libx32gcc1_1%3a6.0.1-0ubuntu1_amd64.deb ...
Unpacking libx32gcc1 (1:6.0.1-0ubuntu1) ...
Selecting previously unselected package lib32gomp1.
Preparing to unpack .../lib32gomp1_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32gomp1 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32gomp1.
Preparing to unpack .../libx32gomp1_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32gomp1 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32itm1.
Preparing to unpack .../lib32itm1_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32itm1 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32itm1.
Preparing to unpack .../libx32itm1_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32itm1 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32atomic1.
Preparing to unpack .../lib32atomic1_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32atomic1 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32atomic1.
Preparing to unpack .../libx32atomic1_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32atomic1 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32asan2.
Preparing to unpack .../lib32asan2_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32asan2 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32asan2.
Preparing to unpack .../libx32asan2_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32asan2 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32stdc++6.
Preparing to unpack .../lib32stdc++6_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32stdc++6 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32ubsan0.
Preparing to unpack .../lib32ubsan0_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32ubsan0 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32stdc++6.
Preparing to unpack .../libx32stdc++6_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32stdc++6 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32ubsan0.
Preparing to unpack .../libx32ubsan0_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32ubsan0 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32cilkrts5.
Preparing to unpack .../lib32cilkrts5_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32cilkrts5 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32cilkrts5.
Preparing to unpack .../libx32cilkrts5_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32cilkrts5 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32mpx0.
Preparing to unpack .../lib32mpx0_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32mpx0 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32quadmath0.
Preparing to unpack .../lib32quadmath0_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32quadmath0 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32quadmath0.
Preparing to unpack .../libx32quadmath0_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32quadmath0 (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32gcc-5-dev.
Preparing to unpack .../lib32gcc-5-dev_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32gcc-5-dev (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32gcc-5-dev.
Preparing to unpack .../libx32gcc-5-dev_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32gcc-5-dev (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package gcc-5-multilib.
Preparing to unpack .../gcc-5-multilib_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking gcc-5-multilib (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package lib32stdc++-5-dev.
Preparing to unpack .../lib32stdc++-5-dev_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking lib32stdc++-5-dev (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package libx32stdc++-5-dev.
Preparing to unpack .../libx32stdc++-5-dev_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking libx32stdc++-5-dev (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package g++-5-multilib.
Preparing to unpack .../g++-5-multilib_5.4.0-6ubuntu1~16.04.10_amd64.deb ...
Unpacking g++-5-multilib (5.4.0-6ubuntu1~16.04.10) ...
Selecting previously unselected package gcc-multilib.
Preparing to unpack .../gcc-multilib_4%3a5.3.1-1ubuntu1_amd64.deb ...
Unpacking gcc-multilib (4:5.3.1-1ubuntu1) ...
Selecting previously unselected package g++-multilib.
Preparing to unpack .../g++-multilib_4%3a5.3.1-1ubuntu1_amd64.deb ...
Unpacking g++-multilib (4:5.3.1-1ubuntu1) ...
Selecting previously unselected package hsa-ext-rocr-dev.
Preparing to unpack .../hsa-ext-rocr-dev_1.1.9-8-g51c00c2_amd64.deb ...
Unpacking hsa-ext-rocr-dev (1.1.9-8-g51c00c2) ...
Selecting previously unselected package hsakmt-roct.
Preparing to unpack .../hsakmt-roct_1.0.9-8-g238782c_amd64.deb ...
Unpacking hsakmt-roct (1.0.9-8-g238782c) ...
Selecting previously unselected package hsakmt-roct-dev.
Preparing to unpack .../hsakmt-roct-dev_1.0.9-8-g238782c_amd64.deb ...
Unpacking hsakmt-roct-dev (1.0.9-8-g238782c) ...
Selecting previously unselected package hsa-rocr-dev.
Preparing to unpack .../hsa-rocr-dev_1.1.9-8-g51c00c2_amd64.deb ...
Unpacking hsa-rocr-dev (1.1.9-8-g51c00c2) ...
Selecting previously unselected package rocminfo.
Preparing to unpack .../rocminfo_1.0.0_amd64.deb ...
Unpacking rocminfo (1.0.0) ...
Selecting previously unselected package rocm-opencl.
Preparing to unpack .../rocm-opencl_1.2.0-2018090737_amd64.deb ...
Unpacking rocm-opencl (1.2.0-2018090737) ...
Selecting previously unselected package rocm-opencl-dev.
Preparing to unpack .../rocm-opencl-dev_1.2.0-2018090737_amd64.deb ...
Unpacking rocm-opencl-dev (1.2.0-2018090737) ...
Selecting previously unselected package rocm-clang-ocl.
Preparing to unpack .../rocm-clang-ocl_0.3.0-7997136_amd64.deb ...
Unpacking rocm-clang-ocl (0.3.0-7997136) ...
Selecting previously unselected package rocm-utils.
Preparing to unpack .../rocm-utils_1.9.211_amd64.deb ...
Unpacking rocm-utils (1.9.211) ...
Selecting previously unselected package hcc.
Preparing to unpack .../hcc_1.2.18354_amd64.deb ...
Unpacking hcc (1.2.18354) ...
Selecting previously unselected package hip_base.
Preparing to unpack .../hip%5fbase_1.5.18353_amd64.deb ...
Unpacking hip_base (1.5.18353) ...
Selecting previously unselected package hip_doc.
Preparing to unpack .../hip%5fdoc_1.5.18353_amd64.deb ...
Unpacking hip_doc (1.5.18353) ...
Selecting previously unselected package hip_hcc.
Preparing to unpack .../hip%5fhcc_1.5.18353_amd64.deb ...
Unpacking hip_hcc (1.5.18353) ...
Selecting previously unselected package hip_samples.
Preparing to unpack .../hip%5fsamples_1.5.18353_amd64.deb ...
Unpacking hip_samples (1.5.18353) ...
Selecting previously unselected package hsa-amd-aqlprofile.
Preparing to unpack .../hsa-amd-aqlprofile_1.0.0_amd64.deb ...
Unpacking hsa-amd-aqlprofile (1.0.0) ...
Selecting previously unselected package rock-dkms.
Preparing to unpack .../rock-dkms_1.9-211_all.deb ...
Unpacking rock-dkms (1.9-211) ...
Selecting previously unselected package rocm-device-libs.
Preparing to unpack .../rocm-device-libs_0.0.1_amd64.deb ...
Unpacking rocm-device-libs (0.0.1) ...
Selecting previously unselected package rocm-smi.
Preparing to unpack .../rocm-smi_1.0.0-72-gec1da05_amd64.deb ...
Unpacking rocm-smi (1.0.0-72-gec1da05) ...
Selecting previously unselected package rocr_debug_agent.
Preparing to unpack .../rocr%5fdebug%5fagent_1.0.0_amd64.deb ...
Unpacking rocr_debug_agent (1.0.0) ...
Selecting previously unselected package rocm-dev.
Preparing to unpack .../rocm-dev_1.9.211_amd64.deb ...
Unpacking rocm-dev (1.9.211) ...
Selecting previously unselected package rocm-dkms.
Preparing to unpack .../rocm-dkms_1.9.211_amd64.deb ...
Unpacking rocm-dkms (1.9.211) ...
Processing triggers for man-db (2.7.5-1) ...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Setting up comgr (0.0.0) ...
Setting up dkms (2.2.0.3-2ubuntu11.5) ...
Setting up libc6-i386 (2.23-0ubuntu10) ...
Setting up libc6-dev-i386 (2.23-0ubuntu10) ...
Setting up libc6-x32 (2.23-0ubuntu10) ...
Setting up libc6-dev-x32 (2.23-0ubuntu10) ...
Setting up lib32gcc1 (1:6.0.1-0ubuntu1) ...
Setting up libx32gcc1 (1:6.0.1-0ubuntu1) ...
Setting up lib32gomp1 (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32gomp1 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32itm1 (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32itm1 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32atomic1 (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32atomic1 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32asan2 (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32asan2 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32stdc++6 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32ubsan0 (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32stdc++6 (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32ubsan0 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32cilkrts5 (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32cilkrts5 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32mpx0 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32quadmath0 (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32quadmath0 (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32gcc-5-dev (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32gcc-5-dev (5.4.0-6ubuntu1~16.04.10) ...
Setting up gcc-5-multilib (5.4.0-6ubuntu1~16.04.10) ...
Setting up lib32stdc++-5-dev (5.4.0-6ubuntu1~16.04.10) ...
Setting up libx32stdc++-5-dev (5.4.0-6ubuntu1~16.04.10) ...
Setting up g++-5-multilib (5.4.0-6ubuntu1~16.04.10) ...
Setting up gcc-multilib (4:5.3.1-1ubuntu1) ...
Setting up g++-multilib (4:5.3.1-1ubuntu1) ...
Setting up hsa-ext-rocr-dev (1.1.9-8-g51c00c2) ...
Setting up hsakmt-roct (1.0.9-8-g238782c) ...
Setting up hsakmt-roct-dev (1.0.9-8-g238782c) ...
Setting up hsa-rocr-dev (1.1.9-8-g51c00c2) ...
Setting up rocminfo (1.0.0) ...
Setting up rocm-opencl (1.2.0-2018090737) ...
Setting up rocm-opencl-dev (1.2.0-2018090737) ...
Setting up rocm-clang-ocl (0.3.0-7997136) ...
Setting up rocm-utils (1.9.211) ...
Setting up hcc (1.2.18354) ...
Setting up hip_base (1.5.18353) ...
Setting up hip_doc (1.5.18353) ...
Setting up hip_hcc (1.5.18353) ...
Setting up hip_samples (1.5.18353) ...
Setting up hsa-amd-aqlprofile (1.0.0) ...
Setting up rock-dkms (1.9-211) ...
Loading new amdgpu-1.9-211 DKMS files...
First Installation: checking all kernels...
Building only for 4.15.0-34-generic
Building for architecture x86_64
Building initial module for 4.15.0-34-generic
Done.
Forcing installation of amdgpu

amdgpu:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amdttm.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amdkcl.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amdchash.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amd-sched.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amdkfd.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

Running the post_install script:
update-initramfs: Generating /boot/initrd.img-4.15.0-34-generic

depmod....

Backing up initrd.img-4.15.0-34-generic to /boot/initrd.img-4.15.0-34-generic.old-dkms
Making new initrd.img-4.15.0-34-generic
(If next boot fails, revert to initrd.img-4.15.0-34-generic.old-dkms image)
update-initramfs....

DKMS: install completed.
Setting up rocm-device-libs (0.0.1) ...
Setting up rocm-smi (1.0.0-72-gec1da05) ...
Setting up rocr_debug_agent (1.0.0) ...
Setting up rocm-dev (1.9.211) ...
Setting up rocm-dkms (1.9.211) ...
KERNEL=="kfd", MODE="0666"
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for initramfs-tools (0.122ubuntu8.12) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-34-generic
W: Possible missing firmware /lib/firmware/amdgpu/vega12_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_asd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sos.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_smc.bin for module amdgpu
Processing triggers for shim-signed (1.33.1~16.04.1+13-0ubuntu2) ...
Secure Boot not enabled on this system.

$ groups
horry adm cdrom sudo dip plugdev lpadmin sambashare

$ sudo usermod -a -G video $LOGNAME

$ echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
ADD_EXTRA_GROUPS=1

$ echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
EXTRA_GROUPS=video
```


```
> `$ groups
horry adm cdrom sudo dip video plugdev lpadmin sambashare

$ uname -r
4.15.0-34-generic 

$ dkms status
amdgpu, 1.9-211, 4.15.0-34-generic, x86_64: installed

$ modinfo amdgpu | grep filename
filename:       /lib/modules/4.15.0-34-generic/updates/dkms/amdgpu.ko

$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-34-generic/updates/dkms/amdkfd.ko

$ dmesg | grep kfd
[    1.625730] kfd kfd: Initialized module
[    1.626379] kfd kfd: skipped device 1002:67df, PCI rejects atomics

$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-34-generic (buildd@lgw01-amd64-037) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)) #37~16.04.1-Ubuntu SMP Tue Aug 28 10:44:06 UTC 2018 (Ubuntu 4.15.0-34.37~16.04.1-generic 4.15.18)
[    1.510995] amdkcl: loading out-of-tree module taints kernel.
[    1.511015] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    1.620238] [drm] amdgpu kernel modesetting enabled.
[    1.620239] [drm] amdgpu version: 18.30.2.15
[    1.626019] fb: switching to amdgpudrmfb from EFI VGA
[    1.626566] amdgpu 0000:02:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.626644] amdgpu 0000:02:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[    1.626646] amdgpu 0000:02:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    1.626763] [drm] amdgpu: 8192M of VRAM memory ready
[    1.626764] [drm] amdgpu: 15955M of GTT memory ready.
[    1.835454] fbcon: amdgpudrmfb (fb0) is primary device
[    1.835526] amdgpu 0000:02:00.0: fb0: amdgpudrmfb frame buffer device
`
```

---

### 评论 #6 — jlgreathouse (2018-09-27T02:29:56Z)

Could you reboot your system and please show me the outputs requested in my previous response? Thank you.

---

### 评论 #7 — tom21tom21 (2018-09-27T02:46:54Z)

> Could you reboot your system and please show me the outputs requested in my previous response? Thank you.

I already rebooted and add up some the response.

---

### 评论 #8 — jlgreathouse (2018-09-27T02:53:22Z)

Hi @tom21tom21 

The following identifies your problem:
```$ dmesg | grep kfd
[    1.625730] kfd kfd: Initialized module
[    1.626379] kfd kfd: skipped device 1002:67df, PCI rejects atomics
```

Your combination of CPU and GPU [are not supported in ROCm](https://rocm.github.io/hardware.html). Your GPU device, a gfx8 "Polaris 10" Radeon RX 580, requires a CPU that supports PCIe atomics. As discussed on our hardware page, if you want to use a Xeon CPU, this will require a Xeon "v3" or newer (Haswell). Your Xeon E5 2670 v2 apparently does not support PCIe atomics.

Perhaps there is an option in your BIOS to enable this. But as your system is currently configured, our drivers are unable to use PCIe atomics in the way they need. As such, your GPU will not work under ROCm in this system configuration.

---

### 评论 #9 — tom21tom21 (2018-09-27T02:55:00Z)

Thank you I will change the other CPU to test.

---

### 评论 #10 — rumatadest (2018-09-27T11:05:02Z)

Under Linux, most AMD cards are currently used for mining. The standard configuration of a mining rig is a computer with a low end CPU like Celeron. With 4-10 GPUs are connected through $3 Chinese risers PCI-E 1x from aliexpress
In this configuration, there can be no support for "PCIe atomics"

In the end, I have to use three versions of the drivers and OS
- kernel 4,15 and amdgpu-pro 17,50 working fine RX 5хх series without any "supports PCIe atomics." but it ugly Power Control and no Vega support
- kernel 4,15 and amdgpu-pro 18,30 - support Vega, but hashrate is lower than windows about 40%
- kernel 4,15 and ROCm 1.9.211 - no PowerControl for Vega and no support RX 5хх/Vega without PCIe atomics
- kernel 4.18 - good PowerControl but rocm-dkms is compiled with an error
- Windows does not have problems with the drivers, but it is very difficult to administer. It is freeze twice a day


---

### 评论 #11 — gstoner (2018-09-27T13:42:03Z)

@rumatadest 
       
You only have two drivers in Linux not three for compute.  AMDGPUpro and ROCm

Again ROCm was designed for different use case then you trying to do, Radio Astronomy, HPC and Deep Learning were it primary market focus when it was conceived,   Coin Minning on GPU was not a real market then.   We had some very advanced hardware that never shipped it was designed to address. 

AMDGPUpro will move forward as the driver that runs everywhere and run with the lowest common denominator system and support broadest number CPU and GPU,  it will get Most of the language runtime which runs on ROCm via PAL base user mode runtime and Kernel Mode packet submission.  Note as of 18.20 for Vega10  it uses the same OpenCL Compilers runtime via PAL layer as Windows. It has always used the same  OpenCL Compiler and Language Runtime as windows for GFX8  and Older GPU's    If you having a performance issue  Between windows and 18.30 AMDGPUpro it not OpenCL issue it in the base Linux driver. 

ROCm Enterprise driver is targeted at the. NVIDIA Tesla market, supporting  Radeon Instinct product family of hardware,  we support other GPU asics as well for the community to get access to the advanced Software feature it offers.  

On PCIe Atomics,  we have a mode for Vega10 that shuts of PCIe atomics,  we looking make sure there is fall back path for those who do not really care about I/O performance or Queue Submission overheads,  which is your use case.   To do this we have to do Firmware changes, this harder for older hardware which the firmware engineering team are more hesitant to touch.  On ROCm for Future hardware release, we have a fallback path. 

4.18 just came out, Aug 30th   I understand it has the feature you want, right now with ROCm 1.9 you can use it with new changes in the Thunk, but understand it takes time to integrate with the bigger stack flow it out in a formal driver release




---

### 评论 #12 — jlgreathouse (2018-09-27T16:33:53Z)

Hi @rumatadest 

To give a bit more info -- ROCm 1.9.0 supports Linux 4.15 (in particular, Ubuntu 16.04 LTS and 18.04 LTS; the most recent versions of these distributions base their HWE kernel on 4.15). We do support Vega 10 GPUs in ROCm 1.8 and 1.9 on systems without PCIe atomics. In ROCm 1.8 we required you to manually set the environment variable HSA_ENABLE_SDMA=0 to avoid the requirement for PCIe atomics; this is no longer the case in ROCm 1.9.

You are right, however, that GPUs in the gfx8 line, includ Radeon RX 5xx GPUs ("Polaris 10", "Polaris 11") do still require PCIe atomics. You can read more information about these requirements in #451.

If you are running kernel 4.18, you do not need to install the full `rocm-dkms` package to get ROCm software working. As of 4.16 (pre-Vega) and 4.17 (including Vega 10 support), a working version of the ROCK drivers are available in the upstream kernel. As such, you can, if you so choose, skip installing rock-dkms, which is one of the dependencies of rocm-dkms. See [this post](https://github.com/RadeonOpenCompute/ROCm/issues/513#issuecomment-421643966), where I link to directions on Phoronix that show a user getting the ROCm user-level software working on the base 4.18 kernel.

We are aware that the ROCm 1.9.0 rock-dkms package won't build on newer kernels. However, AMD's custom ROCm drivers available as part of ROCm 1.9.0 are only supported on RHEL/CentOS 7.4 and 7.5, and on Ubuntu 16.04 LTS and Ubuntu 18.04 LTS. As such, we do not guarantee that they will work on newer kernels that are not officially supported on these distros. For newer kernels, however, you should be able to use the upstream drivers with our user-land software.

---

### 评论 #13 — jlgreathouse (2018-09-27T16:34:54Z)

Hi @tom21tom21

Since the underlying problem reported in this issue is an unsupported CPU+GPU combination, I'm going to close this ticket. If you install a newer CPU and still run into problems, please feel free to open another ticket. Thanks!

---

### 评论 #14 — rumatadest (2018-09-27T16:57:02Z)

Thanks for your reply
Waiting for the ebuilds ))

Wishes.
Is it possible to create a test repository with "nightly builds"? Not every person can compile the latest version of the ROCM from the thunk. This can speed up the process of testing new features.

---

### 评论 #15 — jlgreathouse (2018-09-27T17:19:45Z)

Hi @rumatadest 

That's a good request. I don't know if would be able to do "nightly" builds (our internal nightly builds may contain code that we do not wish to release to the public, such as information about new hardware that we have not released). That said, we can try to explore the possibility of unofficial/testing channels. I can't make any promises about this, but thank you for the request.

---
