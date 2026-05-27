# AMD Mi50 no longer being detected by ROCM

> **Issue #1552**
> **状态**: closed
> **创建时间**: 2021-08-09T18:23:40Z
> **更新时间**: 2022-07-04T18:23:19Z
> **关闭时间**: 2021-08-17T03:44:39Z
> **作者**: SAchuth
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1552

## 描述

Hi there, I have a AMD Radeon Instinct Mi50 GPU which I am trying to use on a Ubuntu 20.04 server. This GPU has worked in the past with my setup, however, recently when I try to use the GPU I'm seeing the GPU is not detected. The amdgpu kernel module appears to have an issue loading.

Thanks
[dmesg_output_mi50.txt](https://github.com/RadeonOpenCompute/ROCm/files/6956556/dmesg_output_mi50.txt)


---

## 评论 (12 条)

### 评论 #1 — ROCmSupport (2021-08-10T12:53:09Z)

Thanks @SAchuth for reaching out.
From the dmesg, looks like its problem with hardware
**Fatal error during GPU init**
I will pull kernel expect to look into this issue. 
Thank you.

---

### 评论 #2 — ROCmSupport (2021-08-11T09:52:32Z)

Hi @kentrussell 
Please take a look at this request and do the needful

---

### 评论 #3 — kentrussell (2021-08-11T12:55:03Z)

As @ROCmSupport pointed out, there is an uncorrectable error in dmesg. Also note, a full dmesg would be a lot more useful, since not every useful kernel message has "amdgpu" in it (e.g. PCI detecting HW errors). Just for reference.
If you can add a full dmesg, that would help us to try to narrow down the HW issue, but there are a couple things that you can try to do in the interim (depending on how much time you have to debug)
Reseating the GPU is always worth a shot when HW errors show up. You never know what a power cycle and a HW adjustment can do. It's unlikely to address it, but for a 10min task, it's always worth a shot (also, you can try a different PCIe bus if there is another one available on the board)
You can disable RAS via the kernel parameter amdgpu.ras_enable=0 , which disables all RAS functionality. It would avoid this HW error (unless the PCI driver picks it up instead), which isn't great but is a way to work around things, but is also a potential workaround.
Lastly, if the card is under warranty still, I'd consider RMA-ing it, since a HW failure under warranty is often far easier to just RMA than to try to work around, with the hope that it doesn't get worse outside of the warranty coverage.


---

### 评论 #4 — SAchuth (2021-08-11T22:48:19Z)

Hi @kentrussell,

Thanks for following up. I've attached a full dmesg log here.

Yes, I've tried the usual steps with power cycling and reseating the card with no luck. Adding the kernel parameter also didn't seem to help with the problem. 
 
[full_dmesg_output_mi50.txt](https://github.com/RadeonOpenCompute/ROCm/files/6971802/full_dmesg_output_mi50.txt)


---

### 评论 #5 — kentrussell (2021-08-12T12:21:12Z)

Sorry, I wasn't as clear as I should've been. Can you add amdgpu.ras_enable=0 to the kernel parameters and then reboot it, then attach that full dmesg? Here the UE is being detected, then the KIQ ring test fails, and finally the GFX IP block fails to initialize. I am just REALLY hoping that if we skip the ECC/RAS initialization, that the KIQ ring test manages to pass. It's not guaranteed, but it's something to pursue before looking at HW failure.

In that full dmesg, the kernel command line didn't show the amdgpu.ras_enable=0 part, so if you're adding the parameter to /etc/default/grub, make sure to "sudo update-grub" afterwards to make it kick in. Otherwise you can either add it in the GRUB before you boot, or you can throw it into /boot/grub/grub.cfg after the "reboot=pci" part. Thanks!

I'm worried that it's starting to look like a HW failure, but hopefully the last dmesg can give me some other options aside from replacing the card. Fingers crossed!

---

### 评论 #6 — SAchuth (2021-08-13T01:29:56Z)

Hi @kentrussell ,

Here is a copy of the dmesg log with the kernel parameter added in as you specified. 
[full_dmesg_output_mi50_w_ras_disabled.txt](https://github.com/RadeonOpenCompute/ROCm/files/6979384/full_dmesg_output_mi50_w_ras_disabled.txt)

Thanks!

---

### 评论 #7 — kentrussell (2021-08-13T12:14:25Z)

Thanks for that. At least now we're hitting a different error, so RAS disablement got past those RAS errors. Since PSP isn't loading, the only other thing I can think of is trying to get the VBIOS updated (you're on v107, I believe that v111 is the latest one) There's always the option of trying the newer ROCm 4.3 release in case there's a firmware issue (though I don't see any issues reported internally on 4.2 WRT MI50). I am just hoping we can try everything non-HW just to try to work through this. Thanks for your efforts on this, hopefully we'll find a solution soon!

---

### 评论 #8 — SAchuth (2021-08-13T20:16:18Z)

Hi Kent, 
Would you be able to direct me to steps on updating the VBIOS of the Mi50? Also, just want to check with you if anything goes wrong with updating the VBIOS will it affect whether or not I can RMA the card?



---

### 评论 #9 — kentrussell (2021-08-16T12:57:20Z)

So it looks like we haven't released any newer VBIOSes for MI50 officially. I only found the one for the old Fiji cards (Fury X or Nano), which obviously won't work. Sorry for the confusion there, I know we've got these internal engineering VBIOSes which are obviously not publicly available, I had just assumed that we had some large repository of VBIOSes for public consumption. Turns out I was very wrong on that.

I would get in touch with the RMA guys at https://www.amd.com/en/support/kb/warranty-information/workstation-graphics . They may have the resources there to flash the VBIOS (since Windows does it through the Catalyst Control Centre, but Linux methods are not official, as far as I can tell). There are non-AMD websites with amdvbflash (the tool to flash the VBIOS in Linux) but I don't see the official MI50 VBIOS available anywhere, so the tool isn't very helpful there. And flashing things using non-AMD-sourced software (non-AMD amdvbflash or non-AMD official VBIOSes) will definitely risk the warranty.

If the RMA guys have access to them and can give it to you as part of their "basic troubleshooting before replacement" process, then awesome. If not, just link them to this ticket and explain that the GPU is throwing hardware errors and that troubleshooting with an AMD Linux dev resulted in the conclusion that the card is faulty.. They can track me down internally if they have any questions, but hopefully they can square you away. Sorry again for misleading you regarding the VBIOS update, but hopefully the warranty guys can square you away with new one quickly!

---

### 评论 #10 — ROCmSupport (2021-08-17T03:44:39Z)

Helped with resolution, closing it now.
Fell free to open a new issue, if any, for quick resolutions.
Thank you.

---

### 评论 #11 — Epliz (2022-07-04T16:33:23Z)

@SAchuth , if you have managed to solve your issue, could you please indicate how?
I am facing a very similar issue, and would appreciate any help.

---

### 评论 #12 — Epliz (2022-07-04T18:23:19Z)

Alright, turns out that for me just upgrading the Linux kernel did the trick for me.
Even though it was indicating RAS errors before.

---
