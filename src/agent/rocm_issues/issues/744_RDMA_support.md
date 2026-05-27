# RDMA support

> **Issue #744**
> **状态**: closed
> **创建时间**: 2019-03-19T18:30:17Z
> **更新时间**: 2023-12-09T01:53:26Z
> **关闭时间**: 2023-12-09T01:01:02Z
> **作者**: FinnStokes
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/744

## 标签

- **Question** (颜色: #cc317c)

## 描述

Is there documentation somewhere or an example of how to use RDMA/Peer Direct with OpenCL or HIP? The page at https://rocm-documentation.readthedocs.io/en/latest/Remote_Device_Programming/Remote-Device-Programming.html seems to describe details about the underlying implementation, but I am not clear how to use it in practice.

My current goal is to transfer data between two Radeon Pro WX 8200 cards on different machines over an infiniband interconnect. I'm not sure how I would initiate a transfer of an OpenCL buffer, perhaps I need to be using HIP instead?

---

## 评论 (13 条)

### 评论 #1 — jlgreathouse (2019-03-20T15:39:41Z)

Hi @FinnStokes 

GPU RDMA transfers are initiated by the RDMA-capable NIC, so you will need to interface with Mellanox's IB verb library to provide source and destination GPU memory targets and also to trigger RDMA. This is outside the scope of AMD’s ROCm software..

RDMA also requires within-node system configuration to allow RDMA NIC to be able to able to directly peer access the GPU. This would be the first step to verify if your in-node configuration supports it. For example, this will likely require PCIe large BAR support to be enabled on your GPU and on your GPU. We have eased this restriction in newer upstream kernels ,but I've yet to verify if it's still required in our ROCm 2.2 `rock-dkms` driver.

There shouldn't be any code differences between sending RDMA data from host memory or device memory, except obviously that device memory would be allocated onto the GPU using e.g. `hipMalloc` or `clSVMAlloc`.

---

### 评论 #2 — FinnStokes (2019-03-20T16:00:21Z)

Thanks, that clarifies a lot of things for me. The main piece of the puzzle that was missing for me was using `clSVMalloc` to allocate the shared virtual memory to back an OpenCL buffer.

For our initial tests, we are planning to use Radeon Pro WX 8200 GPUs, with a ASUS X99-E WS motherboard and Mellanox ConnectX-5 EN for the interconnect. It is my understanding that this configuration should support PCIe large BAR and everything else required for RDMA.

We have been avoiding using the upstreamed versions of the kernel drivers because we thought that they did not support RDMA yet. Has this now been resolved? If so, would you recommend using the upstreamed version of the driver instead of `rock-dkms`? Are there any key features that are missing from newer upstream kernels?

I'm still waiting for the last of our hardware for our test nodes to arrive, but I should be able to get back with how our initial setup/testing goes next week sometime.

---

### 评论 #3 — jlgreathouse (2019-03-20T16:23:29Z)

I'll admit from the get-go that I'm a middleman for this question. All of the folks that actually do RDMA work in the ROCm team either don't have the time or the desire to answer github questions, so all I'm doing is sending your questions to them and then editing their answers a bit before pushing them back here. As such, please don't expect fast turnaround on any of your questions.

I don't believe RDMA support is upstreamed yet. On the other hand, I do not know if the resizable BAR enhancements are in `rock-dkms` or not. If your hardware all supports large BAR, please stick with `rock-dkms`.

---

### 评论 #4 — FinnStokes (2019-03-20T16:33:29Z)

Thankyou for the clarifications, and for acting as a middleman in this discussion. I appreciate your time and the promptness with which you have responded to this and other issues I have raised.

I will continue using `rock-dkms` on the assumption that these devices have the large BAR support I think they have. I guess the question will answer itself once the last of the hardware arrives and we begin proper testing.

---

### 评论 #5 — jinmingjian (2019-03-21T08:41:58Z)

I am also interesting in this topic. Not sure one old (abandoned?) project [ROCnRDMA](https://github.com/RadeonOpenCompute/ROCnRDMA) can give some idea? (It has some tests)



---

### 评论 #6 — jlgreathouse (2019-03-21T15:10:30Z)

To note: we are in the process of archiving ROCnRDMA, because the underlying technologies are now in the `rock-dkms` driver.

---

### 评论 #7 — FinnStokes (2019-04-12T17:21:37Z)

There were some delays with our test hardware arriving, but it got here today. I'm trying to start out with intra-node transfers, then move on to inter-node transfers, but I'm having some issues I don't quite understand.

We have two machines with ASUS X99-E WS/USB 3.1 motherboards, each with to Radeon Pro WX 8200 cards. I've enabled large BAR support ("Above 4G Decoding") in the BIOS, and now one of the two cards in each machine has access to its full address space, but for some reason the other card does not:
```
$ sudo lspci -vv
...
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon PRO WX 8100] (prog-if 00 [VGA controller])
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega
        Flags: bus master, fast devsel, latency 0, IRQ 87, NUMA node 0
        Memory at c0000000 (64-bit, prefetchable) [size=256M]
        Memory at d0000000 (64-bit, prefetchable) [size=2M]
        I/O ports at e000 [size=256]
        Memory at fb400000 (32-bit, non-prefetchable) [size=512K]
        Expansion ROM at 000c0000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Legacy Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150] Advanced Error Reporting
        Capabilities: [200] #15
        Capabilities: [270] #19
        Capabilities: [2a0] Access Control Services
        Capabilities: [2b0] Address Translation Service (ATS)
        Capabilities: [2c0] Page Request Interface (PRI)
        Capabilities: [2d0] Process Address Space ID (PASID)
        Capabilities: [320] Latency Tolerance Reporting
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
...
0d:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon PRO WX 8100] (prog-if 00 [VGA controller])
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega
        Flags: bus master, fast devsel, latency 0, IRQ 61, NUMA node 0
        Memory at 380000000000 (64-bit, prefetchable) [size=8G]
        Memory at 380200000000 (64-bit, prefetchable) [size=2M]
        I/O ports at d000 [size=256]
        Memory at fb800000 (32-bit, non-prefetchable) [size=512K]
        Expansion ROM at fb880000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Legacy Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150] Advanced Error Reporting
        Capabilities: [200] #15
        Capabilities: [270] #19
        Capabilities: [2a0] Access Control Services
        Capabilities: [2b0] Address Translation Service (ATS)
        Capabilities: [2c0] Page Request Interface (PRI)
        Capabilities: [2d0] Process Address Space ID (PASID)
        Capabilities: [320] Latency Tolerance Reporting
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
...
```

My interpretation of this is that thanks to the large BAR support the GPU at 0d:00.0 has mapped its full 8GB of address space, but the GPU at 07:00.0 has not for some reason. As a result, the GPUs don't seem to be available for peer transfers. Am I interpreting this output correctly, and if so, do you have any ideas what the cause might be? Could it be something to do with capabilities available through specific PCI slots?

Some other output that might be relevant, from your `test_cl_amd_copy_buffer_p2p` repo and `dmesg`:
```
$ ./test_p2p 
Searching for platforms...
    Using platform: AMD Accelerated Parallel Processing
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #0: 0
PCIe Topology of device 0: d:0.0
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #1: 0
PCIe Topology of device 1: 7:0.0
Device 0 and device 1 are not P2P neighbors
They cannot be used to test P2P transfers.
Exiting!
```
```
$ dmesg
[    0.000000] Linux version 4.15.0-47-generic (buildd@lgw01-amd64-001) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #50-Ubuntu SMP Wed Mar 13 10:44:52 UTC 2019 (Ubuntu 4.15.0-47.50-generic 4.15.18)
...
[    8.386429] pci 0000:0d:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    8.386429] pci 0000:07:00.0: vgaarb: setting as boot VGA device
[    8.386429] pci 0000:07:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    8.386429] pci 0000:0d:00.0: vgaarb: bridge control possible
[    8.386429] pci 0000:07:00.0: vgaarb: bridge control possible
...
[    9.844635] [drm] amdgpu kernel modesetting enabled.
[    9.845038] [drm] amdgpu version: 19.10.8.418
[    9.845431] [drm] OS DRM version: 4.15.0
[    9.845869] CRAT table not found
[    9.846249] Virtual CRAT table created for CPU
[    9.846626] Parsing CRAT table with 1 nodes
[    9.847007] Creating topology SYSFS entries
[    9.847386] Topology: Add CPU node
[    9.847753] Finished initializing topology
[    9.849310] checking generic (c0000000 300000) vs hw (383fe0000000 10000000)
[    9.849340] amdgpu 0000:0d:00.0: enabling device (0100 -> 0103)
[    9.849911] [drm] initializing kernel modesetting (VEGA10 0x1002:0x6868 0x1002:0x0A0C 0x00).
[    9.850328] [drm] register mmio base: 0xFB800000
[    9.850736] [drm] register mmio size: 524288
[    9.851141] [drm] add ip block number 0 <soc15_common>
[    9.851531] [drm] add ip block number 1 <gmc_v9_0>
[    9.851909] [drm] add ip block number 2 <vega10_ih>
[    9.852289] [drm] add ip block number 3 <psp>
[    9.852652] [drm] add ip block number 4 <gfx_v9_0>
[    9.853005] [drm] add ip block number 5 <sdma_v4_0>
[    9.853352] [drm] add ip block number 6 <powerplay>
[    9.853693] [drm] add ip block number 7 <dm>
[    9.854027] [drm] add ip block number 8 <uvd_v7_0>
[    9.854364] [drm] add ip block number 9 <vce_v4_0>
[    9.854737] [drm] UVD(0) is enabled in VM mode
[    9.855060] [drm] UVD(0) ENC is enabled in VM mode
[    9.855372] [drm] VCE enabled in VM mode
...
[   11.187983] [drm] GPU posting now...
[   11.190068] e1000e 0000:00:19.0 eth0: (PCI Express:2.5GT/s:Width x1) 18:31:bf:cc:ff:c1
[   11.190484] e1000e 0000:00:19.0 eth0: Intel(R) PRO/1000 Network Connection
[   11.190921] e1000e 0000:00:19.0 eth0: MAC: 11, PHY: 12, PBA No: FFFFFF-0FF
[   11.191912] e1000e 0000:00:19.0 eno1: renamed from eth0
[   11.745717] [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[   11.746140] amdgpu 0000:0d:00.0: BAR 2: releasing [mem 0x383ff0000000-0x383ff01fffff 64bit pref]
[   11.746558] amdgpu 0000:0d:00.0: BAR 0: releasing [mem 0x383fe0000000-0x383fefffffff 64bit pref]
[   11.746979] pcieport 0000:0c:00.0: BAR 15: releasing [mem 0x383fe0000000-0x383ff01fffff 64bit pref]
[   11.747388] pcieport 0000:0b:00.0: BAR 15: releasing [mem 0x383fe0000000-0x383ff01fffff 64bit pref]
[   11.747811] pcieport 0000:0a:10.0: BAR 15: releasing [mem 0x383fe0000000-0x383ff01fffff 64bit pref]
[   11.748239] pcieport 0000:09:00.0: BAR 15: releasing [mem 0x383fe0000000-0x383ff01fffff 64bit pref]
[   11.748658] pcieport 0000:00:02.0: BAR 15: releasing [mem 0x383fe0000000-0x383ff01fffff 64bit pref]
[   11.749064] pcieport 0000:00:02.0: BAR 15: assigned [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.749439] pcieport 0000:09:00.0: BAR 15: assigned [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.749808] pcieport 0000:0a:10.0: BAR 15: assigned [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.750187] pcieport 0000:0b:00.0: BAR 15: assigned [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.750536] pcieport 0000:0c:00.0: BAR 15: assigned [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.750880] amdgpu 0000:0d:00.0: BAR 0: assigned [mem 0x380000000000-0x3801ffffffff 64bit pref]
[   11.751231] amdgpu 0000:0d:00.0: BAR 2: assigned [mem 0x380200000000-0x3802001fffff 64bit pref]
[   11.751575] pcieport 0000:00:02.0: PCI bridge to [bus 09-0e]
[   11.751912] pcieport 0000:00:02.0:   bridge window [io  0xd000-0xdfff]
[   11.752283] pcieport 0000:00:02.0:   bridge window [mem 0xfb800000-0xfbafffff]
[   11.752641] pcieport 0000:00:02.0:   bridge window [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.752974] pcieport 0000:09:00.0: PCI bridge to [bus 0a-0e]
[   11.753306] pcieport 0000:09:00.0:   bridge window [io  0xd000-0xdfff]
[   11.753642] pcieport 0000:09:00.0:   bridge window [mem 0xfb800000-0xfb9fffff]
[   11.753975] pcieport 0000:09:00.0:   bridge window [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.754317] pcieport 0000:0a:10.0: PCI bridge to [bus 0b-0d]
[   11.754654] pcieport 0000:0a:10.0:   bridge window [io  0xd000-0xdfff]
[   11.754984] pcieport 0000:0a:10.0:   bridge window [mem 0xfb800000-0xfb9fffff]
[   11.755303] pcieport 0000:0a:10.0:   bridge window [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.755625] pcieport 0000:0b:00.0: PCI bridge to [bus 0c-0d]
[   11.755942] pcieport 0000:0b:00.0:   bridge window [io  0xd000-0xdfff]
[   11.756305] pcieport 0000:0b:00.0:   bridge window [mem 0xfb800000-0xfb8fffff]
[   11.756651] pcieport 0000:0b:00.0:   bridge window [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.756980] pcieport 0000:0c:00.0: PCI bridge to [bus 0d]
[   11.757299] pcieport 0000:0c:00.0:   bridge window [io  0xd000-0xdfff]
[   11.757619] pcieport 0000:0c:00.0:   bridge window [mem 0xfb800000-0xfb8fffff]
[   11.757934] pcieport 0000:0c:00.0:   bridge window [mem 0x380000000000-0x3802ffffffff 64bit pref]
[   11.758287] amdgpu 0000:0d:00.0: VRAM: 8176M 0x000000F400000000 - 0x000000F5FEFFFFFF (8176M used)
[   11.758606] amdgpu 0000:0d:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[   11.758925] amdgpu 0000:0d:00.0: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
[   11.759249] [drm] Detected VRAM RAM=8176M, BAR=8192M
[   11.759573] [drm] RAM width 2048bits HBM
[   11.759970] [TTM] Zone  kernel: Available graphics memory: 61761000 kiB
[   11.760346] [TTM] Initializing pool allocator
[   11.760727] [TTM] Initializing DMA pool allocator
[   11.761084] [drm] amdgpu: 8176M of VRAM memory ready
[   11.761403] [drm] amdgpu: 64334M of GTT memory ready.
[   11.761729] [drm] GART: num cpu pages 131072, num gpu pages 131072
[   11.762127] [drm] PCIE GART of 512M enabled (table at 0x000000F400900000).
[   11.763375] [drm] use_doorbell being set to: [true]
[   11.763777] [drm] use_doorbell being set to: [true]
[   11.764330] [drm] Found UVD firmware Version: 65.29 Family ID: 17
[   11.764684] [drm] PSP loading UVD firmware
[   11.765427] [drm] Found VCE firmware Version: 57.1 Binary ID: 4
[   11.765740] [drm] PSP loading VCE firmware
[   11.913699] [drm] reserve 0x400000 from 0xf400d00000 for PSP TMR SIZE
[   11.952918] pps pps0: new PPS source ptp1
[   11.953295] igb 0000:12:00.0: added PHC on eth0
[   11.953656] igb 0000:12:00.0: Intel(R) Gigabit Ethernet Network Connection
[   11.953993] igb 0000:12:00.0: eth0: (PCIe:2.5Gb/s:Width x1) 18:31:bf:cc:ff:c2
[   11.954393] igb 0000:12:00.0: eth0: PBA No: 000300-000
[   11.954737] igb 0000:12:00.0: Using MSI-X interrupts. 4 rx queue(s), 4 tx queue(s)
[   11.955783] igb 0000:12:00.0 enp18s0: renamed from eth0
[   12.096985] [drm] Display Core initialized with v3.2.14!
[   12.097887] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   12.098303] [drm] Driver supports precise vblank timestamp query.
[   12.119818] [drm] UVD and UVD ENC initialized successfully.
[   12.219805] [drm] VCE initialized successfully.
[   12.239906] kfd kfd: Allocated 3969056 bytes on gart
[   12.240330] Virtual CRAT table created for GPU
[   12.240734] Parsing CRAT table with 1 nodes
[   12.241143] Creating topology SYSFS entries
[   12.241624] Topology: Add dGPU node [0x6868:0x1002]
[   12.242069] kfd kfd: added device 1002:6868
[   12.242667] [drm] Cannot find any crtc or sizes
[   12.243132] amdgpu 0000:0d:00.0: ring gfx uses VM inv eng 0 on hub 0
[   12.243542] amdgpu 0000:0d:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[   12.243947] amdgpu 0000:0d:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[   12.244350] amdgpu 0000:0d:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[   12.244746] amdgpu 0000:0d:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[   12.245137] amdgpu 0000:0d:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[   12.245519] amdgpu 0000:0d:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[   12.245897] amdgpu 0000:0d:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[   12.246271] amdgpu 0000:0d:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[   12.246641] amdgpu 0000:0d:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[   12.247004] amdgpu 0000:0d:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[   12.247366] amdgpu 0000:0d:00.0: ring page0 uses VM inv eng 1 on hub 1
[   12.247722] amdgpu 0000:0d:00.0: ring sdma1 uses VM inv eng 4 on hub 1
[   12.248067] amdgpu 0000:0d:00.0: ring page1 uses VM inv eng 5 on hub 1
[   12.248409] amdgpu 0000:0d:00.0: ring uvd_0 uses VM inv eng 6 on hub 1
[   12.248741] amdgpu 0000:0d:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
[   12.249071] amdgpu 0000:0d:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
[   12.249398] amdgpu 0000:0d:00.0: ring vce0 uses VM inv eng 9 on hub 1
[   12.249725] amdgpu 0000:0d:00.0: ring vce1 uses VM inv eng 10 on hub 1
[   12.250052] amdgpu 0000:0d:00.0: ring vce2 uses VM inv eng 11 on hub 1
[   12.250411] [drm] ECC is active.
[   12.251407] (0000:08:00.0): E-Switch: Total vports 1, per vport: max uc(1024) max mc(16384)
[   12.252102] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:0d:00.0 on minor 0
[   12.252470] checking generic (c0000000 300000) vs hw (c0000000 10000000)
[   12.252471] fb: switching to amdgpudrmfb from EFI VGA
[   12.252819] Console: switching to colour dummy device 80x25
[   12.253018] [drm] initializing kernel modesetting (VEGA10 0x1002:0x6868 0x1002:0x0A0C 0x00).
[   12.253026] [drm] register mmio base: 0xFB400000
[   12.253028] [drm] register mmio size: 524288
[   12.253042] [drm] add ip block number 0 <soc15_common>
[   12.253043] [drm] add ip block number 1 <gmc_v9_0>
[   12.253044] [drm] add ip block number 2 <vega10_ih>
[   12.253046] [drm] add ip block number 3 <psp>
[   12.253047] [drm] add ip block number 4 <gfx_v9_0>
[   12.253048] [drm] add ip block number 5 <sdma_v4_0>
[   12.253050] [drm] add ip block number 6 <powerplay>
[   12.253051] [drm] add ip block number 7 <dm>
[   12.253052] [drm] add ip block number 8 <uvd_v7_0>
[   12.253054] [drm] add ip block number 9 <vce_v4_0>
[   12.253067] [drm] UVD(0) is enabled in VM mode
[   12.253068] [drm] UVD(0) ENC is enabled in VM mode
[   12.253069] [drm] VCE enabled in VM mode
[   12.253092] amdgpu 0000:07:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[   12.253126] ATOM BIOS: 113-D0511100-109
[   12.253142] [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[   12.253151] amdgpu 0000:07:00.0: BAR 2: releasing [mem 0xd0000000-0xd01fffff 64bit pref]
[   12.253153] amdgpu 0000:07:00.0: BAR 0: releasing [mem 0xc0000000-0xcfffffff 64bit pref]
[   12.253171] pcieport 0000:06:00.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[   12.253173] pcieport 0000:05:00.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[   12.253176] pcieport 0000:04:10.0: BAR 15: releasing [mem 0xc0000000-0xd01fffff 64bit pref]
[   12.253203] pcieport 0000:04:10.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[   12.253205] pcieport 0000:04:10.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[   12.253208] pcieport 0000:05:00.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[   12.253211] pcieport 0000:05:00.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[   12.253214] pcieport 0000:06:00.0: BAR 15: no space for [mem size 0x300000000 64bit pref]
[   12.253216] pcieport 0000:06:00.0: BAR 15: failed to assign [mem size 0x300000000 64bit pref]
[   12.253220] amdgpu 0000:07:00.0: BAR 0: no space for [mem size 0x200000000 64bit pref]
[   12.253223] amdgpu 0000:07:00.0: BAR 0: failed to assign [mem size 0x200000000 64bit pref]
[   12.253225] amdgpu 0000:07:00.0: BAR 2: no space for [mem size 0x00200000 64bit pref]
[   12.253227] amdgpu 0000:07:00.0: BAR 2: failed to assign [mem size 0x00200000 64bit pref]
[   12.253230] pcieport 0000:03:00.0: PCI bridge to [bus 04-08]
[   12.253233] pcieport 0000:03:00.0:   bridge window [io  0xe000-0xefff]
[   12.253237] pcieport 0000:03:00.0:   bridge window [mem 0xfb400000-0xfb6fffff]
[   12.253240] pcieport 0000:03:00.0:   bridge window [mem 0xc0000000-0xd3ffffff 64bit pref]
[   12.253245] pcieport 0000:04:10.0: PCI bridge to [bus 05-07]
[   12.253247] pcieport 0000:04:10.0:   bridge window [io  0xe000-0xefff]
[   12.253251] pcieport 0000:04:10.0:   bridge window [mem 0xfb400000-0xfb5fffff]
[   12.253254] pcieport 0000:04:10.0:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[   12.253258] pcieport 0000:05:00.0: PCI bridge to [bus 06-07]
[   12.253261] pcieport 0000:05:00.0:   bridge window [io  0xe000-0xefff]
[   12.253265] pcieport 0000:05:00.0:   bridge window [mem 0xfb400000-0xfb4fffff]
[   12.253269] pcieport 0000:05:00.0:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[   12.253274] pcieport 0000:06:00.0: PCI bridge to [bus 07]
[   12.253277] pcieport 0000:06:00.0:   bridge window [io  0xe000-0xefff]
[   12.253281] pcieport 0000:06:00.0:   bridge window [mem 0xfb400000-0xfb4fffff]
[   12.253285] pcieport 0000:06:00.0:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[   12.253295] [drm] Not enough PCI address space for a large BAR.
[   12.253297] amdgpu 0000:07:00.0: BAR 0: assigned [mem 0xc0000000-0xcfffffff 64bit pref]
[   12.253307] amdgpu 0000:07:00.0: BAR 2: assigned [mem 0xd0000000-0xd01fffff 64bit pref]
[   12.253325] amdgpu 0000:07:00.0: VRAM: 8176M 0x000000F400000000 - 0x000000F5FEFFFFFF (8176M used)
[   12.253328] amdgpu 0000:07:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[   12.253330] amdgpu 0000:07:00.0: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
[   12.253335] [drm] Detected VRAM RAM=8176M, BAR=256M
[   12.253336] [drm] RAM width 2048bits HBM
[   12.253581] [drm] amdgpu: 8176M of VRAM memory ready
[   12.253583] [drm] amdgpu: 64334M of GTT memory ready.
[   12.253596] [drm] GART: num cpu pages 131072, num gpu pages 131072
[   12.253678] [drm] PCIE GART of 512M enabled (table at 0x000000F400900000).
[   12.254362] [drm] use_doorbell being set to: [true]
[   12.254408] [drm] use_doorbell being set to: [true]
[   12.254460] [drm] Found UVD firmware Version: 65.29 Family ID: 17
[   12.254463] [drm] PSP loading UVD firmware
[   12.254804] [drm] Found VCE firmware Version: 57.1 Binary ID: 4
[   12.254808] [drm] PSP loading VCE firmware
[   12.402475] [drm] reserve 0x400000 from 0xf400d00000 for PSP TMR SIZE
[   12.413002] mlx5_core 0000:08:00.0: Port module event: module 0, Cable unplugged
[   12.416316] random: fast init done
[   12.417347] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[   12.417355] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[   12.417366] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[   12.417508] mlx5_core 0000:08:00.0: MLX5E: StrdRq(1) RqSz(8) StrdSz(64) RxCqeCmprss(0)
[   12.513300] mlx5_core 0000:08:00.0 enp8s0: renamed from eth0
[   12.514469] mlx5_ib: Mellanox Connect-IB Infiniband driver v5.0-0
[   12.600156] [drm] Display Core initialized with v3.2.14!
[   12.644331] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   12.644334] [drm] Driver supports precise vblank timestamp query.
[   12.665483] [drm] UVD and UVD ENC initialized successfully.
[   12.765070] [drm] VCE initialized successfully.
[   12.784790] kfd kfd: Allocated 3969056 bytes on gart
[   12.784806] Virtual CRAT table created for GPU
[   12.784807] Parsing CRAT table with 1 nodes
[   12.784815] Creating topology SYSFS entries
[   12.785021] Topology: Add dGPU node [0x6868:0x1002]
[   12.785069] kfd kfd: added device 1002:6868
[   12.786033] [drm] fb mappable at 0xC1100000
[   12.786034] [drm] vram apper at 0xC0000000
[   12.786036] [drm] size 9216000
[   12.786037] [drm] fb depth is 24
[   12.786038] [drm]    pitch is 7680
[   12.786073] fbcon: amdgpudrmfb (fb0) is primary device
[   12.828979] Console: switching to colour frame buffer device 240x75
[   12.848632] amdgpu 0000:07:00.0: fb0: amdgpudrmfb frame buffer device
[   12.864130] amdgpu 0000:07:00.0: ring gfx uses VM inv eng 0 on hub 0
[   12.864146] amdgpu 0000:07:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[   12.864162] amdgpu 0000:07:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[   12.864178] amdgpu 0000:07:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[   12.864194] amdgpu 0000:07:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[   12.864210] amdgpu 0000:07:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[   12.864225] amdgpu 0000:07:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[   12.864241] amdgpu 0000:07:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[   12.864257] amdgpu 0000:07:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[   12.864273] amdgpu 0000:07:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[   12.864289] amdgpu 0000:07:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[   12.864304] amdgpu 0000:07:00.0: ring page0 uses VM inv eng 1 on hub 1
[   12.864319] amdgpu 0000:07:00.0: ring sdma1 uses VM inv eng 4 on hub 1
[   12.864334] amdgpu 0000:07:00.0: ring page1 uses VM inv eng 5 on hub 1
[   12.864349] amdgpu 0000:07:00.0: ring uvd_0 uses VM inv eng 6 on hub 1
[   12.864364] amdgpu 0000:07:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
[   12.864380] amdgpu 0000:07:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
[   12.864396] amdgpu 0000:07:00.0: ring vce0 uses VM inv eng 9 on hub 1
[   12.864411] amdgpu 0000:07:00.0: ring vce1 uses VM inv eng 10 on hub 1
[   12.864426] amdgpu 0000:07:00.0: ring vce2 uses VM inv eng 11 on hub 1
[   12.864481] [drm] ECC is active.
[   12.864888] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:07:00.0 on minor 1
```

---

### 评论 #8 — FinnStokes (2019-04-18T10:02:48Z)

By removing the Infiniband card I've got both GPUs to map their full address space:
```
# lspci -v
...
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon PRO WX 8100] (prog-if 00 [VGA controller])
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega
        Flags: bus master, fast devsel, latency 0, IRQ 67, NUMA node 0
        Memory at 380400000000 (64-bit, prefetchable) [size=8G]
        Memory at 380300000000 (64-bit, prefetchable) [size=2M]
        I/O ports at e000 [size=256]
        Memory at fb800000 (32-bit, non-prefetchable) [size=512K]
        Expansion ROM at 000c0000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Legacy Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150] Advanced Error Reporting
        Capabilities: [200] #15
        Capabilities: [270] #19
        Capabilities: [2a0] Access Control Services
        Capabilities: [2b0] Address Translation Service (ATS)
        Capabilities: [2c0] Page Request Interface (PRI)
        Capabilities: [2d0] Process Address Space ID (PASID)
        Capabilities: [320] Latency Tolerance Reporting
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
...
0d:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon PRO WX 8100] (prog-if 00 [VGA controller])
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega
        Flags: bus master, fast devsel, latency 0, IRQ 61, NUMA node 0
        Memory at 380000000000 (64-bit, prefetchable) [size=8G]
        Memory at 380200000000 (64-bit, prefetchable) [size=2M]
        I/O ports at d000 [size=256]
        Memory at fb500000 (32-bit, non-prefetchable) [size=512K]
        Expansion ROM at fb580000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Legacy Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150] Advanced Error Reporting
        Capabilities: [200] #15
        Capabilities: [270] #19
        Capabilities: [2a0] Access Control Services
        Capabilities: [2b0] Address Translation Service (ATS)
        Capabilities: [2c0] Page Request Interface (PRI)
        Capabilities: [2d0] Process Address Space ID (PASID)
        Capabilities: [320] Latency Tolerance Reporting
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
...
```

However, `test_cl_amd_copy_buffer_p2p` still does not recognise the GPUs as peers:
```
$ ./test_p2p 
Searching for platforms...
    Using platform: AMD Accelerated Parallel Processing
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #0: 0
PCIe Topology of device 0: d:0.0
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #1: 0
PCIe Topology of device 1: 7:0.0
Device 0 and device 1 are not P2P neighbors
They cannot be used to test P2P transfers.
Exiting!
```

I think perhaps this is related to the address ranges being mapped above 2^44, although maybe I read somewhere that wasn't an issue anymore? Either way I can't seem to find the MMIOH Base and MMIO High Size settings in the BIOS for the ASUS X99-E WS/USB 3.1, despite it being listed as one of the working test configurations at https://gpuopen.com/radeon-open-compute-new-era-heterogeneous-in-hpc-ultrascale-computing-the-boltzmann-initiative-delivering-new-opportunities-in-gpu-computing-research/. Any suggestions on how to get this working?

---

### 评论 #9 — FinnStokes (2019-05-07T14:00:17Z)

Since this has drifted quite a bit from the initial question, I have created a separate issue #787 for my large BAR issues.

---

### 评论 #10 — FinnStokes (2019-07-10T18:19:33Z)

By replacing the motherboard, as described in #787, we were able to get the BARs correctly mapped and get OpenMPI transfers between two GPUs in the one node working. The next step will be to replace the motherboard on the other node, and change out one GPU in each node for Infiniband cards so we can test RDMA.

---

### 评论 #11 — tasso (2023-12-08T18:22:52Z)

were you able to get the other motherboard on the other node working?  Is the issue still reproducible?  If not; can we please close the issue?

---

### 评论 #12 — FinnStokes (2023-12-09T01:01:02Z)

Unfortunately this project was shelved indefinitely due to issues with our industry partner. We did replace the other motherboard, but there were issues with our interconnect that we were unable to solve before the project was shelved. I think the issue can be closed.

---

### 评论 #13 — tasso (2023-12-09T01:53:26Z)

Thanks Finn!  Sorry about the project.

---
