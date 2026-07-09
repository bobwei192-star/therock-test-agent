# the dkms amdgpu kernel module does not have powerplay option to disable

- **Issue #:** 580
- **State:** closed
- **Created:** 2018-10-16T16:24:07Z
- **Updated:** 2023-12-09T23:58:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/580

Hi, I'm a Radeon R9 390X user there (GFX7, Hawaii/Grenada XT) on Ubuntu 18.04. README said “full support is not guaranteed” but at least the OpenCL stuff seems to work and the issue I talk about is not in the "ROCm" part neither the `amdkfd` one but in the `amdgpu` kernel provided with.

So, the Radeon R9 R90X is known to not be very stable under Linux, see [FreeDesktop#91880](https://bugs.freedesktop.org/show_bug.cgi?id=91880). To get my R9 390X running stable I have to disable the `amdgpu.powerplay` option. This is my usual kernel command line:

```
radeon.cik_support=0 amdgpu.cik_support=1 amdgpu.modeset=1 amdgpu.dc=1 amdgpu.powerplay=0 amdgpu.dpm=1
```

After having installed ROCm and rebooted, I instantaneously noticed that my system was behaving the same way it behaved months before, before I disabled powerplay: wrong screen brightness on `plymouth` stage (brightness is ok once X11 starts by the way), weird `lm-sensors` related to sensors it fails to parses (probably a `lm-sensors` issue)… and worst than that, I now got random crashes like I had before disabling powerplay: suddenly the screens go black, the GPU stops to send any picture to the screen, the keyboard buttons like “Shift Lock” or “Num Lock” are not able to switch related led state anymore when pressed, and if there was a sound application (video, music player…) running the background sound continue to play for some minutes before getting silent.

Hopefully I'm able to play the magic SysRq dance to `sync`, `umount` and `reboot` to avoid a cold reboot.

So, ROCm itself seems to work on my end but the provided `amdgpu` kernel can't be configured to provide a stable environment so ROCm can't be used.