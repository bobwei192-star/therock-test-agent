# Desire for ROCm to support Ubuntu 18.04 usage and in the future have Day One support Existing Distros

> **Issue #384**
> **状态**: closed
> **创建时间**: 2018-04-10T14:58:02Z
> **更新时间**: 2018-08-28T08:36:03Z
> **关闭时间**: 2018-08-28T08:36:03Z
> **作者**: MathiasMagnus
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/384

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I am installing a new cluster based on Ubuntu Server and Vega cards and I didn't want to do a `do-release-upgrade` two weeks from now, so I installed Ubuntu Server 18.04 daily on one of the nodes and wanted to give ROCm a spin with minimal sysadmin effort. _(Subiquity is a nightmare, but that is a totally different matter.)_

As was indicated in #361 I installed `linux-image-4.16.1-041601-lowlatency_4.16.1-041601.201804081334_amd64.deb` with matching headers from `http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.16.1/` and tried installing the ROCm packages from the xenial repo provided, as I didn't want to build everything from source. I purposly omitted rocm-dkms, because that was the whole point in trying the out-of-tree kernel. The current rocm-dkms package is a patch for 4.13, and I didn't want to open Pandoras box of building a kernel module for a version it was not meant for. I thought something from the Canonical kernel PPA held less surprises.

`lspci` sees the cards alright, I added my user to the `video` group as well, however when I issue `rocm-smi` it fails to detect any of the 2 cards installed, hence clinfo does not see them as well. amdkfd is loaded as well.

```
lsmod | grep kfd
amdkfd                200704  2
amd_iommu_v2           20480  1 amdkfd
```

I hope this thread can become a step-by-step guide for dummies/low-life sysadmins in getting ROCm to work on a mainline, out-of-tree kernel. How does the dev team spin up a node for testing on a headless Ubuntu 18.04?

---

## 评论 (45 条)

### 评论 #1 — jedwards-AMD (2018-04-10T20:37:53Z)

First, I need to know the versions of the amdkfd and amdgpu versions you are using:
'modinfo amdkfd'
'modinfo amdgpu'
It is possible your card type is not supported using these versions of the driver.

See if there are any errors in dmesg:
 'dmesg | grep amdkfd'
 'dmesg | grep amdgpu'
Also check if the /dev/kfd device exists and is accessible (perms should be 666).

---

### 评论 #2 — MathiasMagnus (2018-04-10T21:51:16Z)

I got two AMD Radeon RX Vega 56 cards. This is the output of the commands you mentioned. There are some errors in the amdgpu logs.
## Modinfo of amdkfd
```
mnagy@radeon:~$ modinfo amdkfd
filename:       /lib/modules/4.16.1-041601-lowlatency/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
version:        0.7.2
license:        GPL and additional rights
description:    Standalone HSA driver for AMD's GPUs
author:         AMD Inc. and others
srcversion:     85F6A8C2CC7AEEAF1C3BD41
depends:        amd_iommu_v2
retpoline:      Y
intree:         Y
name:           amdkfd
vermagic:       4.16.1-041601-lowlatency SMP preempt mod_unload
signat:         PKCS#7
signer:
sig_key:
sig_hashalgo:   md4
parm:           sched_policy:Scheduling policy (0 = HWS (Default), 1 = HWS without over-subscription, 2 = Non-HWS (Used for debugging only) (int)
parm:           hws_max_conc_proc:Max # processes HWS can execute concurrently when sched_policy=0 (0 = no concurrency, #VMIDs for KFD = Maximum(default)) (int)
parm:           cwsr_enable:CWSR enable (0 = Off, 1 = On (Default)) (int)
parm:           max_num_of_queues_per_device:Maximum number of supported queues per device (1 = Minimum, 4096 = default) (int)
parm:           send_sigterm:Send sigterm to HSA process on unhandled exception (0 = disable, 1 = enable) (int)
parm:           ignore_crat:Ignore CRAT table during KFD initialization (0 = use CRAT (default), 1 = ignore CRAT) (int)
```
## Modinfo of amdgpu
```
mnagy@radeon:~$ modinfo amdgpu
filename:       /lib/modules/4.16.1-041601-lowlatency/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko
license:        GPL and additional rights
description:    AMD GPU
author:         AMD linux driver team
firmware:       amdgpu/raven_gpu_info.bin
firmware:       amdgpu/vega10_gpu_info.bin
firmware:       radeon/hawaii_k_smc.bin
firmware:       radeon/hawaii_smc.bin
firmware:       radeon/bonaire_k_smc.bin
firmware:       radeon/bonaire_smc.bin
firmware:       radeon/mullins_mec.bin
firmware:       radeon/mullins_rlc.bin
firmware:       radeon/mullins_ce.bin
firmware:       radeon/mullins_me.bin
firmware:       radeon/mullins_pfp.bin
firmware:       radeon/kabini_mec.bin
firmware:       radeon/kabini_rlc.bin
firmware:       radeon/kabini_ce.bin
firmware:       radeon/kabini_me.bin
firmware:       radeon/kabini_pfp.bin
firmware:       radeon/kaveri_mec2.bin
firmware:       radeon/kaveri_mec.bin
firmware:       radeon/kaveri_rlc.bin
firmware:       radeon/kaveri_ce.bin
firmware:       radeon/kaveri_me.bin
firmware:       radeon/kaveri_pfp.bin
firmware:       radeon/hawaii_mec.bin
firmware:       radeon/hawaii_rlc.bin
firmware:       radeon/hawaii_ce.bin
firmware:       radeon/hawaii_me.bin
firmware:       radeon/hawaii_pfp.bin
firmware:       radeon/bonaire_mec.bin
firmware:       radeon/bonaire_rlc.bin
firmware:       radeon/bonaire_ce.bin
firmware:       radeon/bonaire_me.bin
firmware:       radeon/bonaire_pfp.bin
firmware:       radeon/mullins_sdma1.bin
firmware:       radeon/mullins_sdma.bin
firmware:       radeon/kabini_sdma1.bin
firmware:       radeon/kabini_sdma.bin
firmware:       radeon/kaveri_sdma1.bin
firmware:       radeon/kaveri_sdma.bin
firmware:       radeon/hawaii_sdma1.bin
firmware:       radeon/hawaii_sdma.bin
firmware:       radeon/bonaire_sdma1.bin
firmware:       radeon/bonaire_sdma.bin
firmware:       radeon/si58_mc.bin
firmware:       radeon/oland_mc.bin
firmware:       radeon/verde_mc.bin
firmware:       radeon/pitcairn_mc.bin
firmware:       radeon/tahiti_mc.bin
firmware:       radeon/hainan_rlc.bin
firmware:       radeon/hainan_ce.bin
firmware:       radeon/hainan_me.bin
firmware:       radeon/hainan_pfp.bin
firmware:       radeon/oland_rlc.bin
firmware:       radeon/oland_ce.bin
firmware:       radeon/oland_me.bin
firmware:       radeon/oland_pfp.bin
firmware:       radeon/verde_rlc.bin
firmware:       radeon/verde_ce.bin
firmware:       radeon/verde_me.bin
firmware:       radeon/verde_pfp.bin
firmware:       radeon/pitcairn_rlc.bin
firmware:       radeon/pitcairn_ce.bin
firmware:       radeon/pitcairn_me.bin
firmware:       radeon/pitcairn_pfp.bin
firmware:       radeon/tahiti_rlc.bin
firmware:       radeon/tahiti_ce.bin
firmware:       radeon/tahiti_me.bin
firmware:       radeon/tahiti_pfp.bin
firmware:       radeon/banks_k_2_smc.bin
firmware:       radeon/hainan_k_smc.bin
firmware:       radeon/hainan_smc.bin
firmware:       radeon/oland_k_smc.bin
firmware:       radeon/oland_smc.bin
firmware:       radeon/verde_k_smc.bin
firmware:       radeon/verde_smc.bin
firmware:       radeon/pitcairn_k_smc.bin
firmware:       radeon/pitcairn_smc.bin
firmware:       radeon/tahiti_smc.bin
firmware:       amdgpu/topaz_mc.bin
firmware:       radeon/hawaii_mc.bin
firmware:       radeon/bonaire_mc.bin
firmware:       amdgpu/polaris12_mc.bin
firmware:       amdgpu/polaris10_mc.bin
firmware:       amdgpu/polaris11_mc.bin
firmware:       amdgpu/tonga_mc.bin
firmware:       amdgpu/vega10_asd.bin
firmware:       amdgpu/vega10_sos.bin
firmware:       amdgpu/raven_asd.bin
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
firmware:       amdgpu/raven_rlc.bin
firmware:       amdgpu/raven_mec2.bin
firmware:       amdgpu/raven_mec.bin
firmware:       amdgpu/raven_me.bin
firmware:       amdgpu/raven_pfp.bin
firmware:       amdgpu/raven_ce.bin
firmware:       amdgpu/vega10_rlc.bin
firmware:       amdgpu/vega10_mec2.bin
firmware:       amdgpu/vega10_mec.bin
firmware:       amdgpu/vega10_me.bin
firmware:       amdgpu/vega10_pfp.bin
firmware:       amdgpu/vega10_ce.bin
firmware:       amdgpu/topaz_sdma1.bin
firmware:       amdgpu/topaz_sdma.bin
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
firmware:       amdgpu/raven_sdma.bin
firmware:       amdgpu/vega10_sdma1.bin
firmware:       amdgpu/vega10_sdma.bin
firmware:       amdgpu/vega10_uvd.bin
firmware:       amdgpu/polaris12_uvd.bin
firmware:       amdgpu/polaris11_uvd.bin
firmware:       amdgpu/polaris10_uvd.bin
firmware:       amdgpu/stoney_uvd.bin
firmware:       amdgpu/fiji_uvd.bin
firmware:       amdgpu/carrizo_uvd.bin
firmware:       amdgpu/tonga_uvd.bin
firmware:       radeon/mullins_uvd.bin
firmware:       radeon/hawaii_uvd.bin
firmware:       radeon/kaveri_uvd.bin
firmware:       radeon/kabini_uvd.bin
firmware:       radeon/bonaire_uvd.bin
firmware:       amdgpu/vega10_vce.bin
firmware:       amdgpu/polaris12_vce.bin
firmware:       amdgpu/polaris11_vce.bin
firmware:       amdgpu/polaris10_vce.bin
firmware:       amdgpu/stoney_vce.bin
firmware:       amdgpu/fiji_vce.bin
firmware:       amdgpu/carrizo_vce.bin
firmware:       amdgpu/tonga_vce.bin
firmware:       radeon/mullins_vce.bin
firmware:       radeon/hawaii_vce.bin
firmware:       radeon/kaveri_vce.bin
firmware:       radeon/kabini_vce.bin
firmware:       radeon/bonaire_vce.bin
firmware:       amdgpu/raven_vcn.bin
firmware:       amdgpu/vega10_acg_smc.bin
firmware:       amdgpu/vega10_smc.bin
firmware:       amdgpu/polaris12_smc.bin
firmware:       amdgpu/polaris11_k_smc.bin
firmware:       amdgpu/polaris11_smc_sk.bin
firmware:       amdgpu/polaris11_smc.bin
firmware:       amdgpu/polaris10_k_smc.bin
firmware:       amdgpu/polaris10_smc_sk.bin
firmware:       amdgpu/polaris10_smc.bin
firmware:       amdgpu/fiji_smc.bin
firmware:       amdgpu/tonga_k_smc.bin
firmware:       amdgpu/tonga_smc.bin
firmware:       amdgpu/topaz_k_smc.bin
firmware:       amdgpu/topaz_smc.bin
srcversion:     81AD6462367CE104BA4EBB0
alias:          pci:v00001002d000015DDsv*sd*bc*sc*i*
alias:          pci:v00001002d0000687Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Csv*sd*bc*sc*i*
alias:          pci:v00001002d00006868sv*sd*bc*sc*i*
alias:          pci:v00001002d00006867sv*sd*bc*sc*i*
alias:          pci:v00001002d00006864sv*sd*bc*sc*i*
alias:          pci:v00001002d00006863sv*sd*bc*sc*i*
alias:          pci:v00001002d00006862sv*sd*bc*sc*i*
alias:          pci:v00001002d00006861sv*sd*bc*sc*i*
alias:          pci:v00001002d00006860sv*sd*bc*sc*i*
alias:          pci:v00001002d0000699Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006997sv*sd*bc*sc*i*
alias:          pci:v00001002d00006995sv*sd*bc*sc*i*
alias:          pci:v00001002d00006987sv*sd*bc*sc*i*
alias:          pci:v00001002d00006986sv*sd*bc*sc*i*
alias:          pci:v00001002d00006985sv*sd*bc*sc*i*
alias:          pci:v00001002d00006981sv*sd*bc*sc*i*
alias:          pci:v00001002d00006980sv*sd*bc*sc*i*
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
depends:        drm,drm_kms_helper,ttm,chash,gpu-sched,i2c-algo-bit
retpoline:      Y
intree:         Y
name:           amdgpu
vermagic:       4.16.1-041601-lowlatency SMP preempt mod_unload
signat:         PKCS#7
signer:
sig_key:
sig_hashalgo:   md4
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
parm:           lockup_timeout:GPU lockup timeout in ms > 0 (default 10000) (int)
parm:           dpm:DPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           fw_load_type:firmware loading type (0 = direct, 1 = SMU, 2 = PSP, -1 = auto) (int)
parm:           aspm:ASPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           runpm:PX runtime pm (1 = force enable, 0 = disable, -1 = PX only default) (int)
parm:           ip_block_mask:IP Block Mask (all blocks enabled (default)) (uint)
parm:           bapm:BAPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           deep_color:Deep Color support (1 = enable, 0 = disable (default)) (int)
parm:           vm_size:VM address space size in gigabytes (default 64GB) (int)
parm:           vm_fragment_size:VM fragment size in bits (4, 5, etc. 4 = 64K (default), Max 9 = 2M) (int)
parm:           vm_block_size:VM page table size in bits (default depending on vm_size) (int)
parm:           vm_fault_stop:Stop on VM fault (0 = never (default), 1 = print first, 2 = always) (int)
parm:           vm_debug:Debug VM handling (0 = disabled (default), 1 = enabled) (int)
parm:           vm_update_mode:VM update using CPU (0 = never (default except for large BAR(LB)), 1 = Graphics only, 2 = Compute only (default for LB), 3 = Both (int)
parm:           vram_page_split:Number of pages after we split VRAM allocations (default 512, -1 = disable) (int)
parm:           exp_hw_support:experimental hw support (1 = enable, 0 = disable (default)) (int)
parm:           dc:Display Core driver (1 = enable, 0 = disable, -1 = auto (default)) (int)
parm:           dc_log:Display Core Log Level (0 = minimal (default), 1 = chatty (int)
parm:           sched_jobs:the max number of jobs supported in the sw queue (default 32) (int)
parm:           sched_hw_submission:the max number of HW submissions (default 2) (int)
parm:           ppfeaturemask:all power features enabled (default)) (uint)
parm:           no_evict:Support pinning request from user space (1 = enable, 0 = disable (default)) (int)
parm:           direct_gma_size:Direct GMA size in megabytes (max 96MB) (int)
parm:           pcie_gen_cap:PCIE Gen Caps (0: autodetect (default)) (uint)
parm:           pcie_lane_cap:PCIE Lane Caps (0: autodetect (default)) (uint)
parm:           cg_mask:Clockgating flags mask (0 = disable clock gating) (uint)
parm:           pg_mask:Powergating flags mask (0 = disable power gating) (uint)
parm:           sdma_phase_quantum:SDMA context switch phase quantum (x 1K GPU clock cycles, 0 = no change (default 32)) (uint)
parm:           disable_cu:Disable CUs (se.sh.cu,...) (charp)
parm:           virtual_display:Enable virtual display feature (the virtual_display will be set like xxxx:xx:xx.x,x;xxxx:xx:xx.x,x) (charp)
parm:           ngg:Next Generation Graphics (1 = enable, 0 = disable(default depending on gfx)) (int)
parm:           prim_buf_per_se:the size of Primitive Buffer per Shader Engine (default depending on gfx) (int)
parm:           pos_buf_per_se:the size of Position Buffer per Shader Engine (default depending on gfx) (int)
parm:           cntl_sb_buf_per_se:the size of Control Sideband per Shader Engine (default depending on gfx) (int)
parm:           param_buf_per_se:the size of Off-Chip Pramater Cache per Shader Engine (default depending on gfx) (int)
parm:           job_hang_limit:how much time allow a job hang and not drop it (default 0) (int)
parm:           lbpw:Load Balancing Per Watt (LBPW) support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           compute_multipipe:Force compute queues to be spread across pipes (1 = enable, 0 = disable, -1 = auto) (int)
parm:           gpu_recovery:Enable GPU recovery mechanism, (1 = enable, 0 = disable, -1 = auto (int)
parm:           si_support:SI support (1 = enabled, 0 = disabled (default)) (int)
parm:           cik_support:CIK support (1 = enabled, 0 = disabled (default)) (int)
```
## dmesg amdkfd entries
```
mnagy@radeon:~$ dmesg | grep amdkfd
[    1.497074] Modules linked in: amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e(+) drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    1.497509] Modules linked in: amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e(+) drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    1.497916] Modules linked in: amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e(+) drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    3.007730] Modules linked in: hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    3.008168] Modules linked in: hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    3.008580] Modules linked in: hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
```
## dmesg of amdgpu
```
mnagy@radeon:~$ dmesg | grep amdgpu
[    1.301725] [drm] amdgpu kernel modesetting enabled.
[    1.311353] fb: switching to amdgpudrmfb from EFI VGA
[    1.312174] amdgpu 0000:03:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.312232] amdgpu 0000:03:00.0: BAR 2: releasing [mem 0xd0000000-0xd01fffff 64bit pref]
[    1.312235] amdgpu 0000:03:00.0: BAR 0: releasing [mem 0xc0000000-0xcfffffff 64bit pref]
[    1.312285] amdgpu 0000:03:00.0: BAR 0: assigned [mem 0x600000000-0x7ffffffff 64bit pref]
[    1.312292] amdgpu 0000:03:00.0: BAR 2: assigned [mem 0x500000000-0x5001fffff 64bit pref]
[    1.312352] amdgpu 0000:03:00.0: VRAM: 8176M 0x000000F400000000 - 0x000000F5FEFFFFFF (8176M used)
[    1.312355] amdgpu 0000:03:00.0: GTT: 256M 0x000000F600000000 - 0x000000F60FFFFFFF
[    1.312436] [drm] amdgpu: 8176M of VRAM memory ready
[    1.312439] [drm] amdgpu: 8176M of GTT memory ready.
[    1.314575] amdgpu 0000:03:00.0: [mmhub] VMC page fault (src_id:0 ring:157 vmid:0 pas_id:0)
[    1.314580] amdgpu 0000:03:00.0:   at page 0x000000f600700000 from 18
[    1.314582] amdgpu 0000:03:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x0000013A
[    1.492690] [drm:psp_hw_init [amdgpu]] *ERROR* PSP firmware loading failed
[    1.492719] [drm:amdgpu_device_init [amdgpu]] *ERROR* hw_init of IP block <psp> failed -22
[    1.492722] amdgpu 0000:03:00.0: amdgpu_device_ip_init failed
[    1.497074] Modules linked in: amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e(+) drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    1.497155]  amdgpu_vram_mgr_fini+0x2c/0x50 [amdgpu]
[    1.497188]  amdgpu_ttm_fini+0x6b/0x130 [amdgpu]
[    1.497214]  amdgpu_bo_fini+0x12/0x40 [amdgpu]
[    1.497244]  gmc_v9_0_sw_fini+0x32/0x40 [amdgpu]
[    1.497270]  amdgpu_device_ip_fini+0x1c8/0x350 [amdgpu]
[    1.497295]  amdgpu_device_init+0xd4b/0x1360 [amdgpu]
[    1.497319]  amdgpu_driver_load_kms+0x8b/0x2c0 [amdgpu]
[    1.497350]  amdgpu_pci_probe+0x108/0x190 [amdgpu]
[    1.497413]  amdgpu_init+0x83/0x92 [amdgpu]
[    1.497509] Modules linked in: amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e(+) drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    1.497581]  amdgpu_gtt_mgr_fini+0x2c/0x50 [amdgpu]
[    1.497611]  amdgpu_ttm_fini+0x78/0x130 [amdgpu]
[    1.497635]  amdgpu_bo_fini+0x12/0x40 [amdgpu]
[    1.497665]  gmc_v9_0_sw_fini+0x32/0x40 [amdgpu]
[    1.497689]  amdgpu_device_ip_fini+0x1c8/0x350 [amdgpu]
[    1.497712]  amdgpu_device_init+0xd4b/0x1360 [amdgpu]
[    1.497736]  amdgpu_driver_load_kms+0x8b/0x2c0 [amdgpu]
[    1.497766]  amdgpu_pci_probe+0x108/0x190 [amdgpu]
[    1.497823]  amdgpu_init+0x83/0x92 [amdgpu]
[    1.497916] Modules linked in: amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e(+) drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    1.497990]  amdgpu_ttm_mem_global_release+0x12/0x20 [amdgpu]
[    1.498024]  amdgpu_ttm_fini+0xfa/0x130 [amdgpu]
[    1.498048]  amdgpu_bo_fini+0x12/0x40 [amdgpu]
[    1.498077]  gmc_v9_0_sw_fini+0x32/0x40 [amdgpu]
[    1.498100]  amdgpu_device_ip_fini+0x1c8/0x350 [amdgpu]
[    1.498123]  amdgpu_device_init+0xd4b/0x1360 [amdgpu]
[    1.498146]  amdgpu_driver_load_kms+0x8b/0x2c0 [amdgpu]
[    1.498176]  amdgpu_pci_probe+0x108/0x190 [amdgpu]
[    1.498233]  amdgpu_init+0x83/0x92 [amdgpu]
[    1.498332] [drm] amdgpu: ttm finalized
[    1.498335] amdgpu 0000:03:00.0: Fatal error during GPU init
[    1.498338] [drm] amdgpu: finishing device.
[    1.498482] amdgpu: probe of 0000:03:00.0 failed with error -22
[    1.498520] amdgpu 0000:06:00.0: enabling device (0000 -> 0003)
[    2.822301] amdgpu 0000:06:00.0: BAR 2: releasing [mem 0x380ff0000000-0x380ff01fffff 64bit pref]
[    2.822304] amdgpu 0000:06:00.0: BAR 0: releasing [mem 0x380fe0000000-0x380fefffffff 64bit pref]
[    2.822353] amdgpu 0000:06:00.0: BAR 0: assigned [mem 0x800000000-0x9ffffffff 64bit pref]
[    2.822360] amdgpu 0000:06:00.0: BAR 2: assigned [mem 0xa00000000-0xa001fffff 64bit pref]
[    2.822421] amdgpu 0000:06:00.0: VRAM: 8176M 0x000000F400000000 - 0x000000F5FEFFFFFF (8176M used)
[    2.822424] amdgpu 0000:06:00.0: GTT: 256M 0x000000F600000000 - 0x000000F60FFFFFFF
[    2.822503] [drm] amdgpu: 8176M of VRAM memory ready
[    2.822505] [drm] amdgpu: 8176M of GTT memory ready.
[    2.824606] amdgpu 0000:06:00.0: [mmhub] VMC page fault (src_id:0 ring:157 vmid:0 pas_id:0)
[    2.824611] amdgpu 0000:06:00.0:   at page 0x000000f600700000 from 18
[    2.824613] amdgpu 0000:06:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x0000013A
[    3.003359] [drm:psp_hw_init [amdgpu]] *ERROR* PSP firmware loading failed
[    3.003388] [drm:amdgpu_device_init [amdgpu]] *ERROR* hw_init of IP block <psp> failed -22
[    3.003391] amdgpu 0000:06:00.0: amdgpu_device_ip_init failed
[    3.007730] Modules linked in: hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    3.007812]  amdgpu_vram_mgr_fini+0x2c/0x50 [amdgpu]
[    3.007844]  amdgpu_ttm_fini+0x6b/0x130 [amdgpu]
[    3.007870]  amdgpu_bo_fini+0x12/0x40 [amdgpu]
[    3.007901]  gmc_v9_0_sw_fini+0x32/0x40 [amdgpu]
[    3.007926]  amdgpu_device_ip_fini+0x1c8/0x350 [amdgpu]
[    3.007951]  amdgpu_device_init+0xd4b/0x1360 [amdgpu]
[    3.007976]  amdgpu_driver_load_kms+0x8b/0x2c0 [amdgpu]
[    3.008007]  amdgpu_pci_probe+0x108/0x190 [amdgpu]
[    3.008070]  amdgpu_init+0x83/0x92 [amdgpu]
[    3.008168] Modules linked in: hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    3.008243]  amdgpu_gtt_mgr_fini+0x2c/0x50 [amdgpu]
[    3.008272]  amdgpu_ttm_fini+0x78/0x130 [amdgpu]
[    3.008297]  amdgpu_bo_fini+0x12/0x40 [amdgpu]
[    3.008326]  gmc_v9_0_sw_fini+0x32/0x40 [amdgpu]
[    3.008350]  amdgpu_device_ip_fini+0x1c8/0x350 [amdgpu]
[    3.008375]  amdgpu_device_init+0xd4b/0x1360 [amdgpu]
[    3.008398]  amdgpu_driver_load_kms+0x8b/0x2c0 [amdgpu]
[    3.008429]  amdgpu_pci_probe+0x108/0x190 [amdgpu]
[    3.008486]  amdgpu_init+0x83/0x92 [amdgpu]
[    3.008580] Modules linked in: hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea firewire_ohci sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops glue_helper cryptd e1000e drm firewire_core ahci ptp libahci crc_itu_t pps_core wmi
[    3.008655]  amdgpu_ttm_mem_global_release+0x12/0x20 [amdgpu]
[    3.008688]  amdgpu_ttm_fini+0xfa/0x130 [amdgpu]
[    3.008711]  amdgpu_bo_fini+0x12/0x40 [amdgpu]
[    3.008741]  gmc_v9_0_sw_fini+0x32/0x40 [amdgpu]
[    3.008765]  amdgpu_device_ip_fini+0x1c8/0x350 [amdgpu]
[    3.008788]  amdgpu_device_init+0xd4b/0x1360 [amdgpu]
[    3.008811]  amdgpu_driver_load_kms+0x8b/0x2c0 [amdgpu]
[    3.008841]  amdgpu_pci_probe+0x108/0x190 [amdgpu]
[    3.008898]  amdgpu_init+0x83/0x92 [amdgpu]
[    3.009017] [drm] amdgpu: ttm finalized
[    3.009021] amdgpu 0000:06:00.0: Fatal error during GPU init
[    3.009023] [drm] amdgpu: finishing device.
[    3.009187] amdgpu: probe of 0000:06:00.0 failed with error -22
```
## Perms on /dev/kfd
```
mnagy@radeon:~$ ls -al /dev/kfd
crw------- 1 root root 240, 0 Apr 10 14:14 /dev/kfd
```

---

### 评论 #3 — jedwards-AMD (2018-04-10T21:59:13Z)

Yeah, the dmesg output doesn't look good, especially this:
.
[    3.009021] amdgpu 0000:06:00.0: Fatal error during GPU init
[    3.009023] [drm] amdgpu: finishing device.
[    3.009187] amdgpu: probe of 0000:06:00.0 failed with error -22
.
Looks like the base amdgpu driver can't initialize the card. Also, your version for the amdkfd is really old (ROCm is currently on 2.0). I don't think these cards were supported on the drivers you have installed.

---

### 评论 #4 — jedwards-AMD (2018-04-10T23:13:56Z)

Looking through the dmesg output, you can see the reason:
.
[    1.492690] [drm:psp_hw_init [amdgpu]] *ERROR* PSP firmware loading failed
.
I have seen firmware installation ordering problems get resolved by rebuilding the ramfs image: `update-initramfs -u`
However, I think the card just isn't supported.



---

### 评论 #5 — MathiasMagnus (2018-04-11T10:14:43Z)

I uninstalled all the out-of-tree stuff and went ahead and tried installing rocm-dkms. rocm-smi found the cards, but clinfo did not, even though permissions were fine on /dev/kfd. The version of dkms was still the same 0.7.6. How can I update that? I though the point of of rocm-dkms was to update this module?

I had a fairly good understanding of debugging fglrx drivers (lspci, lsmod, chmod, aticonfig, clinfo), but I have no experience in getting this stack to work.

---

### 评论 #6 — jedwards-AMD (2018-04-11T14:12:13Z)

What is the clinfo error? You may also want to run clinfo with strace to make sure you environment is setup correctly. Also, see if rocminfo runs.

---

### 评论 #7 — oscarbg (2018-04-11T20:46:50Z)

@jedwards-AMD Sorry for joining the conversation but has ROCM 2.0 already been released even in beta form? Changelog somewhere?

---

### 评论 #8 — MathiasMagnus (2018-04-13T12:32:03Z)

ROCm info says:
```
mnagy@radeon:~$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104
```
strace of clinfo does not fail, it reports 0 platforms. There is no error code. `/etc/OpenCL/vendros/amdocl64.icd` contains `libamdocl64.so` which is inside `/opt/rocm/opencl/lib/x86_64` which is configured for `ldconfig`.

Strace attached. [strace_clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/1907317/strace_clinfo.txt)

---

### 评论 #9 — MathiasMagnus (2018-04-21T11:46:36Z)

May I get a little guidance here?

_Also, another interesting note is [seeing ROCm on Windows](https://gpuopen.com/using-rocm-to-leverage-hbm-a-matrix-vector-multiplication-case-study/#comment-12269), which would be the first time since long that the Windows drivers receive a major update. Is this work still in progress? My Windows devbox (the one and only) would love to see some OpenCL care as well, not just the Linux cluster._

---

### 评论 #10 — oscarbg (2018-04-21T12:21:52Z)

Hi @MathiasMagnus,
super nice find about ROCM on Windows!!
hope that's why this is being called ROCM 2.0.. I think there were early efforts to support HSA on Windows (the precursor to it)..
sadly HSA only was supported on APUs only so never tested.. hope ROCM brings discrete support..
this month 18.4 or 18.5 should come big driver update from new branch call it 18.10 for windows 18.04 hope ROCM support is included!
just have same setup as yours Unbuntu 18.04 and Vega 56..
the unique solution  if using newer kernels say >4.15 is to use this (build this kernel)(in theory!!):
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/fkxamd/drm-next-wip
that has all the kfd bits for Vega included (4.17rc1 has it for pre Vega cards)..
https://www.phoronix.com/scan.php?page=news_item&px=AMDKFD-GFX9-Vega-Patches
what I really did is clone 4.17rc1 and apply the patches from here:
https://lists.freedesktop.org/archives/amd-gfx/2018-April/021154.html
should be equivalent..
anyway hope gets merged in time for 4.18 and we can download from kernel ppa daily or drm-next kernels soon (say in a month or two)
I have built kernel but have yet to test..
please just post your findings if you have success (you should have)!!


---

### 评论 #11 — briansp2020 (2018-04-21T13:56:41Z)

It's happening. https://github.com/RadeonOpenCompute/ROCm/issues/18#issuecomment-376536175
It just seems to take longer than they anticipated.

---

### 评论 #12 — zpodlovics (2018-04-21T13:56:53Z)

@oscarbg You are right, there WAS HSA support for APUs (Kaveri), unfortunately that support was removed as of https://github.com/RadeonOpenCompute/ROCm/issues/66 

I did some testing with roughly a month ago on 16.04 and 4.13 kernel and 4.15 mainline kernel, with ubuntu rocm packages, the kernel kfd seems to initialized currectly, rocminfo worked fine, but the hsa sample was not (hang both with default/custom libhsakmt). I have seen some patches in the amd-gfx mailing lists to restore the older APU support.

The hsa sample are avaialable at:
/opt/rocm/hsa/sample



---

### 评论 #13 — MathiasMagnus (2018-04-23T12:13:51Z)

@oscarbg Thank you for the info, I am a little too noobish to make any sense of it. The ROCK-Kernel-Driver branch you linked is a patched 4.13 kernel, I don't think it will work with Ubuntu 18.04 shipping 4.15 out of the box. When I tried to build the kernel, the interactive config page says it's 4.13.

The set of patches you link do not apply to 4.17-rc1, or to any 4.15+ kernel tag to be exact. The link you provided does not provide the patch files themselves, so I downloaded them from https://patchwork.freedesktop.org/series/41502/ but when I try to check for compatibility, one patch fails.

```
mnagy@radeon:~/Source/Repos/linux$ git checkout v4.17-rc1
Previous HEAD position was 6d08b06e67cd Linux 4.17-rc2
HEAD is now at 60cc43fc8884 Linux 4.17-rc1
mnagy@radeon:~/Source/Repos/linux$ git apply --check ~/Downloads/amdkfd-patches/07-21-drm-amdkfd-Clean-up-KFD_MMAP_-offset-handling.patch
error: patch failed: drivers/gpu/drm/amd/amdkfd/kfd_doorbell.c:126
error: drivers/gpu/drm/amd/amdkfd/kfd_doorbell.c: patch does not apply
error: patch failed: drivers/gpu/drm/amd/amdkfd/kfd_priv.h:728
error: drivers/gpu/drm/amd/amdkfd/kfd_priv.h: patch does not apply
```
It's becoming quite aggravating in getting all of this to work.

---

### 评论 #14 — MathiasMagnus (2018-04-23T13:11:53Z)

I've found out that the patches cannot be verified all upfront, but instead have to be applied one after the other and only then can they be verified. However, some patches cause `blank-at-eol` when applying, and trying to come up with a setting for it gets me as far as applying patch 11, which then says it doesn't apply.
```
mnagy@radeon:~/Source/Repos/linux$ git reset --hard v4.17-rc1
Checking out files: 100% (13787/13787), done.
HEAD is now at 60cc43fc8884 Linux 4.17-rc1
mnagy@radeon:~/Source/Repos/linux$ git status
HEAD detached at v4.17-rc1
nothing to commit, working tree clean
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/01-21-drm-amdgpu-Remove-unused-interface-from-kfd2kgd-interface.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/02-21-drm-amd-Update-GFXv9-SDMA-MQD-structure.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/03-21-drm-amdgpu-Add-GFXv9-TLB-invalidation-packet-definition.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/04-21-drm-amdgpu-Add-GFXv9-kfd2kgd-interface-functions.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/05-21-drm-amdgpu-Add-doorbell-routing-info-to-kgd2kfd_shared_resources.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/06-21-drm-amdkfd-Make-doorbell-size-ASIC-dependent.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/07-21-drm-amdkfd-Clean-up-KFD_MMAP_-offset-handling.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/08-21-drm-amdkfd-Implement-doorbell-allocation-for-SOC15.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/09-21-drm-amdkfd-Move-packet-writer-functions-into-ASIC-specific-file.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/10-21-drm-amdkfd-Add-GFXv9-PM4-packet-writer-functions.patch
mnagy@radeon:~/Source/Repos/linux$ git apply ~/Downloads/amdkfd-patches/11-21-drm-amdkfd-Add-GFXv9-MQD-manager.patch
error: patch failed: drivers/gpu/drm/amd/amdkfd/kfd_device.c:700
error: drivers/gpu/drm/amd/amdkfd/kfd_device.c: patch does not apply
```
This is as far as I can get.

---

### 评论 #15 — boberfly (2018-04-24T05:09:09Z)

I'm testing this out now too, but on kernel 4.17rc2 from http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.17-rc2/

Looks like kfd is essentially a stub on Vega10, and need to apply those patches also. How fun... :)

@MathiasMagnus that 'patch does not apply' might mean it's just a redundant patch and it's already applied.

---

### 评论 #16 — MathiasMagnus (2018-04-24T06:00:13Z)

@boberfly But there are no sources to apply the patches to. Does that mean that you simply install the 4.17-rc2 kernel and install the rocm runtime and that's it? Or the rocm-dkms package as well?

---

### 评论 #17 — boberfly (2018-04-24T06:18:27Z)

@MathiasMagnus I'm cloning it now (slow) and will apply the patches you are trying to apply, then create a bunch of debs

---

### 评论 #18 — boberfly (2018-04-24T06:23:43Z)

my hunch is you'll see a repo target 18.04 soon with a dkms which is designed to patch 4.15 rather than getting a bleeding edge kernel like what we're doing and apply the last vega patches on top which missed the deadline, we're just in this void time until either one is done... :)

---

### 评论 #19 — boberfly (2018-04-24T06:56:12Z)

That patch is tripping on the 11th patch for this line:
```
-	*mem_obj = kmalloc(sizeof(struct kfd_mem_obj), GFP_NOIO);
+	*mem_obj = kzalloc(sizeof(struct kfd_mem_obj), GFP_NOIO);
```
Change it to:
```
-	*mem_obj = kmalloc(sizeof(struct kfd_mem_obj), GFP_KERNEL);
+	*mem_obj = kzalloc(sizeof(struct kfd_mem_obj), GFP_KERNEL);
```

---

### 评论 #20 — boberfly (2018-04-24T07:43:39Z)

Ok running this new kernel with those patches applied, not sure what to do from here but I get this:
```
alex@alex-HP-Z620-Workstation:~$ dmesg |grep kfd
[    2.774144] kfd kfd: Initialized module
[    3.297248] kfd kfd: Allocated 3969056 bytes on gart
[    3.297484] kfd kfd: added device 1002:6863
alex@alex-HP-Z620-Workstation:~$ dmesg |grep amdgpu                                                                                                                     
[    2.758379] [drm] amdgpu kernel modesetting enabled.
[    2.774415] amdgpu 0000:07:00.0: enabling device (0106 -> 0107)
[    2.774761] amdgpu 0000:07:00.0: BAR 2: releasing [mem 0xe0000000-0xe01fffff 64bit pref]
[    2.774763] amdgpu 0000:07:00.0: BAR 0: releasing [mem 0xd0000000-0xdfffffff 64bit pref]
[    2.774813] amdgpu 0000:07:00.0: BAR 0: no space for [mem size 0x400000000 64bit pref]
[    2.774814] amdgpu 0000:07:00.0: BAR 0: failed to assign [mem size 0x400000000 64bit pref]
[    2.774816] amdgpu 0000:07:00.0: BAR 2: no space for [mem size 0x00200000 64bit pref]
[    2.774817] amdgpu 0000:07:00.0: BAR 2: failed to assign [mem size 0x00200000 64bit pref]
[    2.774869] amdgpu 0000:07:00.0: BAR 0: assigned [mem 0xd0000000-0xdfffffff 64bit pref]
[    2.774875] amdgpu 0000:07:00.0: BAR 2: assigned [mem 0xe0000000-0xe01fffff 64bit pref]
[    2.774886] amdgpu 0000:07:00.0: VRAM: 16368M 0x000000F400000000 - 0x000000F7FEFFFFFF (16368M used)
[    2.774887] amdgpu 0000:07:00.0: GTT: 512M 0x000000F800000000 - 0x000000F81FFFFFFF
[    2.775987] [drm] amdgpu: 16368M of VRAM memory ready
[    2.775988] [drm] amdgpu: 16368M of GTT memory ready.
[    3.298760] amdgpu 0000:07:00.0: ring 0(gfx) uses VM inv eng 4 on hub 0
[    3.298761] amdgpu 0000:07:00.0: ring 1(comp_1.0.0) uses VM inv eng 5 on hub 0
[    3.298763] amdgpu 0000:07:00.0: ring 2(comp_1.1.0) uses VM inv eng 6 on hub 0
[    3.298764] amdgpu 0000:07:00.0: ring 3(comp_1.2.0) uses VM inv eng 7 on hub 0
[    3.298765] amdgpu 0000:07:00.0: ring 4(comp_1.3.0) uses VM inv eng 8 on hub 0
[    3.298767] amdgpu 0000:07:00.0: ring 5(comp_1.0.1) uses VM inv eng 9 on hub 0
[    3.298768] amdgpu 0000:07:00.0: ring 6(comp_1.1.1) uses VM inv eng 10 on hub 0
[    3.298769] amdgpu 0000:07:00.0: ring 7(comp_1.2.1) uses VM inv eng 11 on hub 0
[    3.298770] amdgpu 0000:07:00.0: ring 8(comp_1.3.1) uses VM inv eng 12 on hub 0
[    3.298772] amdgpu 0000:07:00.0: ring 9(kiq_2.1.0) uses VM inv eng 13 on hub 0
[    3.298773] amdgpu 0000:07:00.0: ring 10(sdma0) uses VM inv eng 4 on hub 1
[    3.298774] amdgpu 0000:07:00.0: ring 11(sdma1) uses VM inv eng 5 on hub 1
[    3.298775] amdgpu 0000:07:00.0: ring 12(uvd) uses VM inv eng 6 on hub 1
[    3.298777] amdgpu 0000:07:00.0: ring 13(uvd_enc0) uses VM inv eng 7 on hub 1
[    3.298778] amdgpu 0000:07:00.0: ring 14(uvd_enc1) uses VM inv eng 8 on hub 1
[    3.298779] amdgpu 0000:07:00.0: ring 15(vce0) uses VM inv eng 9 on hub 1
[    3.298780] amdgpu 0000:07:00.0: ring 16(vce1) uses VM inv eng 10 on hub 1
[    3.298781] amdgpu 0000:07:00.0: ring 17(vce2) uses VM inv eng 11 on hub 1
[    3.299392] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:07:00.0 on minor 0
[    7.253538] amdgpu 0000:07:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none  
```

---

### 评论 #21 — boberfly (2018-04-24T08:33:44Z)

I think at this stage we might need to wait for the userspace stuff (ROCm) to catch up :) 1.7.1-beta4 I can only get rocm-smi to work.

---

### 评论 #22 — boberfly (2018-04-24T09:02:08Z)

https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/fxkamd/drm-next-wip looks like this might be the closest to the catch-up branch, time to sleep then

---

### 评论 #23 — MathiasMagnus (2018-04-24T10:41:58Z)

@boberfly Thank you Alex for your work. I appreciate it.

One of the reasons why the the "void time until either is done" is frustrating is because currently none of our AMD HW work. We have had GCN 1.0 cards up until now, which were last supported on Ubuntu 14.04. I have the [dokomix PPA](https://launchpad.net/~dokomix/+archive/ubuntu/fglrx-xenial) set up on the nodes with such HW which forward ports fglrx to kernel 4.4 used in 16.04. It worked fine up until 1-2 months back with some kernel update. Because I screwed up and only made an 800MB sized `/boot`, I cannot keep many kernels on disk and removed those that worked previously. I'll have to find the way to restoring old kernels from the Ubuntu repo. _(Install, modify grub to boot old kernel by default, mark kernel packages not to be updated, etc.)_

No probs, new cards arrived 2 weeks ago, because do-release-upgrade wrecked a node, I went ahead and installed 18.04 to save time when it is officially supported, I've seen others have managed, hoped I could do too.

---

### 评论 #24 — boberfly (2018-04-24T17:50:22Z)

Probably best to go back to 17.10 with 1.7.1-beta4 if you want something to work, but 1.8 looks like it's on the horizon: https://twitter.com/angstroms/status/988746027502010368

---

### 评论 #25 — gstoner (2018-05-05T14:37:56Z)

 @boberfly You will find http://repo.radeon.com/rocm/misc/beta_1.8.0/   

@MathiasMagnus We have never said we support GCN 1.0 parts from Day one, these parts lack key capabilities in the hardware for ROCm.  We are very clear on this from Day 1.   The ROCm team has been a small team when we started our mission was to service the Server GPU computing market aka Tesla.   The team is growing but the team still has to stay focused. 

1.8 is still 16.04 based understand we have to wait until base Linux driver team get is support in place.  

One big change from the past is we now have base driver support for ROCm upstream for Polaris, Fiji Vega10, and some newer GPU so in the future you will be able to get earlier distro access.   This helps us since we always have base driver upstream so we can minimize any patch we may need to do for bug fixes on newest OS release.   This also will allow for broader distribution support and make easier to support newer distro releases

---

### 评论 #26 — boberfly (2018-05-05T20:54:44Z)

@gstoner cheers for the update!

I briefly tried on my kernel 4.17rc2 with Vega10 patches applied but couldn't progress any more than what I had before, so only rocm-smi worked. I still have a 4.13 kernel installed from Ubuntu 17.10 on here, so I got rock-dkms to build against this kernel and success! I am now able to see it as an OpenCL device. I'm currently testing Blender Cycles.

Cheers again!

---

### 评论 #27 — gstoner (2018-05-05T23:44:54Z)

We have all the patches for 1.8 coming out this week.  

---

### 评论 #28 — oscarbg (2018-05-06T03:50:41Z)

@gstoner 
so reading correclty are you saying rocm 1.8beta2 coming this week will have Ubuntu 18.04 support (so dkms patches will support kernel 4.15)?
that's nice..

nice news coming after some frustating spent day also trying to get Vega10 working on Ubuntu 18.04..
tested with kernel 4.17rc1 compiled with patches posted for Vega KFD support but altough it seemed all nice:
(I was getting good looking output in dmesg)
[    1.730347] kfd kfd: Initialized module
[    2.296818] kfd kfd: Allocated 3969056 bytes on gart
[    2.296928] kfd kfd: added device 1002:687f
it doesn't work..
rocminfo reports error on hsa init:

hsa api call failure at line 900, file: /home/ivan/rocminfo/rocminfo.cc. Call returned 4104

no matter if using ROCM 1.6,1.7 or 1.8beta (or I extract libhsa-runtime64.so.1  and libhsakmt.so.1 from these Ubuntu repos or install hsa-rocr-dev deb files manually with dpkg -i)..
anyway these files are set correctly as found as shown:
 ldd rocminfo
	linux-vdso.so.1 (0x00007ffd6994d000)
	libhsa-runtime64.so.1 => /opt/rocm/hsa/lib/libhsa-runtime64.so.1 (0x00007f2a51630000)
	libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f2a512a7000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f2a50eb6000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f2a50c9e000)
        libhsakmt.so.1 => /opt/rocm/libhsakmt/lib/libhsakmt.so.1 (0x00007fcf0a065000)
	
doing strace rocminfo:
lines before failing:
openat(AT_FDCWD, "/dev/dri/renderD128", O_RDWR|O_CLOEXEC) = 4
lots of brk(0x56457a520000)                     = 0x56457a520000
ioctl(3, _IOC(_IOC_READ|_IOC_WRITE, 0x4b, 0x19, 0x10), 0x7ffde27f61a0) = -1 EINVAL (Invalid argument)
ioctl(3, AMDKFD_IOC_GET_PROCESS_APERTURES, 0x7ffde27f6330) = 0
ioctl(3, _IOC(_IOC_WRITE, 0x4b, 0x21, 0x8), 0x7ffde27f61a0) = -1 EINVAL (Invalid argument)

Anyway I still had big hopes of getting working by testing new AMDGPU PRO 18.20  preview (amdgpu-pro-18.20-579836) with Ubuntu 18.04 support! (run with -pro argument so it installs all closed source opengl+opencl+vulkan driver):
https://support.amd.com/en-us/kb-articles/Pages/Radeon-Software-for-Linux-18.20-Early-Preview-Release-Notes.aspx

installed it and amdgpu 18.20 dkms module build correctly for kernel 4.15.0-20 as expected..
it started nice as glxinfo+glxgears showed correctly working OGL closed source driver, vulkan closed driver also works OK..
finally OpenCL works OK (https://github.com/krrishnarraj/clpeak works nice)! and clinfo shows this
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (2633.3)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2633.3)
  Driver Version                                  2633.3 (PAL,HSAIL)
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Board Name (AMD)                         Radeon RX Vega
  Device Topology (AMD)                           PCI-E, 03:00.0
..

so some question is I'm getting confused by reading 18.20 install notes.. they say:
Vega10 and newer cards (18.20)
    ./amdgpu-pro-install -y --opencl=pal
Vega10 and newer cards (when using the 18.Q1.1 Enterprise driver)
    ./amdgpu-pro-install -y --opencl=rocm

is PAL driver using ROCM stack?
I say because I see ( 2633.3 (PAL,HSAIL)) and HSAIL should be usable only on ROCM stack, right?
also this implies ROCM should work OK in that case..
because I can't get ROCM working (rocminfo) on 18.20..

of course I install roct-amdgpu-pro_1.0.8-579836_amd64.deb and roct-amdgpu-pro-dev_1.0.8-579836_amd64.deb for getting libhsakmt.so.1 part for rocminfo..
but we also need libhsa-runtime64.so.1  for running simple rocm apps like rocminfo and seems this has been removed from AMDGPU Pro drivers recently as seeing also the latest stable driver (amdgpu-pro-18.10-572953) also only ships  libhsakmt.so in 
 roct-amdgpu-pro_1.0.7-572953_amd64.deb
roct-amdgpu-pro-dev_1.0.7-572953_amd64.deb
but no packages providing libhsa-runtime64.so..

strangely enough checking amdgpu-pro-17.50-552542 provided 
rocr-amdgpu-pro_1.1.6-552542_amd64.deb (providing libhsa-runtime64.so*)
in addition to 
roct-amdgpu-pro_1.0.7-552542_amd64.deb (providing libhsakmt.so*)

the rocr-amdgpu-pro package is missing..
@gstoner can you point to AMDGPU PRO driver packagers/mantainers to include rocr packages..
seems an important omission..
AMD should add a minimal ROCM test before releasing an AMDGPU Pro driver (check that can run rocminfo correctly and make and run vector_copy sample in rocm/hsa/sample folder)

So have tested using  libhsa-runtime64.so files from ROCM 1.6,1.7,1.8 whithout success.. 
i.e. running rocminfo also fails similarly..
in this case I check I'm using libhsakmt.so from amdgpu-pro 18.20 and of course under kernel 4.15 as said previously by running:
ldd rocminfo 
it changes from :
libhsakmt.so.1 => /opt/rocm/libhsakmt/lib/libhsakmt.so.1 (0x00007fcf0a065000)
to
libhsakmt.so.1 => /opt/amdgpu-pro/lib/x86_64-linux-gnu/libhsakmt.so.1 (0x00007f2a50a7c000)

So briefly: 
even in ROCM 1.8beta2 gets support for 18.04 +kernel 4.15 support this week which is awesome! 
Still help wanted on getting AMDGPU PRO 18.20 ROCM working correctly (and note I have clinfo and OCL apps working correctly there with drv 2633.3 (PAL,HSAIL))
also can you request AMDGPU Pro packages to include  libhsa-runtime64.so files similar to including  libhsakmt.so. isn't enough for running simple apps like rocminfo..
older AMDGPU Pro released included libhsa-runtime64 in rocr-amdgpu-pro.deb but seems both 18.10 and 18.20 preview have removed it..

thanks..
Oscar.

---

### 评论 #29 — oscarbg (2018-05-06T07:03:33Z)

just forget to say that using 18.20 dkms installed with kernel 4.15 and running rocminfo I get in dmesg (in addition to the strace details provided):

[  283.284910] kfd2kgd: amdgpu: failed to validate PT BOs
[  283.284913] kfd2kgd: validate_pt_pd_bos() failed
[  283.284915] Failed to create process VM object

this isn't reported in dmesg on 4.17+KFD Vega patches altough strace messages seem identical..


---

### 评论 #30 — gstoner (2018-05-06T16:03:04Z)

Oscar
No we are not saying this release supports 18.04.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Oscar Barenys <notifications@github.com>
Sent: Sunday, May 6, 2018 2:03:34 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Ubuntu 18.04 usage (#384)


just forget to say that using 18.20 dkms installed with kernel 4.15 and running rocminfo I get in dmesg (in addition to the strace details provided):

[ 283.284910] kfd2kgd: amdgpu: failed to validate PT BOs
[ 283.284913] kfd2kgd: validate_pt_pd_bos() failed
[ 283.284915] Failed to create process VM object

this isn't reported in dmesg on 4.17+KFD Vega patches altough strace messages seem identical..

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/384#issuecomment-386858959>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudoEXdaW793-OEOYT9CrmUJ1rWYDks5tvqBGgaJpZM4TOblq>.


---

### 评论 #31 — gstoner (2018-05-06T16:05:40Z)

Also please do not mix AMDGPUpro drivers with ROCm driver release.  We will not support this.    We have firmware and more bug fixes beyond what that driver does.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Gregory Stoner
Sent: Sunday, May 6, 2018 11:03:00 AM
To: RadeonOpenCompute/ROCm; RadeonOpenCompute/ROCm
Cc: Mention
Subject: Re: [RadeonOpenCompute/ROCm] Ubuntu 18.04 usage (#384)

Oscar
No we are not saying this release supports 18.04.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Oscar Barenys <notifications@github.com>
Sent: Sunday, May 6, 2018 2:03:34 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Ubuntu 18.04 usage (#384)


just forget to say that using 18.20 dkms installed with kernel 4.15 and running rocminfo I get in dmesg (in addition to the strace details provided):

[ 283.284910] kfd2kgd: amdgpu: failed to validate PT BOs
[ 283.284913] kfd2kgd: validate_pt_pd_bos() failed
[ 283.284915] Failed to create process VM object

this isn't reported in dmesg on 4.17+KFD Vega patches altough strace messages seem identical..

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/384#issuecomment-386858959>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudoEXdaW793-OEOYT9CrmUJ1rWYDks5tvqBGgaJpZM4TOblq>.


---

### 评论 #32 — vampyrus (2018-07-03T11:18:09Z)

When we ll get ROCm to work with 18.04     ?

---

### 评论 #33 — jedwards-AMD (2018-07-03T14:55:42Z)

This may work now, but formal testing is occurring for the 1.9 release of ROCm.

---

### 评论 #34 — preda (2018-07-10T11:02:57Z)

@jedwards-AMD: "This may work now" : where can I find the recipe or a script for installing ROCm on Ubuntu 18.04?


---

### 评论 #35 — jedwards-AMD (2018-07-10T14:05:29Z)

Install directly from the repository, using the instructions for 16.04. However, we have noticed that the 4.15 version of the kernel is incompatible with the current version of rock-dkms. This should be fixed in the upcoming 1.8.2 release (scheduled for late this week).

---

### 评论 #36 — jedwards-AMD (2018-07-10T14:05:35Z)

Install directly from the repository, using the instructions for 16.04. However, we have noticed that the 4.15 version of the kernel is incompatible with the current version of rock-dkms. This should be fixed in the upcoming 1.8.2 release (scheduled for late this week).

---

### 评论 #37 — shimmervoid (2018-07-10T14:38:49Z)

thanks @jedwards-AMD & ROCm team for this very welcome forward momentum. 

---

### 评论 #38 — Bengt (2018-07-11T17:15:34Z)

@preda I documented what worked for me. Maybe you want to follow my steps:

https://gist.github.com/Bengt/98df20e0708c9766fc9f12f11365029b/b456e8fbb52087e3460f12660f744918fffa9648#kernel-downgrade

---

### 评论 #39 — MathiasMagnus (2018-08-23T14:56:53Z)

@jedwards-AMD I have followed your advice installing ROCm 1.8.2 from the repo onto an Ubuntu 18.04 Server, but it then fails to boot with the following:

![wp_20180823_16_31_12_pro](https://user-images.githubusercontent.com/9763499/44533134-21426d80-a6f5-11e8-8722-65e193cdf6c4.jpg)

_Following the Windows driver 18.8.1 silently dropping the CPU device as well as SPIR support (enough for ComputeCpp), AMDGPU-PRO 18.30 failing to present any OpenCL device, and ROCm still not installing on an Ubuntu 18.04 machine, I think I'll just shut down the AMD part of the cluster and revisit the issue a few months from now._

---

### 评论 #40 — jedwards-AMD (2018-08-23T15:14:19Z)

This error indicate to me that the KFD is loading, but not finding a valid device. This is a long ticket, but can you give the lspci output for the card and the card type. Also, please give the mother board type. The output to the following two commands would be helpful:
.
dmseg | grep amdgpu
dmesg | grep amdkfd
.


---

### 评论 #41 — jlgreathouse (2018-08-23T15:24:09Z)

In addition, you could try including the following line in your kernel parameters on your next boot:
`amdkfd.dyndbg=+plm`

This will print out more informatino from AMDKFD that may help us debug the issue. After booting with those parameters, if you run `dmesg | grep kfd` you'll see more information that may be useful to put here.

---

### 评论 #42 — MathiasMagnus (2018-08-24T11:11:07Z)

@jlgreathouse I tried adding the kernel argument you mentioned [based on this](https://askubuntu.com/a/19487/220219) answer, but did not see anything new on the monitor once boot halted. The problem is that the machine becomes so unresponsive, not even the `NumLock` led changes state on the keyboard. The machine does not ping, so no SSH either, no terminal in runlevel 1... the machine has not yet booted up. How could I issue `dmesg` commands?

I did start a boot in recovery mode, when tried enabling networking from the purple screen, it halted at some point. So on my next attempt, I chose "resume (normal boot)". It warned me, that some GPU drivers will not like resuming a normal boot from recovery mode, but it managed to boot up. The GPUs did not work, but I got a console and issued the commands you asked.

[dmesg_amdgpu_at_radeon.txt](https://github.com/RadeonOpenCompute/ROCm/files/2318084/dmesg_amdgpu_at_radeon.txt)
[dmesg_kfd_at_radeon.txt](https://github.com/RadeonOpenCompute/ROCm/files/2318085/dmesg_kfd_at_radeon.txt)
[lspci_at_radeon.txt](https://github.com/RadeonOpenCompute/ROCm/files/2318086/lspci_at_radeon.txt)
[uname-r_at_radeon.txt](https://github.com/RadeonOpenCompute/ROCm/files/2318087/uname-r_at_radeon.txt)

The motherboard was repurposed from under Intel Phi accelerator cards. The exact model is a [ASUS P9X79 WS](https://www.asus.com/us/Motherboards/P9X79_WS/), and the installed CPU model is an [Intel® Xeon® Processor E5-1650v2](https://ark.intel.com/products/75780/Intel-Xeon-Processor-E5-1650-v2-12M-Cache-3_50-GHz).

I am not the _non plus ultra_ of sysadmins, so let me know if there's anything I can pull out of a system that cannot boot trying to load the drivers at boot time.

---

### 评论 #43 — jlgreathouse (2018-08-25T19:07:55Z)

A few more questions:

- Could you run `lspci -tv`?
- This may be a bit of an odd question, but do you have PCIe large BAR enabled in your BIOS? (This is often labelled "Above 4G Decoding", sometimes motherboard vendors label it notes about bitcoin mining, or enabling more than 4/8/etc GPUs). If I remember correct, Xeon Phi accelerators required large BAR support. However, if you don't have a large BAR VBIOS on your AMD GPU while the BIOS is trying to use this mode, you may run into issues.
- Last ditch effort: how hard would it be to take one of these systems and try Ubuntu 16.04? One worry I have is that this issue is potentially conflating two things: all of these issues could be because of a broken hardware setup, or they could be because of how we're going about installing 1.8.x on a technically-unsupported Ubuntu 18.04.

---

### 评论 #44 — MathiasMagnus (2018-08-27T08:47:26Z)

Here is the `lspci -tv` output. I recall there is an "Intel Phi support" option in the BIOS, it might be the codename of above 4G. I'll check momentarily when I get to the server room.

[lspci_tv_at_radeon.txt](https://github.com/RadeonOpenCompute/ROCm/files/2323066/lspci_tv_at_radeon.txt)


---

### 评论 #45 — MathiasMagnus (2018-08-28T08:36:03Z)

The problem solved itself by disabling Intel Phi support in BIOS. I thought I turned it off, but it seems I was wrong. Once the feature was turned off, the machine booted properly. OpenCL seems to be working fine.

With 1.8.2 being able to install on Ubuntu 18.04 with no modifications compared to the advertised install method, I'll go ahead and close this issue.

---
