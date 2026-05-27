# the dkms amdgpu kernel module does not have powerplay option to disable

> **Issue #580**
> **状态**: closed
> **创建时间**: 2018-10-16T16:24:07Z
> **更新时间**: 2023-12-09T23:58:31Z
> **关闭时间**: 2023-12-09T23:58:30Z
> **作者**: illwieckz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/580

## 描述

Hi, I'm a Radeon R9 390X user there (GFX7, Hawaii/Grenada XT) on Ubuntu 18.04. README said “full support is not guaranteed” but at least the OpenCL stuff seems to work and the issue I talk about is not in the "ROCm" part neither the `amdkfd` one but in the `amdgpu` kernel provided with.

So, the Radeon R9 R90X is known to not be very stable under Linux, see [FreeDesktop#91880](https://bugs.freedesktop.org/show_bug.cgi?id=91880). To get my R9 390X running stable I have to disable the `amdgpu.powerplay` option. This is my usual kernel command line:

```
radeon.cik_support=0 amdgpu.cik_support=1 amdgpu.modeset=1 amdgpu.dc=1 amdgpu.powerplay=0 amdgpu.dpm=1
```

After having installed ROCm and rebooted, I instantaneously noticed that my system was behaving the same way it behaved months before, before I disabled powerplay: wrong screen brightness on `plymouth` stage (brightness is ok once X11 starts by the way), weird `lm-sensors` related to sensors it fails to parses (probably a `lm-sensors` issue)… and worst than that, I now got random crashes like I had before disabling powerplay: suddenly the screens go black, the GPU stops to send any picture to the screen, the keyboard buttons like “Shift Lock” or “Num Lock” are not able to switch related led state anymore when pressed, and if there was a sound application (video, music player…) running the background sound continue to play for some minutes before getting silent.

Hopefully I'm able to play the magic SysRq dance to `sync`, `umount` and `reboot` to avoid a cold reboot.

So, ROCm itself seems to work on my end but the provided `amdgpu` kernel can't be configured to provide a stable environment so ROCm can't be used.

---

## 评论 (6 条)

### 评论 #1 — jlgreathouse (2018-10-24T02:45:06Z)

I'm not sure what kernel or driver version you were running before, but as far as I can tell, the `powerplay` modparm [never did anything for Hawaii](https://elixir.bootlin.com/linux/v4.5/source/drivers/gpu/drm/amd/amdgpu/amdgpu_powerplay.c#L95). It was used for Tonga and Fiji for a while, and was used for Carrizo and Stoney Ridge up through its removal from the kernel during a refactor of the powerplay code between Linux 4.10.17 and 4.11.0.

However, powerplay was (as far as I can tell) never enabled on Hawaii.

That said, most of the powerplay features are now controllable at a much finger granularity in these new drivers through the modparm `ppfeaturemask`. This is a bitmask, and the bits [are defined in the driver code](https://elixir.bootlin.com/linux/v4.19/source/drivers/gpu/drm/amd/include/amd_shared.h#L113). You may want to try something like this to "disable" most of the powerplay features your GPU may run (if any):
```
radeon.cik_support=0 amdgpu.cik_support=1 amdgpu.modeset=1 amdgpu.dc=1 amdgpu.dpm=1 amdgpu.ppfeaturemask=0
```

If that works, you could slowly start adding back in powerplay features until you run into your problems.

---

### 评论 #2 — illwieckz (2018-11-08T19:39:36Z)

Before upgrading to Ubuntu Cosmic I tried to build rocm dkms without amdgpu by removing any amdgpu reference in `dkms.conf` (i.e. building all other dkms modules but amdgpu), that fixed graphical and stability issues but made rocm opencl unworkable. Since update to Ubuntu Cosmic 18.10 with 4.18 kernel I don't experience graphical neither stability issue since I'm still using the amdgpu upstream module, but rocm opencl now works. I have not yet tried to build the amdgpu module with rocm-dkms, I have not tried yet to use rocm opencl without rocm-dkms just by relying on upstream.

At this point I will probably not spend time to investigate why non-upstream amdgpu module is faulty when upstream one is good enough. Btw, thanks for the knowledge about `ppfeaturemask`, I will probably find other uses cases to experiment with. :smiley:

I'm surprised you said `powerplay` never did anything for hawaii, I noticed disabling it leads to stability improvement and a visible change on userland : for example I noticed that not disabling powerplay has an effect on available sensors, basically I have to disable some unknown sensors parsing in lm-sensors to not get a broken `sensors` output if powerplay is not disabled.

```
chip "amdgpu-pci-*"
	ignore fan1

	# powerplay
	ignore in0
	ignore power1
```

And the weird thing is that both graphical, stability, and sensors issues were there with the dkms without option to disable powerplay, exactly like the behavior I get with an upstream amdgpu module without disabling it.

In any way, is there a way to disable amgpu compilation in the rocm-dkms package without rewriting the `dkms.conf` file by hand?

---

### 评论 #3 — mirh (2020-11-26T22:09:52Z)

GCN 1.1 switched to powerplay around back then https://github.com/torvalds/linux/commit/3120e2a390a9322a8247d7e9b8be52a7efc26dab

---

### 评论 #4 — tasso (2023-12-08T17:16:28Z)

Is this still an issue? If not; can we please close it?  Thanks!

---

### 评论 #5 — mirh (2023-12-09T15:52:19Z)

Even GFX9 is not even possibly supported anymore by now, so..

---

### 评论 #6 — illwieckz (2023-12-09T23:58:30Z)

The GFX7 support was never fixed before being removed to begin with (it only worked a couple of months years ago).

---
