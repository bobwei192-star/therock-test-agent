# Problem with kernel 4.13

> **Issue #479**
> **状态**: closed
> **创建时间**: 2018-07-29T19:36:35Z
> **更新时间**: 2018-07-30T19:11:12Z
> **关闭时间**: 2018-07-30T19:11:12Z
> **作者**: Angel996
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/479

## 描述

This is 4x RX580 GPU system, AMD 970 motherboard, booting from USB flash.

On a fresh Ubuntu 16.04 LTS I am trying to install ROCM per this manual:

https://rocm.github.io/ROCmInstall.html

Since it suggests installing kernel 4.13, I decided to do so. After kernel installs and I reboot, I am getting lots of amd-vi completion-wait loop timed out messages. The system boots, however I cannot ssh to it (connection refused), I cannot login locally either: after I type in my username, I get the Login: prompt again w/o asking for password. So, I cannot reboot and I force power off. After that I cannot boot at all, I get the grub error "unknown file system" (not even getting to grub boot menu).

I did it 3 times, and it's always the same. With 4.4.0-116 I can boot normally. This setup also runs with amdgpu-pro w/o any problems under 4.4.0-116. Any ideas, please?

---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2018-07-30T05:16:30Z)

AMD 970? As in an AM3 or AM3+ consumer board?

If that is the case, please note that ROCm 1.8 requires a chipset with PCIe gen 3 with atomics support, as per the first section of the [ROCm README file](https://github.com/RadeonOpenCompute/ROCm). We have relaxed this support on gfx9-generation GPUs, such as Vega 10. This limitation still exists on gfx8-generation GPUs such as your RX580, however.

The AMD 970 chipset only supports PCIe gen 2, and thus does not meet these requirements.

---

### 评论 #2 — jlgreathouse (2018-07-30T19:11:11Z)

To give a bit more info to this: I have a test system where the motherboard does not support PCIe gen 3 atomics. It's an AMD 890FX. However, It has a FirePro W9100 in it, which is a "Hawaii"-based GPU (gfx701) that does **not** require PCIe gen 3 w/ atomics to work in ROCm.

I installed Ubuntu 16.04.0 (Linux 4.4.0-21) and tried installing ROCm 1.8.1 on top of it. It worked for me, and I was able to run test applications successfully.

I then purged rocm-dkms, manually upgraded to Linux 4.13.0-32, and reinstalled rocm-dkms. This also worked, and I was able to run test applications successfully.

Honestly (and yes, the documentation should likely be upgraded to say this), you can also just install to the latest 16.04 release (e.g. 16.04.4) and upgrade to the latest kernel release. I have a separate system running 4.15.0-29 at the moment, for instance.

Note that the only GPUs we support **without** PCIe gen 3 atomics are Hawaii (gfx701) and Vega 10 (gfx900). Your RX580 GPUs require gen 3 atomics and I strongly suspect that is why you are running into problems installing ROCm. This requirement does not exist in amdgpu-pro.

---
