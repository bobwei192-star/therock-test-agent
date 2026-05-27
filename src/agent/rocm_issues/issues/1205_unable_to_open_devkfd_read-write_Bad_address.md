# unable to open /dev/kfd read-write: Bad address

> **Issue #1205**
> **状态**: closed
> **创建时间**: 2020-08-25T20:33:31Z
> **更新时间**: 2022-11-07T23:40:39Z
> **关闭时间**: 2020-12-16T10:19:48Z
> **作者**: MohamedElsaeidy
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1205

## 描述

after Fresh install of ubuntu 20.04 and ROCm 3.7 latest until today. when verifying installing throw 
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
the first command dont work even when removed the (base) of conda 
my specs , acer315-42G  Ryzen 5 3500u with Vega 8 , radeon 540x 

<pre>(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ cd kfd
bash: cd: kfd: Not a directory
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ groups
mohamed adm cdrom sudo dip video plugdev render lpadmin lxd sambashare
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ ls -la /dev/kfd
crw-rw---- 1 root render 236, 0 Aug 25 21:05 <span style="background-color:#2E3436"><font color="#C4A000"><b>/dev/kfd</b></font></span>
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ /opt/rocm/bin/rocminfo
<font color="#D3D7CF">ROCk module is loaded</font>
<font color="#CC0000">Unable to open /dev/kfd read-write: Bad address</font>
<font color="#D3D7CF">mohamed is member of render group</font>
<font color="#CC0000">hsa api call failure at: /src/rocminfo/rocminfo.cc:1142</font>
<font color="#CC0000">Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.</font>
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ sudo /opt/rocm/bin/rocminfo
<font color="#D3D7CF">ROCk module is loaded</font>
<font color="#CC0000">Unable to open /dev/kfd read-write: Bad address</font>
<font color="#D3D7CF">mohamed is member of render group</font>
<font color="#CC0000">hsa api call failure at: /src/rocminfo/rocminfo.cc:1142</font>
<font color="#CC0000">Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.</font>
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ /opt/rocm/opencl/bin/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3182.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
</pre>

---

## 评论 (19 条)

### 评论 #1 — xuhuisheng (2020-08-26T00:26:02Z)

I am afraid that rocm donot support vega8. Please refer https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support

---

### 评论 #2 — MohamedElsaeidy (2020-08-26T05:09:31Z)

> I am afraid that rocm donot support vega8. Please refer https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support

> GFX8 GPUs
> "Polaris 11" chips, such as on the AMD Radeon RX 570 and Radeon Pro WX 4100
> "Polaris 12" chips, such as on the AMD Radeon RX 550 and Radeon RX 540

it have the same technology of desktop GPU , doest it mean that ROCm does not support Mobile GPUs?

---

### 评论 #3 — xuhuisheng (2020-08-26T05:49:38Z)

Offically, there are a few cards can be supported by ROCm. And gfx803 (RX580) need PCIe Atomic support with both CPU and MotherBoard.

You can use `dmesg` to see whether there is error for kfd

```
$ dmesg |grep kfd
[    4.365875] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    4.371066] kfd kfd: amdgpu: added device 1002:67df

```



---

### 评论 #4 — MohamedElsaeidy (2020-08-26T11:23:49Z)

@xuhuisheng 
<pre>$ dmesg |grep kfd
[    2.978417] <font color="#CC0000"><b>kfd</b></font> <font color="#CC0000"><b>kfd</b></font>: amdgpu: Allocated 3969056 bytes on gart
[    2.979235] <font color="#CC0000"><b>kfd</b></font> <font color="#CC0000"><b>kfd</b></font>: amdgpu: added device 1002:6987
[    3.382581] <font color="#CC0000"><b>kfd</b></font> <font color="#CC0000"><b>kfd</b></font>: amdgpu: Allocated 3969056 bytes on gart
[    3.382998] <font color="#CC0000"><b>kfd</b></font> <font color="#CC0000"><b>kfd</b></font>: amdgpu: added device 1002:15d8
</pre>

---

### 评论 #5 — xuhuisheng (2020-08-26T12:01:39Z)

From https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/master/src/topology.c
6987 is Polaris12, 15d8 is Raven.And both cards can be added by kfd.
https://github.com/radeonopencompute/rocm said both cards are not ful support or support offically. Need amd to check these errors.

---

### 评论 #6 — MohamedElsaeidy (2020-08-26T22:52:23Z)

@xuhuisheng  do you  think it maybe a case of switchable 2 GPUs , Vega 8 and 540X , also is there somewhere i can add the device details manually so rocm be able to identify it like the topology.c file u mentioned 
my Lexa GPU Notes

```
Architecture Codename: Arctic Islands
Codename: Polaris 12
Old Codename: Treasure
CLRX Version: GCN 1.2
Graphics/Compute: GFX8 (gfx804)
Display Core Engine: 11.2
Unified Video Decoder: 6.3
Video Compression Engine: 3.4
```

---

### 评论 #7 — runvnc (2020-09-06T01:59:38Z)

I have a DeskMini A300W (ASRock) with Ryzen 5 2400g and Pop!OS 20.04 (almost exactly Ubuntu).  Was looking forward to using this or maybe upgrading to the new 4000 APUs as a sort of "power embedded" platform with good value that might be useful for robotics with OpenCL or HIP.

Spent multiple days trying to figure out similar issues.  After resolving several previous problems such as BIOS settings and other things, currently stuck on "/dev/kfd: Bad address".  Quite possibly just not supported on my motherboard/CPU, but I am not sure because the documentation seems ambiguous.

I have come to the conclusion that trying to use AMD for this type of parallel processing was a mistake.  I'm just going to rent a cheap Nvidia GPU online and probably eventually buy a new computer.  WiGig probably means I don't need the portability of the APU machines anyway.

---

### 评论 #8 — JoseVSeb (2020-09-06T03:55:29Z)

> I have come to the conclusion that trying to use AMD for this type of parallel processing was a mistake. I'm just going to rent a cheap Nvidia GPU online and probably eventually buy a new computer. WiGig probably means I don't need the portability of the APU machines anyway.

@runvnc  That's not a feasible solution. A software bug should NEVER be bypassed using hardware change; for obvious reasons. Fixing the bug takes a few lines of code (if you're in the development of the said software), changing hardware empties your pocket pretty quick for the solution you propose. And for the most of us; it's once in a decade opportunity to buy new hardware.

---

### 评论 #9 — oberstet (2020-10-17T00:29:43Z)

here is what I run into:

```
oberstet@oberstet-MS-7A40:~$ /opt/rocm/opencl/bin/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3186.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
oberstet@oberstet-MS-7A40:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Bad address
oberstet is member of render group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
oberstet@oberstet-MS-7A40:~$ dmesg | grep kfd
[    8.954824] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    8.955566] kfd kfd: amdgpu: added device 1002:15dd
oberstet@oberstet-MS-7A40:~$ x86info
x86info v1.31pre  Dave Jones 2001-2011
Feedback to <davej@redhat.com>.

Unknown CPU family: 0x17
Unknown CPU family: 0x17
Unknown CPU family: 0x17
Unknown CPU family: 0x17
Unknown CPU family: 0x17
Unknown CPU family: 0x17
Unknown CPU family: 0x17
Unknown CPU family: 0x17
Found 8 identical CPUs
Extended Family: 8 Extended Model: 1 Family: 15 Model: 17 Stepping: 0
CPU Model (x86info's best guess): 
Processor name string (BIOS programmed): AMD Ryzen 5 2400G with Radeon Vega Graphics    

Monitor/Mwait: min/max line size 64/64, ecx bit 0 support, enumeration extension
SVM: revision 1, 32768 ASIDs, np, lbrVirt, SVMLock, NRIPSave, TscRateMsr, VmcbClean, FlushByAsid, DecodeAssists, PauseFilter, PauseFilterThreshold
Address Size: 48 bits virtual, 48 bits physical
The physical package has 8 of 16 possible cores implemented.
 running at an estimated 3.60GHz
oberstet@oberstet-MS-7A40:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
oberstet@oberstet-MS-7A40:~$ 
```

and

```
oberstet@oberstet-MS-7A40:~$ dmesg | grep amd
[    0.000000] Linux version 5.4.0-51-generic (buildd@lcy01-amd64-020) (gcc version 9.3.0 (Ubuntu 9.3.0-10ubuntu2)) #56-Ubuntu SMP Mon Oct 5 14:28:49 UTC 2020 (Ubuntu 5.4.0-51.56-generic 5.4.65)
[    0.396365] amd_uncore: AMD NB counters detected
[    0.396368] amd_uncore: AMD LLC counters detected
[    3.293162] amdkcl: loading out-of-tree module taints kernel.
[    3.293234] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    3.535771] [drm] amdgpu kernel modesetting enabled.
[    3.535773] [drm] amdgpu version: 5.6.15
[    3.537864] amdgpu: Topology: Add APU node [0x0:0x0]
[    3.546002] amdgpu 0000:38:00.0: remove_conflicting_pci_framebuffers: bar 0: 0xe0000000 -> 0xefffffff
[    3.546005] amdgpu 0000:38:00.0: remove_conflicting_pci_framebuffers: bar 2: 0xf0000000 -> 0xf01fffff
[    3.546007] amdgpu 0000:38:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xfe500000 -> 0xfe57ffff
[    3.546010] fb0: switching to amdgpudrmfb from VESA VGA
[    3.546189] amdgpu 0000:38:00.0: vgaarb: deactivate vga console
[    3.546345] amdgpu 0000:38:00.0: amdgpu: Trusted Memory Zone (TMZ) feature disabled as experimental (default)
[    3.546346] amdgpu 0000:38:00.0: amdgpu: set kernel compute queue number to 8 due to invalid parameter provided by user
[    3.570491] amdgpu: ATOM BIOS: 113-RAVEN-104
[    3.571303] amdgpu 0000:38:00.0: amdgpu: VRAM: 256M 0x000000F400000000 - 0x000000F40FFFFFFF (256M used)
[    3.571306] amdgpu 0000:38:00.0: amdgpu: GART: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
[    3.571309] amdgpu 0000:38:00.0: amdgpu: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
[    3.571420] [drm] amdgpu: 256M of VRAM memory ready
[    3.571425] [drm] amdgpu: 15770M of GTT memory ready.
[    3.581433] amdgpu: [powerplay] hwmgr_sw_init smu backed is smu10_smu
[    3.628412] EDAC amd64: Node 0: DRAM ECC disabled.
[    3.628414] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[    3.721815] EDAC amd64: Node 0: DRAM ECC disabled.
[    3.721817] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[    3.820029] amdgpu 0000:38:00.0: amdgpu: RAS: optional ras ta ucode is not available
[    3.824581] EDAC amd64: Node 0: DRAM ECC disabled.
[    3.824583] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[    3.851720] snd_hda_intel 0000:38:00.1: bound 0000:38:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[    3.891852] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    3.892572] amdgpu: Topology: Add APU node [0x15dd:0x1002]
[    3.892574] kfd kfd: amdgpu: added device 1002:15dd
[    3.892576] amdgpu 0000:38:00.0: amdgpu: SE 1, SH per SE 1, CU per SH 11, active_cu_number 11
[    3.894266] fbcon: amdgpudrmfb (fb0) is primary device
[    3.894326] amdgpu 0000:38:00.0: fb0: amdgpudrmfb frame buffer device
[    3.912092] amdgpu 0000:38:00.0: amdgpu: ring gfx uses VM inv eng 0 on hub 0
[    3.912093] amdgpu 0000:38:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[    3.912094] amdgpu 0000:38:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[    3.912095] amdgpu 0000:38:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[    3.912096] amdgpu 0000:38:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[    3.912097] amdgpu 0000:38:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[    3.912098] amdgpu 0000:38:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[    3.912098] amdgpu 0000:38:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[    3.912099] amdgpu 0000:38:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[    3.912100] amdgpu 0000:38:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[    3.912101] amdgpu 0000:38:00.0: amdgpu: ring sdma0 uses VM inv eng 0 on hub 1
[    3.912102] amdgpu 0000:38:00.0: amdgpu: ring vcn_dec uses VM inv eng 1 on hub 1
[    3.912103] amdgpu 0000:38:00.0: amdgpu: ring vcn_enc0 uses VM inv eng 4 on hub 1
[    3.912104] amdgpu 0000:38:00.0: amdgpu: ring vcn_enc1 uses VM inv eng 5 on hub 1
[    3.912105] amdgpu 0000:38:00.0: amdgpu: ring jpeg_dec uses VM inv eng 6 on hub 1
[    3.940770] EDAC amd64: Node 0: DRAM ECC disabled.
[    3.940772] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[    4.009328] EDAC amd64: Node 0: DRAM ECC disabled.
[    4.009330] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[    4.034992] [drm] Initialized amdgpu 3.40.0 20150101 for 0000:38:00.0 on minor 0
[    4.149149] EDAC amd64: Node 0: DRAM ECC disabled.
[    4.149150] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[    4.260700] EDAC amd64: Node 0: DRAM ECC disabled.
[    4.260702] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[    4.360619] EDAC amd64: Node 0: DRAM ECC disabled.
[    4.360622] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   47.652369] amdgpu: Failure to set tba address. error -1.
[   47.653793] amdgpu: Failure to set tba address. error -1.
[   48.831248] amdgpu: Failure to set tba address. error -1.
[  118.989517] amdgpu: Failure to set tba address. error -1.
[  121.798439] amdgpu: Failure to set tba address. error -1.
[  121.799587] amdgpu: Failure to set tba address. error -1.
oberstet@oberstet-MS-7A40:~$ 
```

---

### 评论 #10 — ROCmSupport (2020-12-16T10:19:48Z)

Hi @MohamedElsaeidy 
Thanks for reaching out.
Vega8 (mobile GPUs) not supported with ROCm at present. Please check [https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support](url)

---

### 评论 #11 — oberstet (2020-12-16T11:22:50Z)

@ROCmSupport :

* the link you posted is broken
* "not supported with ROCm at present": so when will it? never?
* not supporting APUs for us means: AMD is no alternative to using Nvidia, as we need embedded (Ryzen V1000 vs XYZ)


---

### 评论 #12 — ROCmSupport (2020-12-16T12:32:16Z)

Sorry for typo.
Please use https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support

---

### 评论 #13 — oberstet (2020-12-16T12:39:44Z)

yes, thanks, I had been aware of this page. the page reads

> As such, they are not yet officially supported targets for ROCm.

as in "yet": when will it be? if not never, why close this issue? if never, pls say so .. thanks!

> fwiw, my personal view is: not supporting APUs, and the V1000 embedded Ryzen in particular, is a big mistake. because AMD could bring some competition to Nvidia NX. maybe. anyways, just my 2cts

---

### 评论 #14 — MohamedElsaeidy (2020-12-16T12:42:34Z)

> yes, thanks, I had been aware of this page. the page reads
> 
> > As such, they are not yet officially supported targets for ROCm.
> 
> as in "yet": when will it be? if not never, why close this issue? if never, pls say so .. thanks!
> 
> > fwiw, my personal view is: not supporting APUs, and the V1000 embedded Ryzen in particular, is a big mistake. because AMD could bring some competition to Nvidia NX. maybe. anyways, just my 2cts

in addition it says it supports polaris 12 tech chips which is same one my laptop GPU so it should be working normally with just few implementation on main installing source code i guess 

---

### 评论 #15 — konflic (2020-12-28T19:24:06Z)

On my laptop I have Vega 8 and Radeon 540X Series (POLARIS12) and have the same issue on latest for this message Ubuntu 20.04.1 and got the same error :(

`./rocminfo 
ROCk module is loaded
Unable to open /dev/kfd read-write: Bad address
$USER is member of render group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
`

---

### 评论 #16 — ROCmSupport (2020-12-29T08:40:51Z)

Hi @konflic , @oberstet and @MohamedElsaeidy 
Polaris12 and Vega8 are old cards as of today and we are not supporting them officially today. Not sure about future plans.
AMD is trying to add support for the new cards.

---

### 评论 #17 — oberstet (2020-12-29T10:43:23Z)

thanks for clarification! I guess I have to look elsewhere. fwiw, I'm talking about this product https://www.amd.com/en/products/embedded-ryzen-v1000-series, which is an APU actively promoted for embedded. with the 3.6 TOPS claimed, it would place itself between Nvidia Nano (472 GOPS)  and Xavier NX (21 TOPS). leaving price and long-term availability (embedded) aside for a moment, it all boils down to software support. for embedded AI use case, the lack of ROCm means: no use ..

---

### 评论 #18 — hapasa (2021-01-21T21:37:51Z)

I wonder if this issue could be happening also when there are both AMD APU, so Ryzen 5 2400G in my case, as well as discrete AMD RX 550 in the system?   

[    1.069011] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    1.069772] kfd kfd: amdgpu: added device 1002:699f
[    1.357892] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    1.358106] kfd kfd: amdgpu: added device 1002:15dd

(Not a laptop in this case, but a HP Pavilion Desktop).
Based on reading the installation instructions, RX 550 should be supported.

For what it is worth, PlaidML is working with AMD Pro driver, Ubuntu 20.04.1 with 5.4.0-62-generic linux.

---

### 评论 #19 — tingxingdong (2022-11-07T23:40:38Z)

If  you run ROCm on an AMD APU + discrete GPU, it is recommend to disable the APU's graphics part in BIOS mode, e.g Chipset->"Integrate Graphics" --> Save and Exit -> reboot. 

---
