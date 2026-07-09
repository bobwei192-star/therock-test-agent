# Pcie atomics not enabled, hostcall not supported on gfx1100 RX7900

- **Issue #:** 2429
- **State:** closed
- **Created:** 2023-09-01T14:38:17Z
- **Updated:** 2023-12-21T16:02:53Z
- **Labels:** hardware:Radeon, application:pytorch
- **Assignees:** hongxiayang
- **URL:** https://github.com/ROCm/ROCm/issues/2429

I tried to use pytorch with ROCm, however it fails with 
```log
:1:rocvirtual.cpp           :2902: 1550313166 us: 7740 : [tid:0x7f5681dfb6c0] Pcie atomics not enabled, hostcall not supported
:1:rocvirtual.cpp           :3235: 1550313176 us: 7740 : [tid:0x7f5681dfb6c0] AQL dispatch failed!
HIP error: the operation cannot be performed in the present state
```

From previous issues in this repository, it seems like PCIe atomics were only a problem with gfx8 GPUs and old CPUs, so I'm wondering why I have this problem. I couldn't find much information about which CPUs support this feature and which don't. Is there a compatibility list somewhere?

ROCm version: 5.6
PyTorch: version: 2.1.0.dev20230901+rocm5.6
GPU: RX 7900 XT
CPU: i5-11400F

dmesg | grep atomic
```log
amdgpu 0000:03:00.0: amdgpu: PCIE atomic ops is not supported
```

However, I don't get the infamous `kfd: PCI rejects atomics`


<details>
    <summary>lspci -tv</summary>

    -[0000:00]-+-00.0  Intel Corporation Device 4c53
               +-01.0-[01-03]----00.0-[02-03]----00.0-[03]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Navi 31 [Radeon RX 7900 XT/7900 XTX]
               |                                            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Navi 31 HDMI/DP Audio
               +-06.0-[04]----00.0  Micron/Crucial Technology P5 Plus NVMe PCIe SSD
               +-14.0  Intel Corporation Tiger Lake-H USB 3.2 Gen 2x1 xHCI Host Controller
               +-14.2  Intel Corporation Tiger Lake-H Shared SRAM
               +-15.0  Intel Corporation Tiger Lake-H Serial IO I2C Controller #0
               +-16.0  Intel Corporation Tiger Lake-H Management Engine Interface
               +-17.0  Intel Corporation Device 43d2
               +-1c.0-[05]--
               +-1d.0-[06]--
               +-1f.0  Intel Corporation B560 LPC/eSPI Controller
               +-1f.3  Intel Corporation Tiger Lake-H HD Audio Controller
               +-1f.4  Intel Corporation Tiger Lake-H SMBus Controller
               +-1f.5  Intel Corporation Tiger Lake-H SPI Controller
               \-1f.6  Intel Corporation Ethernet Connection (14) I219-V
</details>
The device 00:01.0 is the PCIe x16 root port to which the GPU is connected, but it apparently does not support PCIe atomics (note the flags '32bit' and '64-bit'):

<details>
    <summary>lspci -vvvs 00:01.0</summary>

    ...
    DevCap2: Completion Timeout: Range ABC, TimeoutDis+ NROPrPrP- LTR+
                             10BitTagComp- 10BitTagReq- OBFF Via WAKE#, ExtFmt- EETLPPrefix-
                             EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                             FRS- LN System CLS Not Supported, TPHComp- ExtTPHComp- ARIFwd+
                             AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                    DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR+ 10BitTagReq- OBFF Disabled, ARIFwd-
                             AtomicOpsCtl: ReqEn+ EgressBlck+
    ...
</details>
I tried setting those bits with a udev rule which caused the error messages to disappear, but then it just freezes whenever any ROCm operation is performed on the GPU. Is there some BIOS setting or driver configuration required to enable PCIe atomics? Or is it simply that my CPU or mainboard doesn't support them?