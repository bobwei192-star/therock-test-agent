# dkms not recognizing Fiji card

- **Issue #:** 667
- **State:** closed
- **Created:** 2019-01-09T16:14:48Z
- **Updated:** 2019-01-10T01:55:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/667

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
