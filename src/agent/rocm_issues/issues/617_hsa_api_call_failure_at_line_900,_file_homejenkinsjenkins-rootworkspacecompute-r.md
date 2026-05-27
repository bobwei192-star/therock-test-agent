# hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104

> **Issue #617**
> **状态**: closed
> **创建时间**: 2018-11-19T07:28:08Z
> **更新时间**: 2019-03-11T04:19:48Z
> **关闭时间**: 2019-03-11T04:19:47Z
> **作者**: mythreyi22
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/617

## 描述

I've tried most of the solution suggestions from similar issues, but it doesn't seem to resolve this issue. 
Btw, the error is not stable. /opt/rocm/bin/rocminfo works at times. 

Details: 
Vega, Ubuntu 16.04

dkms status
amdgpu, 1.9-224, 4.15.0-38-generic, x86_64: installed
amdgpu, 1.9-224, 4.15.0-39-generic, x86_64: installed

uname -a
Linux All-Series 4.15.0-39-generic #42~16.04.1-Ubuntu SMP Wed Oct 24 17:09:54 UTC 2018 x86_64 x86_64 x86_64



---

## 评论 (22 条)

### 评论 #1 — jlgreathouse (2018-11-19T16:48:46Z)

- What is the output of `groups`?
- When this error happens, what is the output of `dmesg | grep kfd`?
- What model of "Vega" GPU do you have?
- What CPU do you have?

---

### 评论 #2 — mythreyi22 (2018-11-20T08:20:35Z)

groups : adm cdrom sudo dip video plugdev lpadmin sambashare
```
$ dmesg | grep kfd
[ 7083.758053] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7083.758091] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7083.758337]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7083.758343]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7088.762089] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7088.762130] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7088.762378]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7088.762386]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7093.766083] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7093.766122] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7093.766378]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7093.766384]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7169.480839] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7169.480881] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7169.481009]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7169.481015]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7169.511342] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7169.511380] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7169.511654]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7169.511659]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7169.541939] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7169.541978] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7169.542248]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7169.542254]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7169.572549] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7169.572588] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7169.572862]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7169.572868]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7169.603169] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7169.603207] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7169.603477]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7169.603483]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7169.633793] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7169.633830] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7169.634092]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7169.634097]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7169.664379] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7169.664415] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7169.664677]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7169.664683]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7174.690281] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7174.690318] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7174.690548]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7174.690553]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7179.714287] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7179.714324] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7179.714560]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7179.714565]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7184.718296] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7184.718333] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7184.718581]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7184.718587]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7189.722296] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7189.722332] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7189.722576]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7189.722581]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7194.726298] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7194.726333] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7194.726578]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7194.726584]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7270.445159] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7270.445200] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7270.445332]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7270.445338]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7270.475658] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7270.475697] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7270.475997]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7270.476003]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7270.506296] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7270.506336] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7270.506619]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7270.506625]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7270.536912] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7270.536949] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7270.537230]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7270.537236]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7270.567516] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7270.567554] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7270.567829]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7270.567835]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7270.598118] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7270.598156] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7270.598437]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7270.598442]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7270.628726] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7270.628764] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7270.629041]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7270.629047]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7275.654449] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7275.654488] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7275.654755]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7275.654761]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7280.682448] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7280.682488] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7280.682733]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7280.682738]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7285.686456] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7285.686495] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7285.686739]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7285.686745]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7290.690453] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7290.690490] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7290.690751]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7290.690757]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7295.694472] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7295.694510] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7295.694767]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7295.694773]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7371.413328] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7371.413367] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7371.413488]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7371.413494]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7371.443893] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7371.443930] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7371.444211]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7371.444216]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7371.474715] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7371.474750] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7371.475020]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7371.475025]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7371.505415] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7371.505450] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7371.505721]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7371.505726]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7371.536122] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7371.536158] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7371.536406]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7371.536412]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7371.566793] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7371.566829] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7371.567079]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7371.567085]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7371.597442] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7371.597477] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7371.597725]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7371.597730]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7376.618589] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7376.618626] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7376.618925]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7376.618931]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7381.642601] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7381.642638] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7381.642884]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7381.642889]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7386.646600] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7386.646637] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7386.646882]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7386.646887]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7391.650603] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7391.650639] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7391.650884]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7391.650889]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7396.654615] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7396.654650] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7396.654887]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7396.654892]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7472.368597] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7472.368637] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7472.368768]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7472.368774]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7472.399095] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7472.399133] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7472.399406]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7472.399411]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7472.429686] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7472.429723] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7472.430003]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7472.430009]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7472.460288] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7472.460327] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7472.460619]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7472.460625]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7472.490905] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7472.490944] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7472.491220]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7472.491226]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7472.521503] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7472.521541] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7472.521811]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7472.521817]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7472.552110] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7472.552148] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7472.552424]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7472.552429]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7477.578681] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7477.578720] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7477.578981]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7477.578986]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7482.602702] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7482.602742] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7482.602994]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7482.603000]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7487.606700] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7487.606740] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7487.607007]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7487.607013]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7492.610712] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7492.610752] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7492.611007]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7492.611013]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7497.614697] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7497.614736] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7497.615000]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7497.615006]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7573.339429] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7573.339466] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7573.339581]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7573.339586]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7573.369993] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7573.370027] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7573.370282]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7573.370287]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7573.400836] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7573.400871] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7573.401136]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7573.401141]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7573.431536] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7573.431571] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7573.431844]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7573.431849]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7573.462204] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7573.462239] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7573.462515]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7573.462520]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7573.492911] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7573.492945] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7573.493206]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7573.493212]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7573.523595] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7573.523630] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7573.523931]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7573.523936]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7578.546802] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7578.546839] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7578.547069]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7578.547074]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7583.570798] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7583.570833] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7583.571059]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7583.571064]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7588.574783] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7588.574817] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7588.575061]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7588.575066]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7593.578778] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7593.578812] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7593.579036]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
[ 7593.579041]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
[ 7598.582778] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
[ 7598.582813] Workqueue: events kfd_process_hw_exception [amdkfd]
[ 7598.583035]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
```
Vega :  Xeon E3-1200 v3/4th Gen Core
CPU : Haswell i5-4440


---

### 评论 #3 — mythreyi22 (2018-11-21T12:23:56Z)

Any idea what could be the reason?

---

### 评论 #4 — Johnreidsilver (2018-11-22T11:34:37Z)

I had the same error and solved with a clean install.

---

### 评论 #5 — maxcr (2018-11-25T15:30:38Z)

> I had the same error and solved with a clean install.

yikes....

I fixed it by adding AMDKFD before AMDGPU in initramfs. Pretty easy fix...

---

### 评论 #6 — jlgreathouse (2018-11-27T06:11:48Z)

@mythreyi22 I'm not sure what you mean by "Vega : Xeon E3-1200 v3/4th Gen Core CPU : Haswell i5-4440". What GPU model do you have? And is your CPU an i5-4400 or a Xeon?

In addition, could you show me that `dmesg | grep kfd` output soon after a reboot? It appears that your kernel log is truncated because it has a number of messages filling it. I am looking to see what the KFD is printing when it's coming up.

In addition, how did you install ROCm? Using apt? Or from the .deb files? Or manually, from source?

When you say that rocminfo works "sometimes" does this mean across boots, within the same boot, or otherwise? For instance, after you have booted the system, will you go from working -> not working? Will it then (within the same boot) go from not working -> working?

---

### 评论 #7 — mythreyi22 (2018-11-27T10:09:47Z)

Adding AMDKFD before AMDGPU in initramfs worked. Thank you!

---

### 评论 #8 — mythreyi22 (2018-12-03T07:35:00Z)

Hello,
I am facing the same problem again. 

GPU model : Xeon E3-1200 v3/4th Gen Core Processor Integrated Graphics Controller
CPU model is i5-4400
I installed ROCm using apt.
It works for a while after reboot. Then crashes. 

Please find the attachment for dmesg | grep kfd

[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/2638555/dmesg.txt)


---

### 评论 #9 — mythreyi22 (2018-12-05T06:57:36Z)

1] GPU model : RX Vega 64 gfx900

- lspci | grep VGA
00:02.0 VGA compatible controller: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor Integrated Graphics Controller (rev 06)
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev ff)

- clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (2679.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  2679.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         Device 687f
  Device Topology (AMD)                           PCI-E, 03:00.0
  Max compute units                               64
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1630MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     None
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size multiple              64
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
    Correctly-rounded divide and sqrt operations  No
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
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              8573157376 (7.984GiB)
  Global free memory (AMD)                        8370176 (7.982GiB)
  Global memory channels (AMD)                    64
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7287183769 (6.787GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26751
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        7287183769 (6.787GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Thu Jan  1 05:30:00 1970)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.8
  ICD loader Profile                              OpenCL 1.2
	NOTE:	your OpenCL library declares to support OpenCL 1.2,
		but it seems to support up to OpenCL 2.1 too.

2]CPU model : i5-4400

3] After reboot : dmesg | grep kfd 
[    1.318163] kfd kfd: Initialized module
[    3.222096] kfd kfd: Allocated 3969056 bytes on gart
[    3.222251] kfd kfd: added device 1002:687f

4] I installed ROCm using apt.

5] It works across boot. Every time after rebooting, it works for a while.
**Rocminfo after reboot :** 

HSA System Attributes    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

           
HSA Agents               
         
                 
Agent 1                  
                
  Name:                    Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):3300                               
  BDFID:                   0                                  
  Compute Unit:            4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16299332KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16299332KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
               
Agent 2                  
           
  Name:                    gfx900                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 26751                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1630                               
  BDFID:                   768                                
  Compute Unit:            64                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  50332672                           
    Dim[2]:                  0                                  
  Grid Max Size:           4294967295                         
  Waves Per CU:            40                                 
  Max Work-item Per CU:    2560                               
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                         
    Dim[1]:                  4294967295                         
    Dim[2]:                  4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64KB                               
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Dimension: 
        Dim[0]:                  67109888                           
        Dim[1]:                  1024                               
        Dim[2]:                  16777217                           
      Workgroup Max Size:      1024                               
      Grid Max Dimension:      
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      Grid Max Size:           4294967295                         
      FBarrier Max Size:       32                                 
*** Done *** 


**After rocminfo fails,**
- clinfo
Number of platforms                               0

Thank you!

---

### 评论 #10 — Tomhauscz (2019-01-28T14:14:53Z)

Hi all,
I have installed the ROCm in the way that is described in the manual, but I had to include firmware for AMD GPUs to /lib/firmware/amdgpu from https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/amdgpu

I have done it and thought that /opt/rocm/bin/rocminfo will not crash, but still the same.
After some resaerching I found this article and realized that I have maybe the wrong kernel, but I have kernel 4.15.0-43-generic and it is in recommended range (4.13 - 4.17).

mythreyi22 wrote that AMDKFD should be before AMDGPU in initramfs.
After some digging in modules order i found this:
```
tomhaus@Tomhaus-ThinkPad-E580:/lib/modules/4.15.0-43-generic$ cat modules.order | grep amdgpu --line-number
985:kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko
tomhaus@Tomhaus-ThinkPad-E580:/lib/modules/4.15.0-43-generic$ cat modules.order | grep amdkfd --line-number
983:kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
```
Here you can see that AMDKFD is before AMDGPU, but the ROCm is still not working. Still the same error.

Here are some usefull informations:
    

- dmesg  (in file, the other file is command: `dmesg | grep -i amdgpu`) 
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/2803290/dmesg.txt)
[dmesg_with_modprobed_amdkfd.txt](https://github.com/RadeonOpenCompute/ROCm/files/2803302/dmesg_with_modprobed_amdkfd.txt)
- uname -r
        4.15.0-43-generic
- GPU:  AMD Radeon RX 550 Graphics, which seems supported by this ROCm
- lsmod | grep amd
[lsmod.txt](https://github.com/RadeonOpenCompute/ROCm/files/2803296/lsmod.txt)
- lspci | grep AMD
         02:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c0)


Thank you for your time solving this issue. ;)

Btw: I tried a lot of things about that, but I am stucked :D

---

### 评论 #11 — Tomhauscz (2019-02-10T10:41:08Z)

Please , help me solve this issue.

---

### 评论 #12 — seesturm (2019-02-10T12:33:30Z)

@Tomhauscz, I cannot help but only point out that it probably does not work due to
`[    2.949307] kfd kfd: skipped device 1002:699f, PCI rejects atomics`
seen in your dmesg.txt. Maybe consulting [ROCm supported cpus](https://github.com/RadeonOpenCompute/ROCm#supported-cpus) helps you.

---

### 评论 #13 — Tomhauscz (2019-02-10T22:47:48Z)

@seesturm, thank you for your reply.
I found that the problem is in chip controller that connects GPU to CPU, but I have i5 8250U and it also seems to be supported.

---

### 评论 #14 — Tomhauscz (2019-02-10T22:50:48Z)

I found in lspci that the 699f is ID of AMD GPU device

---

### 评论 #15 — karolski (2019-02-24T11:53:52Z)

I seem to have exact same issue, also in Thinkpad e580, with i7 8550.

---

### 评论 #16 — jlgreathouse (2019-03-08T15:58:52Z)

Hi @Tomhauscz 

Indeed, as @seesturm says, it appears that your GPU is not connected to your CPU through a path that enables PCIe atomics. As noted on [our hardware support list, ](https://rocm.github.io/hardware.html), gfx803 GPUs such as your Polaris 12 chip require a PCIe atomic path between the device GPU and the host CPU in order to properly work under ROCm.

While your CPU may support atomics, your system vendor may not have attached the GPU through a PCIe path that properly forwards those atomic operations between the CPU and GPU. If this is a laptop, I do not know if there is much you can do to fix this. @karolski if you are seeing the same "skipped device" message when you run `dmesg`, then you have the same issue.

---

### 评论 #17 — jlgreathouse (2019-03-08T16:05:52Z)

Hi @mythreyi22 

I am still unable to fathom why your GPU works "sometimes" and not "others. Are you still seeing the issue?

Are you taking any actions when the GPU starts working? For instance, running any particular applications? Or does it stop working after you let the system sit silently for some amount of time? How long does it take for this problem to happen? Can you show me a `dmesg` log *immediately* after you observe the problem?

---

### 评论 #18 — Tomhauscz (2019-03-08T16:34:20Z)

Thank you for your reply @jlgreathouse.
I thought that this problem is unsolvable. I can only wait until AMD releases some drivers that can support this type of connection, but it can also never be.

Thank you for your time solving this special type of problem and I wish you better solutions. ;)

---

### 评论 #19 — jlgreathouse (2019-03-08T17:11:53Z)

You should be able to use the amdgpu-pro drivers, though these will not enable all of the ROCm software.

---

### 评论 #20 — Tomhauscz (2019-03-08T21:03:29Z)

I know, I use it actually, because ubuntu does not have universal driver for this type of GPU. When I did not have amdgpu-pro driver, I have seen only black screen after booting. :D

---

### 评论 #21 — mythreyi22 (2019-03-11T04:10:20Z)

Hello @jlgreathouse, 
We replaced the GPU, facing no issues post that. But if I remember right, it stops working after you let the system sit silently for a while. Probably after 10 mins max. I already posted the dmesg log which I got after I observed the problem. 

> groups : adm cdrom sudo dip video plugdev lpadmin sambashare
> 
> ```
> $ dmesg | grep kfd
> [ 7083.758053] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7083.758091] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7083.758337]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7083.758343]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7088.762089] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7088.762130] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7088.762378]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7088.762386]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7093.766083] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7093.766122] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7093.766378]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7093.766384]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7169.480839] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7169.480881] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7169.481009]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7169.481015]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7169.511342] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7169.511380] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7169.511654]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7169.511659]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7169.541939] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7169.541978] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7169.542248]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7169.542254]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7169.572549] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7169.572588] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7169.572862]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7169.572868]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7169.603169] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7169.603207] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7169.603477]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7169.603483]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7169.633793] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7169.633830] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7169.634092]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7169.634097]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7169.664379] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7169.664415] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7169.664677]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7169.664683]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7174.690281] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7174.690318] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7174.690548]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7174.690553]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7179.714287] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7179.714324] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7179.714560]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7179.714565]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7184.718296] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7184.718333] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7184.718581]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7184.718587]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7189.722296] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7189.722332] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7189.722576]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7189.722581]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7194.726298] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7194.726333] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7194.726578]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7194.726584]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7270.445159] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7270.445200] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7270.445332]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7270.445338]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7270.475658] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7270.475697] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7270.475997]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7270.476003]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7270.506296] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7270.506336] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7270.506619]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7270.506625]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7270.536912] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7270.536949] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7270.537230]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7270.537236]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7270.567516] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7270.567554] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7270.567829]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7270.567835]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7270.598118] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7270.598156] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7270.598437]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7270.598442]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7270.628726] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7270.628764] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7270.629041]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7270.629047]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7275.654449] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7275.654488] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7275.654755]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7275.654761]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7280.682448] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7280.682488] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7280.682733]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7280.682738]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7285.686456] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7285.686495] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7285.686739]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7285.686745]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7290.690453] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7290.690490] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7290.690751]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7290.690757]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7295.694472] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7295.694510] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7295.694767]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7295.694773]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7371.413328] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7371.413367] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7371.413488]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7371.413494]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7371.443893] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7371.443930] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7371.444211]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7371.444216]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7371.474715] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7371.474750] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7371.475020]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7371.475025]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7371.505415] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7371.505450] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7371.505721]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7371.505726]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7371.536122] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7371.536158] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7371.536406]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7371.536412]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7371.566793] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7371.566829] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7371.567079]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7371.567085]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7371.597442] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7371.597477] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7371.597725]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7371.597730]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7376.618589] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7376.618626] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7376.618925]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7376.618931]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7381.642601] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7381.642638] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7381.642884]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7381.642889]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7386.646600] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7386.646637] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7386.646882]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7386.646887]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7391.650603] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7391.650639] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7391.650884]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7391.650889]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7396.654615] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7396.654650] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7396.654887]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7396.654892]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7472.368597] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7472.368637] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7472.368768]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7472.368774]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7472.399095] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7472.399133] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7472.399406]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7472.399411]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7472.429686] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7472.429723] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7472.430003]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7472.430009]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7472.460288] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7472.460327] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7472.460619]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7472.460625]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7472.490905] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7472.490944] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7472.491220]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7472.491226]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7472.521503] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7472.521541] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7472.521811]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7472.521817]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7472.552110] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7472.552148] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7472.552424]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7472.552429]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7477.578681] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7477.578720] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7477.578981]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7477.578986]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7482.602702] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7482.602742] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7482.602994]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7482.603000]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7487.606700] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7487.606740] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7487.607007]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7487.607013]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7492.610712] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7492.610752] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7492.611007]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7492.611013]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7497.614697] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7497.614736] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7497.615000]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7497.615006]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7573.339429] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7573.339466] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7573.339581]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7573.339586]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7573.369993] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7573.370027] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7573.370282]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7573.370287]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7573.400836] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7573.400871] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7573.401136]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7573.401141]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7573.431536] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7573.431571] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7573.431844]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7573.431849]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7573.462204] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7573.462239] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7573.462515]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7573.462520]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7573.492911] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7573.492945] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7573.493206]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7573.493212]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7573.523595] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7573.523630] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7573.523931]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7573.523936]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7578.546802] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7578.546839] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7578.547069]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7578.547074]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7583.570798] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7583.570833] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7583.571059]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7583.571064]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7588.574783] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7588.574817] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7588.575061]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7588.575066]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7593.578778] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7593.578812] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7593.579036]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> [ 7593.579041]  kfd_process_hw_exception+0x26/0x30 [amdkfd]
> [ 7598.582778] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic pcbc input_leds snd_hda_intel aesni_intel snd_hda_codec snd_seq_midi snd_seq_midi_event aes_x86_64 snd_hda_core snd_rawmidi snd_hwdep snd_pcm snd_seq snd_seq_device eeepc_wmi crypto_simd glue_helper cryptd snd_timer asus_wmi intel_cstate intel_rapl_perf wmi_bmof sparse_keymap mei_me snd lpc_ich shpchp acpi_pad soundcore mac_hid i2c_i801 mei binfmt_misc parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) i915 amdkcl(OE) i2c_algo_bit r8169 mxm_wmi drm_kms_helper mii syscopyarea sysfillrect sysimgblt fb_sys_fops
> [ 7598.582813] Workqueue: events kfd_process_hw_exception [amdkfd]
> [ 7598.583035]  amdgpu_amdkfd_gpu_reset+0x12/0x20 [amdgpu]
> ```
> 
> Vega : Xeon E3-1200 v3/4th Gen Core
> CPU : Haswell i5-4440



---

### 评论 #22 — jlgreathouse (2019-03-11T04:19:47Z)

My goal was see _a full dmesg log_ (not grepping for anything) _when the problem happens_ (not hours or days later, after the log has truncated due to log length limits).

That said, if replacing the GPU solved the problem, then we may be able to chalk this up to a defective piece of hardware.

---
