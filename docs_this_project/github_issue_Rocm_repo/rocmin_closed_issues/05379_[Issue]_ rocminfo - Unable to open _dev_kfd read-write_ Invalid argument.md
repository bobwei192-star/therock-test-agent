# [Issue]: rocminfo - Unable to open /dev/kfd read-write: Invalid argument

- **Issue #:** 5379
- **State:** closed
- **Created:** 2025-09-18T11:35:06Z
- **Updated:** 2025-09-19T19:45:36Z
- **Labels:** Under Investigation
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5379

### Problem Description

NAME="Ubuntu"
VERSION="24.04 LTS (Noble Numbat)"
CPU:
model name      : AMD Ryzen 7 9700X 8-Core Processor
GPU:


### Operating System

Ubuntu 24.04

### CPU

AMD Ryzen 7 9700X

### GPU

AMD 9070 XT

### ROCm Version

ROCm 7.0.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
root@gpu-test-2:~#  /opt/rocm/bin/rocminfo --support
ROCk module is loaded
Unable to open /dev/kfd read-write: Invalid argument
root is member of render group
```

Hi! I'm facing issues on setting up ROCm with an unprivileged LXC Container under Proxmox with latest ROCm 7.0.1 and AMD 9070 XT. I have passed through my GPU using working tutorials.

I have the right permissions set already (root is both in video and render group).

```
root@gpu-test-2:~# groups
root video render
```

I can see both /dev/kfd and /dev/dri*:

```
root@gpu-test-2:~# ls -la /dev/kfd /dev/dri*
crw-rw-rw- 1 root render 511, 0 Sep 18 11:04 /dev/kfd

/dev/dri:
total 0
drwxr-xr-x 2 root root        80 Sep 18 11:04 .
drwxr-xr-x 7 root root       520 Sep 18 11:04 ..
crw-rw---- 1 root video 226, 128 Sep 18 11:04 renderD128
crw-rw---- 1 root video 226, 129 Sep 18 11:04 renderD129
```

I have installed it using the [official instructions](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)

I'm running Ubuntu 24.04 with Kernel 6.14.11-1:

```
root@gpu-test-2:~# uname -srmv
Linux 6.14.11-1-pve #1 SMP PREEMPT_DYNAMIC PMX 6.14.11-1 (2025-08-26T16:06Z) x86_64
root@gpu-test-2:~# uname -m && cat /etc/*release
x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=24.04
DISTRIB_CODENAME=noble
DISTRIB_DESCRIPTION="Ubuntu 24.04 LTS"
PRETTY_NAME="Ubuntu 24.04 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
```

However, whenever I'm trying to access it using rocminfo I keep getting:

```
root@gpu-test-2:~# rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Invalid argument
root is member of render group
```

**On the host:** AMD Gpu information:

```
➜  ~ dmesg | grep amdgpu
[229101.186133] amdgpu 0000:03:00.0: amdgpu: detected ip block number 0 <soc24_common>
[229101.186136] amdgpu 0000:03:00.0: amdgpu: detected ip block number 1 <gmc_v12_0>
[229101.186138] amdgpu 0000:03:00.0: amdgpu: detected ip block number 2 <ih_v7_0>
[229101.186139] amdgpu 0000:03:00.0: amdgpu: detected ip block number 3 <psp>
[229101.186140] amdgpu 0000:03:00.0: amdgpu: detected ip block number 4 <smu>
[229101.186142] amdgpu 0000:03:00.0: amdgpu: detected ip block number 5 <dm>
[229101.186143] amdgpu 0000:03:00.0: amdgpu: detected ip block number 6 <gfx_v12_0>
[229101.186144] amdgpu 0000:03:00.0: amdgpu: detected ip block number 7 <sdma_v7_0>
[229101.186146] amdgpu 0000:03:00.0: amdgpu: detected ip block number 8 <vcn_v5_0_0>
[229101.186147] amdgpu 0000:03:00.0: amdgpu: detected ip block number 9 <jpeg_v5_0_0>
[229101.186148] amdgpu 0000:03:00.0: amdgpu: detected ip block number 10 <mes_v12_0>
[229101.186167] amdgpu 0000:03:00.0: amdgpu: Fetched VBIOS from VFCT
[229101.186169] amdgpu: ATOM BIOS: 113-EXT112414-100
[229101.194722] amdgpu 0000:03:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
[229101.194751] amdgpu 0000:03:00.0: amdgpu: MEM ECC is not presented.
[229101.194753] amdgpu 0000:03:00.0: amdgpu: SRAM ECC is not presented.
[229101.194774] amdgpu 0000:03:00.0: amdgpu: VRAM: 16304M 0x0000008000000000 - 0x00000083FAFFFFFF (16304M used)
[229101.194776] amdgpu 0000:03:00.0: amdgpu: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[229101.194824] [drm] amdgpu: 16304M of VRAM memory ready
[229101.194825] [drm] amdgpu: 30946M of GTT memory ready.
[229101.194881] amdgpu 0000:03:00.0: amdgpu: PCIE GART of 512M enabled (table at 0x00000083DAB00000).
[229101.484377] amdgpu 0000:03:00.0: amdgpu: RAP: optional rap ta ucode is not available
[229101.484382] amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[229101.484411] amdgpu 0000:03:00.0: amdgpu: smu driver if version = 0x0000002e, smu fw if version = 0x00000032, smu fw program = 0, smu fw version = 0x00684a00 (104.74.0)
[229101.484414] amdgpu 0000:03:00.0: amdgpu: SMU driver if version not matched
[229101.510355] amdgpu 0000:03:00.0: amdgpu: SMU is initialized successfully!
[229101.531843] amdgpu 0000:03:00.0: amdgpu: program CP_MES_CNTL : 0x4000000
[229101.531848] amdgpu 0000:03:00.0: amdgpu: program CP_MES_CNTL : 0xc000000
[229101.578354] amdgpu: HMM registered 16304MB device memory
[229101.579309] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[229101.579322] kfd kfd: amdgpu: Total number of KFD nodes to be created: 1
[229101.579352] amdgpu: Virtual CRAT table created for GPU
[229101.579458] amdgpu: Topology: Add dGPU node [0x7550:0x1002]
[229101.579460] kfd kfd: amdgpu: added device 1002:7550
[229101.579468] amdgpu 0000:03:00.0: amdgpu: SE 4, SH per SE 2, CU per SH 8, active_cu_number 64
[229101.579472] amdgpu 0000:03:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[229101.579473] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[229101.579475] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[229101.579476] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 6 on hub 0
[229101.579477] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 7 on hub 0
[229101.579478] amdgpu 0000:03:00.0: amdgpu: ring sdma0 uses VM inv eng 8 on hub 0
[229101.579479] amdgpu 0000:03:00.0: amdgpu: ring sdma1 uses VM inv eng 9 on hub 0
[229101.579480] amdgpu 0000:03:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[229101.579481] amdgpu 0000:03:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[229101.586331] amdgpu 0000:03:00.0: amdgpu: Using BACO for runtime pm
[229101.586618] amdgpu 0000:03:00.0: [drm] Registered 4 planes with drm panic
[229101.586620] [drm] Initialized amdgpu 3.61.0 for 0000:03:00.0 on minor 0
[229101.590644] amdgpu 0000:03:00.0: [drm] Cannot find any crtc or sizes
[229594.873445] amdgpu 0000:03:00.0: amdgpu: PCIE GART of 512M enabled (table at 0x00000083DAB00000).
[229594.873467] amdgpu 0000:03:00.0: amdgpu: PSP is resuming...
[229595.075149] amdgpu 0000:03:00.0: amdgpu: RAP: optional rap ta ucode is not available
[229595.075153] amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[229595.075155] amdgpu 0000:03:00.0: amdgpu: SMU is resuming...
[229595.075158] amdgpu 0000:03:00.0: amdgpu: smu driver if version = 0x0000002e, smu fw if version = 0x00000032, smu fw program = 0, smu fw version = 0x00684a00 (104.74.0)
[229595.075161] amdgpu 0000:03:00.0: amdgpu: SMU driver if version not matched
[229595.088738] amdgpu 0000:03:00.0: amdgpu: SMU is resumed successfully!
[229595.088896] amdgpu 0000:03:00.0: amdgpu: program CP_MES_CNTL : 0x4000000
[229595.088898] amdgpu 0000:03:00.0: amdgpu: program CP_MES_CNTL : 0xc000000
[229595.106172] amdgpu 0000:03:00.0: [drm] Cannot find any crtc or sizes
[229595.106177] amdgpu 0000:03:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[229595.106178] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[229595.106180] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[229595.106181] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 6 on hub 0
[229595.106181] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 7 on hub 0
[229595.106182] amdgpu 0000:03:00.0: amdgpu: ring sdma0 uses VM inv eng 8 on hub 0
[229595.106184] amdgpu 0000:03:00.0: amdgpu: ring sdma1 uses VM inv eng 9 on hub 0
[229595.106185] amdgpu 0000:03:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[229595.106186] amdgpu 0000:03:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[229595.111686] amdgpu 0000:03:00.0: [drm] Cannot find any crtc or sizes
[229609.024239] amdgpu 0000:03:00.0: amdgpu: PCIE GART of 512M enabled (table at 0x00000083DAB00000).
[229609.024265] amdgpu 0000:03:00.0: amdgpu: PSP is resuming...
[229609.226191] amdgpu 0000:03:00.0: amdgpu: RAP: optional rap ta ucode is not available
[229609.226194] amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[229609.226197] amdgpu 0000:03:00.0: amdgpu: SMU is resuming...
[229609.226199] amdgpu 0000:03:00.0: amdgpu: smu driver if version = 0x0000002e, smu fw if version = 0x00000032, smu fw program = 0, smu fw version = 0x00684a00 (104.74.0)
[229609.226202] amdgpu 0000:03:00.0: amdgpu: SMU driver if version not matched
[229609.240221] amdgpu 0000:03:00.0: amdgpu: SMU is resumed successfully!
[229609.240376] amdgpu 0000:03:00.0: amdgpu: program CP_MES_CNTL : 0x4000000
[229609.240380] amdgpu 0000:03:00.0: amdgpu: program CP_MES_CNTL : 0xc000000
[229609.257105] amdgpu 0000:03:00.0: [drm] Cannot find any crtc or sizes
[229609.257110] amdgpu 0000:03:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[229609.257112] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[229609.257113] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[229609.257114] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 6 on hub 0
[229609.257115] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 7 on hub 0
[229609.257116] amdgpu 0000:03:00.0: amdgpu: ring sdma0 uses VM inv eng 8 on hub 0
[229609.257117] amdgpu 0000:03:00.0: amdgpu: ring sdma1 uses VM inv eng 9 on hub 0
[229609.257118] amdgpu 0000:03:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[229609.257120] amdgpu 0000:03:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[229609.261733] amdgpu 0000:03:00.0: [drm] Cannot find any crtc or sizes
[230037.912351] amdgpu 0000:03:00.0: amdgpu: PCIE GART of 512M enabled (table at 0x00000083DAB00000).
[230037.912378] amdgpu 0000:03:00.0: amdgpu: PSP is resuming...
[230038.113546] amdgpu 0000:03:00.0: amdgpu: RAP: optional rap ta ucode is not available
[230038.113553] amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[230038.113556] amdgpu 0000:03:00.0: amdgpu: SMU is resuming...
[230038.113560] amdgpu 0000:03:00.0: amdgpu: smu driver if version = 0x0000002e, smu fw if version = 0x00000032, smu fw program = 0, smu fw version = 0x00684a00 (104.74.0)
[230038.113563] amdgpu 0000:03:00.0: amdgpu: SMU driver if version not matched
[230038.126687] amdgpu 0000:03:00.0: amdgpu: SMU is resumed successfully!
[230038.126842] amdgpu 0000:03:00.0: amdgpu: program CP_MES_CNTL : 0x4000000
[230038.126845] amdgpu 0000:03:00.0: amdgpu: program CP_MES_CNTL : 0xc000000
[230038.143671] amdgpu 0000:03:00.0: [drm] Cannot find any crtc or sizes
[230038.143682] amdgpu 0000:03:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[230038.143684] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[230038.143686] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[230038.143688] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 6 on hub 0
[230038.143689] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 7 on hub 0
[230038.143691] amdgpu 0000:03:00.0: amdgpu: ring sdma0 uses VM inv eng 8 on hub 0
[230038.143692] amdgpu 0000:03:00.0: amdgpu: ring sdma1 uses VM inv eng 9 on hub 0
[230038.143694] amdgpu 0000:03:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[230038.143695] amdgpu 0000:03:00.0: amdgpu: ring jpeg_dec uses VM inv eng 1 on hub 8
[230038.147220] amdgpu 0000:03:00.0: [drm] Cannot find any crtc or sizes
```

I am clueless and this point unfortunately. Thanks for any help!

### Additional Information

_No response_