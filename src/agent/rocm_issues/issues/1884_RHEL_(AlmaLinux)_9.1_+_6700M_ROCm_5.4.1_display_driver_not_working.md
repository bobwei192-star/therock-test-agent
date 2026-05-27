# RHEL (AlmaLinux) 9.1 + 6700M ROCm 5.4.1 display driver not working

> **Issue #1884**
> **状态**: closed
> **创建时间**: 2023-01-06T11:51:03Z
> **更新时间**: 2024-05-23T18:27:22Z
> **关闭时间**: 2024-05-23T18:27:22Z
> **作者**: klausbu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1884

## 描述

I have a notebook with a AMD Ryzen™ 9 5900HX CPU + 6700M GPU and want to implement rocALUTION in a CFD software and port another GPU application from cuda to HPI using rocThrust.

I installed ROCm 5.4.1 using the installer script:

Step 1:

RHEL v9.1

To download and install the installer for RHEL v9.1 distribution, type the following command:

sudo yum install https://repo.radeon.com/amdgpu-install/5.4.1/rhel/9.1/amdgpu-install-5.4.50401-1.el9.noarch.rpm  

Step 2:

sudo amdgpu-install --usecase=dkms,graphics,opencl,hip,rocm,hiplibsdk 


When rebooting, the display resolution is different and I get a message screen telling me, that something went wrong and that I should contact the system administrator. The boot process stops at that point.

Booting an old kernel (RHEL (AlmaLinux) 9.0), uninstalling ROCm and rebooting fixes the RHEL (AlmaLinux) 9.1 boot issue so I assume it's the display driver that's not installed properly when installing ROCm. 

Is there a known fix for that?

What usecases are actually needed to develop rocALUTION based applications running on the GPU and applications using rocThrust running on the GPU? dkms,graphics,opencl,hip,rocm,hiplibsdk is certainly overkill but I wanted to make sure I don't miss something.

---

## 评论 (6 条)

### 评论 #1 — klausbu (2023-01-09T20:25:19Z)

The install script method doesn't work for me as the installation breaks the boot process - the following 3 steps work better but then, not amdgpu driver gets loaded

Step 1 update the amdgpu.repo file using e.g the gnome editor gedit with the text below: sudo gedit /etc/yum.repos.d/amdgpu.repo

[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/latest/rhel/9.1/main/x86_64  
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key

Step 2 update the rocm.repo file using e.g the gnome editor gedit with the text below: sudo gedit /etc/yum.repos.d/rocm.repo
[rocm]
name=rocm
baseurl=https://repo.radeon.com/rocm/rhel9/rpm  
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key

Step 3 install the relevant ROCm packages, in my case:
sudo dnf install kernel-headers kernel-devel dkms amdgpu-dkms rocm-hip-sdk rocm-opencl-sdk 

With this, I can boot into a configuration with a low screen resolution but no amdgpu driver gets loaded but that's another story/issue.

---

### 评论 #2 — Mystro256 (2023-01-10T21:26:17Z)

Can you try running "dkms status" and give the output?

It sounds like it failed to compile for the 9.1 kernel, but is fine for 9.0.

---

### 评论 #3 — klausbu (2023-01-11T10:16:41Z)

in the meantime, I managed to fix the boot and screen resolution issue by reinstalling just amdgpu-dkms.  rocminfo shows all available devices but I can't run HIP programs on the GPU. 

I tried to run a rocAlution example which runs only on the CPU/OpenMP backend, HIP is not initialized. 

There is no output for dkms status. 

Could it be, that my NAVI22 --gfx1031 is still not "supported" or "enabled" to the extend, that I can write/compile HIP programs and I that need to compile it myself for target --gfx1031?  How about rocThrust which is the other library I need?

Maybe this is important, too:

]$ lsmod | grep -Ei 'amd|ati|radeon'

snd_sof_amd_renoir     16384  0
snd_sof_amd_acp        40960  1 snd_sof_amd_renoir
snd_sof_pci            24576  1 snd_sof_amd_renoir
snd_sof               196608  3 snd_sof_amd_acp,snd_sof_pci,snd_sof_amd_renoir
edac_mce_amd           45056  0
kvm_amd               155648  0
kvm                  1105920  1 kvm_amd
snd_pcm               151552  12 snd_sof_amd_acp,snd_hda_codec_hdmi,snd_pci_acp6x,snd_hda_intel,snd_usb_audio,snd_hda_codec,snd_sof,snd_compress,snd_soc_core,snd_sof_utils,snd_hda_core,snd_acp3x_pdm_dma
snd_acp_config         16384  2 snd_rn_pci_acp3x,snd_sof_amd_renoir
snd_soc_acpi           16384  2 snd_acp_config,snd_sof_amd_renoir
amd_pmc                28672  0
amdgpu               7856128  23
drm_ttm_helper         16384  1 amdgpu
ttm                    86016  2 amdgpu,drm_ttm_helper
iommu_v2               24576  1 amdgpu
gpu_sched              53248  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
drm_dp_helper         159744  1 amdgpu
drm_kms_helper        200704  5 drm_dp_helper,amdgpu
drm                   622592  16 gpu_sched,drm_dp_helper,drm_kms_helper,amdgpu,drm_ttm_helper,ttm
ccp                   118784  1 kvm_amd
amd_sfh                32768  0


---

### 评论 #4 — Mystro256 (2023-01-13T19:53:32Z)

So if you installed amdgpu-dkms, there should be at least some output from ```dkms status```, and based on the lsmod output, looks like the distro's driver modules are being used instead of an amdgpu-dkms built one. I'm not sure off the top of my head if the EL9.1 has inbox support for Navi22, so it's possible that you're falling back to the system kernel driver and the support you need is missing.

Can you confirm 100% that amdgpu-dkms is installed? You can query the package manager via ```rpm -q amdgpu-dkms``` or ```dnf list amdgpu-dkms``` (it should return a name and version string installed), and you can also check if the files in /usr/src/amdgpu-* exist.

If you used ```amdgpu-install --usecase=dkms```, then it should install it, but you can check the output from running the script to see if it gets installed. The amdgpu-dkms package just installs source and calls dkms to compile the modules, then installs the output as an upgraded modules on the system. If you watch the output of the installation, it will let you know if the compilation fails, and if it does, there'll a build.log mentioned in the output that would help for debugging.

I'm assuming you're not using any special setup like a container or something?

To be clear, I'm not a HIP guy, so I can't really answer what is and isn't supported, but you should at least get OpenCL support if you want to try something like ```clinfo``` as a baseline. Also please note that we don't actually support AlmaLinux, but considering we support RHEL 9, it should work without too much issue.

---

### 评论 #5 — ppanchad-amd (2024-05-09T19:17:57Z)

@klausbu Apologies for the lack of response. Can you please test with latest ROCm 6.1.0? If resolved, please close ticket. Thanks!

---

### 评论 #6 — ppanchad-amd (2024-05-23T18:27:22Z)

@klausbu Closing ticket.  Please re-open ticket if problem still exist with latest ROCm 6.1.1 Thanks!

---
