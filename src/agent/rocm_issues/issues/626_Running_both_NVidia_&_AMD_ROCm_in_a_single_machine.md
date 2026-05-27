# Running both NVidia & AMD ROCm in a single machine

> **Issue #626**
> **状态**: closed
> **创建时间**: 2018-11-27T01:47:58Z
> **更新时间**: 2019-01-07T17:41:43Z
> **关闭时间**: 2019-01-07T17:41:43Z
> **作者**: briansp2020
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/626

## 描述

I have Ryzen 7 1800X and want to use both VEGA FE & GTX 1080 in that machine. I can use either GPU separately without issues. GTX1080 also works fine by itself in the secondary PCIe slot. However, if I put both graphics cards in, GUI does not come up even though I can log in to console and see that both graphics cards are working by using lspci/nvidia-smi/rocm-smi commands. Also, only the output from Vega seems to work, probably because MB initializes graphics card in the first PCIe slot. Since my motherboard is GA-AB350M-D3H (https://www.gigabyte.com/us/Motherboard/GA-AB350M-D3H-rev-10#kf), I must install VEGA FE in the first PCIe slot.

Is there a way go get both working? Preferably, I'd like to use GTX 1080 to drive the monitor.
Any help and pointers are appreciated. I tried https://askubuntu.com/questions/892532/nvidia-card-for-cuda-and-amd-card-for-display-on-ubuntu-16-04 but that does not seem to quite work for Ubuntu 18.04 which is what I'm running.

Thanks!

---

## 评论 (7 条)

### 评论 #1 — Avatat (2018-12-05T05:15:26Z)

Are you using Wayland or Xorg?

Remember, that Ryzen CPUs has only 16 PCIe lanes for GPU, so your GPUs will work on PCIe x8 only - it could have an impact on computing speed, especially when you have fast GPUs as yours.

---

### 评论 #2 — Mandrewoid (2018-12-14T23:17:32Z)

@briansp2020 there are a few experts on https://forum.level1techs.com that are using AMD & nvidia GPU's both on the same machine on linux, although they are doing it for gaming, they might be able to help you get your gui up and running. 

---

### 评论 #3 — emerth (2018-12-18T17:35:01Z)

If you are using X, yes you can. I don't know anything about Wayland.

This is roughly how I did it:

1. Put the nVidia card in first x8 or x16 PCIe slot.
2. Put the AMD card in second PCIex8 or x16 slot.
3. Update/upgrade your OS system per whatever  distribution you use. 
4. Ensure you are running a recent 4.1x kernel.
5. Install CUDA in the normal manner, make sure it works. Do CUDA first because you'll probably get to fight with nouveau for a while and it always sucks to corrupt the system while fighting nouveau as the very last step in an install.
6. Install ROCm per the instruction on the ROCm github page.
7. Enjoy!

The location of the cards seemed to matter a lot. If the nVidia card was not in slot 1, then CUDA would get irritated.

---

### 评论 #4 — briansp2020 (2018-12-18T18:00:27Z)

@emerth 
Could you mind telling me the system spec? Do you have a platform that supports NVidia SLI?

---

### 评论 #5 — emerth (2018-12-18T18:51:33Z)

I did the ROCm+CUDA thing on this system:

- ASUS Crosshair VI Hero (X370 not X470).
- Ryzen 1700
- GTX 1080 - "MSI Seahawk X" IIRC - the AIO water cooled card.
- RX Vega 64 - Gigabyte blower design.
- Mellanox MT26428 QDR Infiniband.
- 32 GB RAM - four sticks of KHX2666C15D4/8G.
- Ubuntu 16.04 Server originally. Later Ubuntu 16.04 Workstation.

Later I rebuilt it using a GTX 970 and an RX 470 instead. Same procedure though.

Running Ubuntu Workstation I installed CUDA and told the nVidia driver installer to configure X. Then I verified that X loaded with nVidia driver and that CUDA worked. 

Then I backed up my /etc/X directory tree.

Then I installed ROCm. 

I do not recall needing to run nvidia-xconfig tool afterward. But this was a year ago...

If the ROCm install clobbers your nVidia X configuration, you can just restore the xconfig file from your backup, and make sure the nvidia module is getting loaded at boot. FWIW I've never done SLI on this machine or any other, so whatever has to be done about SLI and X, I've no idea.

This system does support SLI. But the spec is  pair of PCIe3 x16 physical slots that operate as x16/nought or x8/x8, and an x4 PCIe2 slot. So if I added a second GTX1080 I'd have nowhere to put the Vega. 

---

### 评论 #6 — Avatat (2018-12-18T19:06:42Z)

It doesn't matter if setup supports SLI or CrossFireX.

---

### 评论 #7 — briansp2020 (2019-01-07T17:41:12Z)

I was able to get it to work. Two things I did were:
1) update the BIOS to the latest GA-AB350M-D3H (rev. 1.0)  F24
2) Set BIOS option to use PCIe 2nd slot by for initial disply.

With those two changes, I can now run 1080 in the second slot and Vega FE in the first slot which is exactly what I wanted. 1080 performance took a hit because my second slot is through the chipset but they are working now. :+1: 

---
