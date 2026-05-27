# Dual Radeon VII, X370 board, Tensorflow, Total Kernel Module Fail.

> **Issue #858**
> **状态**: closed
> **创建时间**: 2019-08-08T04:28:21Z
> **更新时间**: 2024-01-11T03:40:51Z
> **关闭时间**: 2024-01-11T03:40:51Z
> **作者**: emerth
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/858

## 描述

**Synopsis**

Multi-GPU ROCm experiences amdgpu kernel module corruption.
Running process on either GPU individually succeeds: this is using either PCIe slot.
Running process on both GPUs simultaneously fails.
Both slots are PCIe3 x8 directly attached to CPU, no PCIe switch involved. 
GPU located in either slot works with ROCm, the fail only happens when I try to use both GPUs at the same time.

**System details**

2 Radeon VII with vbios 106 patch applied.
Ryzen 1600X CPU
Asus Prime X370 Pro, BIOS July 2019
64 GB DDR4 2666 (GSkill F4-266615D-32GVR, 2 kits)
850W Thermaltake (mumble mumble) PSU
Ubuntu 18.04.3
Kernel "Linux gpu 4.15.0-55-generic #60-Ubuntu SMP Tue Jul 2 18:22:20 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux"
ROCm 2.6 rocm-dkms
Tensorflow-rocm 1.14 for Python 2.7 installed via pip.

**What I am trying to do**

Trying to run Tensorflow slim's models/research/slim/train_image_classifier.py script utilizing both GPUs. Model is inceptionv1, data is 250 categories grabbed at random from imagenet 2012 challenge dataset. This script works flawlessly on multi-GPU setups from the Green Team.

**What's happening**

If I restrict TF to use either GPU individually by setting environment variable CUDA_VISIBLE_DEVICES to 0 or 1, and passing "--num_clones 1" to train_image_classifier.py then training proceeds on the indicated GPU in the normal manner.

If I unset CUDA_VISIBLE_DEVICES and pass "--num_clones 2" to train_image_classifier.py, then both GPUs are utilized but after a short while several bad things happen:

Bad thing 1) TF freezes,

Bad thing 2) rocm-smi errors out (strings of equals sign in the header & footer removed, they confuse github formatting):

```
	root@gpu:~# rocm-smi
 
       ROCm System Management Interface
 	WARNING: GPU[0] : Unable to read /sys/class/hwmon/hwmon0/temp1_input
 	WARNING: GPU[0] : Unable to read /sys/class/hwmon/hwmon0/temp1_input
 	WARNING: GPU[0] : Unable to read /sys/class/hwmon/hwmon0/power1_average
 	WARNING: GPU[0] : Unable to read /sys/class/drm/card0/device/pp_dpm_sclk
 	WARNING: GPU[0] : Unable to read /sys/class/drm/card0/device/pp_dpm_mclk
 	WARNING: GPU[0] : Unable to read /sys/class/hwmon/hwmon0/pwm1
 	WARNING: GPU[0] : Unable to read /sys/class/drm/card0/device/gpu_busy_percent
 	WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon1/temp1_input
 	WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon1/temp1_input
 	WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon1/power1_average
 	WARNING: GPU[1] : Unable to read /sys/class/drm/card1/device/pp_dpm_sclk
 	WARNING: GPU[1] : Unable to read /sys/class/drm/card1/device/pp_dpm_mclk
 	WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon1/pwm1
 	WARNING: GPU[1] : Unable to read /sys/class/drm/card1/device/gpu_busy_percent
 	GPU  Temp  AvgPwr  SCLK  MCLK  Fan    Perf  PwrCap  VRAM%  GPU%
 	0    N/A   N/A     N/A   N/A   None%  auto  250.0W   54%   N/A
 	1    N/A   N/A     N/A   N/A   None%  auto  250.0W   53%   N/A
	End of ROCm SMI Log 
 

```

Bad thing 3: syslog and kernlog receive messages:
```
Aug  8 01:32:52 localhost kernel: [ 3147.377086] Started restoring pasid 32768
Aug  8 01:32:52 localhost kernel: [ 3147.377847] Restoring PASID 32768 queues
Aug  8 01:32:52 localhost kernel: [ 3147.377856] Restoring PASID 32768 queues
Aug  8 01:32:52 localhost kernel: [ 3147.377870] Finished restoring pasid 32768
Aug  8 01:33:08 localhost kernel: [ 3163.119865] Signal event wasn't created because limit was reached
Aug  8 01:33:26 localhost kernel: [ 3181.587314] pcieport 0000:00:03.1: AER: Multiple Uncorrected (Fatal) error received: id=0000
Aug  8 01:33:26 localhost kernel: [ 3181.629625] pcieport 0000:00:03.1: PCIe Bus Error: severity=Uncorrected (Fatal), type=Transaction Layer, id=0019(Receiver ID)
Aug  8 01:33:26 localhost kernel: [ 3181.630510] pcieport 0000:00:03.1:   device [1022:1453] error status/mask=00040000/04400000
Aug  8 01:33:26 localhost kernel: [ 3181.631159] pcieport 0000:00:03.1:    [18] Malformed TLP          (First)
Aug  8 01:33:26 localhost kernel: [ 3181.631687] pcieport 0000:00:03.1:   TLP Header: 1f000001 00000000 00000000 e750772f
Aug  8 01:33:26 localhost kernel: [ 3181.632291] pcieport 0000:00:03.1: broadcast error_detected message
Aug  8 01:33:26 localhost kernel: [ 3181.632294] amdgpu 0000:0a:00.0: device has no AER-aware driver
Aug  8 01:33:26 localhost kernel: [ 3181.632296] snd_hda_intel 0000:0a:00.1: device has no AER-aware driver
Aug  8 01:33:27 localhost kernel: [ 3182.429577] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.430155] amdgpu: [powerplay] [CopyTableFromSMC] Attempt to Set Dram Addr High Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.430156] amdgpu: [powerplay] Failed to export SMU metrics table!
Aug  8 01:33:27 localhost kernel: [ 3182.431463] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.432037] amdgpu: [powerplay] [CopyTableFromSMC] Attempt to Set Dram Addr High Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.432037] amdgpu: [powerplay] Failed to export SMU metrics table!
Aug  8 01:33:27 localhost kernel: [ 3182.432702] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.433288] amdgpu: [powerplay] [CopyTableFromSMC] Attempt to Set Dram Addr High Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.433289] amdgpu: [powerplay] Failed to export SMU metrics table!
Aug  8 01:33:27 localhost kernel: [ 3182.433390] amdgpu: [powerplay] Failed to send message 0x2d, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.433963] amdgpu: [powerplay] [GetCurrentClkFreq] Attempt to get Current Frequency Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.433964] amdgpu: [powerplay] Attempt to get current gfx clk Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.434060] amdgpu: [powerplay] Failed to send message 0x2d, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.434633] amdgpu: [powerplay] [GetCurrentClkFreq] Attempt to get Current Frequency Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.434634] amdgpu: [powerplay] Attempt to get current mclk freq Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.435319] amdgpu: [powerplay] Failed to send message 0x3c, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.435894] amdgpu: [powerplay] Attempt to get current RPM from SMC Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.437320] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.437894] amdgpu: [powerplay] [CopyTableFromSMC] Attempt to Set Dram Addr High Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.437894] amdgpu: [powerplay] Failed to export SMU metrics table!
Aug  8 01:33:27 localhost kernel: [ 3182.673399] pcieport 0000:00:03.1: Root Port link has been reset
Aug  8 01:33:27 localhost kernel: [ 3182.673404] pcieport 0000:00:03.1: AER: Device recovery failed
Aug  8 01:33:28 localhost kernel: [ 3183.492500] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff

```
ad infinitum.

Bad thing 4: the screen goes blank, and the machine requires a hard reset to recover.

The fail happens after a few tens of iterations, up to 170 iterations.

Googling for solutions, here are things that had no effect on either single GPU or dual GPU training runs:

1. Dis/abling IOMMU in BIOS has no effect.
2. Uninstall ROCM. Reboot. Reinstall ROCM.
3. Uninstall tensorflow et al. Reinstall tensorflow et al.
4. Add "pci=noaer" to grub linux command line makes the TLP & AER error messages go away but TF still fails and rocm-smi cannot read anything under /sys.
 
Has anyone solved this kind of problem before?

I **_think_** there is a problem with the GPUs trying to communicate with each other across PCIe and addressing bytes above a 4GB ceiling - this may be the source of the "Malformed TLP" error message.

Can anyone either tell me that my though is completely wrong, or point me at info about how to configure the address range windows used by the GPUs (PCIe BARs I think they are called)?
The mobo has no BIOS option to enable or disable above 4GB addressing in it's PCIe settings.

(BTW, even if it's not your specific area of work, congrats on Rome: it looks like an Intel Killer.)


---

## 评论 (12 条)

### 评论 #1 — JMadgwick (2019-08-08T09:16:45Z)

Although this problem isn't necessarily specific to Tensorflow, you might want to post in the [Tensorflow issues](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues). The devs there are very active. You are much less likely to get a response posting here. Have you tried other multi-GPU programs? If they work then it will be a Tensorflow related problem.

---

### 评论 #2 — emerth (2019-08-08T12:46:32Z)

> 
> 
> Although this problem isn't necessarily specific to Tensorflow, you might want to post in the [Tensorflow issues](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues). The devs there are very active. You are much less likely to get a response posting here. Have you tried other multi-GPU programs? If they work then it will be a Tensorflow related problem.

Hello James, 

Thanks for your response and your comments on elementary problem analysis.  Do you have anything related to my questions?



---

### 评论 #3 — JMadgwick (2019-08-08T13:49:57Z)

> Can anyone either tell me that my though is completely wrong, or point me at info about how to configure the address range windows used by the GPUs (PCIe BARs I think they are called)?
> The mobo has no BIOS option to enable or disable above 4GB addressing in it's PCIe settings.

You're right that I didn't read through your post fully. I apologise for that.
You have the right idea about this though. One GPU is going to work fine because there is no intercommunication. With 16GB of RAM per GPU there is no way that this is going to work without "above 4G decoding" enabled.
This is suggested [in the documentation](https://rocm.github.io/ROCmPCIeFeatures.html#bar-memory-overview) and I can't see any indication that it can be configured manually at all. Changing the BAR window isn't mentioned anywhere and even if it was possible the driver would need to be able to shrink the window down to below 2GB per GPU to fit. It wouldn't be possible to map the whole of the GPUs memory, so I doubt that even if it was theoretically possible for these two GPUs to somehow communicate using a smaller window the driver wouldn't be designed for and expecting it. Even if all that was possible you could only use under 2GB on each GPU which would likely ruin performance or prevent the model from running at all.

> The mobo has no BIOS option to enable or disable above 4GB addressing in it's PCIe settings.

This seemed odd to me but searching around it seems that [some Motherboards do seem to have omitted this option](https://www.reddit.com/r/EtherMining/comments/6khmnt/asrock_ab350_pro_4_has_no_above_4g_decoding_option/). I would contact Asus and see what they have to say about this, there is no good reason at all to remove this option.
I checked the manual for a Biostar X370 board of mine and it has the option under "PCI Subsystem Settings". I looked in the manual for your Motherboard and it doesn't mention it at all. The default setting of "Above 4G Decoding" is disabled because it causes problems with 32-bit OSes.

Therefore I recommend that you use a different motherboard which does support this option, **OR** you could try to edit the BIOS for your motherboard.[ There is some info which happens to cover your exact motherboard.](https://puissanceled.com/vrac/Bios_modding/EN.html) Using that BIOS editor you could set the BIOS option to visible and then enable it after flashing the modified BIOS.
However I downloaded the latest BIOS for your motherboard and opened in the BIOS editor. [According to the editor the Option is set to visible by default](https://imgur.com/BhkXyQB)? You should be able to see it? Regardless you could try setting the defaults to enabled. It is of course dangerous to modify and flash BIOSes, so I really wouldn't recommend it but I can't see any other option bar buying a different board.

There's a mention of above 4G decoding problems on Nvidia [here](https://www.servethehome.com/nvidia-smi-issues-get-nvidia-cuda-working-grid-tesla-gpus/) and [here](https://nvidia.custhelp.com/app/answers/detail/a_id/4119/~/incorrect-bios-settings-on-a-server-when-used-with-a-hypervisor-can-cause-mmio).

---

### 评论 #4 — emerth (2019-08-08T15:07:03Z)

My goodness, the things I learn on Github! A GUI BIOS image editor! 

Thanks for the confirmation about PCIe above 4G decoding. I've a higher spec board I will try before editing the BIOS image, but it's good to know I can go that route if I must.

---

### 评论 #5 — sos-michael (2019-08-10T08:56:16Z)

Try adding:

`pci=assign-busses,nocrs,realloc` 

To your boot parameters. You most likely don't need all of them but its a nice easy catch-all that might help.

---

### 评论 #6 — emerth (2019-08-10T17:13:26Z)

> 
> 
> Try adding:
> 
> `pci=assign-busses,nocrs,realloc`
> 
> To your boot parameters. You most likely don't need all of them but its a nice easy catch-all that might help.

Hi Michael,

Thanks, I will give this a try. Sadly it looks like I may have been experiencing a slow hardware fail too, as card #2 has died on me. When the RMA process is finished and I have a replacement I'll post back the results.

---

### 评论 #7 — emerth (2020-02-06T18:53:54Z)

@sos-michael 

Sorry I took a long time to post back. This has proven to be rather Heisenberg-ish. 

I got my defective card replaced, and that solved the problem of the module fail. However the BIOS still refused to map the entire 16GB address space of the two cards, but only mapped a 2MB (IIRC) window. This was some months ago in Fall, 2019.

In January 2020 I gave it another go because ROCm 3 came out. Just on the off chance because ROCm does not  set up the BIOS, but WTH, eh?

This time, same mother board, same cards, same BIOS version, both cards are mapped well above 4GB and their entire 16GB space is visible, and ROCm (MiOpen) can use both cards without error.

I have no idea why it works now. I didn't upgrade the BIOS or change anything other than the boot drive setting.

---

### 评论 #8 — JMadgwick (2020-02-06T19:32:44Z)

Presumably, if nothing else changed except for the version of ROCm, then that must have been what fixed it? At least you can close this now.

---

### 评论 #9 — emerth (2020-02-06T21:59:00Z)

James, are you here just to muddy the waters and confuse the issues?

PCIe BARs are set up before the kernel even loads, during PCIe bus autonegotiation, a hardware level thing. ROCm new version did not cause the motherboard to decide to map the VRAM differently. ROCm, being a collection of software running atop an operating system, does not have the ability to reset or set up the memory mapping built by the BIOS/EFI at system POST. 

But you immediately jump to the conclusion "things are fixed by new versions". This is BS.

I mean, you went to Uni and all, you should know this. 

---

### 评论 #10 — JMadgwick (2020-02-06T22:18:39Z)

If what you say is true then the new version of ROCm can't have made any difference. It  would also mean that your problem had nothing to do with ROCm, the kernel module or Linux at all and never did. In which case this issue should be closed and you should discuss the matter with the manufacturer of your motherboard as I mentioned before.

Except that you claim not to have changed anything on the motherboard. It this were true, it would mean that whatever fixed the problem must have happened at the kernel level or above, unless there was in fact no problem initially or somehow it was actually unrelated to the error messages seen which is very unlikely.

I don't see how the issue could be confused any more than it already is. You claim that ROCm has an issue then rebuff my comments saying that it can't in fact have anything to do with ROCm! Which is what I had been saying from the beginning.

What you have said confirms my original view that this is not a ROCm problem. You say that nothing has changed regarding motherboard configuration. Clearly something has to give, you can't get a different result from the same state here, clearly the motherboard is working differently.

My Ryzen motherboard decides to change settings on its own and reset the CMOS at random. Even changing the boot options could be affecting how the board configures the PCIe bus. Of course this shouldn't have any impact but these BIOSes are well known to behave in strange ways.

---

### 评论 #11 — emerth (2020-02-06T22:34:16Z)

I quote from my OP:

> I think there is a problem with the GPUs trying to communicate with each other across PCIe and addressing bytes above a 4GB ceiling - this may be the source of the "Malformed TLP" error message.
> 
> Can anyone either tell me that my though is completely wrong, or point me at info about how to configure the address range windows used by the GPUs (PCIe BARs I think they are called)?
> The mobo has no BIOS option to enable or disable above 4GB addressing in it's PCIe settings.

I quote your answer to my OP:

> Although this problem isn't necessarily specific to Tensorflow, you might want to post in the Tensorflow issues. The devs there are very active. You are much less likely to get a response posting here. Have you tried other multi-GPU programs? If they work then it will be a Tensorflow related problem.

I quote from your answer to my response to that:

> You're right that I didn't read through your post fully. 

I quote from my comment to sos-michael, who actually had a reasonable suggestion:

> I have no idea why it works now. I didn't upgrade the BIOS or change anything other than the boot drive setting.

And your response to that:

> Presumably, if nothing else changed except for the version of ROCm, then that must have been what fixed it? At least you can close this now.

Nowhere did I say ROCm causes the problem. Quite the opposite, in my OP I say I think it's a hardware problem and asked for confirmation. And asking at ROCm is the right place to ask because the ROCm devs ought to know about the failure modes of their software given a problem with a required hardware config.

At every point in your involvement you either deflect (go talk to the TF people), or bring in rather strange solutions (hack the BIOS image for the mobo), or suggest the v3 ROCm release is what made my mobo map the cards properly (patently not the case).

So, I'll just ask my question again: James, are you here just to muddy the waters and confuse the issues?

You're kind of like those people in Ubuntu help forums who answer questions by saying "Why would you want to do that?" and then answering some other question than the one asked.

Oh, and the issue was closed last August 22.

---

### 评论 #12 — nartmada (2024-01-11T03:40:51Z)

Closing this ticket as issue has been fixed.

---
