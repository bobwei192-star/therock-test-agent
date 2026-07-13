# [Issue]: ROCm 6.1.3 crashes on 7900XTX when generating images in Stable Diffusion

- **Issue #:** 3452
- **State:** closed
- **Created:** 2024-07-23T18:01:38Z
- **Updated:** 2024-08-06T15:09:37Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3452

### Problem Description

As requested in https://github.com/ROCm/ROCm/issues/3265 , I'm opening this separate issue since the recommendations listed there did not resolve the issue.

I am running this in an Ubuntu container, but the host and thus kernel is Gentoo.  Kernel is `6.9.9-gentoo-dist`.

Attempting to generate images in Stable Diffusion crashes the card.  The graphical session is recoverable by remotely killing and restarting the X server.

### Operating System

Ubuntu 22.04.4 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 9 3950X 16-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

Followed the exact steps as specified in https://github.com/ROCm/ROCm/issues/3265#issuecomment-2245358795

Installed ROCm 6.1.3:
```
$ cat /etc/apt/sources.list.d/rocm.list 
deb [arch=amd64] https://repo.radeon.com/rocm/apt/6.1.3/ jammy main
$ dpkg-query --list '*rocm*'
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                   Version                      Architecture Description
+++-======================-============================-============-===========================================================
ii  rocm                   6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) software stack meta package
ii  rocm-cmake             0.12.0.60103-122~22.04       amd64        rocm-cmake built using CMake
ii  rocm-core              6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-dbgapi            0.71.0.60103-122~22.04       amd64        Library to provide AMD GPU debugger API
ii  rocm-debug-agent       2.0.3.60103-122~22.04        amd64        Radeon Open Compute Debug Agent (ROCdebug-agent)
ii  rocm-developer-tools   6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs       1.0.0.60103-122~22.04        amd64        Radeon Open Compute - device libraries
ii  rocm-gdb               14.1.60103-122~22.04         amd64        ROCgdb
ii  rocm-hip-libraries     6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-runtime       6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-runtime-dev   6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-sdk           6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-language-runtime  6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-llvm              17.0.0.24193.60103-122~22.04 amd64        ROCm core compiler
ii  rocm-ml-libraries      6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-ml-sdk            6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
un  rocm-ocl-icd           <none>                       <none>       (no description available)
ii  rocm-opencl            2.0.0.60103-122~22.04        amd64        clr built using CMake
ii  rocm-opencl-dev        2.0.0.60103-122~22.04        amd64        clr built using CMake
ii  rocm-opencl-icd-loader 1.2.60103-122~22.04          amd64        OpenCL-ICD-Loader built using CMake
ii  rocm-opencl-runtime    6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl-sdk        6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-openmp-sdk        6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) OpenMP Software development Kit.
un  rocm-smi               <none>                       <none>       (no description available)
ii  rocm-smi-lib           7.2.0.60103-122~22.04        amd64        AMD System Management libraries
ii  rocm-utils             6.1.3.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo               1.0.0.60103-122~22.04        amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool
```

Clone stable diffusion repo.  Make changes as specified:
```
$ grep -E "^[^#]" webui-user.sh
export COMMANDLINE_ARGS="--no-half-vae --opt-sdp-attention"
export TORCH_COMMAND="pip install https://repo.radeon.com/rocm/manylinux/rocm-rel-6.1.3/torch-2.1.2%2Brocm6.1.3-cp310-cp310-linux_x86_64.whl https://repo.radeon.com/rocm/manylinux/rocm-rel-6.1.3/torchvision-0.16.1%2Brocm6.1.3-cp310-cp310-linux_x86_64.whl https://repo.radeon.com/rocm/manylinux/rocm-rel-6.1.3/pytorch_triton_rocm-2.1.0%2Brocm6.1.3.4d510c3a44-cp310-cp310-linux_x86_64.whl"
export TORCH_BLAS_PREFER_HIPBLASLT=0
export HSA_OVERRIDE_GFX_VERSION=11.0.0
export PYTORCH_ROCM_ARCH=gfx1100
export HIP_VISIBLE_DEVICES=0
export PYTORCH_HIP_ALLOC_CONF=garbage_collection_threshold:0.9,max_split_size_mb:512
```

Run and attempt to generate an image.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.13
Runtime Ext Version:     1.4
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 9 3950X 16-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 9 3950X 16-Core Processor
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
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   3500
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            32
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    65750464(0x3eb45c0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65750464(0x3eb45c0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65750464(0x3eb45c0) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1100
  Uuid:                    GPU-5fc6ddc1dd71ff02
  Marketing Name:
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      6144(0x1800) KB
    L3:                      98304(0x18000) KB
  Chip ID:                 29772(0x744c)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2304
  BDFID:                   3328
  Internal Node ID:        1
  Compute Unit:            96
  SIMDs per CU:            2
  Shader Engines:          6
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 202
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    25149440(0x17fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1100
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
```

### Additional Information

Stable Diffusion reports:
```
Model loaded in 2.7s (load weights from disk: 0.8s, create model: 0.3s, apply weights to model: 1.3s, calculate empty prompt: 0.2s).
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 17.95it/s]
Memory access fault by GPU node-1 (Agent handle: 0x55ac14d27600) on address 0x7f9587e00000. Reason: Page not present or supervisor privilege.s]
./webui.sh: line 304:  4388 Aborted                 "${python_cmd}" -u "${LAUNCH_SCRIPT}" "$@"
```

The following errors are emitted from the kernel:

```
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32783)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:  in process python pid 25698 thread python pid 25698)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x00007f9587e00000 from client 10
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: TCP (0x8)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x1
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0x3
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32783)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:  in process python pid 25698 thread python pid 25698)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x00007f9587e00000 from client 10
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: CB/DB (0x0)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32783)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:  in process python pid 25698 thread python pid 25698)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x00007f9587e00000 from client 10
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: CB/DB (0x0)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32783)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:  in process python pid 25698 thread python pid 25698)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x00007f9587e00000 from client 10
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: CB/DB (0x0)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32783)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:  in process python pid 25698 thread python pid 25698)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x00007f9587e00000 from client 10
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: CB/DB (0x0)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:32783)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:  in process python pid 25698 thread python pid 25698)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:   in page starting at address 0x00007f9587e00000 from client 10
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000000
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          Faulty UTCL2 client ID: CB/DB (0x0)
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MORE_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          WALKER_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          PERMISSION_FAULTS: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          MAPPING_ERROR: 0x0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu:          RW: 0x0
[Tue Jul 23 13:49:25 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: Failed to evict queue 1
[Tue Jul 23 13:49:25 2024] print_sq_intr_info_error: 182 callbacks suppressed
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 1, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu: sq_intr: error, detail 0x00000000, type 2, sh 0, priv 1, wave_id 1, simd_id 0, wgp_id 0
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: GPU reset begin!
[Tue Jul 23 13:49:25 2024] amdgpu 0000:0d:00.0: amdgpu: Failed to remove queue 0
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=14
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_mes_flush_shader_debugger [amdgpu]] *ERROR* failed to set_shader_debugger
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:26 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:27 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:27 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:27 2024] [drm:amdgpu_debugfs_mes_event_log_init [amdgpu]] *ERROR* MES failed to response msg=3
[Tue Jul 23 13:49:27 2024] [drm:amdgpu_mes_unmap_legacy_queue [amdgpu]] *ERROR* failed to unmap legacy queue
[Tue Jul 23 13:49:27 2024] [drm:gfx_v9_4_2_set_power_brake_sequence [amdgpu]] *ERROR* failed to halt cp gfx
[Tue Jul 23 13:49:27 2024] amdgpu 0000:0d:00.0: amdgpu: MODE1 reset
[Tue Jul 23 13:49:27 2024] amdgpu 0000:0d:00.0: amdgpu: GPU mode1 reset
[Tue Jul 23 13:49:27 2024] amdgpu 0000:0d:00.0: amdgpu: GPU smu mode1 reset
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: GPU reset succeeded, trying to resume
[Tue Jul 23 13:49:28 2024] [drm] PCIE GART of 512M enabled (table at 0x0000008001300000).
[Tue Jul 23 13:49:28 2024] [drm] VRAM is lost due to GPU reset!
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: PSP is resuming...
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: reserve 0x1300000 from 0x85fc000000 for PSP TMR
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: RAP: optional rap ta ucode is not available
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: SMU is resuming...
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: smu driver if version = 0x0000003d, smu fw if version = 0x00000040, smu fw program = 0, smu fw version = 0x004e7e00 (78.126.0)
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: SMU driver if version not matched
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: SMU is resumed successfully!
[Tue Jul 23 13:49:28 2024] [drm] DMUB hardware initialized: version=0x07002A00
[Tue Jul 23 13:49:28 2024] [drm] kiq ring mec 3 pipe 1 q 0
[Tue Jul 23 13:49:28 2024] [drm] VCN decode and encode initialized successfully(under DPG Mode).
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: [drm:jpeg_v2_0_dec_ring_emit_ib [amdgpu]] JPEG decode initialized successfully.
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring sdma1 uses VM inv eng 13 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring jpeg_dec uses VM inv eng 4 on hub 8
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 14 on hub 0
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: recover vram bo from shadow start
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: recover vram bo from shadow done
[Tue Jul 23 13:49:28 2024] amdgpu 0000:0d:00.0: amdgpu: GPU reset(3) succeeded!
```