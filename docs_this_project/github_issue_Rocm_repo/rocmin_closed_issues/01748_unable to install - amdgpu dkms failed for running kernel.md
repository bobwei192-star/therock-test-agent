# unable to install - amdgpu dkms failed for running kernel

- **Issue #:** 1748
- **State:** closed
- **Created:** 2022-06-03T08:01:10Z
- **Updated:** 2024-01-26T04:22:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1748

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