# rocm_agent_enumerator couldnt recognise the GPU

- **Issue #:** 223
- **State:** closed
- **Created:** 2017-10-10T11:18:06Z
- **Updated:** 2018-02-01T14:01:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/223

Hi , 

I am trying to run **_/opt/rocm/bin/rocm_agent_enumerator -t GPU_**  and getting the following output : 

**gfx000**

No GPU is being specified. I have tried updating the rocm driver but of no use.

**command** : uname -a 
**output** : Linux prasanth 4.11.0-kfd-compute-rocm-rel-1.6-148 #1 SMP Wed Aug 23 12:00:35 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux

**command** : /opt/rocm/hcc/bin/hcc --version
**output** : 
HCC clang version 6.0.0  (based on HCC 1.0.17373-bd1f35c-c639ce0-e4adac0 )
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/hcc/bin

**command** : lspci -v | grep -i amd
**output** : 
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev ca) (prog-if 00 [VGA controller])
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Radeon R9 FURY X / NANO
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8

Any inputs ?