# Desire VMware ESXi  support with  PCI passthrough, Issue VMware is not allowing PCIe Atomics to pass 

> **Issue #307**
> **状态**: closed
> **创建时间**: 2018-01-21T23:27:24Z
> **更新时间**: 2021-01-05T09:50:21Z
> **关闭时间**: 2021-01-05T09:50:21Z
> **作者**: ehrmann
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/307

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I'm trying to get use OpenCL on a GPU that's available in a VM through PCI passthrough. I'm already using PCI passthrough with this hypervisor, and the GPU shows up in dmesg and lspci:

```
00:00.0 Host bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge (rev 01)
00:01.0 PCI bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge (rev 01)
00:07.0 ISA bridge: Intel Corporation 82371AB/EB/MB PIIX4 ISA (rev 08)
00:07.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)
00:07.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08)
00:07.7 System peripheral: VMware Virtual Machine Communication Interface (rev 10)
00:0f.0 VGA compatible controller: VMware SVGA II Adapter
00:10.0 SCSI storage controller: LSI Logic / Symbios Logic 53c1030 PCI-X Fusion-MPT Dual Ultra320 SCSI (rev 01)
00:11.0 PCI bridge: VMware PCI bridge (rev 02)
00:15.0 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.1 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.2 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.3 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.4 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.5 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.6 PCI bridge: VMware PCI Express Root Port (rev 01)
00:15.7 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.0 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.1 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.2 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.3 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.4 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.5 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.6 PCI bridge: VMware PCI Express Root Port (rev 01)
00:16.7 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.0 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.1 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.2 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.3 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.4 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.5 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.6 PCI bridge: VMware PCI Express Root Port (rev 01)
00:17.7 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.0 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.1 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.2 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.3 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.4 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.5 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.6 PCI bridge: VMware PCI Express Root Port (rev 01)
00:18.7 PCI bridge: VMware PCI Express Root Port (rev 01)
02:00.0 USB controller: VMware USB1.1 UHCI Controller
02:01.0 USB controller: VMware USB2 EHCI Controller
02:03.0 SATA controller: VMware SATA AHCI controller
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67ef (rev cf)
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
13:00.0 Ethernet controller: VMware VMXNET3 Ethernet Controller (rev 01)
```

When I try run the HelloWorld demo as root, I get

```
Failed to find any OpenCL platforms.
Failed to create OpenCL context.
```

clinfo also fails:

```
$ sudo /opt/rocm/opencl/bin/x86_64/clinfo
[sudo] password for exobyte:
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
````
`rocm-smi` can't seem to find a GPU:

```
sudo /opt/rocm/bin/rocm-smi


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
Traceback (most recent call last):
  File "/opt/rocm/bin/rocm-smi", line 1058, in <module>
    showAllConcise(deviceList)
  File "/opt/rocm/bin/rocm-smi", line 728, in showAllConcise
    fan = str(getFanSpeed(device))
  File "/opt/rocm/bin/rocm-smi", line 358, in getFanSpeed
    fanLevel = int(getSysfsValue(device, 'fan'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
```

I'm using Ubuntu Xenial 16.04.3 (with the HWE kernel), and the kernel version is 4.13.0-26-generic. This is a recent Ubuntu installation, all packages are up-to-date, and I did a dist-upgrade. The same configuration without the hypervisor works fine. The GPU I'm using is a Radeon RX 460 (entry-level, but Polaris family, so supported). The CPU is a Skylake Core  i5-6600.

Here's the dmesg output from the VM where OpenCL doesn't work:
https://gist.github.com/ehrmann/f45b3200b80f7e9aa2e4f6a7faf00604

Here's the same output when running on physical hardware and OpenCL works fine:
https://gist.github.com/ehrmann/62cba6341493b8324fb240c742c8cc10

---

## 评论 (5 条)

### 评论 #1 — gstoner (2018-01-21T23:31:27Z)

You failing due to VMware not allowing PCIe Atomics aka atomic completor through



---

### 评论 #2 — ehrmann (2018-01-21T23:36:06Z)

> You failing due to VMware not allowing PCIe Atomics aka atomic completor through

Ah. Googling around, it looks like the ROCm team has seen this before with KVM and [talked to VMWare about it](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/26#issuecomment-313886018), too. Did the VMWare team have anything to say?

---

### 评论 #3 — gstoner (2018-01-24T01:07:29Z)

They are still looking at it. 

---

### 评论 #4 — ehrmann (2019-11-17T06:03:25Z)

Any updates? It's been almost two years.

---

### 评论 #5 — ROCmSupport (2021-01-05T09:50:21Z)

Hi @ehrmann 
I am closing this issue as its around 3 years old.
Request to try with the latest ROCm released version 4.0 and open a new issue if any.
Thank you.

---
