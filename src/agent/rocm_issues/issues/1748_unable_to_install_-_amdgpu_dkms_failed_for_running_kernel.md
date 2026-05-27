# unable to install - amdgpu dkms failed for running kernel

> **Issue #1748**
> **状态**: closed
> **创建时间**: 2022-06-03T08:01:10Z
> **更新时间**: 2024-01-26T04:22:39Z
> **关闭时间**: 2024-01-26T04:22:39Z
> **作者**: Hypernoot
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1748

## 描述

I use Ubuntu 20.04.

I used this installation guide: https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.1.3/page/How_to_Install_ROCm.html#d20e4009

I downloaded the installer and installed it.

Then I ran: `sudo amdgpu-install --usecase=rocm` The installation apparently failed with this output:
```
Loading new amdgpu-5.13.20.22.10-1420322 DKMS files...
Building for 5.4.0-113-generic
Building for architecture x86_64
Building initial module for 5.4.0-113-generic
Secure Boot not enabled on this system.
Done.
Forcing installation of amdgpu

amdgpu.ko:
Running module version sanity check.
 - Original module
   - This kernel never originally had a module by this name
 - Installation
   - Installing to /lib/modules/5.4.0-113-generic/updates/dkms/

amdttm.ko:
Running module version sanity check.
 - Original module
   - This kernel never originally had a module by this name
 - Installation
   - Installing to /lib/modules/5.4.0-113-generic/updates/dkms/

amdkcl.ko:
Running module version sanity check.
 - Original module
   - This kernel never originally had a module by this name
 - Installation
   - Installing to /lib/modules/5.4.0-113-generic/updates/dkms/

amd-sched.ko:
Running module version sanity check.
 - Original module
   - This kernel never originally had a module by this name
 - Installation
   - Installing to /lib/modules/5.4.0-113-generic/updates/dkms/

amddrm_ttm_helper.ko:
Running module version sanity check.
 - Original module
   - This kernel never originally had a module by this name
 - Installation
   - Installing to /lib/modules/5.4.0-113-generic/updates/dkms/

Running the post_install script:

depmod...........

DKMS: install completed.
update-initramfs: Generating /boot/initrd.img-5.4.0-113-generic
W: Possible missing firmware /lib/firmware/amdgpu/yellow_carp_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vangogh_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/ip_discovery.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega10_cap.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/navi12_cap.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/psp_13_0_8_ta.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/psp_13_0_8_toc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/psp_13_0_8_asd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/sdma_5_2_7.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/navi10_mes.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/dcn_3_1_6_dmcub.bin for module amdgpu
Nastavuje se balík rocm-core (5.1.3.50103-66) …
update-alternatives: používám /opt/rocm-5.1.3 pro poskytnutí /opt/rocm (rocm) v automatickém režimu
Nastavuje se balík hip-dev (5.1.20532.50103-66) …
Nastavuje se balík rocm-llvm (14.0.0.22114.50103-66) …
Nastavuje se balík hip-runtime-amd (5.1.20532.50103-66) …
Nastavuje se balík rocm-dev (5.1.3.50103-66) …
/opt/rocm-5.1.3/bin/ca not found, but that is OK
/opt/rocm-5.1.3/bin/clang-ocl not found, but that is OK
/opt/rocm-5.1.3/bin/extractkernel not found, but that is OK
/opt/rocm-5.1.3/bin/findcode.sh not found, but that is OK
/opt/rocm-5.1.3/bin/finduncodep.sh not found, but that is OK
update-alternatives: používám /opt/rocm-5.1.3/bin/hipcc pro poskytnutí /usr/bin/hipcc (hipcc) v automatickém režimu
update-alternatives: používám /opt/rocm-5.1.3/bin/hipcc.pl pro poskytnutí /usr/bin/hipcc.pl (hipcc.pl) v automatickém režimu
/opt/rocm-5.1.3/bin/hipcc.bin not found, but that is OK
update-alternatives: používám /opt/rocm-5.1.3/bin/hipcc_cmake_linker_helper pro poskytnutí /usr/bin/hipcc_cmake_linker_helper (hipcc_cmake_linker_helper) v automatickém režimu
update-alternatives: používám /opt/rocm-5.1.3/bin/hipconfig pro poskytnutí /usr/bin/hipconfig (hipconfig) v automatickém režimu
update-alternatives: používám /opt/rocm-5.1.3/bin/hipconfig.pl pro poskytnutí /usr/bin/hipconfig.pl (hipconfig.pl) v automatickém režimu
/opt/rocm-5.1.3/bin/hipconfig.bin not found, but that is OK
/opt/rocm-5.1.3/bin/hipconvertinplace-perl.sh not found, but that is OK
/opt/rocm-5.1.3/bin/hipconvertinplace.sh not found, but that is OK
update-alternatives: používám /opt/rocm-5.1.3/bin/hipdemangleatp pro poskytnutí /usr/bin/hipdemangleatp (hipdemangleatp) v automatickém režimu
/opt/rocm-5.1.3/bin/hipexamine-perl.sh not found, but that is OK
/opt/rocm-5.1.3/bin/hipexamine.sh not found, but that is OK
/opt/rocm-5.1.3/bin/hipify-cmakefile not found, but that is OK
/opt/rocm-5.1.3/bin/hipify-perl not found, but that is OK
/opt/rocm-5.1.3/bin/lpl not found, but that is OK
/opt/rocm-5.1.3/bin/rocgdb not found, but that is OK
/opt/rocm-5.1.3/bin/rocm_agent_enumerator not found, but that is OK
/opt/rocm-5.1.3/bin/rocminfo not found, but that is OK
/opt/rocm-5.1.3/bin/rocm-smi not found, but that is OK
/opt/rocm-5.1.3/bin/rocprof not found, but that is OK
Error! Could not locate dkms.conf file.
File: /var/lib/dkms/amdgpu/5.13.11.21.50-1373630/source/dkms.conf does not exist.
WARNING: amdgpu dkms failed for running kernel
```

The output of `lspci -vvv | grep Radeon` is:
```
01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Sun XT [Radeon HD 8670A/8670M/8690M / R5 M330 / M430 / Radeon 520 Mobile] (rev 83)
	Subsystem: Lenovo Radeon R5 M430
```

Any help is appreciated.

---

## 评论 (12 条)

### 评论 #1 — xuhuisheng (2022-06-03T09:30:23Z)

I am afraid that you need use kernel-5.13

---

### 评论 #2 — Hypernoot (2022-06-03T12:43:57Z)

Now I have kernel `Linux 5.13.11-051311-generic`. When I type `uname -sr`, I see exactly this.

When I type `sudo amdgpu-install --usecase=rocm`, it throws this error:
```
Balík linux-headers-5.13.11-051311-generic není dostupný, ale jiný balík se na něj odkazuje.
To může znamenat že balík chybí, byl zastarán, nebo je dostupný
pouze z jiného zdroje

E: Balík „linux-headers-5.13.11-051311-generic“ nemá kandidáta pro instalaci
```
i.e. package `linux-headers-5.13.11-051311-generic` is not available and it has no candidate for install.

---

### 评论 #3 — sinix-del (2022-06-03T14:39:45Z)

Install 5.11 image / headers / modules ,

sudo apt install linux-modules-5.11.0-46-generic linux-modules-extra-5.11.0-46-generic linux-hwe-5.11-headers-5.11.0-46

after that instal rocm.

---

### 评论 #4 — Hypernoot (2022-06-03T17:53:47Z)

I just installed these packages and still the same error appears.

---

### 评论 #5 — sinix-del (2022-06-03T18:55:37Z)

That is not package that is older kernel, are you sure that you boot in 5.11 ?
uname -a

---

### 评论 #6 — Hypernoot (2022-06-03T19:03:47Z)

`uname -a` says:
```
Linux asw-komp 5.13.11-051311-generic #202108151332 SMP Sun Aug 15 13:57:01 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

---

### 评论 #7 — sinix-del (2022-06-03T19:32:15Z)

remove 5.13.11 image / headers / modules with autoremove and reboot. 
uname -a again, if 5.11 -generic, install rocm

---

### 评论 #8 — Hypernoot (2022-06-04T08:15:49Z)

fyi `sudo apt autoremove` didn't remove any packages. But I managed to boot an older kernel anyway.

Now uname -a shows:
```
Linux asw-komp 5.11.0-46-generic #51~20.04.1-Ubuntu SMP Fri Jan 7 06:51:40 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```

Now I got a bit further with the installation but it still doesn't seem successful. The output of `sudo amdgpu-install --usecase=rocm` is:
```
Mám:1 http://cz.archive.ubuntu.com/ubuntu focal InRelease
Mám:2 http://cz.archive.ubuntu.com/ubuntu focal-updates InRelease              
Mám:3 http://cz.archive.ubuntu.com/ubuntu focal-backports InRelease            
Mám:4 http://security.ubuntu.com/ubuntu focal-security InRelease               
Mám:5 http://archive.canonical.com focal InRelease                             
Mám:6 http://ppa.launchpad.net/cappelikan/ppa/ubuntu focal InRelease           
Mám:7 https://packages.riot.im/debian default InRelease                        
Mám:8 https://repo.radeon.com/amdgpu/22.10.3/ubuntu focal InRelease      
Mám:9 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu InRelease
Načítají se seznamy balíků… Hotovo
Načítají se seznamy balíků… Hotovo
Vytváří se strom závislostí       
Načítají se stavové informace… Hotovo
linux-headers-5.11.0-46-generic je již nejnovější verze (5.11.0-46.51~20.04.1).
Následující dodatečné balíky budou instalovány:
  amdgpu-core amdgpu-dkms-firmware comgr dctrl-tools dkms hip-dev hip-doc
  hip-runtime-amd hip-samples hsa-amd-aqlprofile hsa-rocr hsa-rocr-dev
  hsakmt-roct-dev libdrm-amdgpu-amdgpu1 libdrm-amdgpu-common libdrm2-amdgpu
  libelf-dev libfile-which-perl liburi-encode-perl openmp-extras
  rocm-clang-ocl rocm-cmake rocm-core rocm-dbgapi rocm-debug-agent
  rocm-device-libs rocm-gdb rocm-llvm rocm-ocl-icd rocm-opencl rocm-opencl-dev
  rocm-smi-lib rocm-utils rocminfo rocprofiler-dev roctracer-dev
Navrhované balíky:
  debtags menu
Následující NOVÉ balíky budou nainstalovány:
  amdgpu-core amdgpu-dkms amdgpu-dkms-firmware comgr dctrl-tools dkms hip-dev
  hip-doc hip-runtime-amd hip-samples hsa-amd-aqlprofile hsa-rocr hsa-rocr-dev
  hsakmt-roct-dev libdrm-amdgpu-amdgpu1 libdrm-amdgpu-common libdrm2-amdgpu
  libelf-dev libfile-which-perl liburi-encode-perl openmp-extras
  rocm-clang-ocl rocm-cmake rocm-core rocm-dbgapi rocm-debug-agent rocm-dev
  rocm-device-libs rocm-gdb rocm-llvm rocm-ocl-icd rocm-opencl rocm-opencl-dev
  rocm-smi-lib rocm-utils rocminfo rocprofiler-dev roctracer-dev
0 aktualizováno, 38 nově instalováno, 0 k odstranění a 0 neaktualizováno.
Nutno stáhnout 115 MB/811 MB archivů.
Po této operaci bude na disku použito dalších 826 MB.
Chcete pokračovat? [Y/n] y
Stahuje se:1 http://cz.archive.ubuntu.com/ubuntu focal/universe amd64 liburi-encode-perl all 1.1.1-1 [9 464 B]
Stahuje se:2 https://repo.radeon.com/amdgpu/22.10.3/ubuntu focal/main amd64 amdgpu-core all 22.10.3.50103-1420322 [2 228 B]
Stahuje se:3 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 comgr amd64 2.4.0.50103-66 [44,8 MB]
Stahuje se:4 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 hip-doc amd64 5.1.20532.50103-66 [1 076 kB]
Stahuje se:5 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 hsakmt-roct-dev amd64 20220128.1.7.50103-66 [313 kB]
Stahuje se:6 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 hsa-rocr amd64 1.5.0.50103-66 [693 kB]
Stahuje se:7 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 hsa-rocr-dev amd64 1.5.0.50103-66 [93,4 kB]
Stahuje se:8 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocminfo amd64 1.0.0.50103-66 [28,8 kB]
Stahuje se:9 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 hip-samples amd64 5.1.20532.50103-66 [104 kB]
Stahuje se:10 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 hsa-amd-aqlprofile amd64 1.0.0.50103-66 [143 kB]
Stahuje se:11 https://repo.radeon.com/amdgpu/22.10.3/ubuntu focal/main amd64 libdrm2-amdgpu amd64 1:2.4.109.50103-1420322 [38,5 kB]
Stahuje se:12 https://repo.radeon.com/amdgpu/22.10.3/ubuntu focal/main amd64 libdrm-amdgpu-common all 1.0.0.50103-1420322 [4 876 B]
Stahuje se:13 https://repo.radeon.com/amdgpu/22.10.3/ubuntu focal/main amd64 libdrm-amdgpu-amdgpu1 amd64 1:2.4.109.50103-1420322 [21,0 kB]
Stahuje se:14 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-device-libs amd64 1.0.0.50103-66 [762 kB]
Stahuje se:15 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 openmp-extras amd64 13.51.0.50103-66 [23,2 MB]
Stahuje se:16 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-ocl-icd amd64 2.0.0.50103-66 [15,6 kB]
Stahuje se:17 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-opencl amd64 2.0.0.50103-66 [546 kB]
Stahuje se:18 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-opencl-dev amd64 2.0.0.50103-66 [124 kB]
Stahuje se:19 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-clang-ocl amd64 0.5.0.50103-66 [2 504 B]
Stahuje se:20 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-cmake amd64 0.7.2.50103-66 [20,3 kB]
Stahuje se:21 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-dbgapi amd64 0.64.0.50103-66 [1 606 kB]
Stahuje se:22 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-debug-agent amd64 2.0.3.50103-66 [57,0 kB]
Stahuje se:23 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-gdb amd64 11.2.50103-66 [39,9 MB]
Stahuje se:24 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-smi-lib amd64 5.0.0.50103-66 [982 kB]
Stahuje se:25 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocm-utils amd64 5.1.3.50103-66 [794 B]
Stahuje se:26 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 rocprofiler-dev amd64 1.0.0.50103-66 [253 kB]
Stahuje se:27 https://repo.radeon.com/rocm/apt/5.1.3 ubuntu/main amd64 roctracer-dev amd64 1.0.0.50103-66 [334 kB]
Staženo 115 MB za 53s (2 167 kB/s)                                             
Extrahují se šablony z balíků: 100%
Vybírá se dosud nevybraný balík amdgpu-dkms-firmware.
(Načítá se databáze … nyní je nainstalováno 445132 souborů a adresářů.)
Připravuje se nahrazení …/amdgpu-dkms-firmware_1%3a5.13.20.22.10.50103-1420322_all.deb …
Rozbaluje se amdgpu-dkms-firmware (1:5.13.20.22.10.50103-1420322) …
Vybírá se dosud nevybraný balík dctrl-tools.
Připravuje se nahrazení …/dctrl-tools_2.24-3_amd64.deb …
Rozbaluje se dctrl-tools (2.24-3) …
Vybírá se dosud nevybraný balík dkms.
Připravuje se nahrazení …/dkms_2.8.1-5ubuntu2_all.deb …
Rozbaluje se dkms (2.8.1-5ubuntu2) …
Nastavuje se balík amdgpu-dkms-firmware (1:5.13.20.22.10.50103-1420322) …
Vybírá se dosud nevybraný balík amdgpu-dkms.
(Načítá se databáze … nyní je nainstalováno 445659 souborů a adresářů.)
Připravuje se nahrazení …/00-amdgpu-dkms_1%3a5.13.20.22.10.50103-1420322_all.deb …
Rozbaluje se amdgpu-dkms (1:5.13.20.22.10.50103-1420322) …
Vybírá se dosud nevybraný balík amdgpu-core.
Připravuje se nahrazení …/01-amdgpu-core_22.10.3.50103-1420322_all.deb …
Rozbaluje se amdgpu-core (22.10.3.50103-1420322) …
Vybírá se dosud nevybraný balík rocm-core.
Připravuje se nahrazení …/02-rocm-core_5.1.3.50103-66_amd64.deb …
Rozbaluje se rocm-core (5.1.3.50103-66) …
Vybírá se dosud nevybraný balík comgr.
Připravuje se nahrazení …/03-comgr_2.4.0.50103-66_amd64.deb …
Rozbaluje se comgr (2.4.0.50103-66) …
Vybírá se dosud nevybraný balík liburi-encode-perl.
Připravuje se nahrazení …/04-liburi-encode-perl_1.1.1-1_all.deb …
Rozbaluje se liburi-encode-perl (1.1.1-1) …
Vybírá se dosud nevybraný balík libfile-which-perl.
Připravuje se nahrazení …/05-libfile-which-perl_1.23-1_all.deb …
Rozbaluje se libfile-which-perl (1.23-1) …
Vybírá se dosud nevybraný balík hip-dev.
Připravuje se nahrazení …/06-hip-dev_5.1.20532.50103-66_amd64.deb …
Rozbaluje se hip-dev (5.1.20532.50103-66) …
Vybírá se dosud nevybraný balík hip-doc.
Připravuje se nahrazení …/07-hip-doc_5.1.20532.50103-66_amd64.deb …
Rozbaluje se hip-doc (5.1.20532.50103-66) …
Vybírá se dosud nevybraný balík hsakmt-roct-dev.
Připravuje se nahrazení …/08-hsakmt-roct-dev_20220128.1.7.50103-66_amd64.deb …
Rozbaluje se hsakmt-roct-dev (20220128.1.7.50103-66) …
Vybírá se dosud nevybraný balík hsa-rocr.
Připravuje se nahrazení …/09-hsa-rocr_1.5.0.50103-66_amd64.deb …
Rozbaluje se hsa-rocr (1.5.0.50103-66) …
Vybírá se dosud nevybraný balík hsa-rocr-dev.
Připravuje se nahrazení …/10-hsa-rocr-dev_1.5.0.50103-66_amd64.deb …
Rozbaluje se hsa-rocr-dev (1.5.0.50103-66) …
Vybírá se dosud nevybraný balík rocminfo.
Připravuje se nahrazení …/11-rocminfo_1.0.0.50103-66_amd64.deb …
Rozbaluje se rocminfo (1.0.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-llvm.
Připravuje se nahrazení …/12-rocm-llvm_14.0.0.22114.50103-66_amd64.deb …
Rozbaluje se rocm-llvm (14.0.0.22114.50103-66) …
Vybírá se dosud nevybraný balík hip-runtime-amd.
Připravuje se nahrazení …/13-hip-runtime-amd_5.1.20532.50103-66_amd64.deb …
Rozbaluje se hip-runtime-amd (5.1.20532.50103-66) …
Vybírá se dosud nevybraný balík hip-samples.
Připravuje se nahrazení …/14-hip-samples_5.1.20532.50103-66_amd64.deb …
Rozbaluje se hip-samples (5.1.20532.50103-66) …
Vybírá se dosud nevybraný balík hsa-amd-aqlprofile.
Připravuje se nahrazení …/15-hsa-amd-aqlprofile_1.0.0.50103-66_amd64.deb …
Rozbaluje se hsa-amd-aqlprofile (1.0.0.50103-66) …
Vybírá se dosud nevybraný balík libdrm2-amdgpu:amd64.
Připravuje se nahrazení …/16-libdrm2-amdgpu_1%3a2.4.109.50103-1420322_amd64.deb …
Rozbaluje se libdrm2-amdgpu:amd64 (1:2.4.109.50103-1420322) …
Vybírá se dosud nevybraný balík libdrm-amdgpu-common.
Připravuje se nahrazení …/17-libdrm-amdgpu-common_1.0.0.50103-1420322_all.deb …
Rozbaluje se libdrm-amdgpu-common (1.0.0.50103-1420322) …
Vybírá se dosud nevybraný balík libdrm-amdgpu-amdgpu1:amd64.
Připravuje se nahrazení …/18-libdrm-amdgpu-amdgpu1_1%3a2.4.109.50103-1420322_amd64.deb …
Rozbaluje se libdrm-amdgpu-amdgpu1:amd64 (1:2.4.109.50103-1420322) …
Vybírá se dosud nevybraný balík libelf-dev:amd64.
Připravuje se nahrazení …/19-libelf-dev_0.176-1.1build1_amd64.deb …
Rozbaluje se libelf-dev:amd64 (0.176-1.1build1) …
Vybírá se dosud nevybraný balík rocm-device-libs.
Připravuje se nahrazení …/20-rocm-device-libs_1.0.0.50103-66_amd64.deb …
Rozbaluje se rocm-device-libs (1.0.0.50103-66) …
Vybírá se dosud nevybraný balík openmp-extras.
Připravuje se nahrazení …/21-openmp-extras_13.51.0.50103-66_amd64.deb …
Rozbaluje se openmp-extras (13.51.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-ocl-icd.
Připravuje se nahrazení …/22-rocm-ocl-icd_2.0.0.50103-66_amd64.deb …
Rozbaluje se rocm-ocl-icd (2.0.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-opencl.
Připravuje se nahrazení …/23-rocm-opencl_2.0.0.50103-66_amd64.deb …
Rozbaluje se rocm-opencl (2.0.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-opencl-dev.
Připravuje se nahrazení …/24-rocm-opencl-dev_2.0.0.50103-66_amd64.deb …
Rozbaluje se rocm-opencl-dev (2.0.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-clang-ocl.
Připravuje se nahrazení …/25-rocm-clang-ocl_0.5.0.50103-66_amd64.deb …
Rozbaluje se rocm-clang-ocl (0.5.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-cmake.
Připravuje se nahrazení …/26-rocm-cmake_0.7.2.50103-66_amd64.deb …
Rozbaluje se rocm-cmake (0.7.2.50103-66) …
Vybírá se dosud nevybraný balík rocm-dbgapi.
Připravuje se nahrazení …/27-rocm-dbgapi_0.64.0.50103-66_amd64.deb …
Rozbaluje se rocm-dbgapi (0.64.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-debug-agent.
Připravuje se nahrazení …/28-rocm-debug-agent_2.0.3.50103-66_amd64.deb …
Rozbaluje se rocm-debug-agent (2.0.3.50103-66) …
Vybírá se dosud nevybraný balík rocm-gdb.
Připravuje se nahrazení …/29-rocm-gdb_11.2.50103-66_amd64.deb …
Rozbaluje se rocm-gdb (11.2.50103-66) …
Vybírá se dosud nevybraný balík rocm-smi-lib.
Připravuje se nahrazení …/30-rocm-smi-lib_5.0.0.50103-66_amd64.deb …
Rozbaluje se rocm-smi-lib (5.0.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-utils.
Připravuje se nahrazení …/31-rocm-utils_5.1.3.50103-66_amd64.deb …
Rozbaluje se rocm-utils (5.1.3.50103-66) …
Vybírá se dosud nevybraný balík rocprofiler-dev.
Připravuje se nahrazení …/32-rocprofiler-dev_1.0.0.50103-66_amd64.deb …
Rozbaluje se rocprofiler-dev (1.0.0.50103-66) …
Vybírá se dosud nevybraný balík roctracer-dev.
Připravuje se nahrazení …/33-roctracer-dev_1.0.0.50103-66_amd64.deb …
Rozbaluje se roctracer-dev (1.0.0.50103-66) …
Vybírá se dosud nevybraný balík rocm-dev.
Připravuje se nahrazení …/34-rocm-dev_5.1.3.50103-66_amd64.deb …
Rozbaluje se rocm-dev (5.1.3.50103-66) …
Nastavuje se balík libfile-which-perl (1.23-1) …
Nastavuje se balík rocm-core (5.1.3.50103-66) …
update-alternatives: používám /opt/rocm-5.1.3 pro poskytnutí /opt/rocm (rocm) v automatickém režimu
Nastavuje se balík rocm-device-libs (1.0.0.50103-66) …
Nastavuje se balík liburi-encode-perl (1.1.1-1) …
Nastavuje se balík rocm-ocl-icd (2.0.0.50103-66) …
Nastavuje se balík libelf-dev:amd64 (0.176-1.1build1) …
Nastavuje se balík amdgpu-core (22.10.3.50103-1420322) …
Nastavuje se balík libdrm-amdgpu-common (1.0.0.50103-1420322) …
Nastavuje se balík rocm-smi-lib (5.0.0.50103-66) …
Nastavuje se balík hsakmt-roct-dev (20220128.1.7.50103-66) …
Nastavuje se balík dctrl-tools (2.24-3) …
Nastavuje se balík hip-dev (5.1.20532.50103-66) …
Nastavuje se balík rocm-llvm (14.0.0.22114.50103-66) …
Nastavuje se balík comgr (2.4.0.50103-66) …
Nastavuje se balík openmp-extras (13.51.0.50103-66) …
Nastavuje se balík hip-samples (5.1.20532.50103-66) …
Nastavuje se balík rocm-cmake (0.7.2.50103-66) …
Nastavuje se balík roctracer-dev (1.0.0.50103-66) …
Nastavuje se balík hsa-amd-aqlprofile (1.0.0.50103-66) …
Nastavuje se balík dkms (2.8.1-5ubuntu2) …
Nastavuje se balík amdgpu-dkms (1:5.13.20.22.10.50103-1420322) …
Removing old amdgpu-5.13.20.22.10-1420322 DKMS files...

-------- Uninstall Beginning --------
Module:  amdgpu
Version: 5.13.20.22.10-1420322
Kernel:  5.4.0-113-generic (x86_64)
-------------------------------------

Status: Before uninstall, this module version was ACTIVE on this kernel.

amdgpu.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.4.0-113-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdttm.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.4.0-113-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdkcl.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.4.0-113-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amd-sched.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.4.0-113-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amddrm_ttm_helper.ko:
 - Uninstallation
   - Deleting from: /lib/modules/5.4.0-113-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


Running the post_remove script:
depmod...................................

DKMS: uninstall completed.

------------------------------
Deleting module version: 5.13.20.22.10-1420322
completely from the DKMS tree.
------------------------------
Done.
Loading new amdgpu-5.13.20.22.10-1420322 DKMS files...
Building for 5.11.0-46-generic 5.13.11-051311-generic
Building for architecture x86_64
Building initial module for 5.11.0-46-generic
Secure Boot not enabled on this system.
Done.
Forcing installation of amdgpu

amdgpu.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.11.0-46-generic/updates/dkms/

amdttm.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.11.0-46-generic/updates/dkms/

amdkcl.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.11.0-46-generic/updates/dkms/

amd-sched.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.11.0-46-generic/updates/dkms/

amddrm_ttm_helper.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.11.0-46-generic/updates/dkms/

Running the post_install script:

depmod.................

DKMS: install completed.
Module build for kernel 5.13.11-051311-generic was skipped since the
kernel headers for this kernel does not seem to be installed.
update-initramfs: Generating /boot/initrd.img-5.11.0-46-generic
W: Possible missing firmware /lib/firmware/amdgpu/yellow_carp_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vangogh_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/ip_discovery.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega10_cap.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/navi12_cap.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/psp_13_0_8_ta.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/psp_13_0_8_toc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/psp_13_0_8_asd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/gc_10_3_7_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/sdma_5_2_7.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/navi10_mes.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/dcn_3_1_6_dmcub.bin for module amdgpu
Nastavuje se balík hsa-rocr (1.5.0.50103-66) …
Nastavuje se balík libdrm2-amdgpu:amd64 (1:2.4.109.50103-1420322) …
Nastavuje se balík rocm-dbgapi (0.64.0.50103-66) …
Nastavuje se balík rocm-opencl (2.0.0.50103-66) …
Nastavuje se balík hip-doc (5.1.20532.50103-66) …
Nastavuje se balík libdrm-amdgpu-amdgpu1:amd64 (1:2.4.109.50103-1420322) …
Nastavuje se balík rocminfo (1.0.0.50103-66) …
Nastavuje se balík hsa-rocr-dev (1.5.0.50103-66) …
Nastavuje se balík rocm-gdb (11.2.50103-66) …
Nastavuje se balík rocm-debug-agent (2.0.3.50103-66) …
Nastavuje se balík rocm-opencl-dev (2.0.0.50103-66) …
Nastavuje se balík rocprofiler-dev (1.0.0.50103-66) …
Nastavuje se balík hip-runtime-amd (5.1.20532.50103-66) …
Nastavuje se balík rocm-clang-ocl (0.5.0.50103-66) …
Nastavuje se balík rocm-utils (5.1.3.50103-66) …
Nastavuje se balík rocm-dev (5.1.3.50103-66) …
/opt/rocm-5.1.3/bin/ca not found, but that is OK
update-alternatives: používám /opt/rocm-5.1.3/bin/clang-ocl pro poskytnutí /usr/bin/clang-ocl (clang-ocl) v automatickém režimu
/opt/rocm-5.1.3/bin/extractkernel not found, but that is OK
/opt/rocm-5.1.3/bin/findcode.sh not found, but that is OK
/opt/rocm-5.1.3/bin/finduncodep.sh not found, but that is OK
update-alternatives: používám /opt/rocm-5.1.3/bin/hipcc pro poskytnutí /usr/bin/hipcc (hipcc) v automatickém režimu
update-alternatives: používám /opt/rocm-5.1.3/bin/hipcc.pl pro poskytnutí /usr/bin/hipcc.pl (hipcc.pl) v automatickém režimu
/opt/rocm-5.1.3/bin/hipcc.bin not found, but that is OK
update-alternatives: používám /opt/rocm-5.1.3/bin/hipcc_cmake_linker_helper pro poskytnutí /usr/bin/hipcc_cmake_linker_helper (hipcc_cmake_linker_helper) v automatickém režimu
update-alternatives: varování: alternativa /opt/rocm-4.3.0/bin/hipconfig (součást skupiny odkazů hipconfig) neexistuje; odebírám ze seznamu alternativ.
update-alternatives: používám /opt/rocm-5.1.3/bin/hipconfig.pl pro poskytnutí /usr/bin/hipconfig.pl (hipconfig.pl) v automatickém režimu
/opt/rocm-5.1.3/bin/hipconfig.bin not found, but that is OK
/opt/rocm-5.1.3/bin/hipconvertinplace-perl.sh not found, but that is OK
/opt/rocm-5.1.3/bin/hipconvertinplace.sh not found, but that is OK
update-alternatives: používám /opt/rocm-5.1.3/bin/hipdemangleatp pro poskytnutí /usr/bin/hipdemangleatp (hipdemangleatp) v automatickém režimu
/opt/rocm-5.1.3/bin/hipexamine-perl.sh not found, but that is OK
/opt/rocm-5.1.3/bin/hipexamine.sh not found, but that is OK
/opt/rocm-5.1.3/bin/hipify-cmakefile not found, but that is OK
/opt/rocm-5.1.3/bin/hipify-perl not found, but that is OK
/opt/rocm-5.1.3/bin/lpl not found, but that is OK
update-alternatives: používám /opt/rocm-5.1.3/bin/rocgdb pro poskytnutí /usr/bin/rocgdb (rocgdb) v automatickém režimu
update-alternatives: používám /opt/rocm-5.1.3/bin/rocm_agent_enumerator pro poskytnutí /usr/bin/rocm_agent_enumerator (rocm_agent_enumerator) v automatickém režimu
update-alternatives: používám /opt/rocm-5.1.3/bin/rocminfo pro poskytnutí /usr/bin/rocminfo (rocminfo) v automatickém režimu
update-alternatives: používám /opt/rocm-5.1.3/bin/rocm-smi pro poskytnutí /usr/bin/rocm-smi (rocm-smi) v automatickém režimu
update-alternatives: používám /opt/rocm-5.1.3/bin/rocprof pro poskytnutí /usr/bin/rocprof (rocprof) v automatickém režimu
Zpracovávají se spouštěče pro balík man-db (2.9.1-1) …
Zpracovávají se spouštěče pro balík libc-bin (2.31-0ubuntu9.9) …
Error! Could not locate dkms.conf file.
File: /var/lib/dkms/amdgpu/5.13.11.21.50-1373630/source/dkms.conf does not exist.
WARNING: amdgpu dkms failed for running kernel
```

`/opt/rocm/bin/rocminfo` shows:
```
ROCk module is loaded
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
  Name:                    Intel(R) Core(TM) i3-6100U CPU @ 2.30GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i3-6100U CPU @ 2.30GHz
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
  Max Clock Freq. (MHz):   2300                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            4                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    7860996(0x77f304) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    7860996(0x77f304) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    7860996(0x77f304) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***     
```
It lists only my CPU, not GPU.

`/opt/rocm/opencl/bin/clinfo` shows:
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3423.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```
0 devices O_O

---

### 评论 #9 — sinix-del (2022-06-04T16:11:42Z)

You have loaded some of amd-s when you try to install this version, purge all amd and rocm, reboot, and try with rocm 5.0.0. If you not succesed try clean install upgrade to 5.11 kernel and install rocm.

---

### 评论 #10 — Hypernoot (2022-06-28T12:09:30Z)

I reinstalled whole Ubuntu and tried to install ROCm 5.1.3 again. The warnings with possibly missing firmware appeared as they did before. The installation didn't throw any error. I rebooted after that. The GPU was not listed by neither `/opt/rocm/bin/rocminfo` or `/opt/rocm/opencl/bin/clinfo`

So I uninstalled ROCm completely and tried ROCm 5.0.0. I installed the installer but `sudo amdgpu-install --usecase=rocm` throws:
```
Mám:1 http://cz.archive.ubuntu.com/ubuntu focal InRelease
Mám:2 http://cz.archive.ubuntu.com/ubuntu focal-updates InRelease              
Mám:3 http://cz.archive.ubuntu.com/ubuntu focal-backports InRelease            
Mám:4 http://security.ubuntu.com/ubuntu focal-security InRelease               
Mám:5 http://ppa.launchpad.net/cappelikan/ppa/ubuntu focal InRelease           
Mám:6 https://repo.radeon.com/amdgpu/21.50/ubuntu focal InRelease            
Mám:7 https://repo.radeon.com/rocm/apt/5.0 ubuntu InRelease
Načítají se seznamy balíků… Hotovo
Načítají se seznamy balíků… Hotovo
Vytváří se strom závislostí       
Načítají se stavové informace… Hotovo
Balík linux-modules-extra-5.11.0-051100-generic není dostupný, ale jiný balík se na něj odkazuje.
To může znamenat že balík chybí, byl zastarán, nebo je dostupný
pouze z jiného zdroje

E: Balík „linux-modules-extra-5.11.0-051100-generic“ nemá kandidáta pro instalaci
```
(i.e. no candidate to install package `linux-modules-extra-5.11.0-051100-generic`)

But I made sure that I booted to kernel `5.11.0-051100-generic`

sus

---

### 评论 #11 — nartmada (2023-12-19T04:15:14Z)

Hi @Hume2, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.


---

### 评论 #12 — nartmada (2024-01-26T04:22:39Z)

Closing the ticket.  @Hume2, please re-open the ticket if the issue still exists with latest ROCm.  Thanks.

---
