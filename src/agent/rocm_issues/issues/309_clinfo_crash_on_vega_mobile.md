# clinfo crash on vega mobile

> **Issue #309**
> **状态**: closed
> **创建时间**: 2018-01-24T00:27:57Z
> **更新时间**: 2018-01-24T01:02:22Z
> **关闭时间**: 2018-01-24T01:02:22Z
> **作者**: kiritigowda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/309

## 描述

I am trying to install rocm on AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx × 8 with ubuntu 16.04 LTS.

When I do the 

````
sudo apt dist update
````
I get the following error and after the rocm install the clinfo fails.

````
Processing triggers for bamfdaemon (0.5.3~bzr0+16.04.20160824-0ubuntu1) ...
Rebuilding /usr/share/applications/bamf-2.index...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for initramfs-tools (0.122ubuntu8.10) ...
update-initramfs: Generating /boot/initrd.img-4.13.0-31-generic
W: Possible missing firmware /lib/firmware/amdgpu/raven_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/raven_vcn.bin for module amdgpu
Processing triggers for ca-certificates (20170717~16.04.1) ...
Updating certificates in /etc/ssl/certs...
17 added, 42 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
Processing triggers for resolvconf (1.78ubuntu5) ...
Processing triggers for systemd (229-4ubuntu21) ...
Processing triggers for ureadahead (0.100.0-19) ...

````

---

## 评论 (1 条)

### 评论 #1 — gstoner (2018-01-24T01:02:22Z)

I have to ask a quick question,  did you read the install instruction and also supported hardware list.   Raven is not supported in ROCm 1.7  

---
