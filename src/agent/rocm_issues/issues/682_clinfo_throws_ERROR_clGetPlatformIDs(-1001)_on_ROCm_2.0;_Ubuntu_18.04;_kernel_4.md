# clinfo throws ERROR: clGetPlatformIDs(-1001) on ROCm 2.0; Ubuntu 18.04; kernel 4.15; gfx803

> **Issue #682**
> **状态**: closed
> **创建时间**: 2019-01-19T22:42:05Z
> **更新时间**: 2019-02-08T00:47:11Z
> **关闭时间**: 2019-02-08T00:47:10Z
> **作者**: geofurb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/682

## 描述

Install proceeds without error, but when I try to test after reboot, an error occurs:
```
user@host:~$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
```

System info:
Ubuntu 18.04 (4.15.0-43-generic)
CPU: i7-5820k
GPU: gfx803 (RX480)
rocm-dkms 2.0.89

Additional info:
```
user@host:~$ dmesg | grep kfd
[    1.832810] kfd kfd: Allocated 3969056 bytes on gart
[    1.832933] kfd kfd: added device 1002:67df
```


---

## 评论 (10 条)

### 评论 #1 — jlgreathouse (2019-01-21T16:56:28Z)

Is your user in the group `video`? What happens if you run `clinfo` as sudo? What is the output of `rocminfo`?

---

### 评论 #2 — geofurb (2019-02-03T23:11:34Z)

> Is the user in the group `video`?  

Yes.  
  
> What happens if you run `clinfo` as sudo?  

```
user@host:~$ sudo clinfo
sudo: clinfo: command not found
user@host:~$ clinfo
ERROR: clGetPlatformIDs(-1001)
user@host:~$ which clinfo
/opt/rocm/opencl/bin/x86_64/clinfo
user@host:~$ sudo /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
```  
  
>What is the output of `rocminfo`?  

```
user@host:~$ rocminfo
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Core(TM) i7-5820K CPU @ 3.30GHz
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0
  Queue Min Size:          0
  Queue Max Size:          0
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768KB
  Chip ID:                 0
  Cacheline Size:          64
  Max Clock Frequency (MHz):3600
  BDFID:                   0
  Compute Unit:            12
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    3931460KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    3931460KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx803
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26591
  Cacheline Size:          64
  Max Clock Frequency (MHz):1266
  BDFID:                   1024
  Compute Unit:            36
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  67109888
    Dim[2]:                  0
  Grid Max Size:           4294967295
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295
    Dim[1]:                  4294967295
    Dim[2]:                  4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8388608KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx803
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Dimension:
        Dim[0]:                  67109888
        Dim[1]:                  1024
        Dim[2]:                  16777217
      Workgroup Max Size:      1024
      Grid Max Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      Grid Max Size:           4294967295
      FBarrier Max Size:       32
*** Done ***
```

Sorry for the late reply, I'd missed the notification!


---

### 评论 #3 — jlgreathouse (2019-02-04T17:18:07Z)

Hmm. Looks like this is an OpenCL problem rather than  ROCm problem. If `rocminfo` can see the GPU, that means your driver should be working properly.

Could you try following the debugging steps I show in [this thread](https://github.com/RadeonOpenCompute/ROCm/issues/511)? It may be that your OpenCL installation was performed incorrectly, and the steps I walked through with that user may show us what went wrong.

---

### 评论 #4 — geofurb (2019-02-05T09:17:12Z)

Yes! That was exactly it. No AMD .icd file. Wonder if this could be related to having a amdgpu-pro driver installed and then removed prior to installing ROCm?

Thank you so much for the help!

---

### 评论 #5 — geofurb (2019-02-05T09:54:37Z)

Woah, wait, I'm getting an error:  
`Memory access fault by GPU node-1 (Agent handle: 0x24d5860) on address 0x5bd800000. Reason: Page not present or supervisor privilege.`

---

### 评论 #6 — jlgreathouse (2019-02-05T15:07:19Z)

In your application or in `clinfo`? If it's in an application, then this indicates that you likely have a buffer overflow in a kernel running on the GPU. If this kernel writes or reads beyond the end of a buffer on the GPU, it can cause a page fault and the error you see.

---

### 评论 #7 — geofurb (2019-02-07T23:39:15Z)

This is from an application which was previously working using the amdgpu-pro driver for 16.04. I uninstalled that driver to use ROCm, since 18.04's desktop environment didn't start properly under the 16.04 driver. (I tried the 18.04 amdgpu-pro driver before ROCm, but it doesn't appear to work with OpenCL.)

---

### 评论 #8 — geofurb (2019-02-07T23:41:04Z)

Running `apt-get dist-upgrade` also just threw a ton of errors when setting up `rocm-dkms (2.1.96)`:  
```
Setting up rocm-dkms (2.1.96) ...
KERNEL=="kfd", MODE="0666"
Processing triggers for initramfs-tools (0.130ubuntu3.6) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-45-generic
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
W: Possible missing firmware /lib/firmware/amdgpu/hainan_mc.bin for module amdgpu
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
W: Possible missing firmware /lib/firmware/amdgpu/raven2_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_rlc_am4.bin for module amdgpu
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
W: Possible missing firmware /lib/firmware/amdgpu/raven2_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/mullins_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/hawaii_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kaveri_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/kabini_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/bonaire_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven2_vcn.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/picasso_vcn.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vega12_smc.bin for module amdgpu
Processing triggers for libc-bin (2.27-3ubuntu1) ...
```

---

### 评论 #9 — jlgreathouse (2019-02-08T00:04:09Z)

Those are warnings, because we do not currently ship firmware for those devices as part of the ROCm driver package (partially because such devices are not enabled to run in ROCm anyway). They aren't errors, and they will not prevent anything from working.

As for your application displaying memory faults in ROCm, I'll note that ROCm's memory layout can cause errors in your application to manifest problems that would not appear in other driver stacks. For example, ROCm can create buffers using 4 KiB pages, while many other implementations may always use larger pages (like 64 KiB). If you overflow one of the 4 KiB pages, it may cause a page fault on your GPU, leading to the error you see. If, however, your kernel would not overflow a 64 KiB page, you might not see the error on a different platform. Please see [this post for a bit more detail](https://github.com/RadeonOpenCompute/ROCm/issues/664#issuecomment-452113390).

In addition, that post shows that you may be able to use [clARMOR](https://github.com/ROCm-Developer-Tools/clARMOR/tree/19.01) to identify if any of your OpenCL kernels are causing buffer overflows.

---

### 评论 #10 — geofurb (2019-02-08T00:47:10Z)

Thank you!! That's exactly what I needed.

---
