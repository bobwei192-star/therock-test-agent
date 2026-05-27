# Incorrect VRAM / MMIO reads of RX 6900 XT in virtualized environment

> **Issue #1711**
> **状态**: closed
> **创建时间**: 2022-03-19T07:47:57Z
> **更新时间**: 2022-03-19T14:18:54Z
> **关闭时间**: 2022-03-19T14:18:54Z
> **作者**: haohui
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1711

## 描述

I've encountered  something funny when playing around with the virtualization support of ROCm on RX 6900 XT. My set up is to pass the RX 6900 XT to a Linux guest VM with vfio. I'm running vanilla Linux 5.15.0 and qemu 6.2.

The guest is able to recognize the GPU but it fails to load the PSP runtime database:

```
[    9.335351] amdgpu 0000:03:00.0: amdgpu: PSP runtime database doesn't exist
[   11.208301] [drm] Loading DMUB firmware via PSP: version=0x02010003
[   11.211139] [drm] use_doorbell being set to: [true]
[   11.211786] [drm] use_doorbell being set to: [true]
[   11.212374] [drm] use_doorbell being set to: [true]
[   11.212963] [drm] use_doorbell being set to: [true]
[   11.213735] [drm] Found VCN firmware Version ENC: 1.13 DEC: 2 VEP: 0 Revision: 20
[   11.214612] amdgpu 0000:03:00.0: amdgpu: Will use PSP to load VCN firmware
[   11.399185] [drm] reserve 0xa00000 from 0x83fe000000 for PSP TMR
[   11.516981] amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[   11.518130] amdgpu 0000:03:00.0: amdgpu: smu driver if version = 0x00000040, smu fw if version = 0x0000003d, smu fw version = 0x003a3f00 (58.63.0)
[   11.519613] amdgpu 0000:03:00.0: amdgpu: SMU driver if version not matched
[   11.520420] amdgpu 0000:03:00.0: amdgpu: use vbios provided pptable
[   11.593488] amdgpu 0000:03:00.0: amdgpu: SMU is initialized successfully!
[   11.594886] [drm] Display Core initialized with v3.2.149!
[   11.597609] [drm] DMUB hardware initialized: version=0x02010003
```

Then the kfd refuses to load again due to different versions of firmware on the card:

```
[   11.614269] kfd kfd: amdgpu: skipped device 1002:73bf, PCI rejects atomics 85<92
```

The exact same kernel initializes the GPU just fine on the host. The results are the same for vanilla kernels / qemu on Ubuntu 20.04. I looked at the source codes of the driver. It seems the checks are simply to read the values from VRAM / registers and to compare with the expected results.

The only logical explanation is that the guest VM somehow reads incorrect values from the GPU. It is quite unlikely to me since the initialization has gone this far.

Your helps and ideas are appreciated. 

---

## 评论 (2 条)

### 评论 #1 — haohui (2022-03-19T07:52:40Z)

Here is the complete command line for QEMU:

```
${QEMU} -kernel /boot/vmlinuz-5.15.0 -initrd initrd.img.gz \
	-nodefaults -nodefaults -nographic -serial stdio \
	-m 2048 \
	-accel kvm -cpu host \
	-bios bios64.bin \
	-machine q35,kernel-irqchip=on \
	-append "console=ttyS0" \
	-netdev user,id=net0,net=172.20.254.0/24,dns=10.3.2.100,hostfwd=tcp::10022-:22 \
    -device pcie-root-port,id=root.1,chassis=0,slot=0 \
	-device x3130-upstream,id=upstream_port1,bus=root.1 \
	-device xio3130-downstream,id=downstream_port1,chassis=11,slot=21,bus=upstream_port1 \
	-device vfio-pci,bus=downstream_port1,host=40:00.0,addr=00.0,multifunction=on \
	-device vfio-pci,bus=downstream_port1,host=40:00.1,addr=00.1 \
	-device vfio-pci,bus=downstream_port1,host=40:00.2,addr=00.2 \
	-device vfio-pci,bus=downstream_port1,host=40:00.3,addr=00.3 \
	-device virtio-net-pci,netdev=net0
```

I'm using the OVMF UEFI bios

---

### 评论 #2 — haohui (2022-03-19T14:18:54Z)

Turns out that the root cause is that QEMU fails to propagate the AtomicOps in the PCI express port. Following the description in the following thread works:

https://forum.level1techs.com/t/asus-wrx80e-sage-threadripper-pro-rx-6900-xt-works-on-host-but-not-in-vm/174245/6

---
