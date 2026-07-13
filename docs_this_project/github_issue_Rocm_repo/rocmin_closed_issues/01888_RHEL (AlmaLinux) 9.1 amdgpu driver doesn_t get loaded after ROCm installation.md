# RHEL (AlmaLinux) 9.1 amdgpu driver doesn't get loaded after ROCm installation

- **Issue #:** 1888
- **State:** closed
- **Created:** 2023-01-09T20:33:51Z
- **Updated:** 2024-05-09T19:19:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/1888

I installed ROCm but now, I am booting into a configuration with a very low screen resolution and without amdgpu driver at all I think:

As you can see below, without ROCm, amdgpu get's loaded, after installing ROCm, there's no driver active.

Without ROCm and kernel 9.0 and also when uninstalling ROCm from the kernel 9.1 setup I get:

]$ lsmod | grep -Ei 'amd|ati|radeon'

edac_mce_amd           45056  0
kvm_amd               147456  0
kvm                  1060864  1 kvm_amd
amd_pmc                28672  0
amdgpu               7393280  21
drm_ttm_helper         16384  1 amdgpu
ttm                    86016  2 amdgpu,drm_ttm_helper
iommu_v2               24576  1 amdgpu
gpu_sched              49152  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
drm_kms_helper        311296  1 amdgpu
drm                   634880  15 gpu_sched,drm_kms_helper,amdgpu,drm_ttm_helper,ttm
ccp                   114688  1 kvm_amd
amd_sfh                24576  0


With ROCm and kernel 9.1 I get:

]$ lsmod | grep -Ei 'amd|ati|radeon'

snd_sof_amd_renoir     16384  0
snd_sof_amd_acp        40960  1 snd_sof_amd_renoir
snd_sof_pci            24576  1 snd_sof_amd_renoir
snd_sof               196608  3 snd_sof_amd_acp,snd_sof_pci,snd_sof_amd_renoir
edac_mce_amd           45056  0
kvm_amd               155648  0
snd_pcm               151552  11 snd_sof_amd_acp,snd_hda_codec_hdmi,snd_pci_acp6x,snd_hda_intel,snd_hda_codec,snd_sof,snd_compress,snd_soc_core,snd_sof_utils,snd_hda_core,snd_acp3x_pdm_dma
kvm                  1105920  1 kvm_amd
snd_acp_config         16384  2 snd_rn_pci_acp3x,snd_sof_amd_renoir
snd_soc_acpi           16384  2 snd_acp_config,snd_sof_amd_renoir
amd_pmc                28672  0
ccp                   118784  1 kvm_amd
amd_sfh                32768  0

How should I address this issue?