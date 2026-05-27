# Vega 64 power limit

> **Issue #458**
> **状态**: closed
> **创建时间**: 2018-07-15T12:09:43Z
> **更新时间**: 2018-12-24T22:49:03Z
> **关闭时间**: 2018-12-24T22:39:21Z
> **作者**: Wacholek
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/458

## 描述

Hi, 
In ROCm-SMI a OC function was implemented. There is possibility to change clock profile for GPU and memory ( does not work) and OC the highest GPU profile by setting --setoverdrive %. But in my case almost non of this does not matter because there is power limit of 220W. 
Is there any way to pass this 220W? Any extra power limit extension?

Recently I flashed my card with Vega 64 LC edition bios. There is a limit to 264W but still, I cannot use the full capability of the card and I am the stack to 1560MHz. This card is working flawlessly at 1770Mhz @365W so I am losing a lot of computing power. 
GPU voltage control would also be a very nice feature.

---

## 评论 (11 条)

### 评论 #1 — ghost (2018-07-22T15:56:53Z)

The limit is in there because of pci specs, to bypass the power limit would require you to mod the bios to the point it will and probably not function on windows and would only work on certain linux configurations .

---

### 评论 #2 — Wacholek (2018-07-23T20:19:26Z)

What is so different on Linux drivers that I have to edit card bios to extended power limit? 
Under Windows I can increase power limit up to +50% so I don't think it is so hard-coded into Vega Bios.  Also frequency raport of Vega GPU is not accurate. Vega can adapt GPU freq with steps of 1MHz not by switching between GPU freq states. 
This is all done by Windows driver.  Why this cannot be done in ROCm? 

> This limits your power draw:
echo $MICROWATTS > /sys/class/drm/card0/device/hwmon/hwmon0/power1_cap

Can this extend power draw limit? 
Edit:
No, it cannot :) More info: https://bugs.freedesktop.org/show_bug.cgi?id=106374

---

### 评论 #3 — ghost (2018-08-06T03:15:45Z)

https://cgit.freedesktop.org/~agd5f/linux/log/?h=amdgpu

On Sun, Aug 5, 2018 at 5:57 PM, Hackintoshihope <notifications@github.com>
wrote:

> Voltage and power consumption does not change with these patches. At the
> wall measured with a watt meter power consumption is stuck at 300W per card
> no matter the voltage setting. Did not know is this expected behavior or if
> Vega support is still in beta?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/458#issuecomment-410551113>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0wzjfuE8kY1CglY-sRHV1Q01g1Fi8ks5uN2pOgaJpZM4VQOYn>
> .
>


---

### 评论 #4 — preda (2018-08-24T00:49:17Z)

@Wacholek , how are the GPU temperature and fan at 1770Mhz@365W ? (just curious; I find I have difficulty to cool 220W with the stock air cooler.)

---

### 评论 #5 — Wacholek (2018-08-24T05:09:20Z)

I can't reach 1770Mhz. Under linux its locked to max 265W using Vega LC bios. Than its about 1535Mhz-1600Mhz than@42*C.
Under Windows in gaming I can reach 365W@1690Mhz@46*C. Demands on the GPU usage it varies between 1660 and 1770Mhz. On xmr-stak it is steady 1770Mhz since 365W power limit is not reached. 
All my cards are under water with 9 fan radiator so no problem at all. 

---

### 评论 #6 — preda (2018-08-24T05:58:56Z)

@Wacholek thanks, that's impressively cool :) 

---

### 评论 #7 — Wacholek (2018-08-24T17:14:14Z)

Aktualny not that impresie. One of my AC has failed and I have 25*C in the room. When was 16*C my Vegas was kept at around 37*C. 

---

### 评论 #8 — jlgreathouse (2018-10-26T20:26:00Z)

Hi @Wacholek 

Thanks for your question about this. We went and looked into our Linux OD implementation and found what was causing this limit for you in Linux that you weren't seeing in Windows. This has been fixed in the `amd-staging-drm-next` branch of our drivers, though it may take a while before this makes it upstream and/or into a ROCm kernel driver released.

For now, you can see the amdgpu patch [here](https://github.com/torvalds/linux/commit/f7becf9a0803030ae125189823328e2d62b90f7b).

If you want to try this out on your system, you can modify your ROCm kernel drivers to include this patch. If you are using ROCm 1.9.1 on Ubuntu, you will find the source for these drivers located in `/usr/src/amdgpu-1.9-224/`. On CentOS/RHEL, this would be `/usr/src/amdgpu-1.9-224.el7`.

In particular, if you apply the linked patch to `/usr/src/amdgpu-1.9-224/amd/powerplay/amd_powerplay.c`, you can then rebuild the ROCm kernel drivers with the following commands:
```
sudo dkms remove amdgpu/1.9-224 --all
sudo dkms add amdgpu/1.9-224
sudo dkms build amdgpu/1.9-224
sudo dkms install amdgpu/1.9-224
sudo reboot
```

Note that the patch linked above may be have the modifications on slightly different lines than what you would need to modify in your ROCm 1.9.1 driver, since these changes were applied to the most up-to-date driver prepping for upstream.

Once you've reinstalled this updated driver, you should see a new value in `/sys/class/drm/cardN/device/hwmon/hwmon0/power1_cap_max`, assuming you have OD enabled in the `ppfeaturemask` driver parameter. You can change `power1_cap` up to this value now.

Note that such overclocking capabilities *may lead to damage to your GPU, and such damage is not covered under any AMD product warranty*. Use at your own risk.

A subsequent patch to allow these power limits to be changed from rocm-smi is in flight.

---

### 评论 #9 — v0idwalker (2018-11-20T20:27:53Z)

> 
> 
> Hi @Wacholek
> 
> Thanks for your question about this. We went and looked into our Linux OD implementation and found what was causing this limit for you in Linux that you weren't seeing in Windows. This has been fixed in the `amd-staging-drm-next` branch of our drivers, though it may take a while before this makes it upstream and/or into a ROCm kernel driver released.
> 
> For now, you can see the amdgpu patch [here](https://cgit.freedesktop.org/~agd5f/linux/commit/?h=amd-staging-drm-next&id=708bcae9acd93cce31a01e7f29a7ca53fa32457c).
> 
> If you want to try this out on your system, you can modify your ROCm kernel drivers to include this patch. If you are using ROCm 1.9.1 on Ubuntu, you will find the source for these drivers located in `/usr/src/amdgpu-1.9-224/`. On CentOS/RHEL, this would be `/usr/src/amdgpu-1.9-224.el7`.
> 
> In particular, if you apply the linked patch to `/usr/src/amdgpu-1.9-224/amd/powerplay/amd_powerplay.c`, you can then rebuild the ROCm kernel drivers with the following commands:
> 
> ```
> sudo dkms remove amdgpu/1.9-224 --all
> sudo dkms add amdgpu/1.9-224
> sudo dkms build amdgpu/1.9-224
> sudo dkms install amdgpu/1.9-224
> sudo reboot
> ```
> 
> Note that the patch linked above may be have the modifications on slightly different lines than what you would need to modify in your ROCm 1.9.1 driver, since these changes were applied to the most up-to-date driver prepping for upstream.
> 
> Once you've reinstalled this updated driver, you should see a new value in `/sys/class/drm/cardN/device/hwmon/hwmon0/power1_cap_max`, assuming you have OD enabled in the `ppfeaturemask` driver parameter. You can change `power1_cap` up to this value now.
> 
> Note that such overclocking capabilities _may lead to damage to your GPU, and such damage is not covered under any AMD product warranty_. Use at your own risk.
> 
> A subsequent patch to allow these power limits to be changed from rocm-smi is in flight.

Arch user here. 
I used the kernel patch and now I ma on 4.20rc mainline. 
I still have power1_cap = 165 and power1_cap_max = 165. Which part of your solution actually makes the card believe, that the power1_cap_max is higher? In my case I cannot seem to force it over 165W (is a powercolor reference vega56)
The only way out seem to be to flash bios of vega64, so I don't have to deal with the driver related power issues?
Or did I just miss something. 

---

### 评论 #10 — seansplayin (2018-12-24T06:37:01Z)

I've got kernel 4.20 installed, now I just need to figure out the command to increase Vega64's Power Target
any ideas? 

---

### 评论 #11 — jlgreathouse (2018-12-24T22:39:21Z)

Hi @Wacholek, 

The change I discussed in my previous post has made it both into upstream [Linux as of 4.20](https://github.com/torvalds/linux/blob/v4.20/drivers/gpu/drm/amd/powerplay/amd_powerplay.c#L966) and into [ROCK as of ROCm 2.0.](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/powerplay/amd_powerplay.c#L995). As such, you should be able to use either of these options if you still want to increase the maximum power limit on your AMD GPU.

In addition, [as of ROCm 2.0.0](https://github.com/RadeonOpenCompute/ROC-smi/blob/roc-2.0.0/rocm_smi.py#L1387), you should be able to use `rocm-smi --setpoweroverdrive N` to set the power cap of your GPU, where N is in watts.


Hi @v0idwalker,

The part of [my patch](https://github.com/torvalds/linux/commit/f7becf9a0803030ae125189823328e2d62b90f7b) that allows you to **read** `power1_cap_max` as higher than the default is on lines 1007-1013. In this case, if you have configured OverDrive to be enabled, the value returned by a read to that sysfs file will be `default power cap * (100% + VBIOS-specified maximum power limit increase percentage)`. For example, if your power cap was originally 165, and your VBIOS allows you to increase that by up to 50%, then (when OverDrive is enabled) this read would return 247 W.

The part that allows you to **write** a higher value than the default is on lines 982-988. If you have configured OverDrive to be enabled, it will not reject values that are below `default power cap * (100% + VBIOS-specified maximum power limit increase percentage)`

The important thing I've mentioned a few times here is that you must have OverDrive enabled on the `amdgpu.ppfeaturemask` module configuration variable. Otherwise, any such power boosting is turned off. See [this enum in the driver code](https://github.com/torvalds/linux/blob/v4.20/drivers/gpu/drm/amd/include/amd_shared.h#L114) to to know which bit to set in the mask to enable OverDrive.

Note also that the patch I linked sets the maximum power increase to `TDPODLimit`, which is specified by the VBIOS. As such, if your GPU card vendor (e.g. PowerColor) sets that to `0`, you will not be able to use this feature.


Hi @seansplayin,

You may want to see the above discussion for more details. However, the shortened version is:

- Make sure you have OverDrive enabled in your `ppfeaturemask`. [In this case](https://github.com/torvalds/linux/blob/v4.20/drivers/gpu/drm/amd/include/amd_shared.h#L114) (kernel 4.20), you would want to make sure that you set the following kernel parameters `amdgpu.ppfeaturemask=0xfffd7fff`. I set this particular mask because [the default value of this mask in v4.20](https://github.com/torvalds/linux/blob/v4.20/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c#L118) is `0xfffd3fff`. And the OverDrive feeature is set by ORing in `0x4000`.
- As discussed above, you could directly read `/sys/class/drm/cardN/device/hwmon/hwmon0/power1_cap_max` (where "N" is the GPU number) to see the maximum power cap of that GPU in milliwatts. You could then write into `/sys/class/drm/cardN/device/hwmon/hwmon0/power1_cap` to change your GPU's current power cap. You can write `0` into `power1_cap` to reset the the value to its default.
  - Alternately, you could use `rocm-smi --setpoweroverdrive N` to set the maximum power cap. It will not allow you to set it more than the driver-imposed limit, which you can read with `rocm-smi --showmaxpower`
  - Reading `rocm-smi`'s [Python code for setting the power cap](https://github.com/RadeonOpenCompute/ROC-smi/blob/roc-2.0.0/rocm_smi.py#L1065) may also be useful in understanding what steps you need to go through if you want to do this manually.

---
