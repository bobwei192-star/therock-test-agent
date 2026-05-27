# Clarification regarding PCI-Express requirements

> **Issue #594**
> **状态**: closed
> **创建时间**: 2018-10-29T16:21:40Z
> **更新时间**: 2018-11-06T17:43:53Z
> **关闭时间**: 2018-11-06T17:43:53Z
> **作者**: artyom-beilis
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/594

## 描述

I have multi-GPU setup, one NVidia GTX 960 and another [AMD RX 560 Baffin 16CU/1024 cores](https://www.msi.com/Graphics-card/Radeon-RX-560-AERO-ITX-4G-OC/Specification).

Due to size restrictions I can plug GTX 960 only to PCIEX16 slot and RX 560 to PCIEX4 slot

MB is GA-B150M-D3H-DDR3  [All of the PCI Express slots conform to PCI Express 3.0 standard](https://www.gigabyte.com/Motherboard/GA-B150M-D3H-DDR3-rev-10#sp) and according to the documentation PCI Express 3.0 should be enough 

In such a configuration ROCM driver complains on atomics on PCIEX4 slot - not allowing to run neither OpenCL nor HIP - dmesg reports `PCI rejects atomics`

Notes:

1. ROCM driver works when the RX 560 installed in PCIEX16 slot but for this purpose I need to remove GTX 960 card.
2. When AMDGPU-PRO drivers where installed AMD RX 560 worked on PCIX4 slot - but it does not support hip (and so hipCaffe/tensorflow-hip)

Questions:

1. why atomics are not supported it should be PCI Express 3 connection?
2. Is it possible to enable RX 960 on second PCIEX4 slot without atomics

Setup:

1. Using ROCM 1.9.2 from official repositories
2. Running Ubuntu 16.04, Kernel 4.15

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-10-29T16:42:21Z)

It's possible that the second PCIe slot on your motherboard is actually connected to the B150 chipset. Looking at the CPU support list for this motherboard, even the [highest-end processor it supports](https://ark.intel.com/products/97128/Intel-Core-i7-7700-Processor-8M-Cache-up-to-4-20-GHz-) only includes 16 PCIe gen 3 lanes directly connected to the CPU. As such, my suspicion is that PCI1, PCI2, and PCIEX4 are [connected through the chipset](https://ark.intel.com/products/90592/Intel-B150-Chipset).

The datasheet for the B150 chipset makes no mention of support for the optional atomics extension to PCIe 3.0. Note that PCIe 3.0 compatibility does not mean that a slot supports PCIe 3.0 atomics, as those are a feature that [PCIe 3.0-compliant devices (including bridges) need not support](https://pcisig.com/sites/default/files/specification_documents/ECN_Atomic_Ops_080417.pdf).

It is not possible at this time to enable gfx8 devices without the use of PCIe atomics. See [this discussion](451#issuecomment-422836032) for many more details about this.

---

### 评论 #2 — artyom-beilis (2018-10-29T19:21:06Z)

The problem that putting all mid range GPU like 560/570/580 out of scope for large range of applications including use of eGpu via thunderbolt. Additionaly it is somthing not obvious when you get a GPU and discover that hip/rocm would not work in perfectly normal PCIE slot, like NVIDIA gpus do

---

### 评论 #3 — jlgreathouse (2018-10-29T19:36:37Z)

I'll note that I've given a much longer discussion of why we do not currently support gfx8 without PCIe atomics in [the linked thread](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422836032). I appreciate your request and the reasons behind it, but I don't plan to rehash the same discussion here.

---
