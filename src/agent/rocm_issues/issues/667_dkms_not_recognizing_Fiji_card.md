# dkms not recognizing Fiji card

> **Issue #667**
> **状态**: closed
> **创建时间**: 2019-01-09T16:14:48Z
> **更新时间**: 2019-01-10T01:55:45Z
> **关闭时间**: 2019-01-10T01:55:45Z
> **作者**: awenocur
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/667

## 描述

I'm trying to test ROCm on my Sapphire R9 Fury. It appears that dkms is loading, but not recognizing my GPU as supporting kfd.

The output of commands is thus:

```
$ sudo lshw | grep -A20 "Motherboard"
       description: Motherboard
       product: E3V5 WS
       vendor: ASRock
       physical id: 0
     *-firmware
          description: BIOS
          vendor: American Megatrends Inc.
          physical id: 0
          version: P7.30
          date: 01/22/2018
          size: 64KiB
          capacity: 13MiB
          capabilities: pci upgrade shadowing cdboot bootselect socketedrom edd int13floppy1200 int13floppy720 int13floppy2880 int5printscreen int9keyboard int14serial int17printer acpi usb biosbootspecification uefi
     *-cache:0
          description: L1 cache
          physical id: b
          slot: L1 Cache
          size: 128KiB
          capacity: 128KiB
          capabilities: synchronous internal write-back data
          configuration: level=1
```

```
$ lshw -C display
  *-display
       description: VGA compatible controller
       product: Fiji [Radeon R9 FURY / NANO Series]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:01:00.0
       version: cb
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:126 memory:c0000000-cfffffff memory:d0000000-d01fffff ioport:e000(size=256) memory:dfe00000-dfe3ffff memory:c0000-dffff
```

```
$ lshw -C CPU
  *-cpu
       description: CPU
       product: Intel(R) Xeon(R) CPU E3-1235L v5 @ 2.00GHz
       vendor: Intel Corp.
       physical id: f
       bus info: cpu@0
       version: Intel(R) Xeon(R) CPU E3-1235L v5 @ 2.00GHz
       serial: To Be Filled By O.E.M.
       slot: CPUSocket
       size: 2037MHz
       capacity: 3GHz
       width: 64 bits
       clock: 100MHz
       capabilities: x86-64 fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp flush_l1d cpufreq
       configuration: cores=4 enabledcores=4 threads=4`

` $ modprobe -c | grep amdgpu
alias pci:v00001002d00001304sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001305sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001306sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001307sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001309sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000130Asv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000130Bsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000130Csv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000130Dsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000130Esv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000130Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001310sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001311sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001312sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001313sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001315sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001316sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001317sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00001318sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000131Bsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000131Csv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000131Dsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000015D8sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000015DDsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006600sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006601sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006602sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006603sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006604sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006605sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006606sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006607sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006608sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006610sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006611sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006613sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006617sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006620sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006621sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006623sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006631sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006640sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006641sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006646sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006647sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006649sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006650sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006651sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006658sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000665Csv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000665Dsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000665Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006660sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006663sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006664sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006665sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006667sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000666Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000066A0sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000066A1sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000066A2sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000066A3sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000066A7sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000066AFsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006780sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006784sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006788sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000678Asv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006790sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006791sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006792sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006798sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006799sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000679Asv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000679Bsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000679Esv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000679Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067A0sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067A1sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067A2sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067A8sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067A9sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067AAsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067B0sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067B1sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067B8sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067B9sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067BAsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067BEsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067C0sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067C1sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067C2sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067C4sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067C7sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067C8sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067C9sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067CAsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067CCsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067CFsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067D0sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067DFsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067E0sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067E1sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067E3sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067E7sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067E8sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067E9sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067EBsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067EFsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000067FFsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006800sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006801sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006802sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006806sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006808sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006809sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006810sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006811sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006816sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006817sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006818sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006819sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006820sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006821sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006822sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006823sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006824sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006825sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006826sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006827sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006828sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006829sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000682Asv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000682Bsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000682Csv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000682Dsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000682Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006830sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006831sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006835sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006837sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006838sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006839sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000683Bsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000683Dsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000683Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006860sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006861sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006862sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006863sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006864sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006867sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006868sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000686Csv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000687Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006900sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006901sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006902sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006903sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006907sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006920sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006921sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006928sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006929sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000692Bsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000692Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006930sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006938sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006939sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000694Csv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000694Esv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006980sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006981sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006985sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006986sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006987sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006995sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006997sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000699Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000069A0sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000069A1sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000069A2sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000069A3sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000069AFsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00006FDFsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00007300sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000730Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009830sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009831sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009832sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009833sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009834sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009835sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009836sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009837sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009838sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009839sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000983Asv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000983Bsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000983Csv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000983Dsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000983Esv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000983Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009850sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009851sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009852sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009853sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009854sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009855sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009856sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009857sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009858sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009859sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000985Asv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000985Bsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000985Csv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000985Dsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000985Esv*sd*bc*sc*i* amdgpu
alias pci:v00001002d0000985Fsv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009870sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009874sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009875sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009876sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d00009877sv*sd*bc*sc*i* amdgpu
alias pci:v00001002d000098E4sv*sd*bc*sc*i* amdgpu
alias symbol:amdkfd_query_rdma_interface amdgpu
alias symbol:kgd2kfd_init amdgpu
```

```
$ uname -a
Linux <computer name> 4.15.0-43-generic #46-Ubuntu SMP Thu Dec 6 14:45:28 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

```
$ dkms status
amdgpu, 2.0-89, 4.15.0-43-generic, x86_64: installed
```

```
$ /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104
```

```
$ dmesg | grep kfd
[    1.359009] kfd kfd: Initialized module
[    1.628875] amdgpu 0000:01:00.0: kfd not supported on this ASIC
```


---

## 评论 (11 条)

### 评论 #1 — jlgreathouse (2019-01-09T17:03:59Z)

Could you show the output of `modinfo amdgpu` and `modinfo amdkfd`?

---

### 评论 #2 — awenocur (2019-01-09T18:43:33Z)

```
$ modinfo amdgpu
filename:       /lib/modules/4.15.0-43-generic/updates/dkms/amdgpu.ko
version:        19.10.0.418
license:        GPL and additional rights
description:    AMD GPU
author:         AMD linux driver team
firmware:       amdgpu/raven2_gpu_info.bin
firmware:       amdgpu/picasso_gpu_info.bin
firmware:       amdgpu/raven_gpu_info.bin
firmware:       amdgpu/vega12_gpu_info.bin
firmware:       amdgpu/vega10_gpu_info.bin
firmware:       amdgpu/hawaii_k_smc.bin
firmware:       amdgpu/hawaii_smc.bin
firmware:       amdgpu/bonaire_k_smc.bin
firmware:       amdgpu/bonaire_smc.bin
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
firmware:       amdgpu/topaz_mc.bin
firmware:       amdgpu/hawaii_mc.bin
firmware:       amdgpu/bonaire_mc.bin
firmware:       amdgpu/polaris12_mc.bin
firmware:       amdgpu/polaris10_mc.bin
firmware:       amdgpu/polaris11_mc.bin
firmware:       amdgpu/tonga_mc.bin
firmware:       amdgpu/vega12_asd.bin
firmware:       amdgpu/vega12_sos.bin
firmware:       amdgpu/vega10_asd.bin
firmware:       amdgpu/vega10_sos.bin
firmware:       amdgpu/raven2_asd.bin
firmware:       amdgpu/picasso_asd.bin
firmware:       amdgpu/raven_asd.bin
firmware:       amdgpu/vega20_ta.bin
firmware:       amdgpu/vega20_sos_old.bin
firmware:       amdgpu/vega20_sos.bin
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
firmware:       amdgpu/raven2_rlc.bin
firmware:       amdgpu/raven2_mec2.bin
firmware:       amdgpu/raven2_mec.bin
firmware:       amdgpu/raven2_me.bin
firmware:       amdgpu/raven2_pfp.bin
firmware:       amdgpu/raven2_ce.bin
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
firmware:       amdgpu/raven2_sdma.bin
firmware:       amdgpu/picasso_sdma.bin
firmware:       amdgpu/raven_sdma.bin
firmware:       amdgpu/vega20_sdma1.bin
firmware:       amdgpu/vega20_sdma.bin
firmware:       amdgpu/vega12_sdma1.bin
firmware:       amdgpu/vega12_sdma.bin
firmware:       amdgpu/vega10_sdma1.bin
firmware:       amdgpu/vega10_sdma.bin
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
firmware:       amdgpu/raven2_vcn.bin
firmware:       amdgpu/picasso_vcn.bin
firmware:       amdgpu/raven_vcn.bin
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
firmware:       amdgpu/raven_dmcu.bin
srcversion:     533BB7E5866E52F63B9ACCB
alias:          pci:v00001002d000015D8sv*sd*bc*sc*i*
alias:          pci:v00001002d000015DDsv*sd*bc*sc*i*
alias:          pci:v00001002d000066AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000066A7sv*sd*bc*sc*i*
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
alias:          pci:v00001002d0000686Csv*sd*bc*sc*i*
alias:          pci:v00001002d00006868sv*sd*bc*sc*i*
alias:          pci:v00001002d00006867sv*sd*bc*sc*i*
alias:          pci:v00001002d00006864sv*sd*bc*sc*i*
alias:          pci:v00001002d00006863sv*sd*bc*sc*i*
alias:          pci:v00001002d00006862sv*sd*bc*sc*i*
alias:          pci:v00001002d00006861sv*sd*bc*sc*i*
alias:          pci:v00001002d00006860sv*sd*bc*sc*i*
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
depends:        amdchash,amdttm,amdkcl,drm_kms_helper,drm,amd_iommu_v2,amd-sched,i2c-algo-bit
retpoline:      Y
name:           amdgpu
vermagic:       4.15.0-43-generic SMP mod_unload 
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
parm:           sched_jobs:the max number of jobs supported in the sw queue (default 32) (int)
parm:           sched_hw_submission:the max number of HW submissions (default 2) (int)
parm:           ppfeaturemask:all power features enabled (default)) (uint)
parm:           no_evict:Support pinning request from user space (1 = enable, 0 = disable (default)) (int)
parm:           direct_gma_size:Direct GMA size in megabytes (max 96MB) (int)
parm:           ssg:SSG support (1 = enable, 0 = disable (default)) (int)
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
parm:           gpu_recovery:Enable GPU recovery mechanism, (1 = enable, 0 = disable, -1 = auto) (int)
parm:           emu_mode:Emulation mode, (1 = enable, 0 = disable) (int)
parm:           priv_cp_queues:Enable privileged mode for CP queues (0 = off (default), 1 = on) (int)
parm:           keep_idle_process_evicted:Restore evicted process only if queues are active (N = off(default), Y = on) (bool)
parm:           cma_enable:Enable CMA (1 = enable, 0 = disable (default)). Warning! relaxed access check (int)
parm:           si_support:SI support (1 = enabled (default), 0 = disabled) (int)
parm:           cik_support:CIK support (1 = enabled (default), 0 = disabled) (int)
parm:           smu_memory_pool_size:reserve gtt for smu debug usage, 0 = disable,0x1 = 256Mbyte, 0x2 = 512Mbyte, 0x4 = 1 Gbyte, 0x8 = 2GByte (uint)
parm:           sched_policy:Scheduling policy (0 = HWS (Default), 1 = HWS without over-subscription, 2 = Non-HWS (Used for debugging only) (int)
parm:           hws_max_conc_proc:Max # processes HWS can execute concurrently when sched_policy=0 (0 = no concurrency, #VMIDs for KFD = Maximum(default)) (int)
parm:           cwsr_enable:CWSR enable (0 = Off, 1 = On (Default)) (int)
parm:           max_num_of_queues_per_device:Maximum number of supported queues per device (1 = Minimum, 4096 = default) (int)
parm:           send_sigterm:Send sigterm to HSA process on unhandled exception (0 = disable, 1 = enable) (int)
parm:           debug_largebar:Debug large-bar flag used to simulate large-bar capability on non-large bar machine (0 = disable, 1 = enable) (int)
parm:           ignore_crat:Ignore CRAT table during KFD initialization (0 = use CRAT (default), 1 = ignore CRAT) (int)
parm:           noretry:Set sh_mem_config.retry_disable on Vega10 (0 = retry enabled (default), 1 = retry disabled) (int)
parm:           halt_if_hws_hang:Halt if HWS hang is detected (0 = off (default), 1 = on) (int)
parm:           pcie_p2p:Enable PCIe P2P (requires large-BAR). (N = off, Y = on(default)) (bool)
parm:           dcfeaturemask:all stable DC features enabled (default)) (uint)
```

```
$ modinfo amdkfd
filename:       /lib/modules/4.15.0-43-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
version:        0.7.2
license:        GPL and additional rights
description:    Standalone HSA driver for AMD's GPUs
author:         AMD Inc. and others
srcversion:     E88AFF52E3B4054EE5780DB
depends:        amd_iommu_v2
retpoline:      Y
intree:         Y
name:           amdkfd
vermagic:       4.15.0-43-generic SMP mod_unload 
signat:         PKCS#7
signer:         
sig_key:        
sig_hashalgo:   md4
parm:           sched_policy:Scheduling policy (0 = HWS (Default), 1 = HWS without over-subscription, 2 = Non-HWS (Used for debugging only) (int)
parm:           max_num_of_queues_per_device:Maximum number of supported queues per device (1 = Minimum, 4096 = default) (int)
parm:           send_sigterm:Send sigterm to HSA process on unhandled exception (0 = disable, 1 = enable) (int)
```

---

### 评论 #3 — jlgreathouse (2019-01-09T20:31:26Z)

And could I also see the output of `lspci -n | grep 01:00.0`?

Also, to verify, you've rebooted after installing the DKMS module, correct?

---

### 评论 #4 — awenocur (2019-01-09T20:32:27Z)

```
$ lspci -n | grep 01:00.0
01:00.0 0300: 1002:7300 (rev cb)
```

---

### 评论 #5 — awenocur (2019-01-09T20:32:50Z)

yes; I rebooted after installing DKMS

---

### 评论 #6 — jlgreathouse (2019-01-09T22:02:50Z)

Sorry to keep asking questions -- this is a bit odd, because it *looks* like you're running the correct version of `amdgpu`, but I can't figure out a way to make it through the code with your GPU that would result in the output you're seeing. `amdkfd` is no longer installed as a separate module, so [the code that prints out "kfd: Initialized module"](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.2/drivers/gpu/drm/amd/amdkfd/kfd_module.c#L176) in 1.9.2 and below [no longer exists as of ROCm 2.0](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/amdkfd/kfd_module.c).

Fiji [is very obviously supported](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd.c#L88) in the function that prints out the "kfd not supported on this ASIC" message.

Could you show me the outputs of:
- `lsmod | grep amd`
- `dmesg | grep amd`

---

### 评论 #7 — awenocur (2019-01-09T22:48:52Z)

```
$ lsmod | grep amd
amdkfd                180224  1
amd_iommu_v2           20480  1 amdkfd
amdgpu               2703360  31
chash                  16384  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   106496  1 amdgpu
drm_kms_helper        172032  1 amdgpu
drm                   401408  11 drm_kms_helper,amdgpu,ttm
```

```
$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-43-generic (buildd@lgw01-amd64-001) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #46-Ubuntu SMP Thu Dec 6 14:45:28 UTC 2018 (Ubuntu 4.15.0-43.46-generic 4.15.18)
[    1.144269] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[    1.329919] [drm] amdgpu kernel modesetting enabled.
[    1.334570] fb: switching to amdgpudrmfb from EFI VGA
[    1.335299] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.335382] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    1.335383] amdgpu 0000:01:00.0: GTT: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
[    1.335596] [drm] amdgpu: 4096M of VRAM memory ready
[    1.335596] [drm] amdgpu: 4096M of GTT memory ready.
[    1.335693] amdgpu 0000:01:00.0: amdgpu: using MSI.
[    1.335705] [drm] amdgpu: irq initialized.
[    1.335720] amdgpu: [powerplay] amdgpu: powerplay sw initialized
[    1.335960] amdgpu 0000:01:00.0: fence driver on ring 0 use gpu addr 0x0000000000400040, cpu addr 0x        (ptrval)
[    1.336188] amdgpu 0000:01:00.0: fence driver on ring 1 use gpu addr 0x00000000004000c0, cpu addr 0x        (ptrval)
[    1.336291] amdgpu 0000:01:00.0: fence driver on ring 2 use gpu addr 0x0000000000400140, cpu addr 0x        (ptrval)
[    1.336390] amdgpu 0000:01:00.0: fence driver on ring 3 use gpu addr 0x00000000004001c0, cpu addr 0x        (ptrval)
[    1.336473] amdgpu 0000:01:00.0: fence driver on ring 4 use gpu addr 0x0000000000400240, cpu addr 0x        (ptrval)
[    1.336561] amdgpu 0000:01:00.0: fence driver on ring 5 use gpu addr 0x00000000004002c0, cpu addr 0x        (ptrval)
[    1.336654] amdgpu 0000:01:00.0: fence driver on ring 6 use gpu addr 0x0000000000400340, cpu addr 0x        (ptrval)
[    1.336704] amdgpu 0000:01:00.0: fence driver on ring 7 use gpu addr 0x00000000004003c0, cpu addr 0x        (ptrval)
[    1.336747] amdgpu 0000:01:00.0: fence driver on ring 8 use gpu addr 0x0000000000400440, cpu addr 0x        (ptrval)
[    1.336760] amdgpu 0000:01:00.0: fence driver on ring 9 use gpu addr 0x00000000004004e0, cpu addr 0x        (ptrval)
[    1.337248] amdgpu 0000:01:00.0: fence driver on ring 10 use gpu addr 0x0000000000400560, cpu addr 0x        (ptrval)
[    1.337293] amdgpu 0000:01:00.0: fence driver on ring 11 use gpu addr 0x00000000004005e0, cpu addr 0x        (ptrval)
[    1.337881] amdgpu 0000:01:00.0: fence driver on ring 12 use gpu addr 0x000000f40034d210, cpu addr 0x        (ptrval)
[    1.337993] amdgpu 0000:01:00.0: fence driver on ring 13 use gpu addr 0x00000000004006e0, cpu addr 0x        (ptrval)
[    1.338082] amdgpu 0000:01:00.0: fence driver on ring 14 use gpu addr 0x0000000000400760, cpu addr 0x        (ptrval)
[    1.338166] amdgpu 0000:01:00.0: fence driver on ring 15 use gpu addr 0x00000000004007e0, cpu addr 0x        (ptrval)
[    1.577515] fbcon: amdgpudrmfb (fb0) is primary device
[    1.577603] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    1.600511] amdgpu 0000:01:00.0: kfd not supported on this ASIC
[    1.600519] [drm] Initialized amdgpu 3.23.0 20150101 for 0000:01:00.0 on minor 0
[ 2174.798710] audit: type=1400 audit(1547066689.979:53): apparmor="ALLOWED" operation="open" profile="libreoffice-soffice" name="/usr/share/libdrm/amdgpu.ids" pid=5421 comm="soffice.bin" requested_mask="r" denied_mask="r" fsuid=1000 ouid=0
[ 2194.279541] audit: type=1400 audit(1547066709.459:55): apparmor="ALLOWED" operation="open" profile="libreoffice-soffice" name="/usr/share/libdrm/amdgpu.ids" pid=5562 comm="soffice.bin" requested_mask="r" denied_mask="r" fsuid=1000 ouid=0
```

---

### 评论 #8 — jlgreathouse (2019-01-10T00:25:59Z)

Yeah, I see at least two problems:
1. You should not have an `amdkfd` module loaded. This was merged into the `amdgpu` module as of ROCm 2.0.
2. Your `amdgpu` module is not the correct size for the one built in ROCm 2.0 (it should be something like ~3 MB)

Could you try doing `sudo update-initramfs -u` and rebooting?

---

### 评论 #9 — awenocur (2019-01-10T00:58:43Z)

I thought I saw the dpkg hooks take care of that. I'll report back after rebooting. Here's the output when I try it manually:

```
$ sudo update-initramfs -u
update-initramfs: Generating /boot/initrd.img-4.15.0-43-generic
W: Possible missing firmware /lib/firmware/amdgpu/raven2_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/si58_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/banks_k_2_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hainan_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/oland_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/verde_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_k_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/pitcairn_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/tahiti_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_mc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_asd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sos.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_asd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_asd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_vcn.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_vcn.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_smc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_smc.bin for module amdgpu
```


---

### 评论 #10 — awenocur (2019-01-10T01:52:19Z)

…and there appears to be no difference

I'll poke around my bootloader config to see whether it might be loading the wrong RAM  disk.

---

### 评论 #11 — awenocur (2019-01-10T01:55:45Z)

Thanks for helping me diagnose a problem with REFind. I guess the naming convention for the old image is confusing it, and it's loading it despite the new one being specified in the config file. I didn't see that until I manually looked at the kernel flags when booting.

---
